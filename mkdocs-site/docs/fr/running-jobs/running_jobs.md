---
title: "Running jobs/fr"
slug: "running_jobs"
lang: "fr"

source_wiki_title: "Running jobs/fr"
source_hash: "f57c9ef1af840259cf79ddba99a48768"
last_synced: "2026-09-06T00:43:13.954271+00:00"
last_processed: "2026-09-06T02:54:17.373978+00:00"

tags:
  []

keywords:
  - "script Slurm"
  - "resoumission"
  - "mémoire tampon"
  - "mise en mémoire tampon Slurm"
  - "éditeur de texte"
  - "vim ou emacs"
  - "GPU"
  - "dos2unix"
  - "vecteur de tâches"
  - "dépannage"
  - "--dependency=afterok"
  - "vérification du calcul"
  - "--time"
  - "grappe"
  - "tutoriel Slurm"
  - "ordonnanceur Slurm"
  - "ID de la tâche"
  - "commande sbatch"
  - "tâches de plus de trois heures"
  - "point de contrôle"
  - "Restrictions particulières à Trillium"
  - "préfixes binaires"
  - "job_resubmission.sh"
  - "suivre le progrès"
  - "état des tâches"
  - "soumission de tâches"
  - "job arrays"
  - "Slurm Workload Manager"
  - "Dépannage"
  - "nom du fichier"
  - "commande squeue"
  - "tâches interactives"
  - "Politique d'ordonnancement des tâches"
  - "module load"
  - "ensemble de tâches"
  - "fichier de sortie slurm-*.out"
  - "valeurs de 1 à 10"
  - "directive #SBATCH"
  - "temps d'exécution alloué"
  - "module purge"
  - "nano"
  - "attente plusieurs heures"
  - "symboles de remplacement"
  - "tâche interactive"
  - "SLURM_ACCOUNT"
  - "--partition=default"
  - "documentation Slurm"
  - "$SLURM_ARRAY_TASK_ID"
  - "mémoire"
  - "Gestion des comptes Slurm"
  - "256Mo par cœur"
  - "task farming"
  - "résultats perdus"
  - "lot de tâches"
  - "caractères cachés"
  - "--mem-per-cpu"
  - "resoumission de tâche"
  - "suivi des tâches"
  - "mémoire du nœud"
  - "task array"
  - "OpenMP"
  - "nœuds réguliers"
  - "--error"
  - "commande unique"
  - "scancel"
  - "MPI"
  - "--account"
  - "vecteurs de tâches"
  - "sbatch"
  - "RAP"
  - "Trillium"
  - "commande --output"
  - "--mem"

