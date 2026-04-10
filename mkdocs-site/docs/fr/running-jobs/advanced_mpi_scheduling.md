---
title: "Advanced MPI scheduling/fr"
slug: "advanced_mpi_scheduling"
lang: "fr"

source_wiki_title: "Advanced MPI scheduling/fr"
source_hash: "51adf444893385e1b8947af9a2232d93"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T04:02:55.538599+00:00"

tags:
  - slurm

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

La plupart du temps, vous devriez soumettre les tâches MPI parallèles à mémoire distribuée selon l'exemple présenté à la section **Tâche MPI** de la page [Exécuter des tâches](running-jobs.md#tache-mpi). Il suffit d'utiliser `--ntasks` ou `-n` pour spécifier le nombre de processus et de laisser l'ordonnanceur faire la meilleure allocation, compte tenu de l'efficacité de la grappe.

Si par contre vous voulez plus de contrôle sur l'allocation, prenez connaissance de la page [Prise en charge des architectures multicœurs et multithread](https://slurm.schedmd.com/mc_support.html) de SchedMD; on y décrit comment plusieurs options de la commande [`sbatch`](https://slurm.schedmd.com/sbatch.html) agissent sur l'ordonnancement des processus.

Dans la foire aux questions Slurm, la réponse à [Qu'est-ce qu'un CPU exactement?](https://slurm.schedmd.com/faq.html#cpu_count) peut aussi s'avérer utile.

## Exemples de scénarios

### Peu de cœurs, nœuds indéterminés

En plus de spécifier la durée de *toute tâche Slurm*, il faut aussi indiquer le nombre de processus MPI que Slurm doit démarrer. Le moyen le plus simple de ce faire est d'utiliser `--ntasks`. Puisque l'allocation par défaut de 256Mo de mémoire est souvent insuffisante, vous devriez aussi spécifier la quantité de mémoire nécessaire. Avec `--ntasks`, il est impossible de savoir combien de cœurs seront sur chaque nœud; vous voudrez alors utiliser `--mem-per-cpu` comme suit :

```sh title="basic_mpi_job.sh"
#!/bin/bash
#SBATCH --ntasks=15
#SBATCH --mem-per-cpu=3G
srun application.exe
```

Nous avons ici 15 processus MPI. L'allocation des cœurs pourrait se faire sur 1 nœud, sur 15 nœuds, ou sur tout nombre de nœuds entre 1 et 15.

### Nœuds entiers

Pour une tâche parallèle intensive qui peut utiliser efficacement 64 cœurs ou plus, vous devriez probablement demander des nœuds entiers; il est donc utile de savoir quels types de nœuds sont disponibles sur la grappe que vous utilisez.

La plupart des nœuds de [Fir](fir.md), [Narval](narval.md), [Nibi](nibi.md), [Rorqual](rorqual.md) et [Trillium](trillium.md) sont configurés comme suit :

| Grappe     | Cœurs | Mémoire utilisable | Notes                                                        |
| :--------- | :---- | :----------------- | :----------------------------------------------------------- |
| [Fir](fir.md)       | 192   | 750 Gio            | Certains sont réservés pour les tâches sur nœud entier       |
| [Narval](narval.md) | 64    | 249 Gio            | Certains sont réservés pour les tâches sur nœud entier       |
| [Nibi](nibi.md)     | 192   | 748 Gio            | Aucun n'est réservé pour les tâches sur nœud entier          |
| [Rorqual](rorqual.md) | 192   | 750 Gio            | Certains sont réservés pour les tâches sur nœud entier       |
| [Trillium](trillium.md) | 192   | 749 Gio            | Trillium permet uniquement des tâches sur nœud entier        |

Les tâches sur nœuds entiers peuvent être exécutées sur tous les nœuds. Dans le tableau ci-dessus, la note « Certains sont réservés pour les tâches sur nœuds entiers » signifie que les tâches par cœur sont interdites sur certains nœuds.

Voici un exemple d'un script demandant des nœuds entiers.

<tabs>
  <tab title="Fir">
```sh title="whole_nodes_fir.sh"
#!/bin/bash
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=192
#SBATCH --mem=0
srun application.exe
```
  </tab>
  <tab title="Narval">
```sh title="whole_nodes_narval.sh"
#!/bin/bash
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=64
#SBATCH --mem=0
srun application.exe
```
  </tab>
  <tab title="Nibi">
```sh title="whole_nodes_nibi.sh"
#!/bin/bash
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=192
#SBATCH --mem=0
srun application.exe
```
  </tab>
  <tab title="Rorqual">
```sh title="whole_nodes_rorqual.sh"
#!/bin/bash
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=192
#SBATCH --mem=0
srun application.exe
```
  </tab>
  <tab title="Trillium">
```sh title="whole_nodes_trillium.sh"
#!/bin/bash
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=192
#SBATCH --mem=0
srun application.exe
```
  </tab>
</tabs>

Le fait de demander `--mem=0` indique à Slurm qu'il doit *réserver toute la mémoire disponible de chacun des nœuds assignés à la tâche*.

!!! warning
    Toutefois, si vous avez besoin de plus de mémoire par nœud que ce que le plus petit nœud peut offrir (par exemple plus de 748 Gio sur Nibi), **vous ne devriez pas utiliser** `--mem=0`, mais demander une quantité explicite de mémoire.

De plus, une partie de la mémoire de chaque nœud est réservée au système d'exploitation; dans la section *Caractéristiques des nœuds*, la colonne *Mémoire disponible* indique la plus grande quantité de mémoire qu'une tâche peut demander :
*   [Fir](fir.md#caracteristiques-des-noeuds)
*   [Narval](narval.md#caracteristiques-des-noeuds)
*   [Nibi](nibi.md#caracteristiques-des-noeuds)
*   [Rorqual](rorqual.md#caracteristiques-des-noeuds)

### Peu de cœurs, nœud unique

Si vous avez besoin de moins d'un nœud entier, mais que tous les cœurs doivent être du même nœud, vous pouvez demander par exemple :
```sh title="less_than_whole_node.sh"
#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=15
#SBATCH --mem=45G
srun application.exe
```
Vous pourriez aussi utiliser `--mem-per-cpu=3G`, mais la tâche serait annulée si un des processus dépasse 3 Go. L'avantage avec `--mem=45G` est que la mémoire consommée par chaque processus n'importe pas, pourvu que dans l'ensemble ils ne dépassent pas 45 Go.

### Tâche parallèle intensive, sans multiples de nœuds entiers

Ce ne sont pas toutes les tâches qui sont effectuées de façon optimale sur des cœurs en multiples de 32, 40 ou 48. Le fait d'indiquer ou non un nombre précis de cœurs peut influer sur le *temps d'exécution* (ou la bonne utilisation de la ressource) ou le *temps d'attente* (ou la bonne utilisation du temps qui vous est imparti). Pour de l'aide sur la façon d'évaluer ces facteurs, communiquez avec le [soutien technique](technical-support.md).

## Tâches hybrides : MPI avec OpenMP ou MPI avec fils

Il est important de bien comprendre que le nombre de *tâches* Slurm demandées représente le nombre de *processus* qui seront démarrés avec `srun`. Dans le cas d'une tâche hybride qui utilise à la fois des processus MPI et des fils OpenMP ou Posix, vous voudrez indiquer le nombre de processus MPI avec `--ntasks` ou `--ntasks-per-node` et le nombre de fils avec `--cpus-per-task`.

```bash
#SBATCH --ntasks=16
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=3G
srun --cpus-per-task=$SLURM_CPUS_PER_TASK application.exe
```

Ici, 64 cœurs sont alloués, mais seulement 16 processus (tâches) MPI sont et seront initialisés. S'il s'agit en plus d'une application OpenMP, chacun des processus démarrera 4 fils, soit un par cœur. Chaque processus pourra utiliser 12 Go. Avec 4 cœurs, les tâches pourraient être allouées sur 2 à 16 nœuds, peu importe lesquels. Vous devez aussi spécifier `--cpus-per-task=$SLURM_CPUS_PER_TASK` pour `srun`, puisque c'est exigé depuis Slurm 22.05 et ne nuit pas aux versions les moins récentes.

```bash
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=8
#SBATCH --cpus-per-task=4
#SBATCH --mem=96G
srun --cpus-per-task=$SLURM_CPUS_PER_TASK application.exe
```

La taille de cette tâche est identique à celle de la précédente, c'est-à-dire 16 tâches (soit 16 processus MPI) avec chacune 4 fils. La différence ici est que nous obtiendrons exactement 2 nœuds entiers. N'oubliez pas que `--mem` précise la quantité de mémoire *par nœud* et que nous l'utilisons de préférence à `--mem-per-cpu` pour la raison donnée plus haut.

## Pourquoi srun plutôt que mpiexec ou mpirun?

`mpirun` permet la communication entre processus exécutés sur des ordinateurs différents; les ordonnanceurs récents possèdent cette même fonctionnalité. Avec Torque/Moab, il n'est pas nécessaire de fournir à `mpirun` la liste des nœuds ou le nombre de processus puisque l'ordonnanceur s'en charge. Avec Slurm, c'est l'ordonnanceur qui décide de l'affinité des tâches, ce qui évite d'avoir à préciser des paramètres comme :

```bash
mpirun --map-by node:pe=4 -n 16 application.exe
```

Dans les exemples précédents, on comprend que `srun application.exe` distribue automatiquement les processus aux ressources précises allouées à la tâche.

En termes de niveaux d'abstraction, `srun` est au-dessus de `mpirun`; `srun` peut faire tout ce que fait `mpirun` et davantage. Avec Slurm, `srun` est l'outil de prédilection pour lancer tous les types de calcul; il est aussi plus polyvalent que le `pbsdsh` de Torque. On pourrait dire de `srun` que c'est l'outil Slurm universel pour la distribution des tâches en parallèle : une fois les ressources allouées, la nature de l'application importe peu, qu'il s'agisse de MPI, OpenMP, hybride, distribution sérielle, pipeline, multiprogramme ou autre.

Bien entendu, `srun` est parfaitement adapté à Slurm : il amorce la première étape de la tâche, initialise correctement les variables d'environnement `SLURM_STEP_ID` et `SLURM_PROCID` et fournit les renseignements de suivi appropriés.

Pour des exemples de quelques différences entre `srun` et `mpiexec`, voyez [le forum OpenMPI](https://mail-archive.com/users@lists.open-mpi.org/msg31874.html). Dans certains cas, `mpiexec` offrira une meilleure performance que `srun`, mais `srun` diminue le risque de conflit entre les ressources allouées par Slurm et celles utilisées par OpenMPI.

## Références

*   [documentation sbatch](https://slurm.schedmd.com/sbatch.html)
*   [documentation srun](https://slurm.schedmd.com/srun.html)
*   [Open MPI et Slurm](https://www.open-mpi.org/faq/?category=slurm)