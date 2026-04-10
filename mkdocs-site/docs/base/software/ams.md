---
title: "AMS"
slug: "ams"
lang: "base"

source_wiki_title: "AMS"
source_hash: "44c9924d46e623666cf7433fb5dac08c"
last_synced: "2026-04-10T14:10:18.226633+00:00"
last_processed: "2026-04-10T14:24:11.782172+00:00"

tags:
  - software
  - computationalchemistry

keywords:
  - "Nibi cluster"
  - "Nibi compute node"
  - "Job submission scripts"
  - "AMS-GUI"
  - "Slurm scheduler"
  - "Atoms"
  - "Engine Band"
  - "EFG"
  - "Computational chemistry"
  - "OnDemand"
  - "SnO"
  - "Amsterdam Modeling Suite"
  - "amsinput"
  - "Moessbauer spectroscopy"
  - "AMS"

questions:
  - "What is the Amsterdam Modeling Suite (AMS) and what specific research areas and modules does it encompass?"
  - "What are the licensing restrictions for using AMS on the Nibi cluster, and how can users check for available versions?"
  - "How are AMS jobs submitted using the Slurm scheduler, and what key configurations are demonstrated in the provided example scripts?"
  - "What are the main differences in input formats, output directories, and restart file names between the new AMS and previous ADF versions?"
  - "What is the step-by-step process for launching the AMS-GUI interactively on a Nibi compute node via OnDemand?"
  - "What are the specific usage policies and VirtualGL workarounds when using the OnDemand Nibi Desktop for AMS applications?"
  - "What specific chemical system and atomic coordinates are being defined in the \"Atoms\" section of the text?"
  - "What computational parameters are specified for the engine, and why are the numerical quality and tails set to these specific values?"
  - "According to the text, what type of spectroscopy is this calculation useful for, and what specific physical properties are being evaluated at the nuclei?"
  - "What are the main differences in input formats, output directories, and restart file names between the new AMS and previous ADF versions?"
  - "What is the step-by-step process for launching the AMS-GUI interactively on a Nibi compute node via OnDemand?"
  - "What are the specific usage policies and VirtualGL workarounds when using the OnDemand Nibi Desktop for AMS applications?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Introduction
AMS (Amsterdam Modeling Suite), originally named [ADF](adf.md), is the [SCM Software for Chemistry and Materials](https://www.scm.com/). AMS offers powerful computational chemistry tools for many research areas such as homogeneous and heterogeneous catalysis, inorganic chemistry, heavy element chemistry, various types of spectroscopy, and biochemistry.

The full SCM module products are available:
* ADF
* ADF-GUI
* BAND
* BAND-GUI
* DFTB
* ReaxFF
* COSMO-RS
* QE-GUI
* NBO6

## Running AMS on Nibi
The `ams` module is installed on [Nibi](nibi.md). The license is an Academic Computing Centre license owned by SHARCNET. You may not use the Software for consulting services nor for purposes that have a commercial nature. To check what versions are available, use the `module spider` command as follows:

```bash
name@server $ module spider ams
```

For module commands, please see [Using modules](utiliser-des-modules.md).

### Job submission

The clusters use the Slurm scheduler; for details about submitting jobs, see [running-jobs.md].

#### Example scripts for an AMS job
This `H2O_adf.sh` example script is to request 32 CPUs on one node. Please use a reasonable number of CPUs instead of simply running a full-node job on Nibi, unless you have demonstrated that your job can scale efficiently to 192 CPUs.

```bash H2O_adf.sh
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

```text H2O_adf.run
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

```bash SnO_EFG_band.run
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
1. The input for AMS is different from ADF, the previous ADF input file will not run for the new AMS. Some examples can be found in `/opt/software/ams/2025.102/examples/`
2. Except the output `.log` file, other files are all saved in a subdirectory `AMS_JOBNAME.results`. If `AMS_JOBNAME` is not defined in the input `.run` file, the default name is `ams.results`.
3. The restart file name is `ams.rkf` instead of the `TAPE13` in previous ADF versions.
For more usage information, please check the manuals in [SCM Support](https://www.scm.com/support/)

## Running AMS-GUI
### Nibi

AMS can be run interactively in graphical mode on a Nibi compute node (8hr time limit) via OnDemand with these steps:

1. Log in to [ondemand.sharcnet.ca](https://ondemand.sharcnet.ca)
2. Select *Nibi Desktop* from *Compute* on the top
3. Select your options (select 1 core for visualization purpose, don't select *Enable VirtualGL*) and press *Launch*
4. Select *Launch Nibi Desktop* once your job starts
5. Right-click on the desktop and pick *Open it Terminal*
6. Pick *MATE Terminal* from the *System Tools* menu under the *Applications* menu
7. `module unload openmpi`
8. `module load ams`
9. `amsinput &` (to make AMS input)
10. `amsview &` (for AMS result visualization)

If you need to select *Enable VirtualGL* for some other program that you are using, you will have to disable it for just AMS by starting it with `LD_PRELOAD= amsinput`.

!!! warning "Usage Guidelines"
    OnDemand Nibi Desktop is intended for AMS-GUI applications, such as making input files and visualizing results. Please do not use it to run regular jobs or long interactive jobs. Select a single core and reasonable memory and runtime.