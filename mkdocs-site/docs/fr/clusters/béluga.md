---
title: "Béluga/fr"
slug: "béluga"
lang: "fr"

source_wiki_title: "Béluga/fr"
source_hash: "25aed4b043bff99b4229b51fa10dbc4a"
last_synced: "2026-08-07T19:46:17.777436+00:00"
last_processed: "2026-08-07T22:25:07.146005+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: true
  qa_generated: false
---

!!! attention "Attention"
Béluga a été remplacée par la nouvelle grappe nommée [Rorqual](rorqual.md).

| Disponibilité : | mars 2019 à juin 2026 |
| :-------------- | :-------------------- |
| Nœud de connexion : | **beluga.alliancecan.ca** |
| Collection Globus : | [computecanada#beluga-dtn](https://app.globus.org/file-manager?origin_id=278b9bfe-24da-11e9-9fa2-0a06afd4a22e) |
| Nœud de copie (rsync, scp, sftp,...) : | **beluga.alliancecan.ca** |
| Portail : | <https://portail.beluga.calculquebec.ca/> |

Béluga est une grappe hétérogène et polyvalente conçue pour les calculs ordinaires; elle est située à l'[École de technologie supérieure](http://www.etsmtl.ca/). Son nom rappelle la [baleine béluga](https://fr.wikipedia.org/wiki/B%C3%A9luga_(c%C3%A9tac%C3%A9)), un mammifère marin vivant dans les eaux du fleuve Saint-Laurent.

## Particularités

Notre politique veut que les nœuds de calcul de Béluga n'aient pas accès à l'internet. Pour y faire exception, contactez le [soutien technique](../support/technical_support.md) en expliquant ce dont vous avez besoin et pourquoi. Notez que l'outil `crontab` n'est pas offert.

Chaque tâche devrait être d'une durée d’au moins une heure (au moins cinq minutes pour les tâches de test) et un utilisateur ne peut avoir plus de 1000 tâches (en exécution et en attente) à la fois. La durée maximale d'une tâche est 7 jours (168 heures).

## Stockage

| Type d'espace | Description |
| :------------ | :---------- |
| HOME <br> Système de fichiers Lustre, 105 To d’espace au total | * Cet espace est petit et ne peut pas être agrandi : vous devrez utiliser votre espace `project` pour les grands besoins en stockage.<br>* Petits [quotas](../storage-and-data/storage_and_file_management.md#quotas-et-politiques) fixes par utilisateur<br>* Il y a une sauvegarde automatique une fois par jour. |
| SCRATCH <br> Système de fichiers Lustre, 2.6 Po d’espace au total | * Grand espace pour stocker les fichiers temporaires pendant les calculs.<br>* Pas de système de sauvegarde automatique.<br>* Grands [quotas](../storage-and-data/storage_and_file_management.md#quotas-et-politiques) fixes par utilisateur<br>* Il y a une [purge automatique](../storage-and-data/scratch_purging_policy.md) des vieux fichiers de cet espace. |
| PROJECT <br> Système de fichiers Lustre, 25 Po d’espace au total | * Cet espace est conçu pour le partage de données entre membres d'un groupe et pour le stockage de beaucoup de données.<br>* Grands [quotas](../storage-and-data/storage_and_file_management.md#quotas-et-politiques) ajustables par projet<br>* Il y a une sauvegarde automatique une fois par jour. |

Pour les transferts de données par Globus, on devrait utiliser le point de chute `computecanada#beluga-dtn`, alors que pour les outils comme rsync et scp, on peut utiliser un nœud de connexion.

## Réseautique haute performance

Le réseau Infiniband EDR (100 Gb/s) de Mellanox relie tous les nœuds de la grappe. Un commutateur central de 324 ports rassemble les connexions des îlots avec un facteur de blocage maximum de 5:1. Les serveurs de stockage sont branchés avec une interconnexion non bloquante. L’architecture permet de multiples tâches parallèles avec jusqu’à 640 cœurs (voire plus) grâce à une réseautique non bloquante. Pour les tâches plus imposantes, le facteur de blocage est de 5:1; même pour les tâches exécutées sur plusieurs îlots, l’interconnexion est de haute performance.

## Caractéristiques des nœuds

!!! warning "Note importante"
    En date du 31 juillet 2025, tous les nœuds ci-dessous sont éteints.

| Nœuds | Cœurs | Mémoire disponible | CPU | Stockage | GPU |
| :---- | :---- | :----------------- | :-- | :------- | :-- |
| 160   | 40    | 92G ou 95000M      | 2 x Intel Gold 6148 Skylake @ 2.4 GHz | 1 x SSD de 480G | - |
| 579   | 40    | 186G ou 191000M    | 2 x Intel Gold 6148 Skylake @ 2.4 GHz | 1 x SSD de 480G | - |
| 10    | 40    | 186G ou 191000M    | 2 x Intel Gold 6148 Skylake @ 2.4 GHz | 6 x SSD de 480G | - |
| 51    | 40    | 752G ou 771000M    | 2 x Intel Gold 6148 Skylake @ 2.4 GHz | 1 x SSD de 480G | - |
| 2     | 40    | 752G ou 771000M    | 2 x Intel Gold 6148 Skylake @ 2.4 GHz | 6 x SSD de 480G | - |
| 172   | 40    | 186G ou 191000M    | 2 x Intel Gold 6148 Skylake @ 2.4 GHz | 1 x SSD NVMe de 1.6T | 4 x NVidia V100SXM2 (mémoire 16G), connectés via NVLink |

*   Pour obtenir un plus grand espace `$SLURM_TMPDIR`, il faut demander `--tmp=xG`, où `x` est une valeur entre 350 et 2490.

## Suivi de vos tâches

Depuis l'ancien portail [Metrix](../software/metrix.md) de Béluga, il était possible de suivre les tâches de calculs CPU comme GPU en temps "réel" ou passées afin de maximiser l'utilisation des ressources et diminuer les temps d'attentes dans la file. On pouvait voir pour chaque tâche :

*   l'utilisation des cœurs de calcul;
*   la mémoire utilisée;
*   l'utilisation de GPUs;

Il est important d'utiliser les ressources allouées et de rectifier vos demandes lorsque les ressources de calculs sont peu ou pas utilisées. Par exemple, si vous demandez quatre cœurs (CPU) mais n'en utilisez qu'un seul, vous devez ajuster votre fichier de soumission en conséquence.