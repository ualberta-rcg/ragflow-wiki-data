---
title: "GNU Parallel/fr"
slug: "gnu_parallel"
lang: "fr"

source_wiki_title: "GNU Parallel/fr"
source_hash: "09e58ae1e82e474725e721b6840258a9"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:23:55.750676+00:00"

tags:
  []

keywords:
  - "Liste des tâches"
  - "liste de commandes"
  - "GNU parallel"
  - "--pipepart et --block"
  - "Slurm"
  - "Script bash"
  - "parallel"
  - "SLURM_CPUS_PER_TASK"
  - "tâches parallèles"
  - "GNU Parallel"
  - "sous-tâches"
  - "simulations"
  - "Liste de commandes"
  - "fichier FASTA"
  - "script de soumission"
  - "plusieurs nœuds"
  - "script bash"
  - "ordonnanceur"
  - "taille de bloc"
  - "exécution en parallèle"
  - "fichier"
  - "fichiers volumineux"
  - "journal des commandes"
  - "vecteurs de tâches"
  - "redémarrage"
  - "paramètres"
  - "8 cœurs"
  - "compter en parallèle"
  - "my_commands.txt"

questions:
  - "Quel est le rôle principal de l'outil GNU Parallel et comment peut-on contrôler le nombre de tâches exécutées simultanément ?"
  - "Quelles sont les différentes syntaxes permettant de passer des arguments aux commandes, que ce soit directement en ligne de commande ou à partir d'un fichier ?"
  - "Comment configurer GNU Parallel pour lire et exécuter une liste de sous-tâches ou de commandes complètes à partir d'un fichier texte, notamment avec un ordonnanceur comme Slurm ?"
  - "Quelles sont les ressources matérielles et temporelles allouées par le script Slurm ?"
  - "Comment la commande GNU Parallel gère-t-elle l'exécution et la journalisation des tâches ?"
  - "Quel est le rôle du fichier \"my_commands.txt\" mentionné dans l'onglet de la liste des tâches ?"
  - "Pourquoi l'utilisation de GNU parallel sur plusieurs nœuds est-elle déconseillée et quelle option est recommandée pour atténuer les problèmes de connexion SSH ?"
  - "Quelles options permettent de générer un journal d'exécution des tâches et de relancer uniquement les commandes interrompues ou ayant échoué ?"
  - "Quels arguments spécifiques doivent être utilisés avec GNU parallel pour diviser et traiter efficacement des fichiers de très grande taille ?"
  - "Quel est l'impact de la taille des blocs sur l'efficacité et l'utilisation des cœurs lors de l'exécution de tâches avec GNU Parallel ?"
  - "Comment doit-on procéder pour déterminer la quantité totale de ressources requises avant de lancer des centaines ou des milliers de simulations ?"
  - "Comment peut-on structurer et utiliser un fichier externe pour fournir une liste d'arguments ou de commandes à un script de soumission ?"
  - "Comment peut-on gérer efficacement le traitement de fichiers volumineux lors de l'exécution de tâches en parallèle ?"
  - "Quel est le rôle exact des arguments `--pipepart` et `--block` mentionnés dans le texte ?"
  - "Quelle méthode est illustrée pour compter le nombre de caractères d'un fichier FASTA à l'aide d'une tâche de 8 cœurs ?"
  - "Comment utiliser GNU Parallel dans un script SLURM pour exécuter plusieurs tâches simultanément ?"
  - "Quelle est la procédure pour lire et exécuter une liste de commandes pré-définies à partir d'un fichier texte ?"
  - "Comment générer automatiquement des combinaisons de multiples arguments directement via la commande GNU Parallel sans utiliser de fichier externe ?"
  - "Comment la commande `parallel` utilise-t-elle la variable `$SLURM_CPUS_PER_TASK` pour gérer l'exécution des tâches ?"
  - "À quoi sert le fichier `my_parameters.txt` lors du lancement du programme `my_simulator` ?"
  - "Quelle est la méthode décrite dans la section \"Liste de commandes\" pour exécuter un ensemble de tâches à partir d'un fichier texte ?"
  - "Comment utiliser GNU Parallel dans un script SLURM pour exécuter plusieurs tâches simultanément ?"
  - "Quelle est la procédure pour lire et exécuter une liste de commandes pré-définies à partir d'un fichier texte ?"
  - "Comment générer automatiquement des combinaisons de multiples arguments directement via la commande GNU Parallel sans utiliser de fichier externe ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Introduction
