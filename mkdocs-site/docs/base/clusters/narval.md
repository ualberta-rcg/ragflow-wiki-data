---
title: "Narval"
slug: "narval"
lang: "base"

source_wiki_title: "Narval"
source_hash: "334260a4ca3ccc71b44f645b2f076063"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:40:33.294005+00:00"

tags:
  []

keywords:
  - "serveurs de stockage"
  - "réseau InfiniBand central"
  - "Technologie MIG"
  - "Instances GPU"
  - "processeurs AMD EPYC"
  - "soutien technique"
  - "îlots de nœuds"
  - "Slurm"
  - "nœuds CPU et GPU"
  - "processeurs AMD"
  - "Bibliothèques BLAS et LAPACK"
  - "FlexiBLAS"
  - "compilateurs Intel"
  - "instructions AVX2"
  - "stockage"
  - "nœuds de calcul"
  - "Narval"
  - "A100"
  - "grappe de calcul"
  - "facteur de blocage"
  - "réseau InfiniBand"
  - "Suivi des tâches"
  - "commutateurs HDR"
  - "Intel MKL"

questions:
  - "Qu'est-ce que la grappe Narval et à quel type de calculs scientifiques est-elle destinée ?"
  - "Quelles sont les principales contraintes et limites imposées lors de l'exécution des tâches sur les nœuds de calcul ?"
  - "Quelles sont les différences entre les espaces de stockage HOME, SCRATCH et PROJECT en termes de capacité, de sauvegarde et d'utilisation ?"
  - "Quelles sont les capacités matérielles (cœurs, mémoire, GPU) et l'architecture réseau des nœuds de la grappe Narval ?"
  - "Quelles options de compilation faut-il utiliser ou éviter avec les compilateurs Intel pour garantir la compatibilité avec les processeurs AMD de Narval ?"
  - "Quel est l'environnement logiciel par défaut de Narval et quelle bibliothèque mathématique est recommandée pour optimiser les performances ?"
  - "Comment les commutateurs d'un cabinet sont-ils reliés au réseau InfiniBand central ?"
  - "Quel est le facteur de blocage maximum appliqué aux connexions des îlots de nœuds ?"
  - "Pourquoi les serveurs de stockage utilisent-ils un facteur de blocage significativement plus bas que le reste du réseau ?"
  - "Que faut-il faire si une ressource n'est disponible que sur une ancienne version de l'environnement standard ?"
  - "Quelle est la limitation de la bibliothèque Intel MKL lorsqu'elle est utilisée sur des processeurs AMD ?"
  - "Quelle bibliothèque est désormais recommandée à la place d'Intel MKL pour BLAS et LAPACK ?"
  - "Quelles sont les options Slurm à utiliser pour demander un ou plusieurs GPU A100 complets ?"
  - "Quelles sont les différentes tailles d'instances GPU disponibles avec la technologie MIG et comment les spécifier ?"
  - "Comment et pourquoi doit-on suivre l'utilisation des ressources de ses tâches de calcul via le portail Narval ?"
  - "Quelles sont les options Slurm à utiliser pour demander un ou plusieurs GPU A100 complets ?"
  - "Quelles sont les différentes tailles d'instances GPU disponibles avec la technologie MIG et comment les spécifier ?"
  - "Comment et pourquoi doit-on suivre l'utilisation des ressources de ses tâches de calcul via le portail Narval ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*   **Availability**: Since October 2021
