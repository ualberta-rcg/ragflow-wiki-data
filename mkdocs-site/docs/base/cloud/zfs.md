---
title: "Zfs"
slug: "zfs"
lang: "base"

source_wiki_title: "Zfs"
source_hash: "63703f9052bae195f79d019763fa0b7f"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T13:43:06.187028+00:00"

tags:
  - cloud

keywords:
  - "OpenStack"
  - "zpool"
  - "storage"
  - "ZFS"
  - "zfs create"
  - "dataset"
  - "volumes"
  - "add new device"
  - "data compression"
  - "file system"
  - "growing a zpool"
  - "logical volume manager"

questions:
  - "What is ZFS and what are its main advantages as a combined file system and logical volume manager?"
  - "How does the installation process for ZFS differ across Linux distributions like Ubuntu and CentOS?"
  - "What are the necessary steps and commands to create, configure compression for, and expand a ZFS storage pool?"
  - "What are the specific commands used to add a new device to a zpool, check the pool's status, and destroy the pool?"
  - "Why is it recommended to avoid resizing ZFS volumes within an OpenStack environment?"
  - "How does attaching multiple volumes affect IO performance, and what is the tested limit for the number of attached volumes?"
  - "What command is used to create a new dataset within an existing zpool?"
  - "How does the complexity of growing a zpool compare to expanding other file systems and logical volume managers?"
  - "What are the two specific steps required to add capacity and grow a zpool?"
  - "What are the specific commands used to add a new device to a zpool, check the pool's status, and destroy the pool?"
  - "Why is it recommended to avoid resizing ZFS volumes within an OpenStack environment?"
  - "How does attaching multiple volumes affect IO performance, and what is the tested limit for the number of attached volumes?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

ZFS is a combined [file system](https://en.wikipedia.org/wiki/File_system) and [logical volume manager](https://en.wikipedia.org/wiki/Logical_Volume_Manager_(Linux)) designed by [Sun Microsystems](https://en.wikipedia.org/wiki/Sun_Microsystems). ZFS can scale to very large file system sizes and supports compression.

ZFS greatly simplifies the process of increasing a filesystem size as required. The simplest approach is to add new volumes to your VM and then add them to your ZFS filesystem to grow the size of your file system. This can be done while the filesystem is live and file IO is occurring on the filesystem.

# Installing ZFS

### Ubuntu

Starting with the image `Ubuntu-18.04-Bionic-x64-2018-09`

Ensure your package list is up-to-date and also do upgrades of your installed packages. While it isn't strictly necessary to upgrade your installed packages, it is a good idea.

```bash
[name@server]$ sudo apt-get update
[name@server]$ sudo apt-get dist-upgrade -y
```

Next install ZFS.

```bash
[name@server]$ sudo apt-get install zfsutils-linux
```

### CentOS

Starting with the image `CentOS-7-x64-2018-09`

```bash
[name@server]$ sudo yum install http://download.zfsonlinux.org/epel/zfs-release.el7_5.noarch.rpm
...
Total size: 2.9 k
Installed size: 2.9 k
Is this ok [y/d/N]: y
...
```

hmm... this is looking strangely more complicated, see for example [https://linuxhint.com/install-zfs-centos7/](https://linuxhint.com/install-zfs-centos7/)

### Fedora

Starting with the image `Fedora-Cloud-Base-29-1.2`

to be written!

# Using ZFS

## Creating a zpool

```bash
[name@server]$ sudo zpool create -f data /dev/vdb /dev/vdc
```

This will create a new mount point at `/data` backed by the volumes attached at `/dev/vdb` and `/dev/vdc`. The filesystem will have a size slightly smaller than the combined sizes of all attached volumes. As data is written to the `/data` mount point it will be dynamically stripped across all drives. This is good for performance and allows you to make use of all your storage, however it doesn't provide any additional data replication (see [here](https://www.freebsd.org/doc/handbook/zfs-zpool.html) for information about creating mirrored zpools).

ZFS can compress data as it is written to the file system and uncompress it when it is read. To turn on and choose a compression algorithm for a zpool use the following command.

```bash
[name@server]$ sudo zfs set compression=lz4 data
```

This will use the [lz4](https://en.wikipedia.org/wiki/LZ4_(compression_algorithm)) compression algorithm on the zpool `data`. If your data is largely binary you might not see large reduction in storage use, however, if your data is something more compressible, such as ASCII data, you may see a larger reduction in storage use. Using compression can also improve file IO performance because less data needs to be read and written. However this can depend on the particular compression algorithm chosen and some particularly computationally intensive algorithms may actually reduce file IO performance. The lz4 algorithm was chosen because it is a reasonable compromise between speed and amount of compression achieved; other compression algorithms may provide better compression or speed but likely not both.

To see a list of properties for your pool use the below command.

```bash
[name@server]$ sudo zfs get all data
NAME  PROPERTY              VALUE                  SOURCE
data  type                  filesystem             -
data  creation              Fri Mar  1 17:57 2019  -
data  used                  82.5K                  -
data  available             19.3G                  -
data  referenced            24K                    -
data  compressratio         1.00x                  -
data  mounted               yes                    -
data  quota                 none                   default
...
```

zpools can be further subdivided into datasets. A dataset allows you to operate on smaller portions of your zpool independently. For example, setting a different compression algorithm for the dataset. To create a dataset within the `data` zpool do the following.

```bash
[name@server]$ sudo zfs create data/www
```

## Growing a zpool

Growing a zpool is a relatively simple task when compared to other file systems and logical volume managers. It is a two-step process: 1) add a new volume to your VM and 2) add the new device to your zpool – that's it. Below is the command to add a new device to the zpool `data`.

```bash
[name@server]$ sudo zpool add data /dev/vde
```

The zpool will now have access to the added storage contributed by the newly added device. This process usually takes less than a minute even for very large, several TB-sized zpools and volumes.

Check pool status:

```bash
[name@server]$ sudo zpool status data
```

## Destroying a zpool

```bash
[name@server]$ sudo zpool destroy data
```

# Notes

!!! warning
    While in theory it should be possible to use ZFS with resizing volumes in OpenStack, in practice this has not been straightforward and is better to be avoided if possible.

!!! note
    *   While there is no hard limit to how many volumes you can attach to your VM, it is best to keep the number of volumes attached to a reasonable number. 19 attached volumes has been tested and shown to work well with the Queens version of OpenStack.
    *   Having a pool of two or more volumes may provide improved IO performance.

# See also

*   [https://www.freebsd.org/doc/handbook/zfs.html](https://www.freebsd.org/doc/handbook/zfs.html)