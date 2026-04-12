#!/usr/bin/env bash
# Append a progress snapshot every 30 minutes to pipeline-watch.log
# (Chat assistants cannot message you on a timer; use this file or `tail -f`.)
set -u
ROOT="/opt/vulcan/ragflow-wiki-data"
LOG="$ROOT/pipeline-run.log"
OUT="$ROOT/pipeline-watch.log"

snapshot() {
  echo "========================================" >>"$OUT"
  date -u "+[%Y-%m-%d %H:%M:%S UTC] snapshot" >>"$OUT"
  if pgrep -f "run-full-pipeline.sh" >/dev/null 2>&1; then
    echo "pipeline: RUNNING (run-full-pipeline.sh)" >>"$OUT"
  else
    echo "pipeline: NOT RUNNING (run-full-pipeline.sh)" >>"$OUT"
  fi
  if [[ -f "$LOG" ]]; then
    grep -oE '\[[0-9]+/1050\]' "$LOG" 2>/dev/null | tail -1 | sed 's/^/  sync progress: /' >>"$OUT" || true
    grep -oE '\[[0-9]+/[0-9]+\].*convert' "$LOG" 2>/dev/null | tail -1 >>"$OUT" || true
    grep -E "Step [0-9].*complete|PIPELINE FINISHED|Converted:|Processed:" "$LOG" 2>/dev/null | tail -5 >>"$OUT" || true
    echo "  log lines: $(wc -l <"$LOG")" >>"$OUT"
    tail -2 "$LOG" | sed 's/^/  last: /' >>"$OUT"
  else
    echo "  (no pipeline-run.log)" >>"$OUT"
  fi
}

echo "Started $(date -u '+%Y-%m-%d %H:%M:%S UTC') — logging every 30m to $OUT" >>"$OUT"
snapshot
while sleep 1800; do
  snapshot
done
