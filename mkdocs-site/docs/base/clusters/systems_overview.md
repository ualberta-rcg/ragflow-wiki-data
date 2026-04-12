---
title: "Systems overview"
slug: "systems_overview"
lang: "base"

source_wiki_title: "Systems overview"
source_hash: "d41d8cd98f00b204e9800998ecf8427e"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:44:11.731788+00:00"

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

## Systems overview

The Vulcan cluster is a dedicated computing resource for researchers affiliated with the Alberta Machine Intelligence Institute (AMII), provided by the University of Alberta Research Computing Group (RCG). It is part of the Digital Research Alliance of Canada (the Alliance) national HPC infrastructure.

### Computing Nodes

Vulcan is composed of 10 nodes, each with:

*   2x Intel Xeon E5-2680v4 (Broadwell, 14 cores/CPU, 28 cores/node total)
*   256 GiB RAM
*   4x NVIDIA Tesla P100 GPUs (16 GiB memory each)
*   480 GB SSD (local scratch)

A total of 280 CPU cores, 2.5 TiB RAM, 40 GPUs, and 4.8 TB of local SSD are available on Vulcan.

All nodes are connected by an EDR InfiniBand fabric.

### Storage

Vulcan provides various storage options:

*   **Home directory (`$HOME`)**: 50 GB quota, backed by network file system (NFS), suitable for small files, scripts, and personal configurations. This storage is backed up.
*   **Project directory (`/project/$USER`)**: Shared directory with no quota, backed by NFS, suitable for larger datasets and project-specific files. This storage is *not* backed up.
*   **Scratch directory (`/scratch/$USER`)**: 480 GB per node, local SSD, suitable for temporary files, job-specific outputs, and high-performance I/O during job execution. This storage is *not* backed up and is *purged regularly*.

!!! warning
    Any data stored on `/scratch/$USER` that is older than 60 days *will be automatically purged without warning*. Please move any important data off of `/scratch/$USER` before it is purged.

### Software

Common scientific software is centrally installed and managed using the [Environment Modules](https://modules.readthedocs.io/en/latest/) system. Users can load different versions of compilers, libraries, and applications as needed.

!!! tip
    If you require specific software not currently available, please [contact the RCG team](https://www.ualberta.ca/research-computing/contact.html) to discuss installation options.

### Networking

Vulcan nodes are equipped with 1 Gigabit Ethernet (GbE) for management and access, and an EDR InfiniBand fabric for high-speed inter-node communication and storage access.

### Scheduling

Vulcan uses the [Slurm workload manager](https://slurm.schedmd.com/documentation.html) for resource allocation and job scheduling. Users submit jobs to Slurm, which then manages their execution on the available nodes.

For more information, see [Using Slurm on Vulcan](using-slurm-on-vulcan.md).

### Access

Access to Vulcan is granted to researchers affiliated with AMII. If you are eligible and require an account, please [contact the RCG team](https://www.ualberta.ca/research-computing/contact.html).

Access is primarily via SSH.

```bash
ssh <your_cc_username>@vulcan.computecanada.ca
```

### Supported research areas

Vulcan is optimized for machine learning and deep learning workloads, given its GPU-rich nodes. It also supports general-purpose scientific computing.

!!! note
    Researchers using Vulcan are expected to acknowledge the University of Alberta Research Computing Group and the Digital Research Alliance of Canada in any publications or presentations resulting from work performed on the cluster.