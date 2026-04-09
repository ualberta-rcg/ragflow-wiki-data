#!/usr/bin/env python3
"""
Generate prompt completions (Q&A pairs) for RAGFlow-synced docs using Google Gemini.

For each synced doc, downloads the page text from RAGFlow and generates:
  - Page-level Q&A pairs covering the whole document
  - Chunk-level Q&A pairs for each RAGFlow chunk (grounded in chunk + page context)

Output (mirrors docs/ directory layout):
  completions/{lang}/{category}/{slug}/page.json        Page-level Q&A pairs
  completions/{lang}/{category}/{slug}/chunk-{n}.json   Chunk-level Q&A pairs

Tracks progress via completions_source_hash in processing-state.json.
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
from ragflow_sdk import RAGFlow

# --- Config ---

RAGFLOW_API_KEY = os.environ.get("RAGFLOW_API_KEY", "")
RAGFLOW_BASE_URL = os.environ.get("RAGFLOW_BASE_URL", "")
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY", "")
BATCH_SIZE = int(os.environ.get("BATCH_SIZE", "0"))

REPO_ROOT = Path(__file__).parent.parent
STATE_FILE = REPO_ROOT / "config" / "processing-state.json"
COMPLETIONS_DIR = REPO_ROOT / "completions"

GEMINI_MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
RETRY_ATTEMPTS = 2
RETRY_PAUSE = 3


# --- State ---

def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return {"documents": {}}


def save_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")


# --- Language instructions ---

LANG_INSTRUCTIONS = {
    "fr": "Write ALL questions and answers in Quebec French (français québécois). Use Canadian French terminology and phrasing.",
    "en": "Write all questions and answers in Canadian English.",
    "base": "Write all questions and answers in Canadian English.",
}


# --- Gemini helpers ---

def gemini_call(prompt, retries=RETRY_ATTEMPTS):
    for attempt in range(1, retries + 1):
        try:
            resp = model.generate_content(prompt)
            return resp.text
        except Exception as e:
            print(f"    Gemini attempt {attempt} failed: {e}")
            time.sleep(RETRY_PAUSE * attempt)
    return None


def parse_qa_json(raw):
    raw = raw.strip()
    if raw.startswith("```"):
        raw = re.sub(r"^```[a-zA-Z]*\n", "", raw)
        raw = re.sub(r"\n```$", "", raw)
    qa_list = json.loads(raw)
    if isinstance(qa_list, list) and all("question" in qa and "answer" in qa for qa in qa_list):
        return qa_list
    return None


def gen_qa_pairs(page_text, chunk_text, lang="en"):
    lang_instruction = LANG_INSTRUCTIONS.get(lang, LANG_INSTRUCTIONS["en"])
    prompt = f"""You are generating **question–answer pairs** from a technical document.

Requirements:
- {lang_instruction}
- Output only valid JSON.
- JSON must be a list of objects, each with keys "question" and "answer".
- "question" must be a single string (natural user question).
- "answer" must be a single string that can be answered from the chunk (with page context if needed).
- Do not include any text outside of the JSON block.
- Create as many questions and answers as you can with the given information.

Document (context):
{page_text}

Chunk (focus):
{chunk_text}"""

    for attempt in range(1, RETRY_ATTEMPTS + 1):
        raw = gemini_call(prompt, retries=1)
        if not raw:
            continue
        try:
            result = parse_qa_json(raw)
            if result:
                return result
        except json.JSONDecodeError as e:
            print(f"    Invalid JSON attempt {attempt}: {e}")
            time.sleep(RETRY_PAUSE)
    return []


def get_output_dir(doc_key, doc_state):
    """Mirror the docs/ directory layout: completions/{lang}/{category}/{slug}"""
    cats = doc_state.get("wiki_categories", [])
    subdir = categorize_doc(doc_key, cats)
    lang = doc_state.get("lang", "base")
    slug = doc_key.split("/")[-1] if "/" in doc_key else doc_key
    out_dir = COMPLETIONS_DIR / lang / subdir / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir


# --- Main ---

def get_docs_needing_completions(state, limit=None):
    """Docs synced to RAGFlow but not yet processed for completions."""
    docs = []
    for doc_key, doc_state in state.get("documents", {}).items():
        if doc_key.startswith(("events/", "status/")):
            continue
        ragflow_hash = doc_state.get("ragflow_source_hash", "")
        if not ragflow_hash:
            continue
        completions_hash = doc_state.get("completions_source_hash", "")
        if ragflow_hash != completions_hash:
            docs.append((doc_key, doc_state))
            if limit and len(docs) >= limit:
                break
    return docs


def gen_page_qa(page_text, lang="en"):
    lang_instruction = LANG_INSTRUCTIONS.get(lang, LANG_INSTRUCTIONS["en"])
    prompt = f"""You are generating **question–answer pairs** that cover the entire document below.

