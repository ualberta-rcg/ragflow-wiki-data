---
title: "MPI4py/fr"
tags:
  []

keywords:
  []
---

[MPI for Python](https://mpi4py.readthedocs.io/en/stable/) fournit une interface Python pour la norme de communication MPI (Message Passing Interface), permettant aux applications Python d'exploiter plusieurs processeurs sur des postes de travail, des grappes et des supercalculateurs.

__FORCETOC__

= Versions disponibles =

Dans notre environnement, `mpi4py` est un module et non un paquet précompilé ([wheel](available-python-wheels-fr.md)) comme la plupart des paquets Python. Pour trouver les versions disponibles, utilisez

```bash
module spider mpi4py
```

Pour plus d’information sur une version particulière, utilisez

```bash
module spider mpi4py/X.Y.Z
```

où `X.Y.Z` est le numéro de la version, par exemple `4.0.0`. 

= Exemple avec Hello World =
1.Démarrez une courte [tâche interactive](running_jobs-fr#tâches_interactives.md).

```bash

```
<your account> --ntasks5}}

2. Chargez le module.

```bash
module load mpi4py/4.0.0 python/3.12
```

3. Faites un test de type <i>Hello World</i>.

```bash
srun python -m mpi4py.bench helloworld
```

```
Hello, World! I am process 0 of 5 on node1.
Hello, World! I am process 1 of 5 on node1.
Hello, World! I am process 2 of 5 on node3.
Hello, World! I am process 3 of 5 on node3.
Hello, World! I am process 4 of 5 on node3.
```

Dans cet exemple, deux nœuds (node1 et node3) ont été alloués et les tâches ont été distribuées sur les ressources disponibles.

= mpi4py comme dépendance d'un autre paquet =
Quand un autre paquet dépend de `mpi4py`,

1. Désactivez tout environnement virtuel Python.

```bash
test $VIRTUAL_ENV && deactivate
```

<b>Remarque</b> : Si un environnement virtuel est actif, il est important de le désactiver avant de charger le module. Une fois le module chargé, activez à nouveau votre environnement virtuel.

2. Chargez le module.

```bash
module load mpi4py/4.0.0 python/3.12
```

3.  Vérifiez que le module est visible par `pip`

```bash

```
 grep mpi4py
|result=
mpi4py            4.0.0
}}
et que le module Python que vous avez chargé lui a accès.

```bash
python -c 'import mpi4py'
```

Si aucune erreur ne survient, tout va bien.

