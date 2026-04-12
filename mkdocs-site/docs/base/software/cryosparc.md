---
title: "Cryosparc"
slug: "cryosparc"
lang: "base"

source_wiki_title: "Cryosparc"
source_hash: "361c09b104a0b5fced17f44aa37966a3"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:37:17.875345+00:00"

tags:
  - software

keywords:
  - "graphical interface"
  - "Apptainer container"
  - "code"
  - "markup"
  - "LASTNAME"
  - "cryo-electron microscopy"
  - "sbatch"
  - "GPU job"
  - "Container image"
  - "scancel"
  - "Installation"
  - "Slurm job"
  - "GPU node"
  - "translate"
  - "password"
  - "closing tag"
  - "CCDB username"
  - "XML"
  - "FIRSTNAME"
  - "CryoSPARC"
  - "Slurm batch job"
  - "Apptainer"

questions:
  - "What is CryoSPARC and what is its primary application in scientific research?"
  - "Why must CryoSPARC be installed specifically on GPU nodes like Fir and Nibi instead of standard login nodes?"
  - "What are the key steps and requirements for building a standalone CryoSPARC instance using an Apptainer container image?"
  - "What are the key environment variables and commands required to install CryoSPARC and build its container image?"
  - "How is the CryoSPARC instance launched and managed within a Slurm batch GPU job?"
  - "What steps must a user take to access the CryoSPARC graphical interface locally and properly terminate the session when finished?"
  - "What software application is the password in this script intended to log into?"
  - "Which environment variables must be updated with the user's personal name?"
  - "What specific type of username is required for the \"USER\" export variable?"
  - "How can a user access the CryoSPARC graphical interface after submitting the initial batch script?"
  - "What actions need to be performed using the CryoSPARC graphical interface once it is open?"
  - "Why must the Slurm job be manually canceled with the `scancel` command after the CryoSPARC job finishes?"
  - "What is the primary function of the `</translate>` closing tag within a markup or programming context?"
  - "How do parsers or translation systems process the content that immediately precedes this specific tag?"
  - "In which specific software frameworks or document formats is this tag typically implemented?"
  - "What is the primary function of the `</translate>` closing tag within a markup or programming context?"
  - "How do parsers or translation systems process the content that immediately precedes this specific tag?"
  - "In which specific software frameworks or document formats is this tag typically implemented?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[CryoSPARC](https://cryosparc.com/) is a state of the art scientific software platform for cryo-electron microscopy (cryo-EM) used in research and drug discovery pipelines.

## Installation

!!! warning
    CryoSPARC is **not supported** on login nodes and must be installed and run on a GPU node. Running CryoSPARC on a login node can overload shared system resources and may lead to port conflicts when multiple instances are started at the same time.

Currently, only **Fir** and **Nibi** support CryoSPARC installation and execution on GPU nodes, as these systems provide outbound HTTPS access from GPU nodes to the CryoSPARC download site.

This tutorial describes how to build a standalone CryoSPARC instance in an Apptainer container image on a GPU node, allowing users to run CryoSPARC through GPU batch jobs while reducing filesystem load.

### Step 1. Acquire the licence

