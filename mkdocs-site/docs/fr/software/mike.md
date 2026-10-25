---
title: "MIKE/fr"
slug: "mike"
lang: "fr"

source_wiki_title: "MIKE/fr"
source_hash: "9b2ef4080d8402dbb73c905a6254cca6"
last_synced: "2026-10-25T00:54:39.630071+00:00"
last_processed: "2026-10-25T01:39:41.999909+00:00"

tags:
  - software

keywords:
  - "installation Linux"
  - "module load StdEnv/2023"
  - "license-server 127.0.0.1"
  - "Simulation"
  - "MIKE_TGZ"
  - "licence internet"
  - "tar -xzf"
  - "mike/2023"
  - "install.sh --eula"
  - "setrpaths.sh"
  - "MIKE 2022"
  - "mike/2024"
  - "Intel MPI"
  - "intelmpi"
  - "licconfig"
  - "SLURM"
  - "MIKE"
  - "module d'environnement"
  - "Version"
  - "unzip"
  - "versions MIKE 2024‑2026"
  - "MIKE du groupe DHI"
  - "Créer un module"
  - "MIKE_Zero_2023"
  - "install.sh"
  - "Finite Elements"
  - "module intelmpi"
  - "module load intelmpi"
  - "hydraulic modeling"
  - "DHI group"
  - "my_model.m3fm"
  - "OMP_NUM_THREADS"
  - "FemEngineHD"
  - "MIKE_HOME"
  - "intelmpi/2021.9.0"
  - "modifier la version"
  - "FEM"
  - "module load"
  - "mpirun"

questions:
  - "Quelles sont les conditions de licence requises pour pouvoir utiliser MIKE sur les grappes de calcul du groupe DHI ?"
  - "Quels modules Intel (intel et intelmpi) doivent être chargés selon chaque version de MIKE (2022, 2023, 2024‑2026) avant l’installation ?"
  - "Comment créer le répertoire de travail, télécharger les archives et les extraire pour installer MIKE (par exemple pour la version 2026) ?"
  - "What is the purpose of using `sed -i 's/ cp -rp / cp -r /' install.sh` before running the installation scripts?"
  - "How are the environment variables `MIKE_TGZ` and `MIKE_HOME` set and applied for the different MIKE versions (2026, 2025, 2024, 2023)?"
  - "Which modules are loaded and why is `setrpaths.sh` executed after each MIKE installation?"
  - "Quel rôle jouent les variables d’environnement `MIKE_TGZ` et `MIKE_HOME` dans ce script ?"
  - "Quelles commandes sont utilisées pour décompresser les différents fichiers d’archive MIKE ?"
  - "Quel système d’exploitation (distribution et version) est visé par les archives MIKE présentées ?"
  - "What does the `install.sh` command do with the `--eula` and `--install-path \"$MIKE_HOME\"` options?"
  - "Which modules are loaded (`StdEnv/2023`, `intel/2023.2.1`, `intelmpi/2021.9.0`) and why are they needed before running `setrpaths.sh`?"
  - "How does the `setrpaths.sh` command configure the runtime library paths using `$MIKE_HOME/bin`, `$EBROOTIMPI/mpi/latest/lib/release`, and `$EBROOTIMPI/mpi/latest/lib`?"
  - "Quels sont les étapes principales pour installer MIKE Zero 2023 (et ses outils/exemples) sur un système RHEL 7 ?"
  - "Comment adapter les commandes d’installation lorsqu’on passe à une version mineure ou majeure différente de MIKE (noms d’archives, répertoires, modules MPI) ?"
  - "Quelles sont les instructions pour créer un module d’environnement personnalisé après l’installation de MIKE ?"
  - "Quelle commande devez‑vous exécuter après avoir créé les fichiers de module pour que le nouveau module d’environnement soit reconnu ?"
  - "Quels modules et quelles versions sont spécifiés comme dépendances dans les scripts de module pour chaque version de MIKE ?"
  - "Quelles variables d’environnement et quels chemins sont configurés dans le fichier de module pour définir le répertoire d’installation de MIKE et ajouter ses exécutables au PATH ?"
  - "Quelle commande doit‑on coller dans le terminal pour créer le module d’environnement ?"
  - "Comment faut‑il ajuster la version du module afin qu’elle corresponde à la version de MIKE installée ?"
  - "Pourquoi est‑il nécessaire de modifier également les versions des modules <code>intelmpi</code> et <code>intel</code> ?"
  - "What is the purpose of the MIKE software mentioned in the description?"
  - "Which modules and versions are specified as dependencies for this MIKE setup?"
  - "Which environment variable is being set for MPI, and what path does it point to?"
  - "Comment charger le module MIKE correspondant à la version souhaitée dans une session ou une tâche SLURM ?"
  - "Quelle commande doit‑on exécuter pour configurer la licence MIKE après réception des informations de licence ?"
  - "Quels sont les paramètres principaux du script d’exemple (nodes, ntasks, mémoire, temps, variables d’environnement) pour lancer un modèle MIKE avec srun ?"
  - "What computational resources (nodes, tasks, CPUs per task, memory per CPU, and time limit) are requested in the SLURM job script?"
  - "Which software modules are loaded in the script, and how is the OMP_NUM_THREADS environment variable configured?"
  - "How does the script invoke the FemEngineHD engine with the specified model file, and what is the name of that model file?"
  - "What are the differences in module versions and execution commands between the MIKE 2023 and MIKE 2022 job scripts?"
  - "How does each script configure the number of OpenMP threads for running FemEngineHD?"
  - "What SLURM resource parameters (nodes, tasks, CPUs per task, memory, time) are specified in the provided job scripts?"

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

