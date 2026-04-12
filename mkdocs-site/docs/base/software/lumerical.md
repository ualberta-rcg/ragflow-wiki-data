---
title: "Lumerical"
slug: "lumerical"
lang: "base"

source_wiki_title: "Lumerical"
source_hash: "c536000f183fafd671f1ec5c00648a1f"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:32:42.054304+00:00"

tags:
  - software

keywords:
  - "Gridpoints"
  - "sed"
  - "template submission scripts"
  - "job submission"
  - "TOTALMEM"
  - "Memory required per process"
  - "installation recipe"
  - "sbatch"
  - "Lumerical module"
  - "Timesteps"
  - "Nanophotonics"
  - "Slurm"
  - "submission script"
  - "fdtd-process-template"
  - "Installation"
  - "FILENAME"
  - "fdtd_solutions module"
  - "FDTD"
  - "memory and time estimates"
  - "module load"
  - "MPI implementation"
  - "license server"
  - "simulation"
  - "Lumerical"
  - "FDTD Solutions"
  - "Software module"
  - "license file"
  - "shellfile"
  - "SLURM"
  - "TIME"
  - "Technical support"
  - "job submission script"
  - "PROCMEM"
  - "bash script"
  - "Estimated time"
  - "MPI"
  - "replacements"

questions:
  - "What is the Lumerical software suite used for?"
  - "Why must users perform their own installation of Lumerical on Compute Canada systems?"
  - "How should a user modify the installation command if their downloaded Lumerical release version does not exactly match the available installation recipe?"
  - "What should you do if the standard Lumerical installation process does not work?"
  - "What specific actions and commands are required to load the Lumerical module after installation?"
  - "What configuration step is introduced immediately after the module loading instructions?"
  - "How do you configure the Lumerical module to connect to a specific license server?"
  - "What is the procedure for installing different versions of FDTD Solutions using EasyBuild?"
  - "How should a job submission script be configured to properly handle the MPI implementation for Lumerical or FDTD Solutions?"
  - "How is the total number of cores calculated for the FDTD engine execution in the provided script?"
  - "Why does the FDTD MPI implementation require special job submission options?"
  - "What specific SLURM parameters should be used when submitting a job for the fdtd_solutions module?"
  - "What are the key Slurm directives required in the basic submission script to request resources for an FDTD Solutions job?"
  - "How does the template system improve the efficiency of running multiple FDTD simulations?"
  - "How do you use the `fdtd-run.sh` command to submit multiple project files and specify the number of nodes?"
  - "What is the primary purpose of the `fdtd-process-template.sh` script and what command-line options does it accept?"
  - "How does the script calculate the estimated time and total memory required for the FDTD simulation?"
  - "Which specific tokens in the submission script template are replaced with actual values from the FDTD Solutions project file?"
  - "What is the primary purpose of the `fdtd-process-template.sh` script within this code snippet?"
  - "How can a user fine-tune the memory and time estimates for the generated submission script?"
  - "How does the script extract the total memory value after generating the shell file?"
  - "How is the required memory per process calculated and what minimum threshold is enforced?"
  - "What method does the script use to extract the number of gridpoints and timesteps from the temporary file?"
  - "What variables are factored into the estimated time calculation before applying the minimum time limit?"
  - "How does the script calculate the hours, minutes, and seconds from the initial time value?"
  - "What is the purpose of the sed command and which specific placeholders does it replace in the target file?"
  - "What external variables and arguments, such as $2 and $TOTALMEM, are required for this script snippet to function properly?"
  - "How does the script calculate the hours, minutes, and seconds from the initial time value?"
  - "What is the purpose of the sed command and which specific placeholders does it replace in the target file?"
  - "What external variables and arguments, such as $2 and $TOTALMEM, are required for this script snippet to function properly?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Lumerical](https://www.lumerical.com/) is a suite of applications for modelling [nanophotonic](https://en.wikipedia.org/wiki/Nanophotonics) devices, which includes [FDTD Solutions](https://www.lumerical.com/tcad-products/fdtd/).

