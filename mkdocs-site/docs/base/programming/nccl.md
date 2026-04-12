---
title: "NCCL"
slug: "nccl"
lang: "base"

source_wiki_title: "NCCL"
source_hash: "2ab491b8e0a4febbbceaf28d3122c2a1"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:39:15.151526+00:00"

tags:
  []

keywords:
  - "NCCL_BLOCKING_WAIT"
  - "connect() timed out"
  - "Troubleshooting"
  - "NCCL_DEBUG"
  - "NCCL"

questions:
  - "Where can users find official information explaining what NCCL is?"
  - "Which environment variable must be set to activate NCCL debug outputs?"
  - "How can you resolve the \"connect() timed out\" error during NCCL initialization?"
  - "Where can users find official information explaining what NCCL is?"
  - "Which environment variable must be set to activate NCCL debug outputs?"
  - "How can you resolve the \"connect() timed out\" error during NCCL initialization?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
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