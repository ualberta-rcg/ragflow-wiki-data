#!/usr/bin/env python3
"""
Convert wiki docs to MkDocs Material markdown using Google Gemini.

Reads MediaWiki source from docs/, sends to Gemini for proper markdown conversion,
populates frontmatter from processing-state.json (keywords, tags, metadata),
and outputs to mkdocs-site/docs/.

Uses config/tags.json for canonical tag selection.
Uses config/doc-template.md as the target format reference.
"""

import os
import sys
import json
import re
import time
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from shared import categorize_doc

import google.generativeai as genai

REPO_ROOT = Path(__file__).parent.parent
DOCS_DIR = REPO_ROOT / "docs"
CONFIG_DIR = REPO_ROOT / "config"
MKDOCS_OUTPUT_DIR = REPO_ROOT / "mkdocs-site" / "docs"
STATE_FILE = CONFIG_DIR / "processing-state.json"
TAGS_FILE = CONFIG_DIR / "tags.json"

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY", "")
BATCH_SIZE = int(os.environ.get("BATCH_SIZE", "0"))
GEMINI_MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")

RETRY_ATTEMPTS = 2
RETRY_PAUSE = 3

SKIP_DOC_PREFIXES = ("events/", "status/")

LANG_INSTRUCTIONS = {
    "fr": (
        "The output markdown MUST be written entirely in Quebec French (français québécois). "
        "Use Canadian French terminology and phrasing. "
        "Translate any English UI labels or section headings to Quebec French."
    ),
    "en": "The output markdown must be in Canadian English.",
    "base": "The output markdown must be in Canadian English.",
}

SITE_CONTEXT = (
    "This documentation is hosted by the University of Alberta Research Computing Group (RCG) "
    "for the Vulcan cluster, an AMII (Alberta Machine Intelligence Institute) cluster that is part of the "
    "Digital Research Alliance of Canada (the Alliance) national HPC infrastructure. "
    "The primary documentation lives at docs.alliancecan.ca; this site mirrors and enriches that content."
)


def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return {"documents": {}}


def save_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")


def load_tags():
    if TAGS_FILE.exists():
        return json.loads(TAGS_FILE.read_text(encoding="utf-8"))
    return {}


def gemini_call(prompt, retries=RETRY_ATTEMPTS):
    for attempt in range(1, retries + 1):
        try:
            resp = model.generate_content(prompt)
            return resp.text
        except Exception as e:
            print(f"    Gemini attempt {attempt} failed: {e}")
            time.sleep(RETRY_PAUSE * attempt)
    return None


def build_tag_list(tags_config):
    """Flatten tags.json into a single list for the prompt."""
    all_tags = []
    for category, data in tags_config.items():
        if category.startswith("_"):
            continue
        if isinstance(data, dict) and "tags" in data:
            all_tags.extend(data["tags"])
    return all_tags


def convert_with_gemini(content, doc_key, doc_state, canonical_tags):
    lang = doc_state.get("lang", "en")
    title = doc_state.get("wiki_title", doc_state.get("base_title", "Untitled"))
    lang_instruction = LANG_INSTRUCTIONS.get(lang, LANG_INSTRUCTIONS["en"])
    tags_list = ", ".join(canonical_tags) if canonical_tags else "none defined"

    keywords = doc_state.get("keywords", [])
    questions = doc_state.get("questions", [])
    categories = doc_state.get("wiki_categories", [])

    keywords_hint = ", ".join(keywords) if keywords else "none yet"
    questions_hint = "\n".join(f"- {q}" for q in questions[:5]) if questions else "none yet"
    categories_hint = ", ".join(categories) if categories else "none"

    prompt = f"""You are converting a MediaWiki document to clean MkDocs Material markdown.

CONTEXT: {SITE_CONTEXT}

DOCUMENT INFO:
- Title: {title}
- Language: {lang}
- Wiki categories: {categories_hint}
- RAGFlow keywords: {keywords_hint}
- RAGFlow questions:
{questions_hint}

INSTRUCTIONS:
1. {lang_instruction}
2. Convert ALL MediaWiki markup to proper GitHub-flavored Markdown:
   - == headers == become ## headers
   - '''bold''' becomes **bold**, ''italic'' becomes *italic*
   - [[Page|Text]] becomes [Text](page.md) (lowercase, hyphens for spaces)
   - [url text] becomes [text](url)
   - <code>x</code> becomes `x`
   - {{{{Command|...}}}} becomes ```bash code blocks
   - {{{{File|name=X|contents=Y}}}} becomes labeled code blocks
   - MediaWiki tables ({{| ... |}}) become proper markdown tables
   - <translate>, <!--T:N-->, <languages/>, [[Category:...]] tags are REMOVED entirely
   - {{{{draft}}}}, {{{{stub}}}} and similar templates are REMOVED
   - Image references like [[File:...]] or [[Image:...]] are REMOVED (we don't host images)
3. Preserve ALL technical content accurately. Do NOT summarize or omit sections.
4. Use MkDocs Material features where appropriate:
   - Admonitions (!!!  note, !!! warning, !!! tip) for callouts
   - Code blocks with language hints (```bash, ```python, etc.)
   - Proper nested lists
5. Do NOT add any YAML frontmatter -- I will add that separately.
6. Do NOT wrap the output in ```markdown fences.
7. Output ONLY the converted markdown content, nothing else.

CANONICAL TAGS (for reference, I'll handle tagging): {tags_list}

SOURCE MEDIAWIKI CONTENT:
{content}"""

    result = gemini_call(prompt)
    if not result:
        return None

    result = result.strip()
    if result.startswith("```markdown"):
        result = result[len("```markdown"):].strip()
    if result.startswith("```"):
        result = result[3:].strip()
    if result.endswith("```"):
        result = result[:-3].strip()

    return result


