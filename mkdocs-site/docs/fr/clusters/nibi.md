---
title: "Nibi/fr"
slug: "nibi"
lang: "fr"

source_wiki_title: "Nibi/fr"
source_hash: "f800d9e92676ad5d41a71ca448c31652"
last_synced: "2026-04-18T23:39:30.217451+00:00"
last_processed: "2026-04-19T01:02:04.265941+00:00"

tags:
  []

keywords:
  - "SHARCNET"
  - "JupyterLab"
  - "Stockage parallèle"
  - "Intel 8570"
  - "GPU MI300A"
  - "fichiers"
  - "mémoire unifiée"
  - "AMD MI300A"
  - "Instances GPU"
  - "commande oops"
  - "MIG"
  - "Nibi"
  - "Slurm"
  - "système de sauvegarde"
  - "Stockage et gestion de fichiers"
  - "Grappe Nibi"
  - "GPU H100 de NVIDIA"
  - "Quota /scratch"
  - "script"
  - "liaisons des cœurs et de la mémoire"
  - "SBATCH"
  - "Nœuds AMD MI300A"
  - "H100"
  - "récupérer des fichiers supprimés"
  - "Nœuds de calcul"
  - "processus"
  - "60 jours maximum"
  - "grappe Nibi"
  - "Nvidia H100 SXM"
  - "instantanés"
  - "/scratch"
  - "architecture CDNA3"
  - "1 TB"
  - "Open OnDemand"
  - "environnement virtuel Python"

questions:
  - "Quelles sont les capacités matérielles globales (nombre de CPU et GPU) de la grappe Nibi et par quelle institution est-elle hébergée ?"
  - "Comment fonctionne le nouveau mécanisme expérimental de gestion des limites d'espace et des délais de grâce pour le répertoire de stockage /scratch ?"
  - "Quelles sont les caractéristiques du réseau d'interconnexion et quelle option permet d'optimiser les performances des tâches multi-nœuds ?"
  - "Quelles sont les spécifications matérielles du système équipé des processeurs Intel 8570 et des cartes graphiques Nvidia H100 ?"
  - "Comment la mémoire et les composants sont-ils structurés dans l'architecture des processeurs AMD MI300A ?"
  - "Quelle technologie de connexion est utilisée pour relier les GPU Nvidia entre eux dans la première configuration ?"
  - "Comment peut-on demander une instance GPU complète ou une instance MIG spécifique en utilisant les options Slurm ?"
  - "Comment fonctionne la gestion des répertoires dans l'espace /project pour le partage de données entre les membres d'un groupe ?"
  - "Quelles sont les règles et les limites de temps concernant le quota souple de l'espace de stockage /scratch ?"
  - "Comment peut-on se connecter à la grappe Nibi en utilisant la plateforme Open OnDemand ?"
  - "Quelles sont les deux options disponibles pour configurer et lancer une session JupyterLab via l'interface web ?"
  - "Quelles précautions et configurations spécifiques doivent être prises en compte lors de l'utilisation des nœuds entiers AMD MI300A ?"
  - "Que se passe-t-il sur le répertoire /scratch si le dépassement de quota dure plus de 60 jours ?"
  - "Quelle action l'utilisateur doit-il entreprendre pour pouvoir écrire de nouveaux fichiers après un blocage ?"
  - "Où est-il possible de consulter davantage d'informations sur le stockage et la gestion des fichiers ?"
  - "Quelles sont les conditions de temps et de sauvegarde requises pour qu'un fichier supprimé puisse être récupéré sur le système Nibi ?"
  - "Quelle commande spécifique doit-on utiliser pour localiser un fichier accidentellement supprimé dans un répertoire ?"
  - "Comment doit-on procéder pour restaurer un fichier à partir d'un instantané, et pourquoi ne peut-on pas le modifier directement à cet emplacement ?"
  - "Pourquoi est-il important de configurer correctement les liaisons des cœurs et de la mémoire pour les processus de la tâche ?"
  - "Quelles sont les ressources matérielles spécifiques (processeurs, cartes graphiques MI300A, mémoire) demandées dans cet exemple de script Slurm ?"
  - "Quelle commande le script utilise-t-il pour vérifier la disponibilité des GPU avant de lancer le programme compatible ROCm ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! info
