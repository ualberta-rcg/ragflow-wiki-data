---
title: "Running jobs/fr"
tags:
  []

keywords:
  []
---

Cette page présente l'information sur comment soumettre des tâches sur nos grappes; elle s'adresse à ceux et celles qui connaissent les concepts de préparation de scripts et d'ordonnancement des tâches.
Si vous n'avez jamais travaillé sur une grappe partagée de grande taille, nous vous recommandons de lire d'abord [Qu'est-ce qu'un ordonnanceur?](what_is_a_scheduler%3f-fr.md)

L'ordonnancement des tâches se fait à l'aide de  
[Slurm Workload Manager](https://en.wikipedia.org/wiki/Slurm_Workload_Manager).
La [documentation Slurm](https://slurm.schedmd.com/documentation.html) est préparée par SchedMD. Si vous utilisez PBS/Torque, SGE, LSF ou LoadLeveler, ce [tableau de correspondance des commandes](https://slurm.schedmd.com/rosetta.pdf) vous sera utile.

## Soumettre des tâches avec `sbatch`
La commande `sbatch` est utilisée pour soumettre une tâche.
<source lang="bash">
$ sbatch simple_job.sh
Submitted batch job 123456
</source>

Un script simple Slurm ressemble à ceci&nbsp;:

**`simple_job.sh`**
```sh
#!/bin/bash
#SBATCH --time=00:15:00
#SBATCH --account=def-someuser
echo 'Hello, world!'
sleep 30
```

Sur les superordinateurs d'usage général, cette tâche réserve un (1) cœur et 256Mo de mémoire pendant 15 minutes. Sur [Trillium](trillium-fr.md), la tâche réserve le nœud entier avec toute sa mémoire.
Les directives (ou <i>options</i>) comprises dans le script ont le préfixe `#SBATCH` et doivent précéder toutes les commandes exécutables. La [page sbatch](https://slurm.schedmd.com/sbatch.html) décrit toutes les directives disponibles. Pour chaque tâche, notre politique demande de fournir au moins une durée (`--time`) et un nom de compte (`--account`); voyez la section [Comptes et projets](running-jobs-fr#comptes_et_projets.md) ci-après.

Les directives peuvent aussi être des arguments en ligne de commande pour  `sbatch`. Par exemple,
  $ sbatch --time=00:30:00 simple_job.sh  
soumet le script présenté plus haut en limitant la durée à 30 minutes. Les formats de date valides sont minutes, minutesːsecondes, heuresːminutesːsecondes, jours-heures, jours-heuresːminutes, jours-heuresːminutesːsecondes. Sachez que la durée a une incidence importante sur le temps d'attente avant que la tâche soit exécutée. En effet, les tâches de longue durée sont [susceptibles d'être exécutées sur moins de nœuds](job_scheduling_policies-fr.md).

L'exécution d'un script qui soumet plusieurs tâches à de courts intervalles risque d'affecter la disponibilité de l'ordonnanceur Slurm pour les autres utilisateurs et utilisatrices (voir l'information sur le message d'erreur [Batch job submission failed: Socket timed out on send/recv operation](frequently_asked_questions-fr#sbatch:_error:_batch_job_submission_failed:_socket_timed_out_on_send-recv_operation.md)). Utilisez plutôt un [vecteur de tâches](running-jobs-fr#redémarrage_avec_des_vecteurs_de_tâches.md) ou espacez les appels à `sbatch` de une seconde ou plus avec la commande `sleep`.

<span id="Memory"></span>
### Mémoire 

La quantité de mémoire peut être demandée avec `--mem-per-cpu` (mémoire par cœur) ou `--mem` (mémoire par nœud). Avec les grappes d'usage général, 256Mo par cœur sont alloués par défaut. Avec [Trillium](trillium-fr.md), il n'est pas nécessaire de spécifier la quantité de mémoire car seuls les nœuds entiers sont alloués avec toute la mémoire disponible.

Une source commune de confusion est qu'une certaine quantité de la mémoire du nœud n'est pas disponible pour la tâche, étant réservée pour le système d'exploitation, etc.  Chaque type de nœud a donc une quantité maximum à la disposition des tâches; par exemple, les nœuds de 128Go sont configurés de façon à offrir 125Go pour l'exécution des tâches soumises. Si vous demandez plus que cette quantité, votre tâche devra être exécutée avec des nœuds de plus de mémoire qui pourraient être moins nombreux.

Pour compliquer davantage, K, M, G, etc. sont interprétés par Slurm comme étant des [préfixes binaires](https://fr.wikipedia.org/wiki/Pr%C3%A9fixe_binaire); ainsi `--mem=125G` équivaut à `--mem=128000M`. La quantité de mémoire que vous pouvez demander est indiquée dans le tableau <i>Caractéristiques des nœuds</i> pour [Fir](fir-fr#caractéristiques_des_nœuds.md), [Narval](narval#caractéristiques_des_nœuds.md), [Graham](graham-fr#caractéristiques_des_nœuds.md),  [Narval](narval#caractéristiques_des_nœuds.md)
et [Nibi](nibi-fr#caractéristiques_des_nœuds.md).

<span id="Use_squeue_or_sq_to_list_jobs"></span>
## Lister les tâches avec `squeue` ou `sq`

La commande utilisée pour vérifier le statut des tâches Slurm est `squeue`; par défaut, elle fournit l'information sur <b>toutes</b> les tâches. La forme courte `sq` ne listera que vos propres tâches.

<source lang="bash">
$ sq
   JOBID     USER      ACCOUNT      NAME  ST   TIME_LEFT NODES CPUS    GRES MIN_MEM NODELIST (REASON)
  123456   smithj   def-smithj  simple_j   R        0:03     1    1  (null)      4G cdr234  (None)
  123457   smithj   def-smithj  bigger_j  PD  2-00:00:00     1   16  (null)     16G (Priority)
</source>

En sortie, la colonne ST montre l'état de chaque tâche. Les états les plus communs sont PD (<i>pending</i>) pour en attente, et R (<i>running</i>) pour en cours. 

Pour plus d'information sur les résultats fournis par `sq` et `squeue`, et comment modifier les résultats, consultez la [documentation pour squeue](https://slurm.schedmd.com/squeue.html). `sq` est une commande créée pour nos environnements.

<b>N'exécutez pas</b> à plusieurs reprises et à de courts intervalles les commandes `squeue` ou `sq` à partir d'un script ou d'une application. Ceci surcharge Slurm et risque fort de nuire à sa performance ou à son bon fonctionnement. Pour savoir quand une tâche commence et se termine, voyez plutôt [Notifications par courriel](monitoring-jobs-fr#notification_par_courriel.md).

<span id="Where_does_the_output_go?"></span>
## Enregistrer le résultat

Par défaut, le résultat est écrit dans un fichier dont le nom commence par <i>slurm-</i>, suivi de l'ID de la tâche et du suffixe <i>.out</i>, par exemple `slurm-123456.out`. La présence de l'ID dans le nom du fichier s'avère pratique pour le débogage. Le fichier est placé dans le répertoire à partir duquel la tâche a été soumise.

Si vous avez besoin de spécifier un endroit ou un nom différent, utilisez la commande `--output`. 
Le nom du fichier peut contenir certains symboles de remplacement, par exemple l'ID de la tâche, le nom de la tâche ou l'ID du [vecteur de tâches](job-arrays-fr.md). Voyez la [page sbatch](https://slurm.schedmd.com/sbatch.html) pour la liste complète.

Les erreurs paraissent normalement dans le même fichier que le résultat standard en sortie, tout comme si les commandes étaient données interactivement. Pour diriger le canal standard d'erreurs (stderr pour <i>standard error</i>) vers un autre fichier, utilisez `--error`.

<span id="Accounts_and_projects"></span>
## Comptes et projets

Chaque tâche doit être associée à un nom de compte correspondant à un [RAP (pour <i>Resource Allocation Project</i>](frequently_asked_questions_about_the_ccdb-fr#qu.27est-ce_qu.27un_rap.3f.md)). Si vous êtes membre d'un seul compte, l'ordonnanceur associe automatiquement vos tâches à ce compte.

Si vous recevez un des messages suivants en soumettant une tâche, vous avez accès à plus d'un compte.
<pre>
 You are associated with multiple _cpu allocations...
 Please specify one of the following accounts to submit this job:
</pre>

<pre>
 You are associated with multiple _gpu allocations...
 Please specify one of the following accounts to submit this job:
</pre> 

Dans ce cas, utilisez la directive `--account` pour spécifier un des comptes listés dans le message d'erreur, par exemple
 #SBATCH --account=def-user-ab

Pour connaître le nom du compte correspondant à un projet, 
connectez-vous à [CCDB](https://ccdb.alliancecan.ca) 
et cliquez sur <i>Mes projets --> Mes ressources et allocations</i> pour faire afficher la liste des projets dont vous êtes membre. Le deuxième champ (<i>Nom du groupe</i>) 
contient la chaîne de caractères à utiliser avec la directive `--account`. Sachez qu'un projet qui a reçu une allocation de ressources  
peut être associé à une grappe en particulier (ou à un groupe de grappes) et qu'il se peut
qu'il ne puisse être transféré de cette grappe à une autre. 

Dans l'exemple suivant, les tâches soumises par `--account=def-fuenma` seront attribuées à zhf-914-aa.

[750px|frame|left| Comment trouver le nom du groupe pour un projet d'allocation de ressources (RAP)](file:find-group-name-fr.png.md)
<br clear=all> <!-- This is to prevent the next section from filling to the right of the image. -->

Si vous prévoyez utiliser toujours le même compte pour toutes les tâches, vous trouverez utile de définir les variables d'environnement suivantes dans votre fichier `~/.bashrc`&nbsp;: 
 export SLURM_ACCOUNT=def-someuser
 export SBATCH_ACCOUNT=$SLURM_ACCOUNT
 export SALLOC_ACCOUNT=$SLURM_ACCOUNT
Slurm utilisera dans le script la valeur de `SBATCH_ACCOUNT` plutôt que la directive `--account`. Même si vous spécifiez un nom de compte dans le script, <b>la variable d'environnement a priorité</b>. Pour remplacer la variable d'environnement, il faut fournir un nom de compte comme argument en ligne de commande avec `sbatch`.

`SLURM_ACCOUNT` joue le même rôle que `SBATCH_ACCOUNT`, mais pour la commande `srun` plutôt que `sbatch`. Il en est de même pour `SALLOC_ACCOUNT`.

<span id="Examples_of_job_scripts"></span>
## Exemples de scripts 

### Tâches séquentielles
Une tâche séquentielle est une tâche qui ne nécessite qu'un seul cœur. Il s'agit du type de tâche le plus simple dont un exemple se trouve ci-dessus dans la section [Soumettre des tâches avec sbatch](#soumettre_des_tâches_avec_sbatch.md).

=== Lot de tâches  === 
Un lot de tâches (<i>task array</i> ou <i>array job</i>) sert à soumettre un ensemble de tâches à l'aide d'une seule commande. Chacune des tâches du lot se distingue par la variable d'environnement `$SLURM_ARRAY_TASK_ID` comportant une valeur distincte pour chaque instance de la tâche. L'exemple suivant crée 10 tâches avec `$SLURM_ARRAY_TASK_ID` ayant les valeurs de 1 à 10 :

**`array_job.sh`**
```sh
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --time=0-0:5
#SBATCH --array=1-10
./myapplication $SLURM_ARRAY_TASK_ID
```

Voyez d'autres exemples à la page [Vecteurs de tâches](job-arrays-fr.md) et la documentation détaillée [Slurm de SchedMD.com](https://slurm.schedmd.com/job_array.html).

=== Tâche multifil ou tâche OpenMP === 
Le prochain exemple comprend un seul processus et huit cœurs CPU. N'oubliez pas que pour utiliser OpenMP, une application doit avoir été compilée avec les indicateurs (<i>flags</i>) appropriés, soit `gcc -fopenmp ...` ou `icc -openmp ...`.

**`openmp_job.sh`**
```sh
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --time=0-0:5
#SBATCH --cpus-per-task=8
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
./ompHello
```

Pour plus d'information, consultez la page [OpenMP](openmp-fr.md).

<span id="MPI_job"></span>
### Tâche MPI 

Le prochain script lance quatre processus MPI, chacun nécessitant 1024Mo de mémoire. Le temps d'exécution est limité à cinq minutes. 

**`mpi_job.sh`**
```sh
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --ntasks-per-node=4      # number of MPI processes
#SBATCH --nodes=1
#SBATCH --mem-per-cpu=1024M      # memory; default unit is megabytes
#SBATCH --time=0-00:05           # time (DD-HH:MM)
srun ./mpi_program               # mpirun or mpiexec also work
```

Les tâches intensives avec MPI peuvent utiliser plus d'un nœud. Il est aussi possible d'avoir des tâches hybrides qui sont à la fois exécutées en MPI et en fils multiples. Pour plus d'information sur les tâches distribuées en parallèle, consultez [Contrôle de l'ordonnancement avec MPI](advanced_mpi_scheduling-fr.md).

=== Tâche GPU (avec processeur graphique) === 
Pour des informations et des exemples de comment demander les ressources GPU, voir [Ordonnancement Slurm des tâches avec GPU](using-gpus-with-slurm-fr.md).

## Tâches interactives 
Si la soumission de tâches en lots est la façon la plus efficace d'utiliser nos grappes, il est cependant possible de soumettre des tâches interactivement,  ce qui peut s'avérer utile pour&nbsp;:
* l'exploration de données en mode ligne de commande;
* l'utilisation des outils de console interactifs de R et iPython;
* les projets intensifs de développement, de débogage ou de compilation.

Pour démarrer une session interactive sur un nœud de calcul, utilisez [salloc](https://slurm.schedmd.com/salloc.html). Dans l'exemple suivant, nous avons une tâche sur un cœur CPU et 3Go de mémoire, pour une durée d'une heure.
 $ salloc --time=1:0:0 --mem-per-cpu=3G --ntasks=1 --account=def-someuser
 salloc: Granted job allocation 1234567
 $ ...             # do some work
 $ exit            # terminate the allocation
 salloc: Relinquishing job allocation 1234567

Il est aussi possible d'exécuter des applications graphiques en mode interactif sur un nœud de calcul en ajoutant l'indicateur <b>--x11</b> à la commande `salloc`. Pour ce faire, il faut d'abord activer la redirection X11 (<i>Enable X11 forwarding</i>); consultez la page [SSH](ssh-fr.md). Prenez note qu'une tâche interactive d'une durée de moins de trois (3) heures est susceptible d'être lancée peu de temps après sa soumission puisque nous leur avons dédié des nœuds de test. Les tâches de plus de trois (3) heures sont exécutées sur les nœuds réguliers d'une grappe et peuvent être en attente pour plusieurs heures et même plusieurs jours avant d'être lancées à un moment imprévisible et possiblement inopportun.

<span id="Monitoring_jobs"></span>
## Suivi des tâches 

Voir [la page wiki Performance des tâches](monitoring-jobs-fr.md).

<span id="Cancelling_jobs"></span>
## Annuler une tâche 

Pour annuler une tâche, spécifiez son identifiant ainsi

 $ scancel <jobid>

Annulez toutes vos tâches ou uniquement vos tâches qui sont en attente ainsi

 $ scancel -u $USER
 $ scancel -t PENDING -u $USER

<span id="Resubmitting_jobs_for_long-running_computations"></span>
## Resoumettre une tâche pour un calcul de longue durée

Pour les calculs nécessitant une durée plus longue que la limite de temps du système, l'application doit pouvoir gérer des [points de contrôle](points_de_contr%c3%b4le.md)
(<i>checkpointing</i>). Elle doit aussi permettre la sauvegarde de son état intégral dans un fichier de point de contrôle (<i>checkpoint file</i>) et pouvoir redémarrer et poursuivre le calcul à partir du dernier état. 

Plusieurs utilisateurs auront peu d'occasions de redémarrer un calcul, et ceci peut se faire manuellement. Dans certains cas cependant, des redémarrages fréquents sont requis et une certaine forme d'automatisation peut être appliquée. 

Les deux méthodes recommandées sont 
* l'utilisation de vecteurs de tâches (<i>job arrays</i>) Slurm;
* la resoumission à partir de la fin du script.

Consultez l'information sur le [morcellement d'une longue tâche](tutoriel_apprentissage_machine#morcellement_d'une_longue_tâche.md) dans notre [tutoriel en apprentissage machine](tutoriel-apprentissage-machine.md).

<span id="Restarting_using_job_arrays"></span>
### Redémarrage avec des vecteurs de tâches

La syntaxe `--array=1-100%10` permet de soumettre une collection de tâches identiques en n'exécutant qu'une tâche à la fois.
Le script doit faire en sorte que le dernier point de contrôle soit toujours utilisé pour la prochaine tâche. Le nombre de redémarrages est spécifié avec l'argument `--array`.

Dans l'exemple suivant en dynamique moléculaire, la simulation comporte 1 million d'étapes et dépasse la limite de temps imposée pour la grappe. La simulation peut cependant être divisée en 10 tâches de 100,000 étapes séquentielles. 

Redémarrage d'une simulation avec un vecteur de tâches :

**`job_array_restart.sh`**
```sh
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
```

<span id="Resubmission_from_the_job_script"></span>
### Resoumettre à partir d'un script 

Dans le prochain exemple, la tâche exécute la première partie du calcul et enregistre un point de contrôle. 
Lorsque la première partie est terminée, mais avant que le temps d'exécution alloué pour la tâche ne soit échu,
le script vérifie si le calcul est terminé.
Si le calcul n'est pas terminé, le script soumet une copie de lui-même et poursuit le travail.

Resoumission avec un script :
{{File
  |name=job_resubmission.sh
  |lang="sh"
  |contents=
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
}}

<b>Remarque ː</b> Le test servant à déterminer s'il faut soumettre une seconde tâche (`work_should_continue` dans notre exemple) doit être un <i>test positif</i>. Vous pourriez être tenté de vérifier l'existence d'une condition d'arrêt (par exemple, la rencontre d'un critère de convergence) et soumettre une seconde tâche si la condition <i>n'est pas détectée</i>. Cependant, si une erreur inattendue survient, la condition d'arrêt pourrait ne pas être repérée et la séquence de tâche se poursuivrait indéfiniment.

## Automatiser la soumission de tâches 
Comme nous l'avons déjà mentionné, [les lots de tâches](running-jobs-fr#lot_de_tâches.md) peuvent être utilisés pour automatiser la soumission des tâches. Nous offrons quelques autres outils plus avancés pour l'exécution d'un grand nombre de tâches séquentielles, parallèles ou utilisant des GPU. Ces outils appliquent une technique nommée <i>farming</i>, <i>serial farming</i> ou <i>task farming</i> qui se traduit par <i>grappe de serveurs</i> et parfois <i>ferme de serveurs</i> ou <i>ferme de calcul</i>.  En plus d'automatiser le flux du travail, ces outils améliorent l'efficacité du traitement en regroupant plusieurs petites tâches de calcul pour créer moins de tâches, mais qui ont des durées plus longues.

Les outils suivants sont disponibles sur nos grappes&nbsp;:
* [META-Farm](meta-farm-fr.md)
* [GNU Parallel](gnu-parallel-fr.md)
* [GLOST](glost-fr.md)

<span id="Do_not_specify_a_partition"></span>
### Ne pas spécifier de partition 

Avec certains paquets logiciels comme [Masurca](https://github.com/alekseyzimin/masurca), les tâches sont soumises à Slurm de façon automatique et le logiciel s'attend à ce qu'une partition soit spécifiée pour chacune des tâches. Ceci est contraire à nos meilleures pratiques qui veulent que l'ordonnanceur assigne les tâches de lui-même, selon les ressources requises. Si vous utilisez un tel logiciel, vous pouvez le configurer afin qu'il utilise `--partition=default` pour que le script l'interprète comme si aucune partition n'est spécifiée.

<span id="Cluster_particularities"></span>
## Particularités de certaines grappes 

Les politiques d'ordonnancement ne sont pas les mêmes sur toutes nos grappes.

<tabs>
<tab name="Béluga, Fir, Narval, Nibi et Rorqual">
La durée maximale d'une tâche est de 168 heures (7 jours) et le nombre maximum de tâches en exécution ou en attente dans la queue est de 1000 par utilisateur. La durée d'une tâche en production devrait être d'au moins une heure. 
</tab>

<tab name="Trillium">
Voir [Restrictions particulières à Trillium](trillium_quickstart-fr#restrictions_particulières_à_trillium.md).
</tab>
</tabs>

<span id="Troubleshooting"></span>
## Dépannage 

#### Pour éviter les caractères cachés 
Le fait d'utiliser un logiciel de traitement de texte plutôt qu'un éditeur de texte peut causer des problèmes à vos scripts. En travaillant sur la grappe directement, il est préférable d'utiliser un éditeur comme nano, vim ou emacs. Si vous préparez vos scripts hors ligne,
* <b>sous Windows</b> 
** utilisez un éditeur de texte comme Notepad  ou [Notepad++](https://notepad-plus-plus.org/)
** téléversez le script et changez les codes de fin de ligne Windows pour des codes de fin de ligne Linux avec `dos2unix` 
* <b>sous Mac</b>
** dans une fenêtre de terminal, utilisez un éditeur comme nano, vim ou emacs

#### Annulation de tâches dont les conditions de dépendance ne sont pas satisfaites 
Une tâche dépendante soumise avec <code>--dependency=afterok:<jobid></code> attend que la tâche parent soit terminée avant de s'exécuter. Si la tâche parent s'arrête avant sa fin (c'est-à-dire qu'elle produit un code de sortie non nul), la tâche dépendante ne sera jamais exécutée et elle est automatiquement annulée. Pour plus d'information sur la dépendance, voir [sbatch](https://slurm.schedmd.com/sbatch.html#OPT_dependency).

#### Module non chargé par une tâche 
L'erreur suivante peut survenir si une condition n'est pas satisfaite&nbsp;:

 Lmod has detected the following error: These module(s) exist but cannot be
 loaded as requested: "<module-name>/<version>"
    Try: "module spider <module-name>/<version>" to see how to load the module(s).

Par exemple,

<source lang="console">
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
</source>

Pour résoudre ce problème, ajoutez au script la ligne `module load nixpkgs/16.09 intel/2016.4 openmpi/2.1.1` avant de charger quantumespresso/6.1

#### Propagation de variables d’environnement  
Par défaut, une tâche hérite des variables d’environnement de l’interpréteur (<i>shell</i>) duquel elle a été lancée. La commande de [chargement d’un module](utiliser-des-modules.md) modifie et configure les variables d’environnement qui se propagent ensuite aux tâches soumises à partir de l’interpréteur. Une tâche pourrait donc se trouver incapable de charger des modules si toutes les conditions ne sont pas satisfaites. Il est donc recommandé d’ajouter au script la ligne `module purge` avant le chargement des modules dont vous avez besoin pour faire en sorte que les tâches soient soumises de manière uniforme et qu’elles ne soient pas affectées par les modifications faites dans l’interpréteur.

Les problèmes sont quelquefois difficiles à diagnostiquer quand les paramètres de l'environnement sont hérités de l'interpréteur qui soumet la tâche; la directive `--export=none` empêche ce type d'héritage.

<span id="Job_hangs_/_no_output_/_incomplete_output"></span>
#### Tâche gèle / pas de résultats / résultats incomplets 

Il arrive qu'aucun résultat (ou seulement une partie) ne soit enregistré dans le fichier `.out` pour une tâche qui a été soumise, et qu'il semble qu'elle soit arrêtée. Ceci se produit surtout parce que la [mise en mémoire tampon](#résultats_en_mémoire_tampon.md) effectuée par l'ordonnanceur Slurm est agressive, car il regroupe plusieurs lignes de résultat avant de les acheminer vers le fichier, et souvent celui-ci n'est produit que quand la tâche se termine. Pire encore, si une tâche est annulée ou manque de temps, une partie des résultats peut être perdue. Si vous voulez suivre le progrès de la tâche en cours au fur et à mesure de son exécution, vous pouvez le faire avec une [tâche interactive](#tâches_interactives.md). C'est aussi une bonne façon d'observer combien de temps la tâche a besoin.

## État des tâches et priorité
* Consultez [Politique d'ordonnancement des tâches](job-scheduling-policies-fr.md) pour des renseignements sur la politique de priorisation des tâches et connaître les éléments pouvant influer sur l'ordonnancement de vos tâches.
* Si des tâches <b>dans votre groupe de recherche</b> sont en concurrence entre elles, consultez [Gestion des comptes Slurm](managing_slurm_accounts-fr.md).

## Pour plus d'information 
* SchedMD : [documentation Slurm](https://slurm.schedmd.com/documentation.html) et [tutoriels](https://slurm.schedmd.com/tutorials.html) 
** options pour la commande [sbatch](https://slurm.schedmd.com/sbatch.html)
* [correspondance de commandes et directives](https://slurm.schedmd.com/rosetta.pdf) Slurm avec PBS/Torque, LSF, SGE et LoadLeveler
* CÉCI, Belgique : [tutoriel Slurm](http://www.ceci-hpc.be/slurm_tutorial.html)
* Bright Computing : tutoriel concis [Slurm sous Unix](http://www.brightcomputing.com/blog/bid/174099/slurm-101-basic-slurm-usage-for-linux-clusters)

[Categorie:SLURM](categorie:slurm.md)