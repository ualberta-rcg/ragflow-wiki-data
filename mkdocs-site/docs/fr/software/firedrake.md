---
title: "Firedrake/fr"
slug: "firedrake"
lang: "fr"

source_wiki_title: "Firedrake/fr"
source_hash: "d3b571198b854483682bc854cb11ce08"
last_synced: "2026-08-26T10:16:11.334907+00:00"
last_processed: "2026-08-26T11:25:26.248328+00:00"

tags:
  - software

keywords:
  - "Firedrake"
  - "activate virtualenv"
  - "SBATCH --ntasks=2"
  - "méthode des éléments finis"
  - "PyTorch"
  - "environnement virtuel"
  - "module load gcc/12.3"
  - "mem-per-cpu=4000M"
  - "python/3.13 mpi4py/4.0.3"
  - "VTK"
  - "dépendances optionnelles"
  - "PETSc"
  - "SLEPc"
  - "modules Python"
  - "netgen"

questions:
  - "Quelles versions de PETSc et quels modules supplémentaires sont nécessaires pour chaque version de Firedrake présentée dans le texte ?"
  - "Comment créer et activer l’environnement virtuel Python avant d’installer Firedrake, selon les étapes indiquées ?"
  - "Quels paramètres et quelles commandes sont utilisés dans le script SLURM fourni pour exécuter un job Firedrake avec la méthode multigrid ?"
  - "Comment exécuter le job MPI avec le script `geometric_multigrid.py` fourni par Firedrake ?"
  - "Quelles sont les dépendances optionnelles de Firedrake et comment les installer dans un environnement virtuel Python ?"
  - "Avec quelles versions de Python le module VTK 9.4.2 est‑il compatible selon le texte ?"
  - "What resources (number of tasks and memory per CPU) are requested by the SLURM directives in this script?"
  - "Which software modules (including their versions) are loaded before the job runs?"
  - "How is the Python virtual environment activated for the Firedrake environment in this job script?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Firedrake](https://www.firedrakeproject.org/) est un système automatisé pour la résolution d'équations aux dérivées partielles par la méthode des éléments finis (MEF).

Veuillez noter que chaque version de Firedrake requiert une version spécifique de PETSc, plusieurs autres modules, ainsi que des wheels Python.

## Installation

Tous les modules doivent être chargés avant la création et/ou l'activation de l'environnement virtuel Python.

=== "Firedrake 2026.4.1"
    ```bash
    module load StdEnv/2023  gcc/12.3  openmpi/4.1.5  python/3.14  mpi4py/4.1.0
    module load vtk/9.4.2  symengine/0.14.0  libspatialindex/2.1.0  petsc/3.25.1
    virtualenv venv-firedrake
    source venv-firedrake/bin/activate
    pip install -U pip
    pip install --no-index  msgpack  tables==3.11.0  pytools==2026.1.1  immutabledict
    pip install --no-index  firedrake[check]==2026.4.1
    ```
    Ceci a été testé avec `python/3.14`, `python/3.13`, `python/3.12` et `python/3.11`.
=== "Firedrake 2025.4.2"
    ```bash
    module load StdEnv/2023  gcc/12.3  openmpi/4.1.5  python/3.13  mpi4py/4.0.3  symengine/0.14.0  libspatialindex/1.9.3  petsc/3.23.4
    virtualenv venv-firedrake
    source venv-firedrake/bin/activate
    pip install -U pip
    pip install --no-index  pytools==2025.2.2  immutabledict
    pip install --no-index  firedrake[check]==2025.4.2
    ```
    Ceci a été testé avec `python/3.13` et `python/3.12`.

## Exécuter des tâches

=== "Firedrake 2026.4.1"
    ```bash title="job_firedrake_multigrid.sh"
    #!/bin/bash
    #SBATCH --time=0-00:15:00  # j-hh:mm:ss
    #SBATCH --ntasks=2
    #SBATCH --mem-per-cpu=4000M
    export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}

    # Charger les modules
    module load StdEnv/2023  gcc/12.3  openmpi/4.1.5  python/3.14  mpi4py/4.1.0
    module load vtk/9.4.2  symengine/0.14.0  libspatialindex/2.1.0  petsc/3.25.1

    # Activer l'environnement virtuel
    source venv-firedrake/bin/activate

    # Exécuter la tâche MPI
    # exemple de: https://firedrakeproject.org/demos/geometric_multigrid.py
    srun  python  geometric_multigrid.py
    ```
    Ceci a été testé avec `python/3.14`, `python/3.13`, `python/3.12` et `python/3.11`.
=== "Firedrake 2025.4.2"
    ```bash title="job_firedrake_multigrid.sh"
    #!/bin/bash
    #SBATCH --time=0-00:15:00  # j-hh:mm:ss
    #SBATCH --ntasks=2
    #SBATCH --mem-per-cpu=4000M
    export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}

    # Charger les modules
    module load StdEnv/2023 gcc/12.3 openmpi/4.1.5
    module load python/3.13 mpi4py/4.0.3
    module load symengine/0.14.0 libspatialindex/1.9.3 petsc/3.23.4

    # Activer l'environnement virtuel
    source venv-firedrake/bin/activate

    # Exécuter la tâche MPI
    # exemple de: https://firedrakeproject.org/demos/geometric_multigrid.py
    srun  python  geometric_multigrid.py
    ```
    Ceci a été testé avec `python/3.13` et `python/3.12`.

## Dépendances optionnelles

Voir [les dépendances optionnelles de Firedrake](https://www.firedrakeproject.org/install.html#optional-dependencies) qui peuvent être installées dans [un environnement virtuel Python](python.md) :

*   **SLEPc** et `slepc4py` sont comprises dans le module `petsc` et sont toujours disponibles.
*   **netgen** : Nous fournissons des [wheels précompilés](python.md) pour `ngsPETSc` et `netgen_mesher`.
*   **PyTorch** : Nous fournissons des [wheels précompilés](python.md) pour `torch`.
*   **Jax** : Nous fournissons des [wheels précompilés](python.md) pour `jax`.
*   **VTK** : Le module `vtk/9.4.2` est compatible avec `python/3.14`, `python/3.13`, `python/3.12` et `python/3.11`.