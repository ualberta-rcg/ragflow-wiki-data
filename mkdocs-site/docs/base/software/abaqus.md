---
title: "Abaqus"
slug: "abaqus"
lang: "base"

source_wiki_title: "Abaqus"
source_hash: "1e18b19d83409aa06ed2b13ca3738f3a"
last_synced: "2026-09-06T00:43:13.954271+00:00"
last_processed: "2026-09-06T02:21:34.365344+00:00"

tags:
  - software

keywords:
  - "Open OnDemand"
  - "Abaqus license server"
  - "Slurm job scripts"
  - "thread-based parallelization"
  - "Slurm --mem allocation"
  - "mesa option"
  - "abaqus job=testep2"
  - "RES memory"
  - "cpus-per-task=8"
  - "restart data frequency"
  - "module load abaqus"
  - "memory allocation"
  - "Abaqus 2026 module"
  - "Abaqus license"
  - "queued job"
  - "wall-clock times"
  - "temporary directory script"
  - "#SBATCH --mem"
  - "Abaqus"
  - "EBVERSIONABAQUS"
  - "monitor jobs"
  - "dusky cluster"
  - "memory estimate"
  - "scheduler"
  - "mp_mode=threads"
  - "RESTART"
  - "cae option"
  - "#SBATCH --gpus-per-node=h100:1"
  - "memory"
  - "memory per node"
  - "Abaqus solvers"
  - "restart data"
  - "MRMIO"
  - "#SBATCH --nodes=1"
  - "core-token mapping"
  - "configure license file"
  - "SHARCNET systems"
  - "mp_host_split"
  - "license queuing"
  - "abaqus job command"
  - "#SBATCH --constraint=granite"
  - "job arrays"
  - "abaqus"
  - "firewall"
  - "abaqus/2026"
  - "GPU and VirtualGL support"
  - "license tokens"
  - "mp_host_list"
  - "ABAQUSLM_LICENSE_FILE variable"
  - "mpi-based computing"
  - "SBATCH directives"
  - "license agreement"
  - "SLURM_TMPDIR"
  - "cluster IP addresses"
  - "%CPU"
  - "VIRT and RES columns"
  - "Nibi and Dusky clusters"
  - "SLURM_MEM_PER_NODE"
  - "Slurm email notification"
  - "mpi-based parallelization"
  - "lmhanglimit"
  - "SLURM_SUBMIT_DIR"
  - "required TCP ports"
  - "ssh c50"
  - "lmlicensequeuing=OFF"
  - "Explicit analysis"
  - "restart analysis"
  - "%MEM"
  - "DSLS server configuration"
  - "OVERLAY"
  - "license4.sharcnet.ca"
  - "License agreement"
  - "RES column"
  - "NAT nodes"
  - "abaqus job=test"
  - "tokens"
  - "mem=64G"
  - "Abaqus server"
  - "WRITE"
  - "interactive memory monitoring"
  - "Western site license"
  - "OpenOnDemand"
  - "Abaqus tokens"
  - "FLEXnet server configuration"
  - "hostlist"
  - "#SBATCH --mem=8G"
  - "unshare"
  - "abaqus.lic"
  - "SLURM job script"
  - "ABAQUSLM_LICENSE_FILE"
  - "abaqus cae -mesa"
  - "abaqus job submission"
  - "SLURM directives"
  - "SHARCNET license tokens"
  - "JupyterHub desktop session"
  - "memory=$((${SLURM_MEM_PER_NODE}-3072))MB"
  - "VirtualGL support"
  - "abaqus job"
  - "restart input file"
  - "lmstat"
  - "module load abaqus/2026"
  - "MPI multi-node computing"
  - "job dependency"
  - "proof-of-concept"
  - "license shortage"

