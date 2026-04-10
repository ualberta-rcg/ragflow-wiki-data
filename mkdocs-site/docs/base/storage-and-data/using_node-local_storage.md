---
title: "Using node-local storage"
slug: "using_node-local_storage"
lang: "base"

source_wiki_title: "Using node-local storage"
source_hash: "2163ee38c5685850647c7a53153ec7bd"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T12:27:24.063936+00:00"

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

When [Slurm](running-jobs.md) starts a job, it creates a temporary directory on each node assigned to the job. It then sets the full path name of that directory in an environment variable called `$SLURM_TMPDIR`.

Because this directory resides on local disk, input and output (I/O) to it is almost always faster than I/O to [network storage](storage-and-file-management.md) (/project, /scratch, or /home). Specifically, local disk is better for frequent small I/O transactions than network storage. Any job doing a lot of input and output (which is most jobs!) may expect to run more quickly if it uses `$SLURM_TMPDIR` instead of network storage.

!!! note
    The temporary character of `$SLURM_TMPDIR` makes it more trouble to use than network storage. Input must be copied from network storage to `$SLURM_TMPDIR` before it can be read, and output must be copied from `$SLURM_TMPDIR` back to network storage before the job ends to preserve it for later use.

## Input

In order to *read* data from `$SLURM_TMPDIR`, you must first copy the data there. In the simplest case, you can do this with `cp` or `rsync`:

```bash
cp /project/def-someone/you/input.files.* $SLURM_TMPDIR/
```

This may not work if the input is too large, or if it must be read by processes on different nodes. See [Multinode jobs](using-node-local-storage.md#multinode-jobs) and [Amount of space](using-node-local-storage.md#amount-of-space) below for more.

### Executable files and libraries

A special case of input is the application code itself. In order to run the application, the shell started by Slurm must open at least an application file, which it typically reads from network storage. But few applications these days consist of exactly one file; most also need several other files (such as libraries) in order to work.

We particularly find that using an application in a [Python](python.md) virtual environment generates a large number of small I/O transactions—more than it takes to create the virtual environment in the first place. This is why we recommend [creating virtual environments inside your jobs](python.md#creating-virtual-environments-inside-of-your-jobs) using `$SLURM_TMPDIR`.

## Output

Output data must be copied from `$SLURM_TMPDIR` back to some permanent storage before the job ends. If a job times out, then the last few lines of the job script might not be executed. This can be addressed three ways:
*   request enough runtime to let the application finish, although we understand that this isn't always possible;
*   write [checkpoints](checkpoints.md) to network storage, not to `$SLURM_TMPDIR`;
*   write a signal trapping function.

### Signal trapping

You can arrange that Slurm will send a signal to your job shortly before the runtime expires, and that when that happens your job will copy your output from `$SLURM_TMPDIR` back to network storage. This may be useful if your runtime estimate is uncertain, or if you are chaining together several Slurm jobs to complete a long calculation.

To do so you will need to write a shell function to do the copying, and use the `trap` shell command to associate the function with the signal. See [this page](https://services.criann.fr/en/services/hpc/cluster-myria/guide/signals-sent-by-slurm/) from CRIANN for an example script and detailed guidance.

!!! warning
    This method will not preserve the contents of `$SLURM_TMPDIR` in the case of a node failure, or certain malfunctions of the network file system.

## Multinode jobs

If a job spans multiple nodes and some data is needed on every node, then a simple `cp` or `tar -x` will not suffice.

### Copy files

Copy one or more files to the `$SLURM_TMPDIR` directory on every node allocated like this:

```bash
srun --ntasks=$SLURM_NNODES --ntasks-per-node=1 cp file [files...] $SLURM_TMPDIR
```

### Compressed archives

#### ZIP

Extract to the `$SLURM_TMPDIR`:

```bash
srun --ntasks=$SLURM_NNODES --ntasks-per-node=1 unzip archive.zip -d $SLURM_TMPDIR
```

#### Tarball
Extract to the `$SLURM_TMPDIR`:

```bash
srun --ntasks=$SLURM_NNODES --ntasks-per-node=1 tar -xvf archive.tar.gz -C $SLURM_TMPDIR
```

## Amount of space

At [Trillium](trillium.md), `$SLURM_TMPDIR` is implemented as *RAMdisk*, so the amount of space available is limited by the memory on the node, less the amount of RAM used by your application.

At the general-purpose clusters, the amount of space available depends on the cluster and the node to which your job is assigned.

| cluster | space in $SLURM_TMPDIR | size of disks |
| :------ | :--------------------- | :------------ |
| [Fir](fir.md) | 7T | 7.84T |
| [Narval](narval.md) | 800G | 960G, 3.84T |
| [Nibi](nibi.md) | 3T | 3T, 11T |
| [Rorqual](rorqual.md) | 375G | 480G, 3.84T |

If your job reserves [whole nodes](advanced-mpi-scheduling.md#whole-nodes), then you can reasonably assume that this much space is available to you in `$SLURM_TMPDIR` on each node. However, if the job requests less than a whole node, then other jobs may also write to the same filesystem (but a different directory!), reducing the space available to your job.

Some nodes at each site have more local disk than shown above. See *Node characteristics* at the appropriate cluster's page ([Fir](fir.md), [Narval](narval.md), [Nibi](nibi.md), [Rorqual](rorqual.md)) for guidance.