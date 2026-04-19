---
title: "Using nearline storage/en"
slug: "using_nearline_storage"
lang: "en"

source_wiki_title: "Using nearline storage/en"
source_hash: "6c5b216d75d2c56e9b7b6c8db1c7df34"
last_synced: "2026-04-18T23:39:30.217451+00:00"
last_processed: "2026-04-19T01:14:44.879517+00:00"

tags:
  []

keywords:
  - "inactive data"
  - "Nearline"
  - "virtualized files"
  - "Data storage"
  - "data retrieval"
  - "transferring data"
  - "tape storage"
  - "Béluga"
  - "Slurm scheduler"
  - "HPSS"
  - "file transfers"
  - "Globus"
  - "tapes"
  - "archive files"
  - "tape-based filesystem"
  - "nearline service"
  - "VFS node"
  - "cost per unit"
  - "disk copy"
  - "tape copy"
  - "/nearline"
  - "hierarchical storage manager"
  - "nearline"

questions:
  - "What types of data are best suited for the /nearline filesystem, and what are the main advantages of using it over disk or SSD storage?"
  - "What are the specific file size guidelines and archiving best practices users must follow when preparing and storing files in /nearline?"
  - "What restrictions and recommended methods apply to accessing, transferring, and processing data within the /nearline environment?"
  - "How does the hierarchical storage system manage the lifecycle of a file moving between disk and tape?"
  - "What happens to the transfer time and system process when a user attempts to read a file that has been completely virtualized to tape?"
  - "Which commands can users utilize to check the current storage state or force the restoration of their files on the /nearline system?"
  - "What are the primary cost, scalability, and energy benefits of using the /nearline storage media?"
  - "How does moving inactive data to /nearline improve the performance and capacity of the /project storage?"
  - "What is the initial technical state of a file when it is first created on or copied to the /nearline system?"
  - "What are the specific data retention and tape copy timeframes for the /nearline service on the Nibi system?"
  - "Which underlying technology does the Trillium system use for its /nearline service?"
  - "From which directory should users operate to maintain a record of the locations of all their files?"
  - "How can users automate their file transfers to the HPSS service using the Slurm scheduler?"
  - "What is the recommended approach and command for managing a small number of files in HPSS?"
  - "Which tool and endpoint should be used for occasional transfers between HPSS and other external sites?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Nearline is a tape-based filesystem intended for **inactive data**. Datasets which you do not expect to access for months are good candidates to be stored in /nearline.

## Restrictions and best practices

### Size of files

Retrieving small files from tape is inefficient, while extremely large files pose other problems. Please observe these guidelines when storing files in /nearline:

