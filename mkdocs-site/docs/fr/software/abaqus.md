---
title: "Abaqus/fr"
slug: "abaqus"
lang: "fr"

source_wiki_title: "Abaqus/fr"
source_hash: "c3b8e7b609c4611ef407ca0444438c20"
last_synced: "2026-09-06T00:43:13.954271+00:00"
last_processed: "2026-09-06T02:24:18.156088+00:00"

tags:
  - software

keywords:
  - "Open OnDemand"
  - "grappe Dusky"
  - "redémarrage"
  - "jetons de calcul"
  - "adresse IP"
  - "scripts MPI"
  - "grappe"
  - "VncViewer"
  - "#SBATCH --mem=8000M"
  - "--mem=8000M"
  - "module load abaqus"
  - "module COMSOL"
  - "Abaqus"
  - "export MPI_IC_ORDER='tcp'"
  - "monitor jobs"
  - "#SBATCH --mem-per-cpu=4G"
  - "mémoire maximale"
  - "resident memory size"
  - "memory and CPU efficiency"
  - "mp_mode=threads"
  - "gpus"
  - "mémoire"
  - "SLURM"
  - "Analyse explicite"
  - "RESTART"
  - "licence à distance"
  - "mem-per-cpu"
  - "cpus-per-task"
  - "défaillance matérielle"
  - "vecteur"
  - "fichier en entrée"
  - "module load StdEnv/2020"
  - "pénurie de licences"
  - "Comsol (VNC)"
  - "mem"
  - "comsol/6"
  - "MRMIO"
  - "licence SHARCNET"
  - "serveur DSLS"
  - "mp_host_split"
  - "licence Western"
  - "abaqus"
  - "notification par courriel Slurm"
  - "#SBATCH --ntasks=8"
  - "license3.sharcnet.ca"
  - "fichier abaqus.lic"
  - "cœurs par nœud"
  - "pare-feu"
  - "abaqus/2026"
  - "configuration licence"
  - "serveur de licence Abaqus"
  - "nombre de nœuds"
  - "incréments de N=12"
  - "license server"
  - "mp_mode=mpi"
  - "--cpus-per-task=4"
  - "RES"
  - "Abaqus/202X"
  - "SLURM_TMPDIR"
  - "#SBATCH --cpus-per-task=4"
  - "licence FLEXnet"
  - "fichier de sortie Abaqus test.dat"
  - "mémoire totale"
  - "Segmentation fault"
  - "SLURM_MEM_PER_NODE"
  - "License server machine is down or not responding"
  - "#SBATCH"
  - "Abaqus license error"
  - "lmhanglimit"
  - "TOKENS = floor[5 X CORES^0.422]"
  - "Slurm"
  - "données de redémarrage"
  - "MPI_IC_ORDER"
  - "lmlicensequeuing=OFF"
  - "mémoire estimée"
  - "bureau Jupyter à distance"
  - "nombre de tâches"
  - "OVERLAY"
  - "lmhanglimit=1"
  - "temps d'exécution maximal"
  - "scripts pour un nœud simple"
  - "simulation en mémoire vive"
  - "RES column"
  - "fichier d'entrée"
  - "WRITE"
  - "script de redémarrage"
  - "nœuds multiples"
  - "lmstat -c $ABAQUSLM_LICENSE_FILE"
  - "time"
  - "module load abaqus/20263"
  - "#SBATCH --time=00-06:00"
  - "file d'attente"
  - "Correspondance cœur-jeton"
  - "serveur de licences"
  - "token‑core mapping"
  - "JupyterHub"
  - "#SBATCH --nodes=2"
  - "jetons Abaqus"
  - "abaqus.lic"
  - "ABAQUSLM_LICENSE_FILE"
  - "paramètre MEMOIRE"
  - "licence de calcul"
  - "time=00-06:00"
  - "account"
  - "RESTART WRITE OVERLAY FREQUENCY=12"
  - "répertoire temporaire"
  - "module load abaqus/2026"
  - "tâche en file d'attente"
  - "dépendance"
  - "nœud (--mem=)"
  - "MPI"
  - "tasks-per-node"
  - "jeton additionnel"
  - "#SBATCH --account=def-group"

