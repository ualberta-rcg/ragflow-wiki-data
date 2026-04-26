---
title: "Zfs"
slug: "zfs"
lang: "base"

source_wiki_title: "Zfs"
source_hash: "be2f4533f4e47d5653d5b14fa39d4e88"
last_synced: "2026-04-25T23:42:08.699101+00:00"
last_processed: "2026-04-26T00:25:21.351161+00:00"

tags:
  - cloud

keywords:
  - "datasets"
  - "compression algorithms"
  - "growing a zpool"
  - "zpools"
  - "OpenStack"
  - "zfs create"
  - "ZFS"
  - "logical volume manager"
  - "file system"
  - "destroying a zpool"
  - "zpool list"
  - "dataset"
  - "zpool"

questions:
  - "What is ZFS and what are its main advantages for managing and scaling file systems?"
  - "How is ZFS installed on different Linux distributions such as Ubuntu and CentOS?"
  - "What are the commands and steps required to create a zpool, enable data compression, and subdivide the pool into datasets?"
  - "What are the two steps and the specific command required to grow an existing zpool?"
  - "How can a user check the status of a zpool or completely destroy it?"
  - "What are the known limitations and best practices when using ZFS volumes in an OpenStack environment?"
  - "What is the purpose of subdividing a zpool into datasets?"
  - "How do you create a new dataset within an existing zpool using the command line?"
  - "What command is used to list all existing zpools on the server?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

ZFS is a combined [file system](https://en.wikipedia.org/wiki/File_system) and [logical volume manager](https://en.wikipedia.org/wiki/Logical_Volume_Manager_(Linux)) designed by [Sun Microsystems](https://en.wikipedia.org/wiki/Sun_Microsystems). ZFS can scale to very large file system sizes and supports compression.

ZFS greatly simplifies the process of increasing a file system size as required. The simplest approach is to add new volumes to your VM and then add them to your ZFS file system to grow the size of your file system. This can be done while the file system is live and file I/O is occurring on the file system.

## Installing ZFS

### Ubuntu

Starting with the image `Ubuntu-18.04-Bionic-x64-2018-09`.

Ensure your package list is up-to-date and also do upgrades of your installed packages. While it isn't strictly necessary to upgrade your installed packages, it is a good idea.

```bash
[name@server]$ sudo apt-get update
[name@server]$ sudo apt-get dist-upgrade -y
```

Next, install ZFS.

```bash
[name@server]$ sudo apt-get install zfsutils-linux
```

### CentOS

Starting with the image `CentOS-7-x64-2018-09`.

```bash
[name@server]$ sudo yum install http://download.zfsonlinux.org/epel/zfs-release.el7_5.noarch.rpm
...
Total size: 2.9 k
Installed size: 2.9 k
Is this ok [y/d/N]: y
...
```

!!! note
    This process can be more complicated; see, for example, [this guide](https://linuxhint.com/install-zfs-centos7/).

### Fedora

Starting with the image `Fedora-Cloud-Base-29-1.2`.

!!! note "Content Incomplete"
    This section is yet to be written.

## Using ZFS

### Creating a zpool

```bash
[name@server]$ sudo zpool create -f data /dev/vdb /dev/vdc
```

This will create a new mount point at `/data` backed by the volumes attached at `/dev/vdb` and `/dev/vdc`. The file system will have a size slightly smaller than the combined sizes of all attached volumes. As data is written to the `/data` mount point, it will be dynamically stripped across all drives. This is good for performance and allows you to make use of all your storage; however, it doesn't provide any additional data replication (see [this FreeBSD handbook section](https://www.freebsd.org/doc/handbook/zfs-zpool.html) for information about creating mirrored zpools).

ZFS can compress data as it is written to the file system and uncompress it when it is read. To turn on and choose a compression algorithm for a zpool, use the following command.

```bash
[name@server]$ sudo zfs set compression=lz4 data
```

This will use the [LZ4](https://en.wikipedia.org/wiki/LZ4_(compression_algorithm)) compression algorithm on the zpool `data`. If your data is largely binary, you might not see a large reduction in storage use; however, if your data is something more compressible, such as ASCII data, you may see a larger reduction in storage use. Using compression can also improve file I/O performance because less data needs to be read and written. However, this can depend on the particular compression algorithm chosen, and some particularly computationally intensive algorithms may actually reduce file I/O performance. The LZ4 algorithm was chosen because it is a reasonable compromise between speed and amount of compression achieved; other compression algorithms may provide better compression or speed, but likely not both.

To see a list of properties for your pool, use the command below.

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

Zpools can be further subdivided into datasets. A dataset allows you to operate on smaller portions of your zpool independently. For example, you can set different compression algorithms for the dataset. To create a dataset within the `data` zpool, do the following.

```bash
[name@server]$ sudo zfs create data/www
```

### Listing zpools

The existing pools can be listed with the command `zpool list`.

```bash
[name@server]$ zpool list
NAME           SIZE  ALLOC   FREE  CKPOINT  EXPANDSZ   FRAG    CAP  DEDUP    HEALTH  ALTROOT
data            19G   156K    19G        -         -     0%     0%  1.00x    ONLINE  -
```

### Growing a zpool

Growing a zpool is a relatively simple task when compared to other file systems and logical volume managers. It is a two-step process: 1) add a new volume to your VM, and 2) add the new device to your zpool – that's it. Below is the command to add a new device to the zpool `data`.

```bash
[name@server]$ sudo zpool add data /dev/vde
```

The zpool will now have access to the added storage contributed by the newly added device. This process usually takes less than a minute even for very large, several-TB-sized zpools and volumes.

Check pool status:

```bash
[name@server]$ sudo zpool status data
```

### Destroying a zpool

```bash
[name@server]$ sudo zpool destroy data
```

## Notes

*   While in theory it should be possible to use ZFS with resizing volumes in OpenStack, in practice this has not been straightforward and is better to be avoided if possible.
*   While there is no hard limit to how many volumes you can attach to your VM, it is best to keep the number of volumes attached to a reasonable number. 19 attached volumes has been tested and shown to work well with the Queens version of OpenStack.
*   Having a pool of two or more volumes may provide improved I/O performance.

## See also

*   [FreeBSD ZFS Handbook](https://www.freebsd.org/doc/handbook/zfs.html)