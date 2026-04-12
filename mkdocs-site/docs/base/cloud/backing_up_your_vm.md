---
title: "Backing up your VM"
slug: "backing_up_your_vm"
lang: "base"

source_wiki_title: "Backing up your VM"
source_hash: "4440733a0ee34ca51d39aa5b16a662b7"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:45:34.128516+00:00"

tags:
  - cloud

keywords:
  - "Compute VMs"
  - "OpenStack"
  - "Volumes"
  - "VM snapshots"
  - "create images"
  - "Volume snapshots"
  - "Disk images"
  - "Backup strategies"
  - "QCOW2"
  - "disk format"
  - "VM backups"
  - "volumes"
  - "Virtual machine backup"

questions:
  - "What is the 3-2-1 backup rule, and which tools are recommended for performing file-level backups of a virtual machine?"
  - "How can provisioning and orchestration tools be used to automate the setup and recreation of a virtual machine's software and operating system?"
  - "What are the steps and precautions required to safely create a backup image from a volume attached to a Persistent VM in OpenStack?"
  - "What are the differences between volume snapshots and VM snapshots in OpenStack, and why are volume snapshots considered less than ideal for backups?"
  - "How does the process of creating a backup image for a Compute VM differ from a persistent VM, and what specific data is excluded from a Compute VM snapshot?"
  - "What is the recommended backup strategy for managing large disk images, datasets, and databases to ensure a system can be successfully restored?"
  - "What state must a volume be in before an image can be created from it?"
  - "What are the specific steps required to create an image from a volume?"
  - "Why is the QCOW2 disk format generally recommended over Raw, vmdk, or vdi formats in this context?"
  - "What are the differences between volume snapshots and VM snapshots in OpenStack, and why are volume snapshots considered less than ideal for backups?"
  - "How does the process of creating a backup image for a Compute VM differ from a persistent VM, and what specific data is excluded from a Compute VM snapshot?"
  - "What is the recommended backup strategy for managing large disk images, datasets, and databases to ensure a system can be successfully restored?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Parent page: [Cloud](cloud.md)*

There are a few different strategies to back up your virtual machine and to recover from disasters, which you choose will depend on your requirements and your particular use case. Creating backups in locations outside the cloud is strongly encouraged. A very common backup rule is the 3-2-1 backup rule, which states that you should have three copies of your data stored on at least two different types of media and one of those copies should be offsite. Below are a few common methods to back up or preserve the state of your virtual machine followed by an example strategy of how a few of these methods might be used together to create a complete backup strategy.

