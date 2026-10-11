---
title: "Abaqus/fr"
slug: "abaqus"
lang: "fr"

source_wiki_title: "Abaqus/fr"
source_hash: "d5b0180311df0d8da57b5c9141085cfc"
last_synced: "2026-10-11T01:39:35.690021+00:00"
last_processed: "2026-10-11T02:21:18.258744+00:00"

tags:
  - software

keywords:
  - "SLURM_SUBMIT_DIR"
  - "licence Western"
  - "mpi mode"
  - "jetons dédiés"
  - "#SBATCH --constraint=granite"
  - "serveur DSLS"
  - "%CPU and %MEM"
  - "serveur de licences Abaqus"
  - "DSLicSrv.txt"
  - "abaqus job=testet2"
  - "TOKENS = floor[5 X CORES^0.422]"
  - "license_server_type=DSLS"
  - "Open OnDemand"
  - "abaqus/2026"
  - "module load"
  - "script pour nœuds multiples"
  - "abaqus.lic"
  - "#SBATCH --account=def-group"
  - "utilisation du disque de travail"
  - "valeur estimée"
  - "commandes ps ou top"
  - "lmhanglimit"
  - "Abaqus cae -mesa"
  - "correspondance cœur-jeton"
  - "script du répertoire /project"
  - "module load abaqus/2026"
  - "memory"
  - "SBATCH --mem"
  - "systèmes SHARCNET"
  - "licence Abaqus"
  - "module load abaqus"
  - "mem-per-cpu"
  - "demande d'accès"
  - "script pour le répertoire temporaire"
  - "RESTART WRITE OVERLAY"
  - "lmstat"
  - "tâche en attente"
  - "FlexLM ports"
  - "JupyterLab"
  - "SLURM_CPUS_ON_NODE"
  - "licence SHARCNET"
  - "#SBATCH --mem=8G"
  - "abaqus/2026 module"
  - "srun --overlap"
  - "cœurs"
  - "FLEXnet"
  - "abaqus_v6.env"
  - "SHARCNET"
  - "mp_mode=threads"
  - "mémoire RES"
  - "SLURM"
  - "redémarrage de l'analyse"
  - "mémoire réelle"
  - "unshare"
  - "abaqus"
  - "ABAQUS"
  - "RES resident memory"
  - "scripts du répertoire /project"
  - "efficacité mémoire CPU"
  - "analyse explicite"
  - "espace /scratch du disque"
  - "abaqus -help"
  - "LM_LICENSE_FILE"
  - "processus avec fils"
  - "licences CAE"
  - "mp_host_split"
  - "cpus-per-task"
  - "licence FLEXnet"
  - "Abaqus SHARCNET licence"
  - "redémarrage de tâche"
  - "jetons de calcul"
  - "#SBATCH --cpus-per-task"
  - "#SBATCH --gpus-per-node=h100:1"
  - "tâche de longue durée"
  - "notification par courriel Slurm"
  - "minimiser les entrées/sorties"
  - "monitor jobs"
  - "#SBATCH --nodes=1"
  - "lmhanglimit=1"
  - "fichier en entrée"
  - "scripts MPI"
  - "mémoire totale"
  - "#SBATCH --mem=8000M"
  - "module Abaqus"
  - "serveur de licence DSLS"
  - "jetons"
  - "#!/bin/bash"
  - "fichier abaqus.lic"
  - "SLURM_TMPDIR"
  - "argument memory="
  - "grappe Dusky"
  - "tâches gourmandes en mémoire"
  - "ordonnanceur"
  - "nom d'utilisateur"
  - "MRMIO"
  - "RESTART"
  - "estimation de la mémoire"
  - "script de redémarrage"
  - "allocation sur un nœud"
  - "EBVERSIONABAQUS"
  - "SBATCH"
  - "#SBATCH --cpus-per-task=4"
  - "nœud de calcul"
  - "accord de licence"
  - "lmlicensequeuing=OFF"
  - "#SBATCH --time=00-06:00"
  - "mem=8000M"
  - "scratch"
  - "Abaqus"

