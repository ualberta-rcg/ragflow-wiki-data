#!/usr/bin/env python3
"""
Sync docs to RAGFlow and fetch keywords back.

Hash-driven: only processes docs where source_hash != ragflow_source_hash.
When a doc changes:
  1. Delete old version from RAGFlow (if exists)
  2. Upload new version
  3. Wait for parsing
  4. Fetch keywords back
  5. Save ragflow_source_hash so we know it's current
"""

import os
import sys
import json
import time
import argparse
from pathlib import Path
from datetime import datetime, timezone

try:
    from ragflow_sdk import RAGFlow
except ImportError:
    print("ERROR: ragflow_sdk not installed")
    print("Run: pip install ragflow-sdk")
    sys.exit(1)

# Config
REPO_ROOT = Path(__file__).parent.parent
CONFIG_DIR = REPO_ROOT / "config"
STATE_FILE = CONFIG_DIR / "processing-state.json"

RAGFLOW_API_KEY = os.environ.get("RAGFLOW_API_KEY", "")
RAGFLOW_BASE_URL = os.environ.get("RAGFLOW_BASE_URL", "")

BATCH_SIZE = int(os.environ.get("BATCH_SIZE", "5"))
DRY_RUN = os.environ.get("DRY_RUN", "false").lower() == "true"
PARSE_TIMEOUT = int(os.environ.get("PARSE_TIMEOUT", "300"))


def load_state():
    if STATE_FILE.exists():
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"documents": {}}


def save_state(state):
    if DRY_RUN:
        print("[DRY RUN] Would save state")
        return
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def doc_key_to_filename(doc_key):
    """Convert doc_key to a unique RAGFlow filename."""
    return f"{doc_key.replace('/', '--')}.txt"


def doc_exists_in_ragflow(dataset, doc_key, doc_state):
    """Check if a doc actually exists in RAGFlow (by ID or name)."""
    doc_id = doc_state.get("ragflow_doc_id")
    if doc_id:
        try:
            results = dataset.list_documents(id=doc_id)
            if results:
                return True
        except Exception:
            pass

    filename = doc_key_to_filename(doc_key)
    try:
        results = dataset.list_documents(name=filename)
        if results:
            return True
    except Exception:
        pass

    return False


SKIP_DOC_PREFIXES = ("events/", "status/")


def get_docs_needing_sync(state, limit=None):
    """Get docs where source_hash != ragflow_source_hash (hash-driven)."""
    docs = []
    for doc_key, doc_state in state.get("documents", {}).items():
        if doc_key.startswith(SKIP_DOC_PREFIXES):
            continue
        current_hash = doc_state.get("source_hash", "")
        synced_hash = doc_state.get("ragflow_source_hash", "")

        if current_hash != synced_hash:
            docs.append((doc_key, doc_state))
        if limit and len(docs) >= limit:
            break
    return docs


def verify_synced_docs(state, dataset, limit=None):
    """Find docs that claim to be synced but are missing from RAGFlow."""
    missing = []
    for doc_key, doc_state in state.get("documents", {}).items():
        if doc_key.startswith(SKIP_DOC_PREFIXES):
            continue
        if not doc_state.get("ragflow_source_hash"):
            continue
        if not doc_exists_in_ragflow(dataset, doc_key, doc_state):
            print(f"  Missing from RAGFlow: {doc_key}")
            missing.append((doc_key, doc_state))
            if limit and len(missing) >= limit:
                break
    return missing


def delete_from_ragflow(dataset, doc_key, doc_state):
    """Delete old version(s) of a doc from RAGFlow, including (1)/(2) duplicates."""
    filename = doc_key_to_filename(doc_key)
    old_doc_id = doc_state.get("ragflow_doc_id")
    deleted = 0

    # Delete by stored doc ID
    if old_doc_id:
        try:
            dataset.delete_documents([old_doc_id])
            deleted += 1
        except Exception:
            pass

    # Delete any exact name match
    try:
        existing = dataset.list_documents(name=filename)
        for doc in existing:
            if doc.id != old_doc_id:
                dataset.delete_documents([doc.id])
                deleted += 1
    except Exception:
        pass

    # Delete (1), (2), ... duplicates that RAGFlow auto-creates on name collision
    base = filename.rsplit(".", 1)[0]
    ext = filename.rsplit(".", 1)[1] if "." in filename else ""
    for suffix_num in range(1, 10):
        dup_name = f"{base}({suffix_num}).{ext}" if ext else f"{base}({suffix_num})"
        try:
            dups = dataset.list_documents(name=dup_name)
            for d in dups:
                dataset.delete_documents([d.id])
                deleted += 1
        except Exception:
            break

    if deleted:
        print(f"    Deleted {deleted} old version(s)")


def upload_doc(dataset, doc_path, doc_key):
    """Upload a document to RAGFlow."""
    filename = doc_key_to_filename(doc_key)

    with open(doc_path, "rb") as f:
        content = f.read()

    print(f"    Uploading {filename} ({len(content)} bytes)...")
    dataset.upload_documents([{"display_name": filename, "blob": content}])

    docs = dataset.list_documents(name=filename)
    return docs[0] if docs else None


def wait_for_parse(dataset, doc, timeout=300):
    """Wait for document parsing to complete."""
    start = time.time()
    while time.time() - start < timeout:
        doc = dataset.list_documents(name=doc.name)[0]

        if doc.run == "DONE":
            return True, doc
        if doc.run == "FAIL":
            return False, doc

        print(f"    Parsing: {doc.run} {doc.progress:.0%}")
        time.sleep(5)

    print(f"    Timeout after {timeout}s")
    return False, doc


