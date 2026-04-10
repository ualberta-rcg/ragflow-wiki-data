---
title: "Advanced Job Submission/fr"
tags:
  []

keywords:
  []
---

<span id="Managing_numerous_compute_tasks"></span>
<div class="mw-translate-fuzzy">
## Soumettre plusieurs tâches de calcul 
</div>

<div lang="en" dir="ltr" class="mw-content-ltr">
The following tools are helpful when you need to process multiple files with or without different parameter combinations (*parameter sweep*):
</div>

<div lang="en" dir="ltr" class="mw-content-ltr">
* <b>[Job Arrays](job_arrays.md)</b>: to submit several similar jobs in one single script, an ideal method when each job exceeds one hour and the number of jobs is under one thousand;
* <b>[GNU Parallel](gnu_parallel.md)</b>: to run and manage several short calculations, including parameter sweeps, on a single node reserved via a parallel job;
* <b>[GLOST](glost.md)</b>: the <i>Greedy Launcher Of Small Tasks</i> uses [MPI](mpi.md) and a manager-worker architecture to progressively run a long list of serial jobs on the CPU cores reserved via a parallel job;
* <b>[META](meta-farm.md)</b>: a suite of scripts designed in SHARCNET to automate high-throughput computing (running a large number of related serial, parallel, or GPU calculations).
</div>

<div lang="en" dir="ltr" class="mw-content-ltr">
## Inter-job dependencies 
</div>

<div lang="en" dir="ltr" class="mw-content-ltr">
While Slurm jobs are the building blocks for compute pipelines, inter-job dependencies are the links and relationships between the steps of a pipeline. For example, if two different jobs need to run one after the other, the second job *depends* on the first one. The second could depend on the start time, the end time or the final status of the first job. Typically, we want the second job to be started only once the first job has succeeded. For example:
</div>

<div lang="en" dir="ltr" class="mw-content-ltr">

```bash

```
$(sbatch --parsable job1.sh)           # Save the first job ID
|sbatch --dependencyafterok:$JOBID1 job2.sh   # Depends on the first job
}}
</div>

<div lang="en" dir="ltr" class="mw-content-ltr">
Notes
* Multiple jobs can have the same dependency (multiple jobs waiting after one job).
* A job can have multiple dependencies (one job waiting after multiple jobs).
* There are multiple types of dependencies: `after`, `afterany`, `afterok`, `afternotok`, etc. For more details, see the `--dependency` option on the [official `sbatch` documentation page](https://slurm.schedmd.com/sbatch.html#OPT_dependency).
</div>

<div lang="en" dir="ltr" class="mw-content-ltr">
## Heterogeneous jobs 
</div>

<div lang="en" dir="ltr" class="mw-content-ltr">
The Slurm scheduler supports [heterogeneous jobs](https://slurm.schedmd.com/heterogeneous_jobs.html). This could be very useful if you know in advance that your [MPI](mpi.md) application will require more CPU cores and more memory for the main process than for the other processes.
</div>

<div lang="en" dir="ltr" class="mw-content-ltr">
For example, if the main process requires 8 cores and a total of 32GB of RAM, while the other processes only require 1 core and 1GB of RAM, we can specify both types of requirements in a job script:
</div>

**`heterogeneous_mpi_job.sh`**
```sh
#!/bin/bash
#SBATCH --ntasks=1 --cpus-per-task=8 --mem-per-cpu=4000M
#SBATCH hetjob
#SBATCH --ntasks=15 --cpus-per-task=1 --mem-per-cpu=1000M

srun --cpus-per-task=8 : --cpus-per-task=1 application.exe
```

<div lang="en" dir="ltr" class="mw-content-ltr">
Or we can separate resource requests with a colon (`:`) on the `sbatch` command line:
</div>

```bash

```
1 --cpus-per-task8 --mem-per-cpu4000M : --ntasks15 --cpus-per-task1 --mem-per-cpu1000M  mpi_job.sh
}}