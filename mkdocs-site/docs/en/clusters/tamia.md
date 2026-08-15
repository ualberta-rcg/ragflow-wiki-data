---
title: "TamIA/en"
slug: "tamia"
lang: "en"

source_wiki_title: "TamIA/en"
source_hash: "31709ae237c4dc0ce1c5eb3544e05b5e"
last_synced: "2026-08-15T23:22:43.108655+00:00"
last_processed: "2026-08-15T23:35:18.589818+00:00"

tags:
  []

keywords:
  - "InfiniBand"
  - "NVIDIA NDR200"
  - "no home directory backup"
  - "Globus endpoint"
  - "large adjustable quota"
  - "CCDB access request"
  - "tamIA AI cluster"
  - "login node"
  - "GPU H200"
  - "rsync"
  - "GPU H100"
  - "Lustre storage quotas"
  - "tamIA"
  - "GPU job requirements"
  - "Pan-Canadian AI Compute Environment (PAICE)"

questions:
  - "1. 如何在 CCDB 门户完成 tamIA 集群的访问请求并提交 PAICE 系统的通用访问声明表？"
  - "2. tamIA 集群对作业提交有哪些关键限制（如作业时长、GPU 使用、并发作业数量）以及对登录节点的软件使用（如 VSCode）有哪些规定？"
  - "3. tamIA 提供的三种 Lustre 文件系统（HOME、SCRATCH、PROJECT）各自的用途、配额和备份策略是什么？"
  - "Quel type de réseau interconnecte les nœuds du cluster et quelles sont ses principales caractéristiques ?"
  - "Quelles configurations matérielles (CPU, mémoire, stockage, GPU) sont proposées pour les différents nœuds de tamIA ?"
  - "Comment soumettre des travaux GPU (options de réservation) et suivre leur utilisation en temps réel sur le portail tamIA ?"
  - "What is the current status of backup for the home directories, and when is it planned to be implemented?"
  - "How are filesystem quotas and policies applied and adjusted for each research group?"
  - "Which transfer methods should be used for moving data, and which endpoints or nodes are recommended for Globus, rsync, and scp?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: false
  qa_generated: false
---