questions:
  - "What are the two types of Abaqus license servers supported on Alliance clusters, and what are the key differences in their configuration procedures?"
  - "How must the environment variables and configuration files (such as abaqus.lic, abaqus_v6.env, and DSLicSrv.txt) be set up for FLEXnet‑based and DSLS‑based license servers respectively?"
  - "What additional actions and information are required when a new Abaqus license server is introduced to an Alliance cluster, and why is a special license agreement necessary?"
  - "What information (name or IPv4 address) must be supplied to set up the new Abaqus server?"
  - "Why does the administrator need to open firewall ports for the cluster’s NAT node IP addresses?"
  - "What licensing agreement is required before a campus license can be used on remote Alliance hardware?"
  - "How can you configure Abaqus jobs on a Slurm cluster to avoid indefinite license waiting, and what are the two available settings for immediate termination or a finite wait time?"
  - "What commands and environment settings are needed to verify the Abaqus 2026 module, and which components may fail verification without additional configuration?"
  - "Which Slurm script templates should be chosen for single‑node short runs, long runs that need restarts, and multi‑node MPI jobs, and how does the optional memory= parameter influence job performance?"
  - "How can you determine the optimal number of cores to use for long Abaqus jobs?"
  - "What parallelization methods are supported by Abaqus solvers for Standard Analysis?"
  - "Are scripts provided for restarting Abaqus jobs that run on multiple nodes?"
  - "What SLURM options (account, time, CPUs, memory, nodes, constraints, GPUs) must be set in the scripts to run a single‑node Abaqus job correctly?"
  - "How does the script differentiate between Abaqus version 2021 and versions 2026 or newer, and what command variations are applied for each case?"
  - "Which input file directives and optional Abaqus command flags are recommended for writing restart data and potentially improving simulation performance?"
  - "How should the restart input file be formatted to correctly read restart data in Abaqus?"
  - "What are the key differences in the job submission commands for Abaqus versions 2021 and 2026 in the provided scripts?"
  - "How does the temporary directory handling and periodic data backup work within the SLURM job scripts?"
  - "What is the purpose of using `unshare` with the `--fork --pid --mount-proc --user --map-user $USER` options in this Abaqus job submission script?"
  - "How does the script calculate and assign the memory limit for the Abaqus run based on SLURM environment variables?"
  - "When and how should the commented `#gpus=$SLURM_GPUS_ON_NODE` line be uncommented to enable GPU usage for the Abaqus job?"
  - "What resources (memory, node count, GPU type) are being requested in the SLURM directives?"
  - "Which Abaqus module version is intended to be loaded by the script?"
  - "How can the node‑type constraint and GPU specification be enabled or changed in this script?"
  - "What is the purpose of the background loop that copies `testst2*` files back to `$SLURM_SUBMIT_DIR` every 6 hours in the script?"
  - "How does the script differentiate between Abaqus version 2021 and versions 2026 or newer, and what specific commands are used for each case?"
  - "Which SLURM directives and script steps are required to run an MPI‑based Abaqus job on multiple nodes as shown in the `scriptsp1-mpi.txt` example?"
  - "How does the script differentiate between Abaqus version 2021 and versions 2026 or newer, and what command variations does it apply for each case?"
  - "What SLURM directives and environment configurations are required in the provided scripts to run a single‑node explicit Abaqus analysis?"
  - "What are the required steps and file operations to restart a simulation using the restart script, and how is restart data specified in the input file?"
  - "What is the role of the `donehostlist` and `mphostlist` variables and how are they constructed in the script?"
  - "How does the command configure the Abaqus job to run with MPI, including the use of `SLURM_TMPDIR` and `SLURM_NTASKS`?"
  - "Which options are currently commented out (e.g., `#mp_host_split=1`), and what would be the impact of enabling them on the job execution?"
  - "What does the expression `$((${SLURM_MEM_PER_NODE}-3072))MB` compute in the script?"
  - "Under what condition is the Abaqus job launched with `mp_mode=threads`, and which options are specified for that run?"
  - "According to the text, are any modifications to the input file required to restart the analysis?"
  - "What is the role of the background `while sleep …` loop and the `WPID` process in both scripts?"
  - "How does the script differentiate between Abaqus version 2021 and versions ≥ 2026 when launching the job?"
  - "How are restart data intervals specified in the input file and subsequently verified in the output files?"
  - "How do you submit an Abaqus job on a single node using threads mode with SLURM parameters?"
  - "What are the required steps and script components to run an Abaqus job across multiple nodes using MPI mode?"
  - "How can you estimate the memory requirements for an Abaqus simulation on a SLURM node?"
  - "What actions does the script perform when the Abaqus version is 2021, and how are the `unshare` options used in that case?"
  - "How does the script calculate and allocate memory for the Abaqus job, and what is the significance of subtracting 3072 MB?"
  - "What condition is checked for Abaqus versions 2026 or newer, and what different behavior (if any) is expected in that branch?"
  - "What SLURM resource specifications (e.g., CPUs, memory, account) are defined in the job submission command?"
  - "Which modules are loaded and what specific Abaqus command-line options are used before running the simulation?"
  - "How do you monitor the VIRT and RES columns with `top` on the compute node to identify the job’s steady‑state peak memory usage?"
  - "What steps should be taken to choose the `--mem` value in a Slurm script so that the non‑swapped physical memory (RES) meets the recommended “memory to minimize I/O” (MRMIO) without causing out‑of‑memory errors?"
  - "How can the required `mem-per-cpu` be estimated for multi‑node Abaqus runs, and what role does the `mp_host_split` parameter play in that calculation?"
  - "Which commands and options are needed to start Abaqus in graphical mode through OpenOnDemand or JupyterLab, especially when using nodes without a GPU or without VirtualGL support?"
  - "How can a user access the Open OnDemand portals for Nibi and TRILLIUM?"
  - "Which module must be loaded in a new terminal to run Abaqus, and how is the application started in graphical mode?"
  - "Under what circumstances should the “mesa” option be appended to the Abaqus launch command, and what limitation does it address?"
  - "How can you launch Abaqus CAE in graphical mode through a JupyterHub desktop session on SHARCNET?"
  - "What steps are required to request access, agree to the license terms, and configure the Abaqus license file for the SHARCNET free token pool?"
  - "When should the `-mesa` option be omitted when starting Abaqus, and what GPU/VirtualGL resources are needed for optimal performance?"
  - "What should be checked in the abaqus.lic file when an Abaqus job fails with a segmentation‑fault error using the abaqus/202X modules?"
  - "Which abaqus licensing lmstat commands can be used to query the SHARCNET license server for started, queued jobs and product availability?"
  - "What recommended practices can help prevent license‑shortage problems when submitting multiple Abaqus jobs?"
  - "What steps must be taken to configure the Abaqus license file for use on SHARCNET systems?"
  - "Which SHARCNET clusters and desktop systems are supported by the new license, and what happened to the old license3.sharcnet.ca server?"
  - "How should the “abaqus.lic” file be updated to reflect the shutdown of the previous license server?"
  - "What methods are recommended to avoid Abaqus license shortages when submitting multiple jobs?"
  - "How can Slurm email notifications be used to manage job submissions and prevent license contention?"
  - "What are the two simpler options mentioned for handling license shortage problems?"
  - "How can you disable non‑interactive Abaqus analysis jobs from entering a queued state and make them terminate immediately when no license is available?"
  - "Which environment variable controls the maximum time a job will wait for a license before being dequeued, and what output messages indicate that this limit has been exceeded?"
  - "What Slurm commands and efficiency metrics should be used to assess and adjust the memory and CPU allocations for optimal Abaqus job performance?"
  - "What do the %CPU and %MEM columns indicate about a process on a compute node?"
  - "How is the RES column presented, and what does it measure for each process?"
  - "According to the core‑token mapping table, how many cores correspond to a given number of tokens?"
  - "How is the number of tokens required for each GPU determined using the formula “TOKENS = floor[5 × CORES^0.422]”?"
  - "What are the exact steps to configure the abaqus.lic file to point to the Western Abaqus license server on the Dusky cluster?"
  - "If license checkout requests fail because the license4 server is shut down, what actions should a user take to obtain a working license?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! warning "Translator's Note (June 2026)"
    This page is currently being reviewed.

