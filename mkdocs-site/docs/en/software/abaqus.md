---
title: "Abaqus/en"
slug: "abaqus"
lang: "en"

source_wiki_title: "Abaqus/en"
source_hash: "778490893587d4fcc129f29a384aa064"
last_synced: "2026-10-11T01:39:35.690021+00:00"
last_processed: "2026-10-11T02:19:48.511097+00:00"

tags:
  - software

keywords:
  - "~/.licenses/abaqus.lic"
  - "Abaqus license server"
  - "SLURM_SUBMIT_DIR"
  - "MRMIO (Memory to Operations Required Minimize I/O)"
  - "abaqus licensing"
  - "#SBATCH --mem"
  - "Slurm"
  - "SLURM batch script"
  - "multinode jobs"
  - "maximum requested runtime"
  - "sbatch scriptsp1.txt"
  - "node configuration"
  - "SHARCNET systems"
  - "SBATCH --cpus-per-task=1"
  - "abaqus.lic configuration"
  - "abaqus/2026"
  - "%MEM"
  - "Slurm memory estimate"
  - "abaqus job"
  - "Slurm job submission"
  - "abaqus.lic"
  - "testep2"
  - "MPI_IC_ORDER='tcp'"
  - "lmhanglimit"
  - "Out of Memory (OOM)"
  - "mpi-based parallelization"
  - "module load abaqus/2026"
  - "restart input file"
  - "%CPU"
  - "license queuing"
  - "mem-per-cpu"
  - "Abaqus restart"
  - "token queueing and job scheduling"
  - "lmstat"
  - "nodes"
  - "JupyterLab"
  - "license server query (lmstat)"
  - "Abaqus graphical mode"
  - "TIME_LEFT"
  - "Dusky cluster"
  - "srun --overlap"
  - "FLEXnet"
  - "abaqus_v6.env"
  - "technical support"
  - "restart scripts"
  - "multiple node sections"
  - "tasks-per-node"
  - "mpi scripts"
  - "SBATCH --mem-per-cpu=4G"
  - "JOBID"
  - "Abaqus solvers"
  - "LM_LICENSE_FILE"
  - "ABAQUSLM_LICENSE_FILE"
  - "restart data"
  - "slurm job submission"
  - "testep1.lck"
  - "mp_host_split"
  - "cpus-per-task"
  - "license request"
  - "#SBATCH --cpus-per-task"
  - "Abaqus SHARCNET Academic License"
  - "OpenOnDemand"
  - "license server"
  - "memory allocation"
  - "MPI multi-node computing"
  - "monitor jobs"
  - "Nibi/Dusky clusters"
  - "compute node crash"
  - "Abaqus license shortage"
  - "SBATCH directives"
  - "DSLS-SERVER-HOSTNAME"
  - "memory upper limit"
  - "SHARCNET license"
  - "SLURM_TMPDIR"
  - "restart script"
  - "SBATCH --nodes=2"
  - "MPI computing"
  - "USER"
  - "abaqus cae -mesa"
  - "Abaqus 2026 module"
  - "explicit analysis"
  - "core-token mapping"
  - "DSLS"
  - "Western Abaqus license"
  - "LICENSING-CLIENT-PORT-NUMBER"
  - "temporary directory scripts"
  - "scratch directory"
  - "job failures"
  - "lmlicensequeuing=OFF"
  - "DSLS_LICENSE_FILE"
  - "SLURM memory allocation"
  - "FLEXnet ports"
  - "temporary directory script"
  - "Abaqus"

