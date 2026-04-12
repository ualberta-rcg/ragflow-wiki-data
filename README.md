# University of Alberta - RAGFlow Wiki Data

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![MkDocs Site](https://img.shields.io/badge/Docs-Live-blue?style=flat-square)](https://ualberta-rcg.github.io/ragflow-wiki-data/)
[![Full Pipeline](https://img.shields.io/badge/Pipeline-Weekly-purple?style=flat-square)](https://github.com/ualberta-rcg/ragflow-wiki-data/actions/workflows/full-pipeline.yml)

**Maintained by:** Rahim Khoja ([khoja1@ualberta.ca](mailto:khoja1@ualberta.ca))

---

## Description

Automated pipeline that mirrors the [Digital Research Alliance of Canada](https://docs.alliancecan.ca/) MediaWiki documentation into a **RAGFlow** knowledge base, converts it to a searchable **MkDocs Material** site with AI-generated metadata, and produces **fine-tuning training data** — all driven by content hashing so only changed documents are reprocessed.

**Key Features:**
- **1,700+ source documents** downloaded from Alliance MediaWiki API (English, French, bilingual)
- **RAGFlow integration** — documents synced, parsed, and indexed with keyword and Q&A extraction
- **AI-powered conversion** — Google Gemini converts MediaWiki markup to clean MkDocs Material Markdown
- **Intelligent link repair** — post-processing fixes internal links, removes dead references, strips bad anchors
- **Prompt completions** — page-level (10-20) and chunk-level (2-3) Q&A pairs generated per document
- **Training data export** — 80,000+ Q&A pairs consolidated into OpenAI fine-tuning JSONL format
- **Hash-driven idempotency** — five-layer change tracking ensures no wasted API calls or token spend
- **Multilingual** — English (Canadian) and French (Quebec French) with language-specific AI instructions
- **Automated pipeline** — weekly GitHub Actions schedule with manual dispatch and per-stage batch controls
- **Live site** — auto-deployed to GitHub Pages with SEO-friendly sitemap and robots.txt

---

## Architecture

### Pipeline Stages

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  1. Download  │───▶│  2. RAGFlow   │───▶│  3. Convert   │
│  Wiki/Events/ │    │  Sync + Parse │    │  to MkDocs    │
│  Status       │    │  + Keywords   │    │  (Gemini AI)  │
└──────────────┘    └──────────────┘    └──────────────┘
                                               │
       ┌───────────────────────────────────────┘
       ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  4. Fix Links │───▶│  5. Homepage  │───▶│  6. Build     │
│  + Cleanup    │    │  + Indexes    │    │  MkDocs Site  │
└──────────────┘    └──────────────┘    └──────────────┘
                                               │
       ┌───────────────────────────────────────┘
       ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  7. Generate  │───▶│  8. Export    │───▶│  9. Deploy    │
│  Completions  │    │  Training     │    │  to GitHub    │
│  (Gemini AI)  │    │  Data (JSONL) │    │  Pages        │
└──────────────┘    └──────────────┘    └──────────────┘
```

### Hash-Driven Change Tracking

Each document carries five independent hashes in `config/processing-state.json`:

| Hash | Set by | Triggers reprocessing of |
|------|--------|--------------------------|
| `source_hash` | `download-wiki.py` | Everything downstream |
| `ragflow_source_hash` | `sync-ragflow.py` | RAGFlow re-upload + re-parse |
| `mkdocs_source_hash` | `convert-to-mkdocs.py` | Gemini re-conversion |
| `mkdocs_linkfix_source_hash` | `fix-mkdocs-links.py` | Link normalization pass |
| `completions_source_hash` | `generate-completions.py` | Q&A pair regeneration |

When a source document changes, its `source_hash` updates. Each downstream stage compares its own hash to `source_hash` and only reprocesses on mismatch — no wasted API calls.

### Services

| Service | Purpose | API/SDK |
|---------|---------|---------|
| **Alliance MediaWiki** | Source documentation (1,700+ pages) | MediaWiki API |
| **RAGFlow** | Document parsing, chunking, keyword/Q&A extraction | `ragflow-sdk` |
| **Google Gemini** | MediaWiki → Markdown conversion, Q&A generation | `google-genai` |
| **MkDocs Material** | Static documentation site | `mkdocs-material` |
| **GitHub Pages** | Hosting (gh-pages branch) | GitHub Actions |

---

## Repository Structure

```
ragflow-wiki-data/
├── docs/                    # Source documents (.txt from MediaWiki API)
│   ├── en/                  #   English pages by category
│   ├── fr/                  #   French pages by category
│   ├── base/                #   Bilingual / uncategorized pages
│   ├── events/              #   Alliance training calendar (JSON)
│   └── status/              #   Alliance cluster status (text)
├── completions/             # AI-generated Q&A pairs
│   ├── en/{category}/{slug}/#   page.json + chunk-N.json per document
│   └── fr/{category}/{slug}/
├── mkdocs-site/             # MkDocs Material site
│   ├── docs/                #   Generated Markdown pages + index files
│   ├── mkdocs.yml           #   Site configuration
│   └── site/                #   Built static site (not committed)
├── config/
│   ├── processing-state.json#   Central state tracking (hashes, metadata)
│   ├── tags.json            #   Canonical tag vocabulary for AI
│   └── doc-template.md      #   Reference frontmatter schema
├── scripts/
│   ├── shared.py            #   Shared constants, category mapping, skip logic
│   ├── download-wiki.py     #   MediaWiki API downloader
│   ├── download-events.py   #   Alliance events scraper
│   ├── download-status.py   #   Alliance status scraper
│   ├── sync-ragflow.py      #   RAGFlow document sync + keyword extraction
│   ├── convert-to-mkdocs.py #   Gemini-powered MediaWiki → Markdown
│   ├── fix-mkdocs-links.py  #   Internal link normalization + cleanup
│   ├── generate-homepage.py #   Dynamic homepage + category indexes
│   ├── generate-completions.py # Gemini Q&A pair generation
│   └── export-training-data.py # Consolidate completions → JSONL
├── .github/workflows/       # GitHub Actions (9 workflows)
│   ├── full-pipeline.yml    #   Complete pipeline (scheduled + manual)
│   ├── deploy-docs.yml      #   Manual docs deploy
│   ├── export-training.yml  #   Manual training export
│   └── ...                  #   Individual stage workflows
├── training-data.jsonl      # Consolidated training data (80K+ Q&A pairs)
├── run-full-pipeline.sh     # Local pipeline runner (9 steps + logging)
├── watch-pipeline.sh        # Background pipeline monitor
├── requirements.txt         # Pinned Python dependencies
└── LICENSE                  # MIT License
```

---

## Quick Start

### Prerequisites

- Python 3.12+
- RAGFlow instance with API access
- Google Gemini API key

### Setup

```bash
git clone git@github.com:ualberta-rcg/ragflow-wiki-data.git
cd ragflow-wiki-data
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Environment Variables

Set these (or configure as GitHub Actions secrets):

```bash
export RAGFLOW_API_KEY="your-ragflow-api-key"
export RAGFLOW_BASE_URL="https://your-ragflow-host"
export GOOGLE_API_KEY="your-google-api-key"
```

### Run Locally

Full pipeline (all stages, all documents):

```bash
./run-full-pipeline.sh
```

Or run individual stages:

```bash
source venv/bin/activate
export PYTHONUNBUFFERED=1

python scripts/download-wiki.py          # 1. Download source docs
python scripts/download-events.py        # 2. Download events
python scripts/download-status.py        # 3. Download status
python scripts/sync-ragflow.py           # 4. Sync to RAGFlow
python scripts/convert-to-mkdocs.py      # 5. AI conversion
python scripts/fix-mkdocs-links.py       # 6. Link repair
python scripts/generate-homepage.py      # 7. Homepage + indexes
python scripts/generate-completions.py   # 8. Q&A generation
python scripts/export-training-data.py   # 9. Training export
```

Control batch sizes via environment:

```bash
BATCH_SIZE=10 python scripts/sync-ragflow.py --allow-failures
BATCH_SIZE=5 python scripts/convert-to-mkdocs.py
```

---

## GitHub Actions

### Full Pipeline (`full-pipeline.yml`)

**Schedule:** Saturday 11pm UTC (5pm MDT / 4pm MST)

Runs all 9 stages, commits results, and deploys to GitHub Pages. Manual dispatch with controls:

| Input | Default | Description |
|-------|---------|-------------|
| `sync_batch_size` | `0` (all) | Documents to sync to RAGFlow |
| `convert_batch_size` | `0` (all) | Documents to convert with Gemini |
| `linkfix_batch_size` | `0` (all) | Documents to run link-fix on |
| `completions_batch_size` | `0` (all) | Documents to generate Q&A for |
| `sync_verify` | `false` | Verify docs exist in RAGFlow first |
| `sync_force` | `false` | Force full re-sync (clear all hashes) |

### Other Workflows

| Workflow | Trigger | Purpose |
|----------|---------|---------|
| `deploy-docs.yml` | Manual | Quick docs-only build + deploy |
| `export-training.yml` | Manual | Regenerate training JSONL only |
| `download-wiki.yml` | Manual | Download wiki pages only |
| `download-events.yml` | Manual | Update events + regenerate homepage |
| `download-status.yml` | Manual | Update status + regenerate homepage |
| `sync-ragflow.yml` | Manual | RAGFlow sync only |
| `convert-mkdocs.yml` | Manual | MkDocs conversion only |
| `generate-completions.yml` | Manual | Q&A generation only |

### Required Secrets

| Secret | Used by |
|--------|---------|
| `RAGFLOW_API_KEY` | sync-ragflow, generate-completions |
| `RAGFLOW_BASE_URL` | sync-ragflow, generate-completions |
| `GOOGLE_API_KEY` | convert-to-mkdocs, generate-completions |

---

## Adding Additional Data Sources

The pipeline is modular. To add a new data source:

1. **Create a download script** (e.g., `scripts/download-mydata.py`)
   - Store output in `docs/` with an appropriate prefix
   - Track state in `config/processing-state.json` with `source_hash`

2. **Add to the pipeline** — insert after existing download steps in `full-pipeline.yml` and `run-full-pipeline.sh`

3. **Everything downstream works automatically** — sync, convert, link-fix, completions, and training export will pick up new documents via hash-driven change detection

---

## Training Data

The pipeline produces `training-data.jsonl` — a consolidated file of all Q&A pairs in OpenAI chat fine-tuning format:

```json
{"messages": [{"role": "user", "content": "How do I submit a GPU job on Vulcan?"}, {"role": "assistant", "content": "To submit a GPU job on Vulcan, use sbatch with..."}]}
```

**Stats:**
- ~80,000 Q&A pairs (deduplicated)
- English and Quebec French
- ~23 MB
- No system prompt (set at inference time)

Generated from page-level (10-20 Q&A) and chunk-level (2-3 Q&A) completions across all documents.

---

## Content Filtering

Low-value pages are automatically skipped during sync and conversion (`scripts/shared.py`):

- **Module lists** — `modules_avx*`, `modules_sse*`, `modules_specific*` (huge auto-generated tables)
- **Python wheels** — `wheels*` (version-specific package lists)
- **Navigation fragments** — `sidebar-*`
- **Empty files** — 0-byte documents
- **Non-wiki content** — `events/` and `status/` prefixes

---

## References

* [Digital Research Alliance of Canada](https://alliancecan.ca/)
* [Alliance Documentation (Source)](https://docs.alliancecan.ca/)
* [PAICE (Pan-Canadian AI Compute Environment)](https://alliancecan.ca/en/services/advanced-research-computing/pan-canadian-ai-compute-environment-paice)
* [RAGFlow](https://ragflow.io/)
* [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
* [Research Computing Group](https://www.ualberta.ca/en/information-services-and-technology/research-computing/index.html)

---

## Support

Many Bothans died to bring us this information. This project is provided as-is, but reasonable questions may be answered based on my coffee intake or mood. ;)

Feel free to open an [issue](https://github.com/ualberta-rcg/ragflow-wiki-data/issues) or email **[khoja1@ualberta.ca](mailto:khoja1@ualberta.ca)** or **[kali2@ualberta.ca](mailto:kali2@ualberta.ca)** for U of A related deployments.

---

## License

This project is released under the **MIT License** — see [LICENSE](./LICENSE) for details.

---

## About University of Alberta Research Computing

The [Research Computing Group](https://www.ualberta.ca/en/information-services-and-technology/research-computing/index.html) supports high-performance computing, data-intensive research, and advanced infrastructure for researchers at the University of Alberta and across Canada through the [Digital Research Alliance of Canada](https://alliancecan.ca/).

The [Alberta Machine Intelligence Institute (AMII)](https://amii.ca/) is one of Canada's three national AI institutes and co-operates the Vulcan cluster for machine learning research workloads.
