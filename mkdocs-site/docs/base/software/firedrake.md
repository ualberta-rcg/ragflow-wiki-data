---
title: "Firedrake"
slug: "firedrake"
lang: "base"

source_wiki_title: "Firedrake"
source_hash: "afe2da5a1b1031244ab87452623fb34b"
last_synced: "2026-08-26T10:16:11.334907+00:00"
last_processed: "2026-08-26T11:08:11.617887+00:00"

tags:
  - software

keywords:
  - "module load"
  - "Firedrake"
  - "Firedrake optional dependencies"
  - "module load python/3.13"
  - "PyTorch"
  - "Python virtualenv"
  - "#SBATCH --mem-per-cpu=4000M"
  - "module load gcc/12.3"
  - "virtualenv"
  - "#SBATCH --time=0-00:15:00"
  - "SLEPc"
  - "#SBATCH --ntasks=2"
  - "finite element method"
  - "PETSc"
  - "netgen"

questions:
  - "What is Firedrake and which numerical method does it employ for solving partial differential equations?"
  - "Which modules and Python packages need to be loaded and installed before creating or activating the Firedrake virtual environment for version 2026.4.1?"
  - "How can a user submit a Firedrake multigrid job on a SLURM system, and which Python versions have been tested with the provided job script?"
  - "How do you activate the Firedrake virtual environment and execute the `geometric_multigrid.py` MPI job?"
  - "Which Python versions have been confirmed to work with the provided example script?"
  - "What optional dependencies does Firedrake support, and what are the specific notes on their availability or compatibility?"
  - "What SLURM resource limits (time, tasks, memory) are specified in the script?"
  - "Which software modules are loaded, and what versions are requested for each?"
  - "How is the `OMP_NUM_THREADS` environment variable determined and what fallback value is used?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Firedrake](https://www.firedrakeproject.org/) is an automated system for the solution of partial differential equations using the finite element method (FEM).

!!! note
    Please note that every release of Firedrake requires a specific version of PETSc, several other modules, and Python wheels.

## Installation

!!! note
    Please note that all modules must be loaded before creating and/or activating the Python virtual environment.

!!! tab "Firedrake 2026.4.1"

    ```bash
    module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 python/3.14 mpi4py/4.1.0
    module load vtk/9.4.2 symengine/0.14.0 libspatialindex/2.1.0 petsc/3.25.1
    virtualenv venv-firedrake
    source venv-firedrake/bin/activate
    pip install -U pip
    pip install --no-index msgpack "tables==3.11.0" "pytools==2026.1.1" immutabledict
    pip install --no-index "firedrake[check]==2026.4.1"
    ```
    The above has been tested with `python/3.14`, `python/3.13`, `python/3.12` and `python/3.11`.

!!! tab "Firedrake 2025.4.2"

    ```bash
    module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 python/3.13 mpi4py/4.0.3 symengine/0.14.0 libspatialindex/1.9.3 petsc/3.23.4
    virtualenv venv-firedrake
    source venv-firedrake/bin/activate
    pip install -U pip
    pip install --no-index "pytools==2025.2.2" immutabledict
    pip install --no-index "firedrake[check]==2025.4.2"
    ```
    The above has been tested with both `python/3.13` as well as `python/3.12`.

## Running Jobs

!!! tab "Firedrake 2026.4.1"

    ```bash linenums="1" title="job_firedrake_multigrid.sh"
    #!/bin/bash
    #SBATCH --time=0-00:15:00  # d-hh:mm:ss
    #SBATCH --ntasks=2
    #SBATCH --mem-per-cpu=4000M
    export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}

    # Load modules
    module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 python/3.14 mpi4py/4.1.0
    module load vtk/9.4.2 symengine/0.14.0 libspatialindex/2.1.0 petsc/3.25.1

    # activate virtualenv
    source venv-firedrake/bin/activate

    # run MPI job
    # example from: https://firedrakeproject.org/demos/geometric_multigrid.py
    srun python geometric_multigrid.py
    ```
    The above has been tested with `python/3.14`, `python/3.13`, `python/3.12` and `python/3.11`.

!!! tab "Firedrake 2025.4.2"

    ```bash linenums="1" title="job_firedrake_multigrid.sh"
    #!/bin/bash
    #SBATCH --time=0-00:15:00  # d-hh:mm:ss
    #SBATCH --ntasks=2
    #SBATCH --mem-per-cpu=4000M
    export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}

    # Load modules
    module load StdEnv/2023 gcc/12.3 openmpi/4.1.5
    module load python/3.13 mpi4py/4.0.3
    module load symengine/0.14.0 libspatialindex/1.9.3 petsc/3.23.4

    # activate virtualenv
    source venv-firedrake/bin/activate

    # run MPI job
    # example from: https://firedrakeproject.org/demos/geometric_multigrid.py
    srun python geometric_multigrid.py
    ```
    The above has been tested with both `python/3.13` as well as `python/3.12`.

## Optional Dependencies
Firedrake has a number of [optional dependencies](https://www.firedrakeproject.org/install.html#optional-dependencies) that can be installed into the [Python virtual environment](python.md#creating-and-using-a-virtual-environment):

*   **SLEPc** and slepc4py are part of the `petsc` module and always available.
*   **netgen**: We provide [precompiled wheels](python.md#available-wheels) for `ngsPETSc` and `netgen_mesher`.
*   **PyTorch**: We provide [precompiled wheels](python.md#available-wheels) for `torch`.
*   **Jax**: We provide [precompiled wheels](python.md#available-wheels) for `jax`.
*   **VTK**: The module `vtk/9.4.2` is compatible with `python/3.14`, `python/3.13`, `python/3.12` and `python/3.11`.