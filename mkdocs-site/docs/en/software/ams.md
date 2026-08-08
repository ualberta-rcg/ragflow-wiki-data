---
title: "AMS/en"
slug: "ams"
lang: "en"

source_wiki_title: "AMS/en"
source_hash: "8edab4ed545408612848e783dcc847ef"
last_synced: "2026-08-07T19:46:17.777436+00:00"
last_processed: "2026-08-07T22:06:44.625107+00:00"

tags:
  - software
  - computationalchemistry

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: true
  qa_generated: false
---

## Introduction

AMS (Amsterdam Modeling Suite), originally named [ADF](adf.md) (Amsterdam Density Functional), is the [SCM Software for Chemistry and Materials](https://www.scm.com/). AMS offers powerful computational chemistry tools for many research areas such as homogeneous and heterogeneous catalysis, inorganic chemistry, heavy element chemistry, various types of spectroscopy, and biochemistry.

The full SCM module products are available:

*   ADF
*   ADF-GUI
*   BAND
*   BAND-GUI
*   DFTB
*   ReaxFF
*   COSMO-RS
*   QE-GUI
*   NBO6

## Running AMS on Nibi

The `ams` module is installed on [Nibi](../clusters/nibi.md). The licence is an Academic Computing Centre licence owned by SHARCNET. You may not use the Software for consulting services nor for purposes that have a commercial nature. To check what versions are available, use the `module spider` command as follows:

```bash
module spider ams
```

For module commands, please see [Using modules](../programming/utiliser_des_modules.md).

### Job submission

The clusters use the Slurm scheduler; for details about submitting jobs, see [Running jobs](../running-jobs/running_jobs.md).

#### Example scripts for an AMS job

This `H2O_adf.sh` example script is to request 32 CPUs on one node. Please use a reasonable number of CPUs instead of simply running a full-node job on Nibi, unless you have demonstrated that your job can scale efficiently to 192 CPUs.

```bash title="H2O_adf.sh"
#!/bin/bash
#SBATCH --account=def-pi
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=32          # 32 cpus on 1 node, MPI job
#SBATCH --mem-per-cpu=3G              # memory per cpu
#SBATCH --time=00-01:00               # time (DD-HH:MM)
#SBATCH --output=H2O_adf-%j.log       # output .log file

module unload openmpi
module load ams/2025.102
export SCM_TMPDIR=$SLURM_TMPDIR      # use the local disk
bash H2O_adf.run                    # run the input script
```

This is the input file used in the script:

```sh title="H2O_adf.run"
#!/bin/sh
# This is a shell script for AMS
# You should use '$AMSBIN/ams' instead of '$ADFBIN/adf'

AMS_JOBNAME=H2O_adf $AMSBIN/ams <<eor
   # Input options for the AMS driver:
   System
      Atoms
         O             0.000000     0.000000     0.000000
         H             0.000000    -0.689440    -0.578509
         H             0.000000     0.689440    -0.578509
      End
   End
   Task GeometryOptimization
   GeometryOptimization
      Convergence gradients=1e-4
   End

   # The input options for ADF, which are described in this manual,
   # should be specified in the 'Engine ADF' block:

   Engine ADF
      Basis
         Type TZP
      End
      XC
         GGA PBE
      End
   EndEngine
eor
```

#### Example scripts for a band job

```sh title="SnO_EFG_band.run"
#!/bin/sh
# The calculation of the electric field gradient is invoked by the EFG key block
# Since Sn is quite an heavy atom we use the scalar relativistic option.

$AMSBIN/ams <<eor

Task SinglePoint
System
   FractionalCoords True

   Lattice
      3.8029  0.0  0.0
      0.0  3.8029  0.0
      0.0  0.0  4.8382
   End

   Atoms
      O   0.0  0.0  0.0
      O   0.5  0.5  0.0
      Sn  0.0  0.5  0.2369
      Sn  0.5  0.0 -0.2369
   End
End

Engine Band
   Title SnO EFG
   NumericalQuality Basic      ! Only for speed
   Tails bas=1e-8              ! Only for reproducibility with nr. of cores
   ! useful for Moessbauer spectroscopy: density and coulomb pot. at nuclei
   PropertiesAtNuclei
   End

   EFG
      Enabled True
   End

   Basis
      Type DZ
      Core none
   End
EndEngine
eor
```

### Notes

1.  The input for AMS is different from ADF; the previous ADF input file will not run for the new AMS. Some examples can be found in `/opt/software/ams/2025.102/examples/`
2.  Except for the output `.log` file, other files are all saved in a subdirectory `AMS_JOBNAME.results`. If `AMS_JOBNAME` is not defined in the input `.run` file, the default name is `ams.results`.
3.  The restart file name is `ams.rkf` instead of `TAPE13` in previous ADF versions.

For more usage information, please check the manuals in [SCM Support](https://www.scm.com/support/).

## Running AMS-GUI on Nibi

AMS can be run graphically on Nibi using an OnDemand Compute Node Desktop as follows:

1.  Log into [ondemand.sharcnet.ca](https://ondemand.sharcnet.ca).
2.  Select *Compute Node* then *Compute Desktop* from the top menu pulldown.
3.  Specify Computers=1, Cores=1, GPU=None for visualization then press *Launch*.
4.  Once the Desktop changes from Queued to Running press *Launch Nibi Desktop*.
5.  When your Desktop starts click *Applications* -> *System Tools* -> *MATE Terminal*.
6.  Run the following commands in the terminal:
    ```bash
    module unload openmpi
    module load ams # loads the latest version
    export SCM_OPENGL_SOFTWARE=1 # enables software rendering
    amsinput
    # OR
    amsview
    ```
7.  !!! tip "Using a GPU for AMS-GUI"
    If you specified *GPU=t4 (15GB)* when starting your OnDemand Nibi Desktop, instead use:
    ```bash
    LD_PRELOAD= amsinput
    # OR
    LD_PRELOAD= amsview
    ```

!!! tip "GUI Interaction"
    ▻ To select one or more atoms in the GUI press SHIFT then click.