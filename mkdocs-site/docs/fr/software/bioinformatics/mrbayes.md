---
title: "MrBayes/fr"
slug: "mrbayes"
lang: "fr"

source_wiki_title: "MrBayes/fr"
source_hash: "37bea91f8a0a31245ccb86ff925be3d8"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:33:16.584005+00:00"

tags:
  []

keywords:
  - "tâche"
  - "commande append"
  - "MrBayes"
  - "modèles phylogénétiques"
  - "points de contrôle"
  - "calcul"
  - "fichiers"
  - "SLURM_ARRAY_TASK_ID"
  - "vecteur de tâches"
  - "calcul parallèle"
  - "sbatch"
  - "script"
  - "inférence bayésienne"

questions:
  - "Qu'est-ce que le programme MrBayes et quelle méthode utilise-t-il pour estimer les paramètres des modèles phylogénétiques ?"
  - "Quelles sont les différentes architectures de calcul (séquentiel, parallèle MPI, GPU) sur lesquelles MrBayes peut être exécuté selon les exemples fournis ?"
  - "Pourquoi est-il fortement recommandé d'utiliser le mécanisme de points de contrôle (checkpoints) lors de l'exécution de tâches très longues ?"
  - "Quelles sont les différences de paramètres d'exécution entre les deux fichiers de configuration MrBayes (job1.nex et job2.nex) ?"
  - "Comment le script bash utilise-t-il les vecteurs de tâches (job arrays) pour lancer l'ensemble des calculs avec un seul fichier ?"
  - "Quelle commande permet de soumettre ce script d'exécution à l'ordonnanceur de tâches ?"
  - "Quel est le processus pour enchaîner deux tâches en utilisant le résultat de la première pour la seconde ?"
  - "Comment les fichiers `job1.nex` et `job2.nex` sont-ils utilisés pour diviser le calcul en deux temps ?"
  - "Quelle est la seule différence de contenu entre le premier et le deuxième script mentionnés dans l'exemple ?"
  - "Quelles sont les différences de paramètres d'exécution entre les deux fichiers de configuration MrBayes (job1.nex et job2.nex) ?"
  - "Comment le script bash utilise-t-il les vecteurs de tâches (job arrays) pour lancer l'ensemble des calculs avec un seul fichier ?"
  - "Quelle commande permet de soumettre ce script d'exécution à l'ordonnanceur de tâches ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[MrBayes](https://nbisweden.github.io/MrBayes/) est un programme d'inférence bayésienne et de choix de modèles sur une large gamme de modèles phylogénétiques et évolutifs. MrBayes utilise les méthodes de Monte Carlo par chaîne de Markov (MCMC) pour estimer la distribution *a posteriori* des paramètres du modèle.

## Trouver les modules disponibles

```bash
module spider mrbayes
```

Pour savoir comment trouver et sélectionner une version de MrBayes avec les commandes `module`, consultez [Utiliser des modules](utiliser-des-modules.md).

## Exemples

### Travailler en séquentiel

Le script suivant demande un (1) seul cœur de CPU (`--cpus-per-task=1`).
Dans cet exemple, on utilise un fichier en entrée (ici, `primates.nex`) fourni avec MrBayes.

```bash linenums="1" title="submit-mrbayes-seq.sh"
#!/bin/bash
#SBATCH --account=def-someuser  # remplacez par votre compte de chercheur principal
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=3G        # augmentez au besoin
#SBATCH --time=1:00:00          # augmentez au besoin

module load mrbayes/3.2.7
cd $SCRATCH
cp -v $EBROOTMRBAYES/share/exemples/mrbayes/primates.nex .

srun mb primates.nex
```

Vous pouvez soumettre le script de la tâche avec :

```bash
sbatch submit-mrbayes-seq.sh
```

### Travailler en parallèle

MrBayes permet d'utiliser des GPU et plusieurs cœurs sur plusieurs nœuds.

#### MPI

Le prochain script demande un total de huit (8) cœurs de CPU, sur un ou plusieurs nœuds.
Il utilise un fichier en entrée (ici, `primates.nex`) fourni avec MrBayes.

