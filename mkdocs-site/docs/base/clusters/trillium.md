---
title: "Trillium"
slug: "trillium"
lang: "base"

source_wiki_title: "Trillium"
source_hash: "58b1fb804c958846418ed00c691f7779"
last_synced: "2026-09-27T01:10:57.242992+00:00"
last_processed: "2026-09-27T01:53:41.150908+00:00"

tags:
  []

keywords:
  - "Open OnDemand"
  - "10 million read IOPS"
  - "192-core node scheduling"
  - "Nvidia H100/H200/H200 GPUs"
  - "POSIX and S3 access protocols"
  - "nearline storage via HPSS"
  - "Trillium cluster"
  - "714 GB/s read bandwidth"
  - "400 Gbit/s / 800 Gbit/s InfiniBand network"
  - "29 PB NVMe‑backed storage"
  - "HPSS tape-based archive"
  - "29 PB NVMe-backed storage pool"
  - "16.7 PB raw flash capacity"
  - "SSH Keys and MFA"
  - "direct liquid cooling (PUE < 1.03)"

questions:
  - "What are the hardware specifications of Trillium’s CPU and GPU nodes, including CPU models, GPU types, core counts, and memory capacities?"
  - "How does Trillium achieve its high energy efficiency, and what cooling technology is employed?"
  - "What storage capacity and performance does Trillium’s VAST Data NVMe‑backed system offer, including bandwidth, IOPS, and supported access protocols?"
  - "What storage options does Trillium provide (e.g., HPSS tape archive, nearline, scratch, RAM‑disk) and how are they accessed?"
  - "How must users authenticate to log in to Trillium’s compute nodes, and what restrictions apply to internet access?"
  - "What are the quotas and usage policies for $HOME, $PROJECT, and scratch space on Trillium?"
  - "What is the effective capacity of the storage pool and how is it achieved through deduplication?"
  - "What are the read and write performance specifications, including bandwidth and IOPS, of the system?"
  - "Which access protocols and data service components (C‑Boxes and D‑Boxes) are supported by the storage system?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

: Availability: August 7, 2025
: Login nodes
    * CPU subcluster: **trillium.alliancecan.ca**
    * GPU subcluster: **trillium-gpu.alliancecan.ca**