questions:
  - "Quels sont les deux types de serveurs de licence pris en charge par Abaqus sur les grappes Alliance et quelles sont les procédures d’installation spécifiques à chaque type ?"
  - "Comment créer et configurer le fichier `abaqus.lic` pour un serveur FLEXnet, en précisant les éléments à remplacer (port, adresse IP ou nom de domaine) ?"
  - "Quelles sont les étapes nécessaires pour utiliser un serveur de licence DSLS, notamment la création des fichiers `abaqus_v6.env` et `DSLicSrv.txt` et leur contenu requis ?"
  - "Quelle procédure faut‑il suivre pour obtenir l’adresse IP du serveur de licence Abaqus et les ports à ouvrir ?"
  - "Pourquoi l’administrateur système doit‑il ouvrir les pare‑feu du serveur local pour permettre la connexion de la grappe ?"
  - "Dans quelles circonstances une entente spéciale avec SIMULIA doit‑elle être négociée pour l’utilisation à distance de la licence ?"
  - "How can you configure the Abaqus license server to avoid jobs waiting indefinitely for a license, and what are the effects of using `lmlicensequeuing=OFF` versus setting `lmhanglimit`?"
  - "Which Abaqus modules are currently recommended for use, and what issues are associated with the legacy `abaqus/2021` module?"
  - "What are the key considerations and recommended script options when submitting parallel Abaqus simulations on the cluster, especially regarding memory settings and restart handling?"
  - "Quand faut‑il utiliser les scripts MPI sur plusieurs nœuds au lieu des scripts à fils sur un seul nœud, et quels avantages cela apporte‑t‑il en termes de mémoire et de calcul ?"
  - "Quelle méthode est recommandée pour tester rapidement la scalabilité d’une tâche avant de la lancer en longue durée, afin de déterminer le nombre optimal de cœurs et les besoins en mémoire ?"
  - "Quels sont les principaux paramètres du script SLURM présenté pour un nœud simple (mémoire, nombre de cœurs, options Abaqus comme *mp_mode* et les réglages de redémarrage) et comment les ajuster selon les besoins de la simulation ?"
  - "Quels scénarios peuvent entraîner l'arrêt d’une tâche, comme le dépassement du temps d’exécution maximal ou la défaillance matérielle du nœud de calcul ?"
  - "Comment le fichier d’entrée peut‑il être modifié pour permettre la continuation d’une tâche avec des étapes supplémentaires ou pour ajuster l’analyse ?"
  - "Où peut‑on consulter la documentation afin d’obtenir plus de détails sur les différents types de redémarrage et les options de version ?"
  - "What resources (account, runtime, CPU cores, memory, and nodes) are specified for the job in this SLURM script?"
  - "How can the script be modified to request a specific node type or allocate GPUs for the job?"
  - "What is the role of the `#!/bin/bash` shebang line and the `#SBATCH` directives in this script?"
  - "Quels modules et quelles versions d’Abaqus sont chargés, et quelles versions sont indiquées comme à ne plus utiliser ?"
  - "Comment le script configure‑t‑il les redémarrages de simulation (fichiers d’entrée, options *RESTART, *WRITE, *OVERLAY, FREQUENCY) pour des incréments de N = 12 ?"
  - "De quelle façon le script exploite‑t‑il les ressources SLURM (CPU, mémoire, GPU, répertoire temporaire) et quelles procédures de sauvegarde périodique sont mises en place ?"
  - "À quoi sert la ligne `memory=\"$((${SLURM_MEM_PER_NODE}-3072))MB\"` dans le script et comment calcule‑t‑elle la mémoire allouée ?"
  - "Comment activer l’utilisation des GPU dans ce script (quelle ligne doit‑on décommenter) ?"
  - "Quels éléments doit contenir le fichier d’entrée pour écrire les données de redémarrage en incréments de N=12, et quelle alternative existe‑t‑il pour un total de 12 incréments ?"
  - "Quels paramètres SLURM doivent être configurés pour lancer correctement un redémarrage Abaqus sur un nœud unique ?"
  - "Comment le script assure‑t‑il la sauvegarde périodique des fichiers de simulation afin de respecter la limite de temps d’exécution ?"
  - "Quelles licences et versions d’Abaqus sont requises pour utiliser le script de redémarrage sur plusieurs nœuds avec MPI ?"
  - "What does the `#SBATCH --mem-per-cpu=4G` directive specify for the job?"
  - "Why is the `module load abaqus/2026` command included in this batch script?"
  - "What is the effect of the `unset SLURM_GTIDS` line before exporting `MPI_IC_ORDER`?"
  - "Comment les scripts présentés permettent‑ils de lancer une analyse explicite avec Abaqus en mode threads sur un nœud unique sous SLURM ?"
  - "Quelle est la méthode utilisée dans le script « testsp1‑mpi » pour construire et exporter la liste d’hôtes MPI nécessaire à l’exécution multi‑nœuds ?"
  - "Comment préparer et exécuter un redémarrage d’une tâche Abaqus en spécifiant le nombre d’incréments de redémarrage dans le fichier d’entrée ?"
  - "Quel est le rôle du script de redémarrage et comment il utilise les répertoires temporaires SLURM pour copier les fichiers de travail ?"
  - "Comment le script différencie‑t‑il les versions d’Abaqus (2021 vs ≥ 2026) et quelles options de lancement (unshare, mp_mode, mémoire, etc.) sont appliquées pour chaque version ?"
  - "Quelles modifications doivent être apportées au fichier d’entrée afin d’écrire les données de redémarrage pour un total de 12 incréments (RESTART, WRITE, OVERLAY, NUMBER INTERVAL=12, TIME MARKS=NO) ?"
  - "Quelle est la signification de la directive `#SBATCH --time=00-06:00` dans ce script ?"
  - "Pourquoi le script charge plusieurs versions du module `abaqus` (2026, StdEnv/2020, 2021) et que doit‑on faire avec ces lignes ?"
  - "À quoi sert la commande `unset SLURM_GTIDS` à la fin du script ?"
  - "What resources and limits (account, time, memory, CPUs, nodes) are specified by the SBATCH directives?"
  - "Which Abaqus module version is intended for use, and why are alternative module loads included in the script?"
  - "How does the script configure the job to run on a single node with multiple CPU cores?"
  - "Quels paramètres Slurm (ex. --time, --ntasks, --mem‑per‑cpu, etc.) doivent être définis dans le script pour lancer correctement une analyse Abaqus en mode interactif sur un nœud unique ?"
  - "Comment le script assure‑t‑il la synchronisation des fichiers entre le répertoire de soumission Slurm et le répertoire temporaire du nœud (via les boucles de copie et le processus en arrière‑plan), et pourquoi cette étape est‑elle cruciale pour la reprise ou la continuité de la simulation ?"
  - "Quelles sont les différences principales entre l’exécution d’Abaqus version 2021 et les versions 2026 ou supérieures lorsqu’on utilise le script MPI pour le calcul sur plusieurs nœuds, notamment concernant les options de lancement et les limitations éventuelles ?"
  - "Où se trouve l’estimation de la mémoire totale requise par Slurm pour qu’une simulation Abaqus s’exécute uniquement en mémoire vive ?"
  - "Quelle option de ligne de commande Slurm (par exemple « --mem= ») doit être utilisée pour spécifier cette quantité de mémoire ?"
  - "Pourquoi est‑il souhaitable que la simulation ne soit pas virtualisée sur le disque scratch ?"
  - "Quelle procédure doit‑on suivre pour estimer la consommation mémoire d’une simulation Abaqus sur un nœud unique en utilisant les commandes ps ou top ?"
  - "Comment déterminer la valeur adéquate du paramètre ‑mem ou #SBATCH --mem pour respecter la contrainte MEMORY TO OPERATIONS REQUIRED MINIMIZE I/O sans provoquer d’erreur OOM ?"
  - "Quels sont les calculs à appliquer pour estimer la mémoire mem‑per‑cpu dans un job Slurm multinœuds selon que le paramètre mp_host_split est spécifié ou non ?"
  - "Quelle contrainte doit respecter la valeur de <code>mp_host_split</code> par rapport au nombre de cœurs par nœud alloués par Slurm pour éviter la fermeture d’Abaqus ?"
  - "Comment le nombre de tâches est‑il calculé à partir du nombre de nœuds et de la valeur de <code>mp_host_split</code> ?"
  - "Quelle modification du fichier de configuration permet de contrôler le scénario en spécifiant une valeur pour tasks‑per‑node ?"
  - "Quels sont les paramètres qui influencent le maximum de mémoire allouée par Abaqus et comment cela affecte l’utilisation du disque /scratch ?"
  - "Comment lancer Abaqus/CAE en mode graphique via Open OnDemand ou Jupyter, en choisissant les options appropriées selon la présence d’un GPU ou de VirtualGL ?"
  - "Quelle commande utiliser pour vérifier la disponibilité d’une licence de calcul Abaqus CAE avant de démarrer l’application ?"
  - "Quelle est la procédure recommandée pour se connecter à un nœud de calcul afin d’utiliser Abaqus, en remplacement de l’approche VncViewer obsolète ?"
  - "Quels sont les détails de la licence SHARCNET gratuite (nombre de jetons, limites d’utilisation, conditions d’attribution) et comment obtenir des jetons dédiés ?"
  - "Comment doit‑on configurer le fichier de licence abaqus.lic sur les systèmes SHARCNET pour utiliser la licence gratuite et éviter les erreurs de segmentation ?"
  - "Comment accéder à l'URL du serveur JupyterHub indiqué dans le texte ?"
  - "Quel module COMSOL doit‑on sélectionner dans la section « Available Module » avant de le charger ?"
  - "Quelle action faut‑il réaliser après le chargement du module pour lancer automatiquement COMSOL sur le bureau Jupyter distant ?"
  - "Pourquoi le serveur license3.sharcnet.ca est‑il définitivement fermé et quelles sont les implications pour les utilisateurs d’Abaqus ?"
  - "Quelle modification doit‑on apporter au fichier ~/.licenses/abaqus.lic afin d’utiliser le serveur de licence license1.computecanada.ca ?"
  - "Que faut‑il vérifier dans le fichier abaqus.lic lorsqu’une tâche se termine avec l’erreur « *** ABAQUS/eliT_CheckLicense rank 0 terminated by signal 11 (Segmentation fault) » ?"
  - "Que faut‑il faire si l’on obtient l’erreur « License server machine is down or not responding » avec Abaqus/6.14.1 ?"
  - "Comment vérifier l’état des licences et des tâches en file d’attente sur le serveur de licences SHARCNET à l’aide des commandes lmstat ?"
  - "Quelles stratégies sont recommandées pour éviter la pénurie de licences lorsqu’on soumet plusieurs tâches Abaqus simultanément ?"
  - "How can you disable non‑interactive (analysis) Abaqus jobs from starting on a compute node when no license tokens are available?"
  - "What is the purpose of the `lmhanglimit` setting and how does it control job termination if a license is not obtained within the specified time?"
  - "Which commands and efficiency metrics should be used to determine the optimal `--mem` and `--cpus-per-task` values for an Abaqus job on the cluster?"
  - "Quels problèmes peut‑on rencontrer à cause de la pénurie de licences lorsqu’on soumet plusieurs tâches utilisant des jetons Abaqus coûteux ?"
  - "Quelles alternatives le texte propose‑t‑il pour gérer la soumission de tâches afin d’éviter les conflits de licences (dépendance, vecteur, notification par courriel) ?"
  - "Comment mettre en place une notification par courriel Slurm pour être informé de la fin d’une tâche avant d’en lancer une autre manuellement ?"
  - "Que représente la colonne RES dans l’affichage des processus et comment sont présentées les valeurs supérieures à 1 Go ?"
  - "Où peut‑on trouver des informations supplémentaires pour surveiller les jobs selon le texte ?"
  - "Selon le tableau de correspondance cœur‑jeton, comment calcule‑t‑on le nombre de TOKENS à partir du nombre de CORES ?"
  - "Quelle est la procédure à suivre pour configurer le fichier abaqus.lic afin d’utiliser la licence Western sur la grappe Dusky ?"
  - "Pourquoi le serveur de licences « license4 » n’est‑plus disponible et quelles alternatives temporaires sont proposées aux utilisateurs ?"
  - "Quelles sont les conditions d’éligibilité et les restrictions d’utilisation de la licence Western (ex. matériel du campus, jetons GPU, etc.)?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Abaqus FEA est un progiciel commercial pour l'analyse par éléments finis et l'ingénierie assistée par ordinateur.

