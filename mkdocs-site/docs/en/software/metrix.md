---
title: "Metrix/en"
slug: "metrix"
lang: "en"

source_wiki_title: "Metrix/en"
source_hash: "8ee05649f7cc9c0cdd989fd19c0dae7a"
last_synced: "2026-10-11T01:39:35.690021+00:00"
last_processed: "2026-10-11T02:30:25.458389+00:00"

tags:
  []

keywords:
  - "memory wasted"
  - "job statistics"
  - "requêtes GPU"
  - "filesystem performance"
  - "Show submit command"
  - "requested cores"
  - "SM occupancy"
  - "processes and threads"
  - "allocated vs used resources"
  - "CPU graph"
  - "bandwidth"
  - "Metrix portal"
  - "memory usage"
  - "disk write commands"
  - "CPU cores graph"
  - "memory usage graph"
  - "Allocated vs Used"
  - "memory used"
  - "GPU usage"
  - "power consumption"
  - "mémoire gaspillée"
  - "scheduler statistics"
  - "CPU account"
  - "instances cloud"
  - "short jobs"
  - "resource usage tracking"
  - "utilisation CPU"
  - "comptes GPU"
  - "filesystem IOPS"
  - "Ressources section"
  - "IOPS"
  - "scheduler information"

questions:
  - "What resource usage metrics (e.g., CPUs, GPUs, memory, filesystem bandwidth) are displayed on the Metrix portal, and which time‑range views (last hour, day, week) are available for each category?"
  - "How does the User portal present a user’s quota information and allow comparison between allocated resources and actual usage for their current and recent jobs?"
  - "Where in the Metrix interface can a user access detailed information about a specific job, such as the submitted script, submission command, scheduler account, and allocated versus used resources?"
  - "Comment afficher la commande de soumission dans l’interface ?"
  - "Quelle action permet d’afficher les informations du planificateur pour votre compte CPU ?"
  - "Dans la section « Ressources », comment comparer les colonnes « Allocated » et « Used » pour connaître les ressources utilisées par votre job ?"
  - "How can the “Processes and threads” graph be used to verify that a multithreaded job’s running and sleeping threads stay within the expected limits based on the allocated CPU cores?"
  - "What do the filesystem usage graphs (IOPS and data transfer rate) reveal about a job’s I/O activity, and how can they help identify periods of high or low filesystem usage?"
  - "In the GPU job page, which sections let you compare allocated versus used resources and view the submitted job script or submission command?"
  - "What do the SM usage, SM occupancy, and Tensor metrics represent in the GPU usage graph, and what are the typical target values for each?"
  - "How can the IOPS and bandwidth graphs for the filesystem and local disk be used to identify periods of high or low I/O activity during a job?"
  - "What information is displayed in the “Account Statistics” section for CPU and GPU accounts, and how can it help monitor group resource usage and efficiency?"
  - "What information does the CPU graph provide, and how can you select which cores to display?"
  - "Why is the CPU graph not available for very short jobs?"
  - "What parameters are shown in the memory usage and the “Processes and threads” graphs?"
  - "Quels indicateurs de consommation et de gaspillage (GPU, CPU, mémoire, IOPS, bande passante) sont présentés pour chaque utilisateur du groupe dans la section « GPU accounts » ?"
  - "Comment le tableau « Your Instances » permet‑il de suivre les caractéristiques et les statistiques d’utilisation des machines virtuelles associées à un compte cloud ?"
  - "Où peut‑on consulter la liste des dernières tâches exécutées par le groupe ainsi que les tâches en cours, et quels détails ces vues offrent‑elles ?"
  - "Quels indicateurs le premier graphique présente‑t‑il concernant la mémoire utilisée par chaque utilisateur du groupe ?"
  - "Comment le deuxième graphique illustre‑t‑il la mémoire gaspillée par chaque utilisateur et quelles en sont les implications ?"
  - "Quels deux paramètres d’activité du système de fichiers sont affichés à droite et à gauche, et que mesurent respectivement les IOPS et la bande passante ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# Summary

