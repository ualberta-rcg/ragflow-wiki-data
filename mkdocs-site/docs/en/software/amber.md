---
title: "AMBER/en"
slug: "amber"
lang: "en"

source_wiki_title: "AMBER/en"
source_hash: "562529c7e3d335ee2190657740369161"
last_synced: "2026-04-10T14:10:18.226633+00:00"
last_processed: "2026-04-10T14:23:14.895363+00:00"

tags:
  - software
  - biomolecularsimulation

keywords:
  - "molecular dynamics simulations"
  - "SBATCH"
  - "sander.quick.cuda.MPI"
  - "GPU-accelerated simulations"
  - "MPI job"
  - "AmberTools"
  - "pmemd"
  - "MD engines"
  - "AMBER performance"
  - "GPUs"
  - "quick_MPI_job.sh"
  - "CUDA"
  - "ambertools/21"
  - "openmpi"
  - "Parallel MMPBSA"
  - "pmemd.cuda.MPI"
  - "AMBER"
  - "Amber-PMEMD"
  - "Amber"
  - "CPUs"
  - "SLURM submission script"
  - "SANDER.QUICK"
  - "ambertools"
  - "AMBER version"
  - "MMPBSA.py"
  - "StdEnv/2020"
  - "PB calculations"
  - "H100 GPU clusters"
  - "GPU modules"
  - "PMEMD"
  - "GPU"
  - "Amber modules"

questions:
  - "What are the main differences between the Amber, AmberTools, and Amber-PMEMD modules provided in the software stack?"
  - "Why is it necessary to use specific newer versions of AMBER modules when running simulations on H100 GPU clusters?"
  - "How do the module loading commands differ when running AMBER on CPUs versus GPUs within the StdEnv/2023 environment?"
  - "What specific modules need to be loaded to run ambertools/21 on CPUs?"
  - "How does the module load command differ when running ambertools/21 on GPUs compared to CPUs?"
  - "Which underlying libraries are mentioned in the notes for the ambertools/21 version?"
  - "What are the key differences between the amber/20.9-20.15 and amber/20.12-20.15 modules regarding library usage and hardware compatibility?"
  - "Which molecular dynamics engines are provided by AmberTools 21, and what environment setup step is required after loading its module?"
  - "What are the known limitations associated with the MMPBSA.py tool in specific versions of the AMBER modules?"
  - "What are the specific CUDA version requirements for running GPU-accelerated Amber simulations on A100 GPUs on the Narval cluster?"
  - "How do the Slurm resource requests, such as the number of nodes and tasks per node, differ when submitting a CPU-only parallel MPI job on Narval compared to clusters like Rorqual or Fir?"
  - "Which specific executable and Slurm configuration should be used to submit a QM/MM distributed multi-GPU job requesting eight GPUs?"
  - "What executable is designated for multi-GPU jobs as opposed to single GPU jobs?"
  - "Which specific versions of the Amber module are known to be missing the MMPBSA.py.MPI executable?"
  - "Which module versions are recommended for performing PB calculations to avoid the limitations of the Amber 18 modules?"
  - "Why does the MMPBSA job scale linearly across multiple MPI processes?"
  - "What specific modules and commands are required in the provided SLURM script to run a parallel MMPBSA job?"
  - "What resource is recommended for determining the optimal computing conditions and viewing benchmarks for AMBER simulations?"
  - "What specific computational resources, such as tasks, GPUs, memory, and time limits, are requested in this SLURM script?"
  - "Which software modules and versions must be loaded to properly configure the environment for this job?"
  - "What is the main executable command being run, and what are the specific input and output files defined in its arguments?"
  - "Why does the MMPBSA job scale linearly across multiple MPI processes?"
  - "What specific modules and commands are required in the provided SLURM script to run a parallel MMPBSA job?"
  - "What resource is recommended for determining the optimal computing conditions and viewing benchmarks for AMBER simulations?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Introduction
