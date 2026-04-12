---
title: "Altair FEKO"
slug: "altair_feko"
lang: "base"

source_wiki_title: "Altair FEKO"
source_hash: "4a3caab8ce6f6429a544859c3751d006"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:06:22.120382+00:00"

tags:
  - software

keywords:
  - "ALTAIR_LICENSE_PATH"
  - "license server"
  - "Altair FEKO"
  - "licensing"
  - "computational electromagnetics"

questions:
  - "What is Altair FEKO and which industries commonly use this software?"
  - "How does the hosting provider handle licensing for FEKO on their clusters?"
  - "What are the necessary steps and file configurations required to set up a personal license server for FEKO?"
  - "What is Altair FEKO and which industries commonly use this software?"
  - "How does the hosting provider handle licensing for FEKO on their clusters?"
  - "What are the necessary steps and file configurations required to set up a personal license server for FEKO?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# Introduction
[Altair FEKO](https://altairhyperworks.com/product/FEKO) is a comprehensive computational electromagnetics (CEM) software used widely in the telecommunications, automobile, aerospace and defence industries.

# Licensing
We are a hosting provider for FEKO. This means that we have FEKO software installed on our clusters, but we do not provide a generic license accessible to everyone. However, you may already have a license server for your research group.

## Configuring your own license file
Our module for FEKO is designed to look for license information in a few places. One of those places is your home folder. If you have your own license server, you can write the information to access it in the following format:

```lua title="feko.lic"
setenv("ALTAIR_LICENSE_PATH", "<port>@<hostname>")
```

and put this file in the folder `$HOME/.licenses/`.

!!! note
    Firewall configuration will need to be done on both our side and yours. Please get in touch with our [Technical support](../support/technical_support.md) to arrange this.