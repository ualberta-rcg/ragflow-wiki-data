#!/usr/bin/env python3
"""
Convert wiki docs to MkDocs Material markdown.
Reads from docs/, outputs to site/docs/
Uses tags/keywords from processing-state.json
"""

import os
import sys
import json
import re
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from shared import category_to_dir

REPO_ROOT = Path(__file__).parent.parent
DOCS_DIR = REPO_ROOT / "docs"
CONFIG_DIR = REPO_ROOT / "config"
MKDOCS_OUTPUT_DIR = REPO_ROOT / "mkdocs-site" / "docs"

STATE_FILE = CONFIG_DIR / "processing-state.json"

BATCH_SIZE = int(os.environ.get("BATCH_SIZE", "0"))  # 0 = all
DRY_RUN = os.environ.get("DRY_RUN", "false").lower() == "true"


def load_state():
    if STATE_FILE.exists():
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"documents": {}}


def save_state(state):
    if DRY_RUN:
        return
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def convert_wiki_to_markdown(content):
    """Convert MediaWiki markup to MkDocs Material markdown."""
    
    # Remove language tags
    content = re.sub(r'<languages\s*/?\s*>', '', content)
    
    # Remove category tags
    content = re.sub(r'\[\[Category:[^\]]+\]\]', '', content)
    
    # Convert external links [url text] FIRST (before wiki links)
    # Only match if it starts with http/https/ftp
    content = re.sub(r'\[(https?://\S+)\s+([^\]]+)\]', r'[\2](\1)', content)
    content = re.sub(r'\[(ftp://\S+)\s+([^\]]+)\]', r'[\2](\1)', content)
    
    # Convert wiki links [[Page|Text]] or [[Page]]
    # Format: [[Target Page|Display Text]] -> [Display Text](target-page.md)
    def convert_wiki_link(match):
        target = match.group(1).strip()
        display = match.group(2).strip() if match.lastindex >= 2 else target
        # Convert target to slug (lowercase, spaces to hyphens)
        slug = target.lower().replace(" ", "-").replace("/", "-")
        return f'[{display}]({slug}.md)'
    
    content = re.sub(r'\[\[([^\]|]+)\|([^\]]+)\]\]', convert_wiki_link, content)
    content = re.sub(r'\[\[([^\]|]+)\]\]', lambda m: f'[{m.group(1)}]({m.group(1).lower().replace(" ", "-")}.md)', content)
    
    # Convert <code>...</code> to backticks
    content = re.sub(r'<code>([^<]+)</code>', r'`\1`', content)
    
    # Convert {{Command|...}} - single command
    def convert_command(match):
        full = match.group(0)
        # Extract command (after | or prompt=)
        cmd_match = re.search(r'\|([^|{}]+?)(?:\|result=|\}\})', full, re.DOTALL)
        result_match = re.search(r'\|result=\s*(.*?)\s*\}\}', full, re.DOTALL)
        
        cmd = cmd_match.group(1).strip() if cmd_match else ""
        result = result_match.group(1).strip() if result_match else ""
        
        output = f'\n```bash\n{cmd}\n```\n'
        if result:
            output += f'\n```\n{result}\n```\n'
        return output
    
    content = re.sub(r'\{\{Command[^}]*\}\}', convert_command, content, flags=re.DOTALL)
    
    # Convert {{Commands|...}} - multiple commands
    def convert_commands(match):
        full = match.group(0)
        # Extract lines starting with |
        lines = re.findall(r'\|\s*([^\n|]+)', full)
        # Filter out prompt= lines
        cmds = [l.strip() for l in lines if not l.strip().startswith('prompt=')]
        return f'\n```bash\n' + '\n'.join(cmds) + '\n```\n'
    
    content = re.sub(r'\{\{Commands[^}]*\}\}', convert_commands, content, flags=re.DOTALL)
    
    # Convert {{File|name=...|lang=...|contents=...}}
    def convert_file(match):
        full = match.group(0)
        name_match = re.search(r'name=([^\n|]+)', full)
        lang_match = re.search(r'lang="?([^"\n|]+)"?', full)
        contents_match = re.search(r'contents=\s*(.*?)\s*\}\}', full, re.DOTALL)
        
        name = name_match.group(1).strip() if name_match else "file"
        lang = lang_match.group(1).strip().strip('"') if lang_match else "text"
        contents = contents_match.group(1).strip() if contents_match else ""
        
        return f'\n**`{name}`**\n```{lang}\n{contents}\n```\n'
    
    content = re.sub(r'\{\{File[^}]*\}\}', convert_file, content, flags=re.DOTALL)
    
    # Convert headers
    content = re.sub(r'^====\s*([^=]+)\s*====$', r'#### \1', content, flags=re.MULTILINE)
    content = re.sub(r'^===\s*([^=]+)\s*===$', r'### \1', content, flags=re.MULTILINE)
    content = re.sub(r'^==\s*([^=]+)\s*==$', r'## \1', content, flags=re.MULTILINE)
    
    # Convert bold/italic
    content = re.sub(r"'''([^']+)'''", r'**\1**', content)
    content = re.sub(r"''([^']+)''", r'*\1*', content)
    
    # Convert <br/>
    content = re.sub(r'<br\s*/?>', '\n', content)
    
    # Remove {{ draft }} and similar
    content = re.sub(r'\{\{\s*draft\s*\}\}', '', content, flags=re.IGNORECASE)
    
    # Clean up any remaining {{ }} templates we didn't handle
    content = re.sub(r'\{\{[^}]*\}\}', '', content)
    
    # Remove <translate> tags and translation markers
    content = re.sub(r'</?translate>', '', content)
    content = re.sub(r'<!--T:\d+-->', '', content)
    
    # Clean up blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    return content.strip()


