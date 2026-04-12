#!/usr/bin/env python3
"""
Export all completions to a single training JSONL file.

Reads all completions/{lang}/{category}/{slug}/*.json files and outputs
a consolidated training-data.jsonl in OpenAI fine-tuning format.

Deduplicates questions (keeps first occurrence).
"""

import json
from pathlib import Path
from datetime import datetime, timezone

REPO_ROOT = Path(__file__).resolve().parent.parent
COMPLETIONS_DIR = REPO_ROOT / "completions"
OUTPUT_FILE = REPO_ROOT / "training-data.jsonl"


def export_training_data():
    """Export all completions to a single JSONL file."""
    
    if not COMPLETIONS_DIR.exists():
        print("No completions directory found.")
        return 0
    
    seen_questions = set()
    records = []
    duplicates_skipped = 0
    files_processed = 0
    
    # Find all JSON files in completions
    json_files = list(COMPLETIONS_DIR.rglob("*.json"))
    print(f"Found {len(json_files)} completion files")
    
    for json_file in sorted(json_files):
        try:
            data = json.loads(json_file.read_text(encoding="utf-8"))
            qa_pairs = data.get("qa_pairs", [])
            doc_key = data.get("doc_key", "")
            level = data.get("level", "unknown")
            
            for qa in qa_pairs:
                question = qa.get("question", "").strip()
                answer = qa.get("answer", "").strip()
                
                if not question or not answer:
                    continue
                
                # Deduplicate by normalized question
                q_normalized = question.lower()
                if q_normalized in seen_questions:
                    duplicates_skipped += 1
                    continue
                seen_questions.add(q_normalized)
                
                # OpenAI fine-tuning format (no system prompt - set at inference time)
                record = {
                    "messages": [
                        {"role": "user", "content": question},
                        {"role": "assistant", "content": answer}
                    ]
                }
                records.append(record)
            
            files_processed += 1
            
        except Exception as e:
            print(f"  Warning: Could not process {json_file}: {e}")
    
    # Write JSONL
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
    
    print(f"\nExport complete:")
    print(f"  Files processed: {files_processed}")
    print(f"  Total Q&A pairs: {len(records)}")
    print(f"  Duplicates skipped: {duplicates_skipped}")
    print(f"  Output: {OUTPUT_FILE}")
    print(f"  Size: {OUTPUT_FILE.stat().st_size / 1024:.1f} KB")
    
    return len(records)


if __name__ == "__main__":
    export_training_data()
