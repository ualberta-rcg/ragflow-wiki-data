---
title: "Metrix/en"
slug: "metrix"
lang: "en"

source_wiki_title: "Metrix/en"
source_hash: "114e61c709829994ea396868db8d45d1"
last_synced: "2026-09-20T00:48:35.777859+00:00"
last_processed: "2026-09-20T01:46:18.819796+00:00"

tags:
  []

keywords:
  - "scheduler information"
  - "Allocated"
  - "Ressources"
  - "bandwidth"
  - "submission command"
  - "disk write commands"
  - "Allocated and Used"
  - "short jobs"
  - "GPU"
  - "filesystem performance"
  - "CPU gaspillé"
  - "resource usage"
  - "memory wasted"
  - "instances virtuelles"
  - "CPU graph"
  - "IOPS"
  - "memory usage"
  - "mémoire gaspillée"
  - "GPU usage"
  - "CPU cores"
  - "Processes and threads"
  - "utilisation GPU"
  - "memory used"
  - "CPU account"
  - "Metrix portal"
  - "Show submit command"
  - "working directory"
  - "Used"
  - "SM occupancy"

questions:
  - "What resource usage metrics (e.g., CPUs, GPUs, memory, filesystem bandwidth) does the Metrix portal display, and what time‑range options (last hour, day, week) are available for each tab?"
  - "How can a user view detailed information about their own jobs—including quotas, recent job list, submission script, and real‑time resource consumption—through the User portal and Job statistics sections?"
  - "Which Alliance clusters are linked to the Metrix portal, and what specific URLs are provided for accessing their respective Metrix instances?"
  - "How can you view the working directory and the submission command in the interface?"
  - "Where can you find information about the scheduler in the system?"
  - "What action should you take to display details of your CPU account?"
  - "How can you compare the “Allocated” and “Used” columns in the **Ressources** section to assess a job’s resource consumption?"
  - "What information do the CPU, memory, and “Processes and threads” graphs provide, and what limits or normal behaviors should you watch for when interpreting them?"
  - "How do the filesystem, network, and local‑disk graphs help identify periods of high or low activity, and what specific metrics (e.g., IOPS, bandwidth) should you examine?"
  - "Quels indicateurs permettent d’évaluer l’efficacité d’utilisation du GPU selon le texte, et quelles valeurs cibles sont recommandées pour chaque indicateur ?"
  - "Comment les graphiques relatifs au système de fichiers, au disque local et à la bande passante réseau aident‑ils à identifier les périodes d’activité intense ou faible ?"
  - "Quelles informations sont présentées dans la section « Account Statistics », et comment ces statistiques permettent‑elles de suivre l’usage des ressources CPU et GPU par groupe et par utilisateur ?"
  - "What is the difference between the “Allocated” and “Used” columns in the resources section, and how can you compare them?"
  - "How does the CPU graph display the requested CPU cores over time, and what limitation does it have for very short jobs?"
  - "What does the memory usage graph illustrate regarding the memory requested for CPUs, and how is this information presented over time?"
  - "Comment le tableau « Your Instances » permet‑il de suivre les ressources (CPU, mémoire, bande passante, IOPS) de chaque machine virtuelle ?"
  - "Quels indicateurs sont présentés pour analyser l’utilisation et le gaspillage des GPU, du CPU et de la mémoire au sein d’un groupe ?"
  - "Où peut‑on consulter les dernières tâches exécutées par les membres du groupe ainsi que les statistiques d’IOPS et de bande passante du système de fichiers ?"
  - "What does the first graph illustrate about the memory used by each user in your group?"
  - "How does the second graph depict the memory wasted by each user?"
  - "What two metrics are shown in the filesystem activity representation, and what do they measure?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

<span id="apercu"></span>
# Summary

The Metrix portal is a website for Alliance users. It collects information on compute nodes and management servers to interactively generate data, allowing you to track your resource usage (CPUs, GPUs, memory, filesystems) in real time.

