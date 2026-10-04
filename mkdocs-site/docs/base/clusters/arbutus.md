---
title: "Arbutus"
slug: "arbutus"
lang: "base"

source_wiki_title: "Arbutus"
source_hash: "af3c831a531e03558fad516404cf02e6"
last_synced: "2026-10-04T02:27:33.201522+00:00"
last_processed: "2026-10-04T03:03:25.415421+00:00"

tags:
  []

keywords:
  - "Arbutus IaaS cloud"
  - "NVidia H100 GPU"
  - "7 PB Ceph volume storage"
  - "Legacy and Renewal OpenStack dashboards"
  - "26 PB Ceph object storage"

questions:
  - "When is the Arbutus cloud expected to be available for users?"
  - "What types and total capacities of storage (volume, snapshot, and object) does Arbutus offer?"
  - "What are the primary hardware specifications of the compute nodes on Arbutus, including CPU, memory, GPU, and local SSD details?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

| Feature | Details |
| :------------------------------ | :------------------------------------------------------------------------------------------------------ |
| Availability | late spring 2026 |
| Legacy OpenStack dashboard | [https://arbutus.cloud.alliancecan.ca/](https://arbutus.cloud.alliancecan.ca/) |
| Renewal OpenStack dashboard | [https://arbutus.alliancecan.ca/auth/login/?next=/](https://arbutus.alliancecan.ca/auth/login/?next=/) |
| Globus endpoint | *to be determined* |
| Legacy Object Storage (S3 or Swift) | [https://object-arbutus.cloud.computecanada.ca/](https://object-arbutus.cloud.computecanada.ca/) |
| Renewal Object Storage (S3 or Swift) | `https://object-arbutus.alliancecan.ca/<tenant-id>:<bucket-name>/<object-name>` |

Arbutus is an Infrastructure-as-a-Service cloud hosted at the University of Victoria.

## Storage

*   7 PB of Volume and Snapshot [Ceph](https://en.wikipedia.org/wiki/Ceph_(software)) storage.
*   26 PB of Object/Shared Filesystem [Ceph](https://en.wikipedia.org/wiki/Ceph_(software)) storage.
*   3 PB of NVMe Volume and Snapshot [Ceph](https://en.wikipedia.org/wiki/Ceph_(software)) storage.

## Node characteristics

| Nodes | Cores | Available Memory | Storage | CPU | GPU |
| :---- | :---- | :--------------- | :------ | :-- | :-- |
| 338   | 96    | 768GB DDR5       | 1 x NVMe SSD, 7.68TB | 2 x Intel Platinum 8568Y+ 2.3GHz, 300MB cache | - |
| 22    | 96    | 1536GB DDR5      | 1 x NVMe SSD, 7.68TB | 2 x Intel Platinum 8568Y+ 2.3GHz, 300MB cache | - |
| 11    | 64    | 2048GB DDR5      | 1 x NVMe SSD, 7.68TB | 2 x Intel Platinum 6548Y+ 2.5GHz, 60MB cache | - |
| 16    | 48    | 1024GB DDR4      | 1 x NVMe SSD, 3.84TB | 2 x Intel Gold 6342 2.8 GHz, 36MB cache | 4 x NVidia H100 PCIe Gen5 (94GB) |
| 10    | 48    | 128GB DDR5       | 1 x NVMe SSD, 3.84TB | 2 x Intel Gold 6542Y 2.9 GHz, 60MB cache | 1 x NVidia L40s PCIe Gen4 (48GB) |

See [Cloud resources](../cloud/cloud_resources.md#arbutus-cloud) for current equipment summary.