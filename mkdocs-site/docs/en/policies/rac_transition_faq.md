---
title: "RAC transition FAQ/en"
slug: "rac_transition_faq"
lang: "en"

source_wiki_title: "RAC transition FAQ/en"
source_hash: "166b39bfb65f8f63871624957fad3fc2"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:55:48.674200+00:00"

tags:
  []

keywords:
  - "transition period"
  - "quotas"
  - "storage allocations"
  - "Resource Allocation Competition"
  - "job scheduling"

questions:
  - "How are storage quotas managed during the 30-day transition period, and what is the protocol for transferring data if an allocation moves to a new site?"
  - "What are the consequences for users who leave their data on an original site exceeding the default quota after the transition period ends?"
  - "How will the implementation of the new allocations on April 1 impact job scheduling priorities, currently running jobs, and waiting jobs?"
  - "How are storage quotas managed during the 30-day transition period, and what is the protocol for transferring data if an allocation moves to a new site?"
  - "What are the consequences for users who leave their data on an original site exceeding the default quota after the transition period ends?"
  - "How will the implementation of the new allocations on April 1 impact job scheduling priorities, currently running jobs, and waiting jobs?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Allocations from the 2021 Resource Allocation Competition come into effect on April 1, 2021.
Here are some notes on how we expect the transition to go.

### Storage
* There will be 30 days of overlap between 2020 and 2021 storage allocations, starting on April 1, 2021.
* On a given system, the largest of the two quotas (2020, 2021) will be adopted during the transition period.
* If an allocation has moved from one site to another, users are expected to transfer the data by themselves (via globus, scp, rsync, *etc.*; see [Transferring data](../getting-started/transferring_data.md)). For large amounts of data (*e.g.*, 200TB or more) please [contact support](../support/technical_support.md) for advice or assistance on managing the transfer.
* Contributed storage systems have different dates of activation and decommissioning. For these, we'll be doing the SUM(2020, 2021) for quotas during the 30-day transition period.
* For every other PI, we will use default quotas.
* After the transition period, the quotas on the original sites from which data has been migrated will also be set to default. Users are expected to delete data from those original sites if the usage levels are above the new (default) quota.

!!! warning "Storage Quota Enforcement"
    If usage remains above the new quota after the overlap period, staff may choose to delete everything.

* Reasonable requests for extension of the overlap period will be honoured, but such an extension may be impossible or severely constrained if the original cluster is being defunded.

### Job scheduling
* The scheduler team is planning to archive and compact the Slurm database on March 31 before implementing the new allocations on April 1. We hope to schedule the archiving and compaction during off-peak hours.

!!! note "Scheduler Database Activity"
    During this time, the database may be unresponsive. Specifically, `sacct` and `sacctmgr` may be affected.

* We expect to begin replacing 2020 allocations with 2021 allocations on April 1.

!!! warning "Job Priority Inconsistency"
    Job priority may be inconsistent during the allocation cutover. Specifically, default allocations may face decreased priority.

* Jobs already in the system will be retained. Running jobs will not be stopped. Waiting jobs may be held.

!!! warning "Waiting Jobs and Allocation Changes"
    Waiting jobs attributed to an allocation which has been moved or not renewed may not schedule after the cutover. Advice on how to detect and handle such jobs will be forthcoming.