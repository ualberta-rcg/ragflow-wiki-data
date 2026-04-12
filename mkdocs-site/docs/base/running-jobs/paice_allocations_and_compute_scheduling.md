---
title: "PAICE Allocations and compute scheduling"
slug: "paice_allocations_and_compute_scheduling"
lang: "base"

source_wiki_title: "PAICE Allocations and compute scheduling"
source_hash: "52bf73868f237f9cc58caa6f9280abfc"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:08:46.944723+00:00"

tags:
  []

keywords:
  - "Pan Canadian AI Environment"
  - "FairShare value"
  - "User tiers"
  - "Resource allocations"
  - "Compute scheduling"

questions:
  - "How do the PAICE clusters differ from traditional Alliance sites regarding resource allocation and participation in the Resource Allocation Competition?"
  - "What are the four tiers of users identified within the PAICE system, and what specific account naming structure must they utilize?"
  - "How are the FairShare scheduling values proportionally distributed among the different user tiers and their individual projects?"
  - "How do the PAICE clusters differ from traditional Alliance sites regarding resource allocation and participation in the Resource Allocation Competition?"
  - "What are the four tiers of users identified within the PAICE system, and what specific account naming structure must they utilize?"
  - "How are the FairShare scheduling values proportionally distributed among the different user tiers and their individual projects?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Overview

The Pan Canadian AI Environment (PAICE) clusters, which consists of [Vulcan](../clusters/vulcan.md), [Killarney](../clusters/killarney.md) and [TamIA](../clusters/tamia.md) borrow strongly from the Alliance's traditional [Allocations and compute scheduling](allocations_and_compute_scheduling.md) methodologies, but differ in how resource allocations are assigned.

The PAICE sites do not participate in the Resource Allocation Competition (RAC) and instead derive cluster computational allocations by grouping Projects into one of four groups, which are then allocated resources on the three clusters.

## Identification and Grouping

There are 4 Tiers of users identified:

*   Canada CIFAR AI Chairs and Equivalents and their research teams
*   AI Institute Faculty Affiliates
*   Faculty members with a tenure track appointment at a Canadian university within an AI program
*   Faculty members with a tenure track appointment at a Canadian university applying AI to other domains

Users are assigned to an AI-specific Slurm Account and POSIX group with the prefix of `aip-` versus the more familiar `rrg-` or `rrp-` used on the non-PAICE sites.

!!! note
    Users must utilize this `aip-` naming structure in their job submissions and [storage allocations](../storage-and-data/storage_and_file_management.md) while using the PAICE clusters.

## Scheduling Calculations

Each of the above Tiers are assigned a FairShare value that is proportional to the overall cluster's Shares as per the following chart:

| Tier                                            | % total shares |
| :---------------------------------------------- | :------------: |
| **CIFAR AI Chairs**                             |      45%       |
| **AI Institute Faculty Affiliates**             |      40%       |
| **Faculty members, within an AI program**       |      10%       |
| **Faculty members, applying AI to other domains** |      5%        |

A Tier's allocation percentage will be further equally divided among the Projects assigned to the Tier and are expressed as the FairShare value in the scheduler's Project/Account.

Aside from this method of assigning Shares to an Account, the same methodology of scheduler job priority management that is outlined in [Allocations and compute scheduling](allocations_and_compute_scheduling.md) is in effect on the PAICE clusters.