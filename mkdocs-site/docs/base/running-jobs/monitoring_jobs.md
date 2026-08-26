---
title: "Monitoring jobs"
slug: "monitoring_jobs"
lang: "base"

source_wiki_title: "Monitoring jobs"
source_hash: "5d27babb4e4af6520dca951b49f54ada"
last_synced: "2026-08-26T10:16:11.334907+00:00"
last_processed: "2026-08-26T11:13:02.420069+00:00"

tags:
  []

keywords:
  - "sbatch --mail-type"
  - "sacct --duplicates"
  - "squeue"
  - "srun --jobid"
  - "extern step"
  - "output buffering"
  - "MaxRSS"
  - "tmux"
  - "batch step"
  - "resource consumption"
  - "submission script"
  - "srun"
  - "seff"
  - "sstat"
  - "sacct"

questions:
  - "What tools and commands are recommended for checking the performance and resource efficiency of both running and completed Slurm jobs?"
  - "How can you set up email notifications for job events, and why should `squeue` not be executed frequently from scripts?"
  - "Why is output from non‑interactive Slurm jobs buffered, and what method is suggested for real‑time monitoring of job output?"
  - "How can you display all accounting records for a job, including those from restarts, using the `sacct` command?"
  - "Which accounting fields should you request to identify the task and node that used the maximum memory (`MaxRSS`)?"
  - "What commands and options allow you to attach to a running job (e.g., with `srun` and `tmux`) to monitor GPU usage or other processes without exceeding the job’s allocated resources?"
  - "What is the function of the batch step (.bat+) in a submission script?"
  - "How does invoking srun within the submission script create a .0 step and impact resource usage?"
  - "What is the purpose of the extern step (.ext+), and does it consume significant resources?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Ensuring that your jobs make efficient use of the resources that are assigned to them is an important part of being a responsible user. This is particularly true when you are using a new program or have made some other substantial change in the work being done by your job.

The best tool for examining job performance is the Metrix web service or "portal" for each cluster. Please see [Metrix](../software/metrix.md) for a description of the tool and a list of URLs.

The remainder of *this* page describes other methods for evaluating the efficiency of jobs.

## Current jobs

By default [squeue](https://slurm.schedmd.com/squeue.html) will show all the jobs the scheduler is managing at the moment. It will run much faster if you ask only about your own jobs with
```bash
$ squeue -u $USER
```
You can also use the utility `sq` to do the same thing with less typing.

You can show only running jobs, or only pending jobs:
```bash
$ squeue -u <username> -t RUNNING
$ squeue -u <username> -t PENDING
```

You can show detailed information for a specific job with [scontrol](https://slurm.schedmd.com/scontrol.html):
```bash
$ scontrol show job -dd <jobid>
```

!!! warning "Do not run `squeue` frequently from scripts"
    **Do not** run `squeue` from a script or program at high frequency (e.g., every few seconds). Responding to `squeue` adds load to Slurm and may interfere with its performance or correct operation.

### Email notification

You can ask to be notified by email of certain job conditions by supplying options to sbatch:
```bash
#SBATCH --mail-user=your.email@example.com
#SBATCH --mail-type=ALL
```
For a complete list of the options see [SchedMD's documentation](https://slurm.schedmd.com/sbatch.html#OPT_mail-type).

### Output buffering

Output from a non-interactive Slurm job is normally *buffered*, which means that there is usually a delay between when data is written by the job and when you can see the output on a login node. Depending on the application you are running and the load on the filesystem, this delay can range from less than a second to many minutes, or until the job completes.

!!! warning "Do not disable output buffering"
    There are methods to reduce or eliminate the buffering, but we do not recommend using them because buffering is vital to preserving the overall performance of the filesystem. If you need to monitor the output from a job in *real time*, we recommend you run an [interactive job](#interactive-jobs).

## Completed jobs

Get a short summary of the CPU and memory efficiency of a job with `seff`:
```bash
$ seff 12345678
Job ID: 12345678
Cluster: cedar
User/Group: jsmith/jsmith
State: COMPLETED (exit code 0)
Cores: 1
CPU Utilized: 02:48:58
CPU Efficiency: 99.72% of 02:49:26 core-walltime
Job Wall-clock time: 02:49:26
Memory Utilized: 213.85 MB
Memory Efficiency: 0.17% of 125.00 GB
```

Find more detailed information about a completed job with [sacct](https://slurm.schedmd.com/sacct.html), and optionally, control what it prints using `--format`:
```bash
$ sacct -j <jobid>
$ sacct -j <jobid> --format=JobID,JobName,MaxRSS,Elapsed
```

The output from `sacct` typically includes records labelled `.bat+` and `.ext+`, and possibly `.0, .1, .2, ...`.
The batch step (`.bat+`) is your submission script - for many jobs that's where the main part of the work is done and where the resources are consumed.
If you use `srun` in your submission script, that would create a `.0` step that would consume most of the resources.
The extern (`.ext+`) step is basically prologue and epilogue and normally doesn't consume any significant resources.

If a node fails while running a job, the job may be restarted. `sacct` will normally show you only the record for the last (presumably successful) run. If you wish to see all records related to a given job, add the `--duplicates` option.

Use the MaxRSS accounting field to determine how much memory a job needed. The value returned will be the largest [resident set size](https://en.wikipedia.org/wiki/Resident_set_size) for any of the tasks. If you want to know which task and node this occurred on, print the MaxRSSTask and MaxRSSNode fields also.

The [sstat](https://slurm.schedmd.com/sstat.html) command works on a running job much the same way that [sacct](https://slurm.schedmd.com/sacct.html) works on a completed job.

## Attaching to a running job
It is possible to connect to the node running a job and execute new processes there. You might want to do this for troubleshooting or to monitor the progress of a job.

Suppose you want to run the utility [nvidia-smi](https://developer.nvidia.com/nvidia-system-management-interface) to monitor GPU usage on a node where you have a job running. The following command runs `watch` on the node assigned to the given job, which in turn runs `nvidia-smi` every 30 seconds, displaying the output on your terminal.

```bash
$ srun --jobid 123456 --overlap --pty watch -n 30 nvidia-smi
```

It is possible to launch multiple monitoring commands using [tmux](prolonging_terminal_sessions.md#tmux). The following command launches `htop` and `nvidia-smi` in separate panes to monitor the activity on a node assigned to the given job.

```bash
$ srun --jobid 123456 --overlap --pty tmux new-session -d 'htop -u $USER' \; split-window -h 'watch nvidia-smi' \; attach
```

!!! warning "Resource Consumption"
    Processes launched with `srun` share the resources with the job specified. You should therefore be careful not to launch processes that would use a significant portion of the resources allocated for the job. Using too much memory, for example, might result in the job being killed; using too many CPU cycles will slow down the job.

!!! note
    The `srun` commands shown above work only to monitor a job submitted with `sbatch`. To monitor an interactive job, create multiple panes with `tmux` and start each process in its own pane.

## Monitoring a GPU job
See [Monitor GPU usage](../programming/nvtop.md#monitor-gpu-usage)