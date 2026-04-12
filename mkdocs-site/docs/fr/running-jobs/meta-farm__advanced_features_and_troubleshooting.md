---
title: "META-Farm: Advanced features and troubleshooting/fr"
slug: "meta-farm__advanced_features_and_troubleshooting"
lang: "fr"

source_wiki_title: "META-Farm: Advanced features and troubleshooting/fr"
source_hash: "6b0a07c3d5c5bbcd0c94ce6ad90ca849"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:43:44.670553+00:00"

tags:
  []

keywords:
  - "application name"
  - "Slurm jobs"
  - "time estimate"
  - "dt_cutoff"
  - "failed/unfinished jobs"
  - "job_script.sh"
  - "input file"
  - "CPU waste"
  - "farm directory"
  - "meta-job"
  - "meta-jobs"
  - "resubmit.run"
  - "error messages"
  - "table.dat"
  - "farm status"
  - "run-time limit"
  - "single_case.sh"
  - "META package"
  - "exit early"
  - "auto-resubmission"
  - "environment variables"
  - "MPI scheduling"
  - "META-Farm"
  - "Niagara/Trillium"
  - "serial farming jobs"
  - "sbatch arguments"
  - "config.h"
  - "meta-farm"
  - "job farming"
  - "subdirectory"
  - "srun"
  - "WHOLE_NODE mode"
  - "GPU applications"
  - "META mode"
  - "submit.run"
  - "command line arguments"
  - "post-processing job"
  - "NJOBS_MAX"
  - "failed cases"
  - "WHOLE_NODE"
  - "running jobs"
  - "--mem-per-cpu"
  - "(re)submit.run"
  - "case"
  - "troubleshooting"
  - "lockfile"

questions:
  - "How do you enable the automatic resubmission feature for large farms, and how does it affect the NJOBS_MAX parameter?"
  - "What steps are required to automatically execute a post-processing job, and under what condition will it fail to run?"
  - "How can the WHOLE_NODE mode be enabled and configured for clusters that require packaging serial jobs into whole node jobs?"
  - "How does enabling the WHOLE_NODE mode alter the function of the submit.run command, and what are its specific limitations regarding job types?"
  - "What steps must a user take to manually install and configure the META package from the git repository on a cluster where it is not available as a module?"
  - "How should users modify their job scripts and submission commands to properly configure and run multi-threaded or MPI applications?"
  - "What is the primary function of the WHOLE_NODE mode introduced in meta-farm version 1.0.3?"
  - "Which file needs to be edited to enable the WHOLE_NODE mode, and what specific setting must be changed?"
  - "How should the NWHOLE variable be configured depending on the specific cluster being used?"
  - "How do you specify the memory per CPU when passing arguments to the `(re)submit.run` command?"
  - "Where can users find additional information for handling more complicated MPI scheduling scenarios?"
  - "What are the two alternative methods described for adding the `srun` command to execute your MPI code?"
  - "How can users prevent their meta-jobs from failing when a node's GPU becomes unavailable?"
  - "What is the recommended method for passing custom environment variables to all farm jobs without breaking the default inheritance behavior?"
  - "How should a user configure their job setup if the application requires reading an input file with a strictly prescribed, unchangeable name?"
  - "How can single_case.sh be customized to access individual parameters or a variable number of command-line arguments from the cases table?"
  - "What specific scenario causes a potential waste of CPU cycles when running multiple cases per meta-job?"
  - "How does the task.run script intelligently estimate case run-times to prevent calculations from being interrupted by a job's time limit?"
  - "How must the subdirectories and input files be organized to successfully run multiple cases?"
  - "Where should the pre-configured input files for each individual case be stored?"
  - "What specific information needs to be included in the table.dat file for this process?"
  - "Where is the current time estimate for a meta-job stored?"
  - "How does the meta-job calculate whether it has enough time to finish a case?"
  - "What is the primary benefit of the meta-job exiting early if it lacks sufficient time?"
  - "How does the algorithm use powers of two to optimize the computation of the dt_cutoff estimate and reduce wasted CPU cycles?"
  - "Why is the lockfile utility considered critical for this package, and how does it manage meta-job access?"
  - "What are the primary causes of errors when using submit.run and resubmit.run, and how can they be resolved?"
  - "Why does the \"Jobs are still running/queued\" error occur when using resubmit.run, and how can the farm's status be checked?"
  - "What does the message \"No failed/unfinished jobs; nothing to resubmit\" indicate about the current processing state of the farm?"
  - "What triggers the \"Too many failed (very short) cases - exiting\" error when running jobs?"
  - "How can a user resolve the issue where the initial cases fail in less than the specified duration?"
  - "What troubleshooting steps should be taken if the system reports that the lockfile utility is missing on a compute node?"
  - "What are the different conditions and messages that indicate a meta-job is exiting, either normally or due to time constraints?"
  - "How can a user resolve the issue where the initial cases fail in less than the specified duration?"
  - "What troubleshooting steps should be taken if the system reports that the lockfile utility is missing on a compute node?"
  - "What are the different conditions and messages that indicate a meta-job is exiting, either normally or due to time constraints?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Cette page présente les fonctionnalités avancées du paquet [META-Farm](meta-farm.md).

