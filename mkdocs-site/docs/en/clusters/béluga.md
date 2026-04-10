---
title: "Béluga/en"
slug: "béluga"
lang: "en"

source_wiki_title: "Béluga/en"
source_hash: "9fd5c05b814a50c179ffe3c2c48c08e2"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T05:01:49.310490+00:00"

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
The Béluga cluster has been replaced by [Rorqual](rorqual.md). In order to enable full production on Rorqual, **all Béluga compute nodes were closed**. However, Béluga's storage system and its login nodes remain accessible. Information on Béluga's progressive shutdown can be found on [this incident page](https://status.alliancecan.ca/view_incident?incident=1379) and on the wiki page [Infrastructure renewal](infrastructure-renewal.md).

| Key | Value |
| :-- | :---- |
| Availability | March, 2019 |
| Login node | **beluga.alliancecan.ca** |
| Globus collection | **[computecanada#beluga-dtn](https://app.globus.org/file-manager?origin_id=278b9bfe-24da-11e9-9fa2-0a06afd4a22e)** |
| Data Transfer Node (rsync, scp, sftp,...) | **beluga.alliancecan.ca** |
| Portal | https://portail.beluga.calculquebec.ca/ |

Béluga is a general purpose cluster designed for a variety of workloads and situated at the [École de technologie supérieure](http://www.etsmtl.ca/) in Montreal. The cluster is named in honour of the St. Lawrence River's [Beluga whale](https://en.wikipedia.org/wiki/Beluga_whale) population.

## Site-specific policies
By policy, Béluga's compute nodes cannot access the internet. If you need an exception to this rule, contact [technical support](technical-support.md) explaining what you need and why.

Crontab is not offered on Béluga.

Each job on Béluga should have a duration of at least one hour (five minutes for test jobs) and a user cannot have more than 1000 jobs, running and queued, at any given moment. The maximum duration for a job on Béluga is 7 days (168 hours).

## Storage

| Filesystem | Description |
| :--------- | :---------- |
| HOME <br> Lustre filesystem, 105 TB of space | * Location of home directories, each of which has a small fixed quota.<br>* You should use the `project` space for larger storage needs.<br>* Small fixed [quota](storage-and-file-management.md#filesystem-quotas-and-policies) per user.<br>* There is a daily backup of the home directories. |
| SCRATCH <br> Lustre filesystem, 2.6 PB of space | * Large space for storing temporary files during computations.<br>* No backup system in place.<br>* Large fixed [quota](storage-and-file-management.md#filesystem-quotas-and-policies) per user.<br>* There is an [automated purge](scratch-purging-policy.md) of older files in this space. |
| PROJECT <br> Lustre filesystem, 25 PB of space | * This space is designed for sharing data among the members of a research group and for storing large amounts of data.<br>* Large adjustable [quota](storage-and-file-management.md#filesystem-quotas-and-policies) per group.<br>* There is a daily backup of the project space. |

For transferring data via Globus, you should use the endpoint `computecanada#beluga-dtn`, while for tools like rsync and scp you can use a login node.

## High-performance interconnect

A Mellanox Infiniband EDR (100 Gb/s) network connects together all the nodes of the cluster. A central switch of 324 ports links the cluster's island topology with a maximum blocking factor of 5:1. The storage servers are networked with a non-blocking connection. The architecture permits multiple parallel jobs with up to 640 cores (or more) thanks to a non-blocking network. For jobs requiring greater parallelism, the blocking factor is 5:1 but even for jobs executed across several islands, the interconnection is high-performance.

## Node characteristics
**Note: As of July 31 2025, all the nodes listed here are closed.**<br />
Turbo mode is activated on all compute nodes of Béluga.

| nodes | cores | available memory | CPU | storage | GPU |
| :---- | :---- | :--------------- | :-- | :------ | :-- |
| 160 | 40 | 92G or 95000M | 2 x Intel Gold 6148 Skylake @ 2.4 GHz | 1 x SSD 480G | - |
| 579 | 40 | 186G or 191000M | 2 x Intel Gold 6148 Skylake @ 2.4 GHz | 1 x SSD 480G | - |
| 10 | 40 | 186G or 191000M | 2 x Intel Gold 6148 Skylake @ 2.4 GHz | 6 x SSD 480G | - |
| 51 | 40 | 752G or 771000M | 2 x Intel Gold 6148 Skylake @ 2.4 GHz | 1 x SSD 480G | - |
| 2 | 40 | 752G or 771000M | 2 x Intel Gold 6148 Skylake @ 2.4 GHz | 6 x SSD 480G | - |
| 172 | 40 | 186G or 191000M | 2 x Intel Gold 6148 Skylake @ 2.4 GHz | 1 x NVMe SSD 1.6T | 4 x NVidia V100SXM2 (16G memory), connected via NVLink |

* To get a larger `$SLURM_TMPDIR` space, a job can be submitted with `--tmp=xG`, where `x` is a value between 350 and 2490.

## Monitoring jobs
To maximize the use of resources and reduce your waiting times in the queue, you can monitor your CPU and GPU past or current compute tasks in real time in the [portal](https://portail.beluga.calculquebec.ca/).

For each job you can monitor
* the use of compute cores,
* the use of memory,
* the use of GPUs.

When compute resources are little or not used at all, it is important to use the allocated resources and to adjust your requests.
For example, if you request four cores (CPUs) but only use one, you must adjust your submission file accordingly.