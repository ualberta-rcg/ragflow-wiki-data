---
title: "Using swift"
slug: "using_swift"
lang: "base"

source_wiki_title: "Using swift"
source_hash: "fcaed9397f7d8f698ec3ee916e685290"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:28:07.012933+00:00"

tags:
  []

keywords:
  - "Object Storage"
  - "OpenStack Swift"
  - "Arbutus cloud"
  - "storage container"
  - "OSA cli"

questions:
  - "How can a user obtain S3 access to the OpenStack Object Store (Swift) in the Arbutus cloud?"
  - "What is the difference in accessibility between a public and a private storage container?"
  - "What are the steps to navigate the Cloud web interface to create a container and upload files?"
  - "How can a user obtain S3 access to the OpenStack Object Store (Swift) in the Arbutus cloud?"
  - "What is the difference in accessibility between a public and a private storage container?"
  - "What are the steps to navigate the Cloud web interface to create a container and upload files?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Object Storage in Arbutus cloud

The OpenStack Object Store project, known as Swift, offers cloud storage software so that you can store and retrieve lots of data with a simple API.

If you require S3 access to it, please contact our [technical support](../support/technical_support.md).

## Using the Object Storage via Browser

Swift can be accessed via the `openstack` CLI and/or via the [Cloud web interface](https://arbutus.cloud.computecanada.ca).

| Step/Context | Description |
| :----------- | :---------- |
| Dashboard Menu | The object storage can be accessed via the menu on the left side. |
| Publicly accessible container | To store data, a storage container needs to be created, which can hold the data. Multiple containers can be created if required. By clicking on **Public Access**, the container becomes public and will be accessible by anyone. If the container has no public access, it can only be used within the project's VMs. |
| File upload via browser | To upload files via browser into the container, click on the upload button. |

## Using the Object Storage via OSA CLI