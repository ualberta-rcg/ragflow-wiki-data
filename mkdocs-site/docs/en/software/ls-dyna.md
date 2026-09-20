---
title: "LS-DYNA/en"
slug: "ls-dyna"
lang: "en"

source_wiki_title: "LS-DYNA/en"
source_hash: "bcf5e1c2025f108f98758eadb66ae75d"
last_synced: "2026-09-20T00:48:35.777859+00:00"
last_processed: "2026-09-20T01:44:13.794799+00:00"

tags:
  - software

keywords:
  - "OnDemand"
  - "single precision mpp solver"
  - "RORQUAL"
  - "LS-DYNA"
  - "lspp49"
  - "MPPSOLVER"
  - "~/.licenses/ls-dyna.lic"
  - "ANSYS license server"
  - "LSTC license server"
  - "MPP version"
  - "LS-DYNA scaling"
  - "ls-dyna_s"
  - "module load StdEnv/2020"
  - "SHARCNET license"
  - "single precision"
  - "touch command"
  - "environment variables"
  - "lsprepost"
  - "sbatch script-mpp-bynode.sh"
  - "mem-per-cpu"
  - "ls-dyna-mpi module"
  - "ls-dyna license file"
  - "LSTC_MEMORY=AUTO"
  - "RSNT_ARCH=avx2"
  - "ANSYS License Server"
  - "ntasks"
  - "multiphysics simulations"
  - "TRILLIUM"
  - "ls-prepost/4.9"
  - "double precision"
  - "seff"
  - "ls-dyna-mpi"
  - "ls-dyna_d"
  - "memGB"
  - "SBATCH --cpus-per-task=8"
  - "VncViewer"
  - "slurm_hl2hl.py"
  - "single node SMP jobs"
  - "cluster licensing"
  - "Ansys acquisition"

questions:
  - "What are the two methods for configuring an LS‑DYNA job to use a legacy LSTC license server on the Alliance clusters?"
  - "How can a researcher obtain a free LS‑DYNA license if their institution does not have one, and what steps are required for the initial license‑server setup?"
  - "Where should the ls‑dyna.lic file be placed and what information must it contain for the module system to automatically apply the license settings?"
  - "Which environment variables override the values specified in your ~/.licenses/ls-dyna.lic file when loading an ls-dyna or ls-dyna-mpi module?"
  - "Why does the ~/.licenses/ls-dyna.lic file need to exist (even if empty) for the modules to load, and how do you create it on each cluster?"
  - "Where can you find the official documentation for additional details on the LS‑DYNA licensing setup?"
  - "What environment variables need to be exported in a Slurm script to use an ANSYS LS‑DYNA license, and why must an (even empty) ~/.licenses/ls‑dyna.lic file exist?"
  - "Which LS‑DYNA job types are allowed with the SHARCNET ANSYS license, and what are the current core limits and usage restrictions for Alliance researchers?"
  - "How should memory be specified in a single‑node LS‑DYNA Slurm script, including the role of the LSTC_MEMORY=AUTO setting and the calculation of the mem and memory parameters for implicit and explicit analyses?"
  - "How are the memory bandwidth limits for double‑precision and single‑precision solutions calculated in the formula shown?"
  - "What does each SBATCH directive (account, time, cpus‑per‑task, mem, nodes) specify in the `script‑smp.sh` script?"
  - "Which module is loaded and what is the role of the `RSNT_ARCH=avx2` environment variable in this script?"
  - "How can you configure and submit a multi‑node LS‑DYNA MPP job using the provided SLURM scripts (script‑mpp‑bynode.sh or script‑mpp‑bycore.sh)?"
  - "What are the differences and appropriate use cases for the single‑precision (ls‑dyna_s) versus double‑precision (ls‑dyna_d) solvers in both SMP and MPP modes?"
  - "What guidelines does the document give for allocating memory on the master node and per‑core memory when running LS‑DYNA MPP jobs, and how should these be reflected in the SLURM “mem‑per‑cpu” settings?"
  - "How should the number of cores and memory per CPU be specified in a SLURM job script for LS‑DYNA, and why is this important?"
  - "Why must scaling tests be performed before submitting long LS‑DYNA jobs, and which tools can be used to evaluate their performance metrics?"
  - "What are the recommended ways to run LS‑PrePost or other graphical applications remotely on the Alliance‑CAN clusters (e.g., via OnDemand or VNC)?"
  - "What is the purpose of the conditional check `if [ \"$EBVERSIONNIXPKGS\" == 16.09 ]; then … else … fi` in the script?"
  - "How does the script choose between the single‑precision solver (`ls-dyna_s`) and the double‑precision solver (`ls-dyna_d`)?"
  - "What function does the command `slurm_hl2hl.py --format MPIHOSTLIST` serve when launching the MPI job?"
  - "What are the URLs for the RORQUAL and TRILLIUM JupyterHub services mentioned in the text?"
  - "Which modules must be loaded in a new terminal window, and what are the exact commands to load ls‑prepost version 4.9?"
  - "How does the text instruct a user to connect to a login or compute node using a VNC client?"
  - "What does the term “lsprepost” refer to?"
  - "What does the term “lspp49” refer to?"
  - "In what context would you use the query “lsprepost OR lspp49”?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Introduction
