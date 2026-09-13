---
title: "Killarney/fr"
slug: "killarney"
lang: "fr"

source_wiki_title: "Killarney/fr"
source_hash: "542260361b53613a267925c4e77e4506"
last_synced: "2026-09-13T00:40:43.713374+00:00"
last_processed: "2026-09-13T01:21:13.941296+00:00"

tags:
  []

keywords:
  - "Slurm"
  - "Calcul standard"
  - "quota ajustable"
  - "géoblocage"
  - "NVME VastData"
  - "Dell XE9680"
  - "NVIDIA H100 SXM 80GB"
  - "Killarney"
  - "Calcul de performance"
  - "Infiniband HDR100"
  - "RAP (Resource Allocation Project)"
  - "1"
  - "Université de Toronto"
  - "intelligence artificielle"
  - "7 Po"
  - "Intel Xeon Gold"

questions:
  - "Quelles sont les étapes et les prérequis nécessaires pour obtenir un accès au cluster Killarney via le portail CCDB ?"
  - "Quels sont les types de nœuds disponibles sur Killarney et quelles sont leurs spécifications matérielles (CPU, mémoire, stockage, GPU) ?"
  - "Comment les mesures de cybersécurité, notamment le géoblocage appliqué par Vector, restreignent‑elles l’accès au cluster Killarney ?"
  - "Quels sont les différents espaces de stockage (/home, /scratch, /project) ainsi que leurs politiques de quota, de sauvegarde et de purge sur la plateforme NVME VastData de 1,7 Po ?"
  - "Quels types d’interconnexions réseau sont disponibles pour les nœuds de calcul standard et de performance, et quels sont leurs débits respectifs ?"
  - "Comment l’ordonnanceur Slurm est‑il utilisé sur le cluster et quelles piles logicielles sont proposées aux utilisateurs ?"
  - "Combien de nœuds sont prévus pour le calcul standard et quelles sont leurs spécifications principales (CPU, mémoire, stockage et GPU) ?"
  - "Quelle est la configuration GPU (type de GPU et nombre total) du calcul de performance comparée à celle du calcul standard ?"
  - "Quel est le total de GPU disponible pour chaque catégorie de calcul (standard et performance) et comment cela reflète‑t‑il les capacités de traitement respectives ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

