---
title: "META-Farm: Advanced features and troubleshooting/fr"
slug: "meta-farm__advanced_features_and_troubleshooting"
lang: "fr"

source_wiki_title: "META-Farm: Advanced features and troubleshooting/fr"
source_hash: "e252c3fda651e6ddbb226232269e660b"
last_synced: "2026-10-04T02:27:33.201522+00:00"
last_processed: "2026-10-04T03:10:41.922473+00:00"

tags:
  []

keywords:
  - "WHOLE_NODE"
  - "META mode"
  - "Trillium"
  - "serial farming jobs"
  - "srun"
  - "-auto switch"
  - "(re)submit.run"
  - "gpu_test"
  - "sbatch arguments"
  - "--mem-per-cpu"
  - "run-time limit"
  - "exit early"
  - "farm directory"
  - "not enough runtime left"
  - "auto-resubmit"
  - "meta-jobs"
  - "final.sh"
  - "array COMM"
  - "N_failed_max"
  - "queue.run"
  - "environment variables"
  - "Niagara"
  - "table.dat"
  - "sbatch"
  - "/path/to/code"
  - "Advanced MPI scheduling"
  - "resubmit.run"
  - "list.run"
  - "input file"
  - "submit.run -1"
  - "single_case.sh"
  - "prescribed name"
  - "meta-farm"
  - "automatic job resubmission"
  - "lockfile"
  - "submit.run"
  - "WHOLE_NODE mode"
  - "SBATCH --gres=gpu"
  - "farm 100% processed"
  - "jobs still running/queued"
  - "dt_cutoff"
  - "subdirectory"
  - "NJOBS_MAX"
  - "t_finish - t_now > dt_cutoff"
  - "meta-job"
  - "--export"

questions:
  - "Comment activer la fonction de resoumission automatique des cas échoués en utilisant le commutateur **-auto** ?"
  - "Quelle est la procédure pour configurer et lancer automatiquement une tâche de post‑traitement (script **final.sh**) après que toutes les cases de *table.dat* aient été traitées avec succès ?"
  - "Comment activer le mode **WHOLE_NODE** et quels paramètres du fichier **config.h** doivent être définis (par ex. **WHOLE_NODE=1**, **NWHOLE**) pour l’utiliser sur les clusters Niagara ou Trillium ?"
  - "What does the integer argument to `submit.run` represent in WHOLE_NODE mode, and how many concurrent serial tasks can each allocated whole node run?"
  - "Which line must be added to `~/.bashrc` to enable the “Automatic job resubmission” and “Automatic post‑processing job” features on Trillium, and what types of farming are compatible with WHOLE_NODE mode?"
  - "How can additional `sbatch` options or resource specifications for multi‑threaded (OpenMP) and MPI applications be provided, either by editing `job_script.sh` or by appending them to the `submit.run`/`resubmit.run` commands?"
  - "What version of meta‑farm introduced the WHOLE_NODE mode?"
  - "How can a user enable WHOLE_NODE mode in the farm configuration?"
  - "What should the NWHOLE variable be set to for the Niagara and Trillium clusters?"
  - "How do you specify memory per CPU using the `--mem-per-cpu=M` option when running `(re)submit.run`?"
  - "What is the correct way to prepend `srun` to the command path inside `single_case.sh` for executing your MPI code?"
  - "How can you modify `table.dat` so that each MPI command line is automatically prefixed with `srun`?"
  - "How should a job script be modified to request GPUs and detect GPU availability failures when running META jobs?"
  - "What is the recommended method for passing custom environment variables to all farm jobs without breaking META’s default behavior, especially concerning the use of the --export option?"
  - "How do you construct table.dat for applications that need numbered input files versus those that require a fixed input filename in each subdirectory?"
  - "Comment ajouter une ligne dans `single_case.sh` pour copier le fichier d’entrée dans le sous‑répertoire « farm » de chaque cas ?"
  - "De quelle manière peut‑on accéder individuellement aux colonnes du tableau des cas dans `single_case.sh`, et quelles syntaxes permettent d’extraire des sous‑ensembles de colonnes ?"
  - "Quel mécanisme les scripts utilisent‑ils pour réduire le gaspillage de CPU lorsque la limite de temps d’un méta‑job est atteinte, et comment la valeur `dt_cutoff` est‑elle calculée et appliquée ?"
  - "How should each case be organized in its own subdirectory and what files need to be placed there?"
  - "What naming convention must be used for the input files stored in `/path/to/data.X` for the different cases?"
  - "What content is required in the `table.dat` file for this setup?"
  - "Where is the current estimate for `dt_cutoff` stored?"
  - "What condition must be satisfied for a meta‑job to start computing a case?"
  - "What does a meta‑job do if it determines that the remaining time is insufficient?"
  - "How does the algorithm recompute dt_cutoff at each power‑of‑two case count, and why does using powers of two minimise overhead while improving accuracy?"
  - "What are the typical error messages described in the troubleshooting section, and what steps should be taken to resolve each of them?"
  - "How can the per‑case runtime data saved in /home/$USER/tmp/$NODE.$PID/times be used to profile code and fine‑tune the farm configuration?"
  - "What does the message “Jobs are still running/queued; cannot resubmit” indicate and how can it be resolved?"
  - "Which commands should be used to check the status of a farm before attempting to run `resubmit.run`?"
  - "What does the error “Too many failed (very short) cases – exiting” mean, and what steps can be taken to address it?"
  - "What should you do when the first $N_failed_max cases are very short (less than $dt_failed seconds) and cause failures?"
  - "How can you troubleshoot and fix the “lockfile is not on path on node XXX” error?"
  - "What does the “Not enough runtime left; exiting.” message mean, and how should you respond to it?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Cette page présente les fonctionnalités avancées du paquet META-Farm.

