---
title: "Killarney/fr"
slug: "killarney"
lang: "fr"

source_wiki_title: "Killarney/fr"
source_hash: "8e77c2de0e9b520f2beb52c537cc69f1"
last_synced: "2026-11-15T02:27:25.182546+00:00"
last_processed: "2026-11-15T03:36:49.997034+00:00"

tags:
  []

keywords:
  - "Killarney"
  - "GPU NVIDIA L40S et H100"
  - "grappe d'intelligence artificielle"
  - "accès via CCDB"
  - "ordonnanceur Slurm"
  - "grand quota ajustable"
  - "Université de Toronto"
  - "Calcul de performance"
  - "NVIDIA H100 SXM 80GB"
  - "plateforme NVME VastData"
  - "Dell 750xa"
  - "capacité utilisable de 1.7Po"
  - "Infiniband HDR100"
  - "Calcul standard"
  - "NVIDIA L40S 48GB"

questions:
  - "Qui peut accéder à la grappe Killarney et quelles sont les étapes nécessaires pour obtenir cet accès ?"
  - "Quelles sont les spécifications matérielles des nœuds de calcul standard et de performance de Killarney, notamment en termes de CPU, mémoire, stockage et GPU ?"
  - "Quelles mesures de cybersécurité sont appliquées sur Killarney, notamment le géoblocage, et quelles en sont les implications pour les utilisateurs internationaux ?"
  - "Quels sont les différents espaces de stockage (/home, /scratch, /project) et leurs politiques de quota, sauvegarde et purge ?"
  - "Quels types d’interconnexions réseau sont déployés pour les nœuds de calcul standard et de performance, et quels débits offrent‑ils ?"
  - "Quel ordonnanceur de tâches est utilisé et comment les utilisateurs soumettent‑ils leurs travaux sur le système ?"
  - "Combien de nœuds sont prévus pour le calcul standard et quelles sont leurs spécifications principales (CPU, mémoire, stockage et GPU) ?"
  - "Quelle est la différence en nombre total de GPU entre le calcul standard et le calcul de performance, et quels modèles de GPU sont utilisés dans chaque cas ?"
  - "Quel type de stockage est attribué aux nœuds de calcul standard versus ceux de calcul de performance, et quelles sont leurs capacités respectives ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

| Caractéristique             | Valeur                                       |
| :------------------------- | :------------------------------------------- |
| Disponibilité              | 2025-06-09                                   |
| Nœud de connexion          | **killarney.alliancecan.ca**                 |
| Open OnDemand              | <https://ondemand.killarney.vectorinstitute.ai> |
| Collection Globus          | En préparation                               |
| Page d'état du système     | <https://status.alliancecan.ca/system/Killarney> |

