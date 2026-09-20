---
title: "LS-DYNA"
slug: "ls-dyna"
lang: "base"

source_wiki_title: "LS-DYNA"
source_hash: "59c6ae51048ca0bde3c28464b8996f77"
last_synced: "2026-09-20T00:48:35.777859+00:00"
last_processed: "2026-09-20T01:43:43.830571+00:00"

tags:
  - software

keywords:
  - "mem-per-cpu"
  - "memory"
  - "nodes"
  - "module load"
  - "LSTC license server"
  - "ls-dyna"
  - "~/.licenses/ls-dyna.lic"
  - "module load StdEnv/2020"
  - "memory setting for slurm"
  - "scaling test"
  - "double precision mpp solver"
  - "0.75*memGB"
  - "ls-dyna-mpi"
  - "Ansys"
  - "StdEnv/2020"
  - "SBATCH"
  - "cluster modules"
  - "JupyterHub"
  - "ANSYSLMD_LICENSE_FILE"
  - "single node SMP LS-DYNA jobs"
  - "airbag.deploy.k"
  - "Open OnDemand"
  - "SBATCH --mem=16G"
  - "ls-prepost"
  - "SHARCNET Ansys license"
  - "ls-dyna_d"
  - "STC license server"
  - "touch ~/.licenses/ls-dyna.lic"
  - "single precision"
  - "ls-prepost/4.9"
  - "floating license"
  - "ntasks"
  - "LS-DYNA"
  - "VncViewer"
  - "LSTC_MEMORY=AUTO"
  - "OnDemand"
  - "LSTC_LICENSE=ansys"
  - "slurm_hl2hl.py"
  - "mpirun"
  - "TigerVNC"
  - "https://ondemand.sharcnet.ca"
  - "double precision"

questions:
  - "What is LS‑DYNA, and on which clusters is it available for multiphysics simulations?"
  - "How does the Alliance handle LS‑DYNA licensing, and what options exist for users without a local license?"
  - "What are the two methods for configuring an LS‑DYNA license on the clusters, and how do they differ?"
  - "What is the purpose of the `~/.licenses/ls-dyna.lic` file for the `ls-dyna` and `ls-dyna-mpi` modules?"
  - "How do environment variables relate to the values defined in the `ls-dyna.lic` file?"
  - "Which command must be run on each cluster to ensure the required license file is present?"
  - "What environment variables need to be exported in a Slurm script to use an ANSYS license for LS‑DYNA, and why must a (possibly empty) `~/.licenses/ls-dyna.lic` file exist?"
  - "Which LS‑DYNA job types are allowed with the SHARCNET ANSYS license, and what are the current limits on simultaneous jobs and core usage for Alliance researchers?"
  - "How should memory be specified in a single‑node LS‑DYNA Slurm script, and what effect does setting `LSTC_MEMORY=AUTO` have on explicit versus implicit analyses?"
  - "How is the memory setting for a Slurm job calculated using the 25 % multiplier?"
  - "What are the formulas for converting the requested memory (in GB) to mega‑words for double‑precision and single‑precision solutions?"
  - "In the example `script‑smp.sh`, what does each `#SBATCH` directive (account, time, cpus‑per‑task, mem) specify for the job?"
  - "How should the memory requirements (memory1 and memory2) be configured in a Slurm script to satisfy the LS‑DYNA MPP solver’s decomposition needs on the master node?"
  - "What are the key differences between the single‑node LS‑DYNA scripts and the multiple‑node (MPP) scripts, and how are they submitted using `sbatch`?"
  - "Which modules and environment variables must be loaded or set to run LS‑DYNA with specific versions, precision (single vs double), and licensing on the cluster?"
  - "How should the number of cores and the `mem-per-cpu` value be set in a Slurm job script to ensure optimal node allocation for LS‑DYNA simulations?"
  - "Why is it necessary to perform scaling test jobs before launching long production runs, and which tools can be used to analyze their performance metrics?"
  - "What are the recommended steps to launch LS‑PrePost graphically on a remote system via the OnDemand desktop interface?"
  - "What is the purpose of setting the environment variable `LSTC_MEMORY=AUTO` in this script?"
  - "How does the script choose between using `mpirun` with a generated host list and `srun` to execute `ls-dyna_d`?"
  - "What is the distinction between `ls-dyna_s` and `ls-dyna_d` as mentioned in the comments?"
  - "Which URLs should be used in a laptop browser to access NIBI, FIR, RORQUAL, and TRILLIUM?"
  - "What modules must be loaded in a new terminal window before proceeding?"
  - "How do you open a new terminal window on your desktop and run the required module load commands?"
  - "How do you connect to a login or compute node using a VncViewer client?"
  - "Which modules must be loaded in the terminal before running lsprepost or lspp49?"
  - "What is the purpose of executing the command “lsprepost OR lspp49” after loading the modules?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: false
  qa_generated: false
