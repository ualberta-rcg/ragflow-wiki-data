---
title: "LAMMPS/en"
slug: "lammps"
lang: "en"

source_wiki_title: "LAMMPS/en"
source_hash: "17cc9cbf8d64645f61efd3946a3b69a4"
last_synced: "2026-04-18T23:39:30.217451+00:00"
last_processed: "2026-04-19T00:55:34.672052+00:00"

tags:
  - software
  - biomolecularsimulation

keywords:
  - "CPU efficiency"
  - "CPU"
  - "list-packages.txt"
  - "GPU"
  - "simulation"
  - "cmake"
  - "LAMMPS modules"
  - "Compile and install"
  - "CUDA"
  - "modules"
  - "MPI tasks"
  - "torch"
  - "timesteps"
  - "lammps-mace"
  - "Job Submission"
  - "molecular dynamics"
  - "EBROOTLAMMPS"
  - "PyTorch"
  - "Compiling"
  - "domain decomposition"
  - "packages"
  - "MACE"
  - "force fields"
  - "Python virtual environment"
  - "LAMMPS"
  - "CPU use"
  - "Performance"
  - "enabled packages"
  - "OpenMP threads"

questions:
  - "What is LAMMPS and what parallelization technologies does it use to run simulations?"
  - "What types of modeling and force fields are supported by LAMMPS for different areas of application?"
  - "How can a user check the available versions, executables, and enabled packages of LAMMPS on the system?"
  - "Why might a LAMMPS simulation fail to work with a specific module?"
  - "What information is contained within the `list-packages.txt` file?"
  - "What command should be run to view the enabled and disabled packages after loading a module?"
  - "How can you determine which LAMMPS packages are enabled if the list-packages.txt file is missing?"
  - "What are the key differences between the provided serial and MPI job scripts for running a LAMMPS simulation?"
  - "Why does increasing the number of processors in a LAMMPS simulation eventually decrease CPU efficiency, and how should users determine the optimal number of cores?"
  - "How does the time spent on communication versus computing pair interactions scale with an increasing number of cores across different system sizes?"
  - "What are the initial steps required to clone the LAMMPS repository and set up the Python virtual environment for compiling MACE?"
  - "What are the key differences in the required loaded modules and CMake configuration flags when compiling MACE for a GPU environment compared to a CPU environment?"
  - "What is the overall simulation scale in terms of the number of steps and atoms processed?"
  - "What are the reported performance metrics and CPU utilization details for the given MPI and OpenMP configuration?"
  - "According to the performance table, which computational sections account for the majority of the total execution time?"
  - "How do you compile and install the LAMMPS-MACE software into a local directory?"
  - "What commands are required to perform a quick test of the newly installed LAMMPS executable?"
  - "How do the SLURM job submission scripts differ when running LAMMPS-MACE on a CPU versus a GPU?"
  - "What version of PyTorch is required to be installed before configuring MACE?"
  - "What CMake flags are used to enable MPI and the ML-MACE package in the build configuration?"
  - "Which specific CUDA architecture version is targeted during the CMake setup?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Parent page: [Biomolecular simulation](molecular-sim/biomolecular_simulation.md)*

## General

