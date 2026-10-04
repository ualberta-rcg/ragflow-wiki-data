---
title: "LS-DYNA/en"
slug: "ls-dyna"
lang: "en"

source_wiki_title: "LS-DYNA/en"
source_hash: "a7469cfd32abfc921da1f959a9a48483"
last_synced: "2026-10-04T02:27:33.201522+00:00"
last_processed: "2026-10-04T03:06:27.698203+00:00"

tags:
  - software

keywords:
  - "LSTC license server"
  - "LS-DYNA"
  - "MPPSOLVER=\"ls-dyna_d\""
  - "mem=16G"
  - ".licenses/ls-dyna.lic"
  - "AVX512 binaries"
  - "ANSYSLMD_LICENSE_FILE"
  - "touch ~/.licenses/ls-dyna.lic"
  - "ls-dyna-mpi"
  - "scaling tests"
  - "LS-PrePost"
  - "Ansys"
  - "cpus-per-task=8"
  - "mem-per-cpu"
  - "ls-dyna/12.2.1"
  - "LSTC_LICENSE=ansys"
  - "environment variables"
  - "double precision"
  - "cluster"
  - "LSTC_MEMORY=AUTO"
  - "OnDemand"
  - "ls-dyna_d"
  - "airbag problem"
  - "SLURM_TMPDIR"
  - "single precision"
  - "floating license"
  - "SHARCNET Ansys license"
  - "LSTC_LICENSE"
  - "module load ls-prepost/4.9"
  - "SBATCH"
  - "ANSYS License Server"
  - "single node SMP LS-DYNA jobs"
  - "ls-dyna"
  - "ls-dyna-mpp"
  - "production runs"
  - "sbatch script-mpp-bynode.sh"
  - "scaling test jobs"
  - "~/.licenses/ls-dyna.lic"
  - "VncViewer"
  - "airbag.deploy.k"

questions:
  - "What are the two options for specifying an LS‑DYNA license server when submitting jobs on the clusters?"
  - "How can researchers obtain a free LS‑DYNA license if their institution does not already have one?"
  - "What commands and checks are used to verify that a license file works with a legacy LSTC or ANSYS license server?"
  - "What role does the `~/.licenses/ls-dyna.lic` file play in loading the `ls-dyna` or `ls-dyna-mpi` modules?"
  - "How can you guarantee that the required `ls-dyna.lic` file exists on every cluster where jobs will be submitted?"
  - "Which takes priority when configuring the license: environment variables or the values defined in the `ls-dyna.lic` file?"
  - "What environment variables need to be exported in a Slurm script to use an ANSYS LS‑DYNA license, and why must the `~/.licenses/ls-dyna.lic` file exist?"
  - "Which LS‑DYNA job types are supported by the SHARCNET ANSYS license, and what are the current core and job limits for Alliance researchers?"
  - "How should memory be calculated and set in a single‑node LS‑DYNA Slurm script, particularly when using the `LSTC_MEMORY=AUTO` option for implicit versus explicit analyses?"
  - "What do the expressions (0.5 * memGB / 8Bytes / w) * 1000M and (0.75 * memGB / 4Bytes / w) * 1000M represent for double‑ and single‑precision solutions?"
  - "Which SLURM directives are specified in the script and what resources (time, CPUs, memory, nodes) do they allocate?"
  - "Which modules are loaded by the script and why are they required for the job execution?"
  - "How should memory be allocated for the master node when running LS‑DYNA MPP jobs on multiple nodes?"
  - "What are the key differences between the single‑node solvers (ls‑dyna_s / ls‑dyna_d) and the MPP solvers (ls‑dyna‑mpp) regarding precision and required modules?"
  - "How can a user submit an LS‑DYNA job to a specified number of whole compute nodes using the provided Slurm script?"
  - "What modifications are needed in the script to run LS‑DYNA 12.2.1 or 12.2.2 on the Narval cluster without incurring a ~100× performance penalty?"
  - "How should the core count and mem‑per‑cpu be set in the SLURM submission script to allow the scheduler to choose optimal nodes and ensure the master processor can decompose the job correctly?"
  - "Why must scaling tests be performed before launching long LS‑DYNA simulations, and which tools (e.g., seff or the portal) can be used to extract their performance metrics?"
  - "What environment variables must be set to configure the ANSYS License Server, and what placeholders need to be replaced in their values?"
  - "How are the input filename and the LS‑DYNA solver type (single‑precision vs. double‑precision) specified in the script?"
  - "What role does the LSTC_MEMORY variable play, and how can it be adjusted for explicit solvers?"
  - "Why did the performance characteristics differ between clusters in the initial airbag tests?"
  - "What specific configurations (core count, node distribution, and LS‑Dyna module) were used in the small‑scale tests?"
  - "Why is it important to run scaling tests on the actual research simulation and production cluster rather than on the small test setups?"
  - "How can a user run LS‑PrePost graphically on a remote system using the recommended OnDemand desktop approach?"
  - "What module commands must be executed in a terminal to load and start LS‑PrePost?"
  - "How can a VNC client (e.g., TigerVNC) be used to connect to a login or compute node for graphical LS‑PrePost access?"

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
The Alliance is a hosting provider for LS-DYNA which means LS-DYNA software is installed as modules on the clusters. The Alliance does NOT however provide a free LS-DYNA license or provide LS-DYNA license hosting services. Instead, many institutions, faculties, and departments already have licenses that can be used on our clusters. If a local license is not available then SHARCNET provides a limited number of free licenses on a first come first serve basis to any researcher as described below.

