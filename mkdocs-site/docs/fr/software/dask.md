---
title: "Dask/fr"
slug: "dask"
lang: "fr"

source_wiki_title: "Dask/fr"
source_hash: "27ee2a4a000ba928f01d8ee56c99b307"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:45:04.025178+00:00"

tags:
  []

keywords:
  - "virtualenv"
  - "calcul distribué"
  - "SBATCH"
  - "environnement virtuel"
  - "SLURM"
  - "Dask"
  - "soumettre une tâche"
  - "Python"
  - "script"
  - "srun"
  - "Dask scheduler"

questions:
  - "Qu'est-ce que la bibliothèque Dask et quelles sont ses principales fonctionnalités pour le calcul en Python ?"
  - "Quelle est la méthode recommandée pour installer Dask et ses dépendances à l'aide d'un environnement virtuel ?"
  - "Comment configurer et soumettre une tâche Dask via Slurm, que ce soit sur un nœud simple ou sur plusieurs nœuds ?"
  - "Quel est le rôle du script config_env.sh dans la préparation de l'environnement virtuel pour l'exécution de Dask ?"
  - "Comment le script launch_dask_workers.sh répartit-il les ressources de mémoire et de processeur entre la tâche principale (Rank 0) et les autres tâches SLURM ?"
  - "De quelle manière le script test_dask.py établit-il la connexion avec le planificateur Dask pour effectuer son calcul distribué ?"
  - "What are the specific SLURM resource allocations and job configurations defined at the beginning of the script?"
  - "How does the script prepare the Python virtual environment across the allocated compute nodes?"
  - "What environment variables and commands are used to configure and launch the Dask scheduler?"
  - "Quel est le rôle du script config_env.sh dans la préparation de l'environnement virtuel pour l'exécution de Dask ?"
  - "Comment le script launch_dask_workers.sh répartit-il les ressources de mémoire et de processeur entre la tâche principale (Rank 0) et les autres tâches SLURM ?"
  - "De quelle manière le script test_dask.py établit-il la connexion avec le planificateur Dask pour effectuer son calcul distribué ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Dask](https://docs.dask.org/en/stable/) est une bibliothèque polyvalente pour Python. Elle fournit des tableaux NumPy et des DataFrames Pandas permettant le calcul distribué en Python pur avec accès à la pile PyData.

## Installer le wheel

La meilleure option est d'installer avec [Python wheels](https://pythonwheels.com/) comme suit :

