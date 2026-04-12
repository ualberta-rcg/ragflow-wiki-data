---
title: "Dedalus"
slug: "dedalus"
lang: "base"

source_wiki_title: "Dedalus"
source_hash: "6183527f6b83ce95d50869af2624c387"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:51:07.082449+00:00"

tags:
  []

keywords:
  - "Slurm"
  - "submit-dedalus-whole-nodes.sh"
  - "Dedalus"
  - "Python virtual environment"
  - "bash"
  - "SBATCH"
  - "virtual environment"
  - "job submission"
  - "job submission script"
  - "Whole nodes"
  - "sbatch"
  - "MPI"
  - "partial differential equations"
  - "MPI scheduling"

questions:
  - "What is the Dedalus framework and how can users check its available versions on the clusters?"
  - "What are the required steps to install Dedalus and its dependencies inside a Python virtual environment?"
  - "How should a user configure a job submission script to run Dedalus distributed across multiple nodes or cores?"
  - "How are the computing resources allocated and which software modules are loaded for this job?"
  - "What steps are taken to create and configure the Python virtual environment across all allocated nodes?"
  - "How is the final Python script executed, and what is the proper procedure for testing and submitting the job to the scheduler?"
  - "What is the primary purpose of the `submit-dedalus-whole-nodes.sh` bash script shown in the snippet?"
  - "How do the `#SBATCH` directives configure the job's accounting group, walltime, and node allocation?"
  - "Based on the syntax used in the script, what type of workload management system is this job submission intended for?"
  - "How are the computing resources allocated and which software modules are loaded for this job?"
  - "What steps are taken to create and configure the Python virtual environment across all allocated nodes?"
  - "How is the final Python script executed, and what is the proper procedure for testing and submitting the job to the scheduler?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Dedalus](https://dedalus-project.org/) is a flexible framework for solving partial differential equations using modern spectral methods.

## Available versions
Dedalus is available on our clusters as prebuilt Python packages (wheels). You can list available versions with `avail_wheels`.

```bash
avail_wheels dedalus
```
```text
name     version    python    arch
-------  ---------  --------  ---------
dedalus  3.0.2      cp311     x86-64-v3
dedalus  3.0.2      cp310     x86-64-v3
```

## Installing Dedalus in a Python virtual environment
1. Load Dedalus runtime dependencies.

```bash
module load StdEnv/2023 gcc openmpi mpi4py/3.1.4 fftw-mpi/3.3.10 hdf5-mpi/1.14.2 python/3.11
```

2. Create and activate a Python virtual environment.

```bash
virtualenv --no-download ~/dedalus_env
source ~/dedalus_env/bin/activate
```

3. Install a specific version of Dedalus and its Python dependencies.

```bash
pip install --no-index --upgrade pip
pip install --no-index dedalus==X.Y.Z
```
where `X.Y.Z` is the exact desired version, for instance `3.0.2`.
You can omit to specify the version in order to install the latest one available from the wheelhouse.

4. Validate it.

```bash
python -c 'import dedalus'
```

5. Freeze the environment and requirements set.

```bash
pip freeze --local > ~/dedalus-3.0.2-requirements.txt
```

6. Remove the local virtual environment.

```bash
deactivate && rm -r ~/dedalus_env
```

## Running Dedalus
You can run Dedalus distributed across multiple nodes or cores.
For efficient MPI scheduling, please see:
* [MPI job](../running-jobs/running_jobs.md#mpi-job)
* [Advanced MPI scheduling](../running-jobs/advanced_mpi_scheduling.md)

1. Write your job submission script.

```tabs
  ```tab "Distributed"
```bash title="submit-dedalus-distributed.sh"
#!/bin/bash

#SBATCH --account=def-someprof    # adjust this to match the accounting group you are using to submit jobs
#SBATCH --time=08:00:00           # adjust this to match the walltime of your job
#SBATCH --ntasks=4                # adjust this to match the number of tasks/processes to run
#SBATCH --mem-per-cpu=4G          # adjust this according to the memory you need per process

# Run on cores across the system : https://docs.alliancecan.ca/wiki/Advanced_MPI_scheduling#Few_cores,_any_number_of_nodes

# Load modules dependencies.
module load StdEnv/2023 gcc openmpi mpi4py/3.1.4 fftw-mpi/3.3.10 hdf5-mpi/1.14.2 python/3.11

# create the virtual environment on each allocated node:
srun --ntasks $SLURM_NNODES --tasks-per-node=1 bash << EOF
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate

pip install --no-index --upgrade pip
pip install --no-index -r dedalus-3.0.2-requirements.txt
EOF

# activate only on main node
source $SLURM_TMPDIR/env/bin/activate;

export OMP_NUM_THREADS=1

# srun exports the current env, which contains $VIRTUAL_ENV and $PATH variables
srun python $SCRATCH/myscript.py;
```
  ```tab "Whole nodes"
```bash title="submit-dedalus-whole-nodes.sh"
#!/bin/bash

#SBATCH --account=def-someprof    # adjust this to match the accounting group you are using to submit jobs
#SBATCH --time=08:00:00           # adjust this to match the walltime of your job
#SBATCH --nodes=2                 # adjust this to match the number of whole node
#SBATCH --ntasks-per-node=4       # adjust this to match the number of tasks/processes to run per node
#SBATCH --mem-per-cpu=4G          # adjust this according to the memory you need per process

# Run on N whole nodes : https://docs.alliancecan.ca/wiki/Advanced_MPI_scheduling#Whole_nodes

# Load modules dependencies.
module load StdEnv/2023 gcc openmpi mpi4py/3.1.4 fftw-mpi/3.3.10 hdf5-mpi/1.14.2 python/3.11

# create the virtual environment on each allocated node:
srun --ntasks $SLURM_NNODES --tasks-per-node=1 bash << EOF
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate

pip install --no-index --upgrade pip
pip install --no-index -r dedalus-3.0.2-requirements.txt
EOF

# activate only on main node
source $SLURM_TMPDIR/env/bin/activate;

export OMP_NUM_THREADS=1

# srun exports the current env, which contains $VIRTUAL_ENV and $PATH variables
srun python $SCRATCH/myscript.py;
```
```

2. Submit your job to the scheduler.

Before submitting your job, it is important to test that your submission script will start without errors.
You can do a quick test in an [interactive job](../running-jobs/running_jobs.md#interactive-jobs).

```bash
sbatch submit-dedalus.sh