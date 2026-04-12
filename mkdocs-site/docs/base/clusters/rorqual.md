---
title: "Rorqual"
slug: "rorqual"
lang: "base"

source_wiki_title: "Rorqual"
source_hash: "2432503fbd7ca744828a0b13e8a50f11"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:05:19.856557+00:00"

tags:
  []

keywords:
  - "instances GPU"
  - "Transferts de données"
  - "Topologie des nœuds CPU"
  - "demande d'accès"
  - "mémoire cache"
  - "Nœuds GPU"
  - "Technologie MIG"
  - "Instances GPU"
  - "mémoire GPU"
  - "espace project"
  - "Rorqual"
  - "cœurs"
  - "Réseautique haute performance"
  - "prise CPU"
  - "H100"
  - "nœuds GPU"
  - "Système de fichiers Lustre"
  - "instance GPU"
  - "stockage"
  - "nœuds de calcul"
  - "puissance de calcul"
  - "nœud NUMA"
  - "Caractéristiques des nœuds"
  - "grappe de calcul"
  - "cœurs CPU"
  - "sauvegarde automatique"
  - "chiplets"
  - "technologie MIG"
  - "quotas fixes"
  - "Nœuds NUMA"
  - "NVidia H100"

questions:
  - "Qu'est-ce que la grappe Rorqual et quelle est sa fonction principale ?"
  - "Quelles sont les étapes requises pour demander et obtenir l'accès à ce système de calcul ?"
  - "Quelles sont les contraintes techniques et les limites d'exécution des tâches imposées aux utilisateurs ?"
  - "Quel espace de stockage doit-on utiliser pour répondre à des besoins importants en capacité ?"
  - "Quelle est la fréquence des sauvegardes automatiques pour le petit espace de stockage ?"
  - "Quel est le type de système de fichiers et la capacité totale de l'espace SCRATCH ?"
  - "Quelles sont les principales différences entre les espaces de stockage \"scratch\" et \"project\" en matière de sauvegarde et de conservation des données ?"
  - "Quelles sont les caractéristiques matérielles spécifiques des nœuds équipés d'accélérateurs GPU par rapport aux nœuds CPU standards ?"
  - "Comment la topologie NUMA est-elle structurée au sein d'un nœud CPU de 192 cœurs et quel est son impact sur les délais d'accès à la mémoire ?"
  - "Comment la topologie des cœurs et de la mémoire est-elle structurée dans les nœuds standards pour optimiser les programmes parallèles ?"
  - "Quelles sont les caractéristiques matérielles spécifiques qui composent l'architecture des nœuds GPU ?"
  - "Quelles sont les différentes instances GPU disponibles sur Rorqual et quelles options Slurm permettent de les réserver ?"
  - "Combien de canaux de mémoire système sont connectés à chaque nœud NUMA ?"
  - "Quelle est la capacité de la mémoire cache L3 pour chaque chiplet au sein d'un nœud NUMA ?"
  - "Comment les mémoires caches L1 et L2 sont-elles réparties pour chacun des huit cœurs d'un chiplet ?"
  - "Quelles sont les différentes instances de GPU H100 disponibles et quelles sont leurs capacités respectives en termes de puissance et de mémoire ?"
  - "Quelle est la syntaxe exacte à utiliser pour demander une seule instance GPU spécifique lors d'une tâche de calcul ?"
  - "Où peut-on consulter les recommandations concernant les quantités maximales de cœurs CPU et de mémoire système par instance GPU ?"
  - "Comment doit-on formuler la commande pour allouer plusieurs GPU H100 répartis sur différents nœuds ?"
  - "Quelle proportion des nœuds GPU du cluster Rorqual est configurée avec la technologie MIG ?"
  - "Combien de tailles d'instances GPU sont disponibles sur les nœuds utilisant la technologie MIG ?"
  - "Quelles sont les différentes instances de GPU H100 disponibles et quelles sont leurs capacités respectives en termes de puissance et de mémoire ?"
  - "Quelle est la syntaxe exacte à utiliser pour demander une seule instance GPU spécifique lors d'une tâche de calcul ?"
  - "Où peut-on consulter les recommandations concernant les quantités maximales de cœurs CPU et de mémoire système par instance GPU ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

