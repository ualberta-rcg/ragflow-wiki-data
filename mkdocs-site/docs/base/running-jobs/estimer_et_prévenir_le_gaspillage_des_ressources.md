---
title: "Estimer et prévenir le gaspillage des ressources"
slug: "estimer_et_prévenir_le_gaspillage_des_ressources"
lang: "base"

source_wiki_title: "Estimer et prévenir le gaspillage des ressources"
source_hash: "37acb6094ac88b4fe4de360f5c7e8098"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T06:14:28.343558+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

To minimize resource waste in our clusters, we present the most common errors we have observed among our users, along with the corrective actions to apply. Examples are divided into three categories: CPU, GPU, and memory.

The various graphs come from the Narval and Béluga portals and are presented on the following page: [Portal](portal.md).

## CPU

### Requesting Multiple Cores for a Serial Task

A serial task is a task that runs on a single processor or compute core at a time, without parallelism. Unlike parallel tasks which can mobilize multiple processors or cores simultaneously to accelerate processing, serial tasks follow a strictly sequential execution. Memory is shared by processes and threads.

Here is an example submission script for a serial task. A single core is requested using the `--cpus-per-task=1` option.

```sh title="simple_job.sh"
#!/bin/bash
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=4G
#SBATCH --time=02:00:00
#SBATCH --account=def-someuser

module load python/3.11

python3 mon_script.py
```

What does a serial task look like in the portal interface?

The vertical scale of the CPU graph is set to 1, corresponding to one requested core. Usage is represented in blue and entirely fills the graph, indicating close to 100% utilization.

The CPU graph.

The memory graph represents different parameters. Those to monitor are the **total allocated** memory and the **maximum used** memory.

!!! tip "Memory Request Margin"
    It is recommended to allow for a margin of approximately 20% to avoid an *Out of Memory* (OOM) error.

The Memory graph.

In the context of a serial task, the **Processes and threads** graph indicates that one execution thread is active (*Running threads*). This information is represented by the orange line.

The *Processes and threads* graph.

**What happens if you request multiple cores for a serial task?**

Here is an example submission script for a serial task that requests 8 cores instead of just one (`--cpus-per-task=8`).

```sh title="simple_job.sh"
#!/bin/bash
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=32G
#SBATCH --time=03:00:00
#SBATCH --account=def-someuser

module load python/3.11

python3 mon_script.py
```

In the CPU graph, although the vertical scale represents a total of 8 cores, as requested, only one core is active. The activity of the different execution threads remains below the utilization of a single core. In this example, 7 cores are wasted. The corrective action would be to request only 1 core instead of 8 (`--cpus-per-task=1`).

The CPU graph.

It can be observed in the memory graph that the request is too high. Here, multiplying 8 cores by 32 GB yields a total of 256 GB. However, the graph indicates that only 4 GB are actually used. The correction would be to request `--mem-per-cpu=6G`.

The Memory graph.

The **Processes and threads** graph indicates that only one execution thread is active (orange line), even though 8 cores were requested. A serial task cannot execute in parallel, so it is useless to request more than one core. This graph is a good indicator for determining if the submitted task is serial or parallel: simply observe the number of active execution threads.

The *Processes and threads* graph.

### Requesting More Cores Than Necessary for a Multithreaded Task

A multithreaded task has the ability to use multiple execution threads to perform operations in parallel.

Here is an example submission script for a multithreaded task. The `--cpus-per-task` parameter will be greater than 1. The `$SLURM_CPUS_PER_TASK` environment variable can be used to represent the number of cores in your program. Only one node is necessary, as only distributed tasks can use multiple nodes. See the section on multiprocessor tasks. Execution threads share the allocated memory. In this example, we will have a total of 64 GB (16 cores x 4 GB).

```sh title="simple_job.sh"
#!/bin/bash
#SBATCH --cpus-per-task=16
#SBATCH --mem-per-cpu=4G
#SBATCH --time=00:15:00
#SBATCH --account=def-someuser

monscript --threads $SLURM_CPUS_PER_TASK
```

What does a multithreaded task look like on the portal?

The vertical scale of the CPU graph is set to 16, corresponding to the cores requested in the submission script. The usage of each core is represented by a different colour. Each core is utilized at 100%, as the sum of uses completely fills the graph.

The CPU graph.

It can be observed in the memory graph that the request is 64 GB. This value comes from multiplying 16 cores by 4 GB, for a total of 64 GB. This example comes from the Narval cluster. The most common nodes there have 64 cores and 249 GB of memory, which corresponds to approximately 4 GB of memory per core (249 ÷ 64 ≈ 4).

