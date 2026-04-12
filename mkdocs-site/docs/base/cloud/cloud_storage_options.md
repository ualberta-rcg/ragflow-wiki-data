---
title: "Cloud storage options"
slug: "cloud_storage_options"
lang: "base"

source_wiki_title: "Cloud storage options"
source_hash: "57b500379a430efec3331674ccac3459"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:26:12.579141+00:00"

tags:
  - cloud

keywords:
  - "Shared filesystem storage"
  - "Ephemeral storage"
  - "Object storage"
  - "Cloud storage"
  - "Volume storage"

questions:
  - "What are the four existing storage types available in the cloud environment and what are their primary functions?"
  - "Which storage options are best suited for frequently changing data versus long-term, write-once storage?"
  - "How do the different storage types handle data persistence, such as automatic backups and deletion upon virtual machine removal?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

The existing storage types available in our clouds are:

*   **[Volume storage](working_with_volumes.md)**: The standard storage unit for cloud computing; can be attached to and detached from an instance.
*   **Ephemeral/Disk storage**: Virtual local disk storage tied to the lifecycle of a single instance on a hypervisor's local disk ("c" flavour local disk can be lost)
*   **[Object storage](arbutus_object_storage.md)**: Non-hierarchical storage where data is created or uploaded in whole-file form.
*   **[Shared filesystem storage](arbutus-cephfs.md)**: Private network attached storage space (similar to NFS/SMB shares); must be configured on each instance where it is mounted.

Attributes of each storage type are compared in the following table:

| Attribute | Volume storage | Ephemeral/Disk storage | Object storage | Shared filesystem storage |
|---|---|---|---|---|
| Default storage option | Yes | Yes | No | No |
| Can be accessed via a web browser | No | No | Yes | No |
| Access can be restricted for specific source IP ranges | N/A | N/A | Yes (S3 ACL) | N/A |
| Can be mounted on a single VM | Yes | Yes | No | Yes |
| Can be mounted on multiple VMs (and across projects) simultaneously | No | No | No | Yes |
| Automatic backups | No (manually with snapshots) | No | No | Yes (nightly to tape) |
| Suitable for write once, read only, and public access | No | No | Yes | No |
| Suitable for data/files that change frequently | Yes | Yes | No | Yes |
| Hierarchical filesystem | Yes | Yes | No | Yes |
| Suitable for long-term storage | Yes | No | Yes | Yes |
| Suitable mountable dedicated storage for individual servers | Yes | Only for temporary data | No | No |
| Deleted automatically upon deletion of VM | No | Yes | No | No |
| Standard magnitude of allocation | GB | GB | TB | TB |
| Multi-disk fault tolerance | Yes | c-flavours No; p-flavours Yes | Yes | Yes |
| Physical disk-level encryption | No | No | No | No |