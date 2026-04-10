---
title: "Trillium/en"
slug: "trillium"
lang: "en"

source_wiki_title: "Trillium/en"
source_hash: "6694f56a33cea0d305ef7ac1618f2f5e"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T12:02:36.936852+00:00"

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

The Trillium cluster, located at SciNet in the University of Toronto, is a large parallel computing system built by Lenovo Canada. It is part of the Digital Research Alliance of Canada (the Alliance) national HPC infrastructure.

### Key Features:

*   **Processor:** AMD EPYC (Zen 4, Zen 5)
*   **Performance (Theoretical Peak):** 60 PFlop/s
*   **Memory:** 445 TB DDR5
*   **Storage:** 29 PB NVMe-based storage (VAST Data)
*   **Interconnect:** Nvidia NDR Infiniband
*   **Access:** Secure Shell (SSH), Open OnDemand, Globus
*   **Operating System:** Red Hat Enterprise Linux (RHEL) 8

Refer to the [Trillium Quickstart](trillium-quickstart.md) for specific instructions, as the user experience, while similar to other national clusters, has some differences.

Users transitioning from Niagara are strongly encouraged to review the documentation on [Transition from Niagara to Trillium](transition-from-niagara-to-trillium.md).

| Feature               | Details                                                                                                                                                                                                                                                                                                                                           |
| :-------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Availability:         | Aug/07 2025                                                                                                                                                                                                                                                                                                                                       |
| Login nodes:          | CPU sub-cluster Login node: **trillium.alliancecan.ca**<br><br>GPU sub-cluster Login node: **trillium-gpu.alliancecan.ca**                                                                                                                                                                                                                           |
| Globus collections:   | [alliancecan#trillium](https://app.globus.org/file-manager?origin_id=ad462f99-8436-42b4-adc6-3644e36c1b67) (file system)<br>[alliancecan#hpss](https://app.globus.org/file-manager?origin_id=c55ce750-19d6-4a42-9c30-6a58f06bec7a) (archive/nearline)                                                                                              |
| Data transfer node    | **tri-dm{1,2,3,4}.scinet.utoronto.ca** (rsync, scp, sftp,...)                                                                                                                                                                                                                                                                                       |
| Automation node:      | **robot{1,2,3,4}.scinet.utoronto.ca**                                                                                                                                                                                                                                                                                                             |
| Open OnDemand:        | [ondemand.scinet.utoronto.ca](https://ondemand.scinet.utoronto.ca) (includes JupyterLab)                                                                                                                                                                                                                                                          |
| Portal:               | [my.scinet.utoronto.ca](https://my.scinet.utoronto.ca)                                                                                                                                                                                                                                                                                            |

## Installation and transition

Due to limits on available power and cooling capacity there will be an interim period in which a significant portion of the old Niagara will be shut down in order to provide power for the new system's acceptance testing and transition. We'll update you when we have a better idea of Trillium's installation schedule.

## Storage

Parallel storage: 29 petabytes, NVMe SSD based storage from VAST Data.

## High-performance network

*   Nvidia “NDR” Infiniband network
    *   400 Gbit/s network bandwidth for CPU nodes
    *   800 Gbit/s network bandwidth for GPU nodes
    *   Fully non-blocking, meaning every node can talk to every other node at full bandwidth simultaneously.

## Node characteristics

| Login Node                | Nodes | Cores | Available memory  | CPU                                           | GPU                                                              |
| :------------------------ | :---- | :---- | :---------------- | :-------------------------------------------- | :--------------------------------------------------------------- |
| trillium.alliancecan.ca   | 1224  | 192   | 749G or 767000M   | 2 x AMD EPYC 9655 (Zen 5) @ 2.6 GHz, 384MB cache L3 |                                                                  |
| trillium-**gpu**.alliancecan.ca | 63    | 96    | 749G or 767000M   | 1 x AMD EPYC 9654 (Zen 4) @ 2.4 GHz, 384MB cache L3 | 4 x NVidia H100 SXM (80 GB memory), connected via NVLink |

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