---
title: "Cedar/en"
slug: "cedar"
lang: "en"

source_wiki_title: "Cedar/en"
source_hash: "f967042850b2d09c85bffd07bc4d5bd3"
last_synced: "2026-04-12T15:59:52.668416+00:00"
last_processed: "2026-04-12T18:09:04.808397+00:00"

tags:
  []

keywords:
  - "Cedar cluster"
  - "Cedar"
  - "3.0GHz"
  - "AMD EPYC 7302"
  - "node-local storage"
  - "High-performance interconnect"
  - "Storage space"
  - "job submission"
  - "480G SSD"
  - "network topology"
  - "2.1GHz"
  - "CPU cores"
  - "Node characteristics"
  - "Intel E5-2683 v4 Broadwell"
  - "compute nodes"

questions:
  - "When is the Cedar cluster scheduled to end its service, and where is it physically located?"
  - "What are the differences in purpose, capacity, and backup policies among Cedar's Home, Scratch, and Project storage spaces?"
  - "What are the hardware specifications of Cedar in terms of its total CPU cores, GPU devices, and interconnect technology?"
  - "Why are jobs restricted from running in the `/home` directory, and which filesystems should be used instead?"
  - "How does the scheduler manage memory allocation to prevent swapping, and what is the recommended approach for choosing a node type?"
  - "What is the theoretical peak performance of the Cedar system, and how is its network topology structured?"
  - "What are the different CPU models and their respective clock speeds mentioned in the hardware configurations?"
  - "What is the standard solid-state drive (SSD) storage setup used across all the listed server specifications?"
  - "How do the varying capacity metrics, such as 250G, 502G, 1510G, and 4000G, differentiate the available hardware tiers?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

| Availability         | **SERVICE ENDS 2025 SEPTEMBER 12** |
| :------------------- | :--------------------------------- |
| Login node           | **cedar.alliancecan.ca**           |
| Globus collection    | **computecanada#cedar-globus**     |
| System Status Page   | **https://status.alliancecan.ca/** |

