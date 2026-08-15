---
title: "Cluster batch job submission with Ansys"
slug: "cluster_batch_job_submission_with_ansys"
lang: "base"

source_wiki_title: "Cluster batch job submission with Ansys"
source_hash: "8722eabb66a1f380493f6c72e940adf1"
last_synced: "2026-08-15T23:22:43.108655+00:00"
last_processed: "2026-08-15T23:38:24.892440+00:00"

tags:
  []

keywords:
  - "nodes"
  - "#SBATCH --mem=0"
  - "UDF"
  - "MEMPAR"
  - "#SBATCH"
  - "time resource request"
  - "ANSYS Fluent requeue"
  - "#SBATCH --ntasks-per-node=64"
  - "Slurm scheduler"
  - "#SBATCH --ntasks-per-node=192"
  - "awk '{print $9}'"
  - "slurm_hl2hl.py"
  - "legacy .cas/.dat file format"
  - "Slurm scripts"
  - "module load ansys/2023R2"
  - "Multinode (by core + restart)"
  - "SolveHandlers.xml"
  - "module load ansys"
  - "Discrete Phase Model (DPM)"
  - "#SBATCH directives"
  - "#SBATCH --cpus-per-task=1"
  - "Fluent GUI"
  - "DPM injection file format"
  - "SLURM_NTASKS"
  - "-acc nvidia"
  - "ANSYS-FLUENT"
  - "fluent"
  - "SLURM_NNODES"
  - "SLURM --array requeue"
  - "ntasks-per-node"
  - "timesteps"
  - "journal files"
  - ".cas.h5/.dat.h5 file format"
  - "Discrete Phase Model"
  - "restart files"
  - "-mpi=intel"
  - "mapdl"
  - "ANSYS Fluent restart"
  - "#SBATCH --time=00-03:00"
  - "GPU-based script"
  - "DMP"
  - "ANSYS Fluent"
  - "walltime"
  - "user-defined function (UDF)"
  - "OpenMPI"
  - "/file/cff-files"
  - "Workbench GUI"
  - "journal file (sample.jou)"
  - "Injections dialog box"
  - "--resume"
  - "Interaction with Continuous Phase"
  - "parallel jobs"
  - "SLURM_GPUS_ON_NODE"
  - "SLURM_JOBID"
  - "#SBATCH --account=def-group"
  - "Shared memory Parallel (CPU)"
  - "ln -s $SCRATCH/.ansys"
  - "Ansys MPI implementations"
  - "tail -n1"
  - "machinefile-$SLURM_JOB_ID"
  - "gpus-per-node"
  - "source file name"
  - "Save(Overwrite=True)"
  - "transient simulation"
  - "Rocky --headless --simulate"
  - "Fluent job submission script"
  - "SLURM"
  - "RESUME option"
  - "scancel $SLURM_ARRAY_JOB_ID"
  - "account"
  - "trilliumMYJOURNALFILE"
  - "Slurm time window"
  - "module load"
  - "cfx5solve options"
  - "LD_LIBRARY_PATH"
  - "Ansys memory allocation"
  - "MYVERSION=3d"
  - "H100 GPU"
  - "Fluent User's Guide"
  - "SLURM_CPUS_PER_TASK"
  - "#SBATCH --nodes=1"
  - "parallelized UDF"
  - "Distributed memory parallel (CPU)"
  - "ansys"
  - "double precision"
  - "#SBATCH --nodes=2"
  - "intelmpi/openmpi"
  - "by node script"
  - "Fluent journal file"
  - "#SBATCH --time limit"
  - "journal file"
  - "time limit"
  - "Nrestart"
  - "libudf.so shared library"
  - "cpus-per-task"
  - ".ansys directory"
  - "Slurm scripts for using AnsysEDT"
  - "script-rocky-gpu.sh"
  - "dual-time-iterate"
  - "exit status"
  - "steady file format"
  - "mem-per-cpu"
  - "license requeue"
  - "#SBATCH --mem=24G"
  - "Set Injection Properties"
  - "grep .dat"
  - "auto-save data-frequency"
  - "--use-gpu"
  - "cfx5solve"
  - "fluent -g $MYVERSION"
  - "solution restart journal"
  - "module load ansys/2025R2.04"
  - "SMP"
  - "SLURM job array"
  - "User-Defined Functions (UDF)"
  - "UserConfigured=\"1\""
  - "multinode execution"
  - "symbolic link .fluentconf"
  - "-cnf"
  - "Slurm script"
  - "--gpus=h100_1g.10gb:1"
  - "KMP_AFFINITY"
  - "project cache directory"
  - "steady simulation"

