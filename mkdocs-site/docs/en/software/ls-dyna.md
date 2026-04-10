---
title: "LS-DYNA/en"
slug: "ls-dyna"
lang: "en"

source_wiki_title: "LS-DYNA/en"
source_hash: "d261c2cff7e8ebf19d81e12e546dec07"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T07:51:21.247640+00:00"

tags:
  - software

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

# Introduction

[LS-DYNA](http://www.lstc.com) is available on all our clusters. It is used for many [applications](http://www.lstc.com/applications) to solve problems in multiphysics, solid mechanics, heat transfer, and fluid dynamics. Analyses are performed as separate phenomena or coupled physics simulations such as thermal stress or fluid-structure interaction. LSTC was recently purchased by Ansys, so the LS-DYNA software may eventually be exclusively provided as part of the Ansys module. For now, we recommend using the LS-DYNA software traditionally provided by LSTC as documented in this wiki page.

# Licencing

The Alliance is a hosting provider for LS-DYNA. This means that we have LS-DYNA software installed on our clusters. The Alliance does **not** however provide a generic licence accessible to everyone or provide licence hosting services. Instead, many institutions, faculties, and departments already have licences that can be used on our clusters. So that such licences can be reached from a cluster's compute nodes, some cluster-specific network changes will generally need to be done. In cases where a licence has already been used on a particular cluster, these changes may already be done. Users unable to locate or arrange for a licence on campus may contact [CMC Microsystems](https://www.cmc.ca/support/). Licences purchased from CMC do not require the overhead of hosting a local licence server since they are hosted on a remote server system that CMC manages with the added benefit of being usable anywhere. If you have your own server and need a quote for a locally managed licence, consider contacting [Simutech](https://simutechgroup.com) or contact Ansys directly. SHARCNET does not provide any free LS-DYNA licences or licence hosting services at this time.

## Initial setup and testing

If your (existing or new) licence server has never been used on the cluster where you plan to run jobs, firewall changes will first need to be done on both the cluster side and server side. This will typically require involvement from both our technical team and the technical people managing your licence software. To arrange this, send an email containing the service port and IP address of your floating licence server to [technical support](technical-support.md). To check if your licence file is working, run the following commands:

```bash
module load ls-dyna
ls-dyna_s or ls-dyna_d
```

You don't need to specify any input file or arguments to run this test. The output header should contain a (non-empty) value for `Licensed to:` with the exception of CMC licence servers. Press `Ctrl+C` to quit the program and return to the command line.

# Configuring your licence

In 2019 Ansys purchased the Livermore Software Technology Corporation (LSTC), developer of LS-DYNA. LS-DYNA licences issued by Ansys since that time use **Ansys licence servers**. Licences issued by LSTC may still use an **LSTC licence server**. You can also obtain an LS-DYNA licence through [CMC Microsystems](https://www.cmc.ca/). This section explains how to configure your account or job script for each of these cases.

## LSTC licence

If you have a licence issued to run on an LSTC licence server, there are two options to specify it:

Option 1) Specify your licence server by creating a small file named `ls-dyna.lic` with the following contents:

```bash title="ls-dyna.lic"
#LICENSE_TYPE: network
#LICENSE_SERVER:<port>@<server>
```

where `<port>` is an integer number and `<server>` is the hostname of your LSTC licence server. Put this file in directory `$HOME/.licenses/` on each cluster where you plan to submit jobs. The values in the file are picked up by LS-DYNA when it runs. This occurs because our module system sets the `LSTC_FILE` variable to `LSTC_FILE=/home/$USER.licenses/ls-dyna.lic` whenever you load a `ls-dyna` or `ls-dyna-mpi` module. This approach is recommended for users with a licence hosted on an LSTC licence server since (compared to the next option) the identical settings will automatically be used by all jobs you submit on the cluster (without the need to specify them in each individual Slurm script or setting them in your environment).

Option 2) Specify your licence server by setting the following two environment variables in your Slurm scripts:

```bash
export LSTC_LICENSE=network
export LSTC_LICENSE_SERVER=<port>@<server>
```

