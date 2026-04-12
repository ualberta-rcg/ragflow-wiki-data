---
title: "Cloud storage options/en"
slug: "cloud_storage_options"
lang: "en"

source_wiki_title: "Cloud storage options/en"
source_hash: "6b194ec24a498781fd4c0ab8b7efcc1b"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:26:23.925332+00:00"

tags:
  - cloud

keywords:
  - "Shared filesystem storage"
  - "Ephemeral storage"
  - "Object storage"
  - "Cloud storage"
  - "Volume storage"

questions:
  - "What are the four main types of cloud storage available, and what are their primary characteristics?"
  - "How do the storage types differ in terms of being mounted on single versus multiple virtual machines simultaneously?"
  - "Which storage options are suitable for long-term data retention, and what happens to them when a virtual machine is deleted?"

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

## Storage Type Attributes

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