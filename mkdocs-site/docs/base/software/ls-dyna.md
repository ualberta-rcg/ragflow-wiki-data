---
title: "LS-DYNA"
slug: "ls-dyna"
lang: "base"

source_wiki_title: "LS-DYNA"
source_hash: "04c02b2c53edef8abf1317cc22d5fd66"
last_synced: "2026-10-04T02:27:33.201522+00:00"
last_processed: "2026-10-04T03:05:55.457187+00:00"

tags:
  - software

keywords:
  - "ls-dyna/12.2.1"
  - "intel/2025.2.0"
  - "ANSYSLMD_LICENSE_FILE"
  - "SBATCH"
  - "SHARCNET Ansys license"
  - "LS-PrePost"
  - "~/.licenses/ls-dyna.lic"
  - "ls-dyna-mpp"
  - "Ansys"
  - "LSTC_LICENSE"
  - "ifort160_avx2_openmpi405_sharelib"
  - "ANSYS License Server"
  - "VncViewer"
  - "STC license server"
  - "multiple node jobs"
  - "LSTC license server"
  - "slurm script"
  - "AVX512"
  - "ls-dyna-mpp/17.2.0"
  - "ls-dyna"
  - "LS-DYNA"
  - "floating license"
  - "ls-dyna-mpi"
  - "touch ~/.licenses/ls-dyna.lic"
  - "airbag problem"
  - "OnDemand"
  - "LSTC_MEMORY=AUTO"
  - "memory setting for slurm"
  - "module load"
  - "ls-dyna-mpi/12.2.1"
  - "SLURM script"
  - "single precision"
  - "double precision"
  - "scaling test"
  - "single node SMP LS-DYNA"
  - "full production runs"
  - "memory-per-cpu"
  - "module load StdEnv/2020"
  - "scaling test jobs"
  - "SLURM"
  - "LSTC_LICENSE=ansys"
  - "memGB"

questions:
  - "What types of simulations can LS‑DYNA be used for on the Alliance clusters?"
  - "How can a user configure a LS‑DYNA license that runs on a LSTC license server versus an Ansys license server?"
  - "What steps are required to test and set up a new floating license server for LS‑DYNA on the clusters?"
  - "What role does the `~/.licenses/ls-dyna.lic` file play in loading the `ls-dyna` or `ls-dyna-mpi` modules?"
  - "How should you create or verify the existence of this license file on each cluster before submitting jobs?"
  - "Where can you find the official documentation for further details on the STC license server setup?"
  - "What environment variables need to be exported in a Slurm script to use an ANSYS LS‑DYNA license, and why must a `~/.licenses/ls-dyna.lic` file exist?"
  - "Which LS‑DYNA job types are allowed by the SHARCNET ANSYS license, and what are the current core and simultaneous‑job limits for researchers?"
  - "How should memory be set in a single‑node LS‑DYNA Slurm script, and what effect does the `LSTC_MEMORY=AUTO` option have on implicit versus explicit analyses?"
  - "How is the memory setting for Slurm calculated by multiplying by 25%?"
  - "What are the formulas for converting the memory parameter value to mega words for double‑precision and single‑precision solutions?"
  - "Which Slurm directives are specified in the example `script-smp.sh` to set the account, time limit, number of CPUs, and total memory?"
  - "How should memory be allocated for the master node when using the MPP version of LS‑DYNA on multiple nodes?"
  - "What are the differences between the single‑node and multi‑node LS‑DYNA modules, and how are they loaded in the SLURM scripts?"
  - "How can the number of compute nodes or total cores be specified in a SLURM submission script for LS‑DYNA, and which SBATCH directives are required?"
  - "How do you choose and set the correct LS‑DYNA solver (single vs double precision) and module version for different clusters such as Narval versus AVX‑512 enabled systems?"
  - "What SLURM options must be specified in the script to control the number of cores, memory per CPU, and optional node constraints for an LS‑DYNA MPP job?"
  - "Why should scaling tests be run before large production runs, and which commands or tools can be used to assess job wall‑clock time, CPU efficiency, and memory efficiency?"
  - "Which Intel compiler version is loaded by the script, and on which clusters is it unavailable?"
  - "What is the purpose of the commented lines that reference `LSTC_LICENSE=ansys`?"
  - "Which LS‑DYNA module and version are loaded, and how does it relate to the other module specifications?"
  - "Which cluster and LS‑Dyna module configuration should be used for reliable scaling tests of the airbag problem?"
  - "Why were the previous scaling tests (using only 6 cores on a single node or 6 cores across two nodes) considered inadequate for predicting production performance?"
  - "How should scaling tests be performed to accurately reflect the actual research simulation and the cluster where full production runs will be executed?"
  - "What is LS‑PrePost, and why does it not require a separate license for use with LS‑DYNA models?"
  - "Which steps and URLs are required to run Abaqus graphically through the recommended OnDemand desktop approach?"
  - "How can a VncViewer client be used to access LS‑PrePost on a remote login or compute node, and what module commands must be executed afterward?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: false
  qa_generated: false