## Installation
FDTD Solutions is now available as part of the Lumerical package.
The Digital Research Alliance of Canada (the Alliance) does not have a central installation of the Lumerical suite or FDTD Solutions. However, if you are licensed to use the software, you can install it following the instructions below.

If you have downloaded the whole Lumerical suite (e.g. filename: `Lumerical-2020a-r1-d316eeda68.tar.gz`), follow the instructions in sections "Installing Lumerical" and "Using the Lumerical module".
If you have downloaded FDTD Solutions on its own (e.g. filename: `FDTD_Solutions-8.19.1438.tar.gz`), follow the instructions in sections "Installing FDTD Solutions" and "Using the fdtd_solutions module".

## Installing Lumerical
### In case the installer release matches that of the recipe
To install the Lumerical suite run the command
```bash
eb Lumerical-2020a-r1-d316eeda68.eb --sourcepath=<path> --disable-enforce-checksums
```
where `path` is the path to the folder containing the `.tar.gz` file to install Lumerical on Linux.

### In case the installer release does not match that of the recipe
With a different 2020a release than 2020a-r1-d316eeda68, run
```bash
eb Lumerical-2020a-r1-d316eeda68.eb --try-software-version=<version> --sourcepath=<path> --disable-enforce-checksums
```
For example, if `Lumerical-2020a-r1-d316eeda68.eb.tar.gz` is downloaded in `$HOME/scratch`, the following command will install Lumerical within your `$HOME/.local` folder.
```bash
eb Lumerical-2020a-r1-d316eeda68.eb --try-software-version=2020a-r6-aabbccdd --sourcepath=$HOME/scratch --disable-enforce-checksums
```

It is important that the version of the installation recipe (year plus 'a' or 'b') needs to exactly match that of the installer.
If either the letter or the year changes (e.g. from 2020a to 2020b), we will need to adapt the installation script to the new version.

As of April 1st, 2020 we have the following installation recipes available:

| Installation recipe                               | Intended for Installer                             | Compatible with Installers        |
|:--------------------------------------------------|:---------------------------------------------------|:----------------------------------|
| `Lumerical-2019b-r6-1db3676.eb`                   | `Lumerical-2019b-r6-1db3676.tar.gz`                | `Lumerical-2019b-*.tar.gz`        |
| `Lumerical-2020a-r1-d316eeda68.eb`                | `Lumerical-2020a-r1-d316eeda68.tar.gz`             | `Lumerical-2020a-*.tar.gz`        |
| `Lumerical-2021-R2.5-2885-27742aa972.eb`          | `Lumerical-2021-R2.5-2885-27742aa972.tar.gz`       | `Lumerical-2021-*.tar.gz`         |
| `Lumerical-2022-R1.3-3016-2c0580a.eb`             | `Lumerical-2022-R1.3-3016-2c0580a.tar.gz`          | `Lumerical-2022-*.tar.gz`         |

If this does not work, please contact our [Technical support](../support/technical_support.md) and we will adapt an installation recipe for your version.

Once installed, you will need to log out and back into the server. To load the Lumerical module, use
```bash
module load lumerical
```

### Configuring your own license file

The Lumerical module will look for the file `$HOME/.licenses/lumerical.lic` to determine how to contact the license server.
Create the file with the following content, adjusting `27011@license01.example.com` to the port and hostname of your license server.

!!! tip "Create license file"
    copy the content below to `$HOME/.licenses/lumerical.lic`
    ```
    setenv("LUMERICAL_LICENSE_FILE", "27011@license01.example.com")
    ```

## Installing FDTD Solutions
To install FDTD Solutions, run the command
```bash
eb FDTD_Solutions-8.19.1438.eb --sourcepath=<path> --disable-enforce-checksums
```
where `path` is the path to the folder containing the `.tar.gz` file to install FDTD Solutions on Linux.

