---
title: "Metrix"
slug: "metrix"
lang: "base"

source_wiki_title: "Metrix"
source_hash: "e8e43566a327bde05a7c499aecb751b2"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T08:30:43.360645+00:00"

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

# Overview

The Metrix portal is a website for Alliance users. It uses information collected from compute nodes and management servers to interactively generate data, allowing users to monitor their real-time resource usage (CPU, GPU, memory, file system).

| Cluster | URL |
| :------ | :-- |
| Rorqual | [https://metrix.rorqual.alliancecan.ca](https://metrix.rorqual.alliancecan.ca) |
| Narval  | [https://portail.narval.calculquebec.ca](https://portail.narval.calculquebec.ca) |
| Nibi    | [https://portal.nibi.sharcnet.ca](https://portal.nibi.sharcnet.ca) |

**File System Performance**

This section displays bandwidth and metadata operation graphs, with the following viewing options: last week, last day, and last hour.

**Login Nodes**

CPU, memory, system load, and network usage statistics are presented in this tab, with the following viewing options: last week, last day, and last hour.

**Scheduling**

This tab presents statistics on allocated cluster cores and GPUs, with the following viewing options: last week, last day, and last hour.

**Scientific Software**

The most used software with CPU cores and GPUs are presented in graphs.

**Data Transfer Nodes**

Bandwidth statistics for data transfer nodes are presented in this tab.

# User Summary

Under the user summary tab, you will find your quotas for different file systems, followed by your last 10 jobs. You can select a job by its number to access its detailed page. Additionally, by clicking on (More details), you will be redirected directly to the **Job Statistics** tab, where you will find all your jobs.

# Job Statistics

The first block displays your current usage (CPU cores, memory, and GPUs). These statistics represent the average resources used by all currently running jobs. You can easily compare your allocated resources to those you are actually using.

You then have access to a several-day average, presented in a graph.

Next, you have a representation of your activity on the file systems. On the left, the graph shows the number of disk write commands you have performed (*input/output operations per second (IOPS)*). On the right, you see the amount of data transferred to the servers over a given period (Bandwidth).

The following section presents all the jobs you have already launched, which are currently running or pending. In the top left, you can filter jobs by status (OOM, completed, running, etc.). In the top right, you can search by job ID or name. Finally, in the bottom right, an option allows you to quickly navigate between pages by making multiple jumps.

## CPU Job Page

At the top, you have the job name, its number, your username, and its status. The details of your submission script are displayed by clicking on "View job script". If the job was launched in interactive mode, the submission script will not be available.

The working directory and submission command are accessible by clicking on "View submission command".

The next section is dedicated to scheduler information. You can access your CPU account monitoring page by clicking on your account number.

In the **Resources** section, you can get an initial overview of your job's resource usage by comparing the **Allocated** and **Used** columns for the various parameters listed.

The **CPU** graph allows you to visualize the CPU cores you requested over time. On the right, you can select/deselect different cores according to your needs.

!!! note
    For very short jobs, this graph is not available.

The **Memory** graph allows you to visualize the memory usage you requested over time.

The **Process and threads** graph allows you to observe different parameters related to processes and execution threads.

!!! tip
    Ideally, for a multi-threaded job, the sum of **Running threads** and **Sleeping threads** should not exceed 2 times the number of requested cores. That said, it is quite normal to have some processes in **sleeping** mode (*Sleeping threads*) for certain types of programs (Java, Matlab, commercial software, or complex programs). You also have the program applications executed over time as a parameter.

The following graphs represent file system usage for the current job, not the entire node. On the left, a representation of the number of *input/output operations per second (IOPS)* is displayed. On the right, the graph illustrates the data transfer rate between the job and the file system over time. This graph allows identifying periods of intense activity or low file system usage.

!!! warning
    For statistics on the entire node's resources, please note that they may be imprecise if the node is shared among multiple users.

The graph on the left illustrates the evolution of bandwidth used by the job over time, in relation to software, licenses, etc. The graph on the right represents the evolution of network bandwidth used by a job or set of jobs via the Infiniband network over time. One can observe periods of massive data transfer (e.g., read/write on a file system (Lustre), MPI communication between nodes).

The graph on the left illustrates the evolution of the number of *input/output operations per second (IOPS)* performed on the local disk over time. The one on the right shows the evolution of bandwidth used on the local disk over time, i.e., the amount of data read or written per second.

Graphical representation of local disk space usage.

Graphical representation of power usage.

## CPU Job Page (Job Array)

The CPU job page in a *job array* is identical to that of a regular CPU job, with the exception of the "Other jobs in the array" section. The table lists the other job numbers that are part of the same job array, along with information on their status, name, start time, and end time.

## GPU Job Page

At the top of the page, you have the job name, its number, your username, and its status. The details of your submission script are displayed by clicking on "View job script". If you launched an interactive job, the submission script is not available.

The directory and submission command are accessible by clicking on "View submission command".

The following section is reserved for scheduler information. You can access your GPU account page by clicking on your account number.

In the **Resources** section, you can get an initial overview of your job's resource usage by comparing the **Allocated** and **Used** columns for the various parameters listed.

The **CPU** graph allows you to visualize the usage of requested CPU cores over time. On the right, you can select/deselect different cores according to your needs.

!!! note
    For very short jobs, this graph is not available.

The **Memory** graph allows you to visualize the memory usage you requested for the CPU over time.

The **Process and threads** graph allows you to observe different parameters related to processes and execution threads.

The following graphs represent file system usage for the current job, not the entire node. On the left, a representation of the number of *input/output operations per second (IOPS)* is displayed. On the right, the graph illustrates the data transfer rate between the job and the file system over time. This graph allows identifying periods of intense activity or low file system usage.

The GPU graph represents your GPU usage. The *Streaming Multiprocessors* (SM) active parameter indicates the percentage of time the GPU executes a warp (a group of *threads*) in the last sampling window. This value should ideally be around 80%. For *SM occupancy* (defined as the ratio of warps assigned to an SM to the maximum number of warps an SM can handle), a value around 50% is generally expected. For the *Tensor* parameter, the value should be as high as possible. Ideally, your code should leverage this part of the GPU, optimized for multi-dimensional matrix multiplications and convolutions. Finally, for floating-point operations (*Floating Point*) FP64, FP32, and FP16, you should observe significant activity in only one of these types, depending on the precision used by your code.

On the left, you have a graph indicating the memory used by the GPU. On the right, a graph of GPU memory access cycles, representing the percentage of cycles during which the device's memory interface is active to send or receive data.

The GPU power graph displays the evolution of the GPU's power consumption (in watts) over time.

On the left, GPU bandwidth on the PCIe bus (or **PCI Express**, for *Peripheral Component Interconnect Express*). On the right, GPU bandwidth on the NVLink bus. NVLink is a technology developed by NVIDIA to enable ultra-fast communication between multiple GPUs.

!!! warning
    For statistics on the entire node's resources, please note that they may be imprecise if the node is shared among multiple users.

The graph on the left illustrates the evolution of bandwidth used by the job over time, in relation to software, licenses, etc. The graph on the right represents the evolution of network bandwidth used by a job or set of jobs via the Infiniband network over time. One can observe periods of massive data transfer (e.g., read/write on a file system (Lustre), MPI communication between nodes).

The graph on the left illustrates the evolution of the number of *input/output operations per second (IOPS)* performed on the local disk over time. The one on the right shows the evolution of bandwidth used on the local disk over time, i.e., the amount of data read or written per second.

Graphical representation of local disk space usage.

Graphical representation of power usage.

# Account Statistics

The **Account Statistics** section groups your group's usage into two subsections: CPU and GPU.

## CPU Account Statistics

Here you will find the sum of your group's requests for CPU cores, as well as their corresponding usage over the last months. You can also monitor the evolution of your priority, which varies based on your usage.

This graph shows the most commonly used applications.

Here you can consult resource usage by each user in your group.

This graph shows the evolution over time of CPU cores wasted by each user in the group.

Here you can consult memory usage by each user in your group.

This graph represents the memory wasted by each user.

Next, you have a representation of your activity on the file systems. On the left, the graph shows the number of disk write commands you have performed (input/output operations per second (IOPS)). On the right, you see the amount of data transferred to the servers over a given period (Bandwidth).

You have a list of the latest jobs that have been performed for the entire group.

## GPU Account Statistics

Here you will find the sum of your group's GPU requests, as well as the corresponding usage over the last months. You can also monitor the evolution of your priority, which varies based on your usage.

This graph represents the most commonly used applications.

Here you can consult resource usage by each user in your group.

The following graph represents, over time, the amount of GPUs wasted per user.

Next, you have the CPU cores allocated and used in your GPU jobs.

This figure illustrates the wastage of CPUs in your GPU jobs.

Here you can visualize memory usage for each user in your group.

This graph illustrates the memory wasted by each user.

Next, you have a representation of your activity on the file systems. On the left, the graph shows the number of disk write commands you have performed (input/output operations per second (IOPS)). On the right, you see the amount of data transferred to the servers over a given period (Bandwidth).

Here is a list of the latest jobs performed at your group level.

# Cloud Statistics

The first table, "Your Instances", presents all virtual machines associated with an account. The "Flavour" column refers to the [virtual machine flavour](virtual-machine-flavours.md). The "UUID" column corresponds to a unique identifier assigned to each virtual machine.

Subsequently, each virtual machine has its own usage statistics (CPU Cores, Memory, Disk Bandwidth, Disk IOPS, and Network Bandwidth) viewable for the last month, last week, last day, or last hour.