---
title: "Vulcan/en"
slug: "vulcan"
lang: "en"

source_wiki_title: "Vulcan/en"
source_hash: "0bfd81915a7b6840a02a59038dfd0969"
last_synced: "2026-04-12T19:03:20.394416+00:00"
last_processed: "2026-04-12T19:14:33.173458+00:00"

tags:
  []

keywords:
  - "Artificial Intelligence"
  - "Vulcan cluster"
  - "Pan-Canadian AI Compute Environment"
  - "Storage system"
  - "Hardware specifications"

questions:
  - "What is the primary purpose of the Vulcan cluster and who is eligible to use it?"
  - "What specific steps must researchers and Principal Investigators take to request access and manage project memberships for Vulcan?"
  - "What are the hardware specifications and storage system configurations provided by the Vulcan cluster?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*   **Availability**: April 15, 2025
*   **Login node**: `vulcan.alliancecan.ca`
*   **Globus collection**: [Vulcan Globus v5](https://app.globus.org/file-manager?origin_id=97bda3da-a723-4dc0-ba7e-728f35183b43)
*   **System Status Page**: [https://status.alliancecan.ca/system/Vulcan](https://status.alliancecan.ca/system/Vulcan)
*   **Portal**: [https://portal.vulcan.alliancecan.ca](https://portal.vulcan.alliancecan.ca)

**Vulcan** is a cluster dedicated to the needs of the Canadian scientific Artificial Intelligence community. **Vulcan** is located at the [University of Alberta](https://www.ualberta.ca/) and is managed by the University of Alberta and [Amii](https://amii.ca/). It is named after the town [Vulcan, AB](https://en.wikipedia.org/wiki/Vulcan,_Alberta), located in southern Alberta.

This cluster is part of the Pan-Canadian AI Compute Environment (PAICE).

## Site-specific policies
Internet access is not generally available from the compute nodes. A globally available Squid proxy is enabled by default with certain domains whitelisted. Contact [technical support](../support/technical_support.md) if you are not able to connect to a domain and we will evaluate whether it belongs on the whitelist.

Maximum duration of jobs is 7 days.

Vulcan is currently open to all researchers doing research on AI or applying AI methods in their research.

## Access
To be able to log in to Vulcan, you must [request access in CCDB](https://ccdb.alliancecan.ca/me/access_services).

To be able to submit jobs, you must be a member of an AIP RAP.
If you are a PI and you do not already have one, apply for [General Access to PAICE Systems](https://ccdb.alliancecan.ca/paice/general_access_to_paice_systems).

If you are a PI and need to sponsor other researchers you will have to add them to your AIP RAP. Follow these steps to manage users:
*   Go to the "Resource Allocation Projects" table on the [CCDB home page](https://ccdb.alliancecan.ca).
*   Locate the RAPI of your AIP project (with the `aip-` prefix) and click on it to reach the RAP management page.
*   At the bottom of the RAP management page, click on "Manage RAP memberships."
*   Enter the CCRI of the user you want to add in the "Add Members" section.

## Vulcan hardware specifications

| Nodes | Model | CPU | Cores | System Memory | GPUs per node | Total GPUs |
| :---- | :---- | :-- | :---- | :------------ | :------------ | :--------- |
| 252 | Dell R760xa | 2 x Intel Xeon Gold 6448Y | 64 | 512 GB | 4 x NVIDIA L40s 48GB | 1008 |

## Storage system

**Vulcan**'s storage system uses a combination of NVMe flash and HDD storage running on the Dell PowerScale platform with a total usable capacity of approximately 5PB. Home, Scratch, and Project are on the same Dell PowerScale system.

| Storage Type | Description |
| :----------- | :---------- |
| **Home space** | *   Location of /home directories. <br> *   Each /home directory has a small fixed [quota](../storage-and-data/storage_and_file_management.md#filesystem-quotas-and-policies). <br> *   Not allocated via [RAS](https://alliancecan.ca/en/services/advanced-research-computing/accessing-resources/rapid-access-service) or [RAC](https://alliancecan.ca/en/services/advanced-research-computing/accessing-resources/resource-allocation-competition). Larger requests go to the /project space. <br> *   Has daily backup |
| **Scratch space** | *   For active or temporary (scratch) storage. <br> *   Not allocated. <br> *   Large fixed [quota](../storage-and-data/storage_and_file_management.md#filesystem-quotas-and-policies) per user. <br> *   Inactive data will be [purged](../storage-and-data/scratch_purging_policy.md). |
| **Project space** | *   Large adjustable [quota](../storage-and-data/storage_and_file_management.md#filesystem-quotas-and-policies) per project. <br> *   Has daily backup. |

## Network interconnects

Nodes are interconnected with 100Gbps Ethernet with RoCE (RDMA over Converged Ethernet) enabled.

## Scheduling
The **Vulcan** cluster uses the Slurm scheduler to run user workloads. The basic scheduling commands are similar to the other national systems.

## Software
*   Module-based software stack.
*   Both the standard Alliance software stack as well as cluster-specific software.