Requirements:
- {lang_instruction}
- Output only valid JSON.
- JSON must be a list of objects, each with keys "question" and "answer".
- "question" must be a single string (natural user question).
- "answer" must be a concise string answerable from the document.
- Cover the document broadly: purpose, key concepts, prerequisites, common tasks.
- Do not include any text outside of the JSON block.

Document:
{page_text}"""

    for attempt in range(1, RETRY_ATTEMPTS + 1):
        raw = gemini_call(prompt, retries=1)
        if not raw:
            continue
        try:
            result = parse_qa_json(raw)
            if result:
                return result
        except json.JSONDecodeError as e:
            print(f"    Invalid JSON attempt {attempt}: {e}")
            time.sleep(RETRY_PAUSE)
    return []


def process_doc(dataset, doc_key, doc_state):
    out_dir = get_output_dir(doc_key, doc_state)
    ragflow_doc_id = doc_state.get("ragflow_doc_id", "")

    if not ragflow_doc_id:
        print(f"    No ragflow_doc_id, skipping")
        return False

    docs = dataset.list_documents(id=ragflow_doc_id)
    if not docs:
        print(f"    Doc not found in RAGFlow (id={ragflow_doc_id[:12]})")
        return False

    doc = docs[0]
    page_text = doc.download().decode("utf-8", errors="ignore")
    lang = doc_state.get("lang", "en")

    # Page-level Q&A
    print(f"    Generating page-level Q&A ({lang})...")
    page_qa = gen_page_qa(page_text, lang=lang)
    (out_dir / "page.json").write_text(json.dumps({
        "doc_key": doc_key,
        "level": "page",
        "qa_pairs": page_qa,
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"    Page: {len(page_qa)} Q&A pairs")

    # Chunk-level Q&A
    chunks = []
    for cpage in range(1, 50):
        page_chunks = doc.list_chunks(page=cpage, page_size=50)
        if not page_chunks:
            break
        chunks.extend(page_chunks)

    available_chunks = [c for c in chunks if getattr(c, "available", True)]
    print(f"    {len(available_chunks)} chunks")

    chunk_qa_total = 0
    for i, chunk in enumerate(available_chunks, start=1):
        print(f"    Chunk {i}/{len(available_chunks)}: generating Q&A ({lang})...")
        qa_pairs = gen_qa_pairs(page_text, chunk.content, lang=lang)

        (out_dir / f"chunk-{i}.json").write_text(json.dumps({
            "doc_key": doc_key,
            "level": "chunk",
            "chunk_index": i,
            "qa_pairs": qa_pairs,
            "generated_at": datetime.now(timezone.utc).isoformat(),
        }, indent=2, ensure_ascii=False), encoding="utf-8")

        chunk_qa_total += len(qa_pairs)
        print(f"    Chunk {i}/{len(available_chunks)}: {len(qa_pairs)} Q&A pairs")
        time.sleep(1)

    total = len(page_qa) + chunk_qa_total
    print(f"    Total: {total} Q&A pairs ({len(page_qa)} page + {chunk_qa_total} chunk)")
    return True


def main():
    print("=" * 60)
    print("Prompt Completion Pipeline")
    print("=" * 60)

    if not GOOGLE_API_KEY:
        print("ERROR: GOOGLE_API_KEY not set")
        return 1
    if not RAGFLOW_API_KEY:
        print("ERROR: RAGFLOW_API_KEY not set")
        return 1

    global model
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel(GEMINI_MODEL)
    print(f"Gemini model: {GEMINI_MODEL}")
    print(f"Batch size: {BATCH_SIZE}")

    COMPLETIONS_DIR.mkdir(parents=True, exist_ok=True)

    state = load_state()
    docs_to_process = get_docs_needing_completions(
        state, limit=BATCH_SIZE if BATCH_SIZE > 0 else None
    )

    if not docs_to_process:
        print("\nNo documents need completions (all hashes match).")
        return 0

    print(f"\nFound {len(docs_to_process)} documents needing completions")

    print(f"\nConnecting to RAGFlow...")
    rag = RAGFlow(api_key=RAGFLOW_API_KEY, base_url=RAGFLOW_BASE_URL)
    datasets = rag.list_datasets()
    if not datasets:
        print("ERROR: No datasets found")
        return 1
    dataset = datasets[0]
    print(f"Using dataset: {dataset.name}")

    processed = 0
    failed = 0
    for idx, (doc_key, doc_state) in enumerate(docs_to_process, 1):
        print(f"\n[{idx}/{len(docs_to_process)}] {doc_key}")
        try:
            if process_doc(dataset, doc_key, doc_state):
                doc_state["completions_source_hash"] = doc_state.get("ragflow_source_hash", "")
                doc_state["completions_generated_at"] = datetime.now(timezone.utc).isoformat()
                save_state(state)
                processed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"    ERROR: {e}")
            failed += 1

        time.sleep(2)

    print(f"\n{'=' * 60}")
    print(f"Processed: {processed}, Failed: {failed}")
    print(f"{'=' * 60}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