## Resoumettre automatiquement les cas qui ont échoué

Si votre ferme de tâches est particulièrement grande, c'est-à-dire si elle nécessite plus de ressources que `NJOBS_MAX x job_run_time`, où `NJOBS_MAX` est le nombre maximal de tâches que l'on peut soumettre, vous devrez exécuter `resubmit.run` une fois la ferme de tâches originale terminée – peut-être plus d'une fois. Vous pouvez le faire manuellement, mais avec META, vous pouvez également automatiser ce processus. Pour activer cette fonctionnalité, ajoutez le commutateur `-auto` à votre commande `submit.run` ou `resubmit.run` :

```bash
submit.run N -auto
```

Ceci peut être utilisé en mode SIMPLE ou META. Si votre commande `submit.run` originale n'avait pas le commutateur `-auto`, vous pouvez l'ajouter à `resubmit.run` une fois la ferme originale terminée, pour le même effet.

Lorsque vous ajoutez `-auto`, `(re)submit.run` soumet une tâche supplémentaire (série), en plus des tâches de la ferme. Le but de cette tâche est d'exécuter la commande `resubmit.run` automatiquement juste après la fin de la ferme actuelle. Le script de tâche pour cette tâche additionnelle est `resubmit_script.sh`, qui devrait être présent dans le répertoire de la ferme; un fichier exemple y est automatiquement copié lorsque vous exécutez `farm_init.run`. La seule personnalisation que vous devez faire à ce fichier est de corriger le nom de compte dans la ligne `#SBATCH -A`.

Si vous utilisez `-auto`, la valeur du paramètre `NJOBS_MAX` défini dans le fichier `config.h` doit être au moins une unité inférieure au nombre maximal de tâches que vous pouvez soumettre sur la grappe.
Par exemple, si le nombre maximal de tâches que l'on peut soumettre sur la grappe est 999 et que vous avez l'intention d'utiliser `-auto`, définissez `NJOBS_MAX` à 998. Pour connaître la limite maximale de tâches soumises (MaxSubmit) associée à votre compte sur une grappe spécifique, exécutez la commande suivante :

```bash
sacctmgr list user $USER withassoc
```

Lorsque vous utilisez `-auto`, si, à un moment donné, les seuls cas restants à traiter sont ceux qui ont échoué précédemment, la resoumission automatique s'arrêtera et les calculs de la ferme prendront fin. Cela vise à éviter une boucle infinie sur des cas mal formés qui échoueront toujours. Si cela se produit, vous devrez examiner les raisons de l'échec de ces cas avant de tenter de resoumettre la ferme. Vous pouvez consulter les messages pertinents dans le fichier `farm.log` créé dans le répertoire de la ferme.

