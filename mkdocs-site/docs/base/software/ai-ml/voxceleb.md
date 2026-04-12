---
title: "VoxCeleb"
slug: "voxceleb"
lang: "base"

source_wiki_title: "VoxCeleb"
source_hash: "c606e2dd76495bde66fbf9aa4a01370c"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:47:38.483833+00:00"

tags:
  []

keywords:
  - "Compute Canada"
  - "Graham cluster"
  - "Opt-in service"
  - "VoxCeleb dataset"
  - "NFS3 mount"

questions:
  - "What are the prerequisites and steps required for a user to gain access to the VoxCeleb dataset on the Graham cluster?"
  - "Where is the VoxCeleb dataset located on the cluster, and what are the main components included in its directory structure?"
  - "What potential technical issue might users face due to the dataset being hosted on an NFS3 mount?"
  - "What are the prerequisites and steps required for a user to gain access to the VoxCeleb dataset on the Graham cluster?"
  - "Where is the VoxCeleb dataset located on the cluster, and what are the main components included in its directory structure?"
  - "What potential technical issue might users face due to the dataset being hosted on an NFS3 mount?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! important "Opt-in Service Required"
    Compute Canada makes available on [Graham](../../clusters/graham.md) cluster a copy of the VoxCeleb dataset, stored in the `/datashare` space. For the time being, this dataset is available only on Graham and you must opt-in to access this dataset by agreeing that you have registered for a VoxCeleb license.

    By selecting this service you acknowledge that you have registered with the owner of the data (at https://www.robots.ox.ac.uk/~vgg/data/voxceleb/index.html#portfolio and have agreed to VoxCeleb’s terms of use (https://www.robots.ox.ac.uk/~vgg/data/voxceleb/files/license.txt)

    En sélectionnant ce service, vous reconnaissez que vous êtes inscrit auprès du propriétaire des données (à l'adresse https://www.robots.ox.ac.uk/~vgg/data/voxceleb/index.html#portfolio) et que vous avez accepté les conditions d'utilisation (https://www.robots.ox.ac.uk/~vgg/data/voxceleb/files/license.txt) d'VoxCeleb.

This dataset is provided as is. For requests for updates or inclusion of more data, please contact our [Technical support](../../support/technical_support.md) with the subject `VoxCeleb dataset`, specifying why the add-on is important.

### Request access through the opt-in service

Please visit https://ccdb.computecanada.ca/services/opt_in to request access by acknowledging that you have registered with the providers and that you agree with their terms and conditions.

### Location and contents

The files can be accessed at `/datashare/VoxCeleb/`, and it contains:

```text
├── CMBiometrics
│   ├── denseDynamicImages
│   ├── dense-face-frames.tar.gz
│   ├── unzippedFaces
│   └── unzippedIntervalFaces
├── lastupdate
├── VoxCeleb1
│   ├── Dev
│   ├── duplicates.txt
│   ├── meta
│   ├── Models
│   ├── SITW_overlap.txt
│   └── Test
└── VoxCeleb2
    ├── Dev
    ├── meta
    ├── Models
    └── Test
```

### This is an NFS3 mount!!!

!!! warning
    The VoxCeleb provided in Graham is an NFS3 mount, and therefore you might have issues accessing the files if you belong to more than 16 groups in CC.