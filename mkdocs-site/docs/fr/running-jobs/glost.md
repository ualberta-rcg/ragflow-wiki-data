---
title: "GLOST/fr"
slug: "glost"
lang: "fr"

source_wiki_title: "GLOST/fr"
source_hash: "ff9c8c4bae4f1b4bef19b00031821ea0"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:22:18.697125+00:00"

tags:
  []

keywords:
  - "liste de tâches"
  - "Liste des tâches"
  - "Temps d'exécution"
  - "nargument"
  - "GLOST"
  - "Tâches séquentielles"
  - "fichiers en sortie"
  - "répertoire"
  - "tâches séquentielles"
  - "RUN_${nargument}"
  - "option ou argument"
  - "module"
  - "list_glost_tasks.txt"
  - "répertoires différents"
  - "script"
  - "commandes"
  - "hostname"
  - "exécution de la tâche"
  - "redémarrer une tâche"
  - "tâche MPI"
  - "ordonnanceur"
  - "srun"
  - "processeurs"
  - "log_run.txt"
  - "Greedy Launcher Of Small Tasks"
  - "glost_launch"
  - "vecteurs de tâches"
  - "fichiers temporaires"
  - "sleep 360"
  - "scripts"
  - "Tools for development"
  - "glost/0.3.1"
  - "OpenMPI"

questions:
  - "Qu'est-ce que l'outil GLOST et pour quels types de tâches est-il particulièrement utile ?"
  - "De quelle manière GLOST parvient-il à alléger le fardeau de l'ordonnanceur (Slurm) lors de l'exécution d'un grand nombre de tâches ?"
  - "Quels sont les avantages du paquet logiciel alternatif META par rapport à GLOST selon le texte ?"
  - "What does the acronym GLOST stand for in the context of this module?"
  - "Under which property or category is the GLOST software classified?"
  - "What prerequisite step must be completed before the glost/0.3.1 module can be loaded?"
  - "Comment activer GLOST dans son environnement et quelle est la syntaxe de base pour exécuter une liste de tâches ?"
  - "Comment estimer le temps d'exécution global d'une tâche GLOST en fonction du nombre de sous-tâches et des cœurs alloués ?"
  - "Quelles précautions faut-il prendre lors de la création du fichier de liste de tâches pour optimiser les ressources et éviter les conflits de fichiers en sortie ?"
  - "Pourquoi faut-il éviter que les résultats de différentes tâches utilisent les mêmes fichiers temporaires ou de sortie dans un même répertoire ?"
  - "Comment l'utilisation d'une variable permet-elle de rediriger correctement les résultats et d'identifier l'exécution d'une tâche spécifique ?"
  - "Quelle solution d'organisation des dossiers doit être envisagée si les tâches partagent inévitablement les mêmes noms de fichiers ?"
  - "Comment doit-on séparer plusieurs commandes exécutées séquentiellement au sein d'une même tâche GLOST ?"
  - "Quelle commande spécifique doit être utilisée dans le script de soumission pour lancer l'exécution du fichier contenant la liste des tâches ?"
  - "Quelles précautions faut-il prendre pour éviter les conflits de fichiers lors de l'exécution de plusieurs tâches dans le même répertoire ?"
  - "Comment GLOST gère-t-il l'assignation et l'exécution d'une liste de tâches sur les processeurs disponibles ?"
  - "Pourquoi est-il parfois nécessaire d'exécuter des tâches séquentielles dans des répertoires distincts lors de l'utilisation de GLOST ?"
  - "Quelles sont les commandes et directives requises dans le script SLURM pour charger les modules nécessaires et lancer l'application GLOST ?"
  - "Quel est le rôle principal de la commande `glost_launch` exécutée via `srun` dans ce script ?"
  - "Quelles actions spécifiques sont effectuées par chaque tâche définie dans le fichier `list_glost_tasks.txt` ?"
  - "Comment le script principal assure-t-il le suivi temporel de son exécution et l'enregistrement de son code de retour ?"
  - "What is the overall purpose of this sequence of shell commands?"
  - "Why does the script pause execution for 360 seconds before generating the log files?"
  - "What specific information is being recorded in the `log_run.txt` files within each newly created directory?"
  - "Comment doit-on procéder pour redémarrer une tâche GLOST dont le temps d'exécution a été sous-estimé ?"
  - "Quelle commande permet de copier les exemples de scripts GLOST dans son propre répertoire de travail ?"
  - "Quels sont les autres outils ou concepts de calcul énumérés dans la section des références ?"
  - "Comment doit-on procéder pour redémarrer une tâche GLOST dont le temps d'exécution a été sous-estimé ?"
  - "Quelle commande permet de copier les exemples de scripts GLOST dans son propre répertoire de travail ?"
  - "Quels sont les autres outils ou concepts de calcul énumérés dans la section des références ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Introduction

