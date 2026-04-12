---
title: "Abaqus"
slug: "abaqus"
lang: "base"

source_wiki_title: "Abaqus"
source_hash: "bae677694481cbfac8c6cf3d17e3b911"
last_synced: "2026-04-10T14:10:18.226633+00:00"
last_processed: "2026-04-10T14:32:13.724897+00:00"

tags:
  - software

keywords:
  - "job failures"
  - "Compute node"
  - "SBATCH"
  - "failed job number"
  - "Academic License User Agreement"
  - "lmstat"
  - "User Agreement"
  - "terminated early"
  - "SHARCNET Academic License"
  - "cc-debug_cpu"
  - "restart scripts"
  - "MPI scripts"
  - "Western license"
  - "Slurm memory"
  - "salloc"
  - "SLURM_SUBMIT_DIR"
  - "Job restarts"
  - "parallelization"
  - "MRMIO"
  - "Abaqus solvers"
  - "restart input file"
  - "input file"
  - "restart script"
  - "Job submission"
  - "memory estimate"
  - "dusky"
  - "Technical support"
  - "temporary directory"
  - "single node threaded process"
  - "SHARCNET"
  - "Multiple node computing"
  - "Slurm scripts"
  - "JupyterLab"
  - "ABAQUSLM_LICENSE_FILE"
  - "restart data"
  - "abaqus"
  - "License configuration"
  - "hostlist"
  - "OnDemand desktop"
  - "explicit analysis"
  - "single node computing"
  - "unshare"
  - "configure license file"
  - "Core token mapping"
  - "EBVERSIONABAQUS"
  - "Abaqus"
  - "SIMULIA Academic Software"
  - "Restart analysis"
  - "Memory estimates"
  - "completed restart information"
  - "OpenOnDemand"
  - "tokens"
  - "MPI-based computing"
  - "Memory estimate"
  - "Multi process"
  - "license server"
  - "Slurm"
  - "Temporary directory"
  - "Finite element analysis"
  - "licenses in use"
  - "simulation"
  - "Scratch disk space"
  - "NODELIST"
  - "Job resources"
  - "slurm_hl2hl.py"
  - "Graphical applications"
  - "Abaqus Western license"
  - "interactive simulation"
  - "compute node"
  - "LM_LICENSE_FILE"
  - "SLURM_TMPDIR"
  - "hardware failure"
  - "education purposes"
  - "time increments"
  - "SLURM"
  - "Standard analysis"
  - "Cluster job submission"
  - "Restart input file"
  - "Slurm script"
  - "SLURM_GTIDS"
  - "abaqus.lic"
  - "Abaqus tokens"
  - "myexp-sim.inp"
  - "SHARCNET license"
  - "Abaqus FEA"
  - "MPI_IC_ORDER"
  - "Single node computing"
  - "abaqus licensing"
  - "bash script"

