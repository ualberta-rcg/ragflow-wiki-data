---
title: "Altair FEKO/en"
slug: "altair_feko"
lang: "en"

source_wiki_title: "Altair FEKO/en"
source_hash: "1664ad8dfef74d48c309ea6532660649"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T04:12:55.031235+00:00"

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

# Altair FEKO

[Altair FEKO](https://altairhyperworks.com/product/FEKO) is a comprehensive computational electromagnetics (CEM) software used widely in the telecommunications, automobile, aerospace and defence industries.

## Licensing

We are a hosting provider for FEKO. This means that we have FEKO software installed on our clusters, but we do not provide a generic license accessible to everyone. However, you may already have a license server for your research group.

### Configuring your own license file

Our module for FEKO is designed to look for license information in a few places. One of those places is your home folder. If you have your own license server, you can write the information to access it in the following format:

````lua title="feko.lic"
setenv("ALTAIR_LICENSE_PATH", "<port>@<hostname>")
````

and put this file in the folder `$HOME/.licenses/`. Note that firewall configuration will need to be done on both our side and yours. Please get in touch with our [Technical support](technical-support.md) to arrange this.