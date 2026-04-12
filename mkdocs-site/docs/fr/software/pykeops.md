---
title: "PyKeOps/fr"
slug: "pykeops"
lang: "fr"

source_wiki_title: "PyKeOps/fr"
source_hash: "eda7b062c00a0a77ac46a0ee47f92d49"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:31:50.401115+00:00"

tags:
  []

keywords:
  - "SLURM_TMPDIR"
  - "exécution"
  - "erreurs"
  - "ordonnanceur"
  - "virtual environment"
  - "environnement virtuel"
  - "tâche interactive"
  - "pykeops"
  - "ctypes"
  - "sbatch"
  - "Python"
  - "script"
  - "installation"
  - "nvrtc bindings"
  - "PyKeOps"

questions:
  - "À quoi sert la bibliothèque KeOps et avec quels langages de programmation est-elle compatible ?"
  - "Quelles sont les étapes à suivre pour installer PyKeOps dans un environnement virtuel Python ?"
  - "Comment configurer les scripts d'exécution pour lancer PyKeOps sur un CPU ou un GPU ?"
  - "Comment peut-on vérifier si le script contient des erreurs ?"
  - "À quel composant du système la tâche doit-elle être soumise ?"
  - "Quelle commande spécifique faut-il exécuter pour soumettre la tâche ?"
  - "Why is the custom-ctypes module considered critical when loading the initial environment modules?"
  - "How is the Python virtual environment created and configured to install the pykeops dependencies without downloading them from the internet?"
  - "What specific command is executed to verify that the pykeops installation and its nvrtc bindings are functioning correctly?"
  - "Comment peut-on vérifier si le script contient des erreurs ?"
  - "À quel composant du système la tâche doit-elle être soumise ?"
  - "Quelle commande spécifique faut-il exécuter pour soumettre la tâche ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

La bibliothèque [KeOps](https://www.kernel-operations.io/keops/index.html) permet de calculer des réductions de tableaux de grande taille dont les entrées sont des formules mathématiques ou des réseaux de neurones. Elle combine des routines C++ efficaces avec un moteur de différentiation automatique et peut être utilisée avec [Python](python.md) ([NumPy](https://numpy.org/doc/stable/)), [PyTorch](pytorch.md), [MATLAB](matlab.md) et [R](r.md).

## Versions disponibles
Les versions disponibles sur nos grappes sont des wheels Python. Voyez la liste en lançant `avail_wheels`.

```bash
avail_wheels pykeops
```

Le résultat est le suivant :

```text
name     version    python    arch
-------  ---------  --------  -------
pykeops  2.2.3      py3       generic
```

## Installation dans un environnement virtuel Python

1.  Chargez les dépendances.

    ```bash
    module load StdEnv/2023 python/3.11
    ```

2.  Créez et activez un [environnement virtuel Python](python.md#créer-et-utiliser-un-environnement-virtuel).

    ```bash
    virtualenv --no-download ~/pykeops_env
    source ~/pykeops_env/bin/activate
    ```

3.  Installez une version de PyKeOps avec ses dépendances Python.

    ```bash
    # (pykeops_env) [nom@serveur ~]$
    pip install --no-index --upgrade pip
    pip install --no-index pykeops==X.Y.Z
    ```

    où `X.Y.Z` est le numéro de la version, par exemple `2.2.3`.
    Pour installer la plus récente version, n'entrez pas de numéro.

4.  Validez.

    ```bash
    # (pykeops_env) [nom@serveur ~]$
    python -c 'import pykeops; pykeops.test_numpy_bindings()'
    ```

5.  Gelez l'environnement et l'ensemble des exigences.

    ```bash
    # (pykeops_env) [nom@serveur ~]$
    pip freeze --local > ~/pykeops-2.2.3-requirements.txt
    ```

6.  Supprimez l'environnement virtuel local.

    ```bash
    # (pykeops_env) [nom@serveur ~]$
    deactivate && rm -r ~/pykeops_env
    ```

## Exécution
Vous pouvez exécuter PyKeOps sur un CPU ou un GPU.

1.  Préparez votre script d'exécution.

    ```tabs
    === "CPU"
    ```bash title="submit-pykeops-cpu.sh"
    #!/bin/bash

    #SBATCH --account=def-someprof    # ajustez ce paramètre pour qu'il corresponde au groupe comptable que vous utilisez pour soumettre des tâches
    #SBATCH --time=08:00:00           # ajustez ce paramètre pour qu'il corresponde au temps d'exécution de votre tâche
    #SBATCH --cpus-per-task=4         # ajustez ce paramètre pour qu'il corresponde au nombre de cœurs à utiliser
    #SBATCH --mem-per-cpu=4G          # ajustez ce paramètre en fonction de la mémoire dont vous avez besoin par cœur

    # Chargement des dépendances des modules.
    module load StdEnv/2023 python/3.11

    # Créez l'environnement virtuel sur le nœud de calcul :
    virtualenv --no-download $SLURM_TMPDIR/env
    source $SLURM_TMPDIR/env/bin/activate

    pip install --no-index --upgrade pip
    pip install --no-index -r pykeops-2.2.3-requirements.txt

    # Vérifiez que tout est en ordre
    python -c 'import pykeops; pykeops.test_numpy_bindings()'
    ```

    === "GPU"
    ```bash title="submit-pykeops-gpu.sh"
    #!/bin/bash

    #SBATCH --account=def-someprof    # ajustez ce paramètre pour qu'il corresponde au groupe comptable que vous utilisez pour soumettre des tâches
    #SBATCH --time=08:00:00           # ajustez ce paramètre pour qu'il corresponde au temps d'exécution de votre tâche
    #SBATCH --cpus-per-task=4         # ajustez ce paramètre pour qu'il corresponde au nombre de cœurs à utiliser
    #SBATCH --mem-per-cpu=4G          # ajustez ce paramètre en fonction de la mémoire dont vous avez besoin par cœur
    #SBATCH --gpus=1

    # Chargement des dépendances des modules. Le module custom-ctypes est essentiel ici.
    module load StdEnv/2023 python/3.11 cuda/12 custom-ctypes

    # Créez l'environnement virtuel sur le nœud de calcul :
    virtualenv --no-download $SLURM_TMPDIR/env
    source $SLURM_TMPDIR/env/bin/activate

    pip install --no-index --upgrade pip
    pip install --no-index -r pykeops-2.2.3-requirements.txt

    # Vérifiez que les liaisons nvrtc sont également trouvées
    python -c 'import pykeops; pykeops.test_numpy_bindings()'
    ```
    ```

2.  Pour savoir si votre script contient des erreurs, testez-le avec une [tâche interactive](../running-jobs/running_jobs.md#tâches-interactives).

3.  Soumettez la tâche à l'ordonnanceur.

    ```bash
    sbatch submit-keops.sh