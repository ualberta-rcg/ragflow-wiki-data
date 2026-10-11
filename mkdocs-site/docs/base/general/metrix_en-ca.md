---
title: "Metrix/en-ca"
slug: "metrix_en-ca"
lang: "base"

source_wiki_title: "Metrix/en-ca"
source_hash: "88a1ed8b1565044362f6ff6c49d29ad1"
last_synced: "2026-10-11T01:39:35.690021+00:00"
last_processed: "2026-10-11T02:42:34.934423+00:00"

tags:
  []

keywords:
  - "bande passante réseau"
  - "script de soumission"
  - "CPU gaspillé"
  - "Bande passante disque"
  - "graphique CPU"
  - "tâche GPU"
  - "statistiques CPU"
  - "bus PCIe"
  - "statistiques d'un compte"
  - "IOPS (opérations d’entrée/sortie par seconde)"
  - "utilisation des ressources"
  - "Mémoire"
  - "Cœur CPU"
  - "bande passante PCIe"
  - "interface mémoire"
  - "IOPS disque"
  - "utilisation du disque"
  - "ordonnanceur"
  - "gaspillage GPU"
  - "GPUs"
  - "ressources allouées/utilisées"
  - "IOPS (opérations d'entrée/sortie)"
  - "processus en mode dormant"
  - "utilisation du système de fichiers"
  - "activité sur les systèmes de fichiers"
  - "quotas des systèmes de fichiers"
  - "cœurs CPU alloués"
  - "Voir la commande de soumission"
  - "statistiques d'utilisation"
  - "CPU"
  - "tâches en cours"
  - "commande de soumission"
  - "quantité de données transférées"
  - "Bande passante réseau"
  - "mémoire"
  - "graphique GPU"
  - "Cœurs CPU"
  - "Mémoire cloud"
  - "bande passante GPU"
  - "machine virtuelle"
  - "portail Metrix"
  - "Running threads"
  - "commandes d’écriture sur disque"
  - "script de la tâche"
  - "tâche multifils"
  - "consommation énergétique"
  - "Statistiques des tâches"
  - "graphique de puissance GPU"
  - "statistiques GPU"
  - "tâche interactive"
  - "ressources allouées"
  - "Sleeping threads"
  - "tâche CPU (vecteur de tâches)"
  - "utilisation actuelle"
  - "bande passante"
  - "IOPS"
  - "instances virtuelles"
  - "nombre de cœurs"

