---
title: "GNU Parallel/fr"
tags:
  []

keywords:
  []
---

== Introduction == 
[parallel](http://www.gnu.org/software/parallel/) est un outil de la suite GNU qui permet d'exécuter plusieurs tâches séquentielles en parallèle sur un ou plusieurs nœuds. Il s'agit d'un outil particulièrement utile pour exécuter un grand nombre de tâches séquentielles de courte durée ou de durée variable, sur un jeu de paramètres (exploration de paramètres). Cette documentation traite des notions de base seulement; pour plus d'information, consultez la [documentation du produit](http://www.gnu.org/software/parallel/man.html).

Par défaut, <tt>parallel</tt> maximise l'utilisation de la ressource en exécutant autant de tâches que le nombre de cœurs alloués par l'ordonnanceur. Vous pouvez changer ceci avec l'option <tt>--jobs</tt>, suivie du nombre de tâches que GNU Parallel devrait exécuter simultanément. Quand une tâche est terminée, <tt>parallel</tt> commence automatiquement la prochaine; ainsi, le nombre maximum de tâches est toujours en exécution.

==Commandes de base== 
Les accolades {} indiquent les paramètres passés en argument à la commande à exécuter.  Ainsi, pour exécuter la commande gzip sur tous les fichiers texte d'un répertoire, vous utiliserez <tt>gzip</tt>  ainsi 

```bash

```
 parallel gzip  }}

On peut aussi utiliser <tt>:::</tt>, comme dans l'exemple suivant 

```bash

```
 ::: $(seq 1 3)
|result=
1
2
3
}}

Les commandes de GNU Parallel sont appelées <i>jobs</i>.  Il ne faut pas confondre ces <i>jobs</i> avec les tâches (aussi des *jobs*) qui sont des scripts exécutés par l'ordonnanceur;  dans ce contexte, les tâches exécutées avec parallel sont des <i>sous-tâches</i>.

## Spécifier plusieurs arguments 
Vous pouvez aussi utiliser plusieurs arguments en les numérotant ainsi 

```bash

```
1 2 ::: $(seq 1 3) ::: $(seq 2 3)
|result=
1 2
1 3
2 2
2 3
3 2
3 3
}}

== Utiliser le contenu d'un fichier comme liste d'arguments == 
La syntaxe <tt>::::</tt> permet d'utiliser le contenu d'un fichier comme valeurs des arguments. Ainsi, si votre liste de paramètres est dans le fichier <tt>maliste.txt</tt>, vous pouvez faire afficher son contenu ainsi :

```bash

```
1 :::: maliste.txt}}

== Utiliser le contenu d'un fichier comme liste de commandes == 
Les lignes dans un fichier peuvent représenter des sous-tâches à exécuter en parallèle; dans ce cas, chaque sous-tâche doit être sur une ligne distincte.  Ainsi, si votre liste de sous-tâches se trouve dans le fichier `my_commands.txt`, vous pouvez la faire exécuter ainsi :

```bash
parallel < my_commands.txt
```

Remarquez qu'aucune commande ou argument n'est passé à Parallel. Ce mode d'utilisation est particulièrement utile si les sous-tâches contiennent des symboles spécifiques de GNU Parallel ou si les sous-commandes contiennent quelques commandes, par exemple `cd dir1 && ./executable`.

L'exemple suivant montre comment faire exécuter une tâche par Slurm avec GNU Parallel. La liste des commandes dans `my_commands.txt` sera exécutée en séquence avec 4 CPU. Dès qu'une commande est terminée, une nouvelle commande est lancée afin de toujours avoir 4 commandes en marche à la fois, jusqu'à la fin de la liste.

<tabs>
<tab name="Script">

**`run_gnuparallel_test.sh`**
```bash
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --cpus-per-task=4
#SBATCH --time=00-02:00
#SBATCH --mem=4000M     # Total memory for all tasks

parallel --joblog parallel.log < ./my_commands.txt
```

</tab>

<tab name="Liste des tâches">

**`my_commands.txt`**
```txt
command1
command2
command3
command4
command5
command6
command7
command8
command9
```

</tab>

</tabs>

## Utiliser plusieurs nœuds 

