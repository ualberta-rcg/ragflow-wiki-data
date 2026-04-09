#!/usr/bin/env python3
"""
Download wiki pages from Alliance MediaWiki and organize into directories.
Organizes by language (en/fr/base) and category.
Tracks processing state with content hashes.
"""

import requests
import re
import os
import sys
import json
import hashlib
from pathlib import Path
from collections import defaultdict
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from shared import categorize_doc

API_ENDPOINT = "https://docs.alliancecan.ca/mediawiki/api.php"
OUTPUT_DIR = Path("docs")
CONFIG_DIR = Path("config")
STATE_FILE = CONFIG_DIR / "processing-state.json"

# Categories to skip (maintenance/meta)
SKIP_CATEGORIES = [
    "deprecated", "broken", "syntax", "template", "noindex", 
    "outdated", "draft", "migration", "video", "pages using", "pages with"
]


def md5_str(s: str) -> str:
    """Compute MD5 hash of a string."""
    return hashlib.md5(s.encode("utf-8")).hexdigest()


def now_iso() -> str:
    """Return current UTC timestamp in ISO format."""
    return datetime.now(timezone.utc).isoformat()


def load_state() -> dict:
    """Load processing state from file."""
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {"_description": "Tracks processing state for each document", "documents": {}}


def save_state(state: dict):
    """Save processing state to file."""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2))


def get_all_pages():
    """Fetch list of all wiki pages."""
    pages = []
    params = {
        "action": "query",
        "list": "allpages",
        "format": "json",
        "aplimit": "max"
    }
    while True:
        res = requests.get(API_ENDPOINT, params=params).json()
        pages += res["query"]["allpages"]
        if "continue" in res:
            params.update(res["continue"])
        else:
            break
    return [p["title"] for p in pages]


def get_page_content(title):
    """Fetch content of a single page."""
    params = {
        "action": "query",
        "prop": "revisions",
        "rvprop": "content",
        "format": "json",
        "titles": title
    }
    res = requests.get(API_ENDPOINT, params=params).json()
    pages = res.get("query", {}).get("pages", {})
    for page_id, data in pages.items():
        if "revisions" in data:
            rev = data["revisions"][0]
            return rev.get("*") or rev.get("slots", {}).get("main", {}).get("*", "")
    return ""


def extract_categories(content):
    """Extract categories from wiki content."""
    cats = re.findall(r'\[\[Category:([^\]]+)\]\]', content, re.IGNORECASE)
    return [c.strip() for c in cats 
            if not any(skip in c.lower() for skip in SKIP_CATEGORIES)]


def detect_language(title):
    """Detect language from title suffix."""
    if title.endswith("/en"):
        return "en", title[:-3]
    elif title.endswith("/fr"):
        return "fr", title[:-3]
    else:
        return "base", title


def slugify(title):
    """Convert title to safe filename."""
    return re.sub(r'[^\w\-]', '_', title.lower()).strip('_')


