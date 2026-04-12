---
title: "MIKE/en"
slug: "mike"
lang: "en"

source_wiki_title: "MIKE/en"
source_hash: "ec479b3908895b3c84a3c902cd25e1d1"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:45:48.525091+00:00"

tags:
  - software

keywords:
  - "HPC clusters"
  - "installation procedure"
  - "hydraulic and hydrological modeling software"
  - "SBATCH"
  - "installation"
  - "Simulation"
  - "MIKE powered by DHI"
  - "Slurm"
  - "Bash script"
  - "DHI group"
  - "--install-path"
  - "hydraulic and hydrological modeling"
  - "MIKE 2022"
  - "MIKE"
  - "module load"
  - "hydraulic modeling software"
  - "license requirements"
  - "EBROOTIMPI"
  - "installation archives"
  - "Intel MPI library"
  - "MIKE_HOME"
  - "intelmpi"
  - "MIKE 2023"
  - "MIKE_Zero_2025_Tools_rhel9"
  - "modulefiles"
  - "minor updates"
  - "Finite Elements"
  - "MIKE_Zero_2025_Examples"
  - "environment module"
  - "SLURM"
  - "MPI"
  - "setrpaths.sh"
  - "FemEngineHD"
  - "install.sh"
  - "MIKE Zero"
  - "job script"

questions:
  - "What specific license and software version requirements must a user fulfill to run MIKE on the HPC clusters?"
  - "Why is it necessary to load a matching Intel MPI module before proceeding with the installation?"
  - "What are the main command-line steps required to extract, install, and patch the MIKE software components?"
  - "Why is the `sed` command used to modify the `install.sh` scripts by replacing `cp -rp` with `cp -r`?"
  - "What is the purpose of the `--eula` and `--install-path` arguments provided during the execution of the installation scripts?"
  - "Which specific components of the MIKE Zero 2025 software suite are being navigated to and installed in this sequence of commands?"
  - "What are the general steps and commands required to extract and install the MIKE software packages from their archives?"
  - "Which specific environment modules and library paths need to be loaded and configured for the different versions of MIKE?"
  - "What specific modification is made to the installation script for the MIKE 2024 version compared to the older versions?"
  - "What is the purpose of executing the `setrpaths.sh` script with the specified directory paths in this environment?"
  - "Which specific versions of the Intel compiler and Intel MPI are referenced in the provided command snippet?"
  - "How should the installation process be adapted when installing minor updates that may have different archive filenames?"
  - "How does the described installation procedure for MIKE differ from the official installation instructions?"
  - "What adjustments might be necessary regarding the Intel MPI library when installing future major releases of MIKE?"
  - "What steps and configurations are required to create and activate a custom environment module for a specific version of MIKE?"
  - "How do you activate the MIKE module for a specific version during a job or login session?"
  - "What command is used to configure the MIKE software license, and where is this configuration file stored?"
  - "What are the necessary Slurm directives and commands required to run a MIKE model using the FemEngineHD engine in a batch job script?"
  - "What is the primary purpose and function of the MIKE software package described in the text?"
  - "What specific modeling techniques and keywords are associated with this software?"
  - "How does the script determine the root directory path for the MIKE installation?"
  - "What specific Slurm resource allocations, such as memory, time, and tasks, are requested in this bash script?"
  - "Which software modules and dependencies must be loaded to properly set up the environment for MIKE 2023?"
  - "What are the names of the engine and the model file that this script is configured to run?"
  - "What are the specific Slurm resource allocations, such as nodes, tasks, and memory, requested in the job script?"
  - "Which software modules and environment variables must be loaded to set up the environment for MIKE 2022?"
  - "How does the script configure the MPI hostlist and execute the FemEngineHD engine with the model file?"
  - "What are the specific Slurm resource allocations, such as nodes, tasks, and memory, requested in the job script?"
  - "Which software modules and environment variables must be loaded to set up the environment for MIKE 2022?"
  - "How does the script configure the MPI hostlist and execute the FemEngineHD engine with the model file?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[MIKE powered by DHI](https://www.mikepoweredbydhi.com/) is a hydraulic and hydrological modeling software package.

## License requirements
MIKE is a commercial product and each user needs to supply their own license.

