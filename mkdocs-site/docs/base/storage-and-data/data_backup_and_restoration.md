---
title: "Data backup and restoration"
slug: "data_backup_and_restoration"
lang: "base"

source_wiki_title: "Data backup and restoration"
source_hash: "4ce8cee05eaddde1a8d35491d07bcef0"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T06:00:00.373501+00:00"

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

!!! info "Important Backup Parameters"
    The following parameters outline important numbers for backup and archival processes. These limits, such as the maximum number of daily file changes per user, are established to prevent individual user backups from becoming bottlenecks for the overall backup processes.

## TSM /project backup
*   The most recent version is always kept
*   Number of inactive versions of files to be kept: 1 (2nd copy)
*   Time to keep inactive versions: 60 days
*   Number of deleted versions to be kept: 1
*   Time to keep deleted versions: 60 days
*   Maximum number of file changes per day by every project: 50k files

## TSM /project archival
*   Default archival allocation per project: 10 TB
*   Maximum time to keep archive: 1 year
*   Maximum number of files to be archived: 50k files
*   Number of copies of archived files to keep: 1

## TSM /project restore
*   Maximum number of files to be restored per project per day: 50k files
*   Maximum restore size per day: 10 TB