```bash linenums="1" title="submit-mrbayes-parallel.sh"
#!/bin/bash
#SBATCH --account=def-someuser  # remplacez par votre compte de chercheur principal
#SBATCH --ntasks=8 				# augmentez au besoin
#SBATCH --mem-per-cpu=3G        # augmentez au besoin
#SBATCH --time=1:00:00          # augmentez au besoin

module load mrbayes/3.2.7
cd $SCRATCH
cp -v $EBROOTMRBAYES/share/exemples/mrbayes/primates.nex .

srun mb primates.nex
```

Le script de la tâche peut être soumis avec :

```bash
sbatch submit-mrbayes-parallel.sh
```

#### GPU

Le script suivant demande un GPU et utilise un fichier en entrée (ici, `primates.nex`) fourni par MrBayes.

```bash linenums="1" title="submit-mrbayes-gpu.sh"
#!/bin/bash
#SBATCH --account=def-someuser  # remplacez par votre compte de chercheur principal
#SBATCH --cpus-per-task=1
#SBATCH --gpus=1
#SBATCH --mem-per-cpu=3G        # augmentez au besoin
#SBATCH --time=1:00:00          # augmentez au besoin

module load gcc cuda/12 mrbayes/3.2.7
cd $SCRATCH
cp -v $EBROOTMRBAYES/share/exemples/mrbayes/primates.nex .

srun mb primates.nex
```

Vous pouvez soumettre le script de la tâche avec :

```bash
sbatch submit-mrbayes-gpu.sh
```

## Utiliser des points de contrôle

!!! attention "Recommandation pour les tâches longues"
    Pour les tâches qui exigent un temps d'exécution considérable, nous vous recommandons fortement de fractionner le travail en plusieurs tâches plus petites, car les tâches de longue durée sont plus susceptibles d'être interrompues en raison d'une panne matérielle ou de travaux de maintenance.

Heureusement, MrBayes offre un mécanisme de **points de contrôle** qui vous permet d'enregistrer le résultat d'une tâche et de reprendre le travail avec une autre tâche.

Dans l'exemple suivant, le calcul s'effectue en deux étapes, via deux tâches soumises l'une à la suite de l'autre. Nous avons créé les fichiers `job1.nex` et `job2.nex` qui sont identiques, sauf pour la commande `append` sur la dernière ligne du deuxième script.

```text linenums="1" title="job1.nex"
execute primates.nex;

mcmc ngen=10000000 nruns=2 temp=0.02 mcmcdiag=yes samplefreq=1000
stoprule=yes stopval=0.005 relburnin=yes burninfrac=0.1 printfreq=1000
checkfreq=1000;
```

```text linenums="1" title="job2.nex"
execute primates.nex;

mcmc ngen=20000000 nruns=2 temp=0.02 mcmcdiag=yes samplefreq=1000
stoprule=yes stopval=0.005 relburnin=yes burninfrac=0.1 printfreq=1000
append=yes checkfreq=1000;
```

Créez ensuite le script pour la tâche. Dans cet exemple, nous utilisons un vecteur de tâches. Dans ce cas-ci, nous n'avons besoin que d'un (1) script et une (1) seule commande `sbatch` pour lancer les deux (2) tâches et ainsi l'ensemble des calculs. Voir [Vecteur de tâches](vecteur-de-taches.md) pour plus d'information au sujet du paramètre `--array`
et de la variable `$SLURM_ARRAY_TASK_ID`.

```bash linenums="1" title="submit-mrbayes-cp.sh"
#!/bin/bash
#SBATCH --account=def-someuser  # remplacez par votre compte de chercheur principal
#SBATCH --ntasks=8 				# augmentez au besoin
#SBATCH --mem-per-cpu=3G        # augmentez au besoin
#SBATCH --time=1:00:00          # augmentez au besoin
#SBATCH --array=1-2%1           # faites correspondre le nombre de sous-tâches, seulement 1 à la fois

module load gcc mrbayes/3.2.7
cd $SCRATCH
cp -v $EBROOTMRBAYES/share/exemples/mrbayes/primates.nex .

srun mb job${SLURM_ARRAY_TASK_ID}.nex
```

Vous pouvez soumettre l'exemple avec :

```bash
sbatch submit-mrbayes-cp.sh