questions:
  - "How do you configure a FLEXnet‑based Abaqus license server on a cluster?"
  - "Which commands can be used to verify the status and availability of Abaqus licenses?"
  - "What are the required file configurations for using a DSLS (Dassault Systèmes License Server) versus a FLEXnet license server?"
  - "What placeholder values must be replaced in the ~/.licenses/abaqus.lic file to correctly configure DSLS_LICENSE_FILE?"
  - "How does the abaqus_v6.env file indicate the license server type for Abaqus?"
  - "Which command is used to prepend the DSLS_LICENSE_FILE environment variable with the client‑port‑number and server hostname?"
  - "How can you verify that the Abaqus license server is reachable and responding on the cluster?"
  - "What firewall and port configuration changes are required when adding a new Abaqus license server to an Alliance cluster?"
  - "How can you modify the default license‑queuing behavior in Slurm to prevent jobs from waiting indefinitely for a license?"
  - "Where are the “temporary directory scripts” located within the interface?"
  - "What are the common reasons a job might be terminated early, prompting the use of the restart scripts?"
  - "How can a user customize the input file to create additional restart types or modify the analysis?"
  - "How should users perform scaling tests to determine the optimal number of cores and wall‑clock time before submitting long Abaqus jobs?"
  - "What are the main differences between the single‑node script (scriptsp1.txt) and the restart script (scriptsp2.txt) for running Standard Analysis jobs?"
  - "How can the provided SLURM scripts be modified to request specific node types or GPU resources (e.g., h100 GPUs)?"
  - "What is the purpose of creating the directory `$SLURM_TMPDIR/scratch` in this SLURM script?"
  - "Which line should be uncommented to enable GPU usage for the Abaqus job?"
  - "What specific sections must be present in the restart input file as indicated by the script?"
  - "How do you specify in the Abaqus input file whether restart data should be written every N time increments or for a total of N increments?"
  - "Which SLURM directives need to be uncommented or edited to request a specific node type or GPU resources in these job scripts?"
  - "What are the required commands to create the temporary scratch and project directories and copy the necessary files before executing the Abaqus job?"
  - "What are the key differences between the MPI‑based and thread‑based Abaqus job scripts, and in which scenarios should each parallelization method be chosen?"
  - "How does the single‑node explicit analysis script allocate CPUs, memory, and temporary scratch space, and what is the purpose of the memory calculation `$((${SLURM_MEM_PER_NODE}-3072))MB`?"
  - "What are the required steps to perform a restart of an explicit Abaqus analysis using the provided restart script, and does the input file need any modifications for the restart?"
  - "What limitations are mentioned regarding the use of the restart script for multinode jobs?"
  - "Which Abaqus version is required to run the provided script successfully?"
  - "What SBATCH directives are included in the script and what resources do they request?"
  - "What is the purpose of the loop that copies files matching `testep1*` to the corresponding `testep2*` filenames?"
  - "How does the Abaqus command incorporate SLURM variables (e.g., `SLURM_SUBMIT_DIR`, `SLURM_TMPDIR`, `SLURM_CPUS_ON_NODE`, `SLURM_MEM_PER_NODE`) to configure the job execution?"
  - "According to the text, are any modifications required to the input file in order to restart the analysis?"
  - "How does the SLURM script set up the account, time, memory, CPU, and module environment for running an Abaqus job?"
  - "What are the specific commands and file operations needed to restart an Abaqus analysis using the provided restart script?"
  - "What are the prerequisites, configuration options, and limitations for using the MPI‑based multi‑node script to run Abaqus simulations?"
  - "How can the required Slurm node memory for a single‑process Abaqus simulation be estimated from the test.dat output file?"
  - "What are the recommended steps to monitor and verify the actual memory usage of an Abaqus job interactively on a compute node?"
  - "How is the mem‑per‑cpu value calculated for multi‑node Abaqus runs, and what effect does the mp_host_split parameter have on this calculation?"
  - "What does the `#SBATCH --nodes=2` directive specify in this SLURM script?"
  - "Why is `module load abaqus/2026` included, and what role does the `unset SLURM_GTIDS` line play?"
  - "How are the license environment variables (`LM_LICENSE_FILE` and `ABAQUSLM_LICENSE_FILE`) and the host list (`hostlistnodes`) being set and used in the script?"
  - "How is the mem‑per‑cpu value calculated using the largest memory estimate, number of nodes, mp_host_split, and number of tasks?"
  - "Why must mp_host_split be less than or equal to the number of cores per node assigned by Slurm, and what happens if this condition is violated?"
  - "Which setting should be uncommented to specify a value for tasks‑per‑node to control the scenario described?"
  - "How does the value of the “memory” parameter and the amount of physical RAM determine Abaqus’s upper memory limit and its impact on scratch‑disk usage?"
  - "What are the required steps to start Abaqus in graphical mode via OpenOnDemand or JupyterLab, and when should the ‑mesa option be used?"
  - "What are the SHARCNET license token limits, costs, and the procedure for requesting access to the Abaqus license?"
  - "What usage restrictions are imposed by the Abaqus SHARCNET Academic License User Agreement?"
  - "How must the abaqus.lic file be edited to work with the current SHARCNET license server on Nibi/Dusky clusters?"
  - "Which command‑line queries can be run to check license server status and job queues, and what do their results reveal?"
  - "What steps must a user follow to request and obtain an Abaqus license for use on SHARCNET systems?"
  - "Which clusters are recommended for submitting Abaqus compute batch jobs to the queue?"
  - "Is the license request process required for every individual user, including PIs with dedicated tokens?"
  - "What details does the `sq` command provide for the two listed jobs (JOBID 27530366 and 27530407)?"
  - "Which user and account are running these jobs, and what resources (nodes, CPUs, memory) have been allocated to each?"
  - "What information is the `abaqus licensing lmstat -c $ABAQUSLM_LICENSE_FILE -a | egrep \"Users|start|queued\"` command intended to retrieve?"
  - "What are the two options described for managing Abaqus license shortages when submitting jobs?"
  - "How can users determine and adjust the optimal memory and CPU resources for Abaqus jobs in their Slurm scripts?"
  - "Which methods are recommended to avoid license contention, such as job dependencies, job arrays, or email notifications?"
  - "How do you set the number of CPUs per task in a Slurm script using the `#SBATCH --cpus-per-task=` directive?"
  - "Which `srun` command should be used to monitor the %CPU, %MEM, and RES values of each Abaqus parent process on a compute node while a job is running?"
  - "Where can you find additional documentation on monitoring jobs in the provided wiki?"
  - "How is the required number of tokens determined from the number of GPU cores?"
  - "Which compute systems are permitted to use the Western Abaqus site license, and what is the procedure to obtain access?"
  - "What are the exact steps to configure the abaqus.lic file and submit a job on the Dusky cluster?"

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

Abaqus software modules are available on the Alliance clusters; however, you must provide your own license. There are two types of license servers, each with different setup procedures described below.

### FLEXnet servers

