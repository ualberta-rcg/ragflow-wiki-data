---
title: "MIKE/en"
slug: "mike"
lang: "en"

source_wiki_title: "MIKE/en"
source_hash: "84958b1fe327a48a758e34e26a348a83"
last_synced: "2026-10-25T00:54:39.630071+00:00"
last_processed: "2026-10-25T01:38:54.641021+00:00"

tags:
  - software

keywords:
  - "environment module creation"
  - "mpirun -machinefile"
  - "internet license"
  - "Intel MPI module"
  - "license-server 127.0.0.1"
  - "job_mike_2026_CPU.sh"
  - "MIKE_Zero_2026_rhel9"
  - "add_path"
  - "Simulation"
  - "MIKE Zero installation"
  - "MIKE_TGZ"
  - "tar -xzf"
  - "setrpaths.sh"
  - "modulefile"
  - "module load StdEnv/2020"
  - "srun"
  - "EBROOTIMPI"
  - "MIKE hydraulic and hydrological modeling"
  - "--eula"
  - "MIKE"
  - "Linux version"
  - "sed -i 's/ cp -rp / cp -r /'"
  - "licconfig set"
  - "hydrological modeling"
  - "install.sh"
  - "hydraulic and hydrological modeling"
  - "SBATCH --nodes=1"
  - "Finite Elements"
  - "install.sh installation script"
  - "SBATCH --time=00:20:00"
  - "hydraulic modeling"
  - "DHI group"
  - "I_MPI_PMI_LIBRARY"
  - "my_model.m3fm"
  - "setrpaths.sh script"
  - "MIKE 2026"
  - "depends_on"
  - "intelmpi module"
  - "module load StdEnv/2023 intel/2023.2.1 intelmpi/2021.9.0"
  - "OMP_NUM_THREADS"
  - "MIKE_HOME"
  - "FemEngineHD"
  - "FEM"
  - "module load"

questions:
  - "What license type and contact information are required to run MIKE on the HPC clusters?"
  - "Which Intel and Intel MPI modules must be loaded for each MIKE version before installation, and how do they differ?"
  - "What are the step‑by‑step commands to extract, install, and patch the MIKE 2026 version, including handling of the zip and tgz files?"
  - "What is the purpose of the `sed -i 's/ cp -rp / cp -r /' install.sh` command in each MIKE version installation block?"
  - "Which environment modules are loaded before executing `setrpaths.sh`, and why are they needed?"
  - "How does the installation procedure differ among the MIKE 2025, MIKE 2024, and MIKE 2023 versions shown in the script?"
  - "What is the purpose of extracting the four MIKE tar.gz files with the `tar -xzf` commands?"
  - "Why does the script use `sed -i 's/ cp -rp / cp -r /' install.sh` to modify the copy command before installation?"
  - "What roles do the variables `$MIKE_TGZ` and `$MIKE_HOME` play in the directory navigation and installation steps?"
  - "What is the purpose of the `--add_origin` and `--add_path` options in the `path` command?"
  - "Which directories are assigned to `MIKE_HOME` and `MIKE_TGZ`, and what roles do they play in the setup?"
  - "Which tar.gz files are extracted with `tar -xzf`, and why are they needed for the MIKE 2023 installation?"
  - "What commands are needed to extract and install the MIKE Zero 2023 (or 2022) core, tools, and examples packages on a RHEL 7 system?"
  - "How should the installation procedure be modified for minor updates or future major releases that use different Intel MPI versions?"
  - "What are the steps to create a custom environment module for a specific MIKE version (e.g., 2026) after the software has been installed?"
  - "What is the purpose of the generated `.lua` module files for each MIKE version?"
  - "Which software modules are specified as dependencies for the different MIKE versions, and how do these dependencies change across versions?"
  - "What environment variables and path modifications are configured by the module files for MIKE?"
  - "What is the purpose of the generated `${MIKE_VERSION}.lua` modulefile in the `$HOME/modulefiles/mike/` directory?"
  - "Which metadata fields are defined in the modulefile for MIKE ${MIKE_VERSION}, and what information do they contain?"
  - "How does the script determine the user's home directory, and what fallback is used if the `HOME` environment variable is not set?"
  - "What is the purpose of the modulefile shown in the text?"
  - "Which version of MIKE is referenced by the `${MIKE_VERSION}` variable in the script?"
  - "What metadata (keywords, URL, description) does the modulefile provide through the `whatis` commands?"
  - "How can you activate a specific MIKE version module in a job or login session?"
  - "Where should the MIKE license configuration be stored and what command is used to set it up?"
  - "What are the essential steps and commands included in the example SLURM job script for running a MIKE model?"
  - "What modules and environment variables are loaded and set before executing the FemEngineHD engine?"
  - "How many nodes, tasks, and CPUs per task are requested in the SLURM directives of the MIKE 2022 job script?"
  - "Which engine and model are specified for execution by the `srun` command in the script?"
  - "What does the “#SBATCH --time=00:20:00” directive specify for the job?"
  - "How is the number of OpenMP threads set in the script, and what variable does it depend on?"
  - "Which command generates the machinefile that mpirun later uses, and how is that file referenced?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[MIKE powered by DHI](https://www.mikepoweredbydhi.com/) is a hydraulic and hydrological modelling software package.