where `<port>` is an integer number and `<server>` is the hostname or IP address of your LSTC licence server. These variables will take priority over any values specified in your `~/.licenses/ls-dyna.lic` file which must exist (even if it's empty) for any `ls-dyna` or `ls-dyna-mpi` module to successfully load. To ensure it exists, run `touch ~/.licenses/ls-dyna.lic` once on the command line on each cluster where you will submit jobs. For further details, see the official [documentation](https://lsdyna.ansys.com/download-install-overview/).

## Ansys licence

If your LS-DYNA licence is hosted on an Ansys licence server, set the following two environment variables in your Slurm scripts:

```bash
export LSTC_LICENSE=ansys
export ANSYSLMD_LICENSE_FILE=<port>@<server>
```

where `<port>` is an integer number and `<server>` is the hostname or IP address of your Ansys licence server. These variables cannot be defined in your `~/.licenses/ls-dyna.lic` file. The file however must exist (even if it's empty) for any `ls-dyna` module to load. To ensure this, run `touch ~/.licenses/ls-dyna.lic` once from the command line (or each time in your Slurm scripts). Note that only `module` versions `>= 12.2.1` will work with Ansys licence servers.

### SHARCNET

The SHARCNET Ansys licence supports running SMP and MPP LS-DYNA jobs. It can be used for free by anyone (on a core- and job-limited basis) on Nibi cluster by adding the following lines to your Slurm script:

```bash
export LSTC_LICENSE=ansys
export ANSYSLMD_LICENSE_FILE=1055@license1.computecanada.ca
```

## CMC licence

If your LS-DYNA licence was purchased from CMC, set the following two environment variables according to the cluster you are using:

*   `export LSTC_LICENSE=ansys`
*   Fir:
    ```bash
    export ANSYSLMD_LICENSE_FILE=6624@172.26.0.101
    ```
*   Nibi:
    ```bash
    export ANSYSLMD_LICENSE_FILE=6624@10.25.1.56
    ```
*   Narval:
    ```bash
    export ANSYSLMD_LICENSE_FILE=6624@10.100.64.10
    ```
*   Rorqual:
    ```bash
    export ANSYSLMD_LICENSE_FILE=6624@10.100.64.10
    ```
*   Trillium:
    ```bash
    export ANSYSLMD_LICENSE_FILE=6624@scinet-cmc
    ```

where the IP address corresponds to the respective CADpass servers. No firewall changes are required to use a CMC licence on any cluster since these have already been done. Since the remote CMC server that hosts LS-DYNA licences is Ansys-based, these variables cannot be defined in your `~/.licenses/ls-dyna.lic` file. The file however must exist (even if it's empty) for any `ls-dyna` module to load. To ensure this is the case, run `touch ~/.licenses/ls-dyna.lic` once from the command line (or each time in your Slurm scripts). Note that only `module` versions `>= 13.1.1` will work with Ansys licence servers.

# Cluster job submission

LS-DYNA provides binaries for running jobs on a single compute node (SMP - Shared Memory Parallel using OpenMP) or across multiple compute nodes (MPP - Message Passing Parallel using MPI). This section provides Slurm scripts for each job type.

## Single node jobs

Modules for running jobs on a single compute node can be listed with: `module spider ls-dyna`. Jobs may be submitted to the queue with: `sbatch script-smp.sh`. The following Slurm script shows how to run LS-DYNA with 8 cores on a single compute node. Regarding the AUTO option of the `LSTC_MEMORY` [environment variable](https://www.dynasupport.com/howtos/general/environment-variables), this setting allows memory to be dynamically extended beyond the specified `memory=1500M` word setting where it is suitable for explicit analysis such as metal forming simulations but not crash analysis. Given there are 4 Bytes/word for the single precision solver and 8 Bytes/word for the double precision solver, the `1500M` setting in the Slurm script example below equates to either 1) a maximum amount of (1500Mw\*8 Bytes/w) = 12 GB memory before LS-DYNA self-terminates when solving an implicit problem or 2) a starting amount of 12 GB memory prior to extending it (up 25% if necessary) when solving an explicit problem assuming `LSTC_MEMORY=AUTO` is uncommented. Note that 12 GB represents 75% of the total `mem=16 GB` reserved for the job and is considered ideal for implicit jobs on a single node. To summarize, for both implicit and explicit analysis, once an estimate for the total solver memory is determined in GB, the total memory setting for Slurm can be determined by multiplying by 25% while the memory parameter value in mega words can be calculated as (0.75\*memGB/8 Bytes/w)\*1000M and (0.75\*memGB/4 Bytes/w)\*1000M for double and single precision solutions respectively.

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

#export LSTC_LICENSE=ansys      # Specify an ANSYS Licence Server
#export ANSYSLMD_LICENSE_FILE=<port>@<server>

#export LSTC_MEMORY=AUTO        # Optional for explicit only

ls-dyna_d ncpu=$SLURM_CPUS_ON_NODE i=airbag.deploy.k memory=1500M
```

where
*   `ls-dyna_s` = single precision smp solver
*   `ls-dyna_d` = double precision smp solver

## Multiple node jobs

There are several modules installed for running jobs on multiple nodes using the MPP (Message Passing Parallel) version of LS-DYNA. The method is based on MPI and can scale to very many cores (8 or more). The modules may be listed by running `module spider ls-dyna-mpi`. Sample Slurm scripts below demonstrate how to use these modules for submitting jobs to a specified number of whole nodes **or** a specified total number of cores using `sbatch script-mpp-bynode.sh` or `sbatch script-mpp-bycore.sh` respectively. The MPP version requires a sufficiently large enough amount of `memory` (`memory1`) for the first core (processor 0) on the master node to decompose and simulate the model. This amount may be satisfied by specifying a value of `mem-per-cpu` to Slurm slightly larger than the `memory` (`memory2`) required per core for simulation and then placing enough cores on the master node such that their differential sum (`mem-per-cpu` less `memory2`) is greater than or equal to `memory1`. Similar to the single node model, for best results, keep the sum of all expected memory per node within 75% of the reserved RAM on a node. Thus in the first script below, assuming a 128 GB full node memory compute node, `memory1` may be `6000M` (48 GB) maximum and `memory2` `200M` (48 GB/31 cores).

### Specify node count

Jobs can be submitted to a specified number of **whole** compute nodes with the following script.

```bash title="script-mpp-bynode.sh"
#!/bin/bash
#SBATCH --account=def-account    # Specify
#SBATCH --time=0-03:00           # D-HH:MM
#SBATCH --ntasks-per-node=192    # Specify all cores per node (narval/nibi/fir/trillium 192)
#SBATCH --nodes=1                # Specify number compute nodes (1 or more)
#SBATCH --mem=0                  # Use all memory per compute node (do not change)
##SBATCH --constraint=cascade    # Uncomment to specify a cluster specific node type

#module load StdEnv/2020         # Versions 12.0, 13.0, 13.1.1
#export RSNT_ARCH=avx2
#module load intel/2020.1.217
#module load openmpi/4.0.3
#module load ls-dyna-mpi/13.1.1 

module load StdEnv/2023          # Version 12.2.1
module load intel/2023.2.1
module load ls-dyna-mpi/12.2.1

#export LSTC_LICENSE=ansys       # Specify an ANSYS Licence Server
#export ANSYSLMD_LICENSE_FILE=<port>@<server>

#export LSTC_MEMORY=AUTO         # Optional for explicit only

if [ "$EBVERSIONNIXPKGS" == 16.09 ]; then
 slurm_hl2hl.py --format MPIHOSTLIST > /tmp/mpihostlist-$SLURM_JOB_ID
 mpirun -np $NCORES -hostfile /tmp/mpihostlist-$SLURM_JOB_ID ls-dyna_d i=airbag.deploy.k memory=200M
else
 srun ls-dyna_d i=airbag.deploy.k memory=200M
fi
```

where
*   `ls-dyna_s` = single precision mpp solver
*   `ls-dyna_d` = double precision mpp solver

### Specify core count

Jobs can be submitted to an arbitrary number of compute nodes by specifying the number of cores. This approach allows the scheduler to determine the optimal number of compute nodes to minimize job wait time in the queue. Memory limits are applied per core; therefore, a sufficiently large value of `mem-per-cpu` must be specified so the master processor can successfully decompose and handle its computations as explained in more detail in the opening paragraph of this section.

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

#export LSTC_LICENSE=ansys        # Specify an ANSYS Licence Server
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

## Performance testing

Depending on the simulation, LS-DYNA may not be able to efficiently use very many cores in parallel. Scaling test jobs should therefore always be run before submitting long jobs. Doing this will help determine the maximum number of cores that can be used before performance degradation begins to occur. To extract test job statistics such as Job Wall-clock time, CPU Efficiency, and Memory Efficiency, either the `seff jobnumber` command or a cluster job portal such as [this](https://portal.nibi.sharcnet.ca) can be used. In the past, scaling test jobs for the standard airbag problem have shown significantly different performance characteristics depending on which cluster they were being run on. These tests however were rather small, using only 6 cores on a single node with the `ls-dyna/12.2.1` module and 6 cores evenly distributed across two nodes with the `ls-dyna-mpi/12.2.1` module. Scaling tests should instead be run using the actual research simulation and cluster where the full production runs will be done to get reliable results.

# Graphical use

LSTC provides [LS-PrePost](https://www.lstc.com/products/ls-prepost) for pre- and post-processing of LS-DYNA [models](https://www.dynaexamples.com/). This program is made available by a separate module and does not require a licence. To run Abaqus graphically in a remote GUI desktop, do one of the following where the OnDemand desktop approach is recommended:

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

1.  Connect with a VncViewer client to a login or compute node by following [TigerVNC](vnc.md)
2.  Open a new terminal window in your desktop and run:
    ```bash
    module load StdEnv/2020
    module load ls-prepost/4.9
    lsprepost OR lspp49