To configure your account on a cluster to use a **FLEXnet-based** (also known as FlexLM) Abaqus license server, a single file named `~/.licenses/abaqus.lic` must first be created containing the license manager daemon port number `LMGRD-PORT-NUMBER` and the fully qualified hostname `FLEXnet-SERVER-HOSTNAME`. These two pieces of information are then assigned to the `ABAQUSLM_LICENSE_FILE` environment variable whenever an Abaqus module is loaded. Another file, `abaqus_v6.env`, may also need to exist in your home or job submission directory if its default is not assumed:

```` title="abaqus_v6.env"
license_server_type = FLEXNET
````

```` title="~/.licenses/abaqus.lic"
prepend_path("ABAQUSLM_LICENSE_FILE","LMGRD-PORT-NUMBER@FLEXnet-SERVER-HOSTNAME")
````

To check if your license server connection is working, run the following command:

```bash
module load abaqus
abaqus licensing ru | grep ABAQUSLM:
```

The output `ABAQUSLM: UP v11.19.6.` indicates success.

To check how many CAE licenses in a pool are available for immediate use by anyone (the difference between "issued" and "in use"), run the following command. Note that reserved licenses will always appear to be "in use" regardless of whether they are actually being used by the group for which they are reserved. In the case of the SHARCNET license, there are 4 CAE licenses, but only 1 is reserved; therefore, 3 are in the pool available to anyone for use. The following example shows that at the time the command was run, none of the 3 CAE licenses in the pool were available for use by any group to run Abaqus in GUI mode on the Nibi cluster On-Demand graphical system.

```bash
abaqus licensing ru | grep cae
```

```
Users of cae:  (Total of 4 licenses issued;  Total of 1 license in use)
"cae" v62.7, vendor: ABAQUSLM, expiry: 17-jan-2027
```

For a summary of all licenses provided by a license server:

```bash
module load abaqus
abaqus licensing r
```

```
Feature                         Version     #licenses    Vendor        Expires
_______                         _________   _________    ______        ________
abaqus_extended                 62.7         4           ABAQUSLM      17-jan-2027
abaqus                          62.7         78          ABAQUSLM      17-jan-2027
ams                             62.7         1           ABAQUSLM      17-jan-2027
etc etc etc
```

### DSLS servers

To use a **DSLS** (Dassault Systèmes License Server) based license server, you must first configure two single-line text files named `~/.licenses/abaqus.lic` and `abaqus_v6.env` as shown below. You may either place a copy of `abaqus_v6.env` into each job submission directory **OR** a single copy into your home directory. For example, by placing both `abaqus_v6.env` and `~/.licenses/abaqus.lic` in your home directory, you would just need to replace `LICENSING-CLIENT-PORT-NUMBER:DSLS-SERVER-HOSTNAME` in your `~/.licenses/abaqus.lic` file, then `DSLS_LICENSE_FILE` will be configured accordingly whenever an Abaqus module is loaded:

```` title="abaqus_v6.env"
license_server_type=DSLS
````

```` title="~/.licenses/abaqus.lic"
prepend_path("DSLS_LICENSE_FILE","LICENSING-CLIENT-PORT-NUMBER@DSLS-SERVER-HOSTNAME")
````

With both files set up, you may now check if the license server is reachable and responding by running:

```bash
module load abaqus
abaqus licensing dslsstat
```

A `SUCCESS` message in the output will contain "license servers declared", while a `FAILURE` message will contain "No license server available".

### New servers

If your license server was never set up for use on an Alliance cluster, some additional configuration changes by the Alliance system administrator and your local system administrator will need to be done. Such changes are necessary to ensure the required TCP ports (HTTPS protocol) of your Abaqus server are reachable from all cluster compute nodes through the client/server firewalls. For help, please write to [technical support](../support/technical_support.md) and be sure to include the following:

*   FLEXnet SERVER: flex lmgrd port number (default 27000), static vendor port number (default 28000). Both ports need to be opened on the Alliance cluster and license server firewalls.
*   DSLS SERVER: administrative port number (default 4084), licensing client port number (default 4085). Only the licensing client port must be opened on the Alliance cluster and license server firewalls.
*   Fully qualified domain name or IPV4 address of your new Abaqus server.

You will be sent a list of cluster IP addresses (known as NAT nodes) so your administrator can open the local server firewall to allow connections from these nodes on the required port(s). Please note that a special license agreement must generally be negotiated and signed by both SIMULIA and your institution before a campus license may be used remotely on an Alliance cluster located on the campus of another institution.

### License queuing

The default setup for the license server is to queue jobs started on the cluster by Slurm if not enough tokens are available. There are two options to alter this behaviour so jobs don't sit idle on a cluster compute node waiting for a license indefinitely, wasting valuable resources.

The first option is to terminate a job immediately if not enough licenses are available, therefore never entering a queue. To specify this setting, create a text file named `abaqus_v6.env` in either your `/home` OR working (submit) directory containing the line: `lmlicensequeuing=OFF`.

The second option is to specify a finite wait time where the job can enter into a queued state on the license server, such as 1 minute, by adding the line: `lmhanglimit=1`. If within 1 minute sufficient licenses do not become available, the job will be dequeued by the license server and in turn be terminated by Slurm. For each option, messages will be printed at the bottom of the Slurm output file, as detailed in the Example below.

## Version notes

### 2026

A new module `abaqus/2026` containing the initial *Abaqus 2026 Golden/GA* release has been installed into the default StdEnv/2023 environment. Another module named `abaqus/2026.2614` containing the latest SIMULIA Established Products 2026 Fix Packs, currently at level FD02 (FP.2614), will be made available as soon as possible. To verify your setup, run the following:

