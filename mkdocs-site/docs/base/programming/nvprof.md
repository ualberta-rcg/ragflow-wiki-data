---
title: "Nvprof"
slug: "nvprof"
lang: "base"

source_wiki_title: "Nvprof"
source_hash: "a77ef604ab679c9403ba509598bb595b"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:49:19.915239+00:00"

tags:
  []

keywords:
  - "GPU profiling"
  - "Nvprof"
  - "NVIDIA Visual Profiler"
  - "CUDA"
  - "Summary mode"

questions:
  - "What is Nvprof and what types of profiling reports and data can it generate for CUDA-related activities?"
  - "What specific environment configurations, such as module loading and disabling DCGM, are required to run Nvprof on clusters like Béluga and Narval?"
  - "How does Nvprof's default \"Summary mode\" operate, and what specific performance metrics does it provide for kernel functions and memory copies?"
  - "What is Nvprof and what types of profiling reports and data can it generate for CUDA-related activities?"
  - "What specific environment configurations, such as module loading and disabling DCGM, are required to run Nvprof on clusters like Béluga and Narval?"
  - "How does Nvprof's default \"Summary mode\" operate, and what specific performance metrics does it provide for kernel functions and memory copies?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Nvprof is a command-line, lightweight, GUI-less profiler available for Linux, Windows, and Mac OS. This tool allows you to collect and view profiling data of CUDA-related activities on both CPU and GPU, including kernel execution, memory transfers, etc. Profiling options should be provided to the profiler via the command-line options.

## Strengths
It is capable of providing a textual report:
*   Summary of GPU and CPU activity
*   Trace of GPU and CPU activity
*   Event collection
Nvprof also features headless profile collection with the help of the NVIDIA Visual Profiler:
*   First use Nvprof on a headless node to collect data
*   Then visualize the timeline with Visual Profiler

## Quickstart guide

On [Béluga](béluga.md) and [Narval](narval.md), the [NVIDIA Data Center GPU Manager (DCGM)](https://developer.nvidia.com/dcgm) needs to be disabled, and this must be done while doing your job submission:

```bash
DISABLE_DCGM=1 salloc --gres=gpu:1 ...
```

When your job starts, DCGM will eventually stop running in the following minute. For convenience, the following loop awaits until the monitoring service has stopped (that is as soon as `grep` returns nothing):

```bash
while [ ! -z "$(dcgmi -v | grep 'Hostengine build info:')" ]; do sleep 5; done
```

## Environment modules
Before you start profiling with NVPROF, the appropriate [module](utiliser-des-modules.md) needs to be loaded.

NVPROF is part of the CUDA package, so run `module avail cuda` to see what versions are currently available with the compiler and MPI modules you have loaded. For a comprehensive list of CUDA modules, run `module -r spider '.*cuda.*'`.
At the time this was written these were:
*   cuda/10.0.130
*   cuda/10.0
*   cuda/9.0.176
*   cuda/9.0
*   cuda/8.0.44
*   cuda/8.0

Use `module load cuda/version` to choose a version. For example, to load the CUDA compiler version 10.0, do:
```bash
module load cuda/10.0
```

You also need to let nvprof where to find CUDA libraries. To do that, run this after loading the cuda module:

```bash
export LD_LIBRARY_PATH=$EBROOTCUDA/lib64:$LD_LIBRARY_PATH
```

## Compile your code
To get useful information from Nvprof, you first need to compile your code with one of the CUDA compilers (`nvcc` for C).

## Profiling modes
Nvprof operates in one of the modes listed below.
### Summary mode
This is the default operating mode for Nvprof. It outputs a single result line for each instruction such as a kernel function or CUDA memory copy/set performed by the application. For each kernel function, Nvprof outputs the total time of all instances of the kernel or type of memory copy as well as the average, minimum, and maximum time.
In this example, the application is `a.out` and we run Nvprof to get the profiling:

```bash
nvprof ./a.out
```
```text
[ ] - Starting...
==27694== NVPROF is profiling process 27694, command: a.out
GPU Device 0: "GeForce GTX 580" with compute capability 2.0

MatrixA(320,320), MatrixB(640,320)
Computing result using CUDA Kernel...
done
Performance= 35.35 GFlop/s, Time= 3.708 msec, Size= 131072000 Ops, WorkgroupSize= 1024 threads/block
Checking computed result for correctness: OK

==27694== Profiling application: matrixMul
==27694== Profiling result:
Time(%)      Time     Calls       Avg       Min       Max  Name
 99.94%  1.11524s       301  3.7051ms  3.6928ms  3.7174ms  void matrixMulCUDA<int=32>(float*, float*, float*, int, int)
  0.04%  406.30us         2  203.15us  136.13us  270.18us  [CUDA memcpy HtoD]
  0.02%  248.29us         1  248.29us  248.29us  248.29us  [CUDA memcpy DtoH]