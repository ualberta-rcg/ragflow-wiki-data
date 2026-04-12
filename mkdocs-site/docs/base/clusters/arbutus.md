---
title: "Arbutus"
slug: "arbutus"
lang: "base"

source_wiki_title: "Arbutus"
source_hash: "b4fa8ea7dceb3393a25843e77426b2d8"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:22:57.732570+00:00"

tags:
  []

keywords:
  - "Ceph storage"
  - "Node characteristics"
  - "Infrastructure-as-a-Service"
  - "University of Victoria"
  - "Arbutus cloud"

questions:
  - "What is the Arbutus cloud, where is it hosted, and when is it scheduled to become available?"
  - "What are the specific capacities and types of Ceph storage provided by the Arbutus infrastructure?"
  - "What are the hardware specifications regarding cores, memory, CPUs, and GPUs for the various nodes in the cluster?"
  - "What is the Arbutus cloud, where is it hosted, and when is it scheduled to become available?"
  - "What are the specific capacities and types of Ceph storage provided by the Arbutus infrastructure?"
  - "What are the hardware specifications regarding cores, memory, CPUs, and GPUs for the various nodes in the cluster?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

| Availability | late spring 2026 |
|---|---|
| OpenStack dashboard | [https://arbutus.cloud.alliancecan.ca](https://arbutus.cloud.alliancecan.ca) |
| Globus endpoint | *to be determined* |
| Object Storage (S3 or Swift) | [https://object-arbutus.cloud.computecanada.ca](https://object-arbutus.cloud.computecanada.ca/) |

Arbutus is an Infrastructure-as-a-Service cloud hosted at the University of Victoria.

## Storage
7 PB of Volume and Snapshot [Ceph](https://en.wikipedia.org/wiki/Ceph_(software)) storage.
26 PB of Object/Shared Filesystem [Ceph](https://en.wikipedia.org/wiki/Ceph_(software)) storage.
3 PB of NVMe Volume and Snapshot [Ceph](https://en.wikipedia.org/wiki/Ceph_(software)) storage.

## Node characteristics

| nodes | cores | available memory | storage | CPU | GPU |
|---|---|---|---|---|---|
| 338 | 96 | 768GB DDR5 | 1 x NVMe SSD, 7.68TB | 2 x Intel Platinum 8568Y+ 2.3GHz, 300MB cache | |
| 22 | 96 | 1536GB DDR5 | 1 x NVMe SSD, 7.68TB | 2 x Intel Platinum 8568Y+ 2.3GHz, 300MB cache | |
| 11 | 64 | 2048GB DDR5 | 1 x NVMe SSD, 7.68TB | 2 x Intel Platinum 6548Y+ 2.5GHz, 60MB cache | |
| 16 | 48 | 1024GB DDR4 | 1 x NVMe SSD, 3.84TB | 2 x Intel Gold 6342 2.8 GHz, 36MB cache | 4 x NVidia H100 PCIe Gen5 (94GB) |
| 10 | 48 | 128GB DDR5 | 1 x NVMe SSD, 3.84TB | 2 x Intel Gold 6542Y 2.9 GHz, 60MB cache | 1 x NVidia L40s PCIe Gen4 (48GB) |

See [Cloud resources](cloud-resources.md#arbutus-cloud) for current equipment summary.