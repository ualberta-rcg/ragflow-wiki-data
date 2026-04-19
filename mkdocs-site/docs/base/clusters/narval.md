---
title: "Narval"
slug: "narval"
lang: "base"

source_wiki_title: "Narval"
source_hash: "6c51984e2ad180ce5ab085a7aecdb92a"
last_synced: "2026-04-18T23:39:30.217451+00:00"
last_processed: "2026-04-19T00:58:20.818611+00:00"

tags:
  []

keywords:
  - "nœuds CPU"
  - "A100"
  - "Technologie MIG"
  - "soutien technique"
  - "commutateurs HDR"
  - "réseau InfiniBand"
  - "Réseau InfiniBand"
  - "Instances GPU"
  - "Système de fichiers Lustre"
  - "processeurs AMD"
  - "Slurm"
  - "grappe Narval"
  - "facteur de blocage"
  - "instructions AVX2"
  - "Suivi des tâches"
  - "îlots de nœuds"
  - "compilateurs Intel"
  - "FlexiBLAS"
  - "Nœuds de calcul"
  - "Calcul scientifique"
  - "Grappe Narval"
  - "Bibliothèques BLAS et LAPACK"
  - "Intel MKL"
  - "processeurs AMD EPYC"
  - "serveurs de stockage"

questions:
  - "Quelles sont les restrictions principales concernant l'exécution des tâches et l'accès à internet sur les nœuds de calcul de Narval ?"
  - "Quelles sont les différences entre les espaces de stockage HOME, SCRATCH et PROJECT en termes de capacité, de sauvegarde et d'utilisation ?"
  - "Comment l'architecture du réseau haute performance InfiniBand de Narval est-elle structurée pour relier les nœuds et les serveurs de stockage ?"
  - "Quelles sont les caractéristiques matérielles principales (processeurs, mémoire, cartes graphiques) des différents nœuds de la grappe Narval ?"
  - "Quelles options de compilation faut-il utiliser ou éviter avec les compilateurs Intel pour assurer la compatibilité avec les processeurs AMD de Narval ?"
  - "Quel est l'environnement logiciel par défaut sur cette grappe et quelle bibliothèque mathématique est recommandée à la place d'Intel MKL ?"
  - "Comment les commutateurs d'un cabinet sont-ils reliés au réseau InfiniBand central ?"
  - "Quel est le facteur de blocage maximum appliqué aux connexions des îlots de nœuds ?"
  - "Pourquoi les serveurs de stockage utilisent-ils un facteur de blocage significativement plus bas que le reste du réseau ?"
  - "Que faut-il faire si un élément n'est disponible que sur une ancienne version de l'environnement standard ?"
  - "Quelle est la limitation de la bibliothèque Intel MKL lorsqu'elle est utilisée sur des processeurs AMD ?"
  - "Quelle bibliothèque est désormais recommandée et privilégiée pour l'utilisation de BLAS et LAPACK ?"
  - "Quelles sont les options Slurm à utiliser pour demander un ou plusieurs GPU A100 complets ?"
  - "Comment fonctionne la technologie MIG sur Narval et quelles tailles d'instances GPU fractionnées permet-elle de réserver ?"
  - "Pourquoi est-il recommandé de suivre ses tâches de calcul sur le portail et quelles métriques peut-on y visualiser ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

