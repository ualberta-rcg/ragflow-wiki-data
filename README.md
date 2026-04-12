# RAGFlow Wiki Data

Pipeline for syncing Alliance HPC documentation to RAGFlow and publishing as an MkDocs site.

## Structure

```
docs/                # Source documents (.txt from MediaWiki API)
completions/         # Generated Q&A pairs (page + chunk level)
mkdocs-site/         # MkDocs Material site (docs/ subfolder has .md output)
config/              # processing-state.json, tags.json
scripts/             # Pipeline scripts
```

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Set environment variables (or use GitHub Actions secrets):
- `RAGFLOW_API_KEY`
- `RAGFLOW_BASE_URL`
- `GOOGLE_API_KEY`

## Usage

Run the full pipeline via GitHub Actions (`full-pipeline.yml`) or locally:

```bash
source venv/bin/activate
python scripts/download-wiki.py
python scripts/sync-ragflow.py
python scripts/convert-to-mkdocs.py
python scripts/fix-mkdocs-links.py
python scripts/generate-homepage.py
python scripts/generate-completions.py
```
