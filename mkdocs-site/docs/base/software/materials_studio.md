---
title: "Materials Studio"
tags:
  - software

keywords:
  []
---

The Alliance does not have permission to install Materials Studio centrally on all clusters. If you have a license, follow these instructions to install the application in your account. Please note that the current instructions are only valid for older standard software environments, so before beginning you will need to use a command like `module load StdEnv/2016.4` if you are using the default 2020 [standard software environment](standard_software_environments.md).

= Installing Materials Studio 2020 = 
If you have access to Materials Studio 2020, you will need two things to proceed. First, you must have the archive file that contains the installer; this file should be named `BIOVIA_2020.MaterialsStudio2020.tar`. Second, you must have the IP address (or DNS name) and the port of an already configured license server to which you will connect.

Once you have these, upload the `BIOVIA_2020.MaterialsStudio2020.tar` file to your /home folder on the cluster you intend to use. Then, run the commands 

```bash

```
<port>@<server>}}
and

```bash

```
$HOME}}

Once this command has completed, log out of the cluster and log back in. You should then be able to load the module with

```bash
module load materialsstudio/2020
```

In order to be able to access the license server from the compute nodes, you will need to [contact technical support](technical-support.md) so that we can configure our firewall(s) to allow the software to connect to your licence server.

= Installing Materials Studio 2018 = 
If you have access to Materials Studio 2018, you will need two things to proceed. First, you must have the archive file that contains the installer; this file should be named `MaterialsStudio2018.tgz`. Second, you must have the IP address (or DNS name) and the port of an already configured license server to which you will connect.

Once you have these, upload the `MaterialsStudio2018.tgz` file to your /home folder on the cluster you intend to use. Then, run the commands 

```bash

```
<port>@<server>}}
and

```bash

```
$HOME}}

Once this command has completed, log out of the cluster and log back in. You should then be able to load the module with

```bash
module load materialsstudio/2018
```

In order to be able to access the license server from the compute nodes, you will need to [contact technical support](technical-support.md) so that we can configure our firewall(s) to allow the software to connect to your licence server.

== Team installation == 
If you are a PI holding the Materials Studio licence, you can install Materials Studio once for all your group members. Since normally team work is stored in the `/project` space, determine which project directory you want to use. Suppose it is `~/projects/A_DIRECTORY`, then you will need to know these two values:

1. Determine the actual path of A_DIRECTORY as follows: 
```bash

```
$(readlink -f ~/projects/A_DIRECTORY)|echo $PI_PROJECT_DIR}}
2. Determine the group of A_DIRECTORY as follows: 
```bash

```
$(stat -c%G $PI_PROJECT_DIR)|echo $PI_GROUP}}

With these values known, install Materials Studio.

# Change the default group to your team's `def-` group, e.g., 
```bash
newgrp $PI_GROUP
```

# Open the permissions of your project directory so your team can access it, e.g., 
```bash
chmod g+rsx $PI_PROJECT_DIR
```

# Create an install directory within /project, e.g., 
```bash
mkdir $PI_PROJECT_DIR/MatStudio2018
```

# Install the software, e.g., 
```bash

```
<port>@<server> eb MaterialsStudio-2018-dummy-dummy.eb --installpath$PI_PROJECT_DIR/MatStudio2018 --sourcepath$HOME}}

Before the software can be run:

# Run this command. 
```bash
module use $PI_PROJECT_DIR/MatStudio2018/modules/2017/Core/
```

#* Your team members may wish to add this to their `~/.bashrc` file.
# Load the materialsstudio module, i.e., 
```bash
module load materialsstudio
```

<b>NOTE:</b> Be sure to always replace variables PI_GROUP and PI_PROJECT_DIR with their appropriate values.

= Examples of Slurm job submission scripts = 
The following examples assume that you have installed Materials Studio 2018 according to the above instructions. 

**`file`**
```text

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

**`file`**
```text

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

= Installing earlier versions of Materials Studio = 

If you require an earlier version of Materials Studio than 2018, you will need to install in into an [Apptainer](apptainer.md) container. This involves
# creating an Apptainer container with a compatible distribution of Linux installed in it;
# installing Materials Studio into that container;
# uploading the Apptainer container to your account and using it there.
#* NOTE: In order to be able to access the license server from the compute nodes, you will need to [contact technical support](technical-support.md) so that we can configure our firewall(s) to allow the software to connect to your license server.
Please be aware that you might be restricted to whole-node (single-node) jobs as the version of MPI inside the container might not be able to be used across nodes.