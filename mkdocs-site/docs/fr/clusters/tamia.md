---
title: "TamIA/fr"
slug: "tamia"
lang: "fr"

source_wiki_title: "TamIA/fr"
source_hash: "5ab1aaf610885dae6b97fb05af3eec8a"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:48:19.422581+00:00"

tags:
  []

keywords:
  - "Transferts de données"
  - "temps réel"
  - "Réseau InfiniBand"
  - "portail"
  - "GPU H200"
  - "Quotas fixes"
  - "utilisation des ressources"
  - "tâches de calcul"
  - "Système de fichiers Lustre"
  - "Tâches GPU"
  - "GPU H100"
  - "options Slurm"
  - "stockage"
  - "nœuds de calcul"
  - "Caractéristiques des nœuds"
  - "grappe de calcul"
  - "tamIA"
  - "Suivi de vos tâches"
  - "Espace HOME"
  - "Sauvegarde automatique"
  - "intelligence artificielle"
  - "cœurs de calcul"
  - "Espace project"

questions:
  - "Qu'est-ce que la grappe de calcul tamIA et à quelle communauté scientifique est-elle spécifiquement destinée ?"
  - "Quelles sont les restrictions techniques et les limites d'utilisation (comme l'accès à internet, les logiciels interdits ou la durée des tâches) imposées sur cette grappe ?"
  - "Quelle est la procédure complète permettant à un chercheur d'obtenir l'accès à tamIA et de parrainer d'autres membres ?"
  - "Quelles sont les principales différences entre les espaces de stockage SCRATCH et PROJECT en matière de sauvegarde et de quotas ?"
  - "Comment le réseau haute performance InfiniBand est-il structuré pour relier les nœuds de calcul et les GPU ?"
  - "Quelles options Slurm doivent être utilisées pour soumettre et assigner des tâches sur les nœuds équipés de GPU H100 ou H200 ?"
  - "Quelle alternative est recommandée pour les grands besoins en stockage étant donné que l'espace HOME ne peut pas être agrandi ?"
  - "Quelle est la politique concernant les quotas attribués aux utilisateurs dans cet espace ?"
  - "Quand les sauvegardes automatiques seront-elles mises en place pour ce système de fichiers ?"
  - "Comment les tâches GPU sont-elles assignées sur les serveurs selon le texte ?"
  - "Quelles options Slurm faut-il utiliser pour exécuter une tâche sur un nœud unique avec des GPU H100 ou H200 ?"
  - "Quelle est la syntaxe requise pour configurer les GPU lors de l'exécution de tâches réparties sur plusieurs nœuds ?"
  - "Quel est l'objectif principal du suivi des tâches de calcul sur le portail ?"
  - "Quelles sont les informations spécifiques qu'il est possible de visualiser pour une tâche donnée ?"
  - "Pourquoi est-il important pour les utilisateurs d'ajuster leurs demandes de ressources dans leur fichier de soumission ?"
  - "Quel est l'objectif principal du suivi des tâches de calcul sur le portail ?"
  - "Quelles sont les informations spécifiques qu'il est possible de visualiser pour une tâche donnée ?"
  - "Pourquoi est-il important pour les utilisateurs d'ajuster leurs demandes de ressources dans leur fichier de soumission ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

