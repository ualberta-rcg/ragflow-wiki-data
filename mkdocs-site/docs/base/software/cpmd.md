---
title: "CPMD"
slug: "cpmd"
lang: "base"

source_wiki_title: "CPMD"
source_hash: "fc309ea2527d6e7a645ba3193774266e"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:04:16.215136+00:00"

tags:
  - software
  - computationalchemistry
  - biomolecularsimulation

keywords:
  - "single point calculation"
  - "pseudo-potentials"
  - "openmpi"
  - "SBATCH"
  - "molecular dynamics simulations"
  - "EasyBuild"
  - "optimize wavefunction"
  - "bash script"
  - "isolated hydrogen molecule"
  - "CPMD"
  - "job script"
  - "DFT functional LDA"
  - "local installation"

questions:
  - "How can a user obtain the necessary permissions to access the centrally installed CPMD software on the clusters?"
  - "What is the procedure for building and installing CPMD locally in a user's home directory using EasyBuild?"
  - "How do you properly format the command to run a CPMD job in parallel while specifying the input file and pseudo-potentials location?"
  - "What SLURM resource allocations are specified for running the job in the provided bash scripts?"
  - "What is the primary difference between Script 1 and Script 2 when executing the CPMD program?"
  - "Which specific software modules and versions need to be loaded into the environment to run the simulation?"
  - "What type of calculation is being performed on the hydrogen molecule according to the INFO section?"
  - "What are the specific wavefunction convergence criteria and output settings defined in the CPMD section?"
  - "Which cell dimensions, cutoff energy, and DFT functional are specified for this simulation system?"
  - "What SLURM resource allocations are specified for running the job in the provided bash scripts?"
  - "What is the primary difference between Script 1 and Script 2 when executing the CPMD program?"
  - "Which specific software modules and versions need to be loaded into the environment to run the simulation?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[CPMD](https://www.cpmd.org/wordpress/) is a plane wave/pseudo-potential DFT code for *ab initio* molecular dynamics simulations.

## License Limitations

In the past, access to CPMD required registration and confirmation with the developers, but registration on their website is no longer needed. However, the modules installed on our clusters are still protected by a POSIX group.

!!! note
    Before you can start using [CPMD](http://cpmd.org) on our clusters, [send us a support request](../support/technical_support.md) and ask to be added to the POSIX group that will allow you to access the software.

## Module

You can access CPMD by loading a [module](../programming/utiliser_des_modules.md).

```bash
module load StdEnv/2020
module load intel/2020.1.217 openmpi/4.0.3 cpmd/4.3
```

## Local Installation of CPMD

!!! note
    It has recently been our experience that a response from CPMD admins can unfortunately take weeks or even months. If you are a registered CPMD user, you have access to the CPMD source files and can therefore build the software yourself in your `/home` directory using our software environment called EasyBuild, with the exact same recipe that we would use for a central installation.

Below are instructions on how to build CPMD 4.3 under your account on the cluster of your choice:

Create a local directory like so
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

Then run the EasyBuild command.
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

## Example of a Job Script

To run a job, you will need to set an input file and access to the pseudo-potentials.

If the input file and the pseudo-potentials are in the same directory, the command to run the program in parallel is:

`srun cpmd.x <input files> > <output file>` (as in Script 1)

It is also possible to put the pseudo-potentials in another directory with

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

    srun cpmd.x ${CPMD_INPUT} > ${CPMD_OUTPUT}

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

    srun cpmd.x ${CPMD_INPUT} ${PP_PATH} > ${CPMD_OUTPUT}

    echo "Program finished with exit code $? at: `date`"
    ```

## Related Link

*   CPMD [home page](https://www.cpmd.org/wordpress/).