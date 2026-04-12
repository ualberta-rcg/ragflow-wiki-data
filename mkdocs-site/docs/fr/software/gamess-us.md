---
title: "GAMESS-US/fr"
slug: "gamess-us"
lang: "fr"

source_wiki_title: "GAMESS-US/fr"
source_hash: "d28f4fdf9330720c2fac59c381f1f5d5"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:12:25.374104+00:00"

tags:
  - software
  - computationalchemistry

keywords:
  - "Slurm"
  - "calculs"
  - "MWORDS"
  - "mémoire"
  - "chimie quantique"
  - "GAMESS"
  - "temps d'exécution"
  - "fichiers scratch"
  - "comparer"
  - "soumettre une tâche"
  - "utilisation des ressources"
  - "nombres de CPUs"
  - "plusieurs CPUs"

questions:
  - "Quelles sont les étapes et les fichiers requis pour préparer et soumettre correctement une tâche GAMESS ?"
  - "Comment le logiciel gère-t-il l'enregistrement des fichiers temporaires et supplémentaires lors de l'exécution ?"
  - "Quelles sont les contraintes liées à l'exécution sur plusieurs processeurs et comment évaluer le nombre optimal de cœurs à utiliser ?"
  - "Pourquoi les logiciels de chimie quantique comme GAMESS utilisent-ils le stockage « scratch » et quel est son principal inconvénient par rapport à la mémoire vive ?"
  - "Comment les paramètres MWORDS et MEMDDI permettent-ils de définir et de répartir la quantité de mémoire allouée à GAMESS dans le fichier d'entrée ?"
  - "Que signifie le message d'erreur de l'ordonnanceur Slurm lié au dépassement de la limite de mémoire et quelles sont les solutions pour y remédier ?"
  - "Quel est le résultat idéal attendu concernant le temps d'exécution lorsqu'on double le nombre de CPUs utilisés ?"
  - "Qu'est-ce qui caractérise une mauvaise utilisation des ressources lors de l'augmentation du nombre de processeurs selon le texte ?"
  - "Quel phénomène paradoxal peut parfois survenir concernant le temps de calcul lorsqu'on utilise un plus grand nombre de CPUs ?"
  - "Pourquoi les logiciels de chimie quantique comme GAMESS utilisent-ils le stockage « scratch » et quel est son principal inconvénient par rapport à la mémoire vive ?"
  - "Comment les paramètres MWORDS et MEMDDI permettent-ils de définir et de répartir la quantité de mémoire allouée à GAMESS dans le fichier d'entrée ?"
  - "Que signifie le message d'erreur de l'ordonnanceur Slurm lié au dépassement de la limite de mémoire et quelles sont les solutions pour y remédier ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[GAMESS](http://www.msg.ameslab.gov/gamess/) (pour *General Atomic and Molecular Electronic Structure System*) est un logiciel de chimie quantique *ab initio*.

## Exécution

### Soumettre une tâche

Pour savoir comment soumettre une tâche et en faire le suivi, consultez [Exécuter des tâches](running-jobs.md).