questions:
  - "Quels sont les deux types de serveurs de licences pris en charge par Abaqus sur les clusters et quelles sont les étapes de configuration propres à chaque type ?"
  - "Comment créer et configurer le fichier `abaqus.lic` (ou `abaqus_v6.env` et `DSLicSrv.txt` pour DSLS) afin d’utiliser un serveur de licences FLEXnet ?"
  - "Quelle commande permet de vérifier le nombre de licences CAE disponibles et comment interpréter les informations affichées concernant les licences émises, en cours d’utilisation et réservées ?"
  - "Quel serveur de licence est utilisé par défaut avec Abaqus selon le texte ?"
  - "Quels fichiers texte doivent être créés pour configurer un serveur de licence DSLS de votre établissement ?"
  - "Dans quel répertoire ces fichiers doivent-ils être placés afin d’être lus automatiquement au lancement d’Abaqus ?"
  - "Quels paramètres doit‑on ajouter dans le fichier `abaqus_v6.env` pour désactiver la mise en file d’attente des licences ou définir une limite d’attente, et comment ces réglages influencent le comportement des jobs sous Slurm ?"
  - "Comment configurer correctement le serveur de licences Abaqus (DSLS) afin qu’il soit joignable depuis tous les nœuds de calcul, notamment quelles informations fournir au support technique pour ouvrir les pare‑feux nécessaires ?"
  - "Quelle est la procédure recommandée pour charger le module `abaqus/2026` et vérifier son installation, et pourquoi l’utilisation du module `abaqus/2021` est‑elle déconseillée sur les clusters récents ?"
  - "Quels sont les critères pour choisir entre le script du répertoire /project et un script de redémarrage selon la durée de la tâche ?"
  - "Pourquoi recommande‑t‑on d’utiliser la variable d’environnement SLURM_TMPDIR pour les fichiers de redémarrage volumineux ?"
  - "Comment déterminer le nombre optimal de cœurs et la durée réelle d’exécution avant de lancer des tâches de longue durée sur plusieurs nœuds ?"
  - "Quel rôle joue l’argument <code>memory=</code> dans les scripts du répertoire /project et quand doit‑il être ajusté ?"
  - "Où se trouvent les scripts à utiliser pour configurer une tâche sur un nœud simple ?"
  - "Comment obtenir la liste complète des arguments en ligne de commande d’Abaqus ?"
  - "What is the purpose of the `rm -f testsp1* testsp2*` command at the beginning of the script?"
  - "Why does the script check whether `EBVERSIONABAQUS` equals 2021 before running the `unshare` command?"
  - "Which resources (e.g., scratch directory, CPU count, memory) and optional settings (such as GPU usage) are being specified for the Abaqus job in the `unshare` command?"
  - "Quels paramètres doivent être inclus dans le fichier d'entrée pour écrire les données de redémarrage toutes les N = 12 incréments ou pour un total de 12 incréments ?"
  - "Comment le script différencie‑t‑il les commandes Abaqus selon la version (2021 vs ≥ 2026) et quels modules doivent être chargés pour chaque version ?"
  - "Quelles directives SLURM et quelles options de mémoire, CPU et GPU doivent être spécifiées dans le script pour exécuter correctement un job Abaqus avec redémarrage ?"
  - "What does the `#SBATCH --mem=8G` directive specify for the job’s resource allocation?"
  - "How can you request a specific GPU type and quantity using the `#SBATCH --gpus-per-node` option?"
  - "Which Abaqus module version should be loaded for the latest features, and why might older versions be discouraged?"
  - "Quel est le but du test conditionnel sur la variable $EBVERSIONABAQUS et comment les commandes diffèrent‑elles entre les versions 2021 et ≥ 2026 d’Abaqus ?"
  - "Comment le script assure‑t‑il la sauvegarde périodique des fichiers de simulation (testst2*) pendant l’exécution et quel mécanisme utilise‑t‑il pour gérer le temps limite du job ?"
  - "Quelle syntaxe doit‑on utiliser dans le fichier d’entrée Abaqus pour écrire les données de redémarrage soit par fréquence d’incréments (FREQUENCY=12) soit par nombre total d’incréments (NUMBER INTERVAL=12) ?"
  - "What is the purpose of using `unshare` with the specified options in this Abaqus job submission script?"
  - "How does the script determine whether to execute the Abaqus command based on the `$EBVERSIONABAQUS` variable?"
  - "Which SLURM environment variables are referenced in the Abaqus command, and what role does each play in the job execution?"
  - "Quels paramètres SLURM doivent être configurés pour lancer un job Abaqus en mode MPI sur plusieurs nœuds ?"
  - "Comment le fichier d’entrée doit‑il être structuré pour permettre le redémarrage d’une simulation Abaqus (ex. présence de *HEADING, *RESTART, READ) ?"
  - "Quelles sont les principales différences entre les scripts proposés pour le calcul sur un nœud simple et ceux destinés à un calcul sur plusieurs nœuds ?"
  - "Quel rôle joue la variable $EBVERSIONABAQUS dans la sélection des commandes d’exécution ou de récupération d’Abaqus ?"
  - "Comment le script calcule‑t‑il la quantité de mémoire à allouer à Abaqus à partir de la mémoire totale du nœud SLURM ?"
  - "Quelles sont les étapes de copie et de préparation des fichiers de redémarrage avant d’exécuter le script scriptep2.txt ?"
  - "Quel est l’objectif principal du script contenu dans le fichier scriptep1.txt ?"
  - "Quels paramètres de ressources (compte, temps, mémoire, CPU) sont définis par les directives #SBATCH dans ce script ?"
  - "Comment peut‑on ajuster le script pour modifier la limite de temps ou la quantité de mémoire allouée ?"
  - "Quel est l’objectif du script présenté dans le texte ?"
  - "Quelles ressources (temps, mémoire, compte) sont spécifiées par les directives SBATCH du script ?"
  - "Pourquoi le texte indique‑t‑il que le fichier d’entrée ne nécessite aucune modification pour redémarrer l’analyse ?"
  - "Quels modules doivent être chargés et quelles versions d’Abaqus sont recommandées ou à éviter dans le script ?"
  - "Comment le script assure‑t‑il la synchronisation périodique des fichiers entre le répertoire temporaire SLURM et le répertoire de soumission ?"
  - "Quelles différences de configuration (par ex. utilisation d’`unshare`, paramètres de mémoire et de CPU) le script applique‑t‑il selon que la version d’Abaqus est 2021 ou ≥ 2026 ?"
  - "What is the purpose of using the `unshare` command with the specified options before launching the Abaqus job?"
  - "How are the SLURM environment variables (e.g., `SLURM_SUBMIT_DIR`, `SLURM_TMPDIR`, `SLURM_CPUS_ON_NODE`, `SLURM_MEM_PER_NODE`) utilized to configure the Abaqus simulation parameters?"
  - "Why does the script subtract 3072 MB from `SLURM_MEM_PER_NODE` when setting the memory limit for the Abaqus run?"
  - "Quels sont les prérequis de version d’Abaqus pour pouvoir exécuter le script de calcul sur plusieurs nœuds avec MPI ?"
  - "Comment le script génère‑t‑il la variable `hostlist` (liste des hôtes) utilisée pour la configuration MPI ?"
  - "Quelle méthode est recommandée pour estimer la mémoire totale nécessaire à une simulation Abaqus sur un nœud unique ?"
  - "Quelle méthode est proposée pour estimer la mémoire totale d’un processus avec fils sur un nœud unique ?"
  - "Quels outils (commandes) sont recommandés pour surveiller la consommation de mémoire pendant la simulation ?"
  - "Quelle est la procédure à suivre pour se connecter à la grappe, obtenir une allocation sur un nœud de calcul et démarrer la simulation ?"
  - "Comment déterminer la quantité de mémoire à allouer avec l’option `-mem=` afin de satisfaire la valeur recommandée MRMIO sans provoquer d’erreur OOM dans Abaqus ?"
  - "Quelle méthode est proposée pour estimer la valeur `mem-per-cpu` dans un script Slurm multinœuds, en fonction de `mp_host_split`, du nombre de nœuds et du nombre de tâches ?"
  - "Pourquoi recommande‑t‑on d’observer les colonnes VIRT et RES avec la commande `top` après le lancement d’une tâche Abaqus, et comment ces mesures influencent le réglage de la mémoire allouée ?"
  - "Quels sont les prérequis et les étapes pour lancer Abaqus en mode graphique via Open OnDemand, notamment le chargement du module, le choix de l’option ‑mesa ou non, et la vérification de la disponibilité d’une licence ?"
  - "Comment démarrer COMSOL en mode graphique à l’aide de JupyterLab, depuis la connexion à JupyterHub jusqu’au chargement du module et à l’ouverture de l’icône VNC ?"
  - "Quelles sont les conditions d’utilisation, les limites de jetons et la procédure d’obtention d’accès à la licence SHARCNET (licence gratuite et jetons dédiés) via le soutien technique ?"
  - "Quelle est la relation entre l'utilisation réelle de la mémoire et la valeur estimée de <CODE>MEMORY TO MINIMIZE I/O</CODE> lorsqu'on cherche à minimiser les entrées/sorties ?"
  - "Que se passe-t-il pour l'utilisation de la mémoire et du disque /scratch lorsque la mémoire réelle approche de la limite mentionnée plutôt que de la valeur estimée ?"
  - "Pourquoi le texte indique‑t‑il qu'il est impossible d'évaluer avec précision l'espace /scratch du disque ?"
  - "Quelle procédure doit‑on suivre dans le courriel pour demander l’accès au soutien technique sur les systèmes SHARCNET ?"
  - "Quels éléments (accord de licence, nom, prénom, nom d’utilisateur) doivent être inclus dans le courriel ?"
  - "Pourquoi chaque utilisateur, y compris les chercheur·e·s principaux·es disposant de leurs propres jetons, doit‑il effectuer cette démarche individuellement ?"
  - "Quelles sont les conditions d’utilisation du logiciel « SIMULIA Academic Software » stipulées dans l’accord de licence académique SHARCNET ?"
  - "Comment faut‑il modifier le fichier abaqus.lic pour exploiter la licence SHARCNET gratuite, notamment en fonction de la version d’Abaqus (ex. 202X vs 6.14.1) ?"
  - "Quelles commandes permettent d’interroger le serveur de licences SHARCNET et comment interpréter les informations affichées (tâches en cours, file d’attente, réservations, disponibilité des produits) ?"
  - "Quels sont les deux mécanismes proposés pour éviter que des jobs Abaqus ne restent bloqués faute de licences, et quelles sont leurs différences de fonctionnement ?"
  - "Comment optimiser la consommation de mémoire et de CPU d’un job Abaqus en ajustant les paramètres « #SBATCH » selon les indicateurs d’efficacité présentés ?"
  - "Quelle commande permet de suivre en temps réel l’utilisation du %CPU, %MEM et de la mémoire résidente d’un job Abaqus en cours d’exécution sur le nœud de calcul ?"
  - "Pourquoi la première tâche a‑t‑elle pu démarrer avec exactement 10 jetons alors qu’elle nécessite 12 jetons au total ?"
  - "Quel impact la mise en attente de la seconde tâche a‑t‑elle sur l’utilisation des ressources disponibles et sur la part équitable de l’utilisateur ?"
  - "Sur quels critères l’ordonnanceur se base‑t‑il pour lancer les tâches dans l’ordre de leur soumission et attribuer les jetons ?"
  - "How can you determine the optimal number of CPUs per task before updating the `<code>#SBATCH --cpus-per-task=</code>` directive in your Slurm script?"
  - "Which `srun` command should be used to monitor the %CPU, %MEM, and RES usage of Abaqus parent processes on a compute node?"
  - "What do the %CPU, %MEM, and RES columns indicate in the monitoring output?"
  - "Comment calcule‑t‑on le nombre de jetons requis en fonction du nombre de cœurs, et quelle règle s’applique aux GPU ?"
  - "Qui peut bénéficier de la licence Western, sur quels systèmes elle est autorisée, et comment demander l’accès ou l’achat de jetons ?"
  - "Quelle procédure faut‑il suivre pour configurer le fichier abaqus.lic, soumettre une tâche sur le cluster Dusky, et signaler un problème au support technique ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# Abaqus/fr

Abaqus FEA est un progiciel commercial pour l'analyse par éléments finis et l'ingénierie assistée par ordinateur.

# Licence

Les modules logiciels Abaqus sont disponibles sur les grappes de l'Alliance, mais vous devez fournir votre propre licence. Il existe deux types de serveurs de licences, chacun avec des procédures de configuration différentes décrites ci-dessous.

## Serveurs FLEXnet

Des modules Abaqus sont disponibles sur nos grappes, mais vous devez posséder votre propre licence. Pour configurer votre compte sur les grappes que vous voulez utiliser, connectez-vous et créez sur chacune un fichier `~/.licenses/abaqus.lic` qui contient la ligne ci-dessous. Remplacez ensuite `port@server` par le numéro du port FlexLM et l'adresse IP (ou le nom complet du domaine) de votre serveur de licence Abaqus. Si vous voulez utiliser la version 6.14.1, remplacez `ABAQUSLM_LICENSE_FILE` par `LM_LICENSE_FILE`.

```ini title="abaqus.lic"
prepend_path("ABAQUSLM_LICENSE_FILE","port@server")
```

```bash
[l2 (login node):~ ] cat abaqus_v6.env
license_server_type = FLEXNET
```

```bash
[l2 (login node):~/.licenses] cat abaqus.lic
prepend_path("ABAQUSLM_LICENSE_FILE","LMGRD-PORT-NUMBER@FLEXnet-SERVER-HOSTNAME")
```

```bash
rm -f testsp1* testsp2*
/cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/unshare \
   --fork --pid --mount-proc --user --map-user $USER \
   abaqus job=testsp1 input=mystd-sim.inp \
   scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
   mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB" \
#  gpus=$SLURM_GPUS_ON_NODE  # décommenter cette ligne pour utiliser le GPU
```

