---
title: "MIKE"
slug: "mike"
lang: "base"

source_wiki_title: "MIKE"
source_hash: "3f331bf797401daa6dd8204f11c73e94"
last_synced: "2026-10-25T00:54:39.630071+00:00"
last_processed: "2026-10-25T01:38:14.922269+00:00"

tags:
  - software

keywords:
  - "internet license"
  - "Intel MPI module"
  - "Linux installation archives"
  - "module load StdEnv/2023"
  - "license-server 127.0.0.1"
  - "MIKE_VERSION=2022"
  - "Simulation"
  - "MIKE_TGZ"
  - "mike/2023"
  - "setrpaths.sh"
  - "MIKE installation"
  - "module load Intel MPI"
  - "intelmpi/2021.2.0"
  - "machinefile"
  - "SLURM"
  - "tar"
  - "MIKE"
  - "mkdir -p"
  - "unzip"
  - "install.sh"
  - "hydraulic and hydrological modeling"
  - "MIKE hydraulic modeling"
  - "Finite Elements"
  - "install.sh script"
  - "export"
  - "modulefiles/mike"
  - "module"
  - "MIKE_VERSION"
  - "modulefiles"
  - "I_MPI_PMI_LIBRARY"
  - "SLURM job script"
  - "install.sh --eula --install-path"
  - "license configuration"
  - "SLURM_MPI_TYPE"
  - "SLURM_CPUS_PER_TASK"
  - "MIKE_Zero_2026"
  - "OMP_NUM_THREADS"
  - "FemEngineHD"
  - "MIKE_HOME"
  - "intelmpi/2021.9.0"
  - "FEM"
  - "module load"
  - "mpirun"

questions:
  - "What license type and contact information are required to run MIKE on the HPC clusters?"
  - "Which Intel MPI modules must be loaded for each MIKE version (2022, 2023, 2024‑2026) before installation?"
  - "What are the exact commands and environment variable settings needed to extract and install the MIKE 2026 archives?"
  - "What is the purpose of using `sed -i 's/ cp -rp / cp -r /' install.sh` before running the installation scripts?"
  - "How are the environment variables `MIKE_TGZ` and `MIKE_HOME` set and applied for the different MIKE versions (2026, 2025, 2024, 2023)?"
  - "Which modules are loaded and why is `setrpaths.sh` executed after each MIKE installation?"
  - "¿Qué función tienen las variables de entorno MIKE_TGZ y MIKE_HOME en este script?"
  - "¿Qué tipos de archivos se descomprimen con los comandos tar y unzip en la secuencia mostrada?"
  - "¿En qué sistema operativo está orientada la instalación de MIKE 2026 según los nombres de los archivos?"
  - "What does the `cp -r /' install.sh sh install.sh --eula --install-path \"$MIKE_HOME\"` command accomplish in the installation process?"
  - "Which modules are loaded (`StdEnv/2023`, `intel/2023.2.1`, `intelmpi/2021.9.0`) and what role do they play before executing `setrpaths.sh`?"
  - "How does the `setrpaths.sh` command configure the runtime library paths for the MIKE installation, specifically with the `--add_origin` and `--add_path` options?"
  - "Which commands are required to extract the MIKE Zero archives and run the `install.sh` scripts for a specific version (e.g., 2022 or 2023)?"
  - "How should the `setrpaths.sh` script be executed, and which Intel MPI library paths need to be added to ensure the binaries work with the software stack?"
  - "What are the steps to create a custom environment module for a MIKE version, and which variables (such as version numbers and module names) must be adjusted?"
  - "What dependencies and environment modules are defined for each MIKE version in the generated Lua module files?"
  - "How does the script construct the MIKE_HOME path and set related environment variables for each version?"
  - "Which MIKE versions have different dependency versions (e.g., StdEnv, Intel, IntelMPI) and what are those differences?"
  - "What is the purpose of executing `module use $HOME/modulefiles` after creating a new environment module?"
  - "How do you set the `MIKE_VERSION` variable and create the appropriate modulefile directory for MIKE 2026?"
  - "Why is a fresh login (or reinitialization) necessary for the newly created module to be recognized by `module` commands?"
  - "What is the purpose of setting the `I_MPI_PMI_LIBRARY` environment variable to `/opt/software/slurm/lib/libpmi2.so`?"
  - "Which modules are loaded at the start of the script, and why are they needed for MIKE 2022?"
  - "How does the script modify the `PATH` variable, and which directory is being prepended?"
  - "How can you activate a specific MIKE version module in a job or login session?"
  - "What command and file are used to configure the MIKE license according to the instructions?"
  - "Which modules, environment variables, and commands are included in the example SLURM job script for running MIKE?"
  - "What is the purpose of setting `OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}` in the first script?"
  - "How does the `#SBATCH` configuration in the MIKE 2023 script allocate computational resources for the job?"
  - "Which modules are loaded in the MIKE 2023 script, and what role do they play in running the job?"
  - "What is the purpose of setting `OMP_NUM_THREADS` with `${SLURM_CPUS_PER_TASK:-1}` in both job scripts?"
  - "How does the MIKE 2022 script create and utilize the `machinefile.$SLURM_JOBID` for MPI execution?"
  - "What are the key differences in the SLURM directives and execution commands between the FemEngineHD and MIKE 2022 job scripts?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[MIKE powered by DHI](https://www.mikepoweredbydhi.com/) is a hydraulic and hydrological modelling software package.

## License Requirements
MIKE is a commercial product and each user needs to supply their own license.

In order for you to use it on our HPC clusters, you will need to contact MIKE Customer Care at: [mike@dhigroup.com](mailto:mike@dhigroup.com) and confirm that you have
* an *internet license*, and
* a download link for the *Linux version* of MIKE.