questions:
  - "À quoi sert le portail Metrix et quelles données en temps réel permet‑il aux usagers de suivre ?"
  - "Quels types de statistiques sont présentés dans les différents onglets du portail (performance du système de fichiers, nœuds de connexion, ordonnancement, logiciels scientifiques, nœuds de transfert de données) ?"
  - "Comment les onglets « Sommaire utilisateur » et « Statistiques des tâches » aident‑ils les utilisateurs à contrôler leurs quotas et l’utilisation de leurs ressources ?"
  - "Quelles ressources sont affichées dans le premier bloc des statistiques ?"
  - "Comment les statistiques représentent‑elles la moyenne des ressources utilisées par les tâches en cours ?"
  - "À quoi servent ces statistiques pour comparer les ressources allouées et celles réellement utilisées ?"
  - "Comment visualiser la moyenne d’utilisation des derniers jours et quels types de graphiques sont présentés ?"
  - "Quelles options de filtrage et de recherche sont disponibles pour naviguer parmi les tâches en cours, terminées ou en attente ?"
  - "Comment accéder aux détails d’une tâche CPU, y compris le script de soumission, la commande de soumission et les graphiques d’utilisation des ressources (CPU, mémoire, processus et threads) ?"
  - "Quels graphiques sont présentés pour visualiser l’utilisation du système de fichiers d’une tâche et quelles informations permettent‑ils d’identifier ?"
  - "Comment les différents graphiques (bande passante du nœud, IOPS, bande passante disque local, utilisation du disque et de la puissance) décrivent‑ils l’évolution des ressources du nœud complet au fil du temps ?"
  - "Quelles sections et quelles informations spécifiques sont affichées sur les pages détaillées d’une tâche CPU en vecteur de tâches et d’une tâche GPU ?"
  - "Quelle est la règle idéale concernant la somme des threads «Running» et «Sleeping» par rapport au nombre de cœurs demandés ?"
  - "Pourquoi la présence de threads «Sleeping» est‑elle considérée comme normale pour certains programmes comme Java, Matlab ou des logiciels complexes ?"
  - "Quels autres paramètres sont mentionnés concernant les applications du programme exécutées au fil du temps ?"
  - "Que se passe-t-il lorsqu’une tâche interactive est lancée concernant le script de soumission ?"
  - "Comment accéder au répertoire et à la commande de soumission d’une tâche via l’interface ?"
  - "Où peut‑on visualiser le script de la tâche et la commande de soumission dans le système ?"
  - "Quels indicateurs sont affichés dans la section « Ressources » pour comparer les ressources allouées et utilisées d’une tâche ?"
  - "Comment interpréter les valeurs du graphique GPU relatives aux Streaming Multiprocessors (SM), au SM occupancy et aux différents types de calculs en virgule flottante ?"
  - "Quels graphiques permettent de suivre l’utilisation du système de fichiers et la bande passante PCIe du GPU, et quelles informations clés révèlent‑ils sur la performance de la tâche ?"
  - "Quel rôle joue l’interface mémoire de l’appareil lorsqu’elle est active pour l’envoi ou la réception de données ?"
  - "Comment le graphique de puissance GPU représente‑t-il l’évolution de la consommation énergétique du GPU au fil du temps ?"
  - "Que montre le graphique de la bande passante du GPU sur le bus PCIe (PCI Express) et pourquoi est‑il important ?"
  - "Quels graphiques permettent de suivre l’évolution de la bande passante réseau utilisée par les tâches via Infiniband et comment identifier les périodes de transfert massif de données ?"
  - "Comment les statistiques d’un compte CPU présentent‑elles la consommation totale de cœurs, l’évolution de la priorité, les applications les plus utilisées ainsi que la mémoire et les cœurs gaspillés par chaque utilisateur du groupe ?"
  - "Quels indicateurs sont fournis pour mesurer les performances du disque local (IOPS et bande passante), l’utilisation de l’espace disque et la puissance consommée par le nœud ?"
  - "Quel indicateur le graphique de gauche mesure‑t‑il exactement dans votre activité sur les systèmes de fichiers ?"
  - "Quel type de donnée le graphique de droite représente‑t‑il concernant le transfert vers les serveurs ?"
  - "Comment interpréter conjointement les IOPS et la bande passante pour évaluer la performance de votre système ?"
  - "Quels indicateurs sont présentés pour suivre l’utilisation et le gaspillage des GPU au sein d’un groupe ?"
  - "Comment les statistiques d’utilisation des ressources (CPU, mémoire, bande passante, IOPS) sont‑elles affichées pour chaque machine virtuelle du compte cloud ?"
  - "Quels graphiques permettent d’analyser la répartition des tâches et l’activité des utilisateurs sur le système de fichiers ?"
  - "Quels types de statistiques d'utilisation sont disponibles pour chaque machine virtuelle ?"
  - "Sur quelles périodes temporelles peut‑on consulter ces statistiques ?"
  - "Comment les machines virtuelles sont‑elles présentées dans le tableau illustré ?"
  - "Quels sont les indicateurs de performance présentés dans les images (cœurs CPU, mémoire cloud, bande passante disque, IOPS disque, bande passante réseau) et à quoi servent‑ils dans le contexte du cloud ?"
  - "Comment la bande passante du disque cloud diffère‑t‑elle de la bande passante du réseau cloud selon les graphiques affichés ?"
  - "Quels facteurs peuvent influencer les IOPS d’un disque cloud et comment ces valeurs se comparent‑elles aux capacités CPU et mémoire présentées ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Overview

The Metrix portal is a website for Alliance users. It leverages information collected from compute nodes and management servers to interactively generate data, allowing users to track their real-time resource usage (CPU, GPU, memory, file system).

