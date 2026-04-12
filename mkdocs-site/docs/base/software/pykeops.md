---
title: "PyKeOps"
slug: "pykeops"
lang: "base"

source_wiki_title: "PyKeOps"
source_hash: "cc9fdbf7b9d9da76a862d04402c4c094"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:31:05.099194+00:00"

tags:
  []

keywords:
  - "module load"
  - "submission script"
  - "Python virtual environment"
  - "interactive job"
  - "SBATCH"
  - "nvrtc binding"
  - "KeOps"
  - "virtual environment"
  - "pykeops"
  - "pip install"
  - "custom-ctypes"
  - "job submission script"
  - "sbatch"
  - "array reductions"
  - "PyKeOps"

questions:
  - "What is the primary function of the KeOps library and which programming languages or frameworks does it support?"
  - "What are the necessary steps to install, validate, and freeze a specific version of PyKeOps within a Python virtual environment?"
  - "How should a Slurm job submission script be configured to run PyKeOps on compute nodes using either CPUs or GPUs?"
  - "How can you test that the nvrtc bindings for pykeops are correctly found?"
  - "Why is it recommended to test your submission script in an interactive job before submitting it?"
  - "What command is used to submit the job to the scheduler?"
  - "What specific Slurm resources and environment modules must be loaded for this setup?"
  - "Where is the Python virtual environment created and how is it activated during the job?"
  - "Which specific Python packages and requirements files are installed after the virtual environment is set up?"
  - "How can you test that the nvrtc bindings for pykeops are correctly found?"
  - "Why is it recommended to test your submission script in an interactive job before submitting it?"
  - "What command is used to submit the job to the scheduler?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

The [KeOps](https://www.kernel-operations.io/keops/index.html) library lets you compute reductions of large arrays whose entries are given by a mathematical formula or a neural network. It combines efficient C++ routines with an automatic differentiation engine and can be used with [Python](python.md) ([NumPy](https://numpy.org/doc/stable/)), [PyTorch](pytorch.md), MATLAB, and R.

## Available versions
PyKeOps is available on our clusters as prebuilt Python packages (wheels). You can list available versions with `avail_wheels`.

```bash
avail_wheels pykeops
```

```
name     version    python    arch
-------  ---------  --------  -------
pykeops  2.2.3      py3       generic
```

## Installing PyKeOps in a Python virtual environment
1. Load runtime dependencies.

```bash
module load StdEnv/2023 python/3.11
```

2. Create and activate a [Python virtual environment](python.md#creating-and-using-a-virtual-environment).

```bash
virtualenv --no-download ~/pykeops_env
source ~/pykeops_env/bin/activate
```

3. Install a specific version of PyKeOps and its Python dependencies.

```bash
pip install --no-index --upgrade pip
pip install --no-index pykeops==X.Y.Z
```

where `X.Y.Z` is the exact desired version, for instance `2.2.3`. You can omit to specify the version in order to install the latest one available from the wheelhouse.

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

## Running KeOps
You can run PyKeOps on CPU or GPU.

1. Write your job submission script.

=== "CPU"

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

=== "GPU"

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

2. Before submitting your job, it is important to test that your submission script will start without errors.

!!! note
    You can do a quick test in an [interactive job](running_jobs.md#interactive-jobs).

3. Submit your job to the scheduler.

```bash
sbatch submit-keops.sh