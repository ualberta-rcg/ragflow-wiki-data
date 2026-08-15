---
title: "TamIA"
slug: "tamia"
lang: "base"

source_wiki_title: "TamIA"
source_hash: "48c310c0b6118eb6745373a9f049357a"
last_synced: "2026-08-15T23:22:43.108655+00:00"
last_processed: "2026-08-15T23:34:53.361640+00:00"

tags:
  []

keywords:
  - "NVIDIA HGX H200"
  - "StdEnv/2023"
  - "grappe de calcul"
  - "Gérer l'appartenance aux projets"
  - "GPU h100 et h200"
  - "SSD de 7.68 TB"
  - "Système de fichiers Lustre"
  - "grappe de calcul Canada"
  - "Quotas fixes par utilisateur"
  - "tâches GPU"
  - "utilisation des ressources"
  - "RAPI du projet"
  - "512 GB"
  - "--gpus=h100:4"
  - "tamIA"
  - "NVIDIA HGX H100"
  - "Réseau InfiniBand"
  - "accès via CCDB"
  - "politique sans accès internet"
  - "gestion du RAP"
  - "CCRI du membre"
  - "NVLink"
  - "Sauvegarde automatique"
  - "Intel Xeon Gold 6438M"
  - "portail tamIA"

questions:
  - "Quelles sont les étapes à suivre pour obtenir un accès à la grappe de calcul tamIA via la CCDB ?"
  - "Quelles sont les restrictions imposées aux tâches (durée minimale, durée maximale, nombre maximal, utilisation des GPU et outils interdits) sur les nœuds de tamIA ?"
  - "Quels services et points d’accès (nœuds de connexion, nœud d’automatisation, portail, Globus, etc.) sont disponibles pour les utilisateurs de tamIA ?"
  - "Quels sont les trois espaces de stockage (HOME, SCRATCH, PROJECT) et quelles différences offrent‑ils concernant la taille, les quotas et les sauvegardes ?"
  - "Quelle adresse doit‑on utiliser pour les transferts de données avec Globus versus les outils rsync ou scp ?"
  - "Quels sont les principaux composants matériels des nœuds (CPU, mémoire, GPU, stockage) et comment le réseau InfiniBand est‑il organisé pour assurer la haute performance ?"
  - "Quelle est la procédure détaillée pour ajouter un membre à un projet en utilisant la fonction « Gérer l'appartenance aux projets » ?"
  - "Où faut‑il rechercher le RAPI du projet « aip- » et quelle action doit‑on réaliser une fois trouvé ?"
  - "Quelle limitation géographique est mentionnée concernant l’accès à la grappe de calcul ?"
  - "Combien de cartes NVIDIA HGX H100 sont installées et quelles sont leurs spécifications (mémoire, puissance et interconnexion NVLink) ?"
  - "Quels processeurs Intel Xeon Gold 6438M sont utilisés et quelles sont leurs caractéristiques (cœurs, threads, fréquence, cache) ?"
  - "Quelle capacité de stockage SSD est fournie et quels environnements logiciels sont disponibles sur cette configuration ?"
  - "Quels paramètres Slurm faut‑il spécifier pour réserver des GPU H100 ou H200 sur un nœud complet ?"
  - "Comment suivre en temps réel l’utilisation des cœurs, de la mémoire et des GPU d’une tâche via le portail tamIA ?"
  - "Pourquoi est‑il important d’ajuster les demandes de ressources lorsqu’elles sont sous‑utilisées et comment le faire ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: false
  qa_generated: false
---

