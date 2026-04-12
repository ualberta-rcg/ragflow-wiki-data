---
title: "Estimer et prévenir le gaspillage des ressources"
slug: "estimer_et_prévenir_le_gaspillage_des_ressources"
lang: "base"

source_wiki_title: "Estimer et prévenir le gaspillage des ressources"
source_hash: "37acb6094ac88b4fe4de360f5c7e8098"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:57:50.250367+00:00"

tags:
  []

keywords:
  - "#SBATCH --cpus-per-task=2"
  - "mémoire"
  - "nœud nc30408"
  - "SBATCH"
  - "mémoire totale du nœud"
  - "GROMACS"
  - "tâche multiprocesseur"
  - "Cycle de calcul"
  - "mémoire par cœur"
  - "gaspillage observé"
  - "MIG"
  - "gaspillage de ressources"
  - "allocation de mémoire"
  - "utilisation"
  - "cycle de calcul GPU"
  - "utilisation des GPU"
  - "mémoire GPU"
  - "cœurs"
  - "SLURM_CPUS_PER_TASK"
  - "accélération GPU"
  - "MPS"
  - "graphique de la mémoire"
  - "demande trop élevée"
  - "paramètres de soumission"
  - "MPS (Multi-Process Service)"
  - "Processes and threads"
  - "graphique CPU"
  - "optimisation des ressources"
  - "utilisation du GPU"
  - "graphique GPU"
  - "processus"
  - "capacités du GPU"
  - "tâche GPU"
  - "utilisation du CPU"
  - "tâche multiprocesseur (MPI)"
  - "allocation de ressources"
  - "script de soumission"
  - "fils d'exécution actifs"
  - "GPU"
  - "fils d'exécutions"
  - "CPU"
  - "demande de mémoire"
  - "fils d'exécution"
  - "OMP_NUM_THREADS"
  - "choix de configuration"
  - "Python"
  - "tâche en série"
  - "graphique mémoire"
  - "gaspillage de CPU"
  - "tâches interactives"
  - "$SLURM_CPUS_PER_TASK"
  - "tâche multifil"
  - "cœurs demandés"
  - "vecteurs de tâches"
  - "cœurs de calcul"
  - "nœud GPU"
  - "cœurs alloués"
  - "--mem-per-cpu"
  - "--mem=0"
  - "test comparatif"

