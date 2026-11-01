---
title: "Killarney"
slug: "killarney"
lang: "base"

source_wiki_title: "Killarney"
source_hash: "a52a668bfa4f47c2056a65b16e5ad291"
last_synced: "2026-11-01T01:58:40.824100+00:00"
last_processed: "2026-11-01T02:31:29.642085+00:00"

tags:
  []

keywords:
  - "quota"
  - "Killarney cluster"
  - "HDR 200"
  - "AIP RAP access"
  - "Slurm scheduler"
  - "Project space"
  - "Scratch space"
  - "PAICE"
  - "purging policy"
  - "NVMe VastData storage"
  - "daily backup"
  - "module-based software stack"
  - "Canadian AI community"
  - "Infiniband HDR100"

questions:
  - "What are the hardware specifications and GPU resources available on the Killarney cluster?"
  - "Who is eligible to access Killarney and what steps must a Principal Investigator follow to grant access to their researchers?"
  - "How is storage organized on Killarney, and what are the policies regarding quotas, backups, and data purging?"
  - "What network interconnects are used for standard and performance compute nodes in the Killarney cluster, and what are their respective throughput capacities?"
  - "Which scheduler does the Killarney cluster employ for running user workloads, and how does its basic command set compare to other national systems?"
  - "How is the software environment organized on the Killarney cluster, and what software stacks are provided to users?"
  - "What is the intended use of scratch space and how is its storage quota defined for each user?"
  - "How does project space differ from scratch space regarding quota adjustability and allocation of larger requests?"
  - "What policies apply to inactive data in scratch space and how are daily backups handled?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

| Key                  | Value                                                        |
| :------------------- | :----------------------------------------------------------- |
| Availability         | June 9, 2025                                                 |
| Login node           | **killarney.alliancecan.ca**                                 |
| Open OnDemand        | [Open OnDemand](https://ondemand.killarney.vectorinstitute.ai) |
| Globus collection    | TBA                                                          |
| System Status Page   | [System Status Page](https://status.alliancecan.ca/system/Killarney) |

**Killarney** is a cluster dedicated to the needs of the Canadian scientific Artificial Intelligence community. **Killarney** is located at the [University of Toronto](https://www.utoronto.ca/) and is managed by the [Vector Institute](https://vectorinstitute.ai/) and [SciNet](https://www.scinethpc.ca/). It is named after the [Killarney Ontario Provincial Park](https://www.ontarioparks.ca/park/killarney), located near Georgian Bay.

This cluster is part of the Pan-Canadian AI Compute Environment (PAICE).

## Site-specific policies
Killarney is currently open to Vector affiliated PIs with CCAI Chairs, as well as researchers within an AI program at a Canadian university, or applying AI methods for their research.

!!! note
    Killarney remote filesystems (`/home`, `/scratch`, etc.) are mounted using NFS v3, which does not support ACLs; as such, commands such as `setfacl` are not supported. If you need to share data with users outside of your group, please email ops-help@vectorinstitute.ai requesting a shared directory be created.

## Access
To access Killarney, each researcher must [request access in the CCDB](https://ccdb.alliancecan.ca/me/access_services), and ensure that they have at least [one SSH key in CCDB](../getting-started/ssh_keys.md).

Principal Investigators must be granted an AIP-type RAP (prefix `aip-`) by their AI Institution, or by applying for [General Access to PAICE Systems](https://ccdb.alliancecan.ca/paice/general_access_to_paice_systems).

For the PI to sponsor researchers in their AIP RAP, the PI must:
*   Go to the "Resource Allocation Projects" table on the CCDB Home page.
*   Locate the RAPI of your AIP project (with the `aip-` prefix) and click on it to reach the RAP management page.
*   At the bottom of the RAP management page, click on "Manage RAP memberships."
*   Enter the CCRI of the user you want to add in the "Add Members" section.

!!! warning "Geo-blocking Policy"
    To ensure the integrity and security of this resource, **Vector enforces geo-blocking** on Killarney as one of its cyber-security controls. Vector restricts access to and from countries identified in the [Government of Canada's Cyber Threat Assessment](https://www.cyber.gc.ca/en/guidance/national-cyber-threat-assessment-2025-2026).

## Killarney hardware specifications

| Performance Tier    | Nodes | Model        | CPU                      | Cores | System Memory | Storage     | GPUs per node          | Total GPUs |
| :------------------ | :---- | :----------- | :----------------------- | :---- | :------------ | :---------- | :--------------------- | :--------- |
| Standard Compute    | 168   | Dell 750xa   | 2 x Intel Xeon Gold 6338 | 64    | 512 GB        | 350 GB SSD  | 4 x NVIDIA L40S 48GB   | 672        |
| Performance Compute | 10    | Dell XE9680  | 2 x Intel Xeon Gold 6442Y| 48    | 2048 GB       | 800 GB NVMe | 8 x NVIDIA H100 SXM 80GB | 80         |

## Storage system

**Killarney**'s storage system is an all-NVME VastData platform with a total usable capacity of 1.7PB.

### Home space
*   Location of `/home` directories.
*   Each `/home` directory has a small fixed [quota](../storage-and-data/storage_and_file_management.md#filesystem-quotas-and-policies).
*   Larger requests go to the `/project` space.
*   Has daily backup.

### Scratch space
*   For active or temporary (scratch) storage.
*   Large fixed [quota](../storage-and-data/storage_and_file_management.md#filesystem-quotas-and-policies) per user.
*   Inactive data will be [purged](../storage-and-data/scratch_purging_policy.md).

### Project space
*   Large adjustable [quota](../storage-and-data/storage_and_file_management.md#filesystem-quotas-and-policies) per project.
*   Has daily backup.

## Network interconnects

Standard Compute nodes are interconnected with Infiniband HDR100 for 100Gbps throughput, while Performance Compute nodes are connected with 2 x HDR 200 for 400Gbps aggregate throughput.

## Scheduling
The **Killarney** cluster uses the Slurm scheduler to run user workloads. The basic scheduling commands are similar to the other national systems.

## Software
*   Module-based software stack.
*   Both the standard Alliance software stack as well as cluster-specific software.