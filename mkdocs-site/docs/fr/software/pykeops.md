---
title: "PyKeOps/fr"
tags:
  []

keywords:
  []
---

__FORCETOC__
La bibliothèque [KeOps](https://www.kernel-operations.io/keops/index.html) permet de calculer des réductions de tableaux de grande taille dont les entrées sont des formules mathématiques ou des réseaux de neurones. Elle combine des routines C++ efficaces avec un moteur de différentiation automatique et peut être utilisée avec [Python](python-fr.md) ([NumPy](https://numpy.org/doc/stable/), [PyTorch](pytorch-fr.md)), [MATLAB](matlab-fr.md) et [R](r-fr.md).

= Versions disponibles = 
Les versions disponibles sur nos grappes sont des wheels Python. Voyez la liste en lançant `avail_wheels`.

```bash
avail_wheels pykeops
```

```
name     version    python    arch
-------  ---------  --------  -------
pykeops  2.2.3      py3       generic
```

= Installation dans un environnement virtuel Python =
1. Chargez les dépendances.

```bash
module load StdEnv/2023 python/3.11
```

2. Créez et activez un [environnement virtuel Python](python-fr#créer_et_utiliser_un_environnement_virtuel.md).

```bash
source ~/pykeops_env/bin/activate
```

3. Installez une version  de PyKeOps avec ses dépendances Python.

```bash

```
X.Y.Z
}}
où `X.Y.Z` est le numéro de la version, par exemple `2.2.3`. 
Pour installer la plus récente version, n'entrez pas de numéro.

4. Validez.

```bash
python -c 'import pykeops; pykeops.test_numpy_bindings()'
```

5. Gelez l'environnement et l'ensemble des exigences.

```bash
pip freeze --local > ~/pykeops-2.2.3-requirements.txt
```

6. Supprimez l'environnement virtuel local.

```bash
deactivate && rm -r ~/pykeops_env
```

= Exécution = 
Vous pouvez exécuter PyKeOps sur un CPU ou un GPU. 

1. Préparez votre script d'exécution.
<tabs>
<tab name="CPU">

**`submit-pykeops-cpu.sh`**
```bash
#!/bin/bash

#SBATCH --account=def-someprof    # adjust this to match the accounting group you are using to submit jobs
#SBATCH --time=08:00:00           # adjust this to match the walltime of your job
#SBATCH --cpus-per-task=4         # adjust this to match the number of cores to use
#SBATCH --mem-per-cpu=4G          # adjust this according to the memory you need per cpu

# Load modules dependencies.
module load StdEnv/2023 python/3.11

# create the virtual environment on the compute node: 
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate

pip install --no-index --upgrade pip
pip install --no-index -r pykeops-2.2.3-requirements.txt

# test that everything is OK
python -c 'import pykeops; pykeops.test_numpy_bindings()'
```

</tab>
<tab name="GPU">

**`submit-pykeops-gpu.sh`**
```bash
#!/bin/bash

#SBATCH --account=def-someprof    # adjust this to match the accounting group you are using to submit jobs
#SBATCH --time=08:00:00           # adjust this to match the walltime of your job
#SBATCH --cpus-per-task=4         # adjust this to match the number of cores to use
#SBATCH --mem-per-cpu=4G          # adjust this according to the memory you need per cpu
#SBATCH --gpus=1

# Load modules dependencies. The custom-ctypes is critical here.
module load StdEnv/2023 python/3.11 cuda/12 custom-ctypes

# create the virtual environment on the compute node: 
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate

pip install --no-index --upgrade pip
pip install --no-index -r pykeops-2.2.3-requirements.txt

# test that nvrtc binding are also found
python -c 'import pykeops; pykeops.test_numpy_bindings()'
```

</tab>
</tabs>

2. Pour savoir si votre script contient des erreurs, testez-le avec une  [tâche interactive](running_jobs-fr#tâches_interactives.md).

3. Soumettez la tâche à l'ordonnanceur.

```bash
sbatch submit-keops.sh
```