questions:
  - "How must a user configure their license file and network settings to successfully run Abaqus on the cluster?"
  - "What improvements and necessary script updates are associated with the transition to the new abaqus/2026 module?"
  - "What are the recommended Slurm job submission strategies for handling long-running simulations and large restart files?"
  - "What is the primary purpose of the restart scripts discussed in the text?"
  - "What are the specific scenarios mentioned that can cause a job to fail and terminate early?"
  - "How can a user configure other types of restarts to add steps or modify the analysis?"
  - "Why is it recommended to run short scaling test jobs before executing long simulations?"
  - "What types of parallelization do Abaqus solvers support, and when should a user utilize multiple node MPI scripts?"
  - "How can a user configure the Abaqus input file to write restart data at specific time increments?"
  - "How does the script specify the required hardware resources, such as node types and GPUs, for the job?"
  - "Which version of the Abaqus software is being loaded, and what legacy versions are mentioned as discontinued or alternatives?"
  - "What environment variables are modified or printed, and what specific file cleanup actions are performed in the script?"
  - "How does the script differentiate the execution commands for Abaqus version 2021 compared to version 2026?"
  - "What mechanism is implemented in the bash script to periodically back up data from the temporary directory to the submit directory during a long-running job?"
  - "What specific parameters must be added to the Abaqus input file to control the frequency and method of reading and writing restart data?"
  - "How does the script configure SLURM directives for resource allocation, such as memory, CPUs, and time limits, for an Abaqus job?"
  - "What are the differences in the execution commands when running Abaqus version 2021 compared to version 2026 or newer?"
  - "What are the specific requirements and limitations mentioned for performing multi-node MPI-based computing with Abaqus?"
  - "How do you configure the input file to write restart data at a specific frequency of time increments?"
  - "What parameters must be specified to write restart data for a fixed total number of time intervals?"
  - "Which command can be used to verify the completed restart information in the output files?"
  - "What is the purpose of echoing the LM_LICENSE_FILE and ABAQUSLM_LICENSE_FILE environment variables in this script?"
  - "Why does the script execute the command to remove files matching the pattern testsp1-mpi*?"
  - "How does the script process the Slurm node list using slurm_hl2hl.py to generate the formatted hostlist variable?"
  - "What types of parallelization do Abaqus solvers support for explicit analysis?"
  - "How do the provided SLURM scripts handle the execution differences between Abaqus versions 2021 and 2026?"
  - "What specific parameters must be specified in the input file to write restart data for a given number of time increments?"
  - "What is the purpose of the initial file cleanup and copying process involving the \"testep1\" and \"testep2\" files?"
  - "Why does the script require the use of the `unshare` utility specifically when running Abaqus version 2021?"
  - "How are Slurm environment variables utilized to allocate resources and define the scratch directory for the Abaqus job execution?"
  - "How do the provided scripts utilize the SLURM temporary directory to manage file I/O and periodically back up data during the job execution?"
  - "What specific command differences are implemented in the scripts to handle the execution of Abaqus version 2021 compared to versions 2026 and newer?"
  - "What parameters must be specified in the Abaqus input file to write restart data, and how does the restart script prepare previous job files for the new run?"
  - "What environment variables are being logged at the beginning of the script?"
  - "How does the script handle the copying and renaming of the initial input files to the temporary directory?"
  - "What is the purpose of the background loop that executes every 3 hours?"
  - "What version of Abaqus is required for multiple node computing, and what is the stated limitation regarding restarting these jobs?"
  - "How does the provided Slurm script dynamically generate and configure the MPI host list for a multi-node Abaqus job?"
  - "What are the two methods described for estimating the total memory required for a simulation to run fully in RAM without virtualizing to a scratch disk?"
  - "How can a user balance Abaqus simulation performance and queue wait times by adjusting the requested Slurm node memory relative to the MRMIO?"
  - "How should the required mem-per-cpu be calculated for multi-node Abaqus jobs, particularly when the mp_host_split parameter is specified?"
  - "What are the recommended platforms and steps for accessing Abaqus through a graphical user interface?"
  - "How can a user obtain a total memory estimate for a single node threaded process?"
  - "Which commands are recommended for monitoring the memory usage of the running simulation?"
  - "What is the first step and the corresponding command syntax required to obtain an allocation on a compute node?"
  - "What limitation does the text mention regarding the estimation of scratch disk space?"
  - "Which platforms are recommended for running graphical applications at the Alliance?"
  - "How does a user initiate an OnDemand desktop session for Nibi?"
  - "What are the recommended methods and specific steps for launching the Abaqus graphical interface via Open OnDemand or JupyterLab?"
  - "Under what hardware conditions must a user append the \"-mesa\" option when starting Abaqus from the terminal?"
  - "What are the token limits, hardware restrictions, and mandatory agreement procedures required to utilize the SHARCNET Abaqus license?"
  - "What specific software and license server are governed by this user agreement?"
  - "What are the hardware and institutional affiliation requirements for a user to be eligible for this license?"
  - "What are the permitted and prohibited purposes for using the software under this agreement?"
  - "How must the abaqus.lic file be configured to properly connect to the new SHARCNET license server?"
  - "What environment variables need to be checked or modified if an Abaqus job fails with a segmentation fault or a license server connection error?"
  - "How can a user query the license server for job statuses, and what are the consequences on account priority if a job is queued waiting for a license?"
  - "What methods can be used to avoid license shortage problems when submitting multiple Abaqus jobs?"
  - "How can users monitor and optimize the memory and CPU efficiency of their completed and running jobs?"
  - "What are the current hardware restrictions and operational status of the Western Abaqus site license?"
  - "What are the resource allocations and statuses of the compute jobs running under the user \"roberpj\"?"
  - "What command was executed on the login node to query the software licensing information?"
  - "How many Abaqus licenses are currently issued and how many are actively in use?"
  - "What initial steps, such as providing a username and purchasing tokens, are required to be granted access?"
  - "Which specific file must be configured to point to the Western license server?"
  - "What are the exact environment variable paths and server address details that need to be added to the license configuration file?"
  - "How should a user submit their job once the configuration is complete?"
  - "What action should be taken if a problem occurs after submitting a job?"
  - "What specific details and information must be included when submitting a problem ticket to technical support?"
  - "How should a user submit their job once the configuration is complete?"
  - "What action should be taken if a problem occurs after submitting a job?"
  - "What specific details and information must be included when submitting a problem ticket to technical support?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Abaqus FEA](https://www.3ds.com/products-services/simulia/products/abaqus/) is a software suite for finite element analysis and computer-aided engineering.

