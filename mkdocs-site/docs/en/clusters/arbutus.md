---
title: "Arbutus/en"
slug: "arbutus"
lang: "en"

source_wiki_title: "Arbutus/en"
source_hash: "bcc65e0e2499e1478b62d970e9fc2d34"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T04:32:23.525187+00:00"

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

!!! info "Arbutus Overview"
*   **Availability**: late spring 2026
*   **OpenStack dashboard**: [https://arbutus.cloud.alliancecan.ca](https://arbutus.cloud.alliancecan.ca)
*   **Globus endpoint**: *to be determined*
*   **Object Storage (S3 or Swift)**: [https://object-arbutus.cloud.computecanada.ca/](https://object-arbutus.cloud.computecanada.ca/)

Arbutus is an Infrastructure-as-a-Service cloud hosted at the University of Victoria.

## Storage
*   7 PB of Volume and Snapshot [Ceph](https://en.wikipedia.org/wiki/Ceph_(software)) storage.
*   26 PB of Object/Shared Filesystem [Ceph](https://en.wikipedia.org/wiki/Ceph_(software)) storage.
*   3 PB of NVMe Volume and Snapshot [Ceph](https://en.wikipedia.org/wiki/Ceph_(software)) storage.

## Node characteristics

| nodes | cores | available memory | storage | CPU | GPU |
| :---- | :---- | :--------------- | :------ | :-- | :-- |
| 338   | 96    | 768GB DDR5       | 1 x NVMe SSD, 7.68TB | 2 x Intel Platinum 8568Y+ 2.3GHz, 300MB cache | |
| 22    | 96    | 1536GB DDR5      | 1 x NVMe SSD, 7.68TB | 2 x Intel Platinum 8568Y+ 2.3GHz, 300MB cache | |
| 11    | 64    | 2048GB DDR5      | 1 x NVMe SSD, 7.68TB | 2 x Intel Platinum 6548Y+ 2.5GHz, 60MB cache | |
| 16    | 48    | 1024GB DDR4      | 1 x NVMe SSD, 3.84TB | 2 x Intel Gold 6342 2.8 GHz, 36MB cache | 4 x NVidia H100 PCIe Gen5 (94GB) |
| 10    | 48    | 128GB DDR5       | 1 x NVMe SSD, 3.84TB | 2 x Intel Gold 6542Y 2.9 GHz, 60MB cache | 1 x NVidia L40s PCIe Gen4 (48GB) |

See [Cloud resources](cloud-resources.md#arbutus-cloud) for current equipment summary.