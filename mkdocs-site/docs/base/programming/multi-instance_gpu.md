---
title: "Multi-Instance GPU"
slug: "multi-instance_gpu"
lang: "base"

source_wiki_title: "Multi-Instance GPU"
source_hash: "dcf95e80be8a50c6723f7a133a15ed00"
last_synced: "2026-04-25T23:42:08.699101+00:00"
last_processed: "2026-04-26T00:20:15.489878+00:00"

tags:
  []

keywords:
  - "streaming multiprocessors"
  - "processing units"
  - "SMs"
  - "NVIDIA"
  - "MIG"
  - "GPU configuration"
  - "NVidia MIG documentation"
  - "power consumption"
  - "H100 SXM5"
  - "H100"
  - "CPU cores"
  - "instances"
  - "MIG profiles"
  - "unassigned SMs"
  - "GPU instances"
  - "computing power"
  - "H100 SXM5 GPU"
  - "Multi-Instance GPU"
  - "MIGs"
  - "allocation and priority"
  - "GPU memory"
  - "GPU utilization"

questions:
  - "What is Multi-Instance GPU (MIG) technology and what are the primary benefits of using it instead of a full GPU?"
  - "What are the key technical limitations and restrictions when submitting jobs to MIG instances?"
  - "How are MIG profiles configured, and what do the profile names indicate about the allocated computing power and memory?"
  - "How can a user request a specific fractional GPU instance, such as a 3g.20gb or 4g.20gb, for interactive or batch jobs?"
  - "What performance metrics should be evaluated to determine if a job is suitable for a fractional GPU instance instead of a full GPU?"
  - "Why is the division of an H100 GPU into sevenths or eighths technically more complicated than NVIDIA's MIG documentation suggests?"
  - "What are the computing power and memory specifications for the different H100 GPU profiles?"
  - "How does selecting a less powerful GPU profile affect a user's allocation and priority?"
  - "How can a user list all the available MIG flavors and full-size GPU names on a given cluster?"
  - "How does NVidia's MIG documentation describe the fractional division of a GPU?"
  - "How many streaming multiprocessors are contained within an H100 SXM5 GPU?"
  - "Why does the mathematical factorization of the GPU's processing units complicate the documentation's claims?"
  - "How are the 132 Streaming Multiprocessors (SMs) of an H100 SXM5 partitioned into different instances under MIG?"
  - "What happens to the remaining eight SMs after the instances are assigned, and why are they considered effectively lost?"
  - "Why does the text argue that the partitioned H100 GPU should be measured in \"thirty-thirdths\" rather than NVIDIA's terminology of \"eighths\"?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Many programs are unable to fully use modern GPUs such as NVIDIA [A100s](https://www.nvidia.com/en-us/data-center/a100/) and [H100s](https://www.nvidia.com/en-us/data-center/h100s/). [Multi-Instance GPU (MIG)](https://www.nvidia.com/en-us/technologies/multi-instance-gpu/) is a technology that allows partitioning a single GPU into multiple [instances](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#terminology), making each one a completely independent virtual GPU. Each of the GPU instances gets a portion of the original GPU's computational resources and memory, all detached from the other instances by on-chip protections.

Using GPU instances is less wasteful, and usage is billed accordingly. Jobs submitted on such instances use less of your allocated priority compared to a full GPU; you will then be able to execute more jobs and have shorter wait times.

## Choosing between a full GPU and a GPU instance
Jobs that use less than half of the computing power of a full GPU and less than half of the available memory should be evaluated and tested on an instance. In most cases, these jobs will run just as fast and consume less than half of the computing resource.