## Licensing

### Using your license file

Abaqus software modules are available on our clusters; however, you must provide your own license. To configure your account on a cluster, log in and create a file named ``$HOME/.licenses/abaqus.lic`` containing the following line. Next, replace ``port@server`` with the FlexLM port number and server IP address (or fully qualified hostname) of your Abaqus license server. If you want to use legacy version 6.14.1 then replace ABAQUSLM_LICENSE_FILE with LM_LICENSE_FILE.

```text title="abaqus.lic"
prepend_path("ABAQUSLM_LICENSE_FILE","port@server")
```

If your license has not been set up for use on an Alliance cluster, some additional configuration changes by the Alliance system administrator and your local system administrator will need to be done. Such changes are necessary to ensure the FlexLM and vendor TCP ports of your Abaqus server are reachable from all cluster compute nodes when jobs are run via the queue. For us to help you get this done, write to [technical support](../support/technical_support.md). Please be sure to include the following three items:

*   FlexLM port number
*   static vendor port number
*   IP address of your Abaqus license server

You will then be sent a list of cluster IP addresses so that your administrator can open the local server firewall to allow connections from the cluster on both ports. Please note that a special license agreement must generally be negotiated and signed by SIMULIA and your institution before a local license may be used remotely on Alliance hardware.

### FLEXnet/DSLS Servers

Similar to previously installed modules, the `abaqus/2026` module is configured by default to work with Simulia ``FLEXnet`` license servers such as the free SHARCNET license server. To use a local ``DSLS`` based institutional license server, two small text files, ``abaqus_v6.env`` and ``DSLicSrv.txt``, should be created in your simulation submit directory as follows. These will be read automatically when Abaqus starts running to reconfigure itself accordingly.

```text
[l2 (login node):~/mysimdir] cat abaqus_v6.env
 license_server_type=DSLS
 dsls_license_config="DSLicSrv.txt"
```

```text
[l2 (login node):~/mysimdir] DSLicSrv.txt
 YOUR-SERVER-HOSTNAME:PORT-NUMBER
```

## Version compatibility

### Module change

!!! warning "Module Change"
    A new module for `abaqus/2026` is now installed into the default StdEnv/2023 environment. This new version resolves the *** buffer overflow detected *** error with `abaqus/2021` on all recent clusters. Note that each Slurm script on this wiki page has been updated to work with both `abaqus/2026` and `abaqus/2021` where possible, therefore all personal Slurm scripts should likewise be updated by researchers. The `abaqus/2026` module contains the initial *Abaqus 2026 Golden* release. Another module named `abaqus/2026.2606` containing *Abaqus 2026 FP.CFA.2606* level updates will be installed next.

