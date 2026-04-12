---
title: "Advanced MPI scheduling/en"
slug: "advanced_mpi_scheduling"
lang: "en"

source_wiki_title: "Advanced MPI scheduling/en"
source_hash: "0ac91b43f66208de776738eddc2bf6b9"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T04:55:39.618771+00:00"

tags:
  - slurm

keywords:
  - "schedulers"
  - "SBATCH"
  - "resource allocation"
  - "sbatch"
  - "MPI jobs"
  - "mpirun"
  - "Slurm"
  - "Rorqual"
  - "distributed memory"
  - "hybrid jobs"
  - "ntasks-per-node"
  - "Torque/Moab"
  - "Trillium"
  - "MPI and OpenMP"
  - "srun"
  - "Open MPI"
  - "nodes"
  - "memory allocation"
  - "bash script"
  - "processes"

questions:
  - "How do you specify the number of processes and memory allocation for a basic MPI job when the exact node distribution is unknown?"
  - "What specific Slurm parameters are required in a job script to request whole nodes for large parallel jobs?"
  - "How do the CPU core counts and usable memory configurations differ across the various clusters such as Fir, Narval, and Trillium?"
  - "How does Slurm interpret the `--mem=0` command, and under what circumstances should users explicitly request a specific amount of memory instead?"
  - "What is the proper way to configure Slurm parameters, such as `--ntasks` and `--cpus-per-task`, when submitting a hybrid job that uses both MPI processes and OpenMP threads?"
  - "Why is it advantageous to use `srun` rather than `mpiexec` or `mpirun` when launching parallel applications within a modern scheduler like Slurm?"
  - "What is the primary purpose of the SLURM batch scripts provided in the text?"
  - "How do the resource allocation parameters, specifically `--ntasks-per-node=192` and `--mem=0`, configure the job execution?"
  - "Which specific computing clusters or environments are targeted by these configuration tabs?"
  - "What is the primary purpose of the `mpirun` wrapper in a computing environment?"
  - "Which specific parameters are automatically handled by schedulers like Torque or Moab so they do not need to be manually passed to `mpirun`?"
  - "How does the Slurm scheduler further simplify task execution compared to manually configuring `mpirun`?"
  - "How does srun differ from mpirun in terms of abstraction and the types of computational tasks it can distribute?"
  - "What specific actions and environment variable initializations occur within the Slurm system when a job step is started using srun?"
  - "What is the main trade-off between using mpiexec and srun regarding potential performance benefits and the risk of resource allocation mismatches?"
  - "How does srun differ from mpirun in terms of abstraction and the types of computational tasks it can distribute?"
  - "What specific actions and environment variable initializations occur within the Slurm system when a job step is started using srun?"
  - "What is the main trade-off between using mpiexec and srun regarding potential performance benefits and the risk of resource allocation mismatches?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Most users should submit MPI or distributed memory parallel jobs following the example given at [Running jobs](running_jobs.md#mpi-job). Simply request a number of processes with `--ntasks` or `-n` and trust the scheduler to allocate those processes in a way that balances the efficiency of your job with the overall efficiency of the cluster.

If you want more control over how your job is allocated, then SchedMD's page on [multicore support](https://slurm.schedmd.com/mc_support.html) is a good place to begin. It describes how many of the options to the [`sbatch`](https://slurm.schedmd.com/sbatch.html) command interact to constrain the placement of processes.