questions:
  - "Qu'est-ce qu'une tâche en série et pourquoi le fait de demander plusieurs cœurs pour celle-ci entraîne-t-il un gaspillage de ressources ?"
  - "Comment les graphiques d'utilisation du portail (CPU, mémoire et fils d'exécution) permettent-ils de détecter une surallocation des ressources ?"
  - "Quelles modifications doivent être apportées aux paramètres du script de soumission (notamment --cpus-per-task et --mem-per-cpu) pour corriger ce gaspillage ?"
  - "Comment le graphique \"Processes and threads\" permet-il de déterminer si une tâche soumise s'exécute en série ou en parallèle ?"
  - "Comment configurer les paramètres de cœurs et de mémoire dans un script de soumission Slurm pour une tâche multifil ?"
  - "Pourquoi est-il avantageux d'ajuster à la baisse la mémoire demandée lorsque le graphique indique une utilisation réelle bien inférieure à l'allocation initiale ?"
  - "Quel problème principal est mis en évidence par le graphique de la mémoire ?"
  - "Quelle est la différence entre la quantité de mémoire totale demandée et celle réellement utilisée ?"
  - "Quel paramètre est suggéré pour corriger cette allocation excessive de mémoire ?"
  - "Comment peut-on déterminer si une tâche multifil a demandé plus de cœurs que nécessaire ?"
  - "Quelle est la relation attendue entre le nombre de fils d'exécution actifs et les cœurs demandés ?"
  - "Quel est le rôle du script de soumission \"simple_job.sh\" présenté dans l'exemple ?"
  - "Comment doit-on ajuster les paramètres de cœurs et de mémoire dans un script Slurm lorsqu'une tâche multifil utilise moins de ressources que ce qui a été demandé ?"
  - "Quelles sont les caractéristiques principales d'une tâche multiprocesseur, notamment en ce qui concerne la gestion de la mémoire et l'utilisation des nœuds ?"
  - "Dans quel contexte précis est-il approprié et valide d'utiliser le paramètre `#SBATCH --mem=0` lors de la soumission d'une tâche ?"
  - "Comment peut-on déterminer si l'on a demandé plus de cœurs que nécessaire pour une tâche multiprocesseur ?"
  - "Quelles sont les ressources exactes (tâches, mémoire, temps) allouées par le script de soumission présenté dans l'exemple ?"
  - "Que représente le graphique illustrant les processus et les threads sur un système à 64 cœurs ?"
  - "Comment les graphiques d'utilisation du CPU permettent-ils d'identifier une surallocation de cœurs et quel paramètre Slurm doit être ajusté en conséquence ?"
  - "Quelle observation concernant le graphique de la mémoire justifie la réduction de la valeur allouée via l'option --mem-per-cpu ?"
  - "Pourquoi est-il erroné d'utiliser l'option --cpus-per-task=2 pour une tâche multiprocesseur non multifil et comment cette erreur se manifeste-t-elle visuellement ?"
  - "Pourquoi observe-t-on deux fois moins de fils d'exécution actifs que de cœurs alloués lors de l'utilisation de l'option `#SBATCH --cpus-per-task=2` ?"
  - "Quelle conclusion le texte tire-t-il concernant l'utilisation réelle des cœurs par chaque processus ?"
  - "Comment l'exemple du nœud « nc30408 » démontre-t-il concrètement cette différence entre les ressources allouées et les fils d'exécution actifs ?"
  - "Comment doit-on configurer la variable OMP_NUM_THREADS par rapport aux paramètres SBATCH pour optimiser une tâche GROMACS ?"
  - "Quelles sont les bonnes pratiques recommandées pour tester son programme et éviter le gaspillage de ressources CPU ?"
  - "Pourquoi est-il conseillé d'effectuer un test comparatif entre processeur et carte graphique lorsqu'on demande l'allocation d'un GPU ?"
  - "Pourquoi l'utilisation d'un GPU n'est-elle pas toujours justifiée, même si la tâche s'exécute plus rapidement sur un nœud GPU ?"
  - "Quels indicateurs et graphiques permettent de confirmer qu'un ou plusieurs GPU réservés restent inutilisés pendant l'exécution d'une tâche ?"
  - "Quelles solutions l'utilisateur doit-il envisager s'il constate qu'il a réservé plusieurs GPU mais que son code n'en exploite qu'un seul ?"
  - "Comment peut-on obtenir de l'assistance pour valider ses choix de configuration ?"
  - "Pourquoi est-il problématique de demander un GPU pour une tâche spécifique selon le texte ?"
  - "Quelle démarche est conseillée pour comparer les performances et justifier l'utilisation d'un GPU par rapport à un CPU ?"
  - "Quelles sont les ressources allouées (mémoire, temps d'exécution) et la configuration définies dans le script de soumission SLURM ?"
  - "Que montre le graphique concernant l'utilisation des cycles de calcul GPU, en particulier le fait qu'un seul GPU sur quatre soit actif ?"
  - "Quelles informations spécifiques peut-on tirer des graphiques relatifs à la consommation d'énergie (Power) et à l'utilisation de la mémoire du GPU ?"
  - "Comment doit-on gérer le nombre de CPU demandés par GPU pour éviter les ralentissements liés à l'architecture matérielle (nœuds NUMA) ?"
  - "Quels sont les critères d'utilisation (pourcentage de calcul et mémoire) qui indiquent qu'une tâche devrait être exécutée sur une instance MIG (Multi-Instance GPU) ?"
  - "Quelles stratégies d'optimisation sont recommandées lorsqu'une tâche n'utilise le GPU que temporairement ou n'exploite pas pleinement sa capacité (comme la séparation des phases ou l'utilisation de MPS) ?"
  - "Quelles sont les principales recommandations pour éviter de gaspiller les ressources GPU lors de l'exécution de vos tâches ?"
  - "Dans quels cas spécifiques est-il avantageux d'utiliser un MIG (Multi-Instance GPU) ou d'activer MPS (Multi-Process Service) ?"
  - "Comment calculer et configurer adéquatement sa demande de mémoire avec SBATCH pour correspondre aux besoins réels de la tâche ?"
  - "Quel est le problème principal identifié concernant l'utilisation des capacités du GPU ?"
  - "Quelle solution est proposée pour réduire le gaspillage des ressources graphiques ?"
  - "Quels sont les exemples spécifiques de tâches pour lesquelles l'utilisation du MPS est recommandée ?"
  - "Comment peut-on configurer un script de soumission pour utiliser la totalité de la mémoire d'un nœud ?"
  - "Quel est le rôle de la variable d'environnement `$SLURM_CPUS_PER_TASK` dans l'exemple de script fourni ?"
  - "Quels sont les éléments clés à retenir pour configurer de manière optimale sa demande de mémoire ?"
  - "Quelle est la règle recommandée pour l'allocation de la mémoire par cœur sur les grappes Béluga ou Narval ?"
  - "Quelle erreur fréquente doit-on éviter lors de la définition des ressources pour un vecteur de tâches ?"
  - "À quelles fins principales les tâches interactives doivent-elles être utilisées et quelles sont leurs limites de durée ?"
  - "Quelle est la règle recommandée pour l'allocation de la mémoire par cœur sur les grappes Béluga ou Narval ?"
  - "Quelle erreur fréquente doit-on éviter lors de la définition des ressources pour un vecteur de tâches ?"
  - "À quelles fins principales les tâches interactives doivent-elles être utilisées et quelles sont leurs limites de durée ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

