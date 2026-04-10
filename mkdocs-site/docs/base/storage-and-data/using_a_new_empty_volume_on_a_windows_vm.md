---
title: "Using a new empty volume on a Windows VM"
tags:
  []

keywords:
  []
---

This page describes the steps to partition and format a volume attached to a Windows VM

# If a new volume is not already attached, create and attach a new empty volume to a Windows VM as described in [working with volumes](working_with_volumes.md).
# Connect to the Windows VM using a [Remote desktop connection](creating_a_windows_vm#remote_desktop_connection.md)
# Open up "Computer Management" on the Windows VM. 
# Go to "Storage"->"Disk Management" and then right click on the new disk label probably "Disk 1" and select "online" to bring the disk online.
# Initialize the disk by right clicking again on the disk label and selecting "Initialize Disk". 
# Right click on the "unallocated" disk pane and select create new simple volume.