---
title: "Killarney/fr"
slug: "killarney"
lang: "fr"

source_wiki_title: "Killarney/fr"
source_hash: "cd7c085ef95e6d3a2b38ea092cd339d4"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:24:31.589478+00:00"

tags:
  []

keywords:
  - "Ordonnanceur Slurm"
  - "stockage"
  - "Pile logicielle"
  - "sauvegarde quotidienne"
  - "Quota ajustable"
  - "Killarney"
  - "intelligence artificielle"
  - "Institut Vecteur"
  - "grappe de calcul"
  - "Infiniband"
  - "quota fixe"
  - "Nœuds de calcul"
  - "stockage actif ou temporaire"
  - "/scratch"
  - "données inactives purgées"

questions:
  - "Qu'est-ce que la grappe Killarney et à quelle communauté scientifique est-elle principalement destinée ?"
  - "Quelles sont les conditions d'admissibilité et les démarches requises pour obtenir l'accès à ce système ?"
  - "Quelles sont les caractéristiques techniques de Killarney en matière de matériel de calcul (CPU/GPU) et de capacité de stockage ?"
  - "Quelles sont les caractéristiques de quota et de sauvegarde associées à l'espace de stockage /project ?"
  - "Quelles sont les différences de configuration réseau entre les nœuds de calcul standard et les nœuds de performance ?"
  - "Quel système est utilisé pour l'ordonnancement des tâches et de quoi est composée la pile logicielle ?"
  - "Vers quel répertoire les demandes d'espace supplémentaire doivent-elles être dirigées ?"
  - "Quelle est la fonction principale du répertoire /scratch ?"
  - "Quelle politique s'applique aux données inactives stockées dans le répertoire /scratch ?"
  - "Quelles sont les caractéristiques de quota et de sauvegarde associées à l'espace de stockage /project ?"
  - "Quelles sont les différences de configuration réseau entre les nœuds de calcul standard et les nœuds de performance ?"
  - "Quel système est utilisé pour l'ordonnancement des tâches et de quoi est composée la pile logicielle ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

| Disponibilité | 2025-06-09
| Nœud de connexion | **killarney.alliancecan.ca**
| Collection Globus | [en préparation]
| Page d'état | [Page d'état](https://status.alliancecan.ca/system/Killarney)

**Killarney** est une grappe qui répond aux besoins de la communauté scientifique canadienne en intelligence artificielle. Elle est située à [l'Université de Toronto](https://www.utoronto.ca/) et gérée par [l'Institut Vecteur](https://vectorinstitute.ai/) et [SciNet](https://www.scinethpc.ca/). Son nom rappelle [le parc provincial Killarney](https://www.ontarioparks.ca/park/killarney/fr) qui se trouve près de la baie Georgienne, en Ontario.

Killarney fait partie de ECPIA, l'environnement de calcul pancanadien pour l'intelligence artificielle.

## Particularités
Killarney est présentement disponible pour les chercheuses principales et chercheurs principaux titulaires d'une chaire en intelligence artificielle (IACC) et affiliés à Vector, ainsi que celles et ceux qui sont dans un programme d'IA d'une université canadienne ou qui utilisent l'IA dans leurs travaux de recherche.

## Accès
[Demandez l'accès dans le portail CCDB](https://ccdb.alliancecan.ca/me/access_services).

Les chercheuses principales et chercheurs principaux doivent obtenir de la part de leur établissement un RAP (*Resource Allocation Project*) de type AIP (*Artificial Intelligence Project*); le nom du projet sera préfixé de `aip-`. Pour parrainer les personnes qui participent au projet RAP, la chercheuse principale ou le chercheur principal doit [demander l'accès à l'Environnement informatique pancanadien de l’IA (EIPIA)](https://ccdb.alliancecan.ca/paice/general_access_to_paice_systems).

Pour identifier les personnes que vous parrainez pour le projet :
*   Faites afficher le tableau *Projet(s) avec allocation de ressources* dans CCDB.
*   Cliquez sur le RAPI de votre projet AIP (préfixé `aip-`).
*   Au bas de la page *Détails pour le projet*, cliquez sur *Gérer l'appartenance aux projets*.
*   Entrez le ou les CCRI des personnes que vous parrainez.

Dans le cadre de ses mesures de cybersécurité, Vector applique le blocage géographique à Killarney afin d'assurer l'intégrité et la sécurité. Vector restreint l'accès aux pays identifiés dans [Évaluation des cybermenaces nationales 2025-2026](https://www.cyber.gc.ca/fr/orientation/evaluation-cybermenaces-nationales-2025-2026) publié par le gouvernement du Canada.

## Matériel

| Performance          | Nœuds | Modèle         | CPU                        | Cœurs | Mémoire système | GPU par nœud       | Total de GPU |
| :------------------- | :---- | :------------- | :------------------------- | :---- | :-------------- | :----------------- | :----------- |
| Calcul standard      | 168   | Dell 750xa     | 2 x Intel Xeon Gold 6338   | 64    | 512 GB          | 4 x NVIDIA L40S 48GB | 672          |
| Calcul de performance | 10    | Dell XE9680    | 2 x Intel Xeon Gold 6442Y  | 48    | 2048 GB         | 8 x NVIDIA H100 SXM 80GB | 80           |

## Stockage

Le système de stockage est une plateforme NVME VastData avec une capacité utilisable de 1,7 Po.

|           |                                                                               |
| :-------- | :---------------------------------------------------------------------------- |
| **`/home`** | * emplacement des répertoires /home<br/>* [quota fixe](../storage-and-data/storage_and_file_management.md#quotas-et-politiques) pour chaque répertoire<br/>* les demandes pour plus d'espace sont dirigées vers /project<br/>* sauvegarde quotidienne |
| **`/scratch`** | * conçu pour le stockage actif ou temporaire<br/>* [grand quota fixe](../storage-and-data/storage_and_file_management.md#quotas-et-politiques) par utilisateur<br/>* les données inactives sont [purgées](../storage-and-data/scratch_purging_policy.md) |
| **`/project`** | * [grand quota ajustable](../storage-and-data/storage_and_file_management.md#quotas-et-politiques) par projet<br/>* sauvegarde quotidienne |

## Réseautique

*   Nœuds de calcul standard : Infiniband HDR100, débit de 100 Gbit/s
*   Nœuds de calcul de performance : 2 x HDR 200, débit agrégé de 400 Gbit/s

## Ordonnancement
L'ordonnanceur Slurm exécute les tâches soumises par les utilisateurs. Les commandes Slurm de base sont semblables à celles pour les autres systèmes nationaux.

## Logiciel
*   Pile logicielle de modules.
*   Pile logicielle standard de l'Alliance et logiciels particuliers à chaque grappe.