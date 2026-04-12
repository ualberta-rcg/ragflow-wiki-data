---
title: "Managing your Linux VM"
slug: "managing_your_linux_vm"
lang: "base"

source_wiki_title: "Managing your Linux VM"
source_hash: "30af6413c558553839aa48b421770fb3"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:58:04.048768+00:00"

tags:
  - cloud

keywords:
  - "User management"
  - "System recovery"
  - "Linux VM"
  - "SSH keys"
  - "Admin privileges"

questions:
  - "How can a new user account be created and configured with SSH keys on an Ubuntu virtual machine?"
  - "What command and file edits are required to grant administrative privileges to a user in Ubuntu?"
  - "What resources are available for recovering data or restoring a virtual machine if it becomes compromised?"
  - "How can a new user account be created and configured with SSH keys on an Ubuntu virtual machine?"
  - "What command and file edits are required to grant administrative privileges to a user in Ubuntu?"
  - "What resources are available for recovering data or restoring a virtual machine if it becomes compromised?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

The majority of researchers use the Linux Operating System on their VMs. Common Linux distributions used are AlmaLunix, CentOS, Debian, Fedora, and Ubuntu. This page will help you with some common tasks to manage your Linux VM. VMs can also run the Microsoft Windows operating system. Some Windows management tasks are described [here](cloud_quick_start.md).

# Linux VM user management
There are a number of ways to allow more than one person to log into a VM. We recommend creating new user accounts and adding public [SSH Keys](../getting-started/ssh_keys.md) to these accounts.

## Creating a user account and keys
A new user account can be created on Ubuntu with the command
```bash
sudo adduser --disabled-password USERNAME
```
To be able to connect, the new user will need to have a key pair, see [generating SSH keys in Windows](../getting-started/generating_ssh_keys_in_windows.md) or [creating a key pair in Linux or Mac](../getting-started/using_ssh_keys_in_linux.md#creating-a-key-pair) depending on the operating system they will be connecting from. Then, their public key must be added to `/home/USERNAME/.ssh/authorized_keys` on the VM, ensuring permissions and ownership are correct as described in steps 2 and 3 of [Connecting using a key pair](../getting-started/using_ssh_keys_in_linux.md#connecting-using-a-key-pair).

## Granting admin privileges
In Ubuntu, administrative or root user privileges can be given to a new user with the command
```bash
sudo visudo -f /etc/sudoers.d/90-cloud-init-users
```
which opens an editor where a line like
```text
USERNAME ALL=(ALL) NOPASSWD:ALL
```
can be added. For more detailed information about the `visudo` command and how to edit this file see this [digitalocean](https://www.digitalocean.com/community/tutorials/how-to-edit-the-sudoers-file-on-ubuntu-and-centos#what-is-visudo) tutorial.

## Dealing with system and security issues
See our guides for how to
*   [recover data from a compromised VM](recovering_data_from_a_compromised_vm.md)
*   [recover your VM from the dashboard](vm_recovery_via_cloud_console.md)