| Cluster | URL |
| :------ | :-- |
| Rorqual | [https://metrix.rorqual.alliancecan.ca](https://metrix.rorqual.alliancecan.ca) |
| Narval | [https://metrix.narval.alliancecan.ca](https://metrix.narval.alliancecan.ca) |
| Nibi | [https://portal.nibi.sharcnet.ca](https://portal.nibi.sharcnet.ca) |
| tamIA | [https://portail.tamia.ecpia.ca](https://portail.tamia.ecpia.ca) |
| Vulcan | [https://metrix.vulcan.alliancecan.ca](https://metrix.vulcan.alliancecan.ca) |

**File System Performance**
This section provides bandwidth and metadata operation metrics, with visualization options for the last week, last day, and last hour.

**Login Nodes**
CPU, memory, system load, and network usage statistics are presented in this tab, with visualization options for the last week, last day, and last hour.

**Scheduling**
This tab presents statistics on allocated CPU cores and GPUs for the cluster, with visualization options for the last week, last day, and last hour.

**Scientific Software**
The most used software applications with CPU cores and GPUs are presented.

**Data Transfer Nodes**
Bandwidth statistics for data transfer nodes are presented in this tab.

## User Summary
Under the User Summary tab, you will find your quotas for different file systems, followed by your 10 most recent jobs. You can select a job by its number to access its detailed page. Additionally, by clicking on `(More details)`, you will be redirected directly to the **Job Statistics** tab, where you can view all your jobs.

## Job Statistics
The first block displays your current usage (CPU core, memory, and GPUs). These statistics represent the average resources used by all currently running jobs. You can easily compare the resources allocated to you with those you are actually using.

You then have access to a daily average for recent days.

Next, you'll find a representation of your file system activity. This includes the number of disk write operations you have performed (Input/Output Operations Per Second (IOPS)) and the amount of data transferred to the servers over a given period (bandwidth).

The next section presents all jobs you have launched, which are currently running or pending. You can filter jobs by status (OOM, completed, running, etc.). You can also search by job ID or name. Finally, an option allows you to quickly navigate between pages by making multiple jumps.

### CPU Job Page
At the top of the page, you'll find the job name, its number, your username, and the status. Details of your submission script are displayed by clicking on `See job script`. If the job was launched in interactive mode, the submission script will not be available.

The working directory and submission command are accessible by clicking on `See submission command`.

The next section is dedicated to scheduler information. You can access your CPU account tracking page by clicking on your account number.

In the **Resources** section, you can get an initial overview of your job's resource usage by comparing the **Allocated** and **Used** columns for the various listed parameters.

The **CPU** details allow you to see the CPU cores you requested over time. You can select/deselect different cores as needed. Note that for very short jobs, this information is not available.

The **Memory** details allow you to see the memory usage you requested over time.

The **Process and threads** details allow you to observe various parameters related to processes and execution threads. Ideally, for a multithreaded job, the sum of the **Running threads** and **Sleeping threads** parameters should not exceed twice the number of requested cores. However, it is entirely normal to have some processes in **dormant** (*Sleeping threads*) mode for certain types of programs (Java, MATLAB, commercial software, or complex programs). You also have the program applications executed over time as a parameter.

The following details represent file system usage for the current job, not the entire node. This includes the number of Input/Output Operations Per Second (IOPS) and the data transfer rate between the job and the file system over time. This information helps identify periods of intense activity or low file system utilization.

For full node resource statistics, be aware that these may be imprecise if the node is shared among multiple users. This section illustrates the evolution of bandwidth used by the job over time, in relation to software, licenses, etc. It also represents the evolution of network bandwidth used by a job or set of jobs via the Infiniband network over time. This allows observation of periods of massive data transfer (e.g., reading/writing to a file system (Lustre), MPI communication between nodes).

This section illustrates the evolution of Input/Output Operations Per Second (IOPS) performed on the local disk over time, and the evolution of bandwidth used on the local disk over time, i.e., the amount of data read or written per second.

Representation of local disk space usage.

Representation of power consumption.

### CPU Job Page (Job Array)
The CPU job page for a job array is identical to that of a regular CPU job, with the exception of the *Other jobs in the array* section. This section lists other job numbers belonging to the same job array, along with information on their status, name, start time, and end time.

### GPU Job Page
At the top of the page, you'll find the job name, its number, your username, and the status. Details of your submission script are displayed by clicking on `See job script`. If you launched an interactive job, the submission script is not available.

The directory and submission command are accessible by clicking on `See submission command`.

The next section is reserved for scheduler information. You can access your GPU account page by clicking on your account number.

In the **Resources** section, you can get an initial overview of your job's resource usage by comparing the **Allocated** and **Used** columns for the various listed parameters.

The **CPU** details allow you to see the usage of requested CPU cores over time. You can select/deselect different cores as needed. Note that for very short jobs, this information is not available.

The **Memory** details allow you to see the memory usage you requested for the CPUs over time.

The **Process and threads** details allow you to observe various parameters related to processes and execution threads.

The following details represent file system usage for the current job, not the entire node. This includes the number of Input/Output Operations Per Second (IOPS) and the data transfer rate between the job and the file system over time. This information helps identify periods of intense activity or low file system utilization.

The GPU details represent your GPU usage. The *Streaming Multiprocessors* (SM) active parameter indicates the percentage of time the GPU executes a warp (a group of consecutive threads) in the last sampling window. This value should ideally be around 80%. For *SM occupancy* (defined as the ratio of warps assigned to an SM to the maximum number of warps an SM can handle), a value around 50% is generally expected. Regarding the *Tensor* parameter, the value should be as high as possible. Ideally, your code should leverage this part of the GPU, optimized for multidimensional matrix multiplications and convolutions. Finally, for *Floating Point* operations (FP64, FP32, and FP16), you should observe significant activity on only one of these types, depending on the precision used by your code.

This section provides details on GPU memory usage and GPU memory access cycles. The latter represents the percentage of cycles during which the device's memory interface is active for sending or receiving data.

GPU power consumption details show the evolution of GPU energy consumption (in watts) over time.

This section shows the GPU bandwidth on the PCIe bus (or PCI Express, for Peripheral Component Interconnect Express).

For full node resource statistics, be aware that these may be imprecise if the node is shared among multiple users. This section illustrates the evolution of bandwidth used by the job over time, in relation to software, licenses, etc. It also represents the evolution of network bandwidth used by a job or set of jobs via the Infiniband network over time. This allows observation of periods of massive data transfer (e.g., reading/writing to a file system (Lustre), MPI communication between nodes).

This section illustrates the evolution of Input/Output Operations Per Second (IOPS) performed on the local disk over time, and the evolution of bandwidth used on the local disk over time, i.e., the amount of data read or written per second.

Representation of local disk space usage.

Representation of power consumption.

## Account Statistics
The **Account Statistics** section groups your group's usage into two subsections: CPU and GPU.

### CPU Account Statistics
Here you will find the sum of your group's CPU core requests, as well as their corresponding usage over the past months. You can also track the evolution of your priority, which varies based on your usage.

This section shows the most commonly used applications.

Here you can consult resource usage by each user in your group.

This section shows the evolution over time of wasted CPU cores by each user in the group.

Here you can consult memory usage by each user in your group.

This section represents the memory wasted by each user.

Next, you'll find a representation of your file system activity. This includes the number of disk write operations you have performed (Input/Output Operations Per Second (IOPS)) and the amount of data transferred to the servers over a given period (bandwidth).

You have a list of the most recent jobs that have been performed for the entire group.

### GPU Account Statistics
Here you will find the sum of your group's GPU requests, as well as their corresponding usage over the past months. You can also track the evolution of your priority, which varies based on your usage.

This section represents the most commonly used applications.

Here you can consult resource usage by each user in your group.

The following section represents, over time, the amount of GPU resources wasted per user.

Next, you have the CPU cores allocated and used in your GPU jobs.

This section illustrates the wastage of CPUs within your GPU jobs.

Here you can view memory usage for each user in your group.

This section illustrates the memory wasted by each user.

Next, you'll find a representation of your file system activity. This includes the number of disk write operations you have performed (Input/Output Operations Per Second (IOPS)) and the amount of data transferred to the servers over a given period (bandwidth).

Here is a list of the most recent jobs performed by your group.

## Cloud Statistics
The first table, 'Your Instances,' presents all virtual machines associated with an account. The 'Flavor' column refers to the [virtual machine type](../cloud/virtual_machine_flavors.md). The 'UUID' column corresponds to a unique identifier assigned to each virtual machine.

Each virtual machine then has its own usage statistics (CPU Cores, Memory, Disk Bandwidth, Disk IOPS, and Network Bandwidth) available for the last month, last week, last day, or last hour.