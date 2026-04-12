---
title: "GNU Parallel/en"
slug: "gnu_parallel"
lang: "en"

source_wiki_title: "GNU Parallel/en"
source_hash: "91dcc07509b4d4508246be9666bca3f1"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:23:18.632138+00:00"

tags:
  []

keywords:
  - "text-align"
  - "100MB"
  - "0m10.877s"
  - "sshdelay"
  - "arguments list"
  - "multiple nodes"
  - "cluster"
  - "large files handling"
  - "Slurm job"
  - "subjobs"
  - "827MB"
  - "sequential tasks"
  - "distribute workload"
  - "GNU Parallel"
  - "simulations"
  - "0m2.042s"
  - "joblog"
  - "restart capabilities"
  - "block size"
  - "SLURM"
  - "remote nodes"
  - "OpenMP"

questions:
  - "What is GNU Parallel and how does it manage resource usage by default?"
  - "How can users provide arguments or lists of commands to GNU Parallel using its specific syntax and file redirection?"
  - "Why is running GNU Parallel across multiple nodes not recommended, and what precaution should be taken if one chooses to do so?"
  - "How does GNU Parallel distribute tasks across multiple nodes and manage environment variables in a SLURM environment?"
  - "How can users track the execution status of commands and resume interrupted or failed jobs using GNU Parallel?"
  - "What arguments are used in GNU Parallel to efficiently process large files by splitting them into chunks?"
  - "Why is it necessary to add a delay using the `--sshdelay` option when starting sessions on remote nodes?"
  - "What tool is recommended for distributing workloads across multiple nodes in a cluster environment?"
  - "How does the `scontrol show hostname` command assist in setting up distributed jobs?"
  - "What specific system metrics or benchmark parameters do the memory values such as 827MB and 100MB represent in this table?"
  - "What factors contribute to the significant difference in execution times, specifically between the 2.042-second and 10.877-second runs?"
  - "How do the integer values, such as 8, 9, and -1, correlate with the memory usage and execution times recorded in the data?"
  - "How does the choice of block size impact the efficiency and core utilization of a job?"
  - "What is the recommended approach for estimating the total resources required when running hundreds or thousands of simulations?"
  - "What are the three different methods demonstrated for feeding parameters or commands into GNU Parallel within a submission script?"
  - "How does the choice of block size impact the efficiency and core utilization of a job?"
  - "What is the recommended approach for estimating the total resources required when running hundreds or thousands of simulations?"
  - "What are the three different methods demonstrated for feeding parameters or commands into GNU Parallel within a submission script?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Introduction
