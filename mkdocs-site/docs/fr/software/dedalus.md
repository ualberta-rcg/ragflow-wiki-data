---
title: "Dedalus/fr"
slug: "dedalus"
lang: "fr"

source_wiki_title: "Dedalus/fr"
source_hash: "6414004be54999e3fff4063b114a9612"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:51:48.239027+00:00"

tags:
  []

keywords:
  - "méthodes spectrales"
  - "Dedalus"
  - "mode distribué"
  - "bash"
  - "walltime"
  - "SBATCH"
  - "environnement virtuel"
  - "tâche interactive"
  - "équations aux dérivées partielles"
  - "tasks/processes"
  - "accounting group"
  - "sbatch"
  - "environnement virtuel Python"
  - "MPI"

questions:
  - "Qu'est-ce que l'environnement Dedalus et quelle est sa principale utilité ?"
  - "Quelles sont les étapes à suivre pour installer une version spécifique de Dedalus dans un environnement virtuel Python ?"
  - "Comment doit-on configurer un script SLURM pour exécuter Dedalus en mode distribué sur plusieurs nœuds ou cœurs ?"
  - "Comment l'environnement virtuel et les dépendances logicielles sont-ils configurés sur les nœuds alloués par Slurm ?"
  - "Quelle est la commande utilisée pour lancer l'exécution du script Python principal avec les variables d'environnement appropriées ?"
  - "Quelle étape de vérification est fortement recommandée avant de soumettre la tâche à l'ordonnanceur avec sbatch ?"
  - "What is the primary purpose of the #SBATCH directives included in this bash script?"
  - "How many total tasks or processes will be executed across the requested nodes based on this configuration?"
  - "What is the maximum walltime allowed for the job submitted with this script?"
  - "Comment l'environnement virtuel et les dépendances logicielles sont-ils configurés sur les nœuds alloués par Slurm ?"
  - "Quelle est la commande utilisée pour lancer l'exécution du script Python principal avec les variables d'environnement appropriées ?"
  - "Quelle étape de vérification est fortement recommandée avant de soumettre la tâche à l'ordonnanceur avec sbatch ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Dedalus](https://dedalus-project.org/) est un environnement de développement polyvalent pour résoudre des équations aux dérivées partielles à l'aide de méthodes spectrales modernes.

## Versions disponibles

Sur nos grappes, les versions de Dedalus sont des *wheels* Python. Pour connaître les versions disponibles, exécutez `avail_wheels`.

```bash
avail_wheels dedalus
name     version    python    arch
-------  ---------  --------  ---------
dedalus  3.0.2      cp311     x86-64-v3
dedalus  3.0.2      cp310     x86-64-v3
```

## Installation dans un environnement virtuel Python

1. Chargez les modules requis pour exécuter Dedalus.

```bash
module load StdEnv/2023 gcc openmpi mpi4py/3.1.4 fftw-mpi/3.3.10 hdf5-mpi/1.14.2 python/3.11
```

2. Créez et activez un environnement virtuel Python.

```bash
virtualenv --no-download ~/dedalus_env
source ~/dedalus_env/bin/activate
```

3. Installez une version de Dedalus et ses dépendances Python.

```bash
(dedalus_env) $ pip install --no-index --upgrade pip
(dedalus_env) $ pip install --no-index dedalus==X.Y.Z
```
où `X.Y.Z` est la version choisie (par exemple 3.0.2). Si aucun numéro n'est indiqué, la version la plus récente sera installée.

4. Validez l'installation.

```bash
(dedalus_env) $ python -c 'import dedalus'
```

5. Geler l'environnement et les dépendances requises.

```bash
(dedalus_env) $ pip freeze --local > ~/dedalus-3.0.2-requirements.txt
```

6. Supprimez l'environnement virtuel local.

```bash
(dedalus_env) $ deactivate && rm -r ~/dedalus_env
```

## Exécution

