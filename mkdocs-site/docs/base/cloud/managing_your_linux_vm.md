---
title: "Managing your Linux VM"
tags:
  - cloud

keywords:
  []
---

The majority of researchers use the Linux Operating System on their VMs.  Common Linux distributions used are AlmaLunix, CentOS, Debian, Fedora, and Ubuntu.  This page will help you with some common tasks to manage your Linux VM.  VMs can also run the Microsoft Windows operating system.  Some Windows management tasks are described [here](cloud_quick_start#windows.md).

=Linux VM user management= 
There are a number of ways to allow more than one person to log into a VM. We recommend creating new user accounts and adding public [SSH Keys](ssh-keys.md) to these accounts.

==Creating a user account and keys== 
A new user account can be created on Ubuntu with the command 
```bash
sudo adduser --disabled-password USERNAME
```
 To be able to connect, the new user will need to have a key pair, see [generating SSH keys in Windows](generating_ssh_keys_in_windows.md) or [creating a key pair in Linux or Mac](using_ssh_keys_in_linux#creating-a-key-pair.md) depending on the operating system they will be connecting from. Then, their public key must be added to `/home/USERNAME/.ssh/authorized_keys` on the VM, ensuring permissions and ownership are correct as described in steps 2 and 3 of [Connecting using a key pair](using_ssh_keys_in_linux#connecting-using-a-key-pair.md).

==Granting admin privileges== 
In Ubuntu, administrative or root user privileges can be given to a new user with the command

```bash
sudo visudo -f /etc/sudoers.d/90-cloud-init-users
```

which opens an editor where a line like
 USERNAME ALL=(ALL) NOPASSWD:ALL
can be added. For more detailed information about the `visudo` command and how to edit this file see this [digitalocean](https://www.digitalocean.com/community/tutorials/how-to-edit-the-sudoers-file-on-ubuntu-and-centos#what-is-visudo) tutorial.

==Dealing with system and security issues== 
See our guides for how to 
* [recover data from a compromised VM](recovering_data_from_a_compromised_vm.md)
* [recover your VM from the dashboard](vm_recovery_via_cloud_console.md)