[Abaqus FEA](https://www.3ds.com/products-services/simulia/products/abaqus/) is a software suite for finite element analysis and computer-aided engineering.

## Licensing

Abaqus software modules are available on the Alliance clusters; however, you must provide your own license. There are two types of license servers, each with different setup procedures described below.

### FLEXnet servers

To configure your account on a cluster to use a **FLEXnet-based** (aka FlexLM) Abaqus license server, a single file named `~/.licenses/abaqus.lic` must be created, specifying its fully qualified hostname `FLEXnet-SERVER-HOSTNAME` and license manager daemon port number `LMGRD-PORT-NUMBER`. These two pieces of information are then assigned to the `ABAQUSLM_LICENSE_FILE` environment variable whenever an Abaqus module is loaded by reading:

```bash
[l2 (login node):~/.licenses] cat abaqus.lic
prepend_path("ABAQUSLM_LICENSE_FILE","LMGRD-PORT-NUMBER@FLEXnet-SERVER-HOSTNAME")
```

To use an old legacy version such as 6.14.1, change `ABAQUSLM_LICENSE_FILE` to `LM_LICENSE_FILE`.

### DSLS servers

To use a **DSLS** based license server (Dassault Systèmes License Server), you must first configure two small text files named `abaqus_v6.env` and `DSLicSrv.txt` so Abaqus can find the DSLS license server. You may either put a copy of `abaqus_v6.env` file into each Abaqus working directory **OR** put a single copy into your home directory. Note that the `abaqus_v6.env` file must contain the absolute path to your `DSLicSrv.txt` file so that both the `dslsstat` command and `abaqus` command will run properly. Otherwise you will need to set `export DSLS_CONFIG=/path/to/DSLicSrv.txt` for every job you submit. For example, placing both files into your home directory, you would just need to replace `<username>` with the output from "echo $USER" and then substitute the server IP and PORT values into DSLS-SERVER-HOSTNAME:LICENSING-CLIENT-PORT-NUMBER in the following:

```bash
[l2 (login node):~ ] cat abaqus_v6.env
license_server_type=DSLS
dsls_license_config="/home/<username>/DSLicSrv.txt"
```

```bash
[l2 (login node):~ ] cat DSLicSrv.txt
DSLS-SERVER-HOSTNAME:LICENSING-CLIENT-PORT-NUMBER
```

With both files set up, you may now check if the license server is reachable and responding by running:

```bash
[l2 (login node):~ ] module load abaqus
[l2 (login node):~ ] abaqus licensing dslsstat
```
**SUCCESS**: the output message will contain "license servers declared"
**FAILURE**: the output message will contain "No license server available"

### New servers

If your license server was never set up for use on an Alliance cluster, some additional configuration changes by the Alliance system administrator and your local system administrator will need to be done. Such changes are necessary to ensure the required TCP ports (https protocol) of your Abaqus server are reachable from all cluster compute nodes through the client/server firewalls. For help, please write to [technical support](../support/technical_support.md) and be sure to include the following:
*   FLEXnet SERVER: flex lmgrd port number (default 27000), static vendor port number (default 28000)
*   DSLS SERVER: administrative port number (default 4084), licensing client port number (default 4085)
*   Fully qualified domain name or IPV4 address of your new Abaqus server

You will be sent a list of cluster IP addresses (known as NAT nodes) so that your administrator can open the local server firewall to allow connections from the cluster on both ports. Please note that a special license agreement must generally be negotiated and signed by both SIMULIA and your institution before a campus license may be legally used on Alliance hardware located remotely at another institution.

### License queuing

The default setup for the license server is to queue jobs started on the cluster by Slurm if not enough tokens are available. There are two options to alter this behaviour so jobs don't sit idle on a cluster compute node waiting for a license indefinitely, wasting valuable resources. The first option is to terminate a job immediately if not enough licenses are available, therefore never entering a queue. To specify this setting, create a text file named `abaqus_v6.env` in either your `/home` OR working (submit) directory containing the line: `lmlicensequeuing=OFF`. The second option is to specify a finite wait time where the job can enter into a queued state on the license server, such as 1 minute, by adding the line: `lmhanglimit=1`. If within 1 minute sufficient licenses do not become available, then the job will be dequeued by the license server and in turn be terminated by Slurm. For each option, messages will be printed at the bottom of the Slurm output file as shown in [the Example below](#example).

## Version notes

### 2026

A new module `abaqus/2026` containing the initial *Abaqus 2026 Golden/GA* release has been installed into the default StdEnv/2023 environment. Another module named abaqus/2026.2614 containing the latest SIMULIA Established Products 2026 Fix Packs currently at level FD02 (FP.2614) will be made available as soon as possible. To verify your setup, run the following:

```bash
module load abaqus/2026
module load intel/2024
abaqus verify -all
```

All tests should Succeed except for CAE (unless you log into an OnDemand/Jupyter graphical desktop) and TOSCA (unless you set `export FED_DSFLEX_LICENSE_CONFIG=port@hostname`) before running the verification.

### 2021

It's recommended to discontinue use of `abaqus/2021` installed under the previous StdEnv/2020 since this legacy version generates `*** buffer overflow detected ***` error on all recent clusters. To workaround this problem, an `unshare` workaround has been added into each Slurm script found in this wiki. This, however, only works on single node jobs and does not guarantee accurate results.

## Cluster job submission

Below are prototype Slurm scripts for submitting thread and MPI-based parallel simulations to single or multiple compute nodes. Most users will find it sufficient to use one of the **project directory scripts** provided in the *Single node computing* sections. The optional `memory=` argument found in the last line of the scripts is intended for larger memory or problematic jobs where the 3072MB offset value may require tuning. A listing of all Abaqus command line arguments can be obtained by loading an Abaqus module and running: `abaqus -help | less`.

Single node jobs that run less than one day should find the *project directory script* located in the first tab sufficient. However, single node jobs that run for more than a day should use one of the restart scripts. Jobs that create large restart files will benefit by writing to the local disk through the use of the `SLURM_TMPDIR` environment variable utilized in the **temporary directory scripts** provided in the two rightmost tabs of the single node standard and explicit analysis sections. The restart scripts shown here will continue jobs that have been terminated early for some reason. Such job failures can occur if a job reaches its maximum requested runtime before completing and is killed by the queue or if the compute node the job was running on crashed due to an unexpected hardware failure. Other restart types are possible by further tailoring of the input file (not shown here) to continue a job with additional steps or change the analysis (see the documentation for version specific details).

Jobs that require large memory or larger compute resources (beyond that which a single compute node can provide) should use the MPI scripts in the **multiple node sections** below to distribute computing over arbitrary node ranges determined automatically by the scheduler. Short scaling test jobs should be run to determine wall-clock times (and memory requirements) as a function of the number of cores (2, 4, 8, etc.) to determine the optimal number before running any long jobs.

### Standard analysis

Abaqus solvers support thread-based and MPI-based parallelization. Scripts for each type are provided below for running Standard Analysis type jobs on Single or Multiple nodes respectively. Scripts to perform multiple node job restarts are not currently provided.

#### Single node computing

=== "project directory script"

    ````sh title="scriptsp1.txt"
    #!/bin/bash
    #SBATCH --account=def-group     # Specify account
    #SBATCH --time=00-06:00         # Specify days-hrs:mins
    #SBATCH --cpus-per-task=4       # Specify number of cores
    #SBATCH --mem=8G                # Specify total memory > 5G
    #SBATCH --nodes=1               # Do not change !
    ##SBATCH --constraint=granite   # Uncomment to specify a node type
    ##SBATCH --gpus-per-node=h100:1 # Uncomment to specify [type:]number

    module load abaqus/2026         # Latest version
    #module load StdEnv/2020        # Legacy version
    #module load abaqus/2021        # Discontinue use

    unset SLURM_GTIDS
    export MPI_IC_ORDER='tcp'
    echo "LM_LICENSE_FILE=$LM_LICENSE_FILE"
    echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"

    rm -f testsp1* testsp2*

    if [[ $EBVERSIONABAQUS -eq 2021 ]]; then
       /cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/unshare \
       --fork --pid --mount-proc --user --map-user $USER \
       abaqus job=testsp1 input=mystd-sim.inp \
       scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
       mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB" \
       #gpus=$SLURM_GPUS_ON_NODE  # uncomment this line to use gpu
    elif [[ $EBVERSIONABAQUS -ge 2026 ]]; then
       abaqus job=testsp1 input=mystd-sim.inp \
       scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
       mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB" \
       #gpus=$SLURM_GPUS_ON_NODE  # uncomment this line to use gpu
    fi
    ````

    To write restart data every N=12 time increments, specify in the input file:
    `*RESTART, WRITE, OVERLAY, FREQUENCY=12`
    To write restart data for a total of 12 time increments, specify instead:
    `*RESTART, WRITE, OVERLAY, NUMBER INTERVAL=12, TIME MARKS=NO`
    To check for completed restart information, do:
    `egrep -i "step|start" testsp*.com testsp*.msg testsp*.sta`
    Some simulations may benefit by adding the following to the Abaqus command at the bottom of the script:
    `order_parallel=OFF`

=== "project directory restart script"

    ````sh title="scriptsp2.txt"
    #!/bin/bash
    #SBATCH --account=def-group     # Specify account
    #SBATCH --time=00-06:00         # Specify days-hrs:mins
    #SBATCH --cpus-per-task=4       # Specify number of cores
    #SBATCH --mem=8G                # Specify total memory > 5G
    #SBATCH --nodes=1               # Do not change !
    ##SBATCH --constraint=granite   # Uncomment to specify a node type
    ##SBATCH --gpus-per-node=h100:1 # Uncomment to specify [type:]number

    module load abaqus/2026         # Latest version
    #module load StdEnv/2020        # Legacy version
    #module load abaqus/2021        # Discontinue use

    unset SLURM_GTIDS
    export MPI_IC_ORDER='tcp'
    echo "LM_LICENSE_FILE=$LM_LICENSE_FILE"
    echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"

    rm -f testsp2* testsp1.lck

    if [[ $EBVERSIONABAQUS -eq 2021 ]]; then
       /cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/unshare \
       --fork --pid --mount-proc --user --map-user $USER \
       abaqus job=testsp2 oldjob=testsp1 input=mystd-sim-restart.inp \
       scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
       mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB" \
       #gpus=$SLURM_GPUS_ON_NODE  # uncomment this line to use gpu
    elif [[ $EBVERSIONABAQUS -ge 2026 ]]; then
       abaqus job=testsp2 oldjob=testsp1 input=mystd-sim-restart.inp \
       scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
       mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB" \
       #gpus=$SLURM_GPUS_ON_NODE  # uncomment this line to use gpu
    fi
    ````

    The restart input file should contain:
    `*HEADING`
    `*RESTART, READ`

=== "temporary directory script"

    ````sh title="scriptst1.txt"
    #!/bin/bash
    #SBATCH --account=def-group     # Specify account
    #SBATCH --time=00-06:00         # Specify days-hrs:mins
    #SBATCH --cpus-per-task=4       # Specify number of cores
    #SBATCH --mem=8G                # Specify total memory > 5G
    #SBATCH --nodes=1               # Do not change !
    ##SBATCH --constraint=granite   # Uncomment to specify a node type
    ##SBATCH --gpus-per-node=h100:1 # Uncomment to specify [type:]number


    module load abaqus/2026         # Latest version
    #module load StdEnv/2020        # Legacy version
    #module load abaqus/2021        # Discontinue use

    unset SLURM_GTIDS
    export MPI_IC_ORDER='tcp'
    echo "LM_LICENSE_FILE=$LM_LICENSE_FILE"
    echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"
    echo "SLURM_SUBMIT_DIR =" $SLURM_SUBMIT_DIR
    echo "SLURM_TMPDIR = " $SLURM_TMPDIR

    rm -f testst1* testst2*

    mkdir $SLURM_TMPDIR/scratch
    cd $SLURM_TMPDIR
    while sleep 6h; do
       echo "Saving data due to time limit ..."
       cp -fv * $SLURM_SUBMIT_DIR 2>/dev/null
    done &
    WPID=$!

    if [[ $EBVERSIONABAQUS -eq 2021 ]]; then
       /cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/unshare \
       --fork --pid --mount-proc --user --map-user $USER \
       abaqus job=testst1 input=$SLURM_SUBMIT_DIR/mystd-sim.inp \
       scratch=$SLURM_TMPDIR/scratch cpus=$SLURM_CPUS_ON_NODE interactive \
       mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB" \
       #gpus=$SLURM_GPUS_ON_NODE  # uncomment this line to use gpu
    elif [[ $EBVERSIONABAQUS -ge 2026 ]]; then
       abaqus job=testst1 input=$SLURM_SUBMIT_DIR/mystd-sim.inp \
       scratch=$SLURM_TMPDIR/scratch cpus=$SLURM_CPUS_ON_NODE interactive \
       mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB" \
       #gpus=$SLURM_GPUS_ON_NODE  # uncomment this line to use gpu
    fi

    { kill $WPID && wait $WPID; } 2>/dev/null
    cp -fv * $SLURM_SUBMIT_DIR
    ````

    To write restart data every N=12 time increments, specify in the input file:
    `*RESTART, WRITE, OVERLAY, FREQUENCY=12`
    To write restart data for a total of 12 time increments, specify instead:
    `*RESTART, WRITE, OVERLAY, NUMBER INTERVAL=12, TIME MARKS=NO`
    To check the completed restart information, do:
    `egrep -i "step|start" testst*.com testst*.msg testst*.sta`

=== "temporary directory restart script"

    ````sh title="scriptst2.txt"
    #!/bin/bash
    #SBATCH --account=def-group     # Specify account
    #SBATCH --time=00-06:00         # Specify days-hrs:mins
    #SBATCH --cpus-per-task=4       # Specify number of cores
    #SBATCH --mem=8G                # Specify total memory > 5G
    #SBATCH --nodes=1               # Do not change !
    ##SBATCH --constraint=granite   # Uncomment to specify a node type
    ##SBATCH --gpus-per-node=h100:1 # Uncomment to specify [type:]number

    module load abaqus/2026         # Latest version
    #module load StdEnv/2020        # Legacy version
    #module load abaqus/2021        # Discontinue use

    unset SLURM_GTIDS
    export MPI_IC_ORDER='tcp'
    echo "LM_LICENSE_FILE=$LM_LICENSE_FILE"
    echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"
    echo "SLURM_SUBMIT_DIR =" $SLURM_SUBMIT_DIR
    echo "SLURM_TMPDIR = " $SLURM_TMPDIR

    rm -f testst2* testst1.lck
    cp testst1* $SLURM_TMPDIR
    mkdir $SLURM_TMPDIR/scratch
    cd $SLURM_TMPDIR
    while sleep 6h; do
       echo "Saving data due to time limit ..."
       cp -fv testst2* $SLURM_SUBMIT_DIR 2>/dev/null
    done &
    WPID=$!

    if [[ $EBVERSIONABAQUS -eq 2021 ]]; then
       /cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/unshare \
       --fork --pid --mount-proc --user --map-user $USER \
       abaqus job=testst2 oldjob=testst1 input=$SLURM_SUBMIT_DIR/mystd-sim-restart.inp \
       scratch=$SLURM_TMPDIR/scratch cpus=$SLURM_CPUS_ON_NODE interactive \
       mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB" \
       #gpus=$SLURM_GPUS_ON_NODE  # uncomment this line to use gpu
    elif [[ $EBVERSIONABAQUS -ge 2026 ]]; then
       abaqus job=testst2 oldjob=testst1 input=$SLURM_SUBMIT_DIR/mystd-sim-restart.inp \
       scratch=$SLURM_TMPDIR/scratch cpus=$SLURM_CPUS_ON_NODE interactive \
       mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB" \
       #gpus=$SLURM_GPUS_ON_NODE  # uncomment this line to use gpu
    fi

    { kill $WPID && wait $WPID; } 2>/dev/null
    cp -fv testst2* $SLURM_SUBMIT_DIR
    ````

    The restart input file should contain:
    `*HEADING`
    `*RESTART, READ`

#### Multiple node computing

Users with large memory or compute needs (and correspondingly access to large licenses) can use the following script to perform MPI-based computing over an arbitrary range of nodes, ideally left to the scheduler to automatically determine. A companion template script to perform restart of multinode jobs is not provided due to additional limitations when they can be used. Only abaqus/2026 or newer may be used with this script.

````sh title="scriptsp1-mpi.txt"
!/bin/bash
#SBATCH --account=def-group    # Specify account
#SBATCH --time=00-06:00        # Specify days-hrs:mins
##SBATCH --nodes=2             # Uncomment to specify (optional)
#SBATCH --ntasks=8             # Specify number of cores
#SBATCH --mem-per-cpu=4G       # Specify memory per core
##SBATCH --tasks-per-node=4    # Uncomment to specify (optional)
#SBATCH --cpus-per-task=1      # Do not change !

module load abaqus/2026         # Latest version

unset SLURM_GTIDS
#export MPI_IC_ORDER='tcp'
echo "LM_LICENSE_FILE=$LM_LICENSE_FILE"
echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"

rm -f testsp1-mpi*

unset hostlist
nodes="$(slurm_hl2hl.py --format MPIHOSTLIST | xargs)"
for i in `echo "$nodes" | xargs -n1 | uniq`; do hostlist=${hostlist}$(echo "['${i}',$(echo "$nodes" | xargs -n1 | grep $i | wc -l)],"); done
hostlist="$(echo "$hostlist" | sed 's/,$//g')"
mphostlist="mp_host_list=[$(echo "$hostlist")]"
export $mphostlist
echo "$mphostlist" > abaqus_v6.env

abaqus job=testsp1-mpi input=mystd-sim.inp \
scratch=$SLURM_TMPDIR cpus=$SLURM_NTASKS interactive mp_mode=mpi \
#mp_host_split=1  # number of dmp processes per node >= 1 (uncomment to specify)
````

### Explicit analysis

Abaqus solvers support thread-based and MPI-based parallelization. Scripts for each type are provided below for running explicit analysis type jobs on single or multiple nodes respectively. Template scripts to perform multinode job restarts are not currently provided, pending further testing.

#### Single node computing

=== "project directory script"

    ````sh title="scriptep1.txt"
    #!/bin/bash
    #SBATCH --account=def-group    # specify account
    #SBATCH --time=00-06:00        # days-hrs:mins
    #SBATCH --mem=8000M            # node memory > 5G
    #SBATCH --cpus-per-task=4      # number cores > 1
    #SBATCH --nodes=1              # do not change

    module load abaqus/2026         # Latest version
    #module load StdEnv/2020        # Legacy version
    #module load abaqus/2021        # Discontinue use

    unset SLURM_GTIDS
    export MPI_IC_ORDER='tcp'
    echo "LM_LICENSE_FILE=$LM_LICENSE_FILE"
    echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"

    rm -f testep1* testep2*

    if [[ $EBVERSIONABAQUS -eq 2021 ]]; then
       /cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/unshare \
       --fork --pid --mount-proc --user --map-user $USER \
       abaqus job=testep1 input=myexp-sim.inp \
       scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
       mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB"
    elif [[ $EBVERSIONABAQUS -ge 2026 ]]; then
       abaqus job=testep1 input=myexp-sim.inp \
       scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
       mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB"
    fi
    ````

    To write restart data for a total of 12 time increments, specify in the input file:
    `*RESTART, WRITE, OVERLAY, NUMBER INTERVAL=12, TIME MARKS=NO`
    Check for completed restart information in relevant output files:
    `egrep -i "step|restart" testep*.com testep*.msg testep*.sta`

=== "project directory restart script"

    ````sh title="scriptep2.txt"
    #!/bin/bash
    #SBATCH --account=def-group    # specify account
    #SBATCH --time=00-06:00        # days-hrs:mins
    #SBATCH --mem=8000M            # node memory > 5G
    #SBATCH --cpus-per-task=4      # number cores > 1
    #SBATCH --nodes=1              # do not change

    module load abaqus/2026         # Latest version
    #module load StdEnv/2020        # Legacy version
    #module load abaqus/2021        # Discontinue use

    unset SLURM_GTIDS
    export MPI_IC_ORDER='tcp'
    echo "LM_LICENSE_FILE=$LM_LICENSE_FILE"
    echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"

    rm -f testep2* testep1.lck
    for f in testep1*; do [[ -f ${f} ]] && cp -a "$f" "testep2${f#testep1}"; done

    if [[ $EBVERSIONABAQUS -eq 2021 ]]; then
       /cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/unshare \
       --fork --pid --mount-proc --user --map-user $USER \
       abaqus job=testep2 input=myexp-sim.inp recover \
       scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
       mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB"
    elif [[ $EBVERSIONABAQUS -ge 2026 ]]; then
       abaqus job=testep2 input=myexp-sim.inp recover \
       scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
       mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB"
    fi
    ````

    No input file modifications are required to restart the analysis.

=== "temporary directory script"

    ````sh title="scriptet1.txt"
    #!/bin/bash
    #SBATCH --account=def-group    # specify account
    #SBATCH --time=00-06:00        # days-hrs:mins
    #SBATCH --mem=8000M            # node memory > 5G
    #SBATCH --cpus-per-task=4      # number cores > 1
    #SBATCH --nodes=1              # do not change

    module load abaqus/2026         # Latest version
    #module load StdEnv/2020        # Legacy version
    #module load abaqus/2021        # Discontinue use

    unset SLURM_GTIDS
    export MPI_IC_ORDER='tcp'
    echo "LM_LICENSE_FILE=$LM_LICENSE_FILE"
    echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"
    echo "SLURM_SUBMIT_DIR =" $SLURM_SUBMIT_DIR
    echo "SLURM_TMPDIR = " $SLURM_TMPDIR

    rm -f testet1* testet2*
    cd $SLURM_TMPDIR
    while sleep 6h; do
       cp -f * $SLURM_SUBMIT_DIR 2>/dev/null
    done &
    WPID=$!

    if [[ $EBVERSIONABAQUS -eq 2021 ]]; then
       /cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/unshare \
       --fork --pid --mount-proc --user --map-user $USER \
       abaqus job=testet1 input=$SLURM_SUBMIT_DIR/myexp-sim.inp \
       scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
       mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB"
    elif [[ $EBVERSIONABAQUS -ge 2026 ]]; then
       abaqus job=testet1 input=$SLURM_SUBMIT_DIR/myexp-sim.inp \
       scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
       mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB"
    fi

    { kill $WPID && wait $WPID; } 2>/dev/null
    cp -f * $SLURM_SUBMIT_DIR
    ````

    To write restart data for a total of 12 time increments, specify in the input file:
    `*RESTART, WRITE, OVERLAY, NUMBER INTERVAL=12, TIME MARKS=NO`
    Check for completed restart information in relevant output files:
    `egrep -i "step|restart" testet*.com testet*.msg testet*.sta`

=== "temporary directory restart script"

    ````sh title="scriptet2.txt"
    #!/bin/bash
    #SBATCH --account=def-group    # specify account
    #SBATCH --time=00-06:00        # days-hrs:mins
    #SBATCH --mem=8000M            # node memory > 5G
    #SBATCH --cpus-per-task=4      # number cores > 1
    #SBATCH --nodes=1              # do not change

    module load abaqus/2026         # Latest version
    #module load StdEnv/2020        # Legacy version
    #module load abaqus/2021        # Discontinue use

    unset SLURM_GTIDS
    export MPI_IC_ORDER='tcp'
    echo "LM_LICENSE_FILE=$LM_LICENSE_FILE"
    echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"
    echo "SLURM_SUBMIT_DIR =" $SLURM_SUBMIT_DIR
    echo "SLURM_TMPDIR = " $SLURM_TMPDIR

    rm -f testet2* testet1.lck
    for f in testet1*; do cp -a "$f" $SLURM_TMPDIR/"testet2${f#testet1}"; done
    cd $SLURM_TMPDIR
    while sleep 3h; do
       cp -f * $SLURM_SUBMIT_DIR 2>/dev/null
    done &
    WPID=$!

    if [[ $EBVERSIONABAQUS -eq 2021 ]]; then
       /cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/unshare \
       --fork --pid --mount-proc --user --map-user $USER \
       abaqus job=testet2 input=$SLURM_SUBMIT_DIR/myexp-sim.inp recover \
       scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
       mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB"
    elif [[ $EBVERSIONABAQUS -ge 2026 ]]; then
       abaqus job=testet2 input=$SLURM_SUBMIT_DIR/myexp-sim.inp recover \
       scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
       mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB"
    fi

    { kill $WPID && wait $WPID; } 2>/dev/null
    cp -f  * $SLURM_SUBMIT_DIR
    ````

    No input file modifications are required to restart the analysis.

#### Multiple node computing

Users with large memory or compute needs (and correspondingly access to large licenses) can use the following script to perform MPI-based computing over an arbitrary range of nodes, ideally left to the scheduler to automatically determine. A companion template script to perform restart of multinode jobs is not provided due to additional limitations on how they can be used. Only abaqus/2026 or newer may be used with this script.

````sh title="scriptep1-mpi.txt"
!/bin/bash
#SBATCH --account=def-group    # Specify account
#SBATCH --time=00-06:00        # Specify days-hrs:mins
#SBATCH --ntasks=8             # Specify number of cores
#SBATCH --mem-per-cpu=16000M   # Specify memory per core
# SBATCH --nodes=2             # Specify number of nodes (optional)
#SBATCH --cpus-per-task=1      # Do not change !

module load abaqus/2026        # Latest version

unset SLURM_GTIDS
export MPI_IC_ORDER='tcp'
#export I_MPI_HYDRA_TOPOLIB=ipl
echo "LM_LICENSE_FILE=$LM_LICENSE_FILE"
echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"

rm -f testep1-mpi*

unset hostlist
nodes="$(slurm_hl2hl.py --format MPIHOSTLIST | xargs)"
for i in `echo "$nodes" | xargs -n1 | uniq`; do hostlist=${hostlist}$(echo "['${i}',$(echo "$nodes" | xargs -n1 | grep $i | wc -l)],"); done
hostlist="$(echo "$hostlist" | sed 's/,$//g')"
mphostlist="mp_host_list=[$(echo "$hostlist")]"
export $mphostlist
echo "$mphostlist" > abaqus_v6.env

abaqus job=testep1-mpi input=myexp-sim.inp \
scratch=$SLURM_TMPDIR cpus=$SLURM_NTASKS interactive mp_mode=mpi \
#mp_host_split=1  # number of dmp processes per node >= 1 (uncomment to specify)
````

### Memory estimates

#### Single process

An estimate for the total Slurm node memory (`--mem=`) required for a simulation to run fully in RAM (without being virtualized to scratch disk) can be obtained by examining the Abaqus output `test.dat` file. For example, a simulation that requires a fairly large amount of memory might show:

```bash
                   M E M O R Y   E S T I M A T E

  PROCESS      FLOATING PT       MINIMUM MEMORY        MEMORY TO
              OPERATIONS           REQUIRED          MINIMIZE I/O
             PER ITERATION           (MB)               (MB)

     1          1.89E+14             3612              96345
```

Alternatively, a total memory estimate for a single node threaded process can be obtained by running the simulation interactively on a compute node and then monitoring the memory use with the `top` (or `ps`) command as follows:
1) First, obtain an allocation on a compute node and start your simulation running:

