---
title: "Abaqus/fr"
slug: "abaqus"
lang: "fr"

source_wiki_title: "Abaqus/fr"
source_hash: "3c588f4de7c2da8bb1815a4fcda18e7b"
last_synced: "2026-04-10T14:10:18.226633+00:00"
last_processed: "2026-04-10T14:35:14.854014+00:00"

tags:
  - software

keywords:
  - "scripts Slurm"
  - "Open OnDemand"
  - "Jetons de calcul"
  - "SBATCH"
  - "soutien technique"
  - "gaspillage de ressources"
  - "scripts du répertoire /project"
  - "lmstat"
  - "mp_host_split"
  - "nœuds multiples"
  - "SLURM_SUBMIT_DIR"
  - "parallélisation"
  - "serveur de licences"
  - "fichier en entrée"
  - "fichier de licence"
  - "analyse standard"
  - "analyse explicite"
  - "SHARCNET license server"
  - "redémarrage"
  - "Canadian degree-granting academic institution"
  - "estimation de la mémoire"
  - "données de redémarrage"
  - "memory"
  - "SHARCNET hardware"
  - "nœud simple"
  - "Mode graphique"
  - "licence SHARCNET"
  - "Saving data"
  - "SHARCNET"
  - "Multiple node computing"
  - "serveur de licence"
  - "licence Western"
  - "mystd-sim.inp"
  - "interactive"
  - "répertoire temporaire"
  - "JupyterLab"
  - "ligne de commande"
  - "ABAQUSLM_LICENSE_FILE"
  - "abaqus"
  - "#SBATCH --mem"
  - "jetons Abaqus"
  - "unshare"
  - "jetons"
  - "Licence SHARCNET"
  - "espace /scratch"
  - "EBVERSIONABAQUS"
  - "Abaqus"
  - "SIMULIA Academic Software"
  - "job"
  - "computecanada"
  - "fichier de licences"
  - "Slurm"
  - "VirtualGL"
  - "en attente"
  - "MINIMUM MEMORY REQUIRED (MMR)"
  - "nœuds de calcul"
  - "mode graphique"
  - "simulation"
  - "script de redémarrage"
  - "mémoire insuffisante (OOM)"
  - "module Abaqus"
  - "correspondance cœur-jeton"
  - "serveur de remplacement"
  - "ressources disponibles"
  - "GPU"
  - "RESTART"
  - "script"
  - "argument memory"
  - "SLURM_TMPDIR"
  - "mp_mode=threads"
  - "LM_LICENSE_FILE"
  - "licence Abaqus"
  - "education purposes"
  - "SLURM"
  - "analyse d'éléments finis"
  - "option mesa"
  - "calcul avec MPI"
  - "myexp-sim.inp"
  - "grappe Dusky"
  - "Abaqus FEA"
  - "incréments"
  - "MPI_IC_ORDER"
  - "nœud de calcul"
  - "juste part de l'utilisateur"
  - "script Slurm"
  - "mémoire Slurm"
  - "utilisation des ressources"

