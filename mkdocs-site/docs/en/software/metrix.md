---
title: "Metrix/en"
tags:
  []

keywords:
  []
---

<span id="Aperçu"></span>
= Summary =

[thumb|900px|center](file:aperçu-de-la-page-d'accueil-du-portailen.png.md)

The Metrix portal is a website for Alliance users. It collects information on compute nodes and management servers, to interactively generate data so you can track your resource usage (CPUs, GPUs, memory, filesystems) in real time.

{| class="wikitable"
|-
| Rorqual
| [https://metrix.rorqual.alliancecan.ca](https://metrix.rorqual.alliancecan.ca)
|-
| Narval
| [https://portail.narval.calculquebec.ca](https://portail.narval.calculquebec.ca)
|-
| Nibi
| [https://portal.nibi.sharcnet.ca](https://portal.nibi.sharcnet.ca)
|}

 
<b>Filesystem performance</b>

Here you have the graphs for bandwidths and metadata operations, along with viewing options (last week, last day and last hour).

<b>Login nodes</b>

Under this tab are presented  usage statistics for CPUs, memory, system load, and network, with viewing options (last week, last day, and last hour).

<b>Scheduler</b>

This tab shows statistics for the cluster's allocated cores and GPUs, with viewing options (last week, last day, and last hour).

<b>Scientific software</b>

These graphs show the software most frequently used, with CPU cores and GPUs.

<b>Data transfer nodes</b>

Bandwidth statistics for data transfer nodes are shown under this tab.

= User portal =
Under this tab, you find your quotas for the filesystems, followed by your 10 last jobs. You can select a job by its number to see the details. Also, by clicking on <span style="color:#0000FF">(More details)</span>, you are redirected to the *Job statistics* tab, where all your jobs are listed.
[thumb|900px|center](file:homeen.png.md)
[thumb|900px|center](file:scratchen.png.md)
[thumb|900px|center](file:projecten.png.md)
[900px|thumb|center](file:portail-utilisateur-10-dernières-tâchesen.png.md)

= Job statistics =
The first block shows your current usage (CPU cores, memory, and GPUs). These statistics represent the average usage by all currently running jobs. You can easily compare the resources allocated to you with those you actually use.
[thumb|900px|center](file:utilisation-en-coursen.png.md)

You then have a graph of the average for the last few days.
[thumb|900px|center](file:coeur-cpu-mémoireen.png.md)

Next is a representation of your activity on the filesystems. On the left, the graph shows the number of disk write commands you have performed (*input/output operations per second*). On the right, you see the amount of data transferred to the servers over a given period (*Bandwidth*).
[thumb|900px|center](file:système-de-fichieren.png.md)

The next section shows all the jobs you have already started, which are currently running or pending. In the top left corner, you can filter jobs by their status (OOM, completed, running, etc.). In the top right corner, you can search by job ID or by job name. Finally, in the bottom right corner, there is an option to quickly navigate between pages by performing multiple jumps. 
[thumb|900px|center](file:vos-tâches-top-2en.png.md)

[thumb|900px|center](file:vos-tâches-bottom-2.png.md)

## CPU jobs 
At the top, you see the job name, its number, your username, and the status. Details of your submission script are displayed by clicking on <span style="color:white; background-color:blue">Show submitted job script</span>. If the job was launched in interactive mode, the submission script will not be available.
[thumb|900px|center](file:détails-sur-la-tâche-2en.png.md)

The working directory and the submission command can be seen by clicking on  <span style="color:white; background-color:blue">Show submit command</span>.
[thumb|900px|center](file:commande-de-soumission-3en.png.md)

The next section shows information on the scheduler. To display the information on your CPU account, click on your account number. 
[thumb|900px|center](file:information-ordonnanceur-2en.png.md)

In the **Ressources** section, you can see the resources used by your job by comparing columns **Allocated** and **Used** for the listed parameters.
[thumb|900px|center](file:ressourcesen.png.md)

The **CPU** graph shows the CPU cores you have requested, over time. On the right, you can select the cores you want to see. Please note that this graph is not available for very short jobs.
[thumb|900px|center](file:ressources-utilisées-détails-2en.png.md)

This graphs shows the usage of the memory you requested, over time.  
[thumb|900px|center](file:mémoireen.png.md)

The **Processes and threads** graph shows different parameters. For a multithread job, adding parameters **Running threads** and **Sleeping threads** should  not exceed twice the number of cores requested. However, having some *Sleeping threads* is normal for certain types of programs  (java, Matlab, commercial software or complex programs). There is also a parameter for the program applications that have been executed over time. 
[thumb|900px|center](file:process-and-threadsen.png.md)

The following graphs show filesystem usage by the current job, and not for the entire node. On the left, we have the number of I/O operations per second (IOPS). On the right, the graph illustrates the data transfer rate between the job and the filesystem, over time. This helps identify periods of high or low filesystem activity.
[thumb|900px|center](file:système-de-fichier-2en.png.md)

Resource statistics for the entire node may be inaccurate if the node is shared by multiple users. The graph on the left shows the evolution of the bandwidth used by the job over time, in relation to software, licenses, etc. The graph on the right shows the evolution of the network bandwidth used by a job or a set of jobs via the Infiniband network, over time. We can observe periods of massive data transfer (e.g., reading/writing on a filesystem (Lustre), MPI communication between nodes).
[thumb|900px|center](file:ressource-du-nœud-au-complet.png.md)

The graph on the left shows the evolution of the number of input/output operations per second (IOPS) performed on the local disk, over time. The graph on the right shows the evolution of the bandwidth used on the local disk over time, that is, the amount of data read or written per second.
[thumb|900px|center](file:iops,-bande-passanteen.png.md)

Usage of local disk space
[thumb|900px|center](file:espace-utilisé-sur-le-disque-localen.png.md)

Power consumption
[thumb|900px|center](file:puissanceen.png.md)

<span id="Page_d&#039;une_tâche_CPU_(vecteur_de_tâches,_job_array)"></span>
## CPU jobs (job arrays)

The page for a CPU job in an array is the same as that for a regular CPU job, except for the **Other jobs in the array** section. The table lists the other job numbers that are part of the job array, along with information about their status, name, start time, and finish time.

[thumb|900px|center](file:cpu-job-arrayen.png.md)

<span id="Page_d&#039;une_tâche_GPU"></span>
## GPU jobs 

At the top, you see the job name, its number, your username, and the status. Details of your submission script are displayed by clicking on <span style="color:white; background-color:blue">Show submitted job script</span>. If the job was launched in interactive mode, the submission script will not be available.
[thumb|900px|center](file:détails-sur-la-tâcheen.png.md)

The working directory and the submission command are shown by clicking on  <span style="color:white; background-color:blue">Show submit command</span>.
[thumb|900px|center](file:commande-de-soumission-gpuen.png.md)

The next section shows information on the scheduler. To display the information on your GPU account, click on your account number. 
[thumb|900px|center](file:information-ordonnanceur-gpuen.png.md)

In the **Ressources** section, you can see the resources used by your job by comparing columns **Allocated** and **Used** for the listed parameters.
[thumb|900px|center](file:ressources-gpuen.png.md)

The **CPU** graph shows the CPU cores you have requested, over time. On the right, you can select the cores you want to see. Please note that this graph is not available for very short jobs.
[thumb|900px|center](file:ressources-utilisées-détailsen.png.md)

This next graph shows the usage of the memory you requested for CPUs, over time.  
[thumb|900px|center](file:mémoire-gpuen.png.md)

The **Processes and threads** graph shows different parameters.

[thumb|900px|center](file:processes-and-threads-gpuen.png.md)

The following graphs show the usage of the filesystem by the current job, and not for the entire node. On the left, we have the number of I/O operations per second (IOPS). On the right, the graph illustrates the data transfer rate between the job and the filesystem, over time. This helps identify periods of high or low filesystem activity.
[thumb|900px|center](file:système-de-fichier-gpuen.png.md)

The GPU graph shows your GPU usage. The *Streaming Multiprocessors* (SM) setting indicates the percentage of time taken by the GPU to execute a warp (a group of consecutive threads) in the last sampling. This value should be around 80%. For *SM occupancy* (defined as the ratio between the number of warps assigned to an SM and the maximum number of warps an SM can handle), a value around 50% is generally expected. Regarding the *Tensor* setting, the value should be as high as possible. Ideally, your code should use this part of the GPU, which is optimized for multiplications and convolutions of multidimensional matrices. Finally, for FP64, FP32, and FP16 floating-point operations, you should observe significant activity on only one of these, depending on the precision specified by your code. [thumb|900px|center](file:gpu-compute-cycles-useden.png.md)

On the left, you have a graph showing the memory used by the GPU. On the right, a graph of the GPU's memory access cycles shows the percentage of cycles during which the device's memory interface is active sending or receiving data.
[thumb|900px|center](file:gpumemoryen.png.md)

The GPU power graph displays the evolution of the GPU's power consumption (in watts), over time.
[thumb|900px|center](file:gpupoweren.png.md)

This next graph shows the GPU bandwidth on the PCIe bus (or PCI Express, for Peripheral Component Interconnect Express).
[thumb|900px|center](file:gpu-bandwidthen.png.md)

For statistics on the resources of the entire node, please note that they may be inaccurate if the node is shared among multiple users. The graph on the left shows the evolution of the bandwidth used by the job, over time, in relation to software, licenses, etc. The graph on the right shows the evolution of the network bandwidth used by a job or set of jobs via the Infiniband network, over time. Periods of massive data transfer can be observed (e.g., reading/writing to a filesystem (Lustre), MPI communication between nodes).
[thumb|900px|center](file:node-resourcesen.png.md)

The graph on the left shows the evolution of the number of input/output operations per second (IOPS) performed on the local disk, over time. The graph on the right shows the evolution of the bandwidth used on the local disk, over time; that is, the amount of data read or written per second.
[thumb|900px|center](file:iopsen.png.md)

Usage of local disk space
[thumb|900px|center](file:espace-utiliséen.png.md)

Power consumption
[thumb|900px|center](file:puissance-utiliséen.png.md)

<span id="Statistiques_d&#039;un_compte"></span>
= Account statistics =

The *Account Statistics* section shows your group's usage in two subsections: CPU and GPU.
[thumb|900px|center](file:portail-utilisateur-vos-comptesen.png.md)

<span id="Statistiques_d&#039;un_compte_CPU"></span>
## CPU accounts 

Here you have the total number of CPU cores requested by your group, along with their corresponding usage over the past few months. You can also track your priority status, which varies based on your usage.
[thumb|900px|center](file:account-usageen.png.md)

Applications used most frequently
[thumb|900px|center](file:application-used-cpuen.png.md)

Here are the resources used by each user in your group.
[thumb|900px|center](file:utilisation-détaillée-par-utilisateuren.png.md)

This graph shows the CPU cores wasted by each user, over time.
[thumb|900px|center](file:coeur-cpu-gaspilléen.png.md)

Here you see the memory used by each user in your group.
[thumb|900px|center](file:mémoire-compte.png.md)

This graph shows the memory wasted by each user.
[thumb|900px|center](file:mémoire-gaspillée.png.md)

You then have a representation of your activity on the filesystems. On the left, the graph shows the number of disk write commands you have performed. (*input/output operations per second (IOPS)*) On the right, you see the amount of data transferred to the servers over a given period. (Bandwidth)
[thumb|900px|center](file:système-de-fichier-compte.png.md)

This lists the last jobs ran by all members of the group.
[thumb|900px|center](file:tâches-en-cours-1.png.md)
[thumb|900px|center](file:tâche-en-cours-2.png.md)

<span id="Statistiques_d&#039;un_compte_GPU"></span>
## GPU accounts 

Here you can see the total GPU requests for your group, along with their usage over the past few months. You can also track your priority, which varies based on your usage. 
[thumb|900px|center](file:utilisation-compte-gpu-détails.png.md)

This graph shows the software more frequently used.
[thumb|900px|center](file:application-utilisé-compte-gpu.png.md)

Here you see the resources used by each user in your group.
[thumb|900px|center](file:gpu-utilisé-par-utilisateur-compte-gpu.png.md)

This graph shows the quantity of GPUs wasted by each user.
[thumb|900px|center](file:gpu-gaspillé-compte-gpu.png.md)

Here you see the CPU allocated and used by your GPU jobs.
[thumb|900px|center](file:cpu-compte-gpu.png.md)

This graph shows the CPUs wasted by your GPU jobs.
[thumb|900px|center](file:coeur-cpu-gaspillé-compte-gpu.png.md)

Here you see the memory used by each user in your group.
[thumb|900px|center](file:mémoire-compte-gpu.png.md)

This graph shows the memory wasted by each user.
[thumb|900px|center](file:mémoire-gaspillée-gpu.png.md)

You then have a representation of your activity on the filesystems. On the left, the graph shows the number of disk write commands you have performed. (*input/output operations per second (IOPS)*) On the right, you see the amount of data transferred to the servers over a given period. (Bandwidth)
[thumb|900px|center](file:système-de-fichier-gpu.png.md)

Here you see the last jobs that were run by your group.
[thumb|900px|center](file:tâches-en-cours-1.png.md)
[thumb|900px|center](file:tâche-en-cours-2.png.md)

<span id="Statistiques_du_cloud"></span>
= Cloud statistics =

The table *Your Instances* displays all the virtual machines associated with your account. The *Flavor* column refers to the virtual machine type. The *UUID* column is a unique identifier assigned to each virtual machine.

[thumb|900px|center](file:tableau-vos-instancesen.png.md)

Each virtual machine has its own usage statistics (CPU cores, memory, disk bandwidth, IOPS and network bandwidth) that can be shown for the last month, week, day or hour.

[thumb|900px|center](file:coeurs-cpuen.png.md)

[thumb|900px|center](file:mémoire-clouden.png.md)

[thumb|900px|center](file:bande-passante-disque-cloudautreen.png.md)

[thumb|900px|center](file:iops-disqueen.png.md)

[thumb|900px|center](file:bande_passante_réseau_clouden.png.md)