In the task presented here, the 64 GB is not fully utilized. It would therefore be possible to request 15 GB instead, since the observed maximum is around 10 GB, with stable utilization over time. This modification would have no impact on the CPU-equivalent, but as less memory would be requested, your task could be submitted more quickly.

The Memory graph.

The **Processes and threads** graph indicates that 16 execution threads are active. You should always observe a number of active execution threads similar to the number of requested cores.

The *Processes and threads* graph.

**How to identify if you are requesting more cores than necessary for a multithreaded task?**

Here is the submission script for the following multithreaded task:

```sh title="simple_job.sh"
#!/bin/bash
#SBATCH --cpus-per-task=32
#SBATCH --mem-per-cpu=1G
#SBATCH --time=00:15:00
#SBATCH --account=def-someuser

monscript --threads $SLURM_CPUS_PER_TASK
```

When you do not sufficiently use the requested resources, the graph displays in red. Here, we observe that the maximum number of cores used is 10, which is well below the 32 cores requested. The correction would be to request `#SBATCH --cpus-per-task=10`. See the **Processes and threads** graph for reference.

The CPU graph.

In the context of this task, if the number of cores is reduced to 10, it would be advisable to increase the memory from `#SBATCH --mem-per-cpu=1` to `#SBATCH --mem-per-cpu=3`, for a total of 30 GB.

The Memory graph.

The *Processes and threads* graph indicates that there is indeed an average of 10 active execution threads.

The *Processes and threads* graph.

### Requesting Too Many Cores in Multiprocessor Mode

A multiprocessor task is a task that distributes its work among several independent processes, often executed in parallel on multiple cores or nodes, to accelerate processing.

Characteristics of a multiprocessor task:

*   Uses multiple processes (often via MPI – Message Passing Interface).
*   Can execute on multiple cores and multiple nodes.
*   Each process has its own memory (unlike multithreaded tasks which share memory).

Here is the submission script for the following multiprocessor task:

```sh title="simple_job.sh"
#!/bin/bash
#SBATCH --nodes=4
#SBATCH --ntasks=64
#SBATCH --mem=0
#SBATCH --time=00:15:00
#SBATCH --account=def-someuser

srun ./mpi_program
```

In the CPU graph, a total of 256 cores are observed (64 cores x 4 nodes). Each core is utilized at 100%, as the sum of uses completely fills the graph.

The CPU graph.

By using the `#SBATCH --mem=0` parameter, you are requesting to allocate all available memory on the node. This option is only valid if all cores of the node are also allocated and utilized. In this case, it is possible to request all memory associated with the node.

The Memory graph.

The *Processes and threads* graph indicates that there is indeed an average of 64 active execution threads per node. However, only node nc30328 is visible, because the curves of the other nodes are superimposed.

The *Processes and threads* graph.

**How to identify if you are requesting more cores than necessary for a multiprocessor task?**

Here is the submission script for the following multiprocessor task:

```sh title="simple_job.sh"
#!/bin/bash
#SBATCH --ntasks=24
#SBATCH --mem-per-cpu=12G
#SBATCH --time=00:15:00
#SBATCH --account=def-someuser

srun ./mpi_program
```

Firstly, in the CPU utilization graph, it is observed that only 16 cores are utilized, while the system has 24 available. If all 24 cores had been used, the graph would have been entirely coloured. The corrective action would be to change `#SBATCH --ntasks=24` to `#SBATCH --ntasks=16`.

The CPU graph.

By observing the memory utilization graph, it is noted that the requested amount is excessive. It would be wise to perform a test by reducing the value to `#SBATCH --mem-per-cpu=1G`.

The Memory graph.

Some points on the *Processes and threads* graph overlap, which can make reading difficult. However, by selecting each execution thread individually, it can be determined that a total of 16 execution threads are active. This counting provides a complementary method to estimate the number of cores actually necessary for the execution of the multiprocessor task.

The *Processes and threads* graph.

The Resources section.

### Requesting --cpus-per-task=2 for a Non-Multithreaded Multiprocessor Task

**How to identify if you have requested resources for a multiprocessor task that is not multithreaded?**

```sh title="simple_job.sh"
#!/bin/bash
#SBATCH --ntasks=32
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu=4g
#SBATCH --time=3-00:00:00
#SBATCH --account=def-someuser

srun ./mpi_program
```

The error stems from using the `#SBATCH --cpus-per-task>1` option. In the case of a multiprocessor task that is not multithreaded (i.e., one that uses a single execution thread per process), only one core is required per process. If more cores are allocated, they will remain unused, as each process can only utilize a single thread.