## Resoumission automatique des cas échoués

Si votre ferme de calcul est particulièrement grande, c'est-à-dire si elle nécessite plus de ressources que `NJOBS_MAX x temps_d_exécution_du_job`, où `NJOBS_MAX` est le nombre maximum de jobs qu'il est permis de soumettre, vous devrez exécuter `resubmit.run` après que la ferme initiale ait terminé son exécution – peut-être plus d'une fois. Vous pouvez le faire manuellement, mais avec META, vous pouvez aussi automatiser ce processus. Pour activer cette fonctionnalité, ajoutez le commutateur `-auto` à votre commande `submit.run` ou `resubmit.run` :

```bash
$ submit.run N -auto
```

Ceci peut être utilisé en mode SIMPLE ou META. Si votre commande `submit.run` initiale n'avait pas le commutateur `-auto`, vous pouvez l'ajouter à `resubmit.run` après que la ferme initiale ait terminé son exécution, pour le même résultat.

Lorsque vous ajoutez `-auto`, `(re)submit.run` soumet un job (sériel) supplémentaire, en plus des jobs de la ferme. L'objectif de ce job est d'exécuter la commande `resubmit.run` automatiquement juste après la fin de l'exécution de la ferme actuelle. Le script de job pour ce job additionnel est `resubmit_script.sh`, qui devrait être présent dans le répertoire de la ferme; un fichier d'exemple y est automatiquement copié lorsque vous exécutez `farm_init.run`. La seule personnalisation que vous devez apporter à ce fichier est de corriger le nom du compte dans la ligne `#SBATCH -A`.

Si vous utilisez `-auto`, la valeur du paramètre `NJOBS_MAX` défini dans le fichier `config.h` devrait être au moins d'une unité inférieure au nombre maximal de jobs que vous pouvez soumettre sur le cluster. Par exemple, si le nombre maximal de jobs que l'on peut soumettre sur le cluster est de 999 et que vous comptez utiliser `-auto`, définissez `NJOBS_MAX` à 998. Pour connaître la limite maximale de jobs soumis (MaxSubmit) associée à votre compte sur un cluster spécifique, exécutez la commande suivante :