```bash
module load abaqus/2026
module load intel/2024
abaqus verify -all
```

All tests should succeed except for CAE (unless you log into an OnDemand/Jupyter graphical desktop) and TOSCA (unless you set `export FED_DSFLEX_LICENSE_CONFIG=port@hostname`) before running the verification.

### 2021

It is recommended to discontinue use of `abaqus/2021` installed under the previous StdEnv/2020 since this legacy version generates `*** buffer overflow detected ***` errors on all recent clusters. An unshare workaround previously included in the single node Slurm scripts of this wiki has now been removed.

## Cluster job submission

Below are prototype Slurm scripts for submitting thread and MPI-based parallel simulations to single or multiple compute nodes. Most users will find it sufficient to use one of the **project directory scripts** provided in the *Single node computing* sections. The optional `memory=` argument found in the last line of the scripts is intended for larger memory or problematic jobs where the 3072MB offset value may require tuning. A listing of all Abaqus command line arguments can be obtained by loading an Abaqus module and running: `abaqus -help | less`.

Single node jobs that run less than one day should find the *project directory script* located in the first tab sufficient. However, single node jobs that run for more than a day should use one of the restart scripts. Jobs that create large restart files will benefit by writing to the local disk through the use of the `SLURM_TMPDIR` environment variable utilized in the **temporary directory scripts** provided in the two rightmost tabs of the single node standard and explicit analysis sections. The restart scripts shown here will continue jobs that have been terminated early for some reason. Such job failures can occur if a job reaches its maximum requested runtime before completing and is killed by the queue or if the compute node the job was running on crashed due to an unexpected hardware failure. Other restart types are possible by further tailoring of the input file (not shown here) to continue a job with additional steps or change the analysis (see the documentation for version specific details).

Jobs that require large memory or larger compute resources (beyond that which a single compute node can provide) should use the MPI scripts in the **multiple node sections** below to distribute computing over arbitrary node ranges determined automatically by the scheduler. Short scaling test jobs should be run to determine wall-clock times (and memory requirements) as a function of the number of cores (2, 4, 8, etc.) to determine the optimal number before running any long jobs.

### Standard analysis

Abaqus solvers support thread-based and MPI-based parallelization. Scripts for each type are provided below for running Standard Analysis type jobs on Single or Multiple nodes respectively. Lines that start with `##SBATCH` are commented; to uncomment, change to `#SBATCH`. Most users will find it sufficient to use the first `scriptsp1.txt` script that requires simply changing `def-group` to your account and `mystd-sim.inp` to the name of your input file before submitting with the `sbatch scriptsp1.txt` command.

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
    ##SBATCH --partition=specify    # Uncomment to specify contributor

    module load StdEnv/2023
    module load abaqus/2026

    unset SLURM_GTIDS
    export MPI_IC_ORDER='tcp'
    echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"
    echo "SLURM_SUBMIT_DIR =" $SLURM_SUBMIT_DIR
    echo "SLURM_TMPDIR = " $SLURM_TMPDIR

    rm -f testsp1* testsp2*
    mkdir -p $SLURM_TMPDIR/scratch

    abaqus job=testsp1 input=$SLURM_SUBMIT_DIR/mystd-sim.inp \
    scratch=$SLURM_TMPDIR/scratch cpus=$SLURM_CPUS_ON_NODE interactive \
    mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB" \
    #gpus=$SLURM_GPUS_ON_NODE  # uncomment this line to use gpu
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
    ##SBATCH --partition=specify    # Uncomment to specify contributor

    module load StdEnv/2023
    module load abaqus/2026

    unset SLURM_GTIDS
    export MPI_IC_ORDER='tcp'
    echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"
    echo "SLURM_SUBMIT_DIR =" $SLURM_SUBMIT_DIR
    echo "SLURM_TMPDIR = " $SLURM_TMPDIR

    rm -f testsp1.lck testsp2*
    mkdir -p $SLURM_TMPDIR/scratch

    abaqus job=testsp2 oldjob=testsp1 input=$SLURM_SUBMIT_DIR/mystd-sim-restart.inp \
    scratch=$SLURM_TMPDIR/scratch cpus=$SLURM_CPUS_ON_NODE interactive \
    mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB" \
    #gpus=$SLURM_GPUS_ON_NODE  # uncomment this line to use gpu
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
    ##SBATCH --partition=specify    # Uncomment to specify contributor

    module load StdEnv/2023
    module load abaqus/2026

    unset SLURM_GTIDS
    export MPI_IC_ORDER='tcp'
    echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"
    echo "SLURM_SUBMIT_DIR =" $SLURM_SUBMIT_DIR
    echo "SLURM_TMPDIR = " $SLURM_TMPDIR

    rm -f testst1* testst2*
    mkdir -p $SLURM_TMPDIR/scratch
    mkdir -p $SLURM_TMPDIR/project
    cp abaqus_v6.env $SLURM_TMPDIR/project
    cd $SLURM_TMPDIR/project

    abaqus job=testst1 input=$SLURM_SUBMIT_DIR/mystd-sim.inp \
    scratch=$SLURM_TMPDIR/scratch cpus=$SLURM_CPUS_ON_NODE interactive \
    mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB" \
    #gpus=$SLURM_GPUS_ON_NODE  # uncomment this line to use gpu

    cp -a * $SLURM_SUBMIT_DIR
    cd $SLURM_SUBMIT_DIR
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
    ##SBATCH --partition=specify    # Uncomment to specify contributor

    module load StdEnv/2023
    module load abaqus/2026

    unset SLURM_GTIDS
    export MPI_IC_ORDER='tcp'
    echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"
    echo "SLURM_SUBMIT_DIR =" $SLURM_SUBMIT_DIR
    echo "SLURM_TMPDIR = " $SLURM_TMPDIR

    rm -f testst1.lck testst2*
    mkdir -pv $SLURM_TMPDIR/scratch
    mkdir -pv $SLURM_TMPDIR/project
    cp abaqus_v6.env $SLURM_TMPDIR/project
    cp testst1* $SLURM_TMPDIR/project
    cd $SLURM_TMPDIR/project

    abaqus job=testst2 oldjob=testst1 input=$SLURM_SUBMIT_DIR/mystd-sim-restart.inp \
    scratch=$SLURM_TMPDIR/scratch cpus=$SLURM_CPUS_ON_NODE interactive \
    mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB" \
    #gpus=$SLURM_GPUS_ON_NODE  # uncomment this line to use gpu

    cp -a * $SLURM_SUBMIT_DIR
    cd $SLURM_SUBMIT_DIR
    ````

    The restart input file should contain:
    `*HEADING`
    `*RESTART, READ`