With a version other than 8.19.1438, run
```bash
eb FDTD_Solutions-8.19.1438.eb --try-software-version=<version> --sourcepath=<path> --disable-enforce-checksums
```
For example, if `FDTD_Solutions-8.19.1466.tar` is downloaded in `$HOME/Downloads`, the following command will install FDTD Solution within your `$HOME/.local` folder.
```bash
eb FDTD_Solutions-8.19.1438.eb --try-software-version=8.19.1466 --sourcepath=$HOME/Downloads --disable-enforce-checksums
```

If this does not work, please contact our [Technical support](../support/technical_support.md) and we will adapt an installation script for your version.

Once installed, you will need to log out and back into the server. To load the FDTD module, use
```bash
module load fdtd_solutions
```

You will also need to set up your installation to use your license server. Start the software first on a login node; it should ask you for information about the license server. You will only need to do this once.

## Using the software
The main difference between the modules `fdtd_solutions` and `lumerical`, beside the fact that the Lumerical module contains additional tools, is that the environment variable that contains the install location is named `EBROOTFDTD_SOLUTIONS` and `EBROOTLUMERICAL` respectively. This means scripts written for one module should be adjusted for the other by replacing the name of the module in the `module load ...` line and replacing `EBROOTFDTD_SOLUTIONS` with `EBROOTLUMERICAL` or vice versa.

## Using the Lumerical module

The MPI implementation provided by Lumerical is not tightly coupled with our scheduler. Because of this, you should use options `--ntasks-per-node=1` and `--cpus-per-task=32` when submitting a job.

Your submission script should look like the following example, where two nodes are requested for 30 minutes. You can adjust the time limit and the node count to fit your needs.

=== "lumrical_job.sh"
    ```bash
    #!/bin/bash
    #SBATCH --time=0:30:00            # time limit (D-HH:MM:SS)
    #SBATCH --ntasks-per-node=1       # do not change this number
    #SBATCH --cpus-per-task=32        # adjust to number of cores per node
    #SBATCH --ntasks=2       # the same number as nodes, one task per node
    #SBATCH --nodes=2
    #SBATCH --mem=0          # special value, requests all memory on node

    module load lumerical

    MPI=$EBROOTLUMERICAL/mpich2/nemesis/bin/mpiexec
    MY_PROG=$EBROOTLUMERICAL/bin/fdtd-engine-mpich2nem

    INPUT="avalanche_photodetector_optical.fsp"
    NCORE=$((SLURM_NTASKS * SLURM_CPUS_PER_TASK))

    $MPI -n $NCORE $MY_PROG ./${INPUT}
    ```

## Using the fdtd_solutions module
The MPI implementation provided by FDTD is not tightly coupled with our scheduler. Because of this, you should use options `--ntasks-per-node=1` and `--cpus-per-task=32` when submitting a job.

Your submission script should look like the following example, where two nodes are requested for one hour. You can adjust the time limit and the node count to fit your needs.

=== "fdtd_solutions.sh"
    ```bash
    #!/bin/bash
    #SBATCH --time=0:30:00            # time limit (D-HH:MM:SS)
    #SBATCH --ntasks-per-node=1    # do not change this number
    #SBATCH --cpus-per-task=32     # do not change this number
    #SBATCH --ntasks=2    # the same number as nodes, one task per node
    #SBATCH --nodes=2
    #SBATCH --mem=0       # special value, requests all memory on node

    module load fdtd_solutions
    MPI=$EBROOTFDTD_SOLUTIONS/mpich2/nemesis/bin/mpiexec
    MY_PROG=$EBROOTFDTD_SOLUTIONS/bin/fdtd-engine-mpich2nem

    INPUT="benchmark2.fsp"
    NCORE=$((SLURM_NTASKS * SLURM_CPUS_PER_TASK))
    $MPI -n $NCORE $MY_PROG ./${INPUT}
    ```

## Templates