## Cluster job submission

Below are prototype Slurm scripts for submitting thread and MPI-based parallel simulations to single or multiple compute nodes. Most users will find it sufficient to use one of the **project directory scripts** provided in the *Single node computing* sections. The optional ``memory=`` argument found in the last line of the scripts is intended for larger memory or problematic jobs where the 3072MB offset value may require tuning. A listing of all Abaqus command line arguments can be obtained by loading an Abaqus module and running: `abaqus -help | less`.

Single node jobs that run less than one day should find the *project directory script* located in the first tab sufficient. However, single node jobs that run for more than a day should use one of the restart scripts. Jobs that create large restart files will benefit by writing to the local disk through the use of the `SLURM_TMPDIR` environment variable utilized in the **temporary directory scripts** provided in the two rightmost tabs of the single node standard and explicit analysis sections. The restart scripts shown here will continue jobs that have been terminated early for some reason. Such job failures can occur if a job reaches its maximum requested runtime before completing and is killed by the queue or if the compute node the job was running on crashed due to an unexpected hardware failure. Other restart types are possible by further tailoring of the input file (not shown here) to continue a job with additional steps or change the analysis (see the documentation for version specific details).

Jobs that require large memory or larger compute resources (beyond that which a single compute node can provide) should use the MPI scripts in the **multiple node sections** below to distribute computing over arbitrary node ranges determined automatically by the scheduler. Short scaling test jobs should be run to determine wall-clock times (and memory requirements) as a function of the number of cores (2, 4, 8, etc.) to determine the optimal number before running any long jobs.

### Standard analysis
Abaqus solvers support thread-based and MPI-based parallelization. Scripts for each type are provided below for running Standard Analysis type jobs on Single or Multiple nodes respectively. Scripts to perform multiple node job restarts are not currently provided.

#### Single node computing

=== "Project Directory Script"
    ```bash title="scriptsp1.txt"
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
    ```

    To write restart data every N=12 time increments, specify in the input file:
    ```
    *RESTART, WRITE, OVERLAY, FREQUENCY=12
    ```
    To write restart data for a total of 12 time increments, specify instead:
    ```
    *RESTART, WRITE, OVERLAY, NUMBER INTERVAL=12, TIME MARKS=NO
    ```
    To check for completed restart information, do:
    ```bash
    egrep -i "step|start" testsp*.com testsp*.msg testsp*.sta
    ```
    Some simulations may benefit by adding the following to the Abaqus command at the bottom of the script:
    ```
    order_parallel=OFF
    ```

=== "Project Directory Restart Script"
    ```bash title="scriptsp2.txt"
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
    ```

    The restart input file should contain:
    ```
    *HEADING
    *RESTART, READ
    ```

=== "Temporary Directory Script"
    ```bash title="scriptst1.txt"
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
    ```

    To write restart data every N=12 time increments, specify in the input file:
    ```
    *RESTART, WRITE, OVERLAY, FREQUENCY=12
    ```
    To write restart data for a total of 12 time increments, specify instead:
    ```
    *RESTART, WRITE, OVERLAY, NUMBER INTERVAL=12, TIME MARKS=NO
    ```
    To check the completed restart information, do:
    ```bash
    egrep -i "step|start" testst*.com testst*.msg testst*.sta
    ```

=== "Temporary Directory Restart Script"
    ```bash title="scriptst2.txt"
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
    ```

    The restart input file should contain:
    ```
    *HEADING
    *RESTART, READ
    ```

#### Multiple node computing

Users with large memory or compute needs (and correspondingly access to large licenses) can use the following script to perform MPI-based computing over an arbitrary range of nodes, ideally left to the scheduler to automatically determine. A companion template script to perform restarts of multinode jobs is not provided due to additional limitations when they can be used. Only `abaqus/2026` or newer may be used with this script.

```bash title="scriptsp1-mpi.txt"
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
```

### Explicit analysis