#### Multiple node computing

Users with large memory or compute needs (and correspondingly access to large licenses) can use the following script to perform MPI-based computing over an arbitrary range of nodes, ideally left for the scheduler to automatically determine.

!!! warning
    A companion template script to perform restart of multinode jobs is not provided due to additional limitations on when they can be used. Only `abaqus/2026` or newer may be used with this script.

````sh title="scriptsp1-mpi.txt"
#!/bin/bash
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
for i in $(echo "$nodes" | xargs -n1 | uniq); do hostlist=${hostlist}$(echo "['${i}',$(echo "$nodes" | xargs -n1 | grep $i | wc -l)],"); done
hostlist="$(echo "$hostlist" | sed 's/,$//g')"
mphostlist="mp_host_list=[$(echo "$hostlist")]"
export $mphostlist
echo "$mphostlist" > abaqus_v6.env

abaqus job=testsp1-mpi input=mystd-sim.inp \
scratch=$SLURM_TMPDIR cpus=$SLURM_NTASKS interactive mp_mode=mpi \
#mp_host_split=1  # number of dmp processes per node >= 1 (uncomment to specify)
````

### Explicit analysis

Abaqus solvers support thread-based and MPI-based parallelization. Scripts for each type are provided below for running explicit analysis type jobs on single or multiple nodes respectively.

!!! warning
    Template scripts to perform multinode job restarts are not currently provided, pending further testing.

#### Single node computing

=== "project directory script"

    ````sh title="scriptep1.txt"
    #!/bin/bash
    #SBATCH --account=def-group    # specify account
    #SBATCH --time=00-06:00        # days-hrs:mins
    #SBATCH --mem=8000M            # node memory > 5G
    #SBATCH --cpus-per-task=4      # number cores > 1
    #SBATCH --nodes=1              # do not change
    ##SBATCH --partition=specify   # optional

    module load StdEnv/2023
    module load abaqus/2026

    unset SLURM_GTIDS
    export MPI_IC_ORDER='tcp'
    echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"
    echo "SLURM_SUBMIT_DIR =" $SLURM_SUBMIT_DIR
    echo "SLURM_TMPDIR = " $SLURM_TMPDIR

    rm -f testep1* testep2*
    mkdir -p $SLURM_TMPDIR/scratch

    abaqus job=testep1 input=myexp-sim.inp \
    scratch=$SLURM_TMPDIR/scratch cpus=$SLURM_CPUS_ON_NODE interactive \
    mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB"
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
    ##SBATCH --partition=specify   # optional

    module load StdEnv/2023
    module load abaqus/2026

    unset SLURM_GTIDS
    export MPI_IC_ORDER='tcp'
    echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"
    echo "SLURM_SUBMIT_DIR =" $SLURM_SUBMIT_DIR
    echo "SLURM_TMPDIR = " $SLURM_TMPDIR

    rm -f testep1.lck testep2*
    for f in testep1*; do cp -av "$f" "testep2${f#testep1}"; done

    abaqus job=testep2 input=$SLURM_SUBMIT_DIR/myexp-sim.inp recover \
    scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
    mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB"
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
    ##SBATCH --partition=specify   # optional

    module load StdEnv/2023
    module load abaqus/2026

    unset SLURM_GTIDS
    export MPI_IC_ORDER='tcp'
    echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"
    echo "SLURM_SUBMIT_DIR =" $SLURM_SUBMIT_DIR
    echo "SLURM_TMPDIR = " $SLURM_TMPDIR

    rm -f testet1* testet2*
    mkdir -p $SLURM_TMPDIR/scratch
    mkdir -p $SLURM_TMPDIR/project
    cp abaqus_v6.env $SLURM_TMPDIR/project
    cd $SLURM_TMPDIR/project

    abaqus job=testet1 input=$SLURM_SUBMIT_DIR/myexp-sim.inp \
    scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
    mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB"

    cp -a * $SLURM_SUBMIT_DIR
    cd $SLURM_SUBMIT_DIR
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
    ##SBATCH --partition=specify   # optional

    module load StdEnv/2023
    module load abaqus/2026

    unset SLURM_GTIDS
    export MPI_IC_ORDER='tcp'
    echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"
    echo "SLURM_SUBMIT_DIR =" $SLURM_SUBMIT_DIR
    echo "SLURM_TMPDIR = " $SLURM_TMPDIR

    rm -f testet1.lck testet2*
    mkdir -pv $SLURM_TMPDIR/scratch
    mkdir -pv $SLURM_TMPDIR/project
    cp abaqus_v6.env $SLURM_TMPDIR/project
    for f in testet1*; do cp -av "$f" $SLURM_TMPDIR/project/"testet2${f#testet1}"; done
    cd $SLURM_TMPDIR/project

    abaqus job=testet2 input=$SLURM_SUBMIT_DIR/myexp-sim.inp recover \
    scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
    mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB"

    cp -a * $SLURM_SUBMIT_DIR
    cd $SLURM_SUBMIT_DIR
    ````

    No input file modifications are required to restart the analysis.

