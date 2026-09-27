---
title: "Rocky"
slug: "rocky"
lang: "base"

source_wiki_title: "Rocky"
source_hash: "fa1760a5529896f51215b388183b7834"
last_synced: "2026-09-27T01:10:57.242992+00:00"
last_processed: "2026-09-27T01:55:24.711070+00:00"

tags:
  []

keywords:
  - "immersion‑cooled nodes"
  - "CephFS storage 1.72 PB"
  - "Rocky GPU cluster"
  - "NVIDIA H200 GPUs"
  - "Slurm scheduler"

questions:
  - "How can a user request access to Rocky and what is the current onboarding status of the system?"
  - "What are the key hardware specifications of Rocky, including CPU, memory, GPU model, and network interconnects?"
  - "What storage options does Rocky provide, and how should users handle data between node‑local $SLURM_TMPDIR and the shared CephFS file systems?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

| Key | Value |
| :-- | :---- |
| Availability | **Onboarding in progress** |
| Login node | **rocky.alliancecan.ca** |
| Globus collection | [Rocky Globus v5](https://app.globus.org/file-manager?origin_id=eae9df97-574e-40fa-9e32-015f01dd841e) |
| System Status Page | [Rocky status page](https://status.alliancecan.ca/system/Rocky) |
| Portal | **To be announced** |
| Open OnDemand | **To be announced** |

Rocky is a GPU cluster dedicated to the needs of the Canadian scientific Artificial Intelligence community. Rocky is located in Calgary, Alberta, hosted on Denvr infrastructure, and managed by Amii (Alberta Machine Intelligence Institute). It is currently being onboarded to the Digital Research Alliance of Canada.

## Site-specific policies

Internet access is not generally available from the compute nodes. If you cannot connect to a domain you need, contact [technical support](../support/technical_support.md) and we evaluate the request.

Maximum duration of jobs is 7 days.

## Access

To log in to Rocky, request access in [CCDB](https://ccdb.alliancecan.ca).

## Rocky hardware specifications

Rocky is being deployed in two immersion-cooled tanks of 13 nodes each.

| Nodes | Model | CPU | Cores | System Memory | GPUs per node | Total GPUs |
| :---- | :---- | :-- | :---- | :------------ | :------------ | :--------- |
| 26 (2 tanks × 13) | Dell PowerEdge XE9680 (immersion-cooled) | 2 x Intel Xeon Platinum 8570 (2.1 GHz) | 112 | 2 TB DDR5-5600 | 8 x NVIDIA H200 SXM 141GB | 208 |

Within each node, NVLink fully connects the 8 GPUs through NVSwitch.

Each node also has 7 x 3.84 TB NVMe SSDs for fast node-local job storage. See [Node-local storage](#node-local-storage).

## Storage

Rocky's storage is a Ceph cluster, with user file systems served by CephFS and a total usable capacity of approximately 1.72 PB. Home, Scratch, and Project are on the same CephFS file system.

| | |
| :--- | :--- |
| **Home space** | * Location of `/home` directories.<br />* Each `/home` directory has a small fixed quota.<br />* Not allocated via RAS or RAC. Larger requests go to the `/project` space.<br />* Has daily backup. |
| **Scratch space** | * For active or temporary (scratch) storage.<br />* Not allocated.<br />* Large fixed quota per user.<br />* Inactive data is purged after 60 days. |
| **Project space** | * Large adjustable quota per project.<br />* Has daily backup. |

### Node-local storage

Each job receives a private temporary directory, `$SLURM_TMPDIR`, on the compute node's local NVMe drives. It is much faster than the shared file systems. Copy your input data there at the start of a job, and copy your results back to `/scratch` or `/project` before the job ends.

!!! warning
    **`$SLURM_TMPDIR` is not backed up and has no redundancy.** Its contents are deleted when the job ends, and a single drive failure can destroy them during the job.

## Network interconnects

Each node has a dedicated GPU network of 8 x 400 Gbps Ethernet ports (one NVIDIA ConnectX-7 per GPU) with RoCE v2 (RDMA over Converged Ethernet) enabled. General networking and storage traffic use an NVIDIA BlueField-3 dual-port 200 Gbps Ethernet adapter.

## Scheduling

The Rocky cluster uses the [Slurm scheduler](../running-jobs/running_jobs.md) to run user workloads. The basic scheduling commands are similar to those on the other national clusters.

You do not need to choose a partition. Request a walltime with `--time`, and Slurm places your job in the partition that matches that walltime. Jobs submitted without a walltime default to 1 hour. An interactive partition allows jobs of up to 8 hours.

To request GPUs, specify the type `h200`, for example:

```bash
#SBATCH --gres=gpu:h200:1
```

A job only sees the GPUs it requested.

## Software

*   Module-based software stack.
*   The standard Alliance software stack is available through CVMFS.