This is reflected in the CPU utilization graph: it is observed that only half of the cores are active, because only one of the two cores allocated per process is actually used.

The CPU graph.

Regarding memory, we could reduce the value to `#SBATCH --mem-per-cpu=2g` to limit the excess margin.

The Memory graph.

Another way to highlight this error is to compare the number of cores allocated per node (visible in the Portal's Resources section) with the number of active execution threads displayed in the *Processes and threads* graph. In this case, since the `#SBATCH --cpus-per-task=2` option is used, it is observed that there are half as many active execution threads as allocated cores. This indicates that each process uses only one thread, leaving the other core unused. For example, on node **nc30408**, there are 16 allocated cores (Portal's Resources section), but only 8 active execution threads (*Processes and threads* graph).

The *Processes and threads* graph.

The Resources section.

### Requesting Different SBATCH Parameters and OMP_NUM_THREADS Variable for a GROMACS Task

**How to properly configure submission parameters for a GROMACS task to ensure optimal execution?**

Here is a submission script where the `OMP_NUM_THREADS` variable is not properly configured.

```sh title="simple_job.sh"
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

The `OMP_NUM_THREADS` variable must represent the number of requested cores. Here, `OMP_NUM_THREADS=4` represents half of what was requested with `#SBATCH --cpus-per-task=8`. Therefore, 32 cores will be requested, but only 16 will be used. This can all be visualized in the following CPU graph:

The CPU graph.

To correct the situation, simply use the `SLURM_CPUS_PER_TASK` environment variable. This way, you will be certain that the value set for `--cpus-per-task` will be equivalent to that of `OMP_NUM_THREADS`.

```sh title="simple_job.sh"
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

Here is the CPU graph corresponding to the corrected script's task:

The CPU graph.

### Key Takeaways to Avoid CPU Waste

Identify the type of task you are running.
*   Start with a simple test. If you don't know your program's behaviour, run it with 1 CPU. Then, try with 2 CPUs and observe if both are used efficiently.
*   Consult your application's documentation. Look for parameters like `--threads` or `--cores`. This may indicate that the application can leverage parallelism. It's up to you to test to find the optimal number of cores.
*   Perform your tests in an interactive task. This allows you to quickly test different configurations without waiting in the queue.

Use visualization portals.
*   They allow you to monitor resource usage (CPU, memory, GPU) and identify inefficiencies.

Connect to an active node.
*   Connecting to a node during your task's execution can provide valuable insights into its behaviour.

Need help?
*   Do not hesitate to contact us if you have any questions or would like to validate your configuration choices.

## GPU

### Requesting a GPU but Not Using It At All

Here is an example where the GPU is not utilized at all. In this case, it is relevant to question the necessity of using a GPU for this task. We encourage you to perform a comparative test between CPU and GPU execution.

Even if the execution time is longer on CPU, GPU usage may not be justified given its high cost. It is also possible that the task runs faster on GPU, not thanks to GPU acceleration, but because the CPUs on these nodes are more powerful.

As the graph indicates, the GPU remains unused, suggesting it provides no benefit in this context.

```sh title="simple_job_GPU.sh"
#!/bin/bash
#SBATCH --cpus-per-task=10
#SBATCH --gpu-per-node=1
#SBATCH --mem=14G
#SBATCH --time=3-00:00:00
#SBATCH --account=def-someuser

module load python/3.11

python3 mon_script.py
```

The GPU Graph - GPU Compute Cycle Used.

### Requesting Multiple GPUs but Only Using One

Here is an example where the user requested two GPUs, but only one was necessary. As shown in the compute cycles graph, GPU 1 is not used at all: no values are recorded for metrics such as SM Active, SM Occupancy, etc.

This lack of activity is also visible in the GPU power graph, where no data is recorded for GPU 1, as well as in the GPU memory graph, which confirms its non-utilization.

```sh title="simple_job_GPU.sh"
#!/bin/bash
#SBATCH --cpus-per-task=10
#SBATCH --gpu-per-node=2
#SBATCH --mem=14G
#SBATCH --time=3-00:00:00
#SBATCH --account=def-someuser

module load python/3.11

python3 mon_script.py
```

The GPU Graph - GPU Compute Cycle Used.

The GPU Graph - Power.

The GPU Graph - Memory.

To correct this situation, you can either adapt your code to effectively utilize two GPUs, or simply request only one during your task submission.

```sh title="simple_job_GPU.sh"
#!/bin/bash
#SBATCH --cpus-per-task=10
#SBATCH --gpu-per-node=1
#SBATCH --mem=14G
#SBATCH --time=3-00:00:00
#SBATCH --account=def-someuser

