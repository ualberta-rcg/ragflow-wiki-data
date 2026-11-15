---
title: "GPAW"
slug: "gpaw"
lang: "base"

source_wiki_title: "GPAW"
source_hash: "bf3e3b692c22136f1bc5bf451e8190cf"
last_synced: "2026-11-15T02:27:25.182546+00:00"
last_processed: "2026-11-15T03:28:53.040709+00:00"

tags:
  - software
  - computationalchemistry

keywords:
  - "GPAW_SETUP_PATH"
  - "SLURM jobscript"
  - "virtual environment"
  - "OpenMP threads"
  - "test calculation"
  - "parallel calculation gpaw -P 4"
  - "gpaw-setups-0.9.20000"
  - "GPAW"
  - "venv_gpaw"
  - "MPI enabled"
  - "Python wheels"
  - "PAW-datasets"
  - "gpaw install-data"
  - "gpaw"

questions:
  - "How can you list the available GPAW versions before installation?"
  - "What are the sequential commands required to create a virtual environment, install GPAW, and set up its data files?"
  - "How do you configure the GPAW_SETUP_PATH and verify the installation by running the provided tests?"
  - "What software versions and optional libraries are reported in the gpaw environment summary?"
  - "How does the example SLURM jobscript configure hybrid MPI‑OpenMP parallelization, including the relationship between `--ntasks`, `--cpus-per-task`, and `OMP_NUM_THREADS`?"
  - "Which environment variables and module loads are required in the jobscript, and what purpose does each serve (e.g., `GPAW_SETUP_PATH`, `gcc/9.3.0`, `openmpi/4.0.3`)?"
  - "What is the purpose of the test calculation shown in the output?"
  - "How many CPU cores are used for the serial test versus the parallel test?"
  - "Where is the PAW‑datasets directory located according to the path provided?"

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

## Creating a GPAW virtual Environment
We provide precompiled [Python wheels](../programming/available_python_wheels.md) for GPAW that can be installed into a [virtual Python environment](python.md#creating-and-using-a-virtual-environment).

1.  Check which versions of GPAW are available:

    ```bash
    [name@server ~] avail_wheels gpaw
    name    version    python    arch
    ------  ---------  --------  ------
    gpaw    22.8.0     cp39      avx2
    gpaw    22.8.0     cp38      avx2
    gpaw    22.8.0     cp310     avx2
    ```

2.  Load a Python module (e.g., `python/3.10`)

    ```bash
    (ENV) [name@server ~] module load python/3.10
    ```

3.  Create a new virtual environment

    ```bash
    [name@server ~] virtualenv --no-download venv_gpaw
    created virtual environment CPython3.10.2.final.0-64 in 514ms
    [...]
    ```

4.  Activate the virtual environment (`venv`)

    ```bash
    [name@server ~] source venv_gpaw/bin/activate
    ```

5.  Install GPAW into the virtual environment

    ```bash
    (venv_gpaw) [name@server ~] pip install --no-index gpaw
    [...]
    Successfully installed ... gpaw-22.8.0+computecanada ...
    ```

6.  Download the data and install it into the SCRATCH filesystem

    ```bash
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

7.  Now set `GPAW_SETUP_PATH` to point to the data directory

    ```bash
    (venv_gpaw) [name@server ~] export GPAW_SETUP_PATH=$SCRATCH/gpaw-setups-0.9.20000
    ```

8.  We can run the tests, which are very fast:

    ```bash
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

    ```bash
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
Here is an example SLURM jobscript for hybrid (OpenMP and MPI) parallelization. This assumes that the virtual environment is located in your `$HOME` directory and the PAW datasets are in `$SCRATCH`, as demonstrated in the previous steps.

!!! code-file "job_gpaw.sh"
    ```bash
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

This would use a single node with 8 MPI-ranks (`--ntasks`) and 4 OpenMP threads per MPI rank (`--cpus-per-task`), for a total of 32 CPUs. You will likely want to adjust these numbers so that the product matches the number of cores on a full node; refer to [National systems](../clusters/national_systems.md) or your cluster's quickstart page for guidance.

Setting `OMP_NUM_THREADS` as shown above ensures it is always set to the same value as `cpus-per-task` or 1 if `cpus-per-task` is not defined. Loading the modules `gcc/9.3.0` and `openmpi/4.0.3` ensures that the exact MPI library is used for the job, as was used for building the wheels.