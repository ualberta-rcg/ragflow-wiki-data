---
title: "Rorqual/en"
slug: "rorqual"
lang: "en"

source_wiki_title: "Rorqual/en"
source_hash: "1feb8bbfbccae5db1ee90b2ae6567375"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T10:55:02.469372+00:00"

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

| Availability: | June 19, 2025 |
| :------------ | :------------ |
| Login node: | **rorqual.alliancecan.ca** |
| Data transfer node (rsync, scp, sftp ...): | **rorqual.alliancecan.ca** |
| [Automation node](automation_in_the_context_of_multifactor_authentication.md): | robot.rorqual.alliancecan.ca |
| Globus collection: | [alliancecan#rorqual](https://app.globus.org/file-manager?origin_id=f19f13f5-5553-40e3-ba30-6c151b9d35d4) |
| JupyterHub: | [jupyterhub.rorqual.alliancecan.ca](https://jupyterhub.rorqual.alliancecan.ca/) |
| Portal: | [metrix.rorqual.alliancecan.ca](https://metrix.rorqual.alliancecan.ca/) |
| Webinar: | [slides](https://docs.google.com/presentation/d/1Ah61BBKZIJcn_AeosgUspxRCX_amubPUetZY68SfyXU), [video](https://www.youtube.com/watch?v=lXetzrViI8Q) |

Rorqual is a heterogeneous and versatile cluster designed for a wide variety of scientific calculations. Built by Dell Canada and CDW Canada, the cluster is located at the [École de technologie supérieure](https://www.etsmtl.ca/en/) in Montreal. Its name recalls the [rorqual](https://en.wikipedia.org/wiki/Rorqual), a marine mammal of which several species can be observed in the St. Lawrence River.

## Access
Each researcher must [request access in CCDB](https://ccdb.alliancecan.ca/me/access_systems), via *Resources--> Access Systems*.

1.  Select *Rorqual* from the list on the left.
2.  Select *I request access*.
3.  Click on the button to accept each of the following agreements
    1.  Calcul Québec Consent for the collection and use of personal information
    2.  Rorqual Service Level Agreement
    3.  Calcul Québec Terms of Use

It can take **up to one hour** for your access to be enabled.

## Site-specific policies

Rorqual's compute nodes cannot access the internet. If you need an exception to this rule, contact [technical support](technical_support.md) explaining what you need and why.

The `crontab` tool is not offered.

Each job should have a duration of at least one hour (at least five minutes for test jobs) and you cannot have more than 1000 jobs, running or queued, at any given moment. The maximum duration is 7 days (168 hours).

## Storage

| Filesystem | Description |
| :--------- | :---------- |
| HOME <br> Lustre filesystem, 116 TB | * This small space cannot be increased; for larger storage needs, use the `/project` space<br>* Small per user [quotas](storage_and_file_management.md#filesystem-quotas-and-policies)<br>* Daily automatic backup |
| SCRATCH <br> Lustre filesystem, 6.5 PB | * Accessible via symbolic link `$HOME/links/scratch`<br>* Large space for storing temporary files during computations<br>* No backup system in place<br>* Large per user [quotas](storage_and_file_management.md#filesystem-quotas-and-policies)<br>* Older files are [automatically purged](scratch_purging_policy.md) |
| PROJECT <br> Lustre filesystem, 62 PB | * Accessible via symbolic link `$HOME/links/projects/nom-du-projet`<br>* Designed for sharing data among the members of a research group and for storing large amounts of data<br>* Large and adjustable per group [quotas](storage_and_file_management.md#quotas-et-politiques)<br>* Daily backup |

For transferring data via [Globus](globus_fr.md), use the endpoint specified at the top of this page; for tools like [rsync](transferring_data.md#rsync) and [scp](transferring_data.md#scp), please use the login node.

## High-performance interconnect
*   InfiniBand interconnect
    *   HDR 200Gb/s
    *   Maximum blocking factor 34:6 or 5.667:1
    *   CPU node island size, up to 31 nodes of 192 cores, fully non-blocking.

## Node characteristics

| nodes | cores | available memory | storage | CPU | GPU |
| :---- | :---- | :--------------- | :------ | :-- | :-- |
| 670 | 192 | 750G or 768000M | 1 x SATA SSD, 480G (6Gbit/s) | 2 x [AMD EPYC 9654 (Zen 4)](https://www.amd.com/en/support/downloads/drivers.html/processors/epyc/epyc-9004-series/amd-epyc-9654.html) @ 2.40 GHz, 384MB cache L3 | |
| 8 | 192 | 750G or 768000M | 1 x NVMe SSD, 3.84TB | 2 x [AMD EPYC 9654 (Zen 4)](https://www.amd.com/en/support/downloads/drivers.html/processors/epyc/epyc-9004-series/amd-epyc-9654.html) @ 2.40 GHz, 384MB cache L3 | |
| 8 | 192 | 3013G or 3086250M | 1 x SATA SSD, 480G (6Gbit/s) | 2 x [AMD EPYC 9654 (Zen 4)](https://www.amd.com/en/support/downloads/drivers.html/processors/epyc/epyc-9004-series/amd-epyc-9654.html) @ 2.40 GHz, 384MB cache L3 | |
| 93 | 64 | 498G or 510000M | 1 x NVMe SSD, 3.84TB | 2 x [Intel Xeon Gold 6448Y](https://ark.intel.com/content/www/us/en/ark/products/232384/intel-xeon-gold-6448y-processor-60m-cache-2-10-ghz.html) @ 2.10 GHz, 60MB cache L3 | 4 x NVidia H100 SXM5 (80GB), connected via NVLink |

*   To get a larger `$SLURM_TMPDIR` space, a job can be submitted with `--tmp=xG`, where `x` is a value between 370 and 3360.

### CPU nodes
The 192 cores and the different memory spaces are not equidistant, which causes variable delays (of the order of nanoseconds) to access data. In each node, there are

*   2 sockets, each with 12 system memory channels
    *   4 [NUMA](https://en.wikipedia.org/wiki/Non-uniform_memory_access) nodes per socket, each connected to 3 system memory channels
        *   3 chiplets per NUMA node, each with its own 32 MiB [L3 cache memory](https://en.wikipedia.org/wiki/CPU_cache)
            *   8 cores per chiplet, each with its own 1 MiB L2 cache memory and 32+32 KiB L1 cache memory

In other words, we have
*   groups of 8 closely spaced cores sharing a single L3 cache, which is ideal for [multithreaded parallel programs](running_jobs.md#threaded-or-openmp-job) (for example, with the `--cpus-per-task=8` option)
*   NUMA nodes of 3x8 = 24 cores sharing a trio of system memory channels
*   a total of 2x4x3x8 = 192 cores per node

To fully benefit from this topology, full nodes must be reserved (e.g., with `--ntasks-per-node=24 --cpus-per-task=8`) and the place of processes and threads must be explicitly controlled. Depending on the parallel program and the number of cores used, gains can be marginal or significant.

### GPU nodes
The architecture is not as hierarchical.

*   2 sockets, each with
    *   8 system memory channels
    *   60 MiB L3 cache memory
    *   32 equidistant cores, each each with its own 2 MiB L2 cache memory and 32+48 KiB L1 cache memory
    *   2 NVidia H100 accelerators

The 4 node accelerators are interconnected by [SXM5](https://en.wikipedia.org/wiki/SXM_(socket)).

### GPU instances

Available GPU instance names are:

| Model | Instance | Short name | Without unit | By memory | Long name |
| :---- | :------- | :--------- | :----------- | :-------- | :-------- |
| **GPU** | **H100-80gb** | `h100` | `h100` | `h100_80gb` | `nvidia_h100_80gb_hbm3` |
| **MIG** | **H100-1g.10gb** | `h100_1g.10gb` | `h100_1.10` | `h100_10gb` | `nvidia_h100_80gb_hbm3_1g.10gb` |
| **MIG** | **H100-2g.20gb** | `h100_2g.20gb` | `h100_2.20` | `h100_20gb` | `nvidia_h100_80gb_hbm3_2g.20gb` |
| **MIG** | **H100-3g.40gb** | `h100_3g.40gb` | `h100_3.40` | `h100_40gb` | `nvidia_h100_80gb_hbm3_3g.40gb` |

To request one or more full H100 GPUs, you need to use one of the following Slurm options:
*   **One H100-80gb**: `--gpus=h100:1` or `--gpus=h100_80gb:1`
*   **Multiple H100-80gb** per node:
    *   `--gpus-per-node=h100:2`
    *   `--gpus-per-node=h100:3`
    *   `--gpus-per-node=h100:4`
*   **For multiple full H100 GPUs** spread anywhere: `--gpus=h100:n` (replace `n` with the number of GPUs you want)

Approximately half of the GPU nodes are configured with [MIG technology](multi-instance_gpu.md), and only 3 GPU instance sizes are available:

*   **H100-1g.10gb**: 1/8th of the computing power with 10GB GPU memory
*   **H100-2g.20gb**: 2/8th of the computing power with 20GB GPU memory
*   **H100-3g.40gb**: 3/8th of the computing power with 40GB GPU memory

To request **one and only one GPU instance** for your compute job, use the corresponding option:

*   **H100-1g.10gb**: `--gpus=h100_1g.10gb:1`
*   **H100-2g.20gb**: `--gpus=h100_2g.20gb:1`
*   **H100-3g.40gb**: `--gpus=h100_3g.40gb:1`

The maximum recommended number of **CPU cores and system memory** per GPU instance is listed in [this table](allocations_and_compute_scheduling.md#ratios-in-bundles).