---
title: "LAMMPS/fr"
slug: "lammps"
lang: "fr"

source_wiki_title: "LAMMPS/fr"
source_hash: "1d34dd8f754e308539715fcb3e86f8b3"
last_synced: "2026-04-18T23:39:30.217451+00:00"
last_processed: "2026-04-19T00:56:08.419862+00:00"

tags:
  - software
  - biomolecularsimulation

keywords:
  - "simulation biomoléculaire"
  - "dynamique moléculaire"
  - "simulation"
  - "cmake"
  - "calcul des paires"
  - "performance"
  - "documentation"
  - "exécutable"
  - "CMake"
  - "paquets"
  - "fichiers d'entrée"
  - "interactions de paires"
  - "modules"
  - "torch"
  - "champs de force"
  - "lammps-mace"
  - "Job Submission"
  - "pip install"
  - "PyTorch"
  - "tâches MPI"
  - "efficacité basse"
  - "temps de communication"
  - "MACE"
  - "compilation"
  - "LAMMPS"

questions:
  - "Qu'est-ce que le logiciel LAMMPS et quelles sont ses méthodes de parallélisation ?"
  - "Quels sont les principaux domaines d'application et types de champs de force pris en charge par LAMMPS ?"
  - "Comment les utilisateurs peuvent-ils gérer les différentes versions, exécutables et paquets de LAMMPS sur les grappes de calcul ?"
  - "Combien de paquets différents peuvent être activés ou désactivés lors de la compilation du programme ?"
  - "Est-il possible d'activer la totalité des paquets disponibles dans un seul et même exécutable ?"
  - "Quelle est la cause la plus probable à vérifier si une simulation ne fonctionne pas avec un module spécifique ?"
  - "Comment peut-on déterminer la liste des paquets activés ou non activés pour un module LAMMPS spécifique ?"
  - "Quels sont les différents types de scripts de tâche proposés en exemple pour exécuter une simulation LAMMPS ?"
  - "Pourquoi l'augmentation du nombre de processeurs pour un petit système de particules entraîne-t-elle une baisse de l'efficacité du CPU ?"
  - "Quelles sont les deux étapes de la simulation qui consomment la plus grande proportion du temps total selon l'analyse de performance ?"
  - "Comment le temps de communication évolue-t-il par rapport au temps de calcul des paires lorsque le nombre de cœurs augmente de 1 à 16 ?"
  - "Quelles sont les étapes et commandes principales requises pour configurer et compiler MACE dans LAMMPS avec PyTorch dans un environnement virtuel ?"
  - "Pourquoi l'efficacité de la simulation de ce système de 4000 particules sur 12 cœurs est-elle considérée comme très basse ?"
  - "Comment le temps d'exécution se répartit-il entre le calcul des interactions de paires et la communication entre les processeurs ?"
  - "Quelle est la cause principale expliquant la proportion si importante du temps dédié à la communication ?"
  - "What specific modules and Python packages are required to configure and build MACE with GPU support?"
  - "What are the CMake commands and flags used to configure, compile, and install the LAMMPS-MACE integration?"
  - "How do the SLURM job submission scripts differ when running the compiled LAMMPS-MACE binary on a CPU versus a GPU?"
  - "What version of PyTorch is required to be installed before configuring MACE?"
  - "Which CMake flags are necessary to enable MPI and the ML-MACE package during the configuration step?"
  - "What is the designated installation directory for the LAMMPS-MACE build according to the configuration command?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Page enfant de [Simulation biomoléculaire](molecular-sim/biomolecular_simulation.md)*

## Généralités

