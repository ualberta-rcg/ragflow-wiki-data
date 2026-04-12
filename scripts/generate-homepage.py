#!/usr/bin/env python3
"""
Generate the MkDocs homepage (index.md) from live status and events data.

Reads:
  docs/events/events.json   – Alliance training calendar (JSON-LD)
  docs/status/status_page.txt – Alliance cluster status (scraped text)

Writes:
  mkdocs-site/docs/index.md
"""

import json
import re
from pathlib import Path
from datetime import datetime, timezone

REPO_ROOT = Path(__file__).resolve().parent.parent
EVENTS_FILE = REPO_ROOT / "docs" / "events" / "events.json"
STATUS_FILE = REPO_ROOT / "docs" / "status" / "status_page.txt"
MKDOCS_DOCS_DIR = REPO_ROOT / "mkdocs-site" / "docs"
OUTPUT_FILE = REPO_ROOT / "mkdocs-site" / "docs" / "index.md"

# HPC clusters we care about — ordered for the table.
# Services like "CCDB", "Helpdesk", "Nextcloud" are infrastructure, not clusters.
CLUSTER_SERVICES = [
    "Vulcan", "Trillium", "Narval", "Cedar Cloud", "Graham Cloud",
    "Nibi", "Fir", "Rorqual", "Arbutus", "Béluga",
    "Juno", "Killarney", "Lunaris", "tamIA",
]

STATUS_ICONS = {
    "check":          (":material-check-circle:{ style=\"color: green\" }", "Operational"),
    "warning_amber":  (":material-alert:{ style=\"color: orange\" }", ""),
    "cloud_off":      (":material-close-circle:{ style=\"color: red\" }", "Outage"),
    "power_off":      (":material-power-off:{ style=\"color: grey\" }", "Decommissioned"),
    "event":          (":material-calendar:{ style=\"color: blue\" }", "Scheduled event"),
}


def parse_status(text: str) -> list[dict]:
    """Parse the status_page.txt into (service, icon, detail) tuples.

    The status file has a predictable structure after the "Current incidents"
    header: alternating lines of service-name, icon-keyword, and optionally a
    detail string (for non-"check" statuses).
    """
    lines = [l.strip() for l in text.splitlines() if l.strip()]

    # Find the service table — starts after the line "Current incidents"
    try:
        start = lines.index("Current incidents") + 1
    except ValueError:
        return []

    # Ends at "Retired Services" or "Scheduled events"
    end = len(lines)
    for sentinel in ("Retired Services", "Scheduled events"):
        try:
            idx = lines.index(sentinel, start)
            if idx < end:
                end = idx
        except ValueError:
            pass

    services = []
    i = start
    while i < end:
        name = lines[i]
        i += 1
        if i >= end:
            break
        icon_key = lines[i]
        i += 1
        detail = ""
        # If next line exists and isn't a known service or icon keyword, it's a detail
        if i < end and lines[i] not in STATUS_ICONS and not _is_service_name(lines, i, end):
            detail = lines[i]
            i += 1
        services.append({"name": name, "icon": icon_key, "detail": detail})

    return services


def _is_service_name(lines, idx, end):
    """Heuristic: a line is a service name if the next line is an icon keyword."""
    if idx + 1 < end and lines[idx + 1] in STATUS_ICONS:
        return True
    return False


def build_status_table(services: list[dict]) -> str:
    """Build the MkDocs status table from parsed services."""
    cluster_map = {s["name"]: s for s in services}
    ordered = []
    for name in CLUSTER_SERVICES:
        if name in cluster_map:
            ordered.append(cluster_map[name])

    rows = []
    for s in ordered:
        icon_tup = STATUS_ICONS.get(s["icon"], (":material-help-circle:", s["icon"]))
        icon_md = icon_tup[0]
        # Use detail text if available, otherwise use default label
        label = s["detail"].split(" - ")[0].strip() if s["detail"] else icon_tup[1]
        if not label:
            label = s["icon"]
        rows.append(f"| **{s['name']}** | {icon_md} {label} |")

    return "\n".join(rows)


