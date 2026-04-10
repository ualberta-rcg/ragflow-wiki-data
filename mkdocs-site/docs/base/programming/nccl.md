---
title: "NCCL"
slug: "nccl"
lang: "base"

source_wiki_title: "NCCL"
source_hash: "2ab491b8e0a4febbbceaf28d3122c2a1"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T09:07:08.776107+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

## What is NCCL
Please see the [NVIDIA webpage](https://developer.nvidia.com/nccl).

## Troubleshooting
To activate NCCL debug outputs, set the following variable before running NCCL:
```bash
NCCL_DEBUG=info
```

To fix `Caught error during NCCL init [...] connect() timed out` errors, set the following variable before running NCCL:
```bash
export NCCL_BLOCKING_WAIT=1