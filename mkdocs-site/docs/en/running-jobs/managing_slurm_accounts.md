---
title: "Managing Slurm accounts/en"
slug: "managing_slurm_accounts"
lang: "en"

source_wiki_title: "Managing Slurm accounts/en"
source_hash: "89318dc08bdf5e2b262dad14677f1117"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:57:34.121243+00:00"

tags:
  []

keywords:
  - "Slurm"
  - "scheduling priority"
  - "Resource Allocation Project"
  - "managing usage"
  - "fairshare"

questions:
  - "How does the resource usage of an individual user impact the job scheduling priority for other members sharing the same Resource Allocation Project (RAP) account?"
  - "Why can a user running many small, backfilling jobs prevent other users in the same RAP account from successfully running jobs with larger resource requirements?"
  - "What strategies can research groups implement to effectively manage their shared account usage and mitigate priority conflicts among users?"
  - "How does the resource usage of an individual user impact the job scheduling priority for other members sharing the same Resource Allocation Project (RAP) account?"
  - "Why can a user running many small, backfilling jobs prevent other users in the same RAP account from successfully running jobs with larger resource requirements?"
  - "What strategies can research groups implement to effectively manage their shared account usage and mitigate priority conflicts among users?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Each job submitted to the [job scheduler Slurm](running-jobs.md) has an associated Resource Allocation Project (RAP) which is selected with the `--account` option to `sbatch`. The scheduling priority of the job will be determined by the target share of the account relative to the account's recent usage, as described at [Job scheduling policies](job-scheduling-policies.md).

A research group may have many individual users submitting jobs to a given RAP account. The usage of all the users within the RAP is charged to a single account, thus each user affects the priority of jobs submitted by all the users in the group. Because of this, there are circumstances when active coordination among users may improve the project's throughput.

## When can managing usage within a RAP account be useful?
A user who has not used many resources may submit a job and find that it has very low priority because other users in the group have run a lot of work recently. In this case all users of that account will have to wait for the account's fairshare (LevelFS) to return to a competitive value. Because the fairshare principle is applied *within* a group as well as *between* groups, jobs belonging to the underserved user will have the highest priority and, all else being equal, will run first when the group's fairshare recovers.

This may not happen, however, if different users in the group have jobs with drastically different requirements. For example, if one user runs a lot of small jobs which fit into scheduling gaps ("back filling" or "cycle scavenging") they may be able to achieve substantial throughput even while the group priority remains low. This will make it difficult for other users within the RAP to run jobs with greater resource requirements.

## What strategies are there for managing usage within accounts?
Several of the strategies are things that can be discussed by the group in lab meetings.

!!! tip "Strategies for managing usage"
    *   If various users have distinct deadlines that require bursts of computation it can be valuable to schedule their usage on the system so that they do not affect each others' priority at critical times.
    *   Use different clusters. The national general purpose systems are largely identical in capability, and each RAP is independently accounted on each cluster. User X of account Y on one cluster will not affect the priority of jobs submitted by user Z to account Y on another cluster.
    *   Use multiple accounts. A group that has a RAC award can submit jobs to both the RAC account and the default account; jobs running under one account will not affect the fairshare of the other account.
    *   If the research involves collaboration between different research groups, each Principal Investigator (PI) involved in the research can obtain their own account and the users' work can be divided appropriately among the separate Resource Allocation Projects.

If the above strategies are ineffective, please [contact an analyst](technical-support.md). The analyst might wish to consult [A group in conflict with itself](https://wiki.computecanada.ca/staff/Support_FAQ#A_group_in_conflict_with_itself) in the staff-facing documentation for further suggestions.