---
title: "Scheduling policy updates/en"
slug: "scheduling_policy_updates"
lang: "en"

source_wiki_title: "Scheduling policy updates/en"
source_hash: "0d61021cdcac907e5220b5db66730bfa"
last_synced: "2026-04-18T23:39:30.217451+00:00"
last_processed: "2026-04-19T01:04:25.370889+00:00"

tags:
  []

keywords:
  - "job submission commands"
  - "job scheduling policies"
  - "RAC allocations"
  - "Multi-Instance GPU"
  - "GPU jobs"

questions:
  - "Which job submission commands might experience a change in behavior due to the policy updates recorded on this page?"
  - "What are the specific activation dates for the RAC 2026 accounts and sub-allocations across the fir, nibi, narval, and rorqual clusters?"
  - "What new requirements and limitations have been implemented regarding the specification of GPU models and Multi-Instance GPUs (MIGs) for GPU jobs?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

This page is intended to record when changes to [job scheduling policies](job_scheduling_policies.md) are made which might change the behaviour of job submission commands (`sbatch`, `salloc`, `srun`).

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