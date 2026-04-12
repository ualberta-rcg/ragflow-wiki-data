---
title: "CP2K/fr"
slug: "cp2k"
lang: "fr"

source_wiki_title: "CP2K/fr"
source_hash: "75127b28d2504b18dd006b86f3a4d148"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:02:46.655714+00:00"

tags:
  - software
  - computationalchemistry

keywords:
  - "physique des solides"
  - "chimie quantique"
  - "processus MPI"
  - "simulations atomistiques"
  - "CP2K"

questions:
  - "Qu'est-ce que le logiciel CP2K et quels types de systèmes permet-il de simuler ?"
  - "Quelles sont les étapes et les commandes requises pour configurer, soumettre et vérifier une tâche de calcul CP2K sur une grappe ?"
  - "Quelle est la différence entre les exécutables `cp2k.popt` et `cp2k.psmp`, et comment le choix entre les deux influence-t-il les performances selon le problème traité ?"
  - "Qu'est-ce que le logiciel CP2K et quels types de systèmes permet-il de simuler ?"
  - "Quelles sont les étapes et les commandes requises pour configurer, soumettre et vérifier une tâche de calcul CP2K sur une grappe ?"
  - "Quelle est la différence entre les exécutables `cp2k.popt` et `cp2k.psmp`, et comment le choix entre les deux influence-t-il les performances selon le problème traité ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

**CP2K** est un paquet logiciel pour la chimie quantique et la physique des solides qui permet de faire des simulations atomistiques de systèmes solides, liquides, moléculaires, périodiques, matériels, cristallins et biologiques.

## Versions

La plus récente version installée est CPK2 8.2. Pour charger le module compilé avec GCC, lancez la commande suivante :

```bash
module load StdEnv/2020 gcc/9.3.0 openmpi/4.0.3 cp2k/8.2
```

!!! avertissement "Version Intel"
    Vous pouvez aussi utiliser la version compilée avec Intel, mais elle semble moins stable car elle plante à l'occasion pour des raisons inconnues.

```bash
module load StdEnv/2020 intel/2020.1.217 openmpi/4.0.3 cp2k/8.2
```

## Exemple de tâche

Nous utilisons ici l'exemple de calcul statique tiré du [site web de CP2K](https://www.cp2k.org/howto:static_calculation).

Connectez-vous à une grappe et téléchargez les fichiers requis avec les commandes suivantes :

```bash
wget https://www.cp2k.org/_media/static_calculation.tgz
```

```bash
tar xvfz static_calculation.tgz
```

```bash
cd static_calculation/sample_output_no_smearing
```

Dans ce répertoire, créez le script de tâche suivant en utilisant le nom de votre compte.

````sh title="mpi_job.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --ntasks=4               # nombre de processus MPI
#SBATCH --mem-per-cpu=4G         # mémoire; l'unité par défaut est le mégaoctet
#SBATCH --time=0-00:15           # temps (JJ-HH:MM)

module load StdEnv/2020  gcc/9.3.0  openmpi/4.0.3 cp2k/8.2
srun cp2k.popt -o Si_bulk8.out Si_bulk8.inp
````

Pour soumettre cette tâche, lancez la commande suivante :

```bash
sbatch mpi_job.sh
```

Pour vérifier que la tâche est terminée, lancez la commande suivante :

```bash
sq
```

Votre tâche est terminée si elle ne paraît pas dans la liste.

Le résultat de CP2K sera dans le fichier `Si_bulk8.out`. Il y aura aussi un fichier de résultats nommé `slurm-*.out` qui sera vide si le calcul s'est effectué sans erreurs.

## Fils et MPI

À partir de la version 8.2, l'installation de CP2K fournit l'exécutable `cp2k.popt` et l'exécutable OpenMP/MPI `cp2k.psmp` qui peuvent améliorer la performance de certains calculs. Avec notre test, nous avons obtenu une amélioration de 10 % avec l'essai `QS/H2O-512.inp` en utilisant 2 fils par processus MPI, en comparaison de l'exécution de `cp2k.popt` en MPI seul; dans les deux cas, le total de cœurs CPU était identique.

L'exemple ci-dessous est un fichier OpenMP/MPI pour la soumission d'une tâche sur Béluga. Sur les autres grappes, modifiez le nombre de tâches pour correspondre au nombre de cœurs disponibles sur les nœuds de chaque grappe. La différence en performance avec l'utilisation de fils dépend du problème traité.

!!! conseil "Optimisation"
    Dans certains cas, l'exécutable `cp2k.psmp` peut prendre plus de temps et il est important de faire des essais avec votre code pour pouvoir choisir la meilleure option.

````sh title="openmp_mpi_job.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --nodes=2
#SBATCH --ntasks=40               # nombre de processus MPI
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu=3G          # mémoire (l'unité par défaut est le mégaoctet)
#SBATCH --time=0-00:59            # temps de calcul (JJ-HH:MM)

module load StdEnv/2020  gcc/9.3.0  openmpi/4.0.3 cp2k/8.2

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
srun --cpus-per-task=$OMP_NUM_THREADS cp2k.psmp -o H2O-512.out H2O-512.inp
`