Abaqus solvers support thread-based and MPI-based parallelization. Scripts for each type are provided below for running explicit analysis type jobs on single or multiple nodes respectively. Template scripts to perform multinode job restarts are not currently provided pending further testing.

#### Single node computing

=== "Project Directory Script"
    ```bash title="scriptep1.txt"
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
    ```

    To write restart data for a total of 12 time increments, specify in the input file:
    ```
    *RESTART, WRITE, OVERLAY, NUMBER INTERVAL=12, TIME MARKS=NO
    ```
    Check for completed restart information in relevant output files:
    ```bash
    egrep -i "step|restart" testep*.com testep*.msg testep*.sta
    ```

=== "Project Directory Restart Script"
    ```bash title="scriptep2.txt"
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
    ```

    No input file modifications are required to restart the analysis.

=== "Temporary Directory Script"
    ```bash title="scriptet1.txt"
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
    ```

    To write restart data for a total of 12 time increments, specify in the input file:
    ```
    *RESTART, WRITE, OVERLAY, NUMBER INTERVAL=12, TIME MARKS=NO
    ```
    Check for completed restart information in relevant output files:
    ```bash
    egrep -i "step|restart" testet*.com testet*.msg testet*.sta
    ```

=== "Temporary Directory Restart Script"
    ```bash title="scriptet2.txt"
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
    ```

    No input file modifications are required to restart the analysis.

#### Multiple node computing

Users with large memory or compute needs (and correspondingly access to large licenses) can use the following script to perform MPI-based computing over an arbitrary range of nodes, ideally left to the scheduler to automatically determine. A companion template script to perform restarts of multinode jobs is not provided due to additional limitations how they can be used. Only `abaqus/2026` or newer may be used with this script.

```bash title="scriptep1-mpi.txt"
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
```

### Memory estimates

#### Single process

An estimate for the total Slurm node memory (`--mem=`) required for a simulation to run fully in RAM (without being virtualized to scratch disk) can be obtained by examining the Abaqus output ``test.dat`` file. For example, a simulation that requires a fairly large amount of memory might show:

```text
                   M E M O R Y   E S T I M A T E
  
 PROCESS      FLOATING PT       MINIMUM MEMORY        MEMORY TO
              OPERATIONS           REQUIRED          MINIMIZE I/O
             PER ITERATION           (MB)               (MB)
  
     1          1.89E+14             3612              96345
```

Alternatively, a total memory estimate for a single node threaded process can be obtained by running the simulation interactively on a compute node and then monitoring the memory use with the `top` (or `ps`) command as follows:
1.  First, obtain an allocation on a compute node and start your simulation running:

    ```bash
    salloc --time=0:30:00 --cpus-per-task=8 --mem=64G --account=def-piname
    module load StdEnv/2020
    module load abaqus/2021
    unset SLURM_GTIDS
    abaqus job=test input=Sample.inp scratch=$SLURM_TMPDIR cpus=8 mp_mode=threads interactive
    ```

2.  Next, SSH into the compute node (c50 according to the `sq` command) and then run `top`, i.e.,

    ```bash
    ssh c50
    top -u $USER
    ```

3.  Watch the **VIRT** and **RES** columns until steady peak memory values are observed.

To completely satisfy the recommended **MEMORY TO OPERATIONS REQUIRED MINIMIZE I/O** (**MRMIO**) value, at least the same amount of non-swapped physical memory (**RES**) must be available to Abaqus. Since the **RES** will in general be less than the virtual memory (**VIRT**) by some relatively constant amount for a given simulation, it is necessary to slightly over-allocate the requested Slurm node memory ``-mem=``. In the above sample Slurm script, this over-allocation has been hardcoded to a conservative value of 3072MB based on initial testing of the standard Abaqus solver. To avoid long queue wait times associated with large values of **MRMIO**, it may be worth investigating the simulation performance impact associated with reducing the **RES** memory that is made available to Abaqus significantly below the **MRMIO**. This can be done by lowering the ``-mem=`` value, which in turn will set an artificially low value of ``memory=`` in the Abaqus command (found in the last line of the script). In doing this, the **RES** cannot dip below the **MINIMUM MEMORY REQUIRED** (**MMR**) otherwise Abaqus will exit due to **Out of Memory** (**OOM**). As an example, if your **MRMIO** is 96GB, try running a series of short test jobs with ``#SBATCH --mem=8G, 16G, 32G, 64G`` until an acceptable minimal performance impact is found, noting that smaller values will result in increasingly larger scratch space used by temporary files.

