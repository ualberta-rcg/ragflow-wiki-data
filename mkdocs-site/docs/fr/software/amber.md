---
title: "AMBER/fr"
slug: "amber"
lang: "fr"

source_wiki_title: "AMBER/fr"
source_hash: "a7fba9418904c7395a761b1990f4d225"
last_synced: "2026-04-10T14:10:18.226633+00:00"
last_processed: "2026-04-10T14:23:51.802150+00:00"

tags:
  - software
  - biomolecularsimulation

keywords:
  - "MPI parallèle"
  - "MPI"
  - "FlexiBLAS"
  - "Tâche QM/MM"
  - "SBATCH"
  - "modules"
  - "CPU"
  - "AmberTools"
  - "pmemd"
  - "MMPBSA parallèle"
  - "CUDA"
  - "openmpi"
  - "GPU A100"
  - "grappes"
  - "soumission de tâches"
  - "Amber-PMEMD"
  - "Amber"
  - "dynamique moléculaire"
  - "StdEnv"
  - "CUDA/11.4"
  - "Trillium"
  - "ambertools"
  - "H100 pris en charge"
  - "SANDER.QUICK"
  - "cuda"
  - "amber-pmemd"
  - "bibliothèques MKL"
  - "PMEMD"
  - "Performance et étalonnage"
  - "GPU H100"
  - "GPU"

questions:
  - "Qu'est-ce que le logiciel Amber et à quel type de simulations est-il principalement destiné ?"
  - "Quelles sont les différences principales entre les modules `amber`, `amber-pmemd` et `ambertools` fournis dans la pile logicielle ?"
  - "Quelles versions spécifiques des modules doivent être utilisées pour assurer la compatibilité avec les grappes de GPU H100 ?"
  - "Quels sont les modules et versions requis pour charger Ambertools 25.0 avec et sans support GPU dans l'environnement StdEnv/2023 ?"
  - "Quel modèle de carte graphique et quelle version de PLUMED sont explicitement indiqués comme étant pris en charge dans les notes ?"
  - "Quelles sont les catégories d'informations détaillées dans les en-têtes de colonnes du tableau de l'onglet \"StdEnv/2020\" ?"
  - "Comment doit-on configurer les variables d'environnement après avoir chargé le module AmberTools 21 ?"
  - "Quelles sont les différences de compatibilité matérielle, notamment pour les processeurs AMD et les GPU A100, entre les modules 20.9-20.15 et 20.12-20.15 d'Amber 20 ?"
  - "Quelle version spécifique d'Amber est disponible uniquement sur la grappe Graham et présente des limitations avec certaines fonctionnalités Python ?"
  - "Quelles sont les différences d'exécutables offerts entre les modules pour utilisation avec CPU et ceux pour utilisation avec GPU ?"
  - "Quels sont les problèmes connus concernant l'outil MMPBSA.py dans les différentes versions d'Amber mentionnées ?"
  - "Comment doit-on configurer un script de soumission de tâche pour exécuter une simulation sur un seul GPU, en particulier sur la grappe Narval ?"
  - "Avec quels types de matériel les bibliothèques MKL rencontrent-elles des problèmes de fonctionnement ?"
  - "Comment FlexiBLAS optimise-t-il l'utilisation des bibliothèques en fonction du matériel détecté ?"
  - "Quelle version de CUDA est requise pour effectuer des simulations sur les GPU A100 du système Narval ?"
  - "Comment configurer un script pour exécuter une tâche QM/MM distribuée utilisant plusieurs GPU avec sander.quick ?"
  - "Pourquoi la scalabilité d'une tâche MMPBSA parallèle s'effectue-t-elle de manière linéaire lors de l'utilisation de plusieurs processus MPI ?"
  - "Où peut-on consulter des guides d'étalonnage pour optimiser les performances des simulations moléculaires sur les grappes de calcul ?"
  - "What specific Slurm resource allocations, such as nodes, tasks per node, and memory, are requested for this job on the Trillium cluster?"
  - "Which software modules and specific versions must be loaded into the environment before running the simulation?"
  - "What are the designated input and output files, including topology and coordinate files, specified in the command line execution?"
  - "Comment configurer un script pour exécuter une tâche QM/MM distribuée utilisant plusieurs GPU avec sander.quick ?"
  - "Pourquoi la scalabilité d'une tâche MMPBSA parallèle s'effectue-t-elle de manière linéaire lors de l'utilisation de plusieurs processus MPI ?"
  - "Où peut-on consulter des guides d'étalonnage pour optimiser les performances des simulations moléculaires sur les grappes de calcul ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Introduction
