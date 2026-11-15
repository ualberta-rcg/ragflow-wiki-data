---
title: "GPAW/en"
slug: "gpaw"
lang: "en"

source_wiki_title: "GPAW/en"
source_hash: "c59ccaca1a23e4cd25827e4956f43322"
last_synced: "2026-11-15T02:27:25.182546+00:00"
last_processed: "2026-11-15T03:29:19.237347+00:00"

tags:
  - software
  - computationalchemistry

keywords:
  - "GPAW_SETUP_PATH"
  - "density-functional theory (DFT)"
  - "python-3.10.2"
  - "parallel calculation"
  - "gpaw -P 4"
  - "gpaw-22.8.0"
  - "GPAW"
  - "OpenMP"
  - "MPI"
  - "venv_gpaw"
  - "Python wheels"
  - "jobscript"
  - "PAW-datasets"
  - "virtual environment"

questions:
  - "What are the step‑by‑step instructions for creating and activating a virtual environment to install GPAW?"
  - "How is the GPAW data (setups and pseudopotentials) downloaded, installed, and linked via the GPAW_SETUP_PATH variable?"
  - "What information does the `gpaw test` command display about installed components, and how can a parallel test be run with multiple cores?"
  - "How should `OMP_NUM_THREADS` be set to match the `cpus-per-task` value in the SLURM jobscript?"
  - "Which modules must be loaded to guarantee that the same MPI library used to build the GPAW wheels is employed during the job?"
  - "How many total CPU cores does the example jobscript use, and how are they divided between MPI ranks and OpenMP threads?"
  - "What does the `-P 4` option specify when running `gpaw -P 4 test`?"
  - "Which Python version and GPAW version are being used in this environment?"
  - "Where are the Python interpreter and the GPAW package installed according to the output?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## General

