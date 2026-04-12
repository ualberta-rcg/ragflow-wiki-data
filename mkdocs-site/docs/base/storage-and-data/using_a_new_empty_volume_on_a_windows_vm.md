---
title: "Using a new empty volume on a Windows VM"
slug: "using_a_new_empty_volume_on_a_windows_vm"
lang: "base"

source_wiki_title: "Using a new empty volume on a Windows VM"
source_hash: "d85b89ad2aca6677f822118ea7912a32"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:21:03.157056+00:00"

tags:
  []

keywords:
  - "Initialize Disk"
  - "Disk Management"
  - "create new simple volume"
  - "Windows VM"
  - "partition and format a volume"

questions:
  - "How do you prepare the Windows VM and connect to it before configuring a new volume?"
  - "Which administrative tool must be opened on the Windows VM to access the disk configuration settings?"
  - "What are the exact steps required within Disk Management to bring a new disk online, initialize it, and create a usable volume?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# Using a new empty volume on a Windows VM

This page describes the steps to partition and format a volume attached to a Windows VM.

1.  If a new volume is not already attached, create and attach a new empty volume to a Windows VM as described in [working with volumes](working-with-volumes.md).
2.  Connect to the Windows VM using a [Remote desktop connection](creating-a-windows-vm.md#remote-desktop-connection).
3.  Open up "Computer Management" on the Windows VM.
4.  Go to "Storage"->"Disk Management" and then right-click on the new disk label (probably "Disk 1") and select "online" to bring the disk online.
5.  Initialize the disk by right-clicking again on the disk label and selecting "Initialize Disk".
6.  Right-click on the "unallocated" disk pane and select "create new simple volume".