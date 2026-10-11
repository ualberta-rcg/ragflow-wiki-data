---
title: "Abaqus"
slug: "abaqus"
lang: "base"

source_wiki_title: "Abaqus"
source_hash: "322322572db1259a7a6570852a956820"
last_synced: "2026-10-11T01:39:35.690021+00:00"
last_processed: "2026-10-11T02:18:42.067053+00:00"

tags:
  - software

keywords:
  - "Abaqus license server"
  - "NODES"
  - "#SBATCH --mem"
  - "RES"
  - "GPU with VirtualGL support"
  - "memory= argument"
  - "cannot be done one time"
  - "abaqus job=testet2"
  - "Abaqus standard analysis"
  - "single node computing"
  - "single node jobs"
  - "Abaqus command line arguments"
  - "simulation interactively"
  - "abaqus.lic configuration"
  - "time"
  - "%MEM"
  - "module load"
  - "abaqus job"
  - "multi-node jobs"
  - "Slurm job submission"
  - "memory=$((${SLURM_MEM_PER_NODE}-3072))MB"
  - "memory estimate"
  - "multiple node mpi scripts"
  - "SHARCNET license server"
  - "license tokens"
  - "SLURM_TMPDIR environment variable"
  - "SLURM directives"
  - "MPI_IC_ORDER='tcp'"
  - "lmhanglimit"
  - "module load abaqus/2026"
  - "restart input file"
  - "job submit directory"
  - "ABAQUSLM_LICENSE_FILE environment variable"
  - "%CPU"
  - "order_parallel=OFF"
  - "token core mapping"
  - "DSLS (Dassault Systèmes License Server)"
  - "fair share level"
  - "#SBATCH"
  - "SIMULIA Academic Software"
  - "slurm sbatch submission"
  - "RESTART WRITE OVERLAY"
  - "FLEXnet (FlexLM)"
  - "RES memory"
  - "JupyterLab"
  - "thread and mpi-based parallel simulations"
  - "--cpus-per-task=4"
  - "abaqus licensing dslsstat"
  - "TIME_LEFT"
  - "JupyterHub session"
  - "scratch disk usage"
  - "abaqus/2026 module"
  - "Dusky cluster"
  - "OnDemand desktop"
  - "srun --overlap"
  - "abaqus_v6.env"
  - "full name and username"
  - "abaqus.lic file"
  - "Slurm --mem"
  - "estimated memory to minimize I/O"
  - "JOBID"
  - "monitoring memory"
  - "SBATCH --partition"
  - "Abaqus licensing"
  - "ABAQUSLM_LICENSE_FILE"
  - "SBATCH --nodes=1"
  - "restart data"
  - "User Agreement"
  - "account"
  - "mp_host_split"
  - "#SBATCH --cpus-per-task"
  - "Abaqus SHARCNET Academic License"
  - "OpenOnDemand"
  - "dedicated tokens"
  - "seff JobNumber"
  - "single node threaded process"
  - "Abaqus command"
  - "memory to minimize I/O"
  - "SBATCH directives"
  - "prototype Slurm scripts"
  - "SHARCNET license"
  - "top command"
  - "SLURM_TMPDIR"
  - "restart script"
  - "USER"
  - "SBATCH --gpus-per-node=h100:1"
  - "mpi-based computing"
  - "memory limit"
  - "MRMIO"
  - "Western Abaqus license"
  - "queued jobs"
  - "LICENSING-CLIENT-PORT-NUMBER"
  - "mem"
  - "lmlicensequeuing=OFF"
  - "home directory"
  - "DSLS_LICENSE_FILE"
  - "--mem=8G"
  - "license server ports"