LAMMPS (pour *large-scale atomic/molecular massively parallel simulator*) est un logiciel classique de dynamique moléculaire distribué par [Sandia National Laboratories](http://www.sandia.gov/) du ministère de l’Énergie des États-Unis.

*   Site web du projet : <http://lammps.sandia.gov/>
*   [Documentation](http://lammps.sandia.gov/doc/Manual.html)
*   [Liste de messagerie](http://lammps.sandia.gov/mail.html)

La parallélisation se fait avec [MPI](mpi.md) et [OpenMP](../programming/openmp.md), et LAMMPS peut être exécuté sur [GPU](../running-jobs/using_gpus_with_slurm.md).

## Champs de force

Les champs de force disponibles sont listés à la section [Interatomic potentials](https://lammps.sandia.gov/doc/Intro_features.html#ff) du site web, classés selon leur forme fonctionnelle (soit par paire, N corps, etc.). LAMMPS pouvant traiter un grand nombre de champs de force, il peut être utilisé pour la modélisation dans plusieurs domaines d’application, par exemple :

*   **Biomolécules** : CHARMM, AMBER, OPLS, COMPASS (classe 2), coulombiques longue portée via PPPM, dipôles de moment, etc.
*   **Polymères** : liaison d’atomes, union d’atomes, gros grains (chaînes globulaires FENE), rupture de liaison, etc.
*   **Matériaux** : EAM et MEAM pour les métaux, Buckingham, Morse, Yukawa, Stillinger-Weber, Tersoff, EDIP, COMB, SNAP, etc.
*   **Réactions** : AI-REBO, REBO, ReaxFF, eFF
*   **Échelle mésoscopique** : granulaire, DPD, Gay-Berne, colloïdal, péridynamiques, DSMC, etc.

Les potentiels peuvent aussi être combinés dans des systèmes hybrides, par exemple eau sur métal, interfaces polymère/semi-conducteur, colloïdes en solution, etc.

## Versions et paquets

Pour connaître les versions disponibles, lancez `module spider lammps` (voir [Utiliser des modules](../programming/utiliser_des_modules.md)).

Les numéros de version de LAMMPS comprennent la date de sortie au format AAAAMMJJ. Exécutez

```bash
module avail lammps
```

pour connaître les versions installées et sélectionner celle que vous voulez utiliser.

Il peut y avoir plusieurs modules pour une même version. Par exemple, la version du 31 mars 2017 a les trois modules suivants :

*   `lammps/20170331` développé sous MPI
*   `lammps-omp/20170331` USER-OMP (compatible OpenMP)
*   `lammps-user-intel/20170331` USER-INTEL

Ces versions fonctionnent aussi avec GPU; le module [CUDA](../programming/cuda.md) doit être chargé avant le module LAMMPS.

```bash
module load cuda
module load lammps-omp/20170331
```

Le nom de l’exécutable peut être différent selon la version. Toutes les versions installées sur nos grappes ont le lien symbolique `lmp`; vous pouvez donc exécuter LAMMPS en faisant appel à `lmp` peu importe le module que vous utilisez.

Pour connaître le nom original de l’exécutable d’un module en particulier, faites lister les fichiers dans le répertoire `${EBROOTLAMMPS}/bin` avec, par exemple

```bash
module load lammps-omp/20170331
ls ${EBROOTLAMMPS}/bin/
```

où l’exécutable est `lmp_icc_openmpi` et `lmp` est le lien symbolique associé.

Il existe différents modules pour la même version, dépendant des paquets qui sont inclus. Les versions de LAMMPS les plus récentes comprennent environ 60 paquets différents qui peuvent être activés ou désactivés à la compilation du programme. Ce ne sont pas tous les paquets qui peuvent être activés dans un même exécutable. Consultez la [documentation sur les paquets](https://lammps.sandia.gov/doc/Packages.html). Si votre simulation ne fonctionne pas avec un module, il est possible qu'un des paquets nécessaires n'ait pas été activé.

Pour certains modules LAMMPS, nous fournissons le fichier `list-packages.txt` qui liste les paquets *Supportés* et *Non supportés*. Une fois que vous avez chargé un module, lancez `cat ${EBROOTLAMMPS}/list-packages.txt` pour en connaître le contenu.

Si `list-packages.txt` est introuvable, vous pourriez être capable de déterminer quels sont les paquets disponibles en ouvrant le fichier de recette [EasyBuild](../programming/easybuild.md) avec `$EBROOTLAMMPS/easybuild/LAMMPS*.eb`. Les paquets disponibles se trouvent dans le bloc `general_packages`.

## Exemples de fichiers d'entrée

Le fichier ci-dessous peut être utilisé avec l’un ou l’autre des scripts de tâche donnés en exemple.

=== "Fichier en entrée"

    ```txt
    # 3d Lennard-Jones melt

    units           lj
    atom_style      atomic

    lattice         fcc 0.8442
    region          box block 0 15 0 15 0 15
    create_box      1 box
    create_atoms    1 box
    mass            1 1.0

    velocity        all create 1.44 87287 loop geom

    pair_style      lj/cut 2.5
    pair_coeff      1 1 1.0 1.0 2.5
    neighbor        0.3 bin
    neigh_modify    delay 5 every 1

    fix             1 all nve
    thermo          5
    run             10000
    write_data     config.end_sim

    # End of the Input file.
    ```

=== "Tâche séquentielle"

    ```bash
    #!/bin/bash

    #SBATCH --ntasks=1
    #SBATCH --mem-per-cpu=2500M
    #SBATCH --time=0-00:30

    module load StdEnv/2020 intel/2020.1.217 openmpi/4.0.3 lammps-omp/20210929

    lmp < lammps.in > lammps_output.txt
    ```

=== "Tâche MPI"

    ```bash
    #!/bin/bash

    #SBATCH --ntasks=4
    #SBATCH --mem-per-cpu=2500M
    #SBATCH --time=0-00:30 

    module load StdEnv/2020 intel/2020.1.217 openmpi/4.0.3 lammps-omp/20210929

    srun lmp < lammps.in > lammps_output.txt
    ```

## Performance

Dans le cas de simulations en dynamique moléculaire, le calcul des interactions par paires entre particules monopolise la majeure partie du temps CPU. LAMMPS utilise la méthode de décomposition des domaines pour répartir le travail aux processeurs disponibles en assignant à chacun une partie de la boîte de simulation. Il est nécessaire que les processeurs communiquent entre eux pendant le calcul des interactions entre particules. Pour un nombre déterminé de particules, plus le nombre de processeurs est élevé, plus il y a de parties à la boîte de simulation qui s’échangent de l’information. Ainsi, plus il y a de processeurs, plus longue est la durée du temps de communication, ce qui cause éventuellement la faible efficacité du CPU.

Avant d’exécuter des simulations pour des problèmes d’une certaine taille ou avec des boîtes à plusieurs parties, faites des tests pour voir l’impact du nombre de cœurs sur la performance du programme. Effectuez des tests courts avec un nombre différent de cœurs pour identifier le nombre de cœurs susceptible d’offrir la meilleure efficacité; les résultats demeurent cependant approximatifs.

### Durée de boucle pour 12 processus

Durée de boucle 15.4965 pour 12 processus de 25000 étapes avec 4000 atomes.
Performance : 696931.853 tau/jour, 1613.268 timesteps/s.
CPU utilisé à 90.2% avec 12 tâches MPI x 1 fil OpenMP.

Le tableau suivant montre la durée pour la simulation d’un système de 4000 particules avec 12 tâches MPI. En utilisant 12 cœurs, le système de 4000 atomes est réparti sur 12 petites boîtes et l’efficacité est très basse. Le calcul des interactions de paires occupe 46.45% du temps et la communication entre processeurs 44.5%. La proportion importante du temps de communication est due au fait qu’un si petit système utilise un grand nombre de petites boîtes.

| SECTION | durée minimale | durée moyenne | durée maximale | variation moyenne (%) | total (%) |
| :------ | :------------- | :------------ | :------------- | :-------------------- | :-------- |
| paires  | 6.6964         | 7.1974        | 7.9599         | 14.8                  | **46.45** |
| voisins | 0.94857        | 1.0047        | 1.0788         | 4.3                   | 6.48      |
| communication | 6.0595         | 6.8957        | 7.4611         | 17.1                  | **44.50** |
| sortie  | 0.01517        | 0.01589       | 0.019863       | 1.0                   | 0.10      |
| modification | 0.14023        | 0.14968       | 0.16127        | 1.7                   | 0.97      |
| autre   | --             | 0.2332        | --             | --                    | 1.50      |

Dans le dernier tableau, le temps de communication est comparé au temps de calcul des paires pour différents nombres de cœurs.

| Cœurs | Paires (2048 atomes) | Comm. (2048 atomes) | Paires (4000 atomes) | Comm. (4000 atomes) | Paires (6912 atomes) | Comm. (6912 atomes) | Paires (13500 atomes) | Comm. (13500 atomes) |
| :---- | :------------------- | :------------------ | :------------------- | :------------------ | :------------------- | :------------------ | :-------------------- | :------------------- |
| 1     | 73.68                | 1.36                | 73.70                | 1.28                | 73.66                | 1.27                | 73.72                 | 1.29                 |
| 2     | 70.35                | 5.19                | 70.77                | 4.68                | 70.51                | 5.11                | 67.80                 | 8.77                 |
| 4     | 62.77                | 13.98               | 64.93                | 12.19               | 67.52                | 8.99                | 67.74                 | 8.71                 |
| 8     | 58.36                | 20.14               | 61.78                | 15.58               | 64.10                | 12.86               | 62.06                 | 8.71                 |
| 16    | 56.69                | 20.18               | 56.70                | 20.18               | 56.97                | 19.80               | 56.41                 | 20.38                |

## MACE avec LAMMPS

### Compilation de MACE dans LAMMPS avec PyTorch

1.  À partir d'un nœud de connexion, clonez d'abord la branche `mace` :

    ```bash
    mkdir ~/lammps-mace
    cd $SCRATCH
    git clone --branch=mace --depth=1 https://github.com/ACEsuit/lammps && cd lammps
    git checkout 4d222cb # commit HEAD actuel de la branche
    ```

    Notez le *commit* pour référence future.

=== "CPU"

    2.  Chargez les modules requis pour configurer MACE et construire :
        ```bash
        module load python/3.14 gcc openmpi flexiblas cmake fftw eigen protobuf abseil flatbuffers opencv sleef xnnpack
        ```

    3.  Créez et activez un [environnement virtuel Python](python.md) :
        ```bash
        virtualenv --clear ~/lammps-mace/ENV && source ~/lammps-mace/ENV/bin/activate
        ```

    4.  Installez PyTorch dans cet environnement virtuel :
        ```bash
        pip install --no-index --upgrade pip
        pip install --no-index 'torch>=2.10.0'
        ```

    5.  Configurez MACE :
        ```bash
        cmake --fresh -S cmake -B _build -DBUILD_MPI=ON -DPKG_ML-MACE=ON -DCMAKE_PREFIX_PATH="$(python -c 'import torch; print(torch.utils.cmake_prefix_path)')" -DCMAKE_INSTALL_PREFIX=$HOME/lammps-mace -DCMAKE_SKIP_RPATH=ON
        ```

=== "GPU"

    2.  Chargez les modules requis pour configurer MACE et construire :
        ```bash
        module load python/3.14 gcc openmpi flexiblas cmake fftw eigen protobuf abseil flatbuffers cuda/12.9 cusparselt cudnn nccl magma opencv cudss sleef xnnpack
        ```
        Nous utilisons ici CUDA 12.9, car il correspond à la version avec laquelle PyTorch a été construit.

    3.  Créez et activez un [environnement virtuel Python](python.md) :
        ```bash
        virtualenv --clear ~/lammps-mace/ENV && source ~/lammps-mace/ENV/bin/activate
        ```

    4.  Installez PyTorch dans cet environnement virtuel :
        ```bash
        pip install --no-index --upgrade pip
        pip install --no-index 'torch>=2.10.0'
        ```

    5.  Configurez MACE :
        ```bash
        cmake --fresh -S cmake -B _build -DBUILD_MPI=ON -DPKG_ML-MACE=ON -DCMAKE_PREFIX_PATH="$(python -c 'import torch; print(torch.utils.cmake_prefix_path)')" -DCMAKE_INSTALL_PREFIX=$HOME/lammps-mace -DCMAKE_SKIP_RPATH=ON -DTORCH_CUDA_ARCH_LIST="9.0"
        ```

6.  Compilez et installez dans un répertoire local `lammps-mace` :

    ```bash
    cmake --build _build --parallel 4
    cmake --install _build/ --prefix=$HOME/lammps-mace
    ```

7.  Test rapide :

    ```bash
    deactivate
    module purge
    ~/lammps-mace/bin/lmp -h
    ```

### Exemples de soumission de tâches

=== "CPU"

    ```bash
    #!/bin/bash

    #SBATCH --job-name lammps-mace
    #SBATCH --account MY-ACCOUNT-CPU
    #SBATCH --nodes=1
    #SBATCH --ntasks=4
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=3500M
    #SBATCH --time=01:00:00
    #SBATCH --mail-type=FAIL

    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    srun $HOME/lammps-mace/bin/lmp -in in.lammps
    ```

=== "GPU"

    ```bash
    #!/bin/bash

    #SBATCH --job-name lammps-mace
    #SBATCH --account MY-ACCOUNT-GPU
    #SBATCH --nodes=1
    #SBATCH --ntasks=4
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=3500M
    #SBATCH --gpus=h100_1g.10gb:1
    #SBATCH --time=01:00:00
    #SBATCH --mail-type=FAIL

    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    srun $HOME/lammps-mace/bin/lmp -in in.lammps