def build_frontmatter(doc_key, doc_state, canonical_tags):
    title = doc_state.get("wiki_title", doc_state.get("base_title", "Untitled"))
    base_title = doc_state.get("base_title", title)
    lang = doc_state.get("lang", "en")
    slug = doc_key.split("/")[-1] if "/" in doc_key else doc_key
    source_hash = doc_state.get("source_hash", "")
    downloaded_at = doc_state.get("downloaded_at", "")

    keywords = doc_state.get("keywords", [])
    questions = doc_state.get("questions", [])
    categories = doc_state.get("wiki_categories", [])

    tags = [c.lower().replace(" ", "-") for c in categories] if categories else []

    lines = ["---"]
    lines.append(f'title: "{title}"')
    lines.append(f'slug: "{slug}"')
    lines.append(f'lang: "{lang}"')
    lines.append("")
    lines.append(f'source_wiki_title: "{title}"')
    lines.append(f'source_hash: "{source_hash}"')
    lines.append(f'last_synced: "{downloaded_at}"')
    lines.append(f'last_processed: "{datetime.now(timezone.utc).isoformat()}"')
    lines.append("")

    lines.append("tags:")
    if tags:
        for t in tags:
            lines.append(f"  - {t}")
    else:
        lines.append("  []")
    lines.append("")

    lines.append("keywords:")
    if keywords:
        for k in keywords:
            lines.append(f"  - \"{k}\"")
    else:
        lines.append("  []")
    lines.append("")

    if questions:
        lines.append("questions:")
        for q in questions:
            lines.append(f"  - \"{q}\"")
        lines.append("")

    lines.append("status:")
    lines.append("  downloaded: true")
    lines.append("  converted: true")
    lines.append(f"  tagged: {str(bool(tags)).lower()}")
    lines.append(f"  keywords_generated: {str(bool(keywords)).lower()}")
    ragflow_synced = bool(doc_state.get("ragflow_source_hash"))
    lines.append(f"  ragflow_synced: {str(ragflow_synced).lower()}")
    qa_generated = bool(doc_state.get("completions_source_hash"))
    lines.append(f"  qa_generated: {str(qa_generated).lower()}")

    lines.append("---")
    return "\n".join(lines)


def process_doc(doc_key, doc_state, canonical_tags):
    doc_path = REPO_ROOT / doc_state.get("path", "")
    if not doc_path.exists():
        print(f"  Skip: file not found ({doc_path})")
        return False

    content = doc_path.read_text(encoding="utf-8")

    print(f"  Converting with Gemini...")
    markdown = convert_with_gemini(content, doc_key, doc_state, canonical_tags)
    if not markdown:
        print(f"  ERROR: Gemini conversion failed")
        return False

    frontmatter = build_frontmatter(doc_key, doc_state, canonical_tags)

    lang = doc_state.get("lang", "en")
    slug = doc_key.split("/")[-1] if "/" in doc_key else doc_key
    categories = doc_state.get("wiki_categories", [])
    subdir = categorize_doc(doc_key, categories)

    out_dir = MKDOCS_OUTPUT_DIR / lang / subdir
    out_file = out_dir / f"{slug}.md"

    out_dir.mkdir(parents=True, exist_ok=True)
    out_file.write_text(frontmatter + "\n\n" + markdown, encoding="utf-8")
    print(f"  Wrote: {out_file}")

    return True


def main():
    print("=" * 60)
    print("MkDocs Conversion Pipeline (Gemini)")
    print("=" * 60)

    if not GOOGLE_API_KEY:
        print("ERROR: GOOGLE_API_KEY not set")
        return 1

    global model
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel(GEMINI_MODEL)
    print(f"Gemini model: {GEMINI_MODEL}")
    print(f"Batch size: {BATCH_SIZE}")
    print()

    tags_config = load_tags()
    canonical_tags = build_tag_list(tags_config)
    print(f"Canonical tags: {len(canonical_tags)}")

    state = load_state()
    docs = state.get("documents", {})

    to_convert = []
    skipped = 0
    for k, v in docs.items():
        if k.startswith(SKIP_DOC_PREFIXES):
            continue
        current_hash = v.get("source_hash", "")
        if not current_hash:
            continue

        last_hash = v.get("mkdocs_source_hash", "")
        hash_changed = last_hash != current_hash

        lang = v.get("lang", "en")
        slug = k.split("/")[-1] if "/" in k else k
        categories = v.get("wiki_categories", [])
        subdir = categorize_doc(k, categories)
        out_file = MKDOCS_OUTPUT_DIR / lang / subdir / f"{slug}.md"
        file_missing = not out_file.exists()

        if hash_changed or file_missing:
            to_convert.append((k, v))
        else:
            skipped += 1

    print(f"Skipped (up to date): {skipped}")

    if BATCH_SIZE > 0:
        to_convert = to_convert[:BATCH_SIZE]

    print(f"Documents to convert: {len(to_convert)}")

    converted = 0
    failed = 0
    for idx, (doc_key, doc_state) in enumerate(to_convert, 1):
        print(f"\n[{idx}/{len(to_convert)}] {doc_key}")
        try:
            if process_doc(doc_key, doc_state, canonical_tags):
                doc_state["mkdocs_converted_at"] = datetime.now(timezone.utc).isoformat()
                doc_state["mkdocs_source_hash"] = doc_state.get("source_hash", "")
                save_state(state)
                converted += 1
            else:
                failed += 1
        except Exception as e:
            print(f"  ERROR: {e}")
            failed += 1

        time.sleep(1)

    print(f"\n{'=' * 60}")
    print(f"Converted: {converted}, Failed: {failed}")
    print(f"{'=' * 60}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
