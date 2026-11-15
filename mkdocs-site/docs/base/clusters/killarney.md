---
title: "Killarney"
slug: "killarney"
lang: "base"

source_wiki_title: "Killarney"
source_hash: "6ae9629ee2c792e7a5710942a1bd69d8"
last_synced: "2026-11-15T02:27:25.182546+00:00"
last_processed: "2026-11-15T03:36:04.552169+00:00"

tags:
  []

keywords:
  - "Scratch space"
  - "temporary storage"
  - "HDR 200"
  - "module-based software stack"
  - "Project space"
  - "quota per user"
  - "VastData NVMe storage"
  - "Infiniband HDR100"
  - "NVIDIA L40S GPUs"
  - "AIP‑type RAP access"
  - "Killarney cluster"
  - "Slurm scheduler"
  - "Pan-Canadian AI Compute Environment (PAICE)"
  - "daily backup"

questions:
  - "What are the hardware specifications and GPU allocations for the Standard Compute and Performance Compute tiers on the Killarney cluster?"
  - "How does a Principal Investigator obtain an AIP‑type RAP and grant access to researchers for using Killarney?"
  - "What storage spaces (home, scratch, project) does Killarney offer, and what are the quota, backup, and purging policies for each?"
  - "What are the differences in network interconnects and aggregate throughput between the Standard Compute nodes and the Performance Compute nodes?"
  - "Which job scheduler does the Killarney cluster employ for running user workloads?"
  - "How is the software environment organized on the cluster, and what types of software stacks are provided?"
  - "What are the key characteristics and policies of the Scratch space, including its quota and data purging?"
  - "How does Project space differ from Scratch space in terms of quota flexibility and backup procedures?"
  - "What type of storage is provided for each space, and how are they intended to be used (active/temporary vs. project-related data)?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

| Detail | Value |
| :----- | :---- |
| Availability | June 9, 2025 |
| Login node | **killarney.alliancecan.ca** |
| Open OnDemand | <https://ondemand.killarney.vectorinstitute.ai> |
| Globus collection | TBA |
| System Status Page | <https://status.alliancecan.ca/system/Killarney> |

**Killarney** is a cluster dedicated to the needs of the Canadian scientific Artificial Intelligence community. **Killarney** is located at the [University of Toronto](https://www.utoronto.ca/) and is managed by the [Vector Institute](https://vectorinstitute.ai/) and [SciNet](https://www.scinethpc.ca/). It is named after the [Killarney Ontario Provincial Park](https://www.ontarioparks.ca/park/killarney), located near Georgian Bay.

This cluster is part of the Pan-Canadian AI Compute Environment (PAICE).

## Site-specific policies
Killarney is currently open to Vector-affiliated PIs with CCAI Chairs, as well as researchers within an AI program at a Canadian university, or applying AI methods for their research.

Killarney remote file systems (`/home`, `/scratch`, etc.) are mounted using NFS v3, which does not support ACLs; as such, commands such as `setfacl` are not supported. If you need to share data with users outside of your group, please email `ops-help@vectorinstitute.ai` requesting a shared directory be created.

## Access
Principal Investigators must first be granted an AIP-type RAP (prefix `aip-`) by their AI Institution, or by applying for [General Access to PAICE Systems](https://ccdb.alliancecan.ca/paice/general_access_to_paice_systems).

To sponsor researchers in their AIP RAP, the PI must:
1. In the *Resource Allocation Projects* table on the CCDB home page, click on the RAPI project to display the RAP management page.
2. At the top of the RAP management page, click on *Manage RAP memberships*.
3. In the *Add Members* section, enter the CCRI of the users you want to add.

Once members are registered by the PI, they must [request access in the CCDB](https://ccdb.alliancecan.ca/me/access_services) and have at least [one SSH key in CCDB](../getting-started/ssh_keys.md).

To ensure integrity and security, **Vector enforces geo-blocking** on Killarney as one of its cybersecurity controls. Vector restricts access to and from countries identified in the [Government of Canada's Cyber Threat Assessment](https://www.cyber.gc.ca/en/guidance/national-cyber-threat-assessment-2025-2026).

## Killarney hardware specifications

| Performance Tier | Nodes | Model | CPU | Cores | System Memory | Storage | GPUs per node | Total GPUs |
| :--------------- | :---- | :---- | :-- | :---- | :------------ | :------ | :------------ | :--------- |
| Standard Compute | 168 | Dell 750xa | 2 x Intel Xeon Gold 6338 | 64 | 512 GB | 350 GB SSD | 4 x NVIDIA L40S 48GB | 672 |
| Performance Compute | 10 | Dell XE9680 | 2 x Intel Xeon Gold 6442Y | 48 | 2048 GB | 800 GB NVMe | 8 x NVIDIA H100 SXM 80GB | 80 |

## Storage system

**Killarney**'s storage system is an all-NVMe VastData platform with a total usable capacity of 1.7 PB.

| Storage Type      | Description                                                                                                                   |
| :---------------- | :---------------------------------------------------------------------------------------------------------------------------- |
| **Home space**    | * Location of `/home` directories.<br>* Each `/home` directory has a small fixed [quota](../storage-and-data/storage_and_file_management.md#filesystem-quotas-and-policies).<br>* Larger requests go to the `/project` space.<br>* Has daily backup. |
| **Scratch space** | * For active or temporary (scratch) storage.<br>* Large fixed [quota](../storage-and-data/storage_and_file_management.md#filesystem-quotas-and-policies) per user.<br>* Inactive data will be [purged](../storage-and-data/scratch_purging_policy.md). |
| **Project space** | * Large adjustable [quota](../storage-and-data/storage_and_file_management.md#filesystem-quotas-and-policies) per project.<br>* Has daily backup. |

## Network interconnects

Standard Compute nodes are interconnected with Infiniband HDR100 for 100 Gbps throughput, while Performance Compute nodes are connected with 2 x HDR 200 for 400 Gbps aggregate throughput.

## Scheduling
The **Killarney** cluster uses the Slurm scheduler to run user workloads. The basic scheduling commands are similar to the other national systems.

## Software
* Module-based software stack.
* Both the standard Alliance software stack as well as cluster-specific software.