```bash
[l2 (login node):~]$ module load abaqus
[l2 (login node):~]$ abaqus licensing ru | grep ABAQUSLM:
  ABAQUSLM: UP v11.19.6.   <-- indique le succès
```

Pour vérifier le nombre de licences CAE disponibles pour une utilisation immédiate par n'importe qui (la différence entre les licences « émises » et « en cours d'utilisation »), exécutez la commande suivante. Notez que les licences réservées apparaîtront toujours comme « en cours d'utilisation », qu'elles le soient ou non par le groupe auquel elles sont réservées. Dans le cas de la licence SHARCNET, il y a 4 licences CAE, mais seulement 1 est réservée, ce qui laisse 3 licences dans le bassin disponibles pour n'importe qui afin d'exécuter Abaqus en mode GUI sur le système graphique On-Demand de la grappe Nibi. L'exemple suivant montre qu'au moment où la commande a été exécutée, aucune des 3 licences CAE du bassin n'était disponible pour qu'un groupe puisse exécuter Abaqus en mode GUI sur le système graphique On-Demand de la grappe Nibi.

```bash
[l2 (login node):~]$ abaqus licensing ru | grep cae
 Users of cae:  (Total of 4 licenses issued;  Total of 1 license in use)
 "cae" v62.7, vendor: ABAQUSLM, expiry: 17-jan-2027
```

Pour un sommaire de TOUTES les licences fournies par un serveur de licences :

```bash
[l2 (login node):~]$ module load abaqus
[l2 (login node):~]$ abaqus licensing r
Feature                         Version     #licenses    Vendor        Expires
_______                         _________   _________    ______        ________
abaqus_extended                 62.7         4           ABAQUSLM      17-jan-2027
abaqus                          62.7         78          ABAQUSLM      17-jan-2027
ams                             62.7         1           ABAQUSLM      17-jan-2027
etc etc etc
```

## Serveurs DSLS

Comme c'était le cas avec les modules déjà installés, `abaqus/2026` est configuré pour fonctionner avec le serveur de licence Simulia `FLEXnet` par défaut, tout comme le serveur de licence gratuit de SHARCNET. Pour utiliser un serveur de licence `DSLS` de votre établissement, vous devez créer les fichiers texte `abaqus_v6.env` et `DSLicSrv.txt` dans le répertoire utilisé pour soumettre votre simulation (voir le code ci-dessous). Ils seront lus automatiquement au lancement d'Abaqus et la reconfiguration se fera en conséquence.

```bash
[l2 (login node):~ ] cat abaqus_v6.env
license_server_type=DSLS
```

```bash
[l2 (login node):~/.licenses] cat abaqus.lic
prepend_path("DSLS_LICENSE_FILE","LICENSING-CLIENT-PORT-NUMBER@DSLS-SERVER-HOSTNAME")
```

```bash
[l2 (login node):~/mysimdir] cat abaqus_v6.env
license_server_type=DSLS
dsls_license_config="DSLicSrv.txt"
```

```bash
[l2 (login node):~/mysimdir] cat DSLicSrv.txt
YOUR-SERVER-HOSTNAME:PORT-NUMBER
```

## Nouveaux serveurs

Si votre licence n'est pas configurée pour une grappe en particulier, les administrateurs de systèmes des deux parties devront effectuer certaines modifications. Ceci est nécessaire pour que les ports FlexLM et TCP de votre serveur Abaqus puissent être rejoints par tous les nœuds de calcul quand vos tâches dans la file d'attente seront exécutées. Pour que nous puissions vous assister dans cette tâche, écrivez au [soutien technique](../support/technical_support.md) en indiquant :

*   le numéro du port FlexLM
*   le numéro du port statique
*   l'adresse IP de votre serveur de licence Abaqus.

En retour, vous recevrez une liste d'adresses IP et votre administrateur de système pourra ouvrir les pare-feu de votre serveur local pour que la grappe puisse se connecter via les deux ports. Une entente spéciale doit habituellement être négociée et signée avec SIMULIA pour qu'une telle licence puisse être utilisée à distance avec notre matériel.

## Gestion des files d'attente de licences