### Initial setup and testing

If a license server has never been used on a cluster, firewall changes will first need to be done on both the cluster side and server side. This will typically require involvement from both our technical team and the technical people managing your license software. To arrange this, send an email containing the service port and IP address of your floating license server to [technical support](../support/technical_support.md). To check if your license file is working with a legacy LSTC server or ANSYS server you may run the following commands:

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

In 2019 Ansys, purchased the Livermore Software Technology Corporation (LSTC), developer of LS-DYNA. LS-DYNA licenses issued by Ansys since that time use **Ansys license servers**. Legacy LSTC licenses that run on **LSTC license servers** are now available from ANSYS. This section explains how to configure your job script for each of these cases.

### LSTC license

If you have a license issued to run on a LSTC license server, there are two options to specify it:

Option 1) Specify your license server by creating a small file named `ls-dyna.lic` with the following contents:

!!! info "ls-dyna.lic"
    ```bash
    #LICENSE_TYPE: network
    #LICENSE_SERVER:<port>@<server>
    ```

where `<port>` is an integer number and `<server>` is the hostname of your LSTC license server. Put this file in directory `$HOME/.licenses/` on each cluster where you plan to submit jobs. The values in the file are picked up by LS-DYNA when it runs. This occurs because our module system sets the LSTC_FILE variable to `LSTC_FILE=/home/$USER.licenses/ls-dyna.lic` whenever you load a `ls-dyna` or `ls-dyna-mpi` module. This approach is recommended for users with a license hosted on a LSTC license server since (compared to the next option) the identical settings will automatically be used by all jobs you submit on the cluster (without the need to specify them in each individual slurm script or setting them in your environment).