!!! note
    This section is intended for use with the "fdtd_solutions" module and has not been adapted for "lumerical".

If you are performing a lot of simulations, you may find it inefficient to edit the job submission script for each simulation. You can use template submission scripts to improve this.

For example:
*   Create directory `$HOME/bin` and put the main script `fdtd-run.sh` (see below) there.
*   Create directory `$HOME/bin/templates` and put the job submission template script `fdtd-mpi-template.sh` and process template script `fdtd-process-template.sh` there.

`fdtd-mpi-template.sh` is basically a shell of the `fdtd_solutions.sh` script shown above and `fdtd-process-template.sh` determines the computing resources you need.

To submit a job, run
```bash
fdtd-run.sh fsp1 [fsp2 ...]
```
This will use the 32 cores on a single standard node. If you want to use more cores, request multiple nodes like so:
```bash
fdtd-run.sh -nn <nodes> fsp1 [fsp2 ...]
```

=== "fdtd-run.sh"
    ```bash
    #!/bin/bash
    # This script will create a Slurm-style job submission script for
    # FDTD Solutions project files using the template provided in
    # templates/fdtd-mpi-template.sh. Certain tags in the template
    # file are replaced with values extracted from the project file.
    #
    # The calling convention for this script is:
    #
    # fdtd-run.sh [-nn <nodes>] fsp1 [fsp2 ... fspN]
    #
    # The arguments are as follows:
    #
    # -nn       The number of nodes to use for the job(s).
    #           If no argument is given one node is used.
    #
    # fsp*      An FDTD Solutions project file. One is required, but
    #           multiple can be specified on one command line.
    #
    ##########################################################################

    # Locate the directory of this script so we can find
    # utility scripts and templates relative to this path.
    module load fdtd_solutions
    SCRIPTDIR=$EBROOTFDTD_SOLUTIONS/bin

    # The location of the template file to use when submitting jobs.
    # The line below can be changed to use your own template file.
    TEMPLATE=../bin/templates/fdtd-mpi-template.sh

    # Number of processes per node.
    PROCS=32

    # Number of nodes to use. Default is 1 if no -nn argument is given.
    NODES=1
    if [ "$1" = "-nn" ]; then
        NODES=$2
        shift
        shift
    fi

    # For each fsp file listed on the command line, generate the
    # submission script and submit it with sbatch.
    while(( $# > 0 ))
    do

        # Generate the submission script by replacing the tokens in the template.
        # Additional arguments can be added to fdtd-process-template to fine-tune
        # the memory and time estimates. See comments in that file for details.
        SHELLFILE=${1%.fsp}.sh
        ../bin/templates/fdtd-process-template.sh -ms 500 $1 $TEMPLATE $((PROCS)) > $SHELLFILE
        TOTAL_MEM=$(head -n 1 $SHELLFILE)
        sed -i -e '1,1d' $SHELLFILE

        # Submit the job script.
        echo Submitting: $SHELLFILE
        echo Total Memory Required = $TOTAL_MEM
        sbatch --nodes=${NODES} --ntasks=${NODES} --cpus-per-task=${PROCS} --mem=${TOTAL_MEM} $SHELLFILE

        shift
    done
    ```

=== "fdtd-mpi-template.sh"
    ```bash
    #!/bin/bash
    #SBATCH --time=<hours>:<minutes>:<seconds>
    #SBATCH --ntasks-per-node=1

    module load fdtd_solutions
    MPI=$EBROOTFDTD_SOLUTIONS/mpich2/nemesis/bin/mpiexec
    MY_PROG=$EBROOTFDTD_SOLUTIONS/bin/fdtd-engine-mpich2nem

    INPUT="<filename>"
    NCORE=$((SLURM_NTASKS * SLURM_CPUS_PER_TASK))
    $MPI -n $NCORE $MY_PROG ./${INPUT}
    ```

