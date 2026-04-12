---
title: "Materials Studio"
slug: "materials_studio"
lang: "base"

source_wiki_title: "Materials Studio"
source_hash: "3ee97104b4ccdd4fbe253fbe4657191d"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:00:50.981607+00:00"

tags:
  - software

keywords:
  - "License server"
  - "module load"
  - "install directory"
  - "MaterialsStudio"
  - "Team installation"
  - "Apptainer container"
  - "software installation"
  - "Installation"
  - "MPI"
  - "project directory"
  - "permissions"
  - "Cluster"
  - "Materials Studio"
  - "Slurm job submission scripts"

questions:
  - "What are the necessary prerequisites and files required before a user can begin installing Materials Studio on their cluster account?"
  - "Why is it necessary to contact technical support after completing the installation process for Materials Studio?"
  - "How can a Principal Investigator (PI) configure and install Materials Studio in a shared project directory for their entire research team?"
  - "What commands must be executed to properly configure and load the Materials Studio module before running the software?"
  - "How are the machine lists generated and exported within the provided Slurm job submission scripts for running tasks like DMol3 or CASTEP?"
  - "What is the process and what are the potential limitations for installing and running versions of Materials Studio older than 2018 using an Apptainer container?"
  - "How do you configure the project directory permissions to ensure that team members can access it?"
  - "What command is used to create the specific installation directory for the software within the project folder?"
  - "What parameters and environment variables must be specified when running the installation command for Materials Studio?"
  - "What commands must be executed to properly configure and load the Materials Studio module before running the software?"
  - "How are the machine lists generated and exported within the provided Slurm job submission scripts for running tasks like DMol3 or CASTEP?"
  - "What is the process and what are the potential limitations for installing and running versions of Materials Studio older than 2018 using an Apptainer container?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

The Alliance does not have permission to install Materials Studio centrally on all clusters. If you have a license, follow these instructions to install the application in your account. Please note that the current instructions are only valid for older standard software environments, so before beginning you will need to use a command like `module load StdEnv/2016.4` if you are using the default 2020 [standard software environment](standard-software-environments.md).

## Installing Materials Studio 2020

!!! note "Note"
    These instructions have been tested with Materials Studio 2020.

If you have access to Materials Studio 2020, you will need two things to proceed. First, you must have the archive file that contains the installer; this file should be named `BIOVIA_2020.MaterialsStudio2020.tar`. Second, you must have the IP address (or DNS name) and the port of an already configured license server to which you will connect.

Once you have these, upload the `BIOVIA_2020.MaterialsStudio2020.tar` file to your `/home` folder on the cluster you intend to use. Then, run the commands

```bash
export MS_LICENSE_SERVER=<port>@<server>
```

and

```bash
eb MaterialsStudio-2020.eb --sourcepath=$HOME
```

Once this command has completed, log out of the cluster and log back in. You should then be able to load the module with

```bash
module load materialsstudio/2020
```

In order to be able to access the license server from the compute nodes, you will need to [contact technical support](technical-support.md) so that we can configure our firewall(s) to allow the software to connect to your licence server.

## Installing Materials Studio 2018

!!! note "Note"
    These instructions have been tested with Materials Studio 2018.

If you have access to Materials Studio 2018, you will need two things to proceed. First, you must have the archive file that contains the installer; this file should be named `MaterialsStudio2018.tgz`. Second, you must have the IP address (or DNS name) and the port of an already configured license server to which you will connect.

Once you have these, upload the `MaterialsStudio2018.tgz` file to your `/home` folder on the cluster you intend to use. Then, run the commands

```bash
export MS_LICENSE_SERVER=<port>@<server>
```

and

```bash
eb /cvmfs/soft.computecanada.ca/easybuild/easyconfigs/m/MaterialsStudio/MaterialsStudio-2018.eb --disable-enforce-checksums --sourcepath=$HOME
```

