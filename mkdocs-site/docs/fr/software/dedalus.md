---
title: "Dedalus/fr"
slug: "dedalus"
lang: "fr"

source_wiki_title: "Dedalus/fr"
source_hash: "6414004be54999e3fff4063b114a9612"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T06:08:00.898017+00:00"

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

[Dedalus](https://dedalus-project.org/) est un environnement de développement flexible pour résoudre des équations aux dérivées partielles à l'aide de méthodes spectrales modernes.

## Versions disponibles
Sur nos grappes, les versions de Dedalus sont des *wheels* Python. Pour connaître les versions disponibles, exécutez ``avail_wheels``.

```console
$ avail_wheels dedalus
name     version    python    arch
-------  ---------  --------  ---------
dedalus  3.0.2      cp311     x86-64-v3
dedalus  3.0.2      cp310     x86-64-v3
```

## Installation dans un environnement virtuel Python
1. Chargez les modules requis pour exécuter Dedalus.
```bash
$ module load StdEnv/2023 gcc openmpi mpi4py/3.1.4 fftw-mpi/3.3.10 hdf5-mpi/1.14.2 python/3.11
```

2. Créez et activez un environnement virtuel Python.
```bash
$ virtualenv --no-download ~/dedalus_env
$ source ~/dedalus_env/bin/activate
```

3. Installez une version de Dedalus et ses dépendances Python.
```bash
(dedalus_env) [name@server ~] pip install --no-index --upgrade pip
(dedalus_env) [name@server ~] pip install --no-index dedalus==X.Y.Z
```
où ``X.Y.Z`` est la version choisie (par exemple 3.0.2).
Si aucun numéro n'est indiqué, la plus récente version sera installée.

4. Validez.
```bash
(dedalus_env) [name@server ~] python -c 'import dedalus'
```

5. Gelez l'environnement et les dépendances requises.
```bash
(dedalus_env) [name@server ~] pip freeze --local > ~/dedalus-3.0.2-requirements.txt
```

6. Supprimez l'environnement virtuel local.
```bash
(dedalus_env) [name@server ~] deactivate && rm -r ~/dedalus_env
```

## Exécution
Dedalus peut être exécuté en mode distribué sur plusieurs nœuds ou cœurs. Pour plus d'information, consultez:
* [Tâche MPI](running-jobs.md#tâche-mpi)
* [Contrôle de l'ordonnancement avec MPI](advanced-mpi-scheduling.md)

1. Préparez le script.

=== "Mode distribué"

    ```bash title="submit-dedalus-distributed.sh"
    #!/bin/bash

    #SBATCH --account=def-someprof    # ajustez ceci pour qu'il corresponde au groupe comptable que vous utilisez pour soumettre des tâches
    #SBATCH --time=08:00:00           # ajustez ceci pour qu'il corresponde au temps d'exécution de votre tâche
    #SBATCH --ntasks=4                # ajustez ceci pour qu'il corresponde au nombre de tâches/processus à exécuter
    #SBATCH --mem-per-cpu=4G          # ajustez ceci en fonction de la mémoire dont vous avez besoin par processus

    # Exécuter sur des cœurs à travers le système : https://docs.alliancecan.ca/wiki/Advanced_MPI_scheduling#Few_cores,_any_number_of_nodes

    # Chargez les dépendances des modules.
    module load StdEnv/2023 gcc openmpi mpi4py/3.1.4 fftw-mpi/3.3.10 hdf5-mpi/1.14.2 python/3.11

    # créez l'environnement virtuel sur chaque nœud alloué :
    srun --ntasks $SLURM_NNODES --tasks-per-node=1 bash << EOF
    virtualenv --no-download $SLURM_TMPDIR/env
    source $SLURM_TMPDIR/env/bin/activate

    pip install --no-index --upgrade pip
    pip install --no-index -r dedalus-3.0.2-requirements.txt
    EOF

    # activez uniquement sur le nœud principal
    source $SLURM_TMPDIR/env/bin/activate;

    export OMP_NUM_THREADS=1

    # srun exporte l'environnement actuel, qui contient les variables $VIRTUAL_ENV et $PATH
    srun python $SCRATCH/myscript.py;
    ```

=== "Nœud entier"

    ```bash title="submit-dedalus-whole-nodes.sh"
    #!/bin/bash

    #SBATCH --account=def-someprof    # ajustez ceci pour qu'il corresponde au groupe comptable que vous utilisez pour soumettre des tâches
    #SBATCH --time=08:00:00           # ajustez ceci pour qu'il corresponde au temps d'exécution de votre tâche
    #SBATCH --nodes=2                 # ajustez ceci pour qu'il corresponde au nombre de nœuds entiers
    #SBATCH --ntasks-per-node=4       # ajustez ceci pour qu'il corresponde au nombre de tâches/processus à exécuter par nœud
    #SBATCH --mem-per-cpu=4G          # ajustez ceci en fonction de la mémoire dont vous avez besoin par processus

    # Exécuter sur N nœuds entiers : https://docs.alliancecan.ca/wiki/Advanced_MPI_scheduling#Whole_nodes

    # Chargez les dépendances des modules.
    module load StdEnv/2023 gcc openmpi mpi4py/3.1.4 fftw-mpi/3.3.10 hdf5-mpi/1.14.2 python/3.11

    # créez l'environnement virtuel sur chaque nœud alloué :
    srun --ntasks $SLURM_NNODES --tasks-per-node=1 bash << EOF
    virtualenv --no-download $SLURM_TMPDIR/env
    source $SLURM_TMPDIR/env/bin/activate

    pip install --no-index --upgrade pip
    pip install --no-index -r dedalus-3.0.2-requirements.txt
    EOF

    # activez uniquement sur le nœud principal
    source $SLURM_TMPDIR/env/bin/activate;

    export OMP_NUM_THREADS=1

    # srun exporte l'environnement actuel, qui contient les variables $VIRTUAL_ENV et $PATH
    srun python $SCRATCH/myscript.py;
    ```

2. Soumettez la tâche à l'ordonnanceur.

!!! tip "Vérification préalable"
    Avant de soumettre la tâche, il est important de tester le script pour des erreurs possibles. Faites un test rapide avec une [tâche interactive](running-jobs.md#tâches-interactives).

```bash
$ sbatch submit-dedalus.sh