[LS-DYNA](http://www.lstc.com) is available on all our clusters. It is used for many [applications](http://www.lstc.com/applications) to solve problems in multiphysics, solid mechanics, heat transfer, and fluid dynamics. Analyses are performed as separate phenomena or coupled physics simulations such as thermal stress or fluid structure interaction. LSTC was recently purchased by Ansys, so the LS-DYNA software may eventually be exclusively provided as part of the Ansys module. For now, we recommend using the LS-DYNA software traditionally provided by LSTC as documented in this wiki page.

## Licensing
The Alliance is a hosting provider for LS-DYNA, which means LS-DYNA software is installed as modules on the clusters. The Alliance does NOT, however, provide a free LS-DYNA licence or provide LS-DYNA licence hosting services. Instead, many institutions, faculties, and departments already have licences that can be used on our clusters. If a local licence is not available then SHARCNET provides a limited number of free licences on a first-come, first-served basis to any researcher as described below.

### Initial setup and testing

If a licence server has never been used on a cluster, firewall changes will first need to be done on both the cluster side and server side. This will typically require involvement from both our technical team and the technical people managing your licence software. To arrange this, send an email containing the service port and IP address of your floating licence server to [technical support](../support/technical_support.md). To check if your licence file is working with a legacy LSTC server or ANSYS server you may run the following commands:

```bash
touch ~/.licenses/ls-dyna.lic
module load ls-dyna

# Choose one of the following for LSTC or Ansys licence servers:
export LSTC_LICENSE=network
export LSTC_LICENSE_SERVER=<port>@<server>
# OR
export LSTC_LICENSE=ansys
export ANSYSLMD_LICENSE_FILE=<port>@<server>

# Then run one of the LS-DYNA solvers:
ls-dyna_s  # For single precision
# OR
ls-dyna_d  # For double precision
```

You do not need to specify any input file or arguments to run this test. The output header should contain a (non-empty) value for `Licensed to:`. Press ^C to quit the program and return to the command line.

## Configuring your licence

In 2019 Ansys purchased the Livermore Software Technology Corporation (LSTC), developer of LS-DYNA. LS-DYNA licences issued by Ansys since that time use **Ansys licence servers**. Legacy LSTC licences that run on **LSTC licence servers** are now available from ANSYS. This section explains how to configure your job script for each of these cases.

### LSTC licence

If you have a licence issued to run on an LSTC licence server, there are two options to specify it:

Option 1) Specify your licence server by creating a small file named `ls-dyna.lic` with the following contents:

```bash title="ls-dyna.lic"
#LICENSE_TYPE: network
#LICENSE_SERVER:<port>@<server>
```

where `<port>` is an integer number and `<server>` is the hostname of your LSTC licence server. Put this file in directory `$HOME/.licenses/` on each cluster where you plan to submit jobs. The values in the file are picked up by LS-DYNA when it runs. This occurs because our module system sets the `LSTC_FILE` variable to `LSTC_FILE=/home/$USER.licenses/ls-dyna.lic` whenever you load a `ls-dyna` or `ls-dyna-mpi` module. This approach is recommended for users with a licence hosted on an LSTC licence server since (compared to the next option) the identical settings will automatically be used by all jobs you submit on the cluster (without the need to specify them in each individual Slurm script or setting them in your environment).

