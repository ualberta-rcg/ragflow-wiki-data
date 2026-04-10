---
title: "Multi-Instance GPU"
slug: "multi-instance_gpu"
lang: "base"

source_wiki_title: "Multi-Instance GPU"
source_hash: "a58552e577f7a5020da9b651f4b66f20"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T09:02:12.475328+00:00"

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

Many programs are unable to fully use modern GPUs such as NVidia [A100s](https://www.nvidia.com/en-us/data-center/a100/) and [H100s](https://www.nvidia.com/en-us/data-center/h100/). [Multi-Instance GPU (MIG)](https://www.nvidia.com/en-us/technologies/multi-instance-gpu/) is a technology that allows partitioning a single GPU into multiple [instances](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#terminology), making each one a completely independent virtual GPU. Each of the GPU instances gets a portion of the original GPU's computational resources and memory, all detached from the other instances by on-chip protections.

Using GPU instances is less wasteful, and usage is billed accordingly. Jobs submitted on such instances use less of your allocated priority compared to a full GPU; you will then be able to execute more jobs and have shorter wait time.

## Choosing between a full GPU and a GPU instance
Jobs that use less than half of the computing power of a full GPU and less than half of the available memory should be evaluated and tested on an instance. In most cases, these jobs will run just as fast and consume less than half of the computing resource.

See section [Finding which of your jobs should use an instance](#finding-which-of-your-jobs-should-use-an-instance) for more details.

## Limitations
[The MIG technology does not support](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#application-considerations) [CUDA Inter-Process Communication (IPC)](https://developer.nvidia.com/docs/drive/drive-os/6.0.8.1/public/drive-os-linux-sdk/common/topics/nvsci_nvsciipc/Inter-ProcessCommunication1.html), which optimizes data transfers between GPUs over NVLink and NVSwitch. This limitation also reduces communication efficiency between instances. Consequently, **requesting more than one MIG instance in a job is not permitted**. Such a job will be rejected at submission time. If you feel you need more than one MIG instance, then either:
* Request a larger instance (e.g. a 3g instead of three 1g instances).
* Request an entire GPU or multiple GPUs.
* Use [MPS](hyper-q-mps.md) rather than MIG.
* [Contact Support](technical-support.md) explaining the reason you want to try running on multiple MIGs, and we can help you do the experiment.

Graphic APIs are not supported (for example, OpenGL, Vulkan, etc.); see [Application Considerations](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#application-considerations).

GPU jobs requiring many CPU cores may also require a full GPU instead of an instance. The maximum number of CPU cores per instance depends on [the number of cores per full GPU](allocations-and-compute-scheduling.md#ratios-in-bundles) and on the configured [MIG profiles](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#a100-profiles). Both vary between clusters and between GPU nodes in a cluster.

## Available configurations
While there are [many possible MIG configurations and profiles](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#supported-mig-profiles), the supported profiles are system dependent:
* [Narval, with NVIDIA A100-40gb GPUs](narval.md#gpu-instances)
* [Rorqual, with NVIDIA H100-80gb GPUs](rorqual.md#gpu-instances)
* [Nibi, with NVIDIA H100-80gb GPUS](nibi.md#gpu-instances)
* [Fir, with NVIDIA H100-80gb GPUS](fir.md#gpu-instances)

The profile name describes the size of the instance.
* **H100-1g.10gb**: 1/8th of the computing power with 10GB GPU memory
* **H100-2g.20gb**: 2/8th of the computing power with 20GB GPU memory
* **H100-3g.40gb**: 3/8th of the computing power with 40GB GPU memory

Using less powerful profiles will have a lower impact on your allocation and priority.

To list all the flavours of MIGs (plus the full size GPU names) available on a given cluster, one can run the following command:

```bash
sinfo -o "%G"|grep gpu|sed 's/gpu://g'|sed 's/),/\n/g'|cut -d: -f1|sort|uniq
```

The recommended maximum number of CPU cores and amount of system memory per instance are listed in the [table of ratios in bundles](allocations-and-compute-scheduling.md#ratios-in-bundles).

## Job examples

* Requesting an instance of power 3/8 and size 20GB for a 1-hour interactive job:

```bash
salloc --account=def-someuser --gpus=a100_3g.20gb:1 --cpus-per-task=2 --mem=40gb --time=1:0:0
```

* Requesting an instance of power 4/8 and size 20GB for a 24-hour batch job using the maximum recommended number of cores and system memory:

```bash
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

You can find information on current and past jobs on the [Narval usage portal (writing in progress)](portail.md).

Power consumption is a good indicator of the total computing power requested from the GPU. For example, the following job requested a full A100 GPU with a maximum TDP of 400W, but only used 100W on average, which is only 50W more than the idle electric consumption:

GPU functionality utilization may also provide insights on the usage of the GPU in cases where the power consumption is not sufficient. For this example job, GPU utilization graph supports the conclusion of the GPU power consumption graph, in that the job uses less than 25% of the available computing power of a full A100 GPU:

The final metrics to consider are the maximum amount of GPU memory and the average number of CPU cores required to run the job. For this example, the job uses a maximum of 3GB of GPU memory out of the 40GB of a full A100 GPU.

It was also launched using a single CPU core. When taking into account these three last metrics, we can confirm that the job should easily run on a 3g.20GB or 4g.20GB GPU instance with power and memory to spare.

Another way to monitor the usage of a running job is by [attaching to the node](running-jobs.md#attaching-to-a-running-job) where the job is currently running and then by using `nvidia-smi` to read the GPU metrics in real time. This will not provide maximum and average values for memory and power usage of the entire job, but it may be helpful to identify and troubleshoot underperforming jobs.