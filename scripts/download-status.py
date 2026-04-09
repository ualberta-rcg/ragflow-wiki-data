#!/usr/bin/env python3
"""
Download Alliance status page and track changes.
"""

import requests
import json
import hashlib
from pathlib import Path
from datetime import datetime, timezone
from bs4 import BeautifulSoup

URL = "https://status.alliancecan.ca/"
OUTPUT_DIR = Path("docs/status")
CONFIG_DIR = Path("config")
STATE_FILE = CONFIG_DIR / "processing-state.json"


def md5_str(s: str) -> str:
    return hashlib.md5(s.encode("utf-8")).hexdigest()


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {"_description": "Tracks processing state for each document", "documents": {}}


def save_state(state: dict):
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2))


def fetch_status():
    """Fetch and parse status page."""
    resp = requests.get(URL)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    
    # Get text content
    text = soup.get_text(separator="\n", strip=True)
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(lines)


def main():
    print("Loading processing state...")
    state = load_state()
    docs_state = state.get("documents", {})
    timestamp = now_iso()
    
    print(f"Fetching status page from {URL}...")
    content = fetch_status()
    content_hash = md5_str(content)
    
    # Check previous state
    doc_key = "status/status_page"
    prev_state = docs_state.get(doc_key, {})
    prev_hash = prev_state.get("source_hash", "")
    
    if not prev_hash:
        change_status = "new"
    elif prev_hash != content_hash:
        change_status = "updated"
    else:
        change_status = "unchanged"
    
    print(f"Status: {change_status}")
    
    # Write file
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_file = OUTPUT_DIR / "status_page.txt"
    out_file.write_text(content, encoding="utf-8")
    
    # Update state (merge, don't replace -- preserves ragflow_source_hash etc.)
    if doc_key not in docs_state:
        docs_state[doc_key] = {}
    docs_state[doc_key].update({
        "source_url": URL,
        "source_hash": content_hash,
        "downloaded_at": timestamp,
        "path": str(out_file),
        "change_status": change_status,
    })
    
    if change_status in ("new", "updated"):
        docs_state[doc_key]["needs_ragflow_sync"] = True
        docs_state[doc_key]["needs_mkdocs_convert"] = True
    
    state["documents"] = docs_state
    state["last_status_download"] = timestamp
    save_state(state)
    
    print(f"Saved to {out_file}")
    print(f"Content hash: {content_hash[:12]}...")


if __name__ == "__main__":
    main()