```bash
$ sacctmgr list user $USER withassoc
```

Lorsque vous utilisez `-auto`, si à un certain moment les seuls cas à traiter sont ceux qui ont échoué précédemment, la resoumission automatique s'arrêtera et les calculs de la ferme prendront fin. Ceci vise à éviter une boucle infinie sur des cas mal formulés qui échoueront toujours. Si cela se produit, vous devez remédier aux raisons de l'échec de ces cas avant de tenter de resoumettre la ferme. Vous pouvez consulter les messages pertinents dans le fichier `farm.log` créé dans le répertoire de la ferme.

## Exécution automatique d'un job de post-traitement

Une autre fonctionnalité avancée est la capacité d'exécuter automatiquement un job de post-traitement une fois que tous les cas de `table.dat` ont été **traités avec succès**. Si des cas ont échoué – c'est-à-dire qu'ils avaient un code de sortie non nul – le job de post-traitement ne s'exécutera pas. Pour activer cette fonctionnalité, créez simplement un script pour le job de post-traitement nommé `final.sh` à l'intérieur du répertoire de la ferme. Ce job peut être de n'importe quel type : sériel, parallèle ou un job tableau.

Cette fonctionnalité utilise le même script, `resubmit_script.sh`, décrit pour la [resoumission automatique des cas échoués](#resoumission-automatique-des-cas-échoués) ci-dessus. Assurez-vous que `resubmit_script.sh` contient le nom de compte correct dans la ligne `#SBATCH -A`.

La fonctionnalité de post-traitement automatique entraîne également la soumission de jobs sériels supplémentaires, au-delà du nombre que vous avez demandé. Ajustez le paramètre `NJOBS_MAX` dans `config.h` en conséquence (par exemple, si le cluster a une limite de 999 jobs, définissez-le à 998). Cependant, si vous utilisez à la fois les fonctionnalités de resoumission automatique et de post-traitement automatique, elles ne soumettront ensemble qu'**un** job supplémentaire. Vous n'avez pas besoin de soustraire 2 de `NJOBS_MAX`.

Les messages système de la fonctionnalité de resoumission automatique sont enregistrés dans `farm.log`, dans le répertoire racine de la ferme.

## Mode WHOLE_NODE

À partir de la version 1.0.3, meta-farm prend en charge l'intégration de jobs de ferme sériels individuels dans des jobs de nœud entier. Cela a rendu possible l'utilisation du paquet sur les clusters Niagara/Trillium. Ce mode est désactivé par défaut. Pour l'activer, modifiez le fichier `config.h` à l'intérieur de votre répertoire de ferme. Plus précisément, vous devez définir `WHOLE_NODE=1` et la variable `NWHOLE` au nombre de cœurs CPU par nœud (40 pour Niagara; 192 pour Trillium).

En mode WHOLE_NODE, l'argument entier positif de la commande `submit.run` change de signification : au lieu d'être le nombre de méta-jobs, il s'agit maintenant du nombre de nœuds entiers à utiliser en mode META. Par exemple, considérez cette commande :

```bash
$ submit.run 2
```

Si le mode WHOLE_NODE est activé, la commande ci-dessus allouera 2 nœuds entiers, qui seront utilisés pour exécuter jusqu'à 384 tâches sérielles concurrentes (192 tâches par nœud) en utilisant le mode META (équilibrage dynamique de la charge de travail). Ces tâches sont exécutées comme des fils d'exécution distincts au sein des jobs de nœud entier.

L'argument "-1" pour `submit.run` conserve sa signification originale : exécuter la ferme en mode SIMPLE. Le nombre de jobs réels (nœud entier) est calculé comme `Nombre_de_cas / NWHOLE`.

!!! important "Détails importants"
    *   Les fonctionnalités avancées "Resoumission automatique des jobs" et "Job de post-traitement automatique" ne fonctionneront sur Trillium que si vous ajoutez la ligne suivante à la fin de votre fichier `~/.bashrc` :
        ```bash
        module load StdEnv
        ```
    *   Le mode WHOLE_NODE ne peut être utilisé que pour le calcul sériel en ferme. (Autrement dit, il ne peut pas être utilisé pour le calcul multifil, MPI ou GPU en ferme).
    *   Le mode WHOLE_NODE peut également être utilisé sur d'autres clusters (pas seulement sur Trillium). Il peut être avantageux dans les situations où le temps d'attente dans la file d'attente pour les jobs de nœud entier devient plus court que le temps d'attente pour les jobs sériels.

## Information additionnelle

### Utiliser le dépôt Git

Pour utiliser META sur un cluster où il n'est pas installé en tant que module, vous pouvez cloner le paquet depuis notre dépôt Git :

```bash
$ git clone https://git.computecanada.ca/syam/meta-farm.git
```

Modifiez ensuite votre variable `$PATH` pour qu'elle pointe vers le sous-répertoire `bin` du répertoire `meta-farm` nouvellement créé. En supposant que vous ayez exécuté `git clone` dans votre répertoire personnel, faites ceci :

```bash
$ export PATH=~/meta-farm/bin:$PATH
```

Procédez ensuite comme indiqué dans le guide de démarrage rapide de META à partir de l'étape `farm_init.run`.

### Passer des arguments sbatch supplémentaires

Si vous avez besoin d'utiliser des arguments `sbatch` supplémentaires (comme `--mem 4G`, `--gres=gpu:1`, etc.), ajoutez-les à `job_script.sh` en tant que lignes `#SBATCH` distinctes.

Ou si vous préférez, vous pouvez les ajouter à la fin de la commande `submit.run` ou `resubmit.run` et ils seront passés à `sbatch`, par exemple :

```bash
$  submit.run  -1  --mem 4G
```

### Applications multifils

Pour les applications [multifils](running_jobs.md) (telles que celles qui utilisent [OpenMP](https://www.openmp.org/), par exemple), ajoutez les lignes suivantes à `job_script.sh` :

```bash
#SBATCH --cpus-per-task=N
#SBATCH --mem=M
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
```

...où *N* est le nombre de cœurs CPU à utiliser, et *M* est la mémoire totale à réserver en mégaoctets. Vous pouvez également fournir `--cpus-per-task=N` et `--mem=M` comme arguments à `(re)submit.run`.

### Applications MPI

Pour les applications qui utilisent [MPI](https://www.mpi-forum.org/), ajoutez les lignes suivantes à `job_script.sh` :

```bash
#SBATCH --ntasks=N  
#SBATCH --mem-per-cpu=M
```

...où *N* est le nombre de cœurs CPU à utiliser, et *M* est la mémoire à réserver pour chaque cœur, en mégaoctets. Vous pouvez également fournir `--ntasks=N` et `--mem-per-cpu=M` comme arguments à `(re)submit.run`. Consultez [Planification MPI avancée](advanced_mpi_scheduling.md) pour des informations sur des scénarios MPI plus complexes.

Ajoutez également `srun` avant le chemin de votre code à l'intérieur de `single_case.sh`, par exemple :

```bash
srun  $COMM
```

Alternativement, vous pouvez préfixer `srun` à chaque ligne de `table.dat` :

```bash
srun /path/to/mpi_code arg1 arg2
srun /path/to/mpi_code arg1 arg2
...
srun /path/to/mpi_code arg1 arg2
```

### Applications GPU

Pour les applications qui utilisent des GPU, modifiez `job_script.sh` en suivant les instructions de [Utiliser les GPU avec Slurm](using_gpus_with_slurm.md) :

```bash
#SBATCH --gres=gpu[[:type]:number]
```

Vous pouvez également copier l'utilitaire `~syam/bin/gpu_test` dans votre répertoire `~/bin` (uniquement sur Nibi), et insérer les lignes suivantes dans `job_script.sh` juste avant la ligne `task.run` :

```bash
~/bin/gpu_test
retVal=$?
if [ $retVal -ne 0 ]; then
    echo "No GPU found - exiting..."
    exit 1
fi
```

Ceci permettra de détecter les rares situations où il y a un problème avec le nœud qui rend le GPU indisponible. Si cela se produit pour l'un de vos méta-jobs et que vous ne détectez pas la défaillance du GPU d'une manière ou d'une autre, le job tentera (et échouera) d'exécuter tous vos cas de `table.dat`.

### Variables d'environnement et --export

Tous les jobs générés par le paquet META héritent de l'environnement présent lorsque vous exécutez `submit.run` ou `resubmit.run`. Cela inclut tous les modules chargés et les variables d'environnement. META s'appuie sur ce comportement pour son fonctionnement, en utilisant certaines variables d'environnement pour passer des informations entre les scripts. Vous devez faire attention à ne pas briser ce comportement par défaut, ce qui peut arriver si vous utilisez le commutateur `--export`. Si vous devez utiliser `--export` dans votre ferme, assurez-vous que `ALL` est l'un des arguments de cette commande, par exemple `--export=ALL,X=1,Y=2`.

Si vous avez besoin de passer les valeurs de variables d'environnement personnalisées à tous vos jobs de ferme (y compris les jobs resoumis automatiquement et le job de post-traitement s'il y en a un), n'utilisez pas `--export`. Au lieu de cela, définissez les variables sur la ligne de commande comme dans cet exemple :

```bash
$  VAR1=1 VAR2=5 VAR3=3.1416 submit.run ...
```

Ici, `VAR1`, `VAR2`, `VAR3` sont des variables d'environnement personnalisées qui seront transmises à tous les jobs de la ferme.

### Exemple : Fichiers d'entrée numérotés

Supposons que vous ayez une application appelée `fcode`, et que chaque cas doive lire un fichier distinct depuis l'entrée standard – disons `data.X`, où *X* varie de 1 à *N_cases*. Les fichiers d'entrée sont tous stockés dans un répertoire `/home/user/IC`. Assurez-vous que `fcode` est dans votre `$PATH` (par exemple, placez `fcode` dans `~/bin`, et assurez-vous que `/home/$USER/bin` est ajouté à `$PATH` dans `~/.bashrc`), ou utilisez un chemin complet vers `fcode` dans `table.dat`. Créez `table.dat` dans le répertoire META de la ferme comme ceci :

```
fcode < /home/user/IC/data.1
fcode < /home/user/IC/data.2
fcode < /home/user/IC/data.3
...
```

Vous pourriez vouloir utiliser une boucle shell pour créer `table.dat`, par exemple :

```bash
$  for ((i=1; i<=100; i++)); do echo "fcode < /home/user/IC/data.$i"; done >table.dat
```

### Exemple : Le fichier d'entrée doit avoir le même nom

Certaines applications s'attendent à lire des données d'entrée depuis un fichier avec un nom prédéfini et immuable, comme `INPUT` par exemple. Pour gérer cette situation, chaque cas doit s'exécuter dans son propre sous-répertoire, et vous devez créer un fichier d'entrée avec le nom prédéfini dans chaque sous-répertoire. Supposons pour cet exemple que vous ayez préparé les différents fichiers d'entrée pour chaque cas et les ayez stockés dans `/path/to/data.X`, où *X* varie de 1 à *N_cases*. Votre `table.dat` peut ne contenir que le nom de l'application, répété maintes et maintes fois :

```
/path/to/code
/path/to/code
...
```

Ajoutez une ligne à `single_case.sh` qui copie le fichier d'entrée dans le **sous**-répertoire de la ferme pour chaque cas – la première ligne dans l'exemple ci-dessous :

```bash
cp /path/to/data.$ID INPUT
$COMM
STATUS=$?
```

### Accéder à chaque paramètre d'un cas

Les exemples présentés jusqu'à présent supposent que chaque ligne dans la table des cas est une instruction exécutable, commençant soit par le nom du fichier exécutable (quand il est dans votre `$PATH`), soit par le chemin complet vers le fichier exécutable, puis listant les arguments de ligne de commande particuliers à ce cas, ou quelque chose comme ` < input.$ID` si votre code s'attend à lire un fichier d'entrée standard.

Dans le cas le plus général, vous pourriez vouloir accéder à toutes les colonnes de la table individuellement. Cela peut être fait en modifiant `single_case.sh` :

```bash
...
# ++++++++++++  This part can be customized:  ++++++++++++++++
#  $ID contains the case id from the original table
#  $COMM is the line corresponding to the case $ID in the original table, without the ID field
mkdir RUN$ID
cd RUN$ID

# Converting $COMM to an array:
COMM=( $COMM )
# Number of columns in COMM:
Ncol=${#COMM[@]}
# Now one can access the columns individually, as ${COMM[i]} , where i=0...$Ncol-1
# A range of columns can be accessed as ${COMM[@]:i:n} , where i is the first column
# to display, and n is the number of columns to display
# Use the ${COMM[@]:i} syntax to display all the columns starting from the i-th column
# (use for codes with a variable number of command line arguments).

# Call the user code here.
...

# Exit status of the code:
STATUS=$?
cd ..
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
...
```

Par exemple, vous pourriez avoir besoin de fournir à votre code **à la fois** un fichier d'entrée standard **et** un nombre variable d'arguments de ligne de commande. Votre table des cas ressemblera à ceci :

```
/path/to/IC.1 0.1
/path/to/IC.2 0.2 10
...
```

La manière d'implémenter ceci dans `single_case.sh` est la suivante :

```bash
# Call the user code here.
/path/to/code ${COMM[@]:1} < ${COMM[0]}
```

### Réduire le gaspillage

Voici un problème potentiel lorsque l'on exécute plusieurs cas par job : Et si le nombre de méta-jobs en cours multiplié par le temps d'exécution demandé par méta-job (disons, 3 jours) n'est pas suffisant pour traiter tous vos cas ? Par exemple, vous avez réussi à démarrer le maximum autorisé de 1000 méta-jobs, chacun ayant une limite de temps d'exécution de 3 jours. Cela signifie que votre ferme ne peut traiter tous les cas en une seule exécution que si le *temps_d_exécution_moyen_par_cas x N_cas < 1000 x 3j = 3000* jours CPU. Une fois que vos méta-jobs commencent à atteindre la limite de temps d'exécution de 3 jours, ils commenceront à s'arrêter au milieu du traitement de l'un de vos cas. Cela entraînera jusqu'à 1000 calculs de cas interrompus. Ce n'est pas un problème majeur en termes d'achèvement du travail --- `resubmit.run` trouvera tous les cas qui ont échoué ou qui n'ont jamais été exécutés, et les redémarrera automatiquement. Mais cela peut devenir un gaspillage de cycles CPU. En moyenne, vous gaspillerez *0,5 x N_jobs x temps_d_exécution_moyen_par_cas*. Par exemple, si vos cas ont un temps d'exécution moyen d'une heure et que vous avez 1000 méta-jobs en cours, vous gaspillerez environ 500 heures CPU ou environ 20 jours CPU, ce qui n'est pas acceptable.

Heureusement, les scripts que nous fournissons intègrent une certaine intelligence pour atténuer ce problème. Ceci est implémenté dans `task.run` comme suit :

*   Le script mesure le temps d'exécution de chaque cas et ajoute la valeur comme une ligne dans un fichier temporaire `times` créé dans le répertoire `/home/$USER/tmp/$NODE.$PID/`. Ceci est fait par tous les méta-jobs en cours.
*   Une fois les 8 premiers cas calculés, l'un des méta-jobs lira le contenu du fichier `times` et calculera le quantile de 12,5% le plus élevé pour la distribution actuelle des temps d'exécution des cas. Cela servira d'estimation prudente du temps d'exécution de vos cas individuels, *dt_cutoff*. L'estimation actuelle est stockée dans le fichier `dt_cutoff` dans `/home/$USER/tmp/$NODE.$PID/`.
*   À partir de maintenant, chaque méta-job estimera s'il a le temps de terminer le cas qu'il est sur le point de commencer à calculer, en s'assurant que *t_finish - t_now > dt_cutoff*. Ici, *t_finish* est l'heure à laquelle le job s'arrêtera en raison de la limite de temps d'exécution du job, et *t_now* est l'heure actuelle. S'il calcule qu'il n'a pas le temps, il quittera prématurément, ce qui minimisera le risque qu'un cas soit interrompu à mi-chemin en raison de la limite de temps d'exécution du job.
*   À chaque puissance de deux subséquente du nombre de cas calculés (8, puis 16, puis 32 et ainsi de suite), *dt_cutoff* est recalculé en utilisant l'algorithme ci-dessus. Cela rendra l'estimation de *dt_cutoff* de plus en plus précise. Les puissances de deux sont utilisées pour minimiser les surcharges liées au calcul de *dt_cutoff*; l'algorithme sera également efficace pour un nombre de cas très petit (dizaines) et très grand (plusieurs milliers).
*   L'algorithme ci-dessus réduit en moyenne la quantité de cycles CPU gaspillés en raison des jobs atteignant la limite de temps d'exécution d'un facteur de 8.

Comme effet secondaire utile, chaque fois que vous exécutez une ferme, vous obtenez les temps d'exécution individuels pour tous vos cas stockés dans `/home/$USER/tmp/$NODE.$PID/times`. Vous pouvez analyser ce fichier pour affiner la configuration de votre ferme, pour profiler votre code, etc.

## Dépannage

Ici, nous expliquons les messages d'erreur typiques que vous pourriez rencontrer en utilisant ce paquet.

### Problèmes avec des commandes multiples

#### "Non-farm directory, or no farm has been submitted; exiting"

Soit le répertoire actuel n'est pas un répertoire de ferme, soit vous n'avez jamais exécuté `submit.run` pour cette ferme.

### Problèmes avec submit.run

#### "Wrong first argument: XXX (should be a positive integer or -1) ; exiting"

Utilisez le bon premier argument : -1 pour le mode SIMPLE, ou un entier positif N (nombre de méta-jobs demandés) pour le mode META.

#### "lockfile is not on path; exiting"

Assurez-vous que l'utilitaire `lockfile` est dans votre `$PATH`. Cet utilitaire est essentiel pour ce paquet. Il fournit un accès sérialisé des méta-jobs au fichier `table.dat`, c'est-à-dire qu'il garantit que deux méta-jobs différents ne lisent pas la même ligne de `table.dat` en même temps.

#### "Non-farm directory (config.h, job_script.sh, single_case.sh, and/or table.dat are missing); exiting"

Soit le répertoire actuel n'est pas un répertoire de ferme, soit certains fichiers importants sont manquants. Naviguez vers le répertoire correct (de ferme), ou créez les fichiers manquants.

#### "-auto option requires resubmit_script.sh file in the root farm directory; exiting"

Vous avez utilisé l'option `-auto`, mais vous avez oublié de créer le fichier `resubmit_script.sh` dans le répertoire racine de la ferme. Un exemple de `resubmit_script.sh` est créé automatiquement lorsque vous utilisez `farm_init.run`.

#### "File table.dat doesn't exist. Exiting"

Vous avez oublié de créer le fichier `table.dat` dans le répertoire actuel, ou peut-être exécutez-vous `submit.run` en dehors de l'un de vos sous-répertoires de ferme.

#### "Job runtime sbatch argument (-t or --time) is missing in job_script.sh. Exiting"

Assurez-vous de fournir une limite de temps d'exécution pour tous les méta-jobs en tant qu'argument `#SBATCH` à l'intérieur de votre fichier `job_script.sh`. Le temps d'exécution est le seul qui ne peut pas être passé comme argument optionnel à `submit.run`.

#### "Wrong job runtime in job_script.sh - nnn . Exiting"

Vous n'avez pas correctement formaté l'argument de temps d'exécution à l'intérieur de votre fichier `job_script.sh`.

#### "Something wrong with sbatch farm submission; jobid=XXX; aborting"
#### "Something wrong with a auto-resubmit job submission; jobid=XXX; aborting"

Avec l'un ou l'autre de ces deux messages, il y a eu un problème lors de la soumission des jobs avec `sbatch`. Le planificateur du cluster pourrait mal fonctionner, ou simplement être trop occupé. Réessayez un peu plus tard.

#### "Couldn't create subdirectories inside the farm directory ; exiting"
#### "Couldn't create the temp directory XXX ; exiting"
#### "Couldn't create a file inside XXX ; exiting"

Avec l'un de ces trois messages, il y a un problème avec le système de fichiers : Soit les permissions ont été altérées, soit vous avez épuisé un quota. Résolvez le(s) problème(s), puis réessayez.

### Problèmes avec resubmit.run

#### "Jobs are still running/queued; cannot resubmit"

Vous ne pouvez pas utiliser `resubmit.run` tant que tous les méta-jobs de cette ferme n'ont pas terminé leur exécution. Utilisez `list.run` ou `queue.run` pour vérifier l'état de la ferme.

#### "No failed/unfinished jobs; nothing to resubmit"

Votre ferme a été traitée à 100 %. Il n'y a plus de cas (échoués ou non exécutés) à calculer.

### Problèmes avec les jobs en cours

#### "Too many failed (very short) cases - exiting"

Cela se produit si les premiers cas `$N_failed_max` sont très courts – moins de `$dt_failed` secondes de durée. Déterminez ce qui cause l'échec des cas et corrigez-le, ou ajustez les valeurs `$N_failed_max` et `$dt_failed` dans `config.h`.

#### "lockfile is not on path on node XXX"

Comme le suggère le message d'erreur, l'utilitaire `lockfile` ne se trouve pas dans votre `$PATH` sur un certain nœud. Utilisez `which lockfile` pour vous assurer que l'utilitaire est quelque part dans votre `$PATH`. S'il est dans votre `$PATH` sur un nœud de connexion, alors quelque chose s'est mal passé sur ce nœud de calcul particulier, par exemple un système de fichiers pourrait avoir échoué à se monter.

#### "Exiting after processing one case (-1 option)"

Ce n'est pas un message d'erreur. Il vous indique simplement que vous avez soumis la ferme avec `submit.run -1` (mode un cas par job), donc chaque méta-job se termine après avoir traité un seul cas.

#### "Not enough runtime left; exiting."

Ce message vous indique que le méta-job n'aurait probablement pas assez de temps pour traiter le cas suivant (basé sur l'analyse des temps d'exécution de tous les cas traités jusqu'à présent), il se termine donc prématurément.

#### "No cases left; exiting."

Ce n'est pas un message d'erreur. C'est ainsi que chaque méta-job se termine normalement, lorsque tous les cas ont été calculés.

#### "Only failed cases left; cannot auto-resubmit; exiting"

Cela ne peut se produire que si vous avez utilisé le commutateur `-auto` lors de la soumission de la ferme. Trouvez les cas échoués avec `Status.run -f`, corrigez le(s) problème(s) causant l'échec des cas, puis exécutez `resubmit.run`.

Page enfant de META : Un paquet pour la gestion de jobs en grappe