[GLOST](https://github.com/cea-hpc/glost) (pour *Greedy Launcher Of Small Tasks*) est un outil pour exécuter un grand nombre de tâches séquentielles de courte durée ou de durée variable, ou avec des balayages de paramètres. Son fonctionnement est semblable à celui de [GNU Parallel](gnu_parallel.md) ou d’un [vecteur de tâches](vecteurs-de-taches.md), mais avec une syntaxe simplifiée.

GLOST utilise l’enveloppe (*wrapper*) `glost_launch` et les commandes [MPI](../software/mpi.md) `srun`, `mpiexec` et `mpirun`. Un fichier texte nommé **list_glost_tasks.txt** regroupe les tâches et est employé comme argument pour l’enveloppe `glost_launch`.

GLOST est particulièrement utile dans les cas suivants :

*   plusieurs tâches séquentielles de durée comparable;
*   plusieurs tâches séquentielles de courte durée;
*   tâches séquentielles avec paramètres variables (balayage de paramètres).

Le principe est de grouper plusieurs tâches séquentielles et de les faire exécuter dans une tâche MPI pouvant utiliser plusieurs cœurs (un ou plusieurs nœuds). Avec moins de tâches dans la file d'attente, [l'ordonnanceur](executer-des-taches.md) sera moins sollicité.

Vous pourriez considérer d'utiliser plutôt le paquet logiciel [META](meta-farm.md) développé par une de nos équipes et qui comporte d'importants avantages par rapport à GLOST. Avec META, le temps d'attente total peut être beaucoup plus court; la surcharge imposée est moindre (moins de cycles CPU gaspillés); un mécanisme pratique permet de resoumettre les calculs qui ont échoué ou qui n'ont jamais été exécutés; et META peut traiter autant les tâches séquentielles que les tâches multifils, MPI, GPU et hybrides.

!!! note "Remarque"
    Lisez cette page au complet pour savoir si cet outil peut servir dans vos travaux. Si c’est le cas, vous pourrez demander l'assistance de [l'équipe technique](support-technique.md) pour modifier vos processus.

## Avantages

Selon leur durée et leur nombre, plusieurs tâches séquentielles sont groupées dans une ou plusieurs tâches MPI.

Le fait de soumettre plusieurs tâches séquentielles en même temps peut ralentir l’ordonnanceur et causer de longs délais de réponse et des interruptions fréquentes dans l’exécution de `sbatch` ou `squeue`. La solution de GLOST est de grouper toutes les tâches séquentielles dans un même fichier nommé **list_glost_tasks.txt** et de soumettre une tâche MPI avec l’enveloppe `glost_launch`. Ceci diminue de beaucoup le nombre de tâches dans la file d'attente et produit donc moins de demandes à traiter par l’ordonnanceur que si les tâches étaient soumises séparément. Pour soumettre plusieurs tâches séquentielles sans délai, GLOST atténue le fardeau de Slurm.

Avec GLOST, l’utilisateur soumet et traite quelques tâches MPI plutôt que des centaines ou des milliers de tâches séquentielles.

## Modules

GLOST utilise OpenMPI pour grouper des tâches séquentielles dans une tâche MPI. Vous devez charger OpenMPI et le module GLOST correspondant. Pour plus d’information, consultez [Utiliser des modules](../programming/utiliser_des_modules.md). Pour voir les modules GLOST disponibles, utilisez la commande `module spider glost`. Avant de soumettre une tâche, assurez-vous de pouvoir charger GLOST et les autres modules nécessaires à l’exécution de votre application.

```bash
$  module spider glost/0.3.1

--------------------------------------------------------------------------------------------------------------------------------------
  glost: glost/0.3.1
--------------------------------------------------------------------------------------------------------------------------------------
    Description:
      This is GLOST, the Greedy Launcher Of Small Tasks. 

    Properties:
      Tools for development / Outils de développement

    You will need to load all module(s) on any one of the lines below before the "glost/0.3.1" module is available to load.

      StdEnv/2023  gcc/12.3  openmpi/4.1.5
      StdEnv/2023  intel/2023.2.1  openmpi/4.1.5
 
    Help:
      
      Description
      ===========
      This is GLOST, the Greedy Launcher Of Small Tasks.
      
      
      More information
      ================
       - Homepage: https://github.com/cea-hpc/glost

```
Si un module OpenMPI se trouve déjà dans votre environnement, ce qui est le cas pour l’environnement par défaut, ajouter `module load glost` à la liste des modules dont vous avez besoin est suffisant pour activer GLOST. Pour vous assurer que GLOST et les autres modules sont présents, lancez la commande `module list`.

