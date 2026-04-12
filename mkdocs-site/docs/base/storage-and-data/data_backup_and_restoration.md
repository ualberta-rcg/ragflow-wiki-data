---
title: "Data backup and restoration"
slug: "data_backup_and_restoration"
lang: "base"

source_wiki_title: "Data backup and restoration"
source_hash: "4ce8cee05eaddde1a8d35491d07bcef0"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:45:13.810651+00:00"

tags:
  []

keywords:
  - "TSM"
  - "file changes"
  - "project restore"
  - "project archival"
  - "project backup"

questions:
  - "Why is it necessary to limit the maximum number of daily file changes for individual users in the backup process?"
  - "What are the specific retention rules and timeframes for keeping inactive and deleted versions of files in the TSM project backup?"
  - "What are the maximum daily limits and default storage allocations set for archiving and restoring project files?"
  - "Why is it necessary to limit the maximum number of daily file changes for individual users in the backup process?"
  - "What are the specific retention rules and timeframes for keeping inactive and deleted versions of files in the TSM project backup?"
  - "What are the maximum daily limits and default storage allocations set for archiving and restoring project files?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! important
    To prevent individual user backups from creating bottlenecks for the entire backup process, it is necessary to limit the maximum number of file changes per day by a user.

## TSM /project backup

*   The most recent version of a file is always kept.
*   Number of inactive versions of files to be kept: 1 (a second copy).
*   Time to keep inactive versions: 60 days.
*   Number of deleted versions to be kept: 1.
*   Time to keep deleted versions: 60 days.
*   Maximum number of file changes per day for every project: 50,000 files.

## TSM /project archival

*   Default archival allocation per project: 10 TB.
*   Maximum time to keep an archive: 1 year.
*   Maximum number of files to be archived: 50,000 files.
*   Number of copies of archived files to keep: 1.

## TSM /project restore

*   Maximum number of files to be restored per project per day: 50,000 files.
*   Maximum restore size per day: 10 TB.