[GNU Parallel](http://www.gnu.org/software/parallel/) is a tool for running many sequential tasks at the same time on one or more nodes. It is useful for running a large number of sequential tasks, especially if they are short or of variable durations, as well as when doing a parameter sweep. We will only cover the basic options here; for more advanced usage, please see the [official documentation](http://www.gnu.org/software/parallel/man.html).

By default, `parallel` will run as many tasks as the number of cores allocated by the scheduler, therefore maximizing resource usage. You can change this behaviour using the option `--jobs` followed by the number of simultaneous tasks that GNU Parallel should run. When one task finishes, a new task will automatically be started by `parallel` in its stead, always keeping the maximum number of tasks running.

## Basic Usage
Parallel uses curly brackets `{}` as parameters for the command to be run. For example, to run `gzip` on all the text files in a directory, you can execute:

```bash
ls *.txt | parallel gzip {}
```

An alternative syntax is to use `:::`, such as in this example:

```bash
parallel echo {} ::: $(seq 1 3)
```

```text
1
2
3
```

Note that GNU Parallel refers to each of the commands executed as *jobs*. This can be confusing because on many of our systems, a job is a batch script run by a scheduler, and GNU Parallel would be used inside that job. From that perspective, GNU Parallel's jobs are *subjobs*.

## Multiple Arguments
You can also use multiple arguments by enumerating them, for example:

```bash
parallel echo {1} {2} ::: $(seq 1 3) ::: $(seq 2 3)
```

```text
1 2
1 3
2 2
2 3
3 2
3 3
```

## File Content as Argument List
The syntax `::::` takes the content of a file to generate the list of values for the arguments. For example, if you have a list of parameter values in file `mylist.txt`, you may display its content with:

```bash
parallel echo {1} :::: mylist.txt
```

## File Content as Command List
GNU Parallel can also interpret the lines of a file as the actual subjobs to be run in parallel, by using redirection. For example, if you have a list of subjobs in file `my_commands.txt` (one per line), you may run them in parallel as follows:

```bash
parallel < my_commands.txt
```

Note that there are no commands or arguments given to Parallel. This usage mode can be particularly useful if the subjobs contain symbols that are special to GNU Parallel, or the subcommands are to contain a few commands (e.g. `cd dir1 && ./executable`).

Here is an example how to run a Slurm job using GNU Parallel. The list of commands in `my_commands.txt` will be run sequentially using 4 CPUs. As soon as one command completes, a new one will be started to maintain the total of 4 commands running at the same time, until the list is exhausted.

=== "Script"

```bash title="run_gnuparallel_test.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --cpus-per-task=4
#SBATCH --time=00-02:00
#SBATCH --mem=4000M     # Total memory for all tasks

parallel --joblog parallel.log < ./my_commands.txt
```

=== "List of Tasks"

```text title="my_commands.txt"
command1
command2
command3
command4
command5
command6
command7
command8
command9
```

## Running on Multiple Nodes
!!! warning "Not recommended"
    While GNU Parallel can be used across multiple nodes, it can have problems doing so, and it is not recommended, in particular in the context of a lot of short jobs. That is because it needs to start an SSH session on remote nodes, an operation which often requires several seconds and may hang. If you choose to use it, make sure you add a delay between jobs of 30 seconds or more, using the option `--sshdelay 30`.

You can also use GNU Parallel to distribute a workload across multiple nodes in a cluster, such as in the context of a job on our servers. An example of this use is the following:

```bash
scontrol show hostname > ./node_list_${SLURM_JOB_ID}
```

```bash
parallel --jobs $SLURM_NTASKS_PER_NODE --sshloginfile ./node_list_${SLURM_JOB_ID} --env MY_VARIABLE --workdir $PWD --sshdelay 30 ./my_program
```

In this case, we create a file containing the list of nodes, and we use this file to tell GNU Parallel which nodes to use for the distribution of tasks. The `--env` option allows us to transfer a named environment variable to all the nodes while the `--workdir` option ensures that the GNU Parallel tasks will start in the same directory as the main node.

For example, when a long list of [OpenMP](openmp.md) tasks are executed as a single job submitted with `--nodes=N`, `--ntasks-per-node=5` and `--cpus-per-task=8`, the following command will take into account all processes to be started on all reserved nodes and the number of OpenMP threads per process:

```bash
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
```

```bash
parallel --jobs $SLURM_NTASKS_PER_NODE --sshloginfile ./node_list_${SLURM_JOB_ID} --workdir $PWD --env OMP_NUM_THREADS --sshdelay 30 ./my_program
```

In this case, up to `5*N` OpenMP processes are running simultaneously with a CPU usage of up to `800%` each.

## Keeping Track of Completed and Failed Commands, and Restart Capabilities
You can tell GNU Parallel to keep track of which commands have completed by using the `--joblog JOBLOGFILE` argument. The file JOBLOGFILE will contain the list of completed commands, their start times, durations, hosts, and exit values. For example,

```bash
ls *.txt | parallel --joblog gzip.log gzip {}
```

The job log functionality opens the door to a number of possible restart options. If the `parallel` command was interrupted (e.g. your job ran longer than the requested walltime for a job), you can make it pick up where it left off using the `--resume` option, for instance:

```bash
ls *.txt | parallel --resume --joblog gzip.log gzip {}
```

The new jobs will be appended to the old log file.

If some of the subcommands failed (i.e. they produced a non-zero exit code) and you think that you have eliminated the source of the error, you can re-run the failed ones, using `--resume-failed`, e.g.:

```bash
ls *.txt | parallel --resume-failed --joblog gzip.log gzip {}
```

Note that this will also start subjobs that were not considered before.

## Handling large files
Let's say we want to count the characters in parallel from a big [FASTA](https://en.wikipedia.org/wiki/FASTA_format) file (`database.fa`) in a task with 8 cores. We will have to use the GNU Parallel `--pipepart` and `--block` arguments to efficiently handle chunks of the file.

```bash
parallel --jobs $SLURM_CPUS_PER_TASK --keep-order --block -1 --recstart '>' --pipepart wc :::: database.fa
```

By varying the `block` size we get:

| | # Cores in task | Ref. database size | Block read size | # GNU parallel jobs | # Cores used | Time counting chars |
|:---|----------------:|-------------------:|----------------:|--------------------:|-------------:|--------------------:|
| 1 |               8 |              827MB |            10MB |                  83 |            8 |            0m2.633s |
| 2 |               8 |              827MB |           100MB |                   9 |            8 |            0m2.042s |
| 3 |               8 |              827MB |           827MB |                   1 |            1 |           0m10.877s |
| 4 |               8 |              827MB |              -1 |                   8 |            8 |            0m1.734s |

This table shows that choosing the right block size has a real impact on the efficiency and the number of cores actually used.
The first line shows that the block size is too small, resulting in many jobs dispatched over the available cores.
The second line is a better block size, since it results in a number of jobs close to the number of available cores.
The third line shows that the block size is too big and that we are only using 1 core out of 8, therefore inefficiently processing chunks.
Finally, the last line shows that in many cases, letting GNU Parallel adapt and decide on the block size is often faster.

## Running hundreds or thousands of simulations
First, you must determine how many resources are required by one simulation, then you can estimate the total resources required in your job.

The submission scripts given in the examples below are based on: 1 serial simulation requiring 2 GB of memory, 1 core and 5 minutes, and 1000 simulations. It would take 83.3 hours or 3.472 days to run with 1 core.

On one node, using 32 cores, it can be completed in 2.6 hours.
One could also use more than one node (see [Running on Multiple Nodes](#running-on-multiple-nodes)).

### Arguments List
As shown in section [File Content as Argument List](#file-content-as-argument-list), you can use a file containing all the parameters. In this case, parameters are delimited by a tab character (`\t`) and each line corresponds to one simulation.

=== "Parameters"

```text title="my_parameters.txt"
1   1
1   2
1   3
...
```

=== "Script"

```bash title="sim_submit.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --nodes=1
#SBATCH --cpus-per-task=32
#SBATCH --time=03:00:00
#SBATCH --mem-per-cpu=2G

# Read the parameters, placing each column to their respective argument
parallel -j $SLURM_CPUS_PER_TASK --colsep '\t' my_simulator --alpha {1} --beta {2} :::: ./my_parameters.txt
```

### Commands List
As shown in the section [File Content as Command List](#file-content-as-command-list), you can use a file containing all the commands and their parameters.

=== "Commands"

```text title="my_commands.txt"
my_simulator --alpha 1 --beta 1
my_simulator --alpha 1 --beta 2
my_simulator --alpha 1 --beta 3
...
```

=== "Script"

```bash title="sim_submit.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --nodes=1
#SBATCH --cpus-per-task=32
#SBATCH --time=03:00:00
#SBATCH --mem-per-cpu=2G

parallel -j $SLURM_CPUS_PER_TASK < ./my_commands.txt
```

### Multiple Arguments
You can use GNU Parallel to generate the parameters and feed them to the command.

```bash title="sim_submit.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --nodes=1
#SBATCH --cpus-per-task=32
#SBATCH --time=03:00:00
#SBATCH --mem-per-cpu=2G

# Generates 1000 simulations where the alpha argument ranges from 1-10, and beta from 1-100
# placing each source to their respective argument
parallel -j $SLURM_CPUS_PER_TASK my_simulator --alpha {1} --beta {2} ::: {1..10} ::: {1..100}
```

## Related topics
* [META](meta-a-package-for-job-farming.md)
* [GLOST](glost.md)
* [Job arrays](job-arrays.md)