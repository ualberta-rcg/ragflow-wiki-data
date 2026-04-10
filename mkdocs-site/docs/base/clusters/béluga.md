---
title: "Béluga"
slug: "béluga"
lang: "base"

source_wiki_title: "Béluga"
source_hash: "01b07710e0a505c5917063c7eed10766"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T05:01:28.849439+00:00"

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

!!! warning "Attention"
Béluga has been replaced by a new cluster named [Rorqual](rorqual.md). To allow for the full production deployment of this new cluster, **all Béluga compute nodes have been shut down**. Login nodes and the storage system will remain accessible. To follow the progressive shutdown steps for Béluga, see [this incident page](https://status.alliancecan.ca/view_incident?incident=1379) and the [Infrastructure Renewal](infrastructure-renewal.md) page.

| | |
| :------- | :------------------------------------------------------------------------------------------------------ |
| Availability: | March 2019 |
| Login Node: | **beluga.alliancecan.ca** |
| Globus Collection: | **[computecanada#beluga-dtn](https://app.globus.org/file-manager?origin_id=278b9bfe-24da-11e9-9fa2-0a06afd4a22e)** |
| Copy Node (rsync, scp, sftp,...): | **beluga.alliancecan.ca** |
| Portal: | https://portail.beluga.calculquebec.ca/ |

Béluga is a heterogeneous and versatile cluster designed for general-purpose computing; it is located at the [École de technologie supérieure](http://www.etsmtl.ca/). Its name evokes the [beluga whale](https://en.wikipedia.org/wiki/Beluga_whale), a marine mammal living in the waters of the St. Lawrence River.

## Specifics
Our policy dictates that Béluga compute nodes do not have internet access. To request an exception, contact [technical support](technical-support.md), explaining your needs and reasons. Note that the `crontab` tool is not available.

Each job should have a minimum duration of one hour (at least five minutes for test jobs), and a user cannot have more than 1000 jobs (running and pending) at a time. The maximum job duration is 7 days (168 hours).

## Storage

| | |
| :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| HOME<br>Lustre file system, 105 TB total space | - This space is small and cannot be expanded; you will need to use your `project` space for large storage needs.<br>- Small, fixed [quotas](storage-and-file-management.md#quotas-and-policies) per user.<br>- Automatic daily backups. |
| SCRATCH<br>Lustre file system, 2.6 PB total space | - Large space for temporary files during computations.<br>- No automatic backup system.<br>- Large, fixed [quotas](storage-and-file-management.md#quotas-and-policies) per user.<br>- Automatic [purging](scratch-purging-policy.md) of old files from this space. |
| PROJECT<br>Lustre file system, 25 PB total space | - This space is designed for data sharing among group members and for storing large amounts of data.<br>- Large, adjustable [quotas](storage-and-file-management.md#quotas-and-policies) per project.<br>- Automatic daily backups. |

For Globus data transfers, the `computecanada#beluga-dtn` endpoint should be used, while for tools like rsync and scp, a login node can be used.

## High-Performance Networking

The Mellanox Infiniband EDR (100 Gb/s) network connects all cluster nodes. A central 324-port switch aggregates island connections with a maximum blocking factor of 5:1. Storage servers are connected with a non-blocking interconnect. The architecture allows for multiple parallel tasks with up to 640 cores (or more) thanks to non-blocking networking. For larger tasks, the blocking factor is 5:1; even for tasks spanning multiple islands, the interconnect remains high-performance.

## Node Characteristics
**Note: As of July 31, 2025, all nodes below are shut down.**
Turbo mode is now enabled on all Béluga nodes.

| nodes | cores | available memory | CPU | storage | GPU |
| :---- | :---- | :--------------- | :-- | :------ | :-- |
| 160   | 40    | 92G or 95000M    | 2 x Intel Gold 6148 Skylake @ 2.4 GHz | 1 x 480G SSD | - |
| 579   | 40    | 186G or 191000M  | 2 x Intel Gold 6148 Skylake @ 2.4 GHz | 1 x 480G SSD | - |
| 10    | 40    | 186G or 191000M  | 2 x Intel Gold 6148 Skylake @ 2.4 GHz | 6 x 480G SSD | - |
| 51    | 40    | 752G or 771000M  | 2 x Intel Gold 6148 Skylake @ 2.4 GHz | 1 x 480G SSD | - |
| 2     | 40    | 752G or 771000M  | 2 x Intel Gold 6148 Skylake @ 2.4 GHz | 6 x 480G SSD | - |
| 172   | 40    | 186G or 191000M  | 2 x Intel Gold 6148 Skylake @ 2.4 GHz | 1 x 1.6T NVMe SSD | 4 x NVidia V100SXM2 (16G memory), connected via NVLink |

* To obtain a larger `$SLURM_TMPDIR` space, you must request `--tmp=xG`, where `x` is a value between 350 and 2490.

## Job Monitoring
From the [portal](https://portail.beluga.calculquebec.ca/), you can monitor your CPU and GPU computing jobs in "real-time" or past jobs to maximize resource utilization and reduce queue waiting times.

Specifically, for a job, you can visualize:
* compute core utilization;
* memory usage;
* GPU utilization;

It is important to use the allocated resources and adjust your requests when computing resources are underutilized or unused. For example, if you request four cores (CPUs) but only use one, you should adjust your submission file accordingly.