def parse_events(events_json: list) -> str:
    """Build a Markdown events table from the JSON-LD event list."""
    rows = []
    for ev in sorted(events_json, key=lambda e: e.get("startDate", "")):
        name = ev.get("name", "Untitled")
        url = ev.get("url", "")
        start_raw = ev.get("startDate", "")

        # Parse date — format is "2026-04-10 17:00:00 UTC"
        try:
            dt = datetime.strptime(start_raw, "%Y-%m-%d %H:%M:%S %Z")
            date_str = dt.strftime("%b %d")
        except (ValueError, TypeError):
            date_str = start_raw[:10] if start_raw else "TBD"

        link_text = "Details"
        if url and ("libcal" in url or "forms.gle" in url):
            link_text = "Register"
        link = f"[{link_text}]({url})" if url else ""

        rows.append(f"| {date_str} | {name} | {link} |")

    return "\n".join(rows) if rows else "| | *No upcoming events listed* | |"


def _titleize(name: str) -> str:
    """Convert directory/file slug to readable title."""
    return name.replace("_", " ").replace("-", " ").strip().title()


def generate_directory_indexes():
    """Generate index.md files for language category directories.

    This ensures folder URLs like /en/getting-started/ resolve instead of 404.
    Root language indexes (en/index.md, fr/index.md, base/index.md) are preserved.
    """
    for lang in ("en", "fr", "base"):
        lang_dir = MKDOCS_DOCS_DIR / lang
        if not lang_dir.exists():
            continue

        # Build deepest directories first, then parents.
        all_dirs = sorted(
            [p for p in lang_dir.rglob("*") if p.is_dir()],
            key=lambda p: len(p.parts),
            reverse=True,
        )

        for directory in all_dirs:
            # Keep hand-crafted language landing pages intact.
            if directory == lang_dir:
                continue

            md_files = sorted(
                [p for p in directory.glob("*.md") if p.name != "index.md"]
            )
            child_dirs = sorted([p for p in directory.iterdir() if p.is_dir()])

            rel_dir = directory.relative_to(MKDOCS_DOCS_DIR)
            title = _titleize(directory.name)

            lines = [
                "---",
                f"title: {title}",
                "---",
                "",
                f"# {title}",
                "",
                f"Auto-generated index for `{rel_dir}`.",
                "",
            ]

            if child_dirs:
                lines.extend(["## Subcategories", ""])
                for sub in child_dirs:
                    lines.append(f"- [{_titleize(sub.name)}]({sub.name}/)")
                lines.append("")

            if md_files:
                lines.extend(["## Pages", ""])
                for md in md_files:
                    lines.append(f"- [{_titleize(md.stem)}]({md.name})")
                lines.append("")

            if not child_dirs and not md_files:
                lines.extend(
                    [
                        "_No pages in this section yet._",
                        "",
                    ]
                )

            (directory / "index.md").write_text("\n".join(lines), encoding="utf-8")