Cedar is a heterogeneous cluster suitable for a variety of workloads; it is located at Simon Fraser University. It is named for the [Western Red Cedar](https://en.wikipedia.org/wiki/Thuja_plicata), B.C.’s official tree, which is of great spiritual significance to the region's First Nations people.

Cedar is sold and supported by Scalar Decisions, Inc. The node manufacturer is Dell, the high-performance temporary storage `/scratch` filesystem is from DDN, and the interconnect is from Intel. It is entirely liquid-cooled, using rear-door heat exchangers.

!!! note
    Globus version 4 endpoints are no longer supported. The endpoint **computecanada#cedar-dtn** has been retired. Please use version 5 endpoint **computecanada#cedar-globus**.

*   [Getting started with Cedar](../getting-started/getting_started.md)
*   [How to run jobs](../running-jobs/running_jobs.md)
*   [Transferring data](../getting-started/transferring_data.md)

## Storage

| Storage Space                 | Details                                                                                                                                                                                                                                                                                                                              |
| :---------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Home space**<br>526TB total volume | *   Location of `/home` directories.<br>*   Each `/home` directory has a small fixed [quota](../storage-and-data/storage_and_file_management.md#filesystem-quotas-and-policies).<br>*   Not allocated via [RAS](https://alliancecan.ca/en/services/advanced-research-computing/accessing-resources/rapid-access-service) or [RAC](https://alliancecan.ca/en/services/advanced-research-computing/accessing-resources/resource-allocation-competition). Larger requests go to the `/project` space.<br>*   Has daily backup |
| **Scratch space**<br>5.4PB total volume<br>Parallel high-performance filesystem | *   For active or temporary (scratch) storage.<br>*   Not allocated.<br>*   Large fixed [quota](../storage-and-data/storage_and_file_management.md#filesystem-quotas-and-policies) per user.<br>*   Inactive data will be [purged](../storage-and-data/scratch_purging_policy.md).                                                                                                                                                                           |
| **Project space**<br>23PB total volume<br>External persistent storage | *   Not designed for parallel I/O workloads. Use `/scratch` space instead.<br>*   Large adjustable [quota](../storage-and-data/storage_and_file_management.md#filesystem-quotas-and-policies) per project.<br>*   Has daily backup.                                                                                                                                                                             |

The `/scratch` storage space is a Lustre filesystem based on DDN model ES14K technology. It includes 640 8TB NL-SAS disk drives, and dual redundant metadata controllers with SSD-based storage.

## High-performance interconnect

*Intel OmniPath (version 1) interconnect (100Gbit/s bandwidth).*

A low-latency high-performance fabric connecting all nodes and temporary storage.

By design, Cedar supports multiple simultaneous parallel jobs of up to 1024 Broadwell cores (32 nodes) or 1536 Skylake cores (32 nodes) or 1536 Cascade Lake cores (32 nodes) in a fully non-blocking manner. For larger jobs the interconnect has a 2:1 blocking factor, i.e., even for jobs running on several thousand cores, Cedar provides a high-performance interconnect.

## Node characteristics

Cedar has 100,400 CPU cores for computation, and 1352 GPU devices. Turbo Boost is deactivated for all Cedar nodes.

| nodes | cores | available memory  | CPU                                         | storage      | GPU                                       |
| :---- | :---- | :---------------- | :------------------------------------------ | :----------- | :---------------------------------------- |
| 256   | 32    | 125G or 128000M   | 2 x Intel E5-2683 v4 Broadwell @ 2.1GHz     | 2 x 480G SSD | -                                         |
| 256   | 32    | 250G or 257000M   | 2 x Intel E5-2683 v4 Broadwell @ 2.1GHz     | 2 x 480G SSD | -                                         |
| 40    | 32    | 502G or 515000M   | 2 x Intel E5-2683 v4 Broadwell @ 2.1GHz     | 2 x 480G SSD | -                                         |
| 16    | 32    | 1510G or 1547000M | 2 x Intel E5-2683 v4 Broadwell @ 2.1GHz     | 2 x 480G SSD | -                                         |
| 6     | 32    | 4000G or 4096000M | 2 x AMD EPYC 7302 @ 3.0GHz                  | 2 x 480G SSD | -                                         |
| 2     | 40    | 6000G or 6144000M | 4 x Intel Gold 5215 Cascade Lake @ 2.5GHz   | 2 x 480G SSD | -                                         |
| 96    | 24    | 125G or 128000M   | 2 x Intel E5-2650 v4 Broadwell @ 2.2GHz     | 1 x 800G SSD | 4 x NVIDIA P100 Pascal (12G HBM2 memory)  |
| 32    | 24    | 250G or 257000M   | 2 x Intel E5-2650 v4 Broadwell @ 2.2GHz     | 1 x 800G SSD | 4 x NVIDIA P100 Pascal (16G HBM2 memory)  |
| 192   | 32    | 187G or 192000M   | 2 x Intel Silver 4216 Cascade Lake @ 2.1GHz | 1 x 480G SSD | 4 x NVIDIA V100 Volta (32G HBM2 memory)   |
| 608   | 48    | 187G or 192000M   | 2 x Intel Platinum 8160F Skylake @ 2.1GHz   | 2 x 480G SSD | -                                         |
| 768   | 48    | 187G or 192000M   | 2 x Intel Platinum 8260 Cascade Lake @ 2.4GHz | 2 x 480G SSD | -                                         |

!!! note "Memory Allocation"
    The amount of available memory is fewer than the *round number* suggested by the hardware configuration. For instance, *base* nodes do have 128 GiB of RAM, but some of it is permanently occupied by the kernel and OS. To avoid wasting time by swapping/paging, the scheduler will never allocate jobs whose memory requirements exceed the amount of *available* memory shown above.

All nodes have local (on-node) temporary storage. Compute nodes (except GPU nodes) have two 480GB SSD drives, for a total raw capacity of 960GB. GPU nodes have either an 800GB or a 480GB SSD drive. Use node-local storage through the job-specific directory created by the scheduler, `$SLURM_TMPDIR`. See [Using node-local storage](../storage-and-data/using_node-local_storage.md).

### Choosing a node type
A number of 48-core nodes are reserved for jobs that require whole nodes. There are no 32-core nodes set aside for whole node processing. **Jobs that request less than 48 cores per node can end up sharing nodes with other jobs.**

Most applications will run on either Broadwell, Skylake, or Cascade Lake nodes, and performance differences are expected to be small compared to job waiting times. Therefore, we recommend that you do not select a specific node type for your jobs. If it is necessary, use `--constraint=cascade`, `--constraint=skylake`, or `--constraint=broadwell`. If the requirement is for any AVX512 node, use `--constraint=[skylake|cascade]`.

## Submitting and running jobs policy

!!! warning "Job Submission Policy Change"
    As of **April 17, 2019**, jobs can no longer run in the `/home` filesystem. This policy was implemented to reduce the load on this filesystem and improve responsiveness for interactive work. If you receive the message `Submitting jobs from directories residing in /home is not permitted`, transfer the files either to your `/project` or `/scratch` directory and submit the job from there.

## Performance
Theoretical peak double precision performance of Cedar is 6547 teraflops for CPUs, plus 7434 for GPUs, yielding almost 14 petaflops of theoretical peak double precision performance.

Cedar's network topology is made up of *islands* with a 2:1 blocking factor between islands. Within an island the interconnect (Omni-Path fabric) is fully non-blocking.

Most islands contain 32 nodes:
*   16 islands with 32 Broadwell nodes, each with 32 cores, i.e., 1024 cores per island;
*   43 islands with 32 Skylake or Cascade Lake nodes, each with 48 cores, i.e., 1536 cores per island;
*   4 islands with 32 P100 GPU nodes;
*   6 islands with 32 V100 GPU nodes;
*   2 islands each with 32 big memory nodes; of these 64 nodes, 40 are of 0.5TB, 16 are of 1.5TB, 6 are of 4TB and 2 are of 6TB.