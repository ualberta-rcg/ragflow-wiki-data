#!/usr/bin/env python3
"""
Download Alliance events page and track changes.
"""

import requests
import json
import hashlib
from pathlib import Path
from datetime import datetime, timezone
from bs4 import BeautifulSoup

URL = "https://explora.alliancecan.ca/events"
OUTPUT_DIR = Path("docs/events")
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


def fetch_events():
    """Fetch and parse events from JSON-LD."""
    resp = requests.get(URL)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    
    events = []
    for script in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(script.string)
            if isinstance(data, dict) and data.get("@type") == "Event":
                events.append(data)
        except Exception:
            continue
    
    return events


def main():
    print("Loading processing state...")
    state = load_state()
    docs_state = state.get("documents", {})
    timestamp = now_iso()
    
    print(f"Fetching events from {URL}...")
    events = fetch_events()
    print(f"Found {len(events)} events")
    
    # Serialize for hashing and storage
    content = json.dumps(events, ensure_ascii=False, indent=2, sort_keys=True)
    content_hash = md5_str(content)
    
    # Check previous state
    doc_key = "events/events"
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
    out_file = OUTPUT_DIR / "events.json"
    out_file.write_text(content, encoding="utf-8")
    
    # Update state
    docs_state[doc_key] = {
        "source_url": URL,
        "source_hash": content_hash,
        "downloaded_at": timestamp,
        "path": str(out_file),
        "event_count": len(events),
        "change_status": change_status,
    }
    
    if change_status in ("new", "updated"):
        docs_state[doc_key]["needs_ragflow_sync"] = True
    
    state["documents"] = docs_state
    state["last_events_download"] = timestamp
    save_state(state)
    
    print(f"Saved to {out_file}")
    print(f"Content hash: {content_hash[:12]}...")


if __name__ == "__main__":
    main()
