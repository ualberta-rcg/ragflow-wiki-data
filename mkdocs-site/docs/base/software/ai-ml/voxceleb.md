---
title: "VoxCeleb"
slug: "voxceleb"
lang: "base"

source_wiki_title: "VoxCeleb"
source_hash: "c606e2dd76495bde66fbf9aa4a01370c"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T12:49:51.259878+00:00"

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

The Alliance makes available on the [Graham](graham.md) cluster a copy of the VoxCeleb dataset, stored in the `/datashare` space. For the time being, this dataset is available only on Graham, and you must opt-in to access this dataset by agreeing that you have registered for a VoxCeleb licence:

!!! note "VoxCeleb Licence Agreement"
    By selecting this service you acknowledge that you have registered with the owner of the data (at [https://www.robots.ox.ac.uk/~vgg/data/voxceleb/index.html#portfolio](https://www.robots.ox.ac.uk/~vgg/data/voxceleb/index.html#portfolio)) and have agreed to VoxCeleb's terms of use ([https://www.robots.ox.ac.uk/~vgg/data/voxceleb/files/license.txt](https://www.robots.ox.ac.uk/~vgg/data/voxceleb/files/license.txt)).

This dataset is provided as is. For requests for updates or inclusion of more data, please contact our [Technical support](technical-support.md) with the subject `VoxCeleb dataset`, specifying why the add-on is important.

### Request Access Through the Opt-in Service

Please visit [https://ccdb.computecanada.ca/services/opt_in](https://ccdb.computecanada.ca/services/opt_in) to request access by acknowledging that you have registered with the providers and that you agree with their terms and conditions.

### Location and Contents

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

### This is an NFS3 Mount!!!

!!! warning
    The VoxCeleb provided on Graham is an NFS3 mount, and therefore you might have issues accessing the files if you belong to more than 16 groups within the Alliance.