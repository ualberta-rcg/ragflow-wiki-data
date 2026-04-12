#!/usr/bin/env python3
"""
Post-process generated MkDocs pages and normalize internal links.

Runs AFTER convert-to-mkdocs.py and BEFORE mkdocs build/deploy.

Tracking:
- Uses processing-state.json
- Per-document key: mkdocs_linkfix_source_hash
- A page is reprocessed only when:
  * source_hash == mkdocs_source_hash (page exists and is up to date), and
  * mkdocs_linkfix_source_hash != mkdocs_source_hash
"""

from __future__ import annotations

import json
import os
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

sys_path_added = False
try:
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    from shared import categorize_doc
    sys_path_added = True
except Exception:
    # Keep script usable for ad-hoc troubleshooting even if imports fail.
    categorize_doc = None

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "mkdocs-site" / "docs"
STATE_FILE = REPO_ROOT / "config" / "processing-state.json"
SKIP_DOC_PREFIXES = ("events/", "status/")

BATCH_SIZE = int(os.environ.get("BATCH_SIZE", "0"))
FORCE_ALL = os.environ.get("LINKFIX_FORCE_ALL", "false").lower() == "true"

# Non-image markdown links: [text](target)
LINK_RE = re.compile(r"(?<!\!)\[([^\]]+)\]\(([^)]+)\)")


def normalize_stem(stem: str) -> str:
    return re.sub(r"[-_]", "", stem.lower())


def build_lang_basename_index() -> dict[str, dict[str, list[Path]]]:
    index: dict[str, dict[str, list[Path]]] = defaultdict(lambda: defaultdict(list))
    for md in DOCS_DIR.rglob("*.md"):
        rel = md.relative_to(DOCS_DIR)
        if not rel.parts:
            continue
        lang = rel.parts[0]
        index[lang][normalize_stem(md.stem)].append(md)
    return index


def load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return {"documents": {}}


def save_state(state: dict):
    STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")


def doc_key_to_mkdocs_path(doc_key: str, doc_state: dict) -> Path:
    if categorize_doc is None:
        return Path("")
    lang = doc_state.get("lang", "en")
    slug = doc_key.split("/")[-1] if "/" in doc_key else doc_key
    categories = doc_state.get("wiki_categories", [])
    subdir = categorize_doc(doc_key, categories)
    return DOCS_DIR / lang / subdir / f"{slug}.md"


def is_external(target: str) -> bool:
    t = target.strip().lower()
    return (
        t.startswith("http://")
        or t.startswith("https://")
        or t.startswith("mailto:")
        or t.startswith("tel:")
        or t.startswith("#")
    )


def with_anchor(path_part: str, anchor: str) -> str:
    return f"{path_part}#{anchor}" if anchor else path_part


def resolve_target(
    src_file: Path, target: str, basename_index: dict[str, dict[str, list[Path]]]
) -> str | None:
    # Preserve anchor fragment.
    if "#" in target:
        path_part, anchor = target.split("#", 1)
    else:
        path_part, anchor = target, ""

    # Skip non-md/internal-anchor-only paths.
    if not path_part or not path_part.endswith(".md"):
        return None

    src_rel = src_file.relative_to(DOCS_DIR)
    lang = src_rel.parts[0] if src_rel.parts else "base"
    src_parent = src_file.parent

    # 0) If already valid, keep as-is.
    direct = (src_parent / path_part).resolve()
    if direct.exists():
        return target

    # 1) Same relative path, hyphen/underscore filename style variants.
    candidates = [
        path_part.replace("-", "_"),
        path_part.replace("_", "-"),
    ]
    for cand in candidates:
        cand_abs = (src_parent / cand).resolve()
        if cand_abs.exists():
            return with_anchor(cand, anchor)

    # 2) Unique basename match inside this language tree.
    stem = Path(path_part).stem
    norm = normalize_stem(stem)
    lang_candidates = basename_index.get(lang, {}).get(norm, [])
    if not lang_candidates:
        return None

    chosen: Path | None = None
    if len(lang_candidates) == 1:
        chosen = lang_candidates[0]
    else:
        # Prefer same top-level category when possible.
        src_cat = src_rel.parts[1] if len(src_rel.parts) > 1 else ""
        same_cat = [
            p for p in lang_candidates if len(p.relative_to(DOCS_DIR).parts) > 1
            and p.relative_to(DOCS_DIR).parts[1] == src_cat
        ]
        if len(same_cat) == 1:
            chosen = same_cat[0]

    if not chosen:
        return None

    rel_path = os.path.relpath(chosen, src_parent).replace("\\", "/")
    return with_anchor(rel_path, anchor)


def main() -> int:
    if not DOCS_DIR.exists():
        print(f"Docs directory not found: {DOCS_DIR}")
        return 1

    state = load_state()
    docs = state.get("documents", {})
    if not docs:
        print("No documents in processing-state.json")
        return 0

    basename_index = build_lang_basename_index()
    changed_files = 0
    links_fixed = 0
    unresolved = 0
    processed_docs = 0
    skipped_docs = 0

    to_process: list[tuple[str, dict, Path]] = []
    for doc_key, doc_state in docs.items():
        if doc_key.startswith(SKIP_DOC_PREFIXES):
            continue
        source_hash = doc_state.get("source_hash", "")
        mkdocs_hash = doc_state.get("mkdocs_source_hash", "")
        if not source_hash or not mkdocs_hash or source_hash != mkdocs_hash:
            continue

        out_file = doc_key_to_mkdocs_path(doc_key, doc_state)
        if not out_file.exists():
            continue

        fixed_hash = doc_state.get("mkdocs_linkfix_source_hash", "")
        if not FORCE_ALL and fixed_hash == mkdocs_hash:
            skipped_docs += 1
            continue
        to_process.append((doc_key, doc_state, out_file))

    if BATCH_SIZE > 0:
        to_process = to_process[:BATCH_SIZE]

    print(f"Docs eligible for link-fix: {len(to_process)} (skipped up-to-date: {skipped_docs})")
    print(f"Force all mode: {FORCE_ALL}")

    for idx, (doc_key, doc_state, md) in enumerate(to_process, 1):
        print(f"[{idx}/{len(to_process)}] {doc_key}")
        text = md.read_text(encoding="utf-8")
        replaced = False

        def repl(match: re.Match[str]) -> str:
            nonlocal links_fixed, unresolved, replaced
            label, target = match.group(1), match.group(2)
            if is_external(target):
                return match.group(0)

            resolved = resolve_target(md, target, basename_index)
            if not resolved or resolved == target:
                if resolved is None:
                    unresolved += 1
                return match.group(0)

            links_fixed += 1
            replaced = True
            return f"[{label}]({resolved})"

        new_text = LINK_RE.sub(repl, text)
        if replaced and new_text != text:
            md.write_text(new_text, encoding="utf-8")
            changed_files += 1

        doc_state["mkdocs_linkfix_source_hash"] = doc_state.get("mkdocs_source_hash", "")
        doc_state["mkdocs_linkfix_at"] = datetime.now(timezone.utc).isoformat()
        processed_docs += 1

    save_state(state)

    print(f"Link normalization complete")
    print(f"  Docs processed: {processed_docs}")
    print(f"  Files changed: {changed_files}")
    print(f"  Links fixed: {links_fixed}")
    print(f"  Unresolved links (left unchanged): {unresolved}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
