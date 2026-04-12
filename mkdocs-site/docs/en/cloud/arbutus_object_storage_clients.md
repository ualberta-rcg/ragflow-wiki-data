---
title: "Arbutus object storage clients/en"
slug: "arbutus_object_storage_clients"
lang: "en"

source_wiki_title: "Arbutus object storage clients/en"
source_hash: "37a392e12d45010b0203a348a26842e2"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:29:20.426380+00:00"

tags:
  - cloud

keywords:
  - "AWS CLI"
  - "Arbutus Object Storage"
  - "s3cmd"
  - "object storage client"
  - "S3 Virtual Hosting"

questions:
  - "How can a user obtain Arbutus Object Storage?"
  - "What are the specific client applications listed for managing the Arbutus object store?"
  - "Why must the default settings of object storage clients be modified when connecting to Arbutus?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

For information on obtaining Arbutus Object Storage, please see [this page](arbutus_object_storage.md). For information on how to use an object storage client to manage your Arbutus object store, choose a client and follow instructions from these pages:
* [Accessing object storage with s3cmd](accessing_object_storage_with_s3cmd.md)
* [Accessing object storage with WinSCP](accessing_object_storage_with_winscp.md)
* [Accessing the Arbutus object storage with AWS CLI](accessing_the_arbutus_object_storage_with_aws_cli.md)
* [Accessing the Arbutus object storage with Globus](../getting-started/globus.md#object-storage-on-arbutus)

!!! note
    Arbutus' Object Storage solution does not use Amazon's [S3 Virtual Hosting](https://documentation.help/s3-dg-20060301/VirtualHosting.html) (i.e., DNS-based bucket) approach, which these clients assume by default. They need to be configured not to use that approach, as described in the pages linked above.