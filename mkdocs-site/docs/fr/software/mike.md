---
title: "MIKE/fr"
slug: "mike"
lang: "fr"

source_wiki_title: "MIKE/fr"
source_hash: "a3bfeda37f90dd4476028bc715b3b305"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:46:27.838351+00:00"

tags:
  - software

keywords:
  - "paquets binaires"
  - "installation Linux"
  - "--license-server"
  - "sed"
  - "SBATCH"
  - "installation"
  - "Simulation"
  - "licence internet"
  - "licence"
  - "script pour une tâche"
  - "bash"
  - "--install-path"
  - "hydraulic and hydrological modeling"
  - "MIKE_Zero_2022"
  - "MIKE_Zero_2025_rhel9"
  - "Progiciel MIKE"
  - "module"
  - "MIKE_Zero"
  - "bibliothèque Intel MPI"
  - "grappes de calcul"
  - "module load"
  - "MIKE"
  - "module d'environnement"
  - "modélisation hydraulique"
  - "MIKE_HOME"
  - "intelmpi"
  - "configuration"
  - "install-path"
  - "OMP_NUM_THREADS"
  - "software package"
  - "Finite Elements"
  - "setrpaths.sh"
  - "FemEngineHD"
  - "install.sh"

questions:
  - "À quoi sert le progiciel MIKE et quel est son domaine d'application principal ?"
  - "Quelles sont les exigences spécifiques en matière de licence pour pouvoir utiliser MIKE sur les grappes de calcul ?"
  - "Quelles sont les étapes de préparation et d'installation requises pour déployer les archives Linux de MIKE ?"
  - "Why is the `sed` command repeatedly used to change `cp -rp` to `cp -r` within the installation scripts?"
  - "What specific configuration arguments, such as the installation path and license server, are provided to the `install.sh` scripts during execution?"
  - "Which distinct components or directories of the MIKE Zero 2025 software suite are being navigated to and processed in this sequence?"
  - "What are the common command-line arguments used when executing the install scripts for the different MIKE software versions?"
  - "What specific modification is made to the install.sh scripts using the `sed` command during the MIKE 2024 and 2025 installations?"
  - "Which environment modules and path configurations must be loaded and set after the MIKE software extraction and installation?"
  - "What are the specific shell commands and flags used to install the MIKE Zero 2022 Tools and Examples?"
  - "Which environment modules must be loaded to support the MIKE Zero 2022 software?"
  - "What is the purpose of executing the setrpaths.sh script on the installation's binary directory?"
  - "Comment doit-on ajuster les noms de fichiers et les directives MPI lors de l'installation d'une version différente du logiciel MIKE ?"
  - "Quelle est la méthode recommandée pour gérer la bibliothèque Intel MPI et rendre les paquets binaires compatibles avec la pile logicielle au lieu d'utiliser les prérequis officiels ?"
  - "Quelles sont les étapes et les commandes requises pour créer, configurer et activer un module d'environnement personnalisé pour MIKE ?"
  - "Comment activer le module MIKE pour une tâche ou une session de connexion selon la version choisie ?"
  - "Comment configurer la licence internet de MIKE et dans quel fichier ces informations sont-elles enregistrées ?"
  - "Quels éléments et commandes doivent être inclus dans un script SLURM pour soumettre correctement une tâche MIKE ?"
  - "What is the primary purpose and description of the MIKE software package?"
  - "What specific software dependencies and environment variables must be loaded or set to run this module?"
  - "How does the configuration script determine the root directory path for the MIKE installation?"
  - "What Slurm resource allocations, such as the number of tasks, memory per CPU, and time limit, are specified for this job?"
  - "Which environment modules must be loaded to properly set up the environment for the MIKE 2025 simulation?"
  - "What are the specific names of the engine and the model file being executed by the script?"
  - "How does the execution command differ between MIKE 2022 and the newer versions (2023 and 2024) in the provided SLURM scripts?"
  - "Which specific environment modules need to be loaded to run the MIKE 2024 version compared to the older versions?"
  - "What are the standard SLURM resource allocations, such as memory and time limits, defined across all three job scripts?"
  - "How does the execution command differ between MIKE 2022 and the newer versions (2023 and 2024) in the provided SLURM scripts?"
  - "Which specific environment modules need to be loaded to run the MIKE 2024 version compared to the older versions?"
  - "What are the standard SLURM resource allocations, such as memory and time limits, defined across all three job scripts?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Le progiciel [MIKE du groupe DHI](https://www.mikepoweredbydhi.com/) sert à la modélisation hydraulique et hydrologique.

