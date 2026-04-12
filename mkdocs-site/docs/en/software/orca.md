---
title: "ORCA/en"
slug: "orca"
lang: "en"

source_wiki_title: "ORCA/en"
source_hash: "1862880121787f9e66d06512169c437d"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:50:22.467892+00:00"

tags:
  - software
  - computationalchemistry

keywords:
  - "ORCA"
  - "Slurm"
  - "benzene.inp"
  - "bash"
  - "SBATCH"
  - "orca/4.2.1"
  - "openmpi/4.0.3"
  - "NBO"
  - "Quantum chemistry"
  - "input file"
  - "Gaussian"
  - "Cedar and Graham"
  - "bash script"
  - "run_orca.sh"
  - "MPI"
  - "Job submission"
  - "OpenMPI"
  - "Computational chemistry"

questions:
  - "What is the ORCA software and what are its primary applications in quantum chemistry?"
  - "What are the specific registration steps required to obtain a license and access prebuilt ORCA executables?"
  - "How should a user configure their input files and properly submit an MPI job script to run ORCA?"
  - "How must the input file be configured to properly allocate multiple cores for an ORCA job?"
  - "What is the recommended temporary workaround for resolving fatal errors caused by OpenMPI version inconsistencies?"
  - "How can users run NBO with ORCA on the clusters given that NBO is not installed as a separate module?"
  - "What are the specific computational resources, such as CPUs, memory, and time limit, requested for this SLURM job?"
  - "Which software modules and specific versions must be loaded into the environment before running the application?"
  - "What is the intended application being run by this script, and what is the name of the file where its execution output will be saved?"
  - "On which computing clusters are the Gaussian modules installed?"
  - "What software access is required for users who want to use NBO with ORCA?"
  - "What specific keyword must be included in the input file when setting up the script?"
  - "What specific computational resources, such as nodes, tasks, memory, and time limits, are requested by the Slurm directives in the script?"
  - "Which software modules and environment variables are required to be loaded and configured before running the ORCA executable?"
  - "What is the exact command used to execute the ORCA input file, and where can users find additional tutorials and support forums?"
  - "What specific computational resources, such as nodes, tasks, memory, and time limits, are requested by the Slurm directives in the script?"
  - "Which software modules and environment variables are required to be loaded and configured before running the ORCA executable?"
  - "What is the exact command used to execute the ORCA input file, and where can users find additional tutorials and support forums?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Introduction
ORCA is a flexible, efficient, and easy-to-use general-purpose tool for quantum chemistry with specific emphasis on spectroscopic properties of open-shell molecules. It features a wide variety of standard quantum chemical methods ranging from semiempirical methods to DFT to single- and multireference correlated *ab initio* methods. It can also treat environmental and relativistic effects.

## Licensing
If you wish to use prebuilt ORCA executables:
1. You have to register at https://orcaforum.kofo.mpg.de/.
2. You will receive a first email to verify the email address and activate the account. Follow the instructions in that email.
3. Once the registration is complete, you will get a **second email** stating that the "*registration for ORCA download and usage has been completed*".
4. [Contact us](../support/technical_support.md) requesting access to ORCA with a copy of the **second email**.

## ORCA versions

### ORCA 6

A module `orca/6.0.1` is available under the environment `StdEnv/2023`. To load this module, use:

```bash
module load StdEnv/2023  gcc/12.3  openmpi/4.1.5 orca/6.0.1
```

There is another module `orca/6.0.0`. However, ORCA users should use the latest version `orca/6.0.1` as it addresses some bugs of the first release `6.0.0`.

!!! note "Note"
    This version of ORCA includes xtb 6.7.1.

### ORCA 5

