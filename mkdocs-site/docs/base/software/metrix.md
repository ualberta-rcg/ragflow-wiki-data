---
title: "Metrix"
slug: "metrix"
lang: "base"

source_wiki_title: "Metrix"
source_hash: "e8e43566a327bde05a7c499aecb751b2"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:04:34.242494+00:00"

tags:
  []

keywords:
  - "numéro de tâche"
  - "recherche"
  - "Utilisation des ressources"
  - "transfert massif de données"
  - "communication MPI"
  - "Ordonnanceur"
  - "Gaspillage de GPU"
  - "Tensor"
  - "Statistiques du cloud"
  - "utilisation des ressources"
  - "Statistiques d'un compte"
  - "bande passante"
  - "Machines virtuelles"
  - "Ressources GPU et CPU"
  - "bande passante réseau"
  - "écriture sur disque"
  - "mémoire gaspillée"
  - "opérations en virgule flottante"
  - "Portail Metrix"
  - "tâche GPU"
  - "Mémoire utilisée"
  - "nœuds de calcul"
  - "GPU"
  - "statistiques des tâches"
  - "Script de soumission"
  - "tâche CPU"
  - "SM"
  - "système de fichiers Lustre"
  - "systèmes de fichiers"
  - "Tâche CPU"
  - "réseau Infiniband"
  - "Système de fichiers"
  - "Bande passante"
  - "naviguer entre les pages"
  - "Statistiques d'un compte GPU"
  - "tâches"
  - "filtrer par statut"
  - "IOPS"
  - "vecteur de tâches"
  - "matrices multidimensionnelles"

questions:
  - "Quel est l'objectif principal du portail Metrix et quelles ressources permet-il aux usagers de surveiller en temps réel ?"
  - "Quelles informations spécifiques l'onglet \"Sommaire utilisateur\" fournit-il concernant les quotas et les tâches récentes de l'usager ?"
  - "Comment la section \"Statistiques des tâches\" permet-elle d'analyser l'utilisation des ressources allouées et l'activité sur les systèmes de fichiers ?"
  - "Quels états de tâches sont affichés dans la vue principale de l'interface ?"
  - "Quelles options de recherche et de filtrage sont disponibles dans la partie supérieure de l'écran ?"
  - "Comment l'utilisateur peut-il naviguer rapidement entre les différentes pages de résultats ?"
  - "Comment peut-on consulter les détails du script et la commande de soumission d'une tâche spécifique ?"
  - "Comment les différents graphiques permettent-ils d'évaluer l'utilisation des ressources allouées telles que le CPU, la mémoire et les fils d'exécution ?"
  - "Quelles informations les graphiques liés au système de fichiers et au réseau fournissent-ils, et pourquoi les statistiques globales du nœud peuvent-elles être imprécises ?"
  - "Quelle information principale est illustrée par le graphique de droite concernant le réseau Infiniband ?"
  - "Quels exemples précis de transferts massifs de données peut-on observer durant l'exécution des tâches ?"
  - "Quels autres aspects liés à la tâche, en dehors de la bande passante, sont mentionnés comme étant suivis au fil du temps ?"
  - "Comment les graphiques illustrent-ils l'utilisation du disque local et du système de fichiers (IOPS et bande passante) pendant l'exécution d'une tâche ?"
  - "Quelle est la particularité de la page d'une tâche CPU faisant partie d'un vecteur de tâches (job array) par rapport à une tâche régulière ?"
  - "Quels paramètres spécifiques faut-il analyser dans la section GPU (tels que SM active, SM occupancy et Tensor) pour évaluer l'efficacité de l'utilisation du processeur graphique ?"
  - "Quelles sont les différentes métriques de performance et de consommation du GPU qui peuvent être surveillées à travers les graphiques présentés ?"
  - "Comment les graphiques illustrent-ils l'utilisation des ressources globales du nœud, telles que la bande passante réseau Infiniband et les opérations d'entrée/sortie (IOPS) sur le disque local ?"
  - "Quelles informations la section \"Statistiques d'un compte\" fournit-elle concernant l'utilisation et le gaspillage des ressources (CPU et mémoire) par les différents utilisateurs d'un groupe ?"
  - "Quelle est la valeur d'utilisation généralement attendue concernant les SM et la gestion des warps ?"
  - "Pourquoi est-il recommandé d'optimiser son code pour maximiser l'utilisation du paramètre \"Tensor\" ?"
  - "Comment l'activité liée aux opérations en virgule flottante (FP64, FP32, FP16) doit-elle se manifester lors de l'exécution du code ?"
  - "Que représente le premier graphique concernant l'utilisation de la mémoire par les utilisateurs ?"
  - "Que mesure le graphique de gauche lié à l'activité sur les systèmes de fichiers ?"
  - "Quelle information est indiquée par le graphique de droite concernant les transferts de données vers les serveurs ?"
  - "Comment peut-on suivre l'utilisation et le gaspillage des ressources (GPU, CPU, mémoire) pour chaque utilisateur au sein d'un groupe ?"
  - "Quelles informations et statistiques spécifiques sont disponibles pour surveiller les instances de machines virtuelles dans la section Cloud ?"
  - "De quelle manière l'activité sur les systèmes de fichiers, telle que les opérations d'écriture (IOPS) et la bande passante, est-elle représentée dans les statistiques ?"
  - "Comment peut-on suivre l'utilisation et le gaspillage des ressources (GPU, CPU, mémoire) pour chaque utilisateur au sein d'un groupe ?"
  - "Quelles informations et statistiques spécifiques sont disponibles pour surveiller les instances de machines virtuelles dans la section Cloud ?"
  - "De quelle manière l'activité sur les systèmes de fichiers, telle que les opérations d'écriture (IOPS) et la bande passante, est-elle représentée dans les statistiques ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# Overview

