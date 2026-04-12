---
title: "Mp2/fr"
slug: "mp2"
lang: "fr"

source_wiki_title: "Mp2/fr"
source_hash: "bce11fd230e5cd1623e0ecf4879ba7b3"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:32:15.438458+00:00"

tags:
  []

keywords:
  - "Mammouth-Mp2"
  - "grappe hétérogène"
  - "Université de Sherbrooke"
  - "système de fichiers Lustre"
  - "réseau Infiniband"

questions:
  - "Quelles sont les règles et les limites concernant la durée et la quantité de tâches qu'un utilisateur peut exécuter sur la grappe Mammouth-Mp2 ?"
  - "Quelles sont les différences de capacité, d'utilisation et de politique de sauvegarde entre les espaces de stockage HOME, SCRATCH et PROJECT ?"
  - "Quelles sont les caractéristiques techniques du réseau et des différents types de nœuds de calcul disponibles sur cette grappe ?"
  - "Quelles sont les règles et les limites concernant la durée et la quantité de tâches qu'un utilisateur peut exécuter sur la grappe Mammouth-Mp2 ?"
  - "Quelles sont les différences de capacité, d'utilisation et de politique de sauvegarde entre les espaces de stockage HOME, SCRATCH et PROJECT ?"
  - "Quelles sont les caractéristiques techniques du réseau et des différents types de nœuds de calcul disponibles sur cette grappe ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

| Caractéristique | Valeur |
|---|---|
| Disponibilité | Février 2012 - Avril 2020 |
| Nœud de connexion | `mp2.calculcanada.ca` |
| Point de chute Globus | `computecanada#mammouth` |
| Nœud de copie (rsync, scp, sftp,...) | `mp2.calculcanada.ca` |

!!! attention "Note importante"
    **Mp2 est maintenant exclusive aux chercheurs de l'Université de Sherbrooke.**

Mammouth-Mp2 est une grappe hétérogène et polyvalente conçue pour les calculs ordinaires; elle est située à l'[Université de Sherbrooke](http://www.usherbrooke.ca/).

## Particularités

*   Chaque tâche devrait être d'une durée d’au moins une heure (au moins cinq minutes pour les tâches de test) et un utilisateur ne peut avoir plus de 1000 tâches (en exécution et en attente) à la fois. La durée maximale d'une tâche est 7 jours (168 heures).
*   Pas de GPUs.

## Stockage

| Type de stockage | Description et caractéristiques |
|---|---|
| **HOME** <br> Système de fichiers Lustre <br> 79.6 To d’espace au total | *   Cet espace est petit et ne peut pas être agrandi : vous devrez utiliser votre espace `project` pour les grands besoins en stockage.<br>*   50 Go d’espace et 500K fichiers par utilisateur.<br>*   Il y a une sauvegarde automatique une fois par jour. |
| **SCRATCH** <br> Système de fichiers Lustre <br> 358.3 To d’espace au total | *   Grand espace pour stocker les fichiers temporaires pendant les calculs.<br>*   20 To d’espace et 1M fichiers par utilisateur.<br>*   Pas de système de sauvegarde automatique. |
| **PROJECT** <br> Système de fichiers Lustre <br> 716.6 To d’espace au total | *   Cet espace est conçu pour le partage de données entre membres d'un groupe et pour le stockage de beaucoup de données.<br>*   1 To d’espace et 500K fichiers par groupe.<br>*   Pas de système de sauvegarde automatique. |

Pour les transferts de données par Globus, on devrait utiliser le point de chute `computecanada#mammouth`, alors que pour les outils comme rsync et scp, on peut utiliser un nœud de connexion.

## Réseautique haute performance

Le réseau Infiniband QDR (40 Gb/s) de Mellanox relie tous les nœuds de la grappe, non-bloquant sur 216 nœuds, 5:1 pour le reste.

## Types et caractéristiques des nœuds

| Quantité | Cœurs | Mémoire disponible | Type de CPU | Stockage | Type de GPU |
|---|---|---|---|---|---|
| 1588 | 24 | 31 GB ou 31744 MB | 12 cores/socket, 2 sockets/node. AMD Opteron Processor 6172 @ 2.1 GHz | Disque SATA de 1 To | - |
| 20 | 48 | 251 GB ou 257024 MB | 12 cores/socket, 4 sockets/node. AMD Opteron Processor 6174 @ 2.2 GHz | Disque SATA de 1 To | - |
| 2 | 48 | 503 GB ou 515072 MB | 12 cores/socket, 4 sockets/node. AMD Opteron Processor 6174 @ 2.2 GHz | Disque SATA de 1 To | - |