---

## Introduction
[LS-DYNA](http://www.lstc.com) is available on all our clusters. It is used for many [applications](http://www.lstc.com/applications) to solve problems in multiphysics, solid mechanics, heat transfer, and fluid dynamics. Analyses are performed as separate phenomena or coupled physics simulations such as thermal stress or fluid-structure interaction. LSTC was recently purchased by Ansys, so the LS-DYNA software may eventually be exclusively provided as part of the Ansys module. For now, we recommend using the LS-DYNA software traditionally provided by LSTC as documented in this wiki page.

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
In 2019 Ansys purchased the Livermore Software Technology Corporation (LSTC), developer of LS-DYNA. LS-DYNA licenses issued by Ansys since that time use **Ansys license servers**. Legacy LSTC licenses that run on **LSTC license servers** are now available from Ansys. This section explains how to configure your job script for each of these cases.

### LSTC license
If you have a license issued to run on an LSTC license server, there are two options to specify it:

Option 1) Specify your license server by creating a small file named `ls-dyna.lic` with the following contents:
```bash file=ls-dyna.lic
#LICENSE_TYPE: network
#LICENSE_SERVER:<port>@<server>
```
where `<port>` is an integer number and `<server>` is the hostname of your LSTC license server. Put this file in directory `$HOME/.licenses/` on each cluster where you plan to submit jobs. The values in the file are picked up by LS-DYNA when it runs. This occurs because our module system sets the `LSTC_FILE` variable to `LSTC_FILE=/home/$USER.licenses/ls-dyna.lic` whenever you load an `ls-dyna` or `ls-dyna-mpi` module. This approach is recommended for users with a license hosted on an LSTC license server since (compared to the next option) the identical settings will automatically be used by all jobs you submit on the cluster (without the need to specify them in each individual Slurm script or setting them in your environment).