```bash
salloc --time=0:30:00 --cpus-per-task=8 --mem=64G --account=def-piname
module load StdEnv/2020
module load abaqus/2021
unset SLURM_GTIDS
abaqus job=test input=Sample.inp scratch=$SLURM_TMPDIR cpus=8 mp_mode=threads interactive
```

2) Next, SSH into the compute node (c50 according to the `sq` command) and then run `top`, i.e.:

```bash
ssh c50
top -u $USER
```

3) Watch the `VIRT` and `RES` columns until steady peak memory values are observed.

To completely satisfy the recommended "MEMORY TO OPERATIONS REQUIRED MINIMIZE I/O" (MRMIO) value, at least the same amount of non-swapped physical memory (RES) must be available to Abaqus. Since the RES will in general be less than the virtual memory (VIRT) by some relatively constant amount for a given simulation, it is necessary to slightly over-allocate the requested Slurm node memory `--mem=`. In the above sample Slurm script, this over-allocation has been hardcoded to a conservative value of 3072MB based on initial testing of the standard Abaqus solver. To avoid long queue wait times associated with large values of MRMIO, it may be worth investigating the simulation performance impact associated with reducing the RES memory that is made available to Abaqus significantly below the MRMIO. This can be done by lowering the `--mem=` value, which in turn will set an artificially low value of `memory=` in the Abaqus command (found in the last line of the script). In doing this, the RES cannot dip below the MINIMUM MEMORY REQUIRED (MMR), otherwise Abaqus will exit due to Out of Memory (OOM). As an example, if your MRMIO is 96GB, try running a series of short test jobs with `#SBATCH --mem=8G, 16G, 32G, 64G` until an acceptable minimal performance impact is found, noting that smaller values will result in increasingly larger scratch space used by temporary files.

