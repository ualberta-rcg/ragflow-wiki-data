---
title: "Migration2016:Migrating to Waterloo Storage"
slug: "migration2016_migrating_to_waterloo_storage"
lang: "base"

source_wiki_title: "Migration2016:Migrating to Waterloo Storage"
source_hash: "6857a66a1496f14fdd37e77c04cb7960"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:06:57.752707+00:00"

tags:
  []

keywords:
  - "Compute Canada credentials"
  - "File transfer"
  - "Globus Access"
  - "System Status"
  - "SSH Access"

questions:
  - "What credentials are required to access the new systems and log into the Globus endpoint?"
  - "How can users transfer files using the Globus service and what is the specific endpoint name?"
  - "What is the address provided for connecting directly to the system via SSH to browse and transfer files?"
  - "What credentials are required to access the new systems and log into the Globus endpoint?"
  - "How can users transfer files using the Globus service and what is the specific endpoint name?"
  - "What is the address provided for connecting directly to the system via SSH to browse and transfer files?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# Getting Access to Files
To access the new systems, please use your Compute Canada credentials. For more information, please see [this page](migration2016-user-accounts-and-groups.md).

## Globus Access
You can transfer files from your personal computer or another Compute Canada system using the Globus transfer service with the endpoint `computecanada#new-endpoint` as the source or destination. Globus is a fast, easy, secure way to transfer files designed for researchers. You can find more information about it on our [Globus](globus.md) page.

To log into the new endpoint, please use your Compute Canada username and password. See here to test your password. See here to reset your password.

## SSH Access
You can also connect directly to the system using [SSH](ssh.md) to browse and transfer files by connecting to `dtn-sharcnet.computecanada.ca`.

# System Status
You can see the current [status of the system here](https://www.sharcnet.ca/my/systems).