**LAMMPS** is a classical molecular dynamics code. The name stands for **L**arge-scale **A**tomic / **M**olecular **M**assively **P**arallel **S**imulator. LAMMPS is distributed by [Sandia National Laboratories](http://www.sandia.gov/), a US Department of Energy laboratory.

* Project web site: <http://lammps.sandia.gov/>
* Documentation: [Online Manual](http://lammps.sandia.gov/doc/Manual.html).
* Mailing List: <http://lammps.sandia.gov/mail.html>

LAMMPS is parallelized with [MPI](mpi.md) and [OpenMP](../programming/openmp.md), and can run on [GPUs](../running-jobs/using_gpus_with_slurm.md).

## Force fields

All supported force fields are listed on the [package web site](https://lammps.sandia.gov/doc/Intro_features.html#ff), classified by functional form (e.g. pairwise potentials, many-body potentials, etc.). The large number of supported force fields makes LAMMPS suitable for many areas of application. Here are some types of modelling and force fields suitable for each:

* Biomolecules: CHARMM, AMBER, OPLS, COMPASS (class 2), long-range Coulombics via PPPM, point dipoles, ...
* Polymers: all-atom, united-atom, coarse-grain (bead-spring FENE), bond-breaking, …
* Materials: EAM and MEAM for metals, Buckingham, Morse, Yukawa, Stillinger-Weber, Tersoff, EDIP, COMB, SNAP, ...
* Reactions: AI-REBO, REBO, ReaxFF, eFF
* Mesoscale: granular, DPD, Gay-Berne, colloidal, peri-dynamics, DSMC...

Combinations of potentials can be used for hybrid systems, e.g. water on metal, polymer/semiconductor interfaces, colloids in solution, ...

## Versions and packages

To see which versions of LAMMPS are installed on our systems, run `module spider lammps`. See [Using modules](../programming/modules.md) for more about `module` subcommands.

LAMMPS version numbers are based on their release dates, and have the format YYYYMMDD. You should run:
```bash
module avail lammps
```
to see all the releases that are installed, so you can find the one which is most appropriate for you to use.

For each release installed, one or more modules are available.
For example, the release of 31 March 2017 has three modules:

* Built with MPI: `lammps/20170331`
* Built with USER-OMP support: `lammps-omp/20170331`
* Built with USER-INTEL support: `lammps-user-intel/20170331`

!!! note "GPU-enabled Versions"
    To use the GPU-enabled version, load the [CUDA](../programming/cuda.md) module *before* loading the LAMMPS module:
    ```bash
    module load cuda
    module load lammps-omp/20170331
    ```

The name of the executable may differ from one version to another. All prebuilt versions on our clusters have a symbolic link called `lmp`. This means that no matter which module you pick, you can execute LAMMPS by calling `lmp`.

If you wish to see the original name of the executable for a given module, list the files in the `${EBROOTLAMMPS}/bin` directory. For example:
```bash
module load lammps-omp/20170331
ls ${EBROOTLAMMPS}/bin/
```
In this example the executable is `lmp_icc_openmpi`, and `lmp` is the symbolic link to it.

The reason there are different modules for the same release is the difference in the *packages* included. Recent versions of LAMMPS contain about 60 different packages that can be enabled or disabled when compiling the program. Not all packages can be enabled in a single executable. All [packages](https://lammps.sandia.gov/doc/Packages.html) are documented on the official web page.

!!! warning "Package Compatibility"
    If your LAMMPS simulation does not work with a particular module, it may be because a necessary package was not enabled during compilation. Not all packages can be enabled in a single executable.

For some LAMMPS modules, we provide a file `list-packages.txt` listing the enabled ("Supported") and disabled ("Not Supported") packages. Once you have loaded a particular module, run `cat ${EBROOTLAMMPS}/list-packages.txt` to see the contents.

If `list-packages.txt` is not found, you may be able to determine which packages are available by examining the [EasyBuild](../programming/easybuild.md) recipe file, `$EBROOTLAMMPS/easybuild/LAMMPS*.eb`. The list of enabled packages will appear in the block labelled `general_packages`.

## Example of input file

The input file below can be used with either of the example job scripts.

=== "INPUT"

    ```txt title="lammps.in"
    # 3d Lennard-Jones melt

    units           lj
    atom_style      atomic

    lattice         fcc 0.8442
    region          box block 0 15 0 15 0 15
    create_box      1 box
    create_atoms    1 box
    mass            1 1.0

    velocity        all create 1.44 87287 loop geom

    pair_style      lj/cut 2.5
    pair_coeff      1 1 1.0 1.0 2.5
    neighbor        0.3 bin
    neigh_modify    delay 5 every 1

    fix             1 all nve
    thermo          5
    run             10000
    write_data     config.end_sim

    # End of the Input file.
    ```

=== "Serial job"

    ```bash title="run_lmp_serial.sh"
    #!/bin/bash

    #SBATCH --ntasks=1
    #SBATCH --mem-per-cpu=2500M
    #SBATCH --time=0-00:30

    module load StdEnv/2020 intel/2020.1.217 openmpi/4.0.3 lammps-omp/20210929

    lmp < lammps.in > lammps_output.txt
    ```

=== "MPI job"

    ```bash title="run_lmp_mpi.sh"
    #!/bin/bash

    #SBATCH --ntasks=4
    #SBATCH --mem-per-cpu=2500M
    #SBATCH --time=0-00:30 

    module load StdEnv/2020 intel/2020.1.217 openmpi/4.0.3 lammps-omp/20210929

    srun lmp < lammps.in > lammps_output.txt
    ```

## Performance

Most of the CPU time for molecular dynamics simulations is spent in computing the pair interactions between particles. LAMMPS uses domain decomposition to split the work among the available processors by assigning a part of the simulation box to each processor. During the computation of the interactions between particles, communication between the processors is required. For a given number of particles, the more processors that are used, the more parts of the simulation box there are which must exchange data. Therefore, the communication time increases with increasing number of processors, eventually leading to low CPU efficiency.

!!! tip "Performance Testing"
    Before running extensive simulations for a given problem size or a size of the simulation box, it is recommended to run tests to see how the program's performance changes with the number of cores. Run short tests using different numbers of cores to find a suitable number of cores that will (approximately) maximize the efficiency of the simulation.

The following example shows the timing for a simulation of a system of 4000 particles using 12 MPI tasks. This is an example of a very low efficiency: by using 12 cores, the system of 4000 atoms was divided to 12 small boxes. The code spent 46.45% of the time computing pair interactions and 44.5% in communications between the processors. The large number of small boxes for such a small system is responsible for the large fraction of time spent in communication.

Loop time of 15.4965 on 12 procs for 25000 steps with 4000 atoms.
Performance: 696931.853 tau/day, 1613.268 timesteps/s.
90.2% CPU use with 12 MPI tasks x 1 OpenMP threads.

| Section | **min time** | **avg time** | **max time** | **%varavg** | **%total** |
| :------ | :----------- | :----------- | :----------- | :---------- | :--------- |
| Pair    | 6.6964       | 7.1974       | 7.9599       | 14.8        | **46.45**  |
| Neigh   | 0.94857      | 1.0047       | 1.0788       | 4.3         | 6.48       |
| Comm    | 6.0595       | 6.8957       | 7.4611       | 17.1        | **44.50**  |
| Output  | 0.01517      | 0.01589      | 0.019863     | 1.0         | 0.10       |
| Modify  | 0.14023      | 0.14968      | 0.16127      | 1.7         | 0.97       |
| Other   | --           | 0.2332       | --           | --          | 1.50       |

In the next example, we compare the time spent in communication and computing the pair interactions for different system sizes:

| Cores | 2048 atoms (Pairs) | 2048 atoms (Comm) | 4000 atoms (Pairs) | 4000 atoms (Comm) | 6912 atoms (Pairs) | 6912 atoms (Comm) | 13500 atoms (Pairs) | 13500 atoms (Comm) |
| :---- | :----------------- | :---------------- | :----------------- | :---------------- | :----------------- | :---------------- | :------------------ | :------------------ |
| 1     | 73.68              | 1.36              | 73.70              | 1.28              | 73.66              | 1.27              | 73.72               | 1.29                |
| 2     | 70.35              | 5.19              | 70.77              | 4.68              | 70.51              | 5.11              | 67.80               | 8.77                |
| 4     | 62.77              | 13.98             | 64.93              | 12.19             | 67.52              | 8.99              | 67.74               | 8.71                |
| 8     | 58.36              | 20.14             | 61.78              | 15.58             | 64.10              | 12.86             | 62.06               | 8.71                |
| 16    | 56.69              | 20.18             | 56.70              | 20.18             | 56.97              | 19.80             | 56.41               | 20.38               |

## MACE in LAMMPS
### Compiling MACE in LAMMPS with PyTorch

1. From a login node, first clone the branch `mace`:
```bash
mkdir ~/lammps-mace
cd $SCRATCH
git clone --branch=mace --depth=1 https://github.com/ACEsuit/lammps && cd lammps
git checkout 4d222cb  # current HEAD commit from branch
```
And identify a commit for future reference.

=== "CPU"

    2. Load required modules to configure MACE and build
    ```bash
    module load python/3.14 gcc openmpi flexiblas cmake fftw eigen protobuf abseil flatbuffers opencv sleef xnnpack
    ```

    3. Create and activate a [Python virtual environment](python.md#creating-and-using-a-virtual-environment):
    ```bash
    virtualenv --clear ~/lammps-mace/ENV && source ~/lammps-mace/ENV/bin/activate
    ```

    4. Install PyTorch in this virtual environment:
    ```bash
    pip install --no-index --upgrade pip
    pip install --no-index 'torch>=2.10.0'
    ```

    5. Configure MACE
    ```bash
    cmake --fresh -S cmake -B _build -DBUILD_MPI=ON -DPKG_ML-MACE=ON -DCMAKE_PREFIX_PATH="$(python -c 'import torch; print(torch.utils.cmake_prefix_path)')" -DCMAKE_INSTALL_PREFIX=$HOME/lammps-mace -DCMAKE_SKIP_RPATH=ON
    ```

=== "GPU"

    2. Load required modules to configure MACE and build
    ```bash
    module load python/3.14 gcc openmpi flexiblas cmake fftw eigen protobuf abseil flatbuffers cuda/12.9 cusparselt cudnn nccl magma opencv cudss sleef xnnpack
    ```
    Here we are using cuda 12.9 since it matches what PyTorch was built against.

    3. Create and activate a [Python virtual environment](python.md#creating-and-using-a-virtual-environment):
    ```bash
    virtualenv --clear ~/lammps-mace/ENV && source ~/lammps-mace/ENV/bin/activate
    ```

    4. Install PyTorch in this virtual environment:
    ```bash
    pip install --no-index --upgrade pip
    pip install --no-index 'torch>=2.10.0'
    ```

    5. Configure MACE
    ```bash
    cmake --fresh -S cmake -B _build -DBUILD_MPI=ON -DPKG_ML-MACE=ON -DCMAKE_PREFIX_PATH="$(python -c 'import torch; print(torch.utils.cmake_prefix_path)')" -DCMAKE_INSTALL_PREFIX=$HOME/lammps-mace -DCMAKE_SKIP_RPATH=ON -DTORCH_CUDA_ARCH_LIST="9.0"
    ```

6. Compile and install into a local `lammps-mace` directory
```bash
cmake --build _build --parallel 4
cmake --install _build/ --prefix=$HOME/lammps-mace
```

7. Quick test
```bash
deactivate
module purge
~/lammps-mace/bin/lmp -h
```

### Job Submission Examples

=== "CPU"

    ```bash title="mace-lammps-cpu.sh"
    #!/bin/bash

    #SBATCH --job-name lammps-mace
    #SBATCH --account MY-ACCOUNT-CPU
    #SBATCH --nodes=1
    #SBATCH --ntasks=4
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=3500M
    #SBATCH --time=01:00:00
    #SBATCH --mail-type=FAIL

    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    srun $HOME/lammps-mace/bin/lmp -in in.lammps
    ```

=== "GPU"

    ```bash title="mace-lammps-gpu.sh"
    #!/bin/bash

    #SBATCH --job-name lammps-mace
    #SBATCH --account MY-ACCOUNT-GPU
    #SBATCH --nodes=1
    #SBATCH --ntasks=4
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=3500M
    #SBATCH --gpus=h100_1g.10gb:1
    #SBATCH --time=01:00:00
    #SBATCH --mail-type=FAIL

    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    srun $HOME/lammps-mace/bin/lmp -in in.lammps