---
title: "SAS"
slug: "sas"
lang: "base"

source_wiki_title: "SAS"
source_hash: "d5d1460e079e9492aaf020d4fec6606f"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:11:32.013046+00:00"

tags:
  []

keywords:
  - "command line environment"
  - "statistical analysis suite"
  - "licensing restrictions"
  - "SAS"
  - "Compute Canada clusters"

questions:
  - "What must users supply in order to run the commercial SAS software on Compute Canada clusters?"
  - "Why is it required to install SAS locally in a user's personal directory instead of centrally?"
  - "What is the recommended way to run SAS in a cluster environment, and which command line option facilitates this?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

SAS is a statistical analysis suite developed by the [SAS Institute](https://www.sas.com/en_us/home.html). SAS is commercial software, so users must supply their own licence to run this software on Compute Canada clusters. Due to licensing restrictions, the software must be installed locally, in a user's personal directory, rather than centrally.

!!! tip "Running SAS in a Cluster Environment"
    Given the constraints of a cluster environment, it is recommended that users restrict themselves to the use of SAS in a command line environment by means of the option `-nodms`.