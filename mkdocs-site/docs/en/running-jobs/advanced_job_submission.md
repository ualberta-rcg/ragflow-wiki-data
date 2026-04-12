---
title: "Advanced Job Submission/en"
slug: "advanced_job_submission"
lang: "en"

source_wiki_title: "Advanced Job Submission/en"
source_hash: "f31be4d0da4bdd3d8c11846dcb0deb4b"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T04:51:57.679708+00:00"

tags:
  []

keywords:
  - "inter-job dependencies"
  - "Slurm"
  - "compute tasks"
  - "heterogeneous jobs"
  - "Job Arrays"

questions:
  - "What are the recommended tools for managing and executing a large number of compute tasks or parameter sweeps?"
  - "How can you configure Slurm jobs to run sequentially based on the completion status of previous jobs?"
  - "What is the method for requesting different CPU and memory resources for different processes within a single heterogeneous Slurm job?"
  - "What are the recommended tools for managing and executing a large number of compute tasks or parameter sweeps?"
  - "How can you configure Slurm jobs to run sequentially based on the completion status of previous jobs?"
  - "What is the method for requesting different CPU and memory resources for different processes within a single heterogeneous Slurm job?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Managing numerous compute tasks

The following tools are helpful when you need to process multiple files with or without different parameter combinations (*parameter sweep*):

*   **[Job Arrays](job_arrays.md)**: to submit several similar jobs in one single script, an ideal method when each job exceeds one hour and the number of jobs is under one thousand;
*   **[GNU Parallel](gnu_parallel.md)**: to run and manage several short calculations, including parameter sweeps, on a single node reserved via a parallel job;
*   **[GLOST](glost.md)**: the *Greedy Launcher Of Small Tasks* uses [MPI](../software/mpi.md) and a manager-worker architecture to progressively run a long list of serial jobs on the CPU cores reserved via a parallel job;
*   **[META](meta-farm.md)**: a suite of scripts designed in SHARCNET to automate high-throughput computing (running a large number of related serial, parallel, or GPU calculations).

## Inter-job dependencies

While Slurm jobs are the building blocks for compute pipelines, inter-job dependencies are the links and relationships between the steps of a pipeline. For example, if two different jobs need to run one after the other, the second job *depends* on the first one. The second could depend on the start time, the end time or the final status of the first job. Typically, we want the second job to be started only once the first job has succeeded. For example:

```bash
JOBID1=$(sbatch --parsable job1.sh)           # Save the first job ID
sbatch --dependency=afterok:$JOBID1 job2.sh   # Depends on the first job
```

!!! note "Notes"
    *   Multiple jobs can have the same dependency (multiple jobs waiting after one job).
    *   A job can have multiple dependencies (one job waiting after multiple jobs).
    *   There are multiple types of dependencies: `after`, `afterany`, `afterok`, `afternotok`, etc. For more details, see the `--dependency` option on the [official `sbatch` documentation page](https://slurm.schedmd.com/sbatch.html#OPT_dependency).

## Heterogeneous jobs

The Slurm scheduler supports [heterogeneous jobs](https://slurm.schedmd.com/heterogeneous_jobs.html). This could be very useful if you know in advance that your [MPI](../software/mpi.md) application will require more CPU cores and more memory for the main process than for the other processes.

For example, if the main process requires 8 cores and a total of 32GB of RAM, while the other processes only require 1 core and 1GB of RAM, we can specify both types of requirements in a job script:

```bash title="heterogeneous_mpi_job.sh"
#!/bin/bash
#SBATCH --ntasks=1 --cpus-per-task=8 --mem-per-cpu=4000M
#SBATCH hetjob
#SBATCH --ntasks=15 --cpus-per-task=1 --mem-per-cpu=1000M

srun --cpus-per-task=8 : --cpus-per-task=1 application.exe
```

Or we can separate resource requests with a colon (`:`) on the `sbatch` command line:

```bash
sbatch --ntasks=1 --cpus-per-task=8 --mem-per-cpu=4000M : --ntasks=15 --cpus-per-task=1 --mem-per-cpu=1000M mpi_job.sh