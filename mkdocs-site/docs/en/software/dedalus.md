---
title: "Dedalus/en"
slug: "dedalus"
lang: "en"

source_wiki_title: "Dedalus/en"
source_hash: "b16c0558e027bfec458b1793a5608aaa"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:51:26.844707+00:00"

tags:
  []

keywords:
  - "module load"
  - "Dedalus"
  - "Python virtual environment"
  - "interactive job"
  - "SBATCH"
  - "whole nodes"
  - "virtual environment"
  - "SLURM"
  - "job submission"
  - "job submission script"
  - "openmpi"
  - "partial differential equations"
  - "MPI scheduling"

questions:
  - "What is the Dedalus framework and how can users check its available prebuilt versions on the clusters?"
  - "What are the necessary steps to set up a Python virtual environment and install a specific version of Dedalus?"
  - "How should users configure their job submission scripts to run Dedalus efficiently across multiple nodes or cores?"
  - "How is the virtual environment created and populated with dependencies across all allocated nodes?"
  - "What environment variables and commands are used to execute the Python script on the main node?"
  - "What is the recommended procedure for testing and submitting the job to the scheduler?"
  - "What are the specific SLURM resource allocations defined in the script for tasks and memory?"
  - "Which software modules and specific versions are required to be loaded for this environment?"
  - "What external documentation is referenced for configuring the job to run on whole nodes?"
  - "How is the virtual environment created and populated with dependencies across all allocated nodes?"
  - "What environment variables and commands are used to execute the Python script on the main node?"
  - "What is the recommended procedure for testing and submitting the job to the scheduler?"

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

Expected output:
```
name     version    python    arch
-------  ---------  --------  ---------
dedalus  3.0.2      cp311     x86-64-v3
dedalus  3.0.2      cp310     x86-64-v3
```

## Installing Dedalus in a Python virtual environment
1.  Load Dedalus runtime dependencies.

    ```bash
    module load StdEnv/2023 gcc openmpi mpi4py/3.1.4 fftw-mpi/3.3.10 hdf5-mpi/1.14.2 python/3.11
    ```

2.  Create and activate a Python virtual environment.

    ```bash
    virtualenv --no-download ~/dedalus_env
    source ~/dedalus_env/bin/activate
    ```

3.  Install a specific version of Dedalus and its Python dependencies.

    ```bash
    pip install --no-index --upgrade pip
    pip install --no-index dedalus==X.Y.Z
    ```

    where `X.Y.Z` is the exact desired version, for instance `3.0.2`.
    You can omit to specify the version in order to install the latest one available from the wheelhouse.

4.  Validate it.

    ```bash
    python -c 'import dedalus'
    ```

5.  Freeze the environment and requirements set.

    ```bash
    pip freeze --local > ~/dedalus-3.0.2-requirements.txt
    ```

6.  Remove the local virtual environment.

    ```bash
    deactivate && rm -r ~/dedalus_env
    ```

## Running Dedalus
You can run Dedalus distributed across multiple nodes or cores.
For efficient MPI scheduling, please see:
*   [MPI job](../running-jobs/running_jobs.md#mpi-job)
*   [Advanced MPI scheduling](../running-jobs/advanced_mpi_scheduling.md)

1.  Write your job submission script.

~~~tabs
~~~bash tab="submit-dedalus-distributed.sh"
#!/bin/bash

#SBATCH --account=def-someprof    # adjust this to match the accounting group you are using to submit jobs
#SBATCH --time=08:00:00           # adjust this to match the walltime of your job
#SBATCH --ntasks=4                # adjust this to match the number of tasks/processes to run
#SBATCH --mem-per-cpu=4G          # adjust this according to the memory you need per process

# Run on cores across the system : https://docs.alliancecan.ca/wiki/Advanced_MPI_scheduling#Few_cores,_any_number_of_nodes

# Load modules dependencies.
module load StdEnv/2023 gcc openmpi mpi4py/3.1.4 fftw-mpi/3.3.10 hdf5-mpi/1.14.2 python/3.11

# create the virtual environment on each allocated node:
srun --ntasks "$SLURM_NNODES" --tasks-per-node=1 bash << EOF
virtualenv --no-download "$SLURM_TMPDIR"/env
source "$SLURM_TMPDIR"/env/bin/activate

pip install --no-index --upgrade pip
pip install --no-index -r dedalus-3.0.2-requirements.txt
EOF

# activate only on main node
source "$SLURM_TMPDIR"/env/bin/activate;

export OMP_NUM_THREADS=1

# srun exports the current env, which contains $VIRTUAL_ENV and $PATH variables
srun python "$SCRATCH"/myscript.py;
~~~

~~~bash tab="submit-dedalus-whole-nodes.sh"
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
srun --ntasks "$SLURM_NNODES" --tasks-per-node=1 bash << EOF
virtualenv --no-download "$SLURM_TMPDIR"/env
source "$SLURM_TMPDIR"/env/bin/activate

pip install --no-index --upgrade pip
pip install --no-index -r dedalus-3.0.2-requirements.txt
EOF

# activate only on main node
source "$SLURM_TMPDIR"/env/bin/activate;

export OMP_NUM_THREADS=1

# srun exports the current env, which contains $VIRTUAL_ENV and $PATH variables
srun python "$SCRATCH"/myscript.py;
~~~
~~~

2.  Submit your job to the scheduler.

!!! tip "Test Your Submission Script"
    Before submitting your job, it is important to test that your submission script will start without errors. You can do a quick test in an [interactive job](../running-jobs/running_jobs.md#interactive-jobs).

```bash
sbatch submit-dedalus.sh