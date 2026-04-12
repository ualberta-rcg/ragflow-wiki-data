---
title: "Arbutus object storage clients"
slug: "arbutus_object_storage_clients"
lang: "base"

source_wiki_title: "Arbutus object storage clients"
source_hash: "4cb988d0da72bcfef07a1979125f9727"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:29:13.270106+00:00"

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
  - "Which client applications are listed as options for accessing and managing the Arbutus object store?"
  - "Why must object storage clients be specifically configured to avoid using Amazon's S3 Virtual Hosting approach when connecting to Arbutus?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

For information on obtaining Arbutus Object Storage, please see [this page](arbutus-object-storage.md). For information on how to use an object storage client to manage your Arbutus object store, choose a client and follow instructions from these pages:
*   [Accessing object storage with s3cmd](accessing-object-storage-with-s3cmd.md)
*   [Accessing object storage with WinSCP](accessing-object-storage-with-winscp.md)
*   [Accessing the Arbutus object storage with AWS CLI](accessing-the-arbutus-object-storage-with-aws-cli.md)
*   [Accessing the Arbutus object storage with Globus](globus.md#object-storage-on-arbutus)

!!! note
    Arbutus' Object Storage solution does not use Amazon's [S3 Virtual Hosting](https://documentation.help/s3-dg-20060301/VirtualHosting.html) (i.e., DNS-based bucket) approach which these clients assume by default. They need to be configured not to use that approach, as described in the pages linked above.