To minimize resource waste on our clusters, we present the most common errors observed among our users, along with the corrective actions to apply. Examples are divided into three categories: CPU, GPU, and memory.

The various graphs are from the Narval and Béluga portals and are presented on the following page: Portal.

## CPU

### Requesting multiple cores for a serial task.

A serial task is one that runs on a single processor or compute core at a time, without parallelism. Unlike parallel tasks that can mobilize multiple processors or cores simultaneously to accelerate processing, serial tasks follow a strictly sequential execution. Memory is shared by processes and threads.

Here is an example of a submission script for a serial task. Only one core is requested using the option `--cpus-per-task=1`.

```bash title="simple_job.sh"
#!/bin/bash
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=4G
#SBATCH --time=02:00:00
#SBATCH --account=def-someuser

module load python/3.11

python3 mon_script.py
```

What does a serial task look like in the portal interface?

The vertical scale of the CPU graph is set to 1, corresponding to one requested core. Usage is represented in blue and completely fills the graph, indicating nearly 100% utilization.

The memory graph shows different parameters. Those to monitor are the **total allocated memory** and the **maximum used memory**.

!!! tip "Memory allocation"
    It is recommended to allow a margin of about 20% to avoid an "Out of Memory" (OOM) error.

In the context of a serial task, the *Processes and threads* graph indicates one active thread ("Running threads"). This information is represented by the orange line.

**What happens if you request multiple cores for a serial task?**

Here is an example of a submission script for a serial task that requests 8 cores instead of just one (`--cpus-per-task=8`).

```bash title="simple_job.sh"
#!/bin/bash
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=32G
#SBATCH --time=03:00:00
#SBATCH --account=def-someuser

module load python/3.11

python3 mon_script.py
```

In the CPU graph, although the vertical scale represents a total of 8 cores as requested, we observe that only one core is active. The activity of the various threads remains below the utilization of a single core. In this example, 7 cores are wasted. The fix would be to request only 1 core instead of 8 (`--cpus-per-task=1`).

In the memory graph, we can observe that the request is too high. Here, we multiply 8 cores by 32 GB, which gives a total of 256 GB. However, the graph indicates that only 4 GB are actually used. The correction would be to request `--mem-per-cpu=6G`.

