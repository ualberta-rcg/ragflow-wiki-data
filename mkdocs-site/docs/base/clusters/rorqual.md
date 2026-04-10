---
title: "Rorqual"
slug: "rorqual"
lang: "base"

source_wiki_title: "Rorqual"
source_hash: "2432503fbd7ca744828a0b13e8a50f11"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T10:54:03.433988+00:00"

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

| Availability | June 19, 2025 |
| :----------- | :------------ |
| Login node | **rorqual.alliancecan.ca** |
| Data transfer node (rsync, scp, sftp ...) | **rorqual.alliancecan.ca** |
| [Automation node](automation-in-the-context-of-multifactor-authentication.md) | robot.rorqual.alliancecan.ca |
| Globus collection | [alliancecan#rorqual](https://app.globus.org/file-manager?origin_id=f19f13f5-5553-40e3-ba30-6c151b9d35d4) |
| JupyterHub | [jupyterhub.rorqual.alliancecan.ca](https://jupyterhub.rorqual.alliancecan.ca/) |
| Portal | [metrix.rorqual.alliancecan.ca](https://metrix.rorqual.alliancecan.ca/) |
| Webinar | [slides](https://docs.google.com/presentation/d/1SxqzNI9dtxnVCe8I2otJg6PJpLQwDjeDakNI7yMsuvU), [video](https://www.youtube.com/watch?v=hTM6XOvYjxw) |

Rorqual is a heterogeneous and versatile cluster designed for a wide variety of scientific computations. Built by Dell Canada and CDW Canada, Rorqual is located at the [École de technologie supérieure](http://www.etsmtl.ca/). Its name recalls the [rorqual](https://fr.wikipedia.org/wiki/Rorqual), a marine mammal whose several species, such as the [minke whale](https://baleinesendirect.org/decouvrir/especes-baleines-saint-laurent/13-especes/petit-rorqual/) and the [blue whale](https://baleinesendirect.org/decouvrir/especes-baleines-saint-laurent/13-especes/rorqual-bleu/), have been observed in the waters of the St. Lawrence River.

## Access
To access the computing cluster, each researcher must [complete an access request](https://ccdb.alliancecan.ca/me/access_systems) in the form found via *Resources > System Access* in the CCDB menu bar. In this form:

1.  Select *Rorqual* from the left-hand list.
2.  In the first box on the right, select the access request.
3.  Then accept all special agreements with Calcul Québec:
    *   Consent for the collection and use of personal information,
    *   Rorqual Service Level Agreement,
    *   Terms of Use.

Actual cluster access can take **up to one hour** after completing the access request.

## Specifics

!!! note
    Our policy is that Rorqual compute nodes do not have internet access. To request an exception, please contact [technical support](technical-support.md) explaining what you need and why. Note that the `crontab` tool is not available.

!!! tip "Job Scheduling Limits"
    Each job should have a duration of at least one hour (at least five minutes for test jobs), and you cannot have more than 1000 jobs (running and pending) at once. The maximum job duration is 7 days (168 hours).

## Storage
| Location | Description |
| :------- | :---------- |
| HOME<br>Lustre filesystem, 116 TB total space | * This space is small and cannot be expanded; you will need to use your `project` space for large storage needs.<br>* Small fixed [quotas](storage-and-file-management.md#quotas-and-policies) per user.<br>* Automatic daily backup. |
| SCRATCH<br>Lustre filesystem, 6.5 PB total space | * Accessible via the symbolic link `$HOME/links/scratch`.<br>* Large space for storing temporary files during computations.<br>* No automatic backup system.<br>* Large fixed [quotas](storage-and-file-management.md#quotas-and-policies) per user.<br>* There is an [automatic purging](scratch-purging-policy.md) of old files in this space. |
| PROJECT<br>Lustre filesystem, 62 PB total space | * Accessible via the symbolic link `$HOME/links/projects/project-name`.<br>* This space is designed for sharing data among group members and for storing large amounts of data.<br>* Large adjustable [quotas](storage-and-file-management.md#quotas-and-policies) per project.<br>* Automatic daily backup. |

!!! tip "Data Transfer"
    At the beginning of this page, a table lists several connection addresses. For data transfers via [Globus](globus.md), you must use the **Globus endpoint**. However, for tools like [rsync](transferring-data.md#rsync) and [scp](transferring-data.md#scp), you must use the address of the **data transfer node**.

## High-Performance Networking
*   InfiniBand Networking
    *   HDR 200Gbit/s
    *   Maximum blocking factor: 34:6 or 5.667:1
    *   Size of CPU node islands: up to 31 nodes of 192 cores capable of non-blocking communication.

## Node Characteristics

| Nodes | Cores | Available Memory | Storage | CPU | GPU |
| :---- | :---- | :--------------- | :------ | :-- | :-- |
| 670 | 192 | 750GB or 768000MB | 1 x 480GB SATA SSD (6Gbit/s) | 2 x [AMD EPYC 9654 (Zen 4)](https://www.amd.com/en/support/downloads/drivers.html/processors/epyc/epyc-9004-series/amd-epyc-9654.html) @ 2.40 GHz, 384MB L3 cache | |
| 8 | 192 | 750GB or 768000MB | 1 x 3.84TB NVMe SSD | 2 x [AMD EPYC 9654 (Zen 4)](https://www.amd.com/en/support/downloads/drivers.html/processors/epyc/epyc-9004-series/amd-epyc-9654.html) @ 2.40 GHz, 384MB L3 cache | |
| 8 | 192 | 3013GB or 3086250MB | 1 x 480GB SATA SSD (6Gbit/s) | 2 x [AMD EPYC 9654 (Zen 4)](https://www.amd.com/en/support/downloads/drivers.html/processors/epyc/epyc-9004-series/amd-epyc-9654.html) @ 2.40 GHz, 384MB L3 cache | |
| 93 | 64 | 498GB or 510000MB | 1 x 3.84TB NVMe SSD | 2 x [Intel Xeon Gold 6448Y](https://ark.intel.com/content/www/us/en/ark/products/232384/intel-xeon-gold-6448y-processor-60m-cache-2-10-ghz.html) @ 2.10 GHz, 60MB L3 cache | 4 x NVidia H100 SXM5 (80GB memory), connected via NVLink |

!!! tip
    To obtain a larger `$SLURM_TMPDIR` space, you must request `--tmp=xG`, where `x` is a value between 370 and 3360.

### CPU Node Topology
In a CPU node, the 192 cores and different memory spaces are not equidistant, which causes variable delays (on the order of nanoseconds) to access data. In each node, we have:

*   Two (2) CPU sockets, each having 12 system memory channels.
    *   Four (4) [NUMA nodes](https://fr.wikipedia.org/wiki/Non_uniform_memory_access) per CPU socket, each connected to three (3) system memory channels.
        *   Three (3) *chiplets* per NUMA node, each having its own [L3 cache](https://fr.wikipedia.org/wiki/Cache_de_processeur) of 32 MiB.
            *   Eight (8) cores per *chiplet*, each having its own L2 cache of 1 MiB and L1 cache of 32+32 KiB.

In other words, we have:
*   Groups of 8 closely located cores that share the same L3 cache, which is ideal for [multi-threaded parallel programs](running-jobs.md#multi-threaded-or-openmp-jobs) (for example, with the option `--cpus-per-task=8`).
*   NUMA nodes of 3×8 = 24 cores that share a trio of system memory channels.
*   A total of 2×4×3×8 = 192 cores per node.

!!! tip "Optimizing CPU Node Topology"
    To fully benefit from this topology, you must reserve full nodes (for example, with `--ntasks-per-node=24 --cpus-per-task=8`) and explicitly control the placement of processes and threads. Depending on the parallel program and the number of cores used, the gains can be marginal or significant.

### GPU Node Topology
In GPU nodes, the architecture is less hierarchical. We have:

*   Two (2) CPU sockets. For each, we have:
    *   Eight (8) system memory channels
    *   60 MiB of L3 cache
    *   32 equidistant cores, each having its own L2 cache of 2 MiB and L1 cache of 32+48 KiB.
    *   Two (2) NVidia H100 accelerators

In total, the four (4) accelerators on the node are interconnected by [SXM5](https://en.wikipedia.org/wiki/SXM_(socket)).

### GPU Instances
The different GPU instance names available on Rorqual are:

| Model or Instance | Short Name | No Units | By Memory | Full Name |
| :---------------- | :--------- | :------- | :-------- | :-------- |
| **GPU H100-80gb** | `h100` | `h100` | `h100_80gb` | `nvidia_h100_80gb_hbm3` |
| **MIG H100-1g.10gb** | `h100_1g.10gb` | `h100_1.10` | `h100_10gb` | `nvidia_h100_80gb_hbm3_1g.10gb` |
| **MIG H100-2g.20gb** | `h100_2g.20gb` | `h100_2.20` | `h100_20gb` | `nvidia_h100_80gb_hbm3_2g.20gb` |
| **MIG H100-3g.40gb** | `h100_3g.40gb` | `h100_3.40` | `h100_40gb` | `nvidia_h100_80gb_hbm3_3g.40gb` |

To request one or more full H100 GPUs, use one of the following Slurm options:

*   **One H100-80gb**:
    ```bash
    # Request one H100-80gb GPU
    --gpus=h100:1
    # or using the more specific name
    --gpus=h100_80gb:1
    ```
*   **Multiple H100-80gb** per node:
    ```bash
    # Request 2, 3, or 4 H100-80gb GPUs on a single node
    --gpus-per-node=h100:2
    --gpus-per-node=h100:3
    --gpus-per-node=h100:4
    ```
*   **Multiple H100-80gb** distributed anywhere:
    ```bash
    # Request 'n' H100-80gb GPUs across multiple nodes
    --gpus=h100:n
    ```
    (replace `n` with the desired number)

Approximately half of Rorqual's GPU nodes are configured with [MIG technology](multi-instance-gpu.md), and only three GPU instance sizes are available:

*   **H100-1g.10gb**: 1/8 of the computing power with 10 GB of GPU memory.
*   **H100-2g.20gb**: 2/8 of the computing power with 20 GB of GPU memory.
*   **H100-3g.40gb**: 3/8 of the computing power with 40 GB of GPU memory.

To request **one and only one** GPU instance for your compute job, here are the corresponding options:

*   **H100-1g.10gb**:
    ```bash
    --gpus=h100_1g.10gb:1
    ```
*   **H100-2g.20gb**:
    ```bash
    --gpus=h100_2g.20gb:1
    ```
*   **H100-3g.40gb**:
    ```bash
    --gpus=h100_3g.40gb:1
    ```

!!! note
    The maximum recommended quantities of **CPU cores and system memory** per GPU instance are listed in the [table of *bundle* characteristics](allocations-and-compute-scheduling.md#ratios-in-bundles).