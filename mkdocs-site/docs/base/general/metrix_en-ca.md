---
title: "Metrix/en-ca"
slug: "metrix_en-ca"
lang: "base"

source_wiki_title: "Metrix/en-ca"
source_hash: "b5f12ad303f84bd49bba0575bafaaf33"
last_synced: "2026-10-04T02:27:33.201522+00:00"
last_processed: "2026-10-04T03:19:00.419206+00:00"

tags:
  []

keywords:
  - "visualisation temps réel"
  - "tâche multifils"
  - "Cœur CPU"
  - "script de la tâche"
  - "gaspillage CPU"
  - "bande passante PCIe"
  - "script de soumission"
  - "portail Metrix"
  - "bus PCIe"
  - "utilisation des ressources"
  - "disque local"
  - "ressources allouées vs utilisées"
  - "graphique CPU"
  - "commande de soumission"
  - "mémoire GPU"
  - "machine virtuelle"
  - "systèmes de fichiers"
  - "SM occupancy"
  - "utilisation du système de fichiers"
  - "graphique GPU"
  - "utilisation GPU"
  - "statistiques compte GPU"
  - "Cœurs CPU"
  - "Mémoire"
  - "nombre de cœurs"
  - "tâche interactive"
  - "commandes d’écriture sur disque"
  - "consommation énergétique"
  - "Bande passante disque"
  - "mémoire"
  - "GPUs"
  - "Voir la commande de soumission"
  - "Statistiques des tâches"
  - "utilisation du disque"
  - "graphique Mémoire"
  - "Bande passante réseau"
  - "CPU"
  - "tâches en cours"
  - "Running threads"
  - "statistiques d'utilisation"
  - "CPU gaspillé"
  - "quotas et tâches"
  - "bande passante GPU"
  - "statistiques d'un compte"
  - "IOPS"
  - "tâche GPU"
  - "instances virtuelles"
  - "utilisation actuelle"
  - "processus dormant"
  - "graphique de puissance GPU"
  - "graphique"
  - "interface mémoire"
  - "Mémoire cloud"
  - "statistiques CPU/GPU/mémoire"
  - "IOPS disque"
  - "Sleeping threads"
  - "bande passante"

