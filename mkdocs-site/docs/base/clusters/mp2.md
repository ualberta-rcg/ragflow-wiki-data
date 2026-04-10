---
title: "Mp2"
slug: "mp2"
lang: "base"

source_wiki_title: "Mp2"
source_hash: "79098b75171a390bc253e91b3826c284"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T08:59:22.634847+00:00"

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

| Key | Value |
|---|---|
| Availability | February 2012 - April 2020 |
| Login Node | **mp2.calculcanada.ca** |
| Globus Endpoint | **computecanada#mammouth** |
| Copy Node (rsync, scp, sftp,...) | **mp2.calculcanada.ca** |

!!! warning
    Mp2 is now exclusive to researchers at the Université de Sherbrooke.

Mammouth-Mp2 is a heterogeneous and versatile cluster designed for general computations; it is located at the [Université de Sherbrooke](http://www.usherbrooke.ca/).

## Features

*   Each job should be at least one hour long (at least five minutes for test jobs), and a user cannot have more than 1000 jobs (running and pending) at a time. The maximum job duration is 7 days (168 hours).
*   No GPUs.

## Storage

| Storage Type | Details |
|---|---|
| HOME <br> Lustre Filesystem <br> 79.6 TB total space | !!! note "Usage Recommendation"
    This space is small and cannot be expanded; you should use your `project` space for large storage needs.
    *   50 GB space and 500K files per user.
    *   Automatic daily backup. |
| SCRATCH <br> Lustre Filesystem <br> 358.3 TB total space | *   Large space for storing temporary files during computations.
    *   20 TB space and 1M files per user.
    !!! warning "No Automatic Backup"
        There is no automatic backup system for SCRATCH. |
| PROJECT <br> Lustre Filesystem <br> 716.6 TB total space | *   This space is designed for data sharing among group members and for storing large amounts of data.
    *   1 TB space and 500K files per group.
    !!! warning "No Automatic Backup"
        There is no automatic backup system for PROJECT. |

For data transfers via Globus, the `computecanada#mammouth` endpoint should be used, while for tools like rsync and scp, a login node can be used.

## High-Performance Networking

The Mellanox Infiniband QDR (40 Gb/s) network connects all cluster nodes, non-blocking on 216 nodes, 5:1 for the remainder.

## Node Types and Characteristics

| Quantity | Cores | Available Memory | CPU Type | Storage | GPU Type |
|:---|:---|:---|:---|:---|:---|
| 1588 | 24 | 31 GB or 31744 MB | 12 cores/socket, 2 sockets/node. AMD Opteron Processor 6172 @ 2.1 GHz | 1TB SATA disk. | - |
| 20 | 48 | 251 GB or 257024 MB | 12 cores/socket, 4 sockets/node. AMD Opteron Processor 6174 @ 2.2 GHz | 1TB SATA disk. | - |
| 2 | 48 | 503 GB or 515072 MB | 12 cores/socket, 4 sockets/node. AMD Opteron Processor 6174 @ 2.2 GHz | 1TB SATA disk. | - |