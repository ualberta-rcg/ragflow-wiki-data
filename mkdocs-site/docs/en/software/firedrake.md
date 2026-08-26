---
title: "Firedrake/en"
slug: "firedrake"
lang: "en"

source_wiki_title: "Firedrake/en"
source_hash: "7e560943379800bcde808f7258ec195f"
last_synced: "2026-08-26T10:16:11.334907+00:00"
last_processed: "2026-08-26T11:25:06.134791+00:00"

tags:
  - software

keywords:
  - "module load"
  - "Firedrake"
  - "optional dependencies"
  - "PyTorch"
  - "Python virtualenv"
  - "firedrake"
  - "MPI job"
  - "virtualenv"
  - "VTK"
  - "python/3.13"
  - "SLEPc"
  - "geometric_multigrid.py"
  - "finite element method"
  - "PETSc"
  - "netgen"

questions:
  - "What modules and specific Python versions are required to install Firedrake 2026.4.1?"
  - "How must the Python virtual environment be created and activated before installing Firedrake?"
  - "What does the example SLURM job script for running the Firedrake geometric multigrid demo look like, and which Python versions has it been tested with?"
  - "Which optional dependencies does Firedrake provide precompiled wheels for, and what are their corresponding Python module names?"
  - "How are SLEPc and its Python interface slepc4py included in Firedrake's installation?"
  - "Which Python versions are compatible with the provided VTK module version 9.4.2?"
  - "Which software modules are loaded before activating the Firedrake virtual environment?"
  - "How do you activate the Firedrake virtual environment and run the geometric_multigrid demo?"
  - "With which Python versions has the geometric_multigrid example been tested?"

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
    Every release of Firedrake requires a specific version of PETSc, several other modules, and Python wheels.

## Installation

!!! note
    All modules must be loaded before creating and/or activating the Python virtualenv.

### Firedrake 2026.4.1

```bash
module load StdEnv/2023  gcc/12.3  openmpi/4.1.5  python/3.14  mpi4py/4.1.0
module load vtk/9.4.2  symengine/0.14.0  libspatialindex/2.1.0  petsc/3.25.1
virtualenv venv-firedrake
source venv-firedrake/bin/activate
pip install -U pip
pip install --no-index  msgpack  tables==3.11.0  pytools==2026.1.1  immutabledict
pip install --no-index  firedrake[check]==2026.4.1
```
The above has been tested with `python/3.14`, `python/3.13`, `python/3.12` and `python/3.11`.

### Firedrake 2025.4.2

```bash
module load StdEnv/2023  gcc/12.3  openmpi/4.1.5  python/3.13  mpi4py/4.0.3  symengine/0.14.0  libspatialindex/1.9.3  petsc/3.23.4
virtualenv venv-firedrake
source venv-firedrake/bin/activate
pip install -U pip
pip install --no-index  pytools==2025.2.2  immutabledict
pip install --no-index  firedrake[check]==2025.4.2
```
The above has been tested with both `python/3.13` as well as `python/3.12`.

## Running Jobs

### Firedrake 2026.4.1

```bash title="job_firedrake_multigrid.sh"
#!/bin/bash
#SBATCH --time=0-00:15:00  # d-hh:mm:ss
#SBATCH --ntasks=2
#SBATCH --mem-per-cpu=4000M
export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}

# Load modules
module load StdEnv/2023  gcc/12.3  openmpi/4.1.5  python/3.14  mpi4py/4.1.0
module load vtk/9.4.2  symengine/0.14.0  libspatialindex/2.1.0  petsc/3.25.1

# activate virtualenv
source venv-firedrake/bin/activate

# run MPI job
# example from: https://firedrakeproject.org/demos/geometric_multigrid.py
srun  python  geometric_multigrid.py
```
The above has been tested with `python/3.14`, `python/3.13`, `python/3.12` and `python/3.11`.

### Firedrake 2025.4.2

```bash title="job_firedrake_multigrid.sh"
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
srun  python  geometric_multigrid.py
```
The above has been tested with both `python/3.13` as well as `python/3.12`.

## Optional Dependencies
Firedrake has a number of [optional dependencies](https://www.firedrakeproject.org/install.html#optional-dependencies) that can be installed into the [virtualenv](python.md#creating-and-using-a-virtual-environment):

*   **SLEPc** and slepc4py are part of the `petsc` module and always available.
*   **netgen**: We provide [precompiled wheels](python.md#available-wheels) for `ngsPETSc` and `netgen_mesher`.
*   **PyTorch**: We provide [precompiled wheels](python.md#available-wheels) for `torch`.
*   **Jax**: We provide [precompiled wheels](python.md#available-wheels) for `jax`.
*   **VTK**: The module `vtk/9.4.2` is compatible with `python/3.14`, `python/3.13`, `python/3.12` and `python/3.11`.