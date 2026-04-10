---
title: "GROMACS/fr"
slug: "gromacs"
lang: "fr"

source_wiki_title: "GROMACS/fr"
source_hash: "2f03458fdc8f5989ac6b4ca3ac0279f5"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T06:49:24.660978+00:00"

tags:
  - software
  - biomolecularsimulation

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

# GROMACS

[GROMACS](http://www.gromacs.org/) est un logiciel de simulation en dynamique moléculaire pouvant traiter des systèmes composés de quelques centaines à quelques millions de particules. D'abord conçu pour les molécules biochimiques avec de nombreuses interactions liantes et complexes telles que les protéines, lipides et acides nucléiques, GROMACS est aussi utilisé par plusieurs groupes de recherche sur des systèmes non biologiques (par ex. les polymères) en raison de la vitesse à laquelle le logiciel calcule les interactions non liantes souvent dominantes dans le temps de calcul d'une simulation.

## Points forts

* Très bonne performance comparativement à d'autres applications.
* Depuis GROMACS 4.6, excellente accélération CUDA des GPU possédant la capacité de calcul Nvidia, soit >= 2.0 (par exemple Fermi ou plus).
* Grand choix d'outils d'analyse des trajectoires.
* Exécution en parallèle avec le protocole MPI standard ou la bibliothèque de calcul *Thread MPI* pour les postes de travail à nœuds simples.
* Logiciel gratuit sous la version 2.1 de LGPL (*GNU Lesser General Public License*).

## Points faibles

* Afin d'augmenter la vitesse de simulation, les analyses et/ou la collecte de données interactives sont réduites. Il peut donc s'avérer difficile d'obtenir de l'information non standard sur le système faisant l'objet de la simulation.

* Les méthodes de simulation et les paramètres par défaut varient grandement d'une version à l'autre. Il peut s'avérer difficile de reproduire les mêmes résultats avec des versions différentes.

* Les outils d’analyse et les utilitaires ajoutés au programme ne sont pas toujours de la meilleure qualité : ils peuvent contenir des bogues et les méthodes sont souvent mal documentées. Nous recommandons l'emploi de méthodes indépendantes pour vérifier les résultats.

## Utilisation de GPU

La première partie du fichier de journalisation décrit la configuration et indique si la version utilisée permet l'utilisation de GPU. GROMACS utilise automatiquement tout GPU repéré.

GROMACS utilise à la fois les CPU et les GPU; la performance est tributaire d’un équilibre raisonnable entre les deux.

La nouvelle liste de voisins (*neighbor structure*) exigeait l'ajout au fichier MDP de la nouvelle variable du rayon de coupure (*cutoff-scheme*).
Le comportement des versions d'avant 4.6 correspond à `cutoff-scheme = group`, alors que pour utiliser l'accélération GPU il faut plutôt `cutoff-scheme = verlet` qui est par défaut dans la version 5.

# Guide de démarrage

Cette section aborde les détails de configuration.

## Modules d'environnement

Les versions suivantes sont disponibles :

=== "StdEnv/2023"

| version        | modules pour utiliser les CPU                          | modules pour utiliser les GPU (CUDA)                           | remarques                  |
|:---------------|:-------------------------------------------------------|:---------------------------------------------------------------|:---------------------------|
| gromacs/2025.4 | `StdEnv/2023  gcc/12.3  openmpi/4.1.5  gromacs/2025.4` | `StdEnv/2023 gcc/12.3  openmpi/4.1.5  cuda/12.6  gromacs/2025.4` | GCC, FlexiBLAS & FFTW      |
| gromacs/2024.6 | `StdEnv/2023  gcc/12.3  openmpi/4.1.5  gromacs/2024.6` | `StdEnv/2023 gcc/12.3  openmpi/4.1.5  cuda/12.6  gromacs/2024.6` | GCC, FlexiBLAS & FFTW      |
| gromacs/2024.4 | `StdEnv/2023  gcc/12.3  openmpi/4.1.5  gromacs/2024.4` | `StdEnv/2023 gcc/12.3  openmpi/4.1.5  cuda/12.2  gromacs/2024.4` | GCC, FlexiBLAS & FFTW      |
| gromacs/2024.1 | `StdEnv/2023  gcc/12.3  openmpi/4.1.5  gromacs/2024.1` | `StdEnv/2023 gcc/12.3  openmpi/4.1.5  cuda/12.2  gromacs/2024.1` | GCC, FlexiBLAS & FFTW      |
| gromacs/2023.5 | `StdEnv/2023  gcc/12.3  openmpi/4.1.5  gromacs/2023.5` | `StdEnv/2023  gcc/12.3  openmpi/4.1.5  cuda/12.2  gromacs/2023.5` | GCC, FlexiBLAS & FFTW      |
| gromacs/2023.3 | `StdEnv/2023  gcc/12.3  openmpi/4.1.5  gromacs/2023.3` | `StdEnv/2023 gcc/12.3  openmpi/4.1.5  cuda/12.2  gromacs/2023.3` | GCC, FlexiBLAS & FFTW      |

=== "StdEnv/2020"

| version        | modules pour utiliser les CPU                          | modules pour utiliser les GPU (CUDA)                                      | remarques                  |
|:---------------|:-------------------------------------------------------|:--------------------------------------------------------------------------|:---------------------------|
| gromacs/2023.2 | `StdEnv/2020  gcc/9.3.0  openmpi/4.0.3  gromacs/2023.2` | `StdEnv/2020  gcc/9.3.0  cuda/11.4  openmpi/4.0.3  gromacs/2023.2`         | GCC, FlexiBLAS & FFTW      |
| gromacs/2023   | `StdEnv/2020  gcc/9.3.0  openmpi/4.0.3  gromacs/2023`   | `StdEnv/2020  gcc/9.3.0  cuda/11.4  openmpi/4.0.3  gromacs/2023`           | GCC, FlexiBLAS & FFTW      |
| gromacs/2022.3 | `StdEnv/2020  gcc/9.3.0  openmpi/4.0.3  gromacs/2022.3` | `StdEnv/2020  gcc/9.3.0  cuda/11.4  openmpi/4.0.3  gromacs/2022.3`         | GCC, FlexiBLAS & FFTW      |
| gromacs/2022.2 | `StdEnv/2020  gcc/9.3.0  openmpi/4.0.3  gromacs/2022.2` |                                                                           | GCC, FlexiBLAS & FFTW      |
| gromacs/2021.6 | `StdEnv/2020  gcc/9.3.0  openmpi/4.0.3  gromacs/2021.6` | `StdEnv/2020  gcc/9.3.0  cuda/11.4  openmpi/4.0.3  gromacs/2021.6`         | GCC, FlexiBLAS & FFTW      |
| gromacs/2021.4 | `StdEnv/2020  gcc/9.3.0  openmpi/4.0.3  gromacs/2021.4` | `StdEnv/2020  gcc/9.3.0  cuda/11.4  openmpi/4.0.3  gromacs/2021.4`         | GCC, FlexiBLAS & FFTW      |
| gromacs/2021.2 |                                                        | `StdEnv/2020  gcc/9.3.0  cuda/11.4  openmpi/4.0.3  gromacs/2021.2`         | GCC, FlexiBLAS & FFTW      |
| gromacs/2021.2 | `StdEnv/2020  gcc/9.3.0  openmpi/4.0.3  gromacs/2021.2` | `StdEnv/2020  gcc/9.3.0  cuda/11.0  openmpi/4.0.3  gromacs/2021.2`         | GCC & MKL                  |
| gromacs/2020.6 | `StdEnv/2020  gcc/9.3.0  openmpi/4.0.3  gromacs/2020.6` | `StdEnv/2020  gcc/9.3.0  cuda/11.4  openmpi/4.0.3  gromacs/2020.6`         | GCC, FlexiBLAS & FFTW      |
| gromacs/2020.4 |                                                        | `StdEnv/2020  gcc/9.3.0  cuda/11.4  openmpi/4.0.3  gromacs/2020.4`         | GCC, FlexiBLAS & FFTW      |
| gromacs/2020.4 | `StdEnv/2020  gcc/9.3.0  openmpi/4.0.3  gromacs/2020.4` | `StdEnv/2020  gcc/9.3.0  cuda/11.0  openmpi/4.0.3  gromacs/2020.4`         | GCC & MKL                  |

=== "StdEnv/2018.3"

!!! warning "Déprécié"
    Cet [environnement logiciel](standard-software-environments.md) n'est plus supporté.

| version        | modules pour utiliser les CPU                               | modules pour utiliser les GPU (CUDA)                                        | remarques   |
|:---------------|:------------------------------------------------------------|:----------------------------------------------------------------------------|:------------|
| gromacs/2020.2 | `StdEnv/2018.3  gcc/7.3.0 openmpi/3.1.2 gromacs/2020.2`     | `StdEnv/2018.3  gcc/7.3.0 cuda/10.0.130 openmpi/3.1.2  gromacs/2020.2`     | GCC & MKL   |
| gromacs/2019.6 | `StdEnv/2018.3  gcc/7.3.0 openmpi/3.1.2 gromacs/2019.6`     | `StdEnv/2018.3  gcc/7.3.0 cuda/10.0.130 openmpi/3.1.2  gromacs/2019.6`     | GCC & MKL   |
| gromacs/2019.3 | `StdEnv/2018.3  gcc/7.3.0 openmpi/3.1.2 gromacs/2019.3`     | `StdEnv/2018.3  gcc/7.3.0 cuda/10.0.130 openmpi/3.1.2  gromacs/2019.3`     | GCC & MKL † |
| gromacs/2018.7 | `StdEnv/2018.3  gcc/7.3.0 openmpi/3.1.2 gromacs/2018.7`     | `StdEnv/2018.3  gcc/7.3.0 cuda/10.0.130 openmpi/3.1.2  gromacs/2018.7`     | GCC & MKL   |

=== "StdEnv/2016.4"

!!! warning "Déprécié"
    Cet [environnement logiciel](standard-software-environments.md) n'est plus supporté.

| version        | modules pour utiliser les CPU                                | modules pour utiliser les GPU (CUDA)                                         | remarques        |
|:---------------|:-------------------------------------------------------------|:-----------------------------------------------------------------------------|:-----------------|
| gromacs/2018.3 | `StdEnv/2016.4  gcc/6.4.0 openmpi/2.1.1 gromacs/2018.3`      | `StdEnv/2016.4  gcc/6.4.0 cuda/9.0.176 openmpi/2.1.1  gromacs/2018.3`       | GCC & FFTW       |
| gromacs/2018.2 | `StdEnv/2016.4  gcc/6.4.0 openmpi/2.1.1 gromacs/2018.2`      | `StdEnv/2016.4  gcc/6.4.0 cuda/9.0.176 openmpi/2.1.1  gromacs/2018.2`       | GCC & FFTW       |
| gromacs/2018.1 | `StdEnv/2016.4  gcc/6.4.0 openmpi/2.1.1 gromacs/2018.1`      | `StdEnv/2016.4  gcc/6.4.0 cuda/9.0.176 openmpi/2.1.1  gromacs/2018.1`       | GCC & FFTW       |
| gromacs/2018   | `StdEnv/2016.4  gromacs/2018`                                | `StdEnv/2016.4  cuda/9.0.176 gromacs/2018`                                   | Intel & MKL      |
| gromacs/2016.5 | `StdEnv/2016.4  gcc/6.4.0  openmpi/2.1.1 gromacs/2016.5`     | `StdEnv/2016.4  gcc/6.4.0  cuda/9.0.176  openmpi/2.1.1 gromacs/2016.5`     | GCC & FFTW       |
| gromacs/2016.3 | `StdEnv/2016.4  gromacs/2016.3`                              | `StdEnv/2016.4  cuda/8.0.44 gromacs/2016.3`                                  | Intel & MKL      |
| gromacs/5.1.5  | `StdEnv/2016.4  gromacs/5.1.5`                               | `StdEnv/2016.4  cuda/8.0.44 gromacs/5.1.5`                                   | Intel & MKL      |
| gromacs/5.1.4  | `StdEnv/2016.4  gromacs/5.1.4`                               | `StdEnv/2016.4  cuda/8.0.44 gromacs/5.1.4`                                   | Intel & MKL      |
| gromacs/5.0.7  | `StdEnv/2016.4  gromacs/5.0.7`                               | `StdEnv/2016.4  cuda/8.0.44 gromacs/5.0.7`                                   | Intel & MKL      |
| gromacs/4.6.7  | `StdEnv/2016.4  gromacs/4.6.7`                               | `StdEnv/2016.4  cuda/8.0.44 gromacs/4.6.7`                                   | Intel & MKL      |
| gromacs/4.6.7  | `StdEnv/2016.4  gcc/5.4.0  openmpi/2.1.1 gromacs/4.6.7`      | `StdEnv/2016.4  gcc/5.4.0  cuda/8.0  openmpi/2.1.1  gromacs/4.6.7`         | GCC & MKL & ThreadMPI |

**Remarques**
* Les versions 2020.0 jusqu'à 2021.5 inclusivement contiennent un bogue quand elles sont utilisées avec des GPU de génération Volta ou plus récentes (V100, T4, A100 et H100) avec l'option `-update gpu` de `mdrun` qui aurait pu perturber le calcul viriel et ainsi fausser le raccord de pression. Dans les notes de mise à jour de la version 2021.6 on peut lire :[^1]
    > [traduction libre] *La mise à jour n'est pas activée par défaut sur le GPU et donc l'erreur ne peut se produire que dans les simulations où l'option `-update gpu` a été explicitement sélectionnée; même dans ce cas, l'erreur peut être rare car nous ne l'avons pas observée en pratique dans les tests que nous avons effectués.*
    Vous trouverez plus d'information dans [GitLab, au sujet #4393 du projet GROMACS](https://gitlab.com/gromacs/gromacs/-/issues/4393).[^2]
* Les versions depuis 2020.4 ont été compilées pour [l'environnement logiciel standard](standard-software-environments.md) `StdEnv/2020`.
* Les versions 2018.7 et suivantes ont été compilées avec les compilateurs GCC et la bibliothèque MKL puisqu’ils améliorent légèrement la performance.
* Les versions antérieures ont été compilées avec soit des compilateurs GCC et FFTW, soit avec des compilateurs Intel MKL avec des bibliothèques Open MPI 2.1.1 à partir de l'environnement par défaut, comme indiqué dans le tableau ci-dessus.
* Les versions CPU (non GPU) sont disponibles en simple et double précisions à l'exception de 2019.3 (**†**), où la double précision n'est pas disponible pour AVX512.

Pour charger ces modules, utilisez la commande `module load` avec les noms indiqués dans le tableau ci-dessus, par exemple

```bash
module load  StdEnv/2023  gcc/12.3   openmpi/4.1.5  gromacs/2025.4
# ou
module load  StdEnv/2020  gcc/9.3.0  openmpi/4.0.3  gromacs/2023.2
```

Ces versions utilisent aussi les GPU, mais uniquement en simple précision. Pour charger la version utilisant les GPU, chargez d'abord le module `cuda`. Pour les noms, voyez le tableau ci-dessus.

```bash
module load  StdEnv/2023  gcc/12.3  openmpi/4.1.5  cuda/12.6  gromacs/2025.4
# ou
module load  StdEnv/2020  gcc/9.3.0  cuda/11.4  openmpi/4.0.3  gromacs/2023.2
```

Consultez [Utiliser des modules](https://docs.computecanada.ca/wiki/Utiliser_des_modules) pour plus d’information sur les modules d’environnement.

## Suffixes

### Versions 5.x, 2016.x et suivantes

Les versions 5 et suivantes comprennent quatre binaires possédant toutes les fonctionnalités de GROMACS. Les outils des versions précédentes ont été implémentés en sous-commandes des binaires gmx.
Consultez [GROMACS 5.0 Tool Changes](http://www.gromacs.org/Documentation/How-tos/Tool_Changes_for_5.0) et la [documentation GROMACS](http://manual.gromacs.org/documentation/).

* **`gmx`** - GROMACS en mixte (simple) précision avec OpenMP, mais sans MPI
* **`gmx_mpi`** - GROMACS en mixte (simple) précision avec OpenMP et MPI
* **`gmx_d`** - GROMACS en double précision avec OpenMP, mais sans MPI
* **`gmx_mpi_d`** - GROMACS en double précision avec OpenMP et MPI

### Version 4.6.7

* Les binaires double précision ont le suffixe `_d`.
* Les binaires parallèles simple précision et double précision `mdrun` sont :

* **`mdrun_mpi`**
* **`mdrun_mpi_d`**

## Scripts de soumission des tâches

Consultez [Exécuter des tâches](running-jobs.md) sur comment utiliser l'ordonnanceur Slurm.

### Tâches séquentielles

Voici un script simple pour la tâche séquentielle mdrun.

```sh linenums="1" title="serial_gromacs_job.sh"
#!/bin/bash
#SBATCH --time=0-0:30         # time limit (D-HH:MM)
#SBATCH --mem-per-cpu=1000M   # memory per CPU (in MB)
module purge  
module load  StdEnv/2023  gcc/12.3  openmpi/4.1.5  gromacs/2025.4
export OMP_NUM_THREADS="${SLURM_CPUS_PER_TASK:-1}"
gmx mdrun -nt 1 -deffnm em
```

La simulation du système moléculaire sera exécutée dans le fichier `em.tpr`.

### Nœuds entiers

Les systèmes simulés par GROMACS sont habituellement si grands que vous voudrez utiliser plusieurs nœuds entiers.

Le produit de `--ntasks-per-node=` par `--cpus-per-task` devrait généralement correspondre au nombre de cœurs CPU des nœuds de calcul de la grappe. Voir la section [Performance](#performance) ci-dessous.

Sur les grappes dotées d'un grand nombre de cœurs de CPU (par exemple 192) par nœud de calcul, la décomposition de domaine peut devenir un facteur limitant lors du choix de `--ntasks-per-node`. Plus un système est grand, plus il peut être divisé en régions plus petites, permettant des valeurs de `--ntasks-per-node` plus élevées. Si GROMACS signale une erreur indiquant que la décomposition de domaine est impossible étant donné la taille du système et le nombre de domaines demandé, réduisez de moitié `--ntasks-per-node` et doublez `--cpus-per-task`.

=== "Narval"

```sh linenums="1" title="gromacs_whole_node_narval.sh"
#!/bin/bash
#SBATCH --nodes=1                # number of nodes
#SBATCH --ntasks-per-node=32     # request 32 MPI tasks per node
#SBATCH --cpus-per-task=2        # 2 OpenMP threads per MPI task => total: 32 x 2 = 64 CPUs/node
#SBATCH --mem-per-cpu=2000M      # memory per CPU (in MB)
#SBATCH --time=0-01:00           # time limit (D-HH:MM)
module purge  
module load  StdEnv/2023  gcc/12.3  openmpi/4.1.5  gromacs/2025.4
export OMP_NUM_THREADS="${SLURM_CPUS_PER_TASK:-1}"
 
srun --cpus-per-task=$OMP_NUM_THREADS gmx_mpi mdrun -deffnm md
```

=== "Rorqual"

```sh linenums="1" title="gromacs_whole_node_rorqual.sh"
#!/bin/bash
#SBATCH --nodes=1                # number of nodes
#SBATCH --ntasks-per-node=96     # request 96 MPI tasks per node
#SBATCH --cpus-per-task=2        # 2 OpenMP threads per MPI task => total: 96 x 2 = 192 CPUs/node
#SBATCH --mem-per-cpu=2000M      # memory per CPU (in MB)
#SBATCH --time=0-01:00           # time limit (D-HH:MM)
module purge  
module load  StdEnv/2023  gcc/12.3  openmpi/4.1.5  gromacs/2025.4
export OMP_NUM_THREADS="${SLURM_CPUS_PER_TASK:-1}"

srun --cpus-per-task=$OMP_NUM_THREADS gmx_mpi mdrun -deffnm md
```

=== "Fir"

```sh linenums="1" title="gromacs_whole_node_fir.sh"
#!/bin/bash
#SBATCH --nodes=1                # number of nodes
#SBATCH --ntasks-per-node=96     # request 96 MPI tasks per node
#SBATCH --cpus-per-task=2        # 2 OpenMP threads per MPI task => total: 96 x 2 = 192 CPUs/node
#SBATCH --mem-per-cpu=2000M      # memory per CPU (in MB)
#SBATCH --time=0-01:00           # time limit (D-HH:MM)
module purge  
module load  StdEnv/2023  gcc/12.3  openmpi/4.1.5  gromacs/2025.4
export OMP_NUM_THREADS="${SLURM_CPUS_PER_TASK:-1}"

srun --cpus-per-task=$OMP_NUM_THREADS gmx_mpi mdrun -deffnm md
```

=== "Nibi"

```sh linenums="1" title="gromacs_whole_node_nibi.sh"
#!/bin/bash
#SBATCH --nodes=1                # number of nodes
#SBATCH --ntasks-per-node=96     # request 96 MPI tasks per node
#SBATCH --cpus-per-task=2        # 2 OpenMP threads per MPI task => total: 96 x 2 = 192 CPUs/node
#SBATCH --mem-per-cpu=2000M      # memory per CPU (in MB)
#SBATCH --time=0-01:00           # time limit (D-HH:MM)
module purge  
module load  StdEnv/2023  gcc/12.3  openmpi/4.1.5  gromacs/2025.4
export OMP_NUM_THREADS="${SLURM_CPUS_PER_TASK:-1}"

srun --cpus-per-task=$OMP_NUM_THREADS gmx_mpi mdrun -deffnm md
```

=== "Trillium"

```sh linenums="1" title="gromacs_whole_node_trillium.sh"
#!/bin/bash
#SBATCH --nodes=1                # number of nodes
#SBATCH --ntasks-per-node=96     # request 96 MPI tasks per node
#SBATCH --cpus-per-task=2        # 2 OpenMP threads per MPI task => total: 96 x 2 = 192 CPUs/node
#SBATCH --mem-per-cpu=2000M      # memory per CPU (in MB)
#SBATCH --time=0-01:00           # time limit (D-HH:MM)
module purge  
module load  StdEnv/2023  gcc/12.3  openmpi/4.1.5  gromacs/2025.4
export OMP_NUM_THREADS="${SLURM_CPUS_PER_TASK:-1}"

srun --cpus-per-task=$OMP_NUM_THREADS gmx_mpi mdrun -deffnm md
```

### Tâches GPU

Pour plus d'information, consultez [Ordonnancement Slurm des tâches exécutées avec GPU](using-gpus-with-slurm.md).

Cette tâche pour mdrun utilise 4 fils OpenMP et un (1) GPU.

```sh linenums="1" title="gpu_gromacs_job.sh"
#!/bin/bash
#SBATCH --gpus-per-node=1        # request 1 GPU per node
#SBATCH --cpus-per-task=4        # number of OpenMP threads per MPI process
#SBATCH --mem-per-cpu=2000M      # memory limit per CPU core (megabytes)
#SBATCH --time=0:30:00           # time limit (D-HH:MM:ss)
module purge  
module load StdEnv/2023  gcc/12.3  openmpi/4.1.5  cuda/12.6  gromacs/2025.4
export OMP_NUM_THREADS="${SLURM_CPUS_PER_TASK:-1}"

gmx mdrun -ntomp ${SLURM_CPUS_PER_TASK:-1} -deffnm md
```

#### Travailler avec des GPU

Il faut noter que le fait d'utiliser plus qu'un GPU cause habituellement une pauvre efficacité. Avant d'utiliser plusieurs GPU pour vos simulations, effectuez des tests comparatifs avec un seul et avec plusieurs pour évaluer la performance

* Les versions 2020.0 jusqu'à 2021.5 inclusivement contiennent un bogue quand elles sont utilisées avec des GPU de génération Volta ou plus récentes (V100, T4 et A100) avec l'option `-update gpu` de `mdrun` qui aurait pu perturber le calcul viriel et ainsi fausser le raccord de pression. Dans les notes de mise à jour de la version 2021.6 on peut lire :[^3]
    > [traduction libre] *La mise à jour n'est pas activée par défaut sur le GPU et donc l'erreur ne peut se produire que dans les simulations où l'option `<tt>-update gpu</tt>` a été explicitement sélectionnée; même dans ce cas, l'erreur peut être rare car nous ne l'avons pas observée en pratique dans les tests que nous avons effectués.*
    Vous trouverez plus d'information dans [GitLab, au sujet #4393 du projet GROMACS](https://gitlab.com/gromacs/gromacs/-/issues/4393).[^4]
* Les nœuds GPU sont configurés différemment sur nos grappes.
    Voir [GPU disponibles](using-gpus-with-slurm.md#gpu-disponibles) you can find more information about the different node configurations (GPU models and number of GPUs and CPUs per node).
* GROMACS impose certaines contraintes dans le choix du nombre de GPU, de tâches (rang MPI) et de fils OpenMP.
    Pour la version 2018.2, les contraintes sont :
    * `--tasks-per-node` doit être un multiple du nombre de GPU (`--gres=gpu:`)
    * GROMACS fonctionne avec un seul fil OpenMP seulement si l'option `-ntomp` est utilisée.
        Le nombre optimal de `--cpus-per-task` se situe entre 2 et 6, selon les développeurs.
* Évitez d'utiliser une fraction de CPU et de mémoire plus grande que la fraction de GPU que vous demandez dans un nœud.

Consultez [notre portail *MOLECULAR DYNAMICS PERFORMANCE GUIDE*](https://mdbench.ace-net.ca/mdbench/bform/?software_contains=GROMACS.cuda&software_id=&module_contains=&module_version=&site_contains=&gpu_model=&cpu_model=&arch=&dataset=6n4o).

#### Exécuter plusieurs simulations sur un GPU

GROMACS et d'autres programmes de simulation MD ne peuvent exploiter pleinement les modèles de GPU récents tels que les Nvidia A100 et H100, sauf si le système moléculaire est très volumineux (des millions d'atomes). Exécuter une simulation classique sur un tel GPU gaspille une part importante des ressources de calcul allouées.

Deux solutions sont recommandées pour résoudre ce problème. La première consiste à exécuter plusieurs simulations sur un seul GPU à l'aide de `mdrun -multidir`, comme décrit ci-dessous. C'est la solution idéale si vous exécutez plusieurs simulations similaires, par exemple

* Répéter la même simulation pour obtenir un échantillonnage plus précis de l'espace conformationnel
* Simuler plusieurs variants de protéines, plusieurs petits ligands en complexe avec la même protéine, plusieurs températures ou concentrations ioniques, etc.
* Simuler sur la base des ensembles, telles que l'échange de répliques

Des simulations semblables sont nécessaires pour assurer un équilibrage de charge adéquat. Si les simulations sont dissemblables, certaines progresseront plus vite et se termineront plus tôt que d'autres, ce qui entraînera un gaspillage des ressources.

Le script de tâche suivant exécute trois simulations semblables dans des répertoires distincts (`sim1`, `sim2`, `sim3`) avec un seul GPU. Si vous modifiez le nombre de simulations, veillez à ajuster les paramètres `--ntasks-per-node` et `--cpus-per-task`. Une tâche par simulation doit être exécutée, tandis que le nombre total de cœurs de processeur doit rester constant.

=== "Narval"

```sh linenums="1" title="gpu_gromacs_job_multidir.sh"
#!/bin/bash
#SBATCH --gpus-per-node=1        # request 1 GPU per node
#SBATCH --ntasks-per-node=3      # number of MPI processes and simulations
#SBATCH --cpus-per-task=4        # number of OpenMP threads per MPI process
#SBATCH --mem-per-cpu=2000M      # memory limit per CPU core (megabytes)
#SBATCH --time=0:30:00           # time limit (D-HH:MM:ss)

module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 gromacs/2025.4

export OMP_NUM_THREADS="${SLURM_CPUS_PER_TASK:-1}"

srun gmx_mpi mdrun -ntomp ${SLURM_CPUS_PER_TASK:-1} -deffnm md \
    -multidir sim1 sim2 sim3
```

La deuxième solution est d'utiliser une instance MIG (une fraction de GPU) plutôt qu'un GPU complet. Ceci est idéal si vous n'avez qu'une seule simulation ou si vos simulations sont dissemblables, par exemple

* des systèmes de tailles différentes (différence de plus de 10 % dans le nombre d'atomes);
* des systèmes de formes ou de compositions différentes, comme une protéine membranaire et une protéine soluble.

!!! warning ""
    Notez que [Hyper-Q/MPS](hyper-q-mps.md) ne doit jamais être utilisé avec GROMACS. L'option intégrée `-multidir` permet d'obtenir la même fonctionnalité plus efficacement.

# Utilisation

!!! warning "En préparation"

    Cette section est en préparation.

## Préparation du système

L'exécution d'une simulation requiert un fichier d'entrée binaire *tpr* (*portable binary run input file*) qui contient la structure de simulation de départ, la topologie moléculaire et l'ensemble des paramètres de simulation.

La commande `gmx grompp` crée les fichiers tpr; pour les versions antérieures à 5.0, la commande est `grompp`. Vous avez besoin des fichiers suivants :
* Le fichier de coordonnées avec la structure de départ; les formats de fichiers valides sont '.gro', '.pdb' ou '.cpt' (point de contrôle GROMACS).
* Le fichier de topologie du système au format '*top*'; celui-ci détermine le champ de force et la façon dont les paramètres du champ de force s'appliquent au système simulé. Les topologies des parties individuelles du système simulé (soit les molécules) sont placées dans des fichiers *itp* distincts et sont incluses dans le fichier *top* avec la commande `#include`.
* Le fichier *mdp* des paramètres d'exécution. Consultez le guide GROMACS pour la description détaillée des options.

Les fichiers *trp* sont portables et peuvent donc être groupés (*grompp-ed*) sur une grappe, copiés sur une autre grappe et utilisés comme fichier d'entrée pour *mdrun*. Utilisez toujours la même version GROMACS pour *grompp* et *mdrun*. Même si *mdrun* peut utiliser des fichiers *tpr* créés avec une version antérieure de *grompp*, la simulation peut donner des résultats inattendus.

## Exécuter une simulation

Les simulations MD prennent souvent plus de temps à compléter que la durée maximale permise en temps réel pour une tâche; elles doivent donc être redémarrées. Pour minimiser le temps d'attente avant le lancement d'une tâche, vous pouvez maximiser le [nombre de nœuds auxquels vous avez accès](job-scheduling-policies.md#pourcentages-des-noeuds-disponibles) en choisissant une durée d'exécution plus courte. Un bon compromis entre le temps d'attente et la durée d'exécution est souvent de demander une durée en temps réel de 24 ou 72 heures.

Vous devriez utiliser le paramètre `-maxh` de `mdrun` pour indiquer au programme la durée en temps réel pour que l'étape en cours se termine bien lorsque la durée atteint 99%.
De cette façon, `mdrun` crée à cette étape un fichier de point de contrôle (*checkpoint file*) et lui permet de bien fermer tous les fichiers de sortie (trajectoires, énergie, journalisation, etc.).

Par exemple, utilisez `#SBATCH --time=24:00` avec `gmx mdrun -maxh 24 ...`
ou `#SBATCH --time=3-00:00` avec `gmx mdrun -maxh 72 ...`.

```sh linenums="1" title="gromacs_job.sh"
#!/bin/bash
#SBATCH --nodes=1                # number of Nodes
#SBATCH --tasks-per-node=32      # number of MPI processes per node
#SBATCH --mem-per-cpu=4000       # memory limit per CPU (megabytes)
#SBATCH --time=24:00:00          # time limit (D-HH:MM:ss)
module purge
module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 gromacs/2024.4
export OMP_NUM_THREADS="${SLURM_CPUS_PER_TASK:-1}"

srun  gmx_mpi  mdrun  -deffnm md  -maxh 24
```

### Redémarrer une simulation

Vous pouvez redémarrer une simulation avec la même commande `mdrun` que pour la simulation originale en ajoutant le paramètre `-cpi state.cpt` où `state.cpt` est le nom du dernier fichier de point de contrôle. Depuis la version 4.5, `mdrun` tente par défaut d'utiliser les fichiers existants (trajectoires, énergie, journalisation, etc.).
GROMACS vérifie la cohérence entre les fichiers de sortie et rejette au besoin les étapes plus récentes que le fichier de point de contrôle.

Le paramètre `-maxh` fait en sorte que les fichiers de contrôle et de sortie sont cohérents au moment où la simulation atteint la durée limite d'exécution.

Pour plus d'information, consultez la [documentation GROMACS](http://manual.gromacs.org/documentation/current/user-guide/managing-simulations.html)[^5] et la [page de manuel GROMACS : gmx mdrun](http://manual.gromacs.org/documentation/current/onlinehelp/gmx-mdrun.html#gmx-mdrun)[^6].

```sh linenums="1" title="gromacs_job_restart.sh"
#!/bin/bash
#SBATCH --nodes=1                # number of Nodes
#SBATCH --tasks-per-node=32      # number of MPI processes per node
#SBATCH --mem-per-cpu=4000       # memory limit per CPU (megabytes)
#SBATCH --time=24:00:00          # time limit (D-HH:MM:ss)
module purge
module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 gromacs/2024.4
export OMP_NUM_THREADS="${SLURM_CPUS_PER_TASK:-1}"

srun  gmx_mpi  mdrun  -deffnm md  -maxh 24.0  -cpi md.cpt
```

### Morceler les simulations

La fonctionnalité de redémarrage d'une simulation peut servir à la diviser en plusieurs tâches courtes. Les tâches courtes sont moins longues à exécuter. En particulier, celles qui demandent trois heures ou moins sont éligibles à la planification de remplacement. (Voir nos [politiques de planification des tâches](job-scheduling-policies.md).) Ceci est particulièrement utile si votre groupe de recherche ne dispose que d'une allocation de ressources par défaut (par exemple, `def-sponsor`) sur la grappe, mais sera également bénéfique pour ceux qui disposent d'allocations de ressources compétitives (par exemple, `rrg-sponsor`).

En utilisant un [vecteur de tâches](job-arrays.md), vous pouvez automatiser les points de contrôle. Avec le script suivant, un seul appel à `sbatch` soumet plusieurs tâches courtes, mais seule la première peut commencer. Dès que cette première tâche est terminée, la suivante peut démarrer et reprendre la simulation. Ce processus se répète jusqu'à ce que toutes les tâches soient terminées ou que la simulation elle-même soit terminée, après quoi les tâches en attente sont automatiquement annulées.

=== "Nœuds entiers (Narval)"

```sh linenums="1" title="gromacs_job_checkpoint.sh"
#!/bin/bash
#SBATCH --nodes=1                # number of nodes
#SBATCH --ntasks-per-node=32     # request 32 MPI tasks per node
#SBATCH --cpus-per-task=2        # 2 OpenMP threads per MPI task
#SBATCH --mem-per-cpu=2000M      # memory per CPU (in MB)
#SBATCH --time=03:00:00          # time limit (D-HH:MM:ss)
#SBATCH --array=1-20%1           # job range, running only 1 at a time

module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 gromacs/2024.4

# Adjust simulation name (default filename for -deffnm option)
sim_name=md

nt=${SLURM_CPUS_PER_TASK:-1}
export OMP_NUM_THREADS=$nt

nhours=$(squeue -h -j $SLURM_JOB_ID -O TimeLimit | cut -d: -f1)

srun gmx_mpi mdrun -ntomp $nt -deffnm $sim_name -cpi "$sim_name.cpt" -maxh $nhours

exit_code=$?
if (( exit_code != 0 )); then
	echo "Simulation exited with an error, cancelling pending jobs"
	scancel -t pending $SLURM_ARRAY_JOB_ID
	exit $exit_code
fi

nsteps_expr='^[[:space:]]*nsteps[[:space:]]*=[[:space:]]*[[:digit:]]*$'
nsteps=$(grep "$nsteps_expr" "$sim_name.log" | awk '{ print $3 }')
if grep "^Writing checkpoint, step $nsteps at " "$sim_name.log"; then
	echo "Simulation finished, cancelling pending jobs"
	scancel -t pending $SLURM_ARRAY_JOB_ID
fi
```

=== "Tâche GPU"

```sh linenums="1" title="gromacs_job_checkpoint.sh"
#!/bin/bash
#SBATCH --gpus-per-node=1        # request 1 GPU per node
#SBATCH --cpus-per-task=4        # number of OpenMP threads per MPI process
#SBATCH --mem-per-cpu=2000M      # memory limit per CPU core (megabytes)
#SBATCH --time=03:00:00          # time limit (D-HH:MM:ss)
#SBATCH --array=1-20%1           # job range, running only 1 at a time

module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.2 gromacs/2024.4

# Adjust simulation name (default filename for -deffnm option)
sim_name=md

nt=${SLURM_CPUS_PER_TASK:-1}
export OMP_NUM_THREADS=$nt

nhours=$(squeue -h -j $SLURM_JOB_ID -O TimeLimit | cut -d: -f1)

srun gmx mdrun -ntomp $nt -deffnm $sim_name -cpi "$sim_name.cpt" -maxh $nhours

exit_code=$?
if (( exit_code != 0 )); then
	echo "Simulation exited with an error, cancelling pending jobs"
	scancel -t pending $SLURM_ARRAY_JOB_ID
	exit $exit_code
fi

nsteps_expr='^[[:space:]]*nsteps[[:space:]]*=[[:space:]]*[[:digit:]]*$'
nsteps=$(grep "$nsteps_expr" "$sim_name.log" | awk '{ print $3 }')
if grep "^Writing checkpoint, step $nsteps at " "$sim_name.log"; then
	echo "Simulation finished, cancelling pending jobs"
	scancel -t pending $SLURM_ARRAY_JOB_ID
fi
```

# Performance

Le guide [*Molecular Dynamics Performance Guide*](https://mdbench.ace-net.ca/mdbench/) a été créé par une équipe [d'ACENET](https://www.ace-net.ca/). Le guide décrit les conditions optimales pour exécuter aussi des tâches sur nos grappes avec AMBER, GROMACS, NAMD et OpenMM. Nous abordons ici la performance avec GROMACS.

Il n'est pas facile d'obtenir la meilleure performance mdrun et les développeurs de GROMACS y consacrent beaucoup d'information en rapport avec les options, paramètres et stratégies.[^7]

Il n'y a pas de solution universelle, mais le meilleur choix de paramètres dépend fortement de la taille du système (nombre de particules, taille et forme de la boite de simulation) et des paramètres de la simulation (rayons de coupure, utilisation de la sommation d'Ewald[^8]).

L'information et les statistiques de performance sont imprimées à la fin du fichier `md.log`, permettant de mieux identifier les goulots d'étranglement. On peut souvent y trouver aussi des notes sur comment améliorer la performance.

La **performance de la simulation** se mesure typiquement par le nombre de nanosecondes de trajectoire pouvant être simulée en un jour (ns/jour).

La **scalabilité parallèle** indique l'efficacité de l'utilisation des ressources de calcul. Elle se mesure comme suit :

S = p<sub>N</sub> / ( N * p<sub>1</sub> )

où *p<sub>N</sub>* représente la performance avec *N* cœurs CPU.

Idéalement, la performance s'accroît de façon linéaire avec le nombre de cœurs CPU.
(*scalabilité linéaire*; S = 1).

## Processus MPI / Tâches Slurm / Décomposition des domaines

La façon la plus simple d'augmenter le nombre de processus MPI (*MPI-ranks* dans la documentation GROMACS) est d'utiliser les options Slurm `--ntasks` ou `--ntasks-per-node` Slurm dans le script.

GROMACS utilise la méthode de **décomposition des domaines**[^9] (DD) pour distribuer sur plusieurs cœurs CPU la solution des interactions non liantes entre particules (PP). Ceci s'effectue en découpant en domaines la boite de simulation selon les axes X, Y et/ou Z et en assignant chacun des domaines à un processus MPI.

Ceci fonctionne bien jusqu'à ce que le temps exigé pour la communication devienne grand par rapport à la taille du domaine en termes de *nombre de particules* et de *volume du domaine*. La scalabilité parallèle tombe loin sous 1 et dans les cas extrêmes, la performance diminue avec l'augmentation du nombre de domaines.

GROMACS peut répartir la charge de façon dynamique (*dynamic load balancing*) pour déplacer dans une certaine mesure les frontières des domaines afin d'empêcher que certains prennent beaucoup plus de temps à résoudre que d'autres. Le paramètre `mdrun` est présent par défaut.

Dans chaque direction, un domaine ne peut pas être plus petit que le plus long rayon de coupure.

#### Sommation d'Ewald (PME) et interactions à distance

La sommation d'Ewald (PME ou *particle mesh Ewald method*) est souvent employée pour le calcul des interactions non liantes à distance, soit les interactions qui dépassent le rayon de coupure. Puisque cette méthode nécessite une communication globale, la performance peut se dégrader rapidement lorsque plusieurs processus MPI sont impliqués à la fois dans le calcul des interactions rapprochées protéine-protéine (PP) et des interactions à distance (PME). Pour éviter cette baisse de performance, des processus MPI traiteront uniquement des interactions PME.

Avec un total de plus de 12 processus MPI, mdrun utilise par défaut une méthode heuristique pour attribuer ces processus au calcul des interactions PME. Le nombre de rangs PME peut être sélectionné manuellement avec le paramètre mdrun `-npme`.

Dans le cas d'un débalancement de charge important entre les rangs PP et PME (c'est-à-dire que les rangs PP travaillent plus que les rangs PME au cours d'une étape), le travail peut être redirigé des rangs PP aux rangs PME en augmentant le rayon de coupure. Ceci n'aura aucun effet sur le résultat puisque la somme des forces (ou énergies) des interactions rapprochées et de celles à distance demeure la même pour une étape particulière. À partir de la version 4.6, mdrun tente de faire ceci automatiquement, sauf si le paramètre `-notunepme` est utilisé.

À partir de la version 2018, les interactions PME peuvent être redirigées vers un GPU (voir ci-dessous), mais la version 2018.1 présente toutefois plusieurs contraintes[^10] dont le fait qu'un seul rang GPU peut être dédié aux PME.

## Fils OpenMP / Nombre de CPU par tâche

Une fois que la décomposition des domaines atteint la limite de scalabilité (décroissance de la scalabilité parallèle), la performance peut encore être améliorée avec des **fils OpenMP** par la distribution du travail d'un processus MPI (rang) sur plus d'un cœur CPU. et `srun`. Pour ce faire, utilisez le paramètre `--cpus-per-task` dans le script (à la fois pour `#SBATCH` et `srun`).
Aussi, définissez la variable *OMP_NUM_THREADS* avec `export OMP_NUM_THREADS="${SLURM_CPUS_PER_TASK:-1}"` (recommandé)
ou le paramètre mdrun `-ntomp ${SLURM_CPUS_PER_TASK:-1}`.

Selon les programmeurs de GROMACS, le nombre optimal de fils OpenMP par processus MPI (CPU par tâche) se situe habituellement entre 2 et 6. Cependant, il vaut la peine d'augmenter le nombre de CPU par tâche dans le cas de tâches exécutées sur un nombre élevé de nœuds.

Surtout dans les cas où la méthode PME n'est pas employée, il n'est pas nécessaire de se soucier de *PP-PME Load Imbalance*; nous pouvons sélectionner 2 ou 4 *ntasks-per-node* et définir *cpus-per-task* par une valeur où *ntasks-per-node \* cpus-per-task* correspond au nombre de cœurs CPU dans un nœud de calcul.

## Architecture des CPU

GROMACS utilise des fonctions optimisées (*kernel functions*) pour calculer la portion réelle des interactions non liées à courte portée. Ces fonctions sont disponibles pour une variété de jeux d’instructions SIMD tels qu’AVX, AVX2 ou AVX512. Ces fonctions sont choisies lors de la compilation de GROMACS, et devraient correspondre aux capacités des CPU qui exécuteront les simulations. Cela est fait pour vous par notre équipe : quand vous ajoutez à votre environnement un module pour GROMACS, une version pour AVX/AVX2/AVX512 est choisie en fonction de l’architecture de la grappe de calculs. GROMACS indique quel jeu d’instructions SIMD il supporte dans le fichier du journal (log) et vous avertira si la fonction choisie est sous-optimale.

## GPU

!!! warning "En préparation"

    Contenu en préparation.

# Analyser les résultats

## Outils

*GROMACS* offre beaucoup d'outils pouvant être utilisés pour des tâches communes de post-traitement et d'analyse.
Le manuel de *GROMACS* contient [une liste des commandes disponibles selon le sujet](https://manual.gromacs.org/current/user-guide/cmdline.html#commands-by-topic) et aussi [selon le nom](https://manual.gromacs.org/current/user-guide/cmdline.html#commands-by-name); chaque commande est accompagnée d'une courte description et un lien conduit à l'information de référence.

Typiquement, ces commandes lisent la trajectoire (au format *XTC*, *TNG* ou *TRR*), un fichier de coordonnées (*GRO*, *PDB*, *TPR*, etc.) et produit un graphique [au format *XVG*](https://manual.gromacs.org/current/reference-manual/file-formats.html#xvg) qui peut être utilisé par [l'outil de traçage Grace](https://plasma-gate.weizmann.ac.il/Grace/); voir [Grace User Guide](https://plasma-gate.weizmann.ac.il/Grace/doc/UsersGuide.html). Comme les fichiers *XVG* sont des fichiers texte, ils peuvent être analysés par des scripts ou importés dans des feuilles de calcul.

## VMD

[VMD](vmd.md) est un programme de visualisation moléculaire pour afficher, animer et analyser de grands systèmes biomoléculaires à l'aide de graphiques 3D et de scripts intégrés. Il peut être utilisé pour inspecter visuellement les trajectoires GROMACS et offre également un grand nombre de plugiciels intégrés et externes pour l'analyse.
Il peut également être utilisé en mode ligne de commande.

## Utiliser Python

[MDAnalysis](https://www.mdanalysis.org/) et [MDTraj](https://www.mdtraj.org/) sont deux [Python](python.md) que nous offrons en [wheels Python précompilés](available-python-wheels.md). Ils peuvent lire et écrire des fichiers de trajectoires et de coordonnées GROMACS (*TRR* et *XTC*) et d'autres paquets de dynamique moléculaire, en plus d'offrir plusieurs fonctions d'analyse fréquemment employées. MDAnalysis peut aussi lire l'information topologique contenue dans les fichiers GROMACS *TPR*, mais pas toujours ceux produits par les récentes versions de GROMACS.

Les deux paquets disposent d'un langage de sélection d'atomes polyvalent et exposent les coordonnées des trajectoires, ce qui facilite l'écriture d'outils d'analyse personnalisés qui peuvent être adaptés à un problème particulier et bien s'intégrer aux paquets de science des données de Python tels que NumPy, SciPy et Pandas, et aux bibliothèques de traçage comme Matplotlib/Pyplot et Seaborn.

# Modules reliés

## GROMACS-PLUMED

PLUMED[^11] est une bibliothèque *open source* pour le calcul de l'énergie libre dans les systèmes moléculaires; elle fonctionne avec divers programmes de dynamique moléculaire.

Les modules `gromacs-plumed` sont des versions de GROMACS auxquelles des correctifs ont été apportés en fonction des modifications de PLUMED; ils peuvent exécuter des simulations métadynamiques.

Prenez note que la bibliothèque PLUMED native est activée pour les modules `gromacs` des versions 2025 et suivantes; elle peut être utilisée une fois que vous avez chargé un module `plumed`.

| GROMACS | PLUMED | modules pour utiliser les CPU                            | modules pour utiliser les GPU (CUDA)                                      | remarques             |
|:--------|:-------|:---------------------------------------------------------|:--------------------------------------------------------------------------|:----------------------|
| v2022.6 | v2.8.3 | `StdEnv/2020  gcc/9.3.0  openmpi/4.0.3  gromacs-plumed/2022.6` | `StdEnv/2020  gcc/9.3.0  cuda/11.4  openmpi/4.0.3  gromacs-plumed/2022.6` | GCC, FlexiBLAS & FFTW |
| v2022.3 | v2.8.1 | `StdEnv/2020  gcc/9.3.0  openmpi/4.0.3  gromacs-plumed/2022.3` | `StdEnv/2020  gcc/9.3.0  cuda/11.4  openmpi/4.0.3  gromacs-plumed/2022.3` | GCC, FlexiBLAS & FFTW |
| v2021.6 | v2.7.4 | `StdEnv/2020  gcc/9.3.0  openmpi/4.0.3  gromacs-plumed/2021.6` | `StdEnv/2020  gcc/9.3.0  cuda/11.4  openmpi/4.0.3  gromacs-plumed/2021.6` | GCC, FlexiBLAS & FFTW |
| v2021.4 | v2.7.3 | `StdEnv/2020  gcc/9.3.0  openmpi/4.0.3  gromacs-plumed/2021.4` | `StdEnv/2020  gcc/9.3.0  cuda/11.4  openmpi/4.0.3  gromacs-plumed/2021.4` | GCC, FlexiBLAS & FFTW |
| v2021.2 | v2.7.1 | `StdEnv/2020  gcc/9.3.0  openmpi/4.0.3  gromacs-plumed/2021.2` | `StdEnv/2020  gcc/9.3.0  cuda/11.0  openmpi/4.0.3  gromacs-plumed/2021.2` | GCC & MKL             |
| v2019.6 | v2.6.2 | `StdEnv/2020  gcc/9.3.0  openmpi/4.0.3  gromacs-plumed/2019.6` | `StdEnv/2020  gcc/9.3.0  cuda/11.0  openmpi/4.0.3  gromacs-plumed/2019.6` | GCC & MKL             |
| v2019.6 | v2.5.4 | `StdEnv/2018.3  gcc/7.3.0  openmpi/3.1.2  gromacs-plumed/2019.6` | `StdEnv/2018.3  gcc/7.3.0  cuda/10.0.130  openmpi/3.1.2 gromacs-plumed/2019.6` | GCC & MKL             |
| v2019.5 | v2.5.3 | `StdEnv/2018.3  gcc/7.3.0  openmpi/3.1.2  gromacs-plumed/2019.5` | `StdEnv/2018.3  gcc/7.3.0  cuda/10.0.130  openmpi/3.1.2 gromacs-plumed/2019.5` | GCC & MKL             |
| v2018.1 | v2.4.2 | `StdEnv/2016.4  gcc/6.4.0  openmpi/2.1.1  gromacs-plumed/2018.1` | `StdEnv/2016.4  gcc/6.4.0  cuda/9.0.176  openmpi/2.1.1 gromacs-plumed/2018.1` | GCC & FFTW            |
| v2016.3 | v2.3.2 | `StdEnv/2016.4  intel/2016.4  openmpi/2.1.1  gromacs-plumed/2016.3` | `StdEnv/2016.4  intel/2016.4  cuda/8.0.44  openmpi/2.1.1  gromacs-plumed/2016.3` | Intel & MKL           |

## GROMACS-Colvars

Colvars[^12] est un module logiciel qui ajoute aux programmes de simulation moléculaire les variables collectives avancées pour l'application de potentiels de polarisation; le calcul les potentiels de force moyenne (PMF) pour tous les ensembles de variables; et l'utilisation de méthodes avancées d'échantillonnage comme la force de polarisation adaptative (ABF pour *Adaptive Biasing Force*), la métadynamique, la dynamique moléculaire dirigée et l'échantillonnage parapluie.

À partir de GROMACS v2024[^13], la bibliothèque Colvars est ajoutée aux versions officielles sans devoir recourir à une version corrigée.

Documentation :
* *Collective Variable simulations with the Colvars module*[^14];
* Molecular dynamics parameters (.mdp options) for the Colvars module[^15],
* *Colvars Reference manual for GROMACS*[^16],
* Fiorin et al. **2013**, *Using collective variables to drive molecular dynamics simulations.*[^17]

Les versions de GROMACS antérieures à v2024 auxquelles on a ajouté les modifications de Colvars pour permettre l'utilisation de variables collectives avancées dans les simulations.

| GROMACS | Colvars    | modules pour utiliser les CPU                               | modules pour utiliser les GPU (CUDA)                                       | remarques             |
|:--------|:-----------|:------------------------------------------------------------|:---------------------------------------------------------------------------|:----------------------|
| v2020.6 | 2021-12-20 | `StdEnv/2020  gcc/9.3.0  openmpi/4.0.3  gromacs-colvars/2020.6` | `StdEnv/2020  gcc/9.3.0  cuda/11.4  openmpi/4.0.3  gromacs-colvars/2020.6` | GCC, FlexiBLAS & FFTW |

## GROMACS+CP2K

CP2K[^18] est un progiciel de chimie quantique et de physique du solide. Depuis 2022, GROMACS peut être compilé pour prendre en charge les simulations hybrides quantiques-classiques (QM/MM)[^19] avec CP2K[^20].

Les modules `gromacs-cp2k` sont des versions de GROMACS qui ont été compilées avec le support de QM/MM avec CP2K.

Ils sont différents d'autres modules en ce qu'ils peuvent être utilisés uniquement pour les calculs avec CPU et non avec GPU (CUDA). De plus, ils contiennent uniquement des exécutables compatibles avec MPI :

* **`gmx_mpi`** - GROMACS en mixte précision avec OpenMP et MPI.
* **`gmx_mpi_d`** - GROMACS en double précision avec OpenMP et MPI.

| GROMACS | CP2K | modules for running on CPUs                                | remarques             |
|:--------|:-----|:-----------------------------------------------------------|:----------------------|
| v2022.2 | 9.1  | `StdEnv/2020  gcc/9.3.0  openmpi/4.0.3  gromacs-cp2k/2022.2` | GCC, FlexiBLAS & FFTW |

Les ressources suivantes sont pour les simulations QM/MM avec cette combinaison de GROMACS et CP2K.

* Documentation GROMACS, [Simulations hybrides quantiques-classiques (QM/MM) avec l'interface CP2K](https://manual.gromacs.org/documentation/current/reference-manual/special/qmmm.html).
* BioExcel, [Guide des meilleures pratiques QM/MM de CP2K](https://docs.bioexcel.eu/qmmm_bpg/).
* BioExcel, atelier [QM/MM avec GROMACS + CP2K](https://docs.bioexcel.eu/2021-04-22-qmmm-gromacs-cp2k/)
    Comprend un tutoriel sur comment préparer et faire exécuter des simulations QM/MM et des liens vers des vidéos théoriques sur YouTube. Le tutoriel est conçu pour les ressources de CIP de BioExcel (European Centre of Excellence for Computational Biomolecular Research), mais peut être suivi sur nos systèmes avec quelques légères modifications.
    En particulier, il faut remplacer `gmx_cp2k` par `gmx_mpi` (mixte précision) ou `gmx_mpi_d` (double précision) et modifier les scripts de tâches qui sont aussi pris en charge par Slurm.
    * [Répertoire GitHub](https://github.com/bioexcel/2022-06-16-gromacs-cp2k-tutorial), comprend un fichier en exemple pour le tutoriel de BioExcel.
* Site Web de CP2K, [Intégration GROMACS-CP2K](https://www.cp2k.org/tools:gromacs).

## GROMACS-LS

GROMACS-LS[^21] et la bibliothèque MDStress library permettent le calcul de champs de contraintes locaux à partir de simulations de dynamique moléculaire.
La bibliothèque MDStress est incluse dans le module GROMACS-LS.

Le manuel [Local_stress.pdf](https://vanegaslab.org/files/Local_stress.pdf) contient l'information sur la méthode ainsi que plusieurs publications pour référence.

L'appel de commandes telles que `gmx_LS mdrun -rerun` et `gmx_LS trjconv` nécessite un fichier `.tpr`.
Si vous souhaitez analyser une trajectoire qui a été simulée avec une version plus récente de GROMACS (par exemple 2024), une version plus ancienne ne peut pas lire ce fichier .tpr car de nouvelles options sont ajoutées à la spécification de format à chaque version majeure (2018, 2019... 2024).
Mais comme le suggère la réponse à la question 14 dans le document [Local_stress.pdf](https://vanegaslab.org/files/Local_stress.pdf), vous pouvez utiliser `gmx_LS grompp` ou `gmx grompp` de la version 2016.6 (qui est également disponible) pour créer un nouveau fichier .tpr en utilisant les mêmes fichiers d'entrée (*.mdp, topol.top, *.itp, *.gro, etc.) qui ont été utilisés pour créer le fichier `.tpr` de la simulation.
Ce nouveau .tpr est alors compatible avec GROMACS-LS 2016.3.
Si les fichiers `*.mdp` utilisaient des mots-clés ou des fonctionnalités qui n'étaient pas encore présents en 2016 (par exemple, `pcouple = C-rescale`), vous devez alors les modifier ou les supprimer (par exemple, `pcouple = Berendsen`).
Dans le cas de pcouple, le résultat ne sera pas différent de toute façon, car la trajectoire est traitée comme avec l'option `-rerun` et le couplage de pression ne se produira pas dans ce cas.
La mention de `cutoff-scheme = group` dans la réponse à la question 14 peut être ignorée, car GROMACS 2016 prend déjà en charge `cutoff-scheme = Verlet` et le schéma « group » a été supprimé pour GROMACS 2020.
Par conséquent, GROMACS-LS 2016.3 peut être utilisé pour traiter des simulations utilisant l'une ou l'autre des méthodes de coupure.

Remarques :

* Étant donné que le manuel a été écrit pour GROMACS-LS v4.5.5 et que les commandes de base ont changé dans la version 5, vous devez utiliser des commandes comme `gmx_LS mdrun` et `gmx_LS trjconv` au lieu de `mdrun_LS` et `trjconv_LS`.
* GROMACS-LS nécessite d'être compilé en double précision, ne prend pas en charge MPI, l'accélération matérielle SIMD, ni les GPU et est donc beaucoup plus lent que la version non optimisée de GROMACS. Il ne peut utiliser qu'un seul cœur CPU.
* Contrairement aux autres versions corrigées de GROMACS, les modules `gromacs-ls/2016.3` et `gromacs/2016.6` peuvent être chargés en même temps.

| module          | modules pour utiliser les CPUs                               | remarques                                                              |
|:----------------|:-------------------------------------------------------------|:-----------------------------------------------------------------------|
| gromacs-ls/2016.3 | `StdEnv/2023  gcc/12.3  gromacs-ls/2016.3`                   | GROMACS-LS est une application séquentielle qui ne supporte pas MPI, OpenMP ou GPUs/CUDA. |
| gromacs/2016.6  | `StdEnv/2023  gcc/12.3  openmpi/4.1.5  gromacs/2016.6`       | Ce module peut être utilisé pour préparer des fichier *tpr* en entrée pour GROMACS-LS. |

## GROMACS-RAMD

GROMACS-RAMD est un dérivé de GROMACS qui implémente la méthode RAMD (*Random Acceleration Molecular Dynamics*).[^22]
Cette méthode peut être employée pour identifier les voies de sortie des ligands à partir des poches de liaison enterrées des récepteurs et étudier le mécanisme de dissociation des ligands par l'exécution de simulations de dynamique moléculaire avec une force supplémentaire orientée au hasard appliquée à une molécule du système.

Vous trouverez l'information sur les [Options RAMD](https://github.com/HITS-MCM/gromacs-ramd#usage) dans la page [GitHub GROMACS-RAMD](https://github.com/HITS-MCM/gromacs-ramd).

| GROMACS | RAMD | modules pour utilisation avec CPU                                    | modules pour utilisation avec GPU (CUDA)                                             | remarques             |
|:--------|:-----|:---------------------------------------------------------------------|:-------------------------------------------------------------------------------------|:----------------------|
| v2024.1 | 2.1  | `StdEnv/2023  gcc/12.3  openmpi/4.1.5  gromacs-ramd/2024.1-RAMD-2.1` | `StdEnv/2023  gcc/12.3  openmpi/4.1.5  cuda/12.2  gromacs-ramd/2024.1-RAMD-2.1`     | GCC, FlexiBLAS & FFTW |
| v2020.5 | 2.0  | `StdEnv/2020  gcc/9.3.0  openmpi/4.0.3  gromacs-ramd/2020.5-RAMD-2.0` | `StdEnv/2020  gcc/9.3.0  cuda/11.4  openmpi/4.0.3  gromacs-ramd/2020.5-RAMD-2.0` | GCC, FlexiBLAS & FFTW |

## GROMACS-SWAXS

[Page d'accueil GROMACS-SWAXS](https://biophys.uni-saarland.de/software/gromacs-swaxs/)[^23]
est une version modifiée de GROMACS pour calculer des courbes de diffusion de rayons X ou de neutrons à petit et grand angles (SAXS/SANS)
et pour effectuer des simulations de dynamique moléculaire pilotées par SAXS/SANS.

Veuillez vous référer à la [documentation GROMACS-SWAXS](https://cbjh.gitlab.io/gromacs-swaxs-docs/) pour des tutoriels et pour
la description des fonctionnalités (options d'entrée et de sortie de mdrun, options mpd, utilisation des commandes `gmx genscatt`
et `gmx genenv`) qui ont été ajoutées aux fonctionnalités GROMACS usuelles.

| GROMACS | SWAXS | avec CPU                                                       | avec GPU (CUDA)                                                      | remarques             |
|:--------|:------|:---------------------------------------------------------------|:---------------------------------------------------------------------|:----------------------|
| v2021.7 | 0.5.1 | `StdEnv/2023  gcc/12.3  openmpi/4.1.5  gromacs-swaxs/2021.7-0.5.1` | `StdEnv/2023  gcc/12.3  openmpi/4.1.5  cuda/12.2  gromacs-swaxs/2021.7-0.5.1` | GCC, FlexiBLAS & FFTW |

## G_MMPBSA

!!! warning "Obsolète"
    [L'environnement logiciel StdEnv/2016.4](standard-software-environments.md) n'est plus pris en charge. La dernière mise à jour de `g_mmpbsa` date d'avril 2016. Utilisez plutôt [gmx_MMPBSA](#gmx_mmpbsa)[^24].

[G_MMPBSA](http://rashmikumari.github.io/g_mmpbsa/)[^25] est un outil de calcul des composantes de l'énergie de liaison qui utilise la méthode MM-PBSA, à l'exception de la composante entropique et la contribution énergétique de chaque résidu, par l'utilisation de principes de décomposition de l'énergie.

Le développement de G_MMPBSA semble s'être arrêté en avril 2016; il n'est donc compatible qu'avec GROMACS 5.1.x.
Pour les versions plus récentes de GROMACS, vous pourriez utiliser [gmx_MMPBSA](#gmx_mmpbsa)[^26] (voir ci-dessous).

La version installée peut être chargée avec `module load StdEnv/2016.4 gcc/5.4.0 g_mmpbsa/2016-04-19`. Il s'agit de la plus récente version constituée de la version 1.6 et de modifications la rendant compatible avec GROMACS 5.1.x; elle a été compilée avec `gromacs/5.1.5` et `apbs/1.3`.

Notez que G_MMPBSA utilise des solvants implicites et que certaines études[^27] ont démontré que les méthodes de calcul des énergies libres liantes présentent certains problèmes de précision.

## gmx_MMPBSA

[Page d'accueil de gmx_MMPBSA](https://valdes-tresanco-ms.github.io/gmx_MMPBSA/dev/getting-started/)[^28]
est un outil basé sur le MMPBSA.py d'[AMBER](amber.md) pour le calcul de l'état final de l'énergie libre à l'aide de fichiers GROMACS.

Outre [G_MMPBSA](#g_mmpbsa)[^29] qui est moins récent et seulement compatible avec les versions plus anciennes de GROMACS,
gmx_MMPBSA peut être utilisé avec les versions courantes de GROMACS et [AmberTools](amber.md#ambertools-21).

Il faut savoir que gmx_MMPBSA utilise des solvants implicites et que certaines études [^30] ont démontré que les méthodes de calcul des énergies libres liantes présentent certains problèmes de précision.

### Scripts de soumission

Le script suivant installe et exécute gmx_MMPBSA dans un répertoire temporaire du disque local d'un nœud de calcul. Les tâches MPI doivent toutes être sur le même nœud. Pour soumettre une tâche sur plusieurs nœuds, installez un environnement virtuel dans un système de fichiers partagé.

```sh linenums="1" title="job_gmx_MMPBSA.sh"
#!/bin/bash
#SBATCH --ntasks=5 
#SBATCH --nodes=1
#SBATCH --mem-per-cpu=4000M 
#SBATCH --time=3:0:0 
 
module load StdEnv/2023 ambertools/23.5 gromacs/2024.4 
virtualenv $SLURM_TMPDIR/venv-gmxMMPBSA
source $SLURM_TMPDIR/venv-gmxMMPBSA/bin/activate
pip install --no-index gmx_MMPBSA==1.6.3
 
srun gmx_MMPBSA -O -nogui -i mmpbsa.in \
    -cs com.tpr \
    -ct com_traj.xtc \
    -ci index.ndx \
    -cg 3 4 \
    -cp topol.top \
    -o FINAL_RESULTS_MMPBSA.dat \
    -eo FINAL_RESULTS_MMPBSA.csv
```

### Installer gmx_MMPBSA dans un environnement virtuel

Pour utiliser la visualisation interactive, gmx_MMPBSA doit être installé dans un répertoire permanent.

#### Installation pour gromacs/2024 (StdEnv/2023)

```bash
module load  StdEnv/2023  ambertools/23.5  gromacs/2024.4  qt/5.15.11
virtualenv venv-gmxMMPBSA 
source venv-gmxMMPBSA/bin/activate 
pip install --no-index gmx_MMPBSA==1.6.3 
```

Test

```bash
git clone https://github.com/Valdes-Tresanco-MS/gmx_MMPBSA 
cd gmx_MMPBSA/examples/Protein_DNA
gmx_MMPBSA -O -i mmpbsa.in -cs com.tpr -ct com_traj.xtc -ci index.ndx -cg 3 4 -cp topol.top \ 
                            -o FINAL_RESULTS_MMPBSA.dat -eo FINAL_RESULTS_MMPBSA.csv -no -nogui
```

#### Installation pour gromacs/2021 (StdEnv/2020)

1. Chargez les modules nécessaires et créez l'environnement virtuel.

```bash
module purge
module load StdEnv/2020 gcc/9.3.0 python/3.8  gromacs/2021.4
module load ambertools/21
virtualenv venv_gmxMMPBSA
source venv_gmxMMPBSA/bin/activate
pip install -U pip
pip install --no-index numpy==1.22.2 seaborn==0.13.1 gmx_MMPBSA==1.5.0.3 ParmEd==3.4.4
```

2. Une fois que l'environnement virtuel est prêt, chargez le module Qt/PyQt.

```bash
module load qt/5.15.2
```

3. Testez l'application principale.

```bash
gmx_MMPBSA -h
gmx_MMPBSA_test -ng -n 4
```

Heureusement, le test s'effectue rapidement et vous pouvez l'exécuter sur le nœud de connexion.

Par la suite, quand vous utiliserez gmx_MMPBSA dans une tâche, vous devrez charger les modules et activez l'environnement virtuel comme suit :

```bash
module purge
module load StdEnv/2020 gcc/9.3.0 python/3.8 ambertools/21 gromacs/2021.4 qt/5.15.2
source venv_gmxMMPBSA/bin/activate
```

# Liens utiles

[Simulation biomoléculaire](biomolecular-simulation.md)

* Ressources de projet
    * Site Web principal : <http://www.gromacs.org/>
    * [Documentation GROMACS](http://manual.gromacs.org/documentation/)
    * Forums des utilisateurs de GROMACS : <https://gromacs.bioexcel.eu/>
        Les forums ont succédé aux listes de diffusion.
* Tutoriels
    * Sept très bons tutoriels : <http://www.mdtutorials.com/gmx/>
    * [Autres tutoriels](http://www.gromacs.org/Documentation/Tutorials)
* Ressources externes
    * Outil de génération de petits fichiers de topologie de molécules : <http://www.ccpn.ac.uk/v2-software/software/ACPYPE-folder>
    * Base de données avec topologies de champs de force (CGenFF, GAFF et OPLS/AA) pour petites molécules : <http://www.virtualchemistry.org/>
    * Service Web pour la génération de topologies de petites molécules pour champs de force GROMACS : <https://atb.uq.edu.au/>
    * Discussion sur les meilleures configurations : [Best bang for your buck: GPU nodes for GROMACS biomolecular simulations](https://arxiv.org/abs/1507.00898)

# Références

[^1]: "Fix missing synchronization in CUDA update kernels" in [GROMACS 2021.6 Release Notes](https://manual.gromacs.org/2021.6/release-notes/2021/2021.6.html#fix-missing-synchronization-in-cuda-update-kernels)
[^2]: Issue #4393 in GROMACS Project on [GitLab.com](https://gitlab.com/gromacs/gromacs/-/issues/4393)
[^3]: "Fix missing synchronization in CUDA update kernels" in [GROMACS 2021.6 Release Notes](https://manual.gromacs.org/2021.6/release-notes/2021/2021.6.html#fix-missing-synchronization-in-cuda-update-kernels)
[^4]: Issue #4393 in GROMACS Project on [GitLab.com](https://gitlab.com/gromacs/gromacs/-/issues/4393)
[^5]: [GROMACS User Guide: Managing long simulations.](http://manual.gromacs.org/documentation/current/user-guide/managing-simulations.html)
[^6]: [GROMACS Manual page: gmx mdrun](http://manual.gromacs.org/documentation/current/onlinehelp/gmx-mdrun.html#gmx-mdrun)
[^7]: [GROMACS User-Guide: Getting good performance from mdrun](http://manual.gromacs.org/documentation/current/user-guide/mdrun-performance.html)
[^8]: [GROMACS User-Guide: Performance background information](http://manual.gromacs.org/documentation/current/user-guide/mdrun-performance.html#gromacs-background-information)
[^9]: [GROMACS User-Guide: Performance background information](http://manual.gromacs.org/documentation/current/user-guide/mdrun-performance.html#gromacs-background-information)
[^10]: [GROMACS User-Guide: GPU accelerated calculation of PME](http://manual.gromacs.org/documentation/2018.1/user-guide/mdrun-performance.html#gpu-accelerated-calculation-of-pme)
[^11]: [Site Web PLUMED](http://www.plumed.org/home)
[^12]: [Site Web Colvars](https://colvars.github.io/)
[^13]: [GROMACS 2024 Major Release Highlights](https://manual.gromacs.org/2024.1/release-notes/2024/major/highlights.html)
[^14]: [Collective Variable simulations with the Colvars module (GROMACS 2024.2)](https://manual.gromacs.org/current/reference-manual/special/colvars.html)
[^15]: [Colvars .mdp Options (GROMACS 2024.2)](https://manual.gromacs.org/current/user-guide/mdp-options.html#collective-variables-colvars-module)
[^16]: [Colvars Reference manual for GROMACS](https://colvars.github.io/colvars-refman-gromacs/colvars-refman-gromacs.html)
[^17]: [Fiorin et al. **2013**, *Using collective variables to drive molecular dynamics simulations.*](http://dx.doi.org/10.1080/00268976.2013.813594)
[^18]: [CP2K Home](https://www.cp2k.org/)
[^19]: [QM/MM avec CP2K dans le manuel de référence GROMACS](https://manual.gromacs.org/documentation/current/reference-manual/special/qmmm.html)
[^20]: [Compilation de GROMACS avec le support QM/MM de CP2K](https://manual.gromacs.org/documentation/current/install-guide/index.html#building-with-cp2k-qm-mm-support)
[^21]: [GROMACS-LS et la bibliothèque MDStress](https://vanegaslab.org/software)
[^22]: [Information sur la méthode RAMD](https://kbbox.h-its.org/toolbox/methods/molecular-simulation/random-acceleration-molecular-dynamics-ramd/)
[^23]: [Page d'accueil GROMACS-SWAXS](https://biophys.uni-saarland.de/software/gromacs-swaxs/)
[^24]: [Site Web G_MMPBSA](http://rashmikumari.github.io/g_mmpbsa/)
[^25]: [Site Web G_MMPBSA](http://rashmikumari.github.io/g_mmpbsa/)
[^26]: [Site Web G_MMPBSA](http://rashmikumari.github.io/g_mmpbsa/)
[^27]: [Comparison of Implicit and Explicit Solvent Models for the Calculation of Solvation Free Energy in Organic Solvents](http://pubs.acs.org/doi/abs/10.1021/acs.jctc.7b00169)
[^28]: [gmx_MMPBSA Homepage](https://valdes-tresanco-ms.github.io/gmx_MMPBSA/dev/getting-started/)
[^29]: [Site Web G_MMPBSA](http://rashmikumari.github.io/g_mmpbsa/)
[^30]: [Comparison of Implicit and Explicit Solvent Models for the Calculation of Solvation Free Energy in Organic Solvents](http://pubs.acs.org/doi/abs/10.1021/acs.jctc.7b00169)