La configuration par défaut du serveur de licences est de mettre en file d'attente les tâches démarrées sur la grappe par Slurm si un nombre suffisant de jetons n'est pas disponible. Il existe deux options pour modifier ce comportement afin que les tâches ne restent pas inactives sur un nœud de calcul de la grappe, attendant une licence indéfiniment et gaspillant de précieuses ressources. La première option est de terminer une tâche immédiatement si un nombre suffisant de licences n'est pas disponible, ne lui permettant ainsi jamais d'entrer dans une file d'attente. Pour spécifier ce réglage, créez un fichier texte nommé `abaqus_v6.env` dans votre répertoire `/home` OU votre répertoire de travail (soumission) contenant la ligne : `lmlicensequeuing=OFF`. La deuxième option est de spécifier un temps d'attente fini pendant lequel la tâche peut entrer dans un état de file d'attente sur le serveur de licences, par exemple 1 minute, en ajoutant la ligne : `lmhanglimit=1`. Si dans les 1 minute, un nombre suffisant de licences ne devient pas disponible, la tâche sera retirée de la file d'attente par le serveur de licences et à son tour terminée par Slurm. Pour chaque option, des messages seront imprimés à la fin du fichier de sortie Slurm, comme illustré dans la section [Exemple](#exemple).

# Compatibilité des versions

## 2026

Un nouveau module `abaqus/2026` contenant la version initiale *Abaqus 2026 Golden/GA* a été installé dans l'environnement par défaut StdEnv/2023. Un autre module nommé `abaqus/2026.2614` contenant les derniers packs de correctifs SIMULIA Established Products 2026 actuellement au niveau FD02 (FP.2614) sera mis à disposition dès que possible. Pour vérifier votre configuration, exécutez ce qui suit :

```bash
module load abaqus/2026
module load intel/2024
abaqus verify -all
```

## 2021

Il est recommandé d'interrompre l'utilisation d'`abaqus/2021` installé sous l'ancien StdEnv/2020 car cette version héritée génère une erreur `*** buffer overflow detected ***` sur toutes les grappes récentes. Une solution de contournement `unshare` précédemment incluse dans les scripts Slurm à nœud unique de ce wiki a maintenant été supprimée.

# Soumettre des tâches en lots

Vous trouverez ci-dessous des prototypes de scripts Slurm pour soumettre des simulations parallèles sur un ou plusieurs nœuds de calcul en utilisant des fils et MPI. Dans la plupart des cas, il suffira d'utiliser un des **scripts du répertoire /project** dans une des sections pour un nœud simple. Dans la dernière ligne des scripts, l'argument `memory=` est optionnel et sert aux tâches qui demandent beaucoup de mémoire ou qui posent problème; la valeur de déplacement de 3072Mo pourrait nécessiter un ajustement. Pour obtenir la liste des arguments en ligne de commande, chargez un module Abaqus et lancez `abaqus -help | less`.

Pour une tâche sur un nœud simple d'une durée de moins de 24 heures, le *script du répertoire /project* sous le premier onglet devrait suffire. Pour une tâche de plus longue durée, utilisez un script de redémarrage.

Il est préférable que les tâches qui créent des fichiers de redémarrage volumineux écrivent sur le disque local via l'utilisation de la variable d'environnement `SLURM_TMPDIR` utilisée dans les **scripts de répertoire temporaire** sous les deux onglets les plus à droite des sections d'analyse standard et explicite à nœud unique. Les scripts de redémarrage présentés ici poursuivront les tâches qui ont été interrompues prématurément pour une quelconque raison. De telles interruptions peuvent se produire si une tâche atteint son temps d'exécution maximal demandé avant de se terminer et est arrêtée par la file d'attente ou si le nœud de calcul sur lequel la tâche était exécutée a planté en raison d'une défaillance matérielle inattendue. D'autres types de redémarrage sont possibles en modifiant davantage le fichier d'entrée (non montré) pour continuer une tâche avec des étapes supplémentaires ou modifier l'analyse (consultez la documentation pour plus de détails sur la version).

Les tâches qui exigent beaucoup de mémoire ou beaucoup de ressources de calcul (plus que la capacité d'un nœud simple) devraient utiliser les scripts MPI dans les sections pour nœuds multiples afin de distribuer le calcul sur un ensemble de nœuds arbitraires déterminé automatiquement par l'ordonnanceur. Avant de lancer des tâches de longue durée, il est recommandé d'exécuter de courts tests présentant peu de scalabilité pour déterminer la durée réelle d'exécution (et les exigences en mémoire) en fonction du nombre optimal de cœurs (2, 4, 8, etc.).

## Analyse standard

Les solveurs prennent en charge la parallélisation avec fils et avec MPI. Des scripts pour chaque mode sont présentés sous les onglets pour l'utilisation d'un nœud simple et celle de nœuds multiples. Des scripts pour redémarrer une tâche qui utilise des nœuds multiples ne sont pas présentés pour l'instant.

### Scripts pour un nœud simple

::: tabs

    ::: tab Script pour le répertoire /project

    ```sh title="scriptsp1.txt"
    #!/bin/bash
    #SBATCH --account=def-group     # Indiquer le compte
    #SBATCH --time=00-06:00         # Indiquer jours-heures:minutes
    #SBATCH --cpus-per-task=4       # Indiquer le nombre de cœurs
    #SBATCH --mem=8G                # Indiquer la mémoire totale > 5G
    #SBATCH --nodes=1               # Ne pas modifier !
    ##SBATCH --constraint=granite   # Décommenter pour spécifier un type de nœud
    ##SBATCH --gpus-per-node=h100:1 # Décommenter pour spécifier [type:]nombre

    module load abaqus/2026         # Dernière version
    #module load StdEnv/2020        # Version héritée
    #module load abaqus/2021        # Ne plus utiliser

    unset SLURM_GTIDS
    export MPI_IC_ORDER='tcp'
    echo "LM_LICENSE_FILE=$LM_LICENSE_FILE"
    echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"

    rm -f testsp1* testsp2*

    if [[ $EBVERSIONABAQUS -eq 2021 ]]; then
       /cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/unshare \
       --fork --pid --mount-proc --user --map-user $USER \
       abaqus job=testsp1 input=mystd-sim.inp \
       scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
       mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB" \
       #gpus=$SLURM_GPUS_ON_NODE  # décommenter cette ligne pour utiliser le GPU
    elif [[ $EBVERSIONABAQUS -ge 2026 ]]; then
       abaqus job=testsp1 input=mystd-sim.inp \
       scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
       mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB" \
       #gpus=$SLURM_GPUS_ON_NODE  # décommenter cette ligne pour utiliser le GPU
    fi
    ```

    Pour écrire les données de redémarrage en incréments de N=12, le fichier en entrée doit contenir :
    `*RESTART, WRITE, OVERLAY, FREQUENCY=12`
    Pour écrire les données de redémarrage pour un total de 12 incréments, entrez plutôt :
    `*RESTART, WRITE, OVERLAY, NUMBER INTERVAL=12, TIME MARKS=NO`
    Pour vérifier l'information complète sur le redémarrage :
    `egrep -i "step|start" testsp*.com testsp*.msg testsp*.sta`
    Certaines simulations peuvent être améliorées en ajoutant au bas du script la commande Abaqus :
    `order_parallel=OFF`

    ::: tab Script de redémarrage pour le répertoire /project

    ```sh title="scriptsp2.txt"
    #!/bin/bash
    #SBATCH --account=def-group     # Indiquer le compte
    #SBATCH --time=00-06:00         # Indiquer jours-heures:minutes
    #SBATCH --cpus-per-task=4       # Indiquer le nombre de cœurs
    #SBATCH --mem=8G                # Indiquer la mémoire totale > 5G
    #SBATCH --nodes=1               # Ne pas modifier !
    ##SBATCH --constraint=granite   # Décommenter pour spécifier un type de nœud
    ##SBATCH --gpus-per-node=h100:1 # Décommenter pour spécifier [type:]nombre

    module load abaqus/2026         # Dernière version
    #module load StdEnv/2020        # Version héritée
    #module load abaqus/2021        # Ne plus utiliser

    unset SLURM_GTIDS
    export MPI_IC_ORDER='tcp'
    echo "LM_LICENSE_FILE=$LM_LICENSE_FILE"
    echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"

    rm -f testsp2* testsp1.lck

    if [[ $EBVERSIONABAQUS -eq 2021 ]]; then
       /cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/unshare \
       --fork --pid --mount-proc --user --map-user $USER \
       abaqus job=testsp2 oldjob=testsp1 input=mystd-sim-restart.inp \
       scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
       mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB" \
       #gpus=$SLURM_GPUS_ON_NODE  # décommenter cette ligne pour utiliser le GPU
    elif [[ $EBVERSIONABAQUS -ge 2026 ]]; then
       abaqus job=testsp2 oldjob=testsp1 input=mystd-sim-restart.inp \
       scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
       mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB" \
       #gpus=$SLURM_GPUS_ON_NODE  # décommenter cette ligne pour utiliser le GPU
    fi
    ```

    Le fichier en entrée pour le redémarrage doit contenir :
    `*HEADING`
    `*RESTART, READ`

    ::: tab Script pour répertoire temporaire

    ```sh title="scriptst1.txt"
    #!/bin/bash
    #SBATCH --account=def-group     # Indiquer le compte
    #SBATCH --time=00-06:00         # Indiquer jours-heures:minutes
    #SBATCH --cpus-per-task=4       # Indiquer le nombre de cœurs
    #SBATCH --mem=8G                # Indiquer la mémoire totale > 5G
    #SBATCH --nodes=1               # Ne pas modifier !
    ##SBATCH --constraint=granite   # Décommenter pour spécifier un type de nœud
    ##SBATCH --gpus-per-node=h100:1 # Décommenter pour spécifier [type:]nombre


    module load abaqus/2026         # Dernière version
    #module load StdEnv/2020        # Version héritée
    #module load abaqus/2021        # Ne plus utiliser

    unset SLURM_GTIDS
    export MPI_IC_ORDER='tcp'
    echo "LM_LICENSE_FILE=$LM_LICENSE_FILE"
    echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"
    echo "SLURM_SUBMIT_DIR =" $SLURM_SUBMIT_DIR
    echo "SLURM_TMPDIR = " $SLURM_TMPDIR

    rm -f testst1* testst2*

    if [[ $EBVERSIONABAQUS -eq 2021 ]]; then
       /cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/unshare \
       --fork --pid --mount-proc --user --map-user $USER \
       abaqus job=testst1 input=$SLURM_SUBMIT_DIR/mystd-sim.inp \
       scratch=$SLURM_TMPDIR/scratch cpus=$SLURM_CPUS_ON_NODE interactive \
       mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB" \
       #gpus=$SLURM_GPUS_ON_NODE  # décommenter cette ligne pour utiliser le GPU
    elif [[ $EBVERSIONABAQUS -ge 2026 ]]; then
       abaqus job=testst1 input=$SLURM_SUBMIT_DIR/mystd-sim.inp \
       scratch=$SLURM_TMPDIR/scratch cpus=$SLURM_CPUS_ON_NODE interactive \
       mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB" \
       #gpus=$SLURM_GPUS_ON_NODE  # décommenter cette ligne pour utiliser le GPU
    fi

    { kill $WPID && wait $WPID; } 2>/dev/null
    cp -fv * $SLURM_SUBMIT_DIR
    ```

    Pour écrire les données de redémarrage en incréments de N=12, le fichier en entrée doit contenir :
    `*RESTART, WRITE, OVERLAY, FREQUENCY=12`
    Pour écrire les données de redémarrage pour un total de 12 incréments, entrez plutôt :
    `*RESTART, WRITE, OVERLAY, NUMBER INTERVAL=12, TIME MARKS=NO`
    Pour vérifier l'information complète sur le redémarrage :
    `egrep -i "step|start" testst*.com testst*.msg testst*.sta`

    ::: tab Script de redémarrage pour le répertoire temporaire

    ```sh title="scriptst2.txt"
    #!/bin/bash
    #SBATCH --account=def-group    # Indiquer le compte
    #SBATCH --time=00-06:00        # Indiquer jours-heures:minutes
    #SBATCH --cpus-per-task=4      # Indiquer le nombre de cœurs
    #SBATCH --mem=8G               # Indiquer la mémoire totale > 5G
    #SBATCH --nodes=1              # Ne pas modifier !
    ##SBATCH --constraint=granite   # Décommenter pour spécifier un type de nœud
    ##SBATCH --gpus-per-node=h100:1 # Décommenter pour spécifier [type:]nombre

    module load abaqus/2026         # Dernière version
    #module load StdEnv/2020        # Version héritée
    #module load abaqus/2021        # Ne plus utiliser

    unset SLURM_GTIDS
    export MPI_IC_ORDER='tcp'
    echo "LM_LICENSE_FILE=$LM_LICENSE_FILE"
    echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"
    echo "SLURM_SUBMIT_DIR =" $SLURM_SUBMIT_DIR
    echo "SLURM_TMPDIR = " $SLURM_TMPDIR

    rm -f testst2* testst1.lck
    cp testst1* $SLURM_TMPDIR
    mkdir $SLURM_TMPDIR/scratch
    cd $SLURM_TMPDIR
    while sleep 6h; do
       echo "Saving data due to time limit ..."
       cp -fv testst2* $SLURM_SUBMIT_DIR 2>/dev/null
    done &
    WPID=$!

    if [[ $EBVERSIONABAQUS -eq 2021 ]]; then
       /cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/unshare \
       --fork --pid --mount-proc --user --map-user $USER \
       abaqus job=testst2 oldjob=testst1 input=$SLURM_SUBMIT_DIR/mystd-sim-restart.inp \
       scratch=$SLURM_TMPDIR/scratch cpus=$SLURM_CPUS_ON_NODE interactive \
       mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB" \
       #gpus=$SLURM_GPUS_ON_NODE  # décommenter cette ligne pour utiliser le GPU
    elif [[ $EBVERSIONABAQUS -ge 2026 ]]; then
       abaqus job=testst2 oldjob=testst1 input=$SLURM_SUBMIT_DIR/mystd-sim-restart.inp \
       scratch=$SLURM_TMPDIR/scratch cpus=$SLURM_CPUS_ON_NODE interactive \
       mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB" \
       #gpus=$SLURM_GPUS_ON_NODE  # décommenter cette ligne pour utiliser le GPU
    fi

    { kill $WPID && wait $WPID; } 2>/dev/null
    cp -fv testst2* $SLURM_SUBMIT_DIR
    ```

    Le fichier en entrée pour le redémarrage doit contenir :
    `*HEADING`
    `*RESTART, READ`

:::

### Script pour nœuds multiples

Si vous disposez d'une licence qui vous permet d'exécuter des tâches nécessitant beaucoup de mémoire et de calcul, le script suivant pourra effectuer le calcul avec MPI en utilisant un ensemble de nœuds arbitraires idéalement déterminé automatiquement par l'ordonnanceur. Un script modèle pour redémarrer des tâches sur nœuds multiples n'est pas fourni car son utilisation présente des limitations supplémentaires. Avec ce script, vous pouvez utiliser uniquement Abaqus/2026 et versions plus récentes.

```sh title="scriptsp1-mpi.txt"
#!/bin/bash
#SBATCH --account=def-group    # Indiquer le compte
#SBATCH --time=00-06:00        # Indiquer jours-heures:minutes
##SBATCH --nodes=2             # Décommenter pour spécifier (optionnel)
#SBATCH --ntasks=8             # Indiquer le nombre de cœurs
#SBATCH --mem-per-cpu=4G       # Indiquer la mémoire par cœur
##SBATCH --tasks-per-node=4    # Décommenter pour spécifier (optionnel)
#SBATCH --cpus-per-task=1      # Ne pas modifier !

module load abaqus/2026         # Dernière version

unset SLURM_GTIDS
#export MPI_IC_ORDER='tcp'
echo "LM_LICENSE_FILE=$LM_LICENSE_FILE"
echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"

rm -f testsp1-mpi*

unset hostlist
nodes="$(slurm_hl2hl.py --format MPIHOSTLIST | xargs)"
for i in `echo "$nodes" | xargs -n1 | uniq`; do hostlist=${hostlist}$(echo "['${i}',$(echo "$nodes" | xargs -n1 | grep $i | wc -l)],"); done
hostlist="$(echo "$hostlist" | sed 's/,$//g')"
mphostlist="mp_host_list=[$(echo "$hostlist")]"
export $mphostlist
echo "$mphostlist" > abaqus_v6.env

abaqus job=testsp1-mpi input=mystd-sim.inp \
scratch=$SLURM_TMPDIR cpus=$SLURM_NTASKS interactive mp_mode=mpi \
#mp_host_split=1  # nombre de processus dmp par nœud >= 1 (décommenter pour spécifier)
```

## Analyse explicite

Les solveurs prennent en charge la parallélisation avec fils et avec MPI. Des scripts pour chaque mode sont présentés sous les onglets pour l'utilisation d'un nœud simple et celle de nœuds multiples. Des modèles de scripts pour redémarrer une tâche qui utilise des nœuds multiples nécessitent plus de tests et ne sont pas présentés pour l'instant.

### Scripts pour un nœud simple

::: tabs

    ::: tab Script pour le répertoire /project

    ```sh title="scriptep1.txt"
    #!/bin/bash
    #SBATCH --account=def-group    # indiquer le nom du compte
    #SBATCH --time=00-06:00        # indiquer la limite de temps (jours-heures:minutes)
    #SBATCH --mem=8000M            # indiquer la mémoire totale > 5M
    #SBATCH --cpus-per-task=4      # indiquer le nombre de cœurs > 1
    #SBATCH --nodes=1              # ne pas modifier

    module load abaqus/2026         # Dernière version
    #module load StdEnv/2020        # Version héritée
    #module load abaqus/2021        # Ne plus utiliser

    unset SLURM_GTIDS
    export MPI_IC_ORDER='tcp'
    echo "LM_LICENSE_FILE=$LM_LICENSE_FILE"
    echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"

    rm -f testep1* testep2*

    if [[ $EBVERSIONABAQUS -eq 2021 ]]; then
       /cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/unshare \
       --fork --pid --mount-proc --user --map-user $USER \
       abaqus job=testep1 input=myexp-sim.inp \
       scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
       mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB"
    elif [[ $EBVERSIONABAQUS -ge 2026 ]]; then
       abaqus job=testep1 input=myexp-sim.inp \
       scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
       mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB"
    fi
    ```

    Pour écrire les données de redémarrage pour un total de 12 incréments, le fichier en entrée doit contenir :
    `*RESTART, WRITE, OVERLAY, NUMBER INTERVAL=12, TIME MARKS=NO`
    Pour vérifier l'information complète sur le redémarrage :
    `egrep -i "step|restart" testep*.com testep*.msg testep*.sta`

    ::: tab Script de redémarrage pour le répertoire /project

    ```sh title="scriptep2.txt"
    #!/bin/bash
    #SBATCH --account=def-group    # indiquer le nom du compte
    #SBATCH --time=00-06:00        # indiquer la limite de temps (jours-heures:minutes)
    #SBATCH --mem=8000M            # indiquer la mémoire totale > 5M
    #SBATCH --cpus-per-task=4      # indiquer le nombre de cœurs > 1
    #SBATCH --nodes=1              # ne pas modifier

    module load abaqus/2026         # Dernière version
    #module load StdEnv/2020        # Version héritée
    #module load abaqus/2021        # Ne plus utiliser

    unset SLURM_GTIDS
    export MPI_IC_ORDER='tcp'
    echo "LM_LICENSE_FILE=$LM_LICENSE_FILE"
    echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"

    rm -f testep2* testep1.lck
    for f in testep1*; do [[ -f ${f} ]] && cp -a "$f" "testep2${f#testep1}"; done

    if [[ $EBVERSIONABAQUS -eq 2021 ]]; then
       /cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/unshare \
       --fork --pid --mount-proc --user --map-user $USER \
       abaqus job=testep2 input=myexp-sim.inp recover \
       scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
       mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB"
    elif [[ $EBVERSIONABAQUS -ge 2026 ]]; then
       abaqus job=testep2 input=myexp-sim.inp recover \
       scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
       mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB"
    fi
    ```

    Le fichier en entrée ne requiert aucune modification pour le redémarrage de l'analyse.

    ::: tab Script pour le répertoire temporaire

    ```sh title="scriptet1.txt"
    #!/bin/bash
    #SBATCH --account=def-group    # spécifier le compte
    #SBATCH --time=00-06:00        # jours-heures:minutes
    #SBATCH --mem=8000M            # mémoire du nœud > 5G
    #SBATCH --cpus-per-task=4      # nombre de cœurs > 1
    #SBATCH --nodes=1              # ne pas modifier

    module load abaqus/2026         # Dernière version
    #module load StdEnv/2020        # Version héritée
    #module load abaqus/2021        # Ne plus utiliser

    unset SLURM_GTIDS
    export MPI_IC_ORDER='tcp'
    echo "LM_LICENSE_FILE=$LM_LICENSE_FILE"
    echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"
    echo "SLURM_SUBMIT_DIR =" $SLURM_SUBMIT_DIR
    echo "SLURM_TMPDIR = " $SLURM_TMPDIR

    rm -f testet1* testet2*
    cd $SLURM_TMPDIR
    while sleep 6h; do
       cp -f * $SLURM_SUBMIT_DIR 2>/dev/null
    done &
    WPID=$!

    if [[ $EBVERSIONABAQUS -eq 2021 ]]; then
       /cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/unshare \
       --fork --pid --mount-proc --user --map-user $USER \
       abaqus job=testet1 input=$SLURM_SUBMIT_DIR/myexp-sim.inp \
       scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
       mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB"
    elif [[ $EBVERSIONABAQUS -ge 2026 ]]; then
       abaqus job=testet1 input=$SLURM_SUBMIT_DIR/myexp-sim.inp \
       scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
       mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB"
    fi

    { kill $WPID && wait $WPID; } 2>/dev/null
    cp -f * $SLURM_SUBMIT_DIR
    ```

    Pour écrire les données de redémarrage pour un total de 12 incréments, le fichier en entrée doit contenir :
    `*RESTART, WRITE, OVERLAY, NUMBER INTERVAL=12, TIME MARKS=NO`
    Pour vérifier l'information complète sur le redémarrage :
    `egrep -i "step|restart" testet*.com testet*.msg testet*.sta`

    ::: tab Script de redémarrage pour le répertoire temporaire

    ```sh title="scriptet2.txt"
    #!/bin/bash
    #SBATCH --account=def-group    # spécifier le compte
    #SBATCH --time=00-06:00        # jours-heures:minutes
    #SBATCH --mem=8000M            # mémoire du nœud > 5G
    #SBATCH --cpus-per-task=4      # nombre de cœurs > 1
    #SBATCH --nodes=1              # ne pas modifier

    module load abaqus/2026         # Dernière version
    #module load StdEnv/2020        # Version héritée
    #module load abaqus/2021        # Ne plus utiliser

    unset SLURM_GTIDS
    export MPI_IC_ORDER='tcp'
    echo "LM_LICENSE_FILE=$LM_LICENSE_FILE"
    echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"
    echo "SLURM_SUBMIT_DIR =" $SLURM_SUBMIT_DIR
    echo "SLURM_TMPDIR = " $SLURM_TMPDIR

    rm -f testet2* testet1.lck
    for f in testet1*; do cp -a "$f" $SLURM_TMPDIR/"testet2${f#testet1}"; done
    cd $SLURM_TMPDIR
    while sleep 3h; do
       cp -f * $SLURM_SUBMIT_DIR 2>/dev/null
    done &
    WPID=$!

    if [[ $EBVERSIONABAQUS -eq 2021 ]]; then
       /cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/unshare \
       --fork --pid --mount-proc --user --map-user $USER \
       abaqus job=testet2 input=$SLURM_SUBMIT_DIR/myexp-sim.inp recover \
       scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
       mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB"
    elif [[ $EBVERSIONABAQUS -ge 2026 ]]; then
       abaqus job=testet2 input=$SLURM_SUBMIT_DIR/myexp-sim.inp recover \
       scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
       mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB"
    fi

    { kill $WPID && wait $WPID; } 2>/dev/null
    cp -f  * $SLURM_SUBMIT_DIR
    ```

    Le fichier en entrée ne requiert aucune modification pour le redémarrage de l'analyse.

:::

### Script pour nœuds multiples

Si vous disposez d'une licence qui vous permet d'exécuter des tâches nécessitant beaucoup de mémoire et de calcul, le script suivant pourra effectuer le calcul avec MPI en utilisant un ensemble de nœuds arbitraires idéalement déterminé automatiquement par l'ordonnanceur. Un script modèle pour redémarrer des tâches sur nœuds multiples n'est pas fourni car son utilisation présente des limitations supplémentaires. Avec ce script, vous pouvez utiliser uniquement Abaqus/2026 et versions plus récentes.

```sh title="scriptep1-mpi.txt"
#!/bin/bash
#SBATCH --account=def-group    # Indiquer le compte
#SBATCH --time=00-06:00        # Indiquer jours-heures:minutes
#SBATCH --ntasks=8             # Indiquer le nombre de cœurs
#SBATCH --mem-per-cpu=16000M   # Indiquer la mémoire par cœur
# SBATCH --nodes=2             # Indiquer le nombre de nœuds (optionnel)
#SBATCH --cpus-per-task=1      # Ne pas modifier !

module load abaqus/2026        # Dernière version

unset SLURM_GTIDS
export MPI_IC_ORDER='tcp'
#export I_MPI_HYDRA_TOPOLIB=ipl
echo "LM_LICENSE_FILE=$LM_LICENSE_FILE"
echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"

rm -f testep1-mpi*

unset hostlist
nodes="$(slurm_hl2hl.py --format MPIHOSTLIST | xargs)"
for i in `echo "$nodes" | xargs -n1 | uniq`; do hostlist=${hostlist}$(echo "['${i}',$(echo "$nodes" | xargs -n1 | grep $i | wc -l)],"); done
hostlist="$(echo "$hostlist" | sed 's/,$//g')"
mphostlist="mp_host_list=[$(echo "$hostlist")]"
export $mphostlist
echo "$mphostlist" > abaqus_v6.env

abaqus job=testep1-mpi input=myexp-sim.inp \
scratch=$SLURM_TMPDIR cpus=$SLURM_NTASKS interactive mp_mode=mpi \
#mp_host_split=1  # nombre de processus dmp par nœud >= 1 (décommenter pour spécifier)
```

## Estimer le besoin en termes de mémoire

### Processus simple

Une estimation de la mémoire totale pour un nœud (`--mem=`) requise par Slurm pour qu'une simulation soit effectuée uniquement en mémoire vive (sans être virtualisée sur le disque temporaire) se trouve dans le fichier de sortie Abaqus `test.dat`. Dans l'exemple suivant, la simulation exige une assez grande quantité de mémoire.

```bash
                   M E M O R Y   E S T I M A T E
  
 PROCESS      FLOATING PT       MINIMUM MEMORY        MEMORY TO
              OPERATIONS           REQUIRED          MINIMIZE I/O
             PER ITERATION           (MB)               (MB)
  
     1          1.89E+14             3612              96345
```

Une estimation de la mémoire totale pour un processus avec fils sur un nœud unique peut aussi être obtenue en exécutant la simulation de manière interactive sur un nœud de calcul, puis en surveillant la consommation de mémoire à l'aide des commandes `ps` ou `top`.
1) Connectez-vous d'abord à une grappe avec SSH et obtenez une allocation sur un nœud de calcul (comme gra100) et démarrez votre simulation avec :

```bash
salloc --time=0:30:00 --cpus-per-task=8 --mem=64G --account=def-piname
module load StdEnv/2020
module load abaqus/2021
unset SLURM_GTIDS
abaqus job=test input=Sample.inp scratch=$SLURM_TMPDIR cpus=8 mp_mode=threads interactive
```

2) Ensuite, via SSH, connectez-vous au nœud de calcul et lancez `top`.

