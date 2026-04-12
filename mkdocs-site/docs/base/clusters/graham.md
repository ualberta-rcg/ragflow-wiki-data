---
title: "Graham"
slug: "graham"
lang: "base"

source_wiki_title: "Graham"
source_hash: "3b3f878170e7ba95ebf485d8fe4fdb1f"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:46:23.799271+00:00"

tags:
  []

keywords:
  - "heterogeneous cluster"
  - "cloud nodes"
  - "director switch"
  - "Node characteristics"
  - "noinclude"
  - "markup"
  - "code"
  - "IO buffering"
  - "InfiniBand interconnect"
  - "CPU and GPU nodes"
  - "scratch storage"
  - "Infiniband fabric"
  - "GPU nodes"
  - "storage space"
  - "Slurm"
  - "Turing T4"
  - "GPUs on Graham"
  - "translate"
  - "Graham cluster"
  - "High-performance interconnect"
  - "V100 Volta GPUs"
  - "Tesla GPUs"
  - "Ampere GPU nodes"
  - "GPUs"
  - "IO-intensive job"
  - "Volta V100"
  - "Graham"
  - "compute nodes"
  - "GPU request"
  - "Nibi"
  - "tags"
  - "capacity reduction"
  - "Ampere GPUs"

questions:
  - "What is the current operational status of the Graham cluster and which system has replaced it?"
  - "What are the site-specific policies regarding internet access, crontab usage, and job limits on Graham?"
  - "How do the Home, Scratch, and Project storage spaces differ in terms of capacity, purpose, and backup policies?"
  - "How are the connections for the CPU and GPU nodes aggregated by the director switch?"
  - "What is the architectural layout and uplink configuration specifically designed for the 56 cloud nodes?"
  - "Which network fabrics and bandwidth speeds are utilized to connect the various nodes to the scratch storage?"
  - "How does the Graham system's interconnect design handle multiple simultaneous parallel jobs and larger jobs requiring multiple islands?"
  - "What hardware changes occurred to Graham's node capacity in early 2025, and what specific GPU generations are currently available on the system?"
  - "What are the recommended best practices for users regarding CPU selection, local on-node storage, and memory allocation when submitting jobs?"
  - "What are the key performance differences and intended use cases for the V100 and T4 Turing GPUs?"
  - "What are the specific rules for scaling the requested number of CPU cores relative to GPUs on the different Volta nodes?"
  - "How should users manage significant I/O operations and temporary files when running jobs on the cluster?"
  - "Why do IO-intensive jobs typically need to request more memory than the aggregate size of their processes?"
  - "How many different generations of Tesla GPUs are available on the Graham system?"
  - "What are the specific models and features of the GPUs offered on Graham?"
  - "What is the specific function of the `</translate>` tag within wiki markup?"
  - "How does the `</noinclude>` tag affect the way a page is transcluded or displayed on other pages?"
  - "In what types of wiki environments or extensions are these two specific tags typically used together?"
  - "How do you properly specify a request for Ampere GPU nodes, such as A100 or A5000 cards, on the Graham cluster?"
  - "What operational capacity changes will the Graham cluster undergo starting January 13, 2025?"
  - "What is the name of the new system that will come online following the Graham cluster's capacity reduction?"
  - "What is the specific function of the `</translate>` tag within wiki markup?"
  - "How does the `</noinclude>` tag affect the way a page is transcluded or displayed on other pages?"
  - "In what types of wiki environments or extensions are these two specific tags typically used together?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! warning "Note"
    Graham has been retired and replaced by a new system, [Nibi](nibi.md). Please check the [Infrastructure renewal](infrastructure_renewal.md) page for system capacity, reductions, and outages during the installation and transition to the new systems.

*   **Availability**: In production since June 2017
*   **Login node**: `graham.alliancecan.ca`
*   **Globus collection**: `computecanada#graham-globus`
*   **Data transfer node (rsync, scp, sftp, etc.)**: use robot or login nodes