Vous pouvez aussi distribuer votre travail sur plusieurs nœuds d'une grappe, comme dans l'exemple suivant &nbsp;:
{{Command
|scontrol show hostname > ./node_list_${SLURM_JOB_ID}
}}
{{Command
|parallel --jobs $SLURM_NTASKS_PER_NODE --sshloginfile ./node_list_${SLURM_JOB_ID} --env MY_VARIABLE --workdir $PWD --sshdelay 30 ./my_program
}}
Nous créons ici un fichier qui contient la liste des nœuds pour indiquer à GNU parallel quels sont ceux à utiliser pour distribuer les tâches. L'option <tt>--env</tt> nous permet de transférer à tous les nœuds une variable d'environnement particulière et l'option <tt>--workdir</tt> fait en sorte que les tâches GNU parallel seront lancées dans le même répertoire que le nœud principal.

Par exemple, quand plusieurs tâches [OpenMP](openmp-fr.md) sont soumises ensemble avec <tt>--nodes=N</tt>, <tt>--ntasks-per-node=5</tt> et <tt>--cpus-per-task=8</tt>, la commande suivante va gérer tous les processus à démarrer sur tous les nœuds réservés, ainsi que le nombre de fils OpenMP par processus.

```bash

```
$SLURM_CPUS_PER_TASK
}}
{{Command
|parallel --jobs $SLURM_NTASKS_PER_NODE --sshloginfile ./node_list_${SLURM_JOB_ID} --workdir $PWD --env OMP_NUM_THREADS --sshdelay 30 ./my_program
}}
Dans ce cas, <tt>5*N</tt> processus OpenMP travaillent simultanément et l'utilisation de CPU peut aller jusqu'à 800&nbsp;%.

==Suivi des commandes exécutées ou  des commandes ayant échoué; fonctionnalités de redémarrage== 
L'argument <tt>--joblog JOBLOGFILE</tt> produit le journal des commandes exécutées. Le fichier JOBLOGFILE contient alors la liste des commandes complétées avec l'heure de début, la durée, le nom du nœud de calcul et le code de sortie, par exemple

```bash

```
 parallel --joblog gzip.log gzip  }}

Cette fonction offre plusieurs options pour le redémarrage.  Si la commande  <tt>parallel</tt> était interrompue (c'est-à-dire que la tâche prenait plus de temps que spécifié), elle pourrait reprendre son cours en utilisant l'option <tt>--resume</tt>, par exemple 

```bash

```
 parallel --resume --joblog gzip.log gzip  }}
Les nouvelles tâches seront ajoutées à la fin du même journal.

Si certaines des sous-commandes ont échoué (c'est-à-dire que le code de sortie est différent de zéro) et vous pensez que l'erreur est résolue, ces sous-commandes peuvent être exécutées à nouveau avec  <tt>--resume-failed</tt>, par exemple

```bash

```
 parallel --resume-failed --joblog gzip.log gzip  }}
Ceci exécute également les sous-tâches qui n'étaient pas prises en compte auparavant.

