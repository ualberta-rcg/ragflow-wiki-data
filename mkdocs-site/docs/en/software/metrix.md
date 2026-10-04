---
title: "Metrix/en"
slug: "metrix"
lang: "en"

source_wiki_title: "Metrix/en"
source_hash: "498ec46bf8318a18c9527fe48d004fb7"
last_synced: "2026-10-04T02:27:33.201522+00:00"
last_processed: "2026-10-04T03:12:02.641030+00:00"

tags:
  []

keywords:
  - "planificateur"
  - "memory usage"
  - "CPU graph"
  - "commande de soumission"
  - "compte CPU"
  - "resource usage tracking"
  - "SM occupancy"
  - "Allocated"
  - "afficher la commande"
  - "Mémoire gaspillée"
  - "CPU cores"
  - "resource graph"
  - "Ressources"
  - "filesystem performance"
  - "mémoire"
  - "CPU"
  - "GPU usage"
  - "CPU and GPU statistics"
  - "Processes and threads"
  - "job statistics"
  - "répertoire de travail"
  - "CPU gaspillé"
  - "Allocated and Used"
  - "IOPS"
  - "Bandwidth"
  - "Used"
  - "Metrix portal"
  - "utilisation"
  - "GPU"
  - "utilisation mémoire par utilisateur"
  - "bandwidth"

questions:
  - "What resource usage metrics (e.g., CPUs, GPUs, memory, filesystems) does the Metrix portal display, and what time‑range options (last hour, day, week) are available for each metric?"
  - "How can a user view detailed information about their jobs—including quotas, recent job list, submission script, and real‑time usage—through the User portal and Job statistics tabs?"
  - "Which Alliance compute clusters are supported by the Metrix portal, and what are the corresponding URLs to access their respective Metrix instances?"
  - "Quel élément s’affiche lorsque l’on clique sur le bouton « Show submit command » ?"
  - "Comment accéder aux informations relatives à votre compte CPU dans l’ordonnanceur ?"
  - "Où se trouve l’indication du répertoire de travail dans l’interface présentée ?"
  - "How can you compare the allocated and used resources for a job in the “Ressources” section?"
  - "What do the CPU, memory, and processes‑and‑threads graphs display, and what limitations or normal behaviors should you be aware of when interpreting them?"
  - "How do the filesystem, node‑wide, and local‑disk graphs help identify periods of high I/O or network activity, and what factors can affect the accuracy of these statistics?"
  - "What do the SM occupancy and Tensor metrics indicate about GPU utilization, and what are the typical target values for these parameters?"
  - "How can the various filesystem and I/O graphs (IOPS, bandwidth, local disk usage) help identify performance bottlenecks during a job’s execution?"
  - "Which information is provided in the “Account Statistics” section for CPU and GPU usage, and how can it be used to monitor group resource consumption and efficiency?"
  - "What is the difference between the “Allocated” and “Used” columns in the resources section, and how can you compare them?"
  - "How does the CPU graph display the requested CPU cores over time, and what limitation does it have for short jobs?"
  - "What information does the memory usage graph provide regarding the memory requested for CPUs?"
  - "Quels indicateurs sont présentés pour suivre l’utilisation des GPU (requêtes totales, usage mensuel, priorité, logiciels les plus utilisés, ressources consommées et gaspillées) au sein de mon groupe ?"
  - "Comment les statistiques d’utilisation du CPU, de la mémoire, du disque (IOPS) et de la bande passante sont‑elles affichées pour les jobs GPU et pour chaque machine virtuelle du cloud ?"
  - "Où puis‑je consulter la liste des dernières tâches exécutées par mon groupe ainsi que le tableau récapitulatif de mes instances cloud (type, UUID et métriques d’utilisation) ?"
  - "What does the first graph illustrate about the memory usage of each user in your group?"
  - "How does the second graph depict the amount of memory wasted by each user?"
  - "What do the left‑hand and right‑hand graphs represent regarding filesystem activity (IOPS and bandwidth) over a given period?"

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