```bash
ssh c50
top -u $USER
```

3) Observez les colonnes VIRT et RES jusqu'à ce que des valeurs de mémoire maximales stables soient atteintes.

Pour satisfaire complètement la valeur recommandée pour `MEMORY TO OPERATIONS REQUIRED MINIMIZE I/O` (MRMIO), au moins la même quantité de mémoire physique non échangée (RES) doit être disponible pour Abaqus. Étant donné que la RES sera en général inférieure à la mémoire virtuelle (VIRT) d'une quantité relativement constante pour une simulation donnée, il est nécessaire de surallouer légèrement la mémoire du nœud demandée `--mem=`. Dans l'exemple de script ci-dessus, cette surallocation a été codée en dur à une valeur prudente de 3072Mo sur la base des tests initiaux du solveur Abaqus standard. Pour éviter les longs temps d'attente associés aux valeurs élevées de MRMIO, il peut être utile d'étudier l'impact sur les performances de simulation associées à la réduction de la mémoire RES mise à disposition d'Abaqus de manière significative en dessous de la MRMIO. Cela peut être fait en diminuant la valeur de `--mem=` qui à son tour définira une valeur artificiellement basse de `memory=` dans la commande Abaqus (trouvée dans la dernière ligne du script). En faisant cela, il faut s'assurer que RES ne descende pas en dessous de `MINIMUM MEMORY REQUIRED` (MMR) sinon Abaqus fermera à cause d'une mémoire insuffisante (OOM). Par exemple, si votre MRMIO est de 96Go, essayez d'exécuter une série de tâches de test courtes avec `#SBATCH --mem=8G, 16G, 32G, 64G` jusqu'à ce qu'un impact minimal acceptable sur les performances soit trouvé, en notant que des valeurs plus petites entraîneront un espace `/scratch` de plus en plus grand pour les fichiers temporaires.

