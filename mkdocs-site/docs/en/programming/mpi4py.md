---
title: "MPI4py/en"
tags:
  []

keywords:
  []
---

[MPI for Python](https://mpi4py.readthedocs.io/en/stable/) provides Python bindings for the Message Passing Interface (MPI) standard, allowing Python applications to exploit multiple processors on workstations, clusters and supercomputers.
__FORCETOC__

= Available versions =
`mpi4py` is available as a module, and not from the [wheelhouse](available-python-wheels.md) as typical Python packages are.
You can find available version with

```bash
module spider mpi4py
```

and look for more information on a specific version with

```bash
module spider mpi4py/X.Y.Z
```

where `X.Y.Z` is the exact desired version, for instance `4.0.0`. 

= Famous first words: Hello World =
1. Run a short [interactive job](running-jobs#interactive_jobs.md).

```bash

```
<your account> --ntasks5}}

2. Load the module.

```bash
module load mpi4py/4.0.0 python/3.12
```

3. Run a Hello World test.

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

In the case above, two nodes (`node1` and `node3`) were allocated, and the jobs were distributed across the available resources.

= mpi4py as a package dependency =
Often `mpi4py` is a dependency of another package. In order to fulfill this dependency :

1. Deactivate any Python virtual environment.

```bash
test $VIRTUAL_ENV && deactivate
```

<b>Note:</b> If you had a virtual environment activated, it is important to deactivate it first, then load the module, before reactivating your virtual environment.

2. Load the module.

```bash
module load mpi4py/4.0.0 python/3.12
```

3. Check that it is visible by `pip`

```bash

```
 grep mpi4py
|result=
mpi4py            4.0.0
}}
and is accessible for your currently loaded python module.

```bash
python -c 'import mpi4py'
```

If no errors are raised, then everything is OK!

4. [Create a virtual environment and install your packages](python#creating_and_using_a_virtual_environment.md).

= Running jobs =
You can run mpi jobs distributed across multiple nodes or cores. 
For efficient MPI scheduling, please see:
* [MPI job](running-jobs#mpi_job.md)
* [Advanced MPI scheduling](advanced-mpi-scheduling.md)

## CPU 
1. Write your python code, for instance, broadcasting a numpy array.

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

The example above is based on the [mpi4py tutorial](https://mpi4py.readthedocs.io/en/stable/tutorial.html#running-python-scripts-with-mpi).

2. Write your submission script.
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

<tab name="Whole nodes">

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

3. Test your script.

Before submitting your job, it is important to test that your submission script will start without errors. You can do a quick test in an [interactive job](running_jobs#interactive_jobs.md).

4. Submit your job to the scheduler.

```bash
sbatch submit-mpi4py-distributed.sh
```

## GPU 
1. From a login node, download the demo example.

```bash
wget https://raw.githubusercontent.com/mpi4py/mpi4py/refs/heads/master/demo/cuda-aware-mpi/use_cupy.py
```

The example above and others, can be found in the [demo folder](https://github.com/mpi4py/mpi4py/tree/master/demo).

2. Write your submission script.

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

3. Test your script.

Before submitting your job, it is important to test that your submission script will start without errors.
You can do a quick test in an [interactive job](running_jobs#interactive_jobs.md).

4. Submit your job

```bash
sbatch submit-mpi4py-gpu.sh
```

= Troubleshooting =

## ModuleNotFoundError: No module named 'mpi4py' 
If `mpi4py` is not accessible, you may get the following error when importing it:
`
ModuleNotFoundError: No module named 'mpi4py'
`

Possible solutions:
* check which Python versions are compatible with your loaded mpi4py module using `module spider mpi4py/X.Y.Z`. Once a compatible Python module is loaded, check that `python -c 'import mpi4py'` works.
* load the module before activating your virtual environment: please see the [mpi4py as a package dependency](mpi4py#mpi4py_as_a_package_dependency.md) section above.

See also [ModuleNotFoundError: No module named 'X'](python#modulenotfounderror:_no_module_named_'x'.md).