---
title: "Nibi/fr"
slug: "nibi"
lang: "fr"

source_wiki_title: "Nibi/fr"
source_hash: "4651c5119adf048b9f86606693893d07"
last_synced: "2026-09-06T00:43:13.954271+00:00"
last_processed: "2026-09-06T02:39:49.630443+00:00"

tags:
  []

keywords:
  - "navigateur"
  - "/nearline"
  - "stockage parallèle 25 Po SSD VAST Data"
  - "interconnexion 200/400 Gbit/s Ethernet Nokia"
  - "Nvidia H100 SXM"
  - "quota souple de 1 TB sur /scratch"
  - "384MB cache L3"
  - "mémoire unifiée"
  - "commande oops"
  - "exécution interactive de JupyterLab"
  - "MIG"
  - "Open OnDemand (OOD)"
  - "option Slurm --gpus"
  - "environnement virtuel Python"
  - "répertoires des utilisateurs"
  - "nœuds AMD MI300A"
  - "compilation ROCm"
  - "accès à l'internet"
  - "instantané de sauvegarde"
  - "accès via CCDB"
  - "134 400 CPU et 288 GPU H100"
  - "JupyterLab"
  - "VDI"
  - "Nibi"
  - "prise en charge du bureau à distance (VDI)"
  - "partage de données"
  - "espace $HOME"
  - "/project"
  - "NVLink"
  - "mkdir"
  - "accès via Open OnDemand"
  - "GPU H100-80gb"
  - "3T"
  - "Intel 6972P"
  - "GPU AMD non pris en charge par CUDA"

questions:
  - "Comment demander l'accès au système Nibi via le CCDB et quel est le délai d'activation prévu ?"
  - "Quels sont les quotas de stockage, le mécanisme de gestion du répertoire /scratch (limite souple de 1 TB et délai de grâce de 60 jours) et comment la taille apparente des fichiers est‑elle comptabilisée ?"
  - "Quelles sont les caractéristiques des nœuds (CPU, mémoire, stockage local, GPU H100) et les bandes passantes réseau disponibles pour les communications entre nœuds et vers le stockage VAST ?"
  - "Quels processeurs sont proposés dans chaque configuration et quelles sont leurs spécifications (fréquence, cache, nombre de cœurs) ?"
  - "Quelle est la capacité de mémoire vive (RAM) et de stockage local associée à chaque option ?"
  - "Quelle configuration comprend des GPU Nvidia H100 SXM et comment ces GPU sont-ils connectés entre eux ?"
  - "Quels sont les différents types d’instances GPU H100 (complètes et MIG) et quelles sont leurs capacités de mémoire et de puissance de calcul ?"
  - "Comment demander un GPU H100 complet ou une instance MIG spécifique via les options Slurm (ex. --gpus, --gpus-per-node) ?"
  - "Quelles sont les particularités d’accès à Internet et de création de répertoires dans les espaces /project et /nearline sur les nœuds du cluster ?"
  - "Quel quota souple de 1 TB s’applique au répertoire /scratch et quelles sont les conditions de dépassement et de récupération ?"
  - "Comment se connecter à la grappe Nibi via Open OnDemand et lancer une session JupyterLab ?"
  - "Quelles sont les deux méthodes proposées pour utiliser JupyterLab sur Nibi (environnement préconfiguré ou environnement virtuel Python) et comment installer JupyterLab dans ce dernier ?"
  - "Pourquoi les répertoires des utilisateurs ne sont-ils plus créés automatiquement dans /project et /nearline ?"
  - "Comment les groupes peuvent-ils créer et organiser leurs propres répertoires dans les espaces /project et /nearline ?"
  - "Quels bénéfices cette approche apporte-t-elle pour le partage de données entre les membres du groupe ?"
  - "Comment demander et configurer correctement un nœud AMD MI300A pour garantir les liaisons de cœurs et de mémoire adéquates ?"
  - "Pourquoi la compilation avec CUDA ne fonctionne pas sur les GPU AMD MI300A et comment installer et utiliser ROCm pour compiler son code ?"
  - "Quelle est la procédure pour récupérer un fichier supprimé à l’aide des instantanés de Nibi, et quelles sont les restrictions associées à ces snapshots ?"
  - "Comment lancer JupyterLab pour qu’il s’ouvre dans le navigateur avec le répertoire $HOME affiché ?"
  - "Quel contenu est affiché dans le panneau de gauche de JupyterLab une fois démarré ?"
  - "Quelle solution de bureau à distance Nibi propose‑t‑elle désormais à la place du VDI, et quels avantages offre‑t‑elle ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: false
  qa_generated: false