### Processus multiples

Pour déterminer la mémoire Slurm requise pour les scripts Slurm multinœuds, les estimations de mémoire (par processus de calcul) nécessaires pour minimiser les entrées/sorties sont fournies dans le fichier de sortie `.dat` pour les tâches terminées. Si `mp_host_split` n'est pas spécifié (ou est égal à 1), le nombre total de processus de calcul sera égal au nombre de nœuds. La valeur de `mem-per-cpu` peut alors être estimée en multipliant l'estimation de mémoire la plus élevée par le nombre de nœuds, puis en divisant par le nombre de tâches (`ntasks`). En revanche, si une valeur pour `mp_host_split` est spécifiée (supérieure à 1), la valeur de `mem-per-cpu` peut être estimée en multipliant l'estimation de mémoire la plus élevée par le nombre de nœuds, puis par la valeur de `mp_host_split`, et en divisant le résultat par le nombre de tâches. Notez que `mp_host_split` doit être inférieur ou égal au nombre de cœurs par nœud attribués par Slurm lors de l'exécution, autrement Abaqus fermera. Ce scénario peut être contrôlé en supprimant le commentaire pour la ligne qui permet de spécifier une valeur pour `tasks-per-node`. Le message suivant, présent dans chaque fichier de sortie, est mentionné ici à titre de référence :

