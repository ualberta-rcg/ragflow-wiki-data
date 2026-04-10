---
title: "MrBayes/fr"
tags:
  []

keywords:
  []
---

[MrBayes](https://nbisweden.github.io/MrBayes/) est un programme d'inférence bayésienne et de choix de modèles sur une large gamme de modèles phylogénétiques et évolutifs. MrBayes utilise les méthodes de Monte Carlo par chaîne de Markov (MCMC) pour estimer la distribution a posteriori des paramètres du modèle.

## Trouver les modules disponibles

```bash
module spider mrbayes
```

Pour savoir comment trouver et sélectionner une version de MrBayes avec les commandes  `module`, consultez [Utiliser_des_modules](utiliser_des_modules.md).

<span id="Examples"></span>
## Exemples 

### Travailler en séquentiel 
Le script suivant demande un (1) seul cœur CPU (`--cpus-per-task=1`).
Dans cet exemple, on utilise un fichier en entrée (ici, `primates.nex`) fourni avec MrBayes. 

**`submit-mrbayes-seq.sh`**
```python
#!/bin/bash
#SBATCH --account=def-someuser  # replace with your PI account
#SBATCH --cpus-per-task=1 
#SBATCH --mem-per-cpu=3G        # increase as needed
#SBATCH --time=1:00:00          # increase as needed

module load mrbayes/3.2.7
cd $SCRATCH 
cp -v $EBROOTMRBAYES/share/examples/mrbayes/primates.nex .

srun mb primates.nex
```

Vous pouvez soumettre le script de la tâche avec

```bash
sbatch submit-mrbayes-seq.sh
```

### Travailler en parallèle 
MrBayes permet d'utiliser des GPU et plusieurs cœurs sur plusieurs nœuds.

#### MPI 
Le prochain script demande un total de huit (8) cœurs CPU, sur un ou plusieurs nœuds.  
Il utilise un fichier en entrée (ici, `primates.nex`) fourni avec MrBayes.

**`submit-mrbayes-parallel.sh`**
```python
#!/bin/bash
#SBATCH --account=def-someuser  # replace with your PI account
#SBATCH --ntasks=8 				# increase as needed
#SBATCH --mem-per-cpu=3G        # increase as needed
#SBATCH --time=1:00:00          # increase as needed

module load mrbayes/3.2.7
cd $SCRATCH 
cp -v $EBROOTMRBAYES/share/examples/mrbayes/primates.nex .

srun mb primates.nex
```

Le script pour la tâche peut être soumis avec

```bash
sbatch submit-mrbayes-parallel.sh
```

#### GPU 
Le script suivant demande un GPU et utilise un fichier en entrée (ici, `primates.nex`) fourni par MrBayes.

**`submit-mrbayes-gpu.sh`**
```python
#!/bin/bash
#SBATCH --account=def-someuser  # replace with your PI account
#SBATCH --cpus-per-task=1
#SBATCH --gpus=1
#SBATCH --mem-per-cpu=3G        # increase as needed
#SBATCH --time=1:00:00          # increase as needed

module load gcc cuda/12 mrbayes/3.2.7
cd $SCRATCH 
cp -v $EBROOTMRBAYES/share/examples/mrbayes/primates.nex .

srun mb primates.nex
```

Vous pouvez soumettre le script de la tâche avec

```bash
sbatch submit-mrbayes-gpu.sh
```

## Utiliser des points de contrôle 
Pour les tâches qui exigent beaucoup de temps d'exécution, nous vous recommandons de répartir le travail dans plusieurs petites tâches parce que les tâches de longue durée sont plus susceptibles  d'être interrompues par une panne de matériel ou des travaux de maintenance. Heureusement, MrBayes offre un mécanisme pour créer des points de contrôle qui vous permettent d'enregistrer le résultat d'une tâche et de poursuivre le travail avec une autre tâche.

Dans l'exemple suivant, le calcul se fait en deux temps dans deux tâches qui sont soumises l'une à la suite de l'autre. Nous avons créé les fichiers   `job1.nex` et `job2.nex` qui sont identiques, sauf pour la commande `append` sur la dernière ligne du deuxième script.

**`job1.nex`**
```text
execute primates.nex;

mcmc ngen=10000000 nruns=2 temp=0.02 mcmcdiag=yes samplefreq=1000 
stoprule=yes stopval=0.005 relburnin=yes burninfrac=0.1 printfreq=1000 
checkfreq=1000;
```

**`job2.nex`**
```text
execute primates.nex;

mcmc ngen=20000000 nruns=2 temp=0.02 mcmcdiag=yes samplefreq=1000
stoprule=yes stopval=0.005 relburnin=yes burninfrac=0.1 printfreq=1000
append=yes checkfreq=1000;
```

Créez ensuite le script pour la tâche. Dans cet exemple nous utilisons un vecteur de tâches. Dans ce cas-ci nous n'avons besoin que d'un (1) script et d'une (1) commande `sbatch` pour lancer les deux (2) tâches et donc l'ensemble des calculs. Voir [Vecteur de tâches](job-arrays-fr.md) pour plus d'information au sujet du paramètre `--array` 
et la variable `$SLURM_ARRAY_TASK_ID`.

{{File
  |name=submit-mrbayes-cp.sh
  |lang="bash"
  |contents=
#!/bin/bash
#SBATCH --account=def-someuser  # replace with your PI account
#SBATCH --ntasks=8 				# increase as needed
#SBATCH --mem-per-cpu=3G        # increase as needed
#SBATCH --time=1:00:00          # increase as needed
#SBATCH --array=1-2%1           # match the number of sub-jobs, only 1 at a time

module load gcc mrbayes/3.2.7
cd $SCRATCH 
cp -v $EBROOTMRBAYES/share/examples/mrbayes/primates.nex .

srun mb job${SLURM_ARRAY_TASK_ID}.nex
}}

Vous pouvez soumettre l'exemple avec

```bash
sbatch submit-mrbayes-cp.sh
```