questions:
  - "How do you configure a FLEXnet‑based Abaqus license server on a cluster?"
  - "Which commands can be used to verify the status and availability of Abaqus licenses?"
  - "What files and steps are required to set up a DSLS (Dassault Systèmes License Server) for Abaqus?"
  - "Where should the <code>abaqus_v6.env</code> file be placed to ensure DSLS_LICENSE_FILE is configured automatically?"
  - "What specific change must be made in the <code>~/.licenses/abaqus.lic</code> file after copying the <code>abaqus_v6.env</code> file?"
  - "How does loading an Abaqus module affect the licensing configuration described in the text?"
  - "How can you verify that the Abaqus license server is reachable and responding on an Alliance cluster?"
  - "What configuration changes and firewall port openings are required when adding a new Abaqus license server to an Alliance cluster?"
  - "How can you modify Abaqus license queuing behavior for Slurm jobs using the lmlicensequeuing and lmhanglimit settings?"
  - "What is the purpose of the optional `memory=` argument in the Slurm scripts, and when should it be adjusted?"
  - "Which “project directory scripts” are recommended for most users in the Single node computing sections?"
  - "How can a user obtain a full list of Abaqus command‑line arguments on the system?"
  - "When should a user use the project‑directory script instead of a restart script for single‑node jobs, and how does the expected runtime influence this choice?"
  - "How can large restart files be written efficiently, and what is the purpose of the SLURM_TMPDIR environment variable in the temporary‑directory scripts?"
  - "What procedure is recommended for determining the optimal number of cores and memory when running multi‑node MPI jobs, and how do the provided scripts support this scaling test?"
  - "How can a SLURM batch script be set up to run an Abaqus job using a GPU (e.g., h100) and a temporary scratch directory on the compute node?"
  - "What syntax must be included in the Abaqus input file to enable restart data writing, and how do you specify either a write frequency (e.g., every 12 increments) or a total number of restart increments?"
  - "Which command-line tools or grep patterns are recommended for checking the restart information (steps, start times, etc.) after the Abaqus simulation completes?"
  - "What effect does setting `order_parallel=OFF` have on the Abaqus simulation when placed at the bottom of the script?"
  - "How do the SBATCH directives (account, time, cpus-per-task, mem, nodes) configure the resources for the job submitted with this script?"
  - "Why is the `#SBATCH --constraint=granite` line commented out, and under what circumstances should it be enabled?"
  - "What does the “#SBATCH --gpus-per-node=h100:1” directive specify for the job?"
  - "Which software modules are loaded in the script, and what role do they play in the computation?"
  - "Why does the script unset SLURM_GTIDS, export MPI_IC_ORDER, echo SLURM variables, and remove the testst*.lck files?"
  - "How does the single‑node script configure SLURM resources and launch an Abaqus explicit analysis?"
  - "What are the required steps and environment settings in the multi‑node MPI script to run an Abaqus job across several nodes?"
  - "What format must the restart input file follow for Abaqus, and why are multinode restart scripts not provided?"
  - "What does the `pus-per-task=4` setting specify, and how does it influence the CPU resources allocated for the job?"
  - "Why does the script load the `StdEnv/2023` and `abaqus/2026` modules before executing the Abaqus job?"
  - "What is the purpose of echoing SLURM environment variables and creating the `$SLURM_TMPDIR/scratch` directory in this batch script?"
  - "How does the SLURM script set up resources and environment variables for running an Abaqus job in the project directory?"
  - "What commands and input file options are needed to write and verify restart data for 12 time increments in the simulation?"
  - "In what ways does the temporary‑directory workflow differ from the project‑directory workflow regarding file handling, copying, and cleanup?"
  - "What resources and job parameters are specified in the SBATCH directives of this script?"
  - "Which software modules are loaded, and which versions are requested?"
  - "How would you adjust the script to change the maximum runtime to 12 hours and request 16 GB of memory?"
  - "How does the single‑node SLURM script set up temporary directories, copy files, and launch the Abaqus job?"
  - "What SLURM directives and environment configurations are required in the “scriptep1‑mpi.txt” script to run an MPI‑based Abaqus simulation on multiple nodes?"
  - "Which approaches are recommended for estimating the memory needed by an Abaqus simulation on a Slurm node, and how are those estimates obtained?"
  - "How can you determine the appropriate Slurm memory allocation (‑mem) for a single‑node Abaqus job to satisfy the recommended “memory to minimize I/O” (MRMIO) value?"
  - "What steps should be followed to monitor the virtual (VIRT) and resident (RES) memory usage of an Abaqus job on a compute node using tools like top?"
  - "In a multi‑node Abaqus run, how is the required mem‑per‑cpu estimated from the output .dat file, and what effect does the mp_host_split parameter have on this calculation?"
  - "What method is suggested for obtaining a total memory estimate for a single‑node threaded process?"
  - "Which commands are recommended for monitoring the simulation’s memory usage?"
  - "What are the initial steps to start the simulation after obtaining an allocation on a compute node?"
  - "What factors cause the scratch disk usage to be near zero versus proportional to the memory difference?"
  - "Why can the exact amount of required scratch disk space not be accurately estimated?"
  - "Which platforms are recommended for running graphical applications on the Alliance?"
  - "How do you start an Abaqus CAE session on an OnDemand desktop, and which options (‑mesa or GPU/VirtualGL) should be used depending on the node type?"
  - "What are the steps to launch Abaqus via JupyterHub, including loading the appropriate module and accessing the Abaqus (VNC) icon?"
  - "What are the SHARCNET Abaqus licensing limits, costs, and the procedure required for a user to obtain access to the license?"
  - "What specific details (full name and username) are required to be entered in the license agreement?"
  - "Is it permissible for one user to complete the agreement on behalf of a group, or must each individual submit their own?"
  - "Does this individual completion requirement also apply to principal investigators who have purchased dedicated tokens?"
  - "What are the allowed purposes and institutional affiliations for using “SIMULIA Academic Software” with SHARCNET tokens?"
  - "How must the abaqus.lic file be configured (including environment variables) to work with the current SHARCNET license server, and what adjustments are required for different Abaqus versions?"
  - "Which commands can be used to query the SHARCNET license server for job and token status, and what does a “queued” job indicate about license availability?"
  - "How can you disable non‑interactive Abaqus jobs from queuing when there are not enough licenses available?"
  - "What is the purpose of the `lmhanglimit` parameter and how should it be set in the `abaqus_v6.env` file?"
  - "Which commands should be used to monitor and optimise memory and CPU resources for Abaqus jobs on the cluster?"
  - "What does the “R” status signify for the jobs listed in the output?"
  - "How much time is left for each job and on which compute nodes are they currently running?"
  - "According to the introductory comment, how does wasting resources affect the user’s fair‑share level?"
  - "How do you modify the `<code>#SBATCH --cpus-per-task=</code>` directive in a Slurm script to change the allocated CPU count?"
  - "What is the exact `srun` command syntax for monitoring a running job’s CPU, memory, and resident memory usage, and which job ID should be substituted?"
  - "What do the `%CPU`, `%MEM`, and `RES` columns represent when observing Abaqus parent processes on a compute node?"
  - "How is the required number of tokens calculated from the number of GPU cores?"
  - "Which compute systems are permitted to use the Western Abaqus site license, and how can a researcher obtain access?"
  - "What are the steps to configure the abaqus.lic file on Dusky and submit a job using a Slurm script?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! note "Under Review"
    This page is currently being reviewed.

