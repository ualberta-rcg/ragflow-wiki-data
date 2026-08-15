---
title: "Cluster batch job submission with Ansys/en"
slug: "cluster_batch_job_submission_with_ansys"
lang: "en"

source_wiki_title: "Cluster batch job submission with Ansys/en"
source_hash: "0172382da5775b9809fed2715cbd183f"
last_synced: "2026-08-15T23:22:43.108655+00:00"
last_processed: "2026-08-15T23:39:34.365750+00:00"

tags:
  []

keywords:
  - "minimum memory"
  - "Slurm scripts"
  - "compiled UDF"
  - "CPU only script"
  - "UDF"
  - "requeue attempts"
  - "parallelized UDF"
  - "job array restart"
  - "SLURM"
  - "dual-time-iterate"
  - "Discrete Phase Model"
  - "SBATCH time limit"
  - "Slurm script options"
  - "Distributed memory parallel"
  - "ln -s $SCRATCH/.fluentconf ~/.fluentconf"
  - "distributed memory parallel"
  - "SolveHandlers.xml"
  - "Shared memory parallel"
  - "module versions 2020R1"
  - "#SBATCH --time"
  - "GPU"
  - "module load ansys"
  - "DPM injection file format"
  - "SLURM job array"
  - "Fluent job script"
  - ".writable .ansys directory does not exist"
  - "journal file automation"
  - "interpreted UDF"
  - "Slurm scheduler"
  - "#SBATCH --nodes"
  - "total time of simulation"
  - "optimal number of cores"
  - "DPM source terms"
  - "#SBATCH --mem=0"
  - "ANSYS Fluent"
  - "#SBATCH --nodes=2"
  - "#SBATCH --mem"
  - "--nodes=2"
  - "SBATCH"
  - "intelmpi"
  - "runwb2"
  - "cfx5solve -help"
  - "license"
  - "Rocky simulations"
  - "Nrestart"
  - "Discrete Phase Model (DPM)"
  - "steady file format"
  - "Set Injection Properties"
  - "--mem-per-cpu=4G"
  - "journal files"
  - "GPU-based script"
  - ".fluentconf directory link missing"
  - "slurm array job"
  - "parallel jobs"
  - "double precision (-double)"
  - "SLURM_NTASKS"
  - "#SBATCH --account"
  - "#SBATCH --ntasks-per-node=192"
  - "export OPENMPI_ROOT=$EBROOTOPENMPI"
  - "Save(Overwrite=True)"
  - "Multinode (by core + requeue)"
  - "ls -lh cavity*"
  - "ln -s $SCRATCH/.ansys ~/.ansys"
  - "SLURM job script"
  - "transient simulation"
  - "script-flu-bycore+restart.sh"
  - "KMP_AFFINITY"
  - ".flrecent"
  - "Fluent journal file"
  - "Remove ~/.ansys"
  - "Slurm time window"
  - "cfx5solve"
  - "MYJOURNALFILE=sample.jou"
  - "libudf shared library"
  - "Ansys MAPDL"
  - "#SBATCH --ntasks-per-node"
  - "restart journal file"
  - "sbatch"
  - "multinode execution"
  - "resubmitting job"
  - "Ansys module version compatibility"
  - "requeue job"
  - "output files"
  - "restart"
  - "machinefile"
  - "DMP"
  - "Interaction with Continuous Phase"
  - "SLURM_ARRAY_TASK_ID"
  - "steady simulation"
  - ".cas.h5/.dat.h5 file format"
  - "SBATCH directives"
  - "journal file"
  - "fluent"
  - "Ansys MPI implementations"
  - "ANSYS"
  - "job restart"
  - "license or simulation issue"
  - "cas/dat files"
  - "module load StdEnv/2023"
  - "machinefile generation"
  - "User-Defined Functions (UDF)"
  - "openmpi"
  - "single node SMP scripts"
  - "MYVERSION=3d"
  - "Fluent GUI"
  - "Slurm script"
  - "module load ansys/2023R2"
  - "legacy .cas/.dat file format"
  - "timesteps"
  - "Simulation failed"
  - "LD_LIBRARY_PATH"
  - "auto-save data frequency"
  - "multinode DIS scripts"
  - "RESUME"
  - "user-defined function (UDF)"
  - "ANSYS Workbench"
  - "--ntasks=8"
  - "SLURM_ARRAY_TASK_COUNT"
  - "Fluent User's Guide"
  - "#SBATCH --cpus-per-task=1"