Graham is a heterogeneous cluster, suitable for a variety of workloads, and located at the University of Waterloo. It is named after [Wes Graham](https://en.wikipedia.org/wiki/Wes_Graham), the first director of the Computing Centre at Waterloo.

The parallel filesystem and external persistent storage (called "NDC-Waterloo" in some documents) are similar to [Cedar's](cedar.md). The interconnect is different and there is a slightly different mix of compute nodes.

It is entirely liquid cooled, using rear-door heat exchangers.

[Getting started with Graham](../getting-started/getting_started.md)

[How to run jobs](../running-jobs/running_jobs.md)

[Transferring data](../getting-started/transferring_data.md)

## Site-specific policies

*   By policy, Graham's compute nodes cannot access the internet. If you need an exception to this rule, contact [technical support](../support/technical_support.md) with the following information:

    ```text
    IP:
    Port/s:
    Protocol:  TCP or UDP
    Contact:
    Removal Date:
    ```

    On or after the removal date we will follow up with the contact to confirm if the exception is still required.

*   Crontab is not offered on Graham.
*   Each job on Graham should have a duration of at least one hour (five minutes for test jobs) and no more than 168 hours (seven days).
*   A user cannot have more than 1000 jobs, running and queued, at any given moment. An array job is counted as the number of tasks in the array.

## Storage

| Feature                                                   | Description                                                                                                                                                                                                                                                                                                                                       |
| :-------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Home space**<br>133TB total volume                      | *   Location of home directories.<br>*   Each home directory has a small, fixed [quota](../storage-and-data/storage_and_file_management.md#filesystem-quotas-and-policies).<br>*   Not allocated via [RAS](https://alliancecan.ca/en/services/advanced-research-computing/accessing-resources/rapid-access-service) or [RAC](https://alliancecan.ca/en/services/advanced-research-computing/accessing-resources/resource-allocation-competition). Larger requests go to Project space.<br>*   Has daily backup. |
| **Scratch space**<br>3.2PB total volume<br>Parallel high-performance filesystem | *   For active or temporary (`/scratch`) storage.<br>*   Not allocated.<br>*   Large fixed [quota](../storage-and-data/storage_and_file_management.md#filesystem-quotas-and-policies) per user.<br>*   Inactive data will be purged.                                                                                                                                                                      |
| **Project space**<br>16PB total volume<br>External persistent storage | *   Allocated via [RAS](https://alliancecan.ca/en/services/advanced-research-computing/accessing-resources/rapid-access-service) or [RAC](https://alliancecan.ca/en/services/advanced-research-computing/accessing-resources/resource-allocation-competition).<br>*   Not designed for parallel I/O workloads. Use Scratch space instead.<br>*   Large adjustable [quota](../storage-and-data/storage_and_file_management.md#filesystem-quotas-and-policies) per project.<br>*   Has daily backup.    |

## High-performance interconnect

Mellanox FDR (56Gb/s) and EDR (100Gb/s) InfiniBand interconnect. FDR is used for GPU and cloud nodes, EDR for other node types. A central 324-port director switch aggregates connections from islands of 1024 cores each for CPU and GPU nodes. The 56 cloud nodes are a variation on CPU nodes, and are on a single larger island sharing 8 FDR uplinks to the director switch.

A low-latency high-bandwidth Infiniband fabric connects all nodes and scratch storage.

Nodes configurable for cloud provisioning also have a 10Gb/s Ethernet network, with 40Gb/s uplinks to scratch storage.

The design of Graham is to support multiple simultaneous parallel jobs of up to 1024 cores in a fully non-blocking manner.

For larger jobs the interconnect has a 8:1 blocking factor, i.e., even for jobs running on multiple islands the Graham system provides a high-performance interconnect.

[Graham high performance interconnect diagram](https://docs.computecanada.ca/mediawiki/images/b/b3/Gp3-network-topo.png)

## Visualization on Graham

Graham has dedicated visualization nodes available at **gra-vdi.alliancecan.ca** that allow only VNC connections. For instructions on how to use them, see the [VNC](../interactive/vnc.md) page.

## Node characteristics

In early 2025 Graham's capacity was reduced to make space for the installation of the new Nibi cluster. The table below lists the remaining nodes as of February, 2025.

[Turbo Boost](https://en.wikipedia.org/wiki/Intel_Turbo_Boost) is enabled for all Graham nodes.

| nodes | cores | available memory | CPU                                   | storage         | GPU                                                |
| :---- | :---- | :--------------- | :------------------------------------ | :-------------- | :------------------------------------------------- |
| 2     | 40    | 377G or 386048M  | 2 x Intel Xeon Gold 6248 Cascade Lake @ 2.5GHz | 5.0TB NVMe SSD  | 8 x NVIDIA V100 Volta (32GB HBM2 memory),NVLINK    |
| 6     | 16    | 187G or 191840M  | 2 x Intel Xeon Silver 4110 Skylake @ 2.10GHz | 11.0TB SATA SSD | 4 x NVIDIA T4 Turing (16GB GDDR6 memory)           |
| 30    | 44    | 187G or 191840M  | 2 x Intel Xeon Gold 6238 Cascade Lake @ 2.10GHz | 5.8TB NVMe SSD  | 4 x NVIDIA T4 Turing (16GB GDDR6 memory)           |
| 136   | 44    | 187G or 191840M  | 2 x Intel Xeon Gold 6238 Cascade Lake @ 2.10GHz | 879GB SATA SSD  | -                                                  |
| 1     | 128   | 2000G or 2048000M| 2 x AMD EPYC 7742                     | 3.5TB SATA SSD  | 8 x NVIDIA A100 Ampere                             |
| 2     | 32    | 256G or 262144M  | 2 x Intel Xeon Gold 6326 Cascade Lake @ 2.90GHz | 3.5TB SATA SSD  | 4 x NVIDIA A100 Ampere                             |
| 11    | 64    | 128G or 131072M  | 1 x AMD EPYC 7713                     | 1.8TB SATA SSD  | 4 x NVIDIA RTX A5000 Ampere                        |
| 6     | 32    | 1024G or 1048576M| 1 x AMD EPYC 7543                     | 8x2TB NVMe      | -                                                  |

Most applications will run on either Skylake or Cascade Lake nodes, and performance differences are expected to be small compared to job waiting times. Therefore we recommend that you do not select a specific node type for your jobs. If it is necessary to constrain a CPU job, use `--constraint=cascade`. See [how to specify the CPU architecture](../running-jobs/running_jobs.md#cluster-particularities).

Best practice for local on-node storage is to use the temporary directory generated by [Slurm](../running-jobs/running_jobs.md), `$SLURM_TMPDIR`. Note that this directory and its contents will disappear upon job completion.

Note that the amount of available memory is less than the "round number" suggested by hardware configuration. For instance, "base" nodes do have 128 GiB of RAM, but some of it is permanently occupied by the kernel and OS. To avoid wasting time by swapping/paging, the scheduler will never allocate jobs whose memory requirements exceed the specified amount of "available" memory. Please also note that the memory allocated to the job must be sufficient for IO buffering performed by the kernel and filesystem - this means that an IO-intensive job will often benefit from requesting somewhat more memory than the aggregate size of processes.

## GPUs on Graham
Graham contains Tesla GPUs from three different generations, listed here in order of age, from oldest to newest.

*   V100 Volta GPUs (2 nodes with NVLINK interconnect)
*   T4 Turing GPUs
*   A100 Ampere

P100 GPUs have been decommissioned. V100 is its successor, with about double the performance for standard computation, and about 8X performance for deep learning computations which can utilize its tensor core computation units. T4 Turing is the latest card targeted specifically at deep learning workloads - it does not support efficient double precision computations, but it has good performance for single precision, and it also has tensor cores, plus support for reduced precision integer calculations.

### Pascal GPU nodes on Graham
No longer available.

### Volta GPU nodes on Graham
Graham has a total of 2 Volta nodes. They have high bandwidth NVLINK interconnect.

**The nodes are available to all users with a maximum job duration of seven days.**

Following is an example job script to submit a job to one of the nodes (with 8 GPUs). The module load command will ensure that modules compiled for Skylake architecture will be used. Replace nvidia-smi with the command you want to run.

**Important**: You should scale the number of CPUs requested, keeping the ratio of CPUs to GPUs at 3.5 or less on 28 core nodes. For example, if you want to run a job using 4 GPUs, you should request **at most 14 CPU cores**. For a job with 1 GPU, you should request **at most 3 CPU cores**. Users are allowed to run a few short test jobs (shorter than 1 hour) that break this rule to see how your code performs.

The two newest Volta nodes have 40 cores so the number of cores requested per GPU should be adjusted upwards accordingly, i.e. you can use 5 CPU cores per GPU. They also have NVLINK, which can provide huge benefits for situations where memory bandwidth between GPUs is the bottleneck. If you want to use one of these NVLINK nodes, you should request it directly by adding the `--constraint=cascade,v100` parameter to the job submission script.

Single-GPU example:
```sh linenums="1" title="gpu_single_GPU_job.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --gres=gpu:v100:1
#SBATCH --cpus-per-task=3
#SBATCH --mem=12G
#SBATCH --time=1-00:00
module load arch/avx512 StdEnv/2018.3
nvidia-smi
```
Full-node example:
```sh linenums="1" title="gpu_single_node_job.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --nodes=1
#SBATCH --gres=gpu:v100:8
#SBATCH --exclusive
#SBATCH --cpus-per-task=28
#SBATCH --mem=150G
#SBATCH --time=1-00:00
module load StdEnv/2023
nvidia-smi
```

The Volta nodes have a fast local disk, which should be used for jobs if the amount of I/O performed by your job is significant. Inside the job, the location of the temporary directory on fast local disk is specified by the environment variable `$SLURM_TMPDIR`. You can copy your input files there at the start of your job script before you run your program and your output files out at the end of your job script. All the files in `$SLURM_TMPDIR` will be removed once the job ends, so you do not have to clean up that directory yourself. You can even create Python virtual environments in this temporary space for greater efficiency. Please see the [information on how to do this](../software/python.md#creating-virtual-environments-inside-of-your-jobs).

### Turing GPU nodes on Graham

The usage of these nodes is similar to using the Volta nodes, except when requesting them, you should specify:

`--gres=gpu:t4:2`

In this example, two T4 cards per node are requested.

### Ampere GPU nodes on Graham

The usage of these nodes is similar to using the Volta nodes, except when requesting them, you should specify:

`--gres=gpu:a100:2`

or

`--gres=gpu:a5000:2`

In this example, two Ampere cards per node are requested.

## Graham reduction
Starting January 13, 2025, the Graham cluster will operate at approximately 25% capacity until the new system [Nibi](nibi.md) comes online.