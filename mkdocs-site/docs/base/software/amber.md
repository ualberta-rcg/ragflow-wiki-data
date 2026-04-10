---
title: "AMBER"
slug: "amber"
lang: "base"

source_wiki_title: "AMBER"
source_hash: "94acdb5336ee5a03d369a7aaa9f6df3c"
last_synced: "2026-04-10T14:10:18.226633+00:00"
last_processed: "2026-04-10T14:22:39.905042+00:00"

tags:
  - software
  - biomolecularsimulation

keywords:
  - "A100 GPUs"
  - "molecular dynamics simulations"
  - "SBATCH"
  - "Benchmarking"
  - "amber"
  - "GPU-accelerated simulations"
  - "MPI job"
  - "AmberTools"
  - "pmemd"
  - "ambertools/23.5"
  - "MD engines"
  - "AmberTools/20"
  - "PLUMED/2.9.0"
  - "CUDA"
  - "AMBER"
  - "Amber-PMEMD"
  - "QM/MM distributed multi-GPU job"
  - "Amber"
  - "CPU-only modules"
  - "SANDER.QUICK"
  - "AMBER version"
  - "amber-pmemd"
  - "GPUs (CUDA)"
  - "pmemd.MPI"
  - "GPU modules"
  - "job submission"
  - "H100 GPU Clusters"
  - "StdEnv/2023"
  - "MMPBSA"

questions:
  - "What are the primary differences between the Amber, AmberTools, and Amber-PMEMD modules available in the software stack?"
  - "Why must users avoid legacy AMBER modules and use specific versions like ambertools/25.0 or amber-pmemd/24.3 when running jobs on H100 GPU clusters?"
  - "How can users check the installed versions of Amber and find the correct commands to load the necessary modules for their specific CPU or GPU environment?"
  - "What are the specific module load commands required to run AmberTools 23.5 on CPUs versus GPUs within the StdEnv/2023 environment?"
  - "Which specific GPU architecture and external plugin are explicitly listed as compatible with this AMBER configuration?"
  - "What categories of information are used to organize the AMBER module documentation under the StdEnv/2020 tab?"
  - "What specific molecular dynamics engines are provided by AmberTools 21, and what command is required to set its environment variables?"
  - "Why are there two different versions of Amber 20 modules, and how does the choice between MKL and FlexiBLAS libraries affect performance on AMD CPUs?"
  - "What are the specific molecular dynamics programs provided by the CPU-only modules versus the GPU modules for Amber 20?"
  - "What are the known limitations regarding MMPBSA and PB calculations in specific versions of the Amber modules?"
  - "What are the specific CUDA version requirements for running GPU-accelerated simulations on Narval's A100 GPUs?"
  - "How should a user configure the SLURM job submission script for a CPU-only parallel MPI job across different clusters like Narval and Rorqual?"
  - "What version of CUDA is required to run simulations on the A100 GPUs installed on Narval?"
  - "What specific molecular dynamics programs are included in the CPU-only modules?"
  - "Which additional programs are provided by the GPU modules compared to the CPU-only modules?"
  - "Why does the parallel MMPBSA job scale linearly across multiple MPI processes?"
  - "What SLURM directives and modules are required to run a GPU-accelerated SANDER.QUICK MPI job according to the provided script?"
  - "Where can users find performance guides and specific benchmarks for AMBER tools like PMEMD and SANDER.QUICK?"
  - "What specific software modules and versions must be loaded to run the simulation?"
  - "Which input and output files are specified in the execution command for the Amber simulation?"
  - "What type of job is being configured, and how many GPUs does it request?"
  - "Why does the parallel MMPBSA job scale linearly across multiple MPI processes?"
  - "What SLURM directives and modules are required to run a GPU-accelerated SANDER.QUICK MPI job according to the provided script?"
  - "Where can users find performance guides and specific benchmarks for AMBER tools like PMEMD and SANDER.QUICK?"

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

## Amber modules
We provide modules for Amber, AmberTools, and Amber-PMEMD in our [software stack](available-software.md).