## Exécuter automatiquement une tâche de post-traitement

Une autre fonctionnalité avancée est la capacité d'exécuter une tâche de post-traitement automatiquement une fois que tous les cas de `table.dat` ont été **traités avec succès**. Si des cas ont échoué, c'est-à-dire s'ils ont eu un statut de sortie non nul, la tâche de post-traitement ne s'exécutera pas. Pour activer cette fonctionnalité, créez simplement un script pour la tâche de post-traitement nommé `final.sh` à l'intérieur du répertoire de la ferme. Cette tâche peut être de n'importe quel type – série, parallèle ou une tâche tableau.

Cette fonctionnalité utilise le même script, `resubmit_script.sh`, décrit pour [l'option `-auto`](#resoumettre-automatiquement-les-cas-qui-ont-echoue) ci-dessus. Assurez-vous que `resubmit_script.sh` a le bon nom de compte dans la ligne `#SBATCH -A`.

La fonctionnalité de post-traitement automatique entraîne également la soumission de tâches série supplémentaires, au-delà du nombre que vous demandez. Ajustez le paramètre `NJOBS_MAX` dans `config.h` en conséquence (par exemple, si la grappe a une limite de tâches de 999, définissez-la à 998). Cependant, si vous utilisez à la fois les fonctionnalités de resoumission automatique et de post-traitement automatique, elles ne soumettront ensemble qu'une **seule** tâche supplémentaire. Vous n'avez pas besoin de soustraire 2 de `NJOBS_MAX`.

Les messages système de la fonctionnalité de resoumission automatique sont enregistrés dans `farm.log`, dans le répertoire racine de la ferme.

## Mode WHOLE_NODE

À partir de la version 1.0.3, META-Farm prend en charge l'empaquetage de tâches série individuelles en tâches de nœud entier. Cela a rendu possible l'utilisation du paquet sur les grappes Niagara/Trillium. Ce mode est désactivé par défaut. Pour l'activer, modifiez le fichier `config.h` dans votre répertoire de ferme. Plus précisément, vous devez définir `WHOLE_NODE=1` et définir la variable `NWHOLE` au nombre de cœurs de processeur par nœud (40 pour Niagara; 192 pour Trillium).

En mode WHOLE_NODE, l'argument entier positif de la commande `submit.run` change de signification : au lieu d'être le nombre de méta-tâches, c'est maintenant le nombre de nœuds entiers à utiliser en mode META. Par exemple, considérez cette commande :

```bash
submit.run 2
```

Si le mode WHOLE_NODE est activé, la commande ci-dessus allouera 2 nœuds entiers, qui seront utilisés pour exécuter jusqu'à 384 tâches série concurrentes (192 tâches sur chaque nœud) en utilisant le mode META (équilibrage dynamique de la charge de travail). Ces tâches sont exécutées comme des threads séparés au sein des tâches de nœud entier.

L'argument "-1" pour `submit.run` conserve sa signification originale : exécuter la ferme en utilisant le mode SIMPLE. Le nombre de tâches réelles (nœud entier) est calculé comme `Nombre_de_cas / NWHOLE`.

Détails importants :

*   Les fonctionnalités avancées "Resoumission automatique de tâches" et "Tâche de post-traitement automatique" ne fonctionneront sur Trillium que si vous placez la ligne suivante à la fin de votre fichier `~/.bashrc` :
    ```bash
    module load StdEnv
    ```
*   Le mode WHOLE_NODE ne peut être utilisé que pour le "farming" de tâches série. (C'est-à-dire qu'il ne peut pas être utilisé pour le "farming" multi-thread, MPI ou GPU).
*   Le mode WHOLE_NODE peut également être utilisé sur d'autres grappes (pas seulement sur Trillium). Il peut être avantageux dans les situations où le temps d'attente en file d'attente pour les tâches de nœud entier devient plus court que le temps d'attente en file d'attente pour les tâches série.

## Information additionnelle

### Utiliser le dépôt Git

Pour utiliser META sur une grappe où il n'est pas installé en tant que module, vous pouvez cloner le paquet depuis notre dépôt Git :

```bash
git clone https://git.computecanada.ca/syam/meta-farm.git
```

Ensuite, modifiez votre variable `$PATH` pour qu'elle pointe vers le sous-répertoire `bin` du répertoire `meta-farm` nouvellement créé. En supposant que vous ayez exécuté `git clone` dans votre répertoire personnel, faites ceci :

```bash
export PATH=~/meta-farm/bin:$PATH
```

Puis, procédez comme indiqué dans le [guide de démarrage rapide](meta-farm.md#demarrage-rapide) de META à partir de l'étape `farm_init.run`.

### Transmettre des arguments sbatch additionnels

Si vous avez besoin d'utiliser des arguments `sbatch` supplémentaires (comme `--mem 4G`, `--gres=gpu:1`, *etc.*), ajoutez-les à `job_script.sh` en tant que lignes `#SBATCH` distinctes.

Ou si vous préférez, vous pouvez les ajouter à la fin de la commande `submit.run` ou `resubmit.run` et ils seront transmis à `sbatch`, par exemple :

```bash
submit.run -1 --mem 4G
```

### Applications multifils

Pour les [applications multifils](running_jobs.md#applications-multifils-ou-openmp) (telles que celles qui utilisent [OpenMP](https://docs.alliancecan.ca/wiki/OpenMP), par exemple), ajoutez les lignes suivantes à `job_script.sh` :

```bash
#SBATCH --cpus-per-task=N
#SBATCH --mem=M
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
```

... où *N* est le nombre de cœurs de processeur à utiliser, et *M* est la mémoire totale à réserver en mégaoctets. Vous pouvez également fournir `--cpus-per-task=N` et `--mem=M` comme arguments à `(re)submit.run`.

### Applications MPI

Pour les applications qui utilisent [MPI](https://docs.alliancecan.ca/wiki/MPI), ajoutez les lignes suivantes à `job_script.sh` :

```bash
#SBATCH --ntasks=N
#SBATCH --mem-per-cpu=M
```

... où *N* est le nombre de cœurs de processeur à utiliser, et *M* est la mémoire à réserver pour chaque cœur, en mégaoctets. Vous pouvez également fournir `--ntasks=N` et `--mem-per-cpu=M` comme arguments à `(re)submit.run`. Voir la [planification MPI avancée](advanced_mpi_scheduling.md) pour plus d'informations sur des scénarios MPI plus complexes.

Ajoutez également `srun` avant le chemin de votre code à l'intérieur de `single_case.sh`, par exemple :

```bash
srun $COMM
```

Alternativement, vous pouvez ajouter `srun` au début de chaque ligne de `table.dat` :

```bash
srun /path/to/mpi_code arg1 arg2
srun /path/to/mpi_code arg1 arg2
...
srun /path/to/mpi_code arg1 arg2
```

### Applications GPU

Pour les applications qui utilisent des GPU, modifiez `job_script.sh` en suivant les directives de [Utiliser les GPU avec Slurm](using_gpus_with_slurm.md) :

```bash
#SBATCH --gres=gpu[[:type]:nombre]
```

Vous voudrez peut-être aussi copier l'utilitaire `~syam/bin/gpu_test` dans votre répertoire `~/bin` (uniquement sur Nibi), et mettre les lignes suivantes dans `job_script.sh` juste avant la ligne `task.run` :

```bash
~/bin/gpu_test
retVal=$?
if [ $retVal -ne 0 ]; then
    echo "Aucun GPU trouvé - sortie..."
    exit 1
fi
```

Ceci permettra de détecter les rares situations où un problème avec le nœud rend le GPU indisponible. Si cela arrive à l'une de vos méta-tâches, et que vous ne détectez pas la défaillance du GPU d'une manière ou d'une autre, la tâche tentera (et échouera) d'exécuter tous vos cas de `table.dat`.

### Variables d'environnement et `--export`

Toutes les tâches générées par le paquet META héritent de l'environnement présent lorsque vous exécutez `submit.run` ou `resubmit.run`. Cela inclut tous les modules chargés et les variables d'environnement. META s'appuie sur ce comportement pour son fonctionnement, utilisant certaines variables d'environnement pour transmettre des informations entre les scripts. Vous devez faire attention à ne pas rompre ce comportement par défaut, ce qui peut arriver si vous utilisez le commutateur `--export`. Si vous devez utiliser `--export` dans votre ferme, assurez-vous que `ALL` est l'un des arguments de cette commande, par exemple `--export=ALL,X=1,Y=2`.

Si vous avez besoin de transmettre les valeurs de variables d'environnement personnalisées à toutes vos tâches de ferme (y compris les tâches resoumises automatiquement et la tâche de post-traitement s'il y en a une), n'utilisez pas `--export`. Au lieu de cela, définissez les variables sur la ligne de commande comme dans cet exemple :

```bash
VAR1=1 VAR2=5 VAR3=3.1416 submit.run ...
```

Ici, `VAR1`, `VAR2`, `VAR3` sont des variables d'environnement personnalisées qui seront transmises à toutes les tâches de la ferme.

### Exemple : fichiers d'entrée numérotés

Supposons que vous ayez une application appelée `fcode`, et que chaque cas doive lire un fichier distinct à partir de l'entrée standard – disons `data.X`, où *X* varie de 1 à `N_cases`. Les fichiers d'entrée sont tous stockés dans un répertoire `/home/user/IC`. Assurez-vous que `fcode` est dans votre `$PATH` (par exemple, placez `fcode` dans `~/bin`, et assurez-vous que `/home/$USER/bin` est ajouté à `$PATH` dans `~/.bashrc`), ou utilisez un chemin complet vers `fcode` dans `table.dat`. Créez `table.dat` dans le répertoire de la ferme META comme ceci :

```
fcode < /home/user/IC/data.1
fcode < /home/user/IC/data.2
fcode < /home/user/IC/data.3
...
```

Vous pourriez vouloir utiliser une boucle shell pour créer `table.dat`, par exemple :

```bash
for ((i=1; i<=100; i++)); do echo "fcode < /home/user/IC/data.$i"; done >table.dat
```

### Exemple : le fichier d'entrée doit avoir le même nom

Certaines applications s'attendent à lire l'entrée depuis un fichier avec un nom prescrit et immuable, comme `INPUT` par exemple. Pour gérer cette situation, chaque cas doit s'exécuter dans son propre sous-répertoire, et vous devez créer un fichier d'entrée avec le nom prescrit dans chaque sous-répertoire. Supposons pour cet exemple que vous ayez préparé les différents fichiers d'entrée pour chaque cas et que vous les ayez stockés dans `/path/to/data.X`, où *X* varie de 1 à `N_cases`. Votre `table.dat` peut ne contenir que le nom de l'application, encore et encore :

```
/path/to/code
/path/to/code
...
```

Ajoutez une ligne à `single_case.sh` qui copie le fichier d'entrée dans le sous-répertoire de la ferme pour chaque cas – la première ligne de l'exemple ci-dessous :

```bash
cp /path/to/data.$ID INPUT
$COMM
STATUS=$?
```

### Accéder à chaque paramètre d'un cas

Les exemples montrés jusqu'à présent supposent que chaque ligne dans la table des cas est une instruction exécutable, commençant par le nom du fichier exécutable (quand il est dans votre `$PATH`) ou le chemin complet vers le fichier exécutable, puis listant les arguments de ligne de commande particuliers à ce cas, ou quelque chose comme `< input.$ID` si votre code s'attend à lire un fichier d'entrée standard.

Dans le cas le plus général, vous voudrez peut-être pouvoir accéder à toutes les colonnes de la table individuellement. Cela peut être fait en modifiant `single_case.sh` :

```bash
...
# ++++++++++++ Cette partie peut être personnalisée : ++++++++++++
# $ID contient l'identifiant du cas de la table originale
# $COMM est la ligne correspondant au cas $ID dans la table originale, sans le champ ID
mkdir RUN$ID
cd RUN$ID

# Conversion de $COMM en tableau :
COMM=( $COMM )
# Nombre de colonnes dans COMM :
Ncol=${#COMM[@]}
# On peut maintenant accéder aux colonnes individuellement, comme ${COMM[i]}, où i=0...$Ncol-1
# Une plage de colonnes peut être accédée comme ${COMM[@]:i:n}, où i est la première colonne
# à afficher, et n est le nombre de colonnes à afficher
# Utilisez la syntaxe ${COMM[@]:i} pour afficher toutes les colonnes à partir de la i-ème colonne
# (utilisez pour les codes avec un nombre variable d'arguments en ligne de commande).

# Appeler le code utilisateur ici.
...

# Statut de sortie du code :
STATUS=$?
cd ..
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
...
```

Par exemple, vous pourriez avoir besoin de fournir à votre code *à la fois* un fichier d'entrée standard *et* un nombre variable d'arguments de ligne de commande. Votre table de cas ressemblera à ceci :

```
/path/to/IC.1 0.1
/path/to/IC.2 0.2 10
...
```

La manière de l'implémenter dans `single_case.sh` est la suivante :

```bash
# Appeler le code utilisateur ici.
/path/to/code ${COMM[@]:1} < ${COMM[0]}
```

## Réduire le gaspillage

Voici un problème potentiel lorsque l'on exécute plusieurs cas par tâche : que se passe-t-il si le nombre de méta-tâches en cours d'exécution multiplié par le temps d'exécution demandé par méta-tâche (disons, 3 jours) n'est pas suffisant pour traiter tous vos cas ? Par exemple, vous avez réussi à démarrer le maximum autorisé de 1000 méta-tâches, chacune ayant une limite de temps d'exécution de 3 jours. Cela signifie que votre ferme ne peut traiter tous les cas en une seule exécution que si `temps_d_execution_moyen_du_cas x Nombre_de_cas < 1000 x 3j = 3000` jours CPU. Une fois que vos méta-tâches commencent à atteindre la limite de temps d'exécution de 3 jours, elles commenceront à s'arrêter au milieu du traitement de l'un de vos cas. Cela entraînera jusqu'à 1000 calculs de cas interrompus. Ce n'est pas un gros problème en termes d'achèvement du travail --- `resubmit.run` trouvera tous les cas qui ont échoué ou n'ont jamais été exécutés, et les redémarrera automatiquement. Mais cela peut devenir un gaspillage de cycles CPU. En moyenne, vous gaspillerez `0.5 x N_tâches x temps_d_exécution_moyen_du_cas`. Par exemple, si vos cas ont un temps d'exécution moyen de 1 heure, et que vous avez 1000 méta-tâches en cours d'exécution, vous gaspillerez environ 500 heures CPU ou environ 20 jours CPU, ce qui n'est pas acceptable.

Heureusement, les scripts que nous fournissons ont une certaine intelligence intégrée pour atténuer ce problème. Cela est implémenté dans `task.run` comme suit :

*   Le script mesure le temps d'exécution de chaque cas et ajoute la valeur comme une ligne dans un fichier temporaire `times` créé dans le répertoire `/home/$USER/tmp/$NODE.$PID/`. (Voir les [fichiers de sortie](meta-farm.md#fichiers-de-sortie)). Ceci est fait par toutes les méta-tâches en cours d'exécution.
*   Une fois les 8 premiers cas calculés, l'une des méta-tâches lira le contenu du fichier `times` et calculera le quantile le plus grand de 12,5% pour la distribution actuelle des temps d'exécution des cas. Cela servira d'estimation conservative du temps d'exécution pour vos cas individuels, `dt_cutoff`. L'estimation actuelle est stockée dans le fichier `dt_cutoff` dans `/home/$USER/tmp/$NODE.$PID/`.
*   Désormais, chaque méta-tâche estimera si elle a le temps de terminer le cas qu'elle est sur le point de commencer à calculer, en s'assurant que `t_finish - t_now > dt_cutoff`. Ici, `t_finish` est le moment où la tâche s'arrêtera en raison de la limite de temps d'exécution de la tâche, et `t_now` est l'heure actuelle. Si elle estime qu'elle n'a pas le temps, elle quittera plus tôt, ce qui minimisera le risque qu'un cas soit interrompu à mi-chemin en raison de la limite de temps d'exécution de la tâche.
*   À chaque puissance de deux subséquente du nombre de cas calculés (8, puis 16, puis 32 et ainsi de suite), `dt_cutoff` est recalculé en utilisant l'algorithme ci-dessus. Cela rendra l'estimation de `dt_cutoff` de plus en plus précise. La puissance de deux est utilisée pour minimiser les frais généraux liés au calcul de `dt_cutoff`; l'algorithme sera également efficace pour un nombre de cas très petit (dizaines) et très grand (plusieurs milliers).
*   L'algorithme ci-dessus réduit en moyenne la quantité de cycles CPU gaspillés en raison des tâches atteignant la limite de temps d'exécution d'un facteur 8.

En tant qu'effet secondaire utile, chaque fois que vous exécutez une ferme, vous obtenez les temps d'exécution individuels pour tous vos cas stockés dans `/home/$USER/tmp/$NODE.$PID/times`. Vous pouvez analyser ce fichier pour affiner la configuration de votre ferme, pour le profilage de votre code, etc.

## Dépannage

Ici, nous expliquons les messages d'erreur typiques que vous pourriez rencontrer lors de l'utilisation de ce paquet.

### Problèmes avec des commandes multiples

!!! error "Non-farm directory, or no farm has been submitted; exiting"
    Soit le répertoire actuel n'est pas un répertoire de ferme, soit vous n'avez jamais exécuté `submit.run` pour cette ferme.

### Problèmes avec `submit.run`

!!! error "Wrong first argument: XXX (should be a positive integer or -1) ; exiting"
    Utilisez le bon premier argument : `-1` pour le mode SIMPLE, ou un entier positif `N` (nombre de méta-tâches demandées) pour le mode META.

!!! error "lockfile is not on path; exiting"
    Assurez-vous que l'utilitaire `lockfile` est dans votre `$PATH`. Cet utilitaire est essentiel pour ce paquet. Il fournit un accès sérialisé des méta-tâches au fichier `table.dat`, c'est-à-dire qu'il garantit que deux méta-tâches différentes ne lisent pas la même ligne de `table.dat` en même temps.

!!! error "Non-farm directory (config.h, job_script.sh, single_case.sh, and/or table.dat are missing); exiting"
    Soit le répertoire actuel n'est pas un répertoire de ferme, soit certains fichiers importants sont manquants. Changez pour le bon répertoire (de ferme) ou créez les fichiers manquants (`config.h`, `job_script.sh`, `single_case.sh`, `table.dat`).

!!! error "-auto option requires resubmit_script.sh file in the root farm directory; exiting"
    Vous avez utilisé l'option `-auto`, mais vous avez oublié de créer le fichier `resubmit_script.sh` dans le répertoire racine de la ferme. Un exemple de `resubmit_script.sh` est créé automatiquement lorsque vous utilisez `farm_init.run`.

!!! error "File table.dat doesn't exist. Exiting"
    Vous avez oublié de créer le fichier `table.dat` dans le répertoire actuel, ou peut-être exécutez-vous `submit.run` non pas à l'intérieur de l'un de vos sous-répertoires de ferme.

!!! error "Job runtime sbatch argument (-t or --time) is missing in job_script.sh. Exiting"
    Assurez-vous de fournir une limite de temps d'exécution pour toutes les méta-tâches en tant qu'argument `#SBATCH` dans votre fichier `job_script.sh`. Le temps d'exécution est le seul qui ne peut pas être passé comme argument facultatif à `submit.run`.

!!! error "Wrong job runtime in job_script.sh - nnn . Exiting"
    Vous n'avez pas correctement formaté l'argument de temps d'exécution dans votre fichier `job_script.sh`.

!!! error "Something wrong with sbatch farm submission; jobid=XXX; aborting"
!!! error "Something wrong with a auto-resubmit job submission; jobid=XXX; aborting"
    Avec l'un ou l'autre de ces deux messages, il y a eu un problème avec la soumission de tâches avec `sbatch`. Le planificateur de la grappe pourrait mal fonctionner, ou simplement être trop occupé. Réessayez un peu plus tard.

!!! error "Couldn't create subdirectories inside the farm directory ; exiting"
!!! error "Couldn't create the temp directory XXX ; exiting"
!!! error "Couldn't create a file inside XXX ; exiting"
    Avec l'un de ces trois messages, quelque chose ne va pas avec un système de fichiers : soit les permissions ont été corrompues, soit vous avez épuisé un quota. Corrigez le(s) problème(s), puis réessayez.

### Problèmes avec `resubmit.run`

!!! error "Jobs are still running/queued; cannot resubmit"
    Vous ne pouvez pas utiliser `resubmit.run` tant que toutes les méta-tâches de cette ferme n'ont pas terminé leur exécution. Utilisez `list.run` ou `queue.run` pour vérifier l'état de la ferme.

!!! error "No failed/unfinished jobs; nothing to resubmit"
    Votre ferme a été traitée à 100 %. Il n'y a plus de cas (échoués ou non exécutés) à calculer.

### Problèmes avec les tâches en cours

!!! error "Too many failed (very short) cases - exiting"
    Cela se produit si les `$N_failed_max` premiers cas sont très courts – moins de `$dt_failed` secondes. Déterminez ce qui cause l'échec des cas et corrigez le problème, ou ajustez les valeurs `$N_failed_max` et `$dt_failed` dans `config.h`.

!!! error "lockfile is not on path on node XXX"
    Comme le suggère le message d'erreur, d'une manière ou d'une autre, l'utilitaire `lockfile` n'est pas dans votre `$PATH` sur certains nœuds. Utilisez `which lockfile` pour vous assurer que l'utilitaire est bien dans votre `$PATH`. S'il est dans votre `$PATH` sur un nœud de connexion, alors quelque chose s'est mal passé sur ce nœud de calcul particulier, par exemple un système de fichiers pourrait avoir échoué à se monter.

!!! note "Exiting after processing one case (-1 option)"
    Ceci n'est pas un message d'erreur. Cela vous indique simplement que vous avez soumis la ferme avec `submit.run -1` (mode un cas par tâche), donc chaque méta-tâche quitte après avoir traité un seul cas.

!!! note "Not enough runtime left; exiting."
    Ce message vous indique que la méta-tâche n'aurait probablement pas assez de temps restant pour traiter le cas suivant (selon l'analyse des temps d'exécution de tous les cas traités jusqu'à présent), elle quitte donc plus tôt.

!!! note "No cases left; exiting."
    Ceci n'est pas un message d'erreur. C'est ainsi que chaque méta-tâche se termine normalement, lorsque tous les cas ont été calculés.

!!! warning "Only failed cases left; cannot auto-resubmit; exiting"
    Cela ne peut se produire que si vous avez utilisé le commutateur `-auto` lors de la soumission de la ferme. Trouvez les cas échoués avec `Status.run -f`, corrigez le(s) problème(s) à l'origine de l'échec des cas, puis exécutez `resubmit.run`.

---

!!! info "Page enfant de"
    [META: A package for job farming](meta-farm.md)