*   Files smaller than ~10GB should be combined into archive files (*tarballs*) using [tar](a_tutorial_on__tar.md) or a [similar tool](archiving_and_compressing_files.md).
*   Files larger than 4TB should be split into chunks of 1TB using the [split command](a_tutorial_on__tar.md#splitting-files) or a similar tool.
*   **DO NOT SEND SMALL FILES TO NEARLINE, except for indexes (see *Create an index* below).**

### Use tar or dar

Use [tar](a_tutorial_on__tar.md) or [dar](dar.md) to create an archive file.

Keep the source files in their original filesystem. Do NOT copy the source files to /nearline before creating the archive.

Create the archive directly in /nearline. This does not require additional storage space and is more efficient than creating the archive in /scratch or /project and copying it to /nearline later.

If you have hundreds of gigabytes of data, the `tar` options `-M (--multi-volume)` and `-L (--tape-length)` can be used to produce archive files of suitable size. If you are using `dar`, you can similarly use the `-s (--slice)` option.

#### Create an index
When you bundle files, it becomes inconvenient to find individual files. To avoid having to restore an entire large collection from tape when you only need one or a few of the files from this collection, you should make an index of all archive files you create. Create the index as soon as you create the collection. For instance, you can save the output of tar with the `verbose` option when you create the archive, like this:

```bash
tar cvvf /nearline/def-sponsor/user/mycollection.tar /project/def-sponsor/user/something > /nearline/def-sponsor/user/mycollection.index
```

If you've just created the archive (again using tar as an example), you can create an index like this:

```bash
tar tvvf /nearline/def-sponsor/user/mycollection.tar > /nearline/def-sponsor/user/mycollection.index
```

Index files are an exception to the rule about small files on /nearline: it's okay to store them in /nearline.

### No access from compute nodes

Because data retrieval from /nearline may take an uncertain amount of time (see *How it works* below), we do not permit reading from /nearline in a job context. /nearline is not mounted on compute nodes.

### Use a data-transfer node if available

Creating a tar or dar file for a large volume of data can be resource-intensive. Please do this on a data-transfer node (DTN) on clusters that have them. On clusters that have no DTN nodes, use a login node.

### Use a terminal multiplexer

Archiving large file collections can take several hours or even days. Your SSH session might be interrupted before your program finishes, or you might want to close your session, keep your program running in the background, and come back to it later. Run `tar` or `dar` in [a terminal multiplexer](../running-jobs/prolonging_terminal_sessions.md#terminal-multiplexers) such as `tmux` to manage these issues.

### Use `dar` in non-interactive mode

When used in a terminal, `dar` runs in interactive mode and asks to confirm certain operations. When used without an attached terminal, `dar` runs in non-interactive mode and assumes a “no” answer to any questions. We recommend to explicitly disable interactivity with `dar -Q`. This is especially useful when running `dar` in an unattended terminal multiplexer. See [Dar](dar.md) for additional information.

## Why /nearline?

Tape as a storage medium has these advantages over disk and solid-state (SSD) media.
1.  Cost per unit of data stored is lower.
2.  The volume of data stored can be easily expanded by buying more tapes.
3.  Energy consumption per unit of data stored is effectively zero.

Consequently we can offer much greater volumes of storage on /nearline than we can on /project. Also, keeping inactive data *off* of /project reduces the load and improves its performance.

## How it works

1.  When a file is first copied to (or created on) /nearline, the file exists only on disk, not tape.
2.  After a period (on the order of a day), and if the file meets certain criteria, the system will copy the file to tape. At this stage, the file will be on both disk and tape.
3.  After a further period the disk copy may be deleted, and the file will only be on tape.
4.  When such a file is recalled, it is copied from tape back to disk, returning it to the second state.

When a file has been moved entirely to tape (that is, when it is *virtualized*) it will still appear in the directory listing. If the virtual file is read, it will take some time for the tape to be retrieved from the library and copied back to disk. The process which is trying to read the file will block while this is happening. This may take from less than a minute to over an hour, depending on the size of the file and the demand on the tape system.

### Transferring data from /nearline

While [transferring data](../getting-started/transferring_data.md) with [Globus](../getting-started/globus.md) or any other tool, the data that was on tape gets automatically restored on disk upon reading it. Since tape access is relatively slow, each file restoration can hang the transfer for a few minutes to a few hours. Therefore, users should expect longer transfer times from /nearline.

For an overview of the state of all files saved on /nearline, **some clusters** support the following command:
```bash
diskusage_report --nearline --per_user --all_users
```

The different `Location`s are:
*   `On disk and tape`: this data is available on disk.
*   `Modified, will be archived again`: the newest version of the data is on disk.
*   `Archiving in progress`: the data is being copied or moved to tape.
*   `On tape`: the data is only on tape.

Then, you can determine whether or not a given file has been moved to tape or is still on disk using the `lfs hsm_state` command. "hsm" stands for "hierarchical storage manager".

```bash
# Here, <FILE> is only on disk.
$ lfs hsm_state <FILE>
<FILE>:  (0x00000000)

# Here, <FILE> is in progress of being copied to tape.
$ lfs hsm_state <FILE>
<FILE>: [...]: exists, [...]

# Here, <FILE> is both on the disk and on tape.
$ lfs hsm_state <FILE>
<FILE>: [...]: exists archived, [...]

# Here, <FILE> is on tape but no longer on disk.  There will be a lag when opening it.
$ lfs hsm_state <FILE>
<FILE>: [...]: released exists archived, [...]
```

You can explicitly force a file to be recalled from tape without actually reading it with the command `lfs hsm_restore <FILE>`.

### Cluster-specific information

<div class="tabbed-set" data-tabs="true">
<div class="tab-item" data-id="beluga">
  Béluga
</div>
<div class="tab-item" data-id="nibi">
  Nibi
</div>
<div class="tab-item" data-id="narval">
  Narval
</div>
<div class="tab-item" data-id="trillium">
  Trillium
</div>
</div>

<div class="tabbed-content">
<div class="tab-item" data-id="beluga">

/nearline is only accessible as a directory on login nodes and on DTNs (*Data Transfer Nodes*).

To use /nearline, just put files into your `~/nearline/PROJECT` directory. After a period of time (24 hours as of February 2019), they will be copied onto tape. If the file remains unchanged for another period (24 hours as of February 2019), the copy on disk will be removed, making the file virtualized on tape.

If you accidentally (or deliberately) delete a file from `~/nearline`, the tape copy will be retained for up to 60 days. To restore such a file contact [technical support](../support/technical_support.md) with the full path for the file(s) and desired version (by date), just as you would for restoring a [backup](storage_and_file_management.md#filesystem-quotas-and-policies). Note that since you will need the full path for the file, it is important for you to retain a copy of the complete directory structure of your /nearline space. For example, you can run the command `ls -R > ~/nearline_contents.txt` from the `~/nearline/PROJECT` directory so that you have a copy of the location of all the files.

</div>
<div class="tab-item" data-id="nibi">

/nearline service similar to that on Béluga, except:
1.  It may take longer than 24 hours for the first tape copy of the data to be created.
2.  The disk copy will not be erased (leaving only the tape copies) until 60 days have passed.

</div>
<div class="tab-item" data-id="narval">

/nearline service similar to that on Béluga.

</div>
<div class="tab-item" data-id="trillium">

HPSS is the /nearline service on Trillium.
There are three methods to access the service:

1.  By submitting HPSS-specific commands `htar` or `hsi` to the Slurm scheduler as a job in one of the archive partitions; see [the HPSS documentation](https://docs.scinet.utoronto.ca/index.php/HPSS) for detailed examples. Using job scripts offers the benefit of automating /nearline transfers and is the best method if you use HPSS regularly. Your HPSS files can be found in the $ARCHIVE directory, which is like $PROJECT but with *`/project`* replaced by *`/archive`*.

2.  To manage a small number of files in HPSS, you can use the VFS (*Virtual File System*) node, which is accessed with the command `salloc --time=1:00:00 -pvfsshort`. Your HPSS files can be found in the $ARCHIVE directory, which is like $PROJECT but with *`/project`* replaced by *`/archive`*.

3.  By using [Globus](../getting-started/globus.md) for transfers to and from HPSS using the endpoint **alliancecan#hpss**. This is useful for occasional usage and for transfers to and from other sites.

</div>
</div>