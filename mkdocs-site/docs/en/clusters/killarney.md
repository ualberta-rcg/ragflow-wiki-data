---
title: "Killarney/en"
slug: "killarney"
lang: "en"

source_wiki_title: "Killarney/en"
source_hash: "d3e036562223e80fb23b713efba240c0"
last_synced: "2026-09-13T00:40:43.713374+00:00"
last_processed: "2026-09-13T01:20:47.143212+00:00"

tags:
  []

keywords:
  - "daily backup"
  - "Module-based software stack"
  - "standard Alliance software stack"
  - "Vector Institute"
  - "cluster-specific software"
  - "Slurm scheduler"
  - "Alliance"
  - "100Gbps throughput"
  - "Killarney cluster"
  - "NVMe VastData storage"
  - "HDR 200"
  - "Infiniband HDR100"
  - "PAICE"
  - "software stack"

questions:
  - "What hardware configurations and GPU resources does the Killarney cluster provide for standard and performance compute nodes?"
  - "Who is eligible to use Killarney, and what are the required steps for a Principal Investigator to grant access to their researchers?"
  - "What storage spaces are available on Killarney, and how are quotas, backups, and data purging managed for each space?"
  - "What is a module‑based software stack and how is it structured?"
  - "How does the standard Alliance software stack differ from the cluster‑specific software?"
  - "What advantages does combining the standard Alliance stack with cluster‑specific software provide?"
  - "What are the network interconnect specifications for standard and performance compute nodes in the Killarney cluster?"
  - "How does the Killarney cluster manage user workload scheduling with Slurm?"
  - "Does the Killarney cluster provide daily backups and enforce quotas on a per‑project basis?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

| Availability | June 9, 2025 |
| Login node | **killarney.alliancecan.ca** |
| Open OnDemand | [https://ondemand.killarney.vectorinstitute.ai](https://ondemand.killarney.vectorinstitute.ai) |
| Globus collection | TBA |
| System Status Page | [https://status.alliancecan.ca/system/Killarney](https://status.alliancecan.ca/system/Killarney) |

**Killarney** is a cluster dedicated to the needs of the Canadian scientific Artificial Intelligence community. **Killarney** is located at the [University of Toronto](https://www.utoronto.ca/) and is managed by the [Vector Institute](https://vectorinstitute.ai/) and [SciNet](https://www.scinethpc.ca/). It is named after the [Killarney Ontario Provincial Park](https://www.ontarioparks.ca/park/killarney), located near Georgian Bay.

This cluster is part of the Pan-Canadian AI Compute Environment (PAICE).

## Site-specific policies
Killarney is currently open to Vector affiliated PIs with CCAI Chairs as well as researchers within an AI program at a Canadian university or applying AI methods for their research.

Killarney remote filesystems (/home, /scratch, etc) are mounted using NFS v3, which does not support ACLs; as such, commands such as `setfacl` are not supported. If you need to share data with users outside of your group, please email ops-help@vectorinstitute.ai requesting a shared directory be created.

## Access
To access Killarney, each researcher must [request access in the CCDB](https://ccdb.alliancecan.ca/me/access_services), and ensure that they have at least [one SSH key in CCDB](../getting-started/ssh_keys.md).

Principal Investigators must be granted an AIP-type RAP (prefix `aip-` ) by their AI Institution,
or by applying for [General Access to PAICE Systems](https://ccdb.alliancecan.ca/paice/general_access_to_paice_systems).

For the PI to sponsor researchers in their AIP RAP, the PI must:
* Go to the "Resource Allocation Projects" table on the CCDB Home page.
* Locate the RAPI of your AIP project (with the aip- prefix) and click on it to reach the RAP management page.
* At the bottom of the RAP management page, click on "Manage RAP memberships."
* Enter the CCRI of the user you want to add in the "Add Members" section.

To ensure the integrity and security of this resource, **Vector enforces geo-blocking** on Killarney as one of its cyber-security controls. Vector restricts access to and from countries identified in the [Government of Canada's Cyber Threat Assessment](https://www.cyber.gc.ca/en/guidance/national-cyber-threat-assessment-2025-2026).

## Killarney hardware specifications

| Performance Tier | Nodes | Model | CPU | Cores | System Memory | Storage | GPUs per node | Total GPUs |
|---|---|---|---|---|---|---|---|---|
| Standard Compute | 168 | Dell 750xa | 2 x Intel Xeon Gold 6338 | 64 | 512 GB | 350 GB SSD | 4 x NVIDIA L40S 48GB | 672 |
| Performance Compute | 10 | Dell XE9680 | 2 x Intel Xeon Gold 6442Y | 48 | 2048 GB | 800 GB NVMe | 8 x NVIDIA H100 SXM 80GB | 80 |

## Storage system

**Killarney**'s storage system is an all-NVME VastData platform with a total usable capacity of 1.7PB.

| Storage Space | Details |
|---|---|
| **Home space** | * Location of /home directories. <br> * Each /home directory has a small fixed [quota](../storage-and-data/storage_and_file_management.md#filesystem-quotas-and-policies). <br> * Larger requests go to the /project space. <br> * Has daily backup |
| **Scratch space** | * For active or temporary (scratch) storage. <br> * Large fixed [quota](../storage-and-data/storage_and_file_management.md#filesystem-quotas-and-policies) per user. <br> * Inactive data will be [purged](../storage-and-data/scratch_purging_policy.md). |
| **Project space** | * Large adjustable [quota](../storage-and-data/storage_and_file_management.md#filesystem-quotas-and-policies) per project. <br> * Has daily backup. |

## Network interconnects

Standard Compute nodes are interconnected with Infiniband HDR100 for 100Gbps throughput, while Performance Compute nodes are connected with 2 x HDR 200 for 400Gbps aggregate throughput.

## Scheduling
The **Killarney** cluster uses the Slurm scheduler to run user workloads. The basic scheduling commands are similar to the other national systems.

## Software
* Module-based software stack.
* Both the standard Alliance software stack as well as cluster-specific software.