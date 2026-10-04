---
title: "Arbutus/en"
slug: "arbutus"
lang: "en"

source_wiki_title: "Arbutus/en"
source_hash: "a978fc001b2281cb59dd7a62b0a8d27e"
last_synced: "2026-10-04T02:27:33.201522+00:00"
last_processed: "2026-10-04T03:03:48.849262+00:00"

tags:
  []

keywords:
  - "NVMe Volume and Snapshot"
  - "Arbutus IaaS cloud"
  - "Intel Platinum CPUs"
  - "NVidia H100 GPU"
  - "Ceph storage"

questions:
  - "When is Arbutus expected to become available for users?<br/>What storage capacities and types (volume, snapshot, object, NVMe) does Arbutus provide?<br/>What are the hardware specifications (CPU, GPU, memory, storage) of the compute nodes offered by Arbutus?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

| Feature | Details |
| :-------- | :-------- |
| Availability | late spring 2026 |
| Legacy OpenStack dashboard | [https://arbutus.cloud.alliancecan.ca/](https://arbutus.cloud.alliancecan.ca/) |
| Renewal OpenStack dashboard | [https://arbutus.alliancecan.ca/auth/login/?next=/](https://arbutus.alliancecan.ca/auth/login/?next=/) |
| Globus endpoint | *to be determined* |
| Legacy Object Storage (S3 or Swift) | [https://object-arbutus.cloud.computecanada.ca/](https://object-arbutus.cloud.computecanada.ca/) |
| Renewal Object Storage (S3 or Swift) | https://object-arbutus.alliancecan.ca/\<tenant-id\>:\<bucket-name\>/\<object-name\> |

Arbutus is an Infrastructure-as-a-Service cloud hosted at the University of Victoria.

## Storage
7 PB of Volume and Snapshot [Ceph](https://en.wikipedia.org/wiki/Ceph_(software)) storage.
26 PB of Object/Shared Filesystem [Ceph](https://en.wikipedia.org/wiki/Ceph_(software)) storage.
3 PB of NVMe Volume and Snapshot [Ceph](https://en.wikipedia.org/wiki/Ceph_(software)) storage.

## Node characteristics

| nodes | cores | available memory | storage | CPU | GPU |
| :---- | :---- | :--------------- | :------------------ | :---------------------------------------------- | :----------------------------------- |
| 338 | 96 | 768GB DDR5 | 1 x NVMe SSD, 7.68TB | 2 x Intel Platinum 8568Y+ 2.3GHz, 300MB cache | |
| 22 | 96 | 1536GB DDR5 | 1 x NVMe SSD, 7.68TB | 2 x Intel Platinum 8568Y+ 2.3GHz, 300MB cache | |
| 11 | 64 | 2048GB DDR5 | 1 x NVMe SSD, 7.68TB | 2 x Intel Platinum 6548Y+ 2.5GHz, 60MB cache | |
| 16 | 48 | 1024GB DDR4 | 1 x NVMe SSD, 3.84TB | 2 x Intel Gold 6342 2.8 GHz, 36MB cache | 4 x NVidia H100 PCIe Gen5 (94GB) |
| 10 | 48 | 128GB DDR5 | 1 x NVMe SSD, 3.84TB | 2 x Intel Gold 6542Y 2.9 GHz, 60MB cache | 1 x NVidia L40s PCIe Gen4 (48GB) |

See [Cloud resources](../cloud/cloud_resources.md#arbutus-cloud) for current equipment summary.