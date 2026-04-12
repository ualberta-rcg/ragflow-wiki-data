---
title: "PyKeOps/en"
slug: "pykeops"
lang: "en"

source_wiki_title: "PyKeOps/en"
source_hash: "193cb9115a3bb2ffbecb04fe2f717fdf"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:31:24.728269+00:00"

tags:
  []

keywords:
  - "error"
  - "Python virtual environment"
  - "interactive job"
  - "GPU"
  - "missing content"
  - "KeOps library"
  - "No text provided"
  - "pykeops"
  - "pip install"
  - "job submission"
  - "job submission script"
  - "empty input"
  - "sbatch"
  - "please provide text"
  - "PyKeOps"

questions:
  - "What is the KeOps library and which programming languages or frameworks does it support?"
  - "What are the necessary steps to install and validate a specific version of PyKeOps within a Python virtual environment?"
  - "How do the SLURM job submission scripts differ when configuring PyKeOps to run on a CPU versus a GPU?"
  - "What is the specific purpose or intended meaning of the double closing curly brackets in this context?"
  - "Does this snippet indicate a missing block of code or text that was supposed to precede it?"
  - "In what programming or templating language is this syntax typically utilized?"
  - "How do you install the required dependencies and test the nvrtc bindings for pykeops?"
  - "Why is it recommended to run a quick test in an interactive job before submitting your script?"
  - "What command is used to submit the job to the scheduler?"
  - "What is the specific purpose or intended meaning of the double closing curly brackets in this context?"
  - "Does this snippet indicate a missing block of code or text that was supposed to precede it?"
  - "In what programming or templating language is this syntax typically utilized?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

The [KeOps](https://www.kernel-operations.io/keops/index.html) library lets you compute reductions of large arrays whose entries are given by a mathematical formula or a neural network. It combines efficient C++ routines with an automatic differentiation engine and can be used with [Python](python.md) ([NumPy](https://numpy.org/doc/stable/)), [PyTorch](pytorch.md), [MATLAB](matlab.md) and [R](r.md).

## Available versions
PyKeOps is available on our clusters as prebuilt Python packages (wheels). You can list available versions with `avail_wheels`.

```bash
avail_wheels pykeops
```
```text
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
(pykeops_env) [name@server ~]$ pip install --no-index --upgrade pip
(pykeops_env) [name@server ~]$ pip install --no-index pykeops==X.Y.Z
```
where `X.Y.Z` is the exact desired version, for instance `2.2.3`.
You can omit to specify the version in order to install the latest one available from the wheelhouse.

4. Validate it.
```bash
(pykeops_env) [name@server ~]$ python -c 'import pykeops; pykeops.test_numpy_bindings()'
```

5. Freeze the environment and requirements set.
```bash
(pykeops_env) [name@server ~]$ pip freeze --local > ~/pykeops-2.2.3-requirements.txt
```

6. Remove the local virtual environment.
```bash
(pykeops_env) [name@server ~]$ deactivate && rm -r ~/pykeops_env
```

## Running KeOps
You can run PyKeOps on CPU or GPU.

1. Write your job submission script.
=== "CPU"

    ```bash linenums="1"
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

    ```bash linenums="1"
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
You can do a quick test in an [interactive job](running-jobs.md#interactive-jobs).

3. Submit your job to the scheduler.
```bash
sbatch submit-keops.sh