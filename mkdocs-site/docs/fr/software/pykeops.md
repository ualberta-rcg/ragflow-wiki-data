---
title: "PyKeOps/fr"
slug: "pykeops"
lang: "fr"

source_wiki_title: "PyKeOps/fr"
source_hash: "eda7b062c00a0a77ac46a0ee47f92d49"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T10:04:06.498645+00:00"

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

La bibliothèque [KeOps](https://www.kernel-operations.io/keops/index.html) permet de calculer des réductions de tableaux de grande taille dont les entrées sont des formules mathématiques ou des réseaux de neurones. Elle combine des routines C++ efficaces avec un moteur de différentiation automatique et peut être utilisée avec [Python](python.md) ([NumPy](https://numpy.org/doc/stable/), [PyTorch](pytorch.md)), [MATLAB](matlab.md) et [R](r.md).

## Versions disponibles
Les versions disponibles sur nos grappes sont des wheels Python. Voyez la liste en lançant `avail_wheels`.

```bash
avail_wheels pykeops
name     version    python    arch
-------  ---------  --------  -------
pykeops  2.2.3      py3       generic
```

## Installation dans un environnement virtuel Python
1. Chargez les dépendances.

```bash
module load StdEnv/2023 python/3.11
```

2. Créez et activez un [environnement virtuel Python](python.md#créer-et-utiliser-un-environnement-virtuel).

```bash
virtualenv --no-download ~/pykeops_env
source ~/pykeops_env/bin/activate
```

3. Installez une version de PyKeOps avec ses dépendances Python.

```bash
pip install --no-index --upgrade pip
pip install --no-index pykeops==X.Y.Z
```

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

## Exécution
Vous pouvez exécuter PyKeOps sur un CPU ou un GPU.

1. Préparez votre script d'exécution.

=== "CPU"

    ```bash tab="submit-pykeops-cpu.sh"
    #!/bin/bash

    #SBATCH --account=def-someprof    # ajustez ceci pour correspondre au groupe comptable que vous utilisez pour soumettre des tâches
    #SBATCH --time=08:00:00           # ajustez ceci pour correspondre au temps d'exécution de votre tâche
    #SBATCH --cpus-per-task=4         # ajustez ceci pour correspondre au nombre de cœurs à utiliser
    #SBATCH --mem-per-cpu=4G          # ajustez ceci en fonction de la mémoire dont vous avez besoin par cœur

    # Chargez les dépendances des modules.
    module load StdEnv/2023 python/3.11

    # créez l'environnement virtuel sur le nœud de calcul :
    virtualenv --no-download $SLURM_TMPDIR/env
    source $SLURM_TMPDIR/env/bin/activate

    pip install --no-index --upgrade pip
    pip install --no-index -r pykeops-2.2.3-requirements.txt

    # testez que tout est correct
    python -c 'import pykeops; pykeops.test_numpy_bindings()'
    ```

=== "GPU"

    ```bash tab="submit-pykeops-gpu.sh"
    #!/bin/bash

    #SBATCH --account=def-someprof    # ajustez ceci pour correspondre au groupe comptable que vous utilisez pour soumettre des tâches
    #SBATCH --time=08:00:00           # ajustez ceci pour correspondre au temps d'exécution de votre tâche
    #SBATCH --cpus-per-task=4         # ajustez ceci pour correspondre au nombre de cœurs à utiliser
    #SBATCH --mem-per-cpu=4G          # ajustez ceci en fonction de la mémoire dont vous avez besoin par cœur
    #SBATCH --gpus=1

    # Chargez les dépendances des modules. custom-ctypes est critique ici.
    module load StdEnv/2023 python/3.11 cuda/12 custom-ctypes

    # créez l'environnement virtuel sur le nœud de calcul :
    virtualenv --no-download $SLURM_TMPDIR/env
    source $SLURM_TMPDIR/env/bin/activate

    pip install --no-index --upgrade pip
    pip install --no-index -r pykeops-2.2.3-requirements.txt

    # testez que les liaisons nvrtc sont également trouvées
    python -c 'import pykeops; pykeops.test_numpy_bindings()'
    ```

2. Pour savoir si votre script contient des erreurs, testez-le avec une [tâche interactive](running-jobs.md#taches-interactives).

3. Soumettez la tâche à l'ordonnanceur.

```bash
sbatch submit-keops.sh