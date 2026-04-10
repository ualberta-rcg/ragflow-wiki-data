---
title: "GAMESS-US/fr"
tags:
  - software
  - computationalchemistry

keywords:
  []
---

[GAMESS](http://www.msg.ameslab.gov/gamess/) (pour *General Atomic and Molecular Electronic Structure System*) est un paquet logiciel de chimie quantique *ab initio*.

== Exécution == 

### Soumettre une tâche 
Pour savoir comment soumettre une tâche et en faire le suivi, consultez [Exécuter des tâches](running-jobs-fr.md).

La première étape est de préparer un fichier d'entrée GAMESS qui contient la géométrie moléculaire et le calcul à effectuer. 
Consultez [la documentation GAMESS](http://www.msg.ameslab.gov/gamess/documentation.html) et en particulier [la section 2](http://www.msg.ameslab.gov/gamess/GAMESS_Manual/input.pdf) qui décrit le format du fichier et les mots-clés.

En plus du fichier d'entrée (*name.inp* dans notre exemple), préparez aussi un script pour la tâche qui spécifie les ressources de calcul requises. Le fichier d'entrée et le script doivent se trouver dans le même répertoire.

{{File
  |name=gamess_job.sh
  |lang="sh"
  |contents=
#!/bin/bash
#SBATCH --cpus-per-task=1       # Number of CPUs
#SBATCH --mem-per-cpu=4000M     # memory per CPU in MB
#SBATCH --time=0-00:30          # time (DD-HH:MM)

## Directory for GAMESS supplementary output files ($USERSCR):
#export USERSCR=$SCRATCH

## Directory for GAMESS temporary binary files ($SCR):
## Uncomment the following two lines to use /scratch instead of local disk
#export SCR="$SCRATCH/gamess_${SLURM_JOB_ID}/"
#mkdir -p $SCR

module load gamess-us/20170420-R1
export SLURM_CPUS_PER_TASK      # rungms will use this
rungms name.inp  &>  name.out
}}

Soumettez la tâche à l'ordonnanceur avec

   sbatch gamess_job.sh

### Fichiers *scratch* 

Par défaut, les fichiers binaires temporaires (fichiers *scratch*) sont enregistrés sur le disque local du nœud de calcul (`$SLURM_TMPDIR`), ce qui devrait offrir la meilleure performance.
N'oubliez pas que les données de `$SLURM_TMPDIR` seront **supprimées** lorsque la tâche sera terminée. 
Si l'espace sur le disque local est insuffisant, utilisez plutôt */scratch* avec la variable d'environnement `SCR` comme ci-dessus.

Les fichiers de sortie supplémentaires sont copiés à l'endroit désigné par la variable d'environnement `USERSCR`; par défaut, il s'agit du répertoire `$SCRATCH` de l'utilisateur.

{| class="wikitable"
|-
! Description                        !! Environment Variable !! Default location
|-
| GAMESS temporary binary files      || `SCR`     || `$SLURM_TMPDIR` (node-local storage) 
|-
| GAMESS supplementary output files  || `USERSCR` || `$SCRATCH` (user's SCRATCH directory)
|}

### Exécution sur plusieurs CPUs 

Les calculs peuvent s'effectuer sur plus d'un CPU. Le paramètre `--cpus-per-task` 
définit le nombre de CPUs disponibles pour le calcul.. 

Comme la parallélisation se fait par [sockets](https://en.wikipedia.org/wiki/Unix_domain_socket), GAMESS ne peut utiliser que les cœurs CPU qui se trouvent sur le même nœud de calcul. Le nombre de cœurs CPU maximum pour une tâche dépend donc de la taille des nœuds dans la grappe, soit 32 cœurs CPU par nœud sur [Graham](graham-fr.md).

Les calculs en chimie quantique sont reconnus pour ne pas se transposer sur plusieurs CPUs aussi bien qu'en mécanique moléculaire classique, ce qui signifie qu'ils ne sont pas efficaces avec un grand nombre de CPUs. Le nombre précis de CPUs pouvant être utilisés avec efficacité dépend du niveau théorique et de la quantité d'atomes et de fonctions de base.

Pour déterminer un nombre raisonnable de CPUS à utiliser, il faut exécuter un test de *scalabilité*, c'est-à-dire comparer les temps d'exécution avec des nombres de CPUs différents avec le même fichier. Idéalement, le temps d'exécution devrait diminuer de moitié quand deux fois plus de CPUs sont utilisés. Évidemment, ce serait une piètre utilisation des ressources si par exemple un calcul s'exécutait 30% plus rapidement avec deux fois plus de CPUs. Il se peut même que certains calculs prennent plus de temps avec un nombre plus élevé de CPUs.

### Mémoire 

Les calculs en chimie quantique dépendent souvent de la quantité de mémoire utilisée (*memory bound*) et à un niveau théorique plus élevé, de plus grandes molécules ont souvent besoin de plus de mémoire RAM que ce qui est normalement disponible sur un ordinateur. Dans le but de libérer la mémoire, les paquets comme GAMESS font donc usage de stockage *scratch* pour stocker les résultats intermédiaires et accèdent au disque plus tard pour les calculs.

Le stockage *scratch* le plus rapide est cependant énormément plus lent que la mémoire. Prévoyez donc une quantité de mémoire suffisante ainsi ː 

1. Spécifiez la quantité de mémoire dans le script de soumission de la tâche. La valeur `--mem-per-cpu=4000M` est raisonnable puisqu'elle équivaut au ratio mémoire-CPU des nœuds de base. Le fait de demander plus pourrait faire en sorte que la tâche reste en attente pour être exécutée sur un nœud de type *large*.

2. Dans le groupe `$SYSTEM group` du ficher en entrée, utilisez les options `MWORDS` et `MEMDDI` pour indiquer à GAMESS la quantité de mémoire pouvant être utilisée.
* `MWORDS` est le maximum de mémoire que la tâche peut utiliser sur chacun des cœurs. Les unités sont de 1,000,000 mots (contrairement à 1024*1024 mots), un mot représentant 64 bits = 8 octets. 
* `MEMDDI` est la quantité totale de mémoire nécessaire au DDI (*distributed data interface*), sur la base d'unités de 1,000,000 mots. La mémoire requise sur chaque cœur de processeur utilisant <tt>p</tt> cœurs-CPU est donc de <tt>MEMDDI/p + MWORDS</tt>. 

Pour plus d'information, consultez la section `$SYSTEM group` de [la documentation GAMESS](http://www.msg.ameslab.gov/gamess/GAMESS_Manual/input.pdf).

Il importe de garder une marge de sûreté de quelques centaines de Mo entre la mémoire demandée à l'ordonnanceur et celle que GAMESS peut utiliser. Si les résultats de la tâche sont incomplets et que le fichier `slurm-{JOBID}.out` contient un message comme *slurmstepd: error: Exceeded step/job memory limit at some point*, ceci indique que Slurm a cessé l'exécution de la tâche parce qu'elle utilisait plus de mémoire que la quantité demandée. Dans ce cas, vous pouvez réduire la valeur de `MWORDS` ou `MEMDDI` dans le fichier en entrée, ou augmenter la valeur de  `--mem-per-cpu`  dans le script de soumission.

## References 
<references />