## Utilisation

### Syntaxe

Les formes suivantes sont possibles :

```bash
srun glost_launch list_glost_tasks.txt

mpiexec glost_launch list_glost_tasks.txt 

mpirun glost_launch list_glost_tasks.txt
```

### Nombre de cœurs et nombre de tâches

Les tâches séquentielles sont attribuées aux cœurs disponibles par une distribution cyclique. L’enveloppe (*wrapper*) GLOST commence par la première tâche (ou ligne dans la liste) et lui assigne un processeur. Ceci est répété jusqu’à la fin de la liste ou jusqu’à ce que la durée de la tâche soit atteinte. Le nombre de cœurs ne correspond pas nécessairement au nombre de tâches listées. Cependant, pour optimiser les ressources, assurez-vous que les tâches ont une durée d’exécution similaire et qu’elles peuvent être distribuées également sur le nombre de cœurs demandés. Examinons les cas suivants :

*   Avec un grand nombre de tâches séquentielles très courtes (par exemple des centaines ou des milliers de tâches de quelques minutes chacune), soumettez une ou plusieurs tâches GLOST pour les exécuter en utilisant un nombre limité de cœurs. Vous pouvez soumettre les tâches avec une courte durée et par nœud afin de profiter du remplissage et de l’ordonnanceur.
*   Avec des dizaines à des centaines de tâches relativement courtes (environ une heure), vous pouvez les grouper dans une ou plusieurs tâches GLOST.
*   Avec plusieurs tâches de longue durée ayant des temps d’exécution similaires, vous pouvez aussi les regrouper dans une tâche GLOST.

### Estimation du temps d’exécution

Avant de lancer une tâche, essayez d’estimer son temps d’exécution; ceci peut servir à estimer le temps d’exécution de la tâche GLOST.
Supposons que votre tâche GLOST comprend un nombre **Njobs** de tâches similaires où chacune utilise un temps **t0** sur un (1) processeur. La durée totale sera alors de **t0*Njobs**.

Pour utiliser maintenant un nombre de cœurs **Ncores**, la durée sera de **wt = t0*Njobs/Ncores**.

!!! note "Remarque"
    Une tâche MPI est souvent conçue pour que les processeurs puissent échanger de l'information entre eux, ce qui utilise souvent une grande part du temps pour communiquer plutôt que pour effectuer les calculs. Un grand nombre de petites communications dépendantes peut diminuer la performance du code, mais GLOST utilise MPI pour lancer des tâches séquentielles uniquement et donc, le surcoût en communication est relativement rare. Vous pouvez arriver au même résultat en utilisant directement MPI, mais GLOST est presque aussi efficace en plus de vous épargner l'écriture de code MPI.

### Besoins en mémoire

GLOST exécute des tâches séquentielles avec MPI et la mémoire par cœur devrait être la même que la mémoire utilisée par les tâches exécutées séparément. Dans le script Slurm, utilisez `--mem-per-cpu` plutôt que `--mem`.

### Créer la liste des tâches

Avant de soumettre une tâche, créez un fichier texte nommé **list_glost_tasks.txt** avec une tâche par ligne et les commandes pour chacune des tâches. Choisir des tâches ayant une durée d’exécution similaire permet d’optimiser les ressources utilisées. Les tâches peuvent être localisées dans un seul ou plusieurs répertoires. Si les tâches sont toutes dans le même répertoire, il faut éviter que les résultats utilisent les mêmes fichiers temporaires ou les mêmes fichiers en sortie; pour ce faire, les résultats peuvent être redirigés vers un fichier avec une variable qui indique l’option ou l’argument utilisé dans l’exécution de la tâche. Dans le cas où les tâches utilisent les mêmes fichiers temporaires ou les mêmes fichiers en sortie, vous aurez peut-être besoin de créer un répertoire pour chaque tâche (un répertoire pour chaque option ou argument correspondant à une tâche particulière).

!!! note "Remarque"
    Une tâche peut contenir une ou plusieurs commandes exécutées l’une à la suite de l’autre. Les commandes doivent être séparées par `&&`.

