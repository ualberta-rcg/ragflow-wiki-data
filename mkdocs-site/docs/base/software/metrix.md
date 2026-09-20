---
title: "Metrix"
slug: "metrix"
lang: "base"

source_wiki_title: "Metrix"
source_hash: "10d933d971de6149fcc613a1b80de298"
last_synced: "2026-09-20T00:48:35.777859+00:00"
last_processed: "2026-09-20T01:45:34.972206+00:00"

tags:
  []

keywords:
  - "systèmes de fichiers"
  - "statistiques d'utilisation"
  - "évolution de la priorité"
  - "tâche GPU"
  - "quantité de données transférées"
  - "occupation SM"
  - "machines virtuelles"
  - "tâche en cours"
  - "utilisation du disque local"
  - "Statistiques du cloud"
  - "périodes d’activité intense"
  - "Bande passante réseau"
  - "utilisation Tensor"
  - "UUID"
  - "puissance GPU (watts)"
  - "instances"
  - "utilisation des ressources"
  - "débit de transfert de données"
  - "Mémoire"
  - "GPU"
  - "applications les plus couramment utilisées"
  - "CPU gaspillé"
  - "visualisation des quotas"
  - "bande passante"
  - "statistiques d'un compte"
  - "ressources allouées/utilisées"
  - "tâches en cours"
  - "graphique de droite"
  - "type de machine virtuelle"
  - "IOPS"
  - "graphique de gauche"
  - "utilisation des cœurs CPU"
  - "filtrer par statut"
  - "réseau Infiniband"
  - "transfert massif de données"
  - "statistiques des tâches"
  - "mémoire gaspillée"
  - "commandes d’écriture sur disque"
  - "suivi en temps réel des ressources"
  - "Cœurs CPU"
  - "performance des systèmes de fichiers"
  - "système de fichiers"
  - "Streaming Multiprocessors (SM)"
  - "portail Metrix"
  - "activité système de fichiers"
  - "Job ID"
  - "bande passante PCIe"
  - "ressources allouées vs utilisées"
  - "graphique CPU"
  - "machine virtuelle"
  - "CPU"