## Licence

MIKE est un produit commercial et vous devez avoir votre propre licence.

Pour pouvoir l'utiliser sur nos grappes de calcul, vous devez contacter le service à la clientèle de MIKE à [mike@dhigroup.com](mailto:mike@dhigroup.com) et confirmer que vous avez
* une *licence internet* et
* un lien téléchargé pour la *version Linux* de MIKE.

## Installation

Vous devez télécharger les archives d'installation pour Linux.

Les directives suivantes supposent que les archives d'installation sont dans un fichier Zip (MIKE 2025 et plus récentes) ou dans trois fichiers `*.tgz` (MIKE 2024 et moins récentes).

```tabs
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
```

1. Créez le répertoire `~/scratch/MIKE_TGZ` pour y téléverser les archives d'installation.

2. MIKE a été compilé avec la bibliothèque Intel MPI, donc chargez le module apparié `intelmpi`.

```tabs
=== "MIKE 2024 et 2025"
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
```

3. Lancez les commandes suivantes, selon la version de MIKE. Ceci fera l'extraction des archives. Exécutez les scripts d'installation *install.sh* pour chaque composant, ensuite [modifiez les binaires](../getting-started/installing_software_in_your_home_directory.md#installer-des-paquets-binaires) pour qu'ils trouvent les bibliothèques dynamiques d'Intel MPI.

```tabs
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
```

### Autres versions

Les instructions ci-dessus supposent que les archives d'installation ont des noms de fichiers spécifiques. À l'installation de versions mineures publiées la même année, les noms des fichiers pour les archives (par exemple dans `tar -xzf MIKE_Zero_2023_rhel7_22.11.05.tgz`), 
et les noms des répertoires (par exemple dans `cd $MIKE_TGZ/MIKE_Zero_2023_rhel7_22.11.05`) ont besoin d'être ajustés en conséquence.
Les prochaines versions majeures de MIKE pourraient utiliser des versions différentes de MPI et il faudrait alors modifier les directives en conséquence. Essayez un module de bibliothèque Intel MPI avec une version majeure correspondante (année).

Les directives ci-dessus suivent la procédure d'installation officielle, à l'exception du fait que l'installation de `MIKE_Zero_*_Prerequisites.tgz` (bibliothèque Intel MPI) est omise et qu'un module correspondant est chargé à sa place. De plus, le script `setrpaths.sh` est utilisé pour [installer des paquets binaires](../getting-started/installing_software_in_your_home_directory.md#installer-des-paquets-binaires) afin de les rendre compatibles avec notre pile logicielle.

Si vous avez des difficultés à adapter la recette pour les versions plus récentes de MIKE, écrivez au [soutien technique](../support/technical_support.md).

### Créer un module

Collez ces commandes dans votre terminal pour créer un module d'environnement pour MIKE.
Assurez-vous de modifier la version (par exemple 2025) pour correspondre à la version que vous avez installée.
Modifiez aussi la version des modules `intelmpi` et `intel` pour correspondre à ce que vous avez chargé pendant l'installation.
Après avoir exécuté les commandes ci-dessous, connectez-vous de nouveau pour que le nouveau module d'environnement soit visible par les commandes de modules; vous pouvez aussi exécuter `module use $HOME/modulefiles`.

```tabs
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
```

Activez ce module dans chaque tâche ou dans chaque session de connexion avec

```tabs
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
```

### Configurer la licence

Le service à la clientèle de MIKE vous enverra des directives comme ceci pour configurer votre licence.
```bash
licconfig set --type=internet --iuser=user@example.com --ipassword=my-password
```
Ceci se fait habituellement une seule fois quand vous recevez une nouvelle licence ou un nouveau code de licence.
Les renseignements sur la licence sont enregistrés dans le fichier `~/.config/DHI/license/NetLmLcwConfig.xml`.

## Exemple de script pour une tâche

```tabs
=== "MIKE 2025"
    ```bash title="job_mike_2025_CPU.sh"
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
    ```bash title="job_mike_2024_CPU.sh"
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
    ```bash title="job_mike_2023_CPU.sh"
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
    ```bash title="job_mike_2022_CPU.sh"
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
    ```