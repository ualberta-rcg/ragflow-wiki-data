---
title: "Vulcan/fr"
slug: "vulcan"
lang: "fr"

source_wiki_title: "Vulcan/fr"
source_hash: "a5926a216f4ad9313eb40e55775cf4a2"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:51:50.703764+00:00"

tags:
  []

keywords:
  - "Ordonnanceur Slurm"
  - "service d'accès rapide"
  - "Pile logicielle"
  - "allocation de ressources"
  - "sauvegarde quotidienne"
  - "intelligence artificielle"
  - "calcul informatique de pointe"
  - "grappe de calcul"
  - "ECPIA"
  - "système de stockage"
  - "/scratch"
  - "Stockage"
  - "Réseautique"
  - "Vulcan"

questions:
  - "Qu'est-ce que la grappe Vulcan et à quel type de recherche est-elle spécifiquement destinée ?"
  - "Quelles sont les étapes et les conditions requises pour obtenir l'accès au système et pouvoir y soumettre une tâche ?"
  - "Quelles sont les spécifications matérielles (nœuds, processeurs, GPU) et les caractéristiques du système de stockage de Vulcan ?"
  - "Quelles sont les différences de caractéristiques et de politiques de gestion entre les espaces de stockage /scratch et /project ?"
  - "Quelle technologie réseau est utilisée pour interconnecter les nœuds du système ?"
  - "Quel ordonnanceur gère l'exécution des tâches et de quoi est composée la pile logicielle disponible ?"
  - "Quels sont les deux moyens mentionnés pour obtenir l'accès aux ressources de calcul informatique de pointe ?"
  - "Vers quel répertoire spécifique les utilisateurs doivent-ils se diriger pour demander davantage d'espace de stockage ?"
  - "Quelle est la fréquence de sauvegarde indiquée pour l'espace de projet et quel autre répertoire de stockage est mentionné ?"
  - "Quelles sont les différences de caractéristiques et de politiques de gestion entre les espaces de stockage /scratch et /project ?"
  - "Quelle technologie réseau est utilisée pour interconnecter les nœuds du système ?"
  - "Quel ordonnanceur gère l'exécution des tâches et de quoi est composée la pile logicielle disponible ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

| Caractéristique | Valeur |
| :---------------- | :----- |
| Disponibilité     | 15 avril 2025 |
| Nœud de connexion | **vulcan.alliancecan.ca** |
| Collection Globus | [Vulcan Globus v5](https://app.globus.org/file-manager?origin_id=97bda3da-a723-4dc0-ba7e-728f35183b43) |
| État du système   | [https://status.alliancecan.ca/system/Vulcan](https://status.alliancecan.ca/system/Vulcan) |
| Portail           | [https://portal.vulcan.alliancecan.ca](https://portal.vulcan.alliancecan.ca) |

Vulcan est une grappe au service de la communauté scientifique canadienne en intelligence artificielle. Elle est située à l'Université de l'Alberta et est gérée par l'Université de l'Alberta et [Amii](https://fr.amii.ca/). La grappe porte le nom de la ville de Vulcan située dans le sud de l'Alberta.

Vulcan fait partie de l'ECPIA, l'environnement de calcul pancanadien pour l'intelligence artificielle.

## Politiques spécifiques au site

!!! note "Accès à Internet"
    L'accès à Internet n'est généralement pas disponible à partir des nœuds de calcul. Un proxy Squid, disponible mondialement, est activé par défaut avec certains domaines sur la liste blanche. Contactez le [soutien technique](technical-support.md) si vous ne parvenez pas à vous connecter à un domaine et nous évaluerons son ajout à la liste blanche.

La durée maximale d'une tâche est de sept jours.

Vulcan est présentement disponible à tous les chercheurs et chercheuses dont la recherche porte sur l'intelligence artificielle ou comporte des méthodes d'IA.

## Accès

Pour vous connecter à Vulcan, [demandez l'accès dans le portail CCDB](https://ccdb.alliancecan.ca/me/access_services).

Pour pouvoir soumettre une tâche, vous devez être membre d'un projet RAP (*Resource Allocation Project*) préfixé `aip-`. Si vous êtes une chercheuse principale ou un chercheur principal et que vous n'avez pas de projet, [demandez l'accès à l'Environnement informatique pancanadien de l’IA (EIPIA)](https://ccdb.alliancecan.ca/paice/general_access_to_paice_systems).

Si vous êtes chercheuse principale ou chercheur principal et que vous parrainez d'autres personnes, vous devrez les ajouter à votre RAPI.

*   Sur la page d'accueil de CCDB ([https://ccdb.alliancecan.ca](https://ccdb.alliancecan.ca)), faites afficher le tableau *Projet d'allocation de ressources*.
*   Localisez votre projet AIP (préfixe `aip-`) et cliquez dessus pour faire afficher la page de gestion.
*   Au bas de la page, cliquez sur *Gérer l'appartenance au projet*.
*   Entrez le CCRI de la personne dans la section *Ajouter des membres*.

## Matériel

| Nœuds | Modèle      | CPU                       | Cœurs | Mémoire système | GPU par nœud        | Total de GPU |
| :---- | :---------- | :------------------------ | :---- | :-------------- | :------------------ | :----------- |
| 252   | Dell R760xa | 2 x Intel Xeon Gold 6448Y | 64    | 512 GB          | 4 x NVIDIA L40S 48GB | 1800         |

## Système de stockage

Le système de stockage est une combinaison de flash NVMe et HDD sur la plateforme Dell PowerScale, avec une capacité utilisable de 5PB. Les espaces `/home`, `/scratch` et `/project` sont sur le même système PowerScale.

| Répertoire | Caractéristiques |
| :--------- | :--------------- |
| **`/home`** |
    * Emplacement des répertoires /home
    * [Quota fixe](storage-and-file-management.md#quotas-et-politiques) pour chaque répertoire
    * N'est pas alloué via le [service d'accès rapide](https://alliancecan.ca/fr/services/calcul-informatique-de-pointe/acces-aux-ressources/service-dacces-rapide) ou le [concours pour l'allocation de ressources](https://alliancecan.ca/fr/services/calcul-informatique-de-pointe/acces-aux-ressources/concours-pour-lallocation-de-ressources); les demandes pour plus d'espace sont dirigées vers `/project`
    * Sauvegarde quotidienne
| **`/scratch`** |
    * Stockage actif ou temporaire (`/scratch`)
    * N'est pas alloué
    * Grand [quota fixe](storage-and-file-management.md#quotas-et-politiques) par utilisateur
    * Les données inactives sont [purgées](scratch-purging-policy.md)
| **`/project`** |
    * Grand [quota ajustable](storage-and-file-management.md#quotas-et-politiques), par projet
    * Sauvegarde quotidienne

## Réseautique

Les nœuds sont interconnectés via Ethernet 100Gbps avec le protocole RoCE (RDMA over Converged Ethernet) activé.

## Ordonnancement

L'ordonnanceur Slurm exécute les tâches soumises à Vulcan. Les commandes Slurm de base sont semblables à celles pour les autres systèmes nationaux.

## Logiciel

*   Pile logicielle de modules.
*   Pile logicielle standard de l'Alliance et logiciels particuliers à la grappe.