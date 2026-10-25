---
title: "Nibi/fr"
slug: "nibi"
lang: "fr"

source_wiki_title: "Nibi/fr"
source_hash: "1180829af2cb4398aec234b3bed80bdf"
last_synced: "2026-10-25T00:54:39.630071+00:00"
last_processed: "2026-10-25T01:43:35.938208+00:00"

tags:
  []

keywords:
  - "JupyterLab"
  - "export-controlled data"
  - "espace $HOME"
  - "Nvidia H100 SXM"
  - "prise en charge de VDI via OOD"
  - "288 GPU H100 NVIDIA"
  - "Slack invitation"
  - "/project"
  - "partage de données"
  - "VDI"
  - "option Slurm --gpus"
  - "répertoires utilisateurs"
  - "134 400 CPU"
  - "accès à internet"
  - "nœuds"
  - "Indigenous or community-governed data"
  - "NVLink"
  - "API key creation"
  - "/nearline"
  - "Nibi"
  - "mkdir"
  - "3 T"
  - "MIG"
  - "navigateur"
  - "JupyterLab via OOD"
  - "environnement virtuel Python"
  - "token usage monitoring"
  - "LiteLLM account"
  - "ROCm"
  - "confidential third-party data"
  - "interconnexion 200/400 Gbit/s"
  - "Open OnDemand (OOD)"
  - "mémoire unifiée"
  - "GPU H100-80gb"
  - "Intel 6972P"
  - "LiteLLM"
  - "financial records"
  - "384 MB cache L3"
  - "quota souple de 1 TB sur /scratch"
  - "stockage parallèle 25 Po"
  - "status page"
  - "accès via Open OnDemand"
  - "instantané"
  - "Brine"
  - "MI300A"

questions:
  - "Comment demander l'accès au système Nibi via le CCDB et quel délai d'activation faut‑il prévoir ?"
  - "Quelles sont les capacités de calcul (CPU, GPU) et de stockage (espace, bande passante) offertes par la grappe Nibi ?"
  - "Quelles sont les règles de gestion du répertoire /scratch sur Nibi, notamment la limite souple, le délai de grâce de 60 jours et les conséquences d’un dépassement ?"
  - "Quelle configuration CPU (modèle, fréquence et cache) est indiquée pour chaque ensemble de spécifications ?"
  - "Quelle quantité de mémoire (RAM) et de stockage local (en Go ou Mo) est disponible dans chaque configuration ?"
  - "Quel(s) modèle(s) de GPU sont mentionnés et comment sont‑ils connectés (ex. NVLink) dans la dernière configuration ?"
  - "Quels sont les différents types d’instances GPU H100 proposées (complètes et MIG) et quelles sont leurs capacités en mémoire et en puissance de calcul ?"
  - "Comment demander, avec les options Slurm, un GPU H100 complet ou une instance MIG spécifique pour une tâche ?"
  - "Quelles sont les particularités d’accès à Internet et de création de répertoires dans les espaces /project et /nearline sur les nœuds du cluster ?"
  - "Pourquoi les répertoires des utilisateurs ne sont-ils plus créés automatiquement dans /project et /nearline ?"
  - "Comment créer ses propres répertoires dans les espaces /project et /nearline du groupe avec la commande <code>mkdir</code> ?"
  - "Quel avantage cela offre‑t‑il aux groupes pour organiser leurs espaces /project et /nearline et partager les données entre les membres ?"
  - "Pourquoi les fichiers d'index et les petits fichiers stockés sur /nearline ne sont‑ils pas sauvegardés ni archivés sur ruban ?"
  - "Quel est le quota souple de 1 TB sur /scratch, comment peut‑on le dépasser et quelles sont les conséquences après 60 jours ?"
  - "Quelles sont les deux méthodes proposées pour lancer JupyterLab via Open OnDemand sur la grappe Nibi, et comment les mettre en œuvre ?"
  - "Quels sont les prérequis et les étapes nécessaires pour exécuter correctement des tâches sur les nœuds AMD MI300A ?"
  - "Comment récupérer un fichier supprimé à l’aide de la commande « oops » et quelles sont les limites de cette méthode ?"
  - "Quelles précautions doit‑on prendre lorsqu’on utilise la plateforme Brine AI‑as‑a‑Service et comment obtenir un accès ?"
  - "Comment lancer JupyterLab en spécifiant le répertoire de travail et quel répertoire apparaît dans le panneau de gauche ?"
  - "Où s'ouvre l'interface de JupyterLab et comment le contenu du répertoire $HOME est‑il présenté à l'utilisateur ?"
  - "Quelle alternative Nibi propose‑t‑il à la VDI et quels avantages offre le portail Open OnDemand (OOD) en termes de performances matérielles et de prise en charge logicielle ?"
  - "What types of data are prohibited from being sent to the centrally hosted AI service?"
  - "How can a user request access to the SHARCNET Brine service?"
  - "What steps must a user follow after accepting the terms of service to receive a LiteLLM account?"
  - "What steps must a user follow to create and use an API key for accessing the Brine service?"
  - "Which additional features does the LiteLLM‑powered backend offer beyond basic API key creation?"
  - "How can users stay informed about service outages or receive updates about the Brine AIaaS?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

