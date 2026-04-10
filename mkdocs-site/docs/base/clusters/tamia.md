---
title: "TamIA"
slug: "tamia"
lang: "base"

source_wiki_title: "TamIA"
source_hash: "3473317d9e2c308646af0332a3b1d837"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T11:34:30.905668+00:00"

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

| Availability | **March 31, 2025**
| Login Node | `tamia.alliancecan.ca`
| [Automation Node](automation-in-the-context-of-multifactor-authentication.md) | `robot.tamia.ecpia.ca`
| Globus Collection | [TamIA's Globus v5 Server](https://app.globus.org/file-manager?origin_id=72c3bca0-9281-4742-b066-333ba0fdef72)
| Copy Node (rsync, scp, sftp,...) | **`tamia.alliancecan.ca`**
| Portal | <https://portail.tamia.ecpia.ca/>

TamIA is a cluster dedicated to the needs of the Canadian scientific community in artificial intelligence. TamIA is located at [Université Laval](http://www.ulaval.ca/) and is co-managed with [Mila](https://mila.quebec/) and [Calcul Québec](https://calculquebec.ca/). Its name recalls the [chipmunk](https://en.wikipedia.org/wiki/Chipmunk), a rodent mammal present in North America.

This cluster is part of the [Pan-Canadian AI Computing Environment (PAICE)](https://alliancecan.ca/en/services/advanced-research-computing/pan-canadian-ai-computing-environment-paice).

## Peculiarities
* Our policy states that TamIA compute nodes do not have internet access. To request an exception, please contact [technical support](technical-support.md) explaining your needs and reasons.
* Note that the `crontab` tool is not available.
* Note that the integrated development environment [VSCode](https://code.visualstudio.com/) is **forbidden** on **login nodes** due to its heavy load. It is still permitted on compute nodes.
* Each job should be at least one hour long (at least five minutes for test jobs), and you cannot have more than 1000 jobs (running and pending) at a time.
* The maximum job duration is one day (24 hours).
* Each job must use all allocated GPUs on the servers, i.e., 4 for H100 and 8 for H200.

## Access
To access the cluster, each researcher must [complete an access request in the CCDB](https://ccdb.alliancecan.ca/me/access_services). Effective access to the cluster may take up to one hour after completing the access request. Afterwards, a [declaration of intended use of artificial intelligence](https://ccdb.alliancecan.ca/paice/general_access_to_paice_systems) must be submitted.

Eligible Principal Investigators are members of an AIP-type RAP (prefix `aip-`).

The procedure for sponsoring other researchers is as follows:
* On the [CCDB homepage](https://ccdb.alliancecan.ca/), consult the 'Resource Allocation Project' table;
* Find the RAPI of the `aip-` project and click on it to be redirected to the RAP management page;
* At the bottom of the RAP management page, click on **Manage project membership**;
* In the 'Add members' section, enter the CCRI of the member to add.

The cluster is accessible only from Canada.

## Storage
| | |
| :--- | :--- |
| HOME <br> Lustre File System | * This space is small and cannot be expanded: you will need to use your `project` space for large storage needs.<br>* Small fixed [quotas](storage-and-file-management.md#quotas-and-policies) per user<br>* There is currently no automatic backup. (Planned for Spring 2026)
| SCRATCH <br> Lustre File System | * Large space for storing temporary files during calculations<br>* No automatic backup system<br>* Large fixed [quotas](storage-and-file-management.md#quotas-and-policies) per user<br>* There is an [automatic purging](scratch-purging-policy.md) of old files in this space.
| PROJECT <br> Lustre File System | * This space is designed for data sharing among group members and for storing large amounts of data.<br>* Large adjustable [quotas](storage-and-file-management.md#quotas-and-policies) per project<br>* There is an automatic backup once a day.

At the very beginning of this page, a table lists several connection addresses. For data transfers via [Globus](globus.md), you must use the **Globus Drop Point**. However, for tools like [rsync](transferring-data.md#rsync) and [scp](transferring-data.md#scp), you must use the **Copy Node** address.

## High-Performance Networking
The [InfiniBand](https://en.wikipedia.org/wiki/InfiniBand) [Nvidia NDR](https://www.nvidia.com/en-us/networking/quantum2/) network connects all cluster nodes. Each GPU is connected to a NDR200 port via an Nvidia ConnectX-7 card. Each server therefore has 4 or 8 NDR200 ports connected to the InfiniBand fabric.

The InfiniBand network is non-blocking for compute servers and consists of 2 layers of switches arranged in a "fat-tree" topology. Storage and compute nodes are connected via 4 or 8 x 400 Gb/s connections to the network core.

## Node Characteristics
| nodes | cores | available memory | CPU | storage | GPU |
| :---- | :---- | :--------------- | :-- | :------ | :-- |
| 12 | 64 | 1024GB | 2 x [Intel Xeon Gold 6448Y 2.1 GHz, 32C](https://www.intel.com/content/www/us/en/products/sku/232384/intel-xeon-gold-6448y-processor-60m-cache-2-10-ghz/specifications.html) | 1 x 7.68TB SSD | 8 x [NVIDIA HGX H200](https://www.nvidia.com/en-us/data-center/h200/) SXM 141GB HBM3 700W, connected via NVLink |
| 53 | 48 | 512GB | 2 x [Intel Xeon Gold 6442Y 2.6 GHz, 24C](https://www.intel.com/content/www/us/en/products/sku/232380/intel-xeon-gold-6442y-processor-60m-cache-2-60-ghz/specifications.html) | 1 x 7.68TB SSD | 4 x [NVIDIA HGX H100](https://www.nvidia.com/en-us/data-center/h100/) SXM 80GB HBM3 700W, connected via NVLink |
| 8 | 64 | 512GB | 2 x [Intel Xeon Gold 6438M 2.2G, 32C/64T](https://www.intel.com/content/www/us/en/products/sku/232398/intel-xeon-gold-6438m-processor-60m-cache-2-20-ghz/specifications.html) | 1 x 7.68TB SSD | None |

### Available Software Environments
The [standard software environment `StdEnv/2023`](standard-software-environments.md) is the default environment on TamIA.

### GPU Jobs
Jobs are assigned to full nodes. Use one of the following Slurm options:

For a job on a node with H100 GPUs: `--gpus=h100:4`

For a job on a node with H200 GPUs: `--gpus=h200:8`

For multi-node jobs, use `--gpus-per-nodes=h100:4` or `--gpus-per-nodes=h200:8`.

## Monitoring Your Jobs
From the [portal](https://portail.tamia.ecpia.ca/), you can monitor your GPU and CPU compute jobs **in real-time** or past jobs to maximize resource utilization and decrease your queue wait times.

Specifically, for a job, you can visualize:
* compute core utilization;
* memory usage;
* GPU utilization.

It is important to use the allocated resources and to adjust your requests when compute resources are underutilized or unused. For example, if you request four CPU cores but only use one, you must adjust your submission file accordingly.