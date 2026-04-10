---
title: "Narval"
slug: "narval"
lang: "base"

source_wiki_title: "Narval"
source_hash: "334260a4ca3ccc71b44f645b2f076063"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T09:08:40.798607+00:00"

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

| | |
| :------------------------- | :------------------------------------------------------------------------------------------------------ |
| Availability: | Since October 2021 |
| Login node: | **narval.alliancecan.ca** |
| Globus Collection: | **[Compute Canada - Narval](https://app.globus.org/file-manager?origin_id=a1713da6-098f-40e6-b3aa-034efe8b6e5b)** |
| Copy node (rsync, scp, sftp,...): | **narval.alliancecan.ca** |
| Portal: | https://portail.narval.calculquebec.ca/ |

Narval is a heterogeneous and versatile cluster designed for a wide variety of small to medium-sized scientific computations. Built by Dell Canada and CDW Canada, Narval is located at the [École de technologie supérieure](http://www.etsmtl.ca/). Its name is a reminder of the [narwhal](https://en.wikipedia.org/wiki/Narwhal), a marine mammal sometimes observed in the waters of the St. Lawrence River.

## Features
Our policy is that Narval compute nodes do not have internet access. To make an exception, please contact [technical support](technical-support.md) explaining what you need and why. Note that the `crontab` tool is not available.

Each job should be at least one hour long (at least five minutes for test jobs) and you cannot have more than 1000 jobs (running and pending) at a time. The maximum job duration is 7 days (168 hours).

## Storage

| | |
| :------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| HOME <br> Lustre file system, 64 TB total space | * This space is small and cannot be expanded; you will need to use your `project` space for large storage needs.<br>* Small fixed [quotas](storage-and-file-management.md#quotas-et-politiques) per user.<br>* Automatic daily backup. |
| SCRATCH <br> Lustre file system, 5.7 PB total space | * Large space for storing temporary files during computations.<br>* No automatic backup system.<br>* Large fixed [quotas](storage-and-file-management.md#quotas-et-politiques) per user.<br>* There is an [automatic purging](scratch-purging-policy.md) of old files in this space. |
| PROJECT <br> Lustre file system, 35 PB total space | * This space is designed for sharing data among group members and for storing large amounts of data.<br>* Large adjustable [quotas](storage-and-file-management.md#quotas-et-politiques) per project.<br>* Automatic daily backup. |

At the very beginning of this page, a table indicates several connection addresses. For data transfers via [Globus](globus.md), the **Globus Endpoint** must be used. However, for tools such as [rsync](transferring-data.md#rsync) and [scp](transferring-data.md#scp), the **Copy Node** address must be used.

## High-Performance Networking

The [InfiniBand](https://en.wikipedia.org/wiki/InfiniBand) [Mellanox HDR](https://www.nvidia.com/en-us/networking/infiniband/qm8700/) network connects all cluster nodes. Each 40-port HDR switch (200 Gb/s) connects up to 66 HDR100 (100 Gb/s) nodes with 33 HDR links split into two (2) by special cables. The remaining seven (7) HDR links connect one cabinet's switch to each of the seven (7) HDR switches in the central InfiniBand network. Node islands are thus connected with a maximum blocking factor of 33:7 (4.7:1). However, storage servers are connected with a significantly lower blocking factor for maximum performance.

In practice, Narval's cabinets contain islands of 48 or 56 regular CPU nodes. It is therefore possible to execute parallel jobs using up to 3584 cores and non-blocking networking. For larger or more fragmented jobs across the network, the blocking factor is 4.7:1. The interconnection remains high-performance nonetheless.

## Node Specifications

| Nodes | Cores | Available Memory | CPU | Storage | GPU |
| :---- | :---- | :--------------- | :-- | :------ | :-- |
| 1145 | 64 | 250G or 256000M | 2 x [AMD EPYC 7532 (Zen 2)](https://www.amd.com/en/support/downloads/drivers.html/processors/epyc/epyc-7002-series/amd-epyc-7532.html) @ 2.40 GHz, 256M L3 cache | 1 x 960G SSD | |
| 33 | 64 | 2009G or 2057500M | 2 x [AMD EPYC 7532 (Zen 2)](https://www.amd.com/en/support/downloads/drivers.html/processors/epyc/epyc-7002-series/amd-epyc-7532.html) @ 2.40 GHz, 256M L3 cache | 1 x 960G SSD | |
| 3 | 64 | 4000G or 4096000M | 2 x [AMD EPYC 7502 (Zen 2)](https://www.amd.com/en/support/downloads/drivers.html/processors/epyc/epyc-7002-series/amd-epyc-7502.html) @ 2.50 GHz, 128M L3 cache | 1 x 960G SSD | |
| 159 | 48 | 498G or 510000M | 2 x [AMD EPYC 7413 (Zen 3)](https://www.amd.com/en/support/downloads/drivers.html/processors/epyc/epyc-7003-series/amd-epyc-7413.html) @ 2.65 GHz, 128M L3 cache | 1 x 3.84T SSD | 4 x NVidia A100SXM4 (40G memory), connected via NVLink |

### AMD Processor Specifics
#### Supported Instruction Sets
The Narval cluster is equipped with 2nd and 3rd generation AMD EPYC processors that support [AVX2](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions#Advanced_Vector_Extensions_2) instructions.

Narval does not support [AVX512](https://en.wikipedia.org/wiki/AVX-512) instructions, unlike more recent cluster nodes.

#### Intel Compilers
Intel compilers can compile applications very well for Narval's AMD processors, limiting themselves to AVX2 and older instruction sets. To do this, you must use the Intel compiler option `--march=core-avx2`, which produces executables compatible with both Intel and AMD processors.

However, if you have compiled code on a system using Intel processors and used one or more `-xXXXX` options, such as `-xCORE-AVX2`, the compiled applications will not work on Narval. This is because Intel compilers add extra instructions to verify that the processor being used is an Intel product. On Narval, the options `-xHOST` and `--march=native` are equivalent to `--march=pentium` (the old Pentium from 1993) and should **not** be used.

#### Available Software Environments
[The standard software environment `StdEnv/2023`](standard-software-environments.md) is the default environment on Narval. Older versions (2016 and 2018) have been deliberately blocked. If you need software that is only available on an older standard environment version, we invite you to send a request to [our technical support](technical-support.md).

#### BLAS and LAPACK Libraries
The Intel MKL library works on AMD processors, but it is not optimal. We now favour the use of FlexiBLAS. For more details, consult the [BLAS and LAPACK](blas-and-lapack.md) page.

### GPU Instances

To request one or more full A100 GPUs, use one of the following Slurm options:
*   **One A100-40GB**: `--gpus=a100:1`
*   **Multiple A100-40GB** per node:
    *   `--gpus-per-node=a100:2`
    *   `--gpus-per-node=a100:3`
    *   `--gpus-per-node=a100:4`
*   **Multiple A100-40GB** scattered anywhere: `--gpus=a100:n` (replace `n` with the desired number)

Several Narval GPU nodes are configured with [MIG technology](multi-instance-gpu.md), and four GPU instance sizes are available:

*   **1g.5gb**: 1/8 of the computing power with 5 GB of GPU memory.
*   **2g.10gb**: 2/8 of the computing power with 10 GB of GPU memory.
*   **3g.20gb**: 3/8 of the computing power with 20 GB of GPU memory.
*   **4g.20gb**: 4/8 of the computing power with 20 GB of GPU memory. This version is available in smaller numbers.

To request **one and only one** GPU instance for your compute job, here are the corresponding options:

*   **1g.5gb**: `--gpus=a100_1g.5gb:1`
*   **2g.10gb**: `--gpus=a100_2g.10gb:1`
*   **3g.20gb**: `--gpus=a100_3g.20gb:1`
*   **4g.20gb**: `--gpus=a100_4g.20gb:1`

The maximum recommended quantities of **CPU cores and system memory** per GPU instance are listed in the [table of *bundle* characteristics](allocations-and-compute-scheduling.md#ratios-dans-les-bundles).

## Job Monitoring

From the [portal](https://portail.narval.calculquebec.ca/), you can monitor your CPU and GPU compute jobs **in real-time** or past jobs to maximize resource utilization and reduce your queue wait times.

For a job, you can particularly visualize:
*   compute core usage;
*   memory usage;
*   GPU usage.

It is important to use the allocated resources and adjust your requests when compute resources are underused or not used at all. For example, if you request four CPU cores but only use one, you should adjust your submission file accordingly.