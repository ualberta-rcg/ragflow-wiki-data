---
title: "Accessing the PAICE clusters"
slug: "accessing_the_paice_clusters"
lang: "base"

source_wiki_title: "Accessing the PAICE clusters"
source_hash: "4a041dba98105047433a27612fbc3d7a"
last_synced: "2026-10-11T01:39:35.690021+00:00"
last_processed: "2026-10-11T02:42:45.288346+00:00"

tags:
  []

keywords:
  - "tier assignment"
  - "General Access to PAICE Systems"
  - "aip-[clustername]-tier"
  - "AI project (AIP)"
  - "admin error"

questions:
  - "What are the two methods for a PI to obtain a valid AI project (AIP) and the appropriate tier on PAICE systems?"
  - "How does the assigned tier (e.g., tier 1/2 versus tier 3/4) impact the storage, job access, and cluster priority for the PI and their project members?"
  - "What actions should be taken if a PI already has an AIP without a tier assigned, and what issues can arise from missing configuration steps such as SSH access?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

To run jobs or be granted large storage allocations (i.e. project and scratch), a user needs to belong to an AI project (AIP), and the PI responsible for that AIP must have a tier assigned to them. There are two methods for a PI to get a valid AIP.

### Method 1: Affiliated with an AI Institute

The first method involves PIs that are affiliated with the three AI institutes ([AMII](https://www.amii.ca/), [MILA](https://mila.quebec/en), [Vector](https://vectorinstitute.ai/)). These PIs have AIPs created for them by their home institutes and are then added to the appropriate tier group to grant them preferential access to resources.

An AIP can be created for a PI by navigating to that PI's role page and clicking *Create AI project* in the menu on the left. The PI must then be added to the `aip-[clustername]-tier[1/2]` group (the AI institute determines which group to add them to). This grants that PI, and any members of the AI project (`aip-[PI-name]`), storage and job access on that cluster. It also grants this access at a tier 3 level, amounting to fewer resources and lower cluster priority, on the other two PAICE clusters.

### Method 2: AI Research Without Institute Affiliation

The second way for a PI to gain resources on PAICE systems is if they are either researching AI without being affiliated with these three institutes, or if they are using AI in their (non-AI) research.

The PI can create an AIP by first connecting to the [CCDB](https://ccdb.alliancecan.ca.) and then clicking on `Resources -> General Access to PAICE Systems`, checking a box, and clicking the *Submit* button. This will create an AIP in their name and put them in the aip-tier3 or aip-tier4 group, which then gives them cluster resources and job submission access.

!!! warning "Addressing Missing Tier Assignments"
    If a PI already has an AIP but no tier assigned, they can still click one of these boxes to be granted tier 3 or tier 4 access. However, an AIP created for them with no tier assigned represents an administration error, as users will notice they have an AIP and yet still cannot use the clusters.

!!! warning "Multiple Configuration Layers"
    Users may have an AIP without having opted in to SSH access (e.g., via the first process described above). These are separate layers of configuration required to fully utilize the PAICE systems, and missing one leads to confusion and frustration for both users and administrators.