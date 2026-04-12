---
title: "Mp2"
slug: "mp2"
lang: "base"

source_wiki_title: "Mp2"
source_hash: "79098b75171a390bc253e91b3826c284"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:31:35.672244+00:00"

tags:
  []

keywords:
  - "Mammouth-Mp2"
  - "Université de Sherbrooke"
  - "Grappe hétérogène"
  - "Nœuds de calcul"
  - "Système de fichiers Lustre"

questions:
  - "Quelles sont les restrictions concernant la durée et le nombre de tâches qu'un utilisateur peut soumettre sur la grappe Mammouth-Mp2 ?"
  - "Quelles sont les différences de capacité, d'utilisation et de politique de sauvegarde entre les espaces de stockage HOME, SCRATCH et PROJECT ?"
  - "Quelles sont les caractéristiques matérielles (cœurs, mémoire, processeurs) des différents types de nœuds de calcul disponibles ?"
  - "Quelles sont les restrictions concernant la durée et le nombre de tâches qu'un utilisateur peut soumettre sur la grappe Mammouth-Mp2 ?"
  - "Quelles sont les différences de capacité, d'utilisation et de politique de sauvegarde entre les espaces de stockage HOME, SCRATCH et PROJECT ?"
  - "Quelles sont les caractéristiques matérielles (cœurs, mémoire, processeurs) des différents types de nœuds de calcul disponibles ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

| Feature | Value |
|---|---|
| Availability | February 2012 - April 2020 |
| Login Node | **mp2.calculcanada.ca** |
| Globus Endpoint | **computecanada#mammouth** |
| Copy Node (rsync, scp, sftp,...) | **mp2.calculcanada.ca** |

!!! warning
    Mp2 is now exclusive to University of Sherbrooke researchers.

Mammouth-Mp2 is a heterogeneous, general-purpose cluster designed for ordinary computations; it is located at the [Université de Sherbrooke](http://www.usherbrooke.ca/).

## Features

* Each job should be at least one hour long (at least five minutes for test jobs), and a user cannot have more than 1000 jobs (running and pending) at once. The maximum job duration is 7 days (168 hours).
* No GPUs.

## Storage

| Storage Type | Details |
|---|---|
| HOME <br> Lustre File System <br> 79.6 TB Total Space | * This space is small and cannot be expanded; you will need to use your `project` space for large storage needs. <br> * 50 GB of space and 500K files per user. <br> * There is an automatic daily backup. |
| SCRATCH <br> Lustre File System <br> 358.3 TB Total Space | * Large space for storing temporary files during computations. <br> * 20 TB of space and 1M files per user. <br> * No automatic backup system. |
| PROJECT <br> Lustre File System <br> 716.6 TB Total Space | * This space is designed for data sharing among group members and for storing large amounts of data. <br> * 1 TB of space and 500K files per group. <br> * No automatic backup system. |

For data transfers via Globus, the endpoint `computecanada#mammouth` should be used, while for tools like rsync and scp, a login node can be used.

## High-Performance Networking

The Mellanox Infiniband QDR (40 Gb/s) network connects all cluster nodes, non-blocking for 216 nodes, and 5:1 oversubscribed for the rest.

## Node Types and Characteristics

| Quantity | Cores | Available Memory | CPU Type | Storage | GPU Type |
|---|---|---|---|---|---|
| 1588 | 24 | 31 GB or 31744 MB | 12 cores/socket, 2 sockets/node. AMD Opteron Processor 6172 @ 2.1 GHz | 1TB SATA disk. | - |
| 20 | 48 | 251 GB or 257024 MB | 12 cores/socket, 4 sockets/node. AMD Opteron Processor 6174 @ 2.2 GHz | 1TB SATA disk. | - |
| 2 | 48 | 503 GB or 515072 MB | 12 cores/socket, 4 sockets/node. AMD Opteron Processor 6174 @ 2.2 GHz | 1TB SATA disk. | - |