---
title: "NAMD/fr"
slug: "namd"
lang: "fr"

source_wiki_title: "NAMD/fr"
source_hash: "ec3d33d81db5eda936473a9b0554c7d1"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:39:09.437295+00:00"

tags:
  - software
  - biomolecularsimulation

keywords:
  - "dynamique moléculaire"
  - "performance"
  - "grappe Graham"
  - "fichier de configuration"
  - "calcul de l'efficacité"
  - "Slurm"
  - "cœurs"
  - "nœuds CPU et GPU"
  - "NAMD 3"
  - "nœuds GPU"
  - "Tutoriels"
  - "NAMD"
  - "GPU"
  - "paramètre d'entrée"
  - "étalonnage"
  - "Références"
  - "cœurs CPU"
  - "tâches multifils"
  - "scripts de soumission"
  - "SLURM"
  - "Télécharger"
  - "étalonnage standard apoa1"
  - "NAMD 2.12"
  - "GPUresident"
  - "exécutable"

questions:
  - "Quel est le but principal du logiciel NAMD et quel autre outil est utilisé pour préparer et analyser ses simulations ?"
  - "Quelles sont les limitations de compatibilité matérielle à prendre en compte lors du choix de la version de NAMD, notamment en ce qui concerne les GPU ?"
  - "Quel paramètre spécifique doit-on ajouter au fichier d'entrée de NAMD 3 pour améliorer considérablement les performances lors de l'exécution d'une tâche avec GPU ?"
  - "Jusqu'à quelle limite est-il possible d'augmenter le nombre de cœurs CPU et de GPU ?"
  - "Quel est l'avantage principal du nouveau paramètre d'entrée introduit dans NAMD 3 ?"
  - "Quelle ligne spécifique doit-on ajouter au fichier d'entrée pour diriger davantage de calculs vers le GPU ?"
  - "Quelles sont les configurations recommandées pour exécuter efficacement des tâches NAMD sur plusieurs nœuds GPU, comme illustré avec l'exemple de la grappe Narval ?"
  - "Pourquoi est-il déconseillé d'utiliser la version 2.14 de NAMD sur les grappes de calcul équipées de GPU H100 ?"
  - "Quelle est la méthode suggérée pour réaliser un étalonnage (benchmarking) précis des performances de NAMD et à quoi peuvent servir les données ainsi récoltées ?"
  - "Pourquoi est-il déconseillé de demander un nombre excessif de cœurs pour une simulation et quelle est la limite acceptable selon le premier étalonnage ?"
  - "Quelle est la configuration optimale recommandée pour l'utilisation des GPU sur un seul nœud, et pourquoi faut-il éviter de répartir la tâche sur plusieurs nœuds ?"
  - "Quelles sont les étapes à suivre pour télécharger, configurer et optimiser NAMD 3 afin d'améliorer les performances sur les systèmes utilisant des GPU ?"
  - "Quelles sont les caractéristiques matérielles des nœuds CPU et GPU de la grappe Graham utilisée pour l'étalonnage ?"
  - "Quel logiciel et quel module spécifique sont utilisés dans le premier tableau de l'exercice ?"
  - "Quelle est la formule mathématique employée pour calculer l'efficacité de l'étalonnage ?"
  - "Où peut-on trouver plus d'informations concernant le paramètre \"GPUresident on\" et ses modifications ?"
  - "Quelle est la condition requise pour pouvoir télécharger le logiciel NAMD via le lien fourni ?"
  - "Quelles sont les versions spécifiques de NAMD pour lesquelles des guides d'utilisation et des notes de version sont disponibles dans les références ?"
  - "Que se passe-t-il avec l'exécutable namd3 une fois le script exécuté dans le répertoire ?"
  - "Quelle action l'utilisateur peut-il accomplir après la liaison de l'exécutable aux librairies ?"
  - "Comment peut-on optimiser les performances de NAMD 3 lors de son utilisation sur un GPU ?"
  - "Où peut-on trouver plus d'informations concernant le paramètre \"GPUresident on\" et ses modifications ?"
  - "Quelle est la condition requise pour pouvoir télécharger le logiciel NAMD via le lien fourni ?"
  - "Quelles sont les versions spécifiques de NAMD pour lesquelles des guides d'utilisation et des notes de version sont disponibles dans les références ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[NAMD](http://www.ks.uiuc.edu/Research/namd/) est un logiciel de dynamique moléculaire orienté-objet conçu pour la simulation de gros systèmes biomoléculaires.
