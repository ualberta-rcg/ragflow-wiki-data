---
title: "Advanced Job Submission/fr"
slug: "advanced_job_submission"
lang: "fr"

source_wiki_title: "Advanced Job Submission/fr"
source_hash: "986b86b4bf0029c50174b3c2eae23d41"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T04:52:14.447001+00:00"

tags:
  []

keywords:
  - "High-throughput computing"
  - "Slurm jobs"
  - "Heterogeneous jobs"
  - "Inter-job dependencies"
  - "Job arrays"

questions:
  - "What are the recommended tools for managing and submitting multiple compute tasks or parameter sweeps?"
  - "How can you configure inter-job dependencies in Slurm to ensure a specific execution order for your pipeline?"
  - "What is the proper syntax for requesting different CPU and memory allocations for distinct processes within a heterogeneous Slurm job?"
  - "What are the recommended tools for managing and submitting multiple compute tasks or parameter sweeps?"
  - "How can you configure inter-job dependencies in Slurm to ensure a specific execution order for your pipeline?"
  - "What is the proper syntax for requesting different CPU and memory allocations for distinct processes within a heterogeneous Slurm job?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Soumettre plusieurs tâches de calcul

Les outils suivants sont utiles lorsque vous devez traiter plusieurs fichiers avec ou sans différentes combinaisons de paramètres (*exploration de paramètres*) :

*   **[Tableaux de tâches](job_arrays.md)** : pour soumettre plusieurs tâches similaires dans un seul script, une méthode idéale lorsque chaque tâche dépasse une heure et que le nombre de tâches est inférieur à mille;
*   **[GNU Parallel](gnu_parallel.md)** : pour exécuter et gérer plusieurs calculs courts, y compris des explorations de paramètres, sur un seul nœud réservé via une tâche parallèle;
*   **[GLOST](glost.md)** : le *Greedy Launcher Of Small Tasks* utilise [MPI](../software/mpi.md) et une architecture gestionnaire-travailleur pour exécuter progressivement une longue liste de tâches séquentielles sur les cœurs de CPU réservés via une tâche parallèle;
*   **[META](meta-farm.md)** : une suite de scripts conçue chez SHARCNET pour automatiser le calcul à haut débit (exécutant un grand nombre de calculs séquentiels, parallèles ou GPU connexes).

## Dépendances inter-tâches

Alors que les tâches Slurm sont les éléments constitutifs des chaînes de calcul, les dépendances inter-tâches sont les liens et les relations entre les étapes d'une chaîne. Par exemple, si deux tâches différentes doivent s'exécuter l'une après l'autre, la deuxième tâche *dépend* de la première. La deuxième pourrait dépendre de l'heure de début, de l'heure de fin ou de l'état final de la première tâche. Généralement, nous voulons que la deuxième tâche ne soit lancée qu'une fois la première tâche réussie. Par exemple :

```bash
JOBID1=$(sbatch --parsable job1.sh)           # Sauvegarde l'identifiant de la première tâche
sbatch --dependency=afterok:$JOBID1 job2.sh   # Dépend de la première tâche
```

!!! note "Remarques"
    *   Plusieurs tâches peuvent avoir la même dépendance (plusieurs tâches attendant après une seule tâche).
    *   Une tâche peut avoir plusieurs dépendances (une tâche attendant après plusieurs tâches).
    *   Il existe plusieurs types de dépendances : `after`, `afterany`, `afterok`, `afternotok`, etc. Pour plus de détails, consultez l'option `--dependency` sur la [page de documentation officielle de `sbatch`](https://slurm.schedmd.com/sbatch.html#OPT_dependency).

## Tâches hétérogènes

L'ordonnanceur Slurm supporte les [tâches hétérogènes](https://slurm.schedmd.com/heterogeneous_jobs.html). Cela pourrait être très utile si vous savez d'avance que votre application [MPI](../software/mpi.md) nécessitera plus de cœurs de CPU et plus de mémoire pour le processus principal que pour les autres processus.

Par exemple, si le processus principal nécessite 8 cœurs et un total de 32 Go de RAM, tandis que les autres processus ne nécessitent qu'un cœur et 1 Go de RAM, nous pouvons spécifier les deux types d'exigences dans un script de tâche :

:::bash heterogeneous_mpi_job.sh
#!/bin/bash
#SBATCH --ntasks=1 --cpus-per-task=8 --mem-per-cpu=4000M
#SBATCH hetjob
#SBATCH --ntasks=15 --cpus-per-task=1 --mem-per-cpu=1000M

srun --cpus-per-task=8 : --cpus-per-task=1 application.exe
:::

Ou nous pouvons séparer les requêtes de ressources avec un deux-points (`:`) sur la ligne de commande `sbatch` :

```bash
sbatch --ntasks=1 --cpus-per-task=8 --mem-per-cpu=4000M : --ntasks=15 --cpus-per-task=1 --mem-per-cpu=1000M mpi_job.sh