Dedalus peut être exécuté en mode distribué sur plusieurs nœuds ou cœurs. Pour plus d'information, consultez :
* [Tâche MPI](running-jobs.md#tache-mpi)
* [Contrôle de l'ordonnancement avec MPI](advanced-mpi-scheduling.md)

1. Préparez le script.

=== "Mode distribué"

    ```bash title="submit-dedalus-distributed.sh"
    #!/bin/bash

    #SBATCH --account=def-someprof    # ajustez ceci à votre groupe de comptabilité
    #SBATCH --time=08:00:00           # ajustez ceci à la durée d'exécution souhaitée
    #SBATCH --ntasks=4                # ajustez ceci au nombre de tâches/processus à exécuter
    #SBATCH --mem-per-cpu=4G          # ajustez ceci à la mémoire requise par processus

    # Exécution sur des cœurs répartis dans le système : https://docs.alliancecan.ca/wiki/Advanced_MPI_scheduling#Few_cores,_any_number_of_nodes

    # Charge les modules nécessaires.
    module load StdEnv/2023 gcc openmpi mpi4py/3.1.4 fftw-mpi/3.3.10 hdf5-mpi/1.14.2 python/3.11

    # Crée l'environnement virtuel sur chaque nœud alloué :
    srun --ntasks $SLURM_NNODES --tasks-per-node=1 bash << EOF
    virtualenv --no-download $SLURM_TMPDIR/env
    source $SLURM_TMPDIR/env/bin/activate

    pip install --no-index --upgrade pip
    pip install --no-index -r dedalus-3.0.2-requirements.txt
    EOF

    # Active uniquement sur le nœud principal
    source $SLURM_TMPDIR/env/bin/activate;

    export OMP_NUM_THREADS=1

    # srun exporte l'environnement actuel, qui contient les variables $VIRTUAL_ENV et $PATH
    srun python $SCRATCH/myscript.py;
    ```

=== "Nœud entier"

    ```bash title="submit-dedalus-whole-nodes.sh"
    #!/bin/bash

    #SBATCH --account=def-someprof    # ajustez ceci à votre groupe de comptabilité
    #SBATCH --time=08:00:00           # ajustez ceci à la durée d'exécution souhaitée
    #SBATCH --nodes=2                 # ajustez ceci au nombre de nœuds entiers
    #SBATCH --ntasks-per-node=4       # ajustez ceci au nombre de tâches/processus à exécuter par nœud
    #SBATCH --mem-per-cpu=4G          # ajustez ceci à la mémoire requise par processus

    # Exécution sur N nœuds entiers : https://docs.alliancecan.ca/wiki/Advanced_MPI_scheduling#Whole_nodes

    # Charge les modules nécessaires.
    module load StdEnv/2023 gcc openmpi mpi4py/3.1.4 fftw-mpi/3.3.10 hdf5-mpi/1.14.2 python/3.11

    # Crée l'environnement virtuel sur chaque nœud alloué :
    srun --ntasks $SLURM_NNODES --tasks-per-node=1 bash << EOF
    virtualenv --no-download $SLURM_TMPDIR/env
    source $SLURM_TMPDIR/env/bin/activate

    pip install --no-index --upgrade pip
    pip install --no-index -r dedalus-3.0.2-requirements.txt
    EOF

    # Active uniquement sur le nœud principal
    source $SLURM_TMPDIR/env/bin/activate;

    export OMP_NUM_THREADS=1

    # srun exporte l'environnement actuel, qui contient les variables $VIRTUAL_ENV et $PATH
    srun python $SCRATCH/myscript.py;
    ```

2. Soumettez la tâche à l'ordonnanceur.

!!! note
    Avant de soumettre la tâche, il est important de tester le script pour détecter d'éventuelles erreurs. Faites un test rapide avec une [tâche interactive](running-jobs.md#taches-interactives).

```bash
sbatch submit-dedalus.sh