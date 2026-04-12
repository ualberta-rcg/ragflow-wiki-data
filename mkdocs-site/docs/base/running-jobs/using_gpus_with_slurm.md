---
title: "Using GPUs with Slurm"
slug: "using_gpus_with_slurm"
lang: "base"

source_wiki_title: "Using GPUs with Slurm"
source_hash: "7678c0542b247a340e93781fe0a5ed01"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:16:37.990740+00:00"

tags:
  - slurm

keywords:
  - "SBATCH"
  - "job scheduling"
  - "Slurm"
  - "H100"
  - "L40S-48gb"
  - "GNU Parallel"
  - "MPI process"
  - "single-GPU jobs"
  - "nvidia_h100_80gb_hbm3"
  - "SLURM job"
  - "GPU"
  - "GPU model specifiers"
  - "whole nodes"
  - "Multi-Instance GPUs"
  - "Trillium"
  - "Profiling GPU tasks"
  - "model specifiers"
  - "job scripts"
  - "DCGM"
  - "Killarney"
  - "--gpus-per-node"
  - "CPU cores"
  - "system memory"

questions:
  - "What is the recommended command format to request one or more GPUs for a Slurm job?"
  - "What alternative Slurm directives can be used to allocate GPU resources, and what should users do if these directives do not produce the expected results?"
  - "Which GPU models are available across the different clusters, and how are their model specifiers defined for Slurm?"
  - "How can a user find the available GPU model specifiers on a cluster, and why is it strongly recommended to explicitly include one in a job script?"
  - "What are the recommended maximum limits for CPU cores per full GPU requested on specific clusters like Fir, Narval, Nibi, and Rorqual?"
  - "How do the Slurm directives differ when configuring a single-core GPU job compared to a multi-threaded or MPI GPU job?"
  - "What specific NVIDIA H100 GPU configurations and memory sizes are associated with the Trillium node?"
  - "Which two types of GPUs are listed under the hardware specifications for the Killarney node?"
  - "What are the different memory partitions and variants of the H100 GPU mentioned in the text?"
  - "What specific resource limits, such as memory and time, are configured using the Slurm directives in the script?"
  - "How does the script utilize the allocated CPUs per task to set environment variables and execute the program?"
  - "Why does the text recommend requesting a whole node, and what type of applications benefit from this approach?"
  - "How can users pack multiple single-GPU programs into a single SLURM job using GNU Parallel?"
  - "How does the CUDA_VISIBLE_DEVICES variable prevent concurrent tasks from attempting to use the same GPU simultaneously?"
  - "What specific steps and environment variables are required to disable DCGM and enable GPU profiling on the Narval and Rorqual clusters?"
  - "How can users pack multiple single-GPU programs into a single SLURM job using GNU Parallel?"
  - "How does the CUDA_VISIBLE_DEVICES variable prevent concurrent tasks from attempting to use the same GPU simultaneously?"
  - "What specific steps and environment variables are required to disable DCGM and enable GPU profiling on the Narval and Rorqual clusters?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# Introduction

To request one or more GPUs for a [Slurm](running_jobs.md) job, use this form:
`--gpus-per-node=<model_specifier>:<number>`

For example:
`--gpus-per-node=a100:1`

This requests a single A100 GPU (unless you also use `--nodes` to specify more than a single node). See the following section, *Available GPUs,* for valid model specifiers.

The following form can also be used:
`--gres=gpu:<model_specifier>:<number>`

!!! warning
    The `--gres=gpu:<model_specifier>:<number>` form may not be supported in the future. We recommend that you replace it in your scripts with `--gpus-per-node`.