questions:
  - "Quels types de ressources et de métriques le portail Metrix permet‑il de suivre en temps réel pour les usagers de l’Alliance ?"
  - "Quels sont les différents onglets du portail et quelles informations spécifiques chacun d’eux présente‑t‑il (performance du système de fichiers, nœuds de connexion, ordonnancement, logiciels scientifiques, nœuds de transfert de données) ?"
  - "Comment le sommaire utilisateur et les statistiques des tâches aident‑ils les usagers à comparer leurs quotas alloués avec leur utilisation réelle des ressources ?"
  - "Comment filtrer les tâches par statut et rechercher une tâche précise à l’aide du numéro ou du nom ?"
  - "Quelles sections et quels graphiques sont présentés sur la page détaillée d’une tâche CPU pour suivre l’utilisation des ressources (CPU, mémoire, processus/threads, système de fichiers, bande passante) ?"
  - "Comment afficher le script de soumission et la commande de soumission d’une tâche, et dans quels cas ces options ne sont pas disponibles ?"
  - "Que représente le graphique situé à gauche dans la visualisation de votre activité sur les systèmes de fichiers ?"
  - "Quelle métrique est affichée à droite du graphique et que mesure-t-elle ?"
  - "Comment les indicateurs d’IOPS et de bande passante peuvent-ils être exploités pour évaluer les performances de votre système de fichiers ?"
  - "Que représente le graphique de gauche et quels facteurs (logiciels, licences, etc.) influencent la bande passante qu’il montre ?"
  - "Quel type de trafic réseau est illustré par le graphique de droite et comment identifier les périodes de transfert massif de données ?"
  - "Comment les phases de lecture/écriture sur le système de fichiers Lustre et les communications MPI entre nœuds se reflètent‑elles dans les courbes de bande passante présentées ?"
  - "Quels graphiques sont présentés pour suivre l’évolution de l’utilisation du disque local (IOPS, bande passante, espace utilisé et puissance) ?"
  - "En quoi la page d’une tâche CPU appartenant à un vecteur de tâches diffère‑telle de la page d’une tâche CPU classique ?"
  - "Quelles sections et quels graphiques sont disponibles sur la page d’une tâche GPU pour visualiser l’utilisation des ressources (CPU, mémoire, processus/threads, système de fichiers) ?"
  - "Quels indicateurs du graphique GPU (SM active, SM occupancy, Tensor, FP64/FP32/FP16) sont à surveiller et quelles valeurs cibles sont recommandées ?"
  - "Comment interpréter les graphiques de bande passante (PCIe, NVLink) et de bande passante réseau (Infiniband) pour détecter d’éventuels goulots d’étranglement ?"
  - "Quelles informations les sections « Statistiques d’un compte » (CPU et GPU) fournissent‑elles sur l’utilisation du groupe et l’évolution de la priorité en fonction de cette utilisation ?"
  - "Que montre la représentation du nombre d’opérations d’entrée/sortie par seconde (IOPS) affichée à gauche ?"
  - "Comment le graphique du débit de transfert de données à droite permet‑il d’identifier les périodes d’activité intense ou de faible utilisation du système de fichiers ?"
  - "Pourquoi le fichier présenté concerne‑t‑il uniquement la tâche en cours et non l’ensemble du nœud ?"
  - "Quels types de données sont présentés dans la section « Statistiques d'un compte CPU » ?"
  - "Comment la priorité d’un compte est‑elle déterminée et quelles variables l’influencent ?"
  - "À quoi servent les deux sous‑sections « CPU » et « GPU » mentionnées au début du texte ?"
  - "Quels graphiques permettent de visualiser l’utilisation et le gaspillage des ressources CPU et mémoire par chaque utilisateur du groupe ?"
  - "Comment les différentes statistiques GPU (demande, utilisation, gaspillage, CPU alloué) sont‑elles présentées et suivies dans les graphiques ?"
  - "Quelles informations le tableau « Vos instances » fournit‑il sur les machines virtuelles associées au compte (type, UUID, etc.) ?"
  - "Quelles informations sont présentées dans le tableau « Vos instances » ?"
  - "À quoi correspond la colonne « Saveur » dans ce tableau ?"
  - "Quel est le rôle de la colonne « UUID » pour chaque machine virtuelle ?"
  - "Quelles sont les différentes métriques d’utilisation (CPU, mémoire, bande passante disque, IOPS disque, bande passante réseau) disponibles pour chaque machine virtuelle ?"
  - "Sur quelles périodes temporelles les statistiques d’une machine virtuelle peuvent‑elles être affichées (dernière heure, jour, semaine, mois) ?"
  - "Comment les graphiques illustrant ces statistiques sont‑ils présentés dans la documentation (format d’image, taille, disposition) ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Overview

The Metrix portal is a website for Alliance users. It uses information collected from compute nodes and management servers to interactively generate data, allowing users to monitor their real-time resource usage (CPU, GPU, memory, file system).