!!! note "Message du fichier de sortie (traduction libre)"
    LE MAXIMUM DE MÉMOIRE POUVANT ÊTRE ALLOUÉ PAR ABAQUS DÉPEND EN GÉNÉRAL DE LA VALEUR DU PARAMÈTRE `MÉMOIRE` ET DE LA QUANTITÉ DE MÉMOIRE PHYSIQUE DISPONIBLE SUR LA MACHINE. VEUILLEZ CONSULTER LE MANUEL D'UTILISATION D'ABAQUS ANALYSIS POUR PLUS DE DÉTAILS. L'UTILISATION RÉELLE DE LA MÉMOIRE ET DE L'ESPACE DISQUE POUR LES DONNÉES DE `/SCRATCH` DÉPENDRA DE CETTE LIMITE SUPÉRIEURE AINSI QUE DE LA MÉMOIRE REQUISE POUR MINIMISER LES ENTRÉES/SORTIES. SI LA LIMITE SUPÉRIEURE DE MÉMOIRE EST SUPÉRIEURE À LA MÉMOIRE REQUISE POUR MINIMISER LES ENTRÉES/SORTIES, L'UTILISATION RÉELLE DE LA MÉMOIRE SERA PROCHE DE LA VALEUR ESTIMÉE DE `MEMORY TO MINIMIZE I/O` ET L'UTILISATION DU DISQUE DE TRAVAIL SERA PROCHE DE ZÉRO. AUTREMENT, LA MÉMOIRE RÉELLE UTILISÉE SERA PROCHE DE LA LIMITE DE MÉMOIRE MENTIONNÉE PRÉCÉDEMMENT, ET L'UTILISATION DU DISQUE `/SCRATCH` SERA À PEU PRÈS PROPORTIONNELLE À LA DIFFÉRENCE ENTRE `MEMORY TO MINIMIZE I/O` ESTIMÉE ET LA LIMITE SUPÉRIEURE DE LA MÉMOIRE. TOUTEFOIS, IL EST IMPOSSIBLE D'ÉVALUER AVEC PRÉCISION L'ESPACE `/SCRATCH` DU DISQUE.

# Utilisation graphique

Nous recommandons d'utiliser Open OnDemand ou Jupyter pour travailler avec des applications graphiques.

## OnDemand

1.  Lancez une session OnDemand sur votre bureau en cliquant sur le lien approprié.
    *   [NIBI](https://ondemand.sharcnet.ca) : `https://ondemand.sharcnet.ca`
    *   TRILLIUM : `https://ondemand.scinet.utoronto.ca`

2.  Ouvrez une nouvelle fenêtre de terminal et chargez :

    ```bash
    module load abaqus/2026
    ```

3.  Lancez l'application en mode graphique avec l'option `cae`. Si vous êtes sur un nœud sans GPU ou sur un nœud avec GPU où VirtualGL n'est pas pris en charge, ajoutez l'option `mesa`.

    ```bash
    abaqus cae -mesa
    ```

4.  Si vous avez besoin d'une meilleure performance graphique et êtes sur un nœud avec GPU où VirtualGL est pris en charge, lancez Abaqus sans l'option `mesa`. Dans Nibi Desktop, sélectionnez H100 (80GB) dans le menu déroulant.

    ```bash
    abaqus cae
    ```

5.  Pour lancer Abaqus en mode graphique, il faut au moins une licence de calcul non utilisée, selon :

    ```bash
    $ abaqus licensing lmstat -c $ABAQUSLM_LICENSE_FILE -a | grep "Users of cae"
    Users of cae:  (Total of 4 licenses issued;  Total of 3 licenses in use)
    ```

## JupyterLab

1.  Sur votre bureau, lancez une session JupyterHub en cliquant sur une URL ci-dessous.
    *   FIR : `https://jupyterhub.fir.alliancecan.ca`
    *   NARVAL : `https://portail.narval.calculquebec.ca/`
    *   RORQUAL : `https://jupyterhub.rorqual.alliancecan.ca`
2.  Sélectionnez un module COMSOL (par exemple `comsol/6`) dans la section *Module disponible* de gauche.
3.  Pour le module sélectionné, cliquez sur *Load* pour faire afficher l'icône `Comsol (VNC)` sur le bureau.
4.  Cliquez sur l'icône et COMSOL devrait automatiquement démarrer sur un bureau Jupyter à distance.

## VNCViewer

Cette approche est obsolète. Veuillez utiliser un bureau OnDemand ou JupyterLab comme décrit ci-dessus.

1.  Avec un client VncViewer, connectez-vous à un nœud de calcul ou de connexion sans GPU, comme décrit dans [TigerVNC](../interactive/vnc.md).
2.  Ouvrez une nouvelle fenêtre de terminal et entrez :

    ```bash
    module load abaqus/2026
    ```

3.  Lancez l'application avec :

    ```bash
    abaqus cae -mesa
    ```

# Utilisation spécifique au site

## Licence SHARCNET

La licence SHARCNET a été renouvelée jusqu'au 17 janvier 2026. Elle offre une licence gratuite limitée comprenant 2 jetons de calcul et 35 jetons d'exécution, avec des limites d'utilisation de 10 jetons par utilisateur et 15 jetons par groupe. Pour les groupes ayant acquis des jetons dédiés, les limites d'utilisation des jetons gratuits sont ajoutées à leur réservation. Les jetons gratuits sont attribués selon le principe du premier arrivé, premier servi et sont principalement destinés aux tests et à une utilisation légère avant de décider d'acheter ou non des jetons dédiés. Le coût des jetons dédiés (en 2021) était d'environ 110 $ CA par jeton de calcul et 400 $ CA par jeton d'interface graphique : écrivez au [soutien technique](../support/technical_support.md) pour obtenir un devis officiel. La licence peut être utilisée avec un compte de l'Alliance, mais uniquement sur le matériel SHARCNET. Les groupes qui achètent des jetons dédiés pour le serveur de licences SHARCNET ne peuvent les utiliser que sur le matériel SHARCNET, notamment le système SHARCNET [OOD](https://ondemand.sharcnet.ca) (pour le mode graphique) ou les grappes Nibi/Dusky (pour soumettre des tâches de calcul par lots à la file d'attente). Avant d'utiliser la licence, vous devez contacter le [soutien technique](../support/technical_support.md) et demander l'accès. Dans votre courriel, veuillez 1) préciser que la demande est destinée à une utilisation sur les systèmes SHARCNET et 2) copier-coller l'accord de licence suivant, en indiquant vos nom et prénom ainsi que votre nom d'utilisateur aux emplacements prévus. Veuillez noter que chaque utilisateur doit effectuer cette démarche; elle ne peut être effectuée une seule fois pour un groupe, y compris pour les chercheuses principales et chercheurs principaux ayant acheté leurs propres jetons dédiés.

### Entente

````text
----------------------------------------------------------------------------------
Subject: Abaqus SHARCNET Academic License User Agreement

This email is to confirm that i "_____________" with username "___________" will
only use “SIMULIA Academic Software” with tokens from the SHARCNET license server
for the following purposes:

1) on SHARCNET hardware where the software is already installed
2) in affiliation with a Canadian degree-granting academic institution
3) for education, institutional or instruction purposes and not for any commercial
   or contract-related purposes where results are not publishable
4) for experimental, theoretical and/or digital research work, undertaken primarily
   to acquire new knowledge of the underlying foundations of phenomena and observable
   facts, up to the point of proof-of-concept in a laboratory    
-----------------------------------------------------------------------------------
````

### Configurer le fichier de licence

Configurez votre fichier de licence comme suit (uniquement sur les systèmes SHARCNET comme les grappes Nibi et Dusky ou sur le système de bureau OOD de SHARCNET). Pour utiliser la licence SHARCNET gratuite, vous devez mettre à jour votre fichier `abaqus.lic` comme suit, puisque le serveur `license3.sharcnet.ca` est définitivement fermé.

```bash
[l2 (nibi login node):~] cat ~/.licenses/abaqus.lic
prepend_path("ABAQUSLM_LICENSE_FILE","27050@license1.computecanada.ca")
```

Si votre tâche se termine anormalement avec le message d'erreur `*** ABAQUS/eliT_CheckLicense rank 0 terminated by signal 11 (Segmentation fault)`, vérifiez si votre fichier `abaqus.lic` contient `ABAQUSLM_LICENSE_FILE` pour Abaqus/202X.
Si le message d'erreur est `License server machine is down or not responding etc.` et que vous utilisez Abaqus/6.14.1, remplacez `ABAQUSLM_LICENSE_FILE` par `LM_LICENSE_FILE`.

### Interroger le serveur de licences

Connectez-vous à Nibi, chargez Abaqus et exécutez une des commandes suivantes :

```bash
ssh nibi.alliancecan.ca
module load StdEnv/2020
module load abaqus
```

I) Vérifiez s'il y a des tâches lancées et des tâches dans la file d'attente pour le serveur de licence SHARCNET.

```bash
abaqus licensing lmstat -c $ABAQUSLM_LICENSE_FILE -a | egrep "Users|start|queued"
```

II) Vérifiez s'il y a des tâches lancées et des tâches dans la file d'attente pour le serveur de licence SHARCNET et s'il indique des réservations de produits par groupe d'acquisition.

```bash
abaqus licensing lmstat -c $ABAQUSLM_LICENSE_FILE -a | egrep "Users|start|queued|RESERVATION"
```

