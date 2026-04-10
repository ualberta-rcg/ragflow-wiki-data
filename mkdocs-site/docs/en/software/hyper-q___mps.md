---
title: "Hyper-Q / MPS/en"
slug: "hyper-q___mps"
lang: "en"

source_wiki_title: "Hyper-Q / MPS/en"
source_hash: "a62877e2161ea6a0f2450de01b6cbe1c"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T07:18:04.938962+00:00"

tags:
  - software

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

## Overview

Hyper-Q (or MPS) is a feature of NVIDIA GPUs. It is available in GPUs with CUDA compute capability 3.5 and higher (for a table relating NVIDIA GPU model names, architecture names, and CUDA compute capabilities, see [NVIDIA Tesla](https://en.wikipedia.org/wiki/Nvidia_Tesla)).

[According to NVIDIA](https://docs.nvidia.com/deploy/mps/index.html),
> *The MPS runtime architecture is designed to transparently enable co-operative multi-process CUDA applications, typically MPI jobs, to utilize Hyper-Q capabilities on the latest NVIDIA (Kepler and later) GPUs. Hyper-Q allows CUDA kernels to be processed concurrently on the same GPU; this can benefit performance when the GPU compute capacity is underutilized by a single application process.*

In our tests, MPS may increase the total GPU flop rate even when the GPU is being shared by unrelated CPU processes. That means that MPS is great for CUDA applications with relatively small problem sizes, which on their own cannot efficiently saturate modern GPUs with thousands of cores.

MPS is not enabled by default, but it is straightforward to do. Execute the following commands before running your CUDA application:

```bash
export CUDA_MPS_PIPE_DIRECTORY=/tmp/nvidia-mps
export CUDA_MPS_LOG_DIRECTORY=/tmp/nvidia-log
nvidia-cuda-mps-control -d
```

Then you can use the MPS feature if you have more than one CPU thread accessing the GPU. This will happen if you run a hybrid MPI/CUDA application, a hybrid OpenMP/CUDA application, or multiple instances of a serial CUDA application (*GPU farming*).

Additional details on MPS can be found here: [CUDA Multi Process Service (MPS) - NVIDIA Documentation](https://docs.nvidia.com/deploy/mps/index.html).

## GPU farming

One situation when the MPS feature can be very useful is when you need to run multiple instances of a CUDA application, but the application is too small to saturate a modern GPU. MPS allows you to run multiple instances of the application sharing a single GPU, as long as there is enough of GPU memory for all of the instances of the application. In many cases this should result in a significantly increased throughput from all of your GPU processes.

Here is an example of a job script to set up GPU farming:

```bash title="script.sh"
#!/bin/bash
#SBATCH --gpus-per-node=v100:1
#SBATCH --time=0-10:00
#SBATCH --mem-per-cpu=8G
#SBATCH --cpus-per-task=8
 
mkdir -p $SLURM_TMPDIR/tmp
export CUDA_MPS_LOG_DIRECTORY=$SLURM_TMPDIR/tmp
nvidia-cuda-mps-control -d
 
for ((i=0; i<SLURM_CPUS_PER_TASK; i++))
 do
 echo $i
 ./my_code $i  &
 done
 
wait
```

In the above example, we share a single V100 GPU between 8 instances of `my_code` (which takes a single argument-- the loop index `$i`). We request 8 CPU cores (`#SBATCH --cpus-per-task=8`) so there is one CPU core per application instance. The two important elements are:

*   `&` on the code execution line, which sends the code processes to the background, and
*   the `wait` command at the end of the script, which ensures that the job runs until all background processes end.