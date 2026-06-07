---
title: "Metrix/en"
slug: "metrix"
lang: "en"

source_wiki_title: "Metrix/en"
source_hash: "904c7ad3359cf824b72b759615de14a6"
last_synced: "2026-06-07T00:07:37.701416+00:00"
last_processed: "2026-06-07T00:22:00.059743+00:00"

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

# Summary

The Metrix portal is a website for Alliance users. It collects information on compute nodes and management servers, to interactively generate data so you can track your resource usage (CPUs, GPUs, memory, filesystems) in real time.

| Rorqual | [https://metrix.rorqual.alliancecan.ca](https://metrix.rorqual.alliancecan.ca) |
| :------ | :---------------------------------------------------------------------- |
| Narval  | [https://portail.narval.calculquebec.ca](https://portail.narval.calculquebec.ca) |
| Nibi    | [https://portal.nibi.sharcnet.ca](https://portal.nibi.sharcnet.ca)       |

**Filesystem performance**

Here you have the metrics for bandwidths and metadata operations, along with viewing options (last week, last day, and last hour).

**Login nodes**

Under this tab are presented usage statistics for CPUs, memory, system load, and network, with viewing options (last week, last day, and last hour).

**Scheduler**

This tab shows statistics for the cluster's allocated cores and GPUs, with viewing options (last week, last day, and last hour).

**Scientific software**

These metrics show the software most frequently used, with CPU cores and GPUs.

**Data transfer nodes**

Bandwidth statistics for data transfer nodes are shown under this tab.

# User portal

Under this tab, you find your quotas for the filesystems, followed by your 10 last jobs. You can select a job by its number to see the details. Also, by clicking on **More details**, you are redirected to the *Job statistics* tab, where all your jobs are listed.

# Job statistics

The first block shows your current usage (CPU cores, memory, and GPUs). These statistics represent the average usage by all currently running jobs. You can easily compare the resources allocated to you with those you actually use.

The portal also provides an average usage over the last few days.

Next, your activity on the filesystems is represented, detailing the number of disk write commands performed (input/output operations per second) and the amount of data transferred to the servers over a given period (Bandwidth).

The next section lists all your jobs, including those already started, currently running, or pending. You can filter jobs by their status (OOM, completed, running, etc.) and search by job ID or job name. An option is also available to quickly navigate between pages.

## CPU jobs

The job name, its number, your username, and the status are displayed. Details of your submission script can be viewed by clicking on **Show submitted job script**. If the job was launched in interactive mode, the submission script will not be available.

The working directory and the submission command can be seen by clicking on **Show submit command**.

The next section shows information on the scheduler. To display the information on your CPU account, click on your account number.

In the **Ressources** section, you can review the resources used by your job by comparing the **Allocated** and **Used** columns for the listed parameters.

The CPU usage is shown, detailing the CPU cores you have requested over time. You can select specific cores to view. This information is not available for very short jobs.

Memory usage is displayed, showing the memory you requested over time.

The **Processes and threads** section provides different parameters. For a multithread job, the sum of *Running threads* and *Sleeping threads* should not exceed twice the number of cores requested. However, some *Sleeping threads* are normal for certain types of programs (Java, Matlab, commercial software, or complex programs). The section also includes parameters for program applications that have been executed over time.

Filesystem usage by the current job, rather than the entire node, is detailed. This includes the number of I/O operations per second (IOPS) and the data transfer rate between the job and the filesystem over time. This information helps identify periods of high or low filesystem activity.

Resource statistics for the entire node may be inaccurate if the node is shared by multiple users. The data tracks the evolution of bandwidth used by the job over time, in relation to software, licenses, etc. It also shows the evolution of network bandwidth used by a job or set of jobs via the Infiniband network, over time, allowing observation of periods of massive data transfer (e.g., reading/writing on a filesystem (Lustre), MPI communication between nodes).

The evolution of the number of input/output operations per second (IOPS) performed on the local disk over time is provided. Additionally, the evolution of the bandwidth used on the local disk over time, representing the amount of data read or written per second, is tracked.

Usage of local disk space

Power consumption

## CPU jobs (job arrays)

The display for a CPU job in an array is the same as for a regular CPU job, with the addition of an **Other jobs in the array** section. This section lists other job numbers that are part of the job array, along with their status, name, start time, and finish time.

## GPU jobs

The job name, its number, your username, and the status are displayed. Details of your submission script can be viewed by clicking on **Show submitted job script**. If the job was launched in interactive mode, the submission script will not be available.

The working directory and the submission command are shown by clicking on **Show submit command**.

The next section shows information on the scheduler. To display the information on your GPU account, click on your account number.

In the **Ressources** section, you can review the resources used by your job by comparing the **Allocated** and **Used** columns for the listed parameters.

The CPU usage is shown, detailing the CPU cores you have requested over time. You can select specific cores to view. This information is not available for very short jobs.

The usage of memory requested for CPUs is displayed, over time.

The **Processes and threads** section shows different parameters.

Filesystem usage by the current job, rather than the entire node, is detailed. This includes the number of I/O operations per second (IOPS) and the data transfer rate between the job and the filesystem over time. This information helps identify periods of high or low filesystem activity.

GPU usage is shown, detailing several metrics. The *Streaming Multiprocessors* (SM) setting indicates the percentage of time taken by the GPU to execute a warp (a group of consecutive threads) in the last sampling, ideally around 80%. *SM occupancy*, defined as the ratio between the number of warps assigned to an SM and the maximum number of warps an SM can handle, is generally expected around 50%. The *Tensor* setting should be as high as possible, as it represents the GPU component optimized for multiplications and convolutions of multidimensional matrices. Finally, for FP64, FP32, and FP16 floating-point operations, significant activity should ideally be observed on only one of these, depending on the precision specified by your code.

Memory used by the GPU is tracked. Additionally, the GPU's memory access cycles, indicating the percentage of cycles during which the device's memory interface is active sending or receiving data, are also shown.

The evolution of the GPU's power consumption (in watts) over time is displayed.

GPU bandwidth on the PCIe bus (or PCI Express, for Peripheral Component Interconnect Express) is also shown.

For statistics on the resources of the entire node, please note that they may be inaccurate if the node is shared among multiple users. Data tracks the evolution of bandwidth used by the job over time, in relation to software, licenses, etc. It also shows the evolution of network bandwidth used by a job or set of jobs via the Infiniband network, over time, allowing observation of periods of massive data transfer (e.g., reading/writing to a filesystem (Lustre), MPI communication between nodes).

The evolution of the number of input/output operations per second (IOPS) performed on the local disk over time is provided. Additionally, the evolution of the bandwidth used on the local disk over time, representing the amount of data read or written per second, is tracked.

Usage of local disk space

Power consumption

# Account statistics

The *Account Statistics* section details your group's usage, divided into CPU and GPU subsections.

## CPU accounts

The total number of CPU cores requested by your group, along with their corresponding usage over the past few months, is displayed. You can also track your priority status, which varies based on your usage.

Applications used most frequently

The resources used by each user in your group are listed.

The CPU cores wasted by each user over time are tracked.

The memory used by each user in your group is displayed.

The memory wasted by each user is shown.

Your activity on the filesystems is represented, detailing the number of disk write commands performed (input/output operations per second (IOPS)) and the amount of data transferred to the servers over a given period (Bandwidth).

A list of the last jobs run by all members of the group is available.

## GPU accounts

The total GPU requests for your group, along with their usage over the past few months, are displayed. You can also track your priority, which varies based on your usage.

The software most frequently used is shown.

The resources used by each user in your group are listed.

The quantity of GPUs wasted by each user is tracked.

The CPU allocated and used by your GPU jobs is displayed.

The CPUs wasted by your GPU jobs are tracked.

The memory used by each user in your group is displayed.

The memory wasted by each user is shown.

Your activity on the filesystems is represented, detailing the number of disk write commands performed (input/output operations per second (IOPS)) and the amount of data transferred to the servers over a given period (Bandwidth).

A list of the last jobs run by your group is available.

# Cloud statistics

The *Your Instances* table displays all virtual machines associated with your account. The *Flavor* column refers to the virtual machine type, and the *UUID* column is a unique identifier assigned to each virtual machine.

Each virtual machine has its own usage statistics (CPU cores, memory, disk bandwidth, IOPS, and network bandwidth) that can be shown for the last month, week, day, or hour.