!!! important "Conditions de licence"
    Pour pouvoir l'utiliser sur nos grappes de calcul, vous devez contacter le service à la clientèle de MIKE à [mike@dhigroup.com](mailto:mike@dhigroup.com) et confirmer que vous avez :
    * une *licence internet* et
    * un lien téléchargé pour la *version Linux* de MIKE.

## Installation

Vous devez télécharger les archives d'installation pour Linux.

Les directives suivantes supposent que les archives d'installation sont dans un fichier Zip (MIKE 2025 et plus récentes) ou dans trois fichiers `*.tgz` (MIKE 2024 et moins récentes).

=== "MIKE 2026"
    * `MIKE_Zero_2026_rhel9.zip` Ce fichier contient :
        * `MIKE_Common_2026_rhel9.tgz`
        * `MIKE_Zero_2026_Examples.tgz`
        * `MIKE_Zero_2026_Prerequisites.tgz` (non requis)
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

1. Créez le répertoire `~/scratch/MIKE_TGZ` pour y téléverser les archives d'installation.

2. MIKE a été compilé avec la bibliothèque Intel MPI, donc chargez le module apparié `intelmpi`.

=== "MIKE 2024, 2025 et 2026"
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

3. Lancez les commandes suivantes, selon la version de MIKE.
Ceci fera l'extraction des archives. Exécutez les scripts d'installation *install.sh* pour chaque composant,
ensuite [modifiez les binaires](../getting-started/installing_software_in_your_home_directory.md#installer-des-paquets-binaires) pour qu'ils trouvent les bibliothèques dynamiques d'Intel MPI.

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

Activez ce module dans chaque tâche ou dans chaque session de connexion avec

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

### Configurer la licence

Le service à la clientèle de MIKE vous enverra des directives comme ceci pour configurer votre licence.
```bash
licconfig set --type=internet --iuser=user@example.com --ipassword=my-password
```
Ceci se fait habituellement une seule fois quand vous recevez une nouvelle licence ou un nouveau code de licence. Les renseignements sur la licence sont enregistrés dans le fichier `~/.config/DHI/license/NetLmLcwConfig.xml`.

## Exemple de script pour une tâche

=== "MIKE 2026"
    ```bash title="job_mike_2026_CPU.sh"
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