Le fichier suivant **list_glost_example.txt** contient huit tâches.

=== "Script"
    ```bash
    #!/bin/bash

    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=2
    #SBATCH --time=00-02:00
    #SBATCH --mem-per-cpu=4000M

    # charger le module GLOST

    module load intel/2023.2.1  openmpi/4.1.5 glost/0.3.1

    echo "Début de l'exécution à : `date`"

    # lancer GLOST avec l'argument list_glost_example.txt

    srun glost_launch list_glost_example.txt

    echo "Le programme glost_launch s'est terminé avec le code de sortie $? à : `date`"
    ```

=== "Liste des tâches"
    ```txt
    job01 and/or other commands related to job01 
    job02 and/or other commands related to job02
    job03 and/or other commands related to job03
    job04 and/or other commands related to job04
    job05 and/or other commands related to job05
    job06 and/or other commands related to job06
    job07 and/or other commands related to job07
    job08 and/or other commands related to job08
    ```

!!! note "Remarque"
    Cet exemple de script ne contient pas de commandes et il ne peut pas être exécuté. Il montre seulement
    *   la syntaxe de base pour la liste de tâches **list_glost_tasks.txt** qui servira d’argument pour `glost_launch`;
    *   un script type pour la soumission de tâches.

La liste des tâches et le script doivent être adaptés à votre contexte.

### Liste de tâches situées dans le même répertoire

GLOST peut être utilisé pour exécuter un ensemble ou une liste de tâches séquentielles dans un répertoire. Il faut éviter que les résultats utilisent les mêmes fichiers temporaires ou les mêmes fichiers en sortie en ajoutant des arguments pour différencier les tâches. Le prochain exemple contient 10 tâches dont chacune contient une ou plusieurs commandes qui seront exécutées l’une à la suite de l’autre.

*   La première commande définit `nargument` qui peut être une variable ou un paramètre pouvant par exemple être passé au programme;
*   la deuxième commande exécute le programme; pour les besoins du test, nous utilisons la commande `sleep 360` que vous remplacerez par la ligne de commande pour votre application, par exemple `./my_first_prog < first_input_file.txt > first_output_file.txt`;
*   la troisième commande et les suivantes sont optionnelles; pour les besoins du test, nous utilisons `echo ${nargument}.\`hostname\` > log_${nargument}.txt` qui imprime l’argument et hostname vers le fichier log_${nargument}.txt. Comme c’est le cas pour la deuxième commande, cette ligne sera remplacée selon votre application, par exemple par `./my_second_prog < second_input_file.txt > second_output_file.txt`.

=== "Script"
    ```bash
    #!/bin/bash

    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=2
    #SBATCH --time=00-02:00
    #SBATCH --mem-per-cpu=4000M

    # charger le module GLOST avec les autres modules nécessaires pour lancer votre application

    module load intel/2023.2.1  openmpi/4.1.5 glost/0.3.1

    echo "Début de l'exécution à : `date`"

    # lancer GLOST avec l'argument list_glost_tasks.txt

    srun glost_launch list_glost_tasks.txt

    echo "Le programme glost_launch s'est terminé avec le code de sortie $? à : `date`"
    ```

=== "Liste des tâches"
    ```txt
    nargument=20 && sleep 360 && echo ${nargument}.`hostname` > log_${nargument}.txt
    nargument=21 && sleep 360 && echo ${nargument}.`hostname` > log_${nargument}.txt
    nargument=22 && sleep 360 && echo ${nargument}.`hostname` > log_${nargument}.txt
    nargument=23 && sleep 360 && echo ${nargument}.`hostname` > log_${nargument}.txt
    nargument=24 && sleep 360 && echo ${nargument}.`hostname` > log_${nargument}.txt
    nargument=25 && sleep 360 && echo ${nargument}.`hostname` > log_${nargument}.txt
    nargument=26 && sleep 360 && echo ${nargument}.`hostname` > log_${nargument}.txt
    nargument=27 && sleep 360 && echo ${nargument}.`hostname` > log_${nargument}.txt
    nargument=28 && sleep 360 && echo ${nargument}.`hostname` > log_${nargument}.txt
    nargument=29 && sleep 360 && echo ${nargument}.`hostname` > log_${nargument}.txt
    ```