| Clé | Valeur |
| :----------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Disponibilité            | 31 juillet 2025                                                                                                                                                                |
| Nœud de connexion SSH    | `nibi.alliancecan.ca`                                                                                                                                                          |
| Nœud d'automatisation    | *`robot.nibi.alliancecan.ca`*                                                                                                                                                  |
| Interface web            | [ondemand.sharcnet.ca](https://ondemand.sharcnet.ca)                                                                                                                           |
| Collection Globus        | [alliancecan#nibi](https://app.globus.org/file-manager?origin_id=07baf15f-d7fd-4b6a-bf8a-5b5ef2e229d3)                                                                         |
| Nœud de copie (rsync, scp, sftp, etc.) | utiliser les nœuds de connexion                                                                                                                                              |
| Portail                  | [portal.nibi.sharcnet.ca](https://portal.nibi.sharcnet.ca)                                                                                                                     |
| Plateforme IA            | brine.sharcnet.ca/ui/                                                                                                                                 |

Dans la langue anishinaabe, Nibi est un terme qui désigne l'eau. Cette nouvelle grappe offre 134 400 CPU et 288 GPU H100 de NVIDIA. Conçue par [Hypertec](https://www.hypertec.com/), Nibi est hébergée et exploitée par [SHARCNET](https://www.sharcnet.ca/) à l'Université de Waterloo.

## Accès

Vous devez [demander l'accès dans CCDB](https://ccdb.alliancecan.ca/me/access_systems), en sélectionnant *Ressources --> Accès aux systèmes*.

*   Dans la liste des systèmes, sélectionnez Nibi.
*   Cliquez sur le bouton **Je demande l'accès**.

L'activation de votre accès pourrait prendre environ une heure.

## Stockage

Stockage parallèle : 25 Po, [SSD (Solid-State Drive)](https://fr.wikipedia.org/wiki/SSD) de [VAST Data](https://www.vastdata.com/) pour `/home`, `/project` et `/scratch`.

!!! note
    Vast comptabilise différemment l'espace utilisé pour calculer les quotas. La taille apparente de vos fichiers est prise en compte alors que certaines configurations de Lustre compressent les fichiers de manière transparente et comptabilisent l'espace utilisé après compression.

!!! warning
    Nibi utilise un nouveau mécanisme expérimental pour gérer `/scratch`. Comme sur tous les systèmes, vous disposez d'une limite souple et d'une limite stricte, mais sur Nibi, la limite souple est basse (1 TB) et vous disposez d'un délai de grâce de 60 jours. Après l'expiration de ce délai, la limite souple est imposée (plus aucune création ni extension de fichier). Pour corriger ceci, votre utilisation doit revenir sous la limite souple.

## Interconnexion

*   Ethernet Nokia, 200/400G
    *   Bande passante pour nœuds CPU, 200 Gbit/s
    *   Bande passante non bloquante pour tous les nœuds GPU Nvidia, 200 Gbit/s
    *   Bande passante pour tous les nœuds GPU AMD, 200 Gbit/s
    *   Connexion aux nœuds de stockage VAST, 24x100 Gbit/s
    *   Liaisons montantes (*uplinks*) pour tous les nœuds, 400 Gbit/s; blocage 2:1

La topologie du réseau est décrite dans le fichier `/etc/slurm/topology.conf`.

Pour améliorer la performance des tâches multi-nœuds fortement couplées, vous pouvez forcer l'utilisation d'un seul commutateur (*network switch*) en ajoutant l'option suivante au script de la tâche :

```slurm
#SBATCH --switches=1
```

## Caractéristiques des nœuds

| Nœuds | Cœurs | Mémoire disponible | Stockage local | CPU                                          | GPU                                                               |
| :---- | :---- | :----------------- | :------------- | :------------------------------------------- | :---------------------------------------------------------------- |
| 700   | 192   | 748G ou 766000M    | 3T             | 2 x Intel 6972P @ 2.4 GHz, 384MB cache L3    |                                                                   |
| 10    | 192   | 6000G ou 6144000M  | 3T             | 2 x Intel 6972P @ 2.4 GHz, 384MB cache L3    |                                                                   |
| 36    | 112   | 2000G ou 2048000M  | 11T            | 2 x Intel 8570 @ 2.1 GHz, 300MB cache L3     | 8 x Nvidia H100 SXM (80 GB), connecté via NVLink                  |
| 6     | 96    | 495G ou 507000M    | 3T             | 4 x AMD MI300A @ 2.1GHz (Zen4+CDNA3)         | Les cœurs CPU et les GPU CDNA3 sont dans le même socket, avec une mémoire unifiée. Voir les instructions ci-dessous. |

### Instances de GPU

**Noms des instances de GPU**

|                       | Modèle ou instance   | Nom court           | Sans unité   | Par sa mémoire | Nom complet                            |
| :-------------------- | :------------------- | :------------------ | :----------- | :------------- | :------------------------------------- |
| **GPU**               | **H100-80gb**        | `h100`              | `h100`       | `h100_80gb`    | `nvidia_h100_80gb_hbm3`                |
|                       |                      |                     |              |                |                                        |
| **MIG**               | **H100-1g.10gb**     | `h100_1g.10gb`      | `h100_1.10`  | `h100_10gb`    | `nvidia_h100_80gb_hbm3_1g.10gb`        |
|                       | **H100-2g.20gb**     | `h100_2g.20gb`      | `h100_2.20`  | `h100_20gb`    | `nvidia_h100_80gb_hbm3_2g.20gb`        |
|                       | **H100-3g.40gb**     | `h100_3g.40gb`      | `h100_3.40`  | `h100_40gb`    | `nvidia_h100_80gb_hbm3_3g.40gb`        |

Pour demander un ou plusieurs GPU H100 complets, utilisez une des options Slurm suivantes :

*   **un H100-80gb** : `--gpus=h100:1` ou `--gpus=h100_80gb:1`
*   **plusieurs H100-80gb** par nœud :
    *   `--gpus-per-node=h100:2`
    *   `--gpus-per-node=h100:3`
    *   `--gpus-per-node=h100:4`
*   **plusieurs GPU H100 complets** distribués arbitrairement : `--gpus=h100:n` (remplacer `n` par le nombre de GPU que vous voulez)

Environ la moitié des nœuds GPU utilisent [la technologie MIG](../programming/multi-instance_gpu.md). Trois tailles d'instances sont disponibles :

*   **H100-1g.10gb**: 1/8^e^ de la puissance de calcul, mémoire GPU de 10 Go
*   **H100-2g.20gb**: 2/8^e^ de la puissance de calcul, mémoire GPU de 20 Go
*   **H100-3g.40gb**: 3/8^e^ de la puissance de calcul, mémoire GPU de 40 Go

Pour demander **une et une seule instance GPU** pour une tâche de calcul, utilisez l'option correspondante :

*   **H100-1g.10gb** : `--gpus=h100_1g.10gb:1`
*   **H100-2g.20gb** : `--gpus=h100_2g.20gb:1`
*   **H100-3g.40gb** : `--gpus=h100_3g.40gb:1`

Pour le nombre maximum de cœurs CPU et le maximum de mémoire recommandés par instance GPU, voir [Ratios dans les *bundles*](../running-jobs/allocations_and_compute_scheduling.md#ratios-dans-les-bundles).

## Particularités

### Accès à Internet

Tous les nœuds ont accès à Internet; aucune autorisation de pare-feu spéciale ou proxy n'est nécessaire.

### /project et /nearline

Les répertoires des utilisateurs ne sont plus créés par défaut dans `/project` et `/nearline`. Vous pouvez toujours créer vos propres répertoires dans les espaces `/project` et `/nearline` du groupe à l'aide de `mkdir`. Ceci permet aux groupes de décider de l'organisation de leurs espaces `/project` et `/nearline` pour le partage de données entre les membres.
Sur `/nearline`, les [fichiers d'index](../storage-and-data/using_nearline_storage.md) et les autres petits fichiers ne sont pas sauvegardés ni archivés sur ruban.

### Quota pour /scratch

!!! warning
    Un quota souple de 1 TB sur `/scratch` s'applique à chaque utilisateur. Ce quota souple peut être dépassé pendant 60 jours maximum, après quoi aucun fichier supplémentaire ne peut être écrit sur `/scratch`. Les fichiers peuvent être réécrits une fois que l'utilisateur a supprimé suffisamment de fichiers pour ramener son utilisation `/scratch` totale sous 1 TB. Pour plus d'information, voir [Stockage et gestion de fichiers](../storage-and-data/storage_and_file_management.md).

### Accès via Open OnDemand (OOD)

Il est possible d'accéder à la grappe Nibi simplement via un navigateur web. Nibi utilise Open OnDemand (OOD), une plateforme web qui simplifie l'accès en fournissant une interface web aux nœuds de connexion et un environnement de bureau à distance. Pour vous connecter à Nibi, rendez-vous sur [ondemand.sharcnet.ca/](https://ondemand.sharcnet.ca/) et connectez-vous avec [l'authentification multifacteur](../getting-started/multifactor_authentication.md). Une interface conviviale s'affichera, proposant des options pour ouvrir un terminal Bash ou lancer une session de bureau à distance.

### Utilisation de JupyterLab via OOD

Vous pouvez exécuter JupyterLab de manière interactive via le [portail Nibi Open OnDemand](https://ondemand.sharcnet.ca).

**Option 1** : Travailler dans un environnement préconfiguré (même que [JupyterHub](../interactive/jupyterhub.md))

Quand la connexion au [portail Nibi Open OnDemand](https://ondemand.sharcnet.ca) est établie, cliquez sur **Compute Node** dans le menu du haut et sélectionnez **Nibi JupyterLab**. Une page sera affichée dans laquelle un formulaire vous permet de demander une nouvelle session Nibi JupyterLab.

Après avoir rempli le formulaire avec les détails, cliquez sur **Launch** pour soumettre votre demande. Quand l'état des modifications pour Nibi JupyterLab passe à **Running**, cliquez sur **Connect to Jupyter** pour ouvrir JupyterLab dans le navigateur web.

Pour les détails sur la préconfiguration, voir [Interface JupyterLab](../interactive/jupyterlab.md#interface-jupyterlab).

**Option 2** : Travailler dans un [environnement virtuel Python](../software/python.md) que vous avez créé

Quand la connexion au [portail Nibi Open OnDemand](https://ondemand.sharcnet.ca) est établie, cliquez sur **Compute Node** dans le menu du haut et sélectionnez **Compute Desktop**. Une page sera affichée dans laquelle un formulaire vous permet de demander une nouvelle session Compute Desktop.

Après avoir rempli le formulaire avec les détails, cliquez sur **Launch** pour soumettre votre demande. Quand le bureau Compute passe à **Running**, cliquez sur **Launch Compute Desktop** pour vous connecter au bureau. Un bureau Linux sera affiché.

Sur le bureau Compute, faites un clic droit dans une zone vide; un menu contextuel apparaît. Sélectionnez **Open in Terminal** pour ouvrir une fenêtre de terminal où vous pouvez créer ou activer votre environnement virtuel Python dans lequel JupyterLab est installé.

Si JupyterLab n'est pas installé dans l'environnement virtuel Python que vous souhaitez utiliser, vous pouvez l'installer avec la commande :

```bash
pip install --no-index jupyterlab
```

Vous pouvez ensuite lancer JupyterLab à partir de votre environnement virtuel Python avec :

```bash
jupyter-lab --notebook-dir $HOME
```

JupyterLab s'ouvre dans le navigateur sur le bureau et le contenu de votre espace `$HOME` est listé dans le panneau de gauche.

### Prise en charge de VDI via OOD

Nibi n'offre plus d'infrastructure de bureau virtuel (VDI), mais fournit un environnement de bureau à distance via le [portail Open OnDemand (OOD)](https://ondemand.sharcnet.ca/) avec des performances matérielles et une prise en charge logicielle améliorées.

### Nœuds AMD MI300A

Il faut présentement demander les MI300A comme des nœuds entiers. Vous avez la responsabilité de vous assurer que les processus de votre tâche sont exécutés avec les liaisons correctes des cœurs et de la mémoire. Dans l'exemple ci-dessous, le script utilise quatre processus.

!!! warning "Remarque importante"
    Pour une bonne utilisation des nœuds MI300A, compilez votre code avec ROCm. La compilation avec CUDA ne fonctionne pas parce que les GPU AMD ne sont pas pris en charge.

En date de mai 2026, notre pile logicielle ne prend pas en charge les nœuds MI300A et aucun module ne permet la compilation avec ROCm. Vous pouvez installer vous-même des logiciels avec la suite d'outils ROCm qui se trouve dans le répertoire `/opt/rocm`. Si vous avez besoin d'assistance, écrivez au [soutien technique](../support/technical_support.md).

```sh title="simple_job.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=24
#SBATCH --gpus=mi300a:4
#SBATCH --mem=100g
#SBATCH --time=00:02:00

# verify GPUS are available (optional)

rocm-smi

# run program compiled with ROCm support for MI300A
```

### Récupérer des fichiers supprimés

Nibi dispose d'un système de sauvegarde qui crée un instantané de vos fichiers dans `/home` et `/project` toutes les 30 minutes; ces instantanés sont sauvegardés pour une période de deux semaines. Si vous supprimez accidentellement un fichier, vous pourrez peut-être le récupérer à partir de ces instantanés, à condition qu'il ait été supprimé il y a moins de deux semaines. Cependant, si vous modifiez un fichier après la dernière sauvegarde, pour ensuite le supprimer, il ne pourra pas être récupéré.

Pour localiser un fichier supprimé, utilisez la commande `oops` pour vérifier le répertoire courant, ou spécifiez un autre répertoire où faire la recherche. Pour récupérer un fichier, copiez-le depuis le chemin retourné par la commande `oops` à l'aide d'un outil standard comme `cp`. Les instantanés sont en lecture seule; vous ne pouvez donc ni supprimer ni modifier les fichiers qu'ils contiennent, vous devez d'abord les copier. Ne faites pas référence aux fichiers des instantanés dans vos scripts de soumission de tâches.

```bash
[username@<node>.nibi]$ ls
dont_delete_me.txt
[username@<node>.nibi]$ rm dont_delete_me.txt
[username@<node>.nibi]$ ls
[username@<node>.nibi]$ oops
Deleted files found in snapshots:
./.snapshot/backup_2026-04-01_18_00_00_UTC/dont_delete_me.txt
Files created less than 9 min ago (2026-04-01 14:00:00-04:00) are not yet backed up
Files deleted more than 0 days ago (2026-04-01 13:30:00-04:00) please submit a help ticket
[username@<node>.nibi]$ cp ./.snapshot/backup_2026-04-01_18_00_00_UTC/dont_delete_me.txt .
[username@<node>.nibi]$ ls
dont_delete_me.txt
```

## Brine : plateforme IA-en-tant-que-service

Dans le cadre d'un nouvel effort, SHARCNET a lancé une plateforme IA-en-tant-que-service hébergée au sein du centre de données Nibi. Ce service offre aux chercheurs canadiens l'accès à des modèles d'IA hébergés sur l'infrastructure de SHARCNET, sans l'attente habituelle des files d'attente de HPC.

Brine offre une API toujours active, compatible OpenAI, pour les modèles d'IA hébergés qui prennent en charge le clavardage, l'appel d'outils et la transcription audio. La disponibilité des modèles et leurs paramètres sont décrits [ici](https://github.com/sharcnet/brine-examples/tree/main/model-cards).

Brine fonctionne sur le matériel du centre de données Nibi, de sorte que les données sont traitées au Canada plutôt que d'être envoyées à un fournisseur commercial à l'extérieur du pays. Malgré cela, les utilisateurs ne devraient pas soumettre de données sensibles.

!!! warning "Données sensibles"
    L'information personnelle ou de santé, les dossiers d'étudiants ou financiers, les identifiants, les données confidentielles de tiers, les données soumises au contrôle des exportations, les données autochtones ou gouvernées par la communauté, et toute autre information que vous n'êtes pas autorisé à envoyer à un service d'IA centralisé sont toutes considérées comme des données sensibles.

Pour demander l'accès, envoyez un courriel à help@sharcnet.ca en mentionnant "SHARCNET Brine".

### Obtenir l'accès

Après avoir accepté les conditions d'utilisation, vous recevrez un courriel d'invitation dans votre boîte de réception vous invitant à vous inscrire pour un nouveau compte LiteLLM. Il s'agit d'un nouveau compte dédié uniquement à ce service.

!!! warning "Avertissement"
    Nous avons reçu des alertes indiquant que certaines boîtes de réception signalent l'invitation comme pourriel. Veuillez vérifier votre courrier indésirable.

Après vous être connecté, une interface devrait s'afficher, vous invitant à créer une nouvelle clé. Créez la clé pour vous-même, nommez-la et ne la partagez pas avec d'autres.

Cette clé est requise pour accéder au service en tant qu'API, tel que décrit dans le dépôt des [exemples Brine](https://github.com/sharcnet/brine-examples). Ceci inclut des exemples en Python, Javascript et Curl.

### Interface LiteLLM

Le *backend* de ce service est alimenté par [LiteLLM](https://www.litellm.ai/) et offre plusieurs fonctionnalités intéressantes, au-delà de la création de clés API et du service de modèles :

*   Suivre votre consommation de *tokens* et l'activité de votre clé
*   Comparer les résultats des modèles dans la fonctionnalité *playground*
*   Ajouter des *Vector stores*
*   Gérer les connexions MCP

### État du service

Pour être au courant des changements apportés à ce service, une invitation à un canal Slack est disponible sur demande.

Pour les alertes et les mises à jour en cas de panne, veuillez consulter la page d'état [ici](https://status.alliancecan.ca/system/Nibi%20AIaaS:%20Brine).