def generate_homepage():
    # --- Load data ---
    events = []
    if EVENTS_FILE.exists():
        try:
            events = json.loads(EVENTS_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as e:
            print(f"Warning: could not load events: {e}")

    status_services = []
    if STATUS_FILE.exists():
        try:
            status_services = parse_status(STATUS_FILE.read_text(encoding="utf-8"))
        except OSError as e:
            print(f"Warning: could not load status: {e}")

    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    status_table = build_status_table(status_services)
    events_table = parse_events(events)

    # Ensure language/category folder URLs resolve.
    generate_directory_indexes()

    # --- Assemble page ---
    page = f"""\
---
title: Home
---

<div class="hero" markdown>

```
              __   ___   _ | | ___ __ _ _ __
              \\ \\ / / | | | |/ __/ _` | '_ \\
               \\ V /| |_| | | (_| (_| | | | |
                \\_/  \\__,_|_|\\___\\__,_|_| |_|
```

</div>

**Vulcan** is a high-performance computing cluster operated by the
**University of Alberta Research Computing Group (RCG)** and the
**Alberta Machine Intelligence Institute (AMII)**, as part of the
**Digital Research Alliance of Canada** national HPC infrastructure.

!!! warning "This is not the primary documentation"

    The official Alliance documentation is at
    [docs.alliancecan.ca](https://docs.alliancecan.ca/).
    This site mirrors and enriches that content with AI-generated metadata,
    search, and Q&A for the Vulcan cluster community.

---

## Quick Links

| Resource | Link |
|----------|------|
| **Alliance Support** | [support@tech.alliancecan.ca](mailto:support@tech.alliancecan.ca) |
| **U of A RCG Support** | [rschsppt+vulcan@ualberta.ca](mailto:rschsppt+vulcan@ualberta.ca) |
| **Alliance Docs** | [docs.alliancecan.ca](https://docs.alliancecan.ca/) |
| **Vulcan Portal** | [portal.vulcan.alliancecan.ca](https://portal.vulcan.alliancecan.ca) |
| **Vulcan Login / OOD** | [vulcan.alliancecan.ca](https://vulcan.alliancecan.ca) |
| **CCDB Account** | [ccdb.alliancecan.ca](https://ccdb.alliancecan.ca/) |

| Organization | Links |
|--------------|-------|
| **AMII** | [amii.ca](https://www.amii.ca/) &middot; [GitHub](https://github.com/Amii-Open-Source) &middot; [amiithinks](https://github.com/amiithinks) |
| **U of A RCG** | [Research Computing](https://www.ualberta.ca/en/information-services-and-technology/research-computing/index.html) &middot; [GitHub](https://github.com/ualberta-rcg) |
| **Alliance** | [alliancecan.ca](https://alliancecan.ca/) &middot; [CCDB](https://ccdb.alliancecan.ca/) |

---

## Browse Documentation

<div class="grid cards" markdown>

-   :material-translate:{{ .lg .middle }} **English**

    ---

    Alliance documentation in English

    [:octicons-arrow-right-24: Browse English docs](en/index.md)

-   :material-translate-variant:{{ .lg .middle }} **Francais**

    ---

    Documentation de l'Alliance en francais

    [:octicons-arrow-right-24: Parcourir les docs](fr/index.md)

</div>

---

## Alliance Cluster Status

!!! info "Live status from [status.alliancecan.ca](https://status.alliancecan.ca)"

| Service | Status |
|---------|--------|
{status_table}

<small>*Auto-generated from [status.alliancecan.ca](https://status.alliancecan.ca) &mdash; updated {now_str}. See that page for current incident details.*</small>

---

## Upcoming Training & Events

Events from the [Alliance training calendar](https://explora.alliancecan.ca/events):

| Date | Event | Link |
|------|-------|------|
{events_table}

<small>*Auto-generated from [explora.alliancecan.ca/events](https://explora.alliancecan.ca/events) &mdash; updated {now_str}.*</small>

---

## About This Site

This documentation is automatically generated by a pipeline that:

1. **Downloads** pages from the Alliance [MediaWiki API](https://docs.alliancecan.ca/)
2. **Syncs** content to [RAGFlow](https://ragflow.io/) for AI-powered search and keyword extraction
3. **Converts** MediaWiki markup to MkDocs Material using Google Gemini for accurate formatting
4. **Generates** prompt completions (Q&A pairs) for enhanced discoverability

---

## About University of Alberta Research Computing

The **Research Computing Group (RCG)** supports high-performance computing, data-intensive
research, and advanced infrastructure for researchers at the **University of Alberta** and
across Canada through the **Digital Research Alliance of Canada**.

The **Alberta Machine Intelligence Institute (AMII)** is one of Canada's three national
AI institutes and co-operates the Vulcan cluster for machine learning research workloads.

---

## Support

!!! quote ""

    *Many Bothans died to bring us this information.*

This project is provided as-is, but reasonable questions may be answered based on
coffee intake and/or mood. ;)

Feel free to open an [issue](https://github.com/ualberta-rcg/ragflow-wiki-data/issues)
or email **[khoja1@ualberta.ca](mailto:khoja1@ualberta.ca)** /
**[kali2@ualberta.ca](mailto:kali2@ualberta.ca)** for U of A related deployments.

---

## License

This project is released under the **MIT License** &mdash; see
[LICENSE](https://github.com/ualberta-rcg/ragflow-wiki-data/blob/main/LICENSE) for details.

<div style="text-align: center; margin-top: 2em; color: #888; font-size: 0.85em;">
University of Alberta &middot; Research Computing Group &middot; AMII &middot; Digital Research Alliance of Canada
</div>
"""

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(page, encoding="utf-8")
    print(f"Homepage written to {OUTPUT_FILE}")
    print(f"  Status entries: {len(status_services)}")
    print(f"  Events: {len(events)}")


if __name__ == "__main__":
    generate_homepage()