#### Multi process

To determine the required Slurm memory for multi-node Slurm scripts, memory estimates (per compute process) required to minimize I/O are given in the output dat file of completed jobs. If `mp_host_split` is not specified (or is set to 1) then the total number of compute processes will equal the number of nodes. The `mem-per-cpu` value can then be roughly determined by multiplying the largest memory estimate by the number of nodes and then dividing by the number of `ntasks`. However, if a value for `mp_host_split` is specified (greater than 1) then the `mem-per-cpu` value can be roughly determined from the largest memory estimate times the number of nodes times the value of `mp_host_split` divided by the number of tasks. Note that `mp_host_split` must be less than or equal to the number of cores per node assigned by Slurm at runtime, otherwise Abaqus will terminate. This scenario can be controlled by uncommenting to specify a value for tasks-per-node. The following definitive statement is given in every output dat file and mentioned here for reference:

```
 THE UPPER LIMIT OF MEMORY THAT CAN BE ALLOCATED BY ABAQUS WILL IN GENERAL DEPEND ON THE VALUE OF
 THE "MEMORY" PARAMETER AND THE AMOUNT OF PHYSICAL MEMORY AVAILABLE ON THE MACHINE. PLEASE SEE
 THE "ABAQUS ANALYSIS USER'S MANUAL" FOR MORE DETAILS. THE ACTUAL USAGE OF MEMORY AND OF DISK
 SPACE FOR SCRATCH DATA WILL DEPEND ON THIS UPPER LIMIT AS WELL AS THE MEMORY REQUIRED TO MINIMIZE
 I/O. IF THE MEMORY UPPER LIMIT IS GREATER THAN THE MEMORY REQUIRED TO MINIMIZE I/O, THEN THE ACTUAL
 MEMORY USAGE WILL BE CLOSE TO THE ESTIMATED "MEMORY TO MINIMIZE I/O" VALUE, AND THE SCRATCH DISK
 USAGE WILL BE CLOSE-TO-ZERO; OTHERWISE, THE ACTUAL MEMORY USED WILL BE CLOSE TO THE PREVIOUSLY
 MENTIONED MEMORY LIMIT, AND THE SCRATCH DISK USAGE WILL BE ROUGHLY PROPORTIONAL TO THE DIFFERENCE
 BETWEEN THE ESTIMATED "MEMORY TO MINIMIZE I/O" AND THE MEMORY UPPER LIMIT. HOWEVER ACCURATE
 ESTIMATE OF THE SCRATCH DISK SPACE IS NOT POSSIBLE.
```