#### Multi process

To determine the required Slurm memory for multi-node Slurm scripts, memory estimates (per compute process) required to minimize I/O are given in the output `.dat` file of completed jobs. If `mp_host_split` is not specified (or is set to 1), then the total number of compute processes will equal the number of nodes. The `mem-per-cpu` value can then be roughly determined by multiplying the largest memory estimate by the number of nodes and then dividing by the number or `ntasks`. If, however, a value for `mp_host_split` is specified (greater than 1), then the `mem-per-cpu` value can be roughly determined from the largest memory estimate times the number of nodes times the value of `mp_host_split` divided by the number of tasks. Note that `mp_host_split` must be less than or equal to the number of cores per node assigned by Slurm at runtime, otherwise Abaqus will terminate. This scenario can be controlled by uncommenting to specify a value for `tasks-per-node`. The following definitive statement is given in every output `.dat` file and mentioned here for reference:

```text
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
    *   [Nibi](../clusters/nibi.md#access-through-open-ondemand-ood): `https://ondemand.sharcnet.ca`
    *   TRILLIUM: https://ondemand.scinet.utoronto.ca
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
5.  To start Abaqus in GUI mode, there must be at least **one** unused `cae` license according to:

    ```bash
    $ abaqus licensing lmstat -c $ABAQUSLM_LICENSE_FILE -a | grep "Users of cae"
    Users of cae:  (Total of 4 licenses issued;  Total of 3 licenses in use)
    ```

### JupyterLab

1.  Start a JupyterHub desktop session by clicking one of the following JupyterHub links
    *   FIR: https://jupyterhub.fir.alliancecan.ca
    *   NARVAL: https://portail.narval.calculquebec.ca/
    *   RORQUAL: https://jupyterhub.rorqual.alliancecan.ca
2.  Highlight an Abaqus module such as ``abaqus/2026`` in the left-hand side "Available Module" section
3.  Click "Load" for the highlighted module and an ``Abaqus (VNC)`` Icon will appear in desktop
4.  Click the Icon and Abaqus should automatically be started in a remote Jupyter desktop

### VncViewer

This approach is considered obsolete; please use the above OnDemand/JupyterHub desktop instead.

1.  Connect with a VncViewer client to a login or compute node without a GPU by following [TigerVNC](../interactive/vnc.md)
2.  Open a new terminal window and enter the following
    ```bash
    module load abaqus/2026
    ```
3.  Start the application with
    ```bash
    abaqus cae -mesa
    ```

## Site-specific use
### SHARCNET license

