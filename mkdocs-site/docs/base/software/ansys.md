---
title: "Ansys"
slug: "ansys"
lang: "base"

source_wiki_title: "Ansys"
source_hash: "c2d7262f3c8bbb4e4d04404a03cc5d2f"
last_synced: "2026-04-25T23:42:08.699101+00:00"
last_processed: "2026-04-26T00:08:53.223421+00:00"

tags:
  - software

keywords:
  - "DPM injections"
  - "parameters"
  - "aborting job"
  - ".flrecent"
  - "Slurm batch script"
  - "Ready To Use"
  - "SLURM_JOB_ID"
  - "Compute clusters"
  - "SLURM_ARRAY_TASK_ID"
  - "Interpreted or Compiled UDF"
  - "Linux"
  - "MPI"
  - "transient simulation"
  - "ANSYS-FLUENT"
  - "Job completed successfully"
  - "output files"
  - "fluent"
  - "Ansys license server"
  - "Engineering simulation"
  - "ANSYS CFX"
  - "cff-files"
  - "cluster filesystem"
  - "cfx5solve"
  - "machinefile"
  - "previous calculation"
  - "Slurm job script"
  - "software/hardware compatibility"
  - "Discrete Phase Model"
  - "transfer case file"
  - "Slurm scripts"
  - "License server"
  - "Setup Required"
  - "OpenMPI"
  - "Alliance"
  - "Service packs"
  - "Licensing"
  - "Platform support"
  - "License requeue"
  - "Slurm"
  - ".fluentconf"
  - "file format"
  - "time resource request"
  - "Job restart"
  - "time steps"
  - "Journal files"
  - "cas and dat files"
  - "ANSYS Fluent"
  - "Cluster batch job submission"
  - "firewall setup"
  - "CC_CLUSTER"
  - "Ansys Fluent"
  - "mesh partitioning"
  - "firewall changes"
  - "Restart simulation"
  - "solution restarts"
  - "total time of simulation"
  - "Fluent"
  - "Slurm time window"
  - "Interaction with Continuous Phase"
  - "Slurm scheduler"
  - "Fluent journal file"
  - "SLURM"
  - "bash script"
  - "project folder"
  - "Ansys"
  - "Multinode"
  - "Simulation failed"
  - "ln -s"
  - "Journal file"
  - "case and data files"
  - "Injections"
  - "journal file"
  - "parallel jobs"
  - "SLURM_ARRAY_JOB_ID"
  - "Spaceclaim"
  - "Time step"
  - "license or simulation issue"
  - "ansys.lic"
  - "openmpi"
  - "User-Defined Function"
  - "compute nodes"
  - "writable directory"
  - "Fluent User's Guide"
  - "scancel"
  - "version compatibility"
  - "Discrete Phase Models"
  - "Slurm job submission"
  - "Bash script"
  - "UDF"
  - "SLURM_NNODES"
  - "Solution restart"
  - "Resubmitting job"
  - "steady simulation"
  - "export data file"
  - "Alliance cluster"

questions:
  - "How does the licensing model for Ansys work on the clusters given that a generic license is not provided to everyone?"
  - "What are the specific steps and file paths required to configure a personal license file to point to a license server?"
  - "What technical requirements and firewall changes must be met before a new local institutional Ansys license server can be used on the Alliance clusters?"
  - "What information and steps are required to configure and test a local Ansys license server for use on an Alliance cluster?"
  - "How does version compatibility work for Ansys simulations, and how can a user determine which version was used to create a specific file?"
  - "Where can users find information regarding which Ansys applications are supported on specific operating systems like Linux or Windows?"
  - "What firewall changes must be made on the server and cluster sides before using a local institutional Ansys license server on the Alliance?"
  - "What steps should be followed to use an Ansys server that has already been configured and is considered \"Ready To Use\"?"
  - "What are the two additional steps required for Ansys servers that have never been used on the Alliance before?"
  - "Where can users find detailed software and hardware compatibility information for current and previous Ansys releases?"
  - "Why is the \"Platform Support by Application / Product\" PDF considered to be of special interest to users?"
  - "According to the text, why is the Spaceclaim package not supported on the Alliance?"
  - "What is the current limitation preventing the immediate use of the newly installed Ansys 2025R1.02 module?"
  - "How are Ansys service packs represented in the module naming convention, and why are multiple versions kept available for users?"
  - "What specific steps must a user follow to prepare and transfer a Fluent job from a desktop machine to the cluster for parallel computation?"
  - "How do you export or locate the data file from a previous calculation?"
  - "Which specific filesystems on the cluster should the case and data files be transferred to?"
  - "When and why should you rename the exported files instead of keeping their default names?"
  - "What is the primary purpose of creating a journal file when running Fluent simulations?"
  - "Why is it strongly recommended to monitor Slurm output files when configuring a script to automatically requeue failed jobs?"
  - "What are the performance and stability trade-offs between using a \"by node\" versus a \"by core\" Slurm script for large Fluent jobs?"
  - "How do the Slurm directives differ when allocating resources by core versus allocating by node for an ANSYS Fluent job?"
  - "What specific environment modules and variables need to be configured to run ANSYS Fluent on these clusters?"
  - "How does the script dynamically adjust the Fluent execution command and MPI settings based on the number of nodes and the specific cluster being used?"
  - "How does the script configure the MPI bootstrap environment variables based on the specific cluster being used?"
  - "What is the purpose of the slurm_hl2hl.py command and how is its output utilized in the script?"
  - "How do the ANSYS Fluent execution flags differ between single-node and multi-node job allocations?"
  - "How does the script construct the machinefile to track the number of cores assigned to each node?"
  - "What specific parameters change in the Fluent execution command when scaling from a single-node to a multi-node job?"
  - "What role do the Slurm environment variables play in determining the total number of tasks and the execution logic?"
  - "What are the specific ANSYS Fluent version requirements for running a job on the Trillium cluster compared to the Narval cluster?"
  - "How do the SLURM resource allocation directives differ between the \"by core\" submission script and the \"by node\" submission script?"
  - "What specific directory and file symlinks must be configured in the user's home directory to prevent the Trillium job script from aborting?"
  - "What specific conditions cause the script to output an error message and abort the current job?"
  - "What exact commands does the script instruct the user to run to fix the missing symbolic links?"
  - "Why does the system require the `.fluentconf` and `.flrecent` files to be linked to the `$SCRATCH` directory?"
  - "Under what specific conditions should the \"License requeue\" scripts be used for Fluent jobs?"
  - "Why is it advised against using the requeue scripts for simulations that crash after a long time or have unresolved journal warnings?"
  - "How does the provided Slurm script use job arrays and exit status checks to handle successful completions versus failed license checkout attempts?"
  - "What specific types of issues cause the script to trigger a failure message?"
  - "How does the script use Slurm array variables to determine whether to resubmit a failed job or exit?"
  - "What is the name and intended configuration of the multinode script referenced in the documentation tags?"
  - "How does the provided Slurm script utilize job arrays to handle simulation failures and automatic requeue attempts?"
  - "What specific MPI configurations and execution flags are applied based on the cluster environment (such as narval or nibi) and the number of nodes requested?"
  - "What specific modifications must be made to the initial and restart journal files to automate the continuation of large jobs that exceed the standard runtime limits?"
  - "How does the script utilize SLURM array tasks to manage the initial execution and subsequent solution restarts?"
  - "What cluster-specific MPI configurations and network interfaces are applied when running the job on Narval versus Nibi?"
  - "How does the post-execution logic automatically identify and link the most recent output files for the next restart iteration?"
  - "How is the total time of the simulation calculated based on the time step and the number of solution restarts?"
  - "What determines the total number of time steps and the corresponding number of output files generated?"
  - "How should the Slurm time resource request be configured to ensure all time steps complete within the allowed window?"
  - "How does the script identify and create symbolic links for the most recent .cas and .dat files in the output directory?"
  - "What specific Slurm command is executed to terminate the array job upon a successful completion?"
  - "How does the script handle the output messaging and execution flow in the event of a simulation failure?"
  - "How does the provided Slurm script utilize job arrays to manage simulation restarts and link the appropriate output files for the next time step?"
  - "What are the differences in MPI execution commands and network configurations when running the script on a single node versus multiple nodes across different clusters like Narval and Nibi?"
  - "What role do Fluent journal files play in automating simulations, and how can they be configured to switch between legacy and modern HDF5 file formats?"
  - "Where can users find additional information and a complete list of commands for modifying journal file parameters?"
  - "What specific command must be set in the journal file to utilize the more efficient .cas.h5/.dat.h5 file format?"
  - "How do the default file formats differ between module versions 2019R3 (or older) and 2020R1 (or newer)?"
  - "What are the specific journal file commands required to configure and execute a transient simulation compared to a steady-state simulation?"
  - "Why is the text mode setting critical when transferring User-Defined Function (UDF) source files from a Windows environment to a Linux cluster?"
  - "What precautions must be taken with the UDF dialog boxes and journal file commands before submitting a job to ensure the journal file maintains control?"
  - "How do the setup and execution processes differ between using interpreted and compiled User-Defined Functions (UDFs) in Ansys Fluent on a cluster?"
  - "Why is it necessary to instrument a serial UDF with compiler directives and macros before running it in a parallel Fluent job, and what are the consequences of failing to do so?"
  - "What are the available methods for defining particle injections and specifying \"Point Properties\" when integrating a Discrete Phase Model (DPM) UDF into a simulation?"
  - "Where must the UDF be located in relation to the journal, cas, and dat files?"
  - "At what point in the journal file should the UDF commands be added?"
  - "What configuration check must be performed on the UDF dialog boxes before uploading the cas file to the Alliance?"
  - "How can a user verify that an injection file has been loaded correctly in Fluent?"
  - "What is the purpose of enabling \"Interaction with Continuous Phase\" in the Discrete Phase Model Dialog Box?"
  - "How can the injection setup steps be automated after they are confirmed to work in the GUI?"
  - "What is the required data structure for a manually created steady injection file in DPM simulations?"
  - "How do the `-double` and `-large` command-line options affect the memory requirements and mesh size limits when running the CFX solver?"
  - "What are the key differences in the Slurm script configurations for running CFX on a single node versus multiple compute nodes?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Ansys is a software suite for engineering simulation and 3-D design. It includes packages such as [Ansys Fluent](http://www.ansys.com/Products/Fluids/ANSYS-Fluent) and [Ansys CFX](http://www.ansys.com/products/fluids/ansys-cfx).

## Licensing
We are a hosting provider for Ansys. This means that we have the software installed on our clusters, but we do not provide a generic license accessible to everyone. However, many institutions, faculties, and departments already have licenses that can be used on our clusters. Once the legal aspects are worked out for licensing, there will be remaining technical aspects. The license server on your end will need to be reachable by our compute nodes. This will require our technical team to get in touch with the technical people managing your license software. In some cases, this has already been done. You should then be able to load the Ansys module, and it should find its license automatically. If this is not the case, please contact our [technical support](../support/technical_support.md) so that they can arrange this for you.

### Configuring your license file
Our module for Ansys is designed to look for license information in a few places. One of those places is your `/home` folder. You can specify your license server by creating a file named `$HOME/.licenses/ansys.lic` consisting of two lines as shown. Customize the file by replacing FLEXPORT and LICSERVER with the appropriate values for your server.

!!! note "FILE: ansys.lic"
    ```text
    setenv("ANSYSLMD_LICENSE_FILE", "FLEXPORT@LICSERVER")
    ```