Option 2) Specify your license server by setting the following two environment variables in your slurm scripts:
`export LSTC_LICENSE=network`
`export LSTC_LICENSE_SERVER=<port>@<server>`
where `<port>` is an integer number and `<server>` is the hostname or IP address of your LSTC license server. These variables will take priority over any values specified in your `~/.licenses/ls-dyna.lic` file which must exist (even if it's empty) for any `ls-dyna` or `ls-dyna-mpi` module to successfully load. To ensure it exists, run `touch ~/.licenses/ls-dyna.lic` once on the command line on each cluster where you will submit jobs. For further details, see the official [documentation](https://lsdyna.ansys.com/download-install-overview/).

### ANSYS license

If your LS-DYNA license is hosted on an Ansys license server, set the following two environment variables in your slurm scripts:
`export LSTC_LICENSE=ansys`
`export ANSYSLMD_LICENSE_FILE=<port>@<server>`
where `<port>` is an integer number and `<server>` is the hostname or IP address of your Ansys license server. These variables cannot be defined in your `~/.licenses/ls-dyna.lic` file. The file however must exist (even if it's empty) for any `ls-dyna` module to load. To ensure this, run `touch ~/.licenses/ls-dyna.lic` once from the command line (or each time in your slurm scripts). Note that only module versions >= 12.2.1 will work with Ansys license servers.

**SHARCNET**

The SHARCNET Ansys license supports running **single node** SMP or MPP LS-DYNA jobs with many cores using the included `dysmp` license feature. The SHARCNET Ansys license however does NOT support running **multi-node** distributed memory MPP LS-DYNA jobs since it lacks the required `mppdyna` feature. Any researcher from the Alliance can freely use the SHARCNET license to run upto 5 simultaneous lsdyna jobs with 288 cores without any internal software limits such as those present in the student or teaching licenses. These limits maybe changed depending on the license load to optimize reliable availability and will be updated here at such time. For example a researcher can currently submit and run a 192 core single full node job and a 96 core half node job using an unlimited mesh size. The SHARCNET license may only be used for the purpose of Academic research and associated publications. To utilize the SHARCNET license on the cluster to run LS-DYNA jobs include the following lines to your slurm script:
`export LSTC_LICENSE=ansys`
`export ANSYSLMD_LICENSE_FILE=1055@license1.computecanada.ca`

## Cluster job submission

LS-DYNA provides binaries for running jobs on a single compute node (SMP - Shared Memory Parallel using OpenMP) or across multiple compute nodes (MPP - Message Passing Parallel using MPI). This section provides slurm scripts for each job type.

## Single node jobs

Modules for running jobs on a single compute node can be listed with: `module spider ls-dyna`. Jobs may be submitted to the queue with: `sbatch script-smp.sh`. The following slurm script shows how to run LS-DYNA with 8 cores on a single compute node. Regarding the AUTO option of the LSTC_MEMORY [environment variable](https://www.dynasupport.com/howtos/general/environment-variables), this setting allows memory to be dynamically extended beyond the specified `memory=1500M` word setting where it is suitable for explicit analysis such as metal forming simulations but not crash analysis. Given there are 4 Bytes/word for the single precision solver and 8 Bytes/word for the double precision solver, the 1500M setting in the slurm script example below equates to either 1) a maximum amount of (1500Mw*8Bytes/w) = 12GB memory before LS-DYNA self-terminates when solving an implicit problem or 2) a starting amount of 12GB memory prior to extending it (up 25% if necessary) when solving an explicit problem assuming `LSTC_MEMORY=AUTO` is uncommented. Note that 12GB represents 75% of the total mem=16GB reserved for the job and is considered ideal for implicit jobs on a single node. To summarize, for both implicit and explicit analysis, once an estimate for the total solver memory is determined in GB, the total memory setting for slurm can be determined by multiplying by 25% while the memory parameter value in mega words can be calculated as (0.75*memGB/8Bytes/w)*1000M and (0.75*memGB/4Bytes/w)*1000M for double and single precision solutions respectively.

!!! info "script-smp.sh"
    ```bash
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
*   `ls-dyna_s` = single precision smp solver
*   `ls-dyna_d` = double precision smp solver

## Multiple node jobs

There are several modules installed for running jobs on multiple nodes using the MPP (Message Passing Parallel) version of LS-DYNA. The method is based on mpi and can scale to very many cores (8 or more). The modules may be listed by running `module spider ls-dyna-mpi`. Sample slurm scripts below demonstrate how to use these modules for submitting jobs to a specified number of whole nodes *OR* a specified total number of cores using `sbatch script-mpp-bynode.sh` or `sbatch script-mpp-bycore.sh` respectively. The MPP version requires a sufficiently large enough amount of memory (memory1) for the first core (processor 0) on the master node to decompose and simulate the model. This amount may be satisfied by specifying a value of `mem-per-cpu` to slurm slightly larger than the memory (memory2) required per core for simulation and then placing enough cores on the master node such that their differential sum (mem-per-cpu less memory2) is greater than or equal to memory1. Similar to the single node model, for best results, keep the sum of all expected memory per node within 75% of the reserved ram on a node. Thus in the first script below, assuming a 128GB full node memory compute node, memory1 maybe 6000M (48GB) maximum and memory2 200M (48GB/31cores).

### Specify node count

Jobs can be submitted to a specified number of **whole** compute nodes with the following script. Please note naming of the modules has changed from ls-dyna-mpi to ls-dyna-mpp for all versions >= 13.2.0 in the below script as well these modules use avx512 and sharelib binaries.

!!! info "script-mpp-bynode.sh"
    ```bash
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
*   `ls-dyna_s` = single precision mpp solver
*   `ls-dyna_d` = double precision mpp solver

!!! warning
    To use version 12.2.1 or 12.2.2 on Narval the above script will likely need to be modified to run jobs under `$SLURM_TMPDIR` otherwise performance may be ~100x slower than other clusters. Narval only has lsdyna modules for 12.2.1 and 12.2.2 installed on it since all of its servers are legacy AVX2 based. Newer versions have been installed using AVX512 binaries and are therefore only available on other clusters.

### Specify core count

Jobs can be submitted to an arbitrary number of compute nodes by specifying the number of cores. This approach allows the scheduler to determine the optimal number of compute nodes to minimize job wait time in the queue. Memory limits are applied per core, therefore a sufficiently large value of `mem-per-cpu` must be specified so the master processor can successfully decompose and handle its computations as explained in more detail in the opening paragraph of this section. Please note the naming of the modules has changed from ls-dyna-mpi to ls-dyna-mpp for all versions >= 13.2.0 in the below script as well these modules use avx512 and sharelib binaries.

!!! info "script-mpp-bycore.sh"
    ```bash
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
*   `ls-dyna_s` = single precision mpp solver
*   `ls-dyna_d` = double precision mpp solver

!!! warning
    To use version 12.2.1 or 12.2.2 on Narval the above script will likely need to be modified to run jobs under `$SLURM_TMPDIR` otherwise performance may be ~100x slower than other clusters. Narval only has lsdyna modules for 12.2.1 and 12.2.2 installed on it since all of its servers are legacy AVX2 based. Newer versions have been installed using AVX512 binaries and are therefore only available on other clusters.

## Performance testing

Depending on the simulation LS-DYNA may not be able to efficiently use very many cores in parallel. Scaling test jobs should therefore always be run before submitting long jobs. Doing this will help determine the maximum number of cores that can be used before performance degradation begins to occur. To extract test job statistics such as Job Wall-clock time, CPU Efficiency and Memory Efficiency either the `seff jobnumber` command or a cluster job portal such as [this](https://portal.nibi.sharcnet.ca) can be used. In the past scaling test jobs for the standard airbag problem have shown significantly different performance characteristics in the past depending which cluster they were being run on. These tests however were rather small using only 6 cores on a single node with the ls-dyna/12.2.1 module and 6 cores evenly distributed across two nodes with the ls-dyna-mpi/12.2.1 module. Scaling tests should instead be run using the actual research simulation and cluster where the full production runs will be done to get reliable results.

## Graphical use

LSTC provides [LS-PrePost](https://www.lstc.com/products/ls-prepost) for pre- and post-processing of LS-DYNA [models](https://www.dynaexamples.com/). This program is made available by a separate module and does not require a license. To run abaqus graphically in a remote gui desktop do one of the following where the OnDemand desktop approach is recommended:

## OnDemand
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

## VncViewer
1.  Connect with a VncViewer client to a login or compute node by following [TigerVNC](../interactive/vnc.md)
2.  Open a new terminal window in your desktop and run:
    ```bash
    module load StdEnv/2020
    module load ls-prepost/4.9
    lsprepost OR lspp49