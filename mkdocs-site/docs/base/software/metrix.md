---
title: "Metrix"
slug: "metrix"
lang: "base"

source_wiki_title: "Metrix"
source_hash: "180cbc39ee1248f4d29e3921e0cccaf0"
last_synced: "2026-10-11T01:39:35.690021+00:00"
last_processed: "2026-10-11T02:29:47.645115+00:00"

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
  ragflow_synced: false
  qa_generated: false
---

# Overview

The Metrix portal is a website for Alliance users. It uses information collected from compute nodes and management servers to interactively generate data, allowing users to track their resource usage (CPU, GPU, memory, file system) in real-time.

| Cluster | Metrix URL |
|:--------|:-----------|
| Rorqual | [https://metrix.rorqual.alliancecan.ca](https://metrix.rorqual.alliancecan.ca) |
| Narval  | [https://metrix.narval.alliancecan.ca](https://metrix.narval.alliancecan.ca) |
| Nibi    | [https://portal.nibi.sharcnet.ca](https://portal.nibi.sharcnet.ca)           |
| tamIA   | [https://portail.tamia.ecpia.ca](https://portail.tamia.ecpia.ca)             |
| Vulcan  | [https://metrix.vulcan.alliancecan.ca](https://metrix.vulcan.alliancecan.ca) |

**File System Performance**

This section displays bandwidth and metadata operation graphs, with the following visualization options: last week, last day, and last hour.

**Login Nodes**

CPU, memory, system load, and network usage statistics are presented in this tab, with the following visualization options: last week, last day, and last hour.

**Scheduling**

This tab presents statistics on allocated CPU cores and GPUs for the cluster, with the following visualization options: last week, last day, and last hour.

**Scientific Software**

The most used software with CPU cores and GPUs are presented.

**Data Transfer Nodes**

Bandwidth statistics for data transfer nodes are presented in this tab.

# User Summary

Under the user summary tab, you will find your quotas for the different file systems, followed by your 10 most recent jobs. You can select a job by its number to access its detailed page. Additionally, by clicking on **(More details)**, you will be redirected directly to the **Job Statistics** tab, where you will find all your jobs.

# Job Statistics

The first block displays your current usage (CPU core, memory, and GPUs). These statistics represent the average resources used by all currently running jobs. You can easily compare the resources allocated to you with those you are actually using.

Next, you have access to an average of the last few days' usage.

Next, you have a representation of your activity on the file systems. This includes the number of disk write commands you have performed (*input/output operations per second (IOPS)*) and the amount of data transferred to the servers over a given period (Bandwidth).

The following section presents all jobs you have launched, are currently running, or are pending. You can filter jobs by status (OOM, completed, running, etc.) and search by job number (Job ID) or name. Additionally, an option allows you to quickly navigate between pages by performing multiple jumps.

## CPU Job Page

At the top, you will find the job name, its ID, your username, and its status. Details of your submission script are displayed by clicking **View Job Script**. If the job was launched in interactive mode, the submission script will not be available.

The working directory and submission command are accessible by clicking **View Submission Command**.

The next section is dedicated to scheduler information. You can access your CPU account's tracking page by clicking on your account number.

In the **Resources** section, you can get an initial overview of your job's resource usage by comparing the **Allocated** and **Used** columns for the various listed parameters.

The **CPU** chart allows you to visualize the CPU cores you requested over time. You can select/deselect different cores as needed. Note that for very short jobs, this chart is not available.

The **Memory** chart allows you to visualize the memory usage you requested over time.

The **Process and threads** chart allows you to observe various parameters related to processes and threads. Ideally, for a multi-threaded job, the sum of **Running threads** and **Sleeping threads** should not exceed twice the number of requested cores. However, it is quite normal to have some processes in **sleeping** mode (*Sleeping threads*) for certain types of programs (Java, MATLAB, commercial software, or complex programs). You also have parameters for program applications executed over time.

The following charts represent file system usage for the current job, not the entire node. They display the number of input/output operations per second (IOPS) and illustrate the data transfer rate between the job and the file system over time. This helps identify periods of intense activity or low file system utilization.

Node-wide resource statistics can be imprecise if the node is shared among multiple users. These charts illustrate the evolution of bandwidth used by the job over time, in connection with software, licenses, etc., and the evolution of network bandwidth used by a job or set of jobs via the Infiniband network over time. This allows observation of periods of massive data transfer (e.g., read/write on a Lustre file system, MPI communication between nodes).

Local disk usage includes charts illustrating the evolution of input/output operations per second (IOPS) performed on the local disk over time, and the evolution of bandwidth used on the local disk over time (i.e., the amount of data read or written per second).

Local disk space usage is also presented.

Power usage is also presented.

## CPU Job Page (Job Array)

The page for a CPU job within a job array is identical to that of a regular CPU job, with the exception of the *Other jobs in the array* section. This table lists other job numbers that are part of the same job array, along with information on their status, name, start time, and end time.

## GPU Job Page

At the top of the page, you will find the job name, its ID, your username, and its status. Details of your submission script are displayed by clicking **View Job Script**. If you launched an interactive job, the submission script is not available.

The working directory and submission command are accessible by clicking **View Submission Command**.

The following section is reserved for scheduler information. You can access your GPU account page by clicking on your account number.

In the **Resources** section, you can get an initial overview of your job's resource usage by comparing the **Allocated** and **Used** columns for the various listed parameters.

The **CPU** chart allows you to visualize the usage of requested CPU cores over time. You can select/deselect different cores as needed. Note that for very short jobs, this chart is not available.

The **Memory** chart allows you to visualize the memory usage you requested for CPUs over time.

The **Process and threads** chart allows you to observe various parameters related to processes and threads.

The following charts represent file system usage for the current job, not the entire node. They display the number of input/output operations per second (IOPS) and illustrate the data transfer rate between the job and the file system over time. This helps identify periods of intense activity or low file system utilization.

GPU usage includes details on *Streaming Multiprocessors* (SM) activity, indicating the percentage of time the GPU executes a warp (a group of consecutive *threads*) in the last sampling window. This value should ideally be around 80%. For *SM occupancy* (defined as the ratio of warps assigned to an SM to the maximum number of warps an SM can handle), a value around 50% is generally expected. For the *Tensor* parameter, the value should be as high as possible. Ideally, your code should leverage this part of the GPU, optimized for multi-dimensional matrix multiplications and convolutions. Finally, for *Floating Point* operations (FP64, FP32, and FP16), you should observe significant activity on only one of these types, depending on the precision used by your code.

GPU memory usage and access cycles are displayed. Memory access cycles represent the percentage of cycles during which the device's memory interface is active for sending or receiving data.

GPU power consumption (in watts) over time is displayed.

GPU bandwidth on the PCIe bus (or **PCI Express**, for *Peripheral Component Interconnect Express*) and NVLink bus is also presented. The NVLink bus is a technology developed by NVIDIA to enable ultra-fast communication between multiple GPUs.

Node-wide resource statistics can be imprecise if the node is shared among multiple users. These charts illustrate the evolution of bandwidth used by the job over time, in connection with software, licenses, etc., and the evolution of network bandwidth used by a job or set of jobs via the Infiniband network over time. This allows observation of periods of massive data transfer (e.g., read/write on a Lustre file system, MPI communication between nodes).

Local disk usage includes charts illustrating the evolution of input/output operations per second (IOPS) performed on the local disk over time, and the evolution of bandwidth used on the local disk over time (i.e., the amount of data read or written per second).

Local disk space usage is also presented.

Power usage is also presented.

# Account Statistics

The **Account Statistics** section groups your group's usage into two subsections: CPU and GPU.

## CPU Account Statistics

Here you will find your group's total CPU core requests and their corresponding usage over recent months. You can also track the evolution of your priority, which varies based on your usage.

The most commonly used applications are also presented.

Here you can consult the resource usage by each user in your group.

CPU cores wasted by each user in the group over time are presented.

Here you can consult the memory usage by each user in your group.

Memory wasted by each user is also presented.

Next, you have a representation of your activity on the file systems. This includes the number of disk write commands you have performed (input/output operations per second (IOPS)) and the amount of data transferred to the servers over a given period (Bandwidth).

A list of the latest jobs performed for the entire group is available.

## GPU Account Statistics

Here you will find your group's total GPU requests and their corresponding usage over recent months. You can also track the evolution of your priority, which varies based on your usage.

The most commonly used applications are also presented.

Here you can consult the resource usage by each user in your group.

GPU resources wasted by user over time are presented.

Next, you have the CPU cores allocated and used in your GPU jobs.

CPU wastage within your GPU jobs is also illustrated.

Here you can visualize memory usage for each user in your group.

Memory wasted by each user is also illustrated.

Next, you have a representation of your activity on the file systems. This includes the number of disk write commands you have performed (input/output operations per second (IOPS)) and the amount of data transferred to the servers over a given period (Bandwidth).

A list of the latest jobs performed at your group level is available.

# Cloud Statistics

The first table, 'Your Instances', presents all virtual machines associated with an account. The 'Flavor' column refers to the [virtual machine type](../cloud/virtual_machine_flavors.md). The 'UUID' column corresponds to a unique identifier assigned to each virtual machine.

Subsequently, each virtual machine has its own usage statistics (CPU Cores, Memory, Disk Bandwidth, Disk IOPS, and Network Bandwidth) viewable for the last month, last week, last day, or last hour.