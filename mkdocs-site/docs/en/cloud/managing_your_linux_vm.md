---
title: "Managing your Linux VM/en"
slug: "managing_your_linux_vm"
lang: "en"

source_wiki_title: "Managing your Linux VM/en"
source_hash: "051646d274d2a8594fb4e01c913742d4"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T08:24:41.834770+00:00"

tags:
  - cloud

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

The majority of researchers use the Linux operating system on their VMs. Common Linux distributions used are AlmaLinux, CentOS, Debian, Fedora, and Ubuntu. This page will help you with some common tasks to manage your Linux VM. VMs can also run the Microsoft Windows operating system. Some Windows management tasks are described [here](cloud-quick-start.md#windows).

## Linux VM user management
There are a number of ways to allow more than one person to log into a VM. We recommend creating new user accounts and adding public [SSH keys](ssh-keys.md) to these accounts.

### Creating a user account and keys
A new user account can be created on Ubuntu with the command:

```bash
sudo adduser --disabled-password USERNAME
```

To be able to connect, the new user will need to have a key pair. See [generating SSH keys in Windows](generating-ssh-keys-in-windows.md) or [creating a key pair in Linux or Mac](using-ssh-keys-in-linux.md#creating-a-key-pair) depending on the operating system they will be connecting from. Then, their public key must be added to `/home/USERNAME/.ssh/authorized_keys` on the VM, ensuring permissions and ownership are correct as described in steps 2 and 3 of [Connecting using a key pair](using-ssh-keys-in-linux.md#connecting-using-a-key-pair).

### Granting admin privileges
In Ubuntu, administrative or root user privileges can be given to a new user with the command:

```bash
sudo visudo -f /etc/sudoers.d/90-cloud-init-users
```

which opens an editor where a line like `USERNAME ALL=(ALL) NOPASSWD:ALL` can be added. For more detailed information about the `visudo` command and how to edit this file see this [DigitalOcean tutorial](https://www.digitalocean.com/community/tutorials/how-to-edit-the-sudoers-file-on-ubuntu-and-centos#what-is-visudo).

### Dealing with system and security issues
See our guides for how to:

*   [recover data from a compromised VM](recovering-data-from-a-compromised-vm.md)
*   [recover your VM from the dashboard](vm-recovery-via-cloud-console.md)