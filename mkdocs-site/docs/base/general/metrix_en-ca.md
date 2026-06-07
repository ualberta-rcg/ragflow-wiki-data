---
title: "Metrix/en-ca"
slug: "metrix_en-ca"
lang: "base"

source_wiki_title: "Metrix/en-ca"
source_hash: "0e295916fba3382e31533f0614e6bccd"
last_synced: "2026-06-07T00:07:37.701416+00:00"
last_processed: "2026-06-07T00:24:25.824447+00:00"

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

## Overview

The Metrix portal is a website for Alliance users. It leverages information collected from compute nodes and management servers to interactively generate data, allowing users to monitor their real-time resource utilization (CPU, GPU, memory, file system).

| Cluster | URL |
| :------ | :------------------------------------ |
| Rorqual | [https://metrix.rorqual.alliancecan.ca](https://metrix.rorqual.alliancecan.ca) |
| Narval  | [http://metrix.narval.alliancecan.ca](http://metrix.narval.alliancecan.ca) |
| Nibi    | [https://portal.nibi.sharcnet.ca](https://portal.nibi.sharcnet.ca) |
| tamIA   | [https://portail.tamia.ecpia.ca](https://portail.tamia.ecpia.ca) |
| Vulcan  | [http://metrix.vulcan.alliancecan.ca](http://metrix.vulcan.alliancecan.ca) |

**File System Performance**

This section presents information on bandwidth and metadata operations, with visualization options for the last week, last day, and last hour.

**Login Nodes**

CPU, memory, system load, and network utilization statistics are provided in this tab, with visualization options for the last week, last day, and last hour.

**Scheduling**

This tab presents statistics on allocated CPU cores and GPUs for the cluster, with visualization options for the last week, last day, and last hour.

**Scientific Software**

The most frequently used software with CPU cores and GPUs is presented.

**Data Transfer Nodes**

Bandwidth statistics for data transfer nodes are presented in this tab.

## User Summary

Under the user summary tab, you will find your quotas for different file systems, followed by your last 10 jobs. You can select a job by its number to access the detailed page. Additionally, by clicking on "(More details)", you will be redirected directly to the **Job Statistics** tab, where you will find all your jobs.

## Job Statistics

The first block shows your current utilization (CPU cores, memory, and GPUs). These statistics represent the average of resources used by all currently running jobs. You can easily compare the resources allocated to you with those you actually use.

You then have access to an average of the last few days.

This section provides a representation of your activity on the file systems. It shows the number of disk write commands you have performed (*input/output operations per second (IOPS)*) and the amount of data transferred to the servers over a given period (Bandwidth).

The following section presents all jobs you have launched, which are currently running or pending. You can filter jobs by status (OOM, completed, running, etc.). You can also search by job ID or name. Finally, an option allows you to quickly navigate between pages by making multiple jumps.

### CPU Job Page

At the top, you will find the job name, its number, your username, and the status. Details of your submission script are displayed by clicking "View job script". If the job was launched in interactive mode, the submission script will not be available.

The working directory and submission command are accessible by clicking "View submission command".

The next section is dedicated to scheduler information. You can access your CPU account tracking page by clicking on your account number.

In the **Resources** section, you can get an initial overview of your job's resource utilization by comparing the **Allocated** and **Used** columns for the various parameters listed.

The **CPU** section allows you to visualize the requested CPU cores over time. You can select/deselect different cores as needed. Note that for very short jobs, this information is not available.

The **Memory** section allows you to visualize the requested memory usage over time.

The **Process and threads** section allows you to observe different parameters related to processes and threads. Ideally, for a multithreaded job, the sum of **Running threads** and **Sleeping threads** should not exceed twice the number of requested cores. However, it is quite normal to have some processes in **sleeping** mode (*Sleeping threads*) for certain types of programs (Java, MATLAB, commercial software, or complex programs). Program applications executed over time are also displayed.

This section details file system usage for the current job, not the entire node. It provides information on the number of input/output operations per second (IOPS) and illustrates the data transfer rate between the job and the file system over time. This helps identify periods of intense activity or low file system utilization.

For full node resource statistics, be aware that these may be imprecise if the node is shared among multiple users. This section illustrates the evolution of bandwidth used by the job over time, in relation to software, licenses, etc. It also represents the evolution of network bandwidth used by a job or set of jobs via the Infiniband network over time. This allows observation of periods of massive data transfer (e.g., read/write on a file system (Lustre), MPI communication between nodes).

This section illustrates the evolution of the number of input/output operations per second (IOPS) performed on the local disk over time. It also shows the evolution of bandwidth used on the local disk over time, i.e., the amount of data read or written per second.

Local disk space utilization is displayed.

Power consumption is displayed.

### CPU Job Page (Job Array)

The page for a CPU job within a job array is identical to that of a regular CPU job, except for the *Other jobs in the array* section. This table lists other job numbers belonging to the same job array, along with information on their status, name, start time, and end time.

### GPU Job Page

At the top of the page, you will find the job name, its number, your username, and the status. Details of your submission script are displayed by clicking "View job script". If you launched an interactive job, the submission script is not available.

The working directory and submission command are accessible by clicking "View submission command".

The following section is reserved for scheduler information. You can access your GPU account page by clicking on your account number.

In the **Resources** section, you can get an initial overview of your job's resource utilization by comparing the **Allocated** and **Used** columns for the various parameters listed.

The **CPU** section allows you to visualize the usage of requested CPU cores over time. You can select/deselect different cores as needed. Note that for very short jobs, this information is not available.

The **Memory** section allows you to visualize the usage of memory requested for the CPUs over time.

The **Process and threads** section allows you to observe different parameters related to processes and threads.

This section details file system usage for the current job, not the entire node. It provides information on the number of input/output operations per second (IOPS) and illustrates the data transfer rate between the job and the file system over time. This helps identify periods of intense activity or low file system utilization.

The GPU usage information is displayed here. The *Streaming Multiprocessors* (SM) active parameter indicates the percentage of time the GPU executes a warp (a group of consecutive *threads*) in the last sampling window. This value should ideally be around 80%. For *SM occupancy* (defined as the ratio of warps assigned to an SM to the maximum number of warps an SM can handle), a value around 50% is generally expected. Regarding the *Tensor* parameter, the value should be as high as possible. Ideally, your code should leverage this part of the GPU, optimized for multidimensional matrix multiplications and convolutions. Finally, for *Floating Point* operations (FP64, FP32, and FP16), you should observe significant activity on only one of these types, depending on the precision used by your code.

This section provides information on GPU memory usage and GPU memory access cycles, representing the percentage of cycles during which the device's memory interface is active for sending or receiving data.

GPU power usage shows the evolution of the GPU's energy consumption (in watts) over time.

GPU bandwidth on the PCIe bus (or PCI Express, for Peripheral Component Interconnect Express) is presented.

For full node resource statistics, be aware that these may be imprecise if the node is shared among multiple users. This section illustrates the evolution of bandwidth used by the job over time, in relation to software, licenses, etc. It also represents the evolution of network bandwidth used by a job or set of jobs via the Infiniband network over time. This allows observation of periods of massive data transfer (e.g., read/write on a file system (Lustre), MPI communication between nodes).

This section illustrates the evolution of the number of input/output operations per second (IOPS) performed on the local disk over time. It also shows the evolution of bandwidth used on the local disk over time, i.e., the amount of data read or written per second.

Local disk space utilization is displayed.

Power consumption is displayed.

## Account Statistics

The **Account Statistics** section groups your group's utilization into two sub-sections: CPU and GPU.

### CPU Account Statistics

Here you will find your group's total CPU core requests and their corresponding utilization over the past months. You can also track the evolution of your priority, which varies based on your usage.

The most commonly used applications are shown here.

You can view resource utilization by each user in your group here.

This section shows the evolution of wasted CPU cores by each user in the group over time.

You can view memory utilization by each user in your group here.

Wasted memory per user is displayed here.

This section provides a representation of your activity on the file systems. It shows the number of disk write commands you have performed (input/output operations per second (IOPS)) and the amount of data transferred to the servers over a given period (Bandwidth).

A list of the latest jobs executed for the entire group is available.

### GPU Account Statistics

Here you will find your group's total GPU requests and their corresponding utilization over the past months. You can also track the evolution of your priority, which varies based on your usage.

The most commonly used applications are shown here.

You can view resource utilization by each user in your group here.

This section represents the amount of GPU wasted per user over time.

Allocated and used CPU cores within your GPU jobs are presented here.

CPU wastage within your GPU jobs is illustrated here.

You can visualize memory usage for each user in your group here.

This section illustrates wasted memory per user.

This section provides a representation of your activity on the file systems. It shows the number of disk write commands you have performed (input/output operations per second (IOPS)) and the amount of data transferred to the servers over a given period (Bandwidth).

A list of the latest jobs executed for your group is available here.

## Cloud Statistics

The first table, "Your Instances", presents all virtual machines associated with an account. The "Flavor" column refers to the [virtual machine type](../cloud/virtual_machine_flavors.md). The "UUID" column corresponds to a unique identifier assigned to each virtual machine.

Each virtual machine then has its own usage statistics (CPU Cores, Memory, Disk Bandwidth, Disk IOPS, and Network Bandwidth) viewable for the last month, last week, last day, or last hour.