## Graphical use

It is recommended to use an OpenOnDemand or JupyterLab to run graphical applications at the Alliance.

### OnDemand

1.  Start an OnDemand desktop session by clicking one of the following OnDemand links:
    [Nibi](../clusters/nibi.md#access-through-open-ondemand-ood): `https://ondemand.sharcnet.ca`
    TRILLIUM: `https://ondemand.scinet.utoronto.ca`

2.  Open a new terminal window within your desktop and load:
    ```bash
    module load abaqus/2026
    ```

3.  Start the application in graphical mode using the `cae` option. If you are on either: 1) a node without a GPU or 2) a node with a GPU but without VirtualGL support, then append to use the `mesa` option:
    ```bash
    abaqus cae -mesa
    ```

4.  If you require better graphical performance and are on a node with a GPU and VirtualGL support, then start Abaqus without the `-mesa` option. When using the Nibi OnDemand desktop, a full h100 (80GB) GPU from the GPU pulldown must be selected.
    ```bash
    abaqus cae
    ```

5.  To start Abaqus in GUI mode, there must be at least **one** unused CA license according to:

    ```bash
    abaqus licensing lmstat -c $ABAQUSLM_LICENSE_FILE -a | grep "Users of cae"
    ```
    Users of cae: (Total of 4 licenses issued; Total of 3 licenses in use)