The following table provides established values for the CMC and SHARCNET license servers. To use a different server, locate the corresponding values as explained in [Local license servers](#local-license-servers).

| License | System/Cluster              | LICSERVER                  | FLEXPORT | NOTES                                                                                             |
| :------ | :-------------------------- | :------------------------- | :------- | :------------------------------------------------------------------------------------------------ |
| CMC     | fir                         | `172.26.0.101`             | `6624`   | !!! warning "Discontinue use" (to be shut down May 1/2026) [Discontinue use](https://www.cmc.ca/ansys-academic-research-software/) |
| CMC     | narval/rorqual              | `10.100.64.10`             | `6624`   | !!! warning "Discontinue use" (to be shut down May 1/2026) [Discontinue use](https://www.cmc.ca/ansys-academic-research-software/) |
| CMC     | nibi                        | `10.25.1.56`               | `6624`   | !!! warning "Discontinue use" (to be shut down May 1/2026) [Discontinue use](https://www.cmc.ca/ansys-academic-research-software/) |
| CMC     | trillium                    | scinet-cmc                 | `6624`   | !!! warning "Discontinue use" (to be shut down May 1/2026) [Discontinue use](https://www.cmc.ca/ansys-academic-research-software/) |
| SHARCNET| nibi/fir/narval/rorqual/trillium | `license1.computecanada.ca`| `1055`   |                                                                                                   |

Researchers who purchase a new CMC license subscription must [submit](https://www.cmc.ca/support/) your Alliance account username otherwise license checkouts will fail. The number of cores that can be used with a CMC license is described in the *Other Tricks and Tips* sections of the [Ansys Electronics Desktop and Ansys Mechanical/Fluids quick start guides](https://www.cmc.ca/?s=Other+Tricks+and+Tips&lang=en/).

### Local license servers
Before a local institutional Ansys license server can be used on the Alliance, firewall changes will need to be done on both the server and cluster side. For many Ansys servers this work has already been done and they can be used by following the steps in the "Ready To Use" section below. For Ansys servers that have never used on the Alliance, two additional steps must be done as shown in the "Setup Required" section also below.

#### Ready to use
To use a local institutional ANSYS License server whose network/firewall connections have already been set up for use on an Alliance cluster, contact your local Ansys license server administrator and get the following two pieces of information:
1. the configured Ansys flex port (FLEXPORT) number commonly 1055
2. the fully qualified hostname (LICSERVER) of the license server
Then simply configure your `~/.licenses/ansys.lic` file by plugging the values for FLEXPORT and LICSERVER into the `FILE: ansys.lic` template above.

#### Setup required
To use a local Ansys license server that has never been set up for use with an Alliance cluster, then you will ALSO need to get the following from your local Ansys license server administrator:
3. the statically configured vendor port (VENDPORT) of the license server
4. confirmation <servername> will resolve to the same IP address as LICSERVER on the cluster
where the <servername> can be found in the first line of the license file with format "SERVER <servername> <host id> <lmgrd port>". Send items 1->3 by email to [technical support](../support/technical_support.md) and mention which Alliance cluster you want to run Ansys jobs on. An Alliance system administrator will then open the outbound cluster firewall so license checkout requests can reach your license server from the cluster compute nodes. A range of IP addresses will then be sent back to you. Give these to your local network administrator. Request the firewall into your local license server be opened so that Ansys license connection (checkout requests) can reach your server's FLEXPORT and VENDPORT ports across the IP range.

### Checking license
To test if your `ansys.lic` is configured and working properly with your license server, run the following sequence of commands on the same cluster that you will be submitting jobs to:

```bash
cd /tmp
salloc --time=1:0:0 --mem=1000M --account=def-YOURUSERID
module load StdEnv/2023; module load ansys/2025R2.04
$EBROOTANSYS/v$(echo ${EBVERSIONANSYS:2:2}${EBVERSIONANSYS:5:1})/licensingclient/linx64/lmutil lmstat -c $ANSYSLMD_LICENSE_FILE | grep "ansyslmd: UP" 1> /dev/null && echo Success || echo Fail
```
`Success` output indicates license checkouts should work when jobs are submitted to the queue.
`Fail` output indicates a problem with the licensing setup somewhere and jobs will likely fail.

If there is an Ansys license server checkout problem, then the following message will appear in Slurm output files when Fluent jobs are started by Slurm scripts in the queue **OR** when Fluent is started interactively simply by doing the following:

```bash
fluent -g 2d -n 2
```
```text
Connected License Server List:	<Shared_Web_License_Server>
Hit return to exit.
```

## Version compatibility
Ansys simulations are typically forward compatible but **NOT** backwards compatible. This means that simulations created using an older version of Ansys can be expected to load and run fine with any newer version. For example, a simulation created and saved with `ansys/2022R2` should load and run smoothly with `ansys/2023R2` but **NOT** the other way around. While it may be possible to start a simulation running with an older version, random error messages or crashing will likely occur. Regarding Fluent simulations, if you cannot recall which version of Ansys was used to create your `.cas` file try grepping it as follows to look for clues:

```bash
grep -ia fluent combustor.cas
```
```text
(0 "fluent15.0.7  build-id: 596")
```

```bash
grep -ia fluent cavity.cas.h5
```
```text
ANSYS_FLUENT 24.1 Build 1018
```

### Platform support
Ansys provides detailed platform support information describing software/hardware compatibility for the [Current Release](https://www.ansys.com/it-solutions/platform-support) and [Previous Releases](https://www.ansys.com/it-solutions/platform-support/previous-releases). The *Platform Support by Application / Product* PDF is of special interest since it shows which packages are supported under Windows but not under Linux and thus not on the Alliance, such as SpaceClaim.

### What's new
Ansys posts [Product Release and Updates](https://www.ansys.com/products/release-highlights) for the latest releases. Similar information for previous releases can generally be pulled up for various application topics by visiting the Ansys [blog](https://www.ansys.com/blog) page and using the FILTERS search bar. For example, searching on `What’s New Fluent 2024 gpu` pulls up a document with title `[What’s New for Ansys Fluent in 2024 R1?](https://www.ansys.com/blog/fluent-2024-r1)` containing a wealth of the latest GPU support information. Specifying a version number in the [Press Release](https://www.ansys.com/news-center/press-releases) search bar is also a good way to find new release information. Recently a module for the latest ANSYS release was installed `ansys/2025R1.02`, however to use it requires a suitably updated license server such as CMC's. The upgrade of the SHARCNET license server is underway, however until it is complete (and this message updated accordingly) it will only support jobs run with `ansys/2024R2.04` or older. To request a new version be installed or report a problem with an existing module please [submit a ticket](../support/technical_support.md).

### Service packs
Starting with Ansys 2024 a separate Ansys module will appear on the clusters with a decimal and two digits appearing after the release number whenever a service pack is installed over the initial release. For example, the initial 2024 release with no service pack applied may be loaded with `module load ansys/2024R1` while a module with Service Pack 3 applied may be loaded with `module load ansys/2024R1.03` instead. If a service pack is already available by the time a new release is to be installed, then most likely only a module for that service pack number will be installed unless a request to install the initial release is also received.

Most users will likely want to load the latest module version equipped with the latest installed service pack which can be achieved by simply doing `module load ansys`. While it's not expected service packs will impact numerical results, the changes they make are extensive and so, if computations have already been done with the initial release or an earlier service pack then some groups may prefer to continue using it. Having separate modules for each service pack makes this possible. Starting with Ansys 2024R1 a detailed description of what each service pack does can be found by searching this [link](https://storage.ansys.com/staticfiles/cp/Readme/release2024R1/info_combined.pdf) for *Service Pack Details*. Future versions will presumably be similarly searchable by manually modifying the version number contained in the link.

## Cluster batch job submission
The Ansys software suite comes with multiple implementations of MPI to support parallel computation. Unfortunately, none of them support our [Slurm scheduler](../running-jobs/running_jobs.md). For this reason, we need special instructions for each Ansys package on how to start a parallel job. In the sections below, we give examples of submission scripts for some of the packages. While the Slurm scripts should work on all clusters, Niagara users may need to make some additional changes covered [here](https://docs.scinet.utoronto.ca/index.php).

### Fluent
Typically, you would use the following procedure to run Fluent on one of our clusters:

1. Prepare your Fluent job using Fluent from the Ansys Workbench on your desktop machine up to the point where you would run the calculation.
2. Export the "case" file with *File > Export > Case…* or find the folder where Fluent saves your project's files. The case file will often have a name like `FFF-1.cas.gz`.
3. If you already have data from a previous calculation, which you want to continue, export a "data" file as well (*File > Export > Data…*) or find it in the same project folder (`FFF-1.dat.gz`).
4. [Transfer](../getting-started/transferring_data.md) the case file (and if needed the data file) to a directory on the [/project](../storage-and-data/project_layout.md) or [/scratch](../storage-and-data/storage_and_file_management.md#storage-types) filesystem on the cluster. When exporting, you can save the file(s) under a more instructive name than `FFF-1.*` or rename them when they are uploaded.
5. Now you need to create a "journal" file. Its purpose is to load the case file (and optionally the data file), run the solver and finally write the results. See examples below and remember to adjust the filenames and desired number of iterations.
6. If jobs frequently fail to start due to license shortages and manual resubmission of failed jobs is not convenient, consider modifying your script to requeue your job (up to 4 times) as shown under the *by node + requeue* tab further below. Be aware that doing this will also requeue simulations that fail due to non-license related issues (such as divergence), resulting in lost compute time. Therefore it is strongly recommended to monitor and inspect each Slurm output file to confirm each requeue attempt is license related. When it is determined that a job is requeued due to a simulation issue, immediately manually kill the job progression with `scancel jobid` and correct the problem.
7. After [running the job](../running-jobs/running_jobs.md), you can download the data file and import it back into Fluent with *File > Import > Data…*.

#### Slurm scripts

##### General purpose
Most Fluent jobs should use the following *by node* script to minimize solution latency and maximize performance over as few nodes as possible. Very large jobs, however, might wait less in the queue if they use a *by core* script. However, the startup time of a job using many nodes can be significantly longer, thus offsetting some of the benefits. In addition, be aware that running large jobs over an unspecified number of potentially very many nodes will make them far more vulnerable to crashing if any of the compute nodes fail during the simulation. The scripts will ensure Fluent uses shared memory for communication when run on a single node or distributed memory (utilizing MPI and the appropriate HPC interconnect) when run over multiple nodes. The two Narval tabs may be useful to provide a more robust alternative if Fluent crashes during the initial auto mesh partitioning phase when using the standard Intel-based scripts with the parallel solver. The other option would be to manually perform the mesh partitioning in the Fluent GUI then try to run the job again on the cluster with the Intel scripts. Doing so will allow you to inspect the partition statistics and specify the partitioning method to obtain an optimal result. The number of mesh partitions should be an integral multiple of the number of cores; for optimal efficiency, ensure at least 10,000 cells per core.

=== "Multinode (by node)"
    ```bash
    #!/bin/bash

    #SBATCH --account=def-group   # Specify account name
    #SBATCH --time=00-03:00       # Specify time limit dd-hh:mm
    #SBATCH --nodes=1             # Specify number of compute nodes (narval 1 node max)
    #SBATCH --ntasks-per-node=32  # Specify upto maximum number of cores per compute node
    #SBATCH --mem=0               # Specify memory per compute node (0 allocates all memory)
    #SBATCH --cpus-per-task=1     # Do not change

    module load StdEnv/2023       # Do not change
    module load ansys/2023R2      # or newer versions

    MYJOURNALFILE=sample.jou      # Specify your journal file name
    MYVERSION=3d                  # Specify 2d, 2ddp, 3d or 3ddp

    # ------- do not change any lines below --------

    if [[ "$CC_CLUSTER" == narval ]]; then
    module load intel/2023 intelmpi
    export INTELMPI_ROOT=$I_MPI_ROOT
    unset I_MPI_ROOT
    fi

    if [[ ("${EBVERSIONANSYS//R*}" -ge 2025 && "${CC_CLUSTER}" == nibi) || "${CC_CLUSTER}" == narval ]]; then
    export I_MPI_HYDRA_BOOTSTRAP=ssh
    unset I_MPI_HYDRA_BOOTSTRAP_EXEC_EXTRA_ARGS
    fi

    slurm_hl2hl.py --format ANSYS-FLUENT > /tmp/machinefile-$SLURM_JOB_ID
    NCORES=$SLURM_NTASKS

    if [ "$SLURM_NNODES" == 1 ]; then
    fluent -g $MYVERSION -t $NCORES -mpi=intel -pshmem -i $MYJOURNALFILE
    else
    if [[ "${CC_CLUSTER}" == nibi ]]; then
        fluent -g $MYVERSION -t $NCORES -mpi=intel -peth -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOURNALFILE
    else
        fluent -g $MYVERSION -t $NCORES -mpi=intel -pib -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOURNALFILE
    fi
    fi
    ```
=== "Multinode (by core)"
    ```bash
    #!/bin/bash

    #SBATCH --account=def-group   # Specify account
    #SBATCH --time=00-03:00       # Specify time limit dd-hh:mm
    ##SBATCH --nodes=1            # Uncomment to specify (narval 1 node max)
    #SBATCH --ntasks=16           # Specify total number of cores across all nodes
    #SBATCH --mem-per-cpu=4G      # Specify memory per core
    #SBATCH --cpus-per-task=1     # Do not change

    module load StdEnv/2023       # Do not change
    module load ansys/2023R2      # or newer versions

    MYJOURNALFILE=sample.jou      # Specify your journal file name
    MYVERSION=3d                  # Specify 2d, 2ddp, 3d or 3ddp

    # ------- do not change any lines below --------

    if [[ "$CC_CLUSTER" == narval ]]; then
    module load intel/2023 intelmpi
    export INTELMPI_ROOT=$I_MPI_ROOT
    unset I_MPI_ROOT
    fi

    if [[ ("${EBVERSIONANSYS//R*}" -ge 2025 && "${CC_CLUSTER}" == nibi) || "${CC_CLUSTER}" == narval ]]; then
    export I_MPI_HYDRA_BOOTSTRAP=ssh
    unset I_MPI_HYDRA_BOOTSTRAP_EXEC_EXTRA_ARGS
    fi

    slurm_hl2hl.py --format ANSYS-FLUENT > /tmp/machinefile-$SLURM_JOB_ID
    NCORES=$SLURM_NTASKS

    if [ "$SLURM_NNODES" == 1 ]; then
    fluent -g $MYVERSION -t $NCORES -mpi=intel -pshmem -i $MYJOURNALFILE
    else
    if [[ "${CC_CLUSTER}" == nibi ]]; then
        fluent -g $MYVERSION -t $NCORES -mpi=intel -peth -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOURNALFILE
    else
        fluent -g $MYVERSION -t $NCORES -mpi=intel -pib -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOURNALFILE
    fi
    fi
    ```
=== "Multinode (by node, Narval)"
    ```bash
    #!/bin/bash

    #SBATCH --account=def-group   # Specify account name
    #SBATCH --time=00-03:00       # Specify time limit dd-hh:mm
    #SBATCH --nodes=1             # Specify number of compute nodes (1 or more)
    #SBATCH --ntasks-per-node=64  # Specify number of cores per node (narval 64 or less)
    #SBATCH --mem=0               # Do not change (allocate all memory per compute node)
    #SBATCH --cpus-per-task=1     # Do not change

    module load StdEnv/2023       # Do not change
    module load ansys/2023R2      # or newer versions

    MYJOURNALFILE=sample.jou      # Specify your journal file name
    MYVERSION=3d                  # Specify 2d, 2ddp, 3d or 3ddp

    # ------- do not change any lines below --------

    export OPENMPI_ROOT=$EBROOTOPENMPI
    slurm_hl2hl.py --format ANSYS-FLUENT > /tmp/mf-$SLURM_JOB_ID
    for i in `cat /tmp/mf-$SLURM_JOB_ID | uniq`; do echo "${i}:$(cat /tmp/mf-$SLURM_JOB_ID | grep $i | wc -l)" >> /tmp/machinefile-$SLURM_JOB_ID; done
    NCORES=$SLURM_NTASKS

    if [ "$SLURM_NNODES" == 1 ]; then
    fluent -g $MYVERSION -t $NCORES -mpi=openmpi -pshmem -i $MYJOURNALFILE
    else
    export FI_PROVIDER=verbs
    fluent -g $MYVERSION -t $NCORES -mpi=openmpi -pib -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOURNALFILE
    fi
    ```
=== "Multinode (by core, Narval)"
    ```bash
    #!/bin/bash

    #SBATCH --account=def-group   # Specify account name
    #SBATCH --time=00-03:00       # Specify time limit dd-hh:mm
    ##SBATCH --nodes=1            # Uncomment to specify number of compute nodes (1 or more)
    #SBATCH --ntasks=16           # Specify total number of cores across all nodes
    #SBATCH --mem-per-cpu=4G      # Specify memory per core
    #SBATCH --cpus-per-task=1     # Do not change

    module load StdEnv/2023       # Do not change     
    module load ansys/2023R2      # or newer versions

    MYJOURNALFILE=sample.jou      # Specify your journal file name
    MYVERSION=3d                  # Specify 2d, 2ddp, 3d or 3ddp

    # ------- do not change any lines below --------

    export OPENMPI_ROOT=$EBROOTOPENMPI
    slurm_hl2hl.py --format ANSYS-FLUENT > /tmp/mf-$SLURM_JOB_ID
    for i in `cat /tmp/mf-$SLURM_JOB_ID | uniq`; do echo "${i}:$(cat /tmp/mf-$SLURM_JOB_ID | grep $i | wc -l)" >> /tmp/machinefile-$SLURM_JOB_ID; done
    NCORES=$SLURM_NTASKS

    if [ "$SLURM_NNODES" == 1 ]; then
    fluent -g $MYVERSION -t $NCORES -mpi=openmpi -pshmem -i $MYJOURNALFILE
    else
    export FI_PROVIDER=verbs
    fluent -g $MYVERSION -t $NCORES -mpi=openmpi -pib -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOURNALFILE
    fi
    ```
=== "Multinode (by node, Trillium)"
    ```bash
    #!/bin/bash

    #SBATCH --account=def-group      # Specify account name
    #SBATCH --time=00-03:00          # Specify time limit dd-hh:mm
    #SBATCH --nodes=1                # Specify number of compute nodes (1 or more)
    #SBATCH --ntasks-per-node=16     # Specify number cores per node (max 192 on trillium)
    ##SBATCH --mem=0                 # Do not uncomment (by default trillium uses all memory per node)
    #SBATCH --cpus-per-task=1        # Do not change (required parameter)
    #SBATCH --output=slurm-%j.out    # Writes to slurm-$SLURM_JOB_ID.out

    cd $SLURM_SUBMIT_DIR             # Submit from $SCRATCH/some/dir

    module load StdEnv/2023          # Do not change
    module load ansys/2025R2.04      # only 2025R2 or newer works on trillium

    MYJOURNALFILE=sample.jou         # Specify your journal file name
    MYVERSION=3d                     # Specify 2d, 2ddp, 3d or 3ddp

    # ------- do not change any lines below --------

    slurm_hl2hl.py --format ANSYS-FLUENT > $SLURM_SUBMIT_DIR/machinefile-$SLURM_JOB_ID
    NCORES=$SLURM_NTASKS

    if [ ! -L "$HOME/.ansys" ]; then
    echo "ERROR: A link to a writable .ansys directory does not exist."
    echo 'Remove ~/.ansys if one exists and then run: ln -s $SCRATCH/.ansys ~/.ansys'
    echo "Then try submitting your job again. Aborting the current job now!"
    elif [ ! -L "$HOME/.fluentconf" ]; then
    echo "ERROR: A link to a writable .fluentconf directory does not exist."
    echo 'Remove ~/.fluentconf if one exists and run: ln -s $SCRATCH/.fluentconf ~/.fluentconf'
    echo "Then try submitting your job again. Aborting the current job now!"
    elif [ ! -L "$HOME/.flrecent" ]; then
    echo "ERROR: A link to a writable .flrecent file does not exist."
    echo 'Remove ~/.flrecent if one exists and then run: ln -s $SCRATCH/.flrecent ~/.flrecent'
    echo "Then try submitting your job again. Aborting the current job now!"
    else
    mkdir -pv $SCRATCH/.ansys
    mkdir -pv $SCRATCH/.fluentconf
    touch $SCRATCH/.flrecent
    if [ "$SLURM_NNODES" == 1 ]; then
        fluent -g $MYVERSION -t $NCORES -mpi=intel -pshmem -i $MYJOURNALFILE
    else
        fluent -g $MYVERSION -t $NCORES -mpi=intel -pib -cnf=$SLURM_SUBMIT_DIR/machinefile-$SLURM_JOB_ID -i $MYJOURNALFILE
    fi
    fi
    ```

##### License requeue
The scripts in this section should only be used with Fluent jobs that are known to complete normally without generating any errors in the output, however typically require multiple requeue attempts to checkout licenses. They are not recommended for Fluent jobs that may 1) run for a long time before crashing 2) run to completion but contain unresolved journal file warnings, since in both cases the simulations will be repeated from the beginning until the maximum number of requeue attempts specified by the `array` value is reached. For these types of jobs, the general purpose scripts above should be used instead.

=== "Multinode (by node + requeue)"
    ```bash
    #!/bin/bash

    #SBATCH --account=def-group   # Specify account
    #SBATCH --time=00-03:00       # Specify time limit dd-hh:mm
    #SBATCH --nodes=1             # Specify number of compute nodes (narval 1 node max)
    #SBATCH --ntasks-per-node=32  # Specify upto maximum number of cores per compute node
    #SBATCH --mem=0               # Specify memory per compute node (0 allocates all memory)
    #SBATCH --cpus-per-task=1     # Do not change
    #SBATCH --array=1-5%1         # Specify number of requeue attempts (2 or more, 5 is shown)

    module load StdEnv/2023       # Do not change
    module load ansys/2023R2      # Specify version (or newer)

    MYJOURNALFILE=sample.jou      # Specify your journal file name
    MYVERSION=3d                  # Specify 2d, 2ddp, 3d or 3ddp

    # ------- do not change any lines below --------

    if [[ "$CC_CLUSTER" == narval ]]; then
    module load intel/2023 intelmpi
    export INTELMPI_ROOT=$I_MPI_ROOT
    unset I_MPI_ROOT
    fi

    if [[ ("${EBVERSIONANSYS//R*}" -ge 2025 && "${CC_CLUSTER}" == nibi) || "${CC_CLUSTER}" == narval ]]; then
    export I_MPI_HYDRA_BOOTSTRAP=ssh
    unset I_MPI_HYDRA_BOOTSTRAP_EXEC_EXTRA_ARGS
    fi

    slurm_hl2hl.py --format ANSYS-FLUENT > /tmp/machinefile-$SLURM_JOB_ID
    NCORES=$SLURM_NTASKS

    if [ "$SLURM_NNODES" == 1 ]; then
    fluent -g $MYVERSION -t $NCORES -mpi=intel -pshmem -i $MYJOURNALFILE
    else
    if [[ "${CC_CLUSTER}" == nibi ]]; then
        fluent -g $MYVERSION -t $NCORES -mpi=intel -peth -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOURNALFILE
    else
        fluent -g $MYVERSION -t $NCORES -mpi=intel -pib -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOURNALFILE
    fi
    fi
    if [ $? -eq 0 ]; then
        echo "Job completed successfully! Exiting now."
        scancel $SLURM_ARRAY_JOB_ID
    else
        echo "Job attempt $SLURM_ARRAY_TASK_ID of $SLURM_ARRAY_TASK_COUNT failed due to license or simulation issue!"
        if [ $SLURM_ARRAY_TASK_ID -lt $SLURM_ARRAY_TASK_COUNT ]; then
        echo "Resubmitting job now …"
        else
        echo "All job attempts failed exiting now."
        fi
    fi
    ```
=== "Multinode (by core + requeue)"
    ```bash
    #!/bin/bash

    #SBATCH --account=def-group   # Specify account
    #SBATCH --time=00-03:00       # Specify time limit dd-hh:mm
    ##SBATCH --nodes=1            # Uncomment to specify (narval 1 node max) 
    #SBATCH --ntasks=16           # Specify total number of cores
    #SBATCH --mem-per-cpu=4G      # Specify memory per core
    #SBATCH --cpus-per-task=1     # Do not change
    #SBATCH --array=1-5%1         # Specify number of requeue attempts (2 or more, 5 is shown)

    module load StdEnv/2023       # Do not change
    module load ansys/2023R2      # Specify version (or newer)

    MYJOURNALFILE=sample.jou      # Specify your journal file name
    MYVERSION=3d                  # Specify 2d, 2ddp, 3d or 3ddp

    # ------- do not change any lines below --------

    if [[ "$CC_CLUSTER" == narval ]]; then
    module load intel/2023 intelmpi
    export INTELMPI_ROOT=$I_MPI_ROOT
    unset I_MPI_ROOT
    fi

    if [[ ("${EBVERSIONANSYS//R*}" -ge 2025 && "${CC_CLUSTER}" == nibi) || "${CC_CLUSTER}" == narval ]]; then
    export I_MPI_HYDRA_BOOTSTRAP=ssh
    unset I_MPI_HYDRA_BOOTSTRAP_EXEC_EXTRA_ARGS
    fi

    slurm_hl2hl.py --format ANSYS-FLUENT > /tmp/machinefile-$SLURM_JOB_ID
    NCORES=$SLURM_NTASKS

    if [ "$SLURM_NNODES" == 1 ]; then
    fluent -g $MYVERSION -t $NCORES -mpi=intel -pshmem -i $MYJOURNALFILE
    else
    if [[ "${CC_CLUSTER}" == nibi ]]; then
        fluent -g $MYVERSION -t $NCORES -mpi=intel -peth -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOURNALFILE
    else
        fluent -g $MYVERSION -t $NCORES -mpi=intel -pib -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOURNALFILE
    fi
    fi
    if [ $? -eq 0 ]; then
        echo "Job completed successfully! Exiting now."
        scancel $SLURM_ARRAY_JOB_ID
    else
        echo "Job attempt $SLURM_ARRAY_TASK_ID of $SLURM_ARRAY_TASK_COUNT failed due to license or simulation issue!"
        if [ $SLURM_ARRAY_TASK_ID -lt $SLURM_ARRAY_TASK_COUNT ]; then
        echo "Resubmitting job now …"
        else
        echo "All job attempts failed exiting now."
        fi
    fi
    ```

##### Solution restart
The following two scripts are provided to automate restarting very large jobs that require more than the typical seven-day maximum runtime window available on most clusters. Jobs are restarted from the most recent saved time step files. A fundamental requirement is the first time step can be completed within the requested job array time limit (specified at the top of your Slurm script) when starting a simulation from an initialized solution field. It is assumed that a standard fixed time step size is being used. To begin, a working set of `sample.cas`, `sample.dat` and `sample.jou` files must be present. Next edit your `sample.jou` file to contain `/solve/dual-time-iterate 1` and `/file/auto-save/data-frequency 1`. Then create a restart journal file by doing `cp sample.jou sample-restart.jou` and edit the `sample-restart.jou` file to contain `/file/read-cas-data sample-restart` instead of `/file/read-cas-data sample` and comment out the initialization line with a semicolon for instance `; /solve/initialize/initialize-flow`. If your second and subsequent time steps are known to run twice as fast (as the initial time step), edit `sample-restart.jou` to specify `/solve/dual-time-iterate 2`. By doing this, the solution will only be restarted after two time steps are completed following the initial time step. An output file for each time step will still be saved in the output subdirectory. The value 2 is arbitrary but should be chosen such that the time for 2 steps fits within the job array time limit. Doing this will minimize the number of solution restarts which are computationally expensive. If your first time step performed by `sample.jou` starts from a converged (previous) solution, choose 1 instead of 2 since likely all time steps will require a similar amount of wall time to complete. Assuming 2 is chosen, the total time of simulation to be completed will be `1*Dt+2*Nrestart*Dt` where `Nrestart` is the number of solution restarts specified in the script. The total number of time steps (and hence the number of output files generated) will therefore be `1+2*Nrestart`. The value for the time resource request should be chosen so the initial time step and subsequent time steps will complete comfortably within the Slurm time window specifiable up to a maximum of `"#SBATCH --time=07-00:00"` days.

=== "Multinode (by node + restart)"
    ```bash
    #!/bin/bash

    #SBATCH --account=def-group   # Specify account
    #SBATCH --time=07-00:00       # Specify time limit dd-hh:mm
    #SBATCH --nodes=1             # Specify number of compute nodes (narval 1 node max)
    #SBATCH --ntasks-per-node=32  # Specify upto maximum number of cores per compute node
    #SBATCH --mem=0               # Specify memory per compute node (0 allocates all memory)
    #SBATCH --cpus-per-task=1     # Do not change
    #SBATCH --array=1-5%1         # Specify number of solution restarts (2 or more, 5 is shown)

    module load StdEnv/2023       # Do not change
    module load ansys/2023R2      # Specify version (or newer)

    MYVERSION=3d                        # Specify 2d, 2ddp, 3d or 3ddp
    MYJOUFILE=sample.jou                # Specify your journal filename
    MYJOUFILERES=sample-restart.jou     # Specify journal restart filename
    MYCASFILERES=sample-restart.cas.h5  # Specify cas restart filename
    MYDATFILERES=sample-restart.dat.h5  # Specify dat restart filename

    # ------- do not change any lines below --------

    if [[ "$CC_CLUSTER" == narval ]]; then
    module load intel/2023 intelmpi
    export INTELMPI_ROOT=$I_MPI_ROOT
    unset I_MPI_ROOT
    fi

    if [[ ("${EBVERSIONANSYS//R*}" -ge 2025 && "${CC_CLUSTER}" == nibi) || "${CC_CLUSTER}" == narval ]]; then
    export I_MPI_HYDRA_BOOTSTRAP=ssh
    unset I_MPI_HYDRA_BOOTSTRAP_EXEC_EXTRA_ARGS
    fi

    slurm_hl2hl.py --format ANSYS-FLUENT > /tmp/machinefile-$SLURM_JOB_ID
    NCORES=$SLURM_NTASKS

    if [ "$SLURM_NNODES" == 1 ]; then
    if [ "$SLURM_ARRAY_TASK_ID" == 1 ]; then
        fluent -g 2ddp -t $NCORES -mpi=intel -pshmem -i $MYJOUFILE
    else
        fluent -g 2ddp -t $NCORES -mpi=intel -pshmem -i $MYJOUFILERES
    fi
    else 
    if [ "$SLURM_ARRAY_TASK_ID" == 1 ]; then
    if [[ "${CC_CLUSTER}" == nibi ]]; then
        fluent -g $MYVERSION -t $NCORES -mpi=intel -peth -cnf=/tmp/machinefile-$SLURM_JOB_ID -ssh -i $MYJOUFILE
    else
        fluent -g $MYVERSION -t $NCORES -mpi=intel -pib -cnf=/tmp/machinefile-$SLURM_JOB_ID -ssh -i $MYJOUFILE
    fi
    else
    if [[ "${CC_CLUSTER}" == nibi ]]; then
        fluent -g $MYVERSION -t $NCORES -mpi=intel -peth -cnf=/tmp/machinefile-$SLURM_JOB_ID -ssh -i $MYJOUFILERES
    else
        fluent -g $MYVERSION -t $NCORES -mpi=intel -pib -cnf=/tmp/machinefile-$SLURM_JOB_ID -ssh -i $MYJOUFILERES
    fi
    fi
    fi
    if [ $? -eq 0 ]; then
        echo
        echo "SLURM_ARRAY_TASK_ID  = $SLURM_ARRAY_TASK_ID"
        echo "SLURM_ARRAY_TASK_COUNT = $SLURM_ARRAY_TASK_COUNT"
        echo
        if [ $SLURM_ARRAY_TASK_ID -lt $SLURM_ARRAY_TASK_COUNT ]; then
        echo "Restarting job with the most recent output dat file …"
        ln -sfv output/$(ls -ltr output | grep .cas | tail -n1 | awk '{print $9}') $MYCASFILERES
        ln -sfv output/$(ls -ltr output | grep .dat | tail -n1 | awk '{print $9}') $MYDATFILERES
        ls -lh cavity* output/*
        else
        echo "Job completed successfully! Exiting now."
        scancel $SLURM_ARRAY_JOB_ID
        fi
    else
        echo "Simulation failed. Exiting …"
    fi
    ```
=== "Multinode (by core + restart)"
    ```bash
    #!/bin/bash

    #SBATCH --account=def-group   # Specify account
    #SBATCH --time=00-03:00       # Specify time limit dd-hh:mm
    ##SBATCH --nodes=1            # Uncomment to specify (narval 1 node max)
    #SBATCH --ntasks=16           # Specify total number of cores
    #SBATCH --mem-per-cpu=4G      # Specify memory per core
    #SBATCH --cpus-per-task=1     # Do not change
    #SBATCH --array=1-5%1         # Specify number of restart aka time steps (2 or more, 5 is shown)

    module load StdEnv/2023       # Do not change
    module load ansys/2023R2      # Specify version (or newer)

    MYVERSION=3d                        # Specify 2d, 2ddp, 3d or 3ddp
    MYJOUFILE=sample.jou                # Specify your journal filename
    MYJOUFILERES=sample-restart.jou     # Specify journal restart filename
    MYCASFILERES=sample-restart.cas.h5  # Specify cas restart filename
    MYDATFILERES=sample-restart.dat.h5  # Specify dat restart filename

    # ------- do not change any lines below --------

    if [[ "$CC_CLUSTER" == narval ]]; then
    module load intel/2023 intelmpi
    export INTELMPI_ROOT=$I_MPI_ROOT
    unset I_MPI_ROOT
    fi

    if [[ ("${EBVERSIONANSYS//R*}" -ge 2025 && "${CC_CLUSTER}" == nibi) || "${CC_CLUSTER}" == narval ]]; then
    export I_MPI_HYDRA_BOOTSTRAP=ssh
    unset I_MPI_HYDRA_BOOTSTRAP_EXEC_EXTRA_ARGS
    fi

    slurm_hl2hl.py --format ANSYS-FLUENT > /tmp/machinefile-$SLURM_JOB_ID
    NCORES=$SLURM_NTASKS

    if [ "$SLURM_NNODES" == 1 ]; then
    if [ "$SLURM_ARRAY_TASK_ID" == 1 ]; then
        fluent -g $MYVERSION -t $NCORES -mpi=intel -pshmem -I $MYFILEJOU
    else
        fluent -g $MYVERSION -t $NCORES -mpi=intel -pshmem -I $MYFILEJOURES
    fi
    else 
    if [ "$SLURM_ARRAY_TASK_ID" == 1 ]; then
        if [[ "${CC_CLUSTER}" == nibi ]]; then
        fluent -g $MYVERSION -t $NCORES -mpi=intel -peth -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOUFILE
        else
        fluent -g $MYVERSION -t $NCORES -mpi=intel -pib -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOUFILE
        fi
    else
        if [[ "${CC_CLUSTER}" == nibi ]]; then
        fluent -g $MYVERSION -t $NCORES -mpi=intel -peth -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOUFILERES
        else
        fluent -g $MYVERSION -t $NCORES -mpi=intel -pib -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOUFILERES
        fi
    fi
    fi
    if [ $? -eq 0 ]; then
        echo
        echo "SLURM_ARRAY_TASK_ID  = $SLURM_ARRAY_TASK_ID"
        echo "SLURM_ARRAY_TASK_COUNT = $SLURM_ARRAY_TASK_COUNT"
        echo
        if [ $SLURM_ARRAY_TASK_ID -lt $SLURM_ARRAY_TASK_COUNT ]; then
        echo "Restarting job with the most recent output dat file"
        ln -sfv output/$(ls -ltr output | grep .cas | tail -n1 | awk '{print $9}') $MYCASFILERES
        ln -sfv output/$(ls -ltr output | grep .dat | tail -n1 | awk '{print $9}') $MYDATFILERES
        ls -lh cavity* output/*
        else
        echo "Job completed successfully! Exiting now."
        scancel $SLURM_ARRAY_JOB_ID
        fi
    else
        echo "Simulation failed. Exiting now."
    fi
    ```

#### Journal files
Fluent journal files can include basically any command from Fluent's Text-User-Interface (TUI); commands can be used to change simulation parameters like temperature, pressure and flow speed. With this you can run a series of simulations under different conditions with a single case file, by only changing the parameters in the journal file. Refer to the Fluent User's Guide for more information and a list of all commands that can be used. The following journal files are set up with `/file/cff-files no` to use the legacy .cas/.dat file format (the default in module versions 2019R3 or older). Set this instead to `/file/cff-files yes` to use the more efficient .cas.h5/.dat.h5 file format (the default in module versions 2020R1 or newer).

=== "Journal file (steady, case)"
    ```text
    ; SAMPLE FLUENT JOURNAL FILE - STEADY SIMULATION
    ; ----------------------------------------------
    ; lines beginning with a semicolon are comments

    ; Overwrite files by default
    /file/confirm-overwrite no

    ; Preferentially read/write files in legacy format
    /file/cff-files no

    ; Read input case and data files
    /file/read-case-data FFF-in

    ; Run the solver for this many iterations
    /solve/iterate 1000

    ; Overwrite output files by default
    /file/confirm-overwrite n

    ; Write final output data file
    /file/write-case-data FFF-out

    ; Write simulation report to file (optional)
    /report/summary y "My_Simulation_Report.txt"

    ; Cleanly shutdown fluent
    /exit
    ```
=== "Journal file (steady, case + data)"
    ```text
    ; SAMPLE FLUENT JOURNAL FILE - STEADY SIMULATION
    ; ----------------------------------------------
    ; lines beginning with a semicolon are comments

    ; Overwrite files by default
    /file/confirm-overwrite no

    ; Preferentially read/write files in legacy format
    /file/cff-files no

    ; Read input files
    /file/read-case-data FFF-in

    ; Write a data file every 100 iterations
    /file/auto-save/data-frequency 100

    ; Retain data files from 5 most recent iterations
    /file/auto-save/retain-most-recent-files y

    ; Write data files to output sub-directory (appends iteration)
    /file/auto-save/root-name output/FFF-out

    ; Run the solver for this many iterations
    /solve/iterate 1000

    ; Write final output case and data files
    /file/write-case-data FFF-out

    ; Write simulation report to file (optional)
    /report/summary y "My_Simulation_Report.txt"

    ; Cleanly shutdown fluent
    /exit
    ```
=== "Journal file (transient)"
    ```text
    ; SAMPLE FLUENT JOURNAL FILE - TRANSIENT SIMULATION
    ; -------------------------------------------------
    ; lines beginning with a semicolon are comments

    ; Overwrite files by default
    /file/confirm-overwrite no

    ; Preferentially read/write files in legacy format
    /file/cff-files no

    ; Read the input case file
    /file/read-case FFF-transient-inp

    ; For continuation (restart) read in both case and data input files
    ;/file/read-case-data FFF-transient-inp

    ; Write a data (and maybe case) file every 100 time steps
    /file/auto-save/data-frequency 100
    /file/auto-save/case-frequency if-case-is-modified

    ; Retain only the most recent 5 data (and maybe case) files
    /file/auto-save/retain-most-recent-files y

    ; Write to output sub-directory (appends flowtime and timestep)
    /file/auto-save/root-name output/FFF-transient-out-%10.6f

    ; ##### Settings for Transient simulation :  #####

    ; Set the physical time step size
    /solve/set/time-step 0.0001

    ; Set the number of iterations for which convergence monitors are reported
    /solve/set/reporting-interval 1

    ; ##### End of settings for Transient simulation #####

    ; Initialize using the hybrid initialization method
    /solve/initialize/hyb-initialization

    ; Set max number of iters per time step and number of time steps
    ;/solve/set/max-iterations-per-time-step 75
    ;/solve/dual-time-iterate 1000 ,
    /solve/dual-time-iterate 1000 75

    ; Write final case and data output files
    /file/write-case-data FFF-transient-out

    ; Write simulation report to file (optional)
    /report/summary y Report_Transient_Simulation.txt

    ; Cleanly shutdown fluent
    /exit
    ```

#### UDFs
The first step is to transfer your User-Defined Function or UDF (namely the `sampleudf.c` source file and any additional dependency files) to the cluster. When uploading from a Windows machine, be sure the text mode setting of your transfer client is used, otherwise Fluent won't be able to read the file properly on the cluster since it runs Linux. The UDF should be placed in the directory where your journal, cas and dat files reside. Next add one of the following commands into your journal file before the commands that read in your simulation cas/dat files. Regardless of whether you use the Interpreted or Compiled UDF approach, before uploading your cas file onto the Alliance please check that neither the Interpreted UDFs Dialog Box or the UDF Library Manager Dialog Box are configured to use any UDF; this will ensure that only the journal file commands are in control when jobs are submitted.

##### Interpreted
To tell Fluent to interpret your UDF at runtime, add the following command line into your journal file before the cas/dat files are read or initialized. The filename `sampleudf.c` should be replaced with the name of your source file. The command remains the same regardless if the simulation is being run in serial or parallel. To ensure the UDF can be found in the same directory as the journal file, open your cas file in the Fluent GUI, remove any managed definitions and resave it. Doing this will ensure only the following command/method is in control when Fluent runs. To use an interpreted UDF with parallel jobs, it will need to be parallelized as described in the section below.

```bash
define/user-defined/interpreted-functions "sampleudf.c" "cpp" 10000 no
```

##### Compiled
To use this approach, your UDF must be compiled on an Alliance cluster at least once. Doing so will create a `libudf` subdirectory structure containing the required `libudf.so` shared library. The `libudf` directory cannot simply be copied from a remote system (such as your laptop) to the Alliance since the library dependencies of the shared library will not be satisfied, resulting in Fluent crashing on startup. That said, once you have compiled your UDF on an Alliance cluster, you can transfer the newly created `libudf` to any other Alliance cluster, providing your account loads the same `StdEnv` environment module version. Once copied, the UDF can be used by uncommenting the second (load) `libudf` line below in your journal file when submitting jobs to the cluster. Both (compile and load) `libudf` lines should not be left uncommented in your journal file when submitting jobs on the cluster, otherwise your UDF will be automatically (re)compiled for each and every job. Not only is this highly inefficient, but it will also lead to race-condition-like build conflicts if multiple jobs are run from the same directory. Besides configuring your journal file to build your UDF, the Fluent GUI may also be used. To do this, navigate to the *Compiled UDFs Dialog Box*, add the UDF source file and click *Build*. When using a compiled UDF with parallel jobs, your source file should be parallelized as discussed in the section below.

```bash
define/user-defined/compiled-functions compile libudf yes sampleudf.c "" ""
```

and/or

```bash
define/user-defined/compiled-functions load libudf
```

##### Parallel
Before a UDF can be used with a Fluent parallel job (single node SMP and multinode MPI) it will need to be parallelized. By doing this we control how/which processes (host and/or compute) run specific parts of the UDF code when Fluent is run in parallel on the cluster. The instrumenting procedure involves adding compiler directives, predicates and reduction macros into your working serial UDF. Failure to do so will result in Fluent running slow at best or immediately crashing at worst. The end result will be a single UDF that runs efficiently when Fluent is used in both serial and parallel mode. The subject is described in detail under *Part I: Chapter 7: Parallel Considerations* of the Ansys 2024 *Fluent Customization Manual* which can be accessed [here](#help-resources).

##### DPM
UDFs can be used to customize Discrete Phase Models (DPM) as described in *Part III: Solution Mode | Chapter 24: Modeling Discrete Phase | 24.2 Steps for Using the Discrete Phase Models| 24.2.6 User-Defined Functions* of the *2024R2 Fluent Users Guide* and section *Part I: Creating and Using User Defined Functions | Chapter 2: DEFINE Macros | 2.5 Discrete Phase Model (DPM) DEFINE Macros* of the *2024R2 Fluent Customization Manual*. Before a DPM-based UDF can be worked into a simulation, the injection of a set of particles must be defined by specifying "Point Properties" with variables such as source position, initial trajectory, mass flow rate, time duration, temperature and so forth depending on the injection type. This can be done in the GUI by clicking the *Physics* panel, *Discrete Phase* to open the *Discrete Phase Model* box and then clicking the *Injections* button. Doing so will open an *Injections* dialog box where one or more injections can be created by clicking the *Create* button. The "Set Injection Properties" dialog which appears will contain an "Injection Type" pulldown with first four types available are "single, group, surface, flat-fan-atomizer". If you select any of these then you can then the "Point Properties" tab can be selected to input the corresponding Value fields. Another way to specify the "Point Properties" would be to read an injection text file. To do this select "file" from the *Injection Type* pulldown, specify the Injection Name to be created and then click the *File* button (located beside the *OK* button at the bottom of the "Set Injection Properties" dialog). Here either an Injection Sample File (with `.dpm` extension) or a manually created injection text file can be selected. To Select the File in the *Select File* dialog box change the *File of type* pull down to *All Files (\*)*, then highlight the file which could have any arbitrary name but commonly does have a `.inj` extension, click the *OK* button. Assuming there are no problems with the file, no Console error or warning message will appear in Fluent. As you will be returned to the *Injections* dialog box, you should see the same Injection name that you specified in the "Set Injection Properties" dialog and be able to *List its Particles and Properties* in the console. Next open the *Discrete Phase Model Dialog Box* and select *Interaction with Continuous Phase* which will enable updating DPM source terms every flow iteration. This setting can be saved in your cas file or added via the journal file as shown. Once the injection is confirmed working in the GUI the steps can be automated by adding commands to the journal file after solution initialization, for example:

```text
/define/models/dpm/interaction/coupled-calculations yes
/define/models/dpm/injections/delete-injection injection-0:1
/define/models/dpm/injections/create injection-0:1 no yes file no zinjection01.inj no no no no
/define/models/dpm/injections/list-particles injection-0:1
/define/models/dpm/injections/list-injection-properties injection-0:1
```
where a basic manually created injection steady file format might look like:
```bash
cat zinjection01.inj
```
```text
(z=4 12)
( x          y        z    u         v    w    diameter  t         mass-flow  mass  frequency  time name )
(( 2.90e-02  5.00e-03 0.0 -1.00e-03  0.0  0.0  1.00e-04  2.93e+02  1.00e-06   0.0   0.0        0.0 ) injection-0:1 )
```
noting that injection files for DPM simulations are generally set up for either steady or unsteady particle tracking where the format of the former is described in subsection *Part III: Solution Mode | Chapter 24: Modeling Discrete Phase | 24.3. Setting Initial Conditions for the Discrete Phase | 24.3.13 Point Properties for File Injections | 24.3.13.1 Steady File Format* of the *2024R2 Fluent Customization Manual*.

### CFX

#### Slurm scripts
A summary of command-line options can be printed by running `cfx5solve -help` where the same module version that's loaded in your Slurm script should be first manually loaded. By default `cfx5solve` will run in single precision (`-single`). To run `cfx5solve` in double precision add the `-double` option noting that doing so will also double memory requirements. By default `cfx5solve` can support meshes with up to 80 million elements (structured) or 200 million elements (unstructured). For larger meshes with up to 2 billion elements, add the `-large` option. Various combinations of these options can be specified for the Partitioner, Interpolator or Solver. Consult the ANSYS CFX-Solver Manager User's Guide for further details.

=== "Single node"
    ```bash
    #!/bin/bash

    #SBATCH --account=def-group   # Specify account name
    #SBATCH --time=00-03:00       # Specify time limit dd-hh:mm
    #SBATCH --nodes=1             # Do not change
    #SBATCH --ntasks-per-node=4   # Specify number of cores
    #SBATCH --mem=16G             # Specify total memory
    #SBATCH --cpus-per-task=1     # Do not change

    #module load StdEnv/2020      # Uncomment to use (deprecated)     
    #module load 2021R2           # Specify 2021R2 only

    module load StdEnv/2023
    module load ansys/2023R2      # Or newer module versions

    # append additional cfx5solve command line options as required
    if [[ "$CC_CLUSTER" = narval || "$CC_CLUSTER" == fir ]]; then
    cfx5solve -def YOURFILE.def -start-method "Open MPI Local Parallel" -part $SLURM_CPUS_ON_NODE
    else
    cfx5solve -def YOURFILE.def -start-method "Intel MPI Local Parallel" -part $SLURM_CPUS_ON_NODE
    fi
    ```
=== "Multinode"
    ```bash
    #!/bin/bash

    #SBATCH --account=def-group   # Specify account name
    #SBATCH --time=00-03:00       # Specify time limit dd-hh:mm
    #SBATCH --nodes=2             # Specify multiple compute nodes (2 or more)
    #SBATCH --ntasks-per-node=192 # Use all cores per compute node (do not change)
    #SBATCH --mem=0               # Use all memory on each compute node (do not change)
    #SBATCH --cpus-per-task=1     # Do not change

    #module load StdEnv/2020      # Uncomment to use (deprecated)     
    #module load 2021R2           # Specify 2021R2 only

    module load StdEnv/2023
    module load ansys/2023R2      # Or newer module versions

    NNODES=$(slurm_hl2hl.py --format ANSYS-CFX)

    # append additional cfx5solve command line options as required
    if [[ "$CC_CLUSTER" = narval || "$CC_CLUSTER" == fir ]]; then
    cfx5solve -def YOURFILE.def -start-method "Open MPI Distributed Parallel" -par-dist $NNODES
    else
    export I_MPI_HYDRA_BOOTSTRAP=ssh
    unset I_MPI_HYDRA_BOOTSTRAP_EXEC_EXTRA_ARGS
    cfx5solve -def YOURFILE.def -start-method "Intel MPI Distributed Parallel" -par-dist $NNODES
    fi
    ```

### Workbench
Before submitting a Workbench job to the queue with a Slurm script, you must initialize it once as described in the following steps.
1. On the cluster where you will submit Workbench jobs (Nibi for example) open an [OnDemand](https://ondemand.sharcnet.ca) desktop. For the purpose of this section it will be sufficient and fastest to select either a Compute Desktop (without a GPU) or a Basic Desktop resource.
2. Once the desktop appears, open a terminal window and `cd` into your directory containing your `YOURPROJECT.wbpj` file.
3. Remove the old project cache directory by running `rm -rf _ProjectScratch` as this can be very large from previous runs.
4. Open a terminal window and load the module version that you will be using in your Slurm script for example `module load ansys/2025R2.04`.
5. Open the Workbench GUI with your project file. This can be done by issuing `runwb2 -f YOURPROJECT.wbpj` directly from the command line. If and when a pop-up appears asking "Do you want to recover the project before opening ? (Any changes made since the last save will be lost.)" answer **No**.
6. In the context menu pop-up that should appear in the centre Project Schematic window, right-click on *Model* and select *Reset*. When Ansys Workbench pops up a warning that "This operation will delete the operations local and generated data" click **Ok** to accept and proceed.
7. In the top menu bar pulldown, select *File -> Save* then *File -> Exit* to shut down Workbench.
8. In the Ansys Workbench pop-up, when asked *The current project has been modified. Do you want to save it?*, click on the *No* button.
9. Quit Workbench and submit your job using one of the Slurm scripts shown below.

!!! tip
    Since a Compute Node with up to 96 cores, 768 GB memory and 8 hours runtime can now be reserved for an OnDemand desktop session, consider running your Workbench simulations directly from within the Workbench native GUI when possible as a more intuitive option compared to submitting the job to the queue with a Slurm script.

#### Slurm scripts
A project file can be submitted to the queue by customizing one of the following scripts and then running the `sbatch script-wbpj-202X.sh` command:

=== "Single node (StdEnv/2023)"
    ```bash
    #!/bin/bash

    #SBATCH --account=def-account
    #SBATCH --time=00-03:00                # Time (DD-HH:MM)
    #SBATCH --mem=16G                      # Specify total memory
    #SBATCH --ntasks=4                     # Specify number of cores
    #SBATCH --nodes=1                      # Do not change (multi-node not supported)
    ##SBATCH --exclusive                   # Uncomment ONLY for scaling testing
    ##SBATCH --constraint=broadwell        # Uncomment to specify an available node type

    module load StdEnv/2023 ansys/2023R2   # OR newer Ansys module versions

    if [ "$SLURM_NNODES" == 1 ]; then
    MEMPAR=0                             # Set to 0 for SMP (shared memory parallel)
    else
    MEMPAR=1                             # Set to 1 for DMP (distributed memory parallel)
    fi

    rm -fv *_files/.lock
    MWFILE=~/.mw/Application\ Data/Ansys/`basename $(find $EBROOTANSYS/v* -maxdepth 0 -type d)`/SolveHandlers.xml
    sed -re "s/(.AnsysSolution>+)[a-zA-Z0-9]*(<\/Distribute.)/\1$MEMPAR\2/" -i "$MWFILE"
    sed -re "s/(.Processors>+)[a-zA-Z0-9]*(<\/MaxNumber.)/\1$SLURM_NTASKS\2/" -i "$MWFILE"
    sed -i "s!UserConfigured=\"0\"!UserConfigured=\"1\"!g" "$MWFILE"

    export KMP_AFFINITY=disabled
    export I_MPI_HYDRA_BOOTSTRAP=ssh

    runwb2 -B -E "Update();Save(Overwrite=True)" -F YOURPROJECT.wbpj
    ```
=== "Single node (StdEnv/2020)"
    ```bash
    #!/bin/bash

    #SBATCH --account=def-account
    #SBATCH --time=00-03:00                # Time (DD-HH:MM)
    #SBATCH --mem=16G                      # Specify total memory
    #SBATCH --ntasks=4                     # Specify number of cores
    #SBATCH --nodes=1                      # Do not change (multi-node not supported)
    ##SBATCH --exclusive                   # Uncomment ONLY for scaling testing
    ##SBATCH --constraint=broadwell        # Uncomment to specify an available node type

    module load StdEnv/2020 ansys/2022R2   # OR older Ansys module versions

    if [ "$SLURM_NNODES" == 1 ]; then
    MEMPAR=0                             # Set to 0 for SMP (shared memory parallel)
    else
    MEMPAR=1                             # Set to 1 for DMP (distributed memory parallel)
    fi

    rm -fv *_files/.lock
    MWFILE=~/.mw/Application\ Data/Ansys/`basename $(find $EBROOTANSYS/v* -maxdepth 0 -type d)`/SolveHandlers.xml
    sed -re "s/(.AnsysSolution>+)[a-zA-Z0-9]*(<\/Distribute.)/\1$MEMPAR\2/" -i "$MWFILE"
    sed -re "s/(.Processors>+)[a-zA-Z0-9]*(<\/MaxNumber.)/\1$SLURM_NTASKS\2/" -i "$MWFILE"
    sed -i "s!UserConfigured=\"0\"!UserConfigured=\"1\"!g" "$MWFILE"

    export KMP_AFFINITY=disabled
    export I_MPI_HYDRA_BOOTSTRAP=ssh

    runwb2 -B -E "Update();Save(Overwrite=True)" -F YOURPROJECT.wbpj
    ```

To avoid writing the solution when a running job successfully completes change `Save(Overwrite=True)` to `Save(Overwrite=False)` in the last line of the above Slurm script. Doing this will make it easier to determine how well the simulation scales when `#SBATCH --ntasks` is increased since the initialized solution will not be overwritten by each test job.

### Mechanical
The input file can be generated from within your interactive Workbench Mechanical session by clicking *Solution -> Tools -> Write Input Files* then specify `File name:` `YOURAPDLFILE.inp` and `Save as type:` `APDL Input Files (*.inp)`. APDL jobs can then be submitted to the queue by running the `sbatch script-name.sh` command.

#### Slurm scripts
In the following Slurm scripts, lines beginning with `##SBATCH` are commented.

=== "Shared Memory Parallel (CPU)"
    ```bash
    #!/bin/bash
    #SBATCH --account=def-account   # Specify your account
    #SBATCH --time=00-03:00         # Specify time (DD-HH:MM)
    #SBATCH --mem=32G               # Specify memory for all cores
    #SBATCH --nodes=1               # Do not change
    #SBATCH --tasks=8               # Specify number of cores
    #SBATCH --cpus-per-task=1       # Do not change

    module load StdEnv/2023
    #module load ansys/2023R2
    module load ansys/2024R1.03

    mkdir outdir-$SLURM_JOBID
    [[ "$CC_CLUSTER" = cedar ]] && export LD_LIBRARY_PATH=$EBROOTGCC/../lib/gcc

    mapdl -smp -b nolist -np $SLURM_NTASKS -dir outdir-$SLURM_JOBID -i YOURAPDLFILE.inp
    ```
=== "Distributed Memory Parallel (CPU)"
    ```bash
    #!/bin/bash
    #SBATCH --account=def-account   # Specify your account
    #SBATCH --time=00-03:00         # Specify time (DD-HH:MM)
    #SBATCH --mem-per-cpu=4G        # Specify memory per core
    ##SBATCH --nodes=2              # Specify number of nodes (optional)
    #SBATCH --ntasks=8              # Specify number of cores
    ##SBATCH --ntasks-per-node=4    # Specify cores per node (optional)
    #SBATCH --cpus-per-task=1       # Do not change

    module load StdEnv/2023
    #module load ansys/2023R2
    module load ansys/2024R1.03

    mkdir outdir-$SLURM_JOBID
    if [[ "$CC_CLUSTER" = cedar ]]; then
    ln -s $EBROOTGCC/../lib/gcc/libstdc++.so.6.0.29 $PWD/outdir-$SLURM_JOBID/libstdc++.so.6.0.29
    export LD_LIBRARY_PATH=$PWD/outdir-$SLURM_JOBID
    fi

    if [[ "$CC_CLUSTER" = beluga  ]]; then
    export KMP_AFFINITY=none
    mapdl -dis -mpi intelmpi -b nolist -np $SLURM_NTASKS -dir outdir-$SLURM_JOBID -i YOURAPDLFILE.inp
    else
    mapdl -dis -mpi openmpi -b nolist -np $SLURM_NTASKS -dir outdir-$SLURM_JOBID -i YOURAPDLFILE.inp
    fi
    ```
=== "Shared Memory Parallel (GPU)"
    ```bash
    #!/bin/bash
    #SBATCH --account=def-account    # Specify your account
    #SBATCH --time=00-03:00          # Specify time (DD-HH:MM)
    #SBATCH --mem=32G                # Specify memory for all cores
    #SBATCH --ntasks=8               # Specify number of cores
    #SBATCH --nodes=1                # Do not change
    #SBATCH --cpus-per-task=1        # Do not change
    #SBATCH --gpus-per-node=1        # Specify [gputype:]quantity
    ##SBATCH --gpus-per-node=h100:1  # Temporarily required on mini-graham
    ##SBATCH --partition=debug       # Temporarily required on mini-graham

    module load StdEnv/2023
    #module load ansys/2023R2
    module load ansys/2024R1.03

    mkdir outdir-$SLURM_JOBID
    [[ "$CC_CLUSTER" = cedar ]] && export LD_LIBRARY_PATH=$EBROOTGCC/../lib/gcc

    export ANSGPU_PRINTDEVICES=1
    mapdl -smp -acc nvidia -na $SLURM_GPUS_ON_NODE -b nolist -np $SLURM_NTASKS -dir outdir-$SLURM_JOBID  -i YOURAPDLFILE.inp
    ```
=== "Distributed Memory Parallel (GPU)"
    ```bash
    #!/bin/bash
    #SBATCH --account=def-account    # Specify your account
    #SBATCH --time=00-03:00          # Specify time (DD-HH:MM)
    #SBATCH --mem-per-cpu=4G         # Specify memory per core
    #SBATCH --nodes=1                # Specify number of nodes
    #SBATCH --ntasks-per-node=8      # Specify cores per node
    #SBATCH --cpus-per-task=1        # Do not change
    #SBATCH --gpus-per-node=1        # Specify [gputype:]quantity
    ##SBATCH --gpus-per-node=h100:1  # Temporarily required on mini-graham
    ##SBATCH --partition=debug       # Temporarily required on mini-graham

    module load StdEnv/2023
    #module load ansys/2023R2
    module load ansys/2024R1.03

    mkdir outdir-$SLURM_JOBID
    if [[ "$CC_CLUSTER" = cedar ]]; then
    ln -s $EBROOTGCC/../lib/gcc/libstdc++.so.6.0.29 $PWD/outdir-$SLURM_JOBID/libstdc++.so.6.0.29
    export LD_LIBRARY_PATH=$PWD/outdir-$SLURM_JOBID
    fi

    export ANSGPU_PRINTDEVICES=1
    if [[ "$CC_CLUSTER" = beluga  ]]; then 
    export KMP_AFFINITY=none
    mapdl -dis -acc nvidia -na $SLURM_GPUS_ON_NODE -mpi intelmpi -b nolist -np $SLURM_NTASKS -dir outdir-$SLURM_JOBID -i YOURAPDLFILE.inp
    else
    mapdl -dis -acc nvidia -na $SLURM_GPUS_ON_NODE -mpi openmpi -b nolist -np $SLURM_NTASKS -dir outdir-$SLURM_JOBID -i YOURAPDLFILE.inp
    fi
    ```

Ansys allocates 1024 MB total memory and 1024 MB database memory by default for APDL jobs. These values can be manually specified (or changed) by adding arguments `-m 1024` and/or `-db 1024` to the `mapdl` command line in the above scripts. When using a remote institutional license server with multiple Ansys licenses, it may be necessary to add `-p aa_r` or `-ppf anshpc`, depending on which Ansys module you are using. As always, perform detailed scaling tests before running production jobs to ensure that the optimal number of cores and minimum amount memory is specified in your scripts. The *single node* (SMP Shared Memory Parallel) scripts will typically perform better than the *multinode* (DIS Distributed Memory Parallel) scripts and therefore should be used whenever possible. To help avoid compatibility issues the Ansys module loaded in your script should ideally match the version used to generate the input file:

```text
[gra-login2:~/testcase] cat YOURAPDLFILE.inp | grep version
! ANSYS input file written by Workbench version 2019 R3
```

### Rocky
Besides being able to run simulations in GUI mode (as discussed in the Graphical usage section below) [Ansys Rocky](https://www.ansys.com/products/fluids/ansys-rocky) can also run simulations in non-GUI mode. Both modes support running Rocky with CPUs only or with CPUs and [GPUs](https://www.ansys.com/blog/mastering-multi-gpu-ansys-rocky-software-enhancing-its-performance). Use of the `ansysrocky/2024R2.0` module locally installed only on Nibi and loadable by doing `module load ansysrocky/2024R2.0 StdEnv/2023 ansys/2024R2.04` should be discontinued as it is no longer supported and will be removed. Instead use Rocky included within the `ansys/2025R1` module (and future versions that will be installed) available on all clusters.

#### Slurm scripts
To get a full listing of command line options run `Rocky -h` on the command line after loading any Rocky module. Note that it is currently necessary to set your path to Rocky (as is shown in the scripts below) for the Rocky command to be found. The path will be included in future module version installs and `ansys/2025R1` when updated, at such time this message will be removed. If Rocky is being run with GPUs to solve coupled problems, the number of CPUs you should request from Slurm (on the same node) should be increased to a maximum until the scalability limit of the coupled application is reached. If however Rocky is being run with GPUs to solve standalone uncoupled problems, then only a minimal number of CPUs should be requested that will be sufficient for Rocky to still run optimally. For instance only 2 CPUs or possibly 3 CPUs may be required. When Rocky is run with >= 4 CPUs then *rocky_hpc* licenses will be required which the SHARCNET license does provide. The scripts below have not been tested since the clusters were updated across the Alliance in Fall 2025, therefore some adjustments may be required.

=== "CPU only"
    ```bash
    #!/bin/bash

    #SBATCH --account=account      # Specify your account (def or rrg)
    #SBATCH --time=00-02:00        # Specify time (DD-HH:MM)
    #SBATCH --mem=24G              # Specify total memory for cores
    #SBATCH --cpus-per-task=6      # Specify number of cores to use
    #SBATCH --nodes=1              # Request one node (do not change)

    module load StdEnv/2023 ansys/2025R1       # or newer versions
    export PATH=$EBROOTANSYS/v251/rocky:$PATH

    Rocky --simulate “mysim.rocky” --resume=1 --ncpus=$SLURM_CPUS_PER_TASK --use-gpu=0
    ```
=== "GPU based"
    ```bash
    #!/bin/bash

    #SBATCH --account=account      # Specify your account (def or reg)
    #SBATCH --time=00-01:00        # Specify time (DD-HH:MM)
    #SBATCH --mem=24G              # Specify total memory for cores
    #SBATCH --cpus-per-task=6      # Specify number of cores to use
    #SBATCH --gres=gpu:v100:2      # Specify gpu type : gpu quantity
    #SBATCH --nodes=1              # Request one node (do not change)

    module load StdEnv/2023 ansys/2025R1       # or newer versions
    export PATH=$EBROOTANSYS/v251/rocky:$PATH

    Rocky --simulate “mysim.rocky” --resume=1 --ncpus=$SLURM_CPUS_PER_TASK --use-gpu=1 --gpu-num=$SLURM_GPUS_ON_NODE
    ```

### Electronics
Slurm scripts for using Ansys EDT is provided in a separate wiki page [here](ansysedt.md).

## Graphical use
To run Ansys programs in graphical mode using an OnDemand or JupyterHub desktop click one of the following links:

*   [NIBI](../clusters/nibi.md#access-through-open-ondemand-ood): `https://ondemand.sharcnet.ca`
*   [FIR](fir.md): `https://jupyterhub.fir.alliancecan.ca`
*   [RORQUAL](../clusters/rorqual.md): `https://jupyterhub.rorqual.alliancecan.ca`
*   [NARVAL](../clusters/narval.md): `https://jupyterhub.narval.alliancecan.ca/`
*   [TRILLIUM](https://docs.scinet.utoronto.ca/index.php/Open_OnDemand_Quickstart): `https://ondemand.scinet.utoronto.ca`

A job submission web page should appear in your browser. Configure the resources required for your interactive desktop session and click Launch or Start. If either accelerated graphics or computations will be conducted from within your desktop session then be sure to specify a GPU resource. Once the desktop loads an Ansys module. If you started a Juypter Lab powered desktop then this can be done by clicking the left hand menu, or if you started an OnDemand desktop manually type `module load ansys/version` on the command line. To start one the common Ansys programs such as Fluent, CFX, Workbench and so forth refer to the following section which provides advice for setting environment variables and arguments required by VirtualGL or Mesa-based graphical environments depending on whether a node with a GPU resource was specified or not.

### Fluent
To start Ansys Fluent from the command line of an OnDemand Desktop, open a terminal window and run the commands:

```bash
module load StdEnv/2023 ansys/2025R2.04
fluent
```
When the Fluent Launcher pop-up selector panel appears, click the *Environment Tab* and copy/paste the following environment variable settings, depending on whether you started your OnDemand session with a GPU for graphical acceleration. Do not include the text between the round brackets (as these are comments) and do not put `export` in front of any variable names. If the graphics console window becomes corrupted when starting the GUI, restart Fluent setting `HOOPS_PICTURE=null` to disable creation of the Graphics panel. Although there will be no Graphics tab all menus should continue working so that the job can still be run interactively in the GUI.

**Compute Node (no GPU requested)**

*   `I_MPI_HYDRA_BOOTSTRAP=ssh`      (required on Nibi w/ intelmpi)
*   `HOOPS_PICTURE=opengl2-mesa`     (version 2025R1 or newer)
*   `HOOPS_PICTURE=x11/lin`          (version 2024R2.04 or older)
*   Click the `Start` button

**Compute Node (with GPU requested)**

When starting an OnDemand Desktop on Nibi that requests a GPU you must currently choose a full `h100 (80GB)` GPU so the required VirtualGL environment variables are automatically set up in the Desktop environment required to enable OpenGL graphics calls to be accelerated with OpenGL.
*   `I_MPI_HYDRA_BOOTSTRAP=ssh`      (required on Nibi)
*   `HOOPS_PICTURE=opengl2-mesa`     (version 2025R1 or newer)
*   `HOOPS_PICTURE=opengl`           (version 2024R2.04 or older)
*   Click the `Start` button

!!! warning
    When running Fluent on Nibi cluster the environment variable `I_MPI_HYDRA_BOOTSTRAP=ssh` must be manually set. Otherwise Fluent will crash when started inside OOD Compute Desktop sessions when intelmpi is used. Error output such as the following will be created. Should this occur completely exit Fluent then cleanly shut down Workbench and start over again.
    ```text
    [mpiexec@g4.nibi.sharcnet] Error: Unable to run bstrap_proxy on g4.nibi.sharcnet (pid 2251587, exit code 256)
    [mpiexec@g4.nibi.sharcnet] poll_for_event (../../../../../src/pm/i_hydra/libhydra/demux/hydra_demux_poll.c:157): check exit codes error
    [mpiexec@g4.nibi.sharcnet] HYD_dmx_poll_wait_for_proxy_event (../../../../../src/pm/i_hydra/libhydra/demux/hydra_demux_poll.c:206): poll for  event error
    [mpiexec@g4.nibi.sharcnet] HYD_bstrap_setup (../../../../../src/pm/i_hydra/libhydra/bstrap/src/intel/i_hydra_bstrap.c:1063): error waiting for event
    [mpiexec@g4.nibi.sharcnet] Error setting up the bootstrap proxies
    ```

### CFX
When starting CFX from an OnDemand Desktop the following arguments may be specified on the terminal window command line depending on whether a GPU was requested when the Desktop was started.

*   `module load StdEnv/2023 ansys/2025R1` (or older)
*   `cfx5 -graphics mesa` (no GPU requested)
*   `cfx5 -graphics ogl` (with GPU requested)

### Mapdl
The following steps for starting the Mechanical APDL GUI from the command line of a terminal window should work regardless if you have started your OnDemand Desktop on a Compute node with or without a GPU.

*   `module load StdEnv/2023 ansys/2022R2` (or newer versions)
*   `mapdl -g`, or,
*   `launcher` then click `RUN` button

### Workbench
This section shows how to start Workbench (and optionally Fluent) on either an OnDemand Desktop or Jupyter Lab Desktop.

#### OnDemand Desktop

**Compute Node (no GPU requested) or Basic Desktop**

If accelerated graphics is not required for your desktop session then specify GPU Node to select a Compute Node without a GPU for your OOD session. Doing this will use Mesa software emulation for OpenGL calls instead of running on a more expensive and difficult to reserve GPU node:
*   `module load StdEnv/2023 ansys/2025R2.04`
*   `runwb2`

To start Fluent from within Workbench click *Fluid Flow (Fluent) or (Fluent with Fluent Meshing)* in the left hand *Analysis Menu*, then click *Setup* in the centre canvas *Fluid Flow (Fluent)* pop-up. Once the *Fluent Launcher* selector panel pop-up appears, click the *Environment Tab* and copy/paste the following environment variable settings:
*   `I_MPI_HYDRA_BOOTSTRAP=ssh`      (required on Nibi cluster only)
*   `HOOPS_PICTURE=opengl2-mesa`     (optional for 2025R1 or newer)
*   Click the `Start` button

**Compute Node (with GPU requested)**

If accelerated graphics is required on Nibi cluster then choose **t4 (15GB)** from the GPU selector pulldown list for your OnDemand desktop session. Doing this will ensure the environment variables used by VirtualGL to enable accelerated OpenGL graphics calls are automatically set up inside your Desktop environment for the current session. Once your desktop appears, open a terminal window and start Workbench as follows:
*   `module load StdEnv/2023 ansys/2025R2.04`
*   `runwb2`

To start Fluent from within Workbench click *Fluid Flow (Fluent) or (Fluent with Fluent Meshing)* in the left hand *Analysis Menu*, then click *Setup* in the centre canvas *Fluid Flow (Fluent)* pop-up. Once the *Fluent Launcher* selector panel pop-up appears, click the *Environment Tab* and copy/paste the following environment variable settings.
*   `I_MPI_HYDRA_BOOTSTRAP=ssh`      (required on Nibi cluster only)
*   `HOOPS_PICTURE=opengl2-mesa`     (optional for 2025R1 or newer)
*   Click the `Start` button

!!! warning
    When using Nibi cluster `I_MPI_HYDRA_BOOTSTRAP=ssh` must be manually set when the default intelmpi is used, otherwise Fluent will crash on startup producing error output such as the following. To recover from this close Fluent, shut down Workbench and try again.
    ```text
    [mpiexec@g4.nibi.sharcnet] Error: Unable to run bstrap_proxy on g4.nibi.sharcnet (pid 2251587, exit code 256)
    [mpiexec@g4.nibi.sharcnet] poll_for_event (../../../../../src/pm/i_hydra/libhydra/demux/hydra_demux_poll.c:157): check exit codes error
    [mpiexec@g4.nibi.sharcnet] HYD_dmx_poll_wait_for_proxy_event (../../../../../src/pm/i_hydra/libhydra/demux/hydra_demux_poll.c:206): poll for  event error
    [mpiexec@g4.nibi.sharcnet] HYD_bstrap_setup (../../../../../src/pm/i_hydra/libhydra/bstrap/src/intel/i_hydra_bstrap.c:1063): error waiting for event
    [mpiexec@g4.nibi.sharcnet] Error setting up the bootstrap proxies
    ```

#### Jupyterhub Desktop

**Compute Node (no GPU requested)**

*   Click to load `ansys/2025R1` (or newer version) in the Desktop left hand side menu
*   Click the "Workbench (VNC)" icon located in the Jupyter Lab desktop centre window.
    *   If the graphics of any application (such as Fluent) started within Workbench appear unusable due to corrupted graphics then try carrying out the following steps. They will create a custom `runwb2` desktop icon so that Workbench can be started in Mesa mode. If one of the applications that you will be starting in Workbench is Fluent then when the Fluent launcher starts you may also try setting `HOOPS_PICTURE=opengl2-mesa` variable in the Fluent Launcher window.
    *   To proceed, exit Workbench and then open a terminal window. Copy paste the following command into the Remote Clipboard located in the top right corner of your Jupyter desktop. Now the commands can be pasted into terminal i.e.)
    *   `cd ~/Desktop; cp -p $(realpath workbench.desktop) workbench-mesa.desktop`
    *   Open the newly created file in a text editor such as `nano` by doing the following:
    *   `nano ~/Desktop/workbench-mesa.desktop`. Change all instances of `runwb2` to `runwb2 -oglmesa` and then exit the editor saving the changes. Now REFRESH the Jupyter desktop by pressing the key combination *control-R*. The new icon should now appear in the desktop along with the original Workbench icon. Double click it to start Workbench.
    *   The new icon will persist for future sessions until manually deleted with the command `rm -f ~/Desktop/workbench-mesa.desktop`.

**Compute Node (with GPU requested)**

*   Click to load `ansys/2025R1` (or newer version) in the Desktop left hand side menu
*   Click the Workbench (VNC) icon located in the Jupyter Lab desktop centre window

### Ensight
*   `module load StdEnv/2023 ansys/2022R2; A=222; B=5.12.6`
*   `export LD_LIBRARY_PATH=$EBROOTANSYS/v$A/CEI/apex$A/machines/linux_2.6_64/qt-$B/lib`
*   `ensight -X`

### Rocky
*   `module load StdEnv/2023 ansys/2025R1` (or newer versions)
*   `export PATH=$EBROOTANSYS/v251/rocky:$PATH` (path to be included in future module versions)
*   `Rocky` The Ansys module handles reading your `~/.licenses/ansys.lic`
*   `RockySolver` Run Rocky solver directly from command line (add -h for help, untested)
*   `RockyScheduler` Start Rocky scheduler GUI to submit/run jobs on present node (untested)
*   The SHARCNET license includes Rocky and is therefore free for all researchers to use
*   Rocky supports GPU-accelerated computing however this capability not been tested or documented yet

### Electronics
Information describing how to run Ansys EDT in graphical mode may be found [here](ansysedt.md).

## Site-specific usage

### SHARCNET license
The SHARCNET Ansys license is free for academic use by **any** Alliance researcher on **any** Alliance system. The installed software does not have any solver or geometry limits. The SHARCNET license may be used for ***Publishable Academic Research*** but not for any private/commercial purposes as this is strictly prohibited by the license terms. The SHARCNET Ansys license is based on the Multiphysics Campus Solution and includes products such as: HF, EM, Electronics HPC, Mechanical, CFD, ROCKY and LS-DYNA as described [here](https://www.ansys.com/academic/educator-tools/academic-product-portfolio). Lumerical software is included in recent Ansys module versions however it is NOT covered by the SHARCNET license. SpaceClaim software is not installed with any Ansys module since there is no Linux version available however it is technically covered by the SHARCNET license.

!!! tip "Scalability Note"
    <span style="font-size: 20px;">&#x2696;&#xFE0F;</span> Scaling tests should be run before launching long jobs to determine the optimal scalable job size so that the limited licenses and hardware are used as efficiently as possible and total job run and startup times are minimized. Parallel jobs that do not achieve at least 50% CPU utilization will probably be flagged by the system, resulting in a follow-up by an Alliance team member.

The SHARCNET Ansys license is made available on a first come first serve basis. It currently permits each researcher to run a maximum of 16 simultaneous jobs using a total of up to 512 hpc cores across all clusters, therefore any of the following maximum job size combinations can be run simultaneously: 1x512, 2x256, 4x128, 8x64, 16x32 or more commonly one of these full node combinations: 1x384, 2x192 or 1x192 cores. Note however the SHARCNET license is oversubscribed so there is potential for jobs to fail on startup if all (or nearly all) of the 1986 `anshpc` licenses in the SHARCNET license pool are in use. Should this occur you will need to manually resubmit your job to the queue. If over time there is an increasing number of license shortage instances then the total `anshpc` core limit per researcher may be decreased from 512 to 384. If you need more than 512 hpc cores for your research then consider using the local ANSYS License server at your institution if one is available OR open a ticket to request help purchasing additional licenses for the SHARCNET license in which case your maximum job size `anshpc` limit would be increased respectively.

#### License file
As of February 2026 the old `license3.sharcnet.ca` license server has been permanently shut down. To use the SHARCNET Ansys license on any Alliance cluster, simply configure your `ansys.lic` file as follows instead:

```bash
[username@cluster:~] cat ~/.licenses/ansys.lic
setenv("ANSYSLMD_LICENSE_FILE", "1055@license1.computecanada.ca")
```

#### License query
To show the number of Ansys licenses in use by your username and the total in use by all users, run:

```bash
ssh nibi.alliancecan.ca
module load ansys
$EBROOTANSYS/v$(echo ${EBVERSIONANSYS:2:2}${EBVERSIONANSYS:5:1})/licensingclient/linx64/lmutil \
lmstat -c $ANSYSLMD_LICENSE_FILE -a | grep "Users of\|$USER" | grep -v " Total of 0 licenses in use"
```

#### Example
Consider the case where a user submits an 8-core Fluent job and a 32-core Fluent job. Once both jobs start running, the user runs the `lmutil` query command and the output shown below is generated. Here it can be seen that a total of (8-4) + (32-4) = 32 `anshpc` licenses are used by the two jobs. As a result the total number of `anshpc` licenses increases from 1568 to 1600 so that only (1986-1600) = 386 `anshpc` licenses remain available for additional jobs submitted by all users. Therefore if a 400 core parallel job attempts to start at this moment, it will fail to start since (400-4) = 396 `anshpc` licenses would be required. The user has two options, wait for a sufficient number of `anshpc` licenses to come available OR reduce the job size to 390 cores or less and resubmit immediately. This example focuses on the `anshpc` feature since it is most generously overcommitted to allow any user to submit the largest job possible, but it also shows that the actual number of `anshpc` licenses available per user may sometimes be far less than the 512 per user limit would suggest.

!!! note "License Query Example Output"
    ```text
    [l2(nibi):~] sq
                JOBID     USER        ACCOUNT           NAME  ST  TIME_LEFT NODES CPUS MIN_MEM NODELIST (REASON) 
            10161023  roberpj   cc-debug_cpu script-flu-int   R    2:57:19     4    8     N/A      4G c[630-633] (None) 
            10161033  roberpj   cc-debug_cpu script-flu-int   R    2:58:25    16   32     N/A      4G c[627-628,630-633,637,642,645,655,657,662,665,667,669,682] (None) 
    [l2(nibi):~]
    [l2(nibi):~] module load ansys
    [l2(nibi):~]
    [l2(nibi):~] $EBROOTANSYS/v$(echo ${EBVERSIONANSYS:2:2}${EBVERSIONANSYS:5:1})/licensingclient/linx64/lmutil  \
                lmstat -c $ANSYSLMD_LICENSE_FILE -a | grep "Users of\|$USER" | grep -v " Total of 0 licenses in use"
    Users of anshpc:  (Total of 1986 licenses issued;  Total of 1600 licenses in use)
        roberpj c630 c630.nibi.sharcnet 1238925 (v2025.0506) (license1.computecanada.ca/1055 2579), start Wed 3/11 16:46, 4 licenses, PID: 1239140 
        roberpj c627 c627.nibi.sharcnet 509821 (v2025.0506) (license1.computecanada.ca/1055 5716), start Wed 3/11 16:48, 28 licenses, PID: 510058 
    Users of cfd_base:  (Total of 275 licenses issued;  Total of 19 licenses in use)
        roberpj c630 c630.nibi.sharcnet 1238925 (v2025.0506) (license1.computecanada.ca/1055 10327), start Wed 3/11 16:46, PID: 1239140 
        roberpj c627 c627.nibi.sharcnet 509821 (v2025.0506) (license1.computecanada.ca/1055 7171), start Wed 3/11 16:47, PID: 510058 
    Users of cfd_preppost:  (Total of 275 licenses issued;  Total of 1 license in use)
    Users of cfd_preppost_pro:  (Total of 275 licenses issued;  Total of 1 license in use)
    Users of cfd_solve_level1:  (Total of 275 licenses issued;  Total of 18 licenses in use)
        roberpj c630 c630.nibi.sharcnet 1238925 (v2025.0506) (license1.computecanada.ca/1055 7994), start Wed 3/11 16:46, PID: 1239140 
        roberpj c627 c627.nibi.sharcnet 509821 (v2025.0506) (license1.computecanada.ca/1055 6200), start Wed 3/11 16:47, PID: 510058 
    Users of cfd_solve_level2:  (Total of 275 licenses issued;  Total of 18 licenses in use)
        roberpj c630 c630.nibi.sharcnet 1238925 (v2025.0506) (license1.computecanada.ca/1055 10520), start Wed 3/11 16:46, PID: 1239140 
        roberpj c627 c627.nibi.sharcnet 509821 (v2025.0506) (license1.computecanada.ca/1055 375), start Wed 3/11 16:47, PID: 510058 
    Users of elec_solve_hfss:  (Total of 275 licenses issued;  Total of 1 license in use)
    Users of elec_solve_level1:  (Total of 275 licenses issued;  Total of 1 license in use)
    Users of elec_solve_level2:  (Total of 275 licenses issued;  Total of 1 license in use)
    ```

!!! note "Killing Rogue Processes"
    <span style="font-size: 20px;">&#x1f575;</span> A rare situation can occur where the output from the License query command reveals there are some Ansys licenses unexpectedly still in use by your username on some desktop or compute node. For instance if an Ansys GUI program run on a remote desktop node was not shut down cleanly, leaving some Ansys processes still running. Or an Ansys program crashes on a cluster compute node inside an `salloc` session that was being run interactively from the command line, once again leaving some rogue Ansys processes still running. To kill all potentially responsible Ansys rogue processes either close the desktop, `scancel` the `salloc` session, or simply open a terminal window on the affected node and issue the command `pkill -9 -e -u $USER -f "ansys"`. Any Ansys licenses that were being held open should immediately be returned to the SHARCNET license server and become available for use again by yourself or other researchers.

## Additive Manufacturing
To get started configure your `~/.licenses/ansys.lic` file to point to a license server that has a valid Ansys Mechanical License. This must be done on all systems where you plan to run the software.

### Enable Additive
This section describes how to make the Ansys Additive Manufacturing ACT extension available for use in your project. The steps must be performed on each cluster for each Ansys module version where the extension will be used. Any extensions needed by your project will also need to be installed on the cluster as described below. If you get warnings about missing un-needed extensions (such as ANSYSMotion) then uninstall them from your project.

#### Download Extension
*   Download AdditiveWizard.wbex from https://catalog.ansys.com/
*   Upload AdditiveWizard.wbex to the cluster where it will be used

#### Start Workbench
*   Follow the Workbench section in [Graphical use above](#graphical-use).
*   *File -> Open* your project file (ending in `.wbpj`) into Workbench GUI

#### Open Extension Manager
*   Click *ACT Start Page* and the *ACT Home page* tab will open
*   Click *Manage Extensions* and the *Extension Manager* will open

#### Install Extension
*   Click the box with the large `+` sign under the search bar
*   Navigate to select and install your AdditiveWizard.wbex file

#### Load Extension
*   Click to highlight the *AdditiveWizard* box (loads the AdditiveWizard extension for current session only)
*   Click lower right corner arrow in the *AdditiveWizard* box and select *Load extension* (loads the extension for current AND future sessions)

#### Unload Extension
*   Click to un-highlight the *AdditiveWizard* box (unloads extension for the current session only)
*   Click lower right corner arrow in the *AdditiveWizard* box and select *Do not load as default* (extension will not load for future sessions)

### Run Additive

#### OnDemand
A user can run a single Ansys Additive Manufacturing job in a graphical OnDemand session by doing:

*   Start Workbench as described above in **Enable Additive**.
*   Click *File -> Open* and select *test.wbpj* then click *Open*
*   Click *View -> reset workspace* if you get a grey screen
*   Start Mechanical, Clear Generated Data, tick Distributed, specify Cores
*   Click *File -> Save Project -> Solve*

Check utilization:
*   Open another terminal and run:
    ```bash
    top -u $USER
    ```
    **OR**
    ```bash
    ps u -u $USER | grep ansys
    ```
*   Kill rogue processes from previous runs:
    ```bash
    pkill -9 -e -u $USER -f "ansys|mwrpcss|mwfwrapper|ENGINE"
    ```

!!! warning
    Please note that rogue Ansys related processes can persistently continue tie up valuable licenses inside a running OnDemand login node sessions if an Ansys GUI session (Fluent, Workbench, Mechanical, etc) is not cleanly terminated by the user or is terminated unexpectedly by a network outage or hung filesystem. If the latter is to blame the processes may not be killable until normal disk access is restored.

#### Cluster
Project preparation:

Before submitting a newly uploaded Additive project to a cluster queue (with `sbatch scriptname`) certain preparations must be done. To begin, open your simulation with Workbench GUI (as described in the `Enable Additive` section above) in the same directory that your job will be submitted from and then save it again. Be sure to use the same Ansys module version that will be used for the job. Next create a Slurm script (as explained in the [Cluster Batch Job Submission - WORKBENCH](#workbench) section above). To perform parametric studies, change `Update()` to `UpdateAllDesignPoints()` in the Slurm script. Determine the optimal number of cores and memory by submitting several short test jobs. To avoid needing to manually clear the solution **and** recreate all the design points in Workbench between each test run, either 1) change `Save(Overwrite=True)` to `Save(Overwrite=False)` or 2) save a copy of the original `YOURPROJECT.wbpj` file and corresponding `YOURPROJECT_files` directory. Optionally create and then manually run a replay file on the cluster in the respective test case directory between each run, noting that a single replay file can be used in different directories by opening it in a text editor and changing the internal `FilePath` setting.

```bash
module load ansys/2019R3
rm -f test_files/.lock
runwb2 -R myreplay.wbjn
```

Resource utilization:

Once your additive job has been running for a few minutes, a snapshot of its resource utilization on the compute node(s) can be obtained with the following `srun` command. Sample output corresponding to an eight core submission script is shown next. It can be seen that two nodes were selected by the scheduler:

```text
[gra-login1:~] srun --overlap --jobid=myjobid top -bn1 -u $USER | grep R | grep -v top
  PID USER   PR  NI    VIRT    RES    SHR S  %CPU %MEM    TIME+  COMMAND
22843 demo   20   0 2272124 256048  72796 R  88.0  0.2  1:06.24  ansys.e
22849 demo   20   0 2272118 256024  72822 R  99.0  0.2  1:06.37  ansys.e
22838 demo   20   0 2272362 255086  76644 R  96.0  0.2  1:06.37  ansys.e
  PID USER   PR  NI    VIRT    RES    SHR S  %CPU %MEM    TIME+  COMMAND
 4310 demo   20   0 2740212 271096 101892 R 101.0  0.2  1:06.26  ansys.e
 4311 demo   20   0 2740416 284552  98084 R  98.0  0.2  1:06.55  ansys.e
 4304 demo   20   0 2729516 268824 100388 R 100.0  0.2  1:06.12  ansys.e
 4305 demo   20   0 2729436 263204 100932 R 100.0  0.2  1:06.88  ansys.e
 4306 demo   20   0 2734720 431532  95180 R 100.0  0.3  1:06.57  ansys.e
```

Scaling tests:

After a job completes, its "Job Wall-clock time" can be obtained from `seff myjobid`. Using this value, scaling tests can be performed by submitting short test jobs with an increasing number of cores. If the Wall-clock time decreases by ~50% when the number of cores is doubled, additional cores may be considered.

## Help resources
The official full documentation for recent versions Ansys 202[4|5]R[1|2] is available [here](https://ansyshelp.ansys.com/public/account/secured?returnurl=/Views/Secured/main_page.html?lang=en). Documentation for older versions such as Ansys 2023R[1|2] however requires [login](https://ansyshelp.ansys.com/login). Developer documentation can be found in the Ansys Developer [Portal](https://developer.ansys.com). Additional learning resources include the Ansys HowTo [videos](https://www.youtube.com/@AnsysHowTo/videos), the Ansys Educator [Hub](https://innovationspace.ansys.com/educator-hub/) and the Ansys Webinar [series](https://www.ansys.com/events/ansys-academic-webinar-series).

**XoverSSH Legacy Note**: Some programs can be run remotely on a cluster compute node by forwarding X over SSH to your local desktop. Unlike VNC, this approach is untested and unsupported since it relies on a properly set up X display server for your particular operating system OR the selection, installation and configuration of a suitable X client emulator package such as MobaXterm. Most users will find interactive response times unacceptably slow for basic menu tasks let alone performing more complex tasks such as those involving graphics rendering. Startup times for GUI programs can also be very slow depending on your Internet connection. For example, in one test it took 40 minutes to fully start the GUI up over SSH while starting it with `vncviewer` required only 34 seconds. Despite the potential slowness, using this method to connect may still be of interest if your only goal is to open a simulation and perform some basic menu operations or run some calculations and response delays can be tolerated. The basic steps are given here as a starting point: 1) `ssh -Y username@alliancecan.ca` 2) `salloc --x11 --time=1:00:00 --mem=16G --cpus-per-task=4 [--gpus-per-node=1] --account=def-mygroup`; 3) once connected onto a compute node try running `xclock`. If the clock appears on your desktop, proceed to load the desired Ansys module and try running the program.