1.  Chargez un [module](../programming/utiliser_des_modules.md#sous-commande-load) Python avec `module load python`.
2.  Créez et démarrez un [environnement virtuel](python.md#créer-et-utiliser-un-environnement-virtuel).
3.  Dans l'environnement virtuel, utilisez `pip install` pour installer `dask` et en option `dask-distributed`.

```bash
pip install --no-index dask distributed
```

## Soumettre une tâche

### Nœud simple

L’exemple suivant démarre une grappe Dask avec un nœud simple de 6 CPU et calcule la moyenne d’une colonne pour l'ensemble des données.

```bash linenums="1" title="dask-example.sh"
#!/bin/bash
#SBATCH --account=<votre compte>
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=6
#SBATCH --mem=8000M
#SBATCH --time=0-00:05
#SBATCH --output=%N-%j.out

module load python gcc arrow
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate

pip install dask distributed pandas --no-index

source $SLURM_TMPDIR/env/bin/activate

export DASK_SCHEDULER_ADDR=$(hostname)

export DASK_SCHEDULER_PORT=$((30000 + $RANDOM % 10000))

dask scheduler --host $DASK_SCHEDULER_ADDR --port $DASK_SCHEDULER_PORT &

dask worker "tcp://$DASK_SCHEDULER_ADDR:$DASK_SCHEDULER_PORT" --no-dashboard --nworkers=6 \
--nthreads=1  --local-directory=$SLURM_TMPDIR &

sleep 10

python dask-example.py
```

Ce script démarre une grappe Dask ayant autant de processus de travail que de cœurs dans la tâche. Chacun des processus crée au moins un fil d’exécution. Pour déterminer le nombre de processus et de fils, consultez [la documentation officielle de Dask](https://distributed.dask.org/en/stable/efficiency.html?highlight=workers%20threads#adjust-between-threads-and-processes). Ici, le DataFrame Pandas est divisé en 6 parts et chaque processus en traitera une avec un CPU.

```python linenums="1" title="dask-example.py"
import pandas as pd
import numpy as np # Ajouté pour np.arange

from dask import dataframe as dd
from dask.distributed import Client

import os

n_workers = int(os.environ['SLURM_CPUS_PER_TASK'])

client = Client(f"tcp://{os.environ['DASK_SCHEDULER_ADDR']}:{os.environ['DASK_SCHEDULER_PORT']}")


index = pd.date_range("2021-09-01", periods=2400, freq="1H")
df = pd.DataFrame({"a": np.arange(2400)}, index=index)
ddf = dd.from_pandas(df, npartitions=n_workers) # sépare le DataFrame Pandas en "n_workers" morceaux

result = ddf.a.mean().compute()

print(f"The mean is {result}")
```

### Plusieurs nœuds

Dans le prochain exemple, nous reprenons l'exemple du nœud simple, mais cette fois avec une grappe Dask de deux nœuds comportant 6 CPU chacun. Nous créons aussi deux processus par nœud comportant trois cœurs chacun.

```bash linenums="1" title="dask-example.sh"
#!/bin/bash
#SBATCH --nodes 2
#SBATCH --tasks-per-node=2
#SBATCH --mem=16000M
#SBATCH --cpus-per-task=3
#SBATCH --time=0-00:30
#SBATCH --output=%N-%j.out
#SBATCH --account=<votre compte>

module add python arrow

export DASK_SCHEDULER_ADDR=$(hostname)
export DASK_SCHEDULER_PORT=34567

srun -N 2 -n 2 config_env.sh # -N et -n doivent correspondre au nombre de nœuds

source $SLURM_TMPDIR/env/bin/activate

dask scheduler --host $DASK_SCHEDULER_ADDR --port $DASK_SCHEDULER_PORT &
sleep 10

srun launch_dask_workers.sh &
dask_cluster_pid=$!
sleep 10

python test_dask.py

kill $dask_cluster_pid # arrête les processus Dask worker après la fin du processus python
```

où le script `config_env.sh` est

```bash linenums="1" title="config_env.sh"
#!/bin/bash

echo "Depuis le nœud ${SLURM_NODEID}: installation de virtualenv..."

module load python gcc arrow
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate

pip install --no-index "dask[distributed,dataframe]"

echo "Installation de virtualenv terminée!"

deactivate
```

et le script `launch_dask_workers.sh` est

```bash linenums="1" title="launch_dask_workers.sh"
#!/bin/bash

source $SLURM_TMPDIR/env/bin/activate

SCHEDULER_CONNECTION_STRING="tcp://$DASK_SCHEDULER_ADDR:$DASK_SCHEDULER_PORT"

if [[ "$SLURM_PROCID" -eq "0" ]]; then
## Sur la tâche SLURM de rang 0, où le processus de planificateur Dask a déjà été lancé, nous lançons un worker plus petit,
## avec 40% de la mémoire du travail et nous soustrayons un cœur de la tâche pour le laisser au planificateur.
        DASK_WORKER_MEM=0.4
        DASK_WORKER_THREADS=$(($SLURM_CPUS_PER_TASK-1))

else
## Sur toutes les autres tâches SLURM, chaque worker obtient la moitié de la mémoire allouée au travail et tous les cœurs alloués à sa tâche.
        DASK_WORKER_MEM=0.5
        DASK_WORKER_THREADS=$SLURM_CPUS_PER_TASK
fi

dask worker "tcp://$DASK_SCHEDULER_ADDR:$DASK_SCHEDULER_PORT" --no-dashboard --nworkers=1 \
--nthreads=$DASK_WORKER_THREADS --memory-limit=$DASK_WORKER_MEM --local-directory=$SLURM_TMPDIR

sleep 5
echo "Dask worker démarré!"
```

Enfin, le script `test_dask.py` est

```python linenums="1" title="test_dask.py"
import pandas as pd
import numpy as np # Ajouté pour np.arange

from dask import dataframe as dd
from dask.distributed import Client

import os

client = Client(f"tcp://{os.environ['DASK_SCHEDULER_ADDR']}:{os.environ['DASK_SCHEDULER_PORT']}")

index = pd.date_range("2021-09-01", periods=2400, freq="1H")
df = pd.DataFrame({"a": np.arange(2400)}, index=index)
ddf = dd.from_pandas(df, npartitions=6)

result = ddf.a.mean().compute()

print(f"The mean is {result}")