| Caractéristique             | Détail                                                                |
| :-------------------------- | :-------------------------------------------------------------------- |
| Disponibilité               | 2025-06-09                                                            |
| Nœud de connexion           | **killarney.alliancecan.ca**                                          |
| Open OnDemand               | [https://ondemand.killarney.vectorinstitute.ai](https://ondemand.killarney.vectorinstitute.ai) |
| Collection Globus           | [en préparation]                                                      |
| Page d'état du système      | [https://status.alliancecan.ca/system/Killarney](https://status.alliancecan.ca/system/Killarney) |

**Killarney** est une grappe qui répond aux besoins de la communauté scientifique canadienne en intelligence artificielle. Elle est située à [l'Université de Toronto](https://www.utoronto.ca/) et gérée par [l'Institut Vecteur](https://vectorinstitute.ai/) et [SciNet](https://www.scinethpc.ca/). Son nom rappelle [le parc provincial Killarney](https://www.ontarioparks.ca/park/killarney/fr) qui se trouve près de la baie Georgienne, en Ontario.

Killarney fait partie de l'EIPIA, l'environnement de calcul pancanadien pour l'intelligence artificielle.

## Particularités
Killarney est présentement disponible pour les chercheuses principales et chercheurs principaux titulaires d'une chaire en intelligence artificielle (IACC) et affiliés à Vector, ainsi que celles et ceux qui sont dans un programme d'IA d'une université canadienne ou qui utilisent l'IA dans leurs travaux de recherche.

Les systèmes de fichiers distants de Killarney (`/home`, `/scratch`, etc.) sont montés via NFS v3, qui ne prend pas en charge les listes de contrôle d'accès (ACL); par conséquent, les commandes telles que `setfacl` ne sont pas prises en charge. Si vous devez partager des données avec des personnes qui ne font pas partie de votre groupe, veuillez envoyer un courriel à ops-help@vectorinstitute.ai pour demander la création d'un répertoire partagé.

## Accès
[Demandez l'accès dans le portail CCDB](https://ccdb.alliancecan.ca/me/access_services) en vous assurant d'avoir [au moins une clé SSH enregistrée dans CCDB](../getting-started/ssh.md).

Les chercheuses principales et chercheurs principaux doivent obtenir de la part de leur établissement un RAP (*Resource Allocation Project*) de type AIP (*Artificial Intelligence Project*); le nom du projet sera préfixé de `aip-`. Pour parrainer les personnes qui participent au projet RAP, la chercheuse principale ou le chercheur principal doit [demander l'accès à l'Environnement informatique pancanadien de l’IA (EIPIA)](https://ccdb.alliancecan.ca/paice/general_access_to_paice_systems).

Pour identifier les personnes que vous parrainez pour le projet :
*   Faites afficher le tableau *Projet(s) avec allocation de ressources* dans CCDB.
*   Cliquez sur le RAPI de votre projet AIP (préfixé `aip-`).
*   Au bas de la page *Détails pour le projet*, cliquez sur *Gérer l'appartenance aux projets*.
*   Entrez le ou les CCRI des personnes que vous parrainez.

Dans le cadre de ses mesures de cybersécurité, **Vector applique le géoblocage** sur Killarney afin d'assurer l'intégrité et la sécurité. Vector restreint l'accès aux pays identifiés dans [Évaluation des cybermenaces nationales 2025-2026](https://www.cyber.gc.ca/fr/orientation/evaluation-cybermenaces-nationales-2025-2026) publié par le gouvernement du Canada.

## Matériel

| Performance          | Nœuds | Modèle      | CPU                          | Cœurs | Mémoire système | Stockage   | GPU par nœud           | Total de GPU |
| :------------------- | :---- | :---------- | :--------------------------- | :---- | :-------------- | :--------- | :--------------------- | :----------- |
| Calcul standard      | 168   | Dell 750xa  | 2 x Intel Xeon Gold 6338     | 64    | 512 GB          | 350 GB SSD | 4 x NVIDIA L40S 48GB   | 672          |
| Calcul de performance | 10    | Dell XE9680 | 2 x Intel Xeon Gold 6442Y    | 48    | 2048 GB         | 800 GB NVMe | 8 x NVIDIA H100 SXM 80GB | 80           |

## Stockage

Le système de stockage est une plateforme NVME VastData avec une capacité utilisable de 1.7 Po.

| Espace de stockage | Détails                                                                                                          |
| :----------------- | :--------------------------------------------------------------------------------------------------------------- |
| **`/home`**        | * emplacement des répertoires /home<br/>* [quota fixe](../storage-and-data/storage_and_file_management.md#quotas-et-politiques) pour chaque répertoire<br/>* les demandes pour plus d'espace sont dirigées vers /project<br/>* sauvegarde quotidienne |
| **`/scratch`**     | * conçu pour le stockage actif ou temporaire<br/>* [grand quota fixe](../storage-and-data/storage_and_file_management.md#quotas-et-politiques) par utilisateur<br/>* les données inactives sont [purgées](../storage-and-data/scratch_purging_policy.md) |
| **`/project`**     | * [grand quota ajustable](../storage-and-data/storage_and_file_management.md#quotas-et-politiques) par projet<br/>* sauvegarde quotidienne |

## Réseautique

*   Nœuds de calcul standard : Infiniband HDR100, débit de 100 Gbps
*   Nœuds de calcul de performance : 2 x HDR 200, débit agrégé de 400 Gbps

## Ordonnancement
L'ordonnanceur Slurm exécute les tâches soumises par les utilisateurs. Les commandes Slurm de base sont semblables à celles pour les autres systèmes nationaux.

## Logiciel
*   Pile logicielle de modules.
*   Pile logicielle standard de l'Alliance et logiciels particuliers à chaque grappe.