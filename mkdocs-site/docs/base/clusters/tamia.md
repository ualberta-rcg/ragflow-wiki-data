---
title: "TamIA"
slug: "tamia"
lang: "base"

source_wiki_title: "TamIA"
source_hash: "10d29517a0342e52ef1e87a7cd6f1186"
last_synced: "2026-08-07T19:46:17.777436+00:00"
last_processed: "2026-08-07T22:58:06.915855+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: true
  qa_generated: false
---

| Service | Details |
| :------ | :------ |
| Availability | **March 31, 2025** |
| Login Node | **tamia.alliancecan.ca** |
| [Automation Node](../getting-started/automation_in_the_context_of_multifactor_authentication.md) | robot.tamia.ecpia.ca |
| Globus Collection | [TamIA's Globus v5 Server](https://app.globus.org/file-manager?origin_id=72c3bca0-9281-4742-b066-333ba0fdef72) |
| Copy Node (rsync, scp, sftp,...) | **tamia.alliancecan.ca** |
| Portal | https://portail.tamia.ecpia.ca/ |

TamIA is a cluster dedicated to the needs of the Canadian scientific community in artificial intelligence. TamIA is located at [Université Laval](http://www.ulaval.ca/) and is co-managed with [Mila](https://mila.quebec/) and [Calcul Québec](https://calculquebec.ca/). Its name refers to the [chipmunk](https://fr.wikipedia.org/wiki/Tamia), a rodent mammal found in North America.

This cluster is part of the [Pan-Canadian Artificial Intelligence Computing Environment (PAICE)](https://www.alliancecan.ca/fr/nos-services/calcul-informatique-de-pointe/environnement-de-calcul-pan-canadien-pour-lintelligence-artificielle-ecpia).

## Special Features
*   Our policy dictates that TamIA compute nodes do not have internet access. To request an exception, please contact [technical support](../support/technical_support.md), explaining your needs and reasons.
*   Note that the `crontab` tool is not available.
*   Note that the integrated development environment [VSCode](https://code.visualstudio.com/) is **forbidden** on **login nodes** due to its heavy load. It is still permitted on compute nodes.
*   Each job should have a minimum duration of one hour (at least five minutes for test jobs), and you cannot have more than 1000 jobs (running and pending) at a time.
*   The maximum job duration is one day (24 hours).
*   Each job must use all GPUs of the allocated servers: 4 for H100s and 8 for H200s.

## Access
1.  To access the cluster, each researcher must [complete an access request in the CCDB](https://ccdb.alliancecan.ca/me/access_services) **(select the 'Artificial Intelligence' tab, then 'tamIA')**. Effective access to the cluster may take up to one hour after completing the access request.

2.  To submit compute jobs, you must be a member of an `aip-` prefixed RAP (*Resource Allocation Project*). If you are a **Principal Investigator** and do not yet have such a RAP, you must submit a [declaration of intended use of artificial intelligence](https://ccdb.alliancecan.ca/paice/general_access_to_paice_systems).

The procedure for sponsoring other researchers is as follows:
*   On the **[CCDB homepage](https://ccdb.alliancecan.ca/)**, consult the 'Resource Allocation Project' table;
*   Find the RAPI of the `aip-` project and click on it to be redirected to the RAP management page;
*   At the bottom of the RAP management page, click on **Manage Project Membership**;
*   In the 'Add Members' section, enter the CCRI of the member to add.

The compute cluster is only accessible from Canada.

## Storage
| Storage Location | Details |
| :--------------- | :------ |
| HOME <br> Lustre filesystem | * This space is small and cannot be expanded; you will need to use your `project` space for large storage needs. <br> * Small fixed [quotas](../storage-and-data/storage_and_file_management.md) per user. <br> * There is currently no automatic backup. (Planned for Spring 2026) |
| SCRATCH <br> Lustre filesystem | * Large space for temporary files during calculations. <br> * No automatic backup system. <br> * Large fixed [quotas](../storage-and-data/storage_and_file_management.md) per user. <br> * There is an [automatic purging policy](../storage-and-data/scratch_purging_policy.md) for old files in this space. |
| PROJECT <br> Lustre filesystem | * This space is designed for data sharing among group members and for storing large amounts of data. <br> * Large adjustable [quotas](../storage-and-data/storage_and_file_management.md) per project. <br> * There is an automatic daily backup. |

At the beginning of this page, a table lists several connection addresses. For data transfers via [Globus](../getting-started/globus.md), you should use the **Globus Collection**. However, for tools like [rsync](../getting-started/transferring_data.md#rsync) and [scp](../getting-started/transferring_data.md#scp), you should use the **Copy Node** address.

## High-Performance Networking
The [InfiniBand](https://fr.wikipedia.org/wiki/Bus_InfiniBand) [Nvidia NDR](https://www.nvidia.com/en-us/networking/quantum2/) network connects all nodes in the cluster. Each GPU is connected to an NDR200 port via an Nvidia ConnectX-7 card. Each server therefore has 4 or 8 NDR200 ports connected to the InfiniBand fabric.

The InfiniBand network is non-blocking for compute servers and consists of 2 layers of switches arranged in a 'fat-tree' topology. Storage and compute nodes are connected via 4 or 8 400Gb/s connections to the network core.

## Node Characteristics
| Nodes | Cores | Available Memory | CPU | Storage | GPU |
| :---- | :---- | :--------------- | :-- | :------ | :-- |
| 12 | 64 | 1024GB | 2 x [Intel Xeon Gold 6448Y 2.1 GHz, 32C](https://www.intel.com/content/www/us/en/products/sku/232384/intel-xeon-gold-6448y-processor-60m-cache-2-10-ghz/specifications.html) | 1 x 7.68TB SSD | 8 x [NVIDIA HGX H200](https://www.nvidia.com/en-us/data-center/h200/) SXM 141GB HBM3 700W, connected via NVLink |
| 53 | 48 | 512GB | 2 x [Intel Xeon Gold 6442Y 2.6 GHz, 24C](https://www.intel.com/content/www/us/en/products/sku/232380/intel-xeon-gold-6442y-processor-60m-cache-2-60-ghz/specifications.html) | 1 x 7.68TB SSD | 4 x [NVIDIA HGX H100](https://www.nvidia.com/en-us/data-center/h100/) SXM 80GB HBM3 700W, connected via NVLink |
| 8 | 64 | 512GB | 2 x [Intel Xeon Gold 6438M 2.2G, 32C/64T](https://www.intel.com/content/www/us/en/products/sku/232398/intel-xeon-gold-6438m-processor-60m-cache-2-20-ghz/specifications.html) | 1 x 7.68TB SSD | None |

### Available Software Environments
The [standard software environment `StdEnv/2023`](../programming/standard_software_environments.md) is the default environment on TamIA.

### GPU Jobs
Jobs are assigned to full nodes. Use one of the following Slurm options:

*   For a job on a node with H100 GPUs: `--gpus=h100:4`
*   For a job on a node with H200 GPUs: `--gpus=h200:8`
*   For multi-node jobs, use `--gpus-per-nodes=h100:4` or `--gpus-per-nodes=h200:8`.

## Monitoring Your Jobs
From the [portal](https://portail.tamia.ecpia.ca/), you can monitor your GPU and CPU jobs **in real time** or review past jobs to maximize resource utilization and reduce your queue wait times.

Specifically, for a job, you can visualize:
*   compute core utilization;
*   memory usage;
*   GPU utilization.

It is important to use the allocated resources effectively and adjust your requests when compute resources are underutilized or unused. For example, if you request four CPU cores but only use one, you should adjust your submission file accordingly.