=== "fdtd-process-template.sh"
    ```bash
    #!/bin/bash
    # This script is used to replace tags in a submission script template with
    # actual values from an FDTD Solutions project file. The script is called
    # with the following arguments:
    #
    # fdtd-process-template.sh [options] <fsp file> <template file> <#processes>
    #
    # Valid options are:
    #
    # -r <rate>            The simulation rate in MNodes/s used in time estimates.
    #                      If no option is given the default is 4MNodes/s/process
    #                      which is very conservative.
    #
    # -tm <min_time>       The minimum time in seconds that the simulation can take. 
    #                      If no option is given the default is 600 seconds.
    #
    # -ms <memory_safety>  A multiplicative factor to apply to the memory estimate in %.
    #                      If no option is given the default value is 110.
    #
    # -mm <memory_min>     The minimum memory that a process can use. 
    #                       If no option is given the default is 20MB.
    #
    # The script will replace the following tokens in the template file with specified values:
    #
    # Token                Value
    # <total_memory>       The total memory required by all processes
    # <processor_memory>   The memory required for each simulation process
    # <hours>              The total hours required for the simulation
    # <minutes>            The total minutes required for the simulation
    # <seconds>            The total seconds required for the simulation
    # <n>                  The number of processes to use
    # <dir_fsp>            The path of the fsp project file
    # <filename>           The name of the fsp project file, without a leading path
    #
    ############################################################################################

    #Rate default
    RATE=4

    #Minimum time default
    TIME_MIN=600

    #Memory safety default
    MEMORY_SAFETY=110

    #Minimum memory default
    MEMORY_MIN=20

    #Process command line options
    while [ $# -gt 3 ] ; do
        case $1 in
            -r) RATE=$2
             ;;
            -tm) TIME_MIN=$2
             ;;
            -ms) MEMORY_SAFETY=$2
             ;;
            -mm) MEMORY_MIN=$2
             ;;
        esac
        shift
        shift
    done

    #Number of processes
    PROCS=$3

    #Path of fsp file
    DIRFSP=`dirname $1`

    #fsp file name without path
    FILENAME=`basename $1`

    #Run FDTD to get stats from project file
    module load fdtd_solutions
    SCRIPTDIR=$EBROOTFDTD_SOLUTIONS/bin
    $SCRIPTDIR/fdtd-engine-mpich2nem -mr $1 > $1.tmp

    #Estimated memory
    ESTMEM=`grep memory $1.tmp | sed 's/^.*=//'`

    #Total memory required
    TOTALMEM=$(( ESTMEM * MEMORY_SAFETY / 100 ))

    #Memory required per process
    PROCMEM=$((TOTALMEM / PROCS))
    if [ "$PROCMEM" -lt "$MEMORY_MIN" ]; then
        PROCMEM=$MEMORY_MIN
    fi

    #Gridpoints
    GRIDPTS=`grep gridpoints $1.tmp | sed 's/^.*=//'`

    #Timesteps
    TIMESTEPS=`grep time_steps $1.tmp | sed 's/^.*=//'`

    #Estimated time
    TIME=$(( GRIDPTS * TIMESTEPS / PROCS / RATE / 10000000 ))
    if [ "$TIME" -lt "$TIME_MIN" ]; then
        TIME=$TIME_MIN
    fi

    HOUR=$((TIME / 3600))
    MINSEC=$((TIME - HOUR * 3600))
    MIN=$((MINSEC / 60))
    SEC=$((MINSEC - MIN * 60))

    echo $TOTALMEM

    #The replacements
    sed -e "s#<total_memory>#$TOTALMEM#g" \
        -e "s#<processor_memory>#$PROCMEM#g" \
        -e "s#<hours>#$HOUR#g" \
        -e "s#<minutes>#$MIN#g" \
        -e "s#<seconds>#$SEC#g" \
        -e "s#<n>#$PROCS#g" \
        -e "s#<dir_fsp>#$DIRFSP#g" \
        -e "s#<filename>#$FILENAME#g" \
        $2