## Travailler avec des fichiers volumineux
Si par exemple nous voulons compter en parallèle le nombre de caractères dans le grand fichier [FASTA](https://fr.wikipedia.org/wiki/FASTA_(format_de_fichier)) nommé <tt>database.fa</tt> à l'aide d'une tâche de 8 cœurs, nous devons utiliser les arguments <tt>--pipepart</tt> et <tt>--block</tt> pour gérer efficacement de grandes portions du fichier. 

```bash
parallel --jobs $SLURM_CPUS_PER_TASK --keep-order --block -1 --recstart '>' --pipepart wc :::: database.fa
```

En variant la taille de <tt>block</tt> nous avons :

{| class="wikitable"
! 
! Quantité de cœurs
! Taille de la BD
! Taille des blocs
! Quantité de tâches parallèles
! Cœurs utilisés
! Durée de la tâche
|-
| 1
| style="text-align: right;" | 8
| style="text-align: right;" | 827Mo
| style="text-align: right;" | 10Mo
| style="text-align: right;" | 83
| style="text-align: right;" | 8
| 0m2.633s
|-
| 2
| style="text-align: right;" | 8
| style="text-align: right;" | 827Mo
| style="text-align: right;" | 100Mo
| style="text-align: right;" | 9
| style="text-align: right;" | 8
| 0m2.042s
|-
| 3
| style="text-align: right;" | 8
| style="text-align: right;" | 827Mo
| style="text-align: right;" | 827Mo
| style="text-align: right;" | 1
| style="text-align: right;" | 1
| 0m10.877s
|-
| 4
| style="text-align: right;" | 8
| style="text-align: right;" | 827Mo
| style="text-align: right;" | -1
| style="text-align: right;" | 8
| style="text-align: right;" | 8
| 0m1.734s
|}
Nous constatons que le fait d'utiliser la bonne taille de bloc a un impact réel sur l'efficacité et la quantité de cœurs utilisés. 
Sur la première ligne, la taille des blocs est trop petite et plusieurs tâches sont distribuées sur les cœurs disponibles. Sur la deuxième ligne, la taille des blocs est plus appropriée puisque la quantité de tâches se rapproche de la quantité de cœurs disponibles. 
Sur la troisième ligne, la taille des blocs est trop grande et un seul cœur est utilisé sur les 8, ce qui n'est pas efficace. 
Sur la dernière ligne, on remarque que de laisser GNU Parallel s'adapter et décider de lui-même de la taille des blocs est souvent plus rapide.

## Exécuter des centaines ou des milliers de simulations 
Commencez par déterminer la quantité de ressources nécessaires pour une simulation; vous pourrez ensuite déterminer la quantité totale de ressources requises par la tâche.

Dans les exemples suivants, les scripts de soumission sont pour 1 simulation en série avec 2Go de mémoire, 1  cœur et 5 minutes, et 1000 simulations. Avec 1 cœur, la durée serait de 83,3 heures.

Avec 1 nœud de 32 cœurs, la durée serait de 6 heures. Il serait aussi possible d'utiliser plus d'un nœud (voir [#Utiliser plusieurs nœuds](#utiliser-plusieurs-nœuds.md)).

### Liste d'arguments 
Comme mentionné dans la section [#Utiliser le contenu d'un fichier comme liste d'arguments](#utiliser-le-contenu-d'un-fichier-comme-liste-d'arguments.md), vous pouvez utiliser un fichier qui contient tous les paramètres. Dans ce cas, les paramètres sont séparés par un caractère de tabulation (<tt>\t</tt>) et chaque ligne correspond à une simulation.
<tabs>
<tab name="Paramètres">

**`my_parameters.txt`**
```txt
1   1
1   2
1   3
...
```

</tab>

<tab name="Script">
{{File
|name=sim_submit.sh
|lang="bash"
|contents=
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --nodes=1
#SBATCH --cpus-per-task=32
#SBATCH --time=03:00:00
#SBATCH --mem-per-cpu=2G

# Read the parameters, placing each column to their respective argument
parallel -j $SLURM_CPUS_PER_TASK --colsep '\t' my_simulator --alpha {1} --beta {2} :::: ./my_parameters.txt
}}
</tab>
</tabs>

### Liste de commandes 
Comme mentionné dans la section [#Utiliser le contenu d'un fichier comme liste de commandes](#utiliser-le-contenu-d'un-fichier-comme-liste-de-commandes.md), vous pouvez utiliser un fichier qui contient toutes les commandes et leurs paramètres. 
<tabs>
<tab name="Commandes">

**`my_commands.txt`**
```txt
my_simulator --alpha 1 --beta 1
my_simulator --alpha 1 --beta 2
my_simulator --alpha 1 --beta 3
...
```

</tab>

<tab name="Script">

**`sim_submit.sh`**
```bash
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --nodes=1
#SBATCH --cpus-per-task=32
#SBATCH --time=03:00:00
#SBATCH --mem-per-cpu=2G

parallel -j $SLURM_CPUS_PER_TASK < ./my_commands.txt
```

</tab>
</tabs>

### Plusieurs arguments 
Vous pouvez utiliser GNU Parallel pour générer les paramètres et les associer aux commandes.

{{File
|name=sim_submit.sh
|lang="bash"
|contents=
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --nodes=1
#SBATCH --cpus-per-task=32
#SBATCH --time=03:00:00
#SBATCH --mem-per-cpu=2G

# Generates 1000 simulations where the alpha argument ranges from 1-10, and beta from 1-100
# placing each source to their respective argument
parallel -j $SLURM_CPUS_PER_TASK my_simulator --alpha {1} --beta {2} ::: {1..10} ::: {1..100}
}}

## Voir aussi
* [META](meta:-a-package-for-job-farming-fr.md)
* [GLOST](glost-fr.md)
* [Vecteurs de tâches](job-arrays-fr.md)