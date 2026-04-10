---
title: "Dedalus/en"
slug: "dedalus"
lang: "en"

source_wiki_title: "Dedalus/en"
source_hash: "b16c0558e027bfec458b1793a5608aaa"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T06:07:31.207355+00:00"

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
(dedalus_env) [name@server ~]$ pip install --no-index --upgrade pip
(dedalus_env) [name@server ~]$ pip install --no-index dedalus==X.Y.Z
```
where `X.Y.Z` is the exact desired version, for instance `3.0.2`.
You can omit to specify the version in order to install the latest one available from the wheelhouse.

4. Validate it.
```bash
(dedalus_env) [name@server ~]$ python -c 'import dedalus'
```

5. Freeze the environment and requirements set.
```bash
(dedalus_env) [name@server ~]$ pip freeze --local > ~/dedalus-3.0.2-requirements.txt
```

6. Remove the local virtual environment.
```bash
(dedalus_env) [name@server ~]$ deactivate && rm -r ~/dedalus_env
```

## Running Dedalus
You can run Dedalus distributed across multiple nodes or cores.
For efficient MPI scheduling, please see:
* [MPI job](running-jobs.md#mpi-job)
* [Advanced MPI scheduling](advanced-mpi-scheduling.md)

1. Write your job submission script.

=== "submit-dedalus-distributed.sh"
    ```bash
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

=== "submit-dedalus-whole-nodes.sh"
    ```bash
    #!/bin/bash

    #SBATCH --account=def-someprof    # adjust this to match the accounting group you are using to submit jobs
    #SBATCH --time=08:00:00           # adjust this to match the walltime of your job
    #SBATCH --nodes=2                 # adjust this to match the number of whole node
    #SBATCH --ntasks-per-node=4       # adjust this to match the number of tasks/processes to run per node
    #SBATCH --mem-per-cpu=4G          # adjust this according to the memory you need per process

    # Run on N whole nodes : https://docs.alliancecan.ca/wiki/Advanced_MPI_scheduling#Whole_nodes

    # Load modules dependencies.
    module load StdEnv/2023 gcc openmpi mpi4py/3.1.4 fftw-mpi/3.10 hdf5-mpi/1.14.2 python/3.11

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

2. Submit your job to the scheduler.

!!! tip
    Before submitting your job, it is important to test that your submission script will start without errors. You can do a quick test in an [interactive job](running-jobs.md#interactive-jobs).

```bash
sbatch submit-dedalus.sh