### JupyterLab

1.  Start a JupyterHub desktop session by clicking one of the following JupyterHub links:
    FIR: `https://jupyterhub.fir.alliancecan.ca`
    NARVAL: `https://portail.narval.calculquebec.ca/`
    RORQUAL: `https://jupyterhub.rorqual.alliancecan.ca`
2.  Highlight an Abaqus module such as `abaqus/2026` in the left-hand side *Available Module* section.
3.  Click on *Load* for the highlighted module and an `Abaqus (VNC)` icon will appear in the desktop.
4.  Click on the icon and Abaqus should automatically be started in a remote Jupyter desktop.

### VncViewer

This approach is considered obsolete; please use the above OnDemand/JupyterHub desktop instead.

1.  Connect with a VncViewer client to a login or compute node without a GPU by following [TigerVNC](../interactive/vnc.md).
2.  Open a new terminal window and enter the following:
    ```bash
    module load abaqus/2026
    ```
3.  Start the application with:
    ```bash
    abaqus cae -mesa
    ```

## Site-specific use

### SHARCNET license

!!! warning
    The `abaqus.lic` file given below no longer works since the license4 machine has been shut down and retired. Therefore, all Abaqus license checkout requests on the Dusky cluster from the Western/Robarts Abaqus license server currently will fail. A replacement server for license4 is currently being worked on. Once it is ready for use, `abaqus.lic` will be updated with the new server name and this red warning message removed. In the meantime, the SHARCNET License may be used instead by following the procedure above to request access.

The SHARCNET license has been renewed until 17-Jan-2027 and is operational. It provides a small shared free pool consisting of 3 CAE and 54 execute tokens for all researchers. Maximum usage limits are currently set at: 1cae/user, 10 tokens/user and 15 tokens/group. These free tokens are available on a first-come, first-serve basis and are mainly intended for testing and light usage before deciding whether or not to purchase dedicated tokens. Costs for dedicated tokens (in 2021) were approximately CAD$110 per compute token and CAD$400 per GUI token: submit a ticket to request an official quote if interested. The free SHARCNET license can be used by any registered Alliance researcher, but only on SHARCNET hardware, and only after agreeing to the below Academic License User Agreement. Groups that purchase dedicated tokens to run on the SHARCNET license server may likewise ONLY use them on SHARCNET hardware (as dictated by the negotiated license agreement with Simulia) including the SHARCNET [OOD](../clusters/nibi.md#access-through-open-ondemand-ood) system (to run Abaqus in graphical mode) or Nibi/Dusky clusters (for submitting compute batch jobs to the queue). Before you can use the license, you must contact [technical support](../support/technical_support.md) and request access. In your email, 1) mention that it is for use on SHARCNET systems and 2) include a copy/paste of the following `License Agreement` statement with your full name and username entered in the indicated locations. Please note that every user must do this; it cannot be done one time only for a group; this includes PIs who have purchased their own dedicated tokens.

#### License agreement

```
----------------------------------------------------------------------------------
Subject: Abaqus SHARCNET Academic License User Agreement

This email is to confirm that i "_____________" with username "___________" will
only use “SIMULIA Academic Software” with tokens from the SHARCNET license server
for the following purposes:

1) on SHARCNET hardware where the software is already installed;
2) in affiliation with a Canadian degree-granting academic institution;
3) for education, institutional or instruction purposes and not for any commercial
   or contract-related purposes where results are not publishable;
4) for experimental, theoretical and/or digital research work, undertaken primarily
   to acquire new knowledge of the underlying foundations of phenomena and observable
   facts, up to the point of proof-of-concept in a laboratory.
-----------------------------------------------------------------------------------
```

#### Configure license file

Configure your license file as follows, noting that it is only usable on SHARCNET systems such as the Nibi and Dusky clusters or the SHARCNET OOD desktop system. Note that the old `license3.sharcnet.ca` server has been permanently shut down; you must update your `abaqus.lic` file as follows to use the free SHARCNET license:

```bash
[l2 (nibi login node):~] cat ~/.licenses/abaqus.lic
prepend_path("ABAQUSLM_LICENSE_FILE","27050@license1.computecanada.ca")
```

If your Abaqus job fails with the error message `[*** ABAQUS/eliT_CheckLicense rank 0 terminated by signal 11 (Segmentation fault)]` then verify your `abaqus.lic` file contains `ABAQUSLM_LICENSE_FILE` when using `abaqus/202X` modules. If your Abaqus jobs fails with error message `[License server machine is down or not responding, etc.]` and you are using `abaqus/6.14.1`, then replace `ABAQUSLM_LICENSE_FILE` with `LM_LICENSE_FILE`.

#### Query license server

Log into the Nibi cluster, load Abaqus, and run one of the following:

```bash
ssh nibi.alliancecan.ca
module load StdEnv/2020
module load abaqus
```

I) Check the SHARCNET license server for started and queued jobs:

```bash
abaqus licensing lmstat -c $ABAQUSLM_LICENSE_FILE -a | egrep "Users|start|queued"
```

II) Check the SHARCNET license server for started and queued jobs also showing reservations by purchasing groups:

```bash
abaqus licensing lmstat -c $ABAQUSLM_LICENSE_FILE -a | egrep "Users|start|queued|RESERVATION"
```

III) Check the SHARCNET license server for only CAE, standard and explicit product availability:
```bash
abaqus licensing lmstat -c $ABAQUSLM_LICENSE_FILE -a | grep "Users of" | egrep "cae|standard|explicit"
```

