---
title: "QuantumATK/en"
slug: "quantumatk"
lang: "en"

source_wiki_title: "QuantumATK/en"
source_hash: "6a0fa7f6800e3a8fdfe8f62527300182"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T10:18:00.260303+00:00"

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

# Introduction
[QuantumATK](https://www.synopsys.com/silicon/quantumatk.html) atomic-scale modelling software enables large-scale and thus more realistic material simulations, integrating state-of-the-art methods into an easy-to-use platform. QuantumATK accelerates semiconductor and materials R&D and reduces time and costs by enabling more efficient workflows in the screening process of new materials across a broad range of high-tech industries.

# Licensing
We are a hosting provider for QuantumATK. This means that we have QuantumATK software installed on our clusters, but we do not provide a generic licence accessible to everyone. Many institutions, faculties, and departments already have licences that can be used on our clusters. Alternatively researchers can purchase a licence from [CMC](https://account.cmc.ca/en/WhatWeOffer/Products/CMC-00200-00368.aspx) for use anywhere in Canada, or purchase a dedicated [Licence](https://solvnet.synopsys.com/SmartKeys) directly from Synopsys company for use on our systems.

Once the legal aspects are worked out for licensing, there will be remaining technical aspects. The licence server on your end will need to be reachable by our compute nodes. This will require our technical team to get in touch with the technical people managing your licence software. In some cases such as CMC, this has already been done. You should then be able to load the modules, and it should find its licence automatically. If this is not the case, please contact our [Technical support](technical-support.md), so that we can arrange this for you.

## Configuring your own licence file
Our module for QuantumATK is designed to look for licence information in a few places. One of those places is your home folder. If you have your own licence server, you can write the information to access it in the following format:

```bash title="quantumatk.lic"
SERVER <server> ANY <port>
USE_SERVER
```

and put this file in the folder `$HOME/.licenses/` where `<server>` is your licence server and `<port>` is the port number of the licence server. Note that firewall changes will need to be done on both our side and your side. To arrange this, send an email containing the service port and IP address of your floating QuantumATK licence server to [Technical support](technical-support.md).

### CMC Licence Setup
Researchers who purchase a QuantumATK licence subscription from CMC may use the following settings in their `quantumatk.lic` file:

*   Fir: `SERVER 172.26.0.101 ANY 6053`
*   Narval: `SERVER 10.100.64.10 ANY 6053`
*   Rorqual: `SERVER 10.100.64.10 ANY 6053`
*   Trillium: `SERVER nia-cmc ANY 6053`

If initial licence checkout attempts fail, create a support case with [CMC](https://www.cmc.ca/support/).