| Availability | June 19, 2025
| Login node | **rorqual.alliancecan.ca**
| Data transfer node (rsync, scp, sftp ...) | **rorqual.alliancecan.ca**
| [Automation node](../automation-in-the-context-of-multifactor-authentication.md) | robot.rorqual.alliancecan.ca
| Globus Collection | [alliancecan#rorqual](https://app.globus.org/file-manager?origin_id=f19f13f5-5553-40e3-ba30-6c151b9d35d4)
| JupyterHub | [jupyterhub.rorqual.alliancecan.ca](https://jupyterhub.rorqual.alliancecan.ca/)
| Portal | [metrix.rorqual.alliancecan.ca](https://metrix.rorqual.alliancecan.ca/)
| Webinar | [slides](https://docs.google.com/presentation/d/1SxqzNI9dtxnVCe8I2otJg6PJpLQwDjeDakNI7yMsuvU), [video](https://www.youtube.com/watch?v=hTM6XOvYjxw)

Rorqual is a heterogeneous and versatile cluster designed for a wide variety of scientific computations. Built by Dell Canada and CDW Canada, Rorqual is located at the [École de technologie supérieure](http://www.etsmtl.ca/). Its name recalls the [rorqual](https://fr.wikipedia.org/wiki/Rorqual), a marine mammal whose several species, for example the [minke whale](https://baleinesendirect.org/decouvrir/especes-baleines-saint-laurent/13-especes/petit-rorqual/) and the [blue whale](https://baleinesendirect.org/decouvrir/especes-baleines-saint-laurent/13-especes/rorqual-bleu/), have been observed in the waters of the St. Lawrence River.

## Access
To access the compute cluster, each researcher must [complete an access request](https://ccdb.alliancecan.ca/me/access_systems) in the form found via *Resources > System Access* in the CCDB menu bar. In this form:

1.  Select 'Rorqual' from the left list.
2.  In the first box on the right, select the access request.
3.  Then accept all specific agreements with Calcul Québec:
    *   Consent for the Collection and Use of Personal Information,
    *   Rorqual Service Level Agreement,
    *   Terms of Use.

!!! warning
    Actual access to the cluster may take **up to one hour** after completing the access request.

## Specifics

!!! warning
    Our policy is that Rorqual compute nodes do not have internet access. To request an exception, please contact [technical support](../technical-support.md) explaining your needs and reasons. Note that the `crontab` tool is not available.

Each job should be at least one hour long (at least five minutes for test jobs), and you cannot have more than 1000 jobs (running and pending) at a time. The maximum job duration is 7 days (168 hours).

## Storage

| Filesystem | Description |
| :--------- | :---------- |
| HOME <br> Lustre filesystem, 116 TB total space | * This space is small and cannot be expanded: you will need to use your `project` space for large storage needs.<br>* Small, fixed [quotas](../storage-and-file-management.md#quotas-and-policies) per user<br>* There is an automatic daily backup. |
| SCRATCH <br> Lustre filesystem, 6.5 PB total space | * Accessible via the symbolic link `$HOME/links/scratch`<br>* Large space for storing temporary files during computations.<br>* No automatic backup system<br>* Large, fixed [quotas](../storage-and-file-management.md#quotas-and-policies) per user<br>* There is an [automatic purging policy](../scratch-purging-policy.md) for old files in this space. |
| PROJECT <br> Lustre filesystem, 62 PB total space | * Accessible via the symbolic link `$HOME/links/projects/project-name`<br>* This space is designed for data sharing among group members and for storing large amounts of data.<br>* Large, adjustable [quotas](../storage-and-file-management.md#quotas-and-policies) per project<br>* There is an automatic daily backup. |

At the very beginning of this page, a table lists several connection addresses. For data transfers via [Globus](../globus.md), use the **Globus Endpoint**. However, for tools like [rsync](../transferring-data.md#rsync) and [scp](../transferring-data.md#scp), you must use the **Data transfer node** address.

## High-Performance Networking
*   InfiniBand Networking
    *   HDR 200Gbit/s
    *   Maximum blocking factor: 34:6 or 5.667:1
    *   Size of CPU node islands: up to 31 nodes of 192 cores that can communicate without blocking.

## Node Specifications

| nodes | cores | available memory | storage | CPU | GPU |
| :---- | :---- | :--------------- | :------ | :-- | :-- |
| 670 | 192 | 750G or 768000M | 1 x 480GB SATA SSD (6Gbit/s) | 2 x [AMD EPYC 9654 (Zen 4)](https://www.amd.com/en/support/downloads/drivers.html/processors/epyc/epyc-9004-series/amd-epyc-9654.html) @ 2.40 GHz, 384MB L3 cache | |
| 8 | 192 | 750G or 768000M | 1 x 3.84TB NVMe SSD | 2 x [AMD EPYC 9654 (Zen 4)](https://www.amd.com/en/support/downloads/drivers.html/processors/epyc/epyc-9004-series/amd-epyc-9654.html) @ 2.40 GHz, 384MB L3 cache | |
| 8 | 192 | 3013G or 3086250M | 1 x 480GB SATA SSD (6Gbit/s) | 2 x [AMD EPYC 9654 (Zen 4)](https://www.amd.com/en/support/downloads/drivers.html/processors/epyc/epyc-9004-series/amd-epyc-9654.html) @ 2.40 GHz, 384MB L3 cache | |
| 93 | 64 | 498G or 510000M | 1 x 3.84TB NVMe SSD | 2 x [Intel Xeon Gold 6448Y](https://ark.intel.com/content/www/us/en/ark/products/232384/intel-xeon-gold-6448y-processor-60m-cache-2-10-ghz.html) @ 2.10 GHz, 60MB L3 cache | 4 x NVidia H100 SXM5 (80GB memory), connected via NVLink |

*   To get a larger `$SLURM_TMPDIR` space, you must request `--tmp=xG`, where `x` is a value between 370 and 3360.

### CPU Node Topology
In a CPU node, the 192 cores and different memory spaces are not equidistant, causing variable latencies (on the order of nanoseconds) to access data. In each node, we have:

*   Two (2) CPU *sockets*, each with 12 system memory channels.
    *   Four (4) [NUMA](https://fr.wikipedia.org/wiki/Non_uniform_memory_access) *nodes* per CPU socket, each connected to three (3) system memory channels.
        *   Three (3) *chiplets* per *NUMA node*, each with its own 32 MiB [L3 cache](https://fr.wikipedia.org/wiki/Cache_de_processeur).
            *   Eight (8) cores per *chiplet*, each with its own 1 MiB L2 and 32+32 KiB L1 cache.

In other words, we have:
*   Groups of 8 closely located cores that share the same L3 cache, which is ideal for [multithreaded parallel programs](../running-jobs.md#multithreaded-or-openmp-jobs) (for example, with the `--cpus-per-task=8` option).
*   NUMA *nodes* of 3×8 = 24 cores that share a trio of system memory channels.
*   A total of 2×4×3×8 = 192 cores per node.

To fully benefit from this topology, you must reserve full nodes (for example, with `--ntasks-per-node=24 --cpus-per-task=8`) and explicitly control the placement of processes and execution threads. Depending on the parallel program and the number of cores used, the gains can be marginal or significant.

### GPU Node Topology
In GPU nodes, the architecture is less hierarchical. We have:

*   Two (2) CPU *sockets*. For each, we have:
    *   Eight (8) system memory channels
    *   60 MiB L3 cache
    *   32 equidistant cores, each with its own 2 MiB L2 and 32+48 KiB L1 cache.
    *   Two (2) NVidia H100 accelerators

In total, the four (4) accelerators on the node are interconnected by [SXM5](https://en.wikipedia.org/wiki/SXM_(socket)).

### GPU Instances

The different GPU instance names available on Rorqual are:

| Type | Instance | Short Name | Unitless Name | By Memory | Full Name |
| :--- | :------- | :--------- | :------------ | :-------- | :-------- |
| **GPU** | **H100-80gb** | `h100` | `h100` | `h100_80gb` | `nvidia_h100_80gb_hbm3` |
| **MIG** | **H100-1g.10gb** | `h100_1g.10gb` | `h100_1.10` | `h100_10gb` | `nvidia_h100_80gb_hbm3_1g.10gb` |
| **MIG** | **H100-2g.20gb** | `h100_2g.20gb` | `h100_2.20` | `h100_20gb` | `nvidia_h100_80gb_hbm3_2g.20gb` |
| **MIG** | **H100-3g.40gb** | `h100_3g.40gb` | `h100_3.40` | `h100_40gb` | `nvidia_h100_80gb_hbm3_3g.40gb` |

To request one or more full H100 GPUs, use one of the following Slurm options:
*   **One H100-80gb**: `--gpus=h100:1` or `--gpus=h100_80gb:1`
*   **Multiple H100-80gb** per node:
    *   `--gpus-per-node=h100:2`
    *   `--gpus-per-node=h100:3`
    *   `--gpus-per-node=h100:4`
*   **Multiple H100-80gb** scattered anywhere: `--gpus=h100:n` (replace `n` with the desired number)

Approximately half of Rorqual's GPU nodes are configured with [MIG technology](../multi-instance-gpu.md), and only three GPU instance sizes are available:

*   **H100-1g.10gb**: 1/8 of the compute power with 10 GB of GPU memory.
*   **H100-2g.20gb**: 2/8 of the compute power with 20 GB of GPU memory.
*   **H100-3g.40gb**: 3/8 of the compute power with 40 GB of GPU memory.

To request **one and only one** GPU instance for your compute job, here are the corresponding options:

*   **H100-1g.10gb**: `--gpus=h100_1g.10gb:1`
*   **H100-2g.20gb**: `--gpus=h100_2g.20gb:1`
*   **H100-3g.40gb**: `--gpus=h100_3g.40gb:1`

The maximum recommended amounts of **CPU cores and system memory** per GPU instance are listed in the [bundle characteristics table](../allocations-and-compute-scheduling.md#ratios-in-bundles).