4. [Créer un environnement virtuel](python-fr#créer_et_utiliser_un_environnement_virtuel.md) et installez les paquets.

= Exécuter des tâches =
Les tâches MPI peuvent être distribuées sur plusieurs cœurs ou plusieurs nœuds. Pour plus d’information, voir
* [MPI job](running-jobs-fr#mpi_job.md)
* [Advanced MPI scheduling](advanced-mpi-scheduling.md)

## Sur CPU 
1. Préparez le code Python ci-dessous pour distribuer un tableau NumPy.

**`"mpi4py-np-bc.py"`**
```python
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = np.arange(100, dtype='i')
else:
    data = np.empty(100, dtype='i')

comm.Bcast(data, root=0)

for i in range(100):
    assert data[i] == i
```

Cet exemple est basé sur [le tutopriel mpi4py](https://mpi4py.readthedocs.io/en/stable/tutorial.html#running-python-scripts-with-mpi).

2. Préparez le script de tâche
<tabs>
<tab name="Distributed">

**`submit-mpi4py-distributed.sh`**
```bash
#!/bin/bash

#SBATCH --account=def-someprof    # adjust this to match the accounting group you are using to submit jobs
#SBATCH --time=08:00:00           # adjust this to match the walltime of your job
#SBATCH --ntasks=4                # adjust this to match the number of tasks/processes to run
#SBATCH --mem-per-cpu=4G          # adjust this according to the memory you need per process

# Run on cores across the system : https://docs.alliancecan.ca/wiki/Advanced_MPI_scheduling#Few_cores,_any_number_of_nodes

# Load modules dependencies.
module load StdEnv/2023 gcc mpi4py/4.0.0 python/3.12

# create the virtual environment on each allocated node: 
srun --ntasks $SLURM_NNODES --tasks-per-node=1 bash << EOF
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate

pip install --no-index --upgrade pip
pip install --no-index numpy==2.1.1
EOF

# activate only on main node
source $SLURM_TMPDIR/env/bin/activate;

# srun exports the current env, which contains $VIRTUAL_ENV and $PATH variables
srun python mpi4py-np-bc.py;
```

</tab>

<tab name="Nœuds entiers">

**`submit-mpi4py-whole-nodes.sh`**
```bash
#!/bin/bash

#SBATCH --account=def-someprof    # adjust this to match the accounting group you are using to submit jobs
#SBATCH --time=01:00:00           # adjust this to match the walltime of your job
#SBATCH --nodes=2                 # adjust this to match the number of whole node
#SBATCH --ntasks-per-node=40      # adjust this to match the number of tasks/processes to run per node
#SBATCH --mem-per-cpu=1G          # adjust this according to the memory you need per process

# Run on N whole nodes : https://docs.alliancecan.ca/wiki/Advanced_MPI_scheduling#Whole_nodes

# Load modules dependencies.
module load StdEnv/2023 gcc openmpi mpi4py/4.0.0 python/3.12

# create the virtual environment on each allocated node: 
srun --ntasks $SLURM_NNODES --tasks-per-node=1 bash << EOF
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate

pip install --no-index --upgrade pip
pip install --no-index numpy==2.1.1
EOF

# activate only on main node
source $SLURM_TMPDIR/env/bin/activate;

# srun exports the current env, which contains $VIRTUAL_ENV and $PATH variables
srun python mpi4py-np-bc.py;
```

</tab>
</tabs>

3. Testez votre script.

Avant de soumettre la tâche, il est important de tester le script pour des erreurs possibles. Faites un test rapide avec une [tâche interactive](running_jobs-fr#tâches_interactives.md).

4. Soumettez votre tâche.

```bash
sbatch submit-mpi4py-distributed.sh
```

## GPU 
1. Sur un nœud de connexion, téléchargez l’exemple tiré des [démos](https://github.com/mpi4py/mpi4py/tree/master/demo).

```bash
wget https://raw.githubusercontent.com/mpi4py/mpi4py/refs/heads/master/demo/cuda-aware-mpi/use_cupy.py
```

2. Préparez votre script de soumission.

**`submit-mpi4py-gpu.sh`**
```bash
#!/bin/bash

#SBATCH --account=def-someprof    # adjust this to match the accounting group you are using to submit jobs
#SBATCH --time=08:00:00           # adjust this to match the walltime of your job
#SBATCH --ntasks=2                # adjust this to match the number of tasks/processes to run
#SBATCH --mem-per-cpu=2G          # adjust this according to the memory you need per process
#SBATCH --gpus=1

# Load modules dependencies.
module load StdEnv/2023 gcc cuda/12 mpi4py/4.0.0 python/3.11

# create the virtual environment on each allocated node:
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate

pip install --no-index --upgrade pip
pip install --no-index cupy numba

srun python use_cupy.py;
```

3. Testez votre script.

Avant de soumettre la tâche, il est important de tester le script pour des erreurs possibles. Faites un test rapide avec une [tâche interactive](running_jobs-fr#tâches_interactives.md).

4. Soumettez votre tâche.

```bash
sbatch submit-mpi4py-gpu.sh
```

= Dépannage =

## Message <i>ModuleNotFoundError: No module named 'mpi4py'</i> 
Ce message peut survenir à l’importation quand `mpi4py` n’est pas accessible.
`
ModuleNotFoundError: No module named 'mpi4py'
`

Solutions suggérées :
* avec `module spider mpi4py/X.Y.Z`, vérifiez quelles versions de Python sont compatibles avec le module mpi4py que vous avez chargé. Quand une version compatible est chargée, vérifiez si `python -c 'import mpi4py'` fonctionne;
* chargez le module avant d'activer votre environnement virtuel (voir [<i>mpi4py comme dépendance d'un autre paquet</i>](mpi4py-fr#mpi4py_comme_dépendance_d'un_autre_paquet.md) ci=dessus).

Voir aussi [Message ModuleNotFoundError: No module named 'X'](python-fr#message_modulenotfounderror:_no_module_named_'x'.md).