[Amber](https://ambermd.org/) désigne un ensemble d'applications pour effectuer des simulations de dynamique moléculaire, particulièrement avec les biomolécules. Chacune des applications porte un nom différent, mais l'ensemble fonctionne plutôt bien et constitue un outil puissant pour effectuer plusieurs calculs usuels.

## Modules Amber
Nous fournissons les modules pour Amber, AmberTools et Amber-PMEMD dans notre [pile logicielle](../programming/available_software.md).

*   **[Amber](https://ambermd.org/AmberMD.php)** (module `amber`) : comprend tout ce qui se trouve dans AmberTools, plus le programme avancé *pmemd* pour les simulations de dynamique moléculaire haute performance (`QUICK` pour les calculs de DFT avec GPU et `sander` pour la dynamique moléculaire).
*   **Amber-PMEMD** (module `amber-pmemd`, Amber 24+) : Moteur `pmemd` haute performance optimisé pour CPU et GPU.
    Le moteur `pmemd` (optimized for CPU/GPU) est un module distinct depuis Amber24 parce que `pmemd` n'est plus compilé avec AmberTools.

    !!! note "Remarque"
        Le module `amber-pmemd` n'inclut pas AmberTools. Pour utiliser les deux applications, chargez les deux modules.

*   Le module `ambertools` pour [AmberTools](https://ambermd.org/AmberTools.php) offre des outils pour préparer et analyser les simulations. L'application `sander` est utilisée pour les simulations de dynamique moléculaire. Tous ces outils sont gratuits et *open source*.

Pour la liste des versions installées et de leurs modules dépendants, lancez [la sous-commande `module spider`](https://docs.alliancecan.ca/wiki/Utiliser_des_modules#Sous-commande_spider) ou consultez la page [Logiciels disponibles](../programming/available_software.md).

## Utiliser AMBER sur les grappes de GPU H100

!!! warning "Attention"
    Les anciens modules AMBER ne prennent pas en charge les GPU H100 de NVIDIA. Utilisez plutôt les modules listés dans le tableau ci-dessous.

### Modules requis

`ambertools/25.0` ou `amber-pmemd/24.3`

Ces modules offrent des noyaux ( *kernels*) CUDA pour les H-100 (compilés avec CUDA 12+ pour l'architecture Hopper).

!!! important "Important"
    Pour les tâches avec GPU, n'utilisez pas les anciens modules AMBER; ils ne fonctionnent pas sur les nœuds H100.

## Charger des modules

/// tab | StdEnv/2023
| Version           | avec CPU                                                | avec GPU (CUDA)                                              | Notes             |
| :---------------- | :------------------------------------------------------ | :----------------------------------------------------------- | :---------------- |
| amber-pmemd/24.3  | `StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 amber-pmemd/24.3` | `StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 amber-pmemd/24.3` | H100 pris en charge |
| amber/22.5-23.5   | `StdEnv/2023 gcc/12.3 openmpi/4.1.5 amber/22.5-23.5`    | `StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.2 amber/22.5-23.5` |                   |
| ambertools/25.0   | `StdEnv/2023 gcc/12.3 openmpi/4.1.5 ambertools/25.0`    | `StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 ambertools/25.0` | H100 pris en charge, avec PLUMED/2.9.0 |
///
/// tab | StdEnv/2020
| Version           | avec CPU                                                | avec GPU (CUDA)                                              | Notes                    |
| :---------------- | :------------------------------------------------------ | :----------------------------------------------------------- | :----------------------- |
| ambertools/21     | `StdEnv/2020 gcc/9.3.0 openmpi/4.0.3 scipy-stack ambertools/21` | `StdEnv/2020 gcc/9.3.0 cuda/11.4 openmpi/4.0.3 scipy-stack ambertools/21` | GCC, FlexiBLAS & FFTW    |
| amber/20.12-20.15 | `StdEnv/2020 gcc/9.3.0 openmpi/4.0.3 amber/20.12-20.15` | `StdEnv/2020 gcc/9.3.0 cuda/11.4 openmpi/4.0.3 amber/20.12-20.15` | GCC, FlexiBLAS & FFTW    |
| amber/20.9-20.15  | `StdEnv/2020 gcc/9.3.0 openmpi/4.0.3 amber/20.9-20.15`  | `StdEnv/2020 gcc/9.3.0 cuda/11.0 openmpi/4.0.3 amber/20.9-20.15` | GCC, MKL & FFTW          |
| amber/18.14-18.17 | `StdEnv/2020 gcc/9.3.0 openmpi/4.0.3 amber/18.14-18.17` | `StdEnv/2020 gcc/8.4.0 cuda/10.2 openmpi/4.0.3`              | GCC, MKL                 |
///
/// tab | StdEnv/2016
| Version           | avec CPU                                                        | avec GPU (CUDA)                                                     | Notes                        |
| :---------------- | :-------------------------------------------------------------- | :------------------------------------------------------------------ | :--------------------------- |
| amber/18          | `StdEnv/2016 gcc/5.4.0 openmpi/2.1.1 scipy-stack/2019a amber/18` | `StdEnv/2016 gcc/5.4.0 openmpi/2.1.1 cuda/9.0.176 scipy-stack/2019a amber/18` | GCC, MKL                     |
| amber/18.10-18.11 | `StdEnv/2016 gcc/5.4.0 openmpi/2.1.1 scipy-stack/2019a amber/18.10-18.11` | `StdEnv/2016 gcc/5.4.0 openmpi/2.1.1 cuda/9.0.176 scipy-stack/2019a amber/18.10-18.11` | GCC, MKL                     |
| amber/18.10-18.11 | `StdEnv/2016 gcc/7.3.0 openmpi/3.1.2 scipy-stack/2019a amber/18.10-18.11` | `StdEnv/2016 gcc/7.3.0 cuda/9.2.148 openmpi/3.1.2 scipy-stack/2019a amber/18.10-18.11` | GCC, MKL                     |
| amber/16          | `StdEnv/2016.4 amber/16`                                        |                                                                     | Disponible uniquement sur Graham. Certaines fonctionnalités Python ne sont pas prises en charge. |
///

## Utilisation

### AmberTools 21
Le module AmberTools 21 est présentement disponible sur toutes les grappes et offre `sander`, `sander.LES`, `sander.LES.MPI`, `sander.MPI`, `sander.OMP`, `sander.quick.cuda`, et `sander.quick.cuda.MPI`. Après avoir chargé le module, configurez les variables d'environnement avec

```bash
source $EBROOTAMBERTOOLS/amber.sh
```

### Amber 20
Amber20 est présentement disponible sur toutes les grappes. Il y a deux modules, soit 20.9-20.15 et 20.12-20.15.
*   20.9-20.15 utilise MKL et cuda/11.0; notez que les bibliothèques MKL ne fonctionnent pas bien avec des AMD et des CPU.
*   20.12-20.15 utilise FlexiBLAS et cuda/11.4; FlexiBLAS détecte le type de CPU et utilise des bibliothèques optimisées pour le matériel. De plus, CUDA/11.4 est requis pour effectuer des simulations sur les GPU A100 (installés sur Narval).

Les modules pour utilisation avec CPU offrent les applications disponibles avec AmberTools/20 plus `pmemd` (séquentiel) et `pmemd.MPI` (parallèle). Les modules pour utilisation avec ajoutent `pmemd.cuda` (un seul GPU) et `pmemd.cuda.MPI` (plusieurs GPU).

### Problèmes connus
1.  Le module amber/20.12-20.15 n'offre pas l'exécutable `MMPBSA.py.MPI`.
2.  `MMPBSA.py` des modules amber/18-10-18.11 et amber/18.14-18.17 ne peut pas effectuer les calculs PB; utilisez plutôt les modules amber/20 plus récents.

## Exemples de soumission de tâches

### Avec un seul GPU
Pour les simulations avec un GPU sur Narval, utilisez amber/20.12-20.15. Les modules compilés avec une version CUDA < 11.4 ne fonctionnent pas sur un GPU A100. Voici un exemple de script pour une tâche de calcul utilisant un seul GPU.

```bash title="pmemd_cuda_job.sh"
#!/bin/bash
#SBATCH --ntasks=1 
#SBATCH --gpus-per-node=1 
#SBATCH --mem-per-cpu=2000 
#SBATCH --time=10:00:00

module purge
module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 amber-pmemd/24.3

pmemd.cuda -O -i input.in -p topol.parm7 -c coord.rst7 -o output.mdout -r restart.rst7
```

### Tâche MPI parallèle avec CPU

/// tab | Narval
```bash title="pmemd_MPI_job_narval.sh"
#!/bin/bash
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=64
#SBATCH --mem-per-cpu=2000
#SBATCH --time=1:00:00

module purge
module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 amber-pmemd/24.3

srun pmemd.MPI -O -i input.in -p topol.parm7 -c coord.rst7 -o output.mdout -r restart.rst7
```
///
/// tab | Rorqual
```bash title="pmemd_MPI_job_rorqual.sh"
#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=192
#SBATCH --mem-per-cpu=2000
#SBATCH --time=1:00:00

module purge
module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 amber-pmemd/24.3

srun pmemd.MPI -O -i input.in -p topol.parm7 -c coord.rst7 -o output.mdout -r restart.rst7
```
///
/// tab | Fir
```bash title="pmemd_MPI_job_fir.sh"
#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=192
#SBATCH --mem-per-cpu=2000
#SBATCH --time=1:00:00

module purge
module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 amber-pmemd/24.3

srun pmemd.MPI -O -i input.in -p topol.parm7 -c coord.rst7 -o output.mdout -r restart.rst7
```
///
/// tab | Nibi
```bash title="pmemd_MPI_job_nibi.sh"
#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=192
#SBATCH --mem-per-cpu=2000
#SBATCH --time=1:00:00

module purge
module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 amber-pmemd/24.3

srun pmemd.MPI -O -i input.in -p topol.parm7 -c coord.rst7 -o output.mdout -r restart.rst7
```
///
/// tab | Trillium
```bash title="pmemd_MPI_job_trillium.sh"
#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=192
#SBATCH --mem-per-cpu=2000
#SBATCH --time=1:00:00

module purge
module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 amber-pmemd/24.3

srun pmemd.MPI -O -i input.in -p topol.parm7 -c coord.rst7 -o output.mdout -r restart.rst7
```
///

### Tâche QM/MM distribuée avec plusieurs GPU
Dans l'exemple suivant, huit GPU sont demandés.

```bash title="quick_MPI_job.sh"
#!/bin/bash
#SBATCH --ntasks=8
#SBATCH --gpus-per-task=1 
#SBATCH --mem-per-cpu=4000 
#SBATCH --time=02:00:00

module purge
module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 ambertools/25.0

srun sander.quick.cuda.MPI -O -i input.in -p topol.parm7 -c coord.rst7 -o output.mdout -r restart.rst7
```

### Tâche MMPBSA parallèle
Dans l'exemple suivant, 32 processus MPI sont utilisés. La scalabilité de MMPBSA se fait de façon linéaire parce que chaque séquence de la trajectoire est traitée indépendamment.

```bash title="mmpbsa_job.sh"
#!/bin/bash
#SBATCH --ntasks=32 
#SBATCH --mem-per-cpu=4000 
#SBATCH --time=1:00:00

module purge
module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 ambertools/25.0

srun MMPBSA.py.MPI -O -i mmpbsa.in -o mmpbsa.dat -sp solvated_complex.parm7 -cp complex.parm7 -rp receptor.parm7 -lp ligand.parm7 -y trajectory.nc
```

Pour les détails sur comment modifier vos scripts pour faire des simulations sur des ressources de calcul, voir [Exécuter des tâches](../running-jobs/running_jobs.md).

## Performance et étalonnage

Le [guide *Molecular Dynamics Performance Guide*](https://mdbench.ace-net.ca/mdbench/) a été créé par une équipe [d'ACENET](https://www.ace-net.ca/). Le guide décrit les conditions optimales pour exécuter aussi des tâches sur nos grappes avec GROMACS, NAMD et OpenMM.

*   [Étalonnage de simulations avec PMEMD](http://mdbench.ace-net.ca/mdbench/bform/?software_contains=PMEMD&software_id=&module_contains=&module_version=&site_contains=&gpu_model=&cpu_model=&arch=&dataset=6n4o)
*   [Étalonnage de simulations QM/MM avec SANDER.QUICK](http://mdbench.ace-net.ca/mdbench/bform/?software_contains=&software_id=&module_contains=&module_version=&site_contains=&gpu_model=&cpu_model=&arch=&dataset=4cg1)