!!! note "SHARCNET License Status"
    The SHARCNET license has been renewed until 17-Jan-2027 and is operational. It provides a small shared free pool consisting of 3 `cae` and 54 execute tokens for all researchers. Maximum usage limits are currently set at: 1 `cae`/user, 10 tokens/user and 15 tokens/group. These free tokens are available on a first come, first served basis and mainly intended for testing and light usage before deciding whether or not to purchase dedicated tokens. Costs for dedicated tokens (in 2021) were approximately CAD$110 per compute token and CAD$400 per GUI token: submit a ticket to request an official quote if interested. The free SHARCNET license can be used by any registered Alliance researcher, but only on SHARCNET hardware, and only after agreeing to the Academic License User Agreement below. Groups that purchase dedicated tokens to run on the SHARCNET license server may likewise ONLY use them on SHARCNET hardware (as dictated by the negotiated license agreement with Simulia) including the SHARCNET [OOD](../clusters/nibi.md#access-through-open-ondemand-ood) system (to run Abaqus in graphical mode) or Nibi/Dusky clusters (for submitting compute batch jobs to the queue). Before you can use the license, you must contact [technical support](../support/technical_support.md) and request access. In your email, 1) mention that it is for use on SHARCNET systems and 2) include a copy/paste of the following ``License Agreement`` statement with your full name and username entered in the indicated locations. Please note that every user must do this; it cannot be done one time only for a group; this includes PIs who have purchased their own dedicated tokens.

#### License agreement
```text
----------------------------------------------------------------------------------
Subject: Abaqus SHARCNET Academic License User Agreement

This email is to confirm that i "_____________" with username "___________" will
only use “SIMULIA Academic Software” with tokens from the SHARCNET license server
for the following purposes:

1) on SHARCNET hardware where the software is already installed
2) in affiliation with a Canadian degree-granting academic institution
3) for education, institutional or instruction purposes and not for any commercial
   or contract-related purposes where results are not publishable
4) for experimental, theoretical and/or digital research work, undertaken primarily
   to acquire new knowledge of the underlying foundations of phenomena and observable
   facts, up to the point of proof-of-concept in a laboratory    
-----------------------------------------------------------------------------------
```

#### Configure license file
Configure your license file as follows, noting that it is only usable on SHARCNET systems such as Nibi and Dusky clusters or the SHARCNET OOD desktop system. Note that the old ``license3.sharcnet.ca`` server has been permanently shut down, thus you must update your ``abaqus.lic`` file as follows to use the free SHARCNET license:

```bash title="~/.licenses/abaqus.lic"
[l2 (nibi login node):~] cat ~/.licenses/abaqus.lic
prepend_path("ABAQUSLM_LICENSE_FILE","27050@license1.computecanada.ca")
```

If your Abaqus job fails with the error message `[*** ABAQUS/eliT_CheckLicense rank 0 terminated by signal 11 (Segmentation fault)]` then verify your ``abaqus.lic`` file contains `ABAQUSLM_LICENSE_FILE` when using `abaqus/202X` modules. If your Abaqus job fails with error message `[License server machine is down or not responding, etc.]` and you are using `abaqus/6.14.1`, then replace `ABAQUSLM_LICENSE_FILE` with `LM_LICENSE_FILE`.

#### Query license server
Log into Nibi cluster, load Abaqus and then run one of the following:

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

III) Check the SHARCNET license server for only `cae`, `standard` and `explicit` product availability:
```bash
abaqus licensing lmstat -c $ABAQUSLM_LICENSE_FILE -a | grep "Users of" | egrep "cae|standard|explicit"
```

When the output of query I) above indicates that a job for a particular username is queued, this means the job has entered the "R"unning state from the perspective of ``squeue -j jobid`` or ``sacct -j jobid`` and is therefore idle on a compute node waiting for a license. This will have the same impact on your account priority as if the job were performing computations and consuming CPU time. Eventually, when sufficient licenses become available, the queued job will start.

##### Example

The following shows the situation where a user submitted two 6-core jobs (each requiring 12 tokens) in quick succession. The scheduler then started each job on a different node in the order they were submitted. Since the user had 10 Abaqus compute tokens, the first job (27527287) was able to acquire exactly enough (10) tokens for the solver to begin running. The second job (27527297), not having access to any more tokens, entered an idle "queued" state (as can be seen from the `lmstat` output) until the first job completed, wasting the available resources and depreciating the user's fair share level in the process ...

```text
[l2 (nibi login node):~] sq
            JOBID     USER              ACCOUNT           NAME  ST  TIME_LEFT NODES CPUS TRES_PER_N MIN_MEM NODELIST (REASON) 
         27530366  roberpj         cc-debug_cpu  scriptsp2.txt   R    9:56:13     1    6        N/A      8G     c107  (None) 
         27530407  roberpj         cc-debug_cpu  scriptsp2.txt   R    9:59:37     1    6        N/A      8G     c292  (None) 
```

