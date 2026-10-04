---
title: "Metrix"
slug: "metrix"
lang: "base"

source_wiki_title: "Metrix"
source_hash: "251465bb21bb0dc6a4288addc471ded4"
last_synced: "2026-10-04T02:27:33.201522+00:00"
last_processed: "2026-10-04T03:11:37.924209+00:00"

tags:
  []

keywords:
  - "sauts multiples"
  - "multiplications et convolutions de matrices multidimensionnelles"
  - "script de soumission"
  - "portail Metrix"
  - "quotas des systèmes de fichiers"
  - "utilisation des ressources"
  - "Cœurs CPU alloués"
  - "ressources allouées vs utilisées"
  - "filtrer par statut"
  - "recherche par numéro de tâche"
  - "statistiques des tâches"
  - "graphique CPU"
  - "mémoire GPU"
  - "commandes d’écriture"
  - "tâche CPU"
  - "opérations en virgule flottante"
  - "communication MPI"
  - "utilisateur"
  - "graphique mémoire"
  - "système de fichiers Lustre"
  - "GPU gaspillé"
  - "utilisation du GPU"
  - "SM"
  - "tâches en cours"
  - "navigation entre les pages"
  - "cycles d'accès du GPU"
  - "transfert massif de données"
  - "bande passante des nœuds"
  - "Statistiques du cloud"
  - "bande passante PCIe et NVLink"
  - "IOPS"
  - "nombre maximal de warps"
  - "puissance GPU"
  - "Tensor"
  - "Infiniband"
  - "statistiques d'un compte CPU"
  - "graphique"
  - "Statistiques d'un compte GPU"
  - "Utilisation des ressources par utilisateur"
  - "mémoire gaspillée"
  - "bande passante réseau"
  - "ressources allouées"
  - "bande passante"

questions:
  - "Quel est le rôle principal du portail Metrix et quelles ressources permet‑il de suivre en temps réel ?"
  - "Quels onglets sont proposés sur le portail Metrix et quelles informations affichent chacun d’eux (performance du système de fichiers, utilisation des nœuds, ordonnancement, logiciels scientifiques, etc.) ?"
  - "Comment consulter les détails d’une tâche depuis le « Sommaire utilisateur » et quelles statistiques sont présentées dans l’onglet « Statistiques des tâches » ?"
  - "Comment filtrer les tâches affichées selon leur statut dans l’interface ?"
  - "Comment rechercher une tâche précise en utilisant son numéro (Job ID) ou son nom ?"
  - "Quelle option permet de passer rapidement d’une page à l’autre en effectuant des sauts multiples ?"
  - "Comment accéder aux détails du script de soumission ainsi qu’à la commande de soumission d’une tâche CPU ?"
  - "Quels indicateurs et graphiques sont présentés dans la section « Ressources » (CPU, Mémoire, Process and threads) et comment les interpréter ?"
  - "Quels graphiques permettent de suivre l’utilisation du système de fichiers et de la bande passante réseau d’une tâche, et quelles informations peuvent‑elles révéler ?"
  - "Que représente le graphique de droite présenté dans le texte ?"
  - "Quels types d’activités sont identifiés comme générant des pics de bande passante sur le réseau InfiniBand ?"
  - "Comment ces variations de bande passante peuvent-elles influencer la gestion des ressources (logiciels, licences, etc.) d’une tâche au fil du temps ?"
  - "Quels indicateurs sont affichés dans le graphique GPU et quelles sont les valeurs cibles recommandées pour le SM actif, le SM occupancy, le paramètre Tensor et les types de précision en virgule flottante ?"
  - "En quoi la page d’une tâche CPU appartenant à un vecteur de tâches diffère‑t‑elle d’une page de tâche CPU classique, notamment concernant la section « Other jobs in the array » ?"
  - "Quels graphiques permettent de suivre l’utilisation du disque local et du système de fichiers, et quelles mesures (IOPS, bande passante, débit de transfert) affichent‑ils au fil du temps ?"
  - "Comment le graphique des cycles d’accès du GPU à la mémoire indique‑t‑il l’utilisation de l’interface mémoire de l’appareil ?"
  - "Quelles métriques sont présentées dans la section « Statistiques d’un compte CPU » pour suivre la consommation et l’efficacité des ressources du groupe ?"
  - "Comment les graphiques de bande passante GPU sur le bus PCIe et sur le bus NVLink permettent‑ils de comparer les performances de communication entre GPU ?"
  - "Quelle proportion d’occupation des SM (en pourcentage du nombre maximal de warps) est généralement attendue ?"
  - "Pourquoi le paramètre « Tensor » doit‑il être réglé à la valeur la plus élevée possible et quel impact cela a‑t‑il sur les performances du GPU ?"
  - "Comment identifier quel type d’opération en virgule flottante (FP64, FP32 ou FP16) sera le plus sollicité selon la précision utilisée par le code ?"
  - "Quel type d’information le premier graphique indique‑t‑il concernant chaque utilisateur ?"
  - "Comment la représentation de votre activité sur les systèmes de fichiers est‑elle organisée visuellement ?"
  - "Quels sont les indicateurs mesurés respectivement à gauche (IOPS) et à droite (bande passante) dans cette représentation ?"
  - "Quels indicateurs sont affichés pour suivre l’utilisation et le gaspillage des GPU, CPU et mémoire au sein du groupe ?"
  - "Comment les statistiques d’utilisation (cœurs CPU, mémoire, bande passante disque, IOPS, bande passante réseau) sont‑elles présentées pour chaque machine virtuelle dans la section « Statistiques du cloud » ?"
  - "Quelles informations sont fournies concernant l’activité du système de fichiers, notamment les IOPS et la bande passante de transfert de données ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# Overview