Option 2) Specify your licence server by setting the following two environment variables in your Slurm scripts:
`export LSTC_LICENSE=network`
`export LSTC_LICENSE_SERVER=<port>@<server>`
where `<port>` is an integer number and `<server>` is the hostname or IP address of your LSTC licence server. These variables will take priority over any values specified in your `~/.licenses/ls-dyna.lic` file, which must exist (even if it is empty) for any `ls-dyna` or `ls-dyna-mpi` module to successfully load. To ensure it exists, run `touch ~/.licenses/ls-dyna.lic` once on the command line on each cluster where you will submit jobs. For further details, see the official [documentation](https://lsdyna.ansys.com/download-install-overview/).

### ANSYS licence

If your LS-DYNA licence is hosted on an Ansys licence server, set the following two environment variables in your Slurm scripts:
`export LSTC_LICENSE=ansys`
`export ANSYSLMD_LICENSE_FILE=<port>@<server>`
where `<port>` is an integer number and `<server>` is the hostname or IP address of your Ansys licence server. These variables cannot be defined in your `~/.licenses/ls-dyna.lic` file. The file, however, must exist (even if it is empty) for any `ls-dyna` module to load. To ensure this, run `touch ~/.licenses/ls-dyna.lic` once from the command line (or each time in your Slurm scripts). Note that only module versions >= 12.2.1 will work with Ansys licence servers.

!!! note "SHARCNET"
    The SHARCNET Ansys licence supports running **single node** SMP or MPP LS-DYNA jobs with many cores using the included `dysmp` licence feature. The SHARCNET Ansys licence, however, does NOT support running **multi-node** distributed memory MPP LS-DYNA jobs since it lacks the required `mppdyna` feature. Any researcher from the Alliance can freely use the SHARCNET licence to run up to 5 simultaneous LS-DYNA jobs with 288 cores without any internal software limits such as those present in the student or teaching licences. These limits may be changed depending on the licence load to optimize reliable availability and will be updated here at such time. For example, a researcher can currently submit and run a 192 core single full node job and a 96 core half node job using an unlimited mesh size. The SHARCNET licence may only be used for the purpose of Academic research and associated publications. To utilize the SHARCNET licence on the cluster to run LS-DYNA jobs, include the following lines to your Slurm script:
    `export LSTC_LICENSE=ansys`
    `export ANSYSLMD_LICENSE_FILE=1055@license1.computecanada.ca`

## Cluster job submission

LS-DYNA provides binaries for running jobs on a single compute node (SMP - Shared Memory Parallel using OpenMP) or across multiple compute nodes (MPP - Message Passing Parallel using MPI). This section provides Slurm scripts for each job type.

### Single node jobs

Modules for running jobs on a single compute node can be listed with: `module spider ls-dyna`. Jobs may be submitted to the queue with: `sbatch script-smp.sh`. The following Slurm script shows how to run LS-DYNA with 8 cores on a single compute node. Regarding the AUTO option of the `LSTC_MEMORY` [environment variable](https://www.dynasupport.com/howtos/general/environment-variables), this setting allows memory to be dynamically extended beyond the specified `memory=1500M` word setting where it is suitable for explicit analysis such as metal forming simulations but not crash analysis. Given there are 4 Bytes/word for the single precision solver and 8 Bytes/word for the double precision solver, the 1500M setting in the Slurm script example below equates to either 1) a maximum amount of (1500Mw*8Bytes/w) = 12GB memory before LS-DYNA self-terminates when solving an implicit problem or 2) a starting amount of 12GB memory prior to extending it (up 25% if necessary) when solving an explicit problem assuming `LSTC_MEMORY=AUTO` is uncommented. Note that 12GB represents 75% of the total mem=16GB reserved for the job and is considered ideal for implicit jobs on a single node. To summarize, for both implicit and explicit analysis, once an estimate for the total solver memory is determined in GB, the total memory setting for Slurm can be determined by multiplying by 25% while the memory parameter value in mega words can be calculated as (0.75*memGB/8Bytes/w)*1000M and (0.75*memGB/4Bytes/w)*1000M for double and single precision solutions respectively.

```bash title="script-smp.sh"
#!/bin/bash
#SBATCH --account=def-account   # Specify
#SBATCH --time=0-03:00          # D-HH:MM
#SBATCH --cpus-per-task=8       # Specify number of cores
#SBATCH --mem=16G               # Specify total memory
#SBATCH --nodes=1               # Do not change

#module load StdEnv/2020        # Versions 12.0, 13.0, 13.1.1
#export RSNT_ARCH=avx2
#module load intel/2020.1.217
#module load ls-dyna/13.1.1

module load StdEnv/2023         # Version 12.2.1
module load intel/2023.2.1
module load ls-dyna/12.2.1

#export LSTC_LICENSE=ansys      # Specify an ANSYS License Server
#export ANSYSLMD_LICENSE_FILE=<port>@<server>

#export LSTC_MEMORY=AUTO        # Optional for explicit only

ls-dyna_d ncpu=$SLURM_CPUS_ON_NODE i=airbag.deploy.k memory=1500M
```
where
*   `ls-dyna_s` = single precision smp solver
*   `ls-dyna_d` = double precision smp solver

### Multiple node jobs

There are several modules installed for running jobs on multiple nodes using the MPP (Message Passing Parallel) version of LS-DYNA. The method is based on MPI and can scale to very many cores (8 or more). The modules may be listed by running `module spider ls-dyna-mpi`. Sample Slurm scripts below demonstrate how to use these modules for submitting jobs to a specified number of whole nodes *OR* a specified total number of cores using `sbatch script-mpp-bynode.sh` or `sbatch script-mpp-bycore.sh` respectively. The MPP version requires a sufficiently large enough amount of memory (`memory1`) for the first core (processor 0) on the master node to decompose and simulate the model. This amount may be satisfied by specifying a value of `mem-per-cpu` to Slurm slightly larger than the memory (`memory2`) required per core for simulation and then placing enough cores on the master node such that their differential sum (`mem-per-cpu` less `memory2`) is greater than or equal to `memory1`. Similar to the single node model, for best results, keep the sum of all expected memory per node within 75% of the reserved RAM on a node. Thus in the first script below, assuming a 128GB full node memory compute node, `memory1` maybe 6000M (48GB) maximum and `memory2` 200M (48GB/31cores).

#### Specify node count

Jobs can be submitted to a specified number of **whole** compute nodes with the following script.

```bash title="script-mpp-bynode.sh"
#!/bin/bash
#SBATCH --account=def-account    # Specify
#SBATCH --time=0-03:00           # D-HH:MM
#SBATCH --ntasks-per-node=192    # Specify all cores per node (narval/nibi/fir/trillium 192)
#SBATCH --nodes=1                # Specify number compute nodes (1 or more)
#SBATCH --mem=0                  # Use all memory per compute node (do not change)
##SBATCH --constraint=cascade    # Uncomment to specify a cluster specific node type

#module load StdEnv/2023          # Versions 12.2.1, 12.2.2
#module load intel/2023.2.1       # Modules <=12.2.1 use non-shared libs
#module load ls-dyna-mpi/12.2.2   # Modules >=12.2.2 use shared libraries
# -----------------------------
module load StdEnv/2023           # Versions 13.2.0, 14.2.0, 15.0.2, 16.2.0, 17.0.1
module load intel/2025.2.0        # Modules >= 13.2.0 use avx512 binaries
module load ls-dyna-mpp/17.0.1    # Modules >= 13.2.0 are named ls-dyna-mpp

# Uncomment next two lines to specify an ANSYS License Server
#export LSTC_LICENSE=ansys                   # Do not change
#export ANSYSLMD_LICENSE_FILE=PORT@HOSTNAME  # Specify PORT number & HOSTNAME

#export LSTC_MEMORY=AUTO          # Optional for explicit only

INPUTFILE="airbag.deploy.k"       # Specify an input filename
MPPSOLVER="ls-dyna_d"             # Specify ls-dyna_s OR ls-dyna_d

if [ "$EBVERSIONNIXPKGS" == 16.09 ]; then
 slurm_hl2hl.py --format MPIHOSTLIST > /tmp/mpihostlist-$SLURM_JOB_ID
 mpirun -np $NCORES -hostfile /tmp/mpihostlist-$SLURM_JOB_ID $MPPSOLVER i=$INPUTFILE memory=200M
else
 srun $MPPSOLVER i=$INPUTFILE memory=200M
fi
```
where
*   `ls-dyna_s` = single precision mpp solver
*   `ls-dyna_d` = double precision mpp solver

#### Specify core count

Jobs can be submitted to an arbitrary number of compute nodes by specifying the number of cores. This approach allows the scheduler to determine the optimal number of compute nodes to minimize job wait time in the queue. Memory limits are applied per core, therefore a sufficiently large value of `mem-per-cpu` must be specified so the master processor can successfully decompose and handle its computations as explained in more detail in the opening paragraph of this section.

```bash title="script-mpp-bycore.sh"
#!/bin/bash
#SBATCH --account=def-account     # Specify
#SBATCH --time=0-03:00            # D-HH:MM
#SBATCH --ntasks=64               # Specify any total number of cores
#SBATCH --mem-per-cpu=2G          # Specify memory per core
##SBATCH --constraint=cascade     # Uncomment to specify a cluster specific node type

#module load StdEnv/2020          # Versions 12.0, 13.0, 13.1.1
#export RSNT_ARCH=avx2            # Uncomment on beluga, nibi, rorqual
#export load intel/2020.1.217
#module load openmpi/4.0.3
#module load ls-dyna-mpi/13.1.1

module load StdEnv/2023           # Version 12.2.1 (more versions added on request)
module load intel/2023.2.1
module load ls-dyna-mpi/12.2.1

#export LSTC_LICENSE=ansys        # Specify an ANSYS License Server
#export ANSYSLMD_LICENSE_FILE=<port>@<server>

#export LSTC_MEMORY=AUTO          # Optional for explicit only

if [ "$EBVERSIONNIXPKGS" == 16.09 ]; then
 slurm_hl2hl.py --format MPIHOSTLIST > /tmp/mpihostlist-$SLURM_JOB_ID
 mpirun -np $SLURM_NTASKS -hostfile /tmp/mpihostlist-$SLURM_JOB_ID ls-dyna_d i=airbag.deploy.k memory=200M
else
 srun ls-dyna_d i=airbag.deploy.k memory=200M
fi
```
where
*   `ls-dyna_s` = single precision mpp solver
*   `ls-dyna_d` = double precision mpp solver

### Performance testing

Depending on the simulation, LS-DYNA may not be able to efficiently use very many cores in parallel. Scaling test jobs should therefore always be run before submitting long jobs. Doing this will help determine the maximum number of cores that can be used before performance degradation begins to occur. To extract test job statistics such as Job Wall-clock time, CPU Efficiency, and Memory Efficiency, either the `seff jobnumber` command or a cluster job portal such as [this](https://portal.nibi.sharcnet.ca) can be used. In the past, scaling test jobs for the standard airbag problem have shown significantly different performance characteristics depending on which cluster they were being run on. These tests, however, were rather small, using only 6 cores on a single node with the `ls-dyna/12.2.1` module and 6 cores evenly distributed across two nodes with the `ls-dyna-mpi/12.2.1` module. Scaling tests should instead be run using the actual research simulation and cluster where the full production runs will be done to get reliable results.

## Graphical use

LSTC provides [LS-PrePost](https://www.lstc.com/products/ls-prepost) for pre- and post-processing of LS-DYNA [models](https://www.dynaexamples.com/). This program is made available by a separate module and does not require a licence. To run Abaqus graphically in a remote GUI desktop, do one of the following where the OnDemand desktop approach is recommended:

### OnDemand
1.  Connect to an OnDemand system using one of the following URLs in your laptop browser:
    *   [NIBI](https://docs.alliancecan.ca/wiki/Nibi#Access_through_Open_OnDemand_(OOD)): `https://ondemand.sharcnet.ca`
    *   FIR: `https://jupyterhub.fir.alliancecan.ca`
    *   RORQUAL: `https://jupyterhub.rorqual.alliancecan.ca`
    *   TRILLIUM: `https://ondemand.scinet.utoronto.ca`
2.  Open a new terminal window in your desktop and run:
    ```bash
    module load StdEnv/2020
    module load ls-prepost/4.9
    lsprepost OR lspp49
    ```

### VncViewer
1.  Connect with a VncViewer client to a login or compute node by following [TigerVNC](../interactive/vnc.md)
2.  Open a new terminal window in your desktop and run:
    ```bash
    module load StdEnv/2020
    module load ls-prepost/4.9
    lsprepost OR lspp49