```text
[l2 (nibi login node):~] abaqus licensing lmstat -c $ABAQUSLM_LICENSE_FILE -a | egrep "Users|start|queued"
 Users of abaqus:  (Total of 78 licenses issued;  Total of 53 licenses in use)
    roberpj c107 /dev/tty (v62.6) (license3.sharcnet.ca/27050 1042), start Mon 11/25 17:15, 10 licenses
    roberpj c292 /dev/tty (v62.6) (license3.sharcnet.ca/27050 125) queued for 10 licenses
```

To avoid license shortage problems when submitting multiple jobs when working with expensive Abaqus tokens, either use a [job dependency](../running-jobs/running_jobs.md#cancellation-of-jobs-with-dependency-conditions-which-cannot-be-met), [job array](../running-jobs/job_arrays.md), or at the very least set up a Slurm [email notification](../running-jobs/monitoring_jobs.md#email-notification) to know when your job completes before manually submitting another one.

#### Specify job resources
To ensure optimal usage of both your Abaqus tokens and our resources, it's important to carefully specify the required memory and ncpus in your Slurm script. The values can be determined by submitting a few short test jobs to the queue then checking their utilization. For **completed** jobs, use ``seff JobNumber`` to show the total *Memory Utilized* and *Memory Efficiency*. If the *Memory Efficiency* is less than ~90%, decrease the value of the ``#SBATCH --mem=`` setting in your Slurm script accordingly. Notice that the ``seff JobNumber`` command also shows the total *CPU (time) Utilized* and *CPU Efficiency*. If the *CPU Efficiency* is less than ~90%, perform scaling tests to determine the optimal number of CPUs for optimal performance and then update the value of ``#SBATCH --cpus-per-task=`` in your Slurm script. For **running** jobs, use the ``srun --overlap --jobid=29821580 --pty top -d 5 -u $USER`` command to watch the **%CPU**, **%MEM** and **RES** for each Abaqus parent process on the compute node. The **%CPU** and **%MEM** columns display the percent usage relative to the total available on the node while the **RES** column shows the per-process resident memory size (in human readable format for values over 1GB). Further information regarding how to [monitor jobs](../running-jobs/monitoring_jobs.md) is available on our documentation wiki.

#### Core token mapping
```text
TOKENS 5  6  7  8  10  12  14  16  19  21  25  28  34  38
CORES  1  2  3  4   6   8  12  16  24  32  48  64  96 128
```

where TOKENS = floor[5 X CORES^0.422]

Each GPU used requires 1 additional TOKEN.

### Western license

!!! warning "Western License Not Working"
    The ``abaqus.lic`` file given below no longer works since the license4 machine has been shut down and retired. Therefore, all Abaqus license checkout requests on the Dusky cluster from the Western/Robarts Abaqus license server currently will fail. A replacement server for license4 is currently being worked on. Once it is ready for use, ``abaqus.lic`` will be updated with the new server name and this red warning message will be removed. In the meantime, the SHARCNET License may be used instead by following the above procedure to request access.

The Western site license may only be used by Western researchers on hardware located at Western's campus. Currently, only the Dusky cluster satisfies this condition. Nibi and SHARCNET OOD system are excluded since they are located on Waterloo's campus. Contact the Western Abaqus license server administrator <jmilner@robarts.ca> to inquire about using the Western Abaqus license. You will need to provide your username and possibly make arrangements to purchase tokens. If you are granted access, then you may proceed to configure your ``abaqus.lic`` file to point to the Western license server:

#### Configure license file

```bash title=".licenses/abaqus.lic"
[dus241:~] cat .licenses/abaqus.lic
prepend_path("LM_LICENSE_FILE","27000@license4.sharcnet.ca")
prepend_path("ABAQUSLM_LICENSE_FILE","27000@license4.sharcnet.ca")
```

Once configured, submit your job as described in the *Cluster job submission* section above. If there are any problems, submit a problem ticket to [technical support](../support/technical_support.md). Specify that you are using the Abaqus Western license on Dusky and provide the failed job number along with a paste of any error messages as applicable.