!!! note "Remarque"
    Dans cet exemple, nous utilisons 2 cœurs et une liste de 10 tâches. Les deux premières tâches (correspondant aux deux premières lignes) seront assignées par GLOST aux processeurs disponibles. Quand le ou les processeurs auront terminé le traitement des deux premières tâches, ils passeront à la tâche suivante et ainsi de suite jusqu’à la fin de la liste.

### Liste de tâches situées dans des répertoires différents

Dans ce cas, plusieurs tâches séquentielles sont exécutées dans des répertoires distincts, ce qui peut être utile pour éviter que les tâches se terminent de façon anormale ou que les résultats se chevauchent quand un programme utilise des fichiers temporaires ou des fichiers d’entrée/sortie avec des noms identiques. Il faut s’assurer que chaque tâche à ses fichiers d’entrée et son répertoire. Il est aussi possible d’utiliser les commandes comme dans l’exemple suivant :

=== "Script"
    ```bash
    #!/bin/bash

    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=3
    #SBATCH --time=00-03:00
    #SBATCH --mem-per-cpu=4000M

    # charger le module GLOST avec les autres modules nécessaires pour lancer votre application

    module load intel/2023.2.1  openmpi/4.1.5 glost/0.3.1

    echo "Début de l'exécution à : `date`"

    # lancer GLOST avec l'argument list_glost_tasks.txt

    srun glost_launch list_glost_tasks.txt

    echo "Le programme glost_launch s'est terminé avec le code de sortie $? à : `date`"
    ```

=== "Liste des tâches"
    ```txt
    nargument=20 && mkdir -p RUN_${nargument} && cd RUN_${nargument} && sleep 360 && echo ${nargument}.`hostname` > log_run.txt
    nargument=21 && mkdir -p RUN_${nargument} && cd RUN_${nargument} && sleep 360 && echo ${nargument}.`hostname` > log_run.txt
    nargument=22 && mkdir -p RUN_${nargument} && cd RUN_${nargument} && sleep 360 && echo ${nargument}.`hostname` > log_run.txt
    nargument=23 && mkdir -p RUN_${nargument} && cd RUN_${nargument} && sleep 360 && echo ${nargument}.`hostname` > log_run.txt
    nargument=24 && mkdir -p RUN_${nargument} && cd RUN_${nargument} && sleep 360 && echo ${nargument}.`hostname` > log_run.txt
    nargument=25 && mkdir -p RUN_${nargument} && cd RUN_${nargument} && sleep 360 && echo ${nargument}.`hostname` > log_run.txt
    nargument=26 && mkdir -p RUN_${nargument} && cd RUN_${nargument} && sleep 360 && echo ${nargument}.`hostname` > log_run.txt
    nargument=27 && mkdir -p RUN_${nargument} && cd RUN_${nargument} && sleep 360 && echo ${nargument}.`hostname` > log_run.txt
    nargument=28 && mkdir -p RUN_${nargument} && cd RUN_${nargument} && sleep 360 && echo ${nargument}.`hostname` > log_run.txt
    nargument=29 && mkdir -p RUN_${nargument} && cd RUN_${nargument} && sleep 360 && echo ${nargument}.`hostname` > log_run.txt
    nargument=30 && mkdir -p RUN_${nargument} && cd RUN_${nargument} && sleep 360 && echo ${nargument}.`hostname` > log_run.txt
    nargument=31 && mkdir -p RUN_${nargument} && cd RUN_${nargument} && sleep 360 && echo ${nargument}.`hostname` > log_run.txt
    ```

### Redémarrer une tâche GLOST

Si vous avez mal évalué la durée d’exécution de votre tâche GLOST, il est possible qu’elle doive être redémarrée pour traiter toutes les tâches. Identifiez d’abord les tâches qui ont été exécutées et supprimez les lignes correspondantes dans la liste ou créez une nouvelle liste avec les tâches non exécutées. Soumettez à nouveau le script avec la nouvelle liste comme argument à `glost_launch`.

### Autres exemples

Si vous avez l'habitude de préparer des scripts, utilisez les exemples qui suivent et modifiez-les selon votre contexte.

Après avoir chargé le module GLOST, copiez les exemples dans votre répertoire avec la commande

```bash
cp -r $EBROOTGLOST/examples Glost_Examples
```

Les exemples copiés seront enregistrés dans le répertoire Glost_Examples.

## Références

*   [META-Farm](meta-farm.md)
*   [GNU Parallel](gnu_parallel.md)
*   [Vecteurs de tâches](vecteurs-de-taches.md)
*   [MPI](../software/mpi.md)
*   [Exécuter des tâches](executer-des-taches.md)