def create_frontmatter(doc_key, doc_state):
    """Create YAML frontmatter based on doc-template.md structure."""
    title = doc_state.get("wiki_title", doc_state.get("base_title", "Untitled"))
    base_title = doc_state.get("base_title", title)
    lang = doc_state.get("lang", "en")
    slug = doc_key.split("/")[-1] if "/" in doc_key else doc_key
    
    tags = doc_state.get("tags", [])
    keywords = doc_state.get("keywords", [])
    summary = doc_state.get("summary", "")
    categories = doc_state.get("wiki_categories", [])
    
    # Use categories as tags if no AI tags yet
    if not tags and categories:
        tags = [c.lower().replace(" ", "-") for c in categories]
    
    lines = ["---"]
    lines.append(f'title: "{title}"')
    
    # Tags
    lines.append("tags:")
    if tags:
        for t in tags:
            lines.append(f"  - {t}")
    else:
        lines.append("  []")
    lines.append("")
    
    # AI-generated metadata
    lines.append("keywords:")
    if keywords:
        for k in keywords:
            lines.append(f"  - {k}")
    else:
        lines.append("  []")
    
    if summary:
        lines.append(f'summary: "{summary}"')
    
    lines.append("---")
    return "\n".join(lines)


def process_doc(doc_key, doc_state):
    """Convert a single doc to MkDocs markdown."""
    doc_path = REPO_ROOT / doc_state.get("path", "")
    if not doc_path.exists():
        print(f"  Skip: file not found")
        return False
    
    with open(doc_path) as f:
        content = f.read()
    
    # Convert
    markdown = convert_wiki_to_markdown(content)
    frontmatter = create_frontmatter(doc_key, doc_state)
    
    # Output path
    lang = doc_state.get("lang", "en")
    slug = doc_key.split("/")[-1] if "/" in doc_key else doc_key
    
    categories = doc_state.get("wiki_categories", [])
    primary_cat = categories[0] if categories else "uncategorized"
    subdir = category_to_dir(primary_cat)
    
    out_dir = MKDOCS_OUTPUT_DIR / lang / subdir
    out_file = out_dir / f"{slug}.md"
    
    if DRY_RUN:
        print(f"  [DRY RUN] Would write: {out_file}")
    else:
        out_dir.mkdir(parents=True, exist_ok=True)
        with open(out_file, "w") as f:
            f.write(frontmatter + "\n\n" + markdown)
        print(f"  Wrote: {out_file}")
    
    return True


def main():
    print("Converting wiki docs to MkDocs Material")
    print(f"Dry run: {DRY_RUN}")
    print()
    
    state = load_state()
    docs = state.get("documents", {})
    
    # Filter to docs needing conversion
    # Convert if: needs_mkdocs_convert=True OR source_hash changed since last conversion
    SKIP_DOC_PREFIXES = ("events/", "status/")
    to_convert = []
    for k, v in docs.items():
        if k.startswith(SKIP_DOC_PREFIXES):
            continue
        needs_convert = v.get("needs_mkdocs_convert", True)
        
        # Also check if source changed since last conversion
        last_converted_hash = v.get("mkdocs_source_hash", "")
        current_hash = v.get("source_hash", "")
        source_changed = last_converted_hash != current_hash
        
        if needs_convert or source_changed:
            to_convert.append((k, v))
    
    if BATCH_SIZE > 0:
        to_convert = to_convert[:BATCH_SIZE]
    
    print(f"Converting {len(to_convert)} documents")
    
    converted = 0
    for doc_key, doc_state in to_convert:
        print(f"\n{doc_key}")
        if process_doc(doc_key, doc_state):
            doc_state["needs_mkdocs_convert"] = False
            doc_state["mkdocs_converted_at"] = datetime.now(timezone.utc).isoformat()
            doc_state["mkdocs_source_hash"] = doc_state.get("source_hash", "")  # Track which hash we converted
            converted += 1
    
    save_state(state)
    
    print(f"\nConverted: {converted}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
