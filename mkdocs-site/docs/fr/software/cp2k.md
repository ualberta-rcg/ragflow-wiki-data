---
title: "CP2K/fr"
slug: "cp2k"
lang: "fr"

source_wiki_title: "CP2K/fr"
source_hash: "75127b28d2504b18dd006b86f3a4d148"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T05:12:01.855665+00:00"

tags:
  - software
  - computationalchemistry

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

**CP2K** est un paquet logiciel pour la chimie quantique et la physique des solides qui permet de faire des simulations atomistiques de systèmes solides, liquides, moléculaires, périodiques, matériels, cristallins et biologiques.

## Versions

La plus récente version installée est CP2K 8.2. Pour charger le module compilé avec GCC, lancez la commande suivante :

```bash
module load StdEnv/2020 gcc/9.3.0 openmpi/4.0.3 cp2k/8.2
```

!!! warning "Version Intel moins stable"
    Vous pouvez aussi utiliser la version compilée avec Intel, mais elle semble moins stable, car elle plante à l'occasion pour des raisons inconnues.

```bash
module load StdEnv/2020 intel/2020.1.217 openmpi/4.0.3 cp2k/8.2
```

## Exemple de tâche

Nous utilisons ici l'exemple de calcul statique tiré du [site web de CP2K](https://www.cp2k.org/howto:static_calculation).

Connectez-vous à une grappe et téléchargez les fichiers requis avec les commandes suivantes :

```bash
wget https://www.cp2k.org/_media/static_calculation.tgz
tar xvfz static_calculation.tgz
cd static_calculation/sample_output_no_smearing
```

Dans ce répertoire, créez le script de tâche suivant en utilisant le nom de votre compte.

```bash
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --ntasks=4               # nombre de processus MPI
#SBATCH --mem-per-cpu=4G         # mémoire; l'unité par défaut est le mégaoctet
#SBATCH --time=0-00:15           # temps (JJ-HH:MM)

module load StdEnv/2020 gcc/9.3.0 openmpi/4.0.3 cp2k/8.2
srun cp2k.popt -o Si_bulk8.out Si_bulk8.inp
```

Pour soumettre cette tâche, lancez la commande :

```bash
sbatch mpi_job.sh
```

Pour vérifier que la tâche est terminée, lancez la commande :

```bash
sq
```

Votre tâche est terminée si elle n'apparaît pas dans la liste.

Le résultat de CP2K se trouvera dans le fichier `Si_bulk8.out`. Il y aura aussi un fichier de résultats nommé `slurm-*.out` qui sera vide si le calcul s'est effectué sans erreurs.

## Fils et MPI

À partir de la version 8.2, l'installation de CP2K fournit l'exécutable `cp2k.popt` et l'exécutable OpenMP/MPI `cp2k.psmp` qui peuvent améliorer la performance de certains calculs. Avec notre test, nous avons obtenu une amélioration de 10 % avec l'essai `QS/H2O-512.inp` en utilisant 2 fils par processus MPI, en comparaison de l'exécution de `cp2k.popt` en MPI seul; dans les deux cas, le total de cœurs CPU était identique.

L'exemple ci-dessous est un fichier OpenMP/MPI pour la soumission d'une tâche sur Béluga. Sur les autres grappes, modifiez le nombre de tâches pour correspondre au nombre de cœurs disponibles sur les nœuds de chaque grappe.

!!! tip "Optimisation des performances"
    La différence en performance avec l'utilisation de fils dépend du problème traité. Dans certains cas, l'exécutable `cp2k.psmp` peut prendre plus de temps et il est important de faire des essais avec votre code pour pouvoir choisir la meilleure option.

```bash
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --nodes=2
#SBATCH --ntasks=40               # nombre de processus MPI
-cpus-per-task=2
#SBATCH --mem-per-cpu=3G          # mémoire (en Mo par défaut)
#SBATCH --time=0-00:59            # temps de calcul (JJ-HH:MM)

module load StdEnv/2020 gcc/9.3.0 openmpi/4.0.3 cp2k/8.2

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
srun --cpus-per-task=$OMP_NUM_THREADS cp2k.psmp -o H2O-512.out H2O-512.inp