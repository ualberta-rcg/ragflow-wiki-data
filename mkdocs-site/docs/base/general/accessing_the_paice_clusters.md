---
title: "Accessing the PAICE clusters"
slug: "accessing_the_paice_clusters"
lang: "base"

source_wiki_title: "Accessing the PAICE clusters"
source_hash: "eafa057d1a8957ac01a62e05140344e1"
last_synced: "2026-11-15T02:27:25.182546+00:00"
last_processed: "2026-11-15T03:54:09.933886+00:00"

tags:
  []

keywords:
  - "tier assignment"
  - "PAICE clusters"
  - "SSH key registration"
  - "RAP management"
  - "AI project (AIP)"

questions:
  - "What steps must a principal investigator (PI) follow to create an AI project (AIP) and obtain a tier for accessing PAICE clusters?"
  - "How can a PI add or sponsor other researchers to their AIP through the RAP management page?"
  - "What actions must a user take after being added to an AIP to request access to specific PAICE clusters?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## For PIs

To run jobs or be granted large storage allocations (i.e. project and scratch) on any PAICE cluster ([Killarney](../clusters/killarney.md), [tamIA](../clusters/tamia.md), [Vulcan](../clusters/vulcan.md)) a user must belong to an AI project (AIP), and the AIP must have a tier assigned to it.

An AIP belongs to a principal investigator (PI). **If the PI is affiliated with one of the three AI institutes** ([AMII](https://www.amii.ca/), [MILA](https://mila.quebec/en), [Vector](https://vectorinstitute.ai/)), then their home institute should create the AIP and assign it a tier.

**If the PI is not affiliated with an AI institute** but is either researching AI or using AI in their research, then the PI should visit [CCDB -> Resources -> General Access to PAICE Systems](https://ccdb.alliancecan.ca/paice/general_access_to_paice_systems) and check the appropriate box. This will create an AIP and assign it a tier.

To sponsor researchers in their AIP, the PI must:

1.  In the *Resource Allocation Projects* table on the [CCDB home page](https://ccdb.alliancecan.ca), click on the RAPI to get to the RAP management page.
2.  At the top of the RAP management page, click on *Manage RAP memberships*.
3.  In the *Add Members* section, enter the CCRI of the users you want to add.

## For users

Once your PI has added you to their AIP, you must [request access](https://ccdb.alliancecan.ca/me/access_services) to specific clusters.

!!! note
    PAICE clusters may impose further requirements for access, such as registering an SSH key pair at [CCDB -> My Account -> SSH Keys](https://ccdb.alliancecan.ca/ssh_authorized_keys).