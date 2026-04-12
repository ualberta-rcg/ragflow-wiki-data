---
title: "MPI4py/fr"
slug: "mpi4py"
lang: "fr"

source_wiki_title: "MPI4py/fr"
source_hash: "d2619bd7dfb900828444055ce3a80d20"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:54:03.488996+00:00"

tags:
  []

keywords:
  - "mpi4py"
  - "Dépannage"
  - "module spider"
  - "exécution de tâches"
  - "walltime"
  - "script de soumission"
  - "GPU"
  - "SBATCH"
  - "sbatch"
  - "environnement virtuel"
  - "SLURM"
  - "tâche interactive"
  - "ModuleNotFoundError"
  - "tasks/processes"
  - "memory per cpu"
  - "bash script"
  - "Python"
  - "MPI"

questions:
  - "Comment peut-on rechercher et charger les versions disponibles du module mpi4py dans l'environnement de calcul ?"
  - "Quelle est la procédure à suivre pour configurer un environnement virtuel Python lorsqu'un autre paquet dépend de mpi4py ?"
  - "Comment préparer et soumettre un script de tâche pour distribuer l'exécution d'un code Python utilisant mpi4py sur plusieurs processeurs ?"
  - "Comment configure-t-on l'environnement virtuel Python sur les nœuds alloués pour une tâche mpi4py ?"
  - "Quelle procédure est recommandée pour tester son script avant de le soumettre avec la commande sbatch ?"
  - "Que signifie le message d'erreur \"ModuleNotFoundError: No module named 'mpi4py'\" et dans quel contexte apparaît-il ?"
  - "What workload management system is this bash script designed for, and what is its primary purpose?"
  - "How does the script allocate computational resources in terms of the number of tasks and memory per process?"
  - "Which directive must be modified to ensure the job is billed to the correct accounting group?"
  - "Comment peut-on effectuer un test rapide du script pour détecter d'éventuelles erreurs ?"
  - "Quelle commande doit-on utiliser pour soumettre la tâche ?"
  - "Quelle est la cause du message d'erreur \"ModuleNotFoundError: No module named 'mpi4py'\" ?"
  - "Comment vérifier la compatibilité entre les versions de Python et le module mpi4py que l'on souhaite utiliser ?"
  - "Quelle est la bonne chronologie pour charger le module mpi4py lors de l'utilisation d'un environnement virtuel ?"
  - "Quelle commande permet de tester si le module mpi4py a été correctement chargé et peut être importé dans Python ?"
  - "Comment vérifier la compatibilité entre les versions de Python et le module mpi4py que l'on souhaite utiliser ?"
  - "Quelle est la bonne chronologie pour charger le module mpi4py lors de l'utilisation d'un environnement virtuel ?"
  - "Quelle commande permet de tester si le module mpi4py a été correctement chargé et peut être importé dans Python ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[MPI for Python](https://mpi4py.readthedocs.io/en/stable/) fournit une interface Python pour la norme de communication MPI (Message Passing Interface), permettant aux applications Python d'exploiter plusieurs processeurs sur des postes de travail, des grappes et des supercalculateurs.

## Versions disponibles

Dans notre environnement, `mpi4py` est un module et non un paquet précompilé ([wheel](available-python-wheels.md)) comme la plupart des paquets Python. Pour trouver les versions disponibles, utilisez

```bash
module spider mpi4py
```

Pour plus d’information sur une version particulière, utilisez

```bash
module spider mpi4py/X.Y.Z
```

où `X.Y.Z` est le numéro de la version, par exemple `4.0.0`.

## Exemple avec Hello World