La première étape est de préparer un fichier d'entrée GAMESS qui contient la géométrie moléculaire et le calcul à effectuer.
Consultez [la documentation GAMESS](http://www.msg.ameslab.gov/gamess/documentation.html) et en particulier [la section 2](http://www.msg.ameslab.gov/gamess/GAMESS_Manual/input.pdf) qui décrit le format du fichier et les mots-clés.

En plus du fichier d'entrée (*nom.inp* dans notre exemple), préparez aussi un script pour la tâche qui spécifie les ressources de calcul requises. Le fichier d'entrée et le script doivent se trouver dans le même répertoire.

```sh title="gamess_job.sh"
#!/bin/bash
#SBATCH --cpus-per-task=1       # Nombre de processeurs
#SBATCH --mem-per-cpu=4000M     # Mémoire par processeur en Mo
#SBATCH --time=0-00:30          # Durée (JJ-HH:MM)

## Répertoire pour les fichiers de sortie supplémentaires de GAMESS ($USERSCR) :
#export USERSCR=$SCRATCH

## Répertoire pour les fichiers binaires temporaires de GAMESS ($SCR) :
## Décommentez les deux lignes suivantes pour utiliser /scratch au lieu du disque local
#export SCR="$SCRATCH/gamess_${SLURM_JOB_ID}/"
#mkdir -p $SCR

module load gamess-us/20170420-R1
export SLURM_CPUS_PER_TASK      # rungms utilisera cette variable
rungms name.inp  &>  name.out
```

Soumettez la tâche à l'ordonnanceur avec :

```bash
sbatch gamess_job.sh
```

### Fichiers scratch

Par défaut, les fichiers binaires temporaires (fichiers scratch) sont enregistrés sur le disque local du nœud de calcul (`$SLURM_TMPDIR`), ce qui devrait offrir la meilleure performance.

!!! warning "Avertissement : Les données temporaires sont supprimées"
    Les données stockées dans `$SLURM_TMPDIR` seront **supprimées** à la fin de la tâche.

Si l'espace sur le disque local est insuffisant, utilisez plutôt `/scratch` avec la variable d'environnement `SCR` comme ci-dessus.

Les fichiers de sortie supplémentaires sont copiés à l'endroit désigné par la variable d'environnement `USERSCR`; par défaut, il s'agit du répertoire `$SCRATCH` de l'utilisateur.

| Description                               | Variable d'environnement | Emplacement par défaut                       |
| :---------------------------------------- | :----------------------- | :------------------------------------------- |
| Fichiers binaires temporaires GAMESS      | `SCR`                    | `$SLURM_TMPDIR` (stockage local au nœud)    |
| Fichiers de sortie supplémentaires GAMESS | `USERSCR`                | `$SCRATCH` (répertoire SCRATCH de l'utilisateur) |

### Exécution sur plusieurs processeurs

Les calculs peuvent s'effectuer sur plus d'un processeur. Le paramètre `--cpus-per-task` définit le nombre de processeurs disponibles pour le calcul.

Comme la parallélisation se fait par [sockets](https://en.wikipedia.org/wiki/Unix_domain_socket), GAMESS ne peut utiliser que les cœurs de processeur qui se trouvent sur le même nœud de calcul. Le nombre de cœurs de processeur maximum pour une tâche dépend donc de la taille des nœuds dans la grappe, soit 32 cœurs de processeur par nœud sur [Graham](graham.md).

Les calculs en chimie quantique sont reconnus pour ne pas se transposer sur plusieurs processeurs aussi bien qu'en mécanique moléculaire classique, ce qui signifie qu'ils ne sont pas efficaces avec un grand nombre de processeurs. Le nombre précis de processeurs pouvant être utilisés avec efficacité dépend du niveau théorique et de la quantité d'atomes et de fonctions de base.

Pour déterminer un nombre raisonnable de processeurs à utiliser, il faut exécuter un test de scalabilité, c'est-à-dire comparer les temps d'exécution avec des nombres de processeurs différents avec le même fichier. Idéalement, le temps d'exécution devrait diminuer de moitié quand deux fois plus de processeurs sont utilisés. Évidemment, ce serait une piètre utilisation des ressources si par exemple un calcul s'exécutait 30 % plus rapidement avec deux fois plus de processeurs. Il se peut même que certains calculs prennent plus de temps avec un nombre plus élevé de processeurs.

### Mémoire

Les calculs en chimie quantique dépendent souvent de la quantité de mémoire utilisée (memory bound) et à un niveau théorique plus élevé, de plus grandes molécules ont souvent besoin de plus de mémoire vive que ce qui est normalement disponible sur un ordinateur. Dans le but de libérer la mémoire, les logiciels comme GAMESS font donc usage de stockage scratch pour stocker les résultats intermédiaires et accèdent au disque plus tard pour les calculs.

Le stockage scratch le plus rapide est cependant énormément plus lent que la mémoire. Prévoyez donc une quantité de mémoire suffisante ainsi :

1.  Spécifiez la quantité de mémoire dans le script de soumission de la tâche. La valeur `--mem-per-cpu=4000M` est raisonnable puisqu'elle équivaut au ratio mémoire-processeur des nœuds de base. Le fait de demander plus pourrait faire en sorte que la tâche reste en attente pour être exécutée sur un nœud de type large.

2.  Dans le groupe `$SYSTEM` du fichier en entrée, utilisez les options `MWORDS` et `MEMDDI` pour indiquer à GAMESS la quantité de mémoire pouvant être utilisée.
    *   `MWORDS` est le maximum de mémoire que la tâche peut utiliser sur chacun des cœurs. Les unités sont de 1 000 000 mots (contrairement à 1024\*1024 mots), un mot représentant 64 bits, soit 8 octets.
    *   `MEMDDI` est la quantité totale de mémoire nécessaire au DDI (distributed data interface), sur la base d'unités de 1 000 000 mots. La mémoire requise sur chaque cœur de processeur utilisant `p` cœurs de processeur est donc de `MEMDDI/p + MWORDS`.

Pour plus d'information, consultez la section `$SYSTEM` du [manuel d'entrée de GAMESS](http://www.msg.ameslab.gov/gamess/GAMESS_Manual/input.pdf).

!!! warning "Dépassement de la limite de mémoire"
    Il est crucial de maintenir une marge de sécurité de quelques centaines de Mo entre la mémoire allouée par l'ordonnanceur et celle que GAMESS peut utiliser. Si votre tâche se termine de manière incomplète et que le fichier `slurm-{JOBID}.out` contient un message tel que `slurmstepd: error: Exceeded step/job memory limit at some point`, cela signifie que Slurm a interrompu l'exécution parce que la tâche utilisait plus de mémoire que ce qui avait été demandé. Pour résoudre ce problème, vous pouvez :
    *   Réduire la valeur de `MWORDS` ou de `MEMDDI` dans le fichier d'entrée.
    *   Augmenter la valeur de `--mem-per-cpu` dans le script de soumission.

## Références