questions:
  - "Quelle commande doit‑on employer pour soumettre un script de travail sur les grappes et quel est l’exemple d’utilisation présenté ?"
  - "Quelles directives Slurm sont obligatoires dans chaque script et comment peut‑on les fournir via la ligne de commande ?"
  - "Comment définir la mémoire allouée à une tâche et quelles sont les particularités entre les grappes d’usage général et le nœud entier de Trillium ?"
  - "Comment spécifier la quantité de mémoire demandée pour un travail ?"
  - "Quelle est la quantité de mémoire allouée par défaut par cœur sur les grappes d'usage général ?"
  - "Pourquoi n’est‑il pas nécessaire de préciser la mémoire lorsqu’on utilise Trillium ?"
  - "Quelle quantité de mémoire réellement disponible peut‑on demander sur un nœud et comment les préfixes binaires (K, M, G) sont‑ils interprétés par Slurm ?"
  - "Comment utiliser les commandes `squeue` et `sq` pour lister les tâches et quels sont les états les plus courants affichés ?"
  - "Où sont enregistrés les fichiers de sortie des tâches par défaut et comment peut‑on personnaliser le nom ou l’emplacement du fichier de sortie ?"
  - "Comment rediriger le canal d’erreurs standard (stderr) vers un fichier distinct lors de la soumission d’une tâche avec sbatch ?"
  - "Que faire lorsqu’on reçoit le message indiquant plusieurs allocations _cpu ou _gpu et comment identifier le nom exact du compte à spécifier avec l’option --account ?"
  - "Quel est l’effet des variables d’environnement SLURM_ACCOUNT, SBATCH_ACCOUNT et SALLOC_ACCOUNT sur la sélection du compte, et comment ces variables interagissent avec l’option --account dans les scripts sbatch et srun ?"
  - "Que permet la commande `--output` lors de la soumission d’une tâche ?"
  - "Quels symboles de remplacement peuvent être inclus dans le nom du fichier de sortie (par ex. ID de tâche, nom de tâche, ID du vecteur de tâches) ?"
  - "Où consulter la liste complète des options de nommage disponibles pour le fichier de sortie ?"
  - "Quel est le rôle d’un « lot de tâches » (task array) dans la soumission de travaux avec SLURM ?"
  - "Comment la variable d’environnement $SLURM_ARRAY_TASK_ID permet‑elle d’identifier chaque tâche du lot ?"
  - "Quelle commande ou quel script permet de créer un lot de 10 tâches avec des identifiants de 1 à 10 ?"
  - "Comment créer et soumettre un job array sous Slurm, et où trouver des exemples supplémentaires ?"
  - "Quelles options de script Slurm sont nécessaires pour configurer respectivement une tâche OpenMP, une tâche MPI et une tâche GPU ?"
  - "Comment démarrer une session interactive avec `salloc`, quelles ressources spécifier, et quelles sont les contraintes de durée pour ces tâches ?"
  - "Pourquoi les tâches de plus de trois heures sont‑elles exécutées sur les nœuds réguliers d’une grappe plutôt que sur des nœuds de test dédiés ?"
  - "Quels sont les impacts d’un délai d’attente imprévisible, pouvant durer plusieurs heures ou jours, sur le lancement de ces tâches longues ?"
  - "Où peut‑on consulter les informations de suivi et de performance des tâches mentionnées dans le texte ?"
  - "Comment annuler une tâche précise ou toutes les tâches en attente d’un utilisateur avec la commande `scancel` ?"
  - "Quelles sont les deux méthodes recommandées pour gérer les calculs de longue durée dépassant la limite de temps, et comment les vecteurs de tâches (`job arrays`) permettent‑ils de redémarrer à partir du dernier point de contrôle ?"
  - "Comment le script de resoumission automatique détecte‑t‑il que le calcul n’est pas terminé et soumet‑il une nouvelle tâche en reprenant depuis le fichier de point de contrôle ?"
  - "Quel est le rôle du test positif `work_should_continue` dans le script et pourquoi est‑il recommandé de l’utiliser plutôt qu’un test de condition d’arrêt ?"
  - "Quels outils (META‑Farm, GNU Parallel, GLOST) sont proposés pour automatiser la soumission de nombreuses tâches séquentielles ou parallèles, et quels bénéfices apportent-ils ?"
  - "Quelles sont les bonnes pratiques concernant la spécification d’une partition et les limites de durée maximale des tâches sur les différentes grappes (Béluga, Fir, Narval, Nibi, Rorqual, Trillium) ?"
  - "Comment le script vérifie‑t‑il si le calcul est terminé avant l’expiration du temps d’exécution alloué ?"
  - "Quelle action le script entreprend‑il lorsqu’il constate que le calcul n’est pas terminé ?"
  - "Quel est le rôle du fichier « job_resubmission.sh » présenté dans le texte ?"
  - "Quels problèmes les caractères cachés peuvent-ils causer dans les scripts lorsqu’on utilise un logiciel de traitement de texte au lieu d’un éditeur de texte ?"
  - "Pourquoi est‑il recommandé d’éditer directement sur la grappe avec des éditeurs comme nano, vim ou emacs ?"
  - "Où peut‑on consulter les « Restrictions particulières à Trillium » mentionnées dans le texte ?"
  - "Que se passe-t-il lorsqu’une tâche soumise avec l’option --dependency=afterok:<jobid> a pour tâche parent un code de sortie non nul, et comment éviter son annulation ?"
  - "Comment corriger l’erreur « These module(s) exist but cannot be loaded as requested » (ex. quantumespresso/6.1) dans un script Slurm ?"
  - "Pourquoi les fichiers .out peuvent rester vides ou incomplets et quelle méthode permet de suivre l’avancement d’une tâche en temps réel ?"
  - "Comment consulter la politique d'ordonnancement des tâches et quels critères influencent la priorité des jobs ?"
  - "Que faire lorsqu’il y a concurrence entre les tâches d’un même groupe de recherche ?"
  - "Où puis‑je accéder à la documentation officielle, aux tutoriels et aux ressources complémentaires sur Slurm ?"
  - "Pourquoi le tampon de sortie de Slurm peut-il entraîner la perte de résultats lorsqu’une tâche est annulée ou dépasse le temps imparti ?"
  - "Comment une tâche interactive permet‑elle de suivre le progrès d’une tâche en cours d’exécution sous Slurm ?"
  - "Quels sont les inconvénients de la mise en mémoire tampon agressive effectuée par l’ordonnanceur Slurm ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Cette page présente l'information sur comment soumettre des tâches sur nos grappes; elle s'adresse à ceux et celles qui connaissent les concepts de préparation de scripts et d'ordonnancement des tâches. Si vous n'avez jamais travaillé sur une grappe partagée de grande taille, nous vous recommandons de lire d'abord [Qu'est-ce qu'un ordonnanceur?](what_is_a_scheduler.md)

