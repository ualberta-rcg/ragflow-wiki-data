---
title: "Advanced Job Submission/fr"
slug: "advanced_job_submission"
lang: "fr"

source_wiki_title: "Advanced Job Submission/fr"
source_hash: "2b3c6aa26d81be9ee04720fcd27457ae"
last_synced: "2026-04-18T23:39:30.217451+00:00"
last_processed: "2026-04-19T00:33:01.711809+00:00"

tags:
  []

keywords:
  - "Dépendance entre les tâches"
  - "Calcul à haut débit"
  - "}}"
  - "Vecteurs de tâches"
  - "Slurm"
  - "demandes de ressources"
  - "mem-per-cpu"
  - "cpus-per-task"
  - "sbatch"
  - "Tâches hétérogènes"
  - "ligne de commande"

questions:
  - "Quels sont les outils disponibles pour gérer et exécuter efficacement un grand nombre de tâches de calcul ?"
  - "Comment configurer des dépendances dans Slurm pour qu'une tâche ne démarre qu'après la réussite d'une autre ?"
  - "Comment spécifier des allocations de ressources différentes pour les processus d'une même tâche hétérogène ?"
  - "What is the main idea or central theme of the text?"
  - "What are the key arguments or points provided by the author to support their conclusion?"
  - "What is the intended audience and purpose of this content?"
  - "Quel caractère permet de séparer plusieurs demandes de ressources distinctes lors de la soumission d'une tâche ?"
  - "Sur quelle commande spécifique le texte illustre-t-il l'utilisation de cette séparation de ressources ?"
  - "Comment les cœurs (cpus) et la mémoire sont-ils répartis entre les différentes tâches dans l'exemple fourni ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Gérer de nombreux cas de calcul

Les outils suivants sont utiles pour traiter plusieurs fichiers, avec ou sans différentes combinaisons de paramètres (*parameter sweep*) :

*   **[Vecteurs de tâches](job_arrays.md)** : pour soumettre plusieurs tâches similaires dans un seul script, une méthode idéale lorsque chaque tâche dure plus d’une heure et que leur nombre est inférieur à mille;
*   **[GNU Parallel](gnu_parallel.md)** : pour exécuter et gérer plusieurs calculs courts, y compris des *parameter sweeps*, sur un nœud réservé via une tâche parallèle;
*   **[GLOST](glost.md)** (*Greedy Launcher Of Small Tasks*) : utilise [MPI](../software/mpi.md) et une architecture gestionnaire-travailleur pour exécuter progressivement une longue liste de tâches séquentielles sur les cœurs CPU réservés via une tâche parallèle;
*   **[META](meta-farm.md)** : une suite de scripts conçus chez SHARCNET pour automatiser le calcul à haut débit (exécution d’un grand nombre de calculs séquentiels, parallèles ou GPU).

## Dépendance entre les tâches

Alors que les tâches Slurm constituent les éléments de base des pipelines de calcul, les dépendances entre les tâches sont les liens et les relations entre les étapes d’un pipeline. Par exemple, si deux tâches différentes doivent s’exécuter l’une après l’autre, la seconde dépend de la première. La seconde tâche peut dépendre de l’heure de début, l’heure de fin ou le statut final de la première tâche. En général, on souhaite que la seconde tâche ne démarre qu'une fois la première terminée avec succès. Par exemple,

```bash
JOBID1=$(sbatch --parsable job1.sh)           # Sauvegarde l'ID de la première tâche
sbatch --dependency=afterok:$JOBID1 job2.sh   # Dépend de la première tâche
```

!!! note "Remarques"
    *   Plusieurs tâches peuvent avoir la même dépendance (plusieurs tâches en attente d'une seule tâche).
    *   Une tâche peut avoir plusieurs dépendances (une tâche en attente de plusieurs tâches).
    *   Il existe plusieurs types de dépendances : `after`, `afterany`, `afterok`, `afternotok`, etc. Pour plus de détails, voir l'option `--dependency` à la [page officielle de documentation `sbatch`](https://slurm.schedmd.com/sbatch.html#OPT_dependency).

## Tâches hétérogènes

L'ordonnanceur Slurm prend en charge les tâches hétérogènes, ce qui peut s'avérer très utile si vous savez à l'avance que votre application MPI nécessitera davantage de cœurs CPU et de mémoire pour le processus principal que pour les autres processus.

Par exemple, si le processus principal nécessite 8 cœurs et un total de 32Go de RAM, tandis que les autres processus ne nécessitent que 1 cœur et 1Go de RAM, nous pouvons spécifier les deux types d'exigences dans un même script de tâche.

```bash
# heterogeneous_mpi_job.sh
#!/bin/bash
#SBATCH --ntasks=1 --cpus-per-task=8 --mem-per-cpu=4000M
#SBATCH hetjob
#SBATCH --ntasks=15 --cpus-per-task=1 --mem-per-cpu=1000M

srun --cpus-per-task=8 : --cpus-per-task=1 application.exe
```

Nous pouvons aussi séparer les demandes de ressources par un deux-points (`:`) sur la ligne de commande `sbatch`.

```bash
sbatch --ntasks=1 --cpus-per-task=8 --mem-per-cpu=4000M : --ntasks=15 --cpus-per-task=1 --mem-per-cpu=1000M  mpi_job.sh