| Cluster | URL |
|:---|:---|
| Rorqual | [https://metrix.rorqual.alliancecan.ca](https://metrix.rorqual.alliancecan.ca) |
| Narval | [https://metrix.narval.alliancecan.ca](https://metrix.narval.alliancecan.ca) |
| Nibi | [https://portal.nibi.sharcnet.ca](https://portal.nibi.sharcnet.ca) |
| tamIA | [https://portail.tamia.ecpia.ca](https://portail.tamia.ecpia.ca) |
| Vulcan | [https://metrix.vulcan.alliancecan.ca](https://metrix.vulcan.alliancecan.ca) |

**File System Performance**

This section presents bandwidth and metadata operation graphs, along with the following visualization options: last week, last day, and last hour.

**Login Nodes**

CPU, memory, system load, and network usage statistics are presented in this tab, with the following visualization options: last week, last day, and last hour.

**Scheduling**

This tab presents statistics on allocated cluster cores and GPUs, with the following visualization options: last week, last day, and last hour.

**Scientific Software**

The most used software with CPU cores and GPUs are presented as graphs.

**Data Transfer Nodes**

Bandwidth statistics for data transfer nodes are presented in this tab.

## User Summary
Under the user summary tab, you will find your quotas for different file systems, followed by your last 10 jobs. You can select a job by its number to access its detailed page. Additionally, by clicking on **(More details)**, you will be redirected directly to the **Job Statistics** tab, where you will find all your jobs.

## Job Statistics
The first block displays your current usage (CPU core, memory, and GPUs). These statistics represent the average of resources used by all currently running jobs. You can easily compare your allocated resources with your actual usage.

You then have access to a multi-day average, presented as a graph.

Next, a representation of your file system activity is available. This includes the number of disk write commands you have performed (Input/Output Operations Per Second - IOPS) and the amount of data transferred to servers over a given period (Bandwidth).

The following section presents all jobs you have launched, are currently running, or are pending. You can filter jobs by status (e.g., OOM, completed, running) and search by job number (Job ID) or name. An option also allows you to quickly navigate between pages by making multiple jumps.

### CPU Job Page
At the top, you will find the job name, its number, your username, and the status. Details of your submission script are displayed by clicking on **View Job Script**. If the job was launched in interactive mode, the submission script will not be available.

The working directory and submission command are accessible by clicking on **View Submission Command**.

The next section is dedicated to scheduler information. You can access your CPU account tracking page by clicking on your account number.

In the **Resources** section, you can get an initial overview of your job's resource usage by comparing the **Allocated** and **Used** columns for the various listed parameters.

The **CPU** graph allows you to visualize the CPU cores you requested over time. You can select/deselect different cores as needed. Note that for very short jobs, this graph is not available.

The **Memory** graph allows you to visualize the memory usage you requested over time.

The **Process and threads** graph allows you to observe different parameters related to processes and threads. Ideally, for a multithreaded job, the sum of the **Running threads** and **Sleeping threads** parameters should not exceed twice the number of cores requested. However, it is quite normal to have some processes in **sleeping** mode (*Sleeping threads*) for certain types of programs (Java, MATLAB, commercial software, or complex programs). You also have the program's applications executed over time as a parameter.

The following graphs represent the file system usage for the current job, not the entire node. They display the number of Input/Output Operations Per Second (IOPS) and illustrate the data transfer rate between the job and the file system over time. This information helps identify periods of intense activity or low file system utilization.

For full node resource statistics, be aware that these can be imprecise if the node is shared among multiple users. This section illustrates the evolution of bandwidth used by the job over time, in relation to software, licenses, etc. It also represents the evolution of network bandwidth used by a job or a set of jobs via the Infiniband network over time. Periods of massive data transfer (e.g., read/write on a file system (Lustre), MPI communication between nodes) can be observed here.

This section illustrates the evolution of the number of Input/Output Operations Per Second (IOPS) performed on the local disk over time. It also shows the evolution of bandwidth used on the local disk over time, i.e., the amount of data read or written per second.

Graphical representation of local disk space usage.

Graphical representation of power usage.

### CPU Job Page (Job Array)

The page for a CPU job within a job array is identical to that of a regular CPU job, with the exception of the *Other jobs in the array* section. This table lists other job numbers that are part of the same job array, along with information on their status, name, start time, and end time.

### GPU Job Page

At the top of the page, you will find the job name, its number, your username, and the status. Details of your submission script are displayed by clicking on **View Job Script**. If you launched an interactive job, the submission script is not available.

The directory and submission command are accessible by clicking on **View Submission Command**.

The next section is reserved for scheduler information. You can access your GPU account page by clicking on your account number.

In the **Resources** section, you can get an initial overview of your job's resource usage by comparing the **Allocated** and **Used** columns for the various listed parameters.

The **CPU** graph allows you to visualize the usage of requested CPU cores over time. You can select/deselect different cores as needed. Note that for very short jobs, this graph is not available.

The **Memory** graph allows you to visualize the usage over time of the memory you requested for the CPU.

The **Process and threads** graph allows you to observe different parameters related to processes and threads.

The following graphs represent the file system usage for the current job, not the entire node. They display the number of Input/Output Operations Per Second (IOPS) and illustrate the data transfer rate between the job and the file system over time. This information helps identify periods of intense activity or low file system utilization.

The GPU graph represents your GPU usage. The *Streaming Multiprocessors* (SM) active parameter indicates the percentage of time the GPU executes a warp (a group of consecutive threads) in the last sampling window. This value should ideally be around 80%. For *SM occupancy* (defined as the ratio of warps assigned to an SM to the maximum number of warps an SM can handle), a value around 50% is generally expected. Regarding the *Tensor* parameter, the value should be as high as possible. Ideally, your code should leverage this part of the GPU, which is optimized for multidimensional matrix multiplications and convolutions. Finally, for floating-point operations (*Floating Point*) FP64, FP32, and FP16, you should observe significant activity on only one of these types, depending on the precision used by your code.

This section includes a graph indicating the memory used by the GPU and a graph of GPU memory access cycles, representing the percentage of cycles during which the device's memory interface is active for sending or receiving data.

The GPU power graph displays the evolution of GPU energy consumption (in watts) over time.

This section shows the GPU bandwidth on the PCIe bus (or **PCI Express**, for *Peripheral Component Interconnect Express*) and GPU bandwidth on the NVLink bus. The NVLink bus is a technology developed by NVIDIA to enable ultra-fast communication between multiple GPUs.

For full node resource statistics, be aware that these can be imprecise if the node is shared among multiple users. This section illustrates the evolution of bandwidth used by the job over time, in relation to software, licenses, etc. It also represents the evolution of network bandwidth used by a job or a set of jobs via the Infiniband network over time. Periods of massive data transfer (e.g., read/write on a file system (Lustre), MPI communication between nodes) can be observed here.

This section illustrates the evolution of the number of Input/Output Operations Per Second (IOPS) performed on the local disk over time. It also shows the evolution of bandwidth used on the local disk over time, i.e., the amount of data read or written per second.

Graphical representation of local disk space usage.

Graphical representation of power usage.

## Account Statistics

The **Account Statistics** section groups your group's usage into two sub-sections: CPU and GPU.

### CPU Account Statistics

Here you will find the sum of your group's requests for CPU cores, as well as their corresponding usage over the past months. You can also track the evolution of your priority, which varies based on your usage.

This graph shows the most commonly used applications.

Here you can consult the resource usage for each user in your group.

This graph shows the evolution over time of wasted CPU cores by each user in the group.

Here you can consult the memory usage for each user in your group.

This graph represents the memory wasted by each user.

Next, a representation of your file system activity is available. This includes the number of disk write commands you have performed (Input/Output Operations Per Second - IOPS) and the amount of data transferred to servers over a given period (Bandwidth).

Here is a list of the latest jobs that have been performed for the entire group.

### GPU Account Statistics

Here you will find the sum of your group's GPU requests, as well as their corresponding usage over the past months. You can also track the evolution of your priority, which varies based on your usage.

This graph represents the most commonly used applications.

Here you can consult the resource usage for each user in your group.

The following graph represents, over time, the amount of GPU wasted per user.

Next, you have the CPU cores allocated and used in your GPU jobs.

This section illustrates the waste of CPUs within your GPU jobs.

Here you can visualize the memory usage for each user in your group.

This graph illustrates the memory wasted by each user.

Next, a representation of your file system activity is available. This includes the number of disk write commands you have performed (Input/Output Operations Per Second - IOPS) and the amount of data transferred to servers over a given period (Bandwidth).

Here is the list of the latest jobs performed at your group level.

## Cloud Statistics

The first table, 'Your Instances,' presents all virtual machines associated with an account. The 'Flavor' column refers to the [virtual machine type](../cloud/virtual_machine_flavors.md). The 'UUID' column corresponds to a unique identifier assigned to each virtual machine.

Subsequently, each virtual machine has its own usage statistics (CPU Cores, Memory, Disk Bandwidth, Disk IOPS, and Network Bandwidth) viewable for the last month, last week, last day, or last hour.