questions:
  - "Quels types de ressources et de métriques le portail Metrix permet‑il de suivre en temps réel pour les usagers de l’Alliance ?"
  - "Comment les différents onglets du portail (Performance du système de fichiers, Nœuds de connexion, Ordonnancement, Logiciels scientifiques, Nœuds de transfert de données) présentent‑ils les données et quelles options de visualisation offrent‑ils ?"
  - "Où les utilisateurs peuvent‑ils consulter leurs quotas, leurs dernières tâches et les détails de leurs ressources allouées dans le portail Metrix ?"
  - "Quels types de ressources sont affichés dans le premier bloc des statistiques des tâches ?"
  - "Comment les statistiques présentées sont‑elles calculées pour les tâches en cours d’exécution ?"
  - "À quoi sert la comparaison entre les ressources qui vous sont allouées et celles que vous utilisez réellement ?"
  - "Comment accéder aux graphiques d’utilisation moyenne des derniers jours et quelles informations affichent-ils ?"
  - "Quels filtres et options de recherche sont disponibles pour gérer et naviguer parmi les tâches listées ?"
  - "Quels graphiques et indicateurs sont présentés dans la page détaillée d’une tâche CPU (ressources, CPU, mémoire, processus/threads) et comment les interpréter ?"
  - "Quels graphiques sont utilisés pour visualiser l’utilisation du système de fichiers d’une tâche et quelles informations permettent‑elles d’identifier (par exemple IOPS, débit de transfert) ?"
  - "En quoi les graphiques relatifs aux ressources du nœud complet diffèrent‑ils de ceux centrés sur une tâche, et quels indicateurs clés (bande passante, réseau Infiniband, IOPS, bande passante disque local, espace disque, puissance) montrent‑ils ?"
  - "Quelles informations spécifiques sont affichées sur les pages détaillées d’une tâche CPU en vecteur et d’une tâche GPU (statut, script de soumission, commande de soumission, autres jobs de l’array, etc.) ?"
  - "Quel est le rapport recommandé entre le nombre total de threads (Running + Sleeping) et le nombre de cœurs alloués pour une tâche multithread ?"
  - "Pourquoi la présence de threads « Sleeping » est‑elle considérée comme normale pour certains types de programmes comme Java, Matlab ou les logiciels commerciaux ?"
  - "Quels autres paramètres sont mentionnés concernant les applications du programme exécutées au fil du temps ?"
  - "Pourquoi le script de soumission n’est‑il pas disponible lorsqu’une tâche interactive est lancée ?"
  - "Comment accéder au répertoire et à la commande de soumission en cliquant sur « Voir la commande de soumission » ?"
  - "Que représente l’image « Détail de la tâche.png » affichée dans le texte ?"
  - "Comment accéder à la page de votre compte GPU depuis l’ordonnanceur ?"
  - "Quels indicateurs le graphique « GPU » présente-t-il (SM actif, SM occupancy, Tensor, FP64/FP32/FP16) et quelles sont les valeurs cibles recommandées ?"
  - "Quels graphiques sont proposés pour suivre l’utilisation des ressources (CPU, mémoire, processus/threads, système de fichiers, mémoire GPU, puissance GPU, bande passante PCIe) et que représente chaque graphique ?"
  - "À quoi sert l’interface mémoire de l’appareil mentionnée dans le texte ?"
  - "Que représente le graphique de puissance GPU présenté dans l’article ?"
  - "Quel type de connexion est utilisé pour mesurer la bande passante du GPU selon le texte ?"
  - "Quels graphiques sont utilisés pour visualiser l’évolution de la bande passante réseau d’un nœud et quelles périodes d’activité (ex. : transferts massifs, communications MPI) peuvent‑elles révéler ?"
  - "Comment les différentes sections des « Statistiques d’un compte » (CPU et GPU) permettent‑elles de suivre l’utilisation, la priorité et le gaspillage des cœurs CPU et de la mémoire par chaque utilisateur du groupe ?"
  - "Quels indicateurs sont présentés pour mesurer les performances du disque local (IOPS, bande passante) ainsi que la consommation d’énergie du nœud, et comment ces données sont‑elles affichées graphiquement ?"
  - "Que représente le graphique situé à gauche dans la visualisation de votre activité sur les systèmes de fichiers ?"
  - "Quelle métrique est affichée à droite du graphique et que mesure-t-elle ?"
  - "Comment les indicateurs IOPS et bande passante peuvent-ils être exploités pour évaluer les performances de vos serveurs ?"
  - "Quels indicateurs sont présentés pour suivre l’utilisation et le gaspillage des GPU au sein d’un groupe ?"
  - "Comment les statistiques d’utilisation des ressources (CPU, mémoire, bande passante, IOPS) sont‑elles affichées pour chaque machine virtuelle du cloud ?"
  - "Quels graphiques permettent d’analyser l’activité des utilisateurs sur le système de fichiers ainsi que la liste des tâches récentes du groupe ?"
  - "Quels indicateurs de performance (CPU, mémoire, bande passante disque, IOPS disque, bande passante réseau) sont mesurés pour chaque machine virtuelle ?"
  - "Quelles périodes (dernier mois, dernière semaine, dernier jour, dernière heure) peuvent être sélectionnées pour afficher les statistiques d’une machine virtuelle ?"
  - "Comment ces statistiques sont‑elles présentées dans l’interface (par exemple sous forme de tableau ou de graphique) ?"
  - "Quel nombre de cœurs CPU est illustré dans le premier diagramme ?"
  - "Quelle capacité de mémoire cloud est représentée dans l’image « Mémoire cloud.png » ?"
  - "Comment les valeurs de bande passante disque, d’IOPS disque et de bande passante réseau se comparent‑elles entre elles dans les graphiques présentés ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# Overview

The Metrix portal is a website for Alliance users. It leverages information collected from compute nodes and management servers to interactively generate data, allowing users to track their resource usage (CPU, GPU, memory, file system) in real-time.

