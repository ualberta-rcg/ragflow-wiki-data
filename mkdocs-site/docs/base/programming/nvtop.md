---
title: "NVTOP"
slug: "nvtop"
lang: "base"

source_wiki_title: "NVTOP"
source_hash: "957193df95d2c46903bebf824a5e0a98"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T09:07:22.675208+00:00"

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

[NVTOP](https://github.com/Syllo/nvtop) stands for Neat Videocard TOP, a (h)top like task monitor for GPUs and accelerators. It can handle multiple GPUs and print information about them in a htop-familiar way.

Because a picture is worth a thousand words:

## Monitor GPU usage
NVTOP can monitor single or multiple GPUs. It can show the GPU usage and its memory.
One can also select a specific device from the menu (F2 -> GPU Select).

!!! tip
    NVTOP is useful to monitor and verify that your job is using the GPU as efficiently as possible.

### Monitor batch job
If you have submitted a non-interactive job and would like to see its current GPU usage.

1. From a login node, find the job id and select the one to monitor:
    ```bash
    sq
    ```

2. Attach to the running job:
    ```bash
    srun --pty --overlap --jobid JOBID nvtop
    ```

### Monitor interactive job
1. Start your interactive job with minimal resources.

2. In a second terminal, connect to the login node, find the job id:
    ```bash
    sq
    ```

3. Attach to the running job:
    ```bash
    srun --pty --overlap --jobid JOBID nvtop
    ```

You'll be able to see the usage in real time as you run your commands in the first terminal.

### Monitor a GPU on a specific node
When running multi-nodes jobs, it can be useful to verify that one or all GPUs are effectively used.

1. From a login node, find the job id and identify the node names:
    ```bash
    sq
    srun --jobid JOBID --overlap -n1 -c1 scontrol show hostname
    ```

2. Attach to the running job on the specific node:
    ```bash
    srun --pty --overlap --jobid JOBID --nodelist NODENAME nvtop