[parallel](http://www.gnu.org/software/parallel/parallel) est un outil de la suite GNU qui permet d'exécuter plusieurs tâches séquentielles en parallèle sur un ou plusieurs nœuds. Il s'agit d'un outil particulièrement utile pour exécuter un grand nombre de tâches séquentielles de courte durée ou de durée variable, sur un jeu de paramètres (exploration de paramètres). Cette documentation traite des notions de base seulement; pour plus d'information, consultez la [documentation du produit](http://www.gnu.org/software/parallel/man.html).

Par défaut, `parallel` maximise l'utilisation de la ressource en exécutant autant de tâches que le nombre de cœurs alloués par l'ordonnanceur. Vous pouvez changer ceci avec l'option `--jobs`, suivie du nombre de tâches que GNU Parallel devrait exécuter simultanément. Quand une tâche est terminée, `parallel` commence automatiquement la prochaine; ainsi, le nombre maximum de tâches est toujours en exécution.

## Commandes de base
Les accolades `{}` indiquent les paramètres passés en argument à la commande à exécuter. Ainsi, pour exécuter la commande gzip sur tous les fichiers texte d'un répertoire, vous utiliserez `gzip` ainsi :

```bash
ls *.txt | parallel gzip {}
```

On peut aussi utiliser `:::`, comme dans l'exemple suivant :

```bash
parallel echo {} ::: $(seq 1 3)
```

Résultat :

```text
1
2
3
```

Les commandes de GNU Parallel sont appelées *jobs*. Il ne faut pas confondre ces *jobs* avec les tâches (aussi des *jobs*) qui sont des scripts exécutés par l'ordonnanceur; dans ce contexte, les tâches exécutées avec parallel sont des *sous-tâches*.

## Spécifier plusieurs arguments
Vous pouvez aussi utiliser plusieurs arguments en les numérotant ainsi :

```bash
parallel echo {1} {2} ::: $(seq 1 3) ::: $(seq 2 3)
```

Résultat :

```text
1 2
1 3
2 2
2 3
3 2
3 3
```

## Utiliser le contenu d'un fichier comme liste d'arguments
La syntaxe `::::` permet d'utiliser le contenu d'un fichier comme valeurs des arguments. Ainsi, si votre liste de paramètres est dans le fichier `maliste.txt`, vous pouvez faire afficher son contenu ainsi :

```bash
parallel echo {1} :::: maliste.txt
```

## Utiliser le contenu d'un fichier comme liste de commandes
Les lignes dans un fichier peuvent représenter des sous-tâches à exécuter en parallèle; dans ce cas, chaque sous-tâche doit être sur une ligne distincte. Ainsi, si votre liste de sous-tâches se trouve dans le fichier `my_commands.txt`, vous pouvez la faire exécuter ainsi :

```bash
parallel < my_commands.txt
```

Remarquez qu'aucune commande ou argument n'est passé à Parallel. Ce mode d'utilisation est particulièrement utile si les sous-tâches contiennent des symboles spécifiques de GNU Parallel ou si les sous-commandes contiennent quelques commandes, par exemple `cd dir1 && ./executable`.

L'exemple suivant montre comment faire exécuter une tâche par Slurm avec GNU Parallel. La liste des commandes dans `my_commands.txt` sera exécutée en séquence avec 4 CPU. Dès qu'une commande est terminée, une nouvelle commande est lancée afin de toujours avoir 4 commandes en marche à la fois, jusqu'à la fin de la liste.

=== "Script"
    ```bash
    #!/bin/bash
    #SBATCH --account=def-someuser
    #SBATCH --cpus-per-task=4
    #SBATCH --time=00-02:00
    #SBATCH --mem=4000M     # Total memory for all tasks

    parallel --joblog parallel.log < ./my_commands.txt
    ```

=== "Liste des tâches"
    ```text
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

## Utiliser plusieurs nœuds
!!! warning "NON RECOMMANDÉ"
    Même si GNU parallel peut être utilisé avec plusieurs nœuds d'une grappe, il n'est pas recommandé de le faire, car des problèmes pourraient survenir, surtout dans le cas des tâches courtes. Ceci est dû au fait qu'une session SSH doit être lancée sur un nœud distant, ce qui est souvent une opération de plusieurs secondes et la session est susceptible d'être bloquée. Si vous choisissez de le faire, assurez-vous d'utiliser l'option `--sshdelay 30` pour avoir un délai d'au moins 30 secondes entre chaque tâche.

Vous pouvez aussi distribuer votre travail sur plusieurs nœuds d'une grappe, comme dans l'exemple suivant :

```bash
scontrol show hostname > ./node_list_${SLURM_JOB_ID}
```

```bash
parallel --jobs $SLURM_NTASKS_PER_NODE --sshloginfile ./node_list_${SLURM_JOB_ID} --env MY_VARIABLE --workdir $PWD --sshdelay 30 ./my_program
```

Nous créons ici un fichier qui contient la liste des nœuds pour indiquer à GNU parallel quels sont ceux à utiliser pour distribuer les tâches. L'option `--env` nous permet de transférer à tous les nœuds une variable d'environnement particulière et l'option `--workdir` fait en sorte que les tâches GNU parallel seront lancées dans le même répertoire que le nœud principal.

Par exemple, quand plusieurs tâches [OpenMP](../programming/openmp.md) sont soumises ensemble avec `--nodes=N`, `--ntasks-per-node=5` et `--cpus-per-task=8`, la commande suivante va gérer tous les processus à démarrer sur tous les nœuds réservés, ainsi que le nombre de fils OpenMP par processus.

```bash
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
```

```bash
parallel --jobs $SLURM_NTASKS_PER_NODE --sshloginfile ./node_list_${SLURM_JOB_ID} --workdir $PWD --env OMP_NUM_THREADS --sshdelay 30 ./my_program
```

Dans ce cas, `5*N` processus OpenMP travaillent simultanément et l'utilisation de CPU peut aller jusqu'à 800 %.

## Suivi des commandes exécutées ou des commandes ayant échoué; fonctionnalités de redémarrage
L'argument `--joblog JOBLOGFILE` produit le journal des commandes exécutées. Le fichier JOBLOGFILE contient alors la liste des commandes complétées avec l'heure de début, la durée, le nom du nœud de calcul et le code de sortie, par exemple :

```bash
ls *.txt | parallel --joblog gzip.log gzip {}
```

Cette fonction offre plusieurs options pour le redémarrage. Si la commande `parallel` était interrompue (c'est-à-dire que la tâche prenait plus de temps que spécifié), elle pourrait reprendre son cours en utilisant l'option `--resume`, par exemple :

```bash
ls *.txt | parallel --resume --joblog gzip.log gzip {}
```

Les nouvelles tâches seront ajoutées à la fin du même journal.

Si certaines des sous-commandes ont échoué (c'est-à-dire que le code de sortie est différent de zéro) et vous pensez que l'erreur est résolue, ces sous-commandes peuvent être exécutées à nouveau avec `--resume-failed`, par exemple :

```bash
ls *.txt | parallel --resume-failed --joblog gzip.log gzip {}
```

Ceci exécute également les sous-tâches qui n'étaient pas prises en compte auparavant.

## Travailler avec des fichiers volumineux
Si par exemple nous voulons compter en parallèle le nombre de caractères dans le grand fichier [FASTA](https://fr.wikipedia.org/wiki/FASTA_(format_de_fichier)) nommé `database.fa` à l'aide d'une tâche de 8 cœurs, nous devons utiliser les arguments `--pipepart` et `--block` pour gérer efficacement de grandes portions du fichier.

```bash
parallel --jobs $SLURM_CPUS_PER_TASK --keep-order --block -1 --recstart '>' --pipepart wc :::: database.fa
```

En variant la taille de `block` nous avons :

| | Nombre de cœurs | Taille de la BD | Taille des blocs | Nombre de tâches parallèles | Cœurs utilisés | Durée de la tâche |
|---|---------------:|----------------:|------------------:|------------------------------:|---------------:|-------------------|
| 1 |              8 |           827Mo |              10Mo |                            83 |              8 | 0m2.633s          |
| 2 |              8 |           827Mo |             100Mo |                             9 |              8 | 0m2.042s          |
| 3 |              8 |           827Mo |             827Mo |                             1 |              1 | 0m10.877s         |
| 4 |              8 |           827Mo |                -1 |                             8 |              8 | 0m1.734s          |

Nous constatons que le fait d'utiliser la bonne taille de bloc a un impact réel sur l'efficacité et le nombre de cœurs utilisés.
Sur la première ligne, la taille des blocs est trop petite et plusieurs tâches sont distribuées sur les cœurs disponibles. Sur la deuxième ligne, la taille des blocs est plus appropriée puisque le nombre de tâches se rapproche du nombre de cœurs disponibles.
Sur la troisième ligne, la taille des blocs est trop grande et un seul cœur est utilisé sur les 8, ce qui n'est pas efficace.
Sur la dernière ligne, on remarque que de laisser GNU Parallel s'adapter et décider de lui-même de la taille des blocs est souvent plus rapide.

## Exécuter des centaines ou des milliers de simulations
Commencez par déterminer la quantité de ressources nécessaires pour une simulation; vous pourrez ensuite déterminer la quantité totale de ressources requises par la tâche.

Dans les exemples suivants, les scripts de soumission sont pour 1 simulation en série avec 2Go de mémoire, 1 cœur et 5 minutes, et 1000 simulations. Avec 1 cœur, la durée serait de 83,3 heures.

Avec 1 nœud de 32 cœurs, la durée serait de 6 heures. Il serait aussi possible d'utiliser plus d'un nœud (voir [#utiliser-plusieurs-noeuds](#utiliser-plusieurs-noeuds)).

### Liste d'arguments
Comme mentionné dans la section [#utiliser-le-contenu-dun-fichier-comme-liste-darguments](#utiliser-le-contenu-dun-fichier-comme-liste-darguments), vous pouvez utiliser un fichier qui contient tous les paramètres. Dans ce cas, les paramètres sont séparés par un caractère de tabulation (`\t`) et chaque ligne correspond à une simulation.

=== "Paramètres"
    ```text
    1   1
    1   2
    1   3
    ...
    ```

=== "Script"
    ```bash
    #!/bin/bash
    #SBATCH --account=def-someuser
    #SBATCH --nodes=1
    #SBATCH --cpus-per-task=32
    #SBATCH --time=03:00:00
    #SBATCH --mem-per-cpu=2G

    # Read the parameters, placing each column to their respective argument
    parallel -j $SLURM_CPUS_PER_TASK --colsep '\t' my_simulator --alpha {1} --beta {2} :::: ./my_parameters.txt
    ```

### Liste de commandes
Comme mentionné dans la section [#utiliser-le-contenu-dun-fichier-comme-liste-de-commandes](#utiliser-le-contenu-dun-fichier-comme-liste-de-commandes), vous pouvez utiliser un fichier qui contient toutes les commandes et leurs paramètres.

=== "Commandes"
    ```text
    my_simulator --alpha 1 --beta 1
    my_simulator --alpha 1 --beta 2
    my_simulator --alpha 1 --beta 3
    ...
    ```

=== "Script"
    ```bash
    #!/bin/bash
    #SBATCH --account=def-someuser
    #SBATCH --nodes=1
    #SBATCH --cpus-per-task=32
    #SBATCH --time=03:00:00
    #SBATCH --mem-per-cpu=2G

    parallel -j $SLURM_CPUS_PER_TASK < ./my_commands.txt
    ```

### Plusieurs arguments
Vous pouvez utiliser GNU Parallel pour générer les paramètres et les associer aux commandes.

```bash
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --nodes=1
#SBATCH --cpus-per-task=32
#SBATCH --time=03:00:00
#SBATCH --mem-per-cpu=2G

# Generates 1000 simulations where the alpha argument ranges from 1-10, and beta from 1-100
# placing each source to their respective argument
parallel -j $SLURM_CPUS_PER_TASK my_simulator --alpha {1} --beta {2} ::: {1..10} ::: {1..100}
```

## Voir aussi
* [META](meta-a-package-for-job-farming.md)
* [GLOST](glost.md)
* [Vecteurs de tâches](job_arrays.md)