| Type                 | Valeur                                                                                           |
| :------------------- | :----------------------------------------------------------------------------------------------- |
| Disponibilité        | **31 mars 2025**                                                                                 |
| Nœud de connexion    | **tamia.alliancecan.ca**                                                                         |
| Nœud d'automatisation | [robot.tamia.ecpia.ca](../getting-started/automation_in_the_context_of_multifactor_authentication.md)               |
| Collection Globus    | [Serveur Globus v5 de TamIA](https://app.globus.org/file-manager?origin_id=72c3bca0-9281-4742-b066-333ba0fdef72) |
| Nœud de copie (rsync, scp, sftp,...) | **tamia.alliancecan.ca**                                                                         |
| Portail              | [https://portail.tamia.ecpia.ca/](https://portail.tamia.ecpia.ca/)                                |

tamIA est une grappe dédiée aux besoins de la communauté scientifique canadienne en matière d'intelligence artificielle. tamIA est située à [l'Université Laval](http://www.ulaval.ca/) et est cogérée avec [Mila](https://mila.quebec/) et [Calcul Québec](https://calculquebec.ca/). Son nom rappelle le [tamia](https://fr.wikipedia.org/wiki/Tamia), un mammifère rongeur présent en Amérique du Nord.

Cette grappe fait partie de [l'environnement de calcul pancanadien de l’IA (ECPIA)](https://alliancecan.ca/fr/services/calcul-informatique-de-pointe/environnement-informatique-pancanadien-de-lia-eipia).

## Particularités

!!! warning "Accès Internet restreint"
    Les nœuds de calcul de tamIA n'ont pas accès à l'Internet. Pour y faire exception, veuillez joindre le [soutien technique](../support/technical_support.md) en expliquant ce dont vous avez besoin et pourquoi.

!!! warning "Restriction sur VSCode"
    L'environnement de développement intégré [VSCode](https://code.visualstudio.com/) est **interdit** sur les nœuds **frontaux** (*login nodes*) en raison de sa lourde charge. Il est cependant autorisé sur les nœuds de calcul.

!!! note "Restrictions générales"
    * L'outil `crontab` n'est pas offert.
    * Chaque tâche devrait durer au moins une heure (au moins cinq minutes pour les tâches de test).
    * Vous ne pouvez pas avoir plus de 1000 tâches (en exécution et en attente) à la fois.
    * La durée maximale d'une tâche est d'une journée (24 heures).
    * Chaque tâche doit utiliser tous les GPU des serveurs alloués (soit 4 pour les H100 et 8 pour les H200).

## Accès

Pour accéder à la grappe de calcul, chaque chercheuse ou chercheur doit [compléter une demande d'accès dans la CCDB](https://ccdb.alliancecan.ca/me/access_services). L'accès effectif à la grappe peut prendre jusqu'à une heure après avoir complété la demande d'accès. Ensuite, une [déclaration de l'utilisation envisagée de l'intelligence artificielle](https://ccdb.alliancecan.ca/paice/general_access_to_paice_systems) doit être soumise.

Les chercheuses et chercheurs principaux admissibles sont membres d'un RAP de type AIP (préfixe `aip-`).

La procédure pour parrainer d'autres chercheuses et chercheurs est la suivante :

1.  Sur la **[page d'accueil de la CCDB](https://ccdb.alliancecan.ca/)**, consulter la table *Projet avec allocation de ressources*;
2.  Chercher le RAPI du projet `aip-` et cliquer dessus pour être redirigé vers la page de gestion du RAP;
3.  En bas de la page de gestion du RAP, cliquer sur **Gérer l'appartenance aux projets**;
4.  Dans la section *Ajouter des membres*, entrer le CCRI du membre à ajouter.

La grappe de calcul est accessible uniquement à partir du Canada.

## Stockage

| Type de stockage                     | Détails                                                                                                                                                                                                                                                                                                                             |
| :----------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **HOME**<br>Système de fichiers Lustre | * Cet espace est petit et ne peut pas être agrandi; vous devrez utiliser votre espace `project` pour les grands besoins en stockage.<br>* Petits [quotas](../storage-and-data/storage_and_file_management.md#quotas-et-politiques) fixes par utilisateur.<br>* Il n'y a actuellement aucune sauvegarde automatique. (Planifié pour le printemps 2026) |
| **SCRATCH**<br>Système de fichiers Lustre | * Grand espace pour stocker les fichiers temporaires pendant les calculs.<br>* Pas de système de sauvegarde automatique.<br>* Grands [quotas](../storage-and-data/storage_and_file_management.md#quotas-et-politiques) fixes par utilisateur.<br>* Il y a une [purge automatique](../storage-and-data/scratch_purging_policy.md) des vieux fichiers dans cet espace. |
| **PROJECT**<br>Système de fichiers Lustre | * Cet espace est conçu pour le partage de données entre membres d'un groupe et pour le stockage d'une grande quantité de données.<br>* Grands [quotas](../storage-and-data/storage_and_file_management.md#quotas-et-politiques) ajustables par projet.<br>* Il y a une sauvegarde automatique une fois par jour.                        |

Au tout début de la présente page, un tableau indique plusieurs adresses de connexion. Pour les transferts de données par [Globus](../getting-started/globus.md), il faut utiliser le **Point de chute Globus**. Par contre, pour les outils comme [rsync](../getting-started/transferring_data.md#rsync) et [scp](../getting-started/transferring_data.md#scp), il faut utiliser l'adresse du **Nœud de copie**.

## Réseautique haute performance

Le réseau [InfiniBand](https://fr.wikipedia.org/wiki/Bus_InfiniBand) [NDR de Nvidia](https://www.nvidia.com/en-us/networking/quantum2/) relie tous les nœuds de la grappe. Chaque GPU est connecté à un port NDR200 via une carte Nvidia ConnectX-7. Chaque serveur a donc 4 ou 8 ports NDR200 connectés à la fabrique InfiniBand.

Le réseau InfiniBand est non bloquant pour les serveurs de calcul et est composé de deux étages de commutateurs disposés dans une topologie "fat-tree". Le stockage et les nœuds de calcul sont reliés via 4 ou 8 connexions à 400 Gb/s au cœur du réseau.

## Caractéristiques des nœuds

| Nœuds | Cœurs | Mémoire disponible | CPU                                                                                                                       | Stockage          | GPU                                                                                                              |
| :---- | :---- | :----------------- | :------------------------------------------------------------------------------------------------------------------------ | :---------------- | :--------------------------------------------------------------------------------------------------------------- |
| 12    | 64    | 1024 GB            | 2 x [Intel Xeon Gold 6448Y 2,1 GHz, 32C](https://www.intel.com/content/www/us/en/products/sku/232384/intel-xeon-gold-6448y-processor-60m-cache-2-10-ghz/specifications.html) | 1 x SSD de 7.68 TB | 8 x [NVIDIA HGX H200](https://www.nvidia.com/en-us/data-center/h200/) SXM 141 GB HBM3 700W, connectés via NVLink |
| 53    | 48    | 512 GB             | 2 x [Intel Xeon Gold 6442Y 2,6 GHz, 24C](https://www.intel.com/content/www/us/en/products/sku/232380/intel-xeon-gold-6442y-processor-60m-cache-2-60-ghz/specifications.html) | 1 x SSD de 7.68 TB | 4 x [NVIDIA HGX H100](https://www.nvidia.com/en-us/data-center/h100/) SXM 80 GB HBM3 700W, connectés via NVLink  |
| 8     | 64    | 512 GB             | 2 x [Intel Xeon Gold 6438M 2.2G, 32C/64T](https://www.intel.com/content/www/us/en/products/sku/232398/intel-xeon-gold-6438m-processor-60m-cache-2-20-ghz/specifications.html) | 1 x SSD de 7.68 TB | Aucun                                                                                                            |

### Environnements logiciels disponibles

[L'environnement logiciel standard `StdEnv/2023`](../programming/standard_software_environments.md) est l'environnement par défaut sur tamIA.

### Tâches GPU

Les tâches sont assignées sur les nœuds complets. Utilisez l'une des options Slurm suivantes :

*   Pour une tâche sur un nœud avec GPU H100 : `--gpus=h100:4`
*   Pour une tâche sur un nœud avec GPU H200 : `--gpus=h200:8`
*   Pour les tâches avec plusieurs nœuds, utiliser `--gpus-per-nodes=h100:4` ou `--gpus-per-nodes=h200:8`.

## Suivi de vos tâches

Depuis le [portail](https://portail.tamia.ecpia.ca/), vous pourrez suivre vos tâches de calcul GPU comme CPU **en temps réel** ou celles passées, afin de maximiser l'utilisation des ressources et de diminuer vos temps d'attente dans la file.

Vous pourrez notamment visualiser pour une tâche :

*   l'utilisation des cœurs de calcul;
*   la mémoire utilisée;
*   l'utilisation de GPU.

Il est important d'utiliser les ressources allouées et de rectifier vos demandes lorsque les ressources de calcul sont peu ou pas utilisées.
Par exemple, si vous demandez quatre cœurs (CPU) mais n'en utilisez qu'un seul, vous devez ajuster votre fichier de soumission en conséquence.