module load python/3.11

python3 mon_script.py
```

### Requesting a 4-GPU Node but Only Using 1 GPU

Here is an example where the user reserved a full GPU node, when a single GPU would have been sufficient.

The compute cycles graph clearly shows that GPUs 1, 2, and 3 are not used: no data is recorded for metrics such as SM Active, SM Occupancy, etc.

This lack of activity is also visible in the GPU power graph, where only GPU 0 shows values, as well as in the GPU memory graph, which confirms that the other GPUs remained inactive.

```sh title="simple_job_GPU.sh"
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

The GPU Graph - GPU Compute Cycle Used.

The GPU Graph - Power.

The GPU Graph - Memory.

To correct this situation, you can either adapt your code to actually utilize all four GPUs, or simply request only one during your task submission.

```sh title="simple_job_GPU.sh"
#!/bin/bash
#SBATCH --gpu-per-node=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=14G
#SBATCH --time=3-00:00:00
#SBATCH --account=def-someuser

module load python/3.11

python3 mon_script.py
```

### How to Manage the Number of CPUs for a GPU Task?

!!! warning "CPU Allocation for GPU Tasks"
    On a node with four GPUs, it is inadvisable to request more than a quarter of the CPUs per GPU. Indeed, additional CPUs risk being allocated on a mismatched NUMA node, or even on a different socket than that of the GPU. This can lead to a significant slowdown in transfers between the CPU and the GPU.

```sh title="simple_job_GPU.sh"
#!/bin/bash
#SBATCH --gpu-per-node=1
#SBATCH --cpus-per-task=14
#SBATCH --mem=14G
#SBATCH --time=3-00:00:00
#SBATCH --account=def-someuser

module load python/3.11

python3 mon_script.py
```

Illustration of a GPU node with 2 CPUs that are not on the same socket.

### An Example of an Inefficient GPU Task That Should Run on a MIG

MIG technology is available for A100 GPU instances. If your GPU utilization is more than 10% but less than 40%, and memory usage is less than 20GB, you can most likely run your task on a MIG.

It is important to choose the right MIG type according to your needs to avoid waste.

