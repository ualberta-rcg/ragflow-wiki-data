# RAGFlow Wiki Data

Wiki page content and generated artifacts for RAGFlow knowledge base.

## Structure

```
wiki_pages/          # Source documents (.txt files from MediaWiki)
keywords/            # Generated keyword files (per-chunk)
prompt_completion/   # Generated Q&A pairs for fine-tuning
scripts/             # Pipeline scripts
```

## Setup

1. Create Python venv:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install ragflow-sdk google-generativeai
   ```

2. Copy `config.env.example` to `config.env` and fill in your API keys

3. Run the update script:
   ```bash
   python scripts/update-ragflow.py
   ```

## Git Remote

Uses SSH alias `github.com-ragflow-wiki` for deploy key authentication.
