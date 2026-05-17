---
title: "Metrix/en-ca"
slug: "metrix_en-ca"
lang: "base"

source_wiki_title: "Metrix/en-ca"
source_hash: "972b19619bca87043c08a05de5932a03"
last_synced: "2026-05-17T14:59:09.465984+00:00"
last_processed: "2026-05-17T15:34:36.787601+00:00"

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
  qa_generated: true
---

# Overview

The Metrix portal is a website for Alliance users. It leverages information collected from compute nodes and management servers to interactively generate data, allowing users to track their real-time resource usage (CPU, GPU, memory, file system).

| | |
|---|---|
| Rorqual | [https://metrix.rorqual.alliancecan.ca](https://metrix.rorqual.alliancecan.ca) |
| Narval | [https://portail.narval.calculquebec.ca](https://portail.narval.calculquebec.ca) |
| Nibi | [https://portal.nibi.sharcnet.ca](https://portal.nibi.sharcnet.ca) |

**Filesystem Performance**
This section presents graphs of bandwidth and metadata operations, with visualization options for the last week, last day, and last hour.

**Login Nodes**
CPU, memory, system load, and network usage statistics are presented in this tab, with visualization options for the last week, last day, and last hour.

**Scheduling**
This tab presents statistics on allocated CPU cores and GPUs for the cluster, with visualization options for the last week, last day, and last hour.

**Scientific Software**
The most used software with CPU cores and GPUs are presented in graphical form.

**Data Transfer Nodes**
Bandwidth statistics for data transfer nodes are presented in this tab.

# User Summary

Under the user summary tab, you will find your quotas for the different file systems, followed by your last 10 jobs. You can select a job by its number to access its detailed page. Additionally, by clicking on `(More details)`, you will be redirected directly to the **Job Statistics** tab, where you will find all your jobs.

# Job Statistics

The first block displays your current usage (CPU core, memory, and GPUs). These statistics represent the average resources used by all currently running jobs. You can easily compare the resources allocated to you with those you actually use.

This section provides an average of your resource usage over the last few days.

Next, you have a representation of your activity on the file systems. This includes the number of disk write commands you have performed (*input/output operations per second (IOPS)*), and the amount of data transferred to the servers over a given period (Bandwidth).

The next section presents all the jobs you have launched, which are currently running or pending. You can filter jobs by status (OOM, completed, running, etc.) and search by job number (Job ID) or name. An option also allows you to quickly navigate between pages by making multiple jumps.

## CPU Job Page

At the top of the page, you'll find the job name, its ID, your username, and its status. Details of your submission script are displayed by clicking on `View job script`. If the job was launched in interactive mode, the submission script will not be available.

The working directory and submission command are accessible by clicking on `View submission command`.

The next section is dedicated to scheduler information. You can access your CPU account's tracking page by clicking on your account number.

In the **Resources** section, you can get an initial overview of your job's resource usage by comparing the **Allocated** and **Used** columns for the various listed parameters.

The **CPU** section allows you to visualize the CPU cores you requested over time, with options to select/deselect different cores as needed. Note that for very short jobs, this visualization is not available.

The **Memory** section allows you to visualize the usage of the memory you requested over time.

The **Process and threads** section allows you to observe different parameters related to processes and execution threads. Ideally, for a multithreaded job, the sum of **Running threads** and **Sleeping threads** should not exceed twice the number of requested cores. However, it is quite normal to have some processes in **sleeping** mode (*Sleeping threads*) for certain types of programs (Java, MATLAB, commercial software, or complex programs). You also have the program applications executed over time as a parameter.

The following sections represent file system usage for the current job, not the entire node. They display the number of input/output operations per second (IOPS) and illustrate the data transfer rate between the job and the file system over time. This helps identify periods of intense activity or low file system utilization.

For complete node resource statistics, be aware that these may be imprecise if the node is shared among multiple users. This includes the evolution of bandwidth used by the job over time, in connection with software, licenses, etc., and the evolution of network bandwidth used by a job or set of jobs via the InfiniBand network over time. This can show periods of massive data transfer (e.g., reading/writing to a file system (Lustre), MPI communication between nodes).

This section illustrates the evolution of input/output operations per second (IOPS) performed on the local disk over time, and the evolution of bandwidth used on the local disk over time, i.e., the amount of data read or written per second.

This section shows local disk space usage.

This section shows power consumption.

## CPU Job Page (Job Array)

The page for a CPU job within a job array is identical to that of a regular CPU job, except for the *Other jobs in the array* section. This table lists other job numbers belonging to the same job array, along with information on their status, name, start time, and end time.

## GPU Job Page

At the top of the page, you'll find the job name, its ID, your username, and its status. Details of your submission script are displayed by clicking on `View job script`. If you launched an interactive job, the submission script is not available.

The working directory and submission command are accessible by clicking on `View submission command`.

The next section is reserved for scheduler information. You can access your GPU account page by clicking on your account number.

In the **Resources** section, you can get an initial overview of your job's resource usage by comparing the **Allocated** and **Used** columns for the various listed parameters.

The **CPU** section allows you to visualize the usage of requested CPU cores over time, with options to select/deselect different cores as needed. Note that for very short jobs, this visualization is not available.

The **Memory** section allows you to visualize the usage of memory you requested for the CPUs over time.

The **Process and threads** section allows you to observe different parameters related to processes and execution threads.

The following sections represent file system usage for the current job, not the entire node. They display the number of input/output operations per second (IOPS) and illustrate the data transfer rate between the job and the file system over time. This helps identify periods of intense activity or low file system utilization.

The GPU usage section includes parameters such as *Streaming Multiprocessors* (SM) active (ideally around 80%), *SM occupancy* (around 50% expected), and *Tensor* utilization (as high as possible for optimized matrix operations). For floating-point operations (FP64, FP32, FP16), significant activity should be observed on one type depending on your code's precision.

This section provides information on GPU memory usage and GPU memory access cycles, representing the percentage of cycles during which the device's memory interface is active for sending or receiving data.

This section displays the evolution of GPU energy consumption (in watts) over time.

This section shows the GPU bandwidth on the PCIe bus (or PCI Express, for Peripheral Component Interconnect Express).

For complete node resource statistics, be aware that these may be imprecise if the node is shared among multiple users. This includes the evolution of bandwidth used by the job over time, in connection with software, licenses, etc., and the evolution of network bandwidth used by a job or set of jobs via the InfiniBand network over time. This can show periods of massive data transfer (e.g., reading/writing to a file system (Lustre), MPI communication between nodes).

This section illustrates the evolution of input/output operations per second (IOPS) performed on the local disk over time, and the evolution of bandwidth used on the local disk over time, i.e., the amount of data read or written per second.

This section shows local disk space usage.

This section shows power consumption.

# Account Statistics

The **Account Statistics** section groups your group's usage into two subsections: CPU and GPU.

## CPU Account Statistics

This section presents the sum of your group's CPU core requests, along with their corresponding usage over recent months. You can also track the evolution of your priority, which varies based on your usage.

This section shows the most commonly used applications.

Here, you can view resource usage by each user in your group.

This section shows the evolution over time of wasted CPU cores by each user in the group.

Here, you can view memory usage by each user in your group.

This section represents memory wasted by each user.

Next, you have a representation of your activity on the file systems. This includes the number of disk write commands you have performed (input/output operations per second (IOPS)) and the amount of data transferred to the servers over a given period (Bandwidth).

You have a list of the latest jobs that have been performed for the entire group.

## GPU Account Statistics

This section presents the sum of your group's GPU requests, along with their corresponding usage over recent months. You can also track the evolution of your priority, which varies based on your usage.

This section shows the most commonly used applications.

Here, you can view resource usage by each user in your group.

This section shows the amount of wasted GPU resources per user over time.

Next, you have the CPU cores allocated and used in your GPU jobs.

This section illustrates the wastage of CPUs within your GPU jobs.

Here, you can visualize memory usage for each user in your group.

This section illustrates memory wasted by each user.

Next, you have a representation of your activity on the file systems. This includes the number of disk write commands you have performed (input/output operations per second (IOPS)) and the amount of data transferred to the servers over a given period (Bandwidth).

Here is a list of the latest jobs performed at your group level.

# Cloud Statistics

The first table, 'Your Instances', presents all virtual machines associated with an account. The 'Flavor' column refers to the [virtual machine type](../cloud/virtual_machine_flavors.md). The 'UUID' column corresponds to a unique identifier assigned to each virtual machine.

Each virtual machine then has its own usage statistics (CPU Cores, Memory, Disk Bandwidth, Disk IOPS, and Network Bandwidth) viewable for the last month, last week, last day, or last hour.