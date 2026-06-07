---
title: "Metrix"
slug: "metrix"
lang: "base"

source_wiki_title: "Metrix"
source_hash: "ba22be5650ddd42a355fa50054fb8dc0"
last_synced: "2026-06-07T00:07:37.701416+00:00"
last_processed: "2026-06-07T00:21:15.970128+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: true
  qa_generated: false
---

# Overview

The Metrix portal is a website for Alliance users. It leverages information collected from compute nodes and management servers to interactively generate data, allowing users to monitor their real-time resource usage (CPU, GPU, memory, file system).

| Cluster | URL |
| :------ | :-- |
| Rorqual | [https://metrix.rorqual.alliancecan.ca](https://metrix.rorqual.alliancecan.ca) |
| Narval | [http://metrix.narval.alliancecan.ca](http://metrix.narval.alliancecan.ca) |
| Nibi | [https://portal.nibi.sharcnet.ca](https://portal.nibi.sharcnet.ca) |
| tamIA | [https://portail.tamia.ecpia.ca](https://portail.tamia.ecpia.ca) |
| Vulcan | [http://metrix.vulcan.alliancecan.ca](http://metrix.vulcan.alliancecan.ca) |

**File System Performance**
Here you will find bandwidth and metadata operation metrics, accompanied by the following visualization options: last week, last day, and last hour.

**Login Nodes**
CPU, memory, system load, and network usage statistics are presented in this tab, with the following visualization options: last week, last day, and last hour.

**Scheduling**
This tab presents statistics on allocated CPU cores and GPUs of the cluster, with the following visualization options: last week, last day, and last hour.

**Scientific Software**
The most used software with CPU cores and GPUs are presented as usage metrics.

**Data Transfer Nodes**
Bandwidth statistics for data transfer nodes are presented in this tab.

# User Summary
Under the user summary tab, you will find your quotas for different file systems, followed by your last 10 jobs. You can select one by its number to access the detailed page. Additionally, by clicking on **(More details)**, you will be redirected directly to the **Job Statistics** tab, where you will find all your jobs.

# Job Statistics
The first block displays your current usage (CPU core, memory, and GPUs). These statistics represent the average resources used by all currently running jobs. You can easily compare the resources allocated to you with those you actually use.

You then have access to an average of the last few days' usage.

You then have a representation of your file system activity. This includes the number of disk write commands you have performed (*input/output operations per second (IOPS)*) and the amount of data transferred to the servers over a given period (Bandwidth).

The next section presents all the jobs you have already launched, which are currently running or pending. In the upper left, you can filter jobs by status (OOM, completed, running, etc.). In the upper right, you can search by job ID or name. Finally, in the lower right, an option allows you to quickly navigate between pages by performing multiple jumps.

## CPU Job Page
At the top, you have the job name, its number, your username, and the status. Details of your submission script are displayed by clicking on **View job script**. If the job was launched in interactive mode, the submission script will not be available.

The working directory and submission command are accessible by clicking on **View submission command**.

The next section is dedicated to scheduler information. You can access your CPU account tracking page by clicking on your account number.

In the **Resources** section, you can get an initial overview of your job's resource usage by comparing the **Allocated** and **Used** columns for the various listed parameters.

The **CPU** usage metrics allow you to visualize the CPU cores you requested over time. You can select/deselect different cores as needed. Note that for very short jobs, this metric is not available.

The **Memory** usage metrics allow you to visualize the memory usage you requested over time.

The **Process and threads** metrics allow you to observe different parameters related to processes and execution threads. Ideally, for a multithreading job, the sum of the **Running threads** and **Sleeping threads** parameters should not exceed twice the number of requested cores. That said, it is entirely normal to have some processes in **sleeping** mode (*Sleeping threads*) for certain types of programs (Java, MATLAB, commercial software, or complex programs). You also have the program applications executed over time as a parameter.

File system usage metrics for the current job (not for the entire node) include: the number of input/output operations per second (IOPS), and the data transfer rate between the job and the file system over time. These metrics help identify periods of intense activity or low file system utilization.

!!! note "Node Resource Statistics"
    For full node resource statistics, be aware that these may be imprecise if the node is shared among multiple users. Metrics include: the evolution of bandwidth used by the job over time, in relation to software, licences, etc. and the evolution of network bandwidth used by a job or set of jobs via the InfiniBand network over time. This allows observation of periods of massive data transfer (e.g., reading/writing on a file system (Lustre), MPI communication between nodes).

Metrics also show: the evolution of the number of input/output operations per second (IOPS) performed on the local disk over time, and the evolution of local disk bandwidth usage over time, i.e., the amount of data read or written per second.

Local disk space usage is also presented.

Power consumption is also represented.

## CPU Job Page (Job Array)

The CPU job page for a job array is identical to that of a regular CPU job, with the exception of the *Other jobs in the array* section. This section lists other job numbers belonging to the same job array, along with information on their status, name, start time, and end time.

## GPU Job Page

At the top of the page, you have the job name, its number, your username, and the status. Details of your submission script are displayed by clicking on **View job script**. If you launched an interactive job, the submission script is not available.

The directory and submission command are accessible by clicking on **View submission command**.

The next section is reserved for scheduler information. You can access your GPU account page by clicking on your account number.

In the **Resources** section, you can get an initial overview of your job's resource usage by comparing the **Allocated** and **Used** columns for the various listed parameters.

The **CPU** usage metrics allow you to visualize the requested CPU cores over time. You can select/deselect different cores as needed. Note that for very short jobs, this metric is not available.

The **Memory** usage metrics allow you to visualize the requested CPU memory usage over time.

The **Process and threads** metrics allow you to observe different parameters related to processes and execution threads.

File system usage for the current job (not for the entire node) includes: the number of input/output operations per second (IOPS), and the data transfer rate between the job and the file system over time. These metrics help identify periods of intense activity or low file system utilization.

GPU usage metrics include:
*   *Streaming Multiprocessors* (SM) active: indicates the percentage of time the GPU executes a warp (a group of consecutive *threads*) in the last sampling window. This value should ideally be around 80%.
*   *SM occupancy*: defined as the ratio of warps assigned to an SM to the maximum number of warps an SM can handle. A value around 50% is generally expected.
*   *Tensor* parameter: this value should be as high as possible. Ideally, your code should leverage this part of the GPU, optimized for multidimensional matrix multiplications and convolutions.
*   *Floating Point* operations (FP64, FP32, and FP16): you should observe significant activity on only one of these types, depending on the precision used by your code.

GPU memory usage and GPU memory access cycles are also displayed. The latter represents the percentage of cycles during which the device's memory interface is active for sending or receiving data.

The GPU power metric shows the evolution of the GPU's energy consumption (in watts) over time.

GPU bandwidth metrics include: on the PCIe bus (or **PCI Express**, for *Peripheral Component Interconnect Express*), and on the NVLink bus. The NVLink bus is a technology developed by NVIDIA to enable ultra-fast communication between multiple GPUs.

!!! note "Node Resource Statistics"
    For full node resource statistics, be aware that these may be imprecise if the node is shared among multiple users. Metrics include: the evolution of bandwidth used by the job over time, in relation to software, licences, etc. and the evolution of network bandwidth used by a job or set of jobs via the InfiniBand network over time. This allows observation of periods of massive data transfer (e.g., reading/writing on a file system (Lustre), MPI communication between nodes).

Metrics also show: the evolution of the number of input/output operations per second (IOPS) performed on the local disk over time, and the evolution of local disk bandwidth usage over time, i.e., the amount of data read or written per second.

Local disk space usage is also presented.

Power consumption is also represented.

# Account Statistics

The **Account Statistics** section groups your group's usage into two subsections: CPU and GPU.

## CPU Account Statistics

Here you will find the sum of your group's requests for CPU cores, as well as their corresponding usage over the last few months. You can also track the evolution of your priority, which varies based on your usage.

This section shows the most commonly used applications.

Here you can consult the resource usage by each user in your group.

This section shows the evolution over time of wasted CPU cores by each user in the group.

Here you can consult the memory usage by each user in your group.

This section illustrates the memory wasted by each user.

You then have a representation of your file system activity. This includes the number of disk write commands you have performed (input/output operations per second (IOPS)) and the amount of data transferred to the servers over a given period (Bandwidth).

You have a list of the last jobs that were performed for the entire group.

## GPU Account Statistics

Here you will find the sum of your group's GPU requests, as well as their corresponding usage over the last few months. You can also track the evolution of your priority, which varies based on your usage.

This section represents the most commonly used applications.

Here you can consult the resource usage by each user in your group.

This section represents the amount of wasted GPU by user over time.

Next, you have the allocated and used CPU cores for your GPU jobs.

This section illustrates the wastage of CPUs in the context of your GPU jobs.

Here you can visualize the memory usage for each user in your group.

This section illustrates the memory wasted by each user.

You then have a representation of your file system activity. This includes the number of disk write commands you have performed (input/output operations per second (IOPS)) and the amount of data transferred to the servers over a given period (Bandwidth).

Here is a list of the last jobs performed at your group level.

# Cloud Statistics

The first table, "Your Instances," presents all virtual machines associated with an account. The "Flavour" column refers to the [type of virtual machine](../cloud/virtual_machine_flavors.md). The "UUID" column corresponds to a unique identifier assigned to each virtual machine.

Subsequently, each virtual machine has its own usage statistics (CPU Cores, Memory, Disk Bandwidth, Disk IOPS, and Network Bandwidth) viewable for the last month, last week, last day, or last hour.