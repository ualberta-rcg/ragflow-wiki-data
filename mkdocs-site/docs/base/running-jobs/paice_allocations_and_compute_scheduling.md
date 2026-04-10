---
title: "PAICE Allocations and compute scheduling"
slug: "paice_allocations_and_compute_scheduling"
lang: "base"

source_wiki_title: "PAICE Allocations and compute scheduling"
source_hash: "52bf73868f237f9cc58caa6f9280abfc"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T09:40:56.413699+00:00"

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

## Overview

The Pan Canadian AI Environment (PAICE) clusters, which consists of [Vulcan](vulcan.md), [Killarney](killarney.md) and [TamIA](tamia.md) borrow strongly from the Alliance's traditional [Allocations and compute scheduling](allocations-and-compute-scheduling.md) methodologies, but differ in how resource allocations are assigned.

The PAICE sites do not participate in the Resource Allocation Competition (RAC) and instead derive cluster computational allocations by grouping Projects into one of four groups, which are then allocated resources on the three clusters.

## Identification and Grouping
There are 4 Tiers of users identified;

*   Canada CIFAR AI Chairs and Equivalents and their research teams
*   AI Institute Faculty Affiliates
*   Faculty members with a tenure track appointment at a Canadian university within an AI program
*   Faculty members with a tenure track appointment at a Canadian university applying AI to other domains

Users are assigned to an AI-specific slurm Account and POSIX group with the prefix of `aip-` versus the more familiar `rrg-` or `rrp-` used on the non-PAICE sites.
!!! info
    Users must utilize this naming structure in their job submissions and [storage allocations](storage-and-file-management.md) while using the PAICE clusters.

## Scheduling Calculations
Each of the above Tiers are assigned a FairShare value that is proportional to the overall cluster's Shares as per the following chart;

PAICE Tiering Allocations

| Tier                                                  | % total shares |
| :---------------------------------------------------- | :------------: |
| CIFAR AI Chairs                                       |       45%      |
| AI Institute Faculty Affiliates                       |       40%      |
| Faculty members, within an AI program                 |       10%      |
| Faculty members, applying AI to other domains         |        5%      |

A Tier's allocation percentage will be further equally divided among the Projects assigned to the Tier and are expressed as the FairShare value in the scheduler's Project/Account.

Aside from this method of assigning Shares to an Account, the same methodology of scheduler job priority management that is outlined in [Allocations and compute scheduling](allocations-and-compute-scheduling.md) is in effect on the PAICE clusters.