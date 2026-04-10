---
title: "Arbutus object storage clients"
tags:
  - cloud

keywords:
  []
---

For information on obtaining Arbutus Object Storage, please see [this page](arbutus-object-storage.md). For information on how to use an object storage client to manage your Arbutus object store, choose a client and follow instructions from these pages:
* [ Accessing object storage with s3cmd ](-accessing-object-storage-with-s3cmd-.md)
* [ Accessing object storage with WinSCP ](-accessing-object-storage-with-winscp-.md)
* [Accessing the Arbutus object storage with AWS CLI ](accessing-the-arbutus-object-storage-with-aws-cli-.md)
* [Accessing the Arbutus object storage with Globus](globus#object_storage_on_arbutus.md)

It is important to note that Arbutus' Object Storage solution does not use Amazon's [S3 Virtual Hosting](https://documentation.help/s3-dg-20060301/VirtualHosting.html) (i.e. DNS-based bucket) approach which these clients assume by default. They need to be configured not to use that approach, as described in the pages linked above.