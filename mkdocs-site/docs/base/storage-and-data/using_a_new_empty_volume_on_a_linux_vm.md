---
title: "Using a new empty volume on a Linux VM"
slug: "using_a_new_empty_volume_on_a_linux_vm"
lang: "base"

source_wiki_title: "Using a new empty volume on a Linux VM"
source_hash: "ac919881af3d92f454df80ab65061275"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T12:19:41.674807+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

!!! note
    On most Linux distributions, the following steps can be used to partition, format, and mount the newly created volume. If this is not a newly created volume, the partition and format steps should be skipped as they will result in loss of data on that volume, and only the steps to mount the volume should be followed.

1.  Create a partition on the volume with:
    ```bash
    sudo fdisk /dev/vdb
    ```
    `fdisk` will prompt you to enter a command. Use this sequence of single-character commands to create a new partition on your volume:
    *   `n` => new partition
    *   `p` => primary, only one partition on disk
    *   `1` => partition number 1
    *   `<return>` => first sector (use default)
    *   `<return>` => last sector (use default)
    *   `w` => write partition table to disk and exit
2.  Format the newly created partition with:
    ```bash
    sudo mkfs -t ext4 /dev/vdb1
    ```
3.  Create a place to mount the device with:
    ```bash
    sudo mkdir /media/data
    ```
4.  Finally, mount the volume with:
    ```bash
    sudo mount /dev/vdb1 /media/data
    ```

If the VM is rebooted for some reason, the volume will need to be remounted. To cause the VM to mount the volume automatically at boot time, edit `/etc/fstab` and add a line like:

```
/dev/vdb1 /media/data ext4 defaults 0 2
```

For more details about the fstab file, see this [wikipedia article](https://en.wikipedia.org/wiki/Fstab). If you are not rebooting, you can mount the device just added to `/etc/fstab` with:
```bash
sudo mount -a
```

## Unmounting a Volume or Device

!!! warning
    If you need to remove a volume or other device for some reason (for example, to create an image from it, or to attach it to a different VM), it is best to unmount it first. Unmounting a volume before detaching it helps prevent data corruption.

To unmount our previously mounted volume, use the following command:
```bash
sudo umount /media/data
```
This command will work if no files are being accessed by the operating system or any other program running on the VM. This can be both reading and writing to files. If this is the case, when you try to unmount a volume, you will get a message letting you know that the volume is still busy and it will not be unmounted.