**Killarney** est une grappe qui répond aux besoins de la communauté scientifique canadienne en intelligence artificielle. Elle est située à [l'Université de Toronto](https://www.utoronto.ca/) et gérée par [l'Institut Vecteur](https://vectorinstitute.ai/) et [SciNet](https://www.scinethpc.ca/). Son nom rappelle [le parc provincial Killarney](https://www.ontarioparks.ca/park/killarney/fr) qui se trouve près de la baie Georgienne, en Ontario.

Killarney fait partie de l'EIPIA, l'environnement informatique pancanadien de l'intelligence artificielle.

## Particularités

Killarney est présentement disponible pour les chercheuses principales et chercheurs principaux titulaires d'une chaire en intelligence artificielle (IACC) et affiliés à Vector, ainsi que celles et ceux qui sont dans un programme d'IA d'une université canadienne ou qui utilisent l'IA dans leurs travaux de recherche.

!!! attention "Listes de contrôle d'accès (ACL)"
    Les systèmes de fichiers distants de Killarney (`/home`, `/scratch`, etc.) sont montés via NFS v3, qui ne prend pas en charge les listes de contrôle d'accès (ACL); par conséquent, les commandes telles que `setfacl` ne sont pas prises en charge. Si vous devez partager des données avec des personnes qui ne font *pas* partie de votre groupe, veuillez envoyer un courriel à ops-help@vectorinstitute.ai pour demander la création d'un répertoire partagé.

## Accès

Pour demander l'accès :

*   [Demandez l'accès dans le portail CCDB](https://ccdb.alliancecan.ca/me/access_services) en vous assurant d'avoir [au moins une clé SSH enregistrée dans CCDB](../getting-started/ssh.md).
*   Les chercheuses principales et chercheurs principaux doivent obtenir de la part de leur établissement un RAP (*Resource Allocation Project*) de type AIP (*Artificial Intelligence Project*); le nom du projet sera préfixé de `aip-`.
*   Pour parrainer les personnes qui participent au projet RAP, la chercheuse principale ou le chercheur principal doit [demander l'accès à l'Environnement informatique pancanadien de l’IA (EIPIA)](https://ccdb.alliancecan.ca/paice/general_access_to_paice_systems).

Pour identifier les personnes que vous parrainez pour le projet :

1.  Faites afficher le tableau *Projet(s) avec allocation de ressources* dans CCDB.
2.  Cliquez sur le RAPI de votre projet AIP (préfixé `aip-`).
3.  Au bas de la page *Détails pour le projet*, cliquez sur *Gérer l'appartenance aux projets*.
4.  Entrez le ou les CCRI des personnes que vous parrainez.

!!! attention "Géoblocage"
    Dans le cadre de ses mesures de cybersécurité, **Vector applique le géoblocage** sur Killarney afin d'assurer l'intégrité et la sécurité. Vector restreint l'accès aux pays identifiés dans [Évaluation des cybermenaces nationales 2025-2026](https://www.cyber.gc.ca/fr/orientation/evaluation-cybermenaces-nationales-2025-2026) publié par le gouvernement du Canada.

## Matériel

| Type de calcul       | Nœuds | Modèle        | CPU                          | Cœurs | Mémoire système | Stockage   | GPU par nœud             | Total de GPU |
| :------------------- | :---- | :------------ | :--------------------------- | :---- | :-------------- | :--------- | :----------------------- | :----------- |
| Calcul standard      | 168   | Dell 750xa    | 2 x Intel Xeon Gold 6338     | 64    | 512 GB          | 350 GB SSD | 4 x NVIDIA L40S 48GB     | 672          |
| Calcul de performance | 10    | Dell XE9680   | 2 x Intel Xeon Gold 6442Y    | 48    | 2048 GB         | 800 GB NVMe | 8 x NVIDIA H100 SXM 80GB | 80           |

## Stockage

Le système de stockage est une plateforme NVME VastData avec une capacité utilisable de 1,7 Po.

### /home
*   Emplacement des répertoires personnels (`/home`).
*   [Quota fixe](../storage-and-data/storage_and_file_management.md#quotas-et-politiques) pour chaque répertoire.
*   Les demandes pour plus d'espace sont dirigées vers `/project`.
*   Sauvegarde quotidienne.

### /scratch
*   Conçu pour le stockage actif ou temporaire.
*   [Grand quota fixe](../storage-and-data/storage_and_file_management.md#quotas-et-politiques) par utilisateur.
*   Les données inactives sont [purgées](../storage-and-data/scratch_purging_policy.md).

### /project
*   [Grand quota ajustable](../storage-and-data/storage_and_file_management.md#quotas-et-politiques) par projet.
*   Sauvegarde quotidienne.

## Réseautique

*   Nœuds de calcul standard : Infiniband HDR100, débit de 100 Gbps
*   Nœuds de calcul de performance : 2 x HDR 200, débit agrégé de 400 Gbps

## Ordonnancement

L'ordonnanceur Slurm exécute les tâches soumises par les utilisateurs. Les commandes Slurm de base sont semblables à celles pour les autres systèmes nationaux.

## Logiciel

*   Pile logicielle de modules.
*   Pile logicielle standard de l'Alliance et logiciels particuliers à chaque grappe.