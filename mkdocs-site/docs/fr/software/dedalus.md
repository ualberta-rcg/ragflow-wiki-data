---
title: "Dedalus/fr"
tags:
  []

keywords:
  []
---

__FORCETOC__

[Dedalus](https://dedalus-project.org/) est un environnement de développement flexible pour résoudre des équations aux dérivées partielles à l'aide de méthodes spectrales modernes.

= Versions disponibles =
Sur nos grappes, les versions de Dedalus sont des <i>wheels</i> Python. Pour connaître les versions disponibles, exécutez `avail_wheels`.

```bash
avail_wheels dedalus
```

```
name     version    python    arch
-------  ---------  --------  ---------
dedalus  3.0.2      cp311     x86-64-v3
dedalus  3.0.2      cp310     x86-64-v3
```

= Installation dans un environnement virtuel Python =
1. Chargez les modules requis pour exécuter Dedalus.

```bash
module load StdEnv/2023 gcc openmpi mpi4py/3.1.4 fftw-mpi/3.3.10 hdf5-mpi/1.14.2 python/3.11
```

2. Créez et activez un environnement virtuel Python.

```bash
source ~/dedalus_env/bin/activate
```

3. Installez une version de Dedalus et ses dépendances Python.

```bash

```
X.Y.Z
}}
où `X.Y.Z` est la version choisie (par exemple 3.0.2). 
Si aucun numéro n'est indiqué, la plus récente version sera installée.

4. Validez.

```bash
python -c 'import dedalus'
```

5. Gelez l'environnement et les dépendances requises.

```bash
pip freeze --local > ~/dedalus-3.0.2-requirements.txt
```

6. Supprimez l'environnement virtuel local.

```bash
deactivate && rm -r ~/dedalus_env
```

= Exécution =
Dedalus peut être exécuté en mode distribué sur plusieurs nœuds ou cœurs.  
Pour plus d'information, voir
* [Tâche MPI](running-jobs-fr#tâche_mpi.md)
* [Contrôle de l'ordonnancement avec MPI](advanced-mpi-scheduling-fr.md)

1. Préparez le script.
<tabs>
<tab name="Mode distribué">

**`submit-dedalus-distributed.sh`**
```bash
#!/bin/bash

#SBATCH --account=def-someprof    # adjust this to match the accounting group you are using to submit jobs
#SBATCH --time=08:00:00           # adjust this to match the walltime of your job
#SBATCH --ntasks=4                # adjust this to match the number of tasks/processes to run
#SBATCH --mem-per-cpu=4G          # adjust this according to the memory you need per process

# Run on cores accross the system : https://docs.alliancecan.ca/wiki/Advanced_MPI_scheduling#Few_cores,_any_number_of_nodes

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

</tab>

<tab name="Nœud entier">

**`submit-dedalus-whole-nodes.sh`**
```bash
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

</tab>
</tabs>

2. Soumettez la tâche à l'ordonnanceur.

Avant de soumettre la tâche, il est important de tester le script pour des erreurs possibles. Faites un test rapide avec une [tâche interactive](running_jobs-fr#tâches_interactives.md).

```bash
sbatch submit-dedalus.sh
```