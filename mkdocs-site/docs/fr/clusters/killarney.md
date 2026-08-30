---
title: "Killarney/fr"
slug: "killarney"
lang: "fr"

source_wiki_title: "Killarney/fr"
source_hash: "759afb4169b03fefbb24b42c7d87ac7d"
last_synced: "2026-08-30T01:09:18.871111+00:00"
last_processed: "2026-08-30T01:33:57.615648+00:00"

tags:
  []

keywords:
  - "GPU NVIDIA H100"
  - "NVIDIA L40S 48GB"
  - "Dell 750xa"
  - "ordonnanceur Slurm"
  - "intelligence artificielle"
  - "Infiniband HDR100"
  - "1.7Po"
  - "NVME VastData"
  - "purgées"
  - "quota fixe"
  - "RAP (Resource Allocation Project)"
  - "Intel Xeon Gold 6338"
  - "grand quota ajustable"
  - "Killarney"
  - "ECPIA"

questions:
  - "Quel type de projets et quels chercheurs peuvent actuellement accéder à la grappe Killarney ?"
  - "Quelles sont les étapes et les exigences pour obtenir un RAP de type AIP et parrainer d’autres utilisateurs sur Killarney ?"
  - "Quels sont les principaux composants matériels (CPU, mémoire, GPU, stockage) disponibles sur les nœuds de calcul standard et de performance de Killarney ?"
  - "Quels sont les quotas, les politiques de purge et les sauvegardes associées aux répertoires /home, /scratch et /project ?"
  - "Quel type d’interconnexion réseau est fourni aux nœuds de calcul standard et aux nœuds de calcul de performance ?"
  - "Quel ordonnanceur est utilisé sur le système et comment les utilisateurs accèdent‑ils aux modules logiciels disponibles ?"
  - "Quels sont les composants principaux (processeurs, mémoire, stockage et GPU) du serveur Dell 750xa et leurs spécifications ?"
  - "Comment le serveur Dell XE9680 est‑il configuré en termes de processeurs, capacité mémoire, type et taille de stockage ainsi que nombre et modèle de GPU ?"
  - "Quelle est la capacité utilisable du système de stockage NVME VastData indiqué dans le texte ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

| Caractéristique | Valeur |
| :---------------- | :---- |
| Disponibilité     | 2025-06-09 |
| Nœud de connexion | **killarney.alliancecan.ca** |
| Collection Globus | [en préparation] |
| Page d'état       | [https://status.alliancecan.ca/system/Killarney](https://status.alliancecan.ca/system/Killarney) |

**Killarney** est une grappe de calcul qui répond aux besoins de la communauté scientifique canadienne en intelligence artificielle. Elle est située à [l'Université de Toronto](https://www.utoronto.ca/) et gérée par [l'Institut Vecteur](https://vectorinstitute.ai/) et [SciNet](https://www.scinethpc.ca/). Son nom rappelle le [parc provincial Killarney](https://www.ontarioparks.ca/park/killarney/fr) qui se trouve près de la baie Georgienne, en Ontario.

Killarney fait partie de l'ECPIA, l'environnement de calcul pancanadien pour l'intelligence artificielle.

## Particularités
Killarney est présentement disponible pour les chercheuses principales et chercheurs principaux titulaires d'une chaire en intelligence artificielle (IACC) et affiliés à Vector, ainsi que celles et ceux qui sont dans un programme d'IA d'une université canadienne ou qui utilisent l'IA dans leurs travaux de recherche.

!!! note
    Les systèmes de fichiers distants de Killarney (`/home`, `/scratch`, etc.) sont montés via NFS v3, qui ne prend pas en charge les listes de contrôle d'accès (ACL); par conséquent, les commandes telles que `setfacl` ne sont pas prises en charge. Si vous devez partager des données avec des personnes qui ne font pas partie de votre groupe, veuillez envoyer un courriel à [ops-help@vectorinstitute.ai](mailto:ops-help@vectorinstitute.ai) pour demander la création d'un répertoire partagé.

## Accès
[Demandez l'accès dans le portail CCDB](https://ccdb.alliancecan.ca/me/access_services).

Les chercheuses principales et chercheurs principaux doivent obtenir de la part de leur établissement un RAP (*Resource Allocation Project*) de type AIP (*Artificial Intelligence Project*); le nom du projet sera préfixé de `aip-`. Pour parrainer les personnes qui participent au projet RAP, la chercheuse principale ou le chercheur principal doit [demander l'accès à l'Environnement informatique pancanadien de l’IA (EIPIA)](https://ccdb.alliancecan.ca/paice/general_access_to_paice_systems).

Pour identifier les personnes que vous parrainez pour le projet :
*   Faites afficher le tableau *Projet(s) avec allocation de ressources* dans CCDB.
*   Cliquez sur le RAPI de votre projet AIP (préfixé `aip-`).
*   Au bas de la page *Détails pour le projet*, cliquez sur *Gérer l'appartenance aux projets*.
*   Entrez le ou les CCRI des personnes que vous parrainez.

!!! warning "Blocage géographique"
    Dans le cadre de ses mesures de cybersécurité, Vector applique le blocage géographique à Killarney afin d'assurer l'intégrité et la sécurité. Vector restreint l'accès aux pays identifiés dans l'[Évaluation des cybermenaces nationales 2025-2026](https://www.cyber.gc.ca/fr/orientation/evaluation-cybermenaces-nationales-2025-2026) publié par le gouvernement du Canada.

## Matériel

| Performance          | Nœuds | Modèle         | CPU                        | Cœurs | Mémoire système | Stockage    | GPU par nœud                 | Total de GPU |
| :------------------- | :---- | :------------- | :------------------------- | :---- | :-------------- | :---------- | :--------------------------- | :----------- |
| Calcul standard      | 168   | Dell 750xa     | 2 x Intel Xeon Gold 6338   | 64    | 512 GB          | 350 GB SSD  | 4 x NVIDIA L40S 48GB         | 672          |
| Calcul de performance | 10    | Dell XE9680    | 2 x Intel Xeon Gold 6442Y  | 48    | 2048 GB         | 800 GB NVMe | 8 x NVIDIA H100 SXM 80GB     | 80           |

## Stockage

Le système de stockage est une plateforme NVMe VastData avec une capacité utilisable de 1.7 Po.

| | |
| :--------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`/home`**    | * emplacement des répertoires `/home`<br>* [quota fixe](../storage-and-data/storage_and_file_management.md#quotas-et-politiques) pour chaque répertoire<br>* les demandes pour plus d'espace sont dirigées vers `/project`<br>* sauvegarde quotidienne |
| **`/scratch`** | * conçu pour le stockage actif ou temporaire<br>* [grand quota fixe](../storage-and-data/storage_and_file_management.md#quotas-et-politiques) par utilisateur<br>* les données inactives sont [purgées](../storage-and-data/scratch_purging_policy.md)    |
| **`/project`** | * [grand quota ajustable](../storage-and-data/storage_and_file_management.md#quotas-et-politiques) par projet<br>* sauvegarde quotidienne                                                                                        |

## Réseautique

*   Nœuds de calcul standard : Infiniband HDR100, débit de 100 Gbit/s
*   Nœuds de calcul de performance : 2 x HDR 200, débit agrégé de 400 Gbit/s

## Ordonnancement
L'ordonnanceur Slurm exécute les tâches soumises par les utilisateurs. Les commandes Slurm de base sont semblables à celles pour les autres systèmes nationaux.

## Logiciel
*   Pile logicielle de modules.
*   Pile logicielle standard de l'Alliance et logiciels particuliers à chaque grappe.