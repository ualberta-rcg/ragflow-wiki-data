---
title: "Working with VMs/en"
slug: "working_with_vms"
lang: "en"

source_wiki_title: "Working with VMs/en"
source_hash: "69b898156568f3475fea1db8b47f6169"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T13:38:11.354760+00:00"

tags:
  - cloud

keywords:
  - "OpenStack"
  - "Locking VMs"
  - "Virtual machine flavors"
  - "Resizing VMs"
  - "Virtual machine"

questions:
  - "What is the purpose of locking a virtual machine in OpenStack, and how does it affect the instance's functionality?"
  - "What are the potential risks associated with resizing a virtual machine, and what precautions should be taken before doing so?"
  - "How does the resizing process differ between \"c\" flavor and \"p\" flavor virtual machines, particularly concerning ephemeral drives?"
  - "What is the purpose of locking a virtual machine in OpenStack, and how does it affect the instance's functionality?"
  - "What are the potential risks associated with resizing a virtual machine, and what precautions should be taken before doing so?"
  - "How does the resizing process differ between \"c\" flavor and \"p\" flavor virtual machines, particularly concerning ephemeral drives?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Parent page: [Cloud](cloud.md)*

A virtual machine (VM) is a virtualized server in the cloud infrastructure. In OpenStack, active virtual machines are referred to as instances. VMs can be managed via the OpenStack dashboard.

## Working with VMs
### Locking VMs
When working on a project with multiple people or to protect a VM from accidental deletion or shutdown, it can be useful to lock it.

To **lock** a VM, click on the "Lock Instance" option from the Actions drop-down menu on the dashboard.

!!! note
    Once a VM is locked most of the Actions menu items will not be able to be executed until the instance is unlocked. There is an icon indicating the lock state for every instance.

To **unlock** a VM, select the "Unlock Instance" from the Actions drop-down menu on the dashboard.

### Resizing VMs
It is possible to resize a VM by changing its flavour. However, there are some things to be aware of when choosing to resize a VM which depends on whether you have a "p" flavour or a "c" flavour VM (see [Virtual machine flavours](virtual-machine-flavors.md)).

!!! warning
    Resizing a VM may involve some risk as it is similar to deleting and recreating your VM with a new flavour. If in doubt, contact cloud [technical support](technical-support.md).

#### c flavours
"c" flavours often have extra ephemeral drives, which will be resized when you choose a new "c" flavour. These ephemeral drives cannot become smaller, and as such "c" flavour VMs can only be resized to flavours with equal or larger ephemeral drives. After resizing however, you will not immediately see a larger ephemeral drive within your VM (e.g. the [`df -h`](https://en.wikipedia.org/wiki/Df_(Unix)) command will not show the size increase). To see this extra space you will need to resize your filesystem (see the [`resize2fs`](https://linux.die.net/man/8/resize2fs) command).

!!! warning
    Filesystem resizes should be treated with caution and can take considerable time if the partitions are large. Before resizing a filesystem, it is recommended to create backups of its contents (see [backing up your VM](backing-up-your-vm.md)).

#### p flavours
Unlike "c" flavours, "p" flavours do not typically have extra ephemeral drives associated with them, so they can be resized to larger and smaller flavours.