Option 2) Specify your license server by setting the following two environment variables in your Slurm scripts:
```bash
export LSTC_LICENSE=network
export LSTC_LICENSE_SERVER=<port>@<server>
```
where `<port>` is an integer number and `<server>` is the hostname or IP address of your LSTC license server. These variables will take priority over any values specified in your `~/.licenses/ls-dyna.lic` file, which must exist (even if it's empty) for any `ls-dyna` or `ls-dyna-mpi` module to successfully load. To ensure it exists, run `touch ~/.licenses/ls-dyna.lic` once on the command line on each cluster where you will submit jobs. For further details, see the official [documentation](https://lsdyna.ansys.com/download-install-overview/).

### ANSYS license
If your LS-DYNA license is hosted on an Ansys license server, set the following two environment variables in your Slurm scripts:
```bash
export LSTC_LICENSE=ansys
export ANSYSLMD_LICENSE_FILE=<port>@<server>
```
where `<port>` is an integer number and `<server>` is the hostname or IP address of your Ansys license server. These variables cannot be defined in your `~/.licenses/ls-dyna.lic` file. The file, however, must exist (even if it's empty) for any `ls-dyna` module to load. To ensure this, run `touch ~/.licenses/ls-dyna.lic` once from the command line (or each time in your Slurm scripts). Note that only module versions >= 12.2.1 will work with Ansys license servers.

#### SHARCNET
The SHARCNET Ansys license supports running **single node** SMP or MPP LS-DYNA jobs with many cores using the included `dysmp` license feature. The SHARCNET Ansys license, however, does NOT support running **multi-node** distributed memory MPP LS-DYNA jobs since it lacks the required `mppdyna` feature. Any researcher from the Alliance can freely use the SHARCNET license to run up to 5 simultaneous LS-DYNA jobs with 288 cores without any internal software limits such as those present in the student or teaching licenses. These limits may be changed depending on the license load to optimize reliable availability and will be updated here at such time. For example, a researcher can currently submit and run a 192-core single full node job and a 96-core half-node job using an unlimited mesh size. The SHARCNET license may only be used for the purpose of academic research and associated publications. To utilize the SHARCNET license on the cluster to run LS-DYNA jobs, include the following lines in your Slurm script:
```bash
export LSTC_LICENSE=ansys
export ANSYSLMD_LICENSE_FILE=1055@license1.computecanada.ca
```

## Cluster job submission
LS-DYNA provides binaries for running jobs on a single compute node (SMP - Shared Memory Parallel using OpenMP) or across multiple compute nodes (MPP - Message Passing Parallel using MPI). This section provides Slurm scripts for each job type.

### Single node jobs
Modules for running jobs on a single compute node can be listed with: `module spider ls-dyna`. Jobs may be submitted to the queue with: `sbatch script-smp.sh`. The following Slurm script shows how to run LS-DYNA with 8 cores on a single compute node. Regarding the `AUTO` option of the `LSTC_MEMORY` [environment variable](https://www.dynasupport.com/howtos/general/environment-variables), this setting allows memory to be dynamically extended beyond the specified `memory=1500M` word setting where it is suitable for explicit analysis such as metal forming simulations but not crash analysis. Given there are 4 Bytes/word for the single-precision solver and 8 Bytes/word for the double-precision solver, the `1500M` setting in the Slurm script example below equates to either 1) a maximum amount of (1500Mw\*8Bytes/w) = 12GB memory before LS-DYNA self-terminates when solving an implicit problem or 2) a starting amount of 12GB memory prior to extending it (up 25% if necessary) when solving an explicit problem, assuming `LSTC_MEMORY=AUTO` is uncommented. Note that 12GB represents 75% of the total `mem=16GB` reserved for the job and is considered ideal for implicit jobs on a single node. To summarize, for both implicit and explicit analysis, once an estimate for the total solver memory is determined in GB, the total memory setting for Slurm can be determined by multiplying by 25% while the memory parameter value in mega words can be calculated as `(0.75*memGB/8Bytes/w)*1000M` and `(0.75*memGB/4Bytes/w)*1000M` for double and single precision solutions respectively.

```bash file=script-smp.sh
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
*   `ls-dyna_s` = single-precision SMP solver
*   `ls-dyna_d` = double-precision SMP solver

### Multiple node jobs
There are several modules installed for running jobs on multiple nodes using the MPP (Message Passing Parallel) version of LS-DYNA. The method is based on MPI and can scale to very many cores (8 or more). The modules may be listed by running `module spider ls-dyna-mpi`. Sample Slurm scripts below demonstrate how to use these modules for submitting jobs to a specified number of whole nodes *OR* a specified total number of cores using `sbatch script-mpp-bynode.sh` or `sbatch script-mpp-bycore.sh` respectively. The MPP version requires a sufficiently large amount of memory (memory1) for the first core (processor 0) on the master node to decompose and simulate the model. This amount may be satisfied by specifying a value of `mem-per-cpu` to Slurm slightly larger than the memory (memory2) required per core for simulation and then placing enough cores on the master node such that their differential sum (`mem-per-cpu` less `memory2`) is greater than or equal to `memory1`. Similar to the single-node model, for best results, keep the sum of all expected memory per node within 75% of the reserved RAM on a node. Thus, in the first script below, assuming a 128GB full node memory compute node, `memory1` may be 6000M (48GB) maximum and `memory2` 200M (48GB/31cores).

#### Specify node count
Jobs can be submitted to a specified number of **whole** compute nodes with the following script.
```bash file=script-mpp-bynode.sh
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
*   `ls-dyna_s` = single-precision MPP solver
*   `ls-dyna_d` = double-precision MPP solver

#### Specify core count
Jobs can be submitted to an arbitrary number of compute nodes by specifying the number of cores. This approach allows the scheduler to determine the optimal number of compute nodes to minimize job wait time in the queue. Memory limits are applied per core; therefore, a sufficiently large value of `mem-per-cpu` must be specified so the master processor can successfully decompose and handle its computations as explained in more detail in the opening paragraph of this section.

```bash file=script-mpp-bycore.sh
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
*   `ls-dyna_s` = single-precision MPP solver
*   `ls-dyna_d` = double-precision MPP solver

### Performance testing
Depending on the simulation, LS-DYNA may not be able to efficiently use very many cores in parallel. Scaling test jobs should, therefore, always be run before submitting long jobs. Doing this will help determine the maximum number of cores that can be used before performance degradation begins to occur. To extract test job statistics such as Job Wall-clock time, CPU Efficiency, and Memory Efficiency, either the `seff jobnumber` command or a cluster job portal such as [this portal](https://portal.nibi.sharcnet.ca) can be used. In the past, scaling test jobs for the standard airbag problem have shown significantly different performance characteristics depending on which cluster they were being run on. These tests, however, were rather small, using only 6 cores on a single node with the `ls-dyna/12.2.1` module and 6 cores evenly distributed across two nodes with the `ls-dyna-mpi/12.2.1` module. Scaling tests should instead be run using the actual research simulation and cluster where the full production runs will be done to get reliable results.

## Graphical use
LSTC provides [LS-PrePost](https://www.lstc.com/products/ls-prepost) for pre- and post-processing of LS-DYNA [models](https://www.dynaexamples.com/). This program is made available by a separate module and does not require a license. To run LS-PrePost graphically in a remote GUI desktop, do one of the following where the OnDemand desktop approach is recommended:

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
1.  Connect with a VncViewer client to a login or compute node by following [TigerVNC](../interactive/vnc.md).
2.  Open a new terminal window in your desktop and run:
    ```bash
    module load StdEnv/2020
    module load ls-prepost/4.9
    lsprepost OR lspp49