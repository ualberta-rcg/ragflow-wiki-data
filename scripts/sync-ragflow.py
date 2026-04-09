#!/usr/bin/env python3
"""
Sync docs to RAGFlow and fetch keywords back.

1. Upload docs where needs_ragflow_sync=True
2. Wait for parsing to complete
3. Fetch keywords from chunks
4. Save keywords to processing-state.json
"""

import os
import sys
import json
import time
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

RAGFLOW_API_KEY = os.environ.get("RAGFLOW_API_KEY", "ragflow-obaOcime25CrFMSZCwGtuiR-i17pxaqD8GI2-sla7EM")
RAGFLOW_BASE_URL = os.environ.get("RAGFLOW_BASE_URL", "https://ragflow.vulcan.alliancecan.ca")

BATCH_SIZE = int(os.environ.get("BATCH_SIZE", "5"))
DRY_RUN = os.environ.get("DRY_RUN", "false").lower() == "true"
PARSE_TIMEOUT = int(os.environ.get("PARSE_TIMEOUT", "300"))  # 5 min per doc


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


def get_docs_needing_sync(state, limit=None):
    """Get docs that need RAGFlow sync."""
    docs = []
    for doc_key, doc_state in state.get("documents", {}).items():
        if doc_state.get("needs_ragflow_sync", True):
            docs.append((doc_key, doc_state))
        if limit and len(docs) >= limit:
            break
    return docs


def upload_doc(dataset, doc_path, doc_key):
    """Upload a document to RAGFlow."""
    # Use doc_key as filename to ensure uniqueness across langs
    # e.g. en/abinit -> en--abinit.txt
    filename = f"{doc_key.replace('/', '--')}.txt"
    
    # Check if already exists
    try:
        existing = dataset.list_documents(name=filename)
        if existing:
            print(f"    Already in RAGFlow: {filename}")
            return existing[0], False
    except Exception as e:
        if "don't own" in str(e).lower():
            # Stale doc from another session, use a different name
            filename = f"{doc_key.replace('/', '--')}_{int(time.time())}.txt"
            print(f"    Name conflict, using: {filename}")
        else:
            raise
    
    # Read and upload
    with open(doc_path, "rb") as f:
        content = f.read()
    
    print(f"    Uploading {filename} ({len(content)} bytes)...")
    dataset.upload_documents([{"display_name": filename, "blob": content}])
    
    # Get the uploaded doc
    docs = dataset.list_documents(name=filename)
    return docs[0] if docs else None, True


def wait_for_parse(dataset, doc, timeout=300):
    """Wait for document parsing to complete."""
    start = time.time()
    while time.time() - start < timeout:
        doc = dataset.list_documents(name=doc.name)[0]
        status = doc.run
        progress = doc.progress
        
        if status == "DONE":
            return True, doc
        if status == "FAIL":
            return False, doc
        
        print(f"    Parsing: {status} {progress:.0%}")
        time.sleep(5)
    
    print(f"    Timeout after {timeout}s")
    return False, doc


def fetch_keywords(doc):
    """Fetch keywords from document chunks."""
    keywords = set()
    questions = []
    
    try:
        chunks = doc.list_chunks(page=1, page_size=100)
        for chunk in chunks:
            # Get keywords
            kws = getattr(chunk, 'important_keywords', []) or []
            for kw in kws:
                if kw and kw.strip():
                    keywords.add(kw.strip())
            
            # Get questions
            qs = getattr(chunk, 'questions', []) or []
            for q in qs:
                if q and q.strip():
                    questions.append(q.strip())
    except Exception as e:
        print(f"    Warning: Could not fetch chunks: {e}")
    
    return list(keywords), questions


def process_doc(dataset, doc_key, doc_state):
    """Process a single document through RAGFlow."""
    doc_path = REPO_ROOT / doc_state.get("path", "")
    
    if not doc_path.exists():
        print(f"    ERROR: File not found: {doc_path}")
        return False
    
    if DRY_RUN:
        print(f"    [DRY RUN] Would upload and parse")
        return True
    
    # Upload
    doc, is_new = upload_doc(dataset, doc_path, doc_key)
    if not doc:
        print(f"    ERROR: Upload failed")
        return False
    
    # Parse if new
    if is_new:
        print(f"    Starting parse...")
        dataset.async_parse_documents([doc.id])
        
        success, doc = wait_for_parse(dataset, doc, timeout=PARSE_TIMEOUT)
        if not success:
            print(f"    ERROR: Parse failed")
            return False
    else:
        # Check if already parsed
        if doc.run != "DONE":
            print(f"    Starting parse (existing doc)...")
            dataset.async_parse_documents([doc.id])
            success, doc = wait_for_parse(dataset, doc, timeout=PARSE_TIMEOUT)
            if not success:
                print(f"    ERROR: Parse failed")
                return False
    
    # Fetch keywords
    print(f"    Fetching keywords...")
    keywords, questions = fetch_keywords(doc)
    print(f"    Got {len(keywords)} keywords, {len(questions)} questions")
    
    # Update state
    doc_state["keywords"] = keywords
    doc_state["questions"] = questions[:10]  # Keep first 10 questions
    doc_state["needs_ragflow_sync"] = False
    doc_state["ragflow_synced_at"] = datetime.now(timezone.utc).isoformat()
    doc_state["ragflow_doc_id"] = doc.id
    doc_state["chunk_count"] = doc.chunk_count
    
    return True


def main():
    print("=" * 60)
    print("RAGFlow Sync Pipeline")
    print("=" * 60)
    print(f"RAGFlow URL: {RAGFLOW_BASE_URL}")
    print(f"Batch size: {BATCH_SIZE}")
    print(f"Dry run: {DRY_RUN}")
    print()
    
    # Load state
    state = load_state()
    docs_to_sync = get_docs_needing_sync(state, limit=BATCH_SIZE if BATCH_SIZE > 0 else None)
    
    if not docs_to_sync:
        print("No documents need syncing.")
        return 0
    
    print(f"Found {len(docs_to_sync)} documents to sync")
    
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
    
    # Process docs
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
        
        # Save state after each doc
        save_state(state)
    
    print()
    print("=" * 60)
    print(f"Processed: {processed}, Failed: {failed}")
    print("=" * 60)
    
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