## Installation

You need to download the installation archives for Linux.

The following instructions assume that the installation archives are in one Zip-file (MIKE 2025 and newer) or three `*.tgz` files (MIKE 2024 and older):

=== "MIKE 2026"
    * `MIKE_Zero_2026_rhel9.zip` This file contains:
        * `MIKE_Common_2026_rhel9.tgz`
        * `MIKE_Zero_2026_Examples.tgz`
        * `MIKE_Zero_2026_Prerequisites.tgz` (not needed)
        * `MIKE_Zero_2026_rhel9.tgz`
        * `MIKE_Zero_2026_Tools_rhel9.tgz`
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

=== "MIKE 2024, 2025 and 2026"
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

=== "MIKE 2026"
    ```bash
    export MIKE_TGZ="$HOME/scratch/MIKE_TGZ"
    export MIKE_HOME="$HOME/MIKE/2026"
    
    cd $MIKE_TGZ
    unzip -j  MIKE_Zero_2026_rhel9.zip
    tar -xzf MIKE_Common_2026_rhel9.tgz
    tar -xzf MIKE_Zero_2026_rhel9.tgz
    tar -xzf MIKE_Zero_2026_Tools_rhel9.tgz
    tar -xzf MIKE_Zero_2026_Examples.tgz
    
    cd $MIKE_TGZ/MIKE_Common_2026_rhel9
    sed -i 's/ cp -rp / cp -r /' install.sh
    sh install.sh --eula --install-path "$MIKE_HOME"
    cd $MIKE_TGZ/MIKE_Zero_2026_rhel9
    sed -i 's/ cp -rp / cp -r /' install.sh
    sh install.sh --eula --install-path "$MIKE_HOME"
    cd $MIKE_TGZ/MIKE_Zero_2026_Tools_rhel9
    sed -i 's/ cp -rp / cp -r /' install.sh
    sh install.sh --eula --install-path "$MIKE_HOME"
    cd $MIKE_TGZ/MIKE_Zero_2026_Examples
    sed -i 's/ cp -rp / cp -r /' install.sh
    sh install.sh --eula --install-path "$MIKE_HOME"
    
    module load StdEnv/2023 intel/2023.2.1 intelmpi/2021.9.0
    setrpaths.sh --path "$MIKE_HOME/bin"  --add_origin  \
        --add_path="$EBROOTIMPI/mpi/latest/lib/release:$EBROOTIMPI/mpi/latest/lib"
    ```
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

### Other Versions

The instructions above assume specific filenames for the installation archives. When installing minor updates released in the same year, the filenames for the archives (e.g. in `tar -xzf MIKE_Zero_2023_rhel7_22.11.05.tgz`), as well as the directory names (e.g. in `cd $MIKE_TGZ/MIKE_Zero_2023_rhel7_22.11.05`) need to be adjusted accordingly. Future major releases of MIKE may use a newer version of Intel MPI, so the above instructions may need to be adapted accordingly. Try a module of the Intel MPI library with a matching Major version (i.e. year).

Essentially the above instructions follow the official installation procedure with the exception that the installation of `MIKE_Zero_*_Prerequisites.tgz` (Intel MPI library) is skipped and a matching module is loaded instead. Furthermore the `setrpaths.sh` script is used to [patch the installed binaries](../getting-started/installing_software_in_your_home_directory.md#installing-binary-packages) to make them compatible with our software stack.

If you run into problems adapting the recipe for newer versions of MIKE, contact our [Technical support](../support/technical_support.md).

### Create a Module

Paste these commands into your terminal to create an environment module for MIKE. Make sure to adjust the version (e.g. "2025") to match the version you have installed. Also adjust the version of the `intelmpi` and `intel` modules to match what you had loaded during the installation. After running the commands below, do a fresh login to have the newly created environment module become visible to "module" commands or run `module use $HOME/modulefiles`.

=== "MIKE 2026"
    ```bash
    export MIKE_VERSION=2026
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

=== "MIKE 2026"
    ```bash
    module load StdEnv/2023 mike/2026
    ```
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

### Configure the License

From MIKE Customer Care you will have instructions like this for configuring your license:
```bash
licconfig set --type=internet --iuser=user@example.com --ipassword=my-password
```
This normally needs to be done only once whenever you get a new license or license code. The license information will be stored in a file `~/.config/DHI/license/NetLmLcwConfig.xml`.

## Example Job Script

=== "MIKE 2026"
    ```bash --job_mike_2026_CPU.sh
    #!/bin/bash
    #SBATCH --nodes=1
    #SBATCH --ntasks=8
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=4000M
    #SBATCH --time=00:20:00
    
    module load  StdEnv/2023  intel/2023.2.1  intelmpi/2021.9.0  mike/2026
    export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}
    
    engine="FemEngineHD"
    model="my_model.m3fm"
    
    srun $engine $model
    ```
=== "MIKE 2025"
    ```bash --job_mike_2025_CPU.sh
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
    ```bash --job_mike_2024_CPU.sh
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
    ```bash --job_mike_2023_CPU.sh
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
    ```bash --job_mike_2022_CPU.sh
    #!/bin/bash
    #SBATCH --nodes=1
    #SBATCH --ntasks=8
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=4000M
    #SBATCH --time=00:20:00
    
    module load StdEnv/2020  intel/2020.1.217  intelmpi/2019.7.217  mike/2022
    export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}
    slurm_hl2hl.py --format MPIHOSTLIST > machinefile.$SLURM_JOBID
    
    engine="FemEngineHD"
    model="my_model.m3fm"
    
    mpirun -machinefile machinefile.$SLURM_JOBID $engine $model