---

# LS-DYNA

## Introduction
[LS-DYNA](http://www.lstc.com) is available on all our clusters. It is used for many [applications](http://www.lstc.com/applications) to solve problems in multiphysics, solid mechanics, heat transfer, and fluid dynamics. Analyses are performed as separate phenomena or coupled physics simulations such as thermal stress or fluid structure interaction. LSTC was recently purchased by Ansys, so the LS-DYNA software may eventually be exclusively provided as part of the Ansys module. For now, we recommend using the LS-DYNA software traditionally provided by LSTC as documented in this wiki page.

## Licensing
The Alliance is a hosting provider for LS-DYNA, which means LS-DYNA software is installed as modules on the clusters. The Alliance does NOT, however, provide a free LS-DYNA license or provide LS-DYNA license hosting services. Instead, many institutions, faculties, and departments already have licenses that can be used on our clusters. If a local license is not available, then SHARCNET provides a limited number of free licenses on a first-come, first-served basis to any researcher as described below.

### Initial setup and testing

If a license server has never been used on a cluster, firewall changes will first need to be done on both the cluster side and server side. This will typically require involvement from both our technical team and the technical people managing your license software. To arrange this, send an email containing the service port and IP address of your floating license server to [technical support](../support/technical_support.md). To check if your license file is working with a legacy LSTC server or ANSYS server, you may run the following commands:

```bash
touch ~/.licenses/ls-dyna.lic
module load ls-dyna
export LSTC_LICENSE=network|ansys
export LSTC_LICENSE_SERVER=<port>@<server>, or
export ANSYSLMD_LICENSE_FILE=<port>@<server>
ls-dyna_s, or ls-dyna_d
```

You don't need to specify any input file or arguments to run this test. The output header should contain a (non-empty) value for `Licensed to:`. Press ^C to quit the program and return to the command line.

## Configuring your license

In 2019, Ansys purchased the Livermore Software Technology Corporation (LSTC), developer of LS-DYNA. LS-DYNA licenses issued by Ansys since that time use **Ansys license servers**. Legacy LSTC licenses that run on **LSTC license servers** are now available from ANSYS. This section explains how to configure your job script for each of these cases.

### LSTC license

If you have a license issued to run on a LSTC license server, there are two options to specify it:

Option 1) Specify your license server by creating a small file named `ls-dyna.lic` with the following contents:

```bash title="ls-dyna.lic"
#LICENSE_TYPE: network
#LICENSE_SERVER:<port>@<server>
```

where `<port>` is an integer number and `<server>` is the hostname of your LSTC license server. Put this file in directory `$HOME/.licenses/` on each cluster where you plan to submit jobs. The values in the file are picked up by LS-DYNA when it runs. This occurs because our module system sets the LSTC_FILE variable to `LSTC_FILE=/home/$USER.licenses/ls-dyna.lic` whenever you load a `ls-dyna` or `ls-dyna-mpi` module. This approach is recommended for users with a license hosted on a LSTC license server since (compared to the next option) the identical settings will automatically be used by all jobs you submit on the cluster (without the need to specify them in each individual slurm script or setting them in your environment).