Slurm supports a variety of other directives that you can use to request GPU resources: `--gpus`, `--gpus-per-socket`, `--gpus-per-task`, `--mem-per-gpu`, and `--ntasks-per-gpu`. Please see the Slurm documentation for [sbatch](https://slurm.schedmd.com/sbatch.html) for more about these. Our staff do not test all of these; if you try one but don't get the result you expect, [contact technical support](../support/technical_support.md).

For general advice on job scheduling, see [Running jobs](running_jobs.md).

# Available GPUs
The following table summarizes the available GPU models and their corresponding specifiers:

| Cluster                                                | GPU model     | MIG   | Model specifiers for Slurm               | Synonyms for Slurm                    |
| :----------------------------------------------------- | :------------ | :---- | :--------------------------------------- | :------------------------------------ |
| [Fir](../software/fir.md#node-characteristics)                     | H100-80gb     |       | h100                                     |                                       |
| [Fir](../software/fir.md#node-characteristics)                     | H100-80gb     | 1/8   | nvidia_h100_80gb_hbm3_1g.10gb            |                                       |
| [Fir](../software/fir.md#node-characteristics)                     | H100-80gb     | 2/8   | nvidia_h100_80gb_hbm3_2g.20gb            |                                       |
| [Fir](../software/fir.md#node-characteristics)                     | H100-80gb     | 3/8   | nvidia_h100_80gb_hbm3_3g.40gb            |                                       |
| [Narval](../clusters/narval.md)               | A100-40gb     |       | a100                                     |                                       |
| [Narval](../clusters/narval.md)               | A100-40gb     | 1/8   | a100_1g.5gb                              |                                       |
| [Narval](../clusters/narval.md)               | A100-40gb     | 2/8   | a100_2g.10gb                             |                                       |
| [Narval](../clusters/narval.md)               | A100-40gb     | 2/8   | a100_3g.20gb                             |                                       |
| [Narval](../clusters/narval.md)               | A100-40gb     | 4/8   | a100_4g.20gb                             |                                       |
| [Nibi](../clusters/nibi.md#node-characteristics)                   | H100-80gb     |       | h100                                     |                                       |
| [Nibi](../clusters/nibi.md#node-characteristics)                   | H100-80gb     | 1/8   | nvidia_h100_80gb_hbm3_1g.10gb            | h100_1g.10gb h100_1.10 h100_10gb      |
| [Nibi](../clusters/nibi.md#node-characteristics)                   | H100-80gb     | 2/8   | nvidia_h100_80gb_hbm3_2g.20gb            | h100_2g.20gb h100_2.20 h100_20gb      |
| [Nibi](../clusters/nibi.md#node-characteristics)                   | H100-80gb     | 3/8   | nvidia_h100_80gb_hbm3_3g.40gb            | h100_3g.40gb h100_3.40 h100_40gb      |
| [Nibi](../clusters/nibi.md#node-characteristics)                   | MI300A-128gb  |       | mi300a                                   |                                       |
| [Rorqual](../clusters/rorqual.md)             | H100-80gb     |       | h100                                     |                                       |
| [Rorqual](../clusters/rorqual.md)             | H100-80gb     | 1/8   | nvidia_h100_80gb_hbm3_1g.10gb            | h100_1g.10gb h100_1.10 h100_10gb      |
| [Rorqual](../clusters/rorqual.md)             | H100-80gb     | 2/8   | nvidia_h100_80gb_hbm3_2g.20gb            | h100_2g.20gb h100_2.20 h100_20gb      |
| [Rorqual](../clusters/rorqual.md)             | H100-80gb     | 3/8   | nvidia_h100_80gb_hbm3_3g.40gb            | h100_3g.40gb h100_3.40 h100_40gb      |
| [Trillium](../clusters/trillium.md#node-characteristics)           | H100-80gb     |       | h100                                     |                                       |
| [Killarney](../clusters/killarney.md#killarney-hardware-specifications) | H100-80gb     |       | h100                                     |                                       |
| [Killarney](../clusters/killarney.md#killarney-hardware-specifications) | L40S-48gb     |       | l40s                                     |                                       |
| [tamIA](../clusters/tamia.md)                 | H100-80gb     |       | h100                                     |                                       |
| [tamIA](../clusters/tamia.md)                 | H200          |       | h200                                     |                                       |
| [Vulcan](../clusters/vulcan.md#vulcan-hardware-specifications)     | L40S-48gb     |       | l40s                                     |                                       |

GPU model specifiers (including MIG specifiers) available on any given cluster can be obtained from Slurm with the following command. This may be useful if the table above has not been updated with the latest changes.

```bash
sinfo -o "%G"|grep gpu|sed 's/gpu://g'|sed 's/),/\n/g'|cut -d: -f1|sort|uniq
```

There are short synonyms available for some of the MIG specifiers at certain sites; this command will not provide those synonyms. Also, the presence of a GPU model does not guarantee that you will be able to use one of the corresponding specifiers in your jobs; there may be further restrictions on what model specifiers are available based on (for example) which research group you belong. For further information, see the site-specific page by clicking on the cluster name in the above table, or [contact support](../support/technical_support.md).

!!! warning
    If you do not supply a model specifier, your job may be rejected or sent to an arbitrary GPU instance. There are very few programs which can use an arbitrary GPU efficiently, so we strongly recommend that you always provide a specific GPU model specifier in your job scripts.

There are GPUs available at Arbutus, but like other cloud resources, they cannot be scheduled via Slurm. See [Cloud resources](../cloud/cloud_resources.md) for more details.

## Multi-Instance GPUs (MIGs)
MIG is a technology that partitions a GPU into multiple instances. Your jobs might be able to use a MIG instance instead of a whole GPU. Please see [Multi-Instance GPU](../programming/multi-instance_gpu.md) for more about this.

# Requesting CPU cores and system memory

Along with each GPU instance, your job should have a number of CPU cores (default is `1`) and some amount of system memory. The recommended maximum numbers of CPU cores and gigabytes of system memory per GPU instance are listed in the [table of bundle characteristics](allocations_and_compute_scheduling.md#ratios-in-bundles).

# Examples

## Single-core job
If you need only a single CPU core and one GPU:

```bash linenums="1" title="gpu_serial_job.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --gpus-per-node=a100:1
#SBATCH --mem=4000M               # memory per node
#SBATCH --time=0-03:00
./program                         # you can use 'nvidia-smi' for a test
```

## Multi-threaded job
For a GPU job which needs multiple CPUs in a single node:

```bash linenums="1" title="gpu_threaded_job.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --gpus-per-node=a100:1
#SBATCH --cpus-per-task=6         # CPU cores or threads
#SBATCH --mem=4000M               # memory per node
#SBATCH --time=0-03:00
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
./program
```

!!! note "CPU Core Recommendations"
    For each full GPU requested, we recommend:
    *   on Fir, no more than 12 CPU cores;
    *   on Narval, no more than 12 CPU cores;
    *   on Nibi, no more than 14 CPU cores;
    *   on Rorqual, no more than 16 CPU cores.

## MPI job

```bash linenums="1" title="gpu_mpi_job.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --gpus=a100:8             # total number of GPUs
#SBATCH --ntasks-per-gpu=1        # total of 8 MPI processes
#SBATCH --cpus-per-task=6         # CPU cores per MPI process
#SBATCH --mem-per-cpu=5G          # host memory per CPU core
#SBATCH --time=0-03:00            # time (DD-HH:MM)
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
srun --cpus-per-task=$SLURM_CPUS_PER_TASK ./program
```

## Whole nodes
If your application can efficiently use an entire node and its associated GPUs, you will probably experience shorter wait times if you ask Slurm for a whole node. Use one of the following job scripts as a template.

### Packing single-GPU jobs within one SLURM job

If you need to run four single-GPU programs or two 2-GPU programs for longer than 24 hours, [GNU Parallel](gnu_parallel.md) is recommended. A simple example is:
```bash
cat params.input | parallel -j4 'CUDA_VISIBLE_DEVICES=$(({%} - 1)) python {} &> {#}.out'
```
In this example, the GPU ID is calculated by subtracting 1 from the slot ID `{%}` and `{#}` is the job ID, starting from 1.

A `params.input` file should include input parameters in each line, like this:
```
code1.py
code2.py
code3.py
code4.py
...
```
With this method, you can run multiple tasks in one submission. The `-j4` parameter means that GNU Parallel can run a maximum of four concurrent tasks, launching another as soon as one ends. `CUDA_VISIBLE_DEVICES` is used to ensure that two tasks do not try to use the same GPU at the same time.

## Profiling GPU tasks

On [Narval](../clusters/narval.md) and [Rorqual](../clusters/rorqual.md), profiling is possible but requires disabling the [NVIDIA Data Center GPU Manager (DCGM)](https://developer.nvidia.com/dcgm). This must be done during job submission by setting the `DISABLE_DCGM` environment variable:

```bash
DISABLE_DCGM=1 salloc --account=def-someuser --gpus-per-node=a100:1 --mem=4000M --time=03:00
```

Then, in your interactive job, wait until DCGM is disabled on the node:
```bash
while [ ! -z "$(dcgmi -v | grep 'Hostengine build info:')" ]; do  sleep 5; done
```

Finally, launch your profiler. For more details on profilers, see [Debugging and profiling](../programming/debugging_and_profiling.md).

!!! note
    On Fir and Nibi, GPU profiling like the above technique is not available yet.

# See also
*   [CUDA](../programming/cuda.md)
*   [Multi-Instance GPU](../programming/multi-instance_gpu.md)
*   [Running jobs](running_jobs.md)
*   [Metrix monitoring portal](../software/metrix.md)
*   [NVTOP (htop-like monitor for GPUs)](../programming/nvtop.md)
*   [Cuda Multi-Process Service (MPS)](../software/hyper-q___mps.md)