| Cluster | URL |
| :------ | :-- |
| Rorqual | [https://metrix.rorqual.alliancecan.ca](https://metrix.rorqual.alliancecan.ca) |
| Narval  | [http://metrix.narval.alliancecan.ca](http://metrix.narval.alliancecan.ca) |
| Nibi    | [https://portal.nibi.sharcnet.ca](https://portal.nibi.sharcnet.ca) |
| tamIA   | [https://portail.tamia.ecpia.ca](https://portail.tamia.ecpia.ca) |
| Vulcan  | [http://metrix.vulcan.alliancecan.ca](http://metrix.vulcan.alliancecan.ca) |

**Filesystem performance**

This section provides graphs for bandwidths and metadata operations, with viewing options for the last week, last day, and last hour.

**Login nodes**

Under this tab, usage statistics for CPUs, memory, system load, and network are presented, with viewing options for the last week, last day, and last hour.

**Scheduler**

This tab displays statistics for the cluster's allocated cores and GPUs, with viewing options for the last week, last day, and last hour.

**Scientific software**

Graphs in this section show the most frequently used software, including CPU cores and GPUs.

**Data transfer nodes**

Bandwidth statistics for data transfer nodes are displayed under this tab.

# User portal
Under this tab, you will find your quotas for the filesystems, followed by your 10 most recent jobs. You can select a job by its number to see the details. Additionally, by clicking on (More details), you are redirected to the *Job statistics* tab, where all your jobs are listed.

# Job statistics
The first block shows your current usage (CPU cores, memory, and GPUs). These statistics represent the average usage by all currently running jobs. You can easily compare the resources allocated to you with those you actually use.

You then have access to a graph showing the average usage for the last few days.

Next, a representation of your activity on the filesystems is available. This includes the number of disk write commands you have performed (input/output operations per second, or IOPS) and the amount of data transferred to the servers over a given period (Bandwidth).

The next section shows all the jobs you have already started, which are currently running or pending. In the top left corner, you can filter jobs by their status (OOM, completed, running, etc.). In the top right corner, you can search by job ID or by job name. Finally, in the bottom right corner, there is an option to quickly navigate between pages by performing multiple jumps.

## CPU jobs
At the top of the section, you will find the job name, its number, your username, and its current status. Details of your submission script are displayed by clicking on **Show submitted job script**. Note that if the job was launched in interactive mode, the submission script will not be available.

The working directory and the submission command can be seen by clicking on **Show submit command**.

The next section provides information on the scheduler. To display details about your CPU account, click on your account number.

In the **Ressources** section, you can see the resources used by your job by comparing columns **Allocated** and **Used** for the listed parameters.

The **CPU** graph illustrates the CPU cores you have requested, over time. You can select specific cores to view within the graph.

!!! note "Short Job Data"
    This graph is not available for very short jobs.

A graph shows the usage of the memory you requested, over time.

The **Processes and threads** graph displays various parameters. For a multithreaded job, the sum of **Running threads** and **Sleeping threads** should not exceed twice the number of cores requested. It is normal, however, to observe some *Sleeping threads* for certain program types (e.g., Java, Matlab, commercial software, or complex programs). The graph also includes a parameter for program applications that have been executed over time.

Graphs illustrating filesystem usage by the current job (not the entire node) are provided. One shows the number of I/O operations per second (IOPS), while another illustrates the data transfer rate between the job and the filesystem over time, helping to identify periods of high or low filesystem activity.

!!! warning "Shared Node Accuracy"
    Resource statistics for the entire node may be inaccurate if the node is shared by multiple users.

Separate graphs show: (1) the evolution of the bandwidth used by the job over time, relating to factors like software and licenses; and (2) the evolution of network bandwidth used by a job or set of jobs via the Infiniband network, over time. Periods of massive data transfer (e.g., reading/writing on a Lustre filesystem, MPI communication between nodes) can be observed.

Graphs are provided illustrating the evolution of input/output operations per second (IOPS) performed on the local disk over time, and the evolution of local disk bandwidth usage over time (i.e., the amount of data read or written per second).

Usage of local disk space.

Power consumption.

<span id="page-d-une-tache-cpu-vecteur-de-taches-job-array"></span>
## CPU jobs (job arrays)

The page for a CPU job in an array is the same as that for a regular CPU job, except for the **Other jobs in the array** section. The table lists the other job numbers that are part of the job array, along with information about their status, name, start time, and finish time.

<span id="page-d-une-tache-gpu"></span>
## GPU jobs

At the top of the section, you will find the job name, its number, your username, and its current status. Details of your submission script are displayed by clicking on **Show submitted job script**. Note that if the job was launched in interactive mode, the submission script will not be available.

The working directory and the submission command are shown by clicking on **Show submit command**.

The next section provides information on the scheduler. To display details about your GPU account, click on your account number.

In the **Ressources** section, you can see the resources used by your job by comparing columns **Allocated** and **Used** for the listed parameters.

The **CPU** graph illustrates the CPU cores you have requested, over time. You can select specific cores to view within the graph.

!!! note "Short Job Data"
    This graph is not available for very short jobs.

A graph shows the usage of the memory you requested for CPUs, over time.

The **Processes and threads** graph displays various parameters.

Graphs illustrating filesystem usage by the current job (not the entire node) are provided. One shows the number of I/O operations per second (IOPS), while another illustrates the data transfer rate between the job and the filesystem over time, helping to identify periods of high or low filesystem activity.

The GPU usage display includes several metrics. The *Streaming Multiprocessors* (SM) setting indicates the percentage of time taken by the GPU to execute a warp (a group of consecutive threads) in the last sampling; this value should ideally be around 80%. For *SM occupancy* (defined as the ratio between the number of warps assigned to an SM and the maximum number of warps an SM can handle), a value around 50% is generally expected. Regarding the *Tensor* setting, the value should be as high as possible; ideally, your code should leverage this GPU component, which is optimized for multiplications and convolutions of multidimensional matrices. Finally, for FP64, FP32, and FP16 floating-point operations, you should observe significant activity on only one of these, depending on the precision specified by your code.

Two graphs are available for GPU memory: one showing memory usage by the GPU, and another displaying the GPU's memory access cycles, indicating the percentage of cycles during which the device's memory interface is actively sending or receiving data.

A graph displays the evolution of the GPU's power consumption (in watts) over time.

A graph shows the GPU bandwidth on the PCIe bus (Peripheral Component Interconnect Express).

!!! warning "Shared Node Accuracy"
    For statistics on the resources of the entire node, please note that they may be inaccurate if the node is shared among multiple users.

Separate graphs show: (1) the evolution of the bandwidth used by the job over time, relating to factors like software and licenses; and (2) the evolution of network bandwidth used by a job or set of jobs via the Infiniband network, over time. Periods of massive data transfer (e.g., reading/writing to a Lustre filesystem, MPI communication between nodes) can be observed.

Graphs are provided illustrating the evolution of input/output operations per second (IOPS) performed on the local disk over time, and the evolution of local disk bandwidth usage over time (i.e., the amount of data read or written per second).

Usage of local disk space.

Power consumption.

<span id="statistiques-d-un-compte"></span>
# Account statistics

The **Account Statistics** section presents your group's usage, divided into two subsections: CPU and GPU.

<span id="statistiques-d-un-compte-cpu"></span>
## CPU accounts

This section provides the total number of CPU cores requested by your group, along with their corresponding usage over the past few months. You can also track your priority status, which varies based on your usage.

Applications used most frequently.

Details on the resources used by each user in your group are provided.

A graph illustrates the CPU cores wasted by each user over time.

Memory usage by each user in your group is displayed.

A graph shows the memory wasted by each user.

A representation of your activity on the filesystems is provided, including the number of disk write commands you have performed (input/output operations per second, or IOPS) and the amount of data transferred to the servers over a given period (Bandwidth).

A list of the last jobs run by all members of the group is available.

<span id="statistiques-d-un-compte-gpu"></span>
## GPU accounts

This section displays the total GPU requests for your group, along with their usage over the past few months. You can also track your priority, which varies based on your usage.

A graph shows the most frequently used software.

Resources used by each user in your group are displayed.

A graph shows the quantity of GPUs wasted by each user.

CPU resources allocated and used by your GPU jobs are displayed.

A graph shows the CPUs wasted by your GPU jobs.

Memory used by each user in your group is displayed.

A graph shows the memory wasted by each user.

A representation of your activity on the filesystems is provided, including the number of disk write commands you have performed (input/output operations per second, or IOPS) and the amount of data transferred to the servers over a given period (Bandwidth).

A list of the last jobs run by your group is available.

<span id="statistiques-du-cloud"></span>
# Cloud statistics

The **Your Instances** table displays all virtual machines associated with your account. The **Flavor** column refers to the virtual machine type, and the **UUID** column is a unique identifier assigned to each virtual machine.

Each virtual machine has its own usage statistics (CPU cores, memory, disk bandwidth, IOPS, and network bandwidth) that can be viewed for the last month, week, day, or hour.

A graph shows CPU core usage.

Memory usage is displayed.

Disk bandwidth is displayed.

Disk IOPS are displayed.

Network bandwidth is displayed.