def main():
    print("Loading processing state...")
    state = load_state()
    docs_state = state.get("documents", {})
    
    print("Fetching page list...")
    titles = get_all_pages()
    print(f"Found {len(titles)} pages\n")

    stats = {
        "total": 0,
        "redirects": 0,
        "new": 0,
        "updated": 0,
        "unchanged": 0,
        "by_category": defaultdict(int),
        "by_lang": defaultdict(int),
    }
    manifest = []
    timestamp = now_iso()

    for i, title in enumerate(titles):
        if i % 50 == 0:
            print(f"Processing {i}/{len(titles)}...")

        content = get_page_content(title)

        # Skip redirects
        if content.strip().upper().startswith("#REDIRECT"):
            stats["redirects"] += 1
            continue

        stats["total"] += 1
        lang, base_title = detect_language(title)
        stats["by_lang"][lang] += 1

        # Get primary category
        cats = extract_categories(content)
        primary_cat = cats[0] if cats else "uncategorized"
        stats["by_category"][primary_cat] += 1

        # Build output path
        slug = slugify(base_title)
        doc_key = f"{lang}/{slug}"
        cat_dir = categorize_doc(doc_key, cats)
        out_dir = OUTPUT_DIR / lang / cat_dir
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / f"{slug}.txt"
        
        # Compute content hash
        content_hash = md5_str(content)
        
        # Check if content changed
        doc_key = f"{lang}/{slug}"
        prev_state = docs_state.get(doc_key, {})
        prev_hash = prev_state.get("source_hash", "")
        
        if not prev_hash:
            stats["new"] += 1
            change_status = "new"
        elif prev_hash != content_hash:
            stats["updated"] += 1
            change_status = "updated"
        else:
            stats["unchanged"] += 1
            change_status = "unchanged"
        
        # Write file
        out_file.write_text(content, encoding="utf-8")
        
        # Update state
        if doc_key not in docs_state:
            docs_state[doc_key] = {}
        
        docs_state[doc_key].update({
            "wiki_title": title,
            "base_title": base_title,
            "lang": lang,
            "source_hash": content_hash,
            "downloaded_at": timestamp,
            "path": str(out_file),
            "wiki_categories": cats,
        })
        
        # Mark if content changed (needs reprocessing)
        if change_status in ("new", "updated"):
            docs_state[doc_key]["needs_tagging"] = True
            docs_state[doc_key]["needs_keywords"] = True
            docs_state[doc_key]["needs_ragflow_sync"] = True
            docs_state[doc_key]["needs_mkdocs_convert"] = True

        manifest.append({
            "title": title,
            "base_title": base_title,
            "lang": lang,
            "slug": slug,
            "doc_key": doc_key,
            "categories": cats,
            "primary_category": primary_cat,
            "path": str(out_file),
            "content_hash": content_hash,
            "change_status": change_status,
        })

    # Detect deleted pages: wiki docs in state that weren't seen this run
    seen_keys = {entry["doc_key"] for entry in manifest}
    deleted = 0
    for doc_key in list(docs_state.keys()):
        if doc_key in seen_keys:
            continue
        # Only clean up wiki docs (have wiki_title), not events/status
        if "wiki_title" not in docs_state[doc_key]:
            continue

        doc_info = docs_state[doc_key]
        # Remove source file
        old_path = Path(doc_info.get("path", ""))
        if old_path.exists():
            old_path.unlink()

        # Remove MkDocs output
        lang = doc_info.get("lang", "en")
        slug = doc_key.split("/")[-1] if "/" in doc_key else doc_key
        cats = doc_info.get("wiki_categories", [])
        subdir = categorize_doc(doc_key, cats)
        mkdocs_path = Path("mkdocs-site") / "docs" / lang / subdir / f"{slug}.md"
        if mkdocs_path.exists():
            mkdocs_path.unlink()

        del docs_state[doc_key]
        deleted += 1

    stats["deleted"] = deleted

    # Save manifest
    Path("manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    
    # Save updated state
    state["documents"] = docs_state
    state["last_download"] = timestamp
    save_state(state)

    print(f"\n=== Summary ===")
    print(f"Total content pages: {stats['total']}")
    print(f"Redirects skipped: {stats['redirects']}")
    print(f"\nChanges:")
    print(f"  New: {stats['new']}")
    print(f"  Updated: {stats['updated']}")
    print(f"  Unchanged: {stats['unchanged']}")
    print(f"  Deleted: {stats['deleted']}")
    print(f"\nBy language:")
    for lang, count in sorted(stats["by_lang"].items()):
        print(f"  {lang}: {count}")
    print(f"\nTop categories:")
    for cat, count in sorted(stats["by_category"].items(), key=lambda x: -x[1])[:10]:
        print(f"  {cat}: {count}")
    print(f"\nDone. Files saved to {OUTPUT_DIR}/")
    print(f"State saved to {STATE_FILE}")


if __name__ == "__main__":
    main()