III) Vérifiez si le serveur de licences SHARCNET montre une disponibilité explicite pour le produit standard pour le calcul.

```bash
abaqus licensing lmstat -c $ABAQUSLM_LICENSE_FILE -a | grep "Users of" | egrep "cae|standard|explicit"
```

Lorsque le résultat de la requête I) ci-dessus indique qu'une tâche associée à un nom d'utilisateur donné est en file d'attente, cela signifie que la tâche est passée à l'état `R (running)` pour `squeue -j jobid` ou `sacct -j jobid` et qu'elle est donc inactive sur un nœud de calcul, en attente d'une licence. Cela aura le même impact sur la priorité de votre compte que si la tâche effectuait des calculs et consommait du temps CPU. La tâche en file d'attente démarrera dès que suffisamment de licences seront disponibles.

#### Exemple

L'exemple suivant illustre la situation où un utilisateur soumet successivement deux tâches pour 6 cœurs, nécessitant chacune 12 jetons. L'ordonnanceur a ensuite lancé chaque tâche sur un nœud différent, dans l'ordre de leur soumission. L'utilisateur disposant de 10 jetons Abaqus, la première tâche (27527287) a pu obtenir exactement les 10 jetons nécessaires au démarrage du solveur. La seconde tâche (27527297), n'ayant plus accès à des jetons, est restée en attente (comme le montre la sortie de `lmstat`) jusqu'à la fin de la première, gaspillant ainsi les ressources disponibles et réduisant la juste part de l'utilisateur.

```bash
[l2 (nibi login node):~] sq
           JOBID     USER              ACCOUNT           NAME  ST  TIME_LEFT NODES CPUS TRES_PER_N MIN_MEM NODELIST (REASON) 
        27530366  roberpj         cc-debug_cpu  scriptsp2.txt   R    9:56:13     1    6        N/A      8G     c107  (None) 
        27530407  roberpj         cc-debug_cpu  scriptsp2.txt   R    9:59:37     1    6        N/A      8G     c292  (None) 
```

```bash
[l2 (nibi login node):~] abaqus licensing lmstat -c $ABAQUSLM_LICENSE_FILE -a | egrep "Users|start|queued"
Users of abaqus:  (Total of 78 licenses issued;  Total of 53 licenses in use)
   roberpj c107 /dev/tty (v62.6) (license3.sharcnet.ca/27050 1042), start Mon 11/25 17:15, 10 licenses
   roberpj c292 /dev/tty (v62.6) (license3.sharcnet.ca/27050 125) queued for 10 licenses
```

Pour éviter les problèmes de pénurie de licences lors de la soumission de plusieurs tâches avec des jetons Abaqus coûteux, utilisez soit [une dépendance](../running-jobs/running_jobs.md#annulation-de-tâches-dont-les-conditions-de-dépendance-ne-sont-pas-satisfaites), [un vecteur de tâches](../running-jobs/job_arrays.md), soit au moins configurez [une notification par courriel Slurm](../running-jobs/monitoring_jobs.md#notification-par-courriel) pour savoir quand votre tâche est terminée avant d'en soumettre une autre manuellement.

**Option 1)**

Pour empêcher les tâches non interactives (analyse) de démarrer sur un nœud de calcul après avoir été soumises à la file d'attente et être devenues inactives (lorsque le nombre de jetons disponibles est insuffisant, comportement par défaut), créez un fichier texte dans votre répertoire de soumission (avant de soumettre la tâche) avec la ligne suivante et la tâche se terminera immédiatement.

```bash
[l2 (nibi login node):~/submitdirectory] cat abaqus_v6.env
lmlicensequeuing=OFF
```

Lorsqu'une tâche se termine immédiatement (sans entrer dans un état d'attente pour une licence), la fin du fichier de sortie Slurm correspondant contiendra des messages tels que :

```text
Abaqus 2026   
Checkout exceeds MAX specified in options file.
FlexNet Licensing error:-87,147
Number of requested licenses: 14
Number of total licenses:     78
Number of licenses in use:    14
Number of available licenses: 64
This may be due to insufficient licenses.
ValueError: not enough values to unpack (expected 2, got 1)
During handling of the above exception, another exception occurred:
Exception: DriverLM: can't parse host/port from umbrella
Abaqus Error: Error checking out Abaqus license.
Abaqus/Analysis exited with errors
```

**Option 2)**

Spécifiez un paramètre en minutes pour qu'une tâche démarrée entre dans un état de file d'attente pour attendre une licence avant d'être automatiquement retirée de la file d'attente et terminée si une licence ne devient pas disponible à temps.

```bash
[l2 (nibi login node):~/submitdirectory] cat abaqus_v6.env
 lmhanglimit=1 
```

Lorsqu'une tâche se termine de cette manière, après avoir été mise en file d'attente et qu'aucune licence ne devient disponible dans le temps spécifié selon la valeur de `lmhanglimit` (1 minute dans cet exemple), les messages à la fin du fichier de sortie Slurm apparaîtront plutôt comme suit :

```text
Abaqus 2026
"standard" license request queued for the License Server on license1.computecanada.ca. 
Total time in queue: 0 seconds.
"standard" license request queued for the License Server on license1.computecanada.ca. 
Total time in queue: 30 seconds.
"standard" license request queued for the License Server on license1.computecanada.ca. 
Total time in queue: 60 seconds.
Time limit of in queue has been exceeded. Exiting.
This may be due to insufficient licenses.
ValueError: not enough values to unpack (expected 2, got 1)
During handling of the above exception, another exception occurred:
Exception: DriverLM: can't parse host/port from umbrella
Abaqus Error: Error checking out Abaqus license.
Abaqus/Analysis exited with errors
```

### Spécifier les ressources de la tâche

Pour assurer une utilisation optimale de vos jetons Abaqus et de nos ressources, il est important de spécifier soigneusement la mémoire et le nombre de CPU requis dans votre script Slurm. Les valeurs peuvent être déterminées en soumettant quelques tâches de test courtes à la file d'attente, puis en vérifiant leur utilisation. Pour les tâches **terminées**, utilisez `seff JobNumber` pour afficher la *Mémoire utilisée* totale et l'*Efficacité de la mémoire*. Si l'*Efficacité de la mémoire* est inférieure à environ 90%, diminuez en conséquence la valeur du paramètre `#SBATCH --mem=` dans votre script Slurm. Notez que la commande `seff JobNumber` affiche également le *Temps CPU utilisé* total et l'*Efficacité du CPU*. Si l'*Efficacité du CPU* est inférieure à environ 90%, effectuez des tests de mise à l'échelle pour déterminer le nombre optimal de CPU pour des performances optimales, puis mettez à jour la valeur de `#SBATCH --cpus-per-task=` dans votre script Slurm. Pour les tâches **en cours d'exécution**, utilisez la commande `srun --overlap --jobid=29821580 --pty top -d 5 -u $USER` pour surveiller le `%CPU`, `%MEM` et `RES` pour chaque processus parent Abaqus sur le nœud de calcul. Les colonnes `%CPU` et `%MEM` affichent le pourcentage d'utilisation par rapport au total disponible sur le nœud, tandis que la colonne `RES` indique la taille de la mémoire résidente par processus (au format lisible pour les valeurs supérieures à 1 Go). Des informations supplémentaires sur la façon de [surveiller les tâches](../running-jobs/monitoring_jobs.md) sont disponibles sur notre wiki de documentation.

### Correspondance cœur-jeton

```text
TOKENS 5  6  7  8  10  12  14  16  19  21  25  28  34  38
CORES  1  2  3  4   6   8  12  16  24  32  48  64  96 128
```

où `TOKENS = floor[5 X CORES^0.422]`

Chaque GPU nécessite un jeton additionnel.

## Licence de Western

La licence Western est réservée aux chercheurs et chercheuses de Western et ne peut être utilisée que sur du matériel situé sur le campus. Actuellement, seulement la grappe Dusky remplit cette condition. Les systèmes Nibi et SHARCNET OOD sont exclus, car ils se trouvent sur le campus de Waterloo. Pour toute question concernant l'utilisation de la licence Abaqus de Western, veuillez contacter l'administrateur du serveur de licences Abaqus de Western à l'adresse <jmilner@robarts.ca>. Vous devrez fournir votre nom d'utilisateur et éventuellement prévoir l'achat de jetons. Si votre demande d'accès est acceptée, vous pourrez configurer votre fichier `abaqus.lic` pour qu'il pointe vers le serveur de licences de Western.

```bash
[laptop:~] ssh dusky.alliancecan.ca

[dus241:~] cat .licenses/abaqus.lic
prepend_path("ABAQUSLM_LICENSE_FILE","27000@authorize.robarts.ca")
```

Par la suite, soumettez votre tâche tel que décrit à la section *Soumettre une tâche sur une grappe* ci-dessus. Si un problème survient, écrivez au [soutien technique](../support/technical_support.md) en indiquant que vous utilisez la licence du site Western sur Dusky. Ajoutez le numéro de la tâche qui pose problème et copiez le ou les messages d'erreur s'il y a lieu.