## Licence

Les modules logiciels Abaqus sont disponibles sur les grappes de l'Alliance, mais vous devez fournir votre propre licence. Il existe deux types de serveurs de licences, chacun avec des procédures de configuration différentes décrites ci-dessous.

### Serveurs FLEXnet

Les modules Abaqus sont disponibles sur nos grappes, mais vous devez posséder votre propre licence. Pour configurer votre compte sur les grappes que vous voulez utiliser, connectez-vous et créez sur chacune un fichier `$HOME/.licenses/abaqus.lic` qui contient la ligne ci-dessous. Remplacez ensuite `port@server` par le numéro du port flexlm et l'adresse IP (ou le nom complet du domaine) de votre serveur de licence Abaqus. Si vous voulez utiliser la version 6.14.1, remplacez ABAQUSLM_LICENSE_FILE par LM_LICENSE_FILE.

```ini title="abaqus.lic"
prepend_path("ABAQUSLM_LICENSE_FILE","port@server")
```

```bash
[l2 (login node):~/.licenses] cat abaqus.lic
prepend_path("ABAQUSLM_LICENSE_FILE","LMGRD-PORT-NUMBER@FLEXnet-SERVER-HOSTNAME")
```

### Serveurs DSLS

Comme c'était le cas avec les modules déjà installés, `abaqus/2026` est configuré pour fonctionner avec le serveur de licence Simulia FLEXnet par défaut, tout comme le serveur de licence gratuit de SHARCNET. Pour utiliser un serveur de licence DSLS de votre établissement, vous devez créer les fichiers texte `abaqus_v6.env` et `DSLicSrv.txt` dans le répertoire utilisé pour soumettre votre simulation (voir le code ci-dessous). Ils seront lus automatiquement au lancement d'Abaqus et la reconfiguration se fera en conséquence.

```text title="abaqus_v6.env"
[l2 (login node):~ ] cat abaqus_v6.env
license_server_type=DSLS
dsls_license_config="/home/<username>/DSLicSrv.txt"
```

```text title="DSLicSrv.txt"
[l2 (login node):~ ] cat DSLicSrv.txt
DSLS-SERVER-HOSTNAME:LICENSING-CLIENT-PORT-NUMBER
```

```text title="abaqus_v6.env"
[l2 (login node):~/mysimdir] cat abaqus_v6.env
license_server_type=DSLS
dsls_license_config="DSLicSrv.txt"
```

```text title="DSLicSrv.txt"
[l2 (login node):~/mysimdir] DSLicSrv.txt
YOUR-SERVER-HOSTNAME:PORT-NUMBER
```

!!! note
    Si votre licence n'est pas configurée pour une grappe en particulier, les administrateurs de systèmes des deux parties devront effectuer certaines modifications. Ceci est nécessaire pour que les ports flexlm et TCP de votre serveur Abaqus puissent être rejoints par tous les nœuds de calcul quand vos tâches dans la file d'attente seront exécutées. Pour que nous puissions vous assister dans cette tâche, écrivez au [soutien technique](../support/technical_support.md) en indiquant :
    *   le numéro du port flexlm
    *   le numéro du port statique
    *   l'adresse IP de votre serveur de licence Abaqus.

    En retour vous recevrez une liste d'adresses IP et votre administrateur de système pourra ouvrir les pare-feu de votre serveur local pour que la grappe puisse se connecter via les deux ports. Une entente spéciale doit habituellement être négociée et signée avec SIMULIA pour qu'une telle licence puisse être utilisée à distance avec notre matériel.

## Gestion des licences

### Gestion des files d'attente de licences