!!! warning "Toutes les tâches doivent être soumises via l'ordonnanceur."
    Les seules exceptions sont pour les tâches de compilation et autres tâches qui devraient utiliser moins de 10 minutes de temps CPU et moins de 4Go de mémoire vive. Ces tâches peuvent être exécutées sur un nœud de connexion. Aucun processus ne doit être exécuté sur un nœud de calcul sans d’abord avoir été traité par l’ordonnanceur.

L'ordonnancement des tâches se fait à l'aide de [Slurm Workload Manager](https://en.wikipedia.org/wiki/Slurm_Workload_Manager). La [documentation Slurm](https://slurm.schedmd.com/documentation.html) est préparée par SchedMD. Si vous utilisez PBS/Torque, SGE, LSF ou LoadLeveler, ce [tableau de correspondance des commandes](https://slurm.schedmd.com/rosetta.pdf) vous sera utile.

## Soumettre des tâches avec `sbatch`
La commande `sbatch` est utilisée pour soumettre une tâche.
````bash
$ sbatch simple_job.sh
Submitted batch job 123456
````

Un script simple Slurm ressemble à ceci :
````sh title="simple_job.sh"
#!/bin/bash
#SBATCH --time=00:15:00
#SBATCH --account=def-someuser
echo 'Hello, world!'
sleep 30  
````

Sur les superordinateurs d'usage général, cette tâche réserve un (1) cœur et 256Mo de mémoire pendant 15 minutes. Sur [Trillium](../clusters/trillium.md), la tâche réserve le nœud entier avec toute sa mémoire.
Les directives (ou *options*) comprises dans le script ont le préfixe `#SBATCH` et doivent précéder toutes les commandes exécutables. La [page sbatch](https://slurm.schedmd.com/sbatch.html) décrit toutes les directives disponibles. Pour chaque tâche, notre politique demande de fournir au moins une durée (`--time`) et un nom de compte (`--account`); voyez la section [Comptes et projets](#comptes-et-projets) ci-après.

Les directives peuvent aussi être des arguments en ligne de commande pour `sbatch`. Par exemple,
`sbatch --time=00:30:00 simple_job.sh`
soumet le script présenté plus haut en limitant la durée à 30 minutes. Les formats de date valides sont minutes, minutes :secondes, heures :minutes :secondes, jours-heures, jours-heures :minutes, jours-heures :minutes :secondes. Sachez que la durée a une incidence importante sur le temps d'attente avant que la tâche soit exécutée. En effet, les tâches de longue durée sont [susceptibles d'être exécutées sur moins de nœuds](job_scheduling_policies.md).

L'exécution d'un script qui soumet plusieurs tâches à de courts intervalles risque d'affecter la disponibilité de l'ordonnanceur Slurm pour les autres utilisateurs et utilisatrices (voir l'information sur le message d'erreur [Batch job submission failed: Socket timed out on send/recv operation](../getting-started/frequently_asked_questions.md)). Utilisez plutôt un [vecteur de tâches](#redemarrage-avec-des-vecteurs-de-taches) ou espacez les appels à `sbatch` de une seconde ou plus avec la commande `sleep`.

### Mémoire {#memoire}

La quantité de mémoire peut être demandée avec `--mem-per-cpu` (mémoire par cœur) ou `--mem` (mémoire par nœud). Avec les grappes d'usage général, 256Mo par cœur sont alloués par défaut. Avec [Trillium](../clusters/trillium.md), il n'est pas nécessaire de spécifier la quantité de mémoire car seuls les nœuds entiers sont alloués avec toute la mémoire disponible.

Une source commune de confusion est qu'une certaine quantité de la mémoire du nœud n'est pas disponible pour la tâche, étant réservée pour le système d'exploitation, etc. Chaque type de nœud a donc une quantité maximum à la disposition des tâches; par exemple, les nœuds de 128Go sont configurés de façon à offrir 125Go pour l'exécution des tâches soumises. Si vous demandez plus que cette quantité, votre tâche devra être exécutée avec des nœuds de plus de mémoire qui pourraient être moins nombreux.

Pour compliquer davantage, K, M, G, etc. sont interprétés par Slurm comme étant des [préfixes binaires](https://fr.wikipedia.org/wiki/Pr%C3%A9fixe_binaire); ainsi `--mem=125G` équivaut à `--mem=128000M`. La quantité de mémoire que vous pouvez demander est indiquée dans le tableau *Caractéristiques des nœuds* pour [Fir](../software/fir.md), [Narval](../clusters/narval.md), [Graham](../clusters/graham.md), [Narval](../clusters/narval.md) et [Nibi](../clusters/nibi.md).

## Lister les tâches avec `squeue` ou `sq` {#lister-les-taches-avec-squeue-ou-sq}

La commande utilisée pour vérifier le statut des tâches Slurm est `squeue`; par défaut, elle fournit l'information sur **toutes** les tâches. La forme courte `sq` ne listera que vos propres tâches.

````bash
$ sq
   JOBID     USER      ACCOUNT      NAME  ST   TIME_LEFT NODES CPUS    GRES MIN_MEM NODELIST (REASON)
  123456   smithj   def-smithj  simple_j   R        0:03     1    1  (null)      4G cdr234  (None)
  123457   smithj   def-smithj  bigger_j  PD  2-00:00:00     1   16  (null)     16G (Priority)
````

En sortie, la colonne ST montre l'état de chaque tâche. Les états les plus communs sont PD (*pending*) pour en attente, et R (*running*) pour en cours. 

Pour plus d'information sur les résultats fournis par `sq` et `squeue`, et comment modifier les résultats, consultez la [documentation pour squeue](https://slurm.schedmd.com/squeue.html). `sq` est une commande créée pour nos environnements.

!!! warning
    **N'exécutez pas** à plusieurs reprises et à de courts intervalles les commandes `squeue` ou `sq` à partir d'un script ou d'une application. Ceci surcharge Slurm et risque fort de nuire à sa performance ou à son bon fonctionnement. Pour savoir quand une tâche commence et se termine, voyez plutôt [Notifications par courriel](monitoring_jobs.md#notification-par-courriel).

## Enregistrer le résultat {#enregistrer-le-resultat}

Par défaut, le résultat est écrit dans un fichier dont le nom commence par *slurm-*, suivi de l'ID de la tâche et du suffixe *.out*, par exemple `slurm-123456.out`. La présence de l'ID dans le nom du fichier s'avère pratique pour le débogage. Le fichier est placé dans le répertoire à partir duquel la tâche a été soumise.

Si vous avez besoin de spécifier un endroit ou un nom différent, utilisez la commande `--output`. 
Le nom du fichier peut contenir certains symboles de remplacement, par exemple l'ID de la tâche, le nom de la tâche ou l'ID du [vecteur de tâches](job_arrays.md). Voyez la [page sbatch](https://slurm.schedmd.com/sbatch.html) pour la liste complète.

Les erreurs paraissent normalement dans le même fichier que le résultat standard en sortie, tout comme si les commandes étaient données interactivement. Pour diriger le canal standard d'erreurs (stderr pour *standard error*) vers un autre fichier, utilisez `--error`.

## Comptes et projets {#comptes-et-projets}

Chaque tâche doit être associée à un nom de compte correspondant à un [RAP (pour *Resource Allocation Project*)](../getting-started/frequently_asked_questions_about_the_ccdb.md#quest-ce-quun-rap). Si vous êtes membre d'un seul compte, l'ordonnanceur associe automatiquement vos tâches à ce compte.

Si vous recevez un des messages suivants en soumettant une tâche, vous avez accès à plus d'un compte.
````
 You are associated with multiple _cpu allocations...
 Please specify one of the following accounts to submit this job:
````

````
 You are associated with multiple _gpu allocations...
 Please specify one of the following accounts to submit this job:
```` 

Dans ce cas, utilisez la directive `--account` pour spécifier un des comptes listés dans le message d'erreur, par exemple
````bash
#SBATCH --account=def-user-ab
````

Pour connaître le nom du compte correspondant à un projet, 
connectez-vous à [CCDB](https://ccdb.alliancecan.ca) 
et cliquez sur *Mes projets --> Mes ressources et allocations* pour faire afficher la liste des projets dont vous êtes membre. Le deuxième champ (*Nom du groupe*) 
contient la chaîne de caractères à utiliser avec la directive `--account`. Sachez qu'un projet qui a reçu une allocation de ressources  
peut être associé à une grappe en particulier (ou à un groupe de grappes) et qu'il se peut
qu'il ne puisse être transféré de cette grappe à une autre. 

Dans l'exemple suivant, les tâches soumises par `--account=def-fuenma` seront attribuées à zhf-914-aa.

Si vous prévoyez utiliser toujours le même compte pour toutes les tâches, vous trouverez utile de définir les variables d'environnement suivantes dans votre fichier `~/.bashrc` : 
````bash
export SLURM_ACCOUNT=def-someuser
export SBATCH_ACCOUNT=$SLURM_ACCOUNT
export SALLOC_ACCOUNT=$SLURM_ACCOUNT
````
Slurm utilisera dans le script la valeur de `SBATCH_ACCOUNT` plutôt que la directive `--account`. Même si vous spécifiez un nom de compte dans le script, **la variable d'environnement a priorité**. Pour remplacer la variable d'environnement, il faut fournir un nom de compte comme argument en ligne de commande avec `sbatch`.

`SLURM_ACCOUNT` joue le même rôle que `SBATCH_ACCOUNT`, mais pour la commande `srun` plutôt que `sbatch`. Il en est de même pour `SALLOC_ACCOUNT`.

## Exemples de scripts {#exemples-de-scripts}

### Tâches séquentielles
Une tâche séquentielle est une tâche qui ne nécessite qu'un seul cœur. Il s'agit du type de tâche le plus simple dont un exemple se trouve ci-dessus dans la section [Soumettre des tâches avec `sbatch`](#soumettre-des-taches-avec-sbatch).

### Lot de tâches
Un lot de tâches (*task array* ou *array job*) sert à soumettre un ensemble de tâches à l'aide d'une seule commande. Chacune des tâches du lot se distingue par la variable d'environnement `$SLURM_ARRAY_TASK_ID` comportant une valeur distincte pour chaque instance de la tâche. L'exemple suivant crée 10 tâches avec `$SLURM_ARRAY_TASK_ID` ayant les valeurs de 1 à 10 :

````sh title="array_job.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --time=0-0:5
#SBATCH --array=1-10
./myapplication $SLURM_ARRAY_TASK_ID
````

Voyez d'autres exemples à la page [Vecteurs de tâches](job_arrays.md) et la documentation détaillée [Slurm de SchedMD.com](https://slurm.schedmd.com/job_array.html).

### Tâche multifil ou tâche OpenMP
Le prochain exemple comprend un seul processus et huit cœurs CPU. N'oubliez pas que pour utiliser OpenMP, une application doit avoir été compilée avec les indicateurs (*flags*) appropriés, soit `gcc -fopenmp ...` ou `icc -openmp ...`.

````sh title="openmp_job.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --time=0-0:5
#SBATCH --cpus-per-task=8
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
./ompHello
````

Pour plus d'information, consultez la page [OpenMP](../programming/openmp.md).

### Tâche MPI {#mpi-job}

Le prochain script lance quatre processus MPI, chacun nécessitant 1024Mo de mémoire. Le temps d'exécution est limité à cinq minutes. 

````sh title="mpi_job.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --ntasks-per-node=4      # number of MPI processes
#SBATCH --nodes=1
#SBATCH --mem-per-cpu=1024M      # memory; default unit is megabytes
#SBATCH --time=0-00:05           # time (DD-HH:MM)
srun ./mpi_program               # mpirun or mpiexec also work
````

Les tâches intensives avec MPI peuvent utiliser plus d'un nœud. Il est aussi possible d'avoir des tâches hybrides qui sont à la fois exécutées en MPI et en fils multiples. Pour plus d'information sur les tâches distribuées en parallèle, consultez [Contrôle de l'ordonnancement avec MPI](advanced_mpi_scheduling.md).

### Tâche GPU (avec processeur graphique)
Pour des informations et des exemples de comment demander les ressources GPU, voir [Ordonnancement Slurm des tâches avec GPU](using_gpus_with_slurm.md).

## Tâches interactives {#taches-interactives}
Si la soumission de tâches en lots est la façon la plus efficace d'utiliser nos grappes, il est cependant possible de soumettre des tâches interactivement, ce qui peut s'avérer utile pour :
* l'exploration de données en mode ligne de commande;
* l'utilisation des outils de console interactifs de R et iPython;
* les projets intensifs de développement, de débogage ou de compilation.

Pour démarrer une session interactive sur un nœud de calcul, utilisez [salloc](https://slurm.schedmd.com/salloc.html). Dans l'exemple suivant, nous avons une tâche sur un cœur CPU et 3Go de mémoire, pour une durée d'une heure.
````bash
$ salloc --time=1:0:0 --mem-per-cpu=3G --ntasks=1 --account=def-someuser
salloc: Granted job allocation 1234567
$ ...             # do some work
$ exit            # terminate the allocation
salloc: Relinquishing job allocation 1234567
````

Il est aussi possible d'exécuter des applications graphiques en mode interactif sur un nœud de calcul en ajoutant l'indicateur **--x11** à la commande `salloc`. Pour ce faire, il faut d'abord activer la redirection X11 (*Enable X11 forwarding*); consultez la page [SSH](../getting-started/ssh.md). Prenez note qu'une tâche interactive d'une durée de moins de trois (3) heures est susceptible d'être lancée peu de temps après sa soumission puisque nous leur avons dédié des nœuds de test. Les tâches de plus de trois (3) heures sont exécutées sur les nœuds réguliers d'une grappe et peuvent être en attente pour plusieurs heures et même plusieurs jours avant d'être lancées à un moment imprévisible et possiblement inopportun.

## Suivi des tâches {#suivi-des-taches}

Voir [la page Performance des tâches](monitoring_jobs.md).

## Annuler une tâche {#annuler-une-tache}

Pour annuler une tâche, spécifiez son identifiant ainsi

````bash
$ scancel <jobid>
````

Annulez toutes vos tâches ou uniquement vos tâches qui sont en attente ainsi

````bash
$ scancel -u $USER
$ scancel -t PENDING -u $USER
````

## Resoumettre une tâche pour un calcul de longue durée {#resoumettre-une-tache-pour-un-calcul-de-longue-duree}

Pour les calculs nécessitant une durée plus longue que la limite de temps du système, l'application doit pouvoir gérer des [points de contrôle](points_de_contrôle.md) (*checkpointing*). Elle doit aussi permettre la sauvegarde de son état intégral dans un fichier de point de contrôle (*checkpoint file*) et pouvoir redémarrer et poursuivre le calcul à partir du dernier état. 

Plusieurs utilisateurs auront peu d'occasions de redémarrer un calcul, et ceci peut se faire manuellement. Dans certains cas cependant, des redémarrages fréquents sont requis et une certaine forme d'automatisation peut être appliquée. 

Les deux méthodes recommandées sont 
* l'utilisation de vecteurs de tâches (*job arrays*) Slurm;
* la resoumission à partir de la fin du script.

Consultez l'information sur le [morcellement d'une longue tâche](../software/ai-ml/tutoriel_apprentissage_machine.md) dans notre [tutoriel en apprentissage machine](../software/ai-ml/tutoriel_apprentissage_machine.md).

### Redémarrage avec des vecteurs de tâches {#redemarrage-avec-des-vecteurs-de-taches}

La syntaxe `--array=1-100%10` permet de soumettre une collection de tâches identiques en n'exécutant qu'une tâche à la fois.
Le script doit faire en sorte que le dernier point de contrôle soit toujours utilisé pour la prochaine tâche. Le nombre de redémarrages est spécifié avec l'argument `--array`.

Dans l'exemple suivant en dynamique moléculaire, la simulation comporte 1 million d'étapes et dépasse la limite de temps imposée pour la grappe. La simulation peut cependant être divisée en 10 tâches de 100,000 étapes séquentielles. 

Redémarrage d'une simulation avec un vecteur de tâches :
````sh title="job_array_restart.sh"
#!/bin/bash
# ---------------------------------------------------------------------
# script Slurm pour une tâche de plusieurs étapes 
# ---------------------------------------------------------------------
#SBATCH --account=def-someuser
#SBATCH --cpus-per-task=1
#SBATCH --time=0-10:00
#SBATCH --mem=100M
#SBATCH --array=1-10%1   # exécuter un vecteur de 10 tâches, une à la fois
# ---------------------------------------------------------------------
echo "Current working directory: `pwd`"
echo "Starting run at: `date`"
# ---------------------------------------------------------------------
echo ""
echo "Job Array ID / Job ID: $SLURM_ARRAY_JOB_ID / $SLURM_JOB_ID"
echo "This is job $SLURM_ARRAY_TASK_ID out of $SLURM_ARRAY_TASK_COUNT jobs."
echo ""
# ---------------------------------------------------------------------
# exécuter l'étape de simulation ici...


if test -e state.cpt; then 
     # il y a un point de contrôle, redémarrer
     mdrun --restart state.cpt
else
     # il n'y a pas de point de contrôle, commencer une nouvelle simulation
     mdrun
fi

# ---------------------------------------------------------------------
echo "Job finished with exit code $? at: `date`"
# ---------------------------------------------------------------------
````

### Resoumettre à partir d'un script {#resoumettre-a-partir-dun-script}

Dans le prochain exemple, la tâche exécute la première partie du calcul et enregistre un point de contrôle. 
Lorsque la première partie est terminée, mais avant que le temps d'exécution alloué pour la tâche ne soit échu,
le script vérifie si le calcul est terminé.
Si le calcul n'est pas terminé, le script soumet une copie de lui-même et poursuit le travail.

Resoumission avec un script :
````sh title="job_resubmission.sh"
#!/bin/bash
# ---------------------------------------------------------------------
# script Slurm pour resoumettre une tâche 
# ---------------------------------------------------------------------
#SBATCH --job-name=job_chain
#SBATCH --account=def-someuser
#SBATCH --cpus-per-task=1
#SBATCH --time=0-10:00
#SBATCH --mem=100M
# ---------------------------------------------------------------------
echo "Current working directory: `pwd`"
echo "Starting run at: `date`"
# ---------------------------------------------------------------------
# exécuter l'étape de simulation ici...

if test -e state.cpt; then 
     # il y a un point de contrôle, redémarrer
     mdrun --restart state.cpt
else
     # il n'y a pas de point de contrôle, commencer une nouvelle simulation
     mdrun
fi


# resoumettre si le travail n'est pas encore terminé
# définir la fonction work_should_continue()
if work_should_continue; then
     sbatch ${BASH_SOURCE[0]}
fi

# ---------------------------------------------------------------------
echo "Job finished with exit code $? at: `date`"
# ---------------------------------------------------------------------
````

!!! warning "Remarque"
    Le test servant à déterminer s'il faut soumettre une seconde tâche (`work_should_continue` dans notre exemple) doit être un *test positif*. Vous pourriez être tenté de vérifier l'existence d'une condition d'arrêt (par exemple, la rencontre d'un critère de convergence) et soumettre une seconde tâche si la condition *n'est pas détectée*. Cependant, si une erreur inattendue survient, la condition d'arrêt pourrait ne pas être repérée et la séquence de tâche se poursuivrait indéfiniment.

## Automatiser la soumission de tâches
Comme nous l'avons déjà mentionné, [les lots de tâches](#lot-de-taches) peuvent être utilisés pour automatiser la soumission des tâches. Nous offrons quelques autres outils plus avancés pour l'exécution d'un grand nombre de tâches séquentielles, parallèles ou utilisant des GPU. Ces outils appliquent une technique nommée *farming*, *serial farming* ou *task farming* qui se traduit par *grappe de serveurs* et parfois *ferme de serveurs* ou *ferme de calcul*. En plus d'automatiser le flux du travail, ces outils améliorent l'efficacité du traitement en regroupant plusieurs petites tâches de calcul pour créer moins de tâches, mais qui ont des durées plus longues.

Les outils suivants sont disponibles sur nos grappes :
* [META-Farm](meta-farm.md)
* [GNU Parallel](gnu_parallel.md)
* [GLOST](glost.md)

### Ne pas spécifier de partition {#ne-pas-specifier-de-partition}

Avec certains paquets logiciels comme [Masurca](https://github.com/alekseyzimin/masurca), les tâches sont soumises à Slurm de façon automatique et le logiciel s'attend à ce qu'une partition soit spécifiée pour chacune des tâches. Ceci est contraire à nos meilleures pratiques qui veulent que l'ordonnanceur assigne les tâches de lui-même, selon les ressources requises. Si vous utilisez un tel logiciel, vous pouvez le configurer afin qu'il utilise `--partition=default` pour que le script l'interprète comme si aucune partition n'est spécifiée.

## Particularités de certaines grappes {#particularites-de-certaines-grappes}

Les politiques d'ordonnancement ne sont pas les mêmes sur toutes nos grappes.

````tabs
=== "Béluga, Fir, Narval, Nibi et Rorqual"

La durée maximale d'une tâche est de 168 heures (7 jours) et le nombre maximum de tâches en exécution ou en attente dans la queue est de 1000 par utilisateur. La durée d'une tâche en production devrait être d'au moins une heure. 

=== "Trillium"

Voir [Restrictions particulières à Trillium](../clusters/trillium_quickstart.md).
````

## Dépannage {#depannage}

### Pour éviter les caractères cachés
Le fait d'utiliser un logiciel de traitement de texte plutôt qu'un éditeur de texte peut causer des problèmes à vos scripts. En travaillant sur la grappe directement, il est préférable d'utiliser un éditeur comme nano, vim ou emacs. Si vous préparez vos scripts hors ligne,
* **sous Windows** 
  * utilisez un éditeur de texte comme Notepad ou [Notepad++](https://notepad-plus-plus.org/)
  * téléversez le script et changez les codes de fin de ligne Windows pour des codes de fin de ligne Linux avec `dos2unix` 
* **sous Mac**
  * dans une fenêtre de terminal, utilisez un éditeur comme nano, vim ou emacs

### Annulation de tâches dont les conditions de dépendance ne sont pas satisfaites
Une tâche dépendante soumise avec `--dependency=afterok:<jobid>` attend que la tâche parent soit terminée avant de s'exécuter. Si la tâche parent s'arrête avant sa fin (c'est-à-dire qu'elle produit un code de sortie non nul), la tâche dépendante ne sera jamais exécutée et elle est automatiquement annulée. Pour plus d'information sur la dépendance, voir [sbatch](https://slurm.schedmd.com/sbatch.html#OPT_dependency).

### Module non chargé par une tâche
L'erreur suivante peut survenir si une condition n'est pas satisfaite :

````
Lmod has detected the following error: These module(s) exist but cannot be
loaded as requested: "<module-name>/<version>"
   Try: "module spider <module-name>/<version>" to see how to load the module(s).
````

Par exemple,

````console
$ module load gcc
$ module load quantumespresso/6.1
Lmod has detected the following error:  These module(s) exist but cannot be loaded as requested: "quantumespresso/6.1"
   Try: "module spider quantumespresso/6.1" to see how to load the module(s).
$ module spider quantumespresso/6.1

-----------------------------------------
  quantumespresso: quantumespresso/6.1
------------------------------------------
    Description:
      Quantum ESPRESSO is an integrated suite of computer codes for electronic-structure calculations and materials modeling at the nanoscale. It is based on density-functional theory, plane waves, and pseudopotentials (both
      norm-conserving and ultrasoft).

    Properties:
      Chemistry libraries/apps / Logiciels de chimie

    You will need to load all module(s) on any one of the lines below before the "quantumespresso/6.1" module is available to load.

      nixpkgs/16.09  intel/2016.4  openmpi/2.1.1

    Help:

      Description
      ===========
      Quantum ESPRESSO  is an integrated suite of computer codes
       for electronic-structure calculations and materials modeling at the nanoscale.
       It is based on density-functional theory, plane waves, and pseudopotentials
        (both norm-conserving and ultrasoft).


      More information
      ================
       - Homepage: http://www.pwscf.org/
````

Pour résoudre ce problème, ajoutez au script la ligne `module load nixpkgs/16.09 intel/2016.4 openmpi/2.1.1` avant de charger quantumespresso/6.1.

### Propagation de variables d’environnement
Par défaut, une tâche hérite des variables d’environnement de l’interpréteur (*shell*) duquel elle a été lancée. La commande de [chargement d’un module](../programming/utiliser_des_modules.md) modifie et configure les variables d’environnement qui se propagent ensuite aux tâches soumises à partir de l’interpréteur. Une tâche pourrait donc se trouver incapable de charger des modules si toutes les conditions ne sont pas satisfaites. Il est donc recommandé d’ajouter au script la ligne `module purge` avant le chargement des modules dont vous avez besoin pour faire en sorte que les tâches soient soumises de manière uniforme et qu’elles ne soient pas affectées par les modifications faites dans l’interpréteur.

Les problèmes sont quelquefois difficiles à diagnostiquer quand les paramètres de l'environnement sont hérités de l'interpréteur qui soumet la tâche; la directive `--export=none` empêche ce type d'héritage.

### Tâche gèle / pas de résultats / résultats incomplets {#resultats-en-memoire-tampon}

Il arrive qu'aucun résultat (ou seulement une partie) ne soit enregistré dans le fichier `.out` pour une tâche qui a été soumise, et qu'il semble qu'elle soit arrêtée. Ceci se produit surtout parce que la [mise en mémoire tampon](#resultats-en-memoire-tampon) effectuée par l'ordonnanceur Slurm est agressive, car il regroupe plusieurs lignes de résultat avant de les acheminer vers le fichier, et souvent celui-ci n'est produit que quand la tâche se termine. Pire encore, si une tâche est annulée ou manque de temps, une partie des résultats peut être perdue. Si vous voulez suivre le progrès de la tâche en cours au fur et à mesure de son exécution, vous pouvez le faire avec une [tâche interactive](#taches-interactives). C'est aussi une bonne façon d'observer combien de temps la tâche a besoin.

## État des tâches et priorité
* Consultez [Politique d'ordonnancement des tâches](job_scheduling_policies.md) pour des renseignements sur la politique de priorisation des tâches et connaître les éléments pouvant influer sur l'ordonnancement de vos tâches.
* Si des tâches **dans votre groupe de recherche** sont en concurrence entre elles, consultez [Gestion des comptes Slurm](managing_slurm_accounts.md).

## Pour plus d'information
* SchedMD : [documentation Slurm](https://slurm.schedmd.com/documentation.html) et [tutoriels](https://slurm.schedmd.com/tutorials.html) 
  * options pour la commande [sbatch](https://slurm.schedmd.com/sbatch.html)
* [correspondance de commandes et directives](https://slurm.schedmd.com/rosetta.pdf) Slurm avec PBS/Torque, LSF, SGE et LoadLeveler
* CÉCI, Belgique : [tutoriel Slurm](http://www.ceci-hpc.be/slurm_tutorial.html)
* Bright Computing : tutoriel concis [Slurm sous Unix](http://www.brightcomputing.com/blog/bid/174099/slurm-101-basic-slurm-usage-for-linux-clusters)