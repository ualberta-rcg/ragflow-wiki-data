---
title: "Dalton/en"
slug: "dalton"
lang: "en"

source_wiki_title: "Dalton/en"
source_hash: "38711e3bfc45ca8606b6f7d3af1222b0"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T05:57:00.683144+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

## Introduction

The kernel of the Dalton2016 suite is the two powerful molecular electronic structure programs, Dalton and LSDalton. Together, the two programs provide extensive functionality for the calculations of molecular properties at the HF, DFT, MCSCF, and CC levels of theory. Many of these properties are only available in the Dalton2016 suite.

*   Project web site: [http://daltonprogram.org/](http://daltonprogram.org/)
*   Documentation: [http://daltonprogram.org/documentation/](http://daltonprogram.org/documentation/)
*   Forum: [http://forum.daltonprogram.org/](http://forum.daltonprogram.org/)

## Modules

```bash
$ module load nixpkgs/16.09 intel/2016.4 openmpi/2.0.2 dalton/2017-alpha
```

!!! note
    Notice that `dalton/2017-alpha` depends on a non-default version of Open MPI. For more on the `module` command, see [Using modules](utiliser-des-modules-fr.md).

## Usage

Here is an example:

*   Dalton input file: `dft_rspexci_nosym.dal` (see the examples below).
*   Molecule specification: `H2O_cc-pVDZ_nosym.mol` (see the examples below).
*   To use the atomic basis set installed with the program, supply option `-b ${BASLIB}` to the command line (see the examples below).
*   The number of processes can be set using a command line option or an environment variable:
    *   Add the option `-N ${SLURM_NTASKS}` to the launcher command line (refer to **Script 1** in the examples below);
    *   or, `export DALTON_NUM_MPI_PROCS=${SLURM_NTASKS}` (refer to **Script 2** in the examples below).

To run Dalton, load the module and use the launcher `dalton`:

```bash
dalton -b ${BASLIB} -N ${SLURM_NTASKS} -dal dft_rspexci_nosym.dal -mol H2O_cc-pVDZ_nosym.mol
```

or

```bash
export DALTON_NUM_MPI_PROCS=${SLURM_NTASKS}
dalton -b ${BASLIB} -dal dft_rspexci_nosym.dal -mol H2O_cc-pVDZ_nosym.mol
```

## Examples: scripts and input files

### Example 1: dft_rspexci_nosym

=== "INPUT"
    ```txt title="dft_rspexci_nosym.dal"
    **DALTON INPUT
    .RUN RESPONSE
    **INTEGRALS
    .PROPRINT
    **WAVE FUNCTIONS
    .DFT
     B3LYP
    **RESPONSE
    *LINEAR
    .SINGLE RESIDUE
    .ROOTS
     3
    **END OF DALTON INPUT
    ```

=== "MOLECULE"
    ```txt title="H2O_cc-pVDZ_nosym.mol"
    BASIS
    cc-pVDZ
    H2O

        2    0
            8.    1
    O     0.0  0.0000000000 0.0
            1.    2
    H1    1.430    0.0  1.1
    H2   -1.430    0.0  1.1
    ```

=== "Script 1"
    ```bash title="run_dalton_job.sh"
    #!/bin/bash

    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=4
    #SBATCH --mem-per-cpu=3500M
    #SBATCH --time=00-30:00

    # Load the module:

    module load nixpkgs/16.09 intel/2016.4 openmpi/2.0.2 dalton/2017-alpha

    # Setting the variables:

    dltonlaun=dalton
    dltonexec=dalton.x
    daltoninput=dft_rspexci_nosym.dal
    daltonmol=H2O_cc-pVDZ_nosym.mol

    echo "Starting run at: `date`"

    echo "Running the example: INPUT=${daltoninput} - Molecule=${daltonmol}"

    ${dltonlaun} -b ${BASLIB} -N ${SLURM_NTASKS} -dal ${daltoninput} -mol ${daltonmol}

    echo "Program finished with exit code $? at: `date`"
    ```

=== "Script 2"
    ```bash title="run_dalton_job.sh"
    #!/bin/bash

    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=2
    #SBATCH --mem-per-cpu=3500M
    #SBATCH --time=00-30:00

    # Load the module:

    module load nixpkgs/16.09 intel/2016.4 openmpi/2.0.2 dalton/2017-alpha

    # Setting the variables:

    dltonlaun=dalton
    dltonexec=dalton.x
    daltoninput=dft_rspexci_nosym.dal
    daltonmol=H2O_cc-pVDZ_nosym.mol

    # Set the number of cores DALTON_NUM_MPI_PROCS to ${SLURM_NTASKS}

    export DALTON_NUM_MPI_PROCS=${SLURM_NTASKS}

    echo "Starting run at: `date`"

    echo "Running the example: INPUT=${daltoninput} - Molecule=${daltonmol}"

    ${dltonlaun} -b ${BASLIB} -dal ${daltoninput} -mol ${daltonmol}

    echo "Program finished with exit code $? at: `date`"
    ```

### Example 2: dft_rspexci_sym.dal

=== "INPUT"
    ```txt title="dft_rspexci_sym.dal"
    **DALTON INPUT
    .RUN RESPONSE
    **INTEGRALS
    .PROPRINT
    **WAVE FUNCTIONS
    .DFT
     B3LYP
    **RESPONSE
    *LINEAR
    .SINGLE RESIDUE
    **END OF DALTON INPUT
    ```

=== "MOLECULE"
    ```txt title="H2O_cc-pVDZ_sym.mol"
    BASIS
    cc-pVDZ
    H2O

        2
            8.    1
    O     0.0  0.0000000000 0.0
            1.    2
    H1    1.430    0.0  1.1
    H2   -1.430    0.0  1.1
    ```

=== "Script 1"
    ```bash title="run_dalton_job.sh"
    #!/bin/bash

    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=4
    #SBATCH --mem-per-cpu=3500M
    #SBATCH --time=00-30:00

    # Load the module:

    module load nixpkgs/16.09 intel/2016.4 openmpi/2.0.2 dalton/2017-alpha

    # Setting the variables:

    dltonlaun=dalton
    dltonexec=dalton.x
    daltoninput=dft_rspexci_sym.dal
    daltonmol=H2O_cc-pVDZ_sym.mol

    echo "Starting run at: `date`"

    echo "Running the example: INPUT=${daltoninput} - Molecule=${daltonmol}"

    ${dltonlaun} -b ${BASLIB} -N ${SLURM_NTASKS} -dal ${daltoninput} -mol ${daltonmol}

    echo "Program finished with exit code $? at: `date`"
    ```

=== "Script 2"
    ```bash title="run_dalton_job.sh"
    #!/bin/bash

    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=4
    #SBATCH --mem-per-cpu=3500M
    #SBATCH --time=00-30:00

    # Load the module:

    module load nixpkgs/16.09 intel/2016.4 openmpi/2.0.2 dalton/2017-alpha

    # Setting the variables:

    dltonlaun=dalton
    dltonexec=dalton.x
    daltoninput=dft_rspexci_sym.dal
    daltonmol=H2O_cc-pVDZ_sym.mol

    # Set the number of cores DALTON_NUM_MPI_PROCS to ${SLURM_NTASKS}

    export DALTON_NUM_MPI_PROCS=${SLURM_NTASKS}

    echo "Starting run at: `date`"

    echo "Running the example: INPUT=${daltoninput} - Molecule=${daltonmol}"

    ${dltonlaun} -b ${BASLIB} -dal ${daltoninput} -mol ${daltonmol}

    echo "Program finished with exit code $? at: `date`"