[GPAW](https://wiki.fysik.dtu.dk/gpaw/) is a density-functional theory (DFT) [Python](python.md) code based on the projector-augmented wave (PAW) method and the atomic simulation environment (ASE).

## Creating a GPAW virtual environment

We provide precompiled [Python wheels](../programming/available_python_wheels.md) for GPAW that can be installed into a [virtual Python environment](python.md#creating-and-using-a-virtual-environment).

1.  Check which versions of GPAW are available:

    ```console
    [name@server ~] avail_wheels gpaw
    name    version    python    arch
    ------  ---------  --------  ------
    gpaw    22.8.0     cp39      avx2
    gpaw    22.8.0     cp38      avx2
    gpaw    22.8.0     cp310     avx2
    ```

2.  Load a Python module (e.g., `python/3.10`):

    ```console
    (ENV) [name@server ~] module load python/3.10
    ```

3.  Create a new virtual environment:

    ```console
    [name@server ~] virtualenv --no-download venv_gpaw
    created virtual environment CPython3.10.2.final.0-64 in 514ms
    [...]
    ```

4.  Activate the virtual environment (venv):

    ```console
    [name@server ~] source venv_gpaw/bin/activate
    ```

5.  Install GPAW into the virtual environment:

    ```console
    (venv_gpaw) [name@server ~] pip install --no-index gpaw
    [...]
    Successfully installed ... gpaw-22.8.0+computecanada ...
    ```

6.  Download the data and install it into the `SCRATCH` filesystem:

    ```console
    (venv_gpaw) [name@server ~] gpaw install-data $SCRATCH
    Available setups and pseudopotentials
      [*] https://wiki.fysik.dtu.dk/gpaw-files/gpaw-setups-0.9.20000.tar.gz
    [...]
    Setups installed into /scratch/name/gpaw-setups-0.9.20000.
    Register this setup path in /home/name/.gpaw/rc.py? [y/n] n
    As you wish.
    [...]
    Installation complete.
    ```

7.  Now set `GPAW_SETUP_PATH` to point to the data directory:

    ```console
    (venv_gpaw) [name@server ~] export GPAW_SETUP_PATH=$SCRATCH/gpaw-setups-0.9.20000
    ```

8.  We can run the tests, which are very fast:

    ```console
    (venv_gpaw) [name@server ~] gpaw test
     ------------------------------------------------------------------------------------------------------------
    | python-3.10.2     /home/name/venv_gpaw/bin/python                                                         |
    | gpaw-22.8.0       /home/name/venv_gpaw/lib/python3.10/site-packages/gpaw/                                 |
    | ase-3.22.1        /home/name/venv_gpaw/lib/python3.10/site-packages/ase/                                  |
    | numpy-1.23.0      /home/name/venv_gpaw/lib/python3.10/site-packages/numpy/                                |
    | scipy-1.9.3       /home/name/venv_gpaw/lib/python3.10/site-packages/scipy/                                |
    | libxc-5.2.3       yes                                                                                     |
    | _gpaw             /home/name/venv_gpaw/lib/python3.10/site-packages/_gpaw.cpython-310-x86_64-linux-gnu.so |
    | MPI enabled       yes                                                                                     |
    | OpenMP enabled    yes                                                                                     |
    | scalapack         yes                                                                                     |
    | Elpa              no                                                                                      |
    | FFTW              yes                                                                                     |
    | libvdwxc          no                                                                                      |
    | PAW-datasets (1)  /scratch/name/gpaw-setups-0.9.20000                                                     |
     -----------------------------------------------------------------------------------------------------------
    Doing a test calculation (cores: 1): ... Done
    Test parallel calculation with "gpaw -P 4 test".
    ```

    ```console
    (venv_gpaw) [name@server ~] gpaw -P 4 test
     ------------------------------------------------------------------------------------------------------------
    | python-3.10.2     /home/name/venv_gpaw/bin/python                                                         |
    | gpaw-22.8.0       /home/name/venv_gpaw/lib/python3.10/site-packages/gpaw/                                 |
    | ase-3.22.1        /home/name/venv_gpaw/lib/python3.10/site-packages/ase/                                  |
    | numpy-1.23.0      /home/name/venv_gpaw/lib/python3.10/site-packages/numpy/                                |
    | scipy-1.9.3       /home/name/venv_gpaw/lib/python3.10/site-packages/scipy/                                |
    | libxc-5.2.3       yes                                                                                     |
    | _gpaw             /home/name/venv_gpaw/lib/python3.10/site-packages/_gpaw.cpython-310-x86_64-linux-gnu.so |
    | MPI enabled       yes                                                                                     |
    | OpenMP enabled    yes                                                                                     |
    | scalapack         yes                                                                                     |
    | Elpa              no                                                                                      |
    | FFTW              yes                                                                                     |
    | libvdwxc          no                                                                                      |
    | PAW-datasets (1)  /scratch/name/gpaw-setups-0.9.20000                                                     |
     -----------------------------------------------------------------------------------------------------------
    Doing a test calculation (cores: 4): ... Done
    ```

    Results of the last test can be found in the file `test.txt` that will be created in the current directory.

## Example Jobscript

A jobscript may look something like this for hybrid (OpenMP and MPI) parallelization. This assumes that the virtual environment is in your `$HOME` directory and the PAW-datasets in `$SCRATCH` as shown above.

```bash title="job_gpaw.sh"
#!/bin/bash
#SBATCH --ntasks=8
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=4000M
#SBATCH --time=0-01:00
module load gcc/9.3.0 openmpi/4.0.3
source ~/venv_gpaw/bin/activate

export OMP_NUM_THREADS="${SLURM_CPUS_PER_TASK:-1}"
export GPAW_SETUP_PATH=/scratch/$USER/gpaw-setups-0.9.20000

srun --cpus-per-task=$OMP_NUM_THREADS gpaw python my_gpaw_script.py
```

This would use a single node with 8 MPI-ranks (`ntasks`) and 4 OpenMP threads per MPI rank (`cpus-per-task`), for a total of 32 CPUs. You probably want to adjust those numbers so that the product matches the number of cores on a whole node; see [National systems](../clusters/national_systems.md) or your cluster's quickstart page.

Setting `OMP_NUM_THREADS` as shown above makes sure it is always set to the same value as `cpus-per-task` or 1 in case `cpus-per-task` is not set. Loading the modules `gcc/9.3.0` and `openmpi/4.0.3` ensures that the exact MPI library is used for the job, as was used for building the wheels.