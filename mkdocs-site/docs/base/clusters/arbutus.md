---
title: "Arbutus"
slug: "arbutus"
lang: "base"

source_wiki_title: "Arbutus"
source_hash: "660f91b707d4e9a5edf4cc2b38a7c3af"
last_synced: "2026-10-11T01:39:35.690021+00:00"
last_processed: "2026-10-11T02:21:35.528506+00:00"

tags:
  []

keywords:
  - "node specifications"
  - "Arbutus cloud"
  - "storage capacity"
  - "migration guide"
  - "Legacy Arbutus"

questions:
  - "When will the Legacy Arbutus cloud be decommissioned and how should users migrate their content to the new Arbutus cloud?"
  - "What storage capacities and types (volume, snapshot, object, NVMe) does the new Arbutus cloud provide?"
  - "What are the hardware specifications (cores, memory, CPU, GPU, storage) of the compute nodes offered by Arbutus?"

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
* Legacy OpenStack dashboard: [https://arbutus.cloud.alliancecan.ca](https://arbutus.cloud.alliancecan.ca)
* Legacy Object Storage (S3 or Swift): [https://object-arbutus.cloud.computecanada.ca](https://object-arbutus.cloud.computecanada.ca)

| Feature | Details |
| :---------------------- | :-------------------------------------------------------------------------------------------------- |
| Availability | late spring 2026 |
| OpenStack dashboard | [https://arbutus.alliancecan.ca](https://arbutus.alliancecan.ca) |
| Globus endpoint | *to be determined* |
| Object Storage (S3 or Swift) | https://object-arbutus.alliancecan.ca/&lt;tenant-id&gt;:&lt;bucket-name&gt;/&lt;object-name&gt; |

Arbutus is an Infrastructure-as-a-Service cloud hosted at the University of Victoria.

## Storage
7 PB of Volume and Snapshot [Ceph](https://en.wikipedia.org/wiki/Ceph_(software)) storage.
26 PB of Object/Shared Filesystem [Ceph](https://en.wikipedia.org/wiki/Ceph_(software)) storage.
3 PB of NVMe Volume and Snapshot [Ceph](https://en.wikipedia.org/wiki/Ceph_(software)) storage.

## Node characteristics

| nodes | cores | available memory | storage | CPU | GPU |
| ----- | ----- | ---------------- | ------- | --- | --- |
| 338 | 96 | 768GB DDR5 | 1 x NVMe SSD, 7.68TB | 2 x Intel Platinum 8568Y+ 2.3GHz, 300MB cache | |
| 22 | 96 | 1536GB DDR5 | 1 x NVMe SSD, 7.68TB | 2 x Intel Platinum 8568Y+ 2.3GHz, 300MB cache | |
| 11 | 64 | 2048GB DDR5 | 1 x NVMe SSD, 7.68TB | 2 x Intel Platinum 6548Y+ 2.5GHz, 60MB cache | |
| 16 | 48 | 1024GB DDR4 | 1 x NVMe SSD, 3.84TB | 2 x Intel Gold 6342 2.8 GHz, 36MB cache | 4 x NVidia H100 PCIe Gen5 (94GB) |
| 10 | 48 | 128GB DDR5 | 1 x NVMe SSD, 3.84TB | 2 x Intel Gold 6542Y 2.9 GHz, 60MB cache | 1 x NVidia L40s PCIe Gen4 (48GB) |

See [Cloud resources](../cloud/cloud_resources.md#arbutus-cloud) for current equipment summary.