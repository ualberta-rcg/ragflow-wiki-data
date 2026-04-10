---
title: "Using swift"
slug: "using_swift"
lang: "base"

source_wiki_title: "Using swift"
source_hash: "fcaed9397f7d8f698ec3ee916e685290"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T12:28:29.850588+00:00"

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

## Object Storage in Arbutus cloud

The OpenStack Object Store project, known as Swift, offers cloud storage software so that you can store and retrieve lots of data with a simple API.

If you require s3 access to it, please contact our [Technical support](technical-support.md).

## Using the Object Storage via Browser

Swift can be accessed via the openstack cli and/or via the [Cloud webinterface](https://arbutus.cloud.computecanada.ca).

*   **Dashboard Menu:** The object storage can be accessed via the menu on the left side.
*   **Publicly accessible container:** To store data a storage container needs to be created, which can hold the data. Multiple containers can be created if required, by clicking on **Public Access**, the container becomes public and will be accessible by anyone. If the container has no public access, it can only be used within the projects VMs.
*   **File upload via browser:** To upload files via browser into the container, click on the upload button.

## Using the Object Storage via OSA cli