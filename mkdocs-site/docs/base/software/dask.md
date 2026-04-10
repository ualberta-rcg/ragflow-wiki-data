---
title: "Dask"
slug: "dask"
lang: "base"

source_wiki_title: "Dask"
source_hash: "2cf752ab25e3ee8108877bc7c06a42e1"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T05:59:02.790203+00:00"

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

[Dask](https://docs.dask.org/en/stable/) is a flexible library for parallel computing in Python. It provides distributed NumPy array and Pandas DataFrame objects, as well as enabling distributed computing in pure Python with access to the PyData stack.

## Installing our wheel

The preferred option is to install it using our provided Python [wheel](https://pythonwheels.com/) as follows:
1. Load a Python [module](utiliser-des-modules.md#sub-command-load), thus `module load python/3.11`.
2. Create and start a [virtual environment](python.md#creating-and-using-a-virtual-environment).
3. Install `dask`, and optionally `dask-distributed` in the virtual environment with `pip install`.

```bash
pip install --no-index dask distributed
```

## Job submission

### Single node
Below is an example of a job that spawns a single-node Dask cluster with 6 cpus and computes the mean of a column of a parallelized dataframe.

```bash
#!/bin/bash
#SBATCH --account=<your account>
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

In the script `dask-example.py`, we launch a Dask cluster with as many worker processes as there are cores in our job. This means each worker will spawn at most one CPU thread. For a complete discussion of how to reason about the number of worker processes and the number of threads per worker, see the [official Dask documentation](https://distributed.dask.org/en/stable/efficiency.html?highlight=workers%20threads#adjust-between-threads-and-processes). In this example, we split a pandas data frame into 6 chunks, so each worker will process a part of the data frame using one CPU:

```python title="dask-example.py"
import pandas as pd

from dask import dataframe as dd
from dask.distributed import Client

import os

n_workers = int(os.environ['SLURM_CPUS_PER_TASK'])

client = Client(f"tcp://{os.environ['DASK_SCHEDULER_ADDR']}:{os.environ['DASK_SCHEDULER_PORT']}")


index = pd.date_range("2021-09-01", periods=2400, freq="1H")
df = pd.DataFrame({"a": np.arange(2400)}, index=index)
ddf = dd.from_pandas(df, npartitions=n_workers) # split the pandas data frame into "n_workers" chunks

result = ddf.a.mean().compute()

print(f"The mean is {result}")
```

### Multiple nodes
In the example that follows, we reproduce the single-node example, but this time with a two-node Dask cluster, with 6 CPUs on each node. This time we also spawn 2 workers per node, each with 3 cores.

```bash title="dask-example.sh"
#!/bin/bash
#SBATCH --nodes 2
#SBATCH --tasks-per-node=2
#SBATCH --mem=16000M
#SBATCH --cpus-per-task=3
#SBATCH --time=0-00:30
#SBATCH --output=%N-%j.out
#SBATCH --account=<your account>

module add python arrow

export DASK_SCHEDULER_ADDR=$(hostname)
export DASK_SCHEDULER_PORT=34567

srun -N 2 -n 2 config_virtualenv.sh # set both -N and -n to the number of nodes

source $SLURM_TMPDIR/env/bin/activate

dask scheduler --host $DASK_SCHEDULER_ADDR --port $DASK_SCHEDULER_PORT &
sleep 10

srun launch_dask_workers.sh &
dask_cluster_pid=$!
sleep 10

python test_dask.py

kill $dask_cluster_pid # shut down Dask workers after the python process exits
```

Where the script `config_virtualenv.sh` is:

```bash title="config_env.sh"
#!/bin/bash

echo "From node ${SLURM_NODEID}: installing virtualenv..."

module load python gcc arrow
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate

pip install --no-index dask[distributed,dataframe]

echo "Done installing virtualenv!"

deactivate
```

And the script `launch_dask_workers.sh` is:

```bash title="launch_dask_workers.sh"
#!/bin/bash

source $SLURM_TMPDIR/env/bin/activate

SCHEDULER_CONNECTION_STRING="tcp://$DASK_SCHEDULER_ADDR:$DASK_SCHEDULER_PORT"

if [[ "$SLURM_PROCID" -eq "0" ]]; then
## On the SLURM task with Rank 0, where the Dask scheduler process has already been launched, we launch a smaller worker,
## with 40% of the job's memory and we subtract one core from the task to leave it for the scheduler.
        DASK_WORKER_MEM=0.4
        DASK_WORKER_THREADS=$(($SLURM_CPUS_PER_TASK-1))

else
## On all other SLURM tasks, each worker gets half of the job's allocated memory and all the cores allocated to its task.
        DASK_WORKER_MEM=0.5
        DASK_WORKER_THREADS=$SLURM_CPUS_PER_TASK
fi

dask worker "tcp://$DASK_SCHEDULER_ADDR:$DASK_SCHEDULER_PORT" --no-dashboard --nworkers=1 \
--nthreads=$DASK_WORKER_THREADS --memory-limit=$DASK_WORKER_MEM --local-directory=$SLURM_TMPDIR

sleep 5
echo "dask worker started!"
```

And, finally, the script `test_dask.py` is:

```python title="test_dask.py"
import pandas as pd
import numpy as np

from dask import dataframe as dd
from dask.distributed import Client

import os

client = Client(f"tcp://{os.environ['DASK_SCHEDULER_ADDR']}:{os.environ['DASK_SCHEDULER_PORT']}")

index = pd.date_range("2021-09-01", periods=2400, freq="1H")
df = pd.DataFrame({"a": np.arange(2400)}, index=index)
ddf = dd.from_pandas(df, npartitions=6)

result = ddf.a.mean().compute()

print(f"The mean is {result}")