## License requirements
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
    module load StdEnv/2020 intel/2021.2.0 intelmpi/2021.2.0
    ```

=== "MIKE 2022"
    ```bash
    module load StdEnv/2020 intel/2020.1.217 intelmpi/2019.7.217
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
    setrpaths.sh --path "$MIKE_HOME/bin" --add_origin \
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
    setrpaths.sh --path "$MIKE_HOME/bin" --add_origin \
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
    setrpaths.sh --path "$MIKE_HOME/bin" --add_origin \
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

    module load StdEnv/2020 intel/2021.2.0 intelmpi/2021.2.0
    setrpaths.sh --path "$MIKE_HOME/bin" --add_origin \
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
    setrpaths.sh --path "$MIKE_INST_DIR/bin" --add_origin \
        --add_path="$EBROOTIMPI/intel64/lib/release:$EBROOTIMPI/intel64/lib"
    ```

### Other versions

!!! tip "Adapting to other versions"
    The instructions above assume specific filenames for the installation archives. When installing minor updates released in the same year, the filenames for the archives (e.g., in `tar -xzf MIKE_Zero_2023_rhel7_22.11.05.tgz`), as well as the directory names (e.g., in `cd $MIKE_TGZ/MIKE_Zero_2023_rhel7_22.11.05`) need to be adjusted accordingly. Future major releases of MIKE may use a newer version of Intel MPI, so the above instructions may need to be adapted accordingly. Try a module of the Intel MPI library with a matching Major version (i.e., year).

    Essentially, the above instructions follow the official installation procedure with the exception that the installation of `MIKE_Zero_*_Prerequisites.tgz` (Intel MPI library) is skipped and a matching module is loaded instead. Furthermore, the `setrpaths.sh` script is used to [patch the installed binaries](../getting-started/installing_software_in_your_home_directory.md#installing-binary-packages) to make them compatible with our software stack.

    If you run into problems adapting the recipe for newer versions of MIKE, contact our [Technical support](../support/technical_support.md).

### Create a module

!!! note "Module file adjustments"
    Paste these commands into your terminal to create an environment module for MIKE. Make sure to adjust the version (e.g., "2025") to match the version you have installed. Also adjust the version of the `intelmpi` and `intel` modules to match what you had loaded during the installation. After running the commands below, do a fresh login to have the newly created environment module become visible to "module" commands or run `module use $HOME/modulefiles`.

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

### Configure the license

From MIKE Customer Care you will have instructions like this for configuring your license:
```bash
licconfig set --type=internet --iuser=user@example.com --ipassword=my-password
```
This normally needs to be done only once whenever you get a new license or license code. The license information will be stored in a file `~/.config/DHI/license/NetLmLcwConfig.xml`.

## Example job script

=== "MIKE 2026"
    ```bash linenums="1" title="job_mike_2026_CPU.sh"
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
    ```bash linenums="1" title="job_mike_2025_CPU.sh"
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
    ```bash linenums="1" title="job_mike_2024_CPU.sh"
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
    ```bash linenums="1" title="job_mike_2023_CPU.sh"
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
    ```bash linenums="1" title="job_mike_2022_CPU.sh"
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