Option 2) Specify your license server by setting the following two environment variables in your slurm scripts:
`export LSTC_LICENSE=network`
`export LSTC_LICENSE_SERVER=<port>@<server>`
where `<port>` is an integer number and `<server>` is the hostname or IP address of your LSTC license server. These variables will take priority over any values specified in your `~/.licenses/ls-dyna.lic` file, which must exist (even if it's empty) for any `ls-dyna` or `ls-dyna-mpi` module to successfully load. To ensure it exists, run `touch ~/.licenses/ls-dyna.lic` once on the command line on each cluster where you will submit jobs. For further details, see the official [documentation](https://lsdyna.ansys.com/download-install-overview/).

### ANSYS license

If your LS-DYNA license is hosted on an Ansys license server, set the following two environment variables in your slurm scripts:
`export LSTC_LICENSE=ansys`
`export ANSYSLMD_LICENSE_FILE=<port>@<server>`
where `<port>` is an integer number and `<server>` is the hostname or IP address of your Ansys license server. These variables cannot be defined in your `~/.licenses/ls-dyna.lic` file. The file, however, must exist (even if it's empty) for any `ls-dyna` module to load. To ensure this, run `touch ~/.licenses/ls-dyna.lic` once from the command line (or each time in your slurm scripts). Note that only module versions >= 12.2.1 will work with Ansys license servers.

**SHARCNET**

The SHARCNET Ansys license supports running **single node** SMP or MPP LS-DYNA jobs with many cores using the included `dysmp` license feature. The SHARCNET Ansys license, however, does NOT support running **multi-node** distributed memory MPP LS-DYNA jobs since it lacks the required `mppdyna` feature. Any researcher from the Alliance can freely use the SHARCNET license to run up to 5 simultaneous lsdyna jobs with 288 cores without any internal software limits such as those present in the student or teaching licenses. These limits may be changed depending on the license load to optimize reliable availability and will be updated here at such time. For example, a researcher can currently submit and run a 192 core single full node job and a 96 core half node job using an unlimited mesh size. The SHARCNET license may only be used for the purpose of Academic research and associated publications. To utilize the SHARCNET license on the cluster to run LS-DYNA jobs, include the following lines in your slurm script:
`export LSTC_LICENSE=ansys`
`export ANSYSLMD_LICENSE_FILE=1055@license1.computecanada.ca`

## Cluster job submission

LS-DYNA provides binaries for running jobs on a single compute node (SMP - Shared Memory Parallel using OpenMP) or across multiple compute nodes (MPP - Message Passing Parallel using MPI). This section provides slurm scripts for each job type.

## Single node jobs

Modules for running jobs on a single compute node can be listed with: `module spider ls-dyna`. Jobs may be submitted to the queue with: `sbatch script-smp.sh`. The following slurm script shows how to run LS-DYNA with 8 cores on a single compute node. Regarding the AUTO option of the LSTC_MEMORY [environment variable](https://www.dynasupport.com/howtos/general/environment-variables), this setting allows memory to be dynamically extended beyond the specified `memory=1500M` word setting where it is suitable for explicit analysis such as metal forming simulations but not crash analysis. Given there are 4 Bytes/word for the single precision solver and 8 Bytes/word for the double precision solver, the 1500M setting in the slurm script example below equates to either 1) a maximum amount of (1500Mw*8Bytes/w) = 12GB memory before LS-DYNA self-terminates when solving an implicit problem or 2) a starting amount of 12GB memory prior to extending it (up 25% if necessary) when solving an explicit problem assuming `LSTC_MEMORY=AUTO` is uncommented. Note that 12GB represents 75% of the total mem=16GB reserved for the job and is considered ideal for implicit jobs on a single node. To summarize, for both implicit and explicit analysis, once an estimate for the total solver memory is determined in GB, the total memory setting for slurm can be determined by multiplying by 25% while the memory parameter value in mega words can be calculated as (0.75*memGB/8Bytes/w)*1000M and (0.75*memGB/4Bytes/w)*1000M for double and single precision solutions respectively.

```bash title="script-smp.sh"
#!/bin/bash
#SBATCH --account=def-account   # Specify
#SBATCH --time=0-03:00          # D-HH:MM
#SBATCH --cpus-per-task=8       # Specify number of cores
#SBATCH --mem=16G               # Specify total memory
#SBATCH --nodes=1               # Do not change

module load StdEnv/2023         # Version 12.2.1 :
module load intel/2023.2.1      # available on all clusters,
module load ls-dyna/12.2.1      # uses ifort160_sse2 smp binary

# Uncomment next two lines to use an ANSYS License Server
#export LSTC_LICENSE=ansys                   # Do not change this setting
#export ANSYSLMD_LICENSE_FILE=PORT@HOSTNAME  # Specify PORT and HOSTNAME

#export LSTC_MEMORY=AUTO        # Optional for explicit only

INPUTFILE="airbag.deploy.k"     # Specify an input filename
SMPSOLVER="ls-dyna_d"           # Specify ls-dyna_s OR ls-dyna_d

$SMPSOLVER ncpu=$SLURM_CPUS_ON_NODE i=$INPUTFILE memory=1500M
```

where
* `ls-dyna_s` = single precision smp solver
* `ls-dyna_d` = double precision smp solver

## Multiple node jobs

There are several modules installed for running jobs on multiple nodes using the MPP (Message Passing Parallel) version of LS-DYNA. The method is based on mpi and can scale to very many cores (8 or more). The modules may be listed by running `module spider ls-dyna-mpi`. Sample slurm scripts below demonstrate how to use these modules for submitting jobs to a specified number of whole nodes *OR* a specified total number of cores using `sbatch script-mpp-bynode.sh` or `sbatch script-mpp-bycore.sh` respectively. The MPP version requires a sufficiently large enough amount of memory (memory1) for the first core (processor 0) on the master node to decompose and simulate the model. This amount may be satisfied by specifying a value of `mem-per-cpu` to slurm slightly larger than the memory (memory2) required per core for simulation and then placing enough cores on the master node such that their differential sum (`mem-per-cpu` less memory2) is greater than or equal to memory1. Similar to the single node model, for best results, keep the sum of all expected memory per node within 75% of the reserved ram on a node. Thus in the first script below, assuming a 128GB full node memory compute node, memory1 maybe 6000M (48GB) maximum and memory2 200M (48GB/31cores).

### Specify node count

Jobs can be submitted to a specified number of **whole** compute nodes with the following script. Please note naming of the modules has changed from ls-dyna-mpi to ls-dyna-mpp for all versions >= 13.2.0 in the below script as well these modules use avx512 and sharelib binaries.

```bash title="script-mpp-bynode.sh"
#!/bin/bash
#SBATCH --account=def-account    # Specify
#SBATCH --time=0-03:00           # D-HH:MM
#SBATCH --ntasks-per-node=192    # Specify all cores per node (narval/nibi/fir/trillium 192, narval 64)
#SBATCH --mem=0                  # Set to 0 to use all memory per compute node
#SBATCH --nodes=1                # Specify number of compute nodes (1 or more)
##SBATCH --constraint=granite    # Uncomment to specify a cluster specific node type

#module load StdEnv/2023          # Versions 12.2.1, 12.2.2 :
#module load intel/2023.2.1       # available on all clusters,
#module load ls-dyna-mpi/12.2.1   # 12.2.1 uses ifort160_avx2_openmpi405 binary
#module load ls-dyna-mpi/12.2.2   # 12.2.2 uses ifort160_avx2_openmpi405_sharelib
# -----------------------------
module load StdEnv/2023           # Versions 13.2.0, 14.2.0, 15.0.2, 16.2.0, 17.2.0 :
module load intel/2025.2.0        # available on all clusters except narval,
module load ls-dyna-mpp/17.2.0    # all versions ifort190_avx512_openmpi405_sharelib

# Uncomment next two lines to use an ANSYS License Server
#export LSTC_LICENSE=ansys                   # Do not change this setting
#export ANSYSLMD_LICENSE_FILE=PORT@HOSTNAME  # Specify PORT and HOSTNAME

#export LSTC_MEMORY=AUTO          # Optional for explicit only

INPUTFILE="airbag.deploy.k"       # Specify an input filename
MPPSOLVER="ls-dyna_d"             # Specify ls-dyna_s OR ls-dyna_d

srun $MPPSOLVER i=$INPUTFILE memory=200M
```

where
* `ls-dyna_s` = single precision mpp solver
* `ls-dyna_d` = double precision mpp solver

note
To use version 12.2.1 or 12.2.2 on Narval, the above script will likely need to be modified to run jobs under `$SLURM_TMPDIR` otherwise performance may be ~100x slower than other clusters. Narval only has lsdyna modules for 12.2.1 and 12.2.2 installed on it since all of its servers are legacy AVX2 based. Newer versions have been installed using AVX512 binaries and are therefore only available on other clusters.

### Specify core count

Jobs can be submitted to an arbitrary number of compute nodes by specifying the number of cores. This approach allows the scheduler to determine the optimal number of compute nodes to minimize job wait time in the queue. Memory limits are applied per core; therefore, a sufficiently large value of `mem-per-cpu` must be specified so the master processor can successfully decompose and handle its computations as explained in more detail in the opening paragraph of this section. Please note the naming of the modules has changed from ls-dyna-mpi to ls-dyna-mpp for all versions >= 13.2.0 in the below script as well these modules use avx512 and sharelib binaries.

```bash title="script-mpp-bycore.sh"
#!/bin/bash
#SBATCH --account=def-account     # Specify
#SBATCH --time=0-03:00            # D-HH:MM
#SBATCH --ntasks=64               # Specify any total number of cores
#SBATCH --mem-per-cpu=2G          # Specify memory per core
##SBATCH --nodes=1                # Uncomment to specify number of compute nodes (1 or more)
##SBATCH --constraint=granite     # Uncomment to specify a cluster specific node type

#module load StdEnv/2023          # Versions 12.2.1, 12.2.2 :
#module load intel/2023.2.1       # available on all clusters,
#module load ls-dyna-mpi/12.2.1   # 12.2.1 uses ifort160_avx2_openmpi405 binary
#module load ls-dyna-mpi/12.2.2   # 12.2.2 uses ifort160_avx2_openmpi405_sharelib
# -----------------------------
module load StdEnv/2023           # Versions 13.2.0, 14.2.0, 15.0.2, 16.2.0, 17.2.0 :
module load intel/2025.2.0        # available on all clusters except narval,
module load ls-dyna-mpp/17.2.0    # all versions ifort190_avx512_openmpi405_sharelib

# Uncomment next two lines to use an ANSYS License Server
#export LSTC_LICENSE=ansys                   # Do not change this setting
#export ANSYSLMD_LICENSE_FILE=PORT@HOSTNAME  # Specify PORT and HOSTNAME

#export LSTC_MEMORY=AUTO          # Optional for explicit only

INPUTFILE="airbag.deploy.k"       # Specify an input filename
MPPSOLVER="ls-dyna_d"             # Specify ls-dyna_s OR ls-dyna_d

srun $MPPSOLVER i=$INPUTFILE memory=200M
```

where
* `ls-dyna_s` = single precision mpp solver
* `ls-dyna_d` = double precision mpp solver
To use version 12.2.1 or 12.2.2 on Narval, the above script will likely need to be modified to run jobs under `$SLURM_TMPDIR` otherwise performance may be ~100x slower than other clusters. Narval only has lsdyna modules for 12.2.1 and 12.2.2 installed on it since all of its servers are legacy AVX2 based. Newer versions have been installed using AVX512 binaries and are therefore only available on other clusters.

## Performance testing

Depending on the simulation, LS-DYNA may not be able to efficiently use very many cores in parallel. Scaling test jobs should therefore always be run before submitting long jobs. Doing this will help determine the maximum number of cores that can be used before performance degradation begins to occur. To extract test job statistics such as Job Wall-clock time, CPU Efficiency, and Memory Efficiency, either the `seff jobnumber` command or a cluster job portal such as [this](https://portal.nibi.sharcnet.ca) can be used. In the past, scaling test jobs for the standard airbag problem have shown significantly different performance characteristics depending on which cluster they were being run on. These tests, however, were rather small using only 6 cores on a single node with the `ls-dyna/12.2.1` module and 6 cores evenly distributed across two nodes with the `ls-dyna-mpi/12.2.1` module. Scaling tests should instead be run using the actual research simulation and cluster where the full production runs will be done to get reliable results.

## Graphical use

LSTC provides [LS-PrePost](https://www.lstc.com/products/ls-prepost) for pre- and post-processing of LS-DYNA [models](https://www.dynaexamples.com/). This program is made available by a separate module and does not require a license. To run abaqus graphically in a remote GUI desktop, do one of the following, where the OnDemand desktop approach is recommended:

### OnDemand
1. Connect to an OnDemand system using one of the following URLs in your laptop browser:
   [NIBI](https://docs.alliancecan.ca/wiki/nibi#access_through_open_ondemand_(ood)): `https://ondemand.sharcnet.ca`
   FIR: `https://jupyterhub.fir.alliancecan.ca`
   RORQUAL: `https://jupyterhub.rorqual.alliancecan.ca`
   TRILLIUM: `https://ondemand.scinet.utoronto.ca`
2. Open a new terminal window in your desktop and run:
   `module load StdEnv/2020`
   `module load ls-prepost/4.9`
   `lsprepost` OR `lspp49`

### VncViewer
1. Connect with a VncViewer client to a login or compute node by following [TigerVNC](../interactive/vnc.md)
2. Open a new terminal window in your desktop and run:
   `module load StdEnv/2020`
   `module load ls-prepost/4.9`
   `lsprepost` OR `lspp49`