See section [Finding which of your jobs should use an instance](#finding-which-of-your-jobs-should-use-an-instance) for more details.

## Limitations
[The MIG technology does not support](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#application-considerations) [CUDA Inter-Process Communication (IPC)](https://developer.nvidia.com/docs/drive/drive-os/6.0.8.1/public/drive-os-linux-sdk/common/topics/nvsci_nvsciipc/Inter-ProcessCommunication1.html), which optimizes data transfers between GPUs over NVLink and NVSwitch. This limitation also reduces communication efficiency between instances. Consequently, **requesting more than one MIG instance in a job is not permitted**. Such a job will be rejected at submission time. If you feel you need more than one MIG instance, then either:
*   Request a larger instance (e.g. a 3g instead of three 1g instances).
*   Request an entire GPU or multiple GPUs.
*   Consider whether you can avoid requesting multiple MIGs using a [job array](../running-jobs/job_arrays.md), [META-Farm](../running-jobs/meta-farm.md), [GNU Parallel](../running-jobs/gnu_parallel.md), or [GLOST](../running-jobs/glost.md).
*   Use [MPS](../software/hyper-q___mps.md) rather than MIG.
*   [Contact Support](../support/technical_support.md) explaining the reason you want to try running on multiple MIGs. An analyst can help you find an efficient alternative, or arrange a scheduling exception for you.

Graphic APIs are not supported (for example, OpenGL, Vulkan, etc.); see [Application Considerations](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#application-considerations).

GPU jobs requiring many CPU cores may also require a full GPU instead of an instance. The maximum number of CPU cores per instance depends on [the number of cores per full GPU](../running-jobs/allocations_and_compute_scheduling.md#ratios-in-bundles) and on the configured [MIG profiles](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#a100-profiles). Both vary between clusters and between GPU nodes in a cluster.

## Available configurations
While there are [many possible MIG configurations and profiles](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#supported-mig-profiles), the supported profiles are system dependent:
*   [Narval, with NVIDIA A100-40gb GPUs](../clusters/narval.md#gpu-instances)
*   [Rorqual, with NVIDIA H100-80gb GPUs](../clusters/rorqual.md#gpu-instances)
*   [Nibi, with NVIDIA H100-80gb GPUS](../clusters/nibi.md#gpu-instances)
*   [Fir, with NVIDIA H100-80gb GPUS](../software/fir.md#gpu-instances)

The profile name describes the size of the instance.
*   **H100-1g.10gb**: 1/8th of the computing power with 10GB GPU memory
*   **H100-2g.20gb**: 2/8th of the computing power with 20GB GPU memory
*   **H100-3g.40gb**: 3/8th of the computing power with 40GB GPU memory

Using less powerful profiles will have a lower impact on your allocation and priority.

To list all the flavours of MIGs (plus the full size GPU names) available on a given cluster, one can run the following command:

```bash
sinfo -o "%G"|grep gpu|sed 's/gpu://g'|sed 's/),/\n/g'|cut -d: -f1|sort|uniq
```

The recommended maximum number of CPU cores and amount of system memory per instance are listed in the [table of ratios in bundles](../running-jobs/allocations_and_compute_scheduling.md#ratios-in-bundles).

## Job examples

*   Requesting an instance of power 3/8 and size 20GB for a 1-hour interactive job:

```bash
salloc --account=def-someuser --gpus=a100_3g.20gb:1 --cpus-per-task=2 --mem=40gb --time=1:0:0
```

*   Requesting an instance of power 4/8 and size 20GB for a 24-hour batch job using the maximum recommended number of cores and system memory:

```bash title="a100_4g.20gb_mig_job.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --gpus=a100_4g.20gb:1
#SBATCH --cpus-per-task=6    # There are 6 CPU cores per 3g.20gb and 4g.20gb on Narval.
#SBATCH --mem=62gb           # There are 62GB GPU RAM per 3g.20gb and 4g.20gb on Narval.
#SBATCH --time=24:00:00

hostname
nvidia-smi
```

## Finding which of your jobs should use an instance

You can find information on current and past jobs on the Narval usage portal (writing in progress).

Power consumption is a good indicator of the total computing power requested from the GPU. For example, a job requested a full A100 GPU with a maximum TDP of 400W, but only used 100W on average. This average usage is only 50W more than the idle electric consumption, indicating underutilization.

GPU functionality utilization may also provide insights into GPU usage when power consumption alone is insufficient. For this example job, utilization metrics show that the job used less than 25% of the available computing power of a full A100 GPU.

The final metrics to consider are the maximum amount of GPU memory and the average number of CPU cores required to run the job. For this example, the job used a maximum of 3GB of GPU memory out of the 40GB available on a full A100 GPU.

It was also launched using a single CPU core. When taking into account these three last metrics, we can confirm that the job should easily run on a 3g.20GB or 4g.20GB GPU instance with power and memory to spare.

Another way to monitor the usage of a running job is by [attaching to the node](../running-jobs/running_jobs.md) where the job is currently running and then by using `nvidia-smi` to read the GPU metrics in real time. This will not provide maximum and average values for memory and power usage of the entire job, but it may be helpful to identify and troubleshoot underperforming jobs.

## GPU configuration details

Note that while NVIDIA's [MIG documentation](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/latest/supported-mig-profiles.html#h100-mig-profiles) speaks in terms of sevenths and eighths of a GPU, the reality is rather more complicated. An H100 SXM5 GPU has a total of 132 processing units (streaming multiprocessors; "SMs"). The number 132 factorizes into 11\*3\*2\*2, which is divisible neither by seven nor by eight.

Under MIG, an H100 SXM5's 132 SMs are partitioned into:

*   **One** instance of **60** SMs (`nvidia_h100_80gb_hbm3_3g.40gb`)
*   **One** instance of **32** SMs (`nvidia_h100_80gb_hbm3_2g.20gb`)
*   **Two** instances of **16** SMs (`nvidia_h100_80gb_hbm3_1g.10gb`)

leaving eight SMs *unassigned* and effectively lost (60+32+16+16+(8) = 124 *assigned* + 8 *unassigned* = 132). Rather than speaking of eighths then, we should consider a MIGed H100 divided into *thirty-thirdths*, however unwieldy this may be. What NVIDIA calls "one eighth" is therefore 4/33 of an H100 GPU, "two eighths" is 8/33 and "three eighths" is 15/33, with 2/33 of the GPU not assigned to any instance.