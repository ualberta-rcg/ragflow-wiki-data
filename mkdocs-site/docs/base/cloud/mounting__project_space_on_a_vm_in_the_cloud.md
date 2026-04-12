---
title: "Mounting /project space on a VM in the cloud"
slug: "mounting__project_space_on_a_vm_in_the_cloud"
lang: "base"

source_wiki_title: "Mounting /project space on a VM in the cloud"
source_hash: "d6db02a5e55fa76c4d4f4da9ce032516"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:30:52.937698+00:00"

tags:
  - cloud

keywords:
  - "Cloud"
  - "/project filesystems"
  - "Security requirements"
  - "SSHFS"
  - "Virtual machine"

questions:
  - "How can a virtual machine hosted on the Cloud access the /project filesystems on the national HPC clusters?"
  - "What is SSHFS and how does it integrate the /project folder into the virtual machine's environment?"
  - "What specific security requirements must be followed when mounting the /project directory inside a virtual machine?"
  - "How can a virtual machine hosted on the Cloud access the /project filesystems on the national HPC clusters?"
  - "What is SSHFS and how does it integrate the /project folder into the virtual machine's environment?"
  - "What specific security requirements must be followed when mounting the /project directory inside a virtual machine?"

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

A reference can be found at [https://wiki.archlinux.org/index.php/SSHFS](https://wiki.archlinux.org/index.php/SSHFS)

## Requirements

!!! warning "Security Requirements"
    In order to avoid security issues, the following requirements are needed if you choose to mount /project inside your VM:

    * Do *not* store your password in plain text on the VM.
    * Create an SSH key specifically for use with SSHFS, and *only* use it for that. Do *not* use the same SSH key that you use for logging in.
    * Keep your VM up to date and only open ports that are required and secured.