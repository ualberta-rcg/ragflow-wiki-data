---
title: "Arbutus/en"
slug: "arbutus"
lang: "en"

source_wiki_title: "Arbutus/en"
source_hash: "dfb671cd5acc00bf45f6504c71e6b5d3"
last_synced: "2026-10-11T01:39:35.690021+00:00"
last_processed: "2026-10-11T02:21:47.348112+00:00"

tags:
  []

keywords:
  - "Arbutus cloud"
  - "NVMe Volume and Snapshot storage"
  - "OpenStack dashboard"
  - "Legacy Arbutus decommissioned October 15 2026"
  - "Arbutus Migration Guide"

questions:
  - "When will the first (Legacy) version of the Arbutus cloud be decommissioned, and what migration actions are required for users?<br>"
  - "What storage capacities and formats (volume, snapshot, object/shared filesystem, NVMe) does the new Arbutus cloud provide?<br>"
  - "What are the hardware specifications (CPU, memory, storage, GPU) of the various node types listed for the Arbutus cloud?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! warning "Important"
The first version of the Arbutus cloud (also called Legacy Arbutus) will be decommissioned on October 15, 2026. Please migrate all contents to the new Arbutus cloud as described in the [Arbutus Migration Guide](../cloud/arbutus_migration_guide.md).

References for the Legacy Arbutus cloud:
*   Legacy OpenStack dashboard: [https://arbutus.cloud.alliancecan.ca](https://arbutus.cloud.alliancecan.ca/)
*   Legacy Object Storage (S3 or Swift): [https://object-arbutus.cloud.computecanada.ca/](https://object-arbutus.cloud.computecanada.ca/)

| Key                 | Value                                                              |
| :------------------ | :----------------------------------------------------------------- |
| Availability        | late spring 2026                                                   |
| OpenStack dashboard | [https://arbutus.alliancecan.ca](https://arbutus.alliancecan.ca/auth/login/?next=/) |
| Globus endpoint     | *to be determined*                                                 |
| Object Storage (S3 or Swift) | `https://object-arbutus.alliancecan.ca/<tenant-id>:<bucket-name>/<object-name>` |

Arbutus is an Infrastructure-as-a-Service cloud hosted at the University of Victoria.

## Storage
7 PB of Volume and Snapshot [Ceph](https://en.wikipedia.org/wiki/Ceph_(software)) storage.

26 PB of Object/Shared Filesystem [Ceph](https://en.wikipedia.org/wiki/Ceph_(software)) storage.

3 PB of NVMe Volume and Snapshot [Ceph](https://en.wikipedia.org/wiki/Ceph_(software)) storage.

## Node characteristics

| nodes | cores | available memory | storage                  | CPU                                         | GPU                                  |
| :---- | :---- | :--------------- | :----------------------- | :------------------------------------------ | :----------------------------------- |
| 338   | 96    | 768GB DDR5       | 1 x NVMe SSD, 7.68TB     | 2 x Intel Platinum 8568Y+ 2.3GHz, 300MB cache |                                      |
| 22    | 96    | 1536GB DDR5      | 1 x NVMe SSD, 7.68TB     | 2 x Intel Platinum 8568Y+ 2.3GHz, 300MB cache |                                      |
| 11    | 64    | 2048GB DDR5      | 1 x NVMe SSD, 7.68TB     | 2 x Intel Platinum 6548Y+ 2.5GHz, 60MB cache |                                      |
| 16    | 48    | 1024GB DDR4      | 1 x NVMe SSD, 3.84TB     | 2 x Intel Gold 6342 2.8 GHz, 36MB cache     | 4 x NVidia H100 PCIe Gen5 (94GB)     |
| 10    | 48    | 128GB DDR5       | 1 x NVMe SSD, 3.84TB     | 2 x Intel Gold 6542Y 2.9 GHz, 60MB cache    | 1 x NVidia L40s PCIe Gen4 (48GB)     |

See [Cloud resources](../cloud/cloud_resources.md#arbutus_cloud) for current equipment summary.