Once this command has completed, log out of the cluster and log back in. You should then be able to load the module with

```bash
module load materialsstudio/2018
```

In order to be able to access the license server from the compute nodes, you will need to [contact technical support](technical-support.md) so that we can configure our firewall(s) to allow the software to connect to your licence server.

## Team installation
If you are a PI holding the Materials Studio licence, you can install Materials Studio once for all your group members. Since normally team work is stored in the `/project` space, determine which project directory you want to use. Suppose it is `~/projects/A_DIRECTORY`, then you will need to know these two values:

1. Determine the actual path of A_DIRECTORY as follows:
    ```bash
    PI_PROJECT_DIR=$(readlink -f ~/projects/A_DIRECTORY)
    echo $PI_PROJECT_DIR
    ```
2. Determine the group of A_DIRECTORY as follows:
    ```bash
    PI_GROUP=$(stat -c%G $PI_PROJECT_DIR)
    echo $PI_GROUP
    ```

With these values known, install Materials Studio.

1.  Change the default group to your team's `def-` group, e.g.,
    ```bash
    newgrp $PI_GROUP
    ```
2.  Open the permissions of your project directory so your team can access it, e.g.,
    ```bash
    chmod g+rsx $PI_PROJECT_DIR
    ```
3.  Create an install directory within /project, e.g.,
    ```bash
    mkdir $PI_PROJECT_DIR/MatStudio2018
    ```
4.  Install the software, e.g.,
    ```bash
    MS_LICENSE_SERVER=<port>@<server> eb MaterialsStudio-2018-dummy-dummy.eb --installpath=$PI_PROJECT_DIR/MatStudio2018 --sourcepath=$HOME
    ```

Before the software can be run:

1.  Run this command.
    ```bash
    module use $PI_PROJECT_DIR/MatStudio2018/modules/2017/Core/
    ```
    * Your team members may wish to add this to their `~/.bashrc` file.
2.  Load the materialsstudio module, i.e.,
    ```bash
    module load materialsstudio
    ```

**NOTE:** Be sure to always replace variables PI_GROUP and PI_PROJECT_DIR with their appropriate values.

## Examples of Slurm job submission scripts
The following examples assume that you have installed Materials Studio 2018 according to the above instructions.

```bash
#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=32
#SBATCH --time=12:00:00

module load materialsstudio/2018

# Create a list of nodes to be used for the job
DSD_MachineList="machines.LINUX"
slurm_hl2hl.py --format HP-MPI > $DSD_MachineList
export DSD_MachineList

# Job to run
RunDMol3.sh -np $SLURM_CPUS_PER_TASK Brucite001f
```

Below is an example of a Slurm job script that relies on Materials Studio's RunCASTEP.sh command:

```bash
#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu=1M
#SBATCH --time=0-12:00

module load materialsstudio/2018

DSD_MachineList="mpd.hosts"
slurm_hl2hl.py --format MPIHOSTLIST >$DSD_MachineList
export DSD_MachineList

RunCASTEP.sh -np $SLURM_CPUS_PER_TASK castepjob

if [ -f castepjob_NMR.param ]; then
  cp castepjob.check castepjob_NMR.check
  RunCASTEP.sh -np $SLURM_CPUS_PER_TASK castepjob_NMR
fi
```

## Installing earlier versions of Materials Studio

If you require an earlier version of Materials Studio than 2018, you will need to install in into an [Apptainer](apptainer.md) container. This involves
1. creating an Apptainer container with a compatible distribution of Linux installed in it;
2. installing Materials Studio into that container;
3. uploading the Apptainer container to your account and using it there.
    * NOTE: In order to be able to access the license server from the compute nodes, you will need to [contact technical support](technical-support.md) so that we can configure our firewall(s) to allow the software to connect to your license server.
Please be aware that you might be restricted to whole-node (single-node) jobs as the version of MPI inside the container might not be able to be used across nodes.