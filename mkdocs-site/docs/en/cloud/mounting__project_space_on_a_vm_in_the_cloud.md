---
title: "Mounting /project space on a VM in the cloud/en"
slug: "mounting__project_space_on_a_vm_in_the_cloud"
lang: "en"

source_wiki_title: "Mounting /project space on a VM in the cloud/en"
source_hash: "6dd0d15389239ceead354fcf4855fab3"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:31:04.139993+00:00"

tags:
  - cloud

keywords:
  - "Cloud"
  - "SSH key"
  - "/project filesystems"
  - "SSHFS"
  - "Virtual machine"

questions:
  - "Why do virtual machines hosted on the Cloud require SSHFS to access /project filesystems?"
  - "How does an SSHFS mount function and appear within the virtual machine's operating system?"
  - "What specific security requirements must be followed when mounting the /project filesystem inside a virtual machine?"
  - "Why do virtual machines hosted on the Cloud require SSHFS to access /project filesystems?"
  - "How does an SSHFS mount function and appear within the virtual machine's operating system?"
  - "What specific security requirements must be followed when mounting the /project filesystem inside a virtual machine?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Introduction

This document describes how to let a virtual machine (VM) access [/project](../storage-and-data/project_layout.md) filesystems on the national systems. VMs hosted on our [Cloud](cloud.md) do not have direct access to the filesystems on the national HPC clusters. In order to access files stored on /project from a VM, please use SSHFS and observe the requirements mentioned below.

## SSHFS

SSHFS enables mounting your /project folder inside your VM.
SSHFS mounts appear like regular folders in your VM and can be accessed via regular Linux commands.

A reference can be found at https://wiki.archlinux.org/index.php/SSHFS.

## Requirements

!!! warning "Security Requirements for Mounting /project"
    In order to avoid security issues, the following requirements are needed if you choose to mount /project inside your VM:

    *   Do *not* store your password in plain text on the VM.
    *   Create an SSH key specifically for use with SSHFS, and *only* use it for that. Do *not* use the same SSH key that you use for logging in.
    *   Keep your VM up to date and only open ports that are required and secured.