[Amber](https://ambermd.org/) is the collective name for a suite of programs that allow users to perform molecular dynamics simulations, particularly on biomolecules. None of the individual programs carry this name, but the various parts work reasonably well together and provide a powerful framework for many common calculations.

## Amber Modules
We provide modules for Amber, AmberTools, and Amber-PMEMD in our [software stack](available-software.md).

*   **[AmberTools](https://ambermd.org/AmberTools.php)** (module `ambertools`) - Tools for preparing/analysing simulations, `QUICK` for GPU-accelerated DFT calculations and `sander` for molecular dynamics. Free and open source.
*   **[Amber](https://ambermd.org/AmberMD.php)** (module `amber`) - Everything included in AmberTools, plus the advanced `pmemd` program for high-performance molecular dynamics simulations. 
*   **Amber-PMEMD** (module `amber-pmemd`, Amber 24+) – High-performance MD engine `pmemd`, optimized for CPU and GPU. 
    Provides the high-performance MD engine `pmemd` (optimized for CPU/GPU) as a **standalone module**. This change was made because starting with Amber 24, `pmemd` no longer requires AmberTools for compilation. 
    !!! note "Note"
        The `amber-pmemd` module does not include AmberTools. To use both, load the `ambertools` module as well.

To see a list of installed versions and which other modules they depend on, you can use the `module spider` [command](using-modules.md#sub-command-spider) or check the [Available software](available-software.md) page.

## Using AMBER on H100 GPU Clusters

!!! warning "Key Update"
    Older AMBER modules are incompatible with NVIDIA H100 GPUs. For GPU-accelerated runs, use the newly installed modules below.

### Module Requirements:

`ambertools/25.0` or `amber-pmemd/24.3`

These modules include H100-specific CUDA kernels (compiled with CUDA 12+ for the Hopper architecture).

!!! important "Important"
    Do not use legacy AMBER modules for GPU jobs — they will fail on H100 nodes.

## Loading Modules
=== "StdEnv/2023"
    | AMBER version | modules for running on CPUs | modules for running on GPUs (CUDA) | Notes |
    |---|---|---|---|
    | `amber-pmemd/24.3` | `StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 amber-pmemd/24.3` | `StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 amber-pmemd/24.3` | H100 compatible |
    | `amber/22.5-23.5` | `StdEnv/2023 gcc/12.3 openmpi/4.1.5 amber/22.5-23.5` | `StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.2 amber/22.5-23.5` | |
    | `ambertools/25.0` | `StdEnv/2023 gcc/12.3 openmpi/4.1.5 ambertools/25.0` | `StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 ambertools/25.0` | H100 compatible, with PLUMED/2.9.0 |
    | `ambertools/23.5` | `StdEnv/2023 gcc/12.3 openmpi/4.1.5 ambertools/23.5` | `StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.2 ambertools/23.5` | |
=== "StdEnv/2020"
    | AMBER version | modules for running on CPUs | modules for running on GPUs (CUDA) | Notes |
    |---|---|---|---|
    | `ambertools/21` | `StdEnv/2020 gcc/9.3.0 openmpi/4.0.3 scipy-stack ambertools/21` | `StdEnv/2020 gcc/9.3.0 cuda/11.4 openmpi/4.0.3 scipy-stack ambertools/21` | GCC, FlexiBLAS & FFTW |
    | `amber/20.12-20.15` | `StdEnv/2020 gcc/9.3.0 openmpi/4.0.3 amber/20.12-20.15` | `StdEnv/2020 gcc/9.3.0 cuda/11.4 openmpi/4.0.3 amber/20.12-20.15` | GCC, FlexiBLAS & FFTW |
    | `amber/20.9-20.15` | `StdEnv/2020 gcc/9.3.0 openmpi/4.0.3 amber/20.9-20.15` | `StdEnv/2020 gcc/9.3.0 cuda/11.0 openmpi/4.0.3 amber/20.9-20.15` | GCC, MKL & FFTW |
    | `amber/18.14-18.17` | `StdEnv/2020 gcc/9.3.0 openmpi/4.0.3 amber/18.14-18.17` | `StdEnv/2020 gcc/8.4.0 cuda/10.2 openmpi/4.0.3` | GCC, MKL |
=== "StdEnv/2016"
    | AMBER version | modules for running on CPUs | modules for running on GPUs (CUDA) | Notes |
    |---|---|---|---|
    | `amber/18` | `StdEnv/2016 gcc/5.4.0 openmpi/2.1.1 scipy-stack/2019a amber/18` | `StdEnv/2016 gcc/5.4.0 openmpi/2.1.1 cuda/9.0.176 scipy-stack/2019a amber/18` | GCC, MKL |
    | `amber/18.10-18.11` | `StdEnv/2016 gcc/5.4.0 openmpi/2.1.1 scipy-stack/2019a amber/18.10-18.11` | `StdEnv/2016 gcc/5.4.0 openmpi/2.1.1 cuda/9.0.176 scipy-stack/2019a amber/18.10-18.11` | GCC, MKL |
    | `amber/18.10-18.11` | `StdEnv/2016 gcc/7.3.0 openmpi/3.1.2 scipy-stack/2019a amber/18.10-18.11` | `StdEnv/2016 gcc/7.3.0 cuda/9.2.148 openmpi/3.1.2 scipy-stack/2019a amber/18.10-18.11` | GCC, MKL |
    | `amber/16` | `StdEnv/2016.4 amber/16` | | Available only on Graham. Some Python functionality is not supported |

## Using Modules
### AmberTools 21
Currently, AmberTools 21 module is available on all clusters. AmberTools provide the following MD engines: `sander`, `sander.LES`, `sander.LES.MPI`, `sander.MPI`, `sander.OMP`, `sander.quick.cuda`, and `sander.quick.cuda.MPI`. After loading the module set AMBER environment variables:

```bash
source $EBROOTAMBERTOOLS/amber.sh
```

### Amber 20
There are two versions of `amber/20` modules: `20.9-20.15` and `20.12-20.15`. The first one uses MKL and `cuda/11.0`, while the second uses FlexiBLAS and `cuda/11.4`. MKL libraries do not perform well on AMD CPU, and FlexiBLAS solves this problem. It detects CPU type and uses libraries optimized for the hardware. `cuda/11.4` is required for running simulations on A100 GPUs installed on Narval. 

CPU-only modules provide all MD programs available in `AmberTools/20` plus `pmemd` (serial) and `pmemd.MPI` (parallel). GPU modules add `pmemd.cuda` (single GPU), and `pmemd.cuda.MPI` (multi-GPU).

### Known Issues
1.  Module `amber/20.12-20.15` does not have `MMPBSA.py.MPI` executable.
2.  `MMPBSA.py` from `amber/18-10-18.11` and `amber/18.14-18.17` modules cannot perform PB calculations. Use more recent `amber/20` modules for this type of calculations.

## Job Submission Examples
### Single GPU Job
For GPU-accelerated simulations on Narval, use `amber/20.12-20.15`. Modules compiled with `CUDA` version < 11.4 do not work on A100 GPUs. Below is an example submission script for a single-GPU job.

```bash
# pmemd_cuda_job.sh
#!/bin/bash
#SBATCH --ntasks=1 
#SBATCH --gpus-per-node=1 
#SBATCH --mem-per-cpu=2000 
#SBATCH --time=10:00:00

module purge
module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 amber-pmemd/24.3

pmemd.cuda -O -i input.in -p topol.parm7 -c coord.rst7 -o output.mdout -r restart.rst7
```

### CPU-only Parallel MPI Job

=== "Narval"
    ```sh
    # pmemd_MPI_job_narval.sh
    #!/bin/bash
    #SBATCH --nodes=4
    #SBATCH --ntasks-per-node=64
    #SBATCH --mem-per-cpu=2000
    #SBATCH --time=1:00:00

    module purge
    module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 amber-pmemd/24.3

    srun pmemd.MPI -O -i input.in -p topol.parm7 -c coord.rst7 -o output.mdout -r restart.rst7
    ```
=== "Rorqual"
    ```sh
    # pmemd_MPI_job_rorqual.sh
    #!/bin/bash
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=192
    #SBATCH --mem-per-cpu=2000
    #SBATCH --time=1:00:00

    module purge
    module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 amber-pmemd/24.3

    srun pmemd.MPI -O -i input.in -p topol.parm7 -c coord.rst7 -o output.mdout -r restart.rst7
    ```
=== "Fir"
    ```sh
    # pmemd_MPI_job_fir.sh
    #!/bin/bash
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=192
    #SBATCH --mem-per-cpu=2000
    #SBATCH --time=1:00:00

    module purge
    module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 amber-pmemd/24.3

    srun pmemd.MPI -O -i input.in -p topol.parm7 -c coord.rst7 -o output.mdout -r restart.rst7
    ```
=== "Nibi"
    ```sh
    # pmemd_MPI_job_nibi.sh
    #!/bin/bash
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=192
    #SBATCH --mem-per-cpu=2000
    #SBATCH --time=1:00:00

    module purge
    module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 amber-pmemd/24.3

    srun pmemd.MPI -O -i input.in -p topol.parm7 -c coord.rst7 -o output.mdout -r restart.rst7
    ```
=== "Trillium"
    ```sh
    # pmemd_MPI_job_trillium.sh
    #!/bin/bash
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=192
    #SBATCH --mem-per-cpu=2000
    #SBATCH --time=1:00:00

    module purge
    module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 amber-pmemd/24.3

    srun pmemd.MPI -O -i input.in -p topol.parm7 -c coord.rst7 -o output.mdout -r restart.rst7
    ```

### QM/MM Distributed Multi-GPU Job
The example below requests eight GPUs.

```bash
# quick_MPI_job.sh
#!/bin/bash
#SBATCH --ntasks=8
#SBATCH --gpus-per-task=1 
#SBATCH --mem-per-cpu=4000 
#SBATCH --time=02:00:00

module purge
module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 ambertools/25.0

srun sander.quick.cuda.MPI -O -i input.in -p topol.parm7 -c coord.rst7 -o output.mdout -r restart.rst7
```

### Parallel MMPBSA Job
The example below uses 32 MPI processes. MMPBSA scales linearly because each trajectory frame is processed independently. 

```bash
# mmpbsa_job.sh
#!/bin/bash
#SBATCH --ntasks=32 
#SBATCH --mem-per-cpu=4000 
#SBATCH --time=1:00:00

module purge
module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 ambertools/25.0

srun MMPBSA.py.MPI -O -i mmpbsa.in -o mmpbsa.dat -sp solvated_complex.parm7 -cp complex.parm7 -rp receptor.parm7 -lp ligand.parm7 -y trajectory.nc
```

You can modify scripts to fit your simulation requirements for computing resources. See [Running jobs](running-jobs.md) for more details.

## Performance and Benchmarking

A team at [ACENET](https://www.ace-net.ca/) has created a [Molecular Dynamics Performance Guide](https://mdbench.ace-net.ca/mdbench/) for Alliance clusters.
It can help you determine optimal conditions for AMBER, GROMACS, NAMD, and OpenMM jobs. This section focuses on AMBER performance.

View benchmarks of simulations with [PMEMD](http://mdbench.ace-net.ca/mdbench/bform/?software_contains=PMEMD&software_id=&module_contains=&module_version=&site_contains=&gpu_model=&cpu_model=&arch=&dataset=6n4o) 

View benchmarks of QM/MM simulations with [SANDER.QUICK](http://mdbench.ace-net.ca/mdbench/bform/?software_contains=&software_id=&module_contains=&module_version=&site_contains=&gpu_model=&cpu_model=&arch=&dataset=4cg1).