| | |
| :--- | :--- |
| Availability | **March 31, 2025** |
| Login node | `tamia.alliancecan.ca` |
| Automation node | `robot.tamia.ecpia.ca` |
| Globus collection | [TamIA's Globus v5 Server](https://app.globus.org/file-manager?origin_id=72c3bca0-9281-4742-b066-333ba0fdef72) |
| Data transfer node (rsync, scp, sftp,...) | `tamia.alliancecan.ca` |
| Portal | [https://portail.tamia.ecpia.ca/](https://portail.tamia.ecpia.ca/) |

tamIA is a cluster dedicated to artificial intelligence for the Canadian scientific community. Located at [Université Laval](http://www.ulaval.ca/), tamIA is co-managed with [Mila](https://mila.quebec/) and [Calcul Québec](https://calculquebec.ca/). The cluster is named for the [eastern chipmunk](https://en.wikipedia.org/wiki/Tamias), a common species found in eastern North America.

tamIA is part of [the Pan-Canadian AI Compute Environment (PAICE)](https://www.alliancecan.ca/en/our-services/advanced-research-computing/pan-canadian-ai-compute-environment-paice).

## Site-specific policies

*   By policy, tamIA's compute nodes cannot access the internet. If you need an exception to this rule, contact [technical support](../support/technical_support.md) explaining what you need and why.
*   `crontab` is not offered on tamIA.
*   The maximum duration of a job is one day (24 hours).
*   Each job should be at least one hour long (at least five minutes for test jobs) and you can't have more than 1000 jobs (running and pending) at the same time.
*   Each job must use all 4 GPUs of the servers allocated, i.e., 4 with H100 and 8 with H200.

!!! warning "VSCode on Login Nodes"
    Please note that the **[VSCode IDE](https://code.visualstudio.com/)** is **forbidden** on the **login nodes** due to its heavy footprint. It is still authorized on the compute nodes.

## Access
1. To access the cluster, each researcher must complete [an access request in the CCDB portal](https://ccdb.alliancecan.ca/me/access_services) under *Resources-->Artificial Intelligence-->tamIA*. Access to the cluster may take up to one hour after the access request is sent.
    You must then submit the [General Access to PAICE Systems declaration form](https://ccdb.alliancecan.ca/paice/general_access_to_paice_systems).

2. To submit compute jobs, you must be a member of an RAP (Resource Allocation Project), which has the prefix `aip-`. If you are a principal investigator and do not have a RAP yet, please [request access in CCDB](https://ccdb.alliancecan.ca/me/access_services).

The procedure for sponsoring other researchers is as follows:
*   On the **[CCDB home page](https://ccdb.alliancecan.ca/)**, go to the *Resource Allocation Projects* table
*   Look for the RAPI of the `aip-` project and click on it to be redirected to the RAP management page
*   At the bottom of the RAP management page, click on **Manage RAP memberships**
*   To add a new member, go to *Add Members* and enter the CCRI of the user you want to add.

The cluster can only be reached from Canada.

## Storage

| | |
| :--- | :--- |
| HOME<br>Lustre file system | *   Location of home directories, each of which has a small fixed quota.<br>*   You should use the `project` space for larger storage needs.<br>*   Small per user [quota](../storage-and-data/storage_and_file_management.md#filesystem-quotas-and-policies).<br>*   There is currently no backup of the home directories. (ETA Spring 2026) |
| SCRATCH<br>Lustre file system | *   Large space for storing temporary files during computations<br>*   No backup system in place<br>*   Large [quota](../storage-and-data/storage_and_file_management.md#filesystem-quotas-and-policies) per user<br>*   There is an [automated purge](../storage-and-data/scratch_purging_policy.md) of older files in this space. |
| PROJECT<br>Lustre file system | *   This space is designed for sharing data among the members of a research group and for storing large amounts of data.<br>*   Large and adjustable per group [quota](../storage-and-data/storage_and_file_management.md#filesystem-quotas-and-policies).<br>*   There is currently no backup of the home directories. (ETA Summer 2025) |

For transferring data via [Globus](../getting-started/globus.md), you should use the endpoint specified at the top of this page, while for tools like [rsync](../getting-started/transferring_data.md#rsync) and [scp](../getting-started/transferring_data.md#scp) you can use a login node.

## High-performance interconnect
The [InfiniBand](https://fr.wikipedia.org/wiki/Bus_InfiniBand) [NVIDIA NDR](https://www.nvidia.com/en-us/networking/quantum2/) network links together all of the nodes of the cluster. Each GPU is connected to a single NDR200 port through an NVIDIA ConnectX-7 HCA. Each GPU server has 4 or 8 NDR200 ports connected to the InfiniBand fabric.

The InfiniBand network is non-blocking for compute servers and is composed of two levels of switches in a fat-tree topology. Storage and compute nodes are connected via 4 or 8 400Gb/s connections to the network core.

## Node characteristics

| nodes | cores | available memory | CPU | storage | GPU |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 12 | 64 | 1024GB | 2 x [Intel Xeon Gold 6448Y 2,1 GHz, 32C](https://www.intel.com/content/www/us/en/products/sku/232384/intel-xeon-gold-6448y-processor-60m-cache-2-10-ghz/specifications.html) | 1 x 7.68TB SSD | 8 x [NVIDIA HGX H200](https://www.nvidia.com/en-us/data-center/h200/) SXM 141GB HBM3 700W, connected via NVLink |
| 53 | 48 | 512GB | 2 x [Intel Xeon Gold 6442Y 2,6 GHz, 24C](https://www.intel.com/content/www/us/en/products/sku/232380/intel-xeon-gold-6442y-processor-60m-cache-2-60-ghz/specifications.html) | 1 x 7.68TB SSD | 4 x [NVIDIA HGX H100](https://www.nvidia.com/en-us/data-center/h100/) SXM 80GB HBM3 700W, connected via NVLink |
| 8 | 64 | 512GB | 2 x [Intel Xeon Gold 6438M 2.2G, 32C/64T](https://www.intel.com/content/www/us/en/products/sku/232398/intel-xeon-gold-6438m-processor-60m-cache-2-20-ghz/specifications.html) | 1 x 7.68TB SSD | none |

### Software environments
[`StdEnv/2023`](../programming/standard_software_environments.md) is the standard environment on tamIA.

### GPU jobs
Jobs are assigned on whole nodes with one of the following options:

For jobs on a node with an H100 GPU: `--gpus=h100:4`

For jobs on a node with an H200 GPU: `--gpus=h200:8`

For jobs using several GPUs, options are `--gpus-per-nodes=h100:4` or `--gpus-per-nodes=h200:8`.

## Monitoring jobs

From the tamIA [portal](https://portail.tamia.ecpia.ca/), you can monitor your jobs using CPUs and GPUs **in real time** or examine jobs that have run in the past. This can help you to optimize resource usage and shorten wait time in the queue.

You can monitor your usage of
*   compute nodes,
*   memory,
*   GPU.

It is important that you use the allocated resources and to correct your requests when compute resources are less used or not used at all. For example, if you request 4 cores (CPUs) but use only one, you should adjust the script file accordingly.