You may find this discussion on [What exactly is considered a CPU?](https://slurm.schedmd.com/faq.html#cpu_count) in Slurm to be useful.

## Examples of common MPI scenarios

### Few cores, any number of nodes

In addition to the time limit needed for *any* Slurm job, an MPI job requires that you specify how many MPI processes Slurm should start. The simplest way to do this is with `--ntasks`. Since the default memory allocation of 256MB per core is often insufficient, you may also wish to specify how much memory is needed. Using `--ntasks` you cannot know in advance how many cores will reside on each node, so you should request memory with `--mem-per-cpu`. For example:

```bash linenums="1" title="basic_mpi_job.sh"
#!/bin/bash
#SBATCH --ntasks=15
#SBATCH --mem-per-cpu=3G
srun application.exe
```
This will run 15 MPI processes. The cores could be allocated on one node, on 15 nodes, or on any number in between.

### Whole nodes

If you have a large parallel job to run, that is, one that can efficiently use 64 cores or more, you should probably request whole nodes. To do so, it helps to know what node types are available at the cluster you are using.

Typical nodes in [Fir](../software/fir.md), [Narval](../clusters/narval.md), [Nibi](../clusters/nibi.md), [Rorqual](../clusters/rorqual.md) and [Trillium](../clusters/trillium.md) have the following CPU and memory configuration:

| Cluster | Cores | Usable Memory | Notes |
| :------ | :---- | :------------ | :---- |
| [Fir](../software/fir.md) | 192 | 750 GiB | Some are reserved for whole node jobs. |
| [Narval](../clusters/narval.md) | 64 | 249 GiB | Some are reserved for whole node jobs. |
| [Nibi](../clusters/nibi.md) | 192 | 748 GiB | No node specifically reserved for whole node jobs. |
| [Rorqual](../clusters/rorqual.md) | 192 | 750 GiB | Some are reserved for whole node jobs. |
| [Trillium](../clusters/trillium.md) | 192 | 749 GiB | Only whole-node jobs are possible at Trillium. |

Whole-node jobs are allowed to run on any node. In the table above, *Some are reserved for whole-node jobs* indicates that there are nodes on which by-core jobs are forbidden.

A job script requesting whole nodes should look like this:

=== "Fir"
    ```bash linenums="1" title="whole_nodes_fir.sh"
    #!/bin/bash
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=192
    #SBATCH --mem=0
    srun application.exe
    ```
=== "Narval"
    ```bash linenums="1" title="whole_nodes_narval.sh"
    #!/bin/bash
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=64
    #SBATCH --mem=0
    srun application.exe
    ```
=== "Nibi"
    ```bash linenums="1" title="whole_nodes_nibi.sh"
    #!/bin/bash
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=192
    #SBATCH --mem=0
    srun application.exe
    ```
=== "Rorqual"
    ```bash linenums="1" title="whole_nodes_rorqual.sh"
    #!/bin/bash
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=192
    #SBATCH --mem=0
    srun application.exe
    ```
=== "Trillium"
    ```bash linenums="1" title="whole_nodes_trillium.sh"
    #!/bin/bash
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=192
    #SBATCH --mem=0
    srun application.exe
    ```

Requesting `--mem=0` is interpreted by Slurm to mean *reserve all the available memory on each node assigned to the job.*

If you need more memory per node than the smallest node provides (e.g. more than 748 GiB at Nibi) then you **should not** use `--mem=0`, but request the amount explicitly. Furthermore, some memory on each node is reserved for the operating system. To find the largest amount your job can request and still qualify for a given node type, see the *Available memory* column of the *Node characteristics* table for each cluster.
*   [Fir node characteristics](../software/fir.md#node-characteristics)
*   [Narval node characteristics](../clusters/narval.md#node-characteristics)
*   [Nibi node characteristics](../clusters/nibi.md#node-characteristics)
*   [Rorqual node characteristics](../clusters/rorqual.md#node-characteristics)

### Few cores, single node

If you need less than a full node but need all the cores to be on the same node, then you can request, for example,
```bash linenums="1" title="less_than_whole_node.sh"
#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=15
#SBATCH --mem=45G
srun application.exe
```
In this case, you could also say `--mem-per-cpu=3G`. The advantage of `--mem=45G` is that the memory consumed by each individual process doesn't matter, as long as all of them together don’t use more than 45GB. With `--mem-per-cpu=3G`, the job will be cancelled if any of the processes exceeds 3GB.

### Large parallel job, not a multiple of whole nodes

Not every application runs with maximum efficiency on a multiple of 32 (or 40, or 48) cores. Choosing the number of cores to request—and whether or not to request whole nodes—may be a trade-off between *running* time (or efficient use of the computer) and *waiting* time (or efficient use of your time). If you want help evaluating these factors, please contact [Technical support](../support/technical_support.md).

## Hybrid jobs: MPI and OpenMP, or MPI and threads

It is important to understand that the number of *tasks* requested of Slurm is the number of *processes* that will be started by `srun`. So for a hybrid job that will use both MPI processes and OpenMP threads or Posix threads, you should set the MPI process count with `--ntasks` or `--ntasks-per-node`, and set the thread count with `--cpus-per-task`.

```bash
--ntasks=16
--cpus-per-task=4
--mem-per-cpu=3G
srun --cpus-per-task=$SLURM_CPUS_PER_TASK application.exe
```
In this example, a total of 64 cores will be allocated, but only 16 MPI processes (tasks) can and will be initialized. If the application is also OpenMP, then each process will spawn 4 threads, one per core. Each process will be allocated with 12GB of memory. The tasks, with 4 cores each, could be allocated anywhere, from 2 to up to 16 nodes. Note that you must specify `--cpus-per-task=$SLURM_CPUS_PER_TASK` for `srun` as well, as this is a requirement since Slurm 22.05 and does not hurt for older versions.

```bash
--nodes=2
--ntasks-per-node=8
--cpus-per-task=4
--mem=96G
srun --cpus-per-task=$SLURM_CPUS_PER_TASK application.exe
```
This job is the same size as the last one: 16 tasks (that is, 16 MPI processes), each with 4 threads. The difference here is that we are sure of getting exactly 2 whole nodes. Remember that `--mem` requests memory *per node*, so we use it instead of `--mem-per-cpu` for the reason described earlier.

## Why srun instead of mpiexec or mpirun?

`mpirun` is a wrapper that enables communication between processes running on different machines. Modern schedulers already provide many things that `mpirun` needs. With Torque/Moab, for example, there is no need to pass to `mpirun` the list of nodes on which to run, or the number of processes to launch; this is done automatically by the scheduler. With Slurm, the task affinity is also resolved by the scheduler, so there is no need to specify things like
```bash
mpirun --map-by node:pe=4 -n 16  application.exe
```
As implied in the examples above, `srun application.exe` will automatically distribute the processes to precisely the resources allocated to the job.

In programming terms, `srun` is at a higher level of abstraction than `mpirun`. Anything that can be done with `mpirun` can be done with `srun`, and more. It is the tool in Slurm to distribute any kind of computation. It replaces Torque’s `pbsdsh`, for example, and much more. Think of `srun` as the SLURM *all-around parallel-tasks distributor*; once a particular set of resources is allocated, the nature of your application doesn't matter (MPI, OpenMP, hybrid, serial farming, pipelining, multiprogram, etc.), you just have to `srun` it.

Also, as you would expect, `srun` is fully coupled to Slurm. When you `srun` an application, a *job step* is started, the environment variables `SLURM_STEP_ID` and `SLURM_PROCID` are initialized correctly, and correct accounting information is recorded.

For an example of some differences between `srun` and `mpiexec`, see [this discussion](https://mail-archive.com/users@lists.open-mpi.org/msg31874.html) on the Open MPI support forum. Better performance might be achievable with `mpiexec` than with `srun` under certain circumstances, but using `srun` minimizes the risk of a mismatch between the resources allocated by Slurm and those used by Open MPI.

## External links

*   [`sbatch`](https://slurm.schedmd.com/sbatch.html) documentation
*   [`srun`](https://slurm.schedmd.com/srun.html) documentation
*   [Open MPI](https://www.open-mpi.org/faq/?category=slurm) and Slurm