#### Multiple node computing

Users with large memory or compute needs (and correspondingly access to large licenses) can use the following script to perform MPI-based computing over an arbitrary range of nodes, ideally left for the scheduler to automatically determine.

!!! warning
    A companion template script to perform restart of multinode jobs is not provided due to additional limitations on how they can be used. Only `abaqus/2026` or newer may be used with this script.

````sh title="scriptep1-mpi.txt"
#!/bin/bash
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
for i in $(echo "$nodes" | xargs -n1 | uniq); do hostlist=${hostlist}$(echo "['${i}',$(echo "$nodes" | xargs -n1 | grep $i | wc -l)],"); done
hostlist="$(echo "$hostlist" | sed 's/,$//g')"
mphostlist="mp_host_list=[$(echo "$hostlist")]"
export $mphostlist
echo "$mphostlist" > abaqus_v6.env

abaqus job=testep1-mpi input=myexp-sim.inp \
scratch=$SLURM_TMPDIR cpus=$SLURM_NTASKS interactive mp_mode=mpi \
#mp_host_split=1  # number of dmp processes per node >= 1 (uncomment to specify)
````

## Memory estimates

### Single process

An estimate for the total Slurm node memory (`--mem=`) required for a simulation to run fully in RAM (without being virtualized to scratch disk) can be obtained by examining the Abaqus output `test.dat` file. For example, a simulation that requires a fairly large amount of memory might show:

```bash
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

2.  Next, SSH into the compute node (e.g., c50) and then run `top`:

    ```bash
    ssh c50
    top -u $USER
    ```

3.  Watch the `VIRT` and `RES` columns until steady peak memory values are observed.

To completely satisfy the recommended "MEMORY TO OPERATIONS REQUIRED MINIMIZE I/O" (MRMIO) value, at least the same amount of non-swapped physical memory (`RES`) must be available to Abaqus. Since the `RES` will in general be less than the virtual memory (`VIRT`) by some relatively constant amount for a given simulation, it is necessary to slightly over-allocate the requested Slurm node memory `--mem=`. In the sample Slurm scripts, this over-allocation has been hardcoded to a conservative value of 3072MB based on initial testing of the standard Abaqus solver.

!!! tip "Optimizing Memory Allocation"
    To avoid long queue wait times associated with large values of MRMIO, it may be worth investigating the simulation performance impact associated with reducing the `RES` memory that is made available to Abaqus significantly below the MRMIO. This can be done by lowering the `--mem=` value, which in turn will set an artificially low value of `memory=` in the Abaqus command (found in the last line of the script). In doing this, the `RES` cannot dip below the MINIMUM MEMORY REQUIRED (MMR); otherwise, Abaqus will exit due to Out of Memory (OOM). As an example, if your MRMIO is 96GB, try running a series of short test jobs with `#SBATCH --mem=8G, 16G, 32G, 64G` until an acceptable minimal performance impact is found, noting that smaller values will result in increasingly larger scratch space used by temporary files.

### Multi process

To determine the required Slurm memory for multi-node Slurm scripts, memory estimates (per compute process) required to minimize I/O are given in the output `.dat` file of completed jobs. If `mp_host_split` is not specified (or is set to 1), then the total number of compute processes will equal the number of nodes. The `mem-per-cpu` value can then be roughly determined by multiplying the largest memory estimate by the number of nodes and then dividing by the number of `ntasks`. However, if a value for `mp_host_split` is specified (greater than 1), then the `mem-per-cpu` value can be roughly determined from the largest memory estimate times the number of nodes times the value of `mp_host_split` divided by the number of tasks. Note that `mp_host_split` must be less than or equal to the number of cores per node assigned by Slurm at runtime; otherwise, Abaqus will terminate. This scenario can be controlled by uncommenting to specify a value for `tasks-per-node`.

The following definitive statement is given in every output `.dat` file and mentioned here for reference:

!!! note
    THE UPPER LIMIT OF MEMORY THAT CAN BE ALLOCATED BY ABAQUS WILL IN GENERAL DEPEND ON THE VALUE OF THE "MEMORY" PARAMETER AND THE AMOUNT OF PHYSICAL MEMORY AVAILABLE ON THE MACHINE. PLEASE SEE THE "ABAQUS ANALYSIS USER'S MANUAL" FOR MORE DETAILS. THE ACTUAL USAGE OF MEMORY AND OF DISK SPACE FOR SCRATCH DATA WILL DEPEND ON THIS UPPER LIMIT AS WELL AS THE MEMORY REQUIRED TO MINIMIZE I/O. IF THE MEMORY UPPER LIMIT IS GREATER THAN THE MEMORY REQUIRED TO MINIMIZE I/O, THEN THE ACTUAL MEMORY USAGE WILL BE CLOSE TO THE ESTIMATED "MEMORY TO MINIMIZE I/O" VALUE, AND THE SCRATCH DISK USAGE WILL BE CLOSE-TO-ZERO; OTHERWISE, THE ACTUAL MEMORY USED WILL BE CLOSE TO THE PREVIOUSLY MENTIONED MEMORY LIMIT, AND THE SCRATCH DISK USAGE WILL BE ROUGHLY PROPORTIONAL TO THE DIFFERENCE BETWEEN THE ESTIMATED "MEMORY TO MINIMIZE I/O" AND THE MEMORY UPPER LIMIT. HOWEVER, AN ACCURATE ESTIMATE OF THE SCRATCH DISK SPACE IS NOT POSSIBLE.

## Graphical use

It is recommended to use an OpenOnDemand or JupyterLab to run graphical applications at the Alliance.

### OnDemand

1.  Start an OnDemand desktop session by clicking one of the following OnDemand links:
    *   [Nibi](../clusters/nibi.md#access-through-open-ondemand-ood): `https://ondemand.sharcnet.ca`
    *   TRILLIUM: `https://ondemand.scinet.utoronto.ca`

2.  Open a new terminal window within your desktop and load:
    ```bash
    module load abaqus/2026
    ```

3.  Start the application in graphical mode using the `cae` option. If you are on either: 1) a node without a GPU or 2) a node with a GPU but without VirtualGL support, then append the `mesa` option:
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

    ```
    Users of cae:  (Total of 4 licenses issued;  Total of 3 licenses in use)
    ```

### JupyterLab

1.  Start a JupyterHub desktop session by clicking one of the following JupyterHub links:
    *   FIR: `https://jupyterhub.fir.alliancecan.ca`
    *   NARVAL: `https://portail.narval.calculquebec.ca/`
    *   RORQUAL: `https://jupyterhub.rorqual.alliancecan.ca`
2.  Highlight an Abaqus module such as `abaqus/2026` in the left-hand side *Available Module* section.
3.  Click on *Load* for the highlighted module, and an `Abaqus (VNC)` icon will appear in the desktop.
4.  Click on the icon, and Abaqus should automatically be started in a remote Jupyter desktop.

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

The SHARCNET license has been renewed until 17-Jan-2027 and is operational. It provides a small shared free pool consisting of 3 CAE and 54 execute tokens for all researchers. Maximum usage limits are currently set at: 1 CAE/user, 10 tokens/user, and 15 tokens/group. These free tokens are available on a first-come, first-served basis and are mainly intended for testing and light usage before deciding whether or not to purchase dedicated tokens. Costs for dedicated tokens (in 2021) were approximately CAD$110 per compute token and CAD$400 per GUI token; submit a ticket to request an official quote if interested. The free SHARCNET license can be used by any registered Alliance researcher, but only on SHARCNET hardware, and only after agreeing to the Academic License User Agreement below. Groups that purchase dedicated tokens to run on the SHARCNET license server may likewise ONLY use them on SHARCNET hardware (as dictated by the negotiated license agreement with Simulia), including the SHARCNET [OOD](../clusters/nibi.md#access-through-open-ondemand-ood) system (to run Abaqus in graphical mode) or Nibi/Dusky clusters (for submitting compute batch jobs to the queue). Before you can use the license, you must contact [technical support](../support/technical_support.md) and request access. In your email, 1) mention that it is for use on SHARCNET systems and 2) include a copy/paste of the following `License Agreement` statement with your full name and username entered in the indicated locations. Please note that every user must do this; it cannot be done one time only for a group; this includes PIs who have purchased their own dedicated tokens.

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

````bash title="~/.licenses/abaqus.lic"
prepend_path("ABAQUSLM_LICENSE_FILE","27050@license1.computecanada.ca")
````

If your Abaqus job fails with the error message `[*** ABAQUS/eliT_CheckLicense rank 0 terminated by signal 11 (Segmentation fault)]`, then verify your `abaqus.lic` file contains `ABAQUSLM_LICENSE_FILE` when using `abaqus/202X` modules. If your Abaqus job fails with error message `[License server machine is down or not responding, etc.]` and you are using `abaqus/6.14.1`, then replace `ABAQUSLM_LICENSE_FILE` with `LM_LICENSE_FILE`.

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
III) Check the SHARCNET license server for only CAE, Standard, and Explicit product availability:
```bash
abaqus licensing lmstat -c $ABAQUSLM_LICENSE_FILE -a | grep "Users of" | egrep "cae|standard|explicit"
```

When the output of query I) above indicates that a job for a particular username is queued, this means the job has entered the "R"unning state from the perspective of `squeue -j jobid` or `sacct -j jobid` and is therefore idle on a compute node waiting for a license. This will have the same impact on your account priority as if the job were performing computations and consuming CPU time. Eventually, when sufficient licenses become available, the queued job will start.