## File backup
Many of the backup strategies for physical machines still apply to virtual machines, for example tools such as [rsync](https://rsync.samba.org/), [duplicity](https://nongnu.org/duplicity/), [borg](https://borgbackup.readthedocs.io/), or [restic](https://restic.readthedocs.io/) can be used to perform backups of the data within your VM to remote locations.

## Setup automation
Provisioning tools such as [Ansible](https://www.ansible.com/), [Puppet](https://puppet.com/), [Chef](https://www.chef.io/), and [SaltStack](https://saltstack.com/) can be used to automate setup and configuration of software and operating systems. Recreating your virtual machine then becomes a trivial matter given the right specification files for a given provisioning tool. These specification files can be managed with version control tools like [Git](https://git-scm.com/). Provisioning tools can be combined with orchestration tools such as Heat and Terraform (see [Automating VM creation](automating-vm-creation.md)) to automate the entire process of virtual machine creation and software configuration. Any data which is generated or created outside this automation would then need to be backed up using one of the [file backup](#file-backup) methods.

## OpenStack backup methods
OpenStack has two different storage options: Volumes, which are protected by 3 times replication, and ephemeral storage local to the VM. The 3 times replication of Volumes is to protect against hardware failure and does not protect against accidental deletion or data loss from malicious intent. Data stored on node local ephemeral storage can suffer data loss due to hardware failure and should not be relied upon for any critical data and is best suited to temporary or working data.

OpenStack provides tools to create disk images and snapshots of your virtual machines. The two main VM flavours - persistent (p) and compute (c) - have different behaviours, so we recommend different procedures for backing up each flavour.

### Persistent VMs
Persistent VMs are designed to boot from volumes (see [booting from a volume](working-with-volumes.md#booting-from-a-volume)) thus creating a copy of the volume(s) the VM has attached to it will produce a backup. However this would not preserve things like VM flavour, public IP, and security rules. The best way to create a copy of a volume for backup purposes is to create an image from that volume. An image can be [downloaded](working-with-images.md#downloading-an-image) and reused to create multiple new VMs, can be [accessed by VirtualBox](working-with-images.md#creating-a-virtualbox-vm-from-a-cloud-image) on your desktop or laptop, and [uploaded](working-with-images.md#uploading-an-image) to other clouds.

To be able to create an image from a volume, that volume must be detached from the VM. In addition, if the volume is the root volume of the VM it cannot be detached unless the VM is deleted. If you are sure that when you created the VM you did not check the box "Delete Volume on Instance Delete", then you can delete your VM knowing you will not lose any data. However, if you are unsure whether or not you checked this box, OpenStack unfortunately doesn't tell you if this box was checked when you created a VM.

!!! tip "Ensuring volume retention when deleting a VM"
    One trick which may be useful for getting around this deficiency is to create a snapshot of the volume provided you have a storage quota which allows it, since snapshots count towards your storage quota. As volumes cannot be deleted if there is a volume snapshot created from them, when you delete the VM the volume will not be deleted even if you checked the box.

At this point all the volumes you wish to create images of should be in the "Available" state. To create an image from a volume, select 'Upload to Image' from the drop down menu for the volume. Select the 'QCOW2' disk format and give your image a name. There are several formats for disk images but QCOW2 works well with OpenStack and typically does not take up as much space as "Raw" images. Other formats "vmdk" and "vdi" can be useful when working with other virtualization tools such as VirtualBox.

Once you have created images of all the volumes you wish to back up you can then re-create your VM booting from the original VM's root volume and attaching any additional volumes you may have had attached to the original VM.

#### What about volume snapshots?
Another alternative might be to create a snapshot of a volume, which will save the state of a volume at the time the snapshot was created.

!!! warning "Volume snapshots are not ideal for backups"
    Volume snapshots depend on the original volume remaining intact and as such are not ideal for backups. It is also not possible to download volume snapshots as they depend on the original volume.

However, they do allow you to create a new volume from a snapshot of a volume. For example, if there were file changes since the last volume snapshot you would like to revert. Or if there were file changes specific to that VM which should not be included in other VMs.

#### What about VM snapshots?
Unfortunately, OpenStack uses the word "snapshot" to mean two different things. There are volume snapshots, as discussed above, and snapshots of VMs. Snapshots of VMs behave in different ways depending on the flavour of your VM. If you have a persistent VM and create a snapshot of the VM, OpenStack creates a nearly empty image, which contains pointers to volume snapshots. These pointers point to volume snapshot(s) of the persistent VM's boot volume and any attached volumes which were created as part of creating a snapshot of the VM. You can then create a new VM (boot from image (creates a new volume)) which will create new volumes from the snapshots of the volumes taken previously, boot a new VM from the root volume and attach any other duplicated volumes.

### Compute VMs
As with creating backups of persistent VMs, the main goal is to create an image of at least the root drive, and perhaps also other attached volumes if needed. However, differences with compute flavour VMs change the process of creating that image. Compute VMs are not designed to boot from volumes accessed over the network as persistent VMs are, instead they are meant to be booted from disk images which reside locally on the computer which is actually running your VM. This means there is no volume which you can click on in the OpenStack dashboard to create an image of your root disk. Instead you can do this by clicking "Create Snapshot" on your VM's drop-down menu on the "Instances" tab. As with creating a snapshot with a persistent VM this creates an image; however, in this case the image isn't nearly as empty (i.e. containing only pointers to volume snapshots) since the image instead contains a copy of the VM's root drive.

Compute VMs also come with an extra data drive mounted at `/mnt` and the data on this drive is not captured in the image created of a compute VM. Other arrangements must be made to save this data, such as copying it off the disk before the VM is terminated.

## An example backup strategy
Very large disk images (larger than 10-20 GB) can become difficult to manage with relatively long upload times and long VM creation times. A good basic strategy might be to separate large data sets from your operating system and software stack. The operating system and software stack can be backed up either using a disk image or recreated using some provisioning software (see [setup automation](#setup-automation)). The data sets can then be backed up with using normal [file backup](#file-backup) methods to a remote location. If you are using any database software such as MySQL or PostgreSQL you will want to create dumps of the databases to include in your backups.

!!! important "Test your backups!"
    Finally, and most importantly, **test restoring from your backup**. If you can't restore from your backup it isn't very useful.

## See also
*   [OpenStack command line clients](openstack-command-line-clients.md)
*   [Creating an image from a VM](working-with-images.md#creating-an-image-from-a-vm)
*   [Downloading an image](working-with-images.md#downloading-an-image)
*   [Uploading an image](working-with-images.md#uploading-an-image)
*   [Synchronizing files](transferring-data.md#synchronizing-files)