questions:
  - "What are the necessary steps to prepare, transfer, and run a Fluent case on the cluster using a Slurm submission script?"
  - "How can license shortages be managed through job requeueing in Fluent Slurm scripts, and what precautions should be taken?"
  - "When is it preferable to use a “by node” script versus a “by core” script for Fluent, and how do these choices affect performance and job stability?"
  - "Which SLURM account is specified in the script?"
  - "What is the maximum runtime limit set for the job?"
  - "How many tasks per node are requested and what memory allocation is specified?"
  - "What SLURM directives must be set to define the account, time limit, and resource allocation (nodes, tasks, memory) for running ANSYS Fluent?"
  - "How does the script choose the appropriate MPI library and communication mode (pshmem, peth, pib) based on the detected cluster (narval, nibi) and ANSYS version?"
  - "Which user‑defined variables (e.g., MYJOURNALFILE, MYVERSION) need to be specified, and how are they incorporated into the Fluent command line?"
  - "What SLURM options must be set to specify the total number of cores versus the number of nodes in the two provided Fluent job scripts?"
  - "How does the script determine whether to run Fluent in single‑node mode or multi‑node mode, and what command‑line arguments change accordingly?"
  - "Which ANSYS Fluent versions and corresponding module loads are required for the Narval (by core) and Trillium (by node) configurations?"
  - "What is the correct format for specifying the time limit in the `#SBATCH` directives?"
  - "How does the script allocate compute resources such as nodes, cores per node, and memory?"
  - "Which software modules are required to be loaded, and what version constraints are indicated?"
  - "What is the role of the `MYJOURNALFILE` variable in this script?"
  - "Which simulation formats can be specified with the `MYVERSION` variable?"
  - "What condition does the script verify about the `$HOME/.ansys` directory, and what happens if it is not met?"
  - "What actions does the script perform if the symbolic links for ~/.ansys, ~/.fluentconf, or ~/.flrecent are missing or incorrect?"
  - "How does the script decide which Fluent command options to use for single‑node versus multi‑node (or multinode) jobs?"
  - "What is the purpose of the “license requeue” section, and how is the number of allowed requeue attempts specified in the example SLURM script?"
  - "What does the `#SBATCH --array=1-5%1` directive do in the script, and how does the script manage job failures and automatic resubmission?"
  - "How must the original `sample.jou` file be edited to create a proper restart journal (`sample-restart.jou`) for long Fluent simulations?"
  - "What guidelines are provided for selecting the number of timesteps per restart and the total time request to keep the job within the cluster’s maximum runtime limit?"
  - "What condition triggers the script to run Fluent with the `-pshmem` option instead of other MPI settings?"
  - "How does the script decide between using `-peth` and `-pib` MPI options based on the value of `CC_CLUSTER`?"
  - "What action does the script take if Fluent exits with a status code of 0?"
  - "What is the formula for the total simulation time when 2 is chosen, and how does it depend on the timestep size (Dt) and the number of restarts (Nrestart)?"
  - "How many timesteps and output files will be generated based on the chosen number of restarts?"
  - "How should the Slurm time request be set to ensure all timesteps finish within the allowed maximum of #SBATCH --time=07-00:00?"
  - "What is the role of the SLURM array in this script and how does it handle solution restarts?"
  - "How does the script detect the target cluster (e.g., narval or nibi) and adjust MPI or communication settings accordingly?"
  - "Which user‑defined variables must be set before execution, and what specific files or options do they correspond to?"
  - "What SLURM directives and module loads are required to configure and launch an ANSYS Fluent simulation on the Narval or Nibi clusters?"
  - "How does the script manage job restarts, including the selection of journal, case, and data files for the initial and subsequent array tasks?"
  - "What is the difference between using the legacy .cas/.dat format and the newer .cas.h5/.dat.h5 format in Fluent journal files, and how can the format be switched?"
  - "What does the script use to locate the most recent `.dat` file and extract the ninth column from it?"
  - "How does the script handle successful job completion versus a simulation failure, including any SLURM commands it runs?"
  - "What is the overall purpose of the `script-flu-bycore+restart.sh` file as indicated by its commands and conditional logic?"
  - "What does the /file/cff-files setting control in Fluent journal files?"
  - "Which file formats are used by default for journal files in module versions 2019R3 or older versus 2020R1 or newer?"
  - "Where can users find additional information and a complete list of commands for Fluent?"
  - "How can you set up a Fluent journal file to automatically save data files at specified iteration intervals in a steady simulation?"
  - "What are the necessary steps to transfer, place, and configure an interpreted UDF (e.g., sampleudf.c) for use in a Fluent job on a Linux cluster?"
  - "Which commands in a transient Fluent journal file define the physical time step size, dual‑time iteration parameters, and the automatic saving of case and data files?"
  - "What line should be added to the journal file and where should it be placed to load a UDF before the case/data files are read?"
  - "Why must the cas file be opened in the Fluent GUI, have its managed definitions removed, and then be resaved before running the simulation?"
  - "What additional step is required to use an interpreted UDF in parallel jobs, according to the text?"
  - "Why must a user‑defined function (UDF) be compiled on an Alliance cluster before it can be transferred to other clusters, and what problems arise if the libudf directory is simply copied from a different system?"
  - "What steps are necessary to parallelize a compiled UDF for Fluent parallel jobs, and what are the potential consequences if the UDF is not properly parallelized?"
  - "How are DPM‑based UDFs configured in Fluent, including the definition of injection point properties through the GUI or an injection file, and what key options must be set for successful operation?"
  - "What is the correct syntax and required fields for a steady‑state DPM injection file (e.g., `zinjection01.inj`) in ANSYS Fluent?"
  - "How do you enable double‑precision calculations and support for large meshes when invoking `cfx5solve` from the command line?"
  - "What are the main configuration differences between the provided single‑node and multinode Slurm scripts for running an ANSYS CFX simulation?"
  - "What steps should you follow in the GUI to confirm that the injection is working and its particles and properties are listed in the console?"
  - "How does selecting “Interaction with Continuous Phase” in the Discrete Phase Model dialog affect the updating of DPM source terms during each flow iteration?"
  - "In what way can the injection configuration and DPM interaction settings be automated by adding commands to a journal file after solution initialization?"
  - "What is the purpose of the `#SBATCH --nodes=2` directive in this script?"
  - "Why is `#SBATCH --mem=0` used, and what effect does it have on memory allocation?"
  - "What does the `module load StdEnv/2020` command do, and why is it marked as deprecated?"
  - "What are the necessary initialization steps for an ANSYS Workbench project before submitting it with a Slurm script?"
  - "How does the provided Slurm script determine whether to use SMP (shared memory) or DMP (distributed memory) parallel execution?"
  - "Which module versions and MPI start methods should be used for running cfx5solve on the “narval” or “fir” clusters compared to other clusters?"
  - "What condition does the script evaluate to decide between setting `MEMPAR=0` for SMP (shared memory parallel) and `MEMPAR=1` for DMP (distributed memory parallel)?"
  - "How is the variable `MWFILE` constructed to locate the `SolveHandlers.xml` file that will be edited?"
  - "Which XML tags are targeted by the two `sed` commands, and what values are inserted into the `<AnsysSolution>` and `<Processors>` elements respectively?"
  - "What does changing `UserConfigured=\"0\"` to `UserConfigured=\"1\"` in the `SolveHandlers.xml` file accomplish in the Slurm scripts?"
  - "How does modifying `Save(Overwrite=True)` to `Save(Overwrite=False)` influence the evaluation of simulation scaling across multiple job submissions?"
  - "Which Slurm directives and module loads are necessary to execute an APDL job in shared‑memory (SMP) versus distributed‑memory (DMP) mode on the StdEnv/2023 (or newer) environment?"
  - "What is the purpose of the conditional `export LD_LIBRARY_PATH` statement when `CC_CLUSTER` is set to “cedar”?"
  - "How does the MAPDL command utilize the SLURM variables (e.g., `SLURM_NTASKS`, `SLURM_JOBID`) to configure a distributed memory parallel run?"
  - "Which SBATCH directives are included in `script-dmp-2023-cpu.sh`, and what resources or limits do they specify?"
  - "What are the main differences in SLURM directives and MAPDL command options between the CPU‑only script and the shared‑memory GPU script?"
  - "How does the script handle library dependencies for the cedar and beluga clusters, and why is a symbolic link to libstdc++.so.6.0.29 created?"
  - "Which environment variables and module loads are required to enable GPU acceleration in the distributed‑memory GPU script, and how are they set based on the cluster type?"
  - "How can the default memory and database memory allocations for APDL jobs be modified using MAPDL command‑line arguments?"
  - "What criteria should be used to choose between the CPU‑only and GPU‑based Slurm scripts for Rocky simulations, considering performance scaling and resource limits?"
  - "Which license server flags and Ansys module version settings are recommended to avoid compatibility issues when running Rocky simulations on the cluster?"
  - "What is the role of the environment variables `ANSGPU_PRINTDEVICES=1` and `KMP_AFFINITY=none` in this script?"
  - "How does the script choose between `intelmpi` and `openmpi` for the MAPDL execution based on the cluster name?"
  - "Which command‑line arguments are used to allocate GPUs, set the number of tasks, and define the output directory for the MAPDL run?"
  - "What does the `--resume` option control in the Rocky simulation commands, and how does its value affect the execution?"
  - "How does the script determine whether to run the simulation with CPU resources only or with GPU resources, and what changes in the command line accordingly?"
  - "Which SLURM directives are specified in the script (e.g., account, time, CPUs per task), and what role does each play in scheduling the job?"
  - "What resources (memory, CPUs, GPUs, and nodes) are requested in the Slurm script?"
  - "How does the script determine whether to start a new simulation or resume a previous one, and what commands are executed in each case?"
  - "Which module is loaded before running Rocky, and why does the script remove the lock file and previous simulation results?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: false
  qa_generated: false
