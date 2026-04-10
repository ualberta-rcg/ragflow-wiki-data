---
title: "Firedrake"
slug: "firedrake"
lang: "base"

source_wiki_title: "Firedrake"
source_hash: "697e91a8ecd885353524420235547905"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T06:21:44.853177+00:00"

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

[Firedrake](https://www.firedrakeproject.org/) is an automated system for the solution of partial differential equations using the finite element method (FEM).

!!! note
    Every release of Firedrake requires a specific version of PETSc and several other modules or Python wheels.

## Installation

!!! note
    All modules must be loaded before creating and/or activating the Python virtualenv.

### Firedrake 2025.4.2

```bash
module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 python/3.13 mpi4py/4.0.3 symengine/0.14.0 libspatialindex/1.9.3 petsc/3.23.4
virtualenv venv-firedrake
source venv-firedrake/bin/activate
pip install -U pip
pip install --no-index pytools==2025.2.2 immutabledict
pip install --no-index firedrake[check]==2025.4.2
```

The above has been tested with both `python/3.13` as well as `python/3.12`.

## Running jobs

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

## Optional dependencies

Firedrake has a number of [optional dependencies](https://www.firedrakeproject.org/install.html#optional-dependencies) that can be installed into the virtualenv:

*   **SLEPc** and slepc4py are part of the petsc module and always available.
*   **netgen**: we provide [precompiled wheels](python.md#available-wheels) for `ngsPETSc` and `netgen_mesher`.
*   **PyTorch**: since we provide [precompiled wheels](python.md#available-wheels) for `torch`.
*   **Jax**: since we provide [precompiled wheels](python.md#available-wheels) for `jax`.
*   **VTK**: currently we don't have a module for VTK that supports recent enough versions of Python for Firedrake (Python 3.12 and newer).
    As a temporary workaround VTK can be installed into the virtualenv with: `pip install --no-index --find-links ~stuekero/wheels/vtk vtk==9.4.2` until we install a new VTK module.