| Field               | Value                                                              |
| :------------------ | :----------------------------------------------------------------- |
| Availability        | **March 31, 2025**                                                 |
| Login Node          | **tamia.alliancecan.ca**                                           |
| Automation Node     | [Automation Node](../getting-started/automation_in_the_context_of_multifactor_authentication.md): robot.tamia.ecpia.ca |
| Globus Collection   | [TamIA's Globus v5 Server](https://app.globus.org/file-manager?origin_id=72c3bca0-9281-4742-b066-333ba0fdef72) |
| Copy Node (rsync, scp, sftp,...) | **tamia.alliancecan.ca**                                           |
| Portal              | https://portail.tamia.ecpia.ca/                                    |

TamIA is a cluster dedicated to the needs of the Canadian scientific community in artificial intelligence. TamIA is located at [Université Laval](http://www.ulaval.ca/) and is co-managed with [Mila](https://mila.quebec/) and [Calcul Québec](https://calculquebec.ca/). Its name recalls the [tamia](https://fr.wikipedia.org/wiki/Tamia), a rodent mammal present in North America.

This cluster is part of [the Pan-Canadian Artificial Intelligence Computing Environment (PACEI)](https://www.alliancecan.ca/en/our-services/advanced-research-computing/pan-canadian-artificial-intelligence-computing-environment-pacei).

## Specific Features

*   It is our policy that TamIA compute nodes do not have Internet access. To request an exception, please contact [technical support](../support/technical_support.md), explaining what you need and why.
*   Note that the `crontab` tool is not available.
*   Note that the *[VSCode](https://code.visualstudio.com/)* integrated development environment is **forbidden** on the **login nodes** due to its heavy load. It is still permitted on compute nodes.
*   Each job should have a minimum duration of one hour (at least five minutes for test jobs) and you cannot have more than 1000 jobs (running and pending) at a time.
*   The maximum duration for a job is one day (24 hours).
*   Each job must use all GPUs on the allocated servers: 4 for H100s and 8 for H200s.

## Access

1.  To access the computing cluster, each researcher must [complete an access request in the CCDB](https://ccdb.alliancecan.ca/me/access_services) **(select the 'Artificial Intelligence' tab, then 'tamIA')**. Effective access to the cluster may take up to an hour after completing the access request.
2.  To submit compute jobs, you must be a member of a Resource Allocation Project (RAP) prefixed with `aip-`. If you are a **Principal Investigator** and do not yet have such a RAP, you must submit a [declaration of intended use of artificial intelligence](https://ccdb.alliancecan.ca/paice/general_access_to_paice_systems).

The procedure for sponsoring other researchers is as follows:

*   On the [CCDB homepage](https://ccdb.alliancecan.ca/), consult the 'Project with Resource Allocation' table;
*   Look for the `aip-` project RAP ID and click on it to be redirected to the RAP management page;
*   At the bottom of the RAP management page, click on **Manage Project Membership**;
*   In the 'Add Members' section, enter the member's CCRI.

The computing cluster is accessible only from Canada.

## Storage

| Space   | File System     | Details                                                                                                                                                                                                                                                                                                                                                                                                                             |
| :------ | :-------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| HOME    | Lustre File System | *   This space is small and cannot be expanded; you will need to use your `project` space for large storage needs.<br>*   Small fixed per-user [quotas](../storage-and-data/storage_and_file_management.md)<br>*   There is currently no automatic backup. (Planned for Spring 2026)                                                                                                                                         |
| SCRATCH | Lustre File System | *   Large space for storing temporary files during computations.<br>*   No automatic backup system.<br>*   Large fixed per-user [quotas](../storage-and-data/storage_and_file_management.md).<br>*   There is an [automatic purging](../storage-and-data/scratch_purging_policy.md) of old files in this space.                                                                                                                                       |
| PROJECT | Lustre File System | *   This space is designed for sharing data among group members and for storing large amounts of data.<br>*   Large adjustable per-project [quotas](../storage-and-data/storage_and_file_management.md).<br>*   There is an automatic daily backup.                                                                                                                                                                               |

At the very beginning of this page, a table lists several connection addresses. For data transfers via [Globus](../getting-started/globus.md), you must use the **Globus Drop Point**. However, for tools like [rsync](../getting-started/transferring_data.md#rsync) and [scp](../getting-started/transferring_data.md#scp), you must use the address of the **Copy Node**.

## High-Performance Networking

The [InfiniBand](https://fr.wikipedia.org/wiki/Bus_InfiniBand) [Nvidia NDR](https://www.nvidia.com/en-us/networking/quantum2/) network connects all nodes in the cluster. Each GPU is connected to an NDR200 port via an Nvidia ConnectX-7 card. Each server therefore has 4 or 8 NDR200 ports connected to the InfiniBand fabric.

The InfiniBand network is non-blocking for compute servers and consists of 2 layers of switches arranged in a "fat-tree" topology. Storage and compute nodes are connected via 4 or 8 400Gb/s connections to the network core.

## Node Specifications

| Nodes | Cores | Available Memory | CPU                                                                                                                                                                          | Storage          | GPU                                                                                                                         |
| :---- | :---- | :--------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------- | :-------------------------------------------------------------------------------------------------------------------------- |
| 12    | 64    | 1024GB           | 2 x [Intel Xeon Gold 6448Y 2.1 GHz, 32C](https://www.intel.com/content/www/us/en/products/sku/232384/intel-xeon-gold-6448y-processor-60m-cache-2-10-ghz/specifications.html) | 1 x 7.68TB SSD   | 8 x [NVIDIA HGX H200](https://www.nvidia.com/en-us/data-center/h200/) SXM 141GB HBM3 700W, connected via NVLink |
| 53    | 48    | 512GB            | 2 x [Intel Xeon Gold 6442Y 2.6 GHz, 24C](https://www.intel.com/content/www/us/en/products/sku/232380/intel-xeon-gold-6442y-processor-60m-cache-2-60-ghz/specifications.html) | 1 x 7.68TB SSD   | 4 x [NVIDIA HGX H100](https://www.nvidia.com/en-us/data-center/h100/) SXM 80GB HBM3 700W, connected via NVLink |
| 8     | 64    | 512GB            | 2 x [Intel Xeon Gold 6438M 2.2G, 32C/64T](https://www.intel.com/content/www/us/en/products/sku/232398/intel-xeon-gold-6438m-processor-60m-cache-2-20-ghz/specifications.html) | 1 x 7.68TB SSD   | None                                                                                                                        |

### Available Software Environments

The [standard software environment `StdEnv/2023`](../programming/standard_software_environments.md) is the default environment on TamIA.

### GPU Jobs

Jobs are assigned to full nodes. Use one of the following Slurm options:

*   For a job on a node with H100 GPUs: `--gpus=h100:4`
*   For a job on a node with H200 GPUs: `--gpus=h200:8`
*   For multi-node jobs, use `--gpus-per-nodes=h100:4` or `--gpus-per-nodes=h200:8`.

## Monitoring Your Jobs

From the [portal](https://portail.tamia.ecpia.ca/), you can monitor your GPU and CPU compute jobs **in real-time** or view past jobs to maximize resource utilization and reduce queue waiting times.

Specifically, for a job, you can visualize:

*   compute core usage;
*   memory usage;
*   GPU usage.

It is important to use the allocated resources effectively and to adjust your requests if compute resources are underutilized or unused. For example, if you request four CPU cores but only use one, you should adjust your submission file accordingly.