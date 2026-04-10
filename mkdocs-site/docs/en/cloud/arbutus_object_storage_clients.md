---
title: "Arbutus object storage clients/en"
slug: "arbutus_object_storage_clients"
lang: "en"

source_wiki_title: "Arbutus object storage clients/en"
source_hash: "37a392e12d45010b0203a348a26842e2"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T04:38:02.562216+00:00"

tags:
  - cloud

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

For information on obtaining Arbutus Object Storage, please see [this page](arbutus-object-storage.md). For information on how to use an object storage client to manage your Arbutus object store, choose a client and follow instructions from these pages:

*   [Accessing object storage with s3cmd](accessing-object-storage-with-s3cmd.md)
*   [Accessing object storage with WinSCP](accessing-object-storage-with-winscp.md)
*   [Accessing the Arbutus object storage with AWS CLI](accessing-the-arbutus-object-storage-with-aws-cli.md)
*   [Accessing the Arbutus object storage with Globus](globus.md#object-storage-on-arbutus)

!!! warning "Important Note on Object Storage Configuration"
    Arbutus' Object Storage solution does not use Amazon's [S3 Virtual Hosting](https://documentation.help/s3-dg-20060301/VirtualHosting.html) (i.e. DNS-based bucket) approach which these clients assume by default. Clients need to be configured not to use that approach, as described in the pages linked above.