---
title: "PAICE Allocations and compute scheduling"
slug: "paice_allocations_and_compute_scheduling"
lang: "base"

source_wiki_title: "PAICE Allocations and compute scheduling"
source_hash: "85a24e7c9f2306ca77d83646da6e8cf9"
last_synced: "2026-08-26T10:16:11.334907+00:00"
last_processed: "2026-08-26T11:15:29.588195+00:00"

tags:
  []

keywords:
  - "FairShare allocation"
  - "CIFAR AI Chairs"
  - "aip- slurm account"
  - "PAICE clusters"
  - "AI Institute Faculty Affiliates"

questions:
  - "How does the PAICE allocation system differ from the Resource Allocation Competition (RAC) used by other Alliance clusters?"
  - "What are the four user tiers defined for PAICE clusters, and what share of total cluster resources is each tier allocated?"
  - "What naming convention must users follow for their Slurm accounts and POSIX groups when submitting jobs on PAICE clusters?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

The Pan Canadian AI Environment (PAICE) clusters, which consist of [Vulcan](../clusters/vulcan.md), [Killarney](../clusters/killarney.md) and [TamIA](../clusters/tamia.md) borrow strongly from the Alliance's traditional [Allocations and compute scheduling](allocations_and_compute_scheduling.md) methodologies, but differ in how resource allocations are assigned.

The PAICE sites do not participate in the Resource Allocation Competition (RAC) and instead derive cluster computational allocations by grouping Projects into one of four groups, which are then allocated resources on the three clusters.

## Identification and Grouping
There are 4 Tiers of users identified:

*   Canada CIFAR AI Chairs and Equivalents and their research teams
*   AI Institute Faculty Affiliates
*   Faculty members with a tenure track appointment at a Canadian university within an AI program
*   Faculty members with a tenure track appointment at a Canadian university applying AI to other domains

!!! note
    Users are assigned to an AI-specific Slurm account and POSIX group with the prefix of `aip-` versus the more familiar `rrg-` or `rpp-` used on the non-PAICE sites. Users must utilize this naming structure in their job submissions and [storage allocations](../storage-and-data/storage_and_file_management.md) while using the PAICE clusters.

## Scheduling Calculations
Each of the above Tiers are assigned a FairShare value that is proportional to the overall cluster's Shares as per the following table:

PAICE Tiering Allocations

| Tier                                          | % total shares |
| :-------------------------------------------- | :------------: |
| CIFAR AI Chairs                               | 45%            |
| AI Institute Faculty Affiliates               | 40%            |
| Faculty members, within an AI program         | 10%            |
| Faculty members, applying AI to other domains | 5%             |

A Tier's allocation percentage will be further equally divided among the Projects assigned to the Tier and are expressed as the FairShare value in the scheduler's Project/Account.

Aside from this method of assigning Shares to an Account, the same methodology of scheduler job priority management that is outlined in [Allocations and compute scheduling](allocations_and_compute_scheduling.md) is in effect on the PAICE clusters.