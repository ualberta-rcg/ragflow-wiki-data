---
title: "CPMD/en"
slug: "cpmd"
lang: "en"

source_wiki_title: "CPMD/en"
source_hash: "0a9b7f424479f77f85e5428630e44555"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:04:38.828283+00:00"

tags:
  - software
  - computationalchemistry
  - biomolecularsimulation

keywords:
  - "pseudo-potentials"
  - "H_MT_LDA.psp"
  - "SBATCH"
  - "EasyBuild"
  - "run-cpmd.sh"
  - "cpmd"
  - "bash script"
  - "ab initio molecular dynamics"
  - "CPMD"
  - "srun"
  - "job script"

questions:
  - "What steps must a user take to gain access to the centrally installed CPMD modules on the cluster?"
  - "How can a registered user compile and install CPMD locally in their own directory using EasyBuild?"
  - "What is the correct command syntax to run a CPMD job in parallel using a submission script?"
  - "What is the primary software application being executed by the provided SLURM batch scripts?"
  - "What is the key difference between the two script versions regarding the arguments passed to the cpmd.x command?"
  - "Which specific software modules and resource allocations are required to set up the environment in the second script?"
  - "What specific computational resources are requested in the Slurm batch script?"
  - "Which software modules and versions are loaded to set up the environment for the job?"
  - "What parameters and files are defined in the atoms section of the configuration snippet?"
  - "What is the primary software application being executed by the provided SLURM batch scripts?"
  - "What is the key difference between the two script versions regarding the arguments passed to the cpmd.x command?"
  - "Which specific software modules and resource allocations are required to set up the environment in the second script?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[CPMD](https://www.cpmd.org/wordpress/) is a plane wave/pseudo-potential DFT code for ab initio molecular dynamics simulations.

## License Limitations

!!! note

    In the past, access to CPMD required registration and confirmation with the developers, but registration on their website is no longer needed. However, the modules installed on our clusters are still protected by a POSIX group.

    Before you can start using [CPMD](http://cpmd.org) on our clusters, [send us a support request](technical-support.md) and ask to be added to the POSIX group that will allow you to access the software.

## Module

You can access CPMD by loading a [module](utiliser-des-modules.md).

```bash
module load StdEnv/2020
module load intel/2020.1.217 openmpi/4.0.3 cpmd/4.3
```

## Local Installation of CPMD

!!! tip

    It has recently been our experience that a response from CPMD administrators can unfortunately take weeks or even months. If you are a registered CPMD user, you have access to the CPMD source files and can therefore build the software yourself in your `/home` directory using our software environment called EasyBuild, with the exact same recipe that we would use for a central installation.

Below are instructions on how to build CPMD 4.3 under your account on the cluster of your choice:

Create a local directory like so:

```bash
mkdir -p ~/.local/easybuild/sources/c/CPMD
```

Place all the CPMD source tarballs and patches into that directory.

```bash
ls -al ~/.local/easybuild/sources/c/CPMD
cpmd2cube.tar.gz
cpmd2xyz-scripts.tar.gz
cpmd-v4.3.tar.gz
fourier.tar.gz
patch.to.4612
patch.to.4615
patch.to.4616
patch.to.4621
patch.to.4624
patch.to.4627
```

Then run the EasyBuild command:

```bash
eb CPMD-4.3-iomkl-2020a.eb --rebuild
```

The `--rebuild` option forces EasyBuild to ignore CPMD 4.3 installed in a central location and proceed instead with the installation in your `/home` directory.

Once the software is installed, log out and log back in.

Now, when you type `module load cpmd`, the software installed in your `/home` directory will get picked up.

```bash
module load StdEnv/2020
module load intel/2020.1.217 openmpi/4.0.3 cpmd/4.3
which cpmd.x
~/.local/easybuild/software/2020/avx2/MPI/intel2020/openmpi4/cpmd/4.3/bin/cpmd.x
```

You can use it now as usual in your submission script.

## Example Job Script

To run a job, you will need to set an input file and access to the pseudo-potentials.

If the input file and the pseudo-potentials are in the same directory, the command to run the program in parallel is:

`srun cpmd.x <input files> > <output file>` (as in Script 1)

It is also possible to put the pseudo-potentials in another directory with:

`srun cpmd.x <input files> <path to pseudo potentials location> > <output file>` (as in Script 2)

=== "INPUT"

    ```txt title="1-h2-wave.inp"
    &INFO
    isolated hydrogen molecule.
    single point calculation.
    &END

    &CPMD
     OPTIMIZE WAVEFUNCTION
     CONVERGENCE ORBITALS
      1.0d-7
     CENTER MOLECULE ON
     PRINT FORCES ON
    &END

    &SYSTEM
     SYMMETRY
      1
     ANGSTROM
     CELL
      8.00 1.0 1.0  0.0  0.0  0.0
     CUTOFF
      70.0
    &END

    &DFT
     FUNCTIONAL LDA
    &END

    &ATOMS
    *H_MT_LDA.psp
     LMAX=S
      2
     4.371   4.000   4.000
     3.629   4.000   4.000
    &END
    ```

=== "Script 1"

    ```bash title="run-cpmd.sh"
    #!/bin/bash

    #SBATCH --account=def-someacct
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=4
    #SBATCH --mem-per-cpu=2500M
    #SBATCH --time=0-1:00

    # Load the modules:

    module load StdEnv/2020
    module load intel/2020.1.217 openmpi/4.0.3 cpmd/4.3

    echo "Starting run at: `date`"

    CPMD_INPUT="1-h2-wave.inp"
    CPMD_OUTPUT="1-h2-wave_output.txt"

    srun cpmd.x "${CPMD_INPUT}" > "${CPMD_OUTPUT}"

    echo "Program finished with exit code $? at: `date`"
    ```

=== "Script 2"

    ```bash title="run-cpmd.sh"
    #!/bin/bash

    #SBATCH --account=def-someacct
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=4
    #SBATCH --mem-per-cpu=2500M
    #SBATCH --time=0-1:00

    # Load the modules:

    module load StdEnv/2020
    module load intel/2020.1.217 openmpi/4.0.3 cpmd/4.3

    echo "Starting run at: `date`"

    CPMD_INPUT="1-h2-wave.inp"
    CPMD_OUTPUT="1-h2-wave_output.txt"
    PP_PATH=<path to the location of pseudo-potentials>

    srun cpmd.x "${CPMD_INPUT}" "${PP_PATH}" > "${CPMD_OUTPUT}"

    echo "Program finished with exit code $? at: `date`"
    ```

## Related Link

*   CPMD [home page](https://www.cpmd.org/wordpress/).