The Metrix portal is a website for Alliance users. It leverages information collected from compute nodes and management servers to interactively generate data, allowing users to monitor their real-time resource usage (CPU, GPU, memory, file system).

| Cluster | Portal URL |
| :------ | :--------- |
| Rorqual | [https://metrix.rorqual.alliancecan.ca](https://metrix.rorqual.alliancecan.ca) |
| Narval  | [https://portail.narval.calculquebec.ca](https://portail.narval.calculquebec.ca) |
| Nibi    | [https://portal.nibi.sharcnet.ca](https://portal.nibi.sharcnet.ca) |

## File System Performance

This section presents bandwidth and metadata operation graphs, with the following visualization options: last week, last day, and last hour.

## Login Nodes

CPU and memory usage statistics, system load, and network are presented in this tab, with the following visualization options: last week, last day, and last hour.

## Scheduling

This tab presents statistics on allocated cluster cores and GPUs, with the following visualization options: last week, last day, and last hour.

## Scientific Software

The most used software with CPU cores and GPUs are presented as graphs.

## Data Transfer Nodes

Bandwidth statistics for data transfer nodes are presented in this tab.

# User Summary

Under the user summary tab, you will find your quotas for different file systems, followed by your 10 most recent jobs. You can select a job by its number to access its detailed page. Additionally, by clicking on 'More details', you will be redirected directly to the **Job Statistics** tab, where you can find all your jobs.

# Job Statistics

The first block displays your current usage (CPU Core, memory, and GPUs). These statistics represent the average resources used by all currently running jobs. You can easily compare the resources allocated to you with those you actually use.

Next, you have access to an average over the last few days, presented as a graph.

On the left, the graph shows the number of disk write operations you have performed. (*input/output operations per second (IOPS)*) On the right, you see the amount of data transferred to the servers over a given period. (Bandwidth)

The following section presents all the jobs you have already launched, which are currently running or pending. In the top left, you can filter jobs by status (OOM, completed, running, etc.). In the top right, you can search by job number (Job ID) or by name. Finally, in the bottom right, an option allows you to quickly navigate between pages by making multiple jumps.

## CPU Job Page

At the top, you have the job name, its number, your username, and the status. Details of your submission script are displayed by clicking 'View Job Script'.
!!! note "Interactive Jobs"
    If the job was launched in interactive mode, the submission script will not be available.

The working directory and submission command are accessible by clicking 'View Submission Command'.

The next section is dedicated to scheduler information. You can access your CPU account tracking page by clicking on your account number.

In the **Resources** section, you can get an initial overview of your job's resource usage by comparing the **Allocated** and **Used** columns for the various listed parameters.

The **CPU** graph allows you to visualize the CPU cores you requested over time. On the right, you can select/deselect different cores as needed.
!!! note "Short Jobs"
    Note that for very short jobs, this graph is not available.

The **Memory** graph allows you to visualize the usage of the memory you requested over time.

The **Process and threads** graph allows you to observe various parameters related to processes and threads. Ideally, for a multithreaded job, the sum of the **Running threads** and **Sleeping threads** parameters should not exceed twice the number of requested cores. However, it is quite normal to have some processes in **sleeping** (*Sleeping threads*) mode for certain types of programs (Java, Matlab, commercial software, or complex programs). You also have the program applications executed over time as a parameter.

The following graphs represent file system usage for the current job, not the entire node. On the left, a representation of the number of *input/output operations per second (IOPS)* is displayed. On the right, the graph illustrates the data transfer rate between the job and the file system over time. This graph helps identify periods of intense activity or low file system utilization.

!!! note "Node Resource Statistics"
    For statistics on the entire node's resources, please note that they may be imprecise if the node is shared among multiple users.

The graph on the left illustrates the evolution of bandwidth used by the job over time, in relation to software, licenses, etc. The graph on the right represents the evolution of network bandwidth used by a job or a set of jobs via the Infiniband network over time. This can show periods of massive data transfer (e.g., read/write on a Lustre file system, MPI communication between nodes).

The graph on the left illustrates the evolution of the number of *input/output operations per second (IOPS)* performed on the local disk over time. The one on the right shows the evolution of bandwidth used on the local disk over time, i.e., the amount of data read or written per second.

Graphical representation of local disk space usage.

Graphical representation of power usage.

## CPU Job Page (Job Array)

A CPU job page within a job array is identical to that of a regular CPU job, except for the *Other jobs in the array* section. This table lists other job numbers belonging to the same job array, along with information about their status, name, start time, and end time.

## GPU Job Page

At the top of the page, you have the job name, its number, your username, and the status. Details of your submission script are displayed by clicking 'View Job Script'.
!!! note "Interactive Jobs"
    If you launched an interactive job, the submission script is not available.

The working directory and submission command are accessible by clicking 'View Submission Command'.

The following section is reserved for scheduler information. You can access your GPU account page by clicking on your account number.

In the **Resources** section, you can get an initial overview of your job's resource usage by comparing the **Allocated** and **Used** columns for the various listed parameters.

The **CPU** graph allows you to visualize the usage of requested CPU cores over time. On the right, you can select/deselect different cores as needed.
!!! note "Short Jobs"
    Note that for very short jobs, this graph is not available.

The **Memory** graph allows you to visualize the usage over time of the memory you requested for the CPUs.

The **Process and threads** graph allows you to observe various parameters related to processes and threads.

The following graphs represent file system usage for the current job, not the entire node. On the left, a representation of the number of *input/output operations per second (IOPS)* is displayed. On the right, the graph illustrates the data transfer rate between the job and the file system over time. This graph helps identify periods of intense activity or low file system utilization.

The **GPU** graph represents your GPU usage. The *Streaming Multiprocessors* (SM) active parameter indicates the percentage of time the GPU executes a warp (a group of consecutive *threads*) in the last sampling window. This value should ideally be around 80%. For *SM occupancy* (defined as the ratio between the number of warps assigned to an SM and the maximum number of warps an SM can handle), a value around 50% is generally expected. Regarding the *Tensor* parameter, the value should be as high as possible. Ideally, your code should leverage this part of the GPU, optimized for multiplications and convolutions of multi-dimensional matrices. Finally, for *Floating Point* operations (FP64, FP32, and FP16), you should observe significant activity on only one of these types, depending on the precision used by your code.

On the left, you have a graph indicating GPU memory usage. On the right, a graph of GPU memory access cycles, representing the percentage of cycles during which the device's memory interface is active for sending or receiving data.

The GPU power graph shows the evolution of GPU power consumption (in watts) over time.

On the left, GPU bandwidth on the PCIe bus (or **PCI Express**, for *Peripheral Component Interconnect Express*). On the right, GPU bandwidth on the NVLink bus. The NVLink bus is a technology developed by NVIDIA to enable ultra-fast communication between multiple GPUs.

!!! note "Node Resource Statistics"
    For statistics on the entire node's resources, please note that they may be imprecise if the node is shared among multiple users.

The graph on the left illustrates the evolution of bandwidth used by the job over time, in relation to software, licenses, etc. The graph on the right represents the evolution of network bandwidth used by a job or a set of jobs via the Infiniband network over time. This can show periods of massive data transfer (e.g., read/write on a Lustre file system, MPI communication between nodes).

The graph on the left illustrates the evolution of the number of *input/output operations per second (IOPS)* performed on the local disk over time. The one on the right shows the evolution of bandwidth used on the local disk over time, i.e., the amount of data read or written per second.

Graphical representation of local disk space usage.

Graphical representation of power usage.

# Account Statistics

The **Account Statistics** section groups your group's usage into two subsections: CPU and GPU.

## CPU Account Statistics

Here you will find the sum of your group's requests for CPU cores, as well as their corresponding usage over the last few months. You can also track the evolution of your priority, which varies based on your usage.

This graph shows the most commonly used applications.

Here you can view the resource usage for each user in your group.

This graph shows the evolution over time of wasted CPU cores per user in the group.

Here you can view memory usage for each user in your group.

This graph represents memory wasted per user.

Next, you have a representation of your activity on the file systems. On the left, the graph shows the number of disk write commands you have performed. (*input/output operations per second (IOPS)*) On the right, you see the amount of data transferred to the servers over a given period. (Bandwidth)

You have a list of the latest jobs that have been performed for the entire group.

## GPU Account Statistics

Here you will find the sum of your group's GPU requests, as well as their corresponding usage over the last few months. You can also track the evolution of your priority, which varies based on your usage.

This graph represents the most commonly used applications.

Here you can view the resource usage for each user in your group.

The following graph represents, over time, the amount of wasted GPU per user.

Next, you have the CPU cores allocated and used in your GPU jobs.

This figure illustrates the wastage of CPUs within your GPU jobs.

Here you can visualize memory usage for each user in your group.

This graph illustrates memory wasted per user.

Next, you have a representation of your activity on the file systems. On the left, the graph shows the number of disk write commands you have performed. (*input/output operations per second (IOPS)*) On the right, you see the amount of data transferred to the servers over a given period. (Bandwidth)

Here is the list of the latest jobs performed at your group level.

# Cloud Statistics

The first table, 'Your Instances,' presents all virtual machines associated with an account. The 'Flavor' column refers to the [virtual machine type](../cloud/virtual_machine_flavors.md). The 'UUID' column corresponds to a unique identifier assigned to each virtual machine.

Subsequently, each virtual machine has its own usage statistics (CPU Cores, Memory, Disk Bandwidth, Disk IOPS, and Network Bandwidth) viewable for the last month, last week, last day, or last hour.