---
title: "Altair FEKO/en"
slug: "altair_feko"
lang: "en"

source_wiki_title: "Altair FEKO/en"
source_hash: "1664ad8dfef74d48c309ea6532660649"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:06:35.662984+00:00"

tags:
  - software

keywords:
  - "license server"
  - "Altair FEKO"
  - "licensing"
  - "license file"
  - "computational electromagnetics"

questions:
  - "What is Altair FEKO and in which industries is it primarily used?"
  - "How is the licensing for FEKO managed on the cluster for general users?"
  - "What specific steps must a user take to configure and connect to their own FEKO license server?"
  - "What is Altair FEKO and in which industries is it primarily used?"
  - "How is the licensing for FEKO managed on the cluster for general users?"
  - "What specific steps must a user take to configure and connect to their own FEKO license server?"

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
We are a hosting provider for FEKO. This means that we have FEKO software installed on our clusters, but we do not provide a generic licence accessible to everyone. However, you may already have a licence server for your research group.

## Configuring your own licence file
Our module for FEKO is designed to look for licence information in a few places. One of those places is your home folder. If you have your own licence server, you can write the information to access it in the following format:

```sh title="feko.lic"
setenv("ALTAIR_LICENSE_PATH", "<port>@<hostname>")
```

and put this file in the folder `$HOME/.licenses/`.

!!! note
    Firewall configuration will need to be done on both our side and yours. Please get in touch with our [Technical support](../support/technical_support.md) to arrange this.