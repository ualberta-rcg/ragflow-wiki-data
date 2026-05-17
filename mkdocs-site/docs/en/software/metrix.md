---
title: "Metrix/en"
slug: "metrix"
lang: "en"

source_wiki_title: "Metrix/en"
source_hash: "aa4557e143532d29927d92243a4d74bd"
last_synced: "2026-05-17T14:59:09.465984+00:00"
last_processed: "2026-05-17T15:23:47.307138+00:00"

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

# Summary

The Metrix portal is a website for Alliance users. It collects information on compute nodes and management servers to interactively generate data so you can track your resource usage (CPUs, GPUs, memory, filesystems) in real time.

| Rorqual | [https://metrix.rorqual.alliancecan.ca](https://metrix.rorqual.alliancecan.ca) |
|---|---|
| Narval | [https://portail.narval.calculquebec.ca](https://portail.narval.calculquebec.ca) |
| Nibi | [https://portal.nibi.sharcnet.ca](https://portal.nibi.sharcnet.ca) |

**Filesystem performance**

Here you have the data for bandwidths and metadata operations, along with viewing options (last week, last day and last hour).

**Login nodes**

Under this tab are presented usage statistics for CPUs, memory, system load, and network, with viewing options (last week, last day, and last hour).

**Scheduler**

This tab shows statistics for the cluster's allocated cores and GPUs, with viewing options (last week, last day, and last hour).

**Scientific software**

These sections show the software most frequently used, with CPU cores and GPUs.

**Data transfer nodes**

Bandwidth statistics for data transfer nodes are shown under this tab.

# User portal
Under this tab, you find your quotas for the filesystems, followed by your 10 last jobs. You can select a job by its number to see the details. Also, by clicking on **(More details)**, you are redirected to the *Job statistics* tab, where all your jobs are listed.

# Job statistics
The first block shows your current usage (CPU cores, memory, and GPUs). These statistics represent the average usage by all currently running jobs. You can easily compare the resources allocated to you with those you actually use.

The section also presents an average usage overview for the last few days.

Following this, your activity on the filesystems is presented, detailing the number of disk write commands performed (*input/output operations per second*) and the amount of data transferred to the servers over a given period (*Bandwidth*).

The next section shows all the jobs you have already started, which are currently running or pending. In the top left corner, you can filter jobs by their status (OOM, completed, running, etc.). In the top right corner, you can search by job ID or by job name. Finally, in the bottom right corner, there is an option to quickly navigate between pages by performing multiple jumps.

## CPU jobs
At the top, you see the job name, its number, your username, and the status. Details of your submission script are displayed by clicking on the **Show submitted job script** button. If the job was launched in interactive mode, the submission script will not be available.

The working directory and the submission command can be seen by clicking on the **Show submit command** button.

The next section shows information on the scheduler. To display the information on your CPU account, click on your account number.

In the **Ressources** section, you can see the resources used by your job by comparing columns **Allocated** and **Used** for the listed parameters.

The **CPU** section shows the CPU cores you have requested, over time. You can select specific cores to view. Please note that this data is not available for very short jobs.

Memory usage over time is also displayed, showing the memory you requested.

The **Processes and threads** section shows different parameters. For a multithread job, adding parameters *Running threads* and *Sleeping threads* should not exceed twice the number of cores requested. However, some *Sleeping threads* are normal for certain types of programs (java, Matlab, commercial software, or complex programs). There is also a parameter for the program applications that have been executed over time.

Filesystem usage by the current job (not the entire node) is shown, including the number of I/O operations per second (IOPS) and the data transfer rate between the job and the filesystem over time. This information helps identify periods of high or low filesystem activity.

Resource statistics for the entire node may be inaccurate if the node is shared by multiple users. The data presented includes the evolution of bandwidth used by the job over time (related to software, licences, etc.) and the evolution of network bandwidth used by a job or set of jobs via the Infiniband network over time. Periods of massive data transfer (e.g., reading/writing on a Lustre filesystem, MPI communication between nodes) can be observed.

The evolution of input/output operations per second (IOPS) performed on the local disk and the local disk bandwidth (amount of data read or written per second) over time are also displayed.

Usage of local disk space

Power consumption

## CPU jobs (job arrays)

The display for a CPU job within an array is identical to that for a regular CPU job, with the addition of an **Other jobs in the array** section. This section lists other job numbers belonging to the same array, along with their status, name, start time, and finish time.

## GPU jobs

At the top, you see the job name, its number, your username, and the status. Details of your submission script are displayed by clicking on the **Show submitted job script** button. If the job was launched in interactive mode, the submission script will not be available.

The working directory and the submission command are shown by clicking on the **Show submit command** button.

The next section shows information on the scheduler. To display the information on your GPU account, click on your account number.

In the **Ressources** section, you can see the resources used by your job by comparing columns **Allocated** and **Used** for the listed parameters.

The **CPU** section shows the CPU cores you have requested, over time. You can select specific cores to view. Please note that this data is not available for very short jobs.

Memory usage over time for the requested CPUs is also presented.

The **Processes and threads** section shows different parameters.

Filesystem usage by the current job (not the entire node) is shown, including the number of I/O operations per second (IOPS) and the data transfer rate between the job and the filesystem over time. This information helps identify periods of high or low filesystem activity.

GPU usage information includes the *Streaming Multiprocessors* (SM) setting, which indicates the percentage of time taken by the GPU to execute a warp (a group of consecutive threads) in the last sampling. This value should be around 80%. *SM occupancy* (defined as the ratio between the number of warps assigned to an SM and the maximum number of warps an SM can handle) is generally expected to be around 50%. The *Tensor* setting should be as high as possible; ideally, your code should use this part of the GPU, which is optimized for multiplications and convolutions of multidimensional matrices. Finally, for FP64, FP32, and FP16 floating-point operations, you should observe significant activity on only one of these, depending on the precision specified by your code.

GPU memory usage and GPU memory access cycles (the percentage of cycles during which the device's memory interface is active sending or receiving data) are also displayed.

The evolution of the GPU's power consumption (in watts) over time is also displayed.

GPU bandwidth on the PCIe bus (or PCI Express, for Peripheral Component Interconnect Express) is also shown.

Statistics on the resources of the entire node may be inaccurate if the node is shared among multiple users. This data includes the evolution of bandwidth used by the job over time (related to software, licences, etc.) and the evolution of network bandwidth used by a job or set of jobs via the Infiniband network over time. Periods of massive data transfer (e.g., reading/writing to a Lustre filesystem, MPI communication between nodes) can be observed.

The evolution of input/output operations per second (IOPS) performed on the local disk and the local disk bandwidth (amount of data read or written per second) over time are also displayed.

Usage of local disk space

Power consumption

# Account statistics

The *Account Statistics* section details your group's usage, divided into two subsections: CPU and GPU.

## CPU accounts

This section presents the total number of CPU cores requested by your group and their corresponding usage over the past few months. Your priority status, which varies based on usage, is also tracked.

Applications used most frequently

Resources used by each user within your group are also detailed.

CPU cores wasted by each user over time are presented.

Memory used by each user in your group is also displayed.

Memory wasted by each user is shown.

Your activity on the filesystems is represented, showing the number of disk write commands performed (*input/output operations per second (IOPS)*) and the amount of data transferred to the servers over a given period (*Bandwidth*).

This lists the last jobs run by all members of the group.

## GPU accounts

This section presents the total GPU requests for your group and their usage over the past few months. Your priority, which varies based on usage, is also tracked.

The software most frequently used is also shown.

Resources used by each user in your group are displayed.

The quantity of GPUs wasted by each user is presented.

CPU allocated and used by your GPU jobs are also detailed.

CPUs wasted by your GPU jobs are presented.

Memory used by each user in your group is displayed.

Memory wasted by each user is shown.

Your activity on the filesystems is represented, showing the number of disk write commands performed (*input/output operations per second (IOPS)*) and the amount of data transferred to the servers over a given period (*Bandwidth*).

The last jobs run by your group are also listed.

# Cloud statistics

The table *Your Instances* displays all the virtual machines associated with your account. The *Flavor* column refers to the virtual machine type. The *UUID* column is a unique identifier assigned to each virtual machine.

Each virtual machine features its own usage statistics, including CPU cores, memory, disk bandwidth, IOPS, and network bandwidth, which can be viewed for the last month, week, day, or hour.