The Metrix portal is a website for Alliance users. It uses information collected from compute nodes and management servers to interactively generate data, allowing users to monitor their real-time resource usage (CPU, GPU, memory, filesystem).

| Cluster | URL |
| :------ | :-- |
| Rorqual | [https://metrix.rorqual.alliancecan.ca](https://metrix.rorqual.alliancecan.ca) |
| Narval | [https://metrix.narval.alliancecan.ca](https://metrix.narval.alliancecan.ca) |
| Nibi | [https://portal.nibi.sharcnet.ca](https://portal.nibi.sharcnet.ca) |
| tamIA | [https://portail.tamia.ecpia.ca](https://portail.tamia.ecpia.ca) |
| Vulcan | [https://metrix.vulcan.alliancecan.ca](https://metrix.vulcan.alliancecan.ca) |

### Filesystem Performance

This section presents bandwidth and metadata operation charts, with the following visualization options: last week, last day, and last hour.

### Login Nodes

CPU usage, memory, system load, and network statistics are presented in this tab, with the following visualization options: last week, last day, and last hour.

### Scheduling

This tab presents statistics on allocated CPU cores and GPUs for the cluster, with the following visualization options: last week, last day, and last hour.

### Scientific Software

The most used software with CPU cores and GPUs are presented in charts.

### Data Transfer Nodes

Bandwidth statistics for data transfer nodes are presented in this tab.

## User Summary

Under the User Summary tab, you will find your quotas for different filesystems, followed by your 10 most recent jobs. You can select a job by its number to access its detailed page. Additionally, by clicking on the "(More details)" link, you will be redirected directly to the **Job Statistics** tab, where you can find all your jobs.

## Job Statistics

The first block displays your current usage (CPU core, memory, and GPUs). These statistics represent the average resources used by all currently running jobs. You can easily compare the resources allocated to you with those you are actually using.

You then have access to an average of the last few days, presented in chart form.

You then have a representation of your filesystem activity. The left chart shows the number of disk write commands you have performed (*input/output operations per second (IOPS)*). The right chart displays the amount of data transferred to servers over a given period (*bandwidth*).

The following section presents all the jobs you have launched, which are currently running or pending. In the top left, you can filter jobs by status (OOM, completed, running, etc.). In the top right, you can search by job ID or name. Finally, in the bottom right, an option allows you to quickly navigate between pages by performing multiple jumps.

## CPU Job Page

At the top of the page, you will find the job name, its number, your username, and its status. The details of your submission script are displayed by clicking on the "View job script" button. If the job was launched in interactive mode, the submission script will not be available.

The working directory and submission command are accessible by clicking on the "View submission command" button.

The next section is dedicated to scheduler information. You can access the tracking page for your CPU account by clicking on your account number.

In the **Resources** section, you can get an initial overview of your job's resource usage by comparing the **Allocated** and **Used** columns for the various listed parameters.

The **CPU** chart allows you to visualize the CPU cores you requested over time. On the right, you can select/deselect different cores as needed.
!!! note
    For very short jobs, this chart is not available.

The **Memory** chart allows you to visualize the memory usage you requested over time.

The **Process and threads** chart allows you to observe various parameters related to processes and threads. Ideally, for a multithreaded job, the sum of **Running threads** and **Sleeping threads** should not exceed twice the number of requested cores. However, it is perfectly normal to have some processes in **dormant** (*Sleeping threads*) mode for certain types of programs (Java, MATLAB, commercial software, or complex programs). You also have the program applications executed over time as a parameter.

The following charts represent filesystem usage for the current job, not the entire node. The left chart displays the number of input/output operations per second (IOPS). The right chart illustrates the data transfer rate between the job and the filesystem over time. This chart helps identify periods of intense activity or low filesystem utilization.

For statistics on the entire node's resources, be aware that these can be imprecise if the node is shared among multiple users. The left chart illustrates the evolution of bandwidth used by the job over time, in relation to software, licenses, etc. The right chart represents the evolution of network bandwidth used by a job or set of jobs via the Infiniband network over time. This can show periods of massive data transfer (e.g., reading/writing to a Lustre filesystem, MPI communication between nodes).

The left chart illustrates the evolution of the number of input/output operations per second (IOPS) performed on the local disk over time. The right chart shows the evolution of bandwidth used on the local disk over time, i.e., the amount of data read or written per second.

A chart shows the usage of local disk space.

A chart shows the power consumed.

## CPU Job Page (Job Array)

The page for a CPU job within a job array is identical to that of a regular CPU job, except for the *Other jobs in the array* section. This table lists the other job numbers that are part of the same job array, along with information on their status, name, start time, and end time.

## GPU Job Page

At the top of the page, you will find the job name, its number, your username, and its status. The details of your submission script are displayed by clicking on the "View job script" button. If you launched an interactive job, the submission script is not available.

The working directory and submission command are accessible by clicking on the "View submission command" button.

The following section is reserved for scheduler information. You can access your GPU account page by clicking on your account number.

In the **Resources** section, you can get an initial overview of your job's resource usage by comparing the **Allocated** and **Used** columns for the various listed parameters.

The **CPU** chart allows you to visualize the usage of requested CPU cores over time. On the right, you can select/deselect different cores as needed.
!!! note
    For very short jobs, this chart is not available.

The **Memory** chart allows you to visualize the usage over time of the memory you requested for the CPUs.

The **Process and threads** chart allows you to observe various parameters related to processes and threads.

The following charts represent filesystem usage for the current job, not the entire node. The left chart displays the number of input/output operations per second (IOPS). The right chart illustrates the data transfer rate between the job and the filesystem over time. This chart helps identify periods of intense activity or low filesystem utilization.

The GPU chart represents your GPU usage. The *Streaming Multiprocessors* (SM) active parameter indicates the percentage of time the GPU executes a warp (a group of consecutive *threads*) in the last sampling window. This value should ideally be around 80%. For *SM occupancy* (defined as the ratio between the number of warps assigned to an SM and the maximum number of warps an SM can handle), a value around 50% is generally expected. Regarding the *Tensor* parameter, the value should be as high as possible. Ideally, your code should leverage this part of the GPU, which is optimized for multi-dimensional matrix multiplications and convolutions. Finally, for *Floating Point* operations (FP64, FP32, and FP16), you should observe significant activity on only one of these types, depending on the precision used by your code.

The left chart shows the memory used by the GPU. The right chart displays GPU memory access cycles, representing the percentage of cycles during which the device's memory interface is active for sending or receiving data.

The GPU power chart displays the evolution of GPU power consumption (in watts) over time.

The left chart shows GPU bandwidth on the PCIe bus (or **PCI Express**, for *Peripheral Component Interconnect Express*). The right chart displays GPU bandwidth on the NVLink bus. The NVLink bus is a technology developed by NVIDIA to enable ultra-fast communication between multiple GPUs.

For statistics on the entire node's resources, be aware that these can be imprecise if the node is shared among multiple users. The left chart illustrates the evolution of bandwidth used by the job over time, in relation to software, licenses, etc. The right chart represents the evolution of network bandwidth used by a job or set of jobs via the Infiniband network over time. This can show periods of massive data transfer (e.g., reading/writing to a Lustre filesystem, MPI communication between nodes).

The left chart illustrates the evolution of the number of input/output operations per second (IOPS) performed on the local disk over time. The right chart shows the evolution of bandwidth used on the local disk over time, i.e., the amount of data read or written per second.

A chart shows the usage of local disk space.

A chart shows the power consumed.

## Account Statistics

The **Account Statistics** section groups your group's usage into two subsections: CPU and GPU.

### CPU Account Statistics

Here you will find the sum of your group's CPU core requests, as well as their corresponding usage over the past months. You can also track the evolution of your priority, which varies based on your usage.

This chart displays the most commonly used applications.

Here you can view the resource usage for each user in your group.

This chart shows the evolution over time of wasted CPU cores by each user in the group.

Here you can view the memory usage for each user in your group.

This chart represents the memory wasted by each user.

You then have a representation of your filesystem activity. The left chart shows the number of disk write commands you have performed (input/output operations per second (IOPS)). The right chart displays the amount of data transferred to servers over a given period (bandwidth).

You have a list of the latest jobs that have been performed for the entire group.

### GPU Account Statistics

Here you will find the sum of your group's GPU requests, as well as their corresponding usage over the past months. You can also track the evolution of your priority, which varies based on your usage.

This chart displays the most commonly used applications.

Here you can view the resource usage for each user in your group.

The following chart represents, over time, the amount of wasted GPU resources per user.

You then have the CPU cores allocated and used in your GPU jobs.

This chart illustrates the wastage of CPUs in the context of your GPU jobs.

Here you can visualize the memory usage for each user in your group.

This chart illustrates the memory wasted by each user.

You then have a representation of your filesystem activity. The left chart shows the number of disk write commands you have performed (input/output operations per second (IOPS)). The right chart displays the amount of data transferred to servers over a given period (bandwidth).

Here is a list of the latest jobs performed at your group level.

## Cloud Statistics

The first table, "Your Instances", presents all virtual machines associated with an account. The "Flavor" column refers to the [virtual machine type](../cloud/virtual_machine_flavors.md). The "UUID" column corresponds to a unique identifier assigned to each virtual machine.

Each virtual machine then has its own usage statistics (CPU Cores, Memory, Disk Bandwidth, Disk IOPS, and Network Bandwidth) viewable for the last month, last week, last day, or last hour.