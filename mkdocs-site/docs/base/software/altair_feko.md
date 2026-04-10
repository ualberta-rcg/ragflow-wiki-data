---
title: "Altair FEKO"
slug: "altair_feko"
lang: "base"

source_wiki_title: "Altair FEKO"
source_hash: "4a3caab8ce6f6429a544859c3751d006"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T04:12:41.602315+00:00"

tags:
  - software

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

# Introduction
[Altair FEKO](https://altairhyperworks.com/product/FEKO) is a comprehensive computational electromagnetics (CEM) software used widely in the telecommunications, automobile, aerospace and defence industries.

# Licensing
We are a hosting provider for FEKO. This means that we have FEKO software installed on our clusters, but we do not provide a generic licence accessible to everyone. However, you may already have a licence server for your research group.

## Configuring your own licence file
Our module for FEKO is designed to look for licence information in a few places. One of those places is your home folder. If you have your own licence server, you can write the information to access it in the following format:

```lua title="feko.lic"
setenv("ALTAIR_LICENSE_PATH", "<port>@<hostname>")
```

and put this file in the folder `$HOME/.licenses/`. Note that firewall configuration will need to be done on both our side and yours. Please get in touch with our [Technical support](technical-support.md) to arrange this.