1.  Démarrez une courte [tâche interactive](running-jobs.md#taches-interactives).

    ```bash
    salloc --account=<your account> --ntasks=5
    ```

2.  Chargez le module.

    ```bash
    module load mpi4py/4.0.0 python/3.12
    ```

3.  Faites un test de type *Hello World*.

    ```bash
    srun python -m mpi4py.bench helloworld
    ```

    Output:
    ```text
    Hello, World! I am process 0 of 5 on node1.
    Hello, World! I am process 1 of 5 on node1.
    Hello, World! I am process 2 of 5 on node3.
    Hello, World! I am process 3 of 5 on node3.
    Hello, World! I am process 4 of 5 on node3.
    ```

    Dans cet exemple, deux nœuds (node1 et node3) ont été alloués et les tâches ont été distribuées sur les ressources disponibles.

## mpi4py comme dépendance d'un autre paquet

Quand un autre paquet dépend de `mpi4py`,

1.  Désactivez tout environnement virtuel Python.

    ```bash
    test $VIRTUAL_ENV && deactivate
    ```

    !!! note
        Si un environnement virtuel est actif, il est important de le désactiver avant de charger le module. Une fois le module chargé, activez à nouveau votre environnement virtuel.

2.  Chargez le module.

    ```bash
    module load mpi4py/4.0.0 python/3.12
    ```

3.  Vérifiez que le module est visible par `pip`

    ```bash
    pip list | grep mpi4py
    ```

    Output:
    ```text
    mpi4py            4.0.0
    ```

    et que le module Python que vous avez chargé lui a accès.

    ```bash
    python -c 'import mpi4py'
    ```

    Si aucune erreur ne survient, tout va bien.

4.  [Créer un environnement virtuel](python.md#creer-et-utiliser-un-environnement-virtuel) et installez les paquets.

## Exécuter des tâches

Les tâches MPI peuvent être distribuées sur plusieurs cœurs ou plusieurs nœuds. Pour plus d’information, voir
*   [MPI job](running-jobs.md#mpi-job)
*   [Advanced MPI scheduling](advanced-mpi-scheduling.md)

### Sur CPU

1.  Préparez le code Python ci-dessous pour distribuer un tableau NumPy.

    ```python
    # mpi4py-np-bc.py
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

    Cet exemple est basé sur [le tutoriel mpi4py](https://mpi4py.readthedocs.io/en/stable/tutorial.html#running-python-scripts-with-mpi).

2.  Préparez le script de tâche

    **Script distribué**

    ```bash
    # submit-mpi4py-distributed.sh
    #!/bin/bash

    #SBATCH --account=def-someprof    # ajustez ceci pour qu'il corresponde au groupe de comptabilité que vous utilisez pour soumettre des tâches
    #SBATCH --time=08:00:00           # ajustez ceci pour qu'il corresponde au temps d'exécution (walltime) de votre tâche
    #SBATCH --ntasks=4                # ajustez ceci pour qu'il corresponde au nombre de tâches/processus à exécuter
    #SBATCH --mem-per-cpu=4G          # ajustez ceci en fonction de la mémoire dont vous avez besoin par processus

    # Exécution sur des cœurs à travers le système : [Exécution sur des cœurs à travers le système](https://docs.alliancecan.ca/wiki/Advanced_MPI_scheduling#Few_cores,_any_number_of_nodes)

    # Chargez les dépendances des modules.
    module load StdEnv/2023 gcc mpi4py/4.0.0 python/3.12

    # créez l'environnement virtuel sur chaque nœud alloué :
    srun --ntasks $SLURM_NNODES --tasks-per-node=1 bash << EOF
    virtualenv --no-download $SLURM_TMPDIR/env
    source $SLURM_TMPDIR/env/bin/activate

    pip install --no-index --upgrade pip
    pip install --no-index numpy==2.1.1
    EOF

    # activez seulement sur le nœud principal
    source $SLURM_TMPDIR/env/bin/activate;

    # srun exporte l'environnement actuel, qui contient les variables $VIRTUAL_ENV et $PATH
    srun python mpi4py-np-bc.py;
    ```

    **Nœuds entiers**

    ```bash
    # submit-mpi4py-whole-nodes.sh
    #!/bin/bash

    #SBATCH --account=def-someprof    # ajustez ceci pour qu'il corresponde au groupe de comptabilité que vous utilisez pour soumettre des tâches
    #SBATCH --time=01:00:00           # ajustez ceci pour qu'il corresponde au temps d'exécution (walltime) de votre tâche
    #SBATCH --nodes=2                 # ajustez ceci pour qu'il corresponde au nombre de nœuds entiers
    #SBATCH --ntasks-per-node=40      # ajustez ceci pour qu'il corresponde au nombre de tâches/processus à exécuter par nœud
    #SBATCH --mem-per-cpu=1G          # ajustez ceci en fonction de la mémoire dont vous avez besoin par processus

    # Exécution sur N nœuds entiers : [Exécution sur N nœuds entiers](https://docs.alliancecan.ca/wiki/Advanced_MPI_scheduling#Whole_nodes)

    # Chargez les dépendances des modules.
    module load StdEnv/2023 gcc openmpi mpi4py/4.0.0 python/3.12

    # créez l'environnement virtuel sur chaque nœud alloué :
    srun --ntasks $SLURM_NNODES --tasks-per-node=1 bash << EOF
    virtualenv --no-download $SLURM_TMPDIR/env
    source $SLURM_TMPDIR/env/bin/activate

    pip install --no-index --upgrade pip
    pip install --no-index numpy==2.1.1
    EOF

    # activez seulement sur le nœud principal
    source $SLURM_TMPDIR/env/bin/activate;

    # srun exporte l'environnement actuel, qui contient les variables $VIRTUAL_ENV et $PATH
    srun python mpi4py-np-bc.py;
    ```

3.  Testez votre script.

    Avant de soumettre la tâche, il est important de tester le script pour des erreurs possibles. Faites un test rapide avec une [tâche interactive](running-jobs.md#taches-interactives).

4.  Soumettez votre tâche.

    ```bash
    sbatch submit-mpi4py-distributed.sh
    ```

### GPU

1.  Sur un nœud de connexion, téléchargez l’exemple tiré des [démos](https://github.com/mpi4py/mpi4py/tree/master/demo).

    ```bash
    wget https://raw.githubusercontent.com/mpi4py/mpi4py/refs/heads/master/demo/cuda-aware-mpi/use_cupy.py
    ```

2.  Préparez votre script de soumission.

    ```bash
    # submit-mpi4py-gpu.sh
    #!/bin/bash

    #SBATCH --account=def-someprof    # ajustez ceci pour qu'il corresponde au groupe de comptabilité que vous utilisez pour soumettre des tâches
    #SBATCH --time=08:00:00           # ajustez ceci pour qu'il corresponde au temps d'exécution (walltime) de votre tâche
    #SBATCH --ntasks=2                # ajustez ceci pour qu'il corresponde au nombre de tâches/processus à exécuter
    #SBATCH --mem-per-cpu=2G          # ajustez ceci en fonction de la mémoire dont vous avez besoin par processus
    #SBATCH --gpus=1

    # Chargez les dépendances des modules.
    module load StdEnv/2023 gcc cuda/12 mpi4py/4.0.0 python/3.11

    # créez l'environnement virtuel sur chaque nœud alloué :
    virtualenv --no-download $SLURM_TMPDIR/env
    source $SLURM_TMPDIR/env/bin/activate

    pip install --no-index --upgrade pip
    pip install --no-index cupy numba

    srun python use_cupy.py;
    ```

3.  Testez votre script.

    Avant de soumettre la tâche, il est important de tester le script pour des erreurs possibles. Faites un test rapide avec une [tâche interactive](running-jobs.md#taches-interactives).

4.  Soumettez votre tâche.

    ```bash
    sbatch submit-mpi4py-gpu.sh
    ```

## Dépannage

### Message *ModuleNotFoundError: No module named 'mpi4py'*

Ce message peut survenir à l’importation quand `mpi4py` n’est pas accessible.

```text
ModuleNotFoundError: No module named 'mpi4py'
```

Solutions suggérées :
*   avec `module spider mpi4py/X.Y.Z`, vérifiez quelles versions de Python sont compatibles avec le module mpi4py que vous avez chargé. Quand une version compatible est chargée, vérifiez si `python -c 'import mpi4py'` fonctionne;
*   chargez le module avant d'activer votre environnement virtuel (voir [mpi4py comme dépendance d'un autre paquet](mpi4py.md#mpi4py-comme-dependance-dun-autre-paquet) ci-dessus).

Voir aussi [Message ModuleNotFoundError: No module named 'X'](python.md#message-modulenotfounderror-no-module-named-x).