*   **[AmberTools](https://ambermd.org/AmberTools.php)** (module `ambertools`) - Tools for preparing/analyzing simulations, `QUICK` for GPU-accelerated DFT calculations and `sander` for molecular dynamics. Free and open source.
*   **[Amber](https://ambermd.org/AmberMD.php)** (module `amber`) - Everything included in AmberTools, plus the advanced `pmemd` program for high-performance molecular dynamics simulations.
*   **Amber-PMEMD** (module `amber-pmemd`, Amber 24+) – High-performance MD engine `pmemd`, optimized for CPU and GPU.
    Provides the high-performance MD engine `pmemd` (optimized for CPU/GPU) as a **standalone module**. This change was made because starting with Amber 24, `pmemd` no longer requires AmberTools for compilation.

!!! note "Amber-PMEMD Module"
    The `amber-pmemd` module does not include AmberTools. To use both, load the `ambertools` module as well.

To see a list of installed versions and which other modules they depend on, you can use the `module spider` [command](using-modules.md#sub-command-spider) or check the [Available software](available-software.md) page.

## Using AMBER on H100 GPU Clusters

!!! warning "H100 GPU Compatibility Update"
    Older AMBER modules are incompatible with NVIDIA H100 GPUs. For GPU-accelerated runs, use the newly installed modules below.

### Module Requirements:

`ambertools/25.0` or `amber-pmemd/24.3`

These modules include H100-specific CUDA kernels (compiled with CUDA 12+ for the Hopper architecture).

!!! warning "Avoid Legacy Modules on H100"
    Do not use legacy AMBER modules for GPU jobs — they will fail on H100 nodes.

## Loading modules

=== "StdEnv/2023"

| AMBER version     | modules for running on CPUs                                  | modules for running on GPUs (CUDA)                                | Notes               |
| :---------------- | :----------------------------------------------------------- | :----------------------------------------------------------------- | :------------------ |
| `amber-pmemd/24.3` | `StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 amber-pmemd/24.3` | `StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 amber-pmemd/24.3`    | H100 compatible     |
| `amber/22.5-23.5`  | `StdEnv/2023 gcc/12.3 openmpi/4.1.5 amber/22.5-23.5`         | `StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.2 amber/22.5-23.5`     |                     |
| `ambertools/25.0`  | `StdEnv/2023 gcc/12.3 openmpi/4.1.5 ambertools/25.0`         | `StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 ambertools/25.0`     | H100 compatible, with PLUMED/2.9.0 |
| `ambertools/23.5`  | `StdEnv/2023 gcc/12.3 openmpi/4.1.5 ambertools/23.5`         | `StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.2 ambertools/23.5`     |                     |

=== "StdEnv/2020"

| AMBER version     | modules for running on CPUs                                          | modules for running on GPUs (CUDA)                                           | Notes              |
| :---------------- | :------------------------------------------------------------------- | :--------------------------------------------------------------------------- | :----------------- |
| `ambertools/21`   | `StdEnv/2020 gcc/9.3.0 openmpi/4.0.3 scipy-stack ambertools/21`      | `StdEnv/2020 gcc/9.3.0 cuda/11.4 openmpi/4.0.3 scipy-stack ambertools/21`    | GCC, FlexiBLAS & FFTW |
| `amber/20.12-20.15`| `StdEnv/2020 gcc/9.3.0 openmpi/4.0.3 amber/20.12-20.15`              | `StdEnv/2020 gcc/9.3.0 cuda/11.4 openmpi/4.0.3 amber/20.12-20.15`            | GCC, FlexiBLAS & FFTW |
| `amber/20.9-20.15` | `StdEnv/2020 gcc/9.3.0 openmpi/4.0.3 amber/20.9-20.15`               | `StdEnv/2020 gcc/9.3.0 cuda/11.0 openmpi/4.0.3 amber/20.9-20.15`             | GCC, MKL & FFTW    |
| `amber/18.14-18.17`| `StdEnv/2020 gcc/9.3.0 openmpi/4.0.3 amber/18.14-18.17`              | `StdEnv/2020 gcc/8.4.0 cuda/10.2 openmpi/4.0.3`                              | GCC, MKL           |

=== "StdEnv/2016"

| AMBER version     | modules for running on CPUs                                                | modules for running on GPUs (CUDA)                                                | Notes               |
| :---------------- | :------------------------------------------------------------------------- | :-------------------------------------------------------------------------------- | :------------------ |
| `amber/18`        | `StdEnv/2016 gcc/5.4.0 openmpi/2.1.1 scipy-stack/2019a amber/18`           | `StdEnv/2016 gcc/5.4.0 openmpi/2.1.1 cuda/9.0.176 scipy-stack/2019a amber/18`     | GCC, MKL            |
| `amber/18.10-18.11`| `StdEnv/2016 gcc/5.4.0 openmpi/2.1.1 scipy-stack/2019a amber/18.10-18.11` | `StdEnv/2016 gcc/5.4.0 openmpi/2.1.1 cuda/9.0.176 scipy-stack/2019a amber/18.10-18.11` | GCC, MKL            |
| `amber/18.10-18.11`| `StdEnv/2016 gcc/7.3.0 openmpi/3.1.2 scipy-stack/2019a amber/18.10-18.11` | `StdEnv/2016 gcc/7.3.0 cuda/9.2.148 openmpi/3.1.2 scipy-stack/2019a amber/18.10-18.11` | GCC, MKL            |
| `amber/16`        | `StdEnv/2016.4 amber/16`                                                   |                                                                                   | Available only on Graham. Some Python functionality is not supported |

## Using modules
### AmberTools 21
Currently, AmberTools 21 module is available on all clusters. AmberTools provide the following MD engines: sander, sander.LES, sander.LES.MPI, sander.MPI, sander.OMP, sander.quick.cuda, and sander.quick.cuda.MPI. After loading the module set AMBER environment variables:

```bash
source $EBROOTAMBERTOOLS/amber.sh
```

### Amber 20
There are two versions of amber/20 modules: 20.9-20.15 and 20.12-20.15. The first one uses MKL and cuda/11.0, while the second uses FlexiBLAS and cuda/11.4. MKL libraries do not perform well on AMD CPU, and FlexiBLAS solves this problem. It detects CPU type and uses libraries optimized for the hardware. cuda/11.4 is required for running simulations on A100 GPUs installed on Narval.

CPU-only modules provide all MD programs available in AmberTools/20 plus `pmemd` (serial) and `pmemd.MPI` (parallel). GPU modules add `pmemd.cuda` (single GPU), and `pmemd.cuda.MPI` (multi - GPU).

### Known issues
1.  Module `amber/20.12-20.15` does not have `MMPBSA.py.MPI` executable.
2.  `MMPBSA.py` from `amber/18-10-18.11` and `amber/18.14-18.17` modules cannot perform PB calculations. Use more recent `amber/20` modules for this type of calculations.

## Job submission examples
### Single GPU job
For GPU-accelerated simulations on Narval, use `amber/20.12-20.15`. Modules compiled with CUDA version < 11.4 do not work on A100 GPUs. Below is an example submission script for a single-GPU job.

```bash title="pmemd_cuda_job.sh"
#!/bin/bash
#SBATCH --ntasks=1 
#SBATCH --gpus-per-node=1 
#SBATCH --mem-per-cpu=2000 
#SBATCH --time=10:00:00

module purge
module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 amber-pmemd/24.3

pmemd.cuda -O -i input.in -p topol.parm7 -c coord.rst7 -o output.mdout -r restart.rst7
```

### CPU-only parallel MPI job

=== "Narval"
    ```sh title="pmemd_MPI_job_narval.sh"
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
    ```sh title="pmemd_MPI_job_rorqual.sh"
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
    ```sh title="pmemd_MPI_job_fir.sh"
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
    ```sh title="pmemd_MPI_job_nibi.sh"
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
    ```sh title="pmemd_MPI_job_trillium.sh"
    #!/bin/bash
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=192
    #SBATCH --mem-per-cpu=2000
    #SBATCH --time=1:00:00

    module purge
    module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 amber-pmemd/24.3

    srun pmemd.MPI -O -i input.in -p topol.parm7 -c coord.rst7 -o output.mdout -r restart.rst7
    ```

### QM/MM distributed multi-GPU job
The example below requests eight GPUs.

```bash title="quick_MPI_job.sh"
#!/bin/bash
#SBATCH --ntasks=8
#SBATCH --gpus-per-task=1 
#SBATCH --mem-per-cpu=4000 
#SBATCH --time=02:00:00

module purge
module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 ambertools/25.0

srun sander.quick.cuda.MPI -O -i input.in -p topol.parm7 -c coord.rst7 -o output.mdout -r restart.rst7
```

### Parallel MMPBSA job
The example below uses 32 MPI processes. MMPBSA scales linearly because each trajectory frame is processed independently.

```bash title="mmpbsa_job.sh"
#!/bin/bash
#SBATCH --ntasks=32 
#SBATCH --mem-per-cpu=4000 
#SBATCH --time=1:00:00

module purge
module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 ambertools/25.0

srun MMPBSA.py.MPI -O -i mmpbsa.in -o mmpbsa.dat -sp solvated_complex.parm7 -cp complex.parm7 -rp receptor.parm7 -lp ligand.parm7 -y trajectory.nc
```

You can modify scripts to fit your simulation requirements for computing resources. See [Running jobs](running-jobs.md) for more details.

## Performance and benchmarking

A team at [ACENET](https://www.ace-net.ca/) has created a [Molecular Dynamics Performance Guide](https://mdbench.ace-net.ca/mdbench/ Molecular Dynamics Performance Guide) for Alliance clusters.
It can help you determine optimal conditions for AMBER, GROMACS, NAMD, and OpenMM jobs. The present section focuses on AMBER performance.

View benchmarks of simulations with [PMEMD](http://mdbench.ace-net.ca/mdbench/bform/?software_contains=PMEMD&software_id=&module_contains=&module_version=&site_contains=&gpu_model=&cpu_model=&arch=&dataset=6n4o)

View benchmarks of QM/MM simulations with [SANDER.QUICK](http://mdbench.ace-net.ca/mdbench/bform/?software_contains=&software_id=&module_contains=&module_version=&site_contains=&gpu_model=&cpu_model=&arch=&dataset=4cg1).