Versions 5.0.1 through 5.0.3 have some bugs that were fixed in version 5.0.4, most notably a [bug involving D4 dispersion gradients](https://orcaforum.kofo.mpg.de/viewtopic.php?f=56&t=9985). We therefore recommend that you use the version 5.0.4 instead of any earlier 5.0.x version. Versions 5.0.1, 5.0.2 and 5.0.3 are in our software stack but might be removed in the future.

To load version 5.0.4, use

```bash
module load StdEnv/2020  gcc/10.3.0  openmpi/4.1.1 orca/5.0.4
```

### ORCA 4

To load version 4.2.1, use

```bash
module load StdEnv/2020  gcc/9.3.0  openmpi/4.0.3 orca/4.2.1
```

or

```bash
module load nixpkgs/16.09  gcc/7.3.0  openmpi/3.1.4 orca/4.2.1
```

## Setting ORCA input files

In addition to the different keywords required to run a given simulation, you should make sure to set two additional parameters:

*   number of CPUs
*   maxcore

## Using the software
To see which versions of ORCA are currently available, type `module spider orca`. For detailed information about a specific version, including the other modules that must be loaded first, use the module's full name. For example, `module spider orca/4.0.1.2`.

See [Using modules](../programming/modules.md) for general guidance.

### Job submission
For a general discussion about submitting jobs, see [Running jobs](../running-jobs/running_jobs.md).

!!! note "Note"
    If you run into MPI errors with some of the ORCA executables, you can try to define the following variables:

    `export OMPI_MCA_mtl='^mxm'`
    `export OMPI_MCA_pml='^yalla'`

The following is a job script to run ORCA using [MPI](mpi.md). Note that, unlike most MPI programs, ORCA is not started with a parallel launch command such as `mpirun` or `srun`, but requires the full path to the program, which is given by `$EBROOTORCA`.

/// tab | run_orca.sh
```bash
#!/bin/bash
#SBATCH --account=def-youPIs
#SBATCH --ntasks=8                 # cpus, the nprocs defined in the input file
#SBATCH --mem-per-cpu=3G           # memory per cpu
#SBATCH --time=00-03:00            # time (DD-HH:MM)
#SBATCH --output=benzene.log       # output .log file

module load StdEnv/2020  gcc/9.3.0  openmpi/4.0.3
module load orca/4.2.1
$EBROOTORCA/orca benzene.inp
```

Example of the input file, benzene.inp:
/// tab | benzene.inp
```text
# Benzene RHF Opt Calculation
%pal nprocs 8 end
! RHF TightSCF PModel
! opt

* xyz 0 1
     C    0.000000000000     1.398696930758     0.000000000000
     C    0.000000000000    -1.398696930758     0.000000000000
     C    1.211265339156     0.699329968382     0.000000000000
     C    1.211265339156    -0.699329968382     0.000000000000
     C   -1.211265339156     0.699329968382     0.000000000000
     C   -1.211265339156    -0.699329968382     0.000000000000
     H    0.000000000000     2.491406946734     0.000000000000
     H    0.000000000000    -2.491406946734     0.000000000000
     H    2.157597486829     1.245660462400     0.000000000000
     H    2.157597486829    -1.245660462400     0.000000000000
     H   -2.157597486829     1.245660462400     0.000000000000
     H   -2.157597486829    -1.245660462400     0.000000000000
*
```

### Notes
*   To make sure that the program runs efficiently and makes use of all the resources or the cores asked for in your job script, please add this line `%pal nprocs <ncores> end` to your input file as shown in the above example. Replace `<ncores>` by the number of cores you used in your script.

*   If you want to restart a calculation, delete the file `*.hostnames` (e.g. `benzene.hostnames` in the above example) before you submit the follow-up job. If you do not, the job is likely to fail with the error message `All nodes which are allocated for this job are already filled.`

### Temporary fix to OpenMPI version inconsistency issue (Sep. 6, 2019)

!!! warning "Temporary fix to OpenMPI version inconsistency issue (Sep. 6, 2019)"
    For some type of calculations (DLPNO-STEOM-CCSD in particular), you could receive unknown OpenMPI related fatal errors. This could be due to using an older version of OpenMPI (*i.e.* 3.1.2 as suggested by 'module' for both `orca/4.1.0` and `4.2.0`) than recommended officially (3.1.3 for `orca/4.1.0` and 3.1.4 for `orca/4.2.0`). To temporarily fix this issue, one can build a custom version of OpenMPI.

    The following two commands prepare a custom `openmpi/3.1.4` for `orca/4.2.0`:

    ```bash
    module load gcc/7.3.0
    eb OpenMPI-3.1.2-GCC-7.3.0.eb --try-software-version=3.1.4
    ```

    When the building is finished, you can load the custom OpenMPI using module

    ```bash
    module load openmpi/3.1.4
    ```

    At this step, one can manually install `orca/4.2.0` binaries from the official forum under the home directory after finishing the registration on the official ORCA forum and being granted access to the ORCA program on our clusters.

    Additional notes from the contributor:

    This is a **temporary** fix prior to the official upgrade of OpenMPI on our clusters. Please remember to delete the manually installed ORCA binaries once the official OpenMPI version is up to date.

    The compiling command does not seem to apply to `openmpi/2.1.x`.

## Using NBO with ORCA

To run NBO with ORCA, one needs to have access to NBO. On our clusters, NBO is not available as a separate module. However, it is possible to access it via the Gaussian modules which are installed on [Cedar](../clusters/cedar.md) and [Graham](../clusters/graham.md). Users interested to use NBO with ORCA should have access to ORCA and Gaussian. To get access to Gaussian, you can follow the steps discussed in this [page](gaussian.md#license-agreement).

### Script example

The name of the input file (in this next example *orca_input.inp*) should contain the keyword **NBO**.

/// tab | run_orca-nbo.sh
```bash
#!/bin/bash
#SBATCH --account=def-youPIs
#SBATCH --nodes=1
#SBATCH --ntasks=16
#SBATCH --mem-per-cpu=4000
#SBATCH --time=0-3:00:00

# Load the modules:

module load StdEnv/2020  gcc/10.3.0  openmpi/4.1.1 orca/5.0.4
module load gaussian/g16.c01

export GENEXE=`which gennbo.i4.exe`
export NBOEXE=`which nbo7.i4.exe`

${EBROOTORCA}/orca orca_input.inp > orca_output.out
```

## Related links

*   [ORCA tutorials](https://www.orcasoftware.de/tutorials_orca/)
*   [ORCA Forum](https://orcaforum.kofo.mpg.de/app.php/portal)