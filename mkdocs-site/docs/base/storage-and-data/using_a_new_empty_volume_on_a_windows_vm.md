---
title: "Using a new empty volume on a Windows VM"
slug: "using_a_new_empty_volume_on_a_windows_vm"
lang: "base"

source_wiki_title: "Using a new empty volume on a Windows VM"
source_hash: "d85b89ad2aca6677f822118ea7912a32"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T12:20:26.617220+00:00"

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

This page describes the steps to partition and format a volume attached to a Windows VM

1. If a new volume is not already attached, create and attach a new empty volume to a Windows VM as described in [working with volumes](working-with-volumes.md).
2. Connect to the Windows VM using a [Remote desktop connection](creating-a-windows-vm.md#remote-desktop-connection)
3. Open up "Computer Management" on the Windows VM.
4. Go to "Storage"->"Disk Management" and then right click on the new disk label probably "Disk 1" and select "online" to bring the disk online.
5. Initialize the disk by right clicking again on the disk label and selecting "Initialize Disk".
6. Right click on the "unallocated" disk pane and select create new simple volume.