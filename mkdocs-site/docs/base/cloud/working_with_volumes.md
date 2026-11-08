---
title: "Working with volumes"
slug: "working_with_volumes"
lang: "base"

source_wiki_title: "Working with volumes"
source_hash: "e59c9bf1fa52751f099e245ece98443e"
last_synced: "2026-11-08T02:07:32.985064+00:00"
last_processed: "2026-11-08T03:02:53.194105+00:00"

tags:
  - cloud

keywords:
  - "qcow2"
  - "disk format qcow2"
  - "openstack image create"
  - "download the image"
  - "OpenStack command line"
  - "blkid"
  - "vmdk"
  - "storage backend migration"
  - "On Demand"
  - "UUID"
  - "high_performance"
  - "volume type change"
  - "Delete on Terminate"
  - "mount /etc/fstab"
  - "Retyping"
  - "volume type"
  - "high_performance storage"
  - "cloning a volume"
  - "Create Volume"
  - "boot from volume"
  - "automatic mount"
  - "OpenStack command line client"
  - "Attach Volume"
  - "/etc/fstab"
  - "changing volume type"
  - "retype-policy on-demand"
  - "create image from volume"
  - "Ceph storage"
  - "detaching a volume"
  - "disk format"
  - "OpenStack CLI"
  - "Change Volume Type"
  - "defaults"
  - "nofail"
  - "Volumes page"

questions:
  - "What are the differences between the **rbd1** and **high_performance** volume types regarding storage media and data‑safety mechanisms?"
  - "Which fields must be filled in and what steps must be followed to create a new volume through the OpenStack dashboard?"
  - "After a volume is attached to a VM, what procedures (formatting, mounting, and optional fstab configuration) are needed to make the volume usable?"
  - "How can you view the UUID and other mounting information of a volume in a Linux system?"
  - "What file must be edited to configure a volume to mount automatically at boot, and what information needs to be added?"
  - "What is the correct syntax for adding a new line to /etc/fstab using a volume’s UUID?"
  - "What are the risks of booting a VM from an image instead of from a persistent volume?"
  - "How can you create an image from an existing volume using the OpenStack dashboard?"
  - "Which option should you configure to prevent a volume from being automatically deleted when its instance is terminated?"
  - "What precautions should be taken before cloning a volume to ensure the new volume is not left in an inconsistent state?"
  - "How do you properly detach a volume from a VM, and what special steps are required for boot volumes versus data volumes?"
  - "What steps and considerations are recommended when changing an existing volume’s type from rbd1 to high_performance?"
  - "Which OpenStack CLI command is used to create an image from a volume?"
  - "What are the two possible values for the `<format>` option in this command?"
  - "Where can you find the `<volume_name>` needed to run the command?"
  - "What considerations should be taken into account about data migration and operation time when switching a volume from **rbd1** to **high_performance**?"
  - "Which OpenStack CLI commands are required to list a volume, display its current type, and request a retype to **high_performance** with the **on‑demand** policy?"
  - "How can you monitor the progress of the retype operation and confirm that the volume’s type has successfully changed to **high_performance**?"
  - "How do you locate the specific volume you want to modify in the Volumes page?"
  - "What steps must be taken in the Change Volume Type dialog to set a volume to high_performance with an On Demand migration policy?"
  - "After initiating the change, how can you confirm that the volume’s type has been successfully updated?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

