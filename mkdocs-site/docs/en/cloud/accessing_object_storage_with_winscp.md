---
title: "Accessing object storage with WinSCP/en"
slug: "accessing_object_storage_with_winscp"
lang: "en"

source_wiki_title: "Accessing object storage with WinSCP/en"
source_hash: "75c3cc0d6e80ab8c241462ec52ac061f"
last_synced: "2026-04-10T14:10:18.226633+00:00"
last_processed: "2026-04-10T14:39:02.329096+00:00"

tags:
  - cloud

keywords:
  - "Arbutus object storage"
  - "Configuration"
  - "Access Control Lists"
  - "WinSCP"
  - "Amazon S3"

questions:
  - "What are the required session configurations to connect WinSCP to Arbutus object storage?"
  - "Why must the URL style be changed from \"Virtual Host\" to \"Path\" in the advanced settings?"
  - "How do users create buckets, transfer files, and manage Access Control Lists (ACLs) using the WinSCP interface?"
  - "What are the required session configurations to connect WinSCP to Arbutus object storage?"
  - "Why must the URL style be changed from \"Virtual Host\" to \"Path\" in the advanced settings?"
  - "How do users create buckets, transfer files, and manage Access Control Lists (ACLs) using the WinSCP interface?"

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
*   Access key ID: `20_DIGIT_ACCESS_KEY`

and "Save" these settings.

Next, click on the "Edit" button and then click on "Advanced..." and navigate to "Environment" to "S3" to "Protocol options" to "URL style:" which **must** be changed from "Virtual Host" to "Path".

!!! warning "Important URL Style Configuration"
    This "Path" setting is important, otherwise WinSCP will not work and you will see hostname resolution errors.

## Using WinSCP
Click on the "Login" button and use the WinSCP GUI to create buckets and to transfer files.

## Access Control Lists (ACLs) and Policies
Right-clicking on a file will allow you to set a file's ACL.