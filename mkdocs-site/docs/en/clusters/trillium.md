---
title: "Trillium/en"
slug: "trillium"
lang: "en"

source_wiki_title: "Trillium/en"
source_hash: "78caef642d008ce00d2cad999284ba99"
last_synced: "2026-04-18T23:39:30.217451+00:00"
last_processed: "2026-04-19T01:07:35.510863+00:00"

tags:
  []

keywords:
  - "SciNet"
  - "CPU and GPU subclusters"
  - "Job scheduling"
  - "Compute nodes"
  - "SSH Keys"
  - "MFA"
  - "parallel cluster"
  - "Internet access"
  - "Scratch space"
  - "Trillium"
  - "Home space"
  - "VAST storage"
  - "Open OnDemand"
  - "Project space"

questions:
  - "What are the hardware specifications and network capabilities of Trillium's CPU and GPU nodes?"
  - "How is Trillium's storage infrastructure organized in terms of high-performance parallel storage and archival backup?"
  - "What are the specific login requirements and usage restrictions for users accessing the Trillium cluster?"
  - "What are the different types of storage spaces available on Trillium, and what are their specific access rules and quotas?"
  - "How can users access interactive applications and tools on Trillium through their web browser?"
  - "How are computing resources allocated and scheduled within the CPU and GPU subclusters on Trillium?"
  - "What authentication methods must be used to access the login nodes?"
  - "How does internet connectivity differ between compute nodes and Interactive Apps on OnDemand?"
  - "What are the specific storage capacity and file count limits for a user's home directory?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! note "Availability"
    August 07, 2025

| Category | Detail |
| :------- | :----- |
| Login nodes | * CPU subcluster: **trillium.alliancecan.ca**<br/>* GPU subcluster: **trillium-gpu.alliancecan.ca** |
| Globus collections | **[alliancecan#trillium](https://app.globus.org/file-manager?origin_id=ad462f99-8436-42b4-adc6-3644e36c1b67)** (file system)<br/>**[alliancecan#hpss](https://app.globus.org/file-manager?origin_id=c55ce750-19d6-4a42-9c30-6a58f06bec7a)** (archive/nearline) |
| Data transfer nodes | tri-dm{1,2,3,4}.scinet.utoronto.ca |
| Automation nodes | * CPU subcluster: robot{1,2,3,4}.scinet.utoronto.ca<br/>* GPU subcluster: trig-robot1.scinet.utoronto.ca |
| Open OnDemand | [ondemand.scinet.utoronto.ca](https://ondemand.scinet.utoronto.ca) (includes JupyterLab) |
| Portal | [my.scinet.utoronto.ca](https://my.scinet.utoronto.ca) |

Trillium is a large parallel cluster built by Lenovo Canada and hosted by SciNet at the University of Toronto.

The [Trillium Quickstart](trillium_quickstart.md) has specific instructions for Trillium, where the user experience is similar to that on the other national clusters, but still slightly different.

Current users transitioning from Niagara are strongly encouraged to peruse the documentation on the [Transition from Niagara to Trillium](transition_from_niagara_to_trillium.md).

## Storage

Parallel storage: 29 petabytes, NVMe SSD based storage from VAST Data.

## High-performance network

*   *Nvidia “NDR” Infiniband network*
    *   400 Gbit/s network bandwidth for CPU nodes
    *   800 Gbit/s network bandwidth for GPU nodes
    *   Fully non-blocking, meaning every node can talk to every other node at full bandwidth simultaneously.

## Node characteristics

| Login Node | nodes | cores | available memory | CPU | GPU |
| :--------- | :---- | :---- | :--------------- | :-- | :-- |
| trillium.alliancecan.ca | 1224 | 192 | 749G or 767000M | 2 x AMD EPYC 9655 (Zen 5) @ 2.6 GHz, 384MB cache L3 | |
| trillium-gpu.alliancecan.ca | 63 | 96 | 749G or 767000M | 1 x AMD EPYC 9654 (Zen 4) @ 2.4 GHz, 384MB cache L3 | 4 x NVidia H100 SXM (80 GB memory), connected via NVLink |

## Technical details

### Cooling and energy efficiency

Trillium is fully direct liquid cooled using warm water (35–40 °C input), resulting in:

*   PUE below 1.03 (high energy efficiency)
*   Use of closed-loop dry fluid coolers, avoiding evaporative towers and new water usage
*   Heat reuse: Trillium supplies excess heat to nearby facilities to minimize climate impact

### Storage system

The VAST high-performance file system is comprised of a unified 29 PB NVMe-backed storage pool, with:

*   29 PB effective capacity (deduplicated via VAST)
*   16.7 PB raw flash capacity
*   714 GB/s read bandwidth, 275 GB/s write bandwidth
*   10 million read IOPS, 2 million write IOPS
*   POSIX and S3 access protocols under a unified namespace
*   48 C-Boxes and 14 D-Boxes for data services

### Backup and archive storage

An additional 114 PB HPSS tape-based archive is available for nearline storage:

*   Dual-copy archive across geographically separate libraries
*   Used for both backup and archival purposes
*   Backups are managed using Atempo backup software

## Site specifics

!!! note
    Do not assume that things work the same on Trillium as on the other clusters. While there is a large degree of conformity, Trillium was designed for large-scale computations and this has resulted in a few different design and policy decisions.

    The specifics of Trillium are described only briefly below; please read the [Trillium Quickstart](trillium_quickstart.md) for details.

### Logging in

*   Password access to the login nodes is disabled. You must use [SSH Keys](../getting-started/ssh_keys.md) and MFA.
*   There are separate login and robot nodes for CPU and GPU subclusters.

### Internet access

*   The internet cannot be reached from compute nodes.
*   Interactive Apps on OnDemand, however, do have internet access.

### Home space

*   You will have space for up to 100 GB or 1 million files in your `$HOME` directory.
*   `$HOME` cannot be written to from compute jobs.
*   Interactive Apps on OnDemand, however, do have write access to `HOME`.

### Project space

*   You can find links to the project spaces to which you have access in the `$HOME/links` directory.
*   Default accounts have access to a project space of 1 TB per group.
*   It is not possible to request more project space on Trillium through RAS.
*   `$PROJECT` cannot be written to from compute jobs.

### Scratch space

*   Users have a nominal quota of 25 TB, but are expected to clean up all unused data.
*   There is no purging policy yet, but this is subject to change in the future.

### Nearline space

*   The nearline storage on Trillium is not mounted on the nodes but needs to be accessed via jobs submitted to the [HPSS](https://docs.scinet.utoronto.ca/index.php/HPSS) SLURM partition, or via [Globus](../getting-started/globus.md).

### Local disk space

*   Trillium nodes have no local storage.
*   For certain workflows, using the RAM disk can be a possibility. To reflect this, the `$SLURM_TMPDIR` environment variable points to a folder on the RAM disk.

### Access through Open OnDemand (OOD)

*   Instead of JupyterHub, Trillium has [OpenOnDemand](../interactive/trillium_open_ondemand_quickstart.md). This supports a growing number of applications from your browser, such as JupyterLab, VS Code, RStudio, MATLAB, ParaView, the DDT debugger, as well as a terminal and job submissions.

### Job scheduling

*   The resources in the CPU subcluster are scheduled by whole 192-core node.
*   The resources in the GPU subcluster are scheduled by whole GPU (no "MIG"), or by whole node.
*   For other scheduling specifics, please see the [Trillium Quickstart](trillium_quickstart.md).