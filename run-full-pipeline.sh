#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

LOGFILE="$SCRIPT_DIR/pipeline-run.log"
source venv/bin/activate
export PYTHONUNBUFFERED=1

log() { echo "[$(date -u '+%Y-%m-%d %H:%M:%S UTC')] $*" | tee -a "$LOGFILE"; }

log "=========================================="
log "FULL PIPELINE RUN — ALL DOCS"
log "=========================================="

log "Step 1/9: Download wiki pages"
python3 scripts/download-wiki.py 2>&1 | tee -a "$LOGFILE"
log "Step 1 complete"

log "Step 2/9: Download events"
python3 scripts/download-events.py 2>&1 | tee -a "$LOGFILE"
log "Step 2 complete"

log "Step 3/9: Download status"
python3 scripts/download-status.py 2>&1 | tee -a "$LOGFILE"
log "Step 3 complete"

log "Step 4/9: Sync ALL docs to RAGFlow (BATCH_SIZE=0)"
BATCH_SIZE=0 python3 scripts/sync-ragflow.py --allow-failures 2>&1 | tee -a "$LOGFILE"
log "Step 4 complete"

log "Step 5/9: Convert ALL docs to MkDocs (BATCH_SIZE=0)"
BATCH_SIZE=0 python3 scripts/convert-to-mkdocs.py 2>&1 | tee -a "$LOGFILE"
log "Step 5 complete"

log "Step 6/9: Fix internal MkDocs links"
BATCH_SIZE=0 python3 scripts/fix-mkdocs-links.py 2>&1 | tee -a "$LOGFILE"
log "Step 6 complete"

log "Step 7/9: Regenerate homepage"
python3 scripts/generate-homepage.py 2>&1 | tee -a "$LOGFILE"
log "Step 7 complete"

log "Step 8/9: Generate prompt completions (BATCH_SIZE=0)"
BATCH_SIZE=0 python3 scripts/generate-completions.py 2>&1 | tee -a "$LOGFILE"
log "Step 8 complete"

log "Step 9/9: Export training data"
python3 scripts/export-training-data.py 2>&1 | tee -a "$LOGFILE"
log "Step 9 complete"

log "=========================================="
log "PIPELINE FINISHED"
log "=========================================="