[Abaqus FEA](https://www.3ds.com/products-services/simulia/products/abaqus/) is a software suite for finite element analysis and computer-aided engineering.

## Licensing
Abaqus software modules are available on the Alliance clusters; however, you must provide your own license. There are two types of license servers, each with different setup procedures described below.

### FLEXnet servers
To configure your account on a cluster to use a **FLEXnet-based** (also known as FlexLM) Abaqus license server, a single file named `~/.licenses/abaqus.lic` must first be created containing the license manager daemon port number `LMGRD-PORT-NUMBER` and the fully qualified hostname `FLEXnet-SERVER-HOSTNAME`. These two pieces of information are then assigned to the `ABAQUSLM_LICENSE_FILE` environment variable whenever an Abaqus module is loaded. Another file `abaqus_v6.env` may also need to exist in the home or job submission directory if it's not the assumed default:

```bash title="Example: Displaying abaqus_v6.env"
[l2 (login node):~ ] cat abaqus_v6.env
```
```text title="abaqus_v6.env"
license_server_type = FLEXNET
```
```bash title="Example: Displaying ~/.licenses/abaqus.lic"
[l2 (login node):~/.licenses] cat abaqus.lic
```
```text title="~/.licenses/abaqus.lic"
prepend_path("ABAQUSLM_LICENSE_FILE","LMGRD-PORT-NUMBER@FLEXnet-SERVER-HOSTNAME")
```

To check if your license server connection is working, run the following command:

```bash
[l2 (login node):~]$ module load abaqus
[l2 (login node):~]$ abaqus licensing ru | grep ABAQUSLM:
```
This command should indicate success with output similar to:
```text
  ABAQUSLM: UP v11.19.6.
```

To check how many CAE licenses in a pool are available for immediate use by anyone (the difference between "issued" and "in use"), run the following command. Note that reserved licenses will always appear to be "in use" regardless of whether they actually are or not by the group for which they are reserved. In the case of the SHARCNET license, there are 4 CAE licenses, but only 1 is reserved; therefore, 3 are in the pool available to anyone for use. The following example shows that at the time this command was run, none of the 3 CAE licenses in the pool were available for use by any group to run Abaqus in GUI mode on the Nibi cluster On-Demand graphical system.

```bash
[l2 (login node):~]$ abaqus licensing ru | grep cae
```
Expected output:
```text
Users of cae:  (Total of 4 licenses issued;  Total of 1 license in use)
"cae" v62.7, vendor: ABAQUSLM, expiry: 17-jan-2027
```

For a summary of ALL licenses provided by a license server:

```bash
[l2 (login node):~]$ module load abaqus
[l2 (login node):~]$ abaqus licensing r
```
Expected output:
```text
Feature                         Version     #licenses    Vendor        Expires
_______                         _________   _________    ______        ________
abaqus_extended                 62.7         4           ABAQUSLM      17-jan-2027
abaqus                          62.7         78          ABAQUSLM      17-jan-2027
ams                             62.7         1           ABAQUSLM      17-jan-2027
etc etc etc
```

### DSLS servers
To use a **DSLS**-based license server (Dassault Systèmes License Server), you must first configure two single-line text files named `~/.licenses/abaqus.lic` and `abaqus_v6.env` as shown below. You may either put a copy of `abaqus_v6.env` file into each job submit directory **OR** a single copy into your home directory. For example, placing both `abaqus_v6.env` files in your home directory, you would just need to replace `LICENSING-CLIENT-PORT-NUMBER:DSLS-SERVER-HOSTNAME` in your `~/.licenses/abaqus.lic` file, then `DSLS_LICENSE_FILE` will be configured accordingly whenever an Abaqus module is loaded:

```bash title="Example: Displaying abaqus_v6.env"
[l2 (login node):~ ] cat abaqus_v6.env
```
```text title="abaqus_v6.env"
license_server_type=DSLS
```
```bash title="Example: Displaying ~/.licenses/abaqus.lic"
[l2 (login node):~/.licenses] cat abaqus.lic
```
```text title="~/.licenses/abaqus.lic"
prepend_path("DSLS_LICENSE_FILE","LICENSING-CLIENT-PORT-NUMBER@DSLS-SERVER-HOSTNAME")
```

With both files set up, you may now check if the license server is reachable and responding by running:

```bash
[l2 (login node):~ ] module load abaqus
[l2 (login node):~ ] abaqus licensing dslsstat
```
If successful, the output message will contain "license servers declared". If it fails, the output message will contain "No license server available".

### New servers
If your license server was never set up for use on an Alliance cluster, some additional configuration changes by the Alliance system administrator and your local system administrator will need to be done. Such changes are necessary to ensure the required TCP ports (HTTPS protocol) of your Abaqus server are reachable from all cluster compute nodes through the client/server firewalls. For help, please write to [technical support](../support/technical_support.md) and be sure to include the following:
*   FLEXnet SERVER: lmgrd port number (default 27000), static vendor port number (default 28000)
    where both ports need to be opened on the Alliance cluster and license server firewalls
*   DSLS SERVER: administrative port number (default 4084), licensing client port number (default 4085)
    where only the licensing client port must be opened on the Alliance cluster and license server firewalls
*   Fully qualified domain name or IPV4 address of your new Abaqus server

You will be sent a list of cluster IP addresses (known as NAT nodes) so your administrator can open the local server firewall to allow connections from these nodes on the required port(s). Please note that a special license agreement must generally be negotiated and signed by both SIMULIA and your institution before a campus license may be used remotely on an Alliance cluster located on the campus of another institution.

## License queuing
The default setup for the license server is to queue jobs started on the cluster by Slurm if not enough tokens are available. There are two options to alter this behaviour so jobs don't sit idle on a cluster compute node, wasting valuable resources while waiting for a license indefinitely. The first option is to terminate a job immediately if not enough licenses are available, therefore never entering a queue. To specify this setting, create a text file named `abaqus_v6.env` in either your `/home` OR working (submit) directory containing the line: `lmlicensequeuing=OFF`. The second option is to specify a finite wait time, such as 1 minute, where the job can enter into a queued state on the license server by adding the line: `lmhanglimit=1`. If sufficient licenses do not become available within 1 minute, the job will be dequeued by the license server and, in turn, terminated by Slurm. For each option, messages will be printed at the bottom of the Slurm output file, as shown in [the Example below](#example).

## Version notes

### 2026
A new module `abaqus/2026` containing the initial *Abaqus 2026 Golden/GA* release has been installed into the default `StdEnv/2023` environment. Another module named `abaqus/2026.2614` containing the latest SIMULIA Established Products 2026 Fix Packs, currently at level FD02 (FP.2614), will be made available as soon as possible. To verify your setup, run the following:

```bash
module load abaqus/2026
module load intel/2024
abaqus verify -all
```
All tests should succeed except for CAE (unless you log into an OnDemand/Jupyter graphical desktop) and TOSCA (unless you set `export FED_DSFLEX_LICENSE_CONFIG=port@hostname`) before running the verification.

### 2021
It's recommended to discontinue use of `abaqus/2021` installed under the previous `StdEnv/2020` since this legacy version generates "*** buffer overflow detected ***" error on all recent clusters. An unshare workaround previously included in the single-node Slurm scripts of this wiki has now been removed.

## Cluster job submission
Below are prototype Slurm scripts for submitting thread-based and MPI-based parallel simulations to single or multiple compute nodes. Most users will find it sufficient to use one of the **project directory scripts** provided in the *Single node computing* sections. The optional `memory=` argument found in the last line of the scripts is intended for larger memory or problematic jobs where the 3072MB offset value may require tuning. A listing of all Abaqus command-line arguments can be obtained by loading an Abaqus module and running: `abaqus -help | less`.

Single-node jobs that run less than one day should find the *project directory script* located in the first tab sufficient. However, single-node jobs that run for more than a day should use one of the restart scripts. Jobs that create large restart files will benefit by writing to the local disk through the use of the `SLURM_TMPDIR` environment variable utilized in the **temporary directory scripts** provided in the two rightmost tabs of the single-node standard and explicit analysis sections. The restart scripts shown here will continue jobs that have been terminated early for some reason. Such job failures can occur if a job reaches its maximum requested runtime before completing and is killed by the queue or if the compute node the job was running on crashed due to an unexpected hardware failure. Other restart types are possible by further tailoring the input file (not shown here) to continue a job with additional steps or change the analysis (see the documentation for version-specific details).

Jobs that require large memory or larger compute resources (beyond that which a single compute node can provide) should use the MPI scripts in the **multiple node sections** below to distribute computing over arbitrary node ranges determined automatically by the scheduler. Short scaling test jobs should be run to determine wall-clock times (and memory requirements) as a function of the number of cores (2, 4, 8, etc.) to determine the optimal number before running any long jobs.

### Standard analysis
Abaqus solvers support thread-based and MPI-based parallelization. Scripts for each type are provided below for running Standard Analysis type jobs on single or multiple nodes, respectively. Lines that start with `##SBATCH` are commented; to uncomment, change to `#SBATCH`. Most users will find it sufficient to use the first `scriptsp1.txt` script that requires simply changing `def-group` to your account and `mystd-sim.inp` to the name of your input file before submitting with the "`sbatch scriptsp1.txt`" command.

#### Single node computing
=== "project directory script"
    ```sh title="scriptsp1.txt"
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
    ```
    To write restart data every N=12 time increments, specify in the input file:
    ```
    *RESTART, WRITE, OVERLAY, FREQUENCY=12
    ```
    To write restart data for a total of 12 time increments, specify instead:
    ```
    *RESTART, WRITE, OVERLAY, NUMBER INTERVAL=12, TIME MARKS=NO
    ```
    To check for completed restart information, use:
    ```bash
    egrep -i "step|start" testsp*.com testsp*.msg testsp*.sta
    ```
    Some simulations may benefit by adding the following to the Abaqus command at the bottom of the script:
    ```
    order_parallel=OFF
    ```

=== "project directory restart script"
    ```sh title="scriptsp2.txt"
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
    ```
    The restart input file should contain:
    ```
    *HEADING
    *RESTART, READ
    ```

=== "temporary directory script"
    ```sh title="scriptst1.txt"
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
    ```
    To write restart data every N=12 time increments, specify in the input file:
    ```
    *RESTART, WRITE, OVERLAY, FREQUENCY=12
    ```
    To write restart data for a total of 12 time increments, specify instead:
    ```
    *RESTART, WRITE, OVERLAY, NUMBER INTERVAL=12, TIME MARKS=NO
    ```
    To check the completed restart information, use:
    ```bash
    egrep -i "step|start" testst*.com testst*.msg testst*.sta
    ```

=== "temporary directory restart script"
    ```sh title="scriptst2.txt"
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
    ```
    The restart input file should contain:
    ```
    *HEADING
    *RESTART, READ
    ```

#### Multiple node computing
Users with large memory or compute needs (and correspondingly access to large licenses) can use the following script to perform MPI-based computing over an arbitrary range of nodes, ideally left for the scheduler to automatically determine. A companion template script to perform restart of multi-node jobs is not provided due to additional limitations on when they can be used. Only `abaqus/2026` or newer may be used with this script.

```sh title="scriptsp1-mpi.txt"
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
```

### Explicit analysis
Abaqus solvers support thread-based and MPI-based parallelization. Scripts for each type are provided below for running explicit analysis type jobs on single or multiple nodes, respectively. Template scripts to perform multi-node job restarts are not currently provided, pending further testing.

#### Single node computing
=== "project directory script"
    ```sh title="scriptep1.txt"
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
    ```
    To write restart data for a total of 12 time increments, specify in the input file:
    ```
    *RESTART, WRITE, OVERLAY, NUMBER INTERVAL=12, TIME MARKS=NO
    ```
    Check for completed restart information in relevant output files:
    ```bash
    egrep -i "step|restart" testep*.com testep*.msg testep*.sta
    ```

=== "project directory restart script"
    ```sh title="scriptep2.txt"
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
    ```
    No input file modifications are required to restart the analysis.

=== "temporary directory script"
    ```sh title="scriptet1.txt"
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
    ```
    To write restart data for a total of 12 time increments, specify in the input file:
    ```
    *RESTART, WRITE, OVERLAY, NUMBER INTERVAL=12, TIME MARKS=NO
    ```
    Check for completed restart information in relevant output files:
    ```bash
    egrep -i "step|restart" testet*.com testet*.msg testet*.sta
    ```

=== "temporary directory restart script"
    ```sh title="scriptet2.txt"
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
    ```
    No input file modifications are required to restart the analysis.

#### Multiple node computing
Users with large memory or compute needs (and correspondingly access to large licenses) can use the following script to perform MPI-based computing over an arbitrary range of nodes, ideally left for the scheduler to automatically determine. A companion template script to perform restart of multi-node jobs is not provided due to additional limitations on how they can be used. Only `abaqus/2026` or newer may be used with this script.

```sh title="scriptep1-mpi.txt"
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
```

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

Alternatively, a total memory estimate for a single-node threaded process can be obtained by running the simulation interactively on a compute node and then monitoring the memory use with the `top` (or `ps`) command as follows:
1.  First, obtain an allocation on a compute node and start your simulation running:

```bash
salloc --time=0:30:00 --cpus-per-task=8 --mem=64G --account=def-piname
module load StdEnv/2020
module load abaqus/2021
unset SLURM_GTIDS
abaqus job=test input=Sample.inp scratch=$SLURM_TMPDIR cpus=8 mp_mode=threads interactive
```
2.  Next, SSH into the compute node (c50 according to the `sq` command) and then run `top`, i.e.:

```bash
ssh c50
top -u $USER
```
3.  Watch the `VIRT` and `RES` columns until steady peak memory values are observed.

To completely satisfy the recommended "MEMORY TO OPERATIONS REQUIRED MINIMIZE I/O" (MRMIO) value, at least the same amount of non-swapped physical memory (RES) must be available to Abaqus. Since the `RES` will in general be less than the virtual memory (`VIRT`) by some relatively constant amount for a given simulation, it is necessary to slightly over-allocate the requested Slurm node memory `--mem=`. In the above sample Slurm script, this over-allocation has been hardcoded to a conservative value of 3072MB based on initial testing of the standard Abaqus solver. To avoid long queue wait times associated with large values of MRMIO, it may be worth investigating the simulation performance impact associated with reducing the `RES` memory that is made available to Abaqus significantly below the MRMIO. This can be done by lowering the `--mem=` value, which in turn will set an artificially low value of `memory=` in the Abaqus command (found in the last line of the script). In doing this, the `RES` cannot dip below the MINIMUM MEMORY REQUIRED (MMR); otherwise, Abaqus will exit due to Out of Memory (OOM). As an example, if your MRMIO is 96GB, try running a series of short test jobs with `#SBATCH --mem=8G, 16G, 32G, 64G` until an acceptable minimal performance impact is found, noting that smaller values will result in increasingly larger scratch space used by temporary files.

### Multi process
To determine the required Slurm memory for multi-node Slurm scripts, memory estimates (per compute process) required to minimize I/O are given in the output DAT file of completed jobs. If `mp_host_split` is not specified (or is set to 1), then the total number of compute processes will equal the number of nodes. The `mem-per-cpu` value can then be roughly determined by multiplying the largest memory estimate by the number of nodes and then dividing by the number of `ntasks`. However, if a value for `mp_host_split` is specified (greater than 1), then the `mem-per-cpu` value can be roughly determined from the largest memory estimate times the number of nodes times the value of `mp_host_split` divided by the number of tasks. Note that `mp_host_split` must be less than or equal to the number of cores per node assigned by Slurm at runtime; otherwise, Abaqus will terminate. This scenario can be controlled by uncommenting to specify a value for `tasks-per-node`. The following definitive statement is given in every output DAT file and mentioned here for reference:

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
It is recommended to use an OpenOnDemand or JupyterLab desktop environment to run graphical applications at the Alliance.

### OnDemand
1.  Start an OnDemand desktop session by clicking one of the following OnDemand links:
    *   [Nibi](../clusters/nibi.md#access-through-open-ondemand-ood): `https://ondemand.sharcnet.ca`
    *   TRILLIUM: [https://ondemand.scinet.utoronto.ca](https://ondemand.scinet.utoronto.ca)
2.  Open a new terminal window within your desktop and load:
    ```bash
    module load abaqus/2026
    ```
3.  Start the application in graphical mode using the `cae` option. If you are on either: 1) a node without a GPU, or 2) a node with a GPU but without VirtualGL support, then append the `mesa` option:
    ```bash
    abaqus cae -mesa
    ```
4.  If you require better graphical performance and are on a node with a GPU and VirtualGL support, then start Abaqus without the `-mesa` option. When using the Nibi OnDemand desktop, a full h100 (80GB) GPU from the GPU pulldown must be selected.
    ```bash
    abaqus cae
    ```
5.  To start Abaqus in GUI mode, there must be at least **one** unused CA license, according to:
    ```bash
    $ abaqus licensing lmstat -c $ABAQUSLM_LICENSE_FILE -a | grep "Users of cae"
    ```
    Example output showing available licenses:
    ```text
    Users of cae:  (Total of 4 licenses issued;  Total of 3 licenses in use)
    ```

### JupyterLab
1.  Start a JupyterHub desktop session by clicking one of the following JupyterHub links:
    *   FIR: [https://jupyterhub.fir.alliancecan.ca](https://jupyterhub.fir.alliancecan.ca)
    *   NARVAL: [https://portail.narval.calculquebec.ca/](https://portail.narval.calculquebec.ca/)
    *   RORQUAL: [https://jupyterhub.rorqual.alliancecan.ca](https://jupyterhub.rorqual.alliancecan.ca)
2.  Highlight an Abaqus module such as `abaqus/2026` in the left-hand side *Available Module* section.
3.  Click on *Load* for the highlighted module, and an `Abaqus (VNC)` icon will appear on the desktop.
4.  Click on the icon, and Abaqus should automatically be started in a remote Jupyter desktop.

### VncViewer
!!! warning "Obsolete"
    This approach is considered obsolete; please use the OnDemand/JupyterHub desktop environments instead.
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
The SHARCNET license has been renewed until 17-Jan-2027 and is operational. It provides a small shared free pool consisting of 3 CAE and 54 execute tokens for all researchers. Maximum usage limits are currently set at: 1 CAE/user, 10 tokens/user, and 15 tokens/group. These free tokens are available on a first-come, first-served basis and are mainly intended for testing and light usage before deciding whether or not to purchase dedicated tokens. Costs for dedicated tokens (in 2021) were approximately CAD$110 per compute token and CAD$400 per GUI token; submit a ticket to request an official quote if interested. The free SHARCNET license can be used by any registered Alliance researcher, but only on SHARCNET hardware, and only after agreeing to the Academic License User Agreement below. Groups that purchase dedicated tokens to run on the SHARCNET license server may likewise ONLY use them on SHARCNET hardware (as dictated by the negotiated license agreement with Simulia), including the SHARCNET [OOD](../clusters/nibi.md#access-through-open-ondemand-ood) system (to run Abaqus in graphical mode) or Nibi/Dusky clusters (for submitting compute batch jobs to the queue). Before you can use the license, you must contact [technical support](../support/technical_support.md) and request access. In your email: 1) mention that it is for use on SHARCNET systems, and 2) include a copy/paste of the following `License Agreement` statement with your full name and username entered in the indicated locations. Please note that every user must do this; it cannot be done one time only for a group; this includes PIs who have purchased their own dedicated tokens.

#### License agreement
````text
----------------------------------------------------------------------------------
Subject: Abaqus SHARCNET Academic License User Agreement

This email is to confirm that I "_____________" with username "___________" will
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
````

#### Configure license file
Configure your license file as follows, noting that it is only usable on SHARCNET systems such as the Nibi and Dusky clusters or the SHARCNET OOD desktop system. Note that the old `license3.sharcnet.ca` server has been permanently shut down; you must update your *abaqus.lic* file as follows to use the free SHARCNET license:
```bash
[l2 (nibi login node):~] cat ~/.licenses/abaqus.lic
```
```text title="~/.licenses/abaqus.lic"
prepend_path("ABAQUSLM_LICENSE_FILE","27050@license1.computecanada.ca")
```
If your Abaqus job fails with the error message "[*** ABAQUS/eliT_CheckLicense rank 0 terminated by signal 11 (Segmentation fault)]" then verify your `abaqus.lic` file contains `ABAQUSLM_LICENSE_FILE` when using `abaqus/202X` modules. If your Abaqus jobs fails with error message "[License server machine is down or not responding, etc.]" and you are using `abaqus/6.14.1`, then replace `ABAQUSLM_LICENSE_FILE` with `LM_LICENSE_FILE`.

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
II) Check the SHARCNET license server for started and queued jobs, also showing reservations by purchasing groups:
```bash
abaqus licensing lmstat -c $ABAQUSLM_LICENSE_FILE -a | egrep "Users|start|queued|RESERVATION"
```
III) Check the SHARCNET license server for only CAE, Standard, and Explicit product availability:
```bash
abaqus licensing lmstat -c $ABAQUSLM_LICENSE_FILE -a | grep "Users of" | egrep "cae|standard|explicit"
```
When the output of query I) above indicates that a job for a particular username is queued, this means the job has entered the "Running" state from the perspective of `squeue -j jobid` or `sacct -j jobid` and is therefore idle on a compute node waiting for a license. This will have the same impact on your account priority as if the job were performing computations and consuming CPU time. Eventually, when sufficient licenses become available, the queued job will start.

##### Example
The following shows the situation where a user submitted two 6-core jobs (each requiring 12 tokens) in quick succession. The scheduler then started each job on a different node in the order they were submitted. Since the user had 10 Abaqus compute tokens, the first job (27527287) was able to acquire exactly enough (10) tokens for the solver to begin running. The second job (27527297), not having access to any more tokens, entered an idle "queued" state (as can be seen from the `lmstat` output) until the first job completed, wasting the available resources and depreciating the user's fair share level in the process:

```bash
[l2 (nibi login node):~] sq
```
```text
            JOBID     USER              ACCOUNT           NAME  ST  TIME_LEFT NODES CPUS TRES_PER_N MIN_MEM NODELIST (REASON) 
         27530366  roberpj         cc-debug_cpu  scriptsp2.txt   R    9:56:13     1    6        N/A      8G     c107  (None) 
         27530407  roberpj         cc-debug_cpu  scriptsp2.txt   R    9:59:37     1    6        N/A      8G     c292  (None) 
```
```bash
[l2 (nibi login node):~] abaqus licensing lmstat -c $ABAQUSLM_LICENSE_FILE -a | egrep "Users|start|queued"
```
```text
 Users of abaqus:  (Total of 78 licenses issued;  Total of 53 licenses in use)
    roberpj c107 /dev/tty (v62.6) (license3.sharcnet.ca/27050 1042), start Mon 11/25 17:15, 10 licenses
    roberpj c292 /dev/tty (v62.6) (license3.sharcnet.ca/27050 125) queued for 10 licenses
```

To avoid license shortage problems when submitting multiple jobs when working with expensive Abaqus tokens, either use a [job dependency](../running-jobs/running_jobs.md#cancellation-of-jobs-with-dependency-conditions-which-cannot-be-met), a [job array](../running-jobs/job_arrays.md), or at the very least, set up a Slurm [email notification](../running-jobs/monitoring_jobs.md#email-notification) to know when your job completes before manually submitting another one. There are two easier options for dealing with this situation:

Option 1)
To disable non-interactive (analysis) jobs from starting on a cluster compute node after being submitted to the queue and then becoming idle (which is the default behaviour when not enough tokens are unavailable), create a text file in your submit directory (before submitting the job) with the following one-line contents, and the job will instead terminate immediately.

```bash title="Example: Creating abaqus_v6.env to disable queuing"
[l2 (nibi login node):~/submitdirectory] cat abaqus_v6.env
```
```text title="abaqus_v6.env"
lmlicensequeuing=OFF
```
When a job immediately terminates (without entering a QUEUED state to wait for a license), the end of the corresponding Slurm output file will contain messages such as:

```text
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

```bash title="Example: Creating abaqus_v6.env with lmhanglimit"
[l2 (nibi login node):~/submitdirectory] cat abaqus_v6.env
```
```text title="abaqus_v6.env"
lmhanglimit=1
```
When a job terminates this way, after being queued and no license becomes available in the specified time according to the `lmhanglimit` value (1 minute in this example), the messages at the end of the Slurm output file will instead appear as:

```text
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
To ensure optimal usage of both your Abaqus tokens and our resources, it's important to carefully specify the required memory and NCPUs in your Slurm script. The values can be determined by submitting a few short test jobs to the queue then checking their utilization. For **completed** jobs, use `seff JobNumber` to show the total *Memory Utilized* and *Memory Efficiency*. If the *Memory Efficiency* is less than ~90%, decrease the value of the `#SBATCH --mem=` setting in your Slurm script accordingly. Notice that the `seff JobNumber` command also shows the total *CPU (time) Utilized* and *CPU Efficiency*. If the *CPU Efficiency* is less than ~90%, perform scaling tests to determine the optimal number of CPUs for optimal performance and then update the value of `#SBATCH --cpus-per-task=` in your Slurm script. For **running** jobs, use the `srun --overlap --jobid=29821580 --pty top -d 5 -u $USER` command to watch the `%CPU`, `%MEM` and `RES` for each Abaqus parent process on the compute node. The `%CPU` and `%MEM` columns display the percent usage relative to the total available on the node, while the `RES` column shows the per-process resident memory size (in human-readable format for values over 1GB). Further information regarding how to [monitor jobs](../running-jobs/monitoring_jobs.md) is available on our documentation wiki.

#### Core-token mapping
```text
TOKENS 5  6  7  8  10  12  14  16  19  21  25  28  34  38
CORES  1  2  3  4   6   8  12  16  24  32  48  64  96 128
```
where TOKENS = floor[5 X CORES^0.422]

Each GPU used requires 1 additional TOKEN.

### Western license
The Western Abaqus site license may only be used by Western researchers on compute hardware located on Western's campus. Currently, only the `Dusky` cluster satisfies this condition. The `Nibi` and SHARCNET `OOD` systems may not be used since they are located on Waterloo's campus. Contact the Western Abaqus license server administrator <jmilner@robarts.ca> to inquire about being added to the Western Abaqus license. You will need to provide your Alliance username and possibly make arrangements with your supervisor to purchase tokens. If you are granted access, then you may proceed to log in to Dusky and configure your `abaqus.lic` file using a text editor such as `nano` to contain the following single line:

```bash
[laptop:~] ssh dusky.alliancecan.ca
```
```text title="~/.licenses/abaqus.lic"
[dus241:~] cat .licenses/abaqus.lic
prepend_path("ABAQUSLM_LICENSE_FILE","27000@authorize.robarts.ca")
```
Now you may submit your job using a Slurm script and the `sbatch` command as described in the *Cluster job submission* section above. If there are any problems, submit a problem ticket to [technical support](../support/technical_support.md). Specify that you are using the Abaqus Western license on Dusky and provide the failed job number along with a paste of any error messages as applicable.