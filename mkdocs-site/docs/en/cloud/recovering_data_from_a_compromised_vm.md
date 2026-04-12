---
title: "Recovering data from a compromised VM/en"
slug: "recovering_data_from_a_compromised_vm"
lang: "en"

source_wiki_title: "Recovering data from a compromised VM/en"
source_hash: "1d935633705373e5dffc168d602d23d1"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:01:38.967368+00:00"

tags:
  - cloud

keywords:
  - "OpenStack"
  - "Volume attachment"
  - "Compromised VM"
  - "Data recovery"
  - "Rebuild instance"

questions:
  - "How is a compromised virtual machine detected and initially handled by the support team?"
  - "Why must a user build a new virtual machine instead of restarting the compromised one?"
  - "What are the step-by-step procedures for attaching and accessing the compromised volume on a new recovery instance?"
  - "How is a compromised virtual machine detected and initially handled by the support team?"
  - "Why must a user build a new virtual machine instead of restarting the compromised one?"
  - "What are the step-by-step procedures for attaching and accessing the compromised volume on a new recovery instance?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Parent page:* [Cloud](cloud.md)

You are responsible for recovering data from a virtual machine (VM) that has been compromised.

!!! note
    This page provides an outline of the necessary steps for this situation, though it is not exhaustive.

## What happens when we detect a compromised VM?

1.  Our support team confirms this by investigating network traffic logs and other sources.
2.  The VM is shut down and locked at the sysadmin level.
3.  You are notified by email.

## Why do you need to rebuild?

-   You cannot start an administratively locked VM.
-   The contents of the VM are no longer trustworthy, but it is relatively safe to extract the data.
-   You have to build a new VM.

## What steps should you take?

1.  Send an email to [cloud@tech.alliancecan.ca](mailto:cloud@tech.alliancecan.ca) outlining your recovery plan; if access to the filesystem is required, the cloud support team will unlock the volume.
2.  Log in to the OpenStack admin console.
3.  Launch a new instance that will be used for data rescue operations.
4.  Under *Volumes*, select *Manage Attachments* from the dropdown list at the far right for the volume that was compromised and click on the *Detach Volume* button.
5.  Under *Volumes*, select *Manage Attachments* for the volume that was compromised and select *Attach To Instance* (select the recovery instance you just launched).
6.  SSH into your recovery instance: you will now see your old, compromised volume available as the `vdb` disk.
7.  Mounting the appropriate filesystem from a partition or an LVM logical volume depends on how the base OS image was created. Because instructions vary greatly, contact someone with experience to continue.