---

| Propriété                                  | Valeur                                                                        |
| :----------------------------------------- | :---------------------------------------------------------------------------- |
| Disponibilité                              | 31 juillet 2025                                                               |
| Nœud de connexion SSH                      | nibi.alliancecan.ca                                                           |
| Nœud d'automatisation                      | *robot.nibi.alliancecan.ca*                                                  |
| Interface web                              | [ondemand.sharcnet.ca](https://ondemand.sharcnet.ca)                           |
| Collection Globus                          | [alliancecan#nibi](https://app.globus.org/file-manager?origin_id=07baf15f-d7fd-4b6a-bf8a-5b5ef2e229d3) |
| Nœud de copie (rsync, scp, sftp, etc.)     | utiliser les nœuds de connexion                                               |
| Portail                                    | [portal.nibi.sharcnet.ca](https://portal.nibi.sharcnet.ca)                     |
| Plateforme IA                              | brine.sharcnet.ca/ui/                                 |

Dans la langue anishinaabe, Nibi est un terme qui désigne l'eau. Cette nouvelle grappe offre 134 400 CPU et 288 GPU H100 de NVIDIA. Conçue par [Hypertec](https://www.hypertec.com/), Nibi est hébergée et exploitée par [SHARCNET](https://www.sharcnet.ca/) à l'Université de Waterloo.

## Accès
Vous devez [demander l'accès dans le CCDB](https://ccdb.alliancecan.ca/me/access_systems), en sélectionnant *Ressources* --> *Accès aux systèmes*.

*   Dans la liste des systèmes, sélectionnez Nibi.
*   Cliquez sur le bouton *Je demande l'accès*.

L'activation de votre accès pourrait prendre environ une heure.

## Stockage
Stockage parallèle : 25 Po, [SSD (Solid-State Drive)](https://fr.wikipedia.org/wiki/SSD) de [VAST Data](https://www.vastdata.com/) pour /home, /project et /scratch.

!!! note "Mode de comptabilisation des quotas Vast Data"
    Vast comptabilise différemment l'espace utilisé pour calculer les quotas. La taille apparente de vos fichiers est prise en compte alors que certaines configurations de Lustre compressent les fichiers de manière transparente et comptabilisent l'espace utilisé après compression.

!!! warning "Mécanisme expérimental de gestion de /scratch"
    Nibi utilise un nouveau mécanisme expérimental pour gérer /scratch. Comme sur tous les systèmes, vous disposez d'une limite souple et d'une limite stricte, mais sur Nibi, la limite souple est basse (1 TB) et vous disposez d'un délai de grâce de 60 jours. Après l'expiration de ce délai, la limite souple est imposée (plus aucune création ni extension de fichier). Pour corriger ceci, votre utilisation doit revenir sous la limite souple.

## Interconnexion
*   ethernet Nokia, 200/400 G
    *   bande passante pour nœuds CPU, 200 Gbit/s
    *   bande passante non bloquante pour tous les nœuds GPU Nvidia, 200 Gbit/s
    *   bande passante pour tous les nœuds GPU AMD, 200 Gbit/s
    *   connexion aux nœuds de stockage VAST, 24x100 Gbit/s
    *   liaisons montantes (*uplinks*) pour tous les nœuds, 400 Gbit/s; blocage 2:1

La topologie du réseau est décrite dans le fichier `/etc/slurm/topology.conf`.

Pour améliorer la performance des tâches multi-nœuds fortement couplées, vous pouvez forcer l'utilisation d'un seul commutateur (*network switch*) en ajoutant l'option suivante au script de la tâche.

```bash
#SBATCH --switches=1
```

## Caractéristiques des nœuds

| Nœuds | Cœurs | Mémoire disponible | Stockage local | CPU                                       | GPU                                                          |
| :---- | :---- | :----------------- | :------------- | :---------------------------------------- | :----------------------------------------------------------- |
| 700   | 192   | 748 G ou 766000 M  | 3 T            | 2 x Intel 6972P @ 2.4 GHz, 384 MB cache L3 |                                                              |
| 10    | 192   | 6000 G ou 6144000 M| 3 T            | 2 x Intel 6972P @ 2.4 GHz, 384 MB cache L3 |                                                              |
| 36    | 112   | 2000 G ou 2048000 M| 11 T           | 2 x Intel 8570 @ 2.1 GHz, 300 MB cache L3 | 8 x Nvidia H100 SXM (80 GB), connecté via NVLink           |
| 6     | 96    | 495 G ou 507000 M  | 3 T            | 4 x AMD MI300A @ 2.1 GHz (Zen4+CDNA3)    | Les cœurs CPU et les GPU CDNA3 sont dans le même socket, avec une mémoire unifiée. Voir les instructions ci-dessous. |

### Instances GPU
**Noms des instances GPU**

| Catégorie | Modèle ou instance | Nom court        | Sans unité     | Par sa mémoire  | Nom complet                      |
| :-------- | :----------------- | :--------------- | :------------- | :-------------- | :------------------------------- |
| **GPU**   | **H100-80gb**      | `h100`           | `h100`         | `h100_80gb`     | `nvidia_h100_80gb_hbm3`          |
| **MIG**   | **H100-1g.10gb**   | `h100_1g.10gb`   | `h100_1.10`    | `h100_10gb`     | `nvidia_h100_80gb_hbm3_1g.10gb`  |
| **MIG**   | **H100-2g.20gb**   | `h100_2g.20gb`   | `h100_2.20`    | `h100_20gb`     | `nvidia_h100_80gb_hbm3_2g.20gb`  |
| **MIG**   | **H100-3g.40gb**   | **H100-3g.40gb** | `h100_3.40`    | `h100_40gb`     | `nvidia_h100_80gb_hbm3_3g.40gb`  |

Pour demander un ou plusieurs GPU H100 complets, utilisez une des options Slurm suivantes :

*   **un H100-80gb** : `--gpus=h100:1` ou `--gpus=h100_80gb:1`
*   **plusieurs H100-80gb** par nœud :
    *   `--gpus-per-node=h100:2`
    *   `--gpus-per-node=h100:3`
    *   `--gpus-per-node=h100:4`
*   **plusieurs GPU H100 complets** distribués arbitrairement : `--gpus=h100:n` (remplacer n par le nombre de GPUs que vous voulez)

Environ la moitié des nœuds GPU utilisent [la technologie MIG](../programming/multi-instance_gpu.md). Trois tailles d'instances sont disponibles :

*   **H100-1g.10gb** : 1/8^e^ de la puissance de calcul, mémoire GPU de 10 Go
*   **H100-2g.20gb** : 2/8^e^ de la puissance de calcul, mémoire GPU de 20 Go
*   **H100-3g.40gb** : 3/8^e^ de la puissance de calcul, mémoire GPU de 40 Go

Pour demander **une et une seule instance GPU** pour une tâche de calcul, utilisez l'option correspondante.

*   **H100-1g.10gb** : `--gpus=h100_1g.10gb:1`
*   **H100-2g.20gb** : `--gpus=h100_2g.20gb:1`
*   **H100-3g.40gb** : `--gpus=h100_3g.40gb:1`

Pour le nombre maximum de cœurs CPU et le maximum de mémoire recommandés par instance GPU, voir [Ratios dans les bundles](../running-jobs/allocations_and_compute_scheduling.md#ratios-dans-les-bundles).

## Particularités

### Accès à l'internet
Tous les nœuds ont accès à l'internet; aucune autorisation de pare-feu spéciale ou proxy n'est nécessaire.

### /project et /nearline
Les répertoires des utilisateurs ne sont plus créés par défaut dans /project et /nearline. Vous pouvez toujours créer vos propres répertoires dans les espaces /project et /nearline du groupe à l'aide de `mkdir`. Ceci permet aux groupes de décider de l'organisation de leurs espaces /project et /nearline pour le partage de données entre les membres.
Sur /nearline, les [fichiers d'index](../storage-and-data/using_nearline_storage.md) et les autres petits fichiers ne sont pas sauvegardés ni archivés sur ruban.

### Quota pour /scratch
Un quota souple de 1 TB sur /scratch s'applique à chaque utilisateur. Ce quota souple peut être dépassé pendant 60 jours maximum, après quoi aucun fichier supplémentaire ne peut être écrit sur /scratch. Les fichiers peuvent être réécrits une fois que l'utilisateur a supprimé suffisamment de fichiers pour ramener son utilisation /scratch totale sous 1 TB. Pour plus d'information, voir [Stockage et gestion de fichiers](../storage-and-data/storage_and_file_management.md).

### Accès via Open OnDemand (OOD)
Il est possible d'accéder à la grappe Nibi simplement via un navigateur web. Nibi utilise Open OnDemand (OOD), une plateforme web qui simplifie l'accès en fournissant une interface web aux nœuds de connexion et un environnement de bureau à distance. Pour vous connecter à Nibi, rendez-vous sur [https://ondemand.sharcnet.ca/](https://ondemand.sharcnet.ca/) et connectez-vous avec [l'authentification multifacteur](../getting-started/multifactor_authentication.md). Une interface conviviale s'affichera, proposant des options pour ouvrir un terminal Bash ou lancer une session de bureau à distance.

### Utilisation de JupyterLab via OOD
Vous pouvez exécuter JupyterLab de manière interactive via le [portail Nibi Open OnDemand](https://ondemand.sharcnet.ca).

**Option 1** : Travailler dans un environnement préconfiguré (même que [JupyterHub](../interactive/jupyterhub.md))

Quand la connexion au [portail Nibi Open OnDemand](https://ondemand.sharcnet.ca) est établie, cliquez sur *Compute Node* dans le menu du haut et sélectionnez *Nibi JupyterLab*. Une page sera affichée dans laquelle un formulaire vous permet de demander une nouvelle session Nibi JupyterLab.

Après avoir rempli le formulaire avec les détails, cliquez sur *Launch* pour soumettre votre demande. Quand l'état des modifications pour Nibi JupyterLab passe à *Running*, cliquez sur *Connect to Jupyter* pour ouvrir JupyterLab dans le navigateur web.

Pour les détails sur la préconfiguration, voir [Interface JupyterLab](../interactive/jupyterlab.md#interface-jupyterlab).

**Option 2** : Travailler dans un [environnement virtuel Python](../software/python.md) que vous avez créé

Quand la connexion au [portail Nibi Open OnDemand](https://ondemand.sharcnet.ca) est établie, cliquez sur *Compute Node* dans le menu du haut et sélectionnez *Compute Desktop*. Une page sera affichée dans laquelle un formulaire vous permet de demander une nouvelle session Compute Desktop.

Après avoir rempli le formulaire avec les détails, cliquez sur *Launch* pour soumettre votre demande. Quand le bureau Compute passe à *Running*, cliquez sur *Launch Compute Desktop* pour vous connecter au bureau. Un bureau Linux sera affiché.

Sur le bureau Compute, faites un clic droit dans une zone vide; un menu contextuel apparaît. Sélectionnez *Open in Terminal* pour ouvrir une fenêtre de terminal où vous pouvez créer ou activer votre environnement virtuel Python dans lequel JupyterLab est installé.

Si JupyterLab n'est pas installé dans l'environnement virtuel Python que vous souhaitez utiliser, vous pouvez l'installer avec la commande

```bash
(your_python_ENV) [username@<node>.nibi]$ pip install --no-index jupyterlab
```

Vous pouvez ensuite lancer JupyterLab à partir de votre environnement virtuel Python avec

```bash
(your_python_ENV) [username@<node>.nibi]$ jupyter-lab --notebook-dir $HOME
```

JupyterLab s'ouvre dans le navigateur sur le bureau et le contenu de votre espace $HOME est listé dans le panneau de gauche.

### Prise en charge de VDI via OOD
Nibi n'offre plus d'infrastructure de bureau virtuel (VDI), mais fournit un environnement de bureau à distance via le [portail Open OnDemand (OOD)](https://ondemand.sharcnet.ca/) avec des performances matérielles et une prise en charge logicielle améliorées.

### Nœuds AMD MI300A

Il faut présentement demander les MI300A comme des nœuds entiers. Vous avez la responsabilité de vous assurer que les processus de votre tâche sont exécutés avec les liaisons correctes des cœurs et de la mémoire. Dans l'exemple ci-dessous, le script utilise quatre processus.

!!! note "Remarque importante concernant les nœuds AMD MI300A"
    Pour une bonne utilisation des nœuds MI300A, compilez votre code avec ROCm. La compilation avec CUDA ne fonctionne pas parce que les GPU AMD ne sont pas pris en charge.

En date de mai 2026, notre pile logicielle ne prend pas en charge les nœuds MI300A et aucun module ne permet la compilation avec ROCm. Vous pouvez installer vous-même des logiciels avec la suite d'outils ROCm qui se trouve dans le répertoire /opt/rocm. Si vous avez besoin d'assistance, écrivez au [soutien technique](../support/technical_support.md).

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
Nibi dispose d'un système de sauvegarde qui crée un instantané de vos fichiers dans /home et /project toutes les 30 minutes; ces instantanés sont sauvegardés pour une période de deux semaines. Si vous supprimez accidentellement un fichier, vous pourrez peut-être le récupérer à partir de ces instantanés, à condition qu'il ait été supprimé il y a moins de deux semaines. Cependant, si vous modifiez un fichier après la dernière sauvegarde, pour ensuite le supprimer, il ne pourra pas être récupéré.

Pour localiser un fichier supprimé, utilisez la commande `oops` pour vérifier le répertoire courant, ou spécifiez un autre répertoire où faire la recherche. Pour récupérer un fichier, copiez-le depuis le chemin retourné par la commande `oops` à l'aide d'un outil standard comme cp. Les instantanés sont en lecture seule; vous ne pouvez donc ni supprimer ni modifier les fichiers qu'ils contiennent, vous devez d'abord les copier. Ne faites pas référence aux fichiers des instantanés dans vos scripts de soumission de tâches.

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

## Brine : plateforme IA en tant que service
Dans le cadre d'un nouvel effort, SHARCNET a lancé une plateforme IA en tant que service hébergée au sein du centre de données Nibi. Ce service offre aux chercheurs canadiens un accès à des modèles d'IA hébergés sur l'infrastructure de SHARCNET, sans les délais d'attente habituels des grappes de calcul de haute performance (CHPC).

Brine fournit une API compatible OpenAI et toujours disponible pour les modèles hébergés qui prennent en charge le clavardage, l'appel d'outils et la transcription audio. La disponibilité et les paramètres des modèles sont décrits [ici](https://github.com/sharcnet/brine-examples/tree/main/model-cards).

Brine fonctionne sur le matériel du centre de données Graham, de sorte que les données sont traitées au Canada plutôt que d'être envoyées à un fournisseur commercial à l'extérieur du pays. Malgré cela, les utilisateurs ne devraient pas soumettre de données sensibles. Cela inclut les renseignements personnels ou de santé, les dossiers d'étudiants ou financiers, les identifiants, les données confidentielles de tiers, les données soumises à des contrôles à l'exportation, les données régies par les Autochtones ou les communautés, et tout ce que vous n'êtes pas autorisé à envoyer à un service d'IA hébergé de manière centralisée.

Pour demander l'accès, envoyez un courriel à help@sharcnet.ca en mentionnant "SHARCNET Brine".

### Obtention de l'accès
Après avoir accepté les conditions d'utilisation, vous recevrez une invitation par courriel à votre boîte de réception vous invitant à vous inscrire pour un nouveau compte LiteLLM. Il s'agit d'un nouveau compte pour ce service uniquement.

!!! warning "Note importante"
    Nous avons reçu des alertes selon lesquelles certaines boîtes de courriel signalent l'invitation comme du pourriel. Veuillez vérifier votre courrier indésirable.

Après vous être connecté, une interface devrait s'afficher, vous invitant à créer une nouvelle clé. Créez la clé pour vous-même, nommez-la et ne la partagez pas avec d'autres.

Cette clé est ce qui est requis pour accéder au service en tant qu'API, tel que décrit dans le dépôt [exemples Brine](https://github.com/sharcnet/brine-examples). Cela inclut des exemples en Python, Javascript et Curl.

### Interface LiteLLM
L'infrastructure de ce service est alimentée par [LiteLLM](https://www.litellm.ai/) et offre plusieurs fonctionnalités intéressantes en dehors de la création de clés API et du service de modèles.

*   Surveiller votre utilisation des jetons et l'activité de vos clés
*   Comparer les sorties des modèles dans la fonctionnalité du laboratoire
*   Ajouter des bases de données vectorielles
*   Gérer les connexions MCP

### État du service
Pour vous tenir au courant des changements apportés à ce service, une invitation à un canal Slack est disponible sur demande.

Pour les alertes de panne et les mises à jour, veuillez consulter la page d'état [ici](https://status.alliancecan.ca/system/Nibi%20AIaaS:%20Brine).