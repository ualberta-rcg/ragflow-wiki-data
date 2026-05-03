---
title: "QuantumATK/en"
slug: "quantumatk"
lang: "en"

source_wiki_title: "QuantumATK/en"
source_hash: "a79f9fa8750509b5403a7693f73300f9"
last_synced: "2026-05-02T23:50:34.269007+00:00"
last_processed: "2026-05-03T00:46:16.331749+00:00"

tags:
  []

keywords:
  - "QuantumATK"
  - "Licensing"
  - "License server"
  - "CMC license setup"
  - "Atomic-scale modeling"

questions:
  - "What is QuantumATK and how does it benefit research and development in high-tech industries?"
  - "What are the available options for researchers to obtain a valid license to use QuantumATK on the hosting provider's clusters?"
  - "How do users technically configure their own license file or a CMC license to ensure the compute nodes can access the license server?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Introduction
[QuantumATK](https://www.synopsys.com/silicon/quantumatk.html) atomic-scale modeling software enables large-scale and thus more realistic material simulations, integrating state-of-the-art methods into an easy-to-use platform. QuantumATK accelerates semiconductor and materials R&D and reduces time and costs by enabling more efficient workflows in the screening process of new materials across a broad range of high-tech industries.

## Licensing
We are a hosting provider for QuantumATK. This means that we have QuantumATK software installed on our clusters, but we do not provide a generic license accessible to everyone. Many institutions, faculties, and departments already have licenses that can be used on our clusters. Alternatively, researchers can purchase a license from [CMC](https://account.cmc.ca/en/WhatWeOffer/Products/CMC-00200-00368.aspx) for use anywhere in Canada, or purchase a dedicated [License](https://solvnet.synopsys.com/SmartKeys) directly from Synopsys company for use on our systems.

Once the legal aspects are worked out for licensing, there will be remaining technical aspects. The license server on your end will need to be reachable by our compute nodes. This will require our technical team to get in touch with the technical people managing your license software. In some cases, such as CMC, this has already been done. You should then be able to load the modules, and it should find its license automatically. If this is not the case, please contact our [Technical support](../../support/technical_support.md), so that we can arrange this for you.

### Configuring your own license file
Our module for QuantumATK is designed to look for license information in a few places. One of those places is your home folder. If you have your own license server, you can write the information to access it in the following format:

```bash :file: quantumatk.lic
SERVER <server> ANY <port>
USE_SERVER
```

and put this file in the folder `$HOME/.licenses/` where `<server>` is your license server and `<port>` is the port number of the license server.

!!! warning "Firewall Configuration"
    Firewall changes will need to be done on both our side and your side. To arrange this, send an email containing the service port and IP address of your floating QuantumATK license server to [Technical support](../../support/technical_support.md).

#### CMC License Setup
Researchers who purchase a QuantumATK license subscription from CMC may use the following settings in their `quantumatk.lic` file:

- Fir: `SERVER 172.26.0.101 ANY 6053`
- Narval: `SERVER 10.100.64.10 ANY 6053`
- Rorqual: `SERVER 10.100.64.10 ANY 6053`
- Trillium: `SERVER scinet-cmc ANY 6053`

If initial license checkout attempts fail, create a support case with [CMC](https://www.cmc.ca/support/).