In order for you to use it on our HPC clusters, you will need to contact MIKE Customer Care at: [mike@dhigroup.com](mailto:mike@dhigroup.com) and confirm that you have
* an *internet license*, and
* a download link for the *Linux version* of MIKE.

## Installation

You need to download the installation archives for Linux.

The following instructions assume that the installation archives are in one Zip-file (MIKE 2025 and newer) or three `*.tgz` files (MIKE 2024 and older):

=== "MIKE 2025"
    * `MIKE_Zero_2025_rhel9.zip`
=== "MIKE 2024"
    * `MIKE_Zero_2024_rhel9_Update_1.tgz`
    * `MIKE_Zero_2024_Tools_rhel9_Update_1.tgz`
    * `MIKE_Zero_2024_Examples_Update_1.tgz`
=== "MIKE 2023"
    * `MIKE_Zero_2023_rhel7_22.11.05.tgz`
    * `MIKE_Zero_2023_Tools_rhel7_22.11.05.tgz`
    * `MIKE_Zero_2023_Examples.tgz`
=== "MIKE 2022"
    * `MIKE_Zero_2022_rhel7_Update_1.tgz`
    * `MIKE_Zero_2022_Tools_rhel7_Update_1.tgz`
    * `MIKE_Zero_2022_Examples_Update_1.tgz`

1. Create a directory `~/scratch/MIKE_TGZ` and upload the installation archive(s) to that location.

2. MIKE was compiled with the Intel MPI library, therefore you must load a matching `intelmpi` module.

=== "MIKE 2024 and 2025"
    ```bash
    module load StdEnv/2023 intel/2023.2.1 intelmpi/2021.9.0
    ```
=== "MIKE 2023"
    ```bash
    module load StdEnv/2020  intel/2021.2.0  intelmpi/2021.2.0
    ```
=== "MIKE 2022"
    ```bash
    module load StdEnv/2020  intel/2020.1.217  intelmpi/2019.7.217
    ```