*   **Login Node**: `narval.alliancecan.ca`
*   **Globus Collection**: [Compute Canada - Narval](https://app.globus.org/file-manager?origin_id=a1713da6-098f-40e6-b3aa-034efe8b6e5b)
*   **Copy Node (rsync, scp, sftp,...)**: `narval.alliancecan.ca`
*   **Portal**: [https://portail.narval.calculquebec.ca/](https://portail.narval.calculquebec.ca/)

Narval is a heterogeneous and versatile cluster designed for a wide variety of small to medium-sized scientific computations. Built by Dell Canada and CDW Canada, Narval is located at the [École de technologie supérieure](http://www.etsmtl.ca/). Its name evokes the [narwhal](https://fr.wikipedia.org/wiki/Narval), a marine mammal sometimes observed in the waters of the St. Lawrence River.

## Key Features

!!! warning "Internet Access Restricted"
    Narval compute nodes do not have internet access. To request an exception, please contact [technical support](../support/technical_support.md) explaining your needs and reasons. Note that the `crontab` tool is not available.

!!! note "Job Limits"
    *   Each job should have a minimum duration of one hour (at least five minutes for test jobs).
    *   You cannot have more than 1000 jobs (running and pending) at a time.
    *   The maximum job duration is 7 days (168 hours).

## Storage

| Location                                | Features                                                                                                                                                                                                                                                           |
| :-------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **HOME** <br> Lustre filesystem, 64 TB total space | *   This space is small and cannot be expanded; you will need to use your `project` space for large storage needs.<br>*   Small fixed [quotas per user](../storage-and-data/storage_and_file_management.md).<br>*   Automatic daily backups.                                        |
| **SCRATCH** <br> Lustre filesystem, 5.7 PB total space | *   Large space for temporary files during computations.<br>*   No automatic backups.<br>*   Large fixed [quotas per user](../storage-and-data/storage_and_file_management.md).<br>*   [Automatic purging](../storage-and-data/scratch_purging_policy.md) of old files.                           |
| **PROJECT** <br> Lustre filesystem, 35 PB total space | *   Designed for data sharing among group members and for storing large amounts of data.<br>*   Large adjustable [quotas per project](../storage-and-data/storage_and_file_management.md).<br>*   Automatic daily backups.                                                   |

!!! tip "Data Transfer"
    For data transfers via [Globus](../getting-started/globus.md), use the **Globus Collection**. For tools like [rsync](../getting-started/transferring_data.md#rsync) and [scp](../getting-started/transferring_data.md#scp), use the **Copy Node** address, as specified in the information provided at the beginning of this page.

## High-Performance Networking

The [InfiniBand](https://fr.wikipedia.org/wiki/Bus_InfiniBand) [Mellanox HDR](https://www.nvidia.com/en-us/networking/infiniband/qm8700/) network connects all cluster nodes. Each 40-port HDR (200 Gb/s) switch allows connecting up to 66 nodes in HDR100 (100 Gb/s) with 33 HDR links split into two (2) by special cables. The remaining seven (7) HDR links connect a cabinet switch to each of the seven (7) central InfiniBand network HDR switches. Node islands are thus connected with a maximum blocking factor of 33:7 (4.7:1). However, storage servers are connected with a significantly lower blocking factor for maximum performance.

In practice, Narval cabinets contain islands of 48 or 56 regular CPU nodes. It is therefore possible to execute parallel jobs using up to 3584 cores and non-blocking networking. For larger or more network-fragmented jobs, the blocking factor is 4.7:1. The interconnection nevertheless remains high-performance.

## Node Specifications

| Nodes | Cores | Available Memory  | CPU                                                                                                                              | Storage       | GPU                                                   |
| :---- | :---- | :---------------- | :------------------------------------------------------------------------------------------------------------------------------- | :------------ | :---------------------------------------------------- |
| 1145  | 64    | 250G or 256000M   | 2 x [AMD EPYC 7532 (Zen 2)](https://www.amd.com/en/support/downloads/drivers.html/processors/epyc/epyc-7002-series/amd-epyc-7532.html) @ 2.40 GHz, 256M L3 cache | 1 x 960G SSD  | None                                                  |
| 33    | 64    | 2009G or 2057500M | 2 x [AMD EPYC 7532 (Zen 2)](https://www.amd.com/en/support/downloads/drivers.html/processors/epyc/epyc-7002-series/amd-epyc-7532.html) @ 2.40 GHz, 256M L3 cache | 1 x 960G SSD  | None                                                  |
| 3     | 64    | 4000G or 4096000M | 2 x [AMD EPYC 7502 (Zen 2)](https://www.amd.com/en/support/downloads/drivers.html/processors/epyc/epyc-7002-series/amd-epyc-7502.html) @ 2.50 GHz, 128M L3 cache | 1 x 960G SSD  | None                                                  |
| 159   | 48    | 498G or 510000M   | 2 x [AMD EPYC 7413 (Zen 3)](https://www.amd.com/en/support/downloads/drivers.html/processors/epyc/epyc-7003-series/amd-epyc-7413.html) @ 2.65 GHz, 128M L3 cache | 1 x 3.84T SSD | 4 x NVidia A100SXM4 (40G memory), connected via NVLink |

### AMD Processor Specifics

#### Supported Instruction Sets
The Narval cluster is equipped with 2nd and 3rd generation AMD EPYC processors that support [AVX2](https://fr.wikipedia.org/wiki/Advanced_Vector_Extensions#Advanced_Vector_Extensions_2) instructions.

However, Narval does not support [AVX512](https://en.wikipedia.org/wiki/AVX-512) instructions, unlike more recent cluster nodes.

#### Intel Compilers
Intel compilers can successfully compile applications for Narval's AMD processors, provided they are limited to AVX2 and older instruction sets. To do this, use the Intel compiler option `-march=core-avx2`, which produces executables compatible with both Intel and AMD processors.

!!! warning "Intel Compiler Options"
    If you have compiled code on a system using Intel processors and used options like `-xXXXX` (e.g., `-xCORE-AVX2`), the compiled applications will **not** work on Narval. Intel compilers add extra instructions to verify that the processor used is an Intel product. On Narval, the options `-xHOST` and `-march=native` are equivalent to `-march=pentium` (the old Pentium from 1993) and should **not** be used.

#### Available Software Environments
The [Standard software environment `StdEnv/2023`](../programming/standard_software_environments.md) is the default environment on Narval. Older versions (2016 and 2018) have been intentionally blocked. If you require software only available in an older version of the standard environment, please submit a request to [technical support](../support/technical_support.md).

#### BLAS and LAPACK Libraries
The Intel MKL library works on AMD processors, but it is not optimal. We now recommend using FlexiBLAS. For more details, consult the [BLAS and LAPACK](../programming/blas_and_lapack.md) page.

### GPU Instances

To request one or more full A100 GPUs, use one of the following Slurm options:

*   **One A100-40gb**:
    ```bash
    --gpus=a100:1
    ```
*   **Multiple A100-40gb per node**:
    ```bash
    --gpus-per-node=a100:2
    --gpus-per-node=a100:3
    --gpus-per-node=a100:4
    ```
*   **Multiple A100-40gb scattered anywhere**:
    ```bash
    --gpus=a100:n
    ```
    (replace `n` with the desired number)

Several Narval GPU nodes are configured with [MIG (Multi-Instance GPU) technology](../programming/multi-instance_gpu.md), and four GPU instance sizes are available:

*   **1g.5gb**: 1/8 of the computing power with 5 GB of GPU memory.
*   **2g.10gb**: 2/8 of the computing power with 10 GB of GPU memory.
*   **3g.20gb**: 3/8 of the computing power with 20 GB of GPU memory.
*   **4g.20gb**: 4/8 of the computing power with 20 GB of GPU memory. This version is available in smaller quantities.

To request **one and only one** GPU instance for your computation job, here are the corresponding options:

*   **1g.5gb**:
    ```bash
    --gpus=a100_1g.5gb:1
    ```
*   **2g.10gb**:
    ```bash
    --gpus=a100_2g.10gb:1
    ```
*   **3g.20gb**:
    ```bash
    --gpus=a100_3g.20gb:1
    ```
*   **4g.20gb**:
    ```bash
    --gpus=a100_4g.20gb:1
    ```

The maximum recommended quantities of **CPU cores and system memory** per GPU instance are listed in the [Characteristics of *bundles* table](../running-jobs/allocations_and_compute_scheduling.md#ratios-in-bundles).

## Job Monitoring

From the [portal](https://portail.narval.calculquebec.ca/), you can monitor your CPU and GPU compute jobs **in real-time**, or past jobs, to maximize resource utilization and reduce your queue waiting times.

You can visualize the following for a job:

*   compute core utilization;
*   memory usage;
*   GPU utilization.

!!! tip "Resource Optimization"
    It is important to use the allocated resources effectively and to adjust your requests if compute resources are underutilized or not used at all. For example, if you request four CPU cores but only use one, you should adjust your submission file accordingly.