When the output of query I) above indicates that a job for a particular username is queued, this means the job has entered the "R"unning state from the perspective of `squeue -j jobid` or `sacct -j jobid` and is therefore idle on a compute node waiting for a license. This will have the same impact on your account priority as if the job were performing computations and consuming CPU time. Eventually, when sufficient licenses become available, the queued job will start.

##### Example

The following shows the situation where a user submitted two 6-core jobs (each requiring 12 tokens) in quick succession. The scheduler then started each job on a different node in the order they were submitted. Since the user had 10 Abaqus compute tokens, the first job (27527287) was able to acquire exactly enough (10) tokens for the solver to begin running. The second job (27527297), not having access to any more tokens, entered an idle "queued" state (as can be seen from the lmstat output) until the first job completed, wasting the available resources and depreciating the user's fair share level in the process...

```
[l2 (nibi login node):~] sq
            JOBID     USER              ACCOUNT           NAME  ST  TIME_LEFT NODES CPUS TRES_PER_N MIN_MEM NODELIST (REASON)
         27530366  roberpj         cc-debug_cpu  scriptsp2.txt   R    9:56:13     1    6        N/A      8G     c107  (None)
         27530407  roberpj         cc-debug_cpu  scriptsp2.txt   R    9:59:37     1    6        N/A      8G     c292  (None)
```

```
[l2 (nibi login node):~] abaqus licensing lmstat -c $ABAQUSLM_LICENSE_FILE -a | egrep "Users|start|queued"
 Users of abaqus:  (Total of 78 licenses issued;  Total of 53 licenses in use)
    roberpj c107 /dev/tty (v62.6) (license3.sharcnet.ca/27050 1042), start Mon 11/25 17:15, 10 licenses
    roberpj c292 /dev/tty (v62.6) (license3.sharcnet.ca/27050 125) queued for 10 licenses
```

To avoid license shortage problems when submitting multiple jobs when working with expensive Abaqus tokens, either use a [job dependency](../running-jobs/running_jobs.md#cancellation-of-jobs-with-dependency-conditions-which-cannot-be-met), [job array](../running-jobs/job_arrays.md) or at the very least set up a Slurm [email notification](../running-jobs/monitoring_jobs.md#email-notification) to know when your job completes before manually submitting another one. There are two easier options for dealing with this situation:

Option 1)

Disable non-interactive (analysis) jobs from starting on a cluster compute node after being submitted to the queue and then becoming idle (when not enough tokens are unavailable, this is the default behaviour). Create a text file in your submit directory (before submitting the job) with the following one-line contents and the job will instead terminate immediately.

```bash
[l2 (nibi login node):~/submitdirectory] cat abaqus_v6.env
lmlicensequeuing=OFF
```

When a job immediately terminates (without entering a QUEUED state to wait for a license), the end of the corresponding Slurm output file will contain messages such as:

```
Abaqus 2026
Checkout exceeds MAX specified in options file.
FlexNet Licensing error:-87,147
Number of requested licenses: 14
Number of total licenses:     78
Number of licenses in use:    14
Number of available licenses: 64
This may be due to insufficient licenses.
ValueError: not enough values to unpack (expected 2, got 1)
During handling of the above exception, another exception occurred:
Exception: DriverLM: can't parse host/port from umbrella
Abaqus Error: Error checking out Abaqus license.
Abaqus/Analysis exited with errors
```

Option 2)

Specify a setting in minutes so that a started job will enter a QUEUED state to wait for a license before being automatically DEQUEUED and terminating if a license does not become available in time.

```bash
[l2 (nibi login node):~/submitdirectory] cat abaqus_v6.env
lmhanglimit=1
```

When a job terminates this way, after being queued and no license becomes available in the specified time according to the `lmhanlimit` value (1 minute in this example), the messages at the end of the Slurm output file will instead appear as:

```
Abaqus 2026
"standard" license request queued for the License Server on license1.computecanada.ca.
Total time in queue: 0 seconds.
"standard" license request queued for the License Server on license1.computecanada.ca.
Total time in queue: 30 seconds.
"standard" license request queued for the License Server on license1.computecanada.ca.
Total time in queue: 60 seconds.
Time limit of in queue has been exceeded. Exiting.
This may be due to insufficient licenses.
ValueError: not enough values to unpack (expected 2, got 1)
During handling of the above exception, another exception occurred:
Exception: DriverLM: can't parse host/port from umbrella
Abaqus Error: Error checking out Abaqus license.
Abaqus/Analysis exited with errors
```

##### Specify job resources

To ensure optimal usage of both your Abaqus tokens and our resources, it's important to carefully specify the required memory and ncpus in your Slurm script. The values can be determined by submitting a few short test jobs to the queue then checking their utilization. For **completed** jobs, use `seff JobNumber` to show the total *Memory Utilized* and *Memory Efficiency*. If the *Memory Efficiency* is less than ~90%, decrease the value of the `#SBATCH --mem=` setting in your Slurm script accordingly. Notice that the `seff JobNumber` command also shows the total *CPU (time) Utilized* and *CPU Efficiency*. If the *CPU Efficiency* is less than ~90%, perform scaling tests to determine the optimal number of CPUs for optimal performance and then update the value of `#SBATCH --cpus-per-task=` in your Slurm script. For **running** jobs, use the `srun --overlap --jobid=29821580 --pty top -d 5 -u $USER` command to watch the %CPU, %MEM and RES for each Abaqus parent process on the compute node. The %CPU and %MEM columns display the percent usage relative to the total available on the node while the RES column shows the per process resident memory size (in human readable format for values over 1GB). Further information regarding how to [monitor jobs](../running-jobs/monitoring_jobs.md) is available on our documentation wiki.

##### Core-token mapping

```
TOKENS 5  6  7  8  10  12  14  16  19  21  25  28  34  38
CORES  1  2  3  4   6   8  12  16  24  32  48  64  96 128
```

where TOKENS = floor[5 X CORES^0.422]

Each GPU used requires 1 additional TOKEN.

### Western license

!!! warning
    The `abaqus.lic` file given below no longer works since the license4 machine has been shut down and retired. Therefore, all Abaqus license checkout requests on the Dusky cluster from the Western/Robarts Abaqus license server currently will fail. A replacement server for license4 is currently being worked on. Once it is ready for use, `abaqus.lic` will be updated with the new server name and this red warning message removed. In the meantime, the SHARCNET License may be used instead by following the procedure above to request access.

The Western site license may only be used by Western researchers on hardware located at Western's campus. Currently, only the Dusky cluster satisfies this condition. Nibi and SHARCNET OOD system are excluded since they are located on Waterloo's campus. Contact the Western Abaqus license server administrator <jmilner@robarts.ca> to inquire about using the Western Abaqus license. You will need to provide your username and possibly make arrangements to purchase tokens. If you are granted access, then you may proceed to configure your `abaqus.lic` file to point to the Western license server:

#### Configure license file

```bash
[dus241:~] cat .licenses/abaqus.lic
prepend_path("LM_LICENSE_FILE","27000@license4.sharcnet.ca")
prepend_path("ABAQUSLM_LICENSE_FILE","27000@license4.sharcnet.ca")
```

Once configured, submit your job as described in the *Cluster job submission* section above. If there are any problems, submit a problem ticket to [technical support](../support/technical_support.md). Specify that you are using the Abaqus Western license on Dusky and provide the failed job number along with a paste of any error messages as applicable.