---
title: "Metrix/en"
slug: "metrix"
lang: "en"

source_wiki_title: "Metrix/en"
source_hash: "211620716e2db05933598ec2b9ba4676"
last_synced: "2026-05-02T23:50:34.269007+00:00"
last_processed: "2026-05-03T00:43:40.051152+00:00"

tags:
  []

keywords:
  - "Cloud statistics"
  - "Wasted resources"
  - "CPU cores"
  - "GPU accounts"
  - "filesystems"
  - "Memory"
  - "I/O operations per second"
  - "Ressources"
  - "Compute nodes"
  - "Used"
  - "Resource usage"
  - "Resource statistics"
  - "Virtual machines"
  - "Metrix portal"
  - "Account statistics"
  - "jobs"
  - "Filesystem usage"
  - "Processes and threads"
  - "Allocated"
  - "GPU usage"
  - "filesystem usage"
  - "data transfer rate"
  - "CPU and GPU jobs"
  - "CPU graph"
  - "IOPS"
  - "Job statistics"
  - "Memory usage"
  - "filesystem activity"
  - "Bandwidth"
  - "disk write commands"
  - "Filesystem performance"

questions:
  - "What is the primary purpose of the Metrix portal and what general cluster statistics can be monitored through it?"
  - "How does the User portal section help users track their filesystem quotas and recent job history?"
  - "What specific information and resource usage comparisons can be found in the Job statistics section for individual CPU jobs?"
  - "How can a user compare the resources allocated versus the resources actually used by a job?"
  - "What specific information and interactive options does the CPU graph provide?"
  - "Under what circumstances is the CPU graph unavailable for a job?"
  - "How does the expected behavior of running and sleeping threads relate to the number of requested cores in a multithreaded job?"
  - "What specific metrics are used in the graphs to monitor filesystem activity, local disk usage, and network bandwidth?"
  - "How does the monitoring interface differ when viewing details for a CPU job array or a GPU job compared to a standard CPU job?"
  - "What are the ideal target values for Streaming Multiprocessors (SM) usage, SM occupancy, and Tensor settings when analyzing GPU performance?"
  - "How can users monitor the data transfer, network bandwidth, and input/output operations (IOPS) across the shared node and local disks?"
  - "What specific metrics can be tracked in the \"Account Statistics\" section to evaluate resource efficiency, such as wasted CPU cores and memory, among individual users in a group?"
  - "What parameters are illustrated in the \"Processes and threads\" graph?"
  - "How do the filesystem usage graphs distinguish between the activity of the current job and the entire node?"
  - "What specific metrics are displayed on the filesystem graphs to help identify periods of high or low I/O activity?"
  - "What types of resource usage and waste metrics can be monitored for individual users within a GPU account?"
  - "How does the dashboard display filesystem activity, specifically regarding disk write commands and data transfer bandwidth?"
  - "What details and performance statistics are provided for virtual machine instances in the Cloud statistics section?"
  - "What specific metrics are displayed on the left and right graphs regarding filesystem activity?"
  - "Whose recent job executions are tracked and listed in this interface?"
  - "Based on the section anchor, what specific type of account statistics is this documentation covering?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# Summary

The Metrix portal is a website for Alliance users. It collects information on compute nodes and management servers to interactively generate data so you can track your resource usage (CPUs, GPUs, memory, filesystems) in real time.