A volume provides storage which is not destroyed when a VM is terminated. On our clouds, volumes use [Ceph](https://en.wikipedia.org/wiki/Ceph_(software)) storage with either a 3-fold replication factor or [erasure codes](https://en.wikipedia.org/wiki/Erasure_code) to provide safety against hardware failure. On [Arbutus](cloud_resources.md), the *rbd1* volume type is stored on spinning disk hard drives and uses erasure codes to provide data safety while reducing the extra storage costs of 3-fold replication. The *high_performance* volume type is stored on solid state NVMe drives and uses the less storage efficient but higher performance 3-fold replication factor. More documentation about OpenStack volumes can be found [here](https://docs.openstack.org/cinder/latest/cli/cli-manage-volumes.html).

## Creating a volume

To create a volume, follow these steps and fill in the following fields:

*   *Volume Name*: `data`, for example
*   *Description*: (optional)
*   *Volume Source*: `No source, empty volume`
*   *Type*: `No volume type`
*   *Size (GiB)*: `40`, or some suitable size for your data or operating system
*   *Availability Zone*: the only option is `nova`

Finally, click on the blue **Create Volume** button at the bottom.

## Mounting a volume on a VM
### Attaching a volume
*   **Attaching** is the process of associating a volume with a VM. This is analogous to inserting a USB key or plugging an external drive into your personal computer.
*   You can attach a volume from the **Volumes** page in the dashboard.
*   At the right-hand end of the line describing the volume is the **Actions** column; from the drop-down menu, select **Manage Attachments**.
*   In the **Attach to Instance** drop-down menu, select a VM.
*   Click on the blue **Attach Volume** button.
Attaching should complete in a few seconds. Then the volumes page will show the newly created volume attached to your selected VM on `/dev/vdb` or some similar location.
### Formatting a newly created volume
*   **DO NOT FORMAT** if you are attaching an existing volume. Instead you can skip this step as the volume would have already been formatted if you had been previously using it to store data.
*   **Formatting** erases all existing information on a volume and therefore should be done with care.
*   Formatting is the process of preparing a volume to store directories and files.
*   Before a newly created and attached volume can be used, it must be formatted.
*   See instructions for doing this on a [Linux](../storage-and-data/using_a_new_empty_volume_on_a_linux_vm.md) or [Windows](../storage-and-data/using_a_new_empty_volume_on_a_windows_vm.md) VM.

### Mounting a volume
*   **Mounting** is the process of mapping the volume's directory and file structure logically within the VM's directory and file structure.
*   To mount the volume, use a command similar to `[name@server ~]$ sudo mount /dev/vdb1 /mnt` depending on the device name, disk layout, and the desired mount point in your filesystem.
This command makes the volume's directory and file structure available under the VM's `/mnt` directory. However, when the virtual machine reboots, the volume will need to be re-mounted using the same `mount` command.

It is possible to automatically mount volumes when a virtual machine boots. This requires editing the file named `/etc/fstab` to contain a new line with details about how the volume should be mounted.

To view mounting information, use the `blkid` command:
```bash
blkid
```

Based on the UUID, add a line to `/etc/fstab` like this:

```bash
/dev/disk/by-uuid/anananan-anan-anana-anan-ananananana /mnt auto defaults,nofail 0 3
```

Where 'anananan-anan-anana-anan-ananananana' is substituted with the UUID of the device you wish to auto-mount.

For details on how to edit this file, see this [Ubuntu community help page](https://help.ubuntu.com/community/Fstab).

## Booting from a volume
!!! warning "Attention"
    Booting from an image creates a fast, ephemeral volume which is local to the hypervisor. However, ephemeral volumes are not backed up. The volume will be lost if the instance is deleted, if the hypervisor's highly available disk array fails, or if the instance needs to be evacuated.
If you want to run a persistent machine, it is safest to boot from a volume. When you boot a VM from an image rather than a volume, the VM is stored on the local disk of the actual machine running the VM. If something goes wrong with that machine or its disk, the VM may be lost. Volume storage has redundancy, which protects the VM from hardware failure. Typically when booting from a volume VM flavours starting with the letter p are used (see [Virtual machine flavours](virtual_machine_flavors.md)).

For details on storage options, see this [Cloud storage options](cloud_storage_options.md).
There are several ways to boot a VM from a volume. You can
*   boot from an image, creating a new volume, or
*   boot from a pre-existing volume, or
*   boot from a volume snapshot, creating a new volume.

If you have not done this before, then the first one is your only option. The other two are only possible if you have already created a bootable volume or a volume snapshot.

If creating a volume as part of the process of launching the VM, select *Boot from image (creates a new volume)*, select the image to use, and the size of the volume. If this volume is something you would like to remain longer than the VM, ensure that the **Delete on Terminate** box is not checked. If you are unsure about this option, it is better to leave this box unchecked. You can manually delete the volume later.

## Creating an image from a volume
Creating an image from a volume allows you to download the image. Do this if you want to save it as a backup, or to spin up a VM on a different cloud, e.g., with [VirtualBox](https://www.virtualbox.org/). If you want to copy a volume to a new volume within the same cloud see [cloning a volume](#cloning-a-volume) instead.

To create an image of a volume, it must first be detached from a VM. If it is a boot (root) volume, it can only be detached from a VM if the VM is terminated/deleted; however, make sure you have not checked **Delete Volume on Instance Delete** when creating the VM.

Large images (more than 10-20GB) may be very slow to create, upload, and otherwise manage. You may want to consider [separating data](backing_up_your_vm.md#an-example-backup-strategy) if possible.

### Using the dashboard
1.  Click on the **Volumes** left-hand menu.
2.  Under the volume you wish to create an image of, click on the drop-down **Actions** menu and select **Upload to Image**.
3.  Choose a name for your new image.
4.  Choose a disk format. QCOW2 is recommended for using within the OpenStack cloud as it is relatively compact compared to *Raw* and works well with OpenStack. If you wish to use the image with VirtualBox, the *vmdk* or *vdi* image formats might be better suited.
5.  Finally, click on **Upload**.

### Using the command line client
The [command line client](openstack_command_line_clients.md) can do this:
```bash
openstack image create --disk-format <format> --volume <volume_name> <image_name>
```
where
*   `<format>` is the disk format (two possible values are [qcow2](https://en.wikipedia.org/wiki/Qcow) and [vmdk](https://en.wikipedia.org/wiki/VMDK)),
*   `<volume_name>` can be found from the OpenStack dashboard by clicking on the volume name, and
*   `<image_name>` is a name you choose for the image.
You can then [download the image](working_with_images.md#downloading-an-image).

## Cloning a volume
Cloning is the recommended method for copying volumes. While it is possible to make an image of an existing volume and use it to create a new volume, cloning is much faster and requires less movement of data behind the scenes. This method is handy if you have a persistent VM and you want to test out something before doing it on your production site. It is highly recommended to shut down your VM before creating a clone of the volume as the newly created volume may be left in an inconsistent state if there was writing to the source volume during the time the clone was created. To create a clone you must use the [command line client](openstack_command_line_clients.md) with this command
```bash
openstack volume create --source <source-volume-id> --size <size-of-new-volume> <name-of-new-volume>
```

## Detaching a volume
Before detaching a volume, it is important to make sure that the operating system and other programs running on your VM are not accessing files on this volume. If so, the detached volume can be left in a corrupted state or the programs could show unexpected behaviours. To avoid this, you can either shut down the VM before you detach the volume or [unmount the volume](../storage-and-data/using_a_new_empty_volume_on_a_linux_vm.md#unmounting-a-volume-or-device).

To detach a volume, log in to the OpenStack dashboard (see the [list of links to our cloud systems](cloud.md#cloud-systems)) and select the project containing the volume you wish to detach. Selecting *Volumes -> Volumes* displays the project’s volumes. For each volume, the **Attached to** column indicates where the volume is attached.

*   If attached to `/dev/vda`, it is a boot volume; you must delete the attached VM before the volume can be detached otherwise you will get the error message **Unable to detach volume**.

*   With volumes attached to `/dev/vdb`, `/dev/vdc`, etc. you do not need to delete the VM it is attached to before proceeding. In the **Actions** column drop-down list, select **Manage Attachments**, click on the **Detach Volume** button and again on the next **Detach Volume** button to confirm.

## Changing the Volume Type of an Existing Volume

OpenStack clouds (like Arbutus) can provide multiple volume types with different storage performance characteristics.
The two primary volume types available on Arbutus are:

| Volume type | Storage | Recommended use |
| :--------------- | :------------------------------ | :---------------------------------------------------------------------------------------------------------- |
| rbd1 | Hard disk drive (HDD) based storage | General-purpose storage and workloads where high storage performance is not required or large size is desired |
| high_performance | NVMe-based storage | Operating Systems, Databases and other I/O-intensive or latency-sensitive workloads. Note: Quota is very limited on this volume type. |

Before changing a volume type
We recommend that you:
1.  Back up important data. As with any storage operation, ensure that important data is backed up before making changes.
2.  Check available quota. The destination storage tier may have different quota or availability constraints.
3.  Plan for the operation to take some time. Changing the backing storage of a large volume may require data to be migrated between storage systems.
4.  Avoid unnecessary disk activity during migration. For important or write-intensive applications, consider scheduling the change during a maintenance period.

Existing volumes can be changed from rbd1 to high_performance without creating a new volume. This can be done in both the Web Interface or CLI:

### Changing an existing volume using the Dashboard

Before starting, we recommend backing up any important data on the volume. This example will explain the process of migrating a volume from rbd1 to high_performance volume type.

1.  Log in to the OpenStack Horizon dashboard.
2.  Select the appropriate project.
3.  From the navigation menu, select Project → Volumes -> Volumes.
4.  Locate the volume you want to change.
5.  In the Actions column, open the drop-down menu for the volume and select **Change Volume Type**.
6.  In the **Change Volume Type** dialog:
    *   For Type, select **high_performance**.
    *   For Migration Policy, select **On Demand**.
7.  Click **Change Volume Type** to begin the operation.
8.  Return to the Volumes page and monitor the volume's status. While the operation is underway, the volume may show a status of *Retyping*.
9.  When the operation is complete, verify that the volume's Type is now **high_performance**.

!!! note "Important"
    Changing between rbd1 and high_performance may require the volume's data to be migrated between different storage backends. The operation can therefore take some time, particularly for larger volumes. Do not assume that a volume-type change is instantaneous.

### Changing an existing volume using the CLI

Using the OpenStack command-line client, first identify the volume:
```bash
openstack volume list
```

Check its current volume type:
```bash
openstack volume show <volume>
```

Then request that the volume be changed to the high_performance type:
```bash
openstack volume set --type high_performance --retype-policy on-demand <volume>
```

You can monitor the volume while the change is taking place:
```bash
openstack volume show <volume>
```

Once the operation has completed, verify that the volume type is reported as high_performance.