##### Example

The following shows the situation where a user submitted two 6-core jobs (each requiring 12 tokens) in quick succession. The scheduler then started each job on a different node in the order they were submitted. Since the user had 10 Abaqus compute tokens, the first job (27527287) was able to acquire exactly enough (10) tokens for the solver to begin running. The second job (27527297) not having access to any more tokens entered an idle "queued" state (as can be understood from the `lmstat` output) until the first job completed, wasting the available resources and depreciating the user's fair share level in the process.

```bash
sq
```
```
            JOBID     USER              ACCOUNT           NAME  ST  TIME_LEFT NODES CPUS TRES_PER_N MIN_MEM NODELIST (REASON) 
         27530366  roberpj         cc-debug_cpu  scriptsp2.txt   R    9:56:13     1    6        N/A      8G     c107  (None) 
         27530407  roberpj         cc-debug_cpu  scriptsp2.txt   R    9:59:37     1    6        N/A      8G     c292  (None) 
```

```bash
abaqus licensing lmstat -c $ABAQUSLM_LICENSE_FILE -a | egrep "Users|start|queued"
```
```
Users of abaqus:  (Total of 78 licenses issued;  Total of 53 licenses in use)
    roberpj c107 /dev/tty (v62.6) (license3.sharcnet.ca/27050 1042), start Mon 11/25 17:15, 10 licenses
    roberpj c292 /dev/tty (v62.6) (license3.sharcnet.ca/27050 125) queued for 10 licenses
```

To avoid license shortage problems when submitting multiple jobs while working with expensive Abaqus tokens, either use a [job dependency](../running-jobs/running_jobs.md#cancellation-of-jobs-with-dependency-conditions-which-cannot-be-met), [job array](../running-jobs/job_arrays.md), or at the very least, set up a Slurm [email notification](../running-jobs/monitoring_jobs.md#email-notification) to know when your job completes before manually submitting another one. There are two easier options for dealing with this situation:

**Option 1)**

To disable non-interactive (analysis) jobs from starting on a cluster compute node after being submitted to the queue and then becoming idle (when not enough tokens are unavailable, which is the default behaviour), create a text file in your submit directory (before submitting the job) with the following one-line contents, and the job will instead terminate immediately.

````bash title="~/submitdirectory/abaqus_v6.env"
lmlicensequeuing=OFF
````

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

**Option 2)**

Specify a setting in minutes so that a started job will enter a QUEUED state to wait for a license before being automatically DEQUEUED and terminating if a license does not become available in time.

````bash title="~/submitdirectory/abaqus_v6.env"
lmhanglimit=1 
````

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

#### Specify job resources

To ensure optimal usage of both your Abaqus tokens and our resources, it's important to carefully specify the required memory and CPUs in your Slurm script. The values can be determined by submitting a few short test jobs to the queue, then checking their utilization. For **completed** jobs, use `seff JobNumber` to show the total *Memory Utilized* and *Memory Efficiency*. If the *Memory Efficiency* is less than ~90%, decrease the value of the `#SBATCH --mem=` setting in your Slurm script accordingly. The `seff JobNumber` command also shows the total *CPU (time) Utilized* and *CPU Efficiency*. If the *CPU Efficiency* is less than ~90%, perform scaling tests to determine the optimal number of CPUs for optimal performance and then update the value of `#SBATCH --cpus-per-task=` in your Slurm script. For **running** jobs, use the `srun --overlap --jobid=29821580 --pty top -d 5 -u $USER` command to watch the `%CPU`, `%MEM`, and `RES` for each Abaqus parent process on the compute node. The `%CPU` and `%MEM` columns display the percent usage relative to the total available on the node, while the `RES` column shows the per-process resident memory size (in human-readable format for values over 1GB). Further information regarding how to [monitor jobs](../running-jobs/monitoring_jobs.md) is available on our documentation wiki.

#### Core-token mapping

```
TOKENS 5  6  7  8  10  12  14  16  19  21  25  28  34  38
CORES  1  2  3  4   6   8  12  16  24  32  48  64  96 128
```

where `TOKENS = floor[5 X CORES^0.422]`.

Each GPU used requires 1 additional TOKEN.

### Western license

The Western Abaqus site license may only be used by Western researchers on compute hardware located on Western's campus. Currently, only the Dusky cluster satisfies this condition. The Nibi and SHARCNET OOD systems may not be used since they are located on Waterloo's campus. Contact the Western Abaqus license server administrator `jmilner@robarts.ca` to inquire about being added to the Western Abaqus license. You will need to provide your Alliance username and possibly make arrangements with your supervisor to purchase tokens. If you are granted access, then you may proceed to log in to Dusky and configure your `abaqus.lic` file using a text editor such as `nano` to contain the following single line:

```bash
ssh dusky.alliancecan.ca
```

````bash title="~/.licenses/abaqus.lic"
prepend_path("ABAQUSLM_LICENSE_FILE","27000@authorize.robarts.ca")
````

Now you may submit your job using a Slurm script and the `sbatch` command as described in the *Cluster job submission* section above. If there are any problems, submit a problem ticket to [technical support](../support/technical_support.md). Specify that you are using the Abaqus Western license on Dusky and provide the failed job number along with a paste of any error messages as applicable.