The Metrix portal is a website for Alliance users. It collects information on compute nodes and management servers to interactively generate data, allowing you to track your resource usage (CPUs, GPUs, memory, filesystems) in real time.

| Cluster | URL |
|---|---|
| Rorqual | [https://metrix.rorqual.alliancecan.ca](https://metrix.rorqual.alliancecan.ca) |
| Narval | [https://metrix.narval.alliancecan.ca](https://metrix.narval.alliancecan.ca) |
| Nibi | [https://portal.nibi.sharcnet.ca](https://portal.nibi.sharcnet.ca) |
| tamIA | [https://portail.tamia.ecpia.ca](https://portail.tamia.ecpia.ca) |
| Vulcan | [https://metrix.vulcan.alliancecan.ca](https://metrix.vulcan.alliancecan.ca) |

*   **Filesystem performance**
    This section provides graphs for bandwidths and metadata operations, with viewing options for the last week, last day, and last hour.

*   **Login nodes**
    Under this tab, usage statistics for CPUs, memory, system load, and network are presented, with viewing options for the last week, last day, and last hour.

*   **Scheduler**
    This tab shows statistics for the cluster's allocated cores and GPUs, with viewing options for the last week, last day, and last hour.

*   **Scientific software**
    These graphs display the most frequently used software, including CPU cores and GPUs.

*   **Data transfer nodes**
    Bandwidth statistics for data transfer nodes are shown under this tab.

## User portal

Under this tab, you find your quotas for the filesystems, followed by your 10 last jobs. You can select a job by its number to see the details. Also, by clicking on (More details), you are redirected to the *Job statistics* tab, where all your jobs are listed.

## Job statistics

The first block shows your current usage (CPU cores, memory, and GPUs). These statistics represent the average usage by all currently running jobs. You can easily compare the resources allocated to you with those you actually use.

An additional graph shows the average usage over the last few days.

The system then displays your activity on the filesystems. This includes the number of disk write commands you have performed (*input/output operations per second* or IOPS) and the amount of data transferred to the servers over a given period (*Bandwidth*).

The next section shows all the jobs you have already started, which are currently running or pending. In the top left corner, you can filter jobs by their status (OOM, completed, running, etc.). In the top right corner, you can search by job ID or by job name. Finally, in the bottom right corner, there is an option to quickly navigate between pages by performing multiple jumps.

### CPU jobs

At the top, you see the job name, its number, your username, and the status. Details of your submission script are displayed by clicking on Show submitted job script. If the job was launched in interactive mode, the submission script will not be available.

The working directory and the submission command can be seen by clicking on Show submit command.

The next section shows information on the scheduler. To display the information on your CPU account, click on your account number.

In the **Ressources** section, you can see the resources used by your job by comparing columns **Allocated** and **Used** for the listed parameters.

A graph illustrates the CPU cores you have requested, over time, allowing selection of specific cores.

!!! note "Short Jobs"
    This graph is not available for very short jobs.

A corresponding graph displays the usage of your requested memory, over time.

The **Processes and threads** graph shows different parameters. For a multithread job, adding parameters **Running threads** and **Sleeping threads** should not exceed twice the number of cores requested. However, having some *Sleeping threads* is normal for certain types of programs (Java, Matlab, commercial software, or complex programs). There is also a parameter for the program applications that have been executed over time.

Charts show filesystem usage by the current job, distinct from overall node usage. These include the number of I/O operations per second (IOPS) and the data transfer rate between the job and the filesystem, over time, to highlight periods of high or low filesystem activity.

Node-wide resource statistics may be inaccurate if the node is shared. The displayed data includes the evolution of job bandwidth over time, relating to software and licenses, and the evolution of network bandwidth used by jobs via the Infiniband network, where periods of massive data transfer (e.g., Lustre filesystem I/O, MPI communication) can be observed.

Further statistics show the evolution of local disk IOPS and local disk bandwidth (data read/written per second) over time.

Information on local disk space usage is also available.

Power consumption data is provided.

### CPU jobs (job arrays)

The page for a CPU job in an array is the same as that for a regular CPU job, except for the **Other jobs in the array** section. The table lists the other job numbers that are part of the job array, along with information about their status, name, start time, and finish time.

### GPU jobs

At the top, you see the job name, its number, your username, and the status. Details of your submission script are displayed by clicking on Show submitted job script. If the job was launched in interactive mode, the submission script will not be available.

The working directory and the submission command are shown by clicking on Show submit command.

The next section shows information on the scheduler. To display the information on your GPU account, click on your account number.

In the **Ressources** section, you can see the resources used by your job by comparing columns **Allocated** and **Used** for the listed parameters.

A graph illustrates the CPU cores you have requested, over time, allowing selection of specific cores.

!!! note "Short Jobs"
    This graph is not available for very short jobs.

A corresponding graph displays the usage of your requested memory for CPUs, over time.

The **Processes and threads** section provides various parameters.

Charts display filesystem usage by the current job, separate from overall node usage. These include the number of I/O operations per second (IOPS) and the data transfer rate between the job and the filesystem, over time, to highlight periods of high or low filesystem activity.

A dedicated section outlines your GPU usage metrics. This includes *Streaming Multiprocessors* (SM) which indicates the percentage of time a GPU executes a warp (ideally around 80%). *SM occupancy*, the ratio of assigned to maximum warps, is generally expected around 50%. The *Tensor* setting should be as high as possible, indicating optimal use of the GPU's tensor cores for matrix operations. For FP64, FP32, and FP16 floating-point operations, significant activity should be observed on only one, based on your code's specified precision.

Details are provided on GPU memory usage and GPU memory access cycles, showing the percentage of cycles the device's memory interface is active sending or receiving data.

A power graph illustrates the GPU's power consumption (in watts) over time.

GPU bandwidth on the PCIe (Peripheral Component Interconnect Express) bus is also presented.

Node-wide resource statistics may be inaccurate if the node is shared. The data includes the evolution of job bandwidth over time, relating to software and licenses, and the evolution of network bandwidth used by jobs via the Infiniband network, where periods of massive data transfer (e.g., Lustre filesystem I/O, MPI communication) can be observed.

Further statistics show the evolution of local disk IOPS and local disk bandwidth (data read/written per second) over time.

Information on local disk space usage is also available.

Power consumption data is provided.

## Account statistics

The *Account Statistics* section shows your group's usage in two subsections: CPU and GPU.

### CPU accounts

This section provides the total number of CPU cores requested by your group and their usage over the past few months, allowing you to track your priority status as it fluctuates with usage.

A summary of the most frequently used applications is available.

Detailed resource usage by each user in your group is displayed.

CPU cores wasted by each user over time are tracked.

Memory usage by each user in your group is presented.

Memory wasted by each user is also reported.

Filesystem activity is represented, including the number of disk write commands (*input/output operations per second (IOPS)*) and the amount of data transferred (*Bandwidth*) over a given period.

This lists the last jobs run by all members of the group.

### GPU accounts

This section presents the total GPU requests for your group and their usage over the past few months, enabling you to track your priority as it changes with usage.

A summary of the most frequently used software is provided.

Detailed resource usage by each user in your group is displayed.

The quantity of GPUs wasted by each user is tracked.

CPU resources allocated and used by your GPU jobs are presented.

CPUs wasted by your GPU jobs are reported.

Memory usage by each user in your group is displayed.

Memory wasted by each user is also reported.

Filesystem activity is represented, including the number of disk write commands (*input/output operations per second (IOPS)*) and the amount of data transferred (*Bandwidth*) over a given period.

Here you see the last jobs that were run by your group.

## Cloud statistics

The table *Your Instances* displays all the virtual machines associated with your account. The *Flavor* column refers to the virtual machine type. The *UUID* column is a unique identifier assigned to each virtual machine.

Each virtual machine has its own usage statistics (CPU cores, memory, disk bandwidth, IOPS, and network bandwidth) that can be shown for the last month, week, day, or hour.