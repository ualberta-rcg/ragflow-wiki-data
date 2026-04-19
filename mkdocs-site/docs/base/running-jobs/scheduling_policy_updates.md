---
title: "Scheduling policy updates"
slug: "scheduling_policy_updates"
lang: "base"

source_wiki_title: "Scheduling policy updates"
source_hash: "e8b66869959780eca8d3707426d5ffdd"
last_synced: "2026-04-18T23:39:30.217451+00:00"
last_processed: "2026-04-19T01:04:16.145966+00:00"

tags:
  []

keywords:
  - "GPU requests"
  - "Sub-allocations"
  - "job scheduling policies"
  - "RAC allocations"
  - "Multi-Instance GPU"

questions:
  - "What is the primary purpose of the page regarding job scheduling policies and submission commands?"
  - "When are the RAC 2026 accounts and sub-allocations scheduled to be activated for the different clusters?"
  - "What new requirements and restrictions are being introduced for GPU job requests?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

This page is intended to record when changes to [job scheduling policies](job_scheduling_policies.md) are made which might change the behaviour of job submission commands (sbatch, salloc, srun).

## Account related changes

### RAC allocations

*   RAC 2026 accounts activated
    *   fir: 2026-04-06
    *   nibi: 2026-04-06
    *   narval: 2026-04-07
    *   rorqual: 2026-04-07

### Other policy changes on accounts

*   Sub-allocations enabled
    *   fir: 2026-04-06
    *   nibi: 2026-04-06
    *   narval: 2026-04-07
    *   rorqual: 2026-04-07

## CPU jobs related changes

(None at the moment)

## GPU jobs related changes

*   All GPU requests must specify a GPU or [instance](../programming/multi-instance_gpu.md) model
    *   fir: 2026-04-06
    *   nibi: 2026-04-06
    *   narval: [not done yet]
    *   rorqual: 2026-04-17
*   Multiple [MIGs](../programming/multi-instance_gpu.md) cannot be requested in a single job
    *   fir: 2026-04-06
    *   nibi: 2026-04-06
    *   narval: [not done yet]
    *   rorqual: 2026-04-17