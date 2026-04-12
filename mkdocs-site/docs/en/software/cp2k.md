---
title: "CP2K/en"
slug: "cp2k"
lang: "en"

source_wiki_title: "CP2K/en"
source_hash: "ee3819ff22d7ef112f506bc39f7f5d33"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:02:22.137032+00:00"

tags:
  - software
  - computationalchemistry

keywords:
  - "quantum chemistry"
  - "job submission"
  - "CP2K"
  - "MPI processes"
  - "atomistic simulations"

questions:
  - "What is the CP2K software package and what types of systems can it simulate?"
  - "Why is the GCC-compiled module of CP2K recommended over the Intel-compiled version?"
  - "What are the differences between the cp2k.popt and cp2k.psmp executables, and how do they affect job performance?"
  - "What is the CP2K software package and what types of systems can it simulate?"
  - "Why is the GCC-compiled module of CP2K recommended over the Intel-compiled version?"
  - "What are the differences between the cp2k.popt and cp2k.psmp executables, and how do they affect job performance?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

**CP2K** is a quantum chemistry and solid-state physics software package that can perform atomistic simulations of solid-state, liquid, molecular, periodic, material, crystal, and biological systems.

## Versions

The latest version installed is CP2K 8.2. You can load the module compiled with GCC using:

```bash
module load StdEnv/2020  gcc/9.3.0  openmpi/4.0.3 cp2k/8.2
```

!!! warning "Intel-Compiled Version Stability"
    While an Intel-compiled version is available, it appears less stable and has been observed to crash for unknown reasons. The GCC-compiled module is generally recommended.

```bash
module load StdEnv/2020  intel/2020.1.217  openmpi/4.0.3 cp2k/8.2
```

## Example job

Here we will use the static calculation example from the [CP2K website](https://www.cp2k.org/howto:static_calculation).

First, log into one of our clusters and download the needed files with the following commands:

```bash
wget https://www.cp2k.org/_media/static_calculation.tgz
tar xvfz static_calculation.tgz
cd static_calculation/sample_output_no_smearing
```

Then, in that directory, create the following job submission script, with the account name changed to the one you are using.

```bash title="mpi_job.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --ntasks=4               # number of MPI processes
#SBATCH --mem-per-cpu=4G      # memory; default unit is megabytes
#SBATCH --time=0-00:15           # time (DD-HH:MM)

module load StdEnv/2020  gcc/9.3.0  openmpi/4.0.3 cp2k/8.2
srun cp2k.popt -o Si_bulk8.out Si_bulk8.inp
```

To submit this job, execute:

```bash
sbatch mpi_job.sh
```

To see if the job completed, run the command:

```bash
sq
```

If your job is no longer listed, that means it has completed.

The output of CP2K will be located in the file `Si_bulk8.out`. There will also be an output file named `slurm-*.out` which should be empty if the calculation completed without error.

## Threaded/MPI jobs

The installation of CP2K version 8.2 and later includes both the MPI executable `cp2k.popt` and the OpenMP/MPI executable `cp2k.psmp`, which may give better performance for some calculations. Our test shows a 10% performance increase for `QS/H2O-512.inp` benchmark when using 2 threads per MPI process, compared to running MPI-only executable `cp2k.popt` (both runs used the same number of CPU cores in total).

!!! tip "Considerations for Threaded/MPI Jobs"
    The example OpenMP/MPI job submission file below is configured for the Beluga cluster. If you are using other clusters, you will need to adjust the number of tasks to match the available cores on that cluster's nodes.
    It is crucial to note that performance with threads can be highly problem-dependent. Running the `cp2k.psmp` executable might even be slower in some cases. Always benchmark your code to determine the optimal configuration for your specific scenario.

```bash title="openmp_mpi_job.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --nodes=2
#SBATCH --ntasks=40               # number of MPI processes
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu=3G      # memory; default unit is megabytes
#SBATCH --time=0-00:59           # time (DD-HH:MM)

module load StdEnv/2020  gcc/9.3.0  openmpi/4.0.3 cp2k/8.2

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
srun --cpus-per-task=$OMP_NUM_THREADS cp2k.psmp -o H2O-512.out H2O-512.inp