---
title: "OpenFOAM"
slug: "openfoam"
lang: "base"

source_wiki_title: "OpenFOAM"
source_hash: "3c3df249dcfc533c77de17373d05cb3b"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:00:33.844941+00:00"

tags:
  - software

keywords:
  - "petscFoam solver"
  - "Compile"
  - "submission script"
  - "petsc/3.21.6"
  - "computational fluid dynamics"
  - "node-local scratch"
  - "bugfixes"
  - "module files"
  - "OpenFOAM"
  - "PETSc 3.21.2"
  - "openfoam/v2412"
  - "release branch"
  - "Performance"

questions:
  - "What is the OpenFOAM software package and what types of computational problems is it used to solve?"
  - "How do users properly set up their environment and submit serial or parallel OpenFOAM jobs using Slurm scripts?"
  - "How can a user determine the compatible version of the PETSc library for a specific release of OpenFOAM?"
  - "What are the necessary steps and commands to download, extract, and compile the petscFoam solver?"
  - "How can a user confirm that the petscFoam solver is functional and its dynamic library dependencies are correctly linked?"
  - "What methods can be implemented to improve OpenFOAM's performance and reduce the impact of frequent debug file writes on shared filesystems?"
  - "What command is used to find the PETSc version associated with the openfoam/v2412 module?"
  - "Which specific version of PETSc was openfoam/v2412 originally tested with?"
  - "Why is the petsc/3.21.6 module considered a suitable alternative to the originally tested version?"
  - "What are the necessary steps and commands to download, extract, and compile the petscFoam solver?"
  - "How can a user confirm that the petscFoam solver is functional and its dynamic library dependencies are correctly linked?"
  - "What methods can be implemented to improve OpenFOAM's performance and reduce the impact of frequent debug file writes on shared filesystems?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

