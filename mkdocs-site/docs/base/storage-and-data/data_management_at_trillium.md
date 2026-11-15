---
title: "Data management at Trillium"
slug: "data_management_at_trillium"
lang: "base"

source_wiki_title: "Data management at Trillium"
source_hash: "3a15955486fb43a9c5a49e6a0079d67c"
last_synced: "2026-11-15T02:27:25.182546+00:00"
last_processed: "2026-11-15T03:26:51.620609+00:00"

tags:
  []

keywords:
  - "POSIX ACLs"
  - "ACL"
  - "Trillium file systems"
  - "Slurm job cleanup"
  - "recursive"
  - "setfacl"
  - "VAST all‑flash NVMe"
  - "60 days grace period"
  - "MPI-IO"
  - "datamover nodes"
  - "file I/O bottleneck"
  - "getfacl"
  - "version retention"
  - "Globus"
  - "backup system"
  - "default ACL"
  - "read/write/execute permission"
  - "rsync/scp"
  - "quota limits"
  - "$SLURM_TMPDIR"
  - "file ownership"
  - "daily backup schedule"
  - "snapshots"
  - "diskusage_report"
  - "/scratch"
  - "parallel file systems"
  - "version-based backups"
  - "node-local storage"
  - "RAM disk"
  - "10 years retention"
  - "/project"

questions:
  - "What are the intended purposes, backup policies, and usage restrictions for each Trillium file system (/home, /scratch, /project, /archive, and /dev/shm)?"
  - "How does the VAST parallel file system impact performance, particularly with many small files, and what I/O practices (e.g., MPI‑IO, dedicated I/O processes) are recommended to maintain scalability?"
  - "What guidelines should users follow regarding data placement, naming conventions, and quota management to avoid misuse of /project and ensure efficient long‑term storage?"
  - "Why does heavy file I/O become a bottleneck when migrating desktop‑computing codes to an HPC platform with parallel file systems?"
  - "What is the recommended temporary directory for job‑specific files, and how does Slurm handle its cleanup?"
  - "What must you do with files created directly in /dev/shm after your job finishes?"
  - "What is the purpose of the $SLURM_TMPDIR environment variable on Trillium compute nodes, and how does its location differ from that on the general‑purpose clusters?"
  - "How are storage quotas allocated across the $HOME, $SCRATCH, $PROJECT, and $ARCHIVE file systems, and what factors affect the size of a group's scratch quota?"
  - "What are the key characteristics of Trillium’s backup policy, including version retention, deletion handling, and the time frames for keeping file versions?"
  - "How can you recover an accidentally deleted file using the VAST file system snapshots?"
  - "What are the recommended methods and size limits for transferring data to and from Trillium, including the use of login nodes, datamover nodes, and Globus?"
  - "How can you manage file ownership and grant access to other users or groups on SciNet using POSIX ACLs?"
  - "How long is the most recent version of a file kept in the backup after the grace period?"
  - "Under what conditions can a file retain one or two backup versions for more than 10 years?"
  - "Why might a file created in the morning and deleted in the afternoon not be captured by the backup system?"
  - "How can you grant the user SUPERVISOR read, write, and execute permissions on a directory with setfacl?"
  - "Which command displays the current ACL settings of a file or directory?"
  - "What does the -d option do when setting an ACL, and to which objects does a default ACL apply?"
  - "What command(s) does VAST provide for managing POSIX ACLs, such as granting a supervisor read, write, and execute permissions on a directory?"
  - "How can the original owner retain full access to files or directories while allowing other users or groups read/execute rights using VAST’s ACL mechanism?"
  - "In what ways does using setfacl/getfacl differ from other permission‑granting methods mentioned in the text?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Understanding the various file systems, and how to use them properly, is critical to optimizing your workflow and being a good citizen of the shared system. This page describes the various Trillium file systems and how to use them properly.

