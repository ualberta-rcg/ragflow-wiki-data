---
title: "VM Best Practices"
slug: "vm_best_practices"
lang: "base"

source_wiki_title: "VM Best Practices"
source_hash: "eb4e35d918f9b46cf0401f623d148cca"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:33:38.780806+00:00"

tags:
  - cloud

keywords:
  - "Compute Canada cloud"
  - "VM"
  - "Operating system upgrades"
  - "Kernel timeouts"
  - "Data volumes"

questions:
  - "Why is it highly recommended to create a backup of a virtual machine before performing a major operating system upgrade?"
  - "What is the primary reason for creating a separate data volume instead of relying solely on the root volume for storage?"
  - "What potential issues can occur if more than three volumes are attached to a single virtual machine?"
  - "Why is it highly recommended to create a backup of a virtual machine before performing a major operating system upgrade?"
  - "What is the primary reason for creating a separate data volume instead of relying solely on the root volume for storage?"
  - "What potential issues can occur if more than three volumes are attached to a single virtual machine?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Parent page: [Cloud](cloud.md)*

This page provides some guidance based on user experiences with Compute Canada's cloud instances. Your mileage may vary.

## Upgrades

!!! warning "Operating System Upgrades"
    Updating packages is often a safe operation and is recommended for security reasons. Upgrading from one major version of an operating system to the next is also a good security measure; however, performing a major operating system upgrade can often cause problems. Before doing any major operating system upgrades (e.g., `ubuntu 20.0` to `ubuntu 22.0`), create a [backup](backing_up_your_vm.md) of your VM so that if the process fails for some reason, you will be able to recover from it.

## Volumes

### Data volumes

!!! tip "Separate Data Volumes"
    It is very difficult to expand a root volume, so for any VM which does not have bounded storage requirements, **consider creating a second volume for data**. If more space is needed, and your allocation has enough remaining volume storage, it is fairly straightforward to expand the data volume using OpenStack and then to expand the logical volume, if any, and filesystem within your VM.

### Maximum volumes per VM

!!! warning "Limit Volumes to Three"
    **Avoid attaching more than three volumes to a VM**. This has been observed to lead to kernel timeouts which can affect any disk operations on those volumes and may have a cascading effect, and can render the VM effectively inoperative. While using a data volume is advisable in some cases (see above), use only one and you can carve it up into multiple filesystems inside your VM, and expand it as necessary.

This has been observed on Arbutus (arbutus.cloud.computecanada.ca) by multiple users, although it may be somewhat dependent on volume size. In one case, 3 x 100GB volumes attached to a `p4-6gb` VM caused kernel timeouts whenever disk operations of any magnitude were attempted. It was very difficult to copy more than 500MB of data between two filesystems, for example.

Test of a similar situation was performed on East cloud and with 4 x 100GB data volumes (along with the root volume), the same OS and a similar VM flavour, the issue did not occur. This VM had more memory (15 GB instead of 6 GB) but high memory usage was not observed in the Arbutus case and this isn't believed to be a factor.