| Cluster | URL |
| :------ | :-------------------------------------------- |
| Rorqual | [https://metrix.rorqual.alliancecan.ca](https://metrix.rorqual.alliancecan.ca) |
| Narval  | [https://metrix.narval.alliancecan.ca](https://metrix.narval.alliancecan.ca) |
| Nibi    | [https://portal.nibi.sharcnet.ca](https://portal.nibi.sharcnet.ca)         |
| tamIA   | [https://portail.tamia.ecpia.ca](https://portail.tamia.ecpia.ca)           |
| Vulcan  | [https://metrix.vulcan.alliancecan.ca](https://metrix.vulcan.alliancecan.ca) |

**File System Performance**

This section presents bandwidth and metadata operation graphs, along with the following visualization options: last week, last day, and last hour.

**Login Nodes**

CPU, memory, system load, and network usage statistics are displayed in this tab, with the following visualization options: last week, last day, and last hour.

**Scheduling**

This tab presents statistics on allocated cluster cores and GPUs, with the following visualization options: last week, last day, and last hour.

**Scientific Software**

The most used software, along with CPU cores and GPUs, are presented in graph format.

**Data Transfer Nodes**

Bandwidth statistics for data transfer nodes are presented in this tab.

# User Summary

Under the User Summary tab, you will find your quotas for the different file systems, followed by your last 10 jobs. You can select a job by its number to access its detailed page. Additionally, by clicking **(More details)**, you will be redirected directly to the **Job Statistics** tab, where you will find all your jobs.

# Job Statistics

The first block displays your current usage (CPU core, memory, and GPUs). These statistics represent the average resources used by all running jobs. You can easily compare your allocated resources with your actual usage.

You then have access to an average of the last few days, presented in a graph format.

Next, you will find a representation of your activity on the file systems. On the left, a graph shows the number of disk write commands you have performed (*input/output operations per second (IOPS)*). On the right, you see the amount of data transferred to the servers over a given period (Bandwidth).

The following section presents all the jobs you have submitted, which are currently running or pending. In the upper left, you can filter jobs by status (OOM, completed, running, etc.). In the upper right, you can search by Job ID or name. Finally, in the lower right, an option allows you to quickly navigate between pages by making multiple jumps.

## CPU Job Page

At the top, you have the job name, its number, your username, and the status. Details of your submission script are displayed by clicking **View job script**. If the job was launched in interactive mode, the submission script will not be available.

The working directory and submission command are accessible by clicking **View submission command**.

The next section is dedicated to scheduler information. You can access your CPU account tracking page by clicking on your account number.

In the **Resources** section, you can get an initial overview of your job's resource utilization by comparing the **Allocated** and **Used** columns for the various listed parameters.

The **CPU** graph allows you to visualize the CPU cores you requested over time. On the right, you can select/deselect different cores as needed. Note that for very short jobs, this graph is not available.

The **Memory** graph allows you to visualize your requested memory usage over time.

The **Process and threads** graph allows you to observe various parameters related to processes and threads. Ideally, for a multithreading job, the sum of the *Running threads* and *Sleeping threads* parameters should not exceed twice the number of cores requested. However, it is quite normal to have some processes in *sleeping* mode (*Sleeping threads*) for certain types of programs (Java, Matlab, commercial software, or complex programs). You also have the program applications executed over time as a parameter.

The following graphs represent file system usage for the current job, not the entire node. On the left, a representation of the number of input/output operations per second (IOPS) is displayed. On the right, the graph illustrates the data transfer rate between the job and the file system over time. This graph helps identify periods of intense activity or low file system utilization.

For node-wide resource statistics, be aware that they can be inaccurate if the node is shared among multiple users. The graph on the left illustrates the evolution of bandwidth used by the job over time, in relation to software, licenses, etc. The graph on the right represents the evolution of network bandwidth used by a job or a set of jobs via the Infiniband network, over time. It can show periods of massive data transfer (e.g., reading/writing to a file system (Lustre), MPI communication between nodes).

The graph on the left illustrates the evolution of the number of input/output operations per second (IOPS) performed on the local disk over time. The one on the right shows the evolution of bandwidth used on the local disk over time, i.e., the amount of data read or written per second.

A graphical representation of local disk space usage.

A graphical representation of power consumption.

## CPU Job Page (Job Array)

The page for a CPU job within a job array is identical to that of a regular CPU job, with the exception of the "Other jobs in the array" section. This table lists other job numbers part of the same job array, along with information on their status, name, start time, and end time.

## GPU Job Page

At the top of the page, you have the job name, its number, your username, and the status. Details of your submission script are displayed by clicking **View job script**. If you launched an interactive job, the submission script is not available.

The working directory and submission command are accessible by clicking **View submission command**.

The following section is reserved for scheduler information. You can access your GPU account page by clicking on your account number.

In the **Resources** section, you can get an initial overview of your job's resource utilization by comparing the **Allocated** and **Used** columns for the various listed parameters.

The **CPU** graph allows you to visualize the CPU cores you requested over time. On the right, you can select/deselect different cores as needed. Note that for very short jobs, this graph is not available.

The **Memory** graph allows you to visualize your requested memory usage for the CPU over time.

The **Process and threads** graph allows you to observe various parameters related to processes and threads.

The following graphs represent file system usage for the current job, not the entire node. On the left, a representation of the number of input/output operations per second (IOPS) is displayed. On the right, the graph illustrates the data transfer rate between the job and the file system over time. This graph helps identify periods of intense activity or low file system utilization.

The **GPU** graph represents your GPU usage. The *Streaming Multiprocessors* (SM) active parameter indicates the percentage of time the GPU executes a warp (a group of consecutive threads) in the last sampling window. This value should ideally be around 80%. For *SM occupancy* (defined as the ratio of warps assigned to an SM to the maximum number of warps an SM can handle), a value around 50% is generally expected. Regarding the *Tensor* parameter, the value should be as high as possible. Ideally, your code should leverage this part of the GPU, which is optimized for multidimensional matrix multiplications and convolutions. Finally, for floating-point operations (FP64, FP32, and FP16), you should observe significant activity on only one of these types, depending on the precision used by your code.

On the left, a graph indicates the memory used by the GPU. On the right, a graph shows the GPU's memory access cycles, representing the percentage of cycles during which the device's memory interface is active for sending or receiving data.

The GPU power graph displays the evolution of the GPU's power consumption (in watts) over time.

This next graph shows the GPU bandwidth on the PCIe bus (or PCI Express, for Peripheral Component Interconnect Express).

For node-wide resource statistics, be aware that they can be inaccurate if the node is shared among multiple users. The graph on the left illustrates the evolution of bandwidth used by the job over time, in relation to software, licenses, etc. The graph on the right represents the evolution of network bandwidth used by a job or a set of jobs via the Infiniband network, over time. It can show periods of massive data transfer (e.g., reading/writing to a file system (Lustre), MPI communication between nodes).

The graph on the left illustrates the evolution of the number of input/output operations per second (IOPS) performed on the local disk over time. The one on the right shows the evolution of bandwidth used on the local disk over time, i.e., the amount of data read or written per second.

A graphical representation of local disk space usage.

A graphical representation of power consumption.

# Account Statistics

The **Account Statistics** section groups your group's usage into two subsections: CPU and GPU.

## CPU Account Statistics

Here you will find the sum of your group's requests for CPU cores, as well as their corresponding utilization over the last few months. You can also track the evolution of your priority, which varies based on your usage.

This graph shows the most commonly used applications.

Here you can view the resource usage by each user in your group.

This graph shows the evolution over time of wasted CPU cores by each user in the group.

Here you can view the memory usage by each user in your group.

This graph represents the memory wasted by each user.

Next, you will find a representation of your activity on the file systems. On the left, a graph shows the number of disk write commands you have performed (Input/Output Operations Per Second (IOPS)). On the right, you see the amount of data transferred to the servers over a given period (Bandwidth).

You have a list of the latest jobs that have been executed for the entire group.

## GPU Account Statistics

Here you will find the sum of your group's GPU requests, as well as the corresponding utilization over the last few months. You can also track the evolution of your priority, which varies based on your usage.

This graph represents the most commonly used applications.

Here you can view the resource usage by each user in your group.

The following graph represents, over time, the amount of GPU wasted per user.

Next, you have the CPU cores allocated and used in your GPU jobs.

This figure illustrates the wasted CPUs in the context of your GPU jobs.

Here you can visualize memory usage for each user in your group.

This graph illustrates the memory wasted by each user.

Next, you will find a representation of your activity on the file systems. On the left, a graph shows the number of disk write commands you have performed (Input/Output Operations Per Second (IOPS)). On the right, you see the amount of data transferred to the servers over a given period (Bandwidth).

Here is a list of the latest jobs executed at your group level.

# Cloud Statistics

The first table, "Your Instances", presents all virtual machines associated with an account. The "Flavor" column refers to the [virtual machine type](../cloud/virtual_machine_flavors.md). The "UUID" column corresponds to a unique identifier assigned to each virtual machine.

Subsequently, each virtual machine has its own usage statistics (CPU Cores, Memory, Disk Bandwidth, Disk IOPS, and Network Bandwidth) displayable for the last month, last week, last day, or last hour.