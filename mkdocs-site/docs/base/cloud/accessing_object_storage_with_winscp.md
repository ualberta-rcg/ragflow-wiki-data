---
title: "Accessing object storage with WinSCP"
slug: "accessing_object_storage_with_winscp"
lang: "base"

source_wiki_title: "Accessing object storage with WinSCP"
source_hash: "7765fb788f529489cc883837617ae204"
last_synced: "2026-04-10T14:10:18.226633+00:00"
last_processed: "2026-04-10T14:38:52.989200+00:00"

tags:
  - cloud

keywords:
  - "Arbutus object storage"
  - "File transfer"
  - "Access Control Lists"
  - "WinSCP"
  - "Amazon S3"

questions:
  - "What specific session settings and advanced protocol options must be configured in WinSCP to successfully connect to Arbutus object storage?"
  - "How do users create buckets and transfer files using the WinSCP graphical user interface?"
  - "What steps are required to modify the Access Control Lists (ACLs) for individual files within WinSCP?"
  - "What specific session settings and advanced protocol options must be configured in WinSCP to successfully connect to Arbutus object storage?"
  - "How do users create buckets and transfer files using the WinSCP graphical user interface?"
  - "What steps are required to modify the Access Control Lists (ACLs) for individual files within WinSCP?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

This page contains instructions on how to set up and access [Arbutus object storage](arbutus-object-storage.md) with WinSCP, one of the [object storage clients](arbutus-object-storage-clients.md) available for this storage type.

## Installing WinSCP
WinSCP can be installed from [https://winscp.net/](https://winscp.net/).

## Configuring WinSCP
Under "New Session", make the following configurations:

*   File protocol: Amazon S3
*   Host name: object-arbutus.alliancecan.ca
*   Port number: 443
*   Access key ID: 20_DIGIT_ACCESS_KEY

and "Save" these settings.

Next, click on the "Edit" button and then click on "Advanced..." and navigate to "Environment" to "S3" to "Protocol options" to "URL style:" which **must** be changed from "Virtual Host" to "Path".

!!! warning
    This "Path" setting is important; otherwise, WinSCP will not work, and you will see hostname resolution errors.

## Using WinSCP
Click on the "Login" button and use the WinSCP GUI to create buckets and to transfer files.

## Access Control Lists (ACLs) and Policies
Right-clicking on a file will allow you to set a file's ACL.