3. Run the following commands depending on the version of MIKE. They will extract the archives, run the `install.sh` installation scripts for each component and then [patch the binaries](../getting-started/installing_software_in_your_home_directory.md#installing-binary-packages) so that they can find the dynamic libraries of Intel MPI.

=== "MIKE 2025"
    ```bash
    export MIKE_TGZ="$HOME/scratch/MIKE_TGZ"
    export MIKE_HOME="$HOME/MIKE/2025"
    
    cd $MIKE_TGZ
    unzip -j  MIKE_Zero_2025_rhel9.zip
    tar -xzf MIKE_Common_2025_rhel9.tgz
    tar -xzf MIKE_Zero_2025_rhel9.tgz
    tar -xzf MIKE_Zero_2025_Tools_rhel9.tgz
    tar -xzf MIKE_Zero_2025_Examples.tgz
    
    cd $MIKE_TGZ/MIKE_Common_2025_rhel9
    sed -i 's/ cp -rp / cp -r /' install.sh
    sh install.sh --eula --install-path "$MIKE_HOME" --license-server 127.0.0.1
    cd $MIKE_TGZ/MIKE_Zero_2025_rhel9
    sed -i 's/ cp -rp / cp -r /' install.sh
    sh install.sh --eula --install-path "$MIKE_HOME"
    cd $MIKE_TGZ/MIKE_Zero_2025_Tools_rhel9
    sed -i 's/ cp -rp / cp -r /' install.sh
    sh install.sh --eula --install-path "$MIKE_HOME"
    cd $MIKE_TGZ/MIKE_Zero_2025_Examples
    sed -i 's/ cp -rp / cp -r /' install.sh
    sh install.sh --eula --install-path "$MIKE_HOME"
    
    module load StdEnv/2023 intel/2023.2.1 intelmpi/2021.9.0
    setrpaths.sh --path "$MIKE_HOME/bin"  --add_origin  \
        --add_path="$EBROOTIMPI/mpi/latest/lib/release:$EBROOTIMPI/mpi/latest/lib"
    ```
=== "MIKE 2024"
    ```bash
    export MIKE_TGZ="$HOME/scratch/MIKE_TGZ"
    export MIKE_HOME="$HOME/MIKE/2024"
    
    cd $MIKE_TGZ
    tar -xzf MIKE_Zero_2024_rhel9_Update_1.tgz
    tar -xzf MIKE_Zero_2024_Tools_rhel9_Update_1.tgz
    tar -xzf MIKE_Zero_2024_Examples_Update_1.tgz
    
    cd $MIKE_TGZ/MIKE_Zero_2024_rhel9_Update_1
    sed -i 's/ cp -rp / cp -r /' install.sh
    sh install.sh --eula --install-path "$MIKE_HOME" --license-server 127.0.0.1
    cd $MIKE_TGZ/MIKE_Zero_2024_Tools_rhel9_Update_1
    sed -i 's/ cp -rp / cp -r /' install.sh
    sh install.sh --eula --install-path "$MIKE_HOME"
    cd $MIKE_TGZ/MIKE_Zero_2024_Examples_Update_1
    sed -i 's/ cp -rp / cp -r /' install.sh
    sh install.sh --eula --install-path "$MIKE_HOME"
    
    module load StdEnv/2023 intel/2023.2.1 intelmpi/2021.9.0
    setrpaths.sh --path "$MIKE_HOME/bin"  --add_origin  \
        --add_path="$EBROOTIMPI/mpi/latest/lib/release:$EBROOTIMPI/mpi/latest/lib"
    ```
=== "MIKE 2023"
    ```bash
    export MIKE_TGZ="$HOME/scratch/MIKE_TGZ"
    export MIKE_HOME="$HOME/MIKE/2023"
    
    cd $MIKE_TGZ
    tar -xzf MIKE_Zero_2023_rhel7_22.11.05.tgz
    tar -xzf MIKE_Zero_2023_Tools_rhel7_22.11.05.tgz
    tar -xzf MIKE_Zero_2023_Examples.tgz
    
    cd $MIKE_TGZ/MIKE_Zero_2023_rhel7_22.11.05
    sh install.sh --eula --install-path "$MIKE_HOME" --license-server 127.0.0.1
    cd $MIKE_TGZ/MIKE_Zero_2023_Tools_rhel7_22.11.05
    sh install.sh --eula --install-path "$MIKE_HOME"
    cd $MIKE_TGZ/MIKE_Zero_2023_Examples
    sh install.sh --eula --install-path "$MIKE_HOME"
    
    module load StdEnv/2020  intel/2021.2.0  intelmpi/2021.2.0
    setrpaths.sh --path "$MIKE_HOME/bin"  --add_origin  \
        --add_path="$EBROOTIMPI/mpi/latest/lib/release:$EBROOTIMPI/mpi/latest/lib"
    ```
=== "MIKE 2022"
    ```bash
    MIKE_TGZ_DIR="$HOME/MIKE_TGZ"
    MIKE_INST_DIR="$HOME/MIKE/2022"
    
    cd $MIKE_TGZ_DIR
    tar -xzf MIKE_Zero_2022_rhel7_Update_1.tgz 
    tar -xzf MIKE_Zero_2022_Tools_rhel7_Update_1.tgz
    tar -xzf MIKE_Zero_2022_Examples_Update_1.tgz
    
    cd $MIKE_TGZ_DIR/MIKE_Zero_2022_rhel7_Update_1
    sh install.sh --eula --install-path "$MIKE_INST_DIR" --license-server 127.0.0.1
    cd $MIKE_TGZ_DIR/MIKE_Zero_2022_Tools_rhel7_Update_1
    sh install.sh --eula --install-path "$MIKE_INST_DIR"
    cd $MIKE_TGZ_DIR/MIKE_Zero_2022_Examples_Update_1
    sh install.sh --eula --install-path "$MIKE_INST_DIR"
    
    module load StdEnv/2020 intel/2020.1.217 intelmpi/2019.7.217
    setrpaths.sh --path "$MIKE_INST_DIR/bin"  --add_origin  \
        --add_path="$EBROOTIMPI/intel64/lib/release:$EBROOTIMPI/intel64/lib"
    ```

### Other versions

The instructions above assume specific filenames for the installation archives. When installing minor updates released in the same year, the filenames for the archives (e.g. in `tar -xzf MIKE_Zero_2023_rhel7_22.11.05.tgz`), as well as the directory names (e.g. in `cd $MIKE_TGZ/MIKE_Zero_2023_rhel7_22.11.05`) need to be adjusted accordingly. Future major releases of MIKE may use a newer version of Intel MPI, so the above instructions may need to be adapted accordingly. Try a module of the Intel MPI library with a matching Major version (i.e. year).

Essentially the above instructions follow the official installation procedure with the exception that the installation of `MIKE_Zero_*_Prerequisites.tgz` (Intel MPI library) is skipped and a matching module is loaded instead. Furthermore the `setrpaths.sh` script is used to [patch the installed binaries](../getting-started/installing_software_in_your_home_directory.md#installing-binary-packages) to make them compatible with our software stack.

If you run into problems adapting the recipe for newer versions of MIKE, contact our [Technical support](../support/technical_support.md).

### Create a module

Paste these commands into your terminal to create an environment module for MIKE. Make sure to adjust the version (e.g. "2025") to match the version you have installed. Also adjust the version of the `intelmpi` and `intel` modules to match what you had loaded during the installation. After running the commands below, do a fresh login to have the newly created environment module become visible to "module" commands or run `module use $HOME/modulefiles`.

=== "MIKE 2025"
    ```bash
    export MIKE_VERSION=2025
    mkdir -p $HOME/modulefiles/mike
    cat > $HOME/modulefiles/mike/${MIKE_VERSION}.lua <<EOF
    help([[
    Module for MIKE ${MIKE_VERSION} (by DHI group)
    ]])
    local version = "${MIKE_VERSION}"
    whatis("Version:".. version)
    whatis("Keywords: FEM, Finite Elements, Simulation")
    whatis("URL: https://www.mikepoweredbydhi.com/mike-" .. version)
    whatis("Description: MIKE is a hydraulic and hydrological modeling software package.")
    
    local home = os.getenv("HOME") or "~"
    local root = pathJoin( home, "MIKE", version)
    
    depends_on("StdEnv/2023", "intel/2023.2.1", "intelmpi/2021.9.0")
    setenv("I_MPI_PMI_LIBRARY", "/opt/software/slurm/lib/libpmi2.so")
    setenv("SLURM_MPI_TYPE", "pmi2")
    setenv("MIKE_HOME", root)
    setenv("MIKE_PROGRESS", "STDOUT")
    prepend_path( "PATH", pathJoin(root, "bin"))
    EOF
    ```
=== "MIKE 2024"
    ```bash
    export MIKE_VERSION=2024
    mkdir -p $HOME/modulefiles/mike
    cat > $HOME/modulefiles/mike/${MIKE_VERSION}.lua <<EOF
    help([[
    Module for MIKE ${MIKE_VERSION} (by DHI group)
    ]])
    local version = "${MIKE_VERSION}"
    whatis("Version:".. version)
    whatis("Keywords: FEM, Finite Elements, Simulation")
    whatis("URL: https://www.mikepoweredbydhi.com/mike-" .. version)
    whatis("Description: MIKE is a hydraulic and hydrological modeling software package.")
    
    local home = os.getenv("HOME") or "~"
    local root = pathJoin( home, "MIKE", version)
    
    depends_on("StdEnv/2023", "intel/2023.2.1", "intelmpi/2021.9.0")
    setenv("I_MPI_PMI_LIBRARY", "/opt/software/slurm/lib/libpmi2.so")
    setenv("SLURM_MPI_TYPE", "pmi2")
    setenv("MIKE_HOME", root)
    setenv("MIKE_PROGRESS", "STDOUT")
    prepend_path( "PATH", pathJoin(root, "bin"))
    EOF
    ```
=== "MIKE 2023"
    ```bash
    export MIKE_VERSION=2023
    mkdir -p $HOME/modulefiles/mike
    cat > $HOME/modulefiles/mike/${MIKE_VERSION}.lua <<EOF
    help([[
    Module for MIKE ${MIKE_VERSION} (by DHI group)
    ]])
    local version = "${MIKE_VERSION}"
    whatis("Version:".. version)
    whatis("Keywords: FEM, Finite Elements, Simulation")
    whatis("URL: https://www.mikepoweredbydhi.com/mike-" .. version)
    whatis("Description: MIKE is a hydraulic and hydrological modeling software package.")
    
    local home = os.getenv("HOME") or "~"
    local root = pathJoin( home, "MIKE", version)
    
    depends_on("StdEnv/2020", "intel/2021.2.0", "intelmpi/2021.2.0")
    
    setenv("I_MPI_PMI_LIBRARY", "/opt/software/slurm/lib/libpmi2.so")
    setenv("SLURM_MPI_TYPE", "pmi2")
    setenv("MIKE_HOME", root)
    setenv("MIKE_PROGRESS", "STDOUT")
    prepend_path( "PATH", pathJoin(root, "bin"))
    EOF
    ```
=== "MIKE 2022"
    ```bash
    export MIKE_VERSION=2022
    mkdir -p $HOME/modulefiles/mike
    cat > $HOME/modulefiles/mike/${MIKE_VERSION}.lua <<EOF
    help([[
      Module for MIKE ${MIKE_VERSION} (by DHI group)
    ]])
    local version = "${MIKE_VERSION}"
    whatis("Version:".. version)
    whatis("Keywords: FEM, Finite Elements, Simulation")
    whatis("URL: https://www.mikepoweredbydhi.com/mike-" .. version)
    whatis("Description: MIKE is a hydraulic and hydrological modeling software package.")
    
    local home = os.getenv("HOME") or "~"
    local root = pathJoin( home, "MIKE", version)
    
    depends_on("StdEnv/2020", "intel/2020.1.217", "intelmpi/2019.7.217") 
    
    setenv("I_MPI_PMI_LIBRARY", "/opt/software/slurm/lib/libpmi2.so")
    setenv("SLURM_MPI_TYPE", "pmi2")
    setenv("MIKE_HOME", root)
    setenv("MIKE_PROGRESS", "STDOUT")
    prepend_path( "PATH", pathJoin(root, "bin"))
    EOF
    ```

Activate this module in each job or login session with:

=== "MIKE 2025"
    ```bash
    module load StdEnv/2023 mike/2025
    ```
=== "MIKE 2024"
    ```bash
    module load StdEnv/2023 mike/2024
    ```
=== "MIKE 2023"
    ```bash
    module load StdEnv/2020 mike/2023
    ```
=== "MIKE 2022"
    ```bash
    module load StdEnv/2020 mike/2022
    ```

### Configure the license

From MIKE Customer Care you will have instructions like this for configuring your license:
```bash
licconfig set --type=internet --iuser=user@example.com --ipassword=my-password
```
This normally needs to be done only once whenever you get a new license or license code. The license information will be stored in a file `~/.config/DHI/license/NetLmLcwConfig.xml`.

## Example job script

=== "MIKE 2025"
    ```bash tab="job_mike_2025_CPU.sh"
    #!/bin/bash
    #SBATCH --nodes=1
    #SBATCH --ntasks=8
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=4000M
    #SBATCH --time=00:20:00
    
    module load  StdEnv/2023  intel/2023.2.1  intelmpi/2021.9.0  mike/2025
    export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}
    
    engine="FemEngineHD"
    model="my_model.m3fm"
    
    srun $engine $model
    ```
=== "MIKE 2024"
    ```bash tab="job_mike_2024_CPU.sh"
    #!/bin/bash
    #SBATCH --nodes=1
    #SBATCH --ntasks=8
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=4000M
    #SBATCH --time=00:20:00
    
    module load  StdEnv/2023  intel/2023.2.1  intelmpi/2021.9.0  mike/2024
    export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}
    
    engine="FemEngineHD"
    model="my_model.m3fm"
    
    srun $engine $model
    ```
=== "MIKE 2023"
    ```bash tab="job_mike_2023_CPU.sh"
    #!/bin/bash
    #SBATCH --nodes=1
    #SBATCH --ntasks=8
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=4000M
    #SBATCH --time=00:20:00
    
    module load StdEnv/2020  intel/2021.2.0  intelmpi/2021.2.0  mike/2023
    export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}
    
    engine="FemEngineHD"
    model="my_model.m3fm"
    
    srun $engine $model
    ```
=== "MIKE 2022"
    ```bash tab="job_mike_2022_CPU.sh"
    #!/bin/bash
    #SBATCH --nodes=1
    #SBATCH --ntasks=8
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=4000M
    #SBATCH --time=00:20:00
    
    module load StdEnv/2020 intel/2020.1.217 intelmpi/2019.7.217 mike/2022
    export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}
    slurm_hl2hl.py --format MPIHOSTLIST > machinefile.$SLURM_JOBID
    
    engine="FemEngineHD"
    model="my_model.m3fm"
    
    mpirun -machinefile machinefile.$SLURM_JOBID $engine $model