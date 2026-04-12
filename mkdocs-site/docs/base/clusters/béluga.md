---
title: "Béluga"
slug: "béluga"
lang: "base"

source_wiki_title: "Béluga"
source_hash: "01b07710e0a505c5917063c7eed10766"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:52:26.921475+00:00"

tags:
  []

keywords:
  - "ressources de calcul"
  - "Rorqual"
  - "interconnexion non bloquante"
  - "Béluga"
  - "haute performance"
  - "grappe de calcul"
  - "nœuds de Béluga"
  - "CPU et GPU"
  - "système de stockage"
  - "serveurs de stockage"
  - "facteur de blocage"
  - "tâches parallèles"
  - "suivi des tâches"
  - "SLURM_TMPDIR"
  - "réseautique haute performance"

questions:
  - "Pourquoi les nœuds de calcul de la grappe Béluga ont-ils été fermés et par quel système a-t-elle été remplacée ?"
  - "Quelles sont les contraintes spécifiques concernant l'accès à internet et les limites d'exécution des tâches sur cette grappe ?"
  - "Quelles sont les différences entre les espaces de stockage HOME, SCRATCH et PROJECT en matière de capacité, de sauvegarde et d'utilisation prévue ?"
  - "Quel est le statut actuel des nœuds de Béluga et quelles sont leurs caractéristiques matérielles principales ?"
  - "Quelle est la procédure à suivre pour demander un espace de stockage temporaire plus grand lors de la soumission d'une tâche ?"
  - "Pourquoi est-il recommandé de faire le suivi de ses tâches sur le portail et quelles métriques peuvent y être observées ?"
  - "Quel est le facteur de blocage maximum appliqué aux interconnexions des îlots lors de l'exécution de tâches imposantes ?"
  - "Comment les serveurs de stockage sont-ils connectés au sein de cette architecture ?"
  - "Combien de cœurs peuvent être utilisés simultanément pour des tâches parallèles et quelle caractéristique réseau permet cela ?"
  - "Quel est le statut actuel des nœuds de Béluga et quelles sont leurs caractéristiques matérielles principales ?"
  - "Quelle est la procédure à suivre pour demander un espace de stockage temporaire plus grand lors de la soumission d'une tâche ?"
  - "Pourquoi est-il recommandé de faire le suivi de ses tâches sur le portail et quelles métriques peuvent y être observées ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! warning "Attention"
Béluga has been replaced by a new cluster called [Rorqual](rorqual.md). To enable the full production rollout of this new cluster, **we had to shut down all Béluga compute nodes**. The login nodes and storage system will remain accessible. To follow the progressive shutdown steps for Béluga, see [this incident page](https://status.alliancecan.ca/view_incident?incident=1379) and the [Infrastructure Renewal](infrastructure_renewal.md) page.

| Availability | March 2019 |
| :----------- | :--------- |
| Login Node   | **beluga.alliancecan.ca** |
| Globus Collection | **[computecanada#beluga-dtn](https://app.globus.org/file-manager?origin_id=278b9bfe-24da-11e9-9fa2-0a06afd4a22e)** |
| Transfer Node (rsync, scp, sftp,...) | **beluga.alliancecan.ca** |
| Portal       | https://portail.beluga.calculquebec.ca/ |

Béluga is a heterogeneous, general-purpose cluster designed for ordinary computations; it is located at the [École de technologie supérieure](http://www.etsmtl.ca/). Its name refers to the [beluga whale](https://fr.wikipedia.org/wiki/B%C3%A9luga_(c%C3%A9tac%C3%A9)), a marine mammal living in the waters of the St. Lawrence River.

## Specifics
Our policy dictates that Béluga compute nodes do not have internet access. To request an exception, contact [technical support](../support/technical_support.md) explaining your needs and reasons. Note that the `crontab` tool is not available.

Each job should have a minimum duration of one hour (or at least five minutes for test jobs), and a user cannot have more than 1000 jobs (running and pending) at a time. The maximum job duration is 7 days (168 hours).

## Storage

| Filesystem | Description |
| :--------- | :---------- |
| HOME <br> Lustre Filesystem, 105 TB total space | * This space is small and cannot be expanded; you will need to use your `project` space for large storage needs.<br>* Small fixed per-user [quotas](../storage-and-data/storage_and_file_management.md#quotas-and-policies).<br>* Automatic daily backup. |
| SCRATCH <br> Lustre Filesystem, 2.6 PB total space | * Large space for storing temporary files during computations.<br>* No automatic backup system.<br>* Large fixed per-user [quotas](../storage-and-data/storage_and_file_management.md#quotas-and-policies).<br>* Automatic [purging](../storage-and-data/scratch_purging_policy.md) of old files in this space. |
| PROJECT <br> Lustre Filesystem, 25 PB total space | * This space is designed for sharing data among group members and for storing large amounts of data.<br>* Large adjustable per-project [quotas](../storage-and-data/storage_and_file_management.md#quotas-and-policies).<br>* Automatic daily backup. |

For data transfers via Globus, the `computecanada#beluga-dtn` endpoint should be used, while for tools like rsync and scp, a login node can be used.

## High-Performance Networking

The Mellanox Infiniband EDR (100 Gb/s) network connects all cluster nodes. A central 324-port switch aggregates island connections with a maximum blocking factor of 5:1. Storage servers are connected with non-blocking interconnects. The architecture enables multiple parallel tasks with up to 640 cores (or more) thanks to non-blocking networking. For larger tasks, the blocking factor is 5:1; even for tasks running across multiple islands, the interconnectivity is high-performance.

## Node Specifications
**Note: as of July 31, 2025, all nodes below are powered off.**
Turbo mode is now enabled on all Béluga nodes.

| Nodes | Cores | Available Memory | CPU | Storage | GPU |
| :---- | :---- | :--------------- | :-- | :------ | :-- |
| 160   | 40    | 92G or 95000M    | 2 x Intel Gold 6148 Skylake @ 2.4 GHz | 1 x 480G SSD | - |
| 579   | 40    | 186G or 191000M  | 2 x Intel Gold 6148 Skylake @ 2.4 GHz | 1 x 480G SSD | - |
| 10    | 40    | 186G or 191000M  | 2 x Intel Gold 6148 Skylake @ 2.4 GHz | 6 x 480G SSD | - |
| 51    | 40    | 752G or 771000M  | 2 x Intel Gold 6148 Skylake @ 2.4 GHz | 1 x 480G SSD | - |
| 2     | 40    | 752G or 771000M  | 2 x Intel Gold 6148 Skylake @ 2.4 GHz | 6 x 480G SSD | - |
| 172   | 40    | 186G or 191000M  | 2 x Intel Gold 6148 Skylake @ 2.4 GHz | 1 x 1.6T NVMe SSD | 4 x NVidia V100SXM2 (16G memory), connected via NVLink |

*   To obtain a larger `$SLURM_TMPDIR` space, you must request `--tmp=xG`, where `x` is a value between 350 and 2490.

## Monitoring Your Jobs
From the [portal](https://portail.beluga.calculquebec.ca/), you can monitor your CPU and GPU compute jobs in "real-time" or past jobs to maximize resource utilization and reduce your queue wait times.

For a given job, you can visualize:
*   compute core utilization;
*   memory usage;
*   GPU utilization;

It is important to use the allocated resources and to adjust your requests when compute resources are underutilized or not used at all. For example, if you request four cores (CPUs) but only use one, you must adjust your submission file accordingly.