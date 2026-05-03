---
title: "Scheduling policy updates/en"
slug: "scheduling_policy_updates"
lang: "en"

source_wiki_title: "Scheduling policy updates/en"
source_hash: "7d07a78f6e68a850217d0ea271735e84"
last_synced: "2026-05-02T23:50:34.269007+00:00"
last_processed: "2026-05-03T00:46:44.522604+00:00"

tags:
  []

keywords:
  - "job scheduling policies"
  - "Multi-Instance GPU"
  - "Slurm"
  - "RAC allocations"
  - "GPU jobs"

questions:
  - "Which job submission commands are potentially affected by the scheduling policy changes detailed on this page?"
  - "When were the RAC allocations and sub-allocations activated for the Fir, Nibi, Narval, and Rorqual clusters?"
  - "What specific requirements and limitations must now be followed when requesting GPU jobs or MIG instances?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

This page records changes to [job scheduling policies](job_scheduling_policies.md) which might affect the behaviour of job submission commands `sbatch`, `salloc`, and `srun`.

## Accounts

### RAC allocations

* RAC 2026 accounts activated
    * Fir: 2026-04-06
    * Nibi: 2026-04-06
    * Narval: 2026-04-07
    * Rorqual: 2026-04-07

### Other account updates

* Sub-allocations available
    * Fir: 2026-04-06
    * Nibi: 2026-04-06
    * Narval: 2026-04-07
    * Rorqual: 2026-04-07

## CPU jobs

(none as of May 1, 2026)

## GPU jobs

* All GPU requests must [specify a GPU model](using_gpus_with_slurm.md#introduction) or an [instance model](../programming/multi-instance_gpu.md)
    * Fir: 2026-04-06
    * Nibi: 2026-04-06
    * Narval: (coming soon)
    * Rorqual: 2026-04-17
* Only one [MIG instance](../programming/multi-instance_gpu.md) may be requested at a time
    * Fir: 2026-04-06
    * Nibi: 2026-04-06
    * Narval: (coming soon)
    * Rorqual: 2026-04-17