## Performance
With the exception of /archive, the Trillium file systems use [VAST](https://www.vastdata.com/), an all-flash NVMe parallel file system. It provides high throughput for large datasets read or written in parallel from many nodes, and it is designed to handle metadata-heavy workloads as well.

!!! tip "Small Files Inefficiency"
    Even so, very large numbers of small files are inefficient to manage: they consume inodes, stress the backup and archive systems, and are slower to transfer than a few large files. This is something you should keep in mind when planning your input/output strategy for runs on Trillium.

!!! tip "Scalable I/O Practices"
    For instance, if you run multi-process jobs, having each process write to its own file is not a scalable I/O solution. The directory is locked by the first process that accesses it, so the other processes must wait. The code becomes considerably less parallel, and the file system may time out while waiting, causing your program to fail mysteriously. Consider using MPI-IO (part of the MPI-2 standard), which allows files to be opened simultaneously by different processes, or using a dedicated process for I/O to which all other processes send their data, and which subsequently writes this data to a single file.

## Purpose of each file system
Trillium accesses several different file systems. Note that not all of these file systems are available to all users.

### /home ($HOME)
/home is intended for individual user files, and for common software or small datasets shared within a group, provided the quota is respected. Otherwise you may consider /scratch or /project. /home is read-only on the compute nodes and has daily backups.

### /scratch ($SCRATCH)
/scratch is intended for temporary or transient files, checkpoint dumps, the results of your computations and simulations, or any material that can be easily recreated or reacquired. You may use scratch as well for any intermediate step in your workflow, provided it does not create too much I/O (input/output) or too many small files on this storage pool. Once you have your final results, those that you want to keep for the long term, you may migrate them to /project or /archive. /scratch has no backups. There is currently no automatic purging policy on Trillium, but scratch is not a long-term storage location.

### /project ($PROJECT)
/project is available to groups whose PIs hold a RAC storage allocation, and is intended for common group software, large static datasets, or any material very costly to be reacquired or re-generated by the group, associated with jobs currently running on Trillium.

!!! warning "Immutable Data Expected on /project"
    Material on /project is expected to remain relatively immutable over time. **You should think of $PROJECT as if it were $STATIC.** Temporary or transient files should be kept on scratch, not project. High data turnover stresses the backup system and consumes tapes long after the material has been deleted, because of backup retention policies and the extra versions kept of the same file. Even renaming top-level directories makes the system assume that a completely new directory tree has been created and the old one deleted, so think carefully about your naming convention in advance and stick with it.

!!! warning "Misuse of /project"
    Users abusing the project file system and using it as scratch will be flagged and contacted.

### /archive ($ARCHIVE)
/archive is available to groups whose PIs hold a RAC storage allocation, and is the **nearline** storage pool. It is used to offload semi-active material temporarily from any of the above file systems. In practice, users offload and recall material as part of their regular workflow, or when they reach their quotas on scratch or project. That material can remain on HPSS for a few months to a few years. /archive is not mounted on the login, compute, or datamover nodes.

### /dev/shm (RAM)
On the Trillium nodes a RAM disk is available. It is much faster than real disk: up to 566 GiB of the node's memory (about 75% of usable RAM), less whatever your application uses, may be used as a temporary **local** file system.

!!! tip "Node-Local Storage for I/O Bottlenecks"
    This is particularly useful in the early stages of migrating desktop-computing codes to an an HPC platform, especially those that use a lot of file I/O (input/output). Using a lot of I/O is a bottleneck in large scale computing, especially on parallel file systems, since the files are synchronized across the whole network.

!!! warning "Ephemeral Nature of /dev/shm"
    Files you create directly in `/dev/shm` are not removed when your job ends; delete them yourself. Prefer `$SLURM_TMPDIR`, whose contents Slurm deletes at job end. See [Using node-local storage](using_node-local_storage.md) for how to stage data in and out.

### $SLURM_TMPDIR (RAM)
For consistency with the general-purpose Alliance clusters (Nibi, Fir, Rorqual, and Narval), the environment variable `$SLURM_TMPDIR` will be set on Trillium compute jobs. Note that this variable will point to the RAM disk, not to local hard drives. The `$SLURM_TMPDIR` directory is empty when your job starts, and its contents are deleted when the job finishes.

Trillium compute nodes have no local disks, so `$SLURM_TMPDIR` lives in memory (RAM disk), in contrast to the general-purpose systems (Fir, Nibi, Rorqual, and Narval), where this variable points to a directory on a node-local SSD.

## Quotas
You should understand what each file system is for and how to use it properly. The table below summarizes them.

| location | quota (space) | quota (description/files) | expiration time | backed up | on login nodes | on compute nodes |
| :------- | :------------ | :------------------------ | :-------------- | :-------- | :------------- | :--------------- |
| $HOME    | 100 GiB       | 1,000,000 files per user  |                 | yes       | yes            | read-only        |
| $SCRATCH | 25 TiB        | 10,000,000 files per user (provided group quota not reached) | none at present | no        | yes            | yes              |
|          |               | groups of up to 4 users: 50 TB for the group | none at present | no | yes | yes |
|          |               | groups of up to 11 users: 125 TB for the group | none at present | no | yes | yes |
|          |               | groups of up to 28 users: 250 TB for the group | none at present | no | yes | yes |
|          |               | groups of up to 60 users: 400 TB for the group | none at present | no | yes | yes |
|          |               | groups with over 60 users: 500 TB for the group | none at present | no | yes | yes |
| $PROJECT | by group allocation |                         |                 | yes       | yes            | read-only        |
| $ARCHIVE | by group allocation |                         |                 | dual-copy | no             | no               |

*   [Inode vs. space quota (project and scratch)](https://docs.scinet.utoronto.ca/images/9/9a/Inode_vs._Space_quota_-_v2x.pdf)
*   [Dynamic quota per group (scratch)](https://docs.scinet.utoronto.ca/images/0/0e/Scratch-quota.pdf)
*   Compute nodes do not have local storage.
*   Archive space is on HPSS, and is not accessible on the login, compute, or datamover nodes.
*   A backup is a recent snapshot, not a replica of all data or of every version that ever existed.

### How much disk space do I have left?
The `diskusage_report` command, available on the Trillium login nodes and datamovers, reports how much space and how many files you are using on the home, scratch, project, and nearline file systems. Use `--home`, `--scratch`, `--project`, or `--nearline` to restrict the report, and `--all_users` to show every member of your group's project allocation. See [Storage and file management](storage_and_file_management.md) for an example of its output.

### Scratch purging
There is currently no automatic purging policy for /scratch on Trillium. Scratch is still not a long-term storage location and has no backups: move anything you need to keep to /project or /archive. A purging policy may be introduced in the future; this page will be updated if that happens.

## Backup policy
Backups are version-based, not date-based:

*   In general, we keep the two most recent versions of a file, one per day, as long as the file exists on the file system. Once a file is deleted, we expire the oldest version from the backup and keep the most recent one for 60 days. After that grace period, the remaining version is expired as well.
*   We may have one or two versions of a file in the backup for over 10 years, provided the original has never been deleted from the file system.
*   Conversely, there may be no backup if you created the file in the morning and deleted it in the afternoon, since the backup system runs once a day around midnight and never had a chance to capture it.
*   If you generate several versions of a file during the day, only the most recent version before the backup runs is captured for that day.

### Recovering deleted files
The VAST file system keeps snapshots of your files. If you delete a file by accident, run `oops` in the directory where it lived, or pass a directory name, to see whether a recent snapshot contains a copy. Copy the file back from the snapshot path with `cp`; snapshots are read-only. Files can only be recovered while the snapshot is retained.

## Handling large collections of files
Formats that encapsulate and compact very large numbers of small files can be more performant and convenient than handling those small files directly in the file system. They also reduce stress on the backup system, since tape is not designed for many small files, and help you stay within your inode quota. See [Handling large collections of files](handling_large_collections_of_files.md) for details.

## Moving data
Data for analysis and final results must be moved to and from Trillium. There are several ways to do this.

### Using rsync/scp
**Move amounts less than 10 GB through the login nodes.**

*   Trillium login nodes and datamovers are visible from outside SciNet.
*   Use `scp` or `rsync` to `trillium.scinet.utoronto.ca` or `trillium.alliancecan.ca` (no difference).
*   Transfers larger than about 10 GB will time out.

**Move amounts greater than 10 GB through the datamover nodes.**

*   From a login node, ssh to `tri-dm{1,2,3,4}`. From there you can transfer to or from the cluster.
*   Alternatively, you may also login/scp/rsync directly to the datamovers from the outside:
    *   `tri-dm1.scinet.utoronto.ca`
    *   `tri-dm2.scinet.utoronto.ca`
    *   `tri-dm3.scinet.utoronto.ca`
    *   `tri-dm4.scinet.utoronto.ca`
*   If you do this often, consider using [Globus](../getting-started/globus.md), a web-based tool for data transfer.

You can make at most 4 connections in a 2-minute window to the login or datamover nodes, so bundle your transfers: pass several files to `scp` or `rsync`, copy whole directories, or create a tar archive, transfer it, and extract it at the other end.

To transfer smaller files between Trillium and other Digital Research Alliance of Canada clusters, use the SSH agent forwarding flag `-A` when logging in to the other cluster. For example, to copy files to Trillium from Nibi use:

```bash
ssh -A USERNAME@nibi.alliancecan.ca
```

then perform the copy:

```bash
[USERNAME@l1.nibi ~]$ scp file USERNAME@trillium.alliancecan.ca:/scratch/USERNAME/
```

### Using Globus
See the [Globus](../getting-started/globus.md) page for comprehensive documentation.

The Trillium "endpoint" for Globus is `alliancecan#trillium`; the HPSS endpoint is `alliancecan#hpss`.

### Moving data to HPSS/Archive/Nearline
HPSS is for long-term storage of data.

*   HPSS is a tape-based storage solution, and is SciNet's nearline, a.k.a. archive, facility.
*   Storage space on HPSS is allocated through the annual [Resource Allocation Competition](../running-jobs/resource_allocation_competition.md) administered by the Digital Research Alliance of Canada.

## File ownership management and access control lists
*   By default at SciNet, users in the same group have read permission on each other's files, but not write permission.
*   You can use an access control list (**ACL**) to let your supervisor (or another user within your group) manage files for you (i.e., create, move, rename, delete), while still retaining your access and permission as the original owner of the files/directories. You may also let users in other groups or whole other groups access (read, execute) your files using this same mechanism.

### Using setfacl/getfacl
VAST supports POSIX ACLs, which you can manage with the standard `setfacl` and `getfacl` commands. For example, to give a supervisor read, write, and execute permission on a directory:

```bash
setfacl -m u:SUPERVISOR:rwx /project/G/GROUP/DIR
```

To check the ACL on a file or directory:

```bash
getfacl /project/G/GROUP/DIR
```

To remove that permission:

```bash
setfacl -x u:SUPERVISOR /project/G/GROUP/DIR
```

To make new files and directories inside `DIR` inherit the same permission, add a default ACL:

```bash
setfacl -d -m u:SUPERVISOR:rwx /project/G/GROUP/DIR
```

Default ACLs apply only to directories and control the permissions of files and directories created later inside them.

NOTES:
*   To apply an ACL recursively to existing files and directories, use `setfacl -R`.
*   To give all members of your group read, write, and execute permission, you can also use the plain Unix `chmod g+rwx` command.
*   In the case of /project, your group's supervisor will need to set the proper ACL on the `/project/G/GROUP` level in order to let users from other groups access your files.
*   ACLs do not let you give away permissions to files or directories that do not belong to you.
*   We highly recommend that you never give write permission to other users on the top level of your home directory (`/home/G/GROUP/[owner]`), since that would seriously compromise your privacy, in addition to disabling SSH key authentication, among other things. If necessary, make specific subdirectories under your home directory so that other users can manipulate or access files from those.

See `man setfacl` and `man getfacl` for more information.