The [OpenFOAM](https://www.openfoam.com/) (Open Field Operation and Manipulation) CFD Toolbox is a free, open-source software package for computational fluid dynamics. OpenFOAM has an extensive range of features to solve anything from complex fluid flows involving chemical reactions, turbulence, and heat transfer, to solid dynamics and electromagnetics.

## Module files
To load the recent version, run:
```bash
module load openfoam
```

The OpenFOAM development community consists of:
*   The OpenFOAM Foundation Ltd., with websites [openfoam.org](https://openfoam.org/) and [cfd.direct](https://cfd.direct/)
*   OpenCFD Ltd., with website [openfoam.com](https://www.openfoam.com/)
Up to version 2.3.1, released in December 2014, the release histories appear to be the same. On our clusters, module names after 2.3.1 which begin with "v" are derived from the .com branch (for example, `openfoam/v1706`); those beginning with a digit are derived from the .org branch (for example, `openfoam/4.1`).

See [Using modules](using-modules.md) for more on module commands.

## Documentation
[OpenFOAM.com documentation](https://www.openfoam.com/documentation/) and [CFD Direct user guide](https://cfd.direct/openfoam/user-guide/).

## Usage
OpenFOAM requires substantial preparation of your environment. In order to run OpenFOAM commands (such as `paraFoam`, `blockMesh`, etc.), you must load a [module file](using-modules.md).

Here is an example of a serial submission script for OpenFOAM 5.0:
```bash linenums="1" title="submit.sh"
#!/bin/bash
#SBATCH --time=00:01:00
#SBATCH --account=def-someuser

module purge
module load openfoam/12

blockMesh
icoFoam
```

Here is an example of a parallel submission script:
```bash linenums="1" title="submit.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --ntasks=4               # number of MPI processes
#SBATCH --mem-per-cpu=1024M      # memory; default unit is megabytes
#SBATCH --time=0-00:10           # time (DD-HH:MM)

module purge
module load openfoam/12

blockMesh
setFields
decomposePar
srun interFoam -parallel
```

Mesh preparation (`blockMesh`) may be fast enough to be done at the command line (see [Running jobs](../running-jobs/running_jobs.md)). The solver (`icoFoam` and others) is usually the most expensive step and should always be submitted as a Slurm job except in very small test cases or tutorials.

## petscFoam solver
OpenFOAM can be compiled with the external petscFoam solver. Our OpenFOAM modules don't include this solver, but it can easily be compiled on any of our clusters.

The versions of OpenFOAM and PETSc need to be compatible. Compatible combinations are, for example:

*   `openfoam/v2412` and `petsc/3.21.6`
*   `openfoam/v2312` and `petsc/3.20.0`

### Determine compatible versions of OpenFOAM and PETSc
To check which minor release of PETSc is compatible with a particular version of OpenFOAM, load the desired module of OpenFOAM and run the following `grep` command:

```bash
module load openfoam/v2412 && grep "^petsc_version"  $EBROOTOPENFOAM/OpenFOAM*/etc/config.sh/petsc
```
```text
petsc_version=petsc-3.21.2
```

This tells us that when `openfoam/v2412` was released, it was tested with PETSc 3.21.2.

We have a module for `petsc/3.21.6`, which is from the same 3.21 release branch and should only contain bugfixes compared to 3.21.2.

### Compile petscFoam solver
Next, we need to download and extract the `external-solver-main.tar.gz` package.
```bash
module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 openfoam/v2412 petsc/3.21.6
wget https://develop.openfoam.com/modules/external-solver/-/archive/main/external-solver-main.tar.gz
tar xvfz external-solver-main.tar.gz
cd external-solver-main
```

Running `./Allwmake` will compile the petscFoam solver:
```bash
./Allwmake
```
```text
========================================
2025-08-14 15:00:00 -0400
Starting compile of external-solver (petsc) with OpenFOAM-v2412
[...]
========================================
  Finished compile of external-solver (petsc) with OpenFOAM-v2412
  Gcc system compiler
  linux64GccDPInt32Opt, with EASYBUILDMPI eb-mpi
```

### Confirm that petscFoam solver is functional
A few quick tests will confirm that petscFoam solver is working:

Check whether OpenFOAM can load petscFoam:
```bash
foamHasLibrary -verbose petscFoam
```
```text
Can load "petscFoam"
```

Check whether the dynamic library is located in `$FOAM_USER_LIBBIN`:
```bash
ls $FOAM_USER_LIBBIN
```
```text
libpetscFoam.so
```

Check whether `libpetscFoam.so` can find its dependencies:
```bash
ldd $FOAM_USER_LIBBIN/libpetscFoam.so | grep petsc
```
```text
 libpetsc.so.3.21 => /cvmfs/soft.computecanada.ca/easybuild/software/2023/x86-64-v4/MPI/gcc12/openmpi4/petsc/3.21.6/lib/libpetsc.so.3.21 (0x00007f96fa800000)
 libstrumpack.so.7.2 => /cvmfs/soft.computecanada.ca/easybuild/software/2023/x86-64-v4/MPI/gcc12/openmpi4/petsc/3.21.6/lib/libstrumpack.so.7.2 (0x00007f96f8200000)
 libml.so.13 => /cvmfs/soft.computecanada.ca/easybuild/software/2023/x86-64-v4/MPI/gcc12/openmpi4/petsc/3.21.6/lib/libml.so.13 (0x00007f96fa281000)
```

## Performance
OpenFOAM can emit a lot of debugging information in very frequent small writes (e.g., hundreds per second). This may lead to poor performance on our shared filesystems. If you are in stable production and don't need the debug output, you can reduce or disable it with:
```bash
mkdir -p $HOME/.OpenFOAM/$WM_PROJECT_VERSION
cp $WM_PROJECT_DIR/etc/controlDict $HOME/.OpenFOAM/$WM_PROJECT_VERSION/
```
There are a variety of other parameters which can be used to reduce the amount of output that OpenFOAM writes to disk, as well as the frequency; these run-time parameters are documented for [version 6](https://cfd.direct/openfoam/user-guide/v6-controldict/) and [version 7](https://cfd.direct/openfoam/user-guide/v7-controldict/).

For example, the `debugSwitches` dictionary in `$HOME/.OpenFOAM/$WM_PROJECT_VERSION/controlDict` can be altered to change the flags from values greater than zero to zero. Another solution would be to make use of the local scratch (`$SLURM_TMPDIR`), a disk attached directly to the compute node, discussed [here](../storage-and-data/handling_large_collections_of_files.md#local_disk).

### Node-local scratch

!!! tip "Node-local scratch for performance"
    If your workflow involves the creation of many small files, you may benefit from making `$SLURM_TMPDIR` your working directory. See [Using node-local storage](../storage-and-data/using_node-local_storage.md) for more on this.