La configuration par défaut du serveur de licences est de mettre en file d'attente les tâches démarrées sur la grappe par Slurm si le nombre de jetons disponibles est insuffisant. Il existe deux options pour modifier ce comportement afin que les tâches ne restent pas inactives sur un nœud de calcul de la grappe, en attente d'une licence indéfiniment, gaspillant ainsi des ressources précieuses. La première option est de terminer une tâche immédiatement si le nombre de licences disponibles est insuffisant, de sorte qu'elle n'entre jamais dans une file d'attente. Pour spécifier ce réglage, créez un fichier texte nommé `abaqus_v6.env` dans votre répertoire `/home` OU votre répertoire de travail (de soumission) contenant la ligne suivante : `` `lmlicensequeuing=OFF` ``. La deuxième option consiste à spécifier un temps d'attente défini pendant lequel la tâche peut entrer dans un état de file d'attente sur le serveur de licences, par exemple 1 minute, en ajoutant la ligne : `` `lmhanglimit=1` ``. Si, dans la minute impartie, un nombre suffisant de licences ne devient pas disponible, la tâche sera retirée de la file d'attente par le serveur de licences et, à son tour, sera terminée par Slurm. Pour chaque option, des messages seront imprimés au bas du fichier de sortie Slurm, comme le montre [l'exemple ci-dessous](#exemple).

## Compatibilité des versions

### 2026

Un nouveau module `abaqus/2026` contenant la version initiale *Abaqus 2026 Golden/GA* a été installé dans l'environnement par défaut `StdEnv/2023`. Un autre module nommé `abaqus/2026.2614` contenant les derniers *Fix Packs SIMULIA Established Products 2026* actuellement au niveau FD02 (FP.2614) sera mis à disposition dès que possible. Pour vérifier votre configuration, exécutez ce qui suit :

```bash
module load abaqus/2026
module load intel/2024
abaqus verify -all
```

### 2021

!!! warning
    Il est recommandé de cesser d'utiliser `abaqus/2021` installé sous l'ancien `StdEnv/2020` puisque cette version héritée génère une erreur `*** buffer overflow detected ***` sur toutes les grappes récentes. Pour contourner ce problème, une solution de contournement `unshare` a été ajoutée à chaque script Slurm trouvé dans ce wiki. Cependant, cela ne fonctionne que pour les tâches sur un nœud simple et ne garantit pas des résultats précis.

## Soumettre des tâches en lots

Vous trouverez ci-dessous des prototypes de scripts Slurm pour soumettre des simulations parallèles sur un ou plusieurs nœuds de calcul en utilisant des fils et MPI. Dans la plupart des cas, il suffira d'utiliser un des **scripts du répertoire /project** dans une des sections pour un nœud simple. Dans la dernière ligne des scripts, l'argument `memory=` est optionnel et sert aux tâches qui demandent beaucoup de mémoire ou qui posent problème; la valeur de déplacement de 3072Mo pourrait nécessiter un ajustement. Pour obtenir la liste des arguments en ligne de commande, chargez un module Abaqus et lancez `abaqus -help | less`.

Pour une tâche sur un nœud simple d'une durée de moins de 24 heures, le *script du répertoire /project* sous le premier onglet devrait suffire. Pour une tâche de plus longue durée, utilisez un script de redémarrage.

Il est préférable que les tâches qui créent des fichiers de redémarrage volumineux écrivent sur le disque local via l'utilisation de la variable d'environnement `SLURM_TMPDIR` utilisée dans les **scripts de répertoire temporaire** sous les deux onglets les plus à droite des sections d'analyse standard et explicite à nœud unique. Les scripts de redémarrage présentés ici poursuivront les tâches qui ont été interrompues prématurément pour une quelconque raison. De telles interruptions peuvent se produire si une tâche atteint son temps d'exécution maximal demandé avant de se terminer et est arrêtée par la file d'attente ou si le nœud de calcul sur lequel la tâche était exécutée a planté en raison d'une défaillance matérielle inattendue. D'autres types de redémarrage sont possibles en modifiant davantage le fichier d'entrée (non montré) pour continuer une tâche avec des étapes supplémentaires ou modifier l'analyse (consultez la documentation pour plus de détails sur la version).

Les tâches qui exigent beaucoup de mémoire ou beaucoup de ressources de calcul (plus que la capacité d'un nœud simple) devraient utiliser les scripts MPI dans les sections pour nœuds multiples afin de distribuer le calcul sur un ensemble de nœuds arbitraires déterminé automatiquement par l'ordonnanceur. Avant de lancer des tâches de longue durée, il est recommandé d'exécuter de courts tests présentant peu de scalabilité pour déterminer la durée réelle d'exécution (et les exigences en mémoire) en fonction du nombre optimal de cœurs (2, 4, 8, etc.).

### Analyse standard

Les solveurs prennent en charge la parallélisation avec fils et avec MPI. Des scripts pour chaque mode sont présentés sous les onglets pour l'utilisation d'un nœud simple et celle de nœuds multiples. Des scripts pour redémarrer une tâche qui utilise des nœuds multiples ne sont pas présentés pour l'instant.

#### Scripts pour un nœud simple

=== "Script pour le répertoire /project"

```sh title="scriptsp1.txt"
#!/bin/bash
#SBATCH --account=def-group     # Spécifier le compte
#SBATCH --time=00-06:00         # Spécifier jours-heures:minutes
#SBATCH --cpus-per-task=4       # Spécifier le nombre de cœurs
#SBATCH --mem=8G                # Spécifier la mémoire totale > 5G
#SBATCH --nodes=1               # Ne pas modifier !
##SBATCH --constraint=granite   # Décommenter pour spécifier un type de nœud
##SBATCH --gpus-per-node=h100:1 # Décommenter pour spécifier [type:]nombre

module load abaqus/2026         # Dernière version
#module load StdEnv/2020        # Version héritée
#module load abaqus/2021        # Cesser l'utilisation

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

Pour écrire les données de redémarrage en incréments de N=12, le fichier en entrée doit contenir :
`*RESTART, WRITE, OVERLAY, FREQUENCY=12`
Pour écrire les données de redémarrage pour un total de 12 incréments, entrez plutôt :
`*RESTART, WRITE, OVERLAY, NUMBER INTERVAL=12, TIME MARKS=NO`
Pour vérifier l'information complète sur le redémarrage :
`egrep -i "step|start" testsp*.com testsp*.msg testsp*.sta`
Certaines simulations peuvent être améliorées en ajoutant au bas du script la commande Abaqus :
`order_parallel=OFF`

=== "Script de redémarrage pour le répertoire /project"

```sh title="scriptsp2.txt"
#!/bin/bash
#SBATCH --account=def-group     # Spécifier le compte
#SBATCH --time=00-06:00         # Spécifier jours-heures:minutes
#SBATCH --cpus-per-task=4       # Spécifier le nombre de cœurs
#SBATCH --mem=8G                # Spécifier la mémoire totale > 5G
#SBATCH --nodes=1               # Ne pas modifier !
##SBATCH --constraint=granite   # Décommenter pour spécifier un type de nœud
##SBATCH --gpus-per-node=h100:1 # Décommenter pour spécifier [type:]nombre

module load abaqus/2026         # Dernière version
#module load StdEnv/2020        # Version héritée
#module load abaqus/2021        # Cesser l'utilisation

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

Le fichier en entrée pour le redémarrage doit contenir :
`*HEADING`
`*RESTART, READ`

=== "Script pour répertoire temporaire"

```sh title="scriptst1.txt"
#!/bin/bash
#SBATCH --account=def-group     # Spécifier le compte
#SBATCH --time=00-06:00         # Spécifier jours-heures:minutes
#SBATCH --cpus-per-task=4       # Spécifier le nombre de cœurs
#SBATCH --mem=8G                # Spécifier la mémoire totale > 5G
#SBATCH --nodes=1               # Ne pas modifier !
##SBATCH --constraint=granite   # Décommenter pour spécifier un type de nœud
##SBATCH --gpus-per-node=h100:1 # Décommenter pour spécifier [type:]nombre

module load abaqus/2026         # Dernière version
#module load StdEnv/2020        # Version héritée
#module load abaqus/2021        # Cesser l'utilisation

unset SLURM_GTIDS
export MPI_IC_ORDER='tcp'
echo "LM_LICENSE_FILE=$LM_LICENSE_FILE"
echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"
echo "SLURM_SUBMIT_DIR =" $SLURM_SUBMIT_DIR
echo "SLURM_TMPDIR = " $SLURM_TMPDIR

rm -f testst1* testst2*

mkdir $SLURM_TMPDIR/scratch
cd $SLURM_TMPDIR
while sleep 6h; do
   echo "Saving data due to time limit ..."
   cp -fv * $SLURM_SUBMIT_DIR 2>/dev/null
done &
WPID=$!

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

Pour écrire les données de redémarrage en incréments de N=12, le fichier en entrée doit contenir :
`*RESTART, WRITE, OVERLAY, FREQUENCY=12`
Pour écrire les données de redémarrage pour un total de 12 incréments, entrez plutôt :
`*RESTART, WRITE, OVERLAY, NUMBER INTERVAL=12, TIME MARKS=NO`
Pour vérifier l'information complète sur le redémarrage :
`egrep -i "step|start" testst*.com testst*.msg testst*.sta`

=== "Script de redémarrage pour le répertoire temporaire"

```sh title="scriptst2.txt"
#!/bin/bash
#SBATCH --account=def-group    # Spécifier le compte
#SBATCH --time=00-06:00        # Spécifier jours-heures:minutes
#SBATCH --cpus-per-task=4      # Spécifier le nombre de cœurs
#SBATCH --mem=8G               # Spécifier la mémoire totale > 5G
#SBATCH --nodes=1              # Ne pas modifier !
##SBATCH --constraint=granite   # Décommenter pour spécifier un type de nœud
##SBATCH --gpus-per-node=h100:1 # Décommenter pour spécifier [type:]nombre

module load abaqus/2026         # Dernière version
#module load StdEnv/2020        # Version héritée
#module load abaqus/2021        # Cesser l'utilisation

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
   abaqus job=testst2 oldjob=testsp1 input=$SLURM_SUBMIT_DIR/mystd-sim-restart.inp \
   scratch=$SLURM_TMPDIR/scratch cpus=$SLURM_CPUS_ON_NODE interactive \
   mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB" \
   #gpus=$SLURM_GPUS_ON_NODE  # décommenter cette ligne pour utiliser le GPU
fi

{ kill $WPID && wait $WPID; } 2>/dev/null
cp -fv testst2* $SLURM_SUBMIT_DIR
```

Le fichier en entrée pour le redémarrage doit contenir :
`*HEADING`
`*RESTART, READ`

#### Script pour nœuds multiples

Si vous disposez d'une licence qui vous permet d'exécuter des tâches nécessitant beaucoup de mémoire et de calcul, le script suivant pourra effectuer le calcul avec MPI en utilisant un ensemble de nœuds arbitraires idéalement déterminé automatiquement par l'ordonnanceur. Un script modèle pour redémarrer des tâches sur nœuds multiples n'est pas fourni car son utilisation présente des limitations supplémentaires. Avec ce script, vous pouvez utiliser uniquement `abaqus/2026` et versions plus récentes.

```sh title="scriptsp1-mpi.txt"
#!/bin/bash
#SBATCH --account=def-group    # Spécifier le compte
#SBATCH --time=00-06:00        # Spécifier jours-heures:minutes
##SBATCH --nodes=2             # Décommenter pour spécifier (optionnel)
#SBATCH --ntasks=8             # Spécifier le nombre de cœurs
#SBATCH --mem-per-cpu=4G       # Spécifier la mémoire par cœur
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

### Analyse explicite

Les solveurs prennent en charge la parallélisation avec fils et avec MPI. Des scripts pour chaque mode sont présentés sous les onglets pour l'utilisation d'un nœud simple et celle de nœuds multiples. Des modèles de scripts pour redémarrer une tâche qui utilise des nœuds multiples nécessitent plus de tests et ne sont pas présentés pour l'instant.

#### Scripts pour un nœud simple

=== "Script pour le répertoire /project"

```sh title="scriptep1.txt"
#!/bin/bash
#SBATCH --account=def-group    # indiquer le nom du compte
#SBATCH --time=00-06:00        # indiquer la limite de temps (jours-heures:minutes)
#SBATCH --mem=8000M            # indiquer la mémoire totale > 5M
#SBATCH --cpus-per-task=4      # indiquer le nombre de cœurs > 1
#SBATCH --nodes=1              # ne pas modifier

module load abaqus/2026         # Dernière version
#module load StdEnv/2020        # Version héritée
#module load abaqus/2021        # Cesser l'utilisation

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

Pour écrire les données de redémarrage pour un total de 12 incréments, le fichier en entrée doit contenir :
`*RESTART, WRITE, OVERLAY, NUMBER INTERVAL=12, TIME MARKS=NO`
Pour vérifier l'information complète sur le redémarrage :
`egrep -i "step|restart" testep*.com testep*.msg testep*.sta`

=== "Script de redémarrage pour le répertoire /project"

```sh title="scriptep2.txt"
#!/bin/bash
#SBATCH --account=def-group    # indiquer le nom du compte
#SBATCH --time=00-06:00        # indiquer la limite de temps (jours-heures:minutes)
#SBATCH --mem=8000M            # indiquer la mémoire totale > 5M
#SBATCH --cpus-per-task=4      # indiquer le nombre de cœurs > 1
#SBATCH --nodes=1              # ne pas modifier

module load abaqus/2026         # Dernière version
#module load StdEnv/2020        # Version héritée
#module load abaqus/2021        # Cesser l'utilisation

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

=== "Script pour le répertoire temporaire"

```sh title="scriptet1.txt"
#!/bin/bash
#SBATCH --account=def-group    # spécifier le compte
#SBATCH --time=00-06:00        # jours-heures:minutes
#SBATCH --mem=8000M            # mémoire du nœud > 5G
#SBATCH --cpus-per-task=4      # nombre de cœurs > 1
#SBATCH --nodes=1              # ne pas modifier

module load abaqus/2026         # Dernière version
#module load StdEnv/2020        # Version héritée
#module load abaqus/2021        # Cesser l'utilisation

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

Pour écrire les données de redémarrage pour un total de 12 incréments, le fichier en entrée doit contenir :
`*RESTART, WRITE, OVERLAY, NUMBER INTERVAL=12, TIME MARKS=NO`
Pour vérifier l'information complète sur le redémarrage :
`egrep -i "step|restart" testet*.com testet*.msg testet*.sta`

=== "Script de redémarrage pour le répertoire temporaire"

```sh title="scriptet2.txt"
#!/bin/bash
#SBATCH --account=def-group    # spécifier le compte
#SBATCH --time=00-06:00        # jours-heures:minutes
#SBATCH --mem=8000M            # mémoire du nœud > 5G
#SBATCH --cpus-per-task=4      # nombre de cœurs > 1
#SBATCH --nodes=1              # ne pas modifier

module load abaqus/2026         # Dernière version
#module load StdEnv/2020        # Version héritée
#module load abaqus/2021        # Cesser l'utilisation

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

#### Script pour nœuds multiples

Si vous disposez d'une licence qui vous permet d'exécuter des tâches nécessitant beaucoup de mémoire et de calcul, le script suivant pourra effectuer le calcul avec MPI en utilisant un ensemble de nœuds arbitraires idéalement déterminé automatiquement par l'ordonnanceur. Un script modèle pour redémarrer des tâches sur nœuds multiples n'est pas fourni car son utilisation présente des limitations supplémentaires. Avec ce script, vous pouvez utiliser uniquement `abaqus/2026` et versions plus récentes.

```sh title="scriptep1-mpi.txt"
#!/bin/bash
#SBATCH --account=def-group    # Spécifier le compte
#SBATCH --time=00-06:00        # Spécifier jours-heures:minutes
#SBATCH --ntasks=8             # Spécifier le nombre de cœurs
#SBATCH --mem-per-cpu=16000M   # Spécifier la mémoire par cœur
# SBATCH --nodes=2             # Spécifier le nombre de nœuds (optionnel)
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

### Estimer le besoin en termes de mémoire

#### Processus simple

Une estimation de la mémoire totale pour un nœud (`--mem=`) requise par Slurm pour qu'une simulation soit effectuée uniquement en mémoire vive (sans être virtualisée sur le disque scratch) se trouve dans le fichier de sortie Abaqus `test.dat`. Dans l'exemple suivant, la simulation exige une assez grande quantité de mémoire.

```bash
                   M E M O R Y   E S T I M A T E

 PROCESS      FLOATING PT       MINIMUM MEMORY        MEMORY TO
              OPERATIONS           REQUIRED          MINIMIZE I/O
             PER ITERATION           (MB)               (MB)

     1          1.89E+14             3612              96345
```

Une estimation de la mémoire totale pour un processus avec fils sur un nœud unique peut aussi être obtenue en exécutant la simulation de manière interactive sur un nœud de calcul, puis en surveillant la consommation de mémoire à l'aide des commandes `ps` ou `top`.
1) Connectez-vous d'abord à une grappe avec SSH et obtenez une allocation sur un nœud de calcul (comme gra100) et démarrez votre simulation avec :

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

Pour satisfaire complètement la valeur recommandée pour `MEMORY TO OPERATIONS REQUIRED MINIMIZE I/O` (MRMIO), au moins la même quantité de mémoire physique non paginée (RES) doit être disponible pour Abaqus. Étant donné que la RES sera en général inférieure à la mémoire virtuelle (VIRT) d'une quantité relativement constante pour une simulation donnée, il est nécessaire de surallouer légèrement la mémoire du nœud demandée `--mem=`. Dans l'exemple de script ci-dessus, cette surallocation a été codée en dur à une valeur prudente de 3072Mo sur la base des tests initiaux du solveur Abaqus standard. Pour éviter les longs temps d'attente associés aux valeurs élevées de MRMIO, il peut être utile d'étudier l'impact sur les performances de simulation associées à la réduction de la mémoire RES mise à disposition d'Abaqus de manière significative en dessous de la MRMIO. Cela peut être fait en diminuant la valeur de `--mem=` qui à son tour définira une valeur artificiellement basse de `memory=` dans la commande Abaqus (trouvée dans la dernière ligne du script). En faisant cela, il faut s'assurer que RES ne descende pas en dessous de `MINIMUM MEMORY REQUIRED` (MMR) sinon Abaqus fermera à cause d'une mémoire insuffisante (OOM). Par exemple, si votre MRMIO est de 96Go, essayez d'exécuter une série de tâches de test courtes avec `#SBATCH --mem=8G, 16G, 32G, 64G` jusqu'à ce qu'un impact minimal acceptable sur les performances soit trouvé, en notant que des valeurs plus petites entraîneront un espace `/scratch` de plus en plus grand pour les fichiers temporaires.

#### Processus multiples

Pour déterminer la mémoire Slurm requise pour les scripts Slurm multinœuds, les estimations de mémoire (par processus de calcul) nécessaires pour minimiser les entrées/sorties sont fournies dans le fichier de sortie `.dat` pour les tâches terminées. Si `mp_host_split` n'est pas spécifié (ou est égal à 1), le nombre total de processus de calcul sera égal au nombre de nœuds. La valeur de `mem-per-cpu` peut alors être estimée en multipliant l'estimation de mémoire la plus élevée par le nombre de nœuds, puis en divisant par le nombre de tâches (`ntasks`). En revanche, si une valeur pour `mp_host_split` est spécifiée (supérieure à 1), la valeur de `mem-per-cpu` peut être estimée en multipliant l'estimation de mémoire la plus élevée par le nombre de nœuds, puis par la valeur de `mp_host_split`, et en divisant le résultat par le nombre de tâches. Notez que `mp_host_split` doit être inférieur ou égal au nombre de cœurs par nœud attribués par Slurm lors de l'exécution, autrement Abaqus fermera. Ce scénario peut être contrôlé en supprimant le commentaire pour la ligne qui permet de spécifier une valeur pour `tasks-per-node`. Le message suivant, présent dans chaque fichier de sortie, est mentionné ici à titre de référence :

> LE MAXIMUM DE MÉMOIRE POUVANT ÊTRE ALLOUÉ PAR ABAQUS DÉPEND EN GÉNÉRAL DE LA VALEUR DU PARAMÈTRE **MÉMOIRE** ET DE LA QUANTITÉ DE MÉMOIRE PHYSIQUE DISPONIBLE SUR LA MACHINE. VEUILLEZ CONSULTER LE MANUEL D'UTILISATION D'ABAQUS ANALYSIS POUR PLUS DE DÉTAILS. L'UTILISATION RÉELLE DE LA MÉMOIRE ET DE L'ESPACE DISQUE POUR LES DONNÉES DE /SCRATCH DÉPENDRA DE CETTE LIMITE SUPÉRIEURE AINSI QUE DE LA MÉMOIRE REQUISE POUR MINIMISER LES ENTRÉES/SORTIES. SI LA LIMITE SUPÉRIEURE DE MÉMOIRE EST SUPÉRIEURE À LA MÉMOIRE REQUISE POUR MINIMISER LES ENTRÉES/SORTIES, L'UTILISATION RÉELLE DE LA MÉMOIRE SERA PROCHE DE LA VALEUR ESTIMÉE DE **MEMORY TO MINIMIZE I/O** ET L'UTILISATION DU DISQUE DE TRAVAIL SERA PROCHE DE ZÉRO. AUTREMENT, LA MÉMOIRE RÉELLE UTILISÉE SERA PROCHE DE LA LIMITE DE MÉMOIRE MENTIONNÉE PRÉCÉDEMMENT, ET L'UTILISATION DU DISQUE /SCRATCH SERA À PEU PRÈS PROPORTIONNELLE À LA DIFFÉRENCE ENTRE **MEMORY TO MINIMIZE I/O** ESTIMÉE ET LA LIMITE SUPÉRIEURE DE LA MÉMOIRE. TOUTEFOIS, IL EST IMPOSSIBLE D'ÉVALUER AVEC PRÉCISION L'ESPACE /SCRATCH DU DISQUE.

## Utilisation graphique

Nous recommandons d'utiliser Open OnDemand ou Jupyter pour travailler avec des applications graphiques.

### OnDemand

1.  Lancez une session OnDemand sur votre bureau en cliquant sur le lien approprié.
    *   [NIBI](../clusters/nibi.md#accès-via-open-ondemand-ood) : `https://ondemand.sharcnet.ca`
    *   TRILLIUM : `https://ondemand.scinet.utoronto.ca`
2.  Ouvrez une nouvelle fenêtre de terminal et chargez :
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
5.  Pour lancer Abaqus en mode graphique, il faut au moins une licence de calcul non utilisée, selon :
    ```bash
    $ abaqus licensing lmstat -c $ABAQUSLM_LICENSE_FILE -a | grep "Users of cae"
    Users of cae:  (Total of 4 licenses issued;  Total of 3 licenses in use)
    ```

### JupyterLab

1.  Sur votre bureau, lancez une session JupyterHub en cliquant sur une URL ci-dessous.
    *   FIR: `https://jupyterhub.fir.alliancecan.ca`
    *   NARVAL: `https://portail.narval.calculquebec.ca/`
    *   RORQUAL: `https://jupyterhub.rorqual.alliancecan.ca`
2.  Sélectionnez un module COMSOL (par exemple `comsol/6`) dans la section *Modules disponibles* à gauche.
3.  Pour le module sélectionné, cliquez sur *Charger* pour faire afficher l'icône `Comsol (VNC)` sur le bureau.
4.  Cliquez sur l'icône et COMSOL devrait automatiquement démarrer sur un bureau Jupyter à distance.

### VncViewer

!!! warning
    Cette approche est obsolète. Veuillez utiliser un bureau OnDemand ou JupyterLab comme décrit ci-dessus.

1.  Avec un client VncViewer, connectez-vous à un nœud de calcul ou de connexion sans GPU, comme décrit dans [TigerVNC](../interactive/vnc.md).
2.  Ouvrez une nouvelle fenêtre de terminal et entrez :
    ```bash
    module load abaqus/2026
    ```
3.  Lancez l'application avec :
    ```bash
    abaqus cae -mesa
    ```

## Utilisation spécifique au site

### Licence SHARCNET

La licence SHARCNET a été renouvelée jusqu'au 17 janvier 2026. Elle offre une licence gratuite limitée comprenant 2 jetons de calcul et 35 jetons d'exécution, avec des limites d'utilisation de 10 jetons par utilisateur et 15 jetons par groupe. Pour les groupes ayant acquis des jetons dédiés, les limites d'utilisation des jetons gratuits sont ajoutées à leur réservation. Les jetons gratuits sont attribués selon le principe du premier arrivé, premier servi et sont principalement destinés aux tests et à une utilisation légère avant de décider d'acheter ou non des jetons dédiés. Le coût des jetons dédiés (en 2021) était d'environ 110 $ CA par jeton de calcul et 400 $ CA par jeton d'interface graphique : écrivez au [soutien technique](../support/technical_support.md) pour obtenir un devis officiel. La licence peut être utilisée avec un compte de l'Alliance, mais uniquement sur le matériel SHARCNET. Les groupes qui achètent des jetons dédiés pour le serveur de licences SHARCNET ne peuvent les utiliser que sur le matériel SHARCNET, notamment le système [OOD](../clusters/nibi.md#accès-via-open-ondemand-ood) de SHARCNET (pour le mode graphique) ou les grappes Nibi/Dusky (pour soumettre des tâches de calcul par lots à la file d'attente). Avant d'utiliser la licence, vous devez contacter le [soutien technique](../support/technical_support.md) et demander l'accès. Dans votre courriel, veuillez 1) préciser que la demande est destinée à une utilisation sur les systèmes SHARCNET et 2) copier coller l'accord de licence suivant, en indiquant vos nom et prénom ainsi que votre nom d'utilisateur aux emplacements prévus. Veuillez noter que chaque utilisateur doit effectuer cette démarche; elle ne peut être effectuée une seule fois pour un groupe, y compris pour les chercheuses principales et chercheurs principaux ayant acheté leurs propres jetons dédiés.

#### Entente

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

#### Configurer le fichier de licence

Configurez votre fichier de licence comme suit (uniquement sur les systèmes SHARCNET comme les grappes Nibi et Dusky ou sur le système de bureau OOD de SHARCNET). Pour utiliser la licence SHARCNET gratuite, vous devez mettre à jour votre fichier `abaqus.lic` comme suit, puisque le serveur `license3.sharcnet.ca` est définitivement fermé.

```bash
[l2 (nibi login node):~] cat ~/.licenses/abaqus.lic
prepend_path("ABAQUSLM_LICENSE_FILE","27050@license1.computecanada.ca")
```

Si votre tâche se termine anormalement avec le message d'erreur `*** ABAQUS/eliT_CheckLicense rank 0 terminated by signal 11 (Segmentation fault)`, vérifiez si votre fichier `abaqus.lic` contient `ABAQUSLM_LICENSE_FILE` pour Abaqus/202X.
Si le message d'erreur est `License server machine is down or not responding etc.` et que vous utilisez Abaqus/6.14.1, remplacez `ABAQUSLM_LICENSE_FILE` par `LM_LICENSE_FILE`.

#### Interroger le serveur de licences

Connectez-vous à Nibi, chargez Abaqus et exécutez une des commandes suivantes :

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

##### Exemple

L'exemple suivant illustre la situation où un utilisateur soumet successivement deux tâches pour 6 cœurs, nécessitant chacune 12 jetons. L'ordonnanceur a ensuite lancé chaque tâche sur un nœud différent, dans l'ordre de leur soumission. L'utilisateur disposant de 10 jetons Abaqus, la première tâche (27527287) a pu obtenir exactement les 10 jetons nécessaires au démarrage du solveur. La seconde tâche (27527297), n'ayant plus accès à des jetons, est restée en attente (comme le montre la sortie de `lmstat`) jusqu'à la fin de la première, gaspillant ainsi les ressources disponibles et réduisant la juste part de l'utilisateur.

```bash
[l2 (nibi login node):~] sq
           JOBID     USER              ACCOUNT           NAME  ST  TIME_LEFT NODES CPUS TRES_PER_N MIN_MEM NODELIST (REASON)
        27530366  roberpj         cc-debug_cpu  scriptsp2.txt   R    9:56:13     1    6        N/A      8G     c107  (None)
        27530407  roberpj         cc-debug_cpu  scriptsp2.txt   R    9:59:37     1    6        N/A      8G     c292  (None)

[l2 (nibi login node):~] abaqus licensing lmstat -c $ABAQUSLM_LICENSE_FILE -a | egrep "Users|start|queued"
Users of abaqus:  (Total of 78 licenses issued;  Total of 53 licenses in use)
   roberpj c107 /dev/tty (v62.6) (license3.sharcnet.ca/27050 1042), start Mon 11/25 17:15, 10 licenses
   roberpj c292 /dev/tty (v62.6) (license3.sharcnet.ca/27050 125) queued for 10 licenses
```

Pour éviter les problèmes de pénurie de licences lors de la soumission de plusieurs tâches avec des jetons Abaqus coûteux, utilisez soit [une dépendance](../running-jobs/running_jobs.md#annulation-de-tâches-dont-les-conditions-de-dépendance-ne-sont-pas-satisfaites), [un vecteur de tâches](../running-jobs/job_arrays.md), soit au moins configurez [une notification par courriel Slurm](../running-jobs/monitoring_jobs.md#notification-par-courriel) pour savoir quand votre tâche est terminée avant d'en soumettre une autre manuellement.

#### Option 1

Désactiver le démarrage des tâches non interactives (d'analyse) sur un nœud de calcul de la grappe après leur soumission à la file d'attente et leur mise en inactivité (lorsque le nombre de jetons disponibles est insuffisant, ce qui est le comportement par défaut), créez un fichier texte dans votre répertoire de soumission (avant de soumettre la tâche) avec le contenu d'une seule ligne suivant et la tâche se terminera immédiatement.

```ini title="abaqus_v6.env"
[l2 (nibi login node):~/submitdirectory] cat abaqus_v6.env
lmlicensequeuing=OFF
```

Lorsqu'une tâche se termine immédiatement (sans entrer dans un état EN ATTENTE pour une licence), la fin du fichier de sortie Slurm correspondant contiendra des messages tels que :

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

#### Option 2

Spécifiez un réglage en minutes afin qu'une tâche démarrée entre dans un état EN ATTENTE pour une licence avant d'être automatiquement DÉFILÉE et terminée si une licence ne devient pas disponible à temps.

```ini title="abaqus_v6.env"
[l2 (nibi login node):~/submitdirectory] cat abaqus_v6.env
 lmhanglimit=1
```

Lorsqu'une tâche se termine de cette manière, après avoir été mise en file d'attente et qu'aucune licence n'est devenue disponible dans le temps spécifié selon la valeur `lmhanglimit` (1 minute dans cet exemple), les messages à la fin du fichier de sortie Slurm apparaîtront plutôt comme suit :

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

#### Spécifier les ressources de tâche

Pour assurer une utilisation optimale de vos jetons Abaqus et de nos ressources, il est important de spécifier attentivement la mémoire requise et le nombre de cœurs dans votre script Slurm. Les valeurs peuvent être déterminées en soumettant quelques courtes tâches de test à la file d'attente, puis en vérifiant leur utilisation. Pour les tâches **terminées**, utilisez `seff JobNumber` pour afficher la *Mémoire utilisée* totale et l'*Efficacité de la mémoire*. Si l'*Efficacité de la mémoire* est inférieure à environ 90 %, diminuez la valeur du paramètre `#SBATCH --mem=` dans votre script Slurm en conséquence. Notez que la commande `seff JobNumber` affiche également le *Temps CPU utilisé* total et l'*Efficacité CPU*. Si l'*Efficacité CPU* est inférieure à environ 90 %, effectuez des tests de scalabilité pour déterminer le nombre optimal de CPU pour une performance optimale, puis mettez à jour la valeur de `#SBATCH --cpus-per-task=` dans votre script Slurm. Pour les tâches **en cours**, utilisez la commande `srun --overlap --jobid=29821580 --pty top -d 5 -u $USER` pour surveiller le %CPU, le %MEM et la RES pour chaque processus parent Abaqus sur le nœud de calcul. Les colonnes %CPU et %MEM affichent le pourcentage d'utilisation par rapport au total disponible sur le nœud, tandis que la colonne RES indique la taille de la mémoire résidente par processus (au format lisible par l'humain pour les valeurs supérieures à 1 Go). De plus amples informations sur la manière de [surveiller les tâches](../running-jobs/monitoring_jobs.md) sont disponibles sur notre wiki de documentation.

#### Correspondance cœur-jeton

```text
TOKENS 5  6  7  8  10  12  14  16  19  21  25  28  34  38
CORES  1  2  3  4   6   8  12  16  24  32  48  64  96 128
```

où `TOKENS = floor[5 X CORES^0.422]`

Chaque GPU nécessite un jeton additionnel.

### Licence de Western

!!! warning
    Le fichier `abaqus.lic` ci-dessous ne fonctionne plus, car la machine `license4` a été mise hors service définitivement. Par conséquent, toutes les demandes d'accès à une licence Abaqus sur la grappe Dusky à partir du serveur de licences Abaqus Western/Robarts échoueront. Un serveur de remplacement pour `license4` est en préparation. Dès qu'il sera en fonction, le fichier `abaqus.lic` sera mis à jour avec le nouveau nom du serveur et ce message d'avertissement rouge sera supprimé. En attendant, la licence SHARCNET peut être utilisée en suivant la procédure de demande d'accès ci-dessus.

La licence Western est réservée aux chercheurs et chercheuses de Western et ne peut être utilisée que sur du matériel situé sur le campus. Actuellement, seule la grappe Dusky remplit cette condition. Les systèmes Nibi et SHARCNET OOD sont exclus, car ils se trouvent sur le campus de Waterloo. Pour toute question concernant l'utilisation de la licence Abaqus de Western, veuillez contacter l'administrateur du serveur de licences Abaqus de Western à l'adresse <jmilner@robarts.ca>. Vous devrez fournir votre nom d'utilisateur et éventuellement prévoir l'achat de jetons. Si votre demande d'accès est acceptée, vous pourrez configurer votre fichier `abaqus.lic` pour qu'il pointe vers le serveur de licences de Western.

#### Configurer le fichier de licences

```bash
[dus241:~] cat .licenses/abaqus.lic
prepend_path("LM_LICENSE_FILE","27000@license4.sharcnet.ca")
prepend_path("ABAQUSLM_LICENSE_FILE","27000@license4.sharcnet.ca")
```

Par la suite, soumettez votre tâche tel que décrit à la section *Soumettre une tâche sur une grappe* ci-dessus. Si un problème survient, écrivez au [soutien technique](../support/technical_support.md) en indiquant que vous utilisez la licence du site Western sur Dusky. Ajoutez le numéro de la tâche qui pose problème et copiez le ou les messages d'erreur s'il y a lieu.