For more information, please consult the following wiki page: [Multi-Instance GPU](https://docs.alliancecan.ca/wiki/Multi-Instance_GPU/)

Here is an example graph illustrating the utilization of GPU compute cycles and memory for a GPU task that could be well-suited for execution on a MIG instance.

The GPU Graph - GPU Compute Cycle Used.

The GPU Graph - Memory.

### Your Task Uses the GPU for a Period, Then Stops Using It Completely (or vice versa)

If your task uses the GPU only temporarily or irregularly, this can lead to resource waste.

It is recommended to evaluate the possibility of interrupting the task after the GPU computation phase to resume it on a CPU node, or vice versa.

Knowing your task's requirements well allows for effective separation of CPU and GPU phases, and optimizes resource utilization.

The following graphs illustrate two typical examples of this type of profile.

The GPU Graph - GPU Compute Cycle Used Only at the End.

The GPU Graph - GPU Compute Cycle Used Only at the Beginning.

### Your Task Does Not Efficiently Utilize GPU Capabilities. Using MPS (Multi-Process Service) Could Be a Relevant Solution to Reduce Observed Waste.

Some examples where MPS applies well:

*   A multiprocessor (MPI) task where each process does not individually fill a GPU.
*   A multithreaded task where each execution thread does not individually fill a GPU.
*   Several similar serial tasks where each individual job does not fill a GPU.

If your tasks only require one GPU, grouping them can improve your priority in the queue. You can also leverage MPS (Multi-Process Service) within a MIG (Multi-Instance GPU) to optimize resource utilization. This approach is applicable to all compute clusters with GPUs.

For more information, please consult the following page: [Hyper-Q / MPS](https://docs.alliancecan.ca/wiki/Hyper-Q_/_MPS/fr/)

### Key Takeaways to Avoid GPU Waste

Verify if your program is compatible with the GPU.
*   Ensure your application is properly configured to leverage the GPU.

Perform initial tests with an interactive task.
*   Launch an interactive task, requesting a MIG to validate your code's proper functioning on the GPU.

Analyze your task's efficiency via the visualization portal.
*   Monitor actual GPU usage (compute, memory) to detect any potential waste.

Understand the different ways to request a GPU with SBATCH.
*   Familiarize yourself with the available options for requesting a GPU, a MIG, or enabling MPS according to your needs.

Use a MIG if your task consumes less than 20 GiB of GPU memory.
*   This allows for efficient sharing of the GPU with other users.

Consider MPS if you are running several lightweight tasks.
*   Whether in parallel or in serial, MPS (Multi-Process Service) allows for better utilization of an underutilized GPU.

Do not request more time than necessary.
*   Shorter task durations reduce waiting times and improve your priority in the queue.

## Memory

Each cluster has specific node types, with varying memory capacities depending on the models. You can find this information on the main Wiki page, under the tabs dedicated to each available cluster.

This example illustrates a task submitted on Béluga with a request for 752 GB of memory, whereas only 60 GB was actually needed.

```sh title="simple_job.sh"
#!/bin/bash
#SBATCH --cpus-per-task=12
#SBATCH --mem=752G
#SBATCH --time=3-00:00:00
#SBATCH --account=def-someuser

monscript --threads $SLURM_CPUS_PER_TASK
```

The Memory graph.

The first thing to do to properly assess the necessary amount of memory is to calculate the memory-per-core equivalent based on the node you want to use. For example, on Béluga, the vast majority of CPU nodes have 186 GB of available memory. If we divide 186 GB by 40 cores for a node, we get approximately 4 GB of memory per core.

Here's a way to request 60 GB of memory for 12 cores.

Request 5 GB per core with `--mem-per-cpu`. This will result in a total of 60 GB. `5 GB * 12 cores = 60 GB`.

```sh title="simple_job.sh"
#!/bin/bash
#SBATCH --cpus-per-task=12
#SBATCH --mem-per-cpu=5G
#SBATCH --time=3-00:00:00
#SBATCH --account=def-someuser

monscript --threads $SLURM_CPUS_PER_TASK
```

If you need the total memory of the node, you can configure your submission script this way by using `--mem=0`:

```sh title="simple_job.sh"
#!/bin/bash
#SBATCH --cpus-per-task=40
#SBATCH --mem=0
#SBATCH --time=3-00:00:00
#SBATCH --account=def-someuser

monscript --threads $SLURM_CPUS_PER_TASK
```

Key takeaways for properly configuring your memory request:

1.  In terms of memory-per-core equivalent, on Béluga/Narval you have approximately 4 GB of memory per core.
2.  You can request less; you will save time.
3.  You can request more if your task requires more memory.
4.  It's acceptable to request up to 20% more than what you will use to ensure you don't run out.

## Job Arrays

The resources requested for a job array apply to a single task, not to the entire set of tasks. This is a common error to avoid.

Here's what happens when this error is made. In this example, 12 cores are requested to cover the 12 job array tasks, but each task will receive these 12 cores, leading to an overestimation of resources since only one core is needed per task.

```sh title="simple_job.sh"
#!/bin/bash
#SBATCH --cpus-per-task=12
#SBATCH --mem-per-cpus=8G
#SBATCH --time=3-00:00:00
#SBATCH --account=def-someuser
#SBATCH --array=0-11

module load python/3.11

python3 mon_script.py
```

Here is the CPU graph that accurately represents the situation.

The CPU graph.

Furthermore, we can observe that far too much memory is requested.

The Memory graph.

We can correct the situation in this way:

```sh title="simple_job.sh"
#!/bin/bash
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpus=9G
#SBATCH --time=3-00:00:00
#SBATCH --account=def-someuser
#SBATCH --array=0-11

module load python/3.11

python3 mon_script.py
```

The following CPU and memory graphs illustrate the impact of the modifications: resource utilization is now optimized, with no waste observed.

The CPU graph.

The Memory graph.

## Interactive Tasks

Interactive tasks should remain short and be reserved for testing or debugging, not full development. They should last less than 6 hours and use the minimum possible resources.

Development should be carried out on your local computer, while quick tests can be performed in an interactive environment.

By requesting minimal resources, you reduce wait times and preserve your priority in the execution queue.

If you are working in a Jupyter notebook, you can convert them into scripts:

[JupyterHub#Running_notebooks_as_Python_scripts](https://docs.alliancecan.ca/wiki/JupyterHub#Running_notebooks_as_Python_scripts/)

Here is a recommendation for a CPU request:

```bash
$ salloc --time=1:0:0 --mem-per-cpu=4G --cpus-per-task=1 --account=def-someuser
```

Here is a recommendation for a GPU request:

```bash
$ salloc --time=1:0:0 --mem-per-cpu=4G --cpus-per-task=1 --gres=gpu:a100_1g.5gb:1 --account=def-someuser