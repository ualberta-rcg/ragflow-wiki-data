---
title: "PyKeOps/en"
tags:
  []

keywords:
  []
---

__FORCETOC__
The [KeOps](https://www.kernel-operations.io/keops/index.html) library lets you compute reductions of large arrays whose entries are given by a mathematical formula or a neural network. It combines efficient C++ routines with an automatic differentiation engine and can be used with [Python](python.md) ([NumPy](https://numpy.org/doc/stable/), [PyTorch](pytorch.md)), [MATLAB](matlab.md) and [R](r.md).

= Available versions =
PyKeOps is available on our clusters as prebuilt Python packages (wheels). You can list available versions with `avail_wheels`.

```bash
avail_wheels pykeops
```

```
name     version    python    arch
-------  ---------  --------  -------
pykeops  2.2.3      py3       generic
```

= Installing PyKeOps in a Python virtual environment =
1. Load runtime dependencies.

```bash
module load StdEnv/2023 python/3.11
```

2. Create and activate a [Python virtual environment](python#creating_and_using_a_virtual_environment.md).

```bash
source ~/pykeops_env/bin/activate
```

3. Install a specific version of PyKeOps and its Python dependencies.

```bash

```
X.Y.Z
}}
where `X.Y.Z` is the exact desired version, for instance `2.2.3`. 
You can omit to specify the version in order to install the latest one available from the wheelhouse.

4. Validate it.

```bash
python -c 'import pykeops; pykeops.test_numpy_bindings()'
```

5. Freeze the environment and requirements set.

```bash
pip freeze --local > ~/pykeops-2.2.3-requirements.txt
```

6. Remove the local virtual environment.

```bash
deactivate && rm -r ~/pykeops_env
```

= Running KeOps =
You can run PyKeOps on CPU or GPU. 

1. Write your job submission script.
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

2. Before submitting your job, it is important to test that your submission script will start without errors.
You can do a quick test in an [interactive job](running_jobs#interactive_jobs.md).

3. Submit your job to the scheduler.

```bash
sbatch submit-keops.sh
```