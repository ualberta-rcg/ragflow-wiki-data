---
title: "Vulcan/en"
tags:
  []

keywords:
  []
---

{| class="wikitable"
|-
| Availability: April 15, 2025
|-
| Login node: <b>vulcan.alliancecan.ca</b>
|-
| Globus collection: [Vulcan Globus v5](https://app.globus.org/file-manager?origin_id=97bda3da-a723-4dc0-ba7e-728f35183b43)
|-
| System Status Page: https://status.alliancecan.ca/system/Vulcan
|-
| Portal: https://portal.vulcan.alliancecan.ca
|}

<b>Vulcan</b> is a cluster dedicated to the needs of the Canadian scientific Artificial Intelligence community. <b>Vulcan</b> is located at the [University of Alberta](https://www.ualberta.ca/) and is managed by the University of Alberta and [Amii](https://amii.ca/). It is named after the town [Vulcan, AB](https://en.wikipedia.org/wiki/Vulcan,_Alberta), located in southern Alberta.

This cluster is part of the Pan-Canadian AI Compute Environment (PAICE).

## Site-specific policies
Internet access is not generally available from the compute nodes. A globally available Squid proxy is enabled by default with certain domains whitelisted. Contact [technical support](technical-support.md) if you are not able to connect to a domain and we will evaluate whether it belongs on the whitelist.

Maximum duration of jobs is 7 days.

Vulcan is currently open to all researchers doing research on AI or applying AI methods in their research.

## Access
To be able to log in to Vulcan, you must [request access in CCDB](https://ccdb.alliancecan.ca/me/access_services).

To be able to submit jobs, you must be a member of an AIP RAP.  
If you are a PI and you do not already have one, apply for [General Access to PAICE Systems](https://ccdb.alliancecan.ca/paice/general_access_to_paice_systems).

If you are a PI and need to sponsor other researchers you will have to add them to your AIP RAP. Follow these steps to manage users:
* Go to the "Resource Allocation Projects" table on the [CCDB home page](https://ccdb.alliancecan.ca).
* Locate the RAPI of your AIP project (with the `aip-` prefix) and click on it to reach the RAP management page.
* At the bottom of the RAP management page, click on "Manage RAP memberships."
* Enter the CCRI of the user you want to add in the "Add Members" section.

## Vulcan hardware specifications

{| class="wikitable sortable"
!Nodes !! Model || CPU !! Cores !! System Memory!! GPUs per node || Total GPUs 
|-
|  252 || Dell R760xa || 2 x Intel Xeon Gold 6448Y || 64 || 512 GB || 4 x NVIDIA L40s 48GB || 1008
|}

## Storage system

<b>Vulcan</b>'s storage system uses a combination of NVMe flash and HDD storage running on the Dell PowerScale platform with a total usable capacity of approximately 5PB. Home, Scratch, and Project are on the same Dell PowerScale system.

{| class="wikitable sortable"
|-
| <b>Home space</b>||
* Location of /home directories.
* Each /home directory has a small fixed [quota](storage-and-file-management#filesystem_quotas_and_policies.md).
* Not allocated via [RAS](https://alliancecan.ca/en/services/advanced-research-computing/accessing-resources/rapid-access-service) or [RAC](https://alliancecan.ca/en/services/advanced-research-computing/accessing-resources/resource-allocation-competition). Larger requests go to the /project space.
* Has daily backup
|-
| <b>Scratch space</b> ||
* For active or temporary (scratch) storage.
* Not allocated.
* Large fixed [quota](storage-and-file-management#filesystem_quotas_and_policies.md) per user.
* Inactive data will be [purged](scratch-purging-policy.md).
|-
|<b>Project space</b>
||
* Large adjustable [quota](storage-and-file-management#filesystem_quotas_and_policies.md) per project.
* Has daily backup.
|}

## Network interconnects

Nodes are interconnected with 100Gbps Ethernet with RoCE (RDMA over Converged Ethernet) enabled.

## Scheduling
The <b>Vulcan</b> cluster uses the Slurm scheduler to run user workloads. The basic scheduling commands are similar to the other national systems.

## Software
* Module-based software stack.
* Both the standard Alliance software stack as well as cluster-specific software.