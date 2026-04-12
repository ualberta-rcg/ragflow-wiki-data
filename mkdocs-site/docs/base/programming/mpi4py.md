---
title: "MPI4py"
slug: "mpi4py"
lang: "base"

source_wiki_title: "MPI4py"
source_hash: "7433c56dcf1dd6058aab76b5b71cbeb8"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:53:07.029773+00:00"

tags:
  []

keywords:
  - "SBATCH"
  - "sbatch"
  - "mpi4py"
  - "Slurm"
  - "walltime"
  - "interactive job"
  - "virtual environment"
  - "pip install"
  - "memory per process"
  - "MPI scheduling"
  - "GPU"
  - "submit job"
  - "ModuleNotFoundError"
  - "Python"
  - "package dependency"
  - "Virtual environment"
  - "Message Passing Interface"
  - "submit jobs"
  - "troubleshooting"
  - "Job submission"

questions:
  - "How can a user find and load a specific version of the mpi4py module on the cluster?"
  - "What is the correct procedure for handling mpi4py as a dependency when working with Python virtual environments?"
  - "How do you write and submit a distributed MPI job using a Python script and SLURM directives?"
  - "How is a Python virtual environment created and activated across multiple allocated nodes in a Slurm job script?"
  - "What specific modules and packages are required to run a CUDA-aware mpi4py job on a GPU?"
  - "What is the recommended method for testing a job submission script for errors before submitting it to the scheduler?"
  - "How do you configure the maximum walltime for a job using SBATCH directives?"
  - "Which parameters must be adjusted to specify the number of tasks and the memory required per process?"
  - "Where can users find more information about advanced MPI scheduling for running jobs across multiple nodes?"
  - "How are the required Python packages, such as cupy and numba, installed according to the instructions?"
  - "Why is it recommended to test the submission script in an interactive job before full submission?"
  - "What command should be used to submit the final job script to the cluster?"
  - "What specific error message does this troubleshooting guide address?"
  - "How can a user verify which Python versions are compatible with their loaded mpi4py module?"
  - "What is the recommended sequence for loading the mpi4py module when working with a virtual environment?"
  - "What specific error message does this troubleshooting guide address?"
  - "How can a user verify which Python versions are compatible with their loaded mpi4py module?"
  - "What is the recommended sequence for loading the mpi4py module when working with a virtual environment?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[MPI for Python](https://mpi4py.readthedocs.io/en/stable/) provides Python bindings for the Message Passing Interface (MPI) standard, allowing Python applications to exploit multiple processors on workstations, clusters and supercomputers.

# Available versions
`mpi4py` is available as a module, and not from the [wheelhouse](available_python_wheels.md) as typical Python packages are.
You can find available version with
```bash
module spider mpi4py
```

and look for more information on a specific version with
```bash
module spider mpi4py/X.Y.Z
```
where `X.Y.Z` is the exact desired version, for instance `4.0.0`.

# Famous first words: Hello World
1. Run a short [interactive job](../running-jobs/running_jobs.md#interactive-jobs).
```bash
salloc --account=<your account> --ntasks=5
```

2. Load the module.
```bash
module load mpi4py/4.0.0 python/3.12
```

3. Run a Hello World test.
```bash
srun python -m mpi4py.bench helloworld
```
```text
Hello, World! I am process 0 of 5 on node1.
Hello, World! I am process 1 of 5 on node1.
Hello, World! I am process 2 of 5 on node3.
Hello, World! I am process 3 of 5 on node3.
Hello, World! I am process 4 of 5 on node3.
```
In the case above, two nodes (`node1` and `node3`) were allocated, and the jobs were distributed across the available resources.

# mpi4py as a package dependency
Often `mpi4py` is a dependency of another package. In order to fulfil this dependency:

1. Deactivate any Python virtual environment.
```bash
test $VIRTUAL_ENV && deactivate
```

!!! note
    If you had a virtual environment activated, it is important to deactivate it first, then load the module, before reactivating your virtual environment.

2. Load the module.
```bash
module load mpi4py/4.0.0 python/3.12
```

3. Check that it is visible by `pip`
```bash
pip list | grep mpi4py
```
```text
mpi4py            4.0.0
```
and is accessible for your currently loaded python module.
```bash
python -c 'import mpi4py'
```
If no errors are raised, then everything is OK!

4. [Create a virtual environment and install your packages](../software/python.md#creating-and-using-a-virtual-environment).

# Running jobs
You can run mpi jobs distributed across multiple nodes or cores.
For efficient MPI scheduling, please see:
* [MPI job](../running-jobs/running_jobs.md#mpi-job)
* [Advanced MPI scheduling](../running-jobs/advanced_mpi_scheduling.md)

## CPU
1. Write your python code, for instance, broadcasting a numpy array.
```python title="mpi4py-np-bc.py"
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

=== "Distributed"

    ```bash title="submit-mpi4py-distributed.sh"
    #!/bin/bash

    #SBATCH --account=def-someprof    # adjust this to match the accounting group you are using to submit jobs
    #SBATCH --time=08:00:00           # adjust this to match the walltime of your job
    #SBATCH --ntasks=4                # adjust this to match the number of tasks/processes to run
    #SBATCH --mem-per-cpu=4G          # adjust this according to the memory you need per process

    # Run on cores across the system : [https://docs.alliancecan.ca/wiki/Advanced_MPI_scheduling#Few_cores,_any_number_of_nodes](../running-jobs/advanced_mpi_scheduling.md#few-cores-any-number-of-nodes)

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

=== "Whole nodes"

    ```bash title="submit-mpi4py-whole-nodes.sh"
    #!/bin/bash

    #SBATCH --account=def-someprof    # adjust this to match the accounting group you are using to submit jobs
    #SBATCH --time=01:00:00           # adjust this to match the walltime of your job
    #SBATCH --nodes=2                 # adjust this to match the number of whole node
    #SBATCH --ntasks-per-node=40      # adjust this to match the number of tasks/processes to run per node
    #SBATCH --mem-per-cpu=1G          # adjust this according to the memory you need per process

    # Run on N whole nodes : [https://docs.alliancecan.ca/wiki/Advanced_MPI_scheduling#Whole_nodes](../running-jobs/advanced_mpi_scheduling.md#whole-nodes)

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

3. Test your script.

Before submitting your job, it is important to test that your submission script will start without errors. You can do a quick test in an [interactive job](../running-jobs/running_jobs.md#interactive-jobs).

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
```bash title="submit-mpi4py-gpu.sh"
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
You can do a quick test in an [interactive job](../running-jobs/running_jobs.md#interactive-jobs).

4. Submit your job
```bash
sbatch submit-mpi4py-gpu.sh
```

# Troubleshooting

## ModuleNotFoundError: No module named 'mpi4py'
If `mpi4py` is not accessible, you may get the following error when importing it:
`ModuleNotFoundError: No module named 'mpi4py'`

Possible solutions:
* check which Python versions are compatible with your loaded mpi4py module using `module spider mpi4py/X.Y.Z`. Once a compatible Python module is loaded, check that `python -c 'import mpi4py'` works.
* load the module before activating your virtual environment: please see the [mpi4py as a package dependency](mpi4py.md#mpi4py-as-a-package-dependency) section above.

See also [ModuleNotFoundError: No module named 'X'](../software/python.md#modulenotfounderror-no-module-named-x).