| | |
| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------- |
| Availability: | since October 2021 |
| Login node: | **narval.alliancecan.ca** |
| Globus Collection: | [Compute Canada - Narval](https://app.globus.org/file-manager?origin_id=a1713da6-098f-40e6-b3aa-034efe8b6e5b) |
| Copy node (rsync, scp, sftp,...): | **narval.alliancecan.ca** |
| Portal: | https://portail.narval.calculquebec.ca/ |

Narval is a heterogeneous and versatile cluster designed for a wide variety of small to medium-sized scientific computations. Built by Dell Canada and CDW Canada, Narval is located at the [École de technologie supérieure](http://www.etsmtl.ca/). Its name refers to the [narwhal](https://en.wikipedia.org/wiki/Narwhal), a marine mammal sometimes observed in the waters of the St. Lawrence River.

## Particularities

!!! warning "Internet Access and `crontab`"
    Our policy dictates that Narval compute nodes do not have access to the internet. To request an exception, please contact [technical support](../support/technical_support.md) explaining what you need and why. Note that the `crontab` tool is not available.

Each job should be at least one hour long (at least five minutes for test jobs) and you cannot have more than 1000 jobs (running and pending) at a time. The maximum job duration is 7 days (168 hours).

## Storage

| | |
| :---------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| HOME <br> Lustre filesystem, 64 TB total space | * This space is small and cannot be expanded; you will need to use your `project` space for large storage needs. <br> * Small, fixed [quotas](../storage-and-data/storage_and_file_management.md) per user. <br> * Automatic daily backups are performed. |
| SCRATCH <br> Lustre filesystem, 5.7 PB total space | * Large space for storing temporary files during computations. <br> * No automatic backup system. <br> * Large, fixed [quotas](../storage-and-data/storage_and_file_management.md) per user. <br> * There is an [automatic purging](../storage-and-data/scratch_purging_policy.md) of old files in this space. |
| PROJECT <br> Lustre filesystem, 35 PB total space | * This space is designed for data sharing among group members and for storing large amounts of data. <br> * Large, adjustable [quotas](../storage-and-data/storage_and_file_management.md) per project. <br> * Automatic daily backups are performed. |

At the very beginning of this page, a table indicates several connection addresses. For data transfers via [Globus](../getting-started/globus.md), you must use the **Globus Drop-off Point**. However, for tools like [rsync](../getting-started/transferring_data.md#rsync) and [scp](../getting-started/transferring_data.md#scp), you must use the **Copy Node** address.

## High-Performance Networking

The [Mellanox HDR InfiniBand](https://www.nvidia.com/en-us/networking/infiniband/qm8700/) network connects all nodes in the cluster. Each 40-port HDR switch (200 Gb/s) can connect up to 66 nodes in HDR100 (100 Gb/s) with 33 HDR links split into two (2) using special cables. The remaining seven (7) HDR links are used to connect a cabinet's switch to each of the seven (7) central InfiniBand HDR switches. Node islands are thus connected with a maximum blocking factor of 33:7 (4.7:1). However, storage servers are connected with a significantly lower blocking factor for maximum performance.

In practice, Narval cabinets contain islands of 48 or 56 regular CPU nodes. It is therefore possible to run parallel jobs using up to 3584 cores and non-blocking networking. For larger or more network-fragmented jobs, the blocking factor is 4.7:1. Despite this, the interconnection remains high-performance.

## Node Characteristics

| Nodes | Cores | Available Memory | CPU | Storage | GPU |
| :---- | :---- | :--------------- | :-- | :------ | :-- |
| 1145 | 64 | 250G or 256000M | 2 x [AMD EPYC 7532 (Zen 2)](https://www.amd.com/en/support/downloads/drivers.html/processors/epyc/epyc-7002-series/amd-epyc-7532.html) @ 2.40 GHz, 256M L3 cache | 1 x 960G SSD | |
| 33 | 64 | 2009G or 2057500M | 2 x [AMD EPYC 7532 (Zen 2)](https://www.amd.com/en/support/downloads/drivers.html/processors/epyc/epyc-7002-series/amd-epyc-7532.html) @ 2.40 GHz, 256M L3 cache | 1 x 960G SSD | |
| 3 | 64 | 4000G or 4096000M | 2 x [AMD EPYC 7502 (Zen 2)](https://www.amd.com/en/support/downloads/drivers.html/processors/epyc/epyc-7002-series/amd-epyc-7502.html) @ 2.50 GHz, 128M L3 cache | 1 x 960G SSD | |
| 159 | 48 | 498G or 510000M | 2 x [AMD EPYC 7413 (Zen 3)](https://www.amd.com/en/support/downloads/drivers.html/processors/epyc/epyc-7003-series/amd-epyc-7413.html) @ 2.65 GHz, 128M L3 cache | 1 x 3.84T SSD | 4 x NVidia A100SXM4 (40G memory), connected via NVLink |

### AMD Processor Specifics

#### Supported Instruction Sets

The Narval cluster is equipped with 2nd and 3rd generation AMD EPYC processors that support [AVX2](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions#Advanced_Vector_Extensions_2) instructions.

However, Narval does not support [AVX512](https://en.wikipedia.org/wiki/AVX-512) instructions, unlike newer cluster nodes.

#### Intel Compilers

Intel compilers can effectively compile applications for Narval's AMD processors by limiting them to AVX2 and older instruction sets. To do this, you must use the `-march=core-avx2` option with the Intel compiler, which produces executables that are compatible with both Intel and AMD processors.

However, if you compiled code on a system using Intel processors and used one or more `-xXXXX` options, such as `-xCORE-AVX2`, the compiled applications will not run on Narval, because Intel compilers add additional instructions to verify that the processor used is an Intel product. On Narval, the `-xHOST` and `-march=native` options are equivalent to `-march=pentium` (the old Pentium from 1993) and should **not** be used.

#### Available Software Environments

[The standard software environment `StdEnv/2023`](../programming/standard_software_environments.md) is the default environment on Narval. Older versions (2016 and 2018) have been deliberately blocked. If you need software that is only available on an older version of the standard environment, we invite you to send a request to [our technical support](../support/technical_support.md).

#### BLAS and LAPACK Libraries

The Intel MKL library works on AMD processors, but it is not optimal. We now favour the use of FlexiBLAS. For more details, consult the [BLAS and LAPACK](../programming/blas_and_lapack.md) page.

### GPU Instances

To request one or more full A100 GPUs, use one of the following Slurm options:

*   **One A100-40GB**:
    ```bash
    --gpus=a100:1
    ```
*   **Multiple A100-40GB** per node:
    ```bash
    --gpus-per-node=a100:2
    --gpus-per-node=a100:3
    --gpus-per-node=a100:4
    ```
*   **Multiple A100-40GB** scattered anywhere:
    ```bash
    --gpus=a100:n
    ```
    (replace `n` with the desired number)

Several Narval GPU nodes are configured with [MIG technology](../programming/multi-instance_gpu.md) and three GPU instance sizes are available:

*   **1g.5gb**: 1/8 of the compute power with 5 GB of GPU memory.
*   **2g.10gb**: 2/8 of the compute power with 10 GB of GPU memory.
*   **3g.20gb**: 3/8 of the compute power with 20 GB of GPU memory.

To request **one and only one** GPU instance for your compute job, here are the corresponding options:

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

The maximum recommended quantities of **CPU cores and system memory** per GPU instance are listed in the [bundles characteristics table](../running-jobs/allocations_and_compute_scheduling.md).

## Monitoring Your Jobs

From the [portal](https://portail.narval.calculquebec.ca/), you can monitor your CPU and GPU compute jobs **in real-time** or past jobs to maximize resource utilization and decrease your wait times in the queue.

For a given job, you will be able to visualize:
*   compute core usage;
*   memory usage;
*   GPU usage.

It is important to use the allocated resources and adjust your requests when compute resources are underused or not used at all. For example, if you request four cores (CPU) but only use one, you must adjust your submission file accordingly.