Les simulations sont préparées et analysées dans le logiciel de visualisation [VMD](vmd.md).

## Installation
Le logiciel est installé par notre équipe technique et est disponible via des modules. Si vous avez besoin d'une version plus récente, que vous devez faire vous-même l'installation ou que vous avez des questions, contactez le [soutien technique](../support/technical_support.md).

## Modules d'environnement
La plus récente version 3.0.2 (27 août 2025) est installée sur toutes nos grappes; elle comporte [plusieurs améliorations](https://www.ks.uiuc.edu/Research/namd/3.0.2/announce.html) en comparaison de la version 3.0.1. La version 2.14 est aussi disponible, mais elle ne peut pas être utilisée avec des GPU H100. Vous pouvez utiliser la version GPU seulement sur Narval.

Pour les tâches exécutées sur plusieurs nœuds, utilisez UCX.

## Scripts de soumission des tâches
L'information sur l'ordonnanceur Slurm se trouve à la page [Exécuter des tâches](../running-jobs/running_jobs.md).

### Tâches multifils avec CPU
Le script suivant est pour une simulation multifil. Pour utiliser plus de cœurs, augmentez la valeur de `--cpus-per-task`, sans dépasser le nombre de cœurs disponibles sur le nœud. Pour déterminer le nombre de cœurs à utiliser, voyez *Performance et étalonnage* plus loin.

```sh title="serial_namd_job.sh"
#!/bin/bash
#
#SBATCH --cpus-per-task=8
#SBATCH --mem 10g            # memory in Mb, increase as needed    
#SBATCH -o slurm.%N.%j.out    # STDOUT file
#SBATCH -t 0:05:00            # time (D-HH:MM), increase as needed
#SBATCH --account=def-specifyaccount

module load StdEnv/2023  gcc/12.3 namd-multicore/3.0.2
namd3 +p$SLURM_CPUS_PER_TASK  +idlepoll +setcpuaffinity stmv.namd
```

### Tâches sur plusieurs nœuds avec CPU

#### Tâches UCX
L'exemple suivant est pour 384 tâches sur 2 nœuds à raison de 192 tâches par nœud. Le script suppose que des nœuds entiers sont utilisés; ainsi, `ntasks-per-node` devrait être égal au nombre de cœurs disponibles pour le nœud (192 sur Fir, Rorqual, Nibi et Trillium). Pour une meilleure performance, les tâches UCX devraient utiliser des nœuds entiers. Utilisez la version UCX uniquement si la version multicœurs de NAMD ne convient pas à vos besoins et que vous avez besoin de plusieurs nœuds.

```sh title="ucx_namd_job.sh"
#!/bin/bash
#
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=192
#SBATCH --mem=0            # memory per node, 0 means all memory
#SBATCH -o slurm.%N.%j.out    # STDOUT
#SBATCH -t 0:05:00            # time (D-HH:MM)
#SBATCH --account=def-specifyaccount

module load StdEnv/2023 gcc/13.3 namd-ucx/3.0.2
srun --mpi=pmi2 namd3 stmv.namd
```

#### Tâches multifil avec GPU
Le prochain exemple utilise 16 cœurs CPU et un GPU P100 sur un seul nœud. Le nombre de cœurs CPU et de GPU peut être augmenté jusqu'au maximum pour le nœud.

!!! important
    NAMD 3 offre un nouveau paramètre d’entrée, ce qui dirige plus de calculs vers le GPU. Cela peut améliorer considérablement la performance.

    Pour l'utiliser, ajoutez la ligne suivante à votre fichier en entrée :
    ```
    GPUresident on;
    ```

```sh title="multicore_gpu_namd_job.sh"
#!/bin/bash

#SBATCH --cpus-per-task=16 
#SBATCH --mem=10g    
#SBATCH --time=0:15:00
#SBATCH --gpus-per-node=h100:1
#SBATCH --account=def-specifyaccount

module load StdEnv/2023  gcc/12.3  cuda/12.6 namd-multicore/3.0.2
namd3 +p$SLURM_CPUS_PER_TASK  +idlepoll stmv.namd
```

### Tâches avec plusieurs nœuds GPU
#### Tâches UCX avec GPU
Puisqu'un seul nœud GPU offre une bonne puissance de calcul, leur utilisation est justifiée uniquement quand la tâche peut les utiliser à leur plein potentiel.

Cet exemple est pour Narval et suppose que des nœuds entiers sont utilisés, ce qui offre une meilleure performance pour les tâches NAMD. L'exemple est pour 8 tâches sur 2 nœuds, chacune utilisant 12 fils et 1 GPU. Ceci utilise pleinement les nœuds GPU de Narval qui ont 48 cœurs et 4 GPU par nœud. Remarquez que 1 cœur par tâche est réservé à un fil de communication; il est donc normal que NAMD ne rapporte que 88 cœurs utilisés.

Pour utiliser ce script sur une autre grappe, voyez les caractéristiques des nœuds disponibles sur la grappe et ajustez les options `--cpus-per-task` et `--gpus-per-node` en conséquence.

!!! warning "Remarque"
    Dans cet exemple, la version 2.14 ne devrait pas être utilisée sur les grappes qui ont des GPU H100. La version UCX NAMD 3.0.1 pour les GPU H100 n'est pas encore installée sur nos grappes.

```sh title="ucx_namd_job.sh"
#!/bin/bash

#SBATCH --nodes=2
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=12 # number of threads per task (process)
#SBATCH --gpus-per-node=a100:4
#SBATCH --mem=0            # memory per node, 0 means all memory
#SBATCH --time=0:15:00
#SBATCH --account=def-specifyaccount

module load StdEnv/2020  intel/2020.1.217  cuda/11.0 namd-ucx-smp/2.14
NUM_PES=$(expr $SLURM_CPUS_PER_TASK - 1 )
srun --cpus-per-task=$SLURM_CPUS_PER_TASK --mpi=pmi2 namd2 ++ppn $NUM_PES stmv.namd
```

## Performance et étalonnage
Le guide [*Molecular Dynamics Performance Guide*](https://mdbench.ace-net.ca/mdbench/) a été créé par une équipe [d'ACENET](https://www.ace-net.ca/). Le guide décrit les conditions optimales pour exécuter aussi des tâches sur nos grappes avec AMBER, GROMACS et OpenMM.

Voici un exemple d'étalonnage. La performance de NAMD varie selon les systèmes simulés, en rapport particulièrement avec la quantité d'atomes. Il serait donc très utile d'effectuer le type d'étalonnage montré ici dans les cas où la simulation d'un système particulier serait de longue durée. Les données ainsi collectées peuvent aussi servir à documenter vos demandes aux concours d'allocation de ressources.

Pour obtenir des résultats pertinents, nous vous suggérons de varier le nombre d'étapes pour que la simulation du système se fasse sur quelques minutes et que la collecte des données de durée se fasse à des intervalles d'au moins quelques secondes. Vous pourriez remarquer des variations dans vos résultats de durée si le temps d'exécution est trop court.

Les données ci-dessous proviennent d'un étalonnage standard apoa1 effectué sur la grappe Graham qui possède des nœuds CPU de 32 cœurs et des nœuds GPU de 32 cœurs et 2 GPU. Pour faire le même exercice avec une autre grappe, vous devrez tenir compte de la structure de ses nœuds.

Dans le premier tableau, nous utilisons NAMD 2.12 chargé du module verbs. L'efficacité est calculée avec (durée avec 1 cœur) / (N * (durée avec N cœurs)).

| # cœurs | Durée réelle par étape | Efficacité |
| :------ | :--------------------- | :--------- |
| 1       | 0.8313                 | 100%       |
| 2       | 0.4151                 | 100%       |
| 4       | 0.1945                 | 107%       |
| 8       | 0.0987                 | 105%       |
| 16      | 0.0501                 | 104%       |
| 32      | 0.0257                 | 101%       |
| 64      | 0.0133                 | 98%        |
| 128     | 0.0074                 | 88%        |
| 256     | 0.0036                 | 90%        |
| 512     | 0.0021                 | 77%        |

Dans ce cas, nous constatons qu'il est acceptable d'utiliser 256 cœurs pour simuler le système. Si vous demandez plus de cœurs qu'il n'en faut, vos tâches seront plus longtemps en attente et votre résultat d'ensemble en serait affecté.

Dans le prochain cas, l'étalonnage est fait avec l'utilisation de GPU. Le module multicœur de NAMD est utilisé pour les simulations pouvant être effectuées avec un (1) nœud alors que le module verbs-smp sert dans les cas de tâches nécessitant plusieurs nœuds.

| # cœurs | # GPU | Durée réelle par étape | Notes              |
| :------ | :---- | :--------------------- | :----------------- |
| 4       | 1     | 0.0165                 | 1 nœud, multicœur  |
| 8       | 1     | 0.0088                 | 1 nœud, multicœur  |
| 16      | 1     | 0.0071                 | 1 nœud, multicœur  |
| 32      | 2     | 0.0045                 | 1 nœud, multicœur  |
| 64      | 4     | 0.0058                 | 2 nœuds, verbs-smp |
| 128     | 8     | 0.0051                 | 2 nœuds, verbs-smp |

Les données du tableau indiquent clairement qu'il est absolument inutile d'utiliser plus d'un nœud puisque la performance décroît avec 2 nœuds ou plus. Avec 1 nœud, il est préférable d'utiliser 1 GPU/16 cœurs puisque l'efficacité est maximale; l'utilisation de 2 GPU/32 cœurs est acceptable si vos résultats doivent être produits rapidement. Puisque les nœuds GPU de Graham l'ordre de priorité est le même pour toutes les tâches 1 GPU/16 cœurs, il n'y a aucun avantage à utiliser 4 ou 8 cœurs.

On peut se demander si la simulation peut ou non utiliser un GPU. Les résultats de l'étalonnage indiquent que l'utilisation d'un nœud GPU (2 GPU/32 cœurs) sur Graham traite la tâche plus rapidement que sur 4 nœuds qui ne sont pas des GPU. Puisque le coût d'un nœud GPU sur Graham est près de deux fois plus que celui d'un nœud qui n'est pas un GPU, il est plus économique d'utiliser les GPU. C'est ce que vous devriez faire tant que c'est possible, mais puisque les nœuds CPU sont en plus grand nombre, vous devriez considérer aussi ne pas utiliser de GPU si le temps d'attente est trop long.

## NAMD 3
NAMD 3 est disponible dans un module. Dans le cas de certaines configurations de système, la performance pourrait être meilleure comparée à celle de NAMD 2.14.

Pour l'essayer immédiatement, vous pouvez télécharger le binaire à partir du [site Web de NAMD](http://www.ks.uiuc.edu/Research/namd/) et le modifier pour nos systèmes avec, par exemple (indiquez la version au besoin) :

```bash
tar xvfz NAMD_3.0alpha11_Linux-x86_64-multicore-CUDA-SingleNode.tar.gz 
cd NAMD_3.0alpha11_Linux-x86_64-multicore-CUDA
setrpaths.sh  --path .
```

Par la suite, l'exécutable namd3 dans ce répertoire sera lié aux librairies appropriées. Vous pouvez alors soumettre une tâche qui utilise cet exécutable.

!!! tip
    Pour obtenir une meilleure performance avec NAMD 3 sur un GPU, nous vous recommandons fortement d'ajouter au fichier de configuration le mot-clé suivant, pourvu que la configuration en entrée que vous utilisez le permette :
    ```
    GPUresident on;
    ```

Pour plus d'information sur ce paramètre et ses changements, voir [cette page](https://www.ks.uiuc.edu/Research/namd/alpha/3.0alpha/).

## Références
*   À télécharger : [http://www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=NAMD](http://www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=NAMD) (on vous demandera de vous inscrire)
*   [Guide de l'utilisateur NAMD pour la version 2.14](http://www.ks.uiuc.edu/Research/namd/2.14/ug/)
*   [Guide de l'utilisateur NAMD pour la version 3.0.1](https://www.ks.uiuc.edu/Research/namd/3.0.1/ug/)
*   [Notes de version NAMD 3.0.1](http://www.ks.uiuc.edu/Research/namd/3.0.1/notes.html)
*   [Notes de version NAMD 2.14](http://www.ks.uiuc.edu/Research/namd/2.14/notes.html)
*   Tutoriels : [http://www.ks.uiuc.edu/Training/Tutorials/](http://www.ks.uiuc.edu/Training/Tutorials/)