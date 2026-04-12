---
title: "NVTOP/en"
slug: "nvtop"
lang: "en"

source_wiki_title: "NVTOP/en"
source_hash: "adbb800b8bb31377fc62803ae6cb655a"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:39:33.363312+00:00"

tags:
  []

keywords:
  - "task monitor"
  - "interactive job"
  - "batch job"
  - "GPU usage"
  - "NVTOP"

questions:
  - "What is NVTOP and what primary functions does it serve for GPU monitoring?"
  - "How can a user attach NVTOP to a currently running batch or interactive job?"
  - "What specific steps and commands are required to monitor GPU usage on a designated node during a multi-node job?"
  - "What is NVTOP and what primary functions does it serve for GPU monitoring?"
  - "How can a user attach NVTOP to a currently running batch or interactive job?"
  - "What specific steps and commands are required to monitor GPU usage on a designated node during a multi-node job?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[NVTOP](https://github.com/Syllo/nvtop) stands for Neat Videocard TOP, a (h)top like task monitor for GPUs and accelerators. It can handle multiple GPUs and print information about them in a htop-familiar way.

## Monitor GPU usage
NVTOP can monitor single or multiple GPUs. It can show the GPU usage and its memory.
One can also select a specific device from the menu (F2 -> GPU Select).

!!! tip "GPU Usage Efficiency"
    NVTOP is useful to monitor and verify that your job is using the GPU as efficiently as possible.

### Monitor batch job
If you have submitted a non-interactive job and would like to see its current GPU usage.

1.  From a login node, find the job ID and select the one to monitor:
    ```bash
    sq
    ```

2.  Attach to the running job:
    ```bash
    srun --pty --overlap --jobid JOBID nvtop
    ```

### Monitor interactive job
1.  Start your interactive job with minimal resources.

2.  In a second terminal, connect to the login node, find the job ID:
    ```bash
    sq
    ```

3.  Attach to the running job:
    ```bash
    srun --pty --overlap --jobid JOBID nvtop
    ```
    You'll be able to see the usage in real time as you run your commands in the first terminal.

### Monitor a GPU on a specific node
When running multi-node jobs, it can be useful to verify that one or all GPUs are effectively used.

1.  From a login node, find the job ID and identify the node names:
    ```bash
    sq
    srun --jobid JOBID --overlap -n1 -c1 scontrol show hostname
    ```

2.  Attach to the running job on the specific node:
    ```bash
    srun --pty --overlap --jobid JOBID --nodelist NODENAME nvtop