The **_Processes and threads_** graph indicates that only one thread is active (orange line), even if 8 cores were requested. A serial task cannot run in parallel, so it is unnecessary to request more than one core.

!!! tip "Identifying serial vs. parallel tasks"
    This graph is a good indicator to determine if the submitted task is serial or parallel: simply observe the number of active threads.

### Requesting more cores than necessary for a multi-threaded task.

A multi-threaded task has the ability to use multiple threads to perform operations in parallel.

Here is an example of a submission script for a multi-threaded task. The `--cpus-per-task` parameter will be greater than 1. You can use the `$SLURM_CPUS_PER_TASK` environment variable to represent the number of cores in your program. Only one node is necessary, as only distributed tasks can use multiple nodes. See the section on [multi-processor tasks](#requesting-too-many-cores-in-multi-processor-mode). Threads share allocated memory. In this example, we will have a total of 64 GB (16 cores x 4 GB).

```bash title="simple_job.sh"
#!/bin/bash
#SBATCH --cpus-per-task=16
#SBATCH --mem-per-cpu=4G
#SBATCH --time=00:15:00
#SBATCH --account=def-someuser

monscript --threads $SLURM_CPUS_PER_TASK
```

What does a multi-threaded task look like on the portal?

The vertical scale of the CPU graph is set to 16, corresponding to the cores requested in the submission script. The usage of each core is represented by a different color. Each core is used at 100%, as the sum of uses completely fills the graph.

In the memory graph, we can observe that the request is for 64 GB. This value comes from multiplying 16 cores by 4 GB, for a total of 64 GB. This example comes from the Narval cluster. The most common nodes there have 64 cores and 249 GB of memory, which corresponds to approximately 4 GB of memory per core (249 ÷ 64 ≈ 4).

In the task presented here, the 64 GB are not fully utilized. It would therefore be possible to request 15 GB instead, since the observed maximum is around 10 GB, with stable usage over time.

!!! tip "Optimizing memory requests"
    This modification would have no impact on the CPU-equivalent, but as less memory would be requested, your task could be submitted more quickly.

The **_Processes and threads_** graph indicates that 16 threads are active. You should always observe a number of active threads similar to the number of requested cores.

**How to identify if you are requesting more cores than necessary for a multi-threaded task?**

Here is the submission script for the following multi-threaded task:

```bash title="simple_job.sh"
#!/bin/bash
#SBATCH --cpus-per-task=32
#SBATCH --mem-per-cpu=1G
#SBATCH --time=00:15:00
#SBATCH --account=def-someuser

monscript --threads $SLURM_CPUS_PER_TASK
```

When you don't sufficiently use the requested resources, the graph displays in red. Here we observe that the maximum number of cores used is 10, which is well below the 32 cores requested. The correction would be to request `#SBATCH --cpus-per-task=10`. See the **Processes and threads** graph for reference.

In the context of this task, if we reduce the number of cores to 10, we should consider increasing the memory from `#SBATCH --mem-per-cpu=1` to `#SBATCH --mem-per-cpu=3`, for a total of 30 GB.

The *Processes and threads* graph indicates that there is indeed an average of 10 active threads.

### Requesting too many cores in multi-processor mode.

A multi-processor task is one that distributes its work among several independent processes, often executed in parallel on multiple cores or nodes, to accelerate processing.

Characteristics of a multi-processor task:

*   Uses multiple processes (often via MPI – Message Passing Interface).
*   Can run on multiple cores and multiple nodes.
*   Each process has its own memory (unlike multi-threaded tasks which share memory).

Here is the submission script for the following multi-processor task:

```bash title="simple_job.sh"
#!/bin/bash
#SBATCH --nodes=4
#SBATCH --ntasks=64
#SBATCH --mem=0
#SBATCH --time=00:15:00
#SBATCH --account=def-someuser

srun ./mpi_program
```

In the CPU graph, a total of 256 cores (64 cores x 4 nodes) are observed. Each core is used at 100%, as the sum of uses completely fills the graph.

By using the `#SBATCH --mem=0` parameter, we request to allocate all available memory on the node. This option is only valid if all cores on the node are also allocated and used. In this case, it is possible to request the entirety of the memory associated with the node.

The *Processes and threads* graph indicates that there is indeed an average of 64 active threads per node. However, only node nc30328 is visible, as the curves for the other nodes are superimposed.

**How to identify if you are requesting more cores than necessary for a multi-processor task?**

Here is the submission script for the following multi-processor task:

```bash title="simple_job.sh"
#!/bin/bash
#SBATCH --ntasks=24
#SBATCH --mem-per-cpu=12G
#SBATCH --time=00:15:00
#SBATCH --account=def-someuser

srun ./mpi_program
```

Firstly, in the CPU utilization graph, we observe that only 16 cores are utilized, whereas the system has 24 available. If all 24 cores had been used, the graph would have been entirely colored. The correction would be to change `#SBATCH --ntasks=24` to `#SBATCH --ntasks=16`.

By observing the memory utilization graph, we can see that the requested amount is excessive.

!!! tip "Optimizing memory for multi-processor tasks"
    It would be wise to perform a test by reducing the value to `#SBATCH --mem-per-cpu=1G`.

Some points on the *Processes and threads* graph overlap, which can make reading difficult. However, by selecting each thread individually, we can determine that a total of 16 threads are active. This counting provides a complementary method to estimate the number of cores actually needed for the multi-processor task.

### Requesting --cpus-per-task=2 for a non-multi-threaded multi-processor task.

**How to identify if you have requested resources for a non-multi-threaded multi-processor task?**

```bash title="simple_job.sh"
#!/bin/bash
#SBATCH --ntasks=32
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu=4g
#SBATCH --time=3-00:00:00
#SBATCH --account=def-someuser

srun ./mpi_program
```

The error comes from using the `#SBATCH --cpus-per-task>1` option. In the case of a multi-processor task that is not multi-threaded (i.e., it uses only one thread per process), only one core is required per process. If more cores are allocated, they will remain unused, as each process can only utilize one thread.

This is reflected in the CPU utilization graph: we observe that only half of the cores are active, because only one of the two cores allocated per process is actually used.

Regarding memory, we could reduce the value to `#SBATCH --mem-per-cpu=2g` to limit the excess margin.

!!! tip "Troubleshooting multi-processor core allocation"
    Another way to highlight this error is to compare the number of cores allocated per node (visible in the Portal's Resources section) with the number of active threads displayed in the *Processes and threads* graph. In this case, since the `#SBATCH --cpus-per-task=2` option is used, we observe that there are half as many active threads as allocated cores. This indicates that each process uses only one thread, leaving the other core unused. For example, on node **nc30408**, there are 16 allocated cores (Portal's Resources section), but only 8 active threads (*Processes and threads* graph).

### Requesting different parameters for SBATCH and the OMP_NUM_THREADS variable for a GROMACS task.

**How to properly configure submission parameters for a GROMACS task to ensure optimal execution?**

Here is a submission script where the `OMP_NUM_THREADS` variable is not properly configured.

```bash title="simple_job.sh"
#!/bin/bash
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpus=4000M
#SBATCH --time=3-00:00:00
#SBATCH --account=def-someuser

module load gcc/12.3 openmpi/4.1.5 gromacs/2024.1
export OMP_NUM_THREADS=4
srun --cpus-per-task=$OMP_NUM_THREADS gmx_mpi mdrun -deffnm md
```

The `OMP_NUM_THREADS` variable must represent the number of requested cores. Here, `OMP_NUM_THREADS=4` represents half of what was requested with `#SBATCH --cpus-per-task=8`. Therefore, 32 cores will be requested, but only 16 will be used. This can be visualized in the following CPU graph.

!!! tip "Correcting OMP_NUM_THREADS for GROMACS"
    To correct the situation, simply use the `SLURM_CPUS_PER_TASK` environment variable. This way, you will be sure that the value written for `--cpus-per-task` will be equivalent to that of `OMP_NUM_THREADS`.

```bash title="simple_job.sh"
#!/bin/bash
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpus=4000M
#SBATCH --time=3-00:00:00
#SBATCH --account=def-someuser

module load gcc/12.3 openmpi/4.1.5 gromacs/2024.1
export OMP_NUM_THREADS="${SLURM_CPUS_PER_TASK:-1}"
srun --cpus-per-task=$OMP_NUM_THREADS gmx_mpi mdrun -deffnm md
```

Here is the CPU graph corresponding to the corrected script's task.

### What to remember to avoid CPU waste?

Identify the type of task you are running.
*   !!! tip
    Start with a simple test. If you don't know your program's behaviour, launch it with 1 CPU. Then, try with 2 CPUs and observe if both are used efficiently.
*   !!! tip
    Consult your application's documentation. Look for parameters like `--threads` or `--cores`. This may indicate that the application can take advantage of parallelism. It's up to you to test to find the optimal number of cores.
*   !!! tip
    Perform your tests in an interactive task. This allows you to quickly test different configurations without waiting in the queue.

Use visualization portals.
*   !!! tip
    They allow you to monitor resource utilization (CPU, memory, GPU) and identify inefficiencies.

Connect to an active node.
*   !!! tip
    Connecting to a node while your task is running can give you valuable insights into its behaviour.

Need help?
*   !!! note
    Do not hesitate to contact us if you have questions or wish to validate your configuration choices.

## GPU

### Requesting a GPU but not using it at all.

Here is an example where the GPU is not utilized at all. In this case, it is relevant to question the necessity of using a GPU for this task.

!!! tip "CPU vs. GPU comparison"
    We encourage you to perform a comparative test between CPU and GPU execution.

Even if the execution time is longer on CPU, GPU usage may not be justified given its high cost. It is also possible that the task runs faster on GPU, not due to GPU acceleration, but because the CPUs on these nodes are more powerful.

As the graph indicates, the GPU remains unused, suggesting it provides no gain in this context.

```bash title="simple_job_GPU.sh"
#!/bin/bash
#SBATCH --cpus-per-task=10
#SBATCH --gpu-per-node=1
#SBATCH --mem=14G
#SBATCH --time=3-00:00:00
#SBATCH --account=def-someuser

module load python/3.11

python3 mon_script.py
```

### Requesting multiple GPUs but only using one.

Here is an example where the user requested two GPUs, while only one was necessary. As the compute cycles graph shows, GPU 1 is not used at all: no values are recorded for metrics such as SM Active, SM Occupancy, etc.

This lack of activity is also visible in the GPU power graph, where no data is recorded for GPU 1, as well as in the GPU memory graph, which confirms its disuse.

```bash title="simple_job_GPU.sh"
#!/bin/bash
#SBATCH --cpus-per-task=10
#SBATCH --gpu-per-node=2
#SBATCH --mem=14G
#SBATCH --time=3-00:00:00
#SBATCH --account=def-someuser

module load python/3.11

python3 mon_script.py
```

To correct this situation, you can either adapt your code to effectively utilize two GPUs, or simply request only one when submitting your task.

```bash title="simple_job_GPU.sh"
#!/bin/bash
#SBATCH --cpus-per-task=10
#SBATCH --gpu-per-node=1
#SBATCH --mem=14G
#SBATCH --time=3-00:00:00
#SBATCH --account=def-someuser

module load python/3.11

python3 mon_script.py
```

### Requesting a 4-GPU node but only using 1 GPU.

Here is an example where the user reserved an entire GPU node, while a single GPU would have been sufficient.

The compute cycles graph clearly shows that GPUs 1, 2, and 3 are not being used: no data is recorded for metrics such as SM Active, SM Occupancy, etc.

This lack of activity is also visible in the GPU power graph, where only GPU 0 shows values, as well as in the GPU memory graph, which confirms that the other GPUs remained inactive.

```bash title="simple_job_GPU.sh"
#!/bin/bash
#SBATCH --nodes=1
#SBATCH --gpu-per-node=4
#SBATCH --cpus-per-task=10
#SBATCH --mem=14G
#SBATCH --time=3-00:00:00
#SBATCH --account=def-someuser

module load python/3.11

python3 mon_script.py
```

To correct this situation, you can either adapt your code to effectively utilize all four GPUs, or simply request only one when submitting your task.

```bash title="simple_job_GPU.sh"
#!/bin/bash
#SBATCH --gpu-per-node=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=14G
#SBATCH --time=3-00:00:00
#SBATCH --account=def-someuser

module load python/3.11

python3 mon_script.py
```

### How to manage the number of CPUs for a GPU task?

!!! warning "CPU allocation for GPU tasks"
    On a node with four GPUs, it is inadvisable to request more than a quarter of the CPUs per GPU. Indeed, additional CPUs risk being allocated on the wrong NUMA node, or even on a different socket than the GPU. This can lead to a significant slowdown in transfers between the CPU and the GPU.

```bash title="simple_job_GPU.sh"
#!/bin/bash
#SBATCH --gpu-per-node=1
#SBATCH --cpus-per-task=14
#SBATCH --mem=14G
#SBATCH --time=3-00:00:00
#SBATCH --account=def-someuser

module load python/3.11

python3 mon_script.py
```

### An example of an inefficient GPU task that should run on a MIG.

MIG technology is available for A100 GPU instances.

!!! tip "When to use MIG"
    If your GPU utilization is more than 10% but less than 40%, and memory usage is under 20 GB, you can most likely run your task on a MIG.

!!! note "Choosing the right MIG type"
    It is important to choose the right MIG type according to your needs to avoid waste.

For more information, please consult the following wiki page: [Multi-Instance GPU](https://docs.alliancecan.ca/wiki/Multi-Instance_GPU/)

Here is a graph illustrating GPU compute cycle and memory usage for a GPU task that could be well-suited for execution on a MIG instance.

### Your task uses the GPU for a while, then stops using it completely (or vice-versa).

If your task uses the GPU only temporarily or irregularly, this can lead to resource waste.

!!! tip "Optimizing intermittent GPU usage"
    It is recommended to evaluate the possibility of interrupting the task after the GPU compute phase to resume it on a CPU node, or vice-versa.
    Thoroughly understanding your task's needs allows for effectively separating CPU and GPU phases, and optimizing resource utilization.

The following graphs illustrate two typical examples of this type of profile.

### Your task does not efficiently utilize GPU capabilities. Using MPS (Multi-Process Service) could be a relevant solution to reduce observed waste.

Some examples where MPS applies well:

*   A multi-processor (MPI) task where each process does not individually fill a GPU.
*   A multi-threaded task where each thread does not individually fill a GPU.
*   Several similar serial tasks where each individual job does not fill a GPU.

If your tasks only require one GPU, grouping them can improve your priority in the queue. You can also leverage MPS (Multi-Process Service) within a MIG (Multi-Instance GPU) to optimize resource utilization. This approach is applicable to all compute clusters with GPUs.

For more information, please consult the following page: [Hyper-Q / MPS](https://docs.alliancecan.ca/wiki/Hyper-Q_/_MPS/fr/)

### What to remember to avoid wasting GPUs?

*   !!! tip
    Check if your program is GPU-compatible. Ensure your application is properly configured to leverage the GPU.
*   !!! tip
    Perform initial tests with an interactive task. Launch an interactive task requesting a MIG to validate that your code runs correctly on the GPU.
*   !!! tip
    Analyze your task's efficiency via the visualization portal. Monitor actual GPU usage (compute, memory) to detect any potential waste.
*   !!! tip
    Understand the different ways to request a GPU with SBATCH. Familiarize yourself with the available options for requesting a GPU, a MIG, or enabling MPS according to your needs.
*   !!! tip
    Use a MIG if your task consumes less than 20 GB of GPU memory. This allows for efficient sharing of the GPU with other users.
*   !!! tip
    Consider MPS if you are running multiple lightweight tasks. Whether in parallel or in series, MPS (Multi-Process Service) allows for better utilization of an underutilized GPU.
*   !!! tip
    Do not request more time than necessary. Shorter task durations reduce wait times and improve your priority in the queue.

## Memory

Each cluster has specific node types, with varying memory capacities depending on the models. You can find this information on the main Wiki page, in the tabs dedicated to each available cluster.

This example illustrates a task submitted on Béluga with a request for 752 GB of memory, while only 60 GB were actually needed.

```bash title="simple_job.sh"
#!/bin/bash
#SBATCH --cpus-per-task=12
#SBATCH --mem=752G
#SBATCH --time=3-00:00:00
#SBATCH --account=def-someuser

monscript --threads $SLURM_CPUS_PER_TASK
```

The first thing to do to properly assess the amount of memory needed is to calculate the core-equivalent memory based on the node you want to use. For example, on Béluga, the vast majority of CPU nodes have 186 GB of available memory. If we divide 186 GB by 40 cores for a node, we get approximately 4 GB of memory per core.

Here's a way to request 60 GB of memory for 12 cores.

Request 5 GB per core with `--mem-per-cpu`. This will give a total of 60 GB. `5 GB * 12 cores = 60 GB`.

```bash title="simple_job.sh"
#!/bin/bash
#SBATCH --cpus-per-task=12
#SBATCH --mem-per-cpu=5G
#SBATCH --time=3-00:00:00
#SBATCH --account=def-someuser

monscript --threads $SLURM_CPUS_PER_TASK
```

If you need the total memory of the node, you can configure your submission script this way using `--mem=0`:

```bash title="simple_job.sh"
#!/bin/bash
#SBATCH --cpus-per-task=40
#SBATCH --mem=0
#SBATCH --time=3-00:00:00
#SBATCH --account=def-someuser

monscript --threads $SLURM_CPUS_PER_TASK
```

What to remember for configuring your memory request:

1.  On Béluga/Narval, in core-equivalent, you have approximately 4 GB of memory per core.
2.  You can request less; you will save time.
3.  You can request more if your task requires more memory.
4.  It is acceptable to request up to 20% more compared to what you will actually use to ensure you don't run out.

## Job Arrays

!!! warning "Job array resource allocation"
    Resources requested for a job array apply to a single task, not to all tasks. This is a common mistake to avoid.

Here's what happens when this mistake is made. In this example, 12 cores are requested to cover the 12 job array tasks, but each task will receive these 12 cores, leading to an overestimation of resources since only one core is needed per task.

```bash title="simple_job.sh"
#!/bin/bash
#SBATCH --cpus-per-task=12
#SBATCH --mem-per-cpus=8G
#SBATCH --time=3-00:00:00
#SBATCH --account=def-someuser
#SBATCH --array=0-11

module load python/3.11

python3 mon_script.py
```

Here is the CPU graph that clearly illustrates the situation.

Additionally, we can observe that far too much memory is requested.

We can correct the situation this way:

```bash title="simple_job.sh"
#!/bin/bash
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpus=9G
#SBATCH --time=3-00:00:00
#SBATCH --account=def-someuser
#SBATCH --array=0-11

module load python/3.11

python3 mon_script.py
```

The following CPU and memory graphs illustrate the impact of the modifications: resource utilization is now optimized, with no observed waste.

## Interactive Tasks

!!! warning "Interactive task guidelines"
    Interactive tasks should remain short and be reserved for testing or debugging, not full development. They should last less than 6 hours and use the minimum possible resources.

Development should be performed on your local computer, while quick tests can be done in an interactive environment.

By requesting minimal resources, you reduce wait times and preserve your priority in the execution queue.

If you are working in a Jupyter notebook, you can convert them to scripts:

[JupyterHub#Running notebooks as Python scripts](https://docs.alliancecan.ca/wiki/JupyterHub#Running_notebooks_as_Python_scripts/)

Here is a recommendation for a CPU request:

```bash
salloc --time=1:0:0 --mem-per-cpu=4G --cpus-per-task=1 --account=def-someuser
```

Here is a recommendation for a GPU request:

```bash
salloc --time=1:0:0 --mem-per-cpu=4G --cpus-per-task=1 --gres=gpu:a100_1g.5gb:1 --account=def-someuser