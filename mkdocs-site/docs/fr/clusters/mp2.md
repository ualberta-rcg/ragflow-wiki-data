---
title: "Mp2/fr"
slug: "mp2"
lang: "fr"

source_wiki_title: "Mp2/fr"
source_hash: "bce11fd230e5cd1623e0ecf4879ba7b3"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T09:00:06.624783+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

!!! warning "Avertissement"
Mp2 est maintenant exclusive aux chercheurs de l'Université de Sherbrooke.

Mammouth-Mp2 est une grappe hétérogène et polyvalente conçue pour les calculs ordinaires; elle est située à l'[Université de Sherbrooke](http://www.usherbrooke.ca/).

| Propriété | Valeur |
|:---|:---|
| Disponibilité | Février 2012 - Avril 2020 |
| Nœud de connexion | **mp2.calculcanada.ca** |
| Point de chute Globus | **computecanada#mammouth** |
| Nœud de copie (rsync, scp, sftp,...) | **mp2.calculcanada.ca** |

## Particularités

*   Chaque tâche devrait être d'une durée d’au moins une heure (au moins cinq minutes pour les tâches de test) et un utilisateur ne peut avoir plus de 1000 tâches (en exécution et en attente) à la fois. La durée maximale d'une tâche est 7 jours (168 heures).
*   Pas de GPUs.

## Stockage

| Type de stockage | Détails |
|:---|:---|
| **HOME** <br> Système de fichiers Lustre <br> 79.6 To d’espace total | - Cet espace est limité et ne peut être étendu : vous devrez utiliser votre espace `project` pour les besoins de stockage importants.<br>- 50 Go d’espace et 500 000 fichiers par utilisateur.<br>- Une sauvegarde automatique est effectuée une fois par jour. |
| **SCRATCH** <br> Système de fichiers Lustre <br> 358.3 To d’espace total | - Vaste espace pour stocker les fichiers temporaires pendant les calculs.<br>- 20 To d’espace et 1 000 000 fichiers par utilisateur.<br>- Aucun système de sauvegarde automatique. |
| **PROJECT** <br> Système de fichiers Lustre <br> 716.6 To d’espace total | - Ce stockage est conçu pour le partage de données entre les membres d'un groupe et pour le stockage d'un volume important de données.<br>- 1 To d’espace et 500 000 fichiers par groupe.<br>- Aucun système de sauvegarde automatique. |

Pour les transferts de données par Globus, on devrait utiliser le point de chute `computecanada#mammouth`, alors que pour les outils comme rsync et scp, on peut utiliser un nœud de connexion.

## Réseautique haute performance

Le réseau Infiniband QDR (40 Gb/s) de Mellanox relie tous les nœuds de la grappe, non-bloquant pour 216 nœuds, 5:1 pour les autres.

## Types et caractéristiques des nœuds

| Quantité | Cœurs | Mémoire disponible | Type de CPU | Stockage | Type de GPU |
|:---|:---|:---|:---|:---|:---|
| 1588 | 24 | 31 GB ou 31744 MB | 12 cœurs/socket, 2 sockets/nœud. AMD Opteron Processor 6172 @ 2.1 GHz | Disque SATA de 1 To. | - |
| 20 | 48 | 251 GB ou 257024 MB | 12 cœurs/socket, 4 sockets/nœud. AMD Opteron Processor 6174 @ 2.2 GHz | Disque SATA de 1 To. | - |
| 2 | 48 | 503 GB ou 515072 MB | 12 cœurs/socket, 4 sockets/nœud. AMD Opteron Processor 6174 @ 2.2 GHz | Disque SATA de 1 To. | - |