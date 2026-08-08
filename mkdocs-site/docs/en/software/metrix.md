---
title: "Metrix/en"
slug: "metrix"
lang: "en"

source_wiki_title: "Metrix/en"
source_hash: "8b7197dc79af13096107e89921cf3ac4"
last_synced: "2026-08-07T19:46:17.777436+00:00"
last_processed: "2026-08-07T22:45:12.640340+00:00"

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

## Summary

The Metrix portal is a website for Alliance users. It collects information on compute nodes and management servers to interactively generate data, allowing you to track your resource usage (CPUs, GPUs, memory, filesystems) in real time.

| Cluster | Metrix Portal URL |
| :------ | :---------------- |
| Rorqual | [https://metrix.rorqual.alliancecan.ca](https://metrix.rorqual.alliancecan.ca) |
| Narval | [http://metrix.narval.alliancecan.ca](http://metrix.narval.alliancecan.ca) |
| Nibi    | [https://portal.nibi.sharcnet.ca](https://portal.nibi.sharcnet.ca) |
| tamIA   | [https://portail.tamia.ecpia.ca](https://portail.tamia.ecpia.ca) |
| Vulcan  | [http://metrix.vulcan.alliancecan.ca](http://metrix.vulcan.alliancecan.ca) |

**Filesystem performance**

This section provides graphs for bandwidths and metadata operations, with viewing options for the last week, last day, and last hour.

**Login nodes**

Under this tab, usage statistics for CPUs, memory, system load, and network are presented, with viewing options for the last week, last day, and last hour.

**Scheduler**

This tab shows statistics for the cluster's allocated cores and GPUs, with viewing options for the last week, last day, and last hour.

**Scientific software**

This section presents graphs showing the most frequently used software, along with CPU core and GPU usage.

**Data transfer nodes**

Bandwidth statistics for data transfer nodes are shown under this tab.

## User portal

Under this tab, you can find your quotas for the filesystems, followed by your 10 most recent jobs. You can select a job by its number to see the details. Additionally, by clicking on `(More details)`, you are redirected to the *Job statistics* tab, where all your jobs are listed.

## Job statistics

The first block shows your current usage (CPU cores, memory, and GPUs). These statistics represent the average usage by all currently running jobs. This allows you to easily compare the resources allocated to you with those you actually use.

The interface then provides a graph showing average usage over the last few days.

It also presents your activity on the filesystems, including the number of disk write commands you have performed (input/output operations per second or IOPS) and the amount of data transferred to the servers over a given period (Bandwidth).

This section lists all your jobs—those you have already started, which are currently running, or pending. You can filter jobs by their status (e.g., OOM, completed, running) and search by job ID or job name. Navigation options allow you to quickly move between pages.

### CPU jobs

At the top, you can see the job name, its number, your username, and its status. Details of your submission script are displayed by clicking the `Show submitted job script` button. If the job was launched in interactive mode, the submission script will not be available.

The working directory and the submission command can be seen by clicking the `Show submit command` button.

The next section shows information on the scheduler. To display information on your CPU account, click on your account number within this section.

In the **Resources** section, you can compare the **Allocated** and **Used** columns for various parameters to see the resources consumed by your job.

The **CPU** graph tracks the CPU cores requested by your job over time. You can select specific cores to view.

!!! note
    This graph is not available for very short jobs.

The memory usage graph illustrates the consumption of requested memory over time.

The **Processes and threads** graph displays various parameters. For a multithreaded job, the sum of `Running threads` and `Sleeping threads` should ideally not exceed twice the number of requested cores. However, the presence of `Sleeping threads` is normal for certain types of programs (e.g., Java, MATLAB, commercial software, or complex applications). This graph also includes a parameter showing program applications executed over time.

Filesystem usage for the current job (not the entire node) is presented. This includes graphs for the number of I/O operations per second (IOPS) and the data transfer rate between the job and the filesystem over time, helping to identify periods of high or low filesystem activity.

!!! warning
    Resource statistics for the entire node may be inaccurate if the node is shared by multiple users.
The interface provides insights into node-wide resource usage, including the evolution of job bandwidth over time (in relation to factors like software and licenses), and network bandwidth usage by a job or set of jobs via the Infiniband network. This allows observation of periods of massive data transfer (e.g., reading/writing on a Lustre filesystem, MPI communication between nodes).

Local disk performance metrics are displayed, showing the evolution of input/output operations per second (IOPS) and the bandwidth (amount of data read or written per second) over time.

Usage of local disk space.

Power consumption.

### CPU jobs (job arrays)

The interface for a CPU job within an array is identical to that of a regular CPU job, with the addition of an **Other jobs in the array** section. This section lists other job numbers belonging to the same job array, along with their status, name, start time, and finish time.

### GPU jobs

At the top, you can see the job name, its number, your username, and its status. Details of your submission script are displayed by clicking the `Show submitted job script` button. If the job was launched in interactive mode, the submission script will not be available.

The working directory and submission command are shown by clicking the `Show submit command` button.

The next section shows information on the scheduler. To display information on your GPU account, click on your account number within this section.

In the **Resources** section, you can compare the **Allocated** and **Used** columns for various parameters to see the resources consumed by your job.

The **CPU** graph tracks the CPU cores requested by your job over time. You can select specific cores to view.

!!! note
    This graph is not available for very short jobs.

The memory usage graph illustrates the consumption of requested memory for CPUs over time.

The **Processes and threads** graph displays various parameters.

Filesystem usage for the current job (not the entire node) is presented. This includes graphs for the number of I/O operations per second (IOPS) and the data transfer rate between the job and the filesystem over time, helping to identify periods of high or low filesystem activity.

The Metrix portal provides detailed GPU usage statistics, including metrics for *Streaming Multiprocessors* (SM), which show the percentage of time a GPU spends executing a warp (a group of consecutive threads) in the last sampling (ideally around 80%). *SM occupancy*, defined as the ratio between the number of warps assigned to an SM and the maximum number of warps an SM can handle, is generally expected to be around 50%. The *Tensor* setting should be as high as possible, as it indicates the use of GPU components optimized for multidimensional matrix operations. Finally, for floating-point operations (FP64, FP32, FP16), significant activity on only one of these should be observed, depending on your code's specified precision.

GPU memory usage is monitored, including the amount of memory consumed by the GPU and the percentage of cycles during which the device's memory interface is active sending or receiving data (GPU memory access cycles).

The GPU's power consumption (in watts) over time is displayed.

GPU bandwidth on the PCIe (Peripheral Component Interconnect Express) bus is also shown.

!!! warning
    Node-wide resource statistics may be inaccurate if the node is shared among multiple users.
However, the interface provides insights into the evolution of job bandwidth over time (in relation to factors like software and licenses), and network bandwidth usage by a job or set of jobs via the Infiniband network. This allows observation of periods of massive data transfer (e.g., reading/writing to a Lustre filesystem, MPI communication between nodes).

Local disk performance metrics are displayed, showing the evolution of input/output operations per second (IOPS) and the bandwidth (amount of data read or written per second) over time.

Usage of local disk space.

Power consumption.

## Account statistics

The *Account Statistics* section is divided into two subsections: CPU and GPU, displaying your group's overall usage.

### CPU accounts

This section presents the total CPU cores requested by your group and their usage over the past few months. Your priority status, which varies based on usage, can also be tracked.

Applications used most frequently are shown.

Resources used by each user in your group are listed here.

The interface provides a graph illustrating the CPU cores wasted by each user over time.

Memory usage by each user in your group is displayed.

The interface also shows a graph illustrating the memory wasted by each user.

Your group's activity on the filesystems is represented by metrics such as the number of disk write commands performed (input/output operations per second (IOPS)) and the amount of data transferred to the servers over a given period (Bandwidth).

A list of the last jobs run by all members of the group is provided.

### GPU accounts

This section displays the total GPU requests for your group and their usage over the past few months. Your priority status, which varies based on usage, can also be tracked.

The interface provides a graph illustrating the most frequently used software.

Resources used by each user in your group are listed here.

A graph illustrates the quantity of GPUs wasted by each user.

CPU resources allocated and used by your GPU jobs are displayed.

A graph illustrates the CPUs wasted by your GPU jobs.

Memory used by each user in your group is displayed.

A graph illustrates the memory wasted by each user.

Your group's activity on the filesystems is represented by metrics such as the number of disk write commands performed (input/output operations per second (IOPS)) and the amount of data transferred to the servers over a given period (Bandwidth).

The last jobs run by your group are listed here.

## Cloud statistics

The *Your Instances* table lists all virtual machines associated with your account. The *Flavor* column indicates the virtual machine type, and the *UUID* column provides a unique identifier for each virtual machine.

Each virtual machine features its own usage statistics, including CPU cores, memory, disk bandwidth, IOPS, and network bandwidth. These statistics can be viewed for various periods, such as the last month, week, day, or hour.