---

The Ansys software suite comes with multiple implementations of MPI to support parallel computation. Unfortunately, none of them support our [Slurm scheduler](running_jobs.md). For this reason, we need special instructions on how to start a parallel job for each Ansys package. In the sections below, we give examples of submission scripts for some of the packages. While Slurm scripts should work on all clusters, Trillium users may need to make some additional [changes covered here](https://docs.scinet.utoronto.ca/index.php).

## Fluent
Typically, you would use the following procedure to run Fluent on one of our clusters:

1.  Prepare your Fluent job using Fluent from the Ansys Workbench on your desktop machine, up to the point where you would run the calculation.
2.  Export the case file with *File > Export > Case…* or find the folder where Fluent saves your project's files. The case file will often have a name like `FFF-1.cas.gz`.
3.  If you already have data from a previous calculation, which you want to continue, export a data file as well (*File > Export > Data…*) or find it in the same project folder (`FFF-1.dat.gz`).
4.  [Transfer](../getting-started/transferring_data.md) the case file (and if needed the data file) to a directory on the [/project](../storage-and-data/project_layout.md) or [/scratch](../storage-and-data/storage_and_file_management.md#storage-types) filesystem on the cluster. When exporting, you can save the file(s) under a more instructive name than `FFF-1.*`, or rename them when they are uploaded.
5.  Now you need to create a journal file. Its purpose is to load the case file (and optionally the data file), run the solver, and finally write the results. See examples below and remember to adjust the filenames and desired number of iterations.
6.  If jobs frequently fail to start due to license shortages and manual resubmission of failed jobs is not convenient, consider modifying your script to requeue your job (up to 4 times) as shown under the *by node + requeue* tab further below.
    !!! warning
        Be aware that doing this will also requeue simulations that fail due to other related issues (such as divergence), resulting in wasted compute time. Therefore, it is strongly recommended to monitor and inspect each Slurm output file to confirm that each requeue attempt is license-related. When it is determined that a job is requeued due to a simulation issue, immediately kill the job progression manually with `scancel jobid` and correct the problem.
7.  After [running the job](running_jobs.md), you can download the data file and import it back into Fluent with *File > Import > Data…*.

### Slurm scripts

#### General purpose

Most Fluent jobs should use the following *by node* script to minimize solution latency and maximize performance over as few nodes as possible. Very large jobs might wait less in the queue if they use a *by core* script; however, the startup time of a job using many nodes can be significantly longer, thus offsetting some of the benefits. In addition, be aware that running large jobs over an unspecified number of very many nodes will make them far more vulnerable to crashing if any of the compute nodes fail during the simulation. The scripts will ensure Fluent uses shared memory for communication when run on a single node, and distributed memory (utilizing MPI and the appropriate HPC interconnect) when run over multiple nodes. The two Narval tabs may be useful to provide a more robust alternative if Fluent crashes during the initial automatic mesh partitioning phase when using the standard Intel-based scripts with the parallel solver. The other option would be to manually perform the mesh partitioning in the Fluent GUI, then try to run the job again on the cluster with the Intel scripts. Doing so will allow you to inspect the partition statistics and specify the partitioning method to obtain an optimal result. The number of mesh partitions should be an integral multiple of the number of cores; for optimal efficiency, ensure at least 10000 cells per core.

=== "Multinode (by node)"

    ```bash title="script-flu-bynode-intel.sh"
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

    ```bash title="script-flu-bycore-intel.sh"
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

    ```bash title="script-flu-bynode-openmpi.sh"
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

    ```bash title="script-flu-bycore-openmpi.sh"
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

    ```bash title="script-flu-bynode-intel-tri.sh"
    #!/bin/bash

    #SBATCH --account=def-group      # Specify account name
    #SBATCH --time=00-03:00          # Specify time limit dd-hh:mm
    #SBATCH --nodes=1                # Specify number of compute nodes (1 or more)
    #SBATCH --ntasks-per-node=16     # Specify number cores per node (max 192 on trillium)
    ##SBATCH --mem=0                 # Do not uncomment (be default trillium uses all memory per node)
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

#### License requeue

The scripts in this section should only be used with Fluent jobs that are known to complete normally without generating any errors in the output, but typically require multiple requeue attempts to check out licenses. They are not recommended for Fluent jobs that may 1) run for a long time before crashing 2) run to completion but contain unresolved journal file warnings, since in both cases the simulations will be repeated from the beginning until the maximum number of requeue attempts specified by the `array` value is reached. For these types of jobs, the general purpose scripts above should be used instead.

=== "Multinode (by node + requeue)"

    ```bash title="script-flu-bynode+requeue.sh"
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

    ```bash title="script-flu-bycore+requeue.sh"
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

#### Solution restart

The following scripts are provided to automate restarting very large jobs that require more than the typical seven-day maximum runtime window available on most clusters. Jobs are restarted from the most recently saved timestep files. A fundamental requirement is that the first timestep can be completed within the requested job array time limit (specified at the top of your Slurm script) when starting a simulation from an initialized solution field. It is assumed that a standard fixed timestep size is being used. To begin, a working set of `sample.cas`, `sample.dat` and `sample.jou` files must be present. Next, edit your `sample.jou` file to contain `/solve/dual-time-iterate 1` and `/file/auto-save/data-frequency 1`. Then, create a restart journal file with `cp sample.jou sample-restart.jou` and edit the `sample-restart.jou` file to contain `/file/read-cas-data sample-restart` instead of `/file/read-cas-data sample`. Also comment out the initialization line with a semicolon, for example `; /solve/initialize/initialize-flow`. If your second and subsequent timesteps are known to run twice as fast as the initial timestep, edit the `sample-restart.jou` file to add `/solve/dual-time-iterate 2`. By adding this specification, the solution will only be restarted after two timesteps have been completed following the initial timestep. An output file for each timestep will still be saved in the output subdirectory. The value 2 is arbitrary but should be chosen so that the time for 2 steps fits within the job array time limit. Doing so minimizes the number of solution restarts which are computationally expensive. If the first timestep performed by `sample.jou` starts from a converged (previous) solution, choose 1 instead of 2, since likely all timesteps will require a similar amount of walltime to complete. Assuming 2 is chosen, the total time of simulation to be completed will be `1*Dt+2*Nrestart*Dt` where `Nrestart` is the number of solution restarts specified in the script. The total number of timesteps (and hence the number of output files generated) will therefore be `1+2*Nrestart`. The value for the time resource request should be chosen so that the initial timestep and subsequent timesteps will complete comfortably within the Slurm time window specifiable up to a maximum of `#SBATCH --time=07-00:00` days.

=== "Multinode (by node + restart)"

    ```bash title="script-flu-bynode+restart.sh"
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

    ```bash title="script-flu-bycore+restart.sh"
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

### Journal files

Fluent journal files can include basically any command from Fluent's Text User Interface (TUI); commands can be used to change simulation parameters like temperature, pressure, and flow speed. You can then run a series of simulations under different conditions with a single case file, by only changing the parameters in the journal file. Refer to the [Fluent User's Guide](https://ansyshelp.ansys.com/public/account/secured?returnurl=/Views/Secured/corp/v242/en/flu_ug/flu_ug.html) for more information, and a list of all commands that can be used. The following journal files are set up with `/file/cff-files no` to use the legacy `.cas/.dat` file format (the default in module versions 2019R3 or older). Set this to `/file/cff-files yes` instead to use the more efficient `.cas.h5/.dat.h5` file format (the default in module versions 2020R1 or newer).

=== "Journal file (steady, case)"

    ```text title="sample1.jou"
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

    ```text title="sample2.jou"
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

    ```text title="sample3.jou"
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

### UDFs

The first step is to transfer your user-defined function or UDF (namely the `sampleudf.c` source file and any additional dependency files) to the cluster. When uploading from a Windows machine, be sure the text mode setting of your transfer client is used, otherwise Fluent won't be able to read the file properly on the Linux cluster. The UDF should be placed in the directory where your journal, cas, and dat files reside. Next, add one of the following commands into your journal file before the commands that read in your simulation cas/dat files. Regardless of whether you use the interpreted or compiled UDF approach, before uploading your cas file onto the cluster, please check that neither the *Interpreted UDFs* dialog box or the *UDF Library Manager* dialog box are configured to use any UDF; this will ensure that only the journal file commands are in control when jobs are submitted.

#### Interpreted

To tell Fluent to interpret your UDF at runtime, add the following command line into your journal file before the cas/dat files are read or initialized. The filename `sampleudf.c` should be replaced with the name of your source file. The command remains the same whether the simulation is being run in serial or parallel. To ensure the UDF can be found in the same directory as the journal file, open your cas file in the Fluent GUI, remove any managed definitions, and resave it. Doing this ensures only the following command/method is in control when Fluent runs. To use an interpreted UDF with parallel jobs, it will need to be parallelized as described in the section below.

```
define/user-defined/interpreted-functions "sampleudf.c" "cpp" 10000 no
```

#### Compiled

To use this approach, your UDF must be compiled on an Alliance cluster at least once. Doing so will create a `libudf` subdirectory structure containing the required `libudf.so` shared library. The `libudf` directory cannot simply be copied from a remote system (such as your laptop) to the cluster since the library dependencies of the shared library will not be satisfied, resulting in Fluent crashing on startup. That said, once you have compiled your UDF on an Alliance cluster, you can transfer the newly created `libudf` to any other Alliance cluster, providing your account loads the same StdEnv environment module version. Once copied, the UDF can be used by uncommenting the second (load) libudf line below in your journal file when submitting jobs to the cluster. Both (compile and load) libudf lines should not be left uncommented in your journal file when submitting jobs on the cluster, otherwise your UDF will automatically be (re)compiled for each and every job. Not only is this highly inefficient, but it will also lead to racetime-like build conflicts if multiple jobs are run from the same directory. Besides configuring your journal file to build your UDF, the Fluent GUI may also be used. To do this, navigate to the *Compiled UDFs* dialog box, add the UDF source file and click on *Build*. When using a compiled UDF with parallel jobs, your source file should be parallelized as discussed in the section below.

```
define/user-defined/compiled-functions compile libudf yes sampleudf.c "" ""
```

and/or

```
define/user-defined/compiled-functions load libudf
```

#### Parallel

Before a UDF can be used with a Fluent parallel job (single node SMP and multinode MPI), it will need to be parallelized. By doing this we control how/which processes (host and/or compute) run specific parts of the UDF code when Fluent is run in parallel on the cluster. The instrumenting procedure involves adding compiler directives, predicates, and reduction macros into your working serial UDF. Failure to do so will result in Fluent running slow at best, or immediately crashing at worst. The end result will be a single UDF that runs efficiently when Fluent is used in both serial and parallel mode. The topic is described in detail in [Parallel Considerations](https://ansyshelp.ansys.com/public/account/secured?returnurl=//////Views/Secured/corp/v242/en/flu_udf/flu_udf_ChapParallelUDFUsage.html?q=parallel%20considerations).

#### DPM
UDFs can be used to customize Discrete Phase Models (DPM) as described in
*   [2024R2 Fluent Users Guide](https://ansyshelp.ansys.com/public/account/secured?returnurl=/Views/Secured/corp/v242/en/flu_ug/flu_ug.html): *Part III: Solution Mode | Chapter 24: Modeling Discrete Phase | 24.2 Steps for Using the Discrete Phase Models| 24.2.6 User-Defined Functions*, and
*   [2024R2 Fluent Customization Manual](https://ansyshelp.ansys.com/public/account/secured?returnurl=//////Views/Secured/corp/v242/en/flu_udf/flu_udf.html): *Part I: Creating and Using User Defined Functions | Chapter 2: DEFINE Macros | 2.5 Discrete Phase Model (DPM) DEFINE Macros*.

Before a DMP-based UDF can be worked into a simulation, the injection of a set of particles must be defined by specifying *Point Properties* with variables such as source position, initial trajectory, mass flow rate, time duration, temperature, and so forth, depending on the injection type. This can be done in the GUI by clicking on *Physics panel --> Discrete Phase* to open the *Discrete Phase Model* box and then clicking on the *Injections* button. Doing so will open an *Injections* dialog box where one or more injections can be created by clicking on the *Create* button. The *Set Injection Properties* dialog which appears will contain an *Injection Type* pulldown where available types are single, group, surface, and flat-fan-atomizer. If you select any of these, you can then select the *Point Properties* tab to input the corresponding value fields. Another way to specify the *Point Properties* would be to read an injection text file. To do this, select *File* from the *Injection Type* pulldown, specify the *Injection Name* to be created, and click on the *File* button (located beside the *OK* button at the bottom of the dialog). Here, either an *Injection Sample File* (with a `.dpm` extension) or a manually created injection text file can be selected. To select the file in the Select File dialog box that change the File of type pull down to All Files (*), then highlight the file which could have any arbitrary name but commonly has an `.inj` extension, click the OK button. Assuming there are no problems with the file, no console error or warning message will appear. As you will be returned to the *Injections* dialog box, you should see the same injection name that you specified in the *Set Injection Properties* dialog and be able to list its particles and properties in the console. Next, open the *Discrete Phase Model* dialog box and select *Interaction with Continuous Phase* which will enable updating DPM source terms every flow iteration. This setting can be saved in your cas file or added via the journal file as shown. Once the injection is confirmed working in the GUI, the steps can be automated by adding commands to the journal file after the solution initialization, for example
```
 /define/models/dpm/interaction/coupled-calculations yes
 /define/models/dpm/injections/delete-injection injection-0:1
 /define/models/dpm/injections/create injection-0:1 no yes file no zinjection01.inj no no no no
 /define/models/dpm/injections/list-particles injection-0:1
 /define/models/dpm/injections/list-injection-properties injection-0:1
```
where a basic manually created injection steady file format might look like
```bash
$ cat  zinjection01.inj
(z=4 12)
( x          y        z    u         v    w    diameter  t         mass-flow  mass  frequency  time name )
(( 2.90e-02  5.00e-03 0.0 -1.00e-03  0.0  0.0  1.00e-04  2.93e+02  1.00e-06   0.0   0.0        0.0 ) injection-0:1 )
```
Note that injection files for DPM simulations are generally set up for either steady or unsteady particle tracking where the format of the former is described in [2024R2 Fluent Customization Manual](https://ansyshelp.ansys.com/public/account/secured?returnurl=//////Views/Secured/corp/v242/en/flu_udf/flu_udf.html) *Part III: Solution Mode | Chapter 24: Modeling Discrete Phase | 24.3. Setting Initial Conditions for the Discrete Phase | 24.3.13 Point Properties for File Injections | 24.3.13.1 Steady File Format*.

## CFX

### Slurm scripts

A summary of command-line options can be printed by running `cfx5solve -help` where the same module version loaded in your Slurm script should be first manually loaded. By default `cfx5solve` will run in single precision (`-single`). To run in double precision add the `-double` option, noting that doing so will also double memory requirements. By default `cfx5solve` can support meshes with up to 80 million elements (structured) or 200 million elements (unstructured). For larger meshes with up to 2 billion elements, add the `-large` option. Various combinations of these options can be specified for the Partitioner, Interpolator or Solver. Consult the [ANSYS CFX-Solver Manager User's Guide](https://ansyshelp.ansys.com/public/Views/Secured/corp/v251/en/pdf/Ansys_CFX-Solver_Manager_Users_Guide.pdf) for further details.

=== "Single node"

    ```bash title="script-cfx-local.sh"
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

    ```bash title="script-cfx-multiple.sh"
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

## Workbench

Before submitting a Workbench job to the queue with a Slurm script, you must initialize it once in the following steps.
1.  On the cluster where you will submit Workbench jobs, start an [OnDemand desktop](../interactive/open_ondemand.md#logging-into-the-open-ondemand-portal).
2.  Once the desktop appears, open a terminal window and `cd` into the directory containing your `YOURPROJECT.wbpj` file.
3.  Remove the old project cache directory by running `rm -rf _ProjectScratch` as this can be very large from previous runs.
4.  Open a terminal window and load the module version that you will be using in your Slurm script for example `module load ansys/2025R2.04`.
5.  Open the Workbench GUI with your project file. This can be done by issuing `runwb2 -f YOURPROJECT.wbpj` directly from the command line. If and when a popup appears asking *Do you want to recover the project before opening ? (Any changes made since the last save will be lost.)* answer **No**.
6.  In the context menu popup that should appear in the centre *Project Schematic* window, right-click on *Model* and select *Reset*. When Ansys Workbench pops up a warning that *This operation will delete the operations local and generated data* click on **Ok** to accept and proceed.
7.  In the top menu bar pulldown, select *File -> Save* then *File -> Exit* to shut down Workbench.
8.  In the Ansys Workbench popup, when asked *The current project has been modified. Do you want to save it?*, click on the **No** button.
9.  Quit Workbench and submit your job using one of the Slurm scripts shown below.

Since a compute node with up to 96 cores, 768GB memory and 8 hours runtime can now be reserved for an OnDemand desktop session, consider running your Workbench simulations directly from within the Workbench native GUI when possible. This is a more intuitive option compared to submitting the job to the queue with a Slurm script.

### Slurm scripts

A project file can be submitted to the queue by customizing one of the following scripts and then running the `sbatch script-wbpj-202X.sh` command.

=== "Single node (StdEnv/2023)"

    ```bash title="script-wbpj-2023.sh"
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

    ```bash title="script-wbpj-2020.sh"
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

To avoid writing the solution when a running job successfully completes, change `Save(Overwrite=True)` to `Save(Overwrite=False)` in the last line of the above Slurm script. Doing this makes it easier to determine how well the simulation scales when `#SBATCH --ntasks` is increased, since the initialized solution will not be overwritten by each test job.

## Mechanical

The input file can be generated from within your interactive Workbench Mechanical session by clicking on *Solution -> Tools -> Write Input Files* then specifying *File name:* `YOURAPDLFILE.inp` and *Save as type:* APDL Input Files (*.inp). APDL jobs can then be submitted to the queue with the `sbatch script-name.sh` command.

### Slurm scripts

In the following scripts, lines beginning with `##SBATCH` are commented.

=== "Shared memory Parallel (CPU)"

    ```bash title="script-smp-2023-cpu.sh"
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

=== "Distributed memory parallel (CPU)"

    ```bash title="script-dmp-2023-cpu.sh"
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

=== "Shared memory parallel (GPU)"

    ```bash title="script-smp-2023-gpu.sh"
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

=== "Distributed memory parallel (GPU)"

    ```bash title="script-dmp-2023-gpu.sh"
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

Ansys allocates 1024 MB total memory and 1024 MB database memory by default for APDL jobs. These values can be manually specified (or changed) by adding arguments `-m 1024` and/or `-db 1024` to the `mapdl` command line in the above scripts. When using a remote institutional license server with multiple Ansys licenses, it may be necessary to add `-p aa_r` or `-ppf anshpc`, depending on which Ansys module you are using. As always, perform detailed scaling tests before running production jobs to ensure that the optimal number of cores and minimum amount memory is specified in your scripts. The single node (SMP shared memory parallel) scripts will typically perform better than the multinode (DIS distributed memory parallel) scripts and therefore should be used whenever possible. To help avoid compatibility issues, the Ansys module loaded in your script should ideally match the version used to generate the input file.

```
[gra-login2:~/testcase] cat YOURAPDLFILE.inp | grep version
 ! ANSYS input file written by Workbench version 2019 R3
```

## Rocky

This section provides sample Slurm scripts to solve standalone non-coupled Rocky simulations in a cluster queue. Both scripts are configured with `RESUME=0` so simulations are solved from the beginning by default. To restart a partially completed simulation, set `RESUME=1` and resubmit the script to the queue. To get a full listing of command line options, run `Rocky -h` on the command line after loading the Ansys module. Since a lock file is generated every time a simulation is started, only one job should be submitted at a time from the same directory. Regarding which script to use, while all simulations should be tested independently, for a basic test case the GPU only script was found to outperform the CPU only script by a factor of 3.5x. Further increases in resources beyond 6cpus (for the CPU only script) or 2cpu + 1g (1/7 of a H100 GPU for the GPU based script) provided no further speedup based on scaling testing for either script. Given these results, it appears likely that the GPU-based script will provide significantly faster solution times compared to just using CPUs for other standalone Rocky simulations. As summarized under [Ratios in bundles](allocations_and_compute_scheduling.md#ratios-in-bundles), all clusters but Narval have H100 GPUs. Therefore, when using the GPU script on Narval, the `--gpus` Slurm option should be changed to request an a100 GPU instead. Note that as of May 2026, only Rocky with the `ansys/2025R2|2.04` modules have been tested but not the `ansys/2025R1|1.02` modules yet.

### Slurm scripts

=== "CPU only"

    ```bash title="script-rocky-cpu.sh"
    #!/bin/bash

    #SBATCH --account=account      # Specify account (def or rrg)
    #SBATCH --time=00-02:00        # Specify time (DD-HH:MM)
    #SBATCH --mem=24G              # Specify total memory for cores
    #SBATCH --cpus-per-task=6      # Specify number of cores to use
    #SBATCH --nodes=1              # Request one node (do not change)

    module load StdEnv/2023 ansys/2025R2.04   # Specify 2025R1 or newer versions

    INPUTFILE="mySim.rocky"                   # Specify input filename
    rm -f $INPUTFILE.lock                     # Removes old lock files

    RESUME=0                                  # Specify 0 or 1
    if [ $RESUME -eq 0 ]; then
      rm -rf $INPUTFILE.files/simulation      # Removes previous results
      Rocky --headless --simulate --resume=0 --ncpus=$SLURM_CPUS_PER_TASK --use-gpu=0 $INPUTFILE
    else
      Rocky --headless --simulate --resume=1 --ncpus=$SLURM_CPUS_PER_TASK --use-gpu=0 $INPUTFILE
    fi
    ```

=== "GPU-based"

    ```bash title="script-rocky-gpu.sh"
    #!/bin/bash

    #SBATCH --account=account      # Specify account (def or rrg)
    #SBATCH --time=00-01:00        # Specify time (DD-HH:MM)
    #SBATCH --mem=24G              # Specify total memory for cores
    #SBATCH --cpus-per-task=2      # Specify number of cores to use
    #SBATCH --gpus=h100_1g.10gb:1  # Specify a100_1g.5gb:1 on narval
    #SBATCH --nodes=1              # Request one node (do not change)

    module load StdEnv/2023 ansys/2025R2.04   # Specify 2025R1 or newer versions

    INPUTFILE="mySim.rocky"                   # Specify input filename
    rm -f $INPUTFILE.lock                     # Removes old lock files

    RESUME=0                                  # Specify 0 or 1
    if [ $RESUME -eq 0 ]; then
      rm -rf $INPUTFILE.files/simulation      # Removes previous results
      Rocky --headless --simulate --resume=0 --ncpus=$SLURM_CPUS_PER_TASK --use-gpu=1 $INPUTFILE
    else
      Rocky --headless --simulate --resume=1 --ncpus=$SLURM_CPUS_PER_TASK --use-gpu=1 $INPUTFILE
    fi
    ```

## Electronics

Slurm scripts for using AnsysEDT are provided in [this specific page](../software/ansysedt.md).