Complete the form at [https://cryosparc.com/download](https://cryosparc.com/download) to request a licence. The licence key is a string of letters and numbers in the following format:

`1a23b4d5-67ef-89g0-hi1j-kl2m3n4o5p6q`

### Step 2. Set up the installation directory

Create the directory where you would like to install CryoSPARC.
```bash
export HOST_PATH=/path/to/cryosparc
```
Set up the `LICENSE_ID` by replacing `1a23b4d5-67ef-89g0-hi1j-kl2m3n4o5p6q` with the licence key you obtained from [https://cryosparc.com/download](https://cryosparc.com/download) in **Step 1**.
```bash
export LICENSE_ID="1a23b4d5-67ef-89g0-hi1j-kl2m3n4o5p6q"
mkdir -p $HOST_PATH && cd $HOST_PATH
mkdir -p cryosparc_master cryosparc_worker
```

### Step 3. Download the installation package

```bash
curl -sL https://get.cryosparc.com/download/master-latest/$LICENSE_ID > cryosparc2_master.tar.gz
curl -sL https://get.cryosparc.com/download/worker-latest/$LICENSE_ID > cryosparc2_worker.tar.gz
```

### Step 4. Submit a GPU job for installation

Launch an interactive job:
```bash
salloc --account=def-account --time=3:00:00 --gpus=h100:1 --cpus-per-task=4 --mem=16000M
```

Prepare the first definition file. Change the value of `$HOST_PATH` to match the path you set in **Step 2**.

```bash linenums="1" hl_lines="10" title="ubuntu.def"
Bootstrap: docker
From: ubuntu
Stage: build

%environment
    export LC_ALL=C

%post
    HOST_PATH=/path/to/cryosparc                         # Change the path to the same you set in Step 2.
    INSTALL_PATH=/usr/local/cryosparc
    mkdir -p $HOST_PATH/
    mkdir -p /localscratch
    mkdir -p $INSTALL_PATH

%labels

%help
```

Build the first container image using the prepared definition file.
```bash
module load apptainer
apptainer build ubuntu.sif ubuntu.def
```

Prepare the second definition file. Update the values according to the comments below.

```bash linenums="1" hl_lines="10-16" title="cryosparc.def"
Bootstrap: localimage
From: ubuntu.sif
Stage: build

%environment
    export LC_ALL=C
    export PATH="/usr/local/cryosparc/cryosparc_master/bin:$PATH"

%post
    export HOST_PATH="/path/to/cryosparc"                                # Change this path to match the one specified in Step 2 and in ubuntu.def.
    export LICENSE_ID="1a23b4d5-67ef-89g0-hi1j-kl2m3n4o5p6q"             # Replace this with your license ID.
    export MY_EMAIL="user@email.com"                                     # Replace this with your email address. This email is what you used to obtain the licence, and will be used as the login email for CryoSPARC.
    export CRYOSPARC_PASSWD="Password123"                                # Replace this with your password. This will be used to log in to CryoSPARC.
    export FIRSTNAME="FirstName"                                         # Replace this with your first name.
    export LASTNAME="LastName"	                                         # Replace this with your last name.
	export USER="username"                                           # Important: replace this with your CCDB username.
	
    export INSTALL_PATH="/usr/local/cryosparc"
    export CRYOSPARC_DB_PATH="${HOST_PATH}/database"
    export WORKER_PATH="${INSTALL_PATH}/cryosparc_worker"
    export SSD_PATH="/tmp"
    export PATH="$INSTALL_PATH/cryosparc_master/bin:$PATH"
    apt update && apt install vim wget curl -y
    apt-get update && apt-get install -y iproute2
    mkdir -p ${INSTALL_PATH} && cd ${INSTALL_PATH}
    tar -xf ${HOST_PATH}/cryosparc2_master.tar.gz -C ${INSTALL_PATH}
    tar -xf ${HOST_PATH}/cryosparc2_worker.tar.gz -C ${INSTALL_PATH}
    mkdir -p /etc/pki/tls/certs/
    cp -r /etc/ssl/certs/ca-certificates.crt /etc/pki/tls/certs/ca-bundle.crt
    cd ${INSTALL_PATH}/cryosparc_master
    ./install.sh    --standalone \
                    --license ${LICENSE_ID} \
                    --worker_path ${WORKER_PATH} \
                    --ssdpath ${SSD_PATH} \
    			    --dbpath ${CRYOSPARC_DB_PATH} \
                    --initial_email ${MY_EMAIL} \
                    --initial_username "${USER}" \
                    --initial_firstname "${FIRSTNAME}" \
                    --initial_lastname "${LASTNAME}" \
                    --port 61000 \
                    --initial_password "${CRYOSPARC_PASSWD}" \
    			    --yes
    mv ${INSTALL_PATH}/cryosparc_master/config.sh $HOST_PATH/cryosparc_master/config.sh
    ln -s $HOST_PATH/cryosparc_master/config.sh ${INSTALL_PATH}/cryosparc_master/config.sh
    mv ${INSTALL_PATH}/cryosparc_master/run $HOST_PATH/cryosparc_master/run
    ln -s $HOST_PATH/cryosparc_master/run ${INSTALL_PATH}/cryosparc_master/run
    mv ${INSTALL_PATH}/cryosparc_worker/registry $HOST_PATH/cryosparc_worker/registry
    ln -s $HOST_PATH/cryosparc_worker/registry ${INSTALL_PATH}/cryosparc_worker/registry

%labels

%help
```

Build CryoSPARC container image:
```bash
apptainer build -B $HOST_PATH -B $SLURM_TMPDIR:/tmp --nv cryosparc.sif cryosparc.def
```

### Step 5. Launch CryoSPARC in a batch GPU job

Prepare the running job script. Replace `export HOST_PATH=/path/to/cryosparc` with the path you set in **Step 2**.

```bash linenums="1" hl_lines="13" title="run_cryosparc.sh"
#!/bin/bash
#SBATCH --account=def-account
#SBATCH --time=3:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64000M
#SBATCH --gpus=h100:1
#SBATCH --mail-user=user@email.com
#SBATCH --mail-type=ALL

mkdir $SLURM_TMPDIR/cryosparc_cache
module load apptainer
export HOST_PATH=/path/to/cryosparc            # replace this path to the one specified in Step 2.
cd ${HOST_PATH}
sed -i "s/^export CRYOSPARC_MASTER_HOSTNAME=.*/export CRYOSPARC_MASTER_HOSTNAME=\"$(hostname -f)\"/" cryosparc_master/config.sh

apptainer instance start --nv -B ${HOST_PATH} -B $SLURM_TMPDIR:/tmp \
  ${HOST_PATH}/cryosparc.sif cryosparc-master

apptainer exec instance://cryosparc-master /usr/local/cryosparc/cryosparc_master/bin/cryosparcm start

echo "To start Cryosparc, please run the following in your PC terminal:"
echo "ssh -N -L 61000:$HOSTNAME:61000 ${USER}@fir.alliancecan.ca"
echo
echo "User the email and password you set up in cryosparc.def to log in:"
echo
echo "Don't forget to cancel the job when the analysis is finished"
echo "scancel ${SLURM_JOB_ID}"

while (( ! stop_now )); do
    echo "[$(date)] starting one chunk"

    # do one bounded unit of work here
    # keep each chunk short enough that it can finish before the buffer expires
    sleep 60

    echo "[$(date)] chunk done"
done
```

Submit the job:
```bash
sbatch run_cryosparc.sh
```

!!! note
    After the job starts, follow the instructions in the job log file (for example, `slurm-123456.out`) to open the CryoSPARC graphical interface in your local browser. Use the interface to set up your CryoSPARC job and launch the worker. Once the CryoSPARC job is complete, check the output files and cancel the Slurm job with `scancel`; otherwise, the job will continue running until it reaches the walltime limit.