def fetch_keywords(doc):
    """Fetch keywords and questions from document chunks."""
    keywords = set()
    questions = []

    try:
        chunks = doc.list_chunks(page=1, page_size=50)
        for chunk in chunks:
            for kw in (getattr(chunk, 'important_keywords', []) or []):
                if kw and kw.strip():
                    keywords.add(kw.strip())
            for q in (getattr(chunk, 'questions', []) or []):
                if q and q.strip():
                    questions.append(q.strip())
    except Exception as e:
        print(f"    Warning: Could not fetch chunks: {e}")

    return list(keywords), questions


def process_doc(dataset, doc_key, doc_state):
    """Process a single document: delete old, upload new, parse, fetch keywords."""
    doc_path = REPO_ROOT / doc_state.get("path", "")

    if not doc_path.exists():
        print(f"    ERROR: File not found: {doc_path}")
        return False

    if DRY_RUN:
        print(f"    [DRY RUN] Would sync {doc_path.name}")
        return True

    # Delete old version if it exists
    if doc_state.get("ragflow_doc_id") or doc_state.get("ragflow_source_hash"):
        delete_from_ragflow(dataset, doc_key, doc_state)

    # Upload new version
    doc = upload_doc(dataset, doc_path, doc_key)
    if not doc:
        print(f"    ERROR: Upload failed")
        return False

    # Parse
    print(f"    Starting parse...")
    dataset.async_parse_documents([doc.id])

    success, doc = wait_for_parse(dataset, doc, timeout=PARSE_TIMEOUT)
    if not success:
        print(f"    ERROR: Parse failed")
        return False

    # Fetch keywords
    print(f"    Fetching keywords...")
    keywords, questions = fetch_keywords(doc)
    print(f"    Got {len(keywords)} keywords, {len(questions)} questions")

    # Update state - hash is the key tracking field
    doc_state["keywords"] = keywords
    doc_state["questions"] = questions[:10]
    doc_state["needs_ragflow_sync"] = False
    doc_state["ragflow_source_hash"] = doc_state.get("source_hash", "")
    doc_state["ragflow_synced_at"] = datetime.now(timezone.utc).isoformat()
    doc_state["ragflow_doc_id"] = doc.id
    doc_state["chunk_count"] = doc.chunk_count

    return True


def main():
    parser = argparse.ArgumentParser(description="Sync docs to RAGFlow")
    parser.add_argument("--force", action="store_true",
                        help="Clear all ragflow_source_hash values, forcing full re-sync")
    parser.add_argument("--verify", action="store_true",
                        help="Check RAGFlow for missing docs before syncing")
    args = parser.parse_args()

    print("=" * 60)
    print("RAGFlow Sync Pipeline")
    print("=" * 60)
    print(f"RAGFlow URL: {RAGFLOW_BASE_URL}")
    print(f"Batch size: {BATCH_SIZE}")
    print(f"Dry run: {DRY_RUN}")
    if args.force:
        print("Mode: FORCE (re-sync everything)")
    if args.verify:
        print("Mode: VERIFY (check RAGFlow for missing docs)")
    print()

    state = load_state()

    # --force: clear all ragflow hashes so every doc looks like it needs sync
    if args.force:
        cleared = 0
        for doc_state in state.get("documents", {}).values():
            if doc_state.get("ragflow_source_hash"):
                doc_state["ragflow_source_hash"] = ""
                cleared += 1
        print(f"Force mode: cleared ragflow_source_hash on {cleared} docs")
        save_state(state)

    # Connect to RAGFlow
    print(f"\nConnecting to RAGFlow...")
    try:
        rag = RAGFlow(api_key=RAGFLOW_API_KEY, base_url=RAGFLOW_BASE_URL)
        datasets = rag.list_datasets()
        if not datasets:
            print("ERROR: No datasets found in RAGFlow")
            return 1
        dataset = datasets[0]
        print(f"Using dataset: {dataset.name}")
    except Exception as e:
        print(f"ERROR: Could not connect to RAGFlow: {e}")
        return 1

    # --verify: find docs that claim synced but are missing from RAGFlow
    if args.verify:
        print(f"\nVerifying synced docs exist in RAGFlow...")
        missing = verify_synced_docs(state, dataset)
        if missing:
            print(f"\n{len(missing)} docs missing from RAGFlow, clearing their hashes")
            for doc_key, doc_state in missing:
                doc_state["ragflow_source_hash"] = ""
                doc_state["ragflow_doc_id"] = ""
            save_state(state)
        else:
            print("All synced docs verified in RAGFlow")

    docs_to_sync = get_docs_needing_sync(state, limit=BATCH_SIZE if BATCH_SIZE > 0 else None)

    if not docs_to_sync:
        print("\nNo documents need syncing (all hashes match).")
        return 0

    print(f"\nFound {len(docs_to_sync)} documents needing sync")

    processed = 0
    failed = 0

    for doc_key, doc_state in docs_to_sync:
        print(f"\n[{processed + failed + 1}/{len(docs_to_sync)}] {doc_key}")

        try:
            if process_doc(dataset, doc_key, doc_state):
                processed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"    ERROR: {e}")
            failed += 1

        save_state(state)

    print()
    print("=" * 60)
    print(f"Processed: {processed}, Failed: {failed}")
    print("=" * 60)

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