questions:
  - "How should Fluent case and data files be prepared and transferred to the cluster before submitting a Slurm job?"
  - "What are the differences between the “by node” and “by core” Slurm scripts, and when should each be used for Fluent simulations?"
  - "How can license shortages be managed with the requeue option in Fluent Slurm submissions, and what precautions are recommended?"
  - "What does the `#SBATCH --time=00-03:00` directive specify, and how is the time format interpreted by SLURM?"
  - "How does the `#SBATCH --mem=0` option affect memory allocation for the job on a compute node?"
  - "Which software modules are loaded by this script, and why are they required for the job?"
  - "What user‑defined variables (e.g., MYJOURNALFILE, MYVERSION, SLURM directives) need to be set before executing the script, and what do they control?"
  - "How does the script choose the appropriate MPI library and communication mode (e.g., ‑pshmem, ‑peth, ‑pib) based on the detected cluster (narval, nibi) and ANSYS version?"
  - "What are the key differences between the “Multinode (by core)” and “Multinode (by node, Narval)” script versions in terms of SLURM resource specifications and Fluent launch commands?"
  - "What is the role of the `slurm_hl2hl.py` command and the loop that creates `/tmp/machinefile-$SLURM_JOB_ID` in the Fluent job scripts?"
  - "How does the script decide whether to run Fluent with shared memory (`-pshmem`) or with the PNI (`-pib`) option based on the number of allocated nodes?"
  - "Which environment preparations (module loads, symbolic links, variable settings) are required before submitting the job on the Trillium system?"
  - "What is the purpose of the SBATCH directives (e.g., --nodes, --ntasks-per-node, --cpus-per-task) in this script?"
  - "Why are the module load commands for StdEnv/2023 and ansys/2023R2 explicitly marked as “Do not change”?"
  - "How are the variables MYJOURNALFILE and MYVERSION intended to be used, and what does the final command with slurm_hl2hl.py accomplish?"
  - "What action does the script recommend when the writable .ansys directory does not exist?"
  - "How should a user fix the error regarding a missing symbolic link to a writable .fluentconf directory?"
  - "Why does the script instruct the user to remove any existing ~/.ansys or ~/.fluentconf before creating the new symlink?"
  - "What is the purpose of checking and creating a symbolic link to ~/.flrecent before running the Fluent job?"
  - "How does the script decide between single‑node and multi‑node Fluent execution, and which MPI options are used for each scenario?"
  - "In the license‑requeue section, how are multiple job attempts controlled, and what determines whether a job is resubmitted or terminated?"
  - "What condition causes the script to resubmit the job attempt?"
  - "How does the script decide that all job attempts have failed and exit?"
  - "Which SLURM directives are included in the provided script snippet?"
  - "How does the Slurm script allocate resources and launch ANSYS Fluent differently depending on the cluster (narval, nibi, etc.)?"
  - "What are the required modifications to the original sample.jou file to create a proper restart journal for long‑running Fluent simulations?"
  - "How should the time limit and dual‑time‑iterate settings be chosen to ensure each timestep (or group of timesteps) fits within the Slurm job‑array time window?"
  - "How is the total simulation time computed when option 2 is chosen, and which parameters (Dt, Nrestart) influence it?"
  - "What determines the total number of timesteps—and thus the number of output files—produced by the run?"
  - "How should the requested wall‑time be selected to fit comfortably within the Slurm limit, and what is the maximum time that can be specified with `#SBATCH --time`?"
  - "What is the purpose of the SLURM array in this script and how does it handle solution restarts between array tasks?"
  - "Which user‑defined variables (e.g., MYVERSION, MYJOUFILE, MYJOUFILERES) need to be set, and what do they represent?"
  - "How does the script detect the target cluster (narval vs nibi) and adjust the Fluent launch options accordingly?"
  - "How does the script decide whether to launch a fresh Fluent simulation or a restart based on the value of `SLURM_ARRAY_TASK_ID`?"
  - "What is the difference between using the legacy `.cas/.dat` file format and the newer `.cas.h5/.dat.h5` format in Fluent journal files, and how can you switch between them in the script?"
  - "Which modules and environment variables are required for running ANSYS Fluent on the Narval and Nibi clusters, and what specific roles do they play in the job submission process?"
  - "What actions does the script take when a job finishes successfully versus when it fails?"
  - "What is the role of the `scancel $SLURM_ARRAY_JOB_ID` command within the script?"
  - "Which SLURM directives are defined in the `script-flu-bycore+restart.sh` file and what do they specify?"
  - "What does the `/file/cff-files` command control, and how does changing its setting affect the journal file format?"
  - "Which file extensions correspond to the legacy format versus the newer, more efficient format mentioned in the guide?"
  - "In which Fluent module versions are the defaults for `/file/cff-files` set to `no` (legacy) and `yes` (newer format)?"
  - "How do you set up a Fluent journal file to run a steady simulation and specify the output case and data files?"
  - "What are the required steps to transfer a UDF to the Linux cluster and configure it for interpreted execution in a Fluent journal?"
  - "In a transient Fluent simulation journal, how are automatic data‑saving frequency, time‑step size, and iteration limits defined?"
  - "What steps must be taken to replace the placeholder filename “sampleudf.c” with the actual source file name when preparing the UDF?"
  - "How can you ensure that the UDF file is correctly located and recognized by Fluent when running a simulation, especially regarding managed definitions and the cas file?"
  - "Why does an interpreted UDF require additional parallelization for parallel jobs, and where can the necessary instructions be found?"
  - "What steps are required to compile a user‑defined function (UDF) on an ANSYS Fluent Alliance cluster and correctly load it in subsequent jobs?"
  - "How must a serial UDF be modified to run efficiently in parallel (SMP or MPI) Fluent jobs, and what are the consequences of not parallelizing it?"
  - "What procedures are described for creating and loading DPM injections using UDFs, including specifying point properties and using injection text files?"
  - "What steps must be taken to confirm that an injection is correctly defined and its particles and properties are listed in the Fluent console?"
  - "How do you enable and save the “Interaction with Continuous Phase” option in the Discrete Phase Model dialog for updating DPM source terms each flow iteration?"
  - "How can the injection setup be automated by adding commands to a journal file after solution initialization?"
  - "How should a steady injection file for DPM simulations be formatted, and which fields are required for each particle entry?"
  - "What command‑line options does **cfx5solve** offer for precision, mesh size, and large‑scale partitioning, and how are these options incorporated into a Slurm job script?"
  - "How do the provided Slurm scripts differ between single‑node and multi‑node execution, and what module loads and environment variables must be set for each case?"
  - "What initialization steps must be performed on the OnDemand desktop before submitting an Ansys Workbench job to the Slurm queue?"
  - "How does the provided Slurm script decide between SMP (shared memory) and DMP (distributed memory) execution and modify the SolveHandlers.xml file accordingly?"
  - "What differences in the cfx5solve command options are required when running on the “narval” or “fir” clusters compared to other clusters?"
  - "What compute resources (nodes, tasks per node, memory, CPUs per task) are being requested for the job?"
  - "Which software modules and versions are being loaded in this script?"
  - "Why are some directives marked as “do not change” or “deprecated,” and what implications does that have for modifying the script?"
  - "What modifications are the `sed` commands applying to the `SolveHandlers.xml` file and why are they needed for DMP execution?"
  - "How does the script locate the appropriate Ansys version directory to construct the `MWFILE` path?"
  - "Which environment variables are exported for parallel runs, and what roles do `KMP_AFFINITY` and `I_MPI_HYDRA_BOOTSTRAP` play?"
  - "How can you modify the Slurm script to prevent overwriting the solution after a successful job run?"
  - "What are the key differences in resource specifications and directives between the shared‑memory (CPU) and distributed‑memory (CPU) Slurm scripts shown?"
  - "How do you generate an APDL input file from within a Workbench Mechanical session for submission with sbatch?"
  - "How do the scripts configure environment variables and library paths differently for the cedar and beluga clusters?"
  - "What are the main differences between the shared‑memory (SMP) GPU script and the distributed‑memory (DIS) GPU script in terms of SLURM options and MAPDL command flags?"
  - "Which command‑line arguments can be used to adjust MAPDL memory allocation and licensing, and why is it advised to run scaling tests and prefer SMP scripts when possible?"
  - "What does the `#SBATCH --time=00-03:00` directive specify in this SLURM script?"
  - "How are computational resources such as memory, nodes, and tasks allocated in the script?"
  - "Which Ansys software versions are loaded, and why is the `outdir-$SLURM_JOBID` directory created?"
  - "Why is it important to specify the optimal number of cores and the minimum amount of memory in your production job scripts?"
  - "When should single‑node (SMP shared memory) scripts be preferred over multinode (DIS distributed memory) scripts, and what performance advantage do they offer?"
  - "How can you avoid compatibility issues by matching the Ansys module version loaded in your script to the version used to generate the input file?"
  - "How should the RESUME variable be configured to restart a partially completed Rocky simulation?"
  - "Which Slurm script (CPU‑only or GPU‑based) is recommended for faster solution times, and what are the optimal CPU/GPU resource limits for each?"
  - "What change must be made to the --gpus option in the GPU‑based script when running on the Narval cluster?"

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
2.  Export the case file with *File > Export > Case…* or find the folder where Fluent saves your project's files. The case file will often have a name like FFF-1.cas.gz.
3.  If you already have data from a previous calculation, which you want to continue, export a data file as well (*File > Export > Data…*) or find it in the same project folder (FFF-1.dat.gz).
4.  [Transfer](../getting-started/transferring_data.md) the case file (and if needed the data file) to a directory on the [/project](../storage-and-data/project_layout.md) or [/scratch](../storage-and-data/storage_and_file_management.md#storage-types) filesystem on the cluster. When exporting, you can save the file(s) under a more instructive name than FFF-1.*, or rename them when they are uploaded.
5.  Now you need to create a journal file. Its purpose is to load the case file (and optionally the data file), run the solver, and finally write the results. See examples below and remember to adjust the filenames and desired number of iterations.
6.  If jobs frequently fail to start due to license shortages and manual resubmission of failed jobs is not convenient, consider modifying your script to requeue your job (up to 4 times) as shown under the *by node + requeue* tab further below.

    !!! warning "License Requeue Precautions"
        Be aware that using the requeue option will also requeue simulations that fail due to other related issues (such as divergence), resulting in wasted compute time. Therefore, it is strongly recommended to monitor and inspect each Slurm output file to confirm that each requeue attempt is license-related. When it is determined that a job is requeued due to a simulation issue, immediately kill the job progression manually with `scancel jobid` and correct the problem.

7.  After [running the job](running_jobs.md), you can download the data file and import it back into Fluent with *File > Import > Data…*.

### Slurm scripts

#### General purpose

Most Fluent jobs should use the following *by node* script to minimize solution latency and maximize performance over as few nodes as possible. Very large jobs might wait less in the queue if they use a *by core* script; however, the startup time of a job using many nodes can be significantly longer, thus offsetting some of the benefits. In addition, be aware that running large jobs over an unspecified number of very many nodes will make them far more vulnerable to crashing if any of the compute nodes fail during the simulation. The scripts will ensure Fluent uses shared memory for communication when run on a single node, and distributed memory (utilizing MPI and the appropriate HPC interconnect) when run over multiple nodes. The two Narval tabs may be useful to provide a more robust alternative if Fluent crashes during the initial automatic mesh partitioning phase when using the standard Intel-based scripts with the parallel solver. The other option would be to manually perform the mesh partitioning in the Fluent GUI, then try to run the job again on the cluster with the Intel scripts. Doing so will allow you to inspect the partition statistics and specify the partitioning method to obtain an optimal result.

!!! note "Optimal Mesh Partitioning"
    The number of mesh partitions should be an integral multiple of the number of cores; for optimal efficiency, ensure at least 10000 cells per core.

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

The following scripts are provided to automate restarting very large jobs that require more than the typical seven-day maximum runtime window available on most clusters. Jobs are restarted from the most recently saved timestep files. A fundamental requirement is that the first timestep can be completed within the requested job array time limit (specified at the top of your Slurm script) when starting a simulation from an initialized solution field. It is assumed that a standard fixed timestep size is being used. To begin, a working set of `sample.cas`, `sample.dat` and `sample.jou` files must be present. Next, edit your `sample.jou` file to contain `/solve/dual-time-iterate 1` and `/file/auto-save/data-frequency 1`. Then, create a restart journal file with `cp sample.jou sample-restart.jou` and edit the `sample-restart.jou` file to contain `/file/read-cas-data sample-restart` instead of `/file/read-cas-data sample`. Also comment out the initialization line with a semicolon, for example `;/solve/initialize/initialize-flow`. If your second and subsequent timesteps are known to run twice as fast as the initial timestep, edit the `sample-restart.jou` file to add `/solve/dual-time-iterate 2`. By adding this specification, the solution will only be restarted after two timesteps have been completed following the initial timestep. An output file for each timestep will still be saved in the output subdirectory. The value 2 is arbitrary but should be chosen so that the time for 2 steps fits within the job array time limit. Doing so minimizes the number of solution restarts which are computationally expensive. If the first timestep performed by `sample.jou` starts from a converged (previous) solution, choose 1 instead of 2, since likely all timesteps will require a similar amount of walltime to complete. Assuming 2 is chosen, the total time of simulation to be completed will be 1\*Dt+2\*Nrestart\*Dt where Nrestart is the number of solution restarts specified in the script. The total number of timesteps (and hence the number of output files generated) will therefore be 1+2\*Nrestart. The value for the time resource request should be chosen so that the initial timestep and subsequent timesteps will complete comfortably within the Slurm time window specifiable up to a maximum of `#SBATCH --time=07-00:00` days.

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

Fluent journal files can include basically any command from Fluent's Text User Interface (TUI); commands can be used to change simulation parameters like temperature, pressure, and flow speed. You can then run a series of simulations under different conditions with a single case file, by only changing the parameters in the journal file. Refer to the [Fluent User's Guide](https://ansyshelp.ansys.com/public/account/secured?returnurl=/Views/Secured/corp/v242/en/flu_ug/flu_ug.html) for more information, and a list of all commands that can be used. The following journal files are set up with `/file/cff-files no` to use the legacy .cas/.dat file format (the default in module versions 2019R3 or older). Set this to `/file/cff-files yes` instead to use the more efficient .cas.h5/.dat.h5 file format (the default in module versions 2020R1 or newer).

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

```text
define/user-defined/interpreted-functions "sampleudf.c" "cpp" 10000 no
```

#### Compiled

To use this approach, your UDF must be compiled on an Alliance cluster at least once. Doing so will create a `libudf` subdirectory structure containing the required `libudf.so` shared library. The `libudf` directory cannot simply be copied from a remote system (such as your laptop) to the cluster since the library dependencies of the shared library will not be satisfied, resulting in Fluent crashing on startup. That said, once you have compiled your UDF on an Alliance cluster, you can transfer the newly created `libudf` to any other Alliance cluster, providing your account loads the same StdEnv environment module version. Once copied, the UDF can be used by uncommenting the second (load) libudf line below in your journal file when submitting jobs to the cluster.

!!! warning "UDF Compilation in Journal Files"
    Both (compile and load) `libudf` lines should not be left uncommented in your journal file when submitting jobs on the cluster, otherwise your UDF will automatically be (re)compiled for each and every job. Not only is this highly inefficient, but it will also lead to race-condition-like build conflicts if multiple jobs are run from the same directory.

Besides configuring your journal file to build your UDF, the Fluent GUI may also be used. To do this, navigate to the *Compiled UDFs* dialog box, add the UDF source file and click on *Build*. When using a compiled UDF with parallel jobs, your source file should be parallelized as discussed in the section below.

```text
define/user-defined/compiled-functions compile libudf yes sampleudf.c "" ""
```

and/or

```text
define/user-defined/compiled-functions load libudf
```

#### Parallel

Before a UDF can be used with a Fluent parallel job (single node SMP and multinode MPI), it will need to be parallelized. By doing this we control how/which processes (host and/or compute) run specific parts of the UDF code when Fluent is run in parallel on the cluster. The instrumenting procedure involves adding compiler directives, predicates, and reduction macros into your working serial UDF. Failure to do so will result in Fluent running slow at best, or immediately crashing at worst. The end result will be a single UDF that runs efficiently when Fluent is used in both serial and parallel mode. The topic is described in detail in [Parallel Considerations](https://ansyshelp.ansys.com/public/account/secured?returnurl=//////Views/Secured/corp/v242/en/flu_udf/flu_udf_ChapParallelUDFUsage.html?q=parallel%20considerations).

#### DPM

UDFs can be used to customize Discrete Phase Models (DPM) as described in
*   [2024R2 Fluent Users Guide](https://ansyshelp.ansys.com/public/account/secured?returnurl=/Views/Secured/corp/v242/en/flu_ug/flu_ug.html): *Part III: Solution Mode | Chapter 24: Modeling Discrete Phase | 24.2 Steps for Using the Discrete Phase Models| 24.2.6 User-Defined Functions*, and
*   [2024R2 Fluent Customization Manual](https://ansyshelp.ansys.com/public/account/secured?returnurl=//////Views/Secured/corp/v242/en/flu_udf/flu_udf.html): *Part I: Creating and Using User Defined Functions | Chapter 2: DEFINE Macros | 2.5 Discrete Phase Model (DPM) DEFINE Macros*.<br>
Before a DMP-based UDF can be worked into a simulation, the injection of a set of particles must be defined by specifying *Point Properties* with variables such as source position, initial trajectory, mass flow rate, time duration, temperature, and so forth, depending on the injection type. This can be done in the GUI by clicking on *Physics panel --> Discrete Phase* to open the *Discrete Phase Model* box and then clicking on the *Injections* button. Doing so will open an *Injections* dialog box where one or more injections can be created by clicking on the *Create* button. The *Set Injection Properties* dialog which appears will contain an *Injection Type* pulldown where available types are single, group, surface, and flat-fan-atomizer. If you select any of these, you can then select the *Point Properties* tab to input the corresponding value fields. Another way to specify the *Point Properties* would be to read an injection text file. To do this, select *File* from the *Injection Type* pulldown, specify the *Injection Name* to be created, and click on the *File* button (located beside the *OK* button at the bottom of the dialog). Here, either an *Injection Sample File* (with a .dpm extension) or a manually created injection text file can be selected. To select the file in the Select File dialog box that change the File of type pull down to All Files (*), then highlight the file which could have any arbitrary name but commonly has an .inj extension, click the OK button. Assuming there are no problems with the file, no console error or warning message will appear. As you will be returned to the *Injections* dialog box, you should see the same injection name that you specified in the *Set Injection Properties* dialog and be able to list its particles and properties in the console. Next, open the *Discrete Phase Model* dialog box and select *Interaction with Continuous Phase* which will enable updating DPM source terms every flow iteration. This setting can be saved in your cas file or added via the journal file as shown. Once the injection is confirmed working in the GUI, the steps can be automated by adding commands to the journal file after the solution initialization, for example

```text
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

Before submitting a Workbench job to the queue with a Slurm script, you must initialize it once as described in the following steps.

1.  On the cluster where you will submit Workbench jobs, start an [OnDemand desktop](../interactive/open_ondemand.md#logging-into-the-open-ondemand-portal).
2.  Once the desktop appears, open a terminal window and `cd` into the directory containing your `YOURPROJECT.wbpj` file.
3.  Remove the old project cache directory by running `rm -rf _ProjectScratch` as this can be very large from previous runs.
4.  Open a terminal window and load the module version that you will be using in your Slurm script, for example `module load ansys/2025R2.04`.
5.  Open the Workbench GUI with your project file. This can be done by issuing `runwb2 -f YOURPROJECT.wbpj` directly from the command line. If and when a popup appears asking *Do you want to recover the project before opening ? (Any changes made since the last save will be lost.)* answer **No**.
6.  In the context menu popup that should appear in the centre *Project Schematic* window, right-click on *Model* and select *Reset*. When Ansys Workbench pops up a warning that *This operation will delete the operations local and generated data* click on **Ok** to accept and proceed.
7.  In the top menu bar pulldown, select *File -> Save* then *File -> Exit* to shut down Workbench.
8.  In the Ansys Workbench popup, when asked *The current project has been modified. Do you want to save it?*, click on the **No** button.
9.  Quit Workbench and submit your job using one of the Slurm scripts shown below.

!!! tip "Running Workbench Simulations via GUI"
    Since a compute node with up to 96 cores, 768 GB memory and 8 hours runtime can now be reserved for an OnDemand desktop session, consider running your Workbench simulations directly from within the Workbench native GUI when possible. This is a more intuitive option compared to submitting the job to the queue with a Slurm script.

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

The input file can be generated from within your interactive Workbench Mechanical session by clicking on *Solution -> Tools -> Write Input Files* then specifying *File name:* `YOURAPDLFILE.inp` and *Save as type:* `APDL Input Files (*.inp)`. APDL jobs can then be submitted to the queue with the `sbatch script-name.sh` command.

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

Ansys allocates 1024 MB total memory and 1024 MB database memory by default for APDL jobs. These values can be manually specified (or changed) by adding arguments `-m 1024` and/or `-db 1024` to the `mapdl` command line in the above scripts. When using a remote institutional license server with multiple Ansys licenses, it may be necessary to add `-p aa_r` or `-ppf anshpc`, depending on which Ansys module you are using.

!!! tip "Performance Optimization"
    Always perform detailed scaling tests before running production jobs to ensure that the optimal number of cores and minimum amount memory is specified in your scripts. The single node (SMP shared memory parallel) scripts will typically perform better than the multinode (DIS distributed memory parallel) scripts and therefore should be used whenever possible. To help avoid compatibility issues, the Ansys module loaded in your script should ideally match the version used to generate the input file.

For example, to check the version:

```bash
[gra-login2:~/testcase] cat YOURAPDLFILE.inp | grep version
 ! ANSYS input file written by Workbench version 2019 R3
```

## Rocky

This section provides sample Slurm scripts to solve standalone non-coupled Rocky simulations in a cluster queue. Both scripts are configured with `RESUME=0` so simulations are solved from the beginning by default. To restart a partially completed simulation, set `RESUME=1` and resubmit the script to the queue. To get a full listing of command line options, run `Rocky -h` on the command line after loading the Ansys module. Since a lock file is generated every time a simulation is started, only one job should be submitted at a time from the same directory.

Regarding which script to use, while all simulations should be tested independently, for a basic test case the GPU only script was found to outperform the CPU only script by a factor of 3.5x. Further increases in resources beyond 6 CPUs (for the CPU only script) or 2 CPUs + 1 GPU (1/7 of a H100 GPU for the GPU based script) provided no further speedup based on scaling testing for either script. Given these results, it appears likely that the GPU-based script will provide significantly faster solution times compared to just using CPUs for other standalone Rocky simulations.

!!! note "GPU Resources on Narval"
    As summarized under [Ratios in bundles](allocations_and_compute_scheduling.md#ratios-in-bundles), all clusters but Narval have H100 GPUs. Therefore, when using the GPU script on Narval, the `--gpus` Slurm option should be changed to request an a100 GPU instead.

Note that as of May 2026, only Rocky with the `ansys/2025R2|2.04` modules have been tested but not the `ansys/2025R1|1.02` modules yet.

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
      Rocky --headless --simulate --resume=0 --ncpus=$SLURM_CPUS_PER_TASK --use-gpu=0 $INPUTFILE
    else
      Rocky --headless --simulate --resume=1 --ncpus=$SLURM_CPUS_PER_TASK --use-gpu=1 $INPUTFILE
    fi
    ```

## Electronics

Slurm scripts for using AnsysEDT are provided in [this specific page](../software/ansysedt.md).