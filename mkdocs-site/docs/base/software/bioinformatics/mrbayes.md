---
title: "MrBayes"
slug: "mrbayes"
lang: "base"

source_wiki_title: "MrBayes"
source_hash: "617a82055a165823dc8cf9b73ce3b087"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:32:36.811371+00:00"

tags:
  []

keywords:
  - "Markov chain Monte Carlo"
  - "MrBayes"
  - "mcmc"
  - "append keyword"
  - "Slurm jobs"
  - "Slurm job scripts"
  - "Checkpointing"
  - "primates.nex"
  - "job array"
  - "split calculation"
  - "job1.nex"
  - "sbatch"
  - "Bayesian inference"

questions:
  - "What is the primary purpose of the MrBayes program and what statistical method does it use to estimate model parameters?"
  - "What are the different hardware configurations, such as sequential, MPI parallel, and GPU, available for running MrBayes job scripts?"
  - "How does the checkpointing mechanism in MrBayes help manage very long computational runs across multiple jobs?"
  - "What specific MCMC parameters are defined in the Nexus file to control the execution and stopping rules of the MrBayes calculation?"
  - "How does the provided bash script utilize a Slurm job array and the $SLURM_ARRAY_TASK_ID variable to manage multiple calculation jobs?"
  - "What command is required to submit the configured job script to the cluster?"
  - "What is the primary purpose of creating the two files, job1.nex and job2.nex?"
  - "How are the two Slurm jobs scheduled to execute in relation to one another?"
  - "What is the key syntax difference between the first and second job files?"
  - "What specific MCMC parameters are defined in the Nexus file to control the execution and stopping rules of the MrBayes calculation?"
  - "How does the provided bash script utilize a Slurm job array and the $SLURM_ARRAY_TASK_ID variable to manage multiple calculation jobs?"
  - "What command is required to submit the configured job script to the cluster?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[MrBayes](https://nbisweden.github.io/MrBayes/) is a program for Bayesian inference and model choice across a wide range of phylogenetic and evolutionary models. MrBayes uses Markov chain Monte Carlo (MCMC) methods to estimate the posterior distribution of model parameters.

## Finding available modules
```bash
module spider mrbayes
```
For more on finding and selecting a version of MrBayes using `module` commands see [Using modules](../../programming/modules.md)

## Examples

### Sequential
The following job script uses only one CPU core (`--cpus-per-task=1`).
The example uses an input file (`primates.nex`) distributed with MrBayes.

```bash title="submit-mrbayes-seq.sh"
#!/bin/bash
#SBATCH --account=def-someuser  # replace with your PI account
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=3G        # increase as needed
#SBATCH --time=1:00:00          # increase as needed

module load mrbayes/3.2.7
cd $SCRATCH
cp -v $EBROOTMRBAYES/share/examples/mrbayes/primates.nex .

srun mb primates.nex
```

The job script can be submitted with
```bash
sbatch submit-mrbayes-seq.sh
```

### Parallel
MrBayes can be run on multiple cores, on multiple nodes, and on GPUs.

#### MPI
The following job script will use 8 CPU cores in total, on one or more nodes.
Like the previous example, it uses an input file (`primates.nex`) distributed with MrBayes.

```bash title="submit-mrbayes-parallel.sh"
#!/bin/bash
#SBATCH --account=def-someuser  # replace with your PI account
#SBATCH --ntasks=8 				# increase as needed
#SBATCH --mem-per-cpu=3G        # increase as needed
#SBATCH --time=1:00:00          # increase as needed

module load mrbayes/3.2.7
cd $SCRATCH
cp -v $EBROOTMRBAYES/share/examples/mrbayes/primates.nex .

srun mb primates.nex
```

The job script can be submitted with
```bash
sbatch submit-mrbayes-parallel.sh
```

#### GPU
The following job script will use a GPU.
Like the previous examples, it uses an input file (`primates.nex`) distributed with MrBayes.

```bash title="submit-mrbayes-gpu.sh"
#!/bin/bash
#SBATCH --account=def-someuser  # replace with your PI account
#SBATCH --cpus-per-task=1
#SBATCH --gpus=1
#SBATCH --mem-per-cpu=3G        # increase as needed
#SBATCH --time=1:00:00          # increase as needed

module load gcc cuda/12 mrbayes/3.2.7
cd $SCRATCH
cp -v $EBROOTMRBAYES/share/examples/mrbayes/primates.nex .

srun mb primates.nex
```

The job script can be submitted with
```bash
sbatch submit-mrbayes-gpu.sh
```

## Checkpointing
!!! tip
    If you need very long runs of MrBayes, we suggest you break up the work into several small jobs rather than one very long job. Long jobs are more likely to be interrupted by hardware failure or maintenance outage. Fortunately, MrBayes has a mechanism for creating checkpoints, in which progress can be saved from one job and continued in a subsequent job.

Here is an example of how to split a calculation into two Slurm jobs which will run one after the other. Create two files, `job1.nex` and `job2.nex`, as shown below. Notice that the key difference between them is the presence of the `append` keyword in the second.

```text title="job1.nex"
execute primates.nex;

mcmc ngen=10000000 nruns=2 temp=0.02 mcmcdiag=yes samplefreq=1000
stoprule=yes stopval=0.005 relburnin=yes burninfrac=0.1 printfreq=1000
checkfreq=1000;
```

```text title="job2.nex"
execute primates.nex;

mcmc ngen=20000000 nruns=2 temp=0.02 mcmcdiag=yes samplefreq=1000
stoprule=yes stopval=0.005 relburnin=yes burninfrac=0.1 printfreq=1000
append=yes checkfreq=1000;
```

Then create a job script. This example is a job array, which means that one script and one `sbatch` command will be sufficient to launch two Slurm jobs, and therefore both parts of the calculation. See [Job arrays](../../running-jobs/job_arrays.md) for more about the `--array` parameter and the `$SLURM_ARRAY_TASK_ID` variable used here.

```bash title="submit-mrbayes-cp.sh"
#!/bin/bash
#SBATCH --account=def-someuser  # replace with your PI account
#SBATCH --ntasks=8 				# increase as needed
#SBATCH --mem-per-cpu=3G        # increase as needed
#SBATCH --time=1:00:00          # increase as needed
#SBATCH --array=1-2%1           # match the number of sub-jobs, only 1 at a time

module load gcc mrbayes/3.2.7
cd $SCRATCH
cp -v $EBROOTMRBAYES/share/examples/mrbayes/primates.nex .

srun mb job${SLURM_ARRAY_TASK_ID}.nex
```

The example can be submitted with
```bash
sbatch submit-mrbayes-cp.sh