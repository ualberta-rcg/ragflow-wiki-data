---
title: "GPAW/en"
slug: "gpaw"
lang: "en"

source_wiki_title: "GPAW/en"
source_hash: "68b3f4cabf3ad09fabcf9d793009328f"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:24:47.590674+00:00"

tags:
  - software
  - computationalchemistry

keywords:
  - "density-functional theory"
  - "Jobscript"
  - "parallel calculation"
  - "gpaw-22.8.0"
  - "venv_gpaw"
  - "virtual environment"
  - "python-3.10.2"
  - "gpaw"
  - "OpenMP"
  - "Python"
  - "Hybrid parallelization"
  - "MPI"
  - "installation"
  - "GPAW"

questions:
  - "What is GPAW and what computational methods does it utilize?"
  - "How do you create a virtual environment and install the precompiled GPAW Python wheels?"
  - "What steps are required to download the necessary GPAW data, configure its path, and test the installation?"
  - "What are the key software dependencies and enabled features shown in the GPAW environment configuration?"
  - "How does the example SLURM jobscript configure hybrid parallelization using MPI and OpenMP?"
  - "How should users adjust the task and CPU parameters in the jobscript to optimally match the core counts of specific HPC cluster nodes?"
  - "What specific command is executed to test the parallel calculation using four cores?"
  - "Which versions of Python and GPAW are displayed in the test results?"
  - "What is the name of the virtual environment directory where the software is installed?"
  - "What are the key software dependencies and enabled features shown in the GPAW environment configuration?"
  - "How does the example SLURM jobscript configure hybrid parallelization using MPI and OpenMP?"
  - "How should users adjust the task and CPU parameters in the jobscript to optimally match the core counts of specific HPC cluster nodes?"

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
We provide precompiled [Python wheels](../programming/available_python_wheels.md) for GPAW that can be installed into a [virtual python environment](python.md#creating-and-using-a-virtual-environment).

1.  Check which versions of gpaw are available:

    ```bash
    avail_wheels gpaw
    ```

    Example output:

    | name | version | python | arch |
    | :--- | :------ | :----- | :--- |
    | gpaw | 22.8.0  | cp39   | avx2 |
    | gpaw | 22.8.0  | cp38   | avx2 |
    | gpaw | 22.8.0  | cp310  | avx2 |

2.  Load a Python module (e.g., python/3.10):

    ```bash
    module load python/3.10
    ```

3.  Create a new virtualenv:

    ```bash
    virtualenv --no-download venv_gpaw
    ```

    Example output:

    ```text
    created virtual environment CPython3.10.2.final.0-64 in 514ms
    [...]
    ```

4.  Activate the virtualenv (venv):

    ```bash
    source venv_gpaw/bin/activate
    ```

5.  Install gpaw into venv:

    ```bash
    pip install --no-index gpaw
    ```

    Example output:

    ```text
    [...]
    Successfully installed ... gpaw-22.8.0+computecanada ...
    ```

6.  Download the data and install it into the SCRATCH filesystem:

    ```bash
    gpaw install-data $SCRATCH
    ```

    Example output:

    ```text
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

    ```bash
    export GPAW_SETUP_PATH=$SCRATCH/gpaw-setups-0.9.20000
    ```

8.  We can run the tests, which are very fast:

    ```bash
    gpaw test
    ```

    Example output:

    | Key           | Value                                                              |
    | :------------ | :----------------------------------------------------------------- |
    | python-3.10.2 | /home/name/venv_gpaw/bin/python                                    |
    | gpaw-22.8.0   | /home/name/venv_gpaw/lib/python3.10/site-packages/gpaw/            |
    | ase-3.22.1    | /home/name/venv_gpaw/lib/python3.10/site-packages/ase/             |
    | numpy-1.23.0  | /home/name/venv_gpaw/lib/python3.10/site-packages/numpy/           |
    | scipy-1.9.3   | /home/name/venv_gpaw/lib/python3.10/site-packages/scipy/           |
    | libxc-5.2.3   | yes                                                                |
    | _gpaw         | /home/name/venv_gpaw/lib/python3.10/site-packages/_gpaw.cpython-310-x86_64-linux-gnu.so |
    | MPI enabled   | yes                                                                |
    | OpenMP enabled| yes                                                                |
    | scalapack     | yes                                                                |
    | Elpa          | no                                                                 |
    | FFTW          | yes                                                                |
    | libvdwxc      | no                                                                 |
    | PAW-datasets (1)| /scratch/name/gpaw-setups-0.9.20000                              |

    ```text
    Doing a test calculation (cores: 1): ... Done
    Test parallel calculation with "gpaw -P 4 test".
    ```

    ```bash
    gpaw -P 4 test
    ```

    Example output:

    | Key           | Value                                                              |
    | :------------ | :----------------------------------------------------------------- |
    | python-3.10.2 | /home/name/venv_gpaw/bin/python                                    |
    | gpaw-22.8.0   | /home/name/venv_gpaw/lib/python3.10/site-packages/gpaw/            |
    | ase-3.22.1    | /home/name/venv_gpaw/lib/python3.10/site-packages/ase/             |
    | numpy-1.23.0  | /home/name/venv_gpaw/lib/python3.10/site-packages/numpy/           |
    | scipy-1.9.3   | /home/name/venv_gpaw/lib/python3.10/site-packages/scipy/           |
    | libxc-5.2.3   | yes                                                                |
    | _gpaw         | /home/name/venv_gpaw/lib/python3.10/site-packages/_gpaw.cpython-310-x86_64-linux-gnu.so |
    | MPI enabled   | yes                                                                |
    | OpenMP enabled| yes                                                                |
    | scalapack     | yes                                                                |
    | Elpa          | no                                                                 |
    | FFTW          | yes                                                                |
    | libvdwxc      | no                                                                 |
    | PAW-datasets (1)| /scratch/name/gpaw-setups-0.9.20000                              |

    ```text
    Doing a test calculation (cores: 4): ... Done
    ```

Results of the last test can be found in the file `test.txt` that will be created in the current directory.

## Example Jobscript
A jobscript may look something like this for hybrid (OpenMP and MPI) parallelization.
This assumes that the virtualenv is in your `$HOME` directory and the PAW-datasets in `$SCRATCH` as shown above.

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

This would use a single node with 8 MPI-ranks (`ntasks`) and 4 OpenMP threads per MPI rank (`cpus-per-task`), for a total of 32 CPUs. You probably want to adjust those numbers so that the product matches the number of cores of a whole node (i.e., 32 at [Graham](../clusters/graham.md), 40 at [Béluga](../clusters/béluga.md) and [Niagara](../clusters/national_systems.md), 48 at [Cedar](../clusters/cedar.md) or 64 at [Narval](../clusters/narval.md)).

Setting `OMP_NUM_THREADS` as shown above makes sure it is always set to the same value as `cpus-per-task` or `1` in case `cpus-per-task` is not set.
Loading the modules `gcc/9.3.0` and `openmpi/4.0.3` ensures that the exact MPI library is used for the job, as was used for building the wheels.