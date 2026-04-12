---
title: "Trillium/en"
slug: "trillium"
lang: "en"

source_wiki_title: "Trillium/en"
source_hash: "6694f56a33cea0d305ef7ac1618f2f5e"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:05:43.590162+00:00"

tags:
  []

keywords:
  - "SciNet"
  - "Trillium cluster"
  - "CPU and GPU nodes"
  - "VAST storage"
  - "High-performance network"

questions:
  - "Why is a significant portion of the old Niagara cluster being shut down during the installation and transition period of Trillium?"
  - "What are the key hardware specifications and network bandwidth differences between Trillium's CPU nodes and GPU nodes?"
  - "How does Trillium's direct liquid cooling system operate to ensure high energy efficiency and minimize environmental impact?"
  - "Why is a significant portion of the old Niagara cluster being shut down during the installation and transition period of Trillium?"
  - "What are the key hardware specifications and network bandwidth differences between Trillium's CPU nodes and GPU nodes?"
  - "How does Trillium's direct liquid cooling system operate to ensure high energy efficiency and minimize environmental impact?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

| Feature | Details |
| :------ | :------ |
| Availability | Aug/07 2025 |
| Login nodes | **CPU sub-cluster:** trillium.alliancecan.ca<br>**GPU sub-cluster:** trillium-gpu.alliancecan.ca |
| Globus collections | **Filesystem:** [alliancecan#trillium](https://app.globus.org/file-manager?origin_id=ad462f99-8436-42b4-adc6-3644e36c1b67)<br>**Archive/Nearline:** [alliancecan#hpss](https://app.globus.org/file-manager?origin_id=c55ce750-19d6-4a42-9c30-6a58f06bec7a) |
| Data transfer node (rsync, scp, sftp,...) | **tri-dm{1,2,3,4}.scinet.utoronto.ca** |
| Automation node | **robot{1,2,3,4}.scinet.utoronto.ca** |
| Open OnDemand | [ondemand.scinet.utoronto.ca](https://ondemand.scinet.utoronto.ca) (includes JupyterLab) |
| Portal | [my.scinet.utoronto.ca](https://my.scinet.utoronto.ca) |

Trillium is a large parallel cluster built by Lenovo Canada and hosted by SciNet at the University of Toronto.

The [Trillium Quickstart](trillium-quickstart.md) has specific instructions for Trillium, where the user experience is similar to that on the other national clusters, but still slightly different.

!!! note "Transitioning from Niagara"
    Current users transitioning from Niagara are strongly encouraged to peruse the documentation on the [Transition from Niagara to Trillium](transition-from-niagara-to-trillium.md).

## Installation and Transition
Due to limits on available power and cooling capacity there will be an interim period in which a significant portion of the old Niagara will be shut down in order to provide power for the new system's acceptance testing and transition. We'll update you when we have a better idea of Trillium's installation schedule.

## Storage
Parallel storage: 29 petabytes, NVMe SSD based storage from VAST Data.

## High-performance Network
*   Nvidia "NDR" Infiniband network
    *   400 Gbit/s network bandwidth for CPU nodes
    *   800 Gbit/s network bandwidth for GPU nodes
    *   Fully non-blocking, meaning every node can talk to every other node at full bandwidth simultaneously.

## Node Characteristics
| Login Node | nodes | cores | available memory | CPU | GPU |
| :--------- | :---- | :---- | :--------------- | :-- | :-- |
| trillium.alliancecan.ca | 1224 | 192 | 749G or 767000M | 2 x AMD EPYC 9655 (Zen 5) @ 2.6 GHz, 384MB cache L3 | |
| trillium-**gpu**.alliancecan.ca | 63 | 96 | 749G or 767000M | 1 x AMD EPYC 9654 (Zen 4) @ 2.4 GHz, 384MB cache L3 | 4 x NVidia H100 SXM (80 GB memory), connected via NVLink |

## Technical Details

### Cooling and Energy Efficiency

Trillium is fully direct liquid cooled using warm water (35–40 °C input), resulting in:

*   PUE below 1.03 (high energy efficiency)
*   Use of closed-loop dry fluid coolers, avoiding evaporative towers and new water usage
*   Heat reuse: Trillium supplies excess heat to nearby facilities to minimize climate impact

### Storage System

The VAST high-performance file system is comprised of a unified 29 PB NVMe-backed storage pool, with:

*   29 PB effective capacity (deduplicated via VAST)
*   16.7 PB raw flash capacity
*   714 GB/s read bandwidth, 275 GB/s write bandwidth
*   10 million read IOPS, 2 million write IOPS
*   POSIX and S3 access protocols under a unified namespace
*   48 C-Boxes and 14 D-Boxes for data services

### Backup and Archive Storage

An additional 114 PB HPSS tape-based archive is available for nearline storage:

*   Dual-copy archive across geographically separate libraries
*   Used for both backup and archival purposes
*   Backups are managed using Atempo backup software