| Cluster | URL                                          |
| :------ | :------------------------------------------- |
| Rorqual | [https://metrix.rorqual.alliancecan.ca](https://metrix.rorqual.alliancecan.ca) |
| Narval  | [https://portail.narval.calculquebec.ca](https://portail.narval.calculquebec.ca) |
| Nibi    | [https://portal.nibi.sharcnet.ca](https://portal.nibi.sharcnet.ca) |

**Filesystem performance**

Here you have the graphs for bandwidths and metadata operations, along with viewing options (last week, last day and last hour).

**Login nodes**

Under this tab are presented usage statistics for CPUs, memory, system load, and network, with viewing options (last week, last day, and last hour).

**Scheduler**

This tab shows statistics for the cluster's allocated cores and GPUs, with viewing options (last week, last day, and last hour).

**Scientific software**

These graphs show the software most frequently used, with CPU cores and GPUs.

**Data transfer nodes**

Bandwidth statistics for data transfer nodes are shown under this tab.

# User portal

Under this tab, you find your quotas for the filesystems, followed by your 10 last jobs. You can select a job by its number to see the details. Also, by clicking on **(More details)**, you are redirected to the *Job statistics* tab, where all your jobs are listed.

# Job statistics

Current usage statistics are provided, showing your CPU cores, memory, and GPUs. These statistics represent the average usage by all currently running jobs. You can easily compare the resources allocated to you with those you actually use.

Average usage trends for the last few days are available.

Filesystem activity is represented by the number of disk write commands (*input/output operations per second*). Data transfer to the servers (*Bandwidth*) over a given period is also displayed.

A dedicated section lists all your jobs, whether started, running, or pending. In the top left corner, you can filter jobs by their status (OOM, completed, running, etc.). In the top right corner, you can search by job ID or by job name. Finally, in the bottom right corner, there is an option to quickly navigate between pages by performing multiple jumps.

## CPU jobs

Job name, number, your username, and status are displayed. Details of your submission script are displayed by clicking on **Show submitted job script**. If the job was launched in interactive mode, the submission script will not be available.

The working directory and the submission command can be seen by clicking on **Show submit command**.

The next section shows information on the scheduler. To display the information on your CPU account, click on your account number.

In the **Ressources** section, you can see the resources used by your job by comparing columns **Allocated** and **Used** for the listed parameters.

The **CPU** graph shows the CPU cores you have requested, over time. Core selection options are provided. Please note that this graph is not available for very short jobs.

Memory usage over time is displayed.

The **Processes and threads** graph shows different parameters. For a multithread job, adding parameters **Running threads** and **Sleeping threads** should not exceed twice the number of cores requested. However, having some *Sleeping threads* is normal for certain types of programs (java, Matlab, commercial software or complex programs). There is also a parameter for the program applications that have been executed over time.

Filesystem usage by the current job is detailed, showing the number of I/O operations per second (IOPS) and the data transfer rate over time. This helps identify periods of high or low filesystem activity.

Resource statistics for the entire node may be inaccurate if the node is shared by multiple users. Bandwidth usage by the job, including network bandwidth via the Infiniband network, is presented over time. This can indicate periods of massive data transfer (e.g., reading/writing on a filesystem (Lustre), MPI communication between nodes).

The evolution of input/output operations per second (IOPS) on the local disk is shown, alongside the local disk's bandwidth (amount of data read or written per second) over time.

Usage of local disk space

Power consumption

## CPU jobs (job arrays)

The page for a CPU job in an array is the same as that for a regular CPU job, except for the **Other jobs in the array** section. A table lists the other job numbers that are part of the job array, along with information about their status, name, start time, and finish time.

## GPU jobs

Job name, number, your username, and status are displayed. Details of your submission script are displayed by clicking on **Show submitted job script**. If the job was launched in interactive mode, the submission script will not be available.

The working directory and the submission command are shown by clicking on **Show submit command**.

The next section shows information on the scheduler. To display the information on your GPU account, click on your account number.

In the **Ressources** section, you can see the resources used by your job by comparing columns **Allocated** and **Used** for the listed parameters.

The **CPU** graph shows the CPU cores you have requested, over time. Core selection options are provided. Please note that this graph is not available for very short jobs.

CPU memory usage over time is shown.

The **Processes and threads** graph shows different parameters.

Filesystem usage by the current job is detailed, showing the number of I/O operations per second (IOPS) and the data transfer rate over time. This helps identify periods of high or low filesystem activity.

GPU usage statistics are provided, including *Streaming Multiprocessors* (SM) settings, *SM occupancy*, *Tensor* settings, and activity for FP64, FP32, and FP16 floating-point operations. The *Streaming Multiprocessors* (SM) setting indicates the percentage of time taken by the GPU to execute a warp (a group of consecutive threads) in the last sampling. This value should be around 80%. For *SM occupancy* (defined as the ratio between the number of warps assigned to an SM and the maximum number of warps an SM can handle), a value around 50% is generally expected. Regarding the *Tensor* setting, the value should be as high as possible. Ideally, your code should use this part of the GPU, which is optimized for multiplications and convolutions of multidimensional matrices. Finally, for FP64, FP32, and FP16 floating-point operations, you should observe significant activity on only one of these, depending on the precision specified by your code.

GPU memory usage and GPU memory access cycles (percentage of cycles during which the device's memory interface is active sending or receiving data) are displayed.

The evolution of the GPU's power consumption (in watts) over time is displayed.

GPU bandwidth on the PCIe bus (or PCI Express, for Peripheral Component Interconnect Express) is shown.

For statistics on the resources of the entire node, please note that they may be inaccurate if the node is shared among multiple users. Bandwidth usage by the job, including network bandwidth via the Infiniband network, is presented over time. Periods of massive data transfer can be observed (e.g., reading/writing to a filesystem (Lustre), MPI communication between nodes).

The evolution of input/output operations per second (IOPS) on the local disk is shown, alongside the local disk's bandwidth (amount of data read or written per second) over time.

Usage of local disk space

Power consumption

# Account statistics

The *Account Statistics* section shows your group's usage in two subsections: CPU and GPU.

## CPU accounts

Here you have the total number of CPU cores requested by your group, along with their corresponding usage over the past few months. You can also track your priority status, which varies based on your usage.

Applications used most frequently are listed.

Resources used by each user in your group are displayed.

CPU cores wasted by each user over time are tracked.

Memory used by each user in your group is shown.

Memory wasted by each user is displayed.

Filesystem activity is represented by the number of disk write commands (*input/output operations per second (IOPS)*) and the amount of data transferred to the servers (*Bandwidth*) over a given period.

The last jobs run by all members of the group are listed.

## GPU accounts

Here you can see the total GPU requests for your group, along with their usage over the past few months. You can also track your priority, which varies based on your usage.

The most frequently used software is shown.

Resources used by each user in your group are displayed.

The quantity of GPUs wasted by each user is shown.

CPU allocated and used by your GPU jobs are presented.

CPUs wasted by your GPU jobs are tracked.

Memory used by each user in your group is shown.

Memory wasted by each user is displayed.

Filesystem activity is represented by the number of disk write commands (*input/output operations per second (IOPS)*) and the amount of data transferred to the servers (*Bandwidth*) over a given period.

The last jobs run by your group are listed.

# Cloud statistics

The table *Your Instances* displays all the virtual machines associated with your account. The *Flavor* column refers to the virtual machine type. The *UUID* column is a unique identifier assigned to each virtual machine.

Each virtual machine has its own usage statistics (CPU cores, memory, disk bandwidth, IOPS and network bandwidth) that can be shown for the last month, week, day or hour.