| Cluster | URL |
| :------ | :--------------------------------------- |
| Rorqual | [https://metrix.rorqual.alliancecan.ca](https://metrix.rorqual.alliancecan.ca) |
| Narval  | [http://metrix.narval.alliancecan.ca](http://metrix.narval.alliancecan.ca) |
| Nibi    | [https://portal.nibi.sharcnet.ca](https://portal.nibi.sharcnet.ca) |
| tamIA   | [https://portail.tamia.ecpia.ca](https://portail.tamia.ecpia.ca) |
| Vulcan  | [http://metrix.vulcan.alliancecan.ca](http://metrix.vulcan.alliancecan.ca) |

**Filesystem performance**

This section presents data for bandwidths and metadata operations, with viewing options for the last week, last day, and last hour.

**Login nodes**

This tab displays usage statistics for CPUs, memory, system load, and network, with viewing options for the last week, last day, and last hour.

**Scheduler**

This tab shows statistics for the cluster's allocated cores and GPUs, with viewing options for the last week, last day, and last hour.

**Scientific software**

These sections show the software most frequently used, alongside statistics for CPU cores and GPUs.

**Data transfer nodes**

Bandwidth statistics for data transfer nodes are shown under this tab.

## User portal

Under this tab, you find your quotas for the filesystems, followed by your 10 most recent jobs. You can select a job by its number to see the details. Also, by clicking on (More details), you are redirected to the *Job statistics* tab, where all your jobs are listed.

## Job statistics

Your current usage of CPU cores, memory, and GPUs is displayed. These statistics represent the average usage by all currently running jobs. You can easily compare the resources allocated to you with those you actually use.

The system also provides an average usage over the last few days.

A representation of your activity on the filesystems is shown. This includes the number of disk write commands you have performed (*input/output operations per second (IOPS)*), and the amount of data transferred to the servers over a given period (*Bandwidth*).

The next section shows all the jobs you have already started, which are currently running or pending. In the top left corner, you can filter jobs by their status (OOM, completed, running, etc.). In the top right corner, you can search by job ID or by job name. Finally, there is an option to quickly navigate between pages by performing multiple jumps.

### CPU jobs

At the top, you see the job name, its number, your username, and the status. Details of your submission script are displayed by clicking on **Show submitted job script**. If the job was launched in interactive mode, the submission script will not be available.

The working directory and the submission command can be seen by clicking on **Show submit command**.

The next section shows information on the scheduler. To display the information on your CPU account, click on your account number.

In the **Ressources** section, you can see the resources used by your job by comparing columns **Allocated** and **Used** for the listed parameters.

The **CPU** graph shows the CPU cores you have requested, over time. On the right, you can select the cores you want to see. Please note that this graph is not available for very short jobs.

This section provides details on the usage of the memory you requested, over time.

The **Processes and threads** graph shows different parameters. For a multithread job, adding parameters *Running threads* and *Sleeping threads* should not exceed twice the number of cores requested. However, having some *Sleeping threads* is normal for certain types of programs (Java, Matlab, commercial software or complex programs). There is also a parameter for the program applications that have been executed over time.

Details on filesystem usage by the current job (not for the entire node) are provided. This includes the number of I/O operations per second (IOPS), and the data transfer rate between the job and the filesystem over time. This helps identify periods of high or low filesystem activity.

Resource statistics for the entire node may be inaccurate if the node is shared by multiple users. The display includes the evolution of the bandwidth used by the job over time, in relation to software, licenses, etc., and the evolution of the network bandwidth used by a job or a set of jobs via the Infiniband network, over time. Periods of massive data transfer can be observed (e.g., reading/writing on a filesystem (Lustre), MPI communication between nodes).

Information on local disk performance includes the evolution of the number of input/output operations per second (IOPS) performed on the local disk over time, and the evolution of the bandwidth used on the local disk over time (the amount of data read or written per second).

Usage of local disk space is also displayed.

Power consumption is available.

### CPU jobs (job arrays)

The page for a CPU job in an array is the same as that for a regular CPU job, except for the **Other jobs in the array** section. The table lists the other job numbers that are part of the job array, along with information about their status, name, start time, and finish time.

### GPU jobs

At the top, you see the job name, its number, your username, and the status. Details of your submission script are displayed by clicking on **Show submitted job script**. If the job was launched in interactive mode, the submission script will not be available.

The working directory and the submission command are shown by clicking on **Show submit command**.

The next section shows information on the scheduler. To display the information on your GPU account, click on your account number.

In the **Ressources** section, you can see the resources used by your job by comparing columns **Allocated** and **Used** for the listed parameters.

The **CPU** graph shows the CPU cores you have requested, over time. On the right, you can select the cores you want to see. Please note that this graph is not available for very short jobs.

This section shows the usage of the memory you requested for CPUs, over time.

The **Processes and threads** graph shows different parameters.

Details on filesystem usage by the current job (not for the entire node) are provided. This includes the number of I/O operations per second (IOPS), and the data transfer rate between the job and the filesystem over time. This helps identify periods of high or low filesystem activity.

**GPU** usage information includes:
- The *Streaming Multiprocessors* (SM) setting, indicating the percentage of time taken by the GPU to execute a warp (a group of consecutive threads) in the last sampling. This value should be around 80%.
- *SM occupancy*, defined as the ratio between the number of warps assigned to an SM and the maximum number of warps an SM can handle. A value around 50% is generally expected.
- The *Tensor* setting, where the value should be as high as possible. Ideally, your code should use this part of the GPU, which is optimized for multiplications and convolutions of multidimensional matrices.
- FP64, FP32, and FP16 floating-point operations, where you should observe significant activity on only one of these, depending on the precision specified by your code.

A graph shows the memory used by the GPU. Another graph illustrates the GPU's memory access cycles, showing the percentage of cycles during which the device's memory interface is active sending or receiving data.

The GPU power graph displays the evolution of the GPU's power consumption (in watts), over time.

This section shows the GPU bandwidth on the PCIe bus (or PCI Express, for Peripheral Component Interconnect Express).

For statistics on the resources of the entire node, please note that they may be inaccurate if the node is shared among multiple users. This includes the evolution of the bandwidth used by the job, over time, in relation to software, licenses, etc. It also covers the evolution of the network bandwidth used by a job or set of jobs via the Infiniband network, over time. Periods of massive data transfer can be observed (e.g., reading/writing to a filesystem (Lustre), MPI communication between nodes).

Information on local disk performance includes the evolution of the number of input/output operations per second (IOPS) performed on the local disk over time, and the evolution of the bandwidth used on the local disk over time; that is, the amount of data read or written per second.

Usage of local disk space is also displayed.

Power consumption is available.

## Account statistics

The *Account Statistics* section shows your group's usage in two subsections: CPU and GPU.

### CPU accounts

Here you have the total number of CPU cores requested by your group, along with their corresponding usage over the past few months. You can also track your priority status, which varies based on your usage.

Applications used most frequently are listed.

Here are the resources used by each user in your group.

This section shows the CPU cores wasted by each user, over time.

Here you see the memory used by each user in your group.

This section shows the memory wasted by each user.

A representation of your activity on the filesystems is provided. This includes the number of disk write commands you have performed (*input/output operations per second (IOPS)*), and the amount of data transferred to the servers over a given period (*Bandwidth*).

This lists the last jobs run by all members of the group.

### GPU accounts

Here you can see the total GPU requests for your group, along with their usage over the past few months. You can also track your priority, which varies based on your usage.

This section shows the software more frequently used.

Here you see the resources used by each user in your group.

This section shows the quantity of GPUs wasted by each user.

Here you see the CPU allocated and used by your GPU jobs.

This section shows the CPUs wasted by your GPU jobs.

Here you see the memory used by each user in your group.

This section shows the memory wasted by each user.

A representation of your activity on the filesystems is provided. This includes the number of disk write commands you have performed (*input/output operations per second (IOPS)*), and the amount of data transferred to the servers over a given period (*Bandwidth*).

Here you see the last jobs that were run by your group.

## Cloud statistics

The *Your Instances* table displays all the virtual machines associated with your account. The *Flavor* column refers to the virtual machine type. The *UUID* column is a unique identifier assigned to each virtual machine.

Each virtual machine has its own usage statistics (CPU cores, memory, disk bandwidth, IOPS, and network bandwidth) that can be shown for the last month, week, day or hour.