: Globus collections
    * [alliancecan#trillium](https://app.globus.org/file-manager?origin_id=ad462f99-8436-42b4-adc6-3644e36c1b67) (file system)
    * [alliancecan#hpss](https://app.globus.org/file-manager?origin_id=c55ce750-19d6-4a42-9c30-6a58f06bec7a) (archive/nearline)
: Data transfer nodes (rsync, scp, sftp,...)
    * **tri-dm{1,2,3,4}.scinet.utoronto.ca**
: Automation nodes
    * CPU subcluster: **robot{1,2,3,4}.scinet.utoronto.ca**
    * GPU subcluster: **trig-robot1.scinet.utoronto.ca**
: Open OnDemand
    * [ondemand.scinet.utoronto.ca](https://ondemand.scinet.utoronto.ca) (includes JupyterLab)
: Portal
    * [my.scinet.utoronto.ca](https://my.scinet.utoronto.ca)

Trillium is a large parallel cluster built by Lenovo Canada and hosted by SciNet at the University of Toronto.

The [Trillium Quickstart](trillium_quickstart.md) has specific instructions for Trillium, where the user experience is similar to that on the other national clusters, but still slightly different.

Current users transitioning from Niagara are strongly encouraged to peruse the documentation on the [Transition from Niagara to Trillium](transition_from_niagara_to_trillium.md).

# Storage
Parallel storage: 29 petabytes, NVMe SSD based storage from VAST Data.

# High-performance network
* Nvidia “NDR” InfiniBand network
    * 400 Gbit/s network bandwidth for CPU nodes
    * 800 Gbit/s network bandwidth for GPU nodes
    * Fully non-blocking, meaning every node can talk to every other node at full bandwidth simultaneously.

# Node characteristics

| Login Node | nodes | cores | available memory | CPU | GPU |
| :--------- | :---- | :---- | :--------------- | :-- | :-- |
| trillium.alliancecan.ca | 1224 | 192 | 749G or 767000M | 2 x AMD EPYC 9655 (Zen 5) @ 2.6 GHz, 384MB cache L3 | |
| trillium-**gpu**.alliancecan.ca | 63 | 96 | 749G or 767000M | 1 x AMD EPYC 9654 (Zen 4) @ 2.4 GHz, 384MB cache L3 | 4 x NVidia H100 SXM (80 GB memory), connected via NVLink |
| trillium-**gpu**.alliancecan.ca | 1 | 96 | 1498G or 1534M | 2 x AMD EPYC 9455 (Zen 5) @ 3.15 GHz, 256MB cache L3 | 4 x NVidia H200 SXM (141GB memory), connected via NVLink |
| trillium-**gpu**.alliancecan.ca | 52 | 96 | 2000G or 2048000M | 2 x Intel 8558P @ 2.7 GHz, 260MB cache L3 | 8 x NVidia B200 SXM (180 GB memory), connected via NVLink |

!!! warning "B200s Not Yet Available"
    The B200 GPUs listed above are not yet available.

# Technical details

## Cooling and energy efficiency

Trillium is fully direct liquid cooled using warm water (35–40 °C input), resulting in:

* PUE below 1.03 (high energy efficiency)
* Use of closed-loop dry fluid coolers, avoiding evaporative towers and new water usage
* Heat reuse: Trillium supplies excess heat to nearby facilities to minimize climate impact

## Storage system

The VAST high-performance file system is comprised of a unified 29 PB NVMe-backed storage pool, with:

* 29 PB effective capacity (deduplicated via VAST)
* 16.7 PB raw flash capacity
* 714 GB/s read bandwidth, 275 GB/s write bandwidth
* 10 million read IOPS, 2 million write IOPS
* POSIX and S3 access protocols under a unified namespace
* 48 C-Boxes and 14 D-Boxes for data services

## Backup and archive storage

An additional 114 PB HPSS tape-based archive is available for nearline storage:

* Dual-copy archive across geographically separate libraries
* Used for both backup and archival purposes
* Backups are managed using Atempo backup software

# Site specifics

!!! note "Site Specifics"
    Do not assume that things work the same on Trillium as on the other clusters. While there is a large degree of conformity, Trillium was designed for large-scale computations and this has resulted in a few different design and policy decisions.

The specifics of Trillium are described only briefly below; please read the [Trillium Quickstart](trillium_quickstart.md) for details.

## Logging in

* Password access to the login nodes is disabled. You must use [SSH Keys](../getting-started/ssh_keys.md) and MFA.
* There are separate login and robot nodes for CPU and GPU subclusters.

## Internet access
* The internet cannot be reached from compute nodes.
* Interactive Apps on Open OnDemand, however, do have internet access.

## Home space

* You will have space for up to 100 GB or 1 million files in your `$HOME` directory.
* `$HOME` cannot be written to from compute jobs.
* Interactive Apps on Open OnDemand, however, do have write access to `HOME`.

## Project space

* You can find links to the project spaces to which you have access in the `$HOME/links` directory.
* Default accounts have access to a project space of 1 TB per group.
* It is not possible to request more project space on Trillium through RAS.
* `$PROJECT` cannot be written to from compute jobs.

## Scratch space

* Users have a nominal quota of 25TB, but are expected to clean up all unused data.
* There is no purging policy yet, but this is subject to change in the future.

## Nearline space

* The nearline storage on Trillium is not mounted on the nodes but needs to be accessed via jobs submitted to the [HPSS](https://docs.scinet.utoronto.ca/index.php/HPSS) SLURM partition, or via [Globus](../getting-started/globus.md).

## Local disk space

* Trillium nodes have no local storage.
* For certain workflows, using the RAM disk can be a possibility. To reflect this, the `$SLURM_TMPDIR` environment variable points to a folder on the RAM disk.

## Access through Open OnDemand (OOD)

* Instead of JupyterHub, Trillium has [Open OnDemand](../interactive/trillium_open_ondemand_quickstart.md). This supports a growing number of applications from your browser, such as JupyterLab, VS Code, RStudio, MATLAB, ParaView, the DDT debugger, as well as a terminal and job submissions.

## Job scheduling

* The resources in the CPU subcluster are scheduled by whole 192-core node.
* The resources in the GPU subcluster are scheduled by whole GPU (no "MIG"), or by whole node.
* For other scheduling specifics, please see the [Trillium Quickstart](trillium_quickstart.md).