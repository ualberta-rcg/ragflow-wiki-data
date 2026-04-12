---
title: "Migration2016:Migrating to SFU Storage"
slug: "migration2016_migrating_to_sfu_storage"
lang: "base"

source_wiki_title: "Migration2016:Migrating to SFU Storage"
source_hash: "cf49fc0cefb82639ea5b4df7166822d1"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:06:48.120539+00:00"

tags:
  []

keywords:
  - "Compute Canada"
  - "Globus transfer service"
  - "File access"
  - "System Status"
  - "SSH Access"

questions:
  - "What credentials are required to access the new systems and log into the Globus endpoint?"
  - "How can users transfer files to or from the new system using the Globus service and SSH?"
  - "Where can users check the current operational status of the system?"
  - "What credentials are required to access the new systems and log into the Globus endpoint?"
  - "How can users transfer files to or from the new system using the Globus service and SSH?"
  - "Where can users check the current operational status of the system?"

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
You can transfer files from your personal computer or another Compute Canada system using Globus transfer service using the endpoint **computecanada#new-endpoint** as the source or destination. Globus is a fast, easy, secure way to transfer files designed for researchers. You can find more information about it on our [Globus](globus.md) page.

!!! note
    To log into the new endpoint, please use your Compute Canada username and password. See here to test your password. See here to reset your password.

## SSH Access
You can also connect directly to the system using [SSH](ssh.md) to browse and transfer files by connecting to `dtn-sfu.computecanada.ca`.

# System Status
You can see the current [status of the system here](https://www.westgrid.ca/support/system_status).