**Disponibilité** : 31 juillet 2025
**Nœud de connexion SSH** : `nibi.alliancecan.ca`
**Nœud d'automatisation** : *robot.nibi.alliancecan.ca*
**Interface web** : [ondemand.sharcnet.ca](https://ondemand.sharcnet.ca)
**Collection Globus** : [alliancecan#nibi](https://app.globus.org/file-manager?origin_id=07baf15f-d7fd-4b6a-bf8a-5b5ef2e229d3)
**Nœud de copie (rsync, scp, sftp, etc.)** : utiliser les nœuds de connexion
**Portail** : [portal.nibi.sharcnet.ca](https://portal.nibi.sharcnet.ca)
!!!

Dans la langue anishinaabe, Nibi est un terme qui désigne l'eau. Cette nouvelle grappe offre 134 400 CPU et 288 GPU H100 de NVIDIA. Conçue par [Hypertec](https://www.hypertec.com/), Nibi est hébergée et exploitée par [SHARCNET](https://www.sharcnet.ca/) à l'Université de Waterloo.

## Stockage
Stockage parallèle : 25 Po, [SSD (Solid-State Drive)](https://fr.wikipedia.org/wiki/SSD) de [VAST Data](https://www.vastdata.com/) pour `/home`, `/project` et `/scratch`.

!!! attention "Comptabilisation des quotas Vast"
    Vast comptabilise différemment l'espace utilisé pour calculer les quotas. La taille apparente de vos fichiers est prise en compte alors que certaines configurations de Lustre compressent les fichiers de manière transparente et comptabilisent l'espace utilisé après compression.

!!! attention "Gestion expérimentale de /scratch"
    Nibi utilise un nouveau mécanisme expérimental pour gérer `/scratch`. Comme sur tous les systèmes, vous disposez d'une limite souple et d'une limite stricte, mais sur Nibi, la limite souple est basse (1 TB) et vous disposez d'un délai de grâce de 60 jours. Après l'expiration de ce délai, la limite souple est imposée (plus aucune création ni extension de fichier). Pour résoudre ce problème, votre utilisation doit revenir sous la limite souple.

## Interconnexion
*   Ethernet Nokia, 200/400 G
    *   Bande passante pour les nœuds CPU : 200 Gbit/s
    *   Bande passante non bloquante pour tous les nœuds GPU Nvidia : 200 Gbit/s
    *   Bande passante pour tous les nœuds GPU AMD : 200 Gbit/s
    *   Connexion aux nœuds de stockage VAST : 24x100 Gbit/s
    *   Liaisons montantes (uplinks) pour tous les nœuds : 400 Gbit/s; blocage 2:1

La topologie du réseau est décrite dans le fichier `/etc/slurm/topology.conf`.

Pour améliorer la performance des tâches multi-nœuds fortement couplées, vous pouvez forcer l'utilisation d'un seul commutateur réseau en ajoutant l'option suivante au script de la tâche :

```bash
#SBATCH --switches=1
```

## Caractéristiques des nœuds

| Nœuds | Cœurs | Mémoire disponible | Stockage local au nœud | CPU                                      | GPU                                                                                                                                                                                                                               |
| :---- | :---- | :----------------- | :--------------------- | :--------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 700   | 192   | 748G ou 766000M    | 3T                     | 2 x Intel 6972P @ 2.4GHz, cache L3 de 384Mo |                                                                                                                                                                                                                           |
| 10    | 192   | 6000G ou 6144000M  | 3T                     | 2 x Intel 6972P @ 2.4GHz, cache L3 de 384Mo |                                                                                                                                                                                                                           |
| 36    | 112   | 2000G ou 2048000M  | 11T                    | 2 x Intel 8570 @ 2.1GHz, cache L3 de 300Mo | 8 x Nvidia H100 SXM (80Go), connexion via NVLink                                                                                                                                                                          |
| 6     | 96    | 495G ou 507000M    | 3T                     | 4 x AMD MI300A @ 2.1GHz (Zen4+CDNA3)     | Les cœurs CPU et les GPU de l'architecture CDNA3 sont dans le même socket et partagent la même mémoire unifiée. Pour les instructions d'utilisation, voir la section sur les [Nœuds AMD MI300A](#nœuds-amd-mi300a) ci-dessous. |

### Instances GPU
**Noms des instances GPU disponibles**

| Type | Modèle ou instance | Nom court        | Sans l'unité     | Par mémoire      | Nom long                           |
| :--- | :----------------- | :--------------- | :--------------- | :--------------- | :--------------------------------- |
| GPU  | **H100-80gb**      | `h100`           | `h100`           | `h100_80gb`      | `nvidia_h100_80gb_hbm3`            |
| MIG  | **H100-1g.10gb**   | `h100_1g.10gb`   | `h100_1.10`      | `h100_10gb`      | `nvidia_h100_80gb_hbm3_1g.10gb`    |
| MIG  | **H100-2g.20gb**   | `h100_2g.20gb`   | `h100_2.20`      | `h100_20gb`      | `nvidia_h100_80gb_hbm3_2g.20gb`    |
| MIG  | **H100-3g.40gb**   | `h100_3g.40gb`   | `h100_3.40`      | `h100_40gb`      | `nvidia_h100_80gb_hbm3_3g.40gb`    |

Pour demander un ou plusieurs GPU H100 complets, utilisez une des options Slurm suivantes :

*   **un H100-80gb** : `--gpus=h100:1` ou `--gpus=h100_80gb:1`
*   **plusieurs H100-80gb** par nœud :
    *   `--gpus-per-node=h100:2`
    *   `--gpus-per-node=h100:3`
    *   `--gpus-per-node=h100:4`
*   **plusieurs GPU H100 complets** distribués arbitrairement : `--gpus=h100:n` (remplacer `n` par le nombre de GPU que vous voulez)

Environ la moitié des nœuds GPU utilisent [la technologie MIG](../programming/multi-instance_gpu.md). Trois tailles d'instances sont disponibles :

*   **H100-1g.10gb** : 1/8^e^ de la puissance de calcul, mémoire GPU de 10Go
*   **H100-2g.20gb** : 2/8^e^ de la puissance de calcul, mémoire GPU de 20Go
*   **H100-3g.40gb** : 3/8^e^ de la puissance de calcul, mémoire GPU de 40Go

Pour demander **une et une seule instance GPU** pour une tâche de calcul, utilisez l'option correspondante.

*   **H100-1g.10gb** : `--gpus=h100_1g.10gb:1`
*   **H100-2g.20gb** : `--gpus=h100_2g.20gb:1`
*   **H100-3g.40gb** : `--gpus=h100_3g.40gb:1`

Pour le nombre maximum de cœurs CPU et le maximum de mémoire recommandés par instance GPU, voir [Ratios dans les bundles](../running-jobs/allocations_and_compute_scheduling.md#ratios-dans-les-bundles).

## Particularités

### Accès à l'internet
Tous les nœuds ont accès à l'internet; aucune autorisation de pare-feu spéciale ni aucun serveur mandataire (proxy) n'est nécessaire.

### Espace /project
Les répertoires des utilisateurs ne sont plus créés par défaut dans `/project`. Vous pouvez toujours créer vos propres répertoires dans l'espace `/project` du groupe à l'aide de `mkdir`. Ceci permet aux groupes de décider de l'organisation de leur espace `/project` pour le partage de données entre les membres.

### Quota pour l'espace /scratch
Un quota souple de 1 TB sur `/scratch` s'applique à chaque utilisateur. Ce quota souple peut être dépassé pendant 60 jours maximum, après quoi aucun fichier supplémentaire ne peut être écrit sur `/scratch`. Les fichiers peuvent être réécrits une fois que l'utilisateur a supprimé suffisamment de fichiers pour ramener son utilisation `/scratch` totale sous 1 TB. Pour plus d'information, voir [Stockage et gestion de fichiers](../storage-and-data/storage_and_file_management.md).

### Accès via Open OnDemand (OOD)
Il est possible d'accéder à la grappe Nibi simplement via un navigateur web. Nibi utilise Open OnDemand (OOD), une plateforme web qui simplifie l'accès en fournissant une interface web aux nœuds de connexion et un environnement de bureau à distance. Pour vous connecter à Nibi, rendez-vous sur [https://ondemand.sharcnet.ca/](https://ondemand.sharcnet.ca/) et connectez-vous avec l'authentification multifacteur. Une interface conviviale s'affichera, proposant des options pour ouvrir un terminal Bash ou lancer une session de bureau à distance.

### Utilisation de JupyterLab via OOD
Vous pouvez exécuter JupyterLab de manière interactive via le [portail Nibi Open OnDemand](https://ondemand.sharcnet.ca).

**Option 1** : travailler dans un environnement préconfiguré, le même que pour [JupyterHub](../interactive/jupyterhub.md)

Lorsque la connexion au [portail Nibi Open OnDemand](https://ondemand.sharcnet.ca) est établie, cliquez sur *Nœud de calcul* dans le menu du haut et sélectionnez *JupyterLab Nibi*. Une page sera affichée dans laquelle un formulaire vous permet de demander une nouvelle session JupyterLab Nibi.

Après avoir rempli le formulaire avec les détails, cliquez sur *Lancer* pour soumettre votre demande. Quand l'état des modifications pour JupyterLab Nibi passe à *En cours d'exécution*, cliquez sur *Se connecter à Jupyter* pour ouvrir JupyterLab dans le navigateur web.

Pour les détails sur la préconfiguration, voir [Interface JupyterLab](../interactive/jupyterlab.md#interface-jupyterlab).

**Option 2** : travailler dans un [environnement virtuel Python](../software/python.md) que vous avez créé

Lorsque la connexion au [portail Nibi Open OnDemand](https://ondemand.sharcnet.ca) est établie, cliquez sur *Nœud de calcul* dans le menu du haut et sélectionnez *Bureau de calcul*. Une page sera affichée dans laquelle un formulaire vous permet de demander une nouvelle session Bureau de calcul.

Après avoir rempli le formulaire avec les détails, cliquez sur *Lancer* pour soumettre votre demande. Quand le bureau de calcul passe à *En cours d'exécution*, cliquez sur *Lancer le bureau de calcul* pour vous connecter au bureau. Un bureau Linux sera affiché.

Sur le bureau de calcul, faites un clic droit dans une zone vide; un menu contextuel apparaît. Sélectionnez *Ouvrir dans le terminal* pour ouvrir une fenêtre de terminal où vous pouvez créer ou activer votre environnement virtuel Python dans lequel JupyterLab est installé.

Si JupyterLab n'est pas installé dans l'environnement virtuel Python que vous souhaitez utiliser, vous pouvez l'installer avec la commande :

```bash
# (your_python_ENV) [username@<node>.nibi]$
pip install --no-index jupyterlab
```

Vous pouvez ensuite lancer JupyterLab à partir de votre environnement virtuel Python avec :

```bash
# (your_python_ENV) [username@<node>.nibi]$
jupyter-lab --notebook-dir $HOME
```

JupyterLab s'ouvre dans le navigateur sur le bureau et le contenu de votre espace `$HOME` est listé dans le panneau de gauche.

### Prise en charge de VDI via OOD
Nibi n'offre plus d'infrastructure de bureau virtuel (VDI), mais fournit un environnement de bureau à distance via le [portail Open OnDemand (OOD)](https://ondemand.sharcnet.ca/) avec des performances matérielles et une prise en charge logicielle améliorées.

<span id="nœuds-amd-mi300a"></span>
### Nœuds AMD MI300A

Ceux-ci sont présentement des nœuds entiers. Vous avez la responsabilité de vous assurer que les processus de la tâche sont exécutés avec des liaisons correctes des cœurs et de la mémoire. Dans l'exemple suivant, le script utilise quatre processus.

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
# [username@<node>.nibi]$
ls
dont_delete_me.txt
# [username@<node>.nibi]$
rm dont_delete_me.txt
# [username@<node>.nibi]$
ls
# [username@<node>.nibi]$
oops
Deleted files found in snapshots:
./.snapshot/backup_2026-04-01_18_00_00_UTC/dont_delete_me.txt
Files created less than 9 min ago (2026-04-01 14:00:00-04:00) are not yet backed up
Files deleted more than 0 days ago (2026-04-01 13:30:00-04:00) please submit a help ticket
# [username@<node>.nibi]$
cp ./.snapshot/backup_2026-04-01_18_00_00_UTC/dont_delete_me.txt .
# [username@<node>.nibi]$
ls
dont_delete_me.txt