questions:
  - "Comment configurer les fichiers de licence (FLEXnet ou DSLS) et les accès réseau pour utiliser sa propre licence Abaqus sur les grappes de calcul ?"
  - "Pourquoi est-il nécessaire de passer au nouveau module abaqus/2026 et quelles modifications cela implique-t-il pour les scripts des utilisateurs ?"
  - "Quelle est la procédure recommandée pour soumettre des simulations parallèles en lots à l'aide de scripts Slurm et comment ajuster la mémoire allouée ?"
  - "Quel répertoire contient les scripts à utiliser pour configurer un nœud simple ?"
  - "Quelle est l'utilité de l'argument optionnel \"memory=\" et dans quels cas faut-il l'ajuster ?"
  - "Quelle commande permet d'obtenir la liste des arguments en ligne de commande après avoir chargé un module Abaqus ?"
  - "Dans quelles situations spécifiques est-il recommandé d'utiliser un script de redémarrage pour une tâche ?"
  - "Comment doit-on configurer et gérer les tâches qui exigent des ressources dépassant la capacité d'un nœud simple ou qui créent des fichiers volumineux ?"
  - "Quelle étape de validation est conseillée avant de lancer des calculs de longue durée afin de déterminer les ressources optimales requises ?"
  - "How does the script utilize Slurm environment variables to configure the computational resources for the Abaqus job?"
  - "What is the specific formula used to allocate memory for the simulation, and how does it relate to the node's total memory?"
  - "What is the purpose of the conditional statement checking if the Abaqus version (`$EBVERSIONABAQUS`) is greater than or equal to 2026?"
  - "Quelles sont les commandes spécifiques à inclure dans le fichier d'entrée Abaqus pour configurer l'écriture et la lecture des données de redémarrage ?"
  - "Comment le script de soumission SLURM adapte-t-il la commande d'exécution d'Abaqus en fonction de la version du logiciel (2021 par rapport à 2026) ?"
  - "Quelle stratégie est mise en place dans le script du répertoire temporaire pour sauvegarder automatiquement les données vers le répertoire de soumission pendant l'exécution ?"
  - "Quelles commandes doivent être ajoutées au fichier d'entrée pour configurer l'écriture des données de redémarrage selon une fréquence ou un intervalle donné ?"
  - "Comment le script SLURM gère-t-il la sauvegarde des données en cours d'exécution et l'adaptation aux différentes versions d'Abaqus ?"
  - "Que doit obligatoirement contenir le fichier d'entrée pour effectuer la lecture des données lors d'un redémarrage ?"
  - "What is the purpose of the background loop that copies files every 6 hours?"
  - "Which SLURM environment variables are logged and used for directory management in the script?"
  - "What specific action is triggered if the Abaqus version is determined to be 2021?"
  - "Comment la mémoire allouée pour la tâche interactive est-elle calculée à partir des variables d'environnement SLURM ?"
  - "Quelles directives spécifiques le fichier d'entrée doit-il obligatoirement contenir pour permettre un redémarrage ?"
  - "Quelle commande le script utilise-t-il pour transférer les fichiers de résultats vers le répertoire de soumission à la fin de l'exécution ?"
  - "Quelles sont les conditions requises, notamment en termes de version du logiciel, pour utiliser le script de calcul sur nœuds multiples avec MPI ?"
  - "Quels modes de parallélisation sont pris en charge par les solveurs lors d'une analyse explicite ?"
  - "Pourquoi les scripts modèles permettant de redémarrer des tâches sur des nœuds multiples ne sont-ils pas fournis dans cette documentation ?"
  - "Comment doit-on configurer le fichier d'entrée pour écrire les données de redémarrage pour un nombre spécifique d'incréments ?"
  - "Quelles sont les différences de commande d'exécution entre les versions 2021 et 2026 d'Abaqus dans les scripts de soumission Slurm ?"
  - "Comment le script conçu pour le répertoire temporaire assure-t-il la sauvegarde régulière des données vers le répertoire de soumission pendant l'exécution ?"
  - "How does the execution method of the Abaqus job change when the software version is 2026 or newer?"
  - "Which SLURM environment variables are used to configure the computational resources like memory and CPUs for the simulation?"
  - "What is the purpose of using the `unshare` command and its associated flags in the first execution branch?"
  - "What specific parameters and resource allocations are defined for the Abaqus job execution in this script?"
  - "How does the script utilize Slurm environment variables to configure the simulation's resources?"
  - "What is the purpose of the conditional statement checking the `$EBVERSIONABAQUS` variable?"
  - "Comment doit-on configurer le fichier en entrée pour écrire les données de redémarrage pour un nombre précis d'incréments ?"
  - "Comment le script de redémarrage gère-t-il le transfert et la sauvegarde régulière des fichiers entre le répertoire de soumission et le répertoire temporaire ?"
  - "Quelles sont les conditions et limitations spécifiques mentionnées pour l'exécution d'un calcul Abaqus sur des nœuds multiples avec MPI ?"
  - "Comment peut-on obtenir l'estimation de la mémoire requise directement à partir du fichier de sortie d'Abaqus ?"
  - "Quelles sont les étapes pour surveiller la consommation de mémoire de manière interactive lors de l'exécution d'une simulation sur un nœud de calcul ?"
  - "Quelles sont les conséquences sur la simulation et l'espace disque si la mémoire allouée est inférieure à la valeur recommandée pour minimiser les entrées/sorties (MRMIO) ?"
  - "What specific hardware resources, such as memory per core and number of nodes, are requested using the SLURM directives in the script?"
  - "Which software version is being loaded, and how are the MPI environment variables configured for this job?"
  - "What is the purpose of the final shell commands regarding the license file variables and the removal of previous test files?"
  - "Que se passe-t-il si la mémoire allouée descend en dessous du \"MINIMUM MEMORY REQUIRED\" (MMR) lors de l'utilisation d'Abaqus ?"
  - "Quelle méthode est recommandée pour déterminer la quantité de mémoire optimale à allouer pour une tâche ?"
  - "Quel est l'impact de l'utilisation d'une plus petite quantité de mémoire sur l'espace de stockage temporaire (/scratch) ?"
  - "Comment peut-on estimer la mémoire requise (mem-per-cpu) pour les scripts Slurm multinœuds en fonction de l'utilisation du paramètre mp_host_split ?"
  - "Quel est l'impact de la limite supérieure de mémoire sur l'utilisation réelle de la mémoire et de l'espace disque (/scratch) pour minimiser les entrées/sorties dans Abaqus ?"
  - "Quelles sont les étapes et les options de commande à utiliser pour lancer l'application Abaqus en mode graphique via Open OnDemand selon le type de nœud (avec ou sans GPU) ?"
  - "Dans quelles conditions matérielles doit-on ajouter l'option \"mesa\" pour lancer l'application ?"
  - "Comment optimiser les performances graphiques d'Abaqus sur un nœud avec GPU prenant en charge VirtualGL ?"
  - "Quelle option matérielle précise faut-il sélectionner dans le menu déroulant de Nibi Desktop ?"
  - "Quelles sont les étapes à suivre pour lancer une session graphique via JupyterLab ?"
  - "Quelles sont les restrictions et les limites d'utilisation associées aux jetons gratuits de la licence SHARCNET ?"
  - "Quelle procédure administrative chaque utilisateur doit-il accomplir auprès du soutien technique avant de pouvoir utiliser la licence SHARCNET ?"
  - "Comment doit-on configurer le fichier de licence Abaqus sur les systèmes SHARCNET et quelles solutions appliquer en cas d'erreur de segmentation ou de serveur inactif ?"
  - "Quelles commandes faut-il utiliser pour interroger le serveur de licences afin de vérifier l'état des tâches et la disponibilité des produits Abaqus ?"
  - "Quel est l'impact sur les ressources de calcul et la priorité de l'utilisateur lorsqu'une tâche lancée reste en attente de jetons de licence ?"
  - "On what specific hardware must the SIMULIA Academic Software be used according to this agreement?"
  - "What type of institutional affiliation is required for the user to access the software?"
  - "What are the permitted and prohibited purposes for using the software under this license?"
  - "Pourquoi la seconde tâche est-elle restée en attente jusqu'à la fin de la première au lieu d'utiliser les ressources disponibles ?"
  - "Quel rôle la commande ''lmstat'' a-t-elle joué dans l'identification de ce problème de gestion des tâches ?"
  - "Quelles informations spécifiques sur l'état et l'allocation des ressources de la tâche de l'utilisateur \"roberpj\" sont fournies par la sortie de la console ?"
  - "Comment peut-on éviter les problèmes de pénurie de licences lors de la soumission de plusieurs tâches Abaqus ?"
  - "Quelles commandes doivent être utilisées pour vérifier et optimiser l'utilisation des ressources (mémoire et CPU) des tâches terminées et en cours d'exécution ?"
  - "Quel est l'état actuel du serveur de licences de Western et quelle alternative est proposée aux utilisateurs en attendant son remplacement ?"
  - "Quel est le problème actuel affectant les demandes d'accès à la licence Abaqus sur la grappe Dusky ?"
  - "Quelles actions seront entreprises au niveau du système une fois que le serveur de remplacement sera mis en fonction ?"
  - "Quelle solution de rechange les utilisateurs peuvent-ils utiliser en attendant la résolution définitive du problème ?"
  - "Quelles sont les conditions d'admissibilité et les restrictions matérielles pour utiliser la licence Western ?"
  - "Quelle est la procédure à suivre et qui doit-on contacter pour demander l'accès à la licence Abaqus de Western ?"
  - "Comment configurer le fichier de licences et quelles informations fournir au soutien technique en cas de problème lors de la soumission d'une tâche ?"
  - "Quelles sont les conditions d'admissibilité et les restrictions matérielles pour utiliser la licence Western ?"
  - "Quelle est la procédure à suivre et qui doit-on contacter pour demander l'accès à la licence Abaqus de Western ?"
  - "Comment configurer le fichier de licences et quelles informations fournir au soutien technique en cas de problème lors de la soumission d'une tâche ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Abaqus FEA est un progiciel commercial pour l'analyse d'éléments finis et l'ingénierie assistée par ordinateur.

## Licence

### Utiliser votre licence

Des modules Abaqus sont disponibles sur nos grappes, mais vous devez posséder votre propre licence. Pour configurer votre compte sur les grappes que vous voulez utiliser, connectez-vous et créez sur chacune un fichier `$HOME/.licenses/abaqus.lic` qui contient la ligne ci-dessous. Remplacez ensuite `port@server` par le numéro du port flexlm et l'adresse IP (ou le nom complet du domaine) de votre serveur de licence Abaqus. Si vous voulez utiliser la version 6.14.1, remplacez ABAQUSLM_LICENSE_FILE par LM_LICENSE_FILE.

```ini title="abaqus.lic"
prepend_path("ABAQUSLM_LICENSE_FILE","port@server")
```

Si votre licence n'est pas configurée pour une grappe en particulier, les administrateurs de systèmes des deux parties devront effectuer certaines modifications. Ceci est nécessaire pour que les ports flexlm et TCP de votre serveur Abaqus puissent être rejoints par tous les nœuds de calcul quand vos tâches dans la queue seront exécutées. Pour que nous puissions vous assister dans cette tâche, écrivez au [soutien technique](technical-support.md) en indiquant
*   le numéro du port flexlm
*   le numéro du port statique
*   l'adresse IP de votre serveur de licence Abaqus.
En retour vous recevrez une liste d'adresses IP et votre administrateur de système pourra ouvrir les pare-feu de votre serveur local pour que la grappe puisse se connecter via les deux ports. Une entente spéciale doit habituellement être négociée et signée avec SIMULIA pour qu'une telle licence puisse être utilisée à distance avec notre matériel.

### Serveurs FLEXnet et DSLS

Comme c'était le cas avec les modules déjà installés, `abaqus/2026` est configuré pour fonctionner avec le serveur de licence Simulia `FLEXnet` par défaut, tout comme le serveur de licence gratuit de SHARCNET. Pour utiliser un serveur de licence `DSLS` de votre établissement, vous devez créer les fichiers texte `abaqus_v6.env` et `DSLicSrv.txt` dans le répertoire utilisé pour soumettre votre simulation (voir le code ci-dessous). Ils seront lus automatiquement au lancement d'Abaqus et la reconfiguration se fera en conséquence.

```bash
[l2 (login node):~/mysimdir] cat abaqus_v6.env
license_server_type=DSLS
dsls_license_config="DSLicSrv.txt"
```

```text title="DSLicSrv.txt"
YOUR-SERVER-HOSTNAME:PORT-NUMBER
```

## Compatibilité des versions

### Nouveau module

!!! danger "Attention"
    Un nouveau module pour `abaqus/2026` est installé dans l'environnement par défaut `StdEnv/2023`. La nouvelle version résout la source de l'erreur **buffer overflow detected** qui survenait sur toutes les récentes grappes avec `abaqus/2021`. Les scripts Slurm présentés dans cette page ont été adaptés pour fonctionner avec `abaqus/2026` et `abaqus/2021` lorsque possible; vous devez donc modifier tous les scripts Slurm que vous utilisez. Le module `abaqus/2026` contient la version initiale *Abaqus 2026 Golden*. Un autre module nommé `abaqus/2026.2606` contient les mises à niveau *Abaqus 2026 FP.CFA.2606* et sera installé prochainement.

## Soumettre des tâches en lots

Vous trouverez ci-dessous des prototypes de scripts Slurm pour soumettre des simulations parallèles sur un ou plusieurs nœuds de calcul en utilisant des fils et MPI. Dans la plupart des cas, il suffira d'utiliser un des **scripts du répertoire /project** dans une des sections pour un nœud simple. Dans la dernière ligne des scripts, l'argument `memory=` est optionnel et sert aux tâches qui demandent beaucoup de mémoire ou qui posent problème; la valeur de déplacement de 3072Mo pourrait nécessiter un ajustement. Pour obtenir la liste des arguments en ligne de commande, chargez un module Abaqus et lancez `abaqus -help | less`.

Pour une tâche sur un nœud simple d'une durée de moins de 24 heures, le *script du répertoire /project* sous le premier onglet devrait suffire. Pour une tâche de plus longue durée, utilisez un script de redémarrage.

Il est préférable que les tâches qui créent des fichiers de redémarrage volumineux écrivent sur le disque local via l'utilisation de la variable d'environnement `SLURM_TMPDIR` utilisée dans les **scripts de répertoire temporaire** sous les deux onglets les plus à droite des sections d'analyse standard et explicite à nœud unique. Les scripts de redémarrage présentés ici poursuivront les tâches qui ont été interrompues prématurément pour une quelconque raison. De telles interruptions peuvent se produire si une tâche atteint son temps d'exécution maximal demandé avant de se terminer et est arrêtée par la file d'attente ou si le nœud de calcul sur lequel la tâche était exécutée a planté en raison d'une défaillance matérielle inattendue. D'autres types de redémarrage sont possibles en modifiant davantage le fichier d'entrée (non montré) pour continuer une tâche avec des étapes supplémentaires ou modifier l'analyse (consultez la documentation pour plus de détails sur la version).

Les tâches qui exigent beaucoup de mémoire ou beaucoup de ressources de calcul (plus que la capacité d'un nœud simple) devraient utiliser les scripts MPI dans les sections pour nœuds multiples afin de distribuer le calcul sur un ensemble de nœuds arbitraires déterminé automatiquement par l'ordonnanceur. Avant de lancer des tâches de longue durée, il est recommandé d'exécuter de courts tests présentant peu de scalabilité pour déterminer la durée réelle d'exécution (et les exigences en mémoire) en fonction du nombre optimal de cœurs (2, 4, 8, etc.).

### Analyse standard

Les solveurs prennent en charge la parallélisation avec fils et avec MPI. Des scripts pour chaque mode sont présentés sous les onglets pour l'utilisation d'un nœud simple et celle de nœuds multiples. Des scripts pour redémarrer une tâche qui utilise des nœuds multiples ne sont pas présentés pour l'instant.

#### Scripts pour un nœud simple

=== "Script pour le répertoire /project"

    ```bash title="scriptsp1.txt"
    #!/bin/bash
    #SBATCH --account=def-group     # Spécifier le compte
    #SBATCH --time=00-06:00         # Indiquer la limite de temps (jours-heures:minutes)
    #SBATCH --cpus-per-task=4       # Indiquer le nombre de cœurs
    #SBATCH --mem=8G                # Indiquer la mémoire totale > 5G
    #SBATCH --nodes=1               # Ne pas modifier !
    ##SBATCH --constraint=granite   # Décommenter pour spécifier un type de nœud
    ##SBATCH --gpus-per-node=h100:1 # Décommenter pour spécifier [type:]nombre

    module load abaqus/2026         # Version la plus récente
    #module load StdEnv/2020        # Ancienne version
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

    Pour écrire les données de redémarrage en incréments de N=12, le fichier en entrée doit contenir
    `*RESTART, WRITE, OVERLAY, FREQUENCY=12`
    Pour écrire les données de redémarrage pour un total de 12 incréments, entrez plutôt
    `*RESTART, WRITE, OVERLAY, NUMBER INTERVAL=12, TIME MARKS=NO`
    Pour vérifier l'information complète sur le redémarrage
    `egrep -i "step|start" testsp*.com testsp*.msg testsp*.sta`
    Certaines simulations peuvent être améliorées en ajoutant au bas du script la commande Abaqus
    `order_parallel=OFF`

=== "Script de redémarrage pour le répertoire /project"

    ```bash title="scriptsp2.txt"
    #!/bin/bash
    #SBATCH --account=def-group     # Spécifier le compte
    #SBATCH --time=00-06:00         # Indiquer la limite de temps (jours-heures:minutes)
    #SBATCH --cpus-per-task=4       # Indiquer le nombre de cœurs
    #SBATCH --mem=8G                # Indiquer la mémoire totale > 5G
    #SBATCH --nodes=1               # Ne pas modifier !
    ##SBATCH --constraint=granite   # Décommenter pour spécifier un type de nœud
    ##SBATCH --gpus-per-node=h100:1 # Décommenter pour spécifier [type:]nombre

    module load abaqus/2026         # Version la plus récente
    #module load StdEnv/2020        # Ancienne version
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

    Le fichier en entrée pour le redémarrage doit contenir
    `*HEADING`
    `*RESTART, READ`

=== "Script pour répertoire temporaire"

    ```bash title="scriptst1.txt"
    #!/bin/bash
    #SBATCH --account=def-group     # Spécifier le compte
    #SBATCH --time=00-06:00         # Indiquer la limite de temps (jours-heures:minutes)
    #SBATCH --cpus-per-task=4       # Indiquer le nombre de cœurs
    #SBATCH --mem=8G                # Indiquer la mémoire totale > 5G
    #SBATCH --nodes=1               # Ne pas modifier !
    ##SBATCH --constraint=granite   # Décommenter pour spécifier un type de nœud
    ##SBATCH --gpus-per-node=h100:1 # Décommenter pour spécifier [type:]nombre


    module load abaqus/2026         # Version la plus récente
    #module load StdEnv/2020        # Ancienne version
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
       echo "Sauvegarde des données en raison de la limite de temps ..."
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

    Pour écrire les données de redémarrage en incréments de N=12, le fichier en entrée doit contenir
    `*RESTART, WRITE, OVERLAY, FREQUENCY=12`
    Pour écrire les données de redémarrage pour un total de 12 incréments, entrez plutôt
    `*RESTART, WRITE, OVERLAY, NUMBER INTERVAL=12, TIME MARKS=NO`
    Pour vérifier l'information complète sur le redémarrage
    `egrep -i "step|start" testst*.com testst*.msg testst*.sta`

=== "Script de redémarrage pour le répertoire temporaire"

    ```bash title="scriptst2.txt"
    #!/bin/bash
    #SBATCH --account=def-group    # Spécifier le compte
    #SBATCH --time=00-06:00        # Indiquer la limite de temps (jours-heures:minutes)
    #SBATCH --cpus-per-task=4      # Indiquer le nombre de cœurs
    #SBATCH --mem=8G               # Indiquer la mémoire totale > 5G
    #SBATCH --nodes=1              # Ne pas modifier !
    ##SBATCH --constraint=granite   # Décommenter pour spécifier un type de nœud
    ##SBATCH --gpus-per-node=h100:1 # Décommenter pour spécifier [type:]nombre

    module load abaqus/2026         # Version la plus récente
    #module load StdEnv/2020        # Ancienne version
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
       echo "Sauvegarde des données en raison de la limite de temps ..."
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

    Le fichier en entrée pour le redémarrage doit contenir
    `*HEADING`
    `*RESTART, READ`

#### Script pour nœuds multiples

Si vous disposez d'une licence qui vous permet d'exécuter des tâches nécessitant beaucoup de mémoire et de calcul, le script suivant pourra effectuer le calcul avec MPI en utilisant un ensemble de nœuds arbitraires idéalement déterminé automatiquement par l'ordonnanceur. Un script modèle pour redémarrer des tâches sur nœuds multiples n'est pas fourni car son utilisation présente des limitations supplémentaires. Avec ce script, vous pouvez utiliser uniquement `abaqus/2026` et versions plus récentes.

```bash title="scriptsp1-mpi.txt"
#!/bin/bash
#SBATCH --account=def-group    # Spécifier le compte
#SBATCH --time=00-06:00        # Indiquer la limite de temps (jours-heures:minutes)
##SBATCH --nodes=2             # Décommenter pour spécifier (optionnel)
#SBATCH --ntasks=8             # Indiquer le nombre de cœurs
#SBATCH --mem-per-cpu=4G       # Spécifier la mémoire par cœur
##SBATCH --tasks-per-node=4    # Décommenter pour spécifier (optionnel)
#SBATCH --cpus-per-task=1      # Ne pas modifier !

module load abaqus/2026         # Version la plus récente

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

    ```bash title="scriptep1.txt"
    #!/bin/bash
    #SBATCH --account=def-group    # indiquer le nom du compte
    #SBATCH --time=00-06:00        # indiquer la limite de temps (jours-heures:minutes)
    #SBATCH --mem=8000M            # indiquer la mémoire totale > 5M
    #SBATCH --cpus-per-task=4      # indiquer le nombre de cœurs > 1
    #SBATCH --nodes=1              # ne pas modifier

    module load abaqus/2026         # Version la plus récente
    #module load StdEnv/2020        # Ancienne version
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

    Pour écrire les données de redémarrage pour un total de 12 incréments, le fichier en entrée doit contenir
    `*RESTART, WRITE, OVERLAY, NUMBER INTERVAL=12, TIME MARKS=NO`
    Pour vérifier l'information complète sur le redémarrage
    `egrep -i "step|restart" testep*.com testep*.msg testep*.sta`

=== "Script de redémarrage pour le répertoire /project"

    ```bash title="scriptep2.txt"
    #!/bin/bash
    #SBATCH --account=def-group    # indiquer le nom du compte
    #SBATCH --time=00-06:00        # indiquer la limite de temps (jours-heures:minutes)
    #SBATCH --mem=8000M            # indiquer la mémoire totale > 5M
    #SBATCH --cpus-per-task=4      # indiquer le nombre de cœurs > 1
    #SBATCH --nodes=1              # ne pas modifier

    module load abaqus/2026         # Version la plus récente
    #module load StdEnv/2020        # Ancienne version
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

    ```bash title="scriptet1.txt"
    #!/bin/bash
    #SBATCH --account=def-group    # indiquer le nom du compte
    #SBATCH --time=00-06:00        # jours-heures:minutes
    #SBATCH --mem=8000M            # mémoire du nœud > 5G
    #SBATCH --cpus-per-task=4      # nombre de cœurs > 1
    #SBATCH --nodes=1              # ne pas modifier

    module load abaqus/2026         # Version la plus récente
    #module load StdEnv/2020        # Ancienne version
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

    Pour écrire les données de redémarrage pour un total de 12 incréments, le fichier en entrée doit contenir
    `*RESTART, WRITE, OVERLAY, NUMBER INTERVAL=12, TIME MARKS=NO`
    Pour vérifier l'information complète sur le redémarrage
    `egrep -i "step|restart" testet*.com testet*.msg testet*.sta`

=== "Script de redémarrage pour le répertoire temporaire"

    ```bash title="scriptet2.txt"
    #!/bin/bash
    #SBATCH --account=def-group    # indiquer le nom du compte
    #SBATCH --time=00-06:00        # jours-heures:minutes
    #SBATCH --mem=8000M            # mémoire du nœud > 5G
    #SBATCH --cpus-per-task=4      # nombre de cœurs > 1
    #SBATCH --nodes=1              # ne pas modifier

    module load abaqus/2026         # Version la plus récente
    #module load StdEnv/2020        # Ancienne version
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

```bash title="scriptep1-mpi.txt"
#!/bin/bash
#SBATCH --account=def-group    # Spécifier le compte
#SBATCH --time=00-06:00        # Indiquer la limite de temps (jours-heures:minutes)
#SBATCH --ntasks=8             # Indiquer le nombre de cœurs
#SBATCH --mem-per-cpu=16000M   # Spécifier la mémoire par cœur
# SBATCH --nodes=2             # Spécifier le nombre de nœuds (optionnel)
#SBATCH --cpus-per-task=1      # Ne pas modifier !

module load abaqus/2026        # Version la plus récente

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

Une estimation de la mémoire totale pour un nœud (--mem=) requise par Slurm pour qu'une simulation soit effectuée uniquement en mémoire vive (sans être virtualisée sur le disque scratch) se trouve dans le fichier de sortie Abaqus `test.dat`. Dans l'exemple suivant, la simulation exige une assez grande quantité de mémoire.

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
salloc --time=0:30:00 --cpus-per-task=8 --mem=64G --account=def-nom-du-pi
module load StdEnv/2020
module load abaqus/2021
unset SLURM_GTIDS
abaqus job=test input=Sample.inp scratch=$SLURM_TMPDIR cpus=8 mp_mode=threads interactive
```

2) Ensuite, via SSH, connectez-vous au nœud de calcul et lancez top.

```bash
ssh c50
```

```bash
top -u $USER
```

3) Observez les colonnes `VIRT` and `RES` jusqu'à ce que des valeurs de mémoire maximales stables soient atteintes.

Pour satisfaire complètement la valeur recommandée pour **MEMORY TO OPERATIONS REQUIRED MINIMIZE I/O** (MRMIO), au moins la même quantité de mémoire physique non échangée (RES) doit être disponible pour Abaqus. Étant donné que la RES sera en général inférieure à la mémoire virtuelle (VIRT) d'une quantité relativement constante pour une simulation donnée, il est nécessaire de surallouer légèrement la mémoire du nœud demandée `-mem=`. Dans l'exemple de script ci-dessus, cette surallocation a été codée en dur à une valeur prudente de 3072Mo sur la base des tests initiaux du solveur Abaqus standard. Pour éviter les longs temps d'attente associés aux valeurs élevées de MRMIO, il peut être utile d'étudier l'impact sur les performances de simulation associées à la réduction de la mémoire RES mise à disposition d'Abaqus de manière significative en dessous de la MRMIO. Cela peut être fait en diminuant la valeur de `-mem=` qui à son tour définira une valeur artificiellement basse de `memory=` dans la commande Abaqus (trouvée dans la dernière ligne du script). En faisant cela, il faut s'assurer que RES ne descende pas en dessous de **MINIMUM MEMORY REQUIRED** (MMR) sinon Abaqus fermera à cause d'une mémoire insuffisante (OOM). Par exemple, si votre MRMIO est de 96Go, essayez d'exécuter une série de tâches de test courtes avec `#SBATCH --mem=8G, 16G, 32G, 64G` jusqu'à ce qu'un impact minimal acceptable sur les performances soit trouvé, en notant que des valeurs plus petites entraîneront un espace `/scratch` de plus en plus grand pour les fichiers temporaires.

### Processus multiples

Pour déterminer la mémoire Slurm requise pour les scripts Slurm multinœuds, les estimations de mémoire (par processus de calcul) nécessaires pour minimiser les entrées/sorties sont fournies dans le fichier de sortie `.dat` pour les tâches terminées. Si `mp_host_split` n'est pas spécifié (ou est égal à 1), le nombre total de processus de calcul sera égal au nombre de nœuds. La valeur de `mem-per-cpu` peut alors être estimée en multipliant l'estimation de mémoire la plus élevée par le nombre de nœuds, puis en divisant par le nombre de tâches (`ntasks`). En revanche, si une valeur pour `mp_host_split` est spécifiée (supérieure à 1), la valeur de `mem-per-cpu` peut être estimée en multipliant l'estimation de mémoire la plus élevée par le nombre de nœuds, puis par la valeur de `mp_host_split`, et en divisant le résultat par le nombre de tâches. Notez que `mp_host_split` doit être inférieur ou égal au nombre de cœurs par nœud attribués par Slurm lors de l'exécution, autrement Abaqus fermera. Ce scénario peut être contrôlé en supprimant le commentaire pour la ligne qui permet de spécifier une valeur pour tasks-per-node. Le message suivant, présent dans chaque fichier de sortie, est mentionné ici à titre de référence :

!!! note "Remarque"
    LE MAXIMUM DE MÉMOIRE POUVANT ÊTRE ALLOUÉ PAR ABAQUS DÉPEND EN GÉNÉRAL DE LA VALEUR DU PARAMÈTRE `MÉMOIRE` ET DE LA QUANTITÉ DE MÉMOIRE PHYSIQUE DISPONIBLE SUR LA MACHINE. VEUILLEZ CONSULTER LE MANUEL D'UTILISATION D'ABAQUS ANALYSIS POUR PLUS DE DÉTAILS. L'UTILISATION RÉELLE DE LA MÉMOIRE ET DE L'ESPACE DISQUE POUR LES DONNÉES DE `/SCRATCH` DÉPENDRA DE CETTE LIMITE SUPÉRIEURE AINSI QUE DE LA MÉMOIRE REQUISE POUR MINIMISER LES ENTRÉES/SORTIES. SI LA LIMITE SUPÉRIEURE DE MÉMOIRE EST SUPÉRIEURE À LA MÉMOIRE REQUISE POUR MINIMISER LES ENTRÉES/SORTIES, L'UTILISATION RÉELLE DE LA MÉMOIRE SERA PROCHE DE LA VALEUR ESTIMÉE DE **MEMORY TO MINIMIZE I/O** ET L'UTILISATION DU DISQUE DE TRAVAIL SERA PROCHE DE ZÉRO. AUTREMENT, LA MÉMOIRE RÉELLE UTILISÉE SERA PROCHE DE LA LIMITE DE MÉMOIRE MENTIONNÉE PRÉCÉDEMMENT, ET L'UTILISATION DU DISQUE `/SCRATCH` SERA À PEU PRÈS PROPORTIONNELLE À LA DIFFÉRENCE ENTRE **MEMORY TO MINIMIZE I/O** ESTIMÉE ET LA LIMITE SUPÉRIEURE DE LA MÉMOIRE. TOUTEFOIS, IL EST IMPOSSIBLE D'ÉVALUER AVEC PRÉCISION L'ESPACE `/SCRATCH` DU DISQUE.

## Utilisation graphique

Nous recommandons d'utiliser Open OnDemand ou Jupyter pour travailler avec des applications graphiques.

### OnDemand

1.  Lancez une session OnDemand sur votre bureau en cliquant sur le lien approprié.
    [NIBI](nibi.md#acces-via-open-ondemand-ood) : `https://ondemand.sharcnet.ca`
    TRILLIUM : `https://ondemand.scinet.utoronto.ca`

2.  Ouvrez une nouvelle fenêtre de terminal et chargez
    ```bash
    module load abaqus/2026
    ```

3.  Lancez l'application en mode graphique avec l'option `cae`. Si vous êtes sur un nœud sans GPU ou sur un nœud avec GPU où VirtualGL n'est pas pris en charge, ajoutez l'option `mesa`.
    ```bash
    abaqus cae -mesa
    ```

4.  Si vous avez besoin d'une meilleure performance graphique et êtes sur un nœud avec GPU où VirtualGL est pris en charge, lancez Abaqus sans l'option `mesa`. Dans Nibi Desktop, sélectionnez h100 (80GB) dans le menu déroulant.
    ```bash
    abaqus cae
    ```

5.  Pour lancer Abaqus en mode graphique, il faut au moins une licence de calcul non utilisée, selon

    ```bash
    abaqus licensing lmstat -c $ABAQUSLM_LICENSE_FILE -a | grep "Users of cae"
    ```
    Users of cae: (Total of 4 licenses issued; Total of 3 licenses in use)

### JupyterLab

1.  Sur votre bureau, lancez une session JupyterHub en cliquant sur une URL ci-dessous.
    FIR: `https://jupyterhub.fir.alliancecan.ca`
    NARVAL: `https://portail.narval.calculquebec.ca/`
    RORQUAL: `https://jupyterhub.rorqual.alliancecan.ca`
2.  Sélectionnez un module COMSOL (par exemple `comsol/6`) dans la section *Module disponible* de gauche.
3.  Pour le module sélectionné, cliquez sur *Charger* pour faire afficher l'icône `Comsol (VNC)` sur le bureau.
4.  Cliquez sur l'icône et COMSOL devrait automatiquement démarrer sur un bureau Jupyter à distance.

### VncViewer

Cette approche est obsolète. Veuillez utiliser un bureau OnDemand ou JupyterLab comme décrit ci-dessus.

1.  Avec un client VncViewer, connectez-vous à un nœud de calcul ou de connexion sans GPU, comme décrit dans [TigerVNC](vnc.md).
2.  Ouvrez une nouvelle fenêtre de terminal et entrez
    ```bash
    module load abaqus/2026
    ```
3.  Lancez l'application avec
    ```bash
    abaqus cae -mesa
    ```

## Utilisation spécifique au site

### Licence SHARCNET

La licence SHARCNET a été renouvelée jusqu'au 17 janvier 2026. Elle offre une licence gratuite limitée comprenant 2 jetons de calcul et 35 jetons d'exécution, avec des limites d'utilisation de 10 jetons par utilisateur et 15 jetons par groupe. Pour les groupes ayant acquis des jetons dédiés, les limites d'utilisation des jetons gratuits sont ajoutées à leur réservation. Les jetons gratuits sont attribués selon le principe du premier arrivé, premier servi et sont principalement destinés aux tests et à une utilisation légère avant de décider d'acheter ou non des jetons dédiés. Le coût des jetons dédiés (en 2021) était d'environ 110 $ CA par jeton de calcul et 400 $ CA par jeton d'interface graphique : écrivez au [soutien technique](technical-support.md) pour obtenir un devis officiel. La licence peut être utilisée avec un compte de l'Alliance, mais uniquement sur le matériel SHARCNET. Les groupes qui achètent des jetons dédiés pour le serveur de licences SHARCNET ne peuvent les utiliser que sur le matériel SHARCNET, notamment le système SHARCNET [OOD](nibi.md#acces-via-open-ondemand-ood) (pour le mode graphique) ou les grappes Nibi/Dusky (pour soumettre des tâches de calcul par lots à la file d'attente). Avant d'utiliser la licence, vous devez contacter le [soutien technique](technical-support.md) et demander l'accès. Dans votre courriel, veuillez 1) préciser que la demande est destinée à une utilisation sur les systèmes SHARCNET et 2) copier coller l'accord de licence suivant, en indiquant vos nom et prénom ainsi que votre nom d'utilisateur aux emplacements prévus. Veuillez noter que chaque utilisateur doit effectuer cette démarche; elle ne peut être effectuée une seule fois pour un groupe, y compris pour les chercheuses principales et chercheurs principaux ayant acheté leurs propres jetons dédiés.

#### Entente

```text
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
```

#### Configurer le fichier de licence

Configurez votre fichier de licence comme suit (uniquement sur les systèmes SHARCNET comme les grappes Nibi et Dusky ou sur le système de bureau OOD de SHARCNET). Pour utiliser la licence SHARCNET gratuite, vous devez mettre à jour votre fichier `abaqus.lic` comme suit, puisque le serveur `license3.sharcnet.ca` est définitivement fermé.

```bash
[l2 (nibi login node):~] cat ~/.licenses/abaqus.lic
prepend_path("ABAQUSLM_LICENSE_FILE","27050@license1.computecanada.ca")
```

Si votre tâche se termine anormalement avec le message d'erreur `*** ABAQUS/eliT_CheckLicense rank 0 terminated by signal 11 (Segmentation fault)`, vérifiez si votre fichier `abaqus.lic` contient `ABAQUSLM_LICENSE_FILE` pour Abaqus/202X.
Si le message d'erreur est `License server machine is down or not responding etc.` et que vous utilisez Abaqus/6.14.1, remplacez ABAQUSLM_LICENSE_FILE par `LM_LICENSE_FILE`.

#### Interroger le serveur de licences

Connectez-vous à Nibi, chargez Abaqus et exécutez une des commandes suivante :

```bash
ssh nibi.alliancecan.ca
module load StdEnv/2020
module load abaqus
```

I) Vérifiez s'il y a des tâches lancées et des tâches dans la queue pour le serveur de licence SHARCNET.

```bash
abaqus licensing lmstat -c $ABAQUSLM_LICENSE_FILE -a | egrep "Users|start|queued"
```
II) Vérifiez s'il y a des tâches lancées et des tâches dans la queue pour le serveur de licence SHARCNET et s'il indique des réservations de produits par groupe d'acquisition.

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

```text
[l2 (nibi login node):~] sq
           JOBID     USER              ACCOUNT           NAME  ST  TIME_LEFT NODES CPUS TRES_PER_N MIN_MEM NODELIST (REASON)
        27530366  roberpj         cc-debug_cpu  scriptsp2.txt   R    9:56:13     1    6        N/A      8G     c107  (None)
        27530407  roberpj         cc-debug_cpu  scriptsp2.txt   R    9:59:37     1    6        N/A      8G     c292  (None)

[l2 (nibi login node):~] abaqus licensing lmstat -c $ABAQUSLM_LICENSE_FILE -a | egrep "Users|start|queued"
Users of abaqus:  (Total of 78 licenses issued;  Total of 53 licenses in use)
   roberpj c107 /dev/tty (v62.6) (license3.sharcnet.ca/27050 1042), start Mon 11/25 17:15, 10 licenses
   roberpj c292 /dev/tty (v62.6) (license3.sharcnet.ca/27050 125) queued for 10 licenses
```

Pour éviter les problèmes de pénurie de licences lors de la soumission de plusieurs tâches avec des jetons Abaqus coûteux, utilisez soit [une dépendance](running-jobs.md#annulation-de-taches-dont-les-conditions-de-dependance-ne-sont-pas-satisfaites), [un vecteur](job-arrays.md), soit au moins configurez [une notification par courriel Slurm](monitoring-jobs.md#notification-par-courriel) pour savoir quand votre tâche est terminée avant d'en soumettre une autre manuellement.

#### Spécifier les ressources de la tâche

Pour garantir une utilisation optimale de vos jetons Abaqus et de nos ressources, il est important de spécifier avec précision la mémoire et le nombre de cœurs (ncpus) requis dans votre script Slurm. Vous pouvez déterminer ces valeurs en soumettant quelques courtes tâches de test à la file d'attente, puis en vérifiant l'utilisation des ressources. Pour les tâches **terminées**, utilisez `seff JobNumber` pour afficher la *mémoire utilisée* et son *efficacité*. Si l'efficacité de la mémoire est inférieure à environ 90 %, diminuez la valeur du paramètre `#SBATCH --mem=` dans votre script Slurm. Notez que la commande `seff JobNumber` affiche également le *temps CPU utilisé* et l'*efficacité du CPU*. Si l'efficacité du CPU est inférieure à environ 90 %, effectuez des testez la scalabilité pour déterminer le nombre optimal de CPU afin d'obtenir de meilleures performances, puis mettez à jour la valeur de `#SBATCH --cpus-per-task=` dans votre script Slurm. Pour les tâches en cours d'exécution, utilisez la commande `srun --overlap --jobid=29821580 --pty top -d 5 -u $USER` pour surveiller les pourcentages d'utilisation du CPU (%CPU), de la mémoire (%MEM) et de la mémoire résidente (RES) de chaque processus parent Abaqus. Les colonnes %CPU et %MEM affichent le pourcentage d'utilisation par rapport à la mémoire totale disponible du nœud, tandis que la colonne RES indique la taille de la mémoire résidente par CPU (dans un format lisible pour les valeurs supérieures à 1Go). Vous trouverez plus d'information dans [Suivi des tâches](monitoring-jobs.md#suivi-des-taches).

#### Correspondance cœur-jeton

| TOKENS | CORES |
|--------|-------|
| 5      | 1     |
| 6      | 2     |
| 7      | 3     |
| 8      | 4     |
| 10     | 6     |
| 12     | 8     |
| 14     | 12    |
| 16     | 16    |
| 19     | 24    |
| 21     | 32    |
| 25     | 48    |
| 28     | 64    |
| 34     | 96    |
| 38     | 128   |

où `TOKENS = floor[5 X CORES^0.422]`

Chaque GPU nécessite un jeton additionnel.

### Licence de Western

!!! warning "Avertissement"
    Le fichier `abaqus.lic` ci-dessous ne fonctionne plus, car la machine `license4.sharcnet.ca` a été mise hors service définitivement. Par conséquent, toutes les demandes d'accès à une licence Abaqus sur la grappe Dusky à partir du serveur de licences Abaqus Western/Robarts échoueront. Un serveur de remplacement pour `license4.sharcnet.ca` est en préparation. Dès qu'il sera en fonction, le fichier `abaqus.lic` sera mis à jour avec le nouveau nom du serveur et ce message d'avertissement rouge sera supprimé. En attendant, la licence SHARCNET peut être utilisée en suivant la procédure de demande d'accès ci-dessus.

La licence Western est réservée aux chercheurs et chercheuses de Western et ne peut être utilisée que sur du matériel situé sur le campus. Actuellement, seulement la grappe Dusky remplit cette condition. Les systèmes Nibi et SHARCNET OOD sont exclus, car ils se trouvent sur le campus de Waterloo. Pour toute question concernant l'utilisation de la licence Abaqus de Western, veuillez contacter l'administrateur du serveur de licences Abaqus de Western à l'adresse `jmilner@robarts.ca`. Vous devrez fournir votre nom d'utilisateur et éventuellement prévoir l'achat de jetons. Si votre demande d'accès est acceptée, vous pourrez configurer votre fichier `abaqus.lic` pour qu'il pointe vers le serveur de licences de Western.

#### Configurer le fichier de licences

```bash
[dus241:~] cat .licenses/abaqus.lic
prepend_path("LM_LICENSE_FILE","27000@license4.sharcnet.ca")
prepend_path("ABAQUSLM_LICENSE_FILE","27000@license4.sharcnet.ca")
```
Par la suite, soumettez votre tâche tel que décrit à la section **Soumettre des tâches en lots** ci-dessus. Si un problème survient, écrivez au [soutien technique](technical-support.md) en indiquant que vous utilisez la licence du site Western sur Dusky. Ajoutez le numéro de la tâche qui pose problème et copiez le ou les messages d'erreur s'il y a lieu.