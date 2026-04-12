---
title: "Using a new empty volume on a Linux VM"
slug: "using_a_new_empty_volume_on_a_linux_vm"
lang: "base"

source_wiki_title: "Using a new empty volume on a Linux VM"
source_hash: "ac919881af3d92f454df80ab65061275"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:20:20.389881+00:00"

tags:
  []

keywords:
  - "Linux volume"
  - "unmount"
  - "partition"
  - "format"
  - "mount"

questions:
  - "What are the necessary steps and commands to partition, format, and mount a newly created volume in Linux?"
  - "How can you configure a Linux virtual machine to automatically mount a volume at boot time?"
  - "Why should you unmount a volume before detaching it, and what condition will cause the unmount command to fail?"
  - "What are the necessary steps and commands to partition, format, and mount a newly created volume in Linux?"
  - "How can you configure a Linux virtual machine to automatically mount a volume at boot time?"
  - "Why should you unmount a volume before detaching it, and what condition will cause the unmount command to fail?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! warning "Data Loss Advisory"
If this is not a newly created volume, the partition and format steps should be skipped as they will result in the loss of all existing data on that volume. Only the steps to mount the volume should be followed in such cases.

1.  Create a partition on the volume:
    ```bash
    sudo fdisk /dev/vdb
    ```
    `fdisk` will prompt you to enter a command. Use the following sequence of single-character commands to create a new partition on your volume:
    *   `n`: Create a new partition
    *   `p`: Specify it as a primary partition (there will only be one partition on this disk)
    *   `1`: Assign partition number 1
    *   `<return>`: Accept the default for the first sector
    *   `<return>`: Accept the default for the last sector
    *   `w`: Write the partition table to disk and exit

2.  Format the newly created partition:
    ```bash
    sudo mkfs -t ext4 /dev/vdb1
    ```

3.  Create a mount point for the device:
    ```bash
    sudo mkdir /media/data
    ```

4.  Finally, mount the volume:
    ```bash
    sudo mount /dev/vdb1 /media/data
    ```

If the VM is rebooted for some reason, the volume will need to be remounted. To configure the VM to mount the volume automatically at boot time, edit `/etc/fstab` and add a line like this:

```
/dev/vdb1 /media/data ext4 defaults 0 2
```

For more details about the `fstab` file, refer to this [Wikipedia article](https://en.wikipedia.org/wiki/Fstab). If you are not rebooting, you can mount the device just added to `/etc/fstab` immediately with:

```bash
sudo mount -a
```

## Unmounting a Volume or Device

If you need to remove a volume or other device for some reason, for example, to create an image from it, or to attach it to a different VM, it is best to unmount it first. Unmounting a volume before detaching it helps prevent data corruption.

To unmount our previously mounted volume, use the following command:

```bash
sudo umount /media/data
```

This command will work if no files are being accessed by the operating system or any other program running on the VM. This can include both reading and writing to files. If this is the case, when you try to unmount a volume, you will receive a message indicating that the volume is still busy, and it will not be unmounted.