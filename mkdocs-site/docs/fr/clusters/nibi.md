---
title: "Nibi/fr"
slug: "nibi"
lang: "fr"

source_wiki_title: "Nibi/fr"
source_hash: "cedefc4d8ff7057f3a656fbad217e72d"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T09:17:55.050118+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

| Clé                 | Valeur                                                                                   |
| :------------------ | :--------------------------------------------------------------------------------------- |
| Disponibilité       | 31 juillet 2025                                                                          |
| Nœud de connexion SSH | nibi.alliancecan.ca                                                                      |
| Nœud d'automatisation | *robot.nibi.alliancecan.ca*                                                              |
| Interface web       | [ondemand.sharcnet.ca](https://ondemand.sharcnet.ca)                                     |
| Collection Globus   | [alliancecan#nibi](https://app.globus.org/file-manager?origin_id=07baf15f-d7fd-4b6a-bf8a-5b5ef2e229d3) |
| Nœud de copie (rsync, scp, sftp, etc.) | utiliser les nœuds de connexion                                                            |
| Portail             | [portal.nibi.sharcnet.ca](https://portal.nibi.sharcnet.ca)                              |

Dans la langue anishinaabe, Nibi est un terme qui désigne l'eau. Cette nouvelle grappe offre 134 400 CPU et 288 GPU H100 de NVIDIA. Conçue par [Hypertec](https://www.hypertec.com/), Nibi est hébergée et exploitée par [SHARCNET](https://www.sharcnet.ca/) à l'Université de Waterloo.

## Stockage

Stockage parallèle : 25 Po, [SSD (Solid-State Drive)](https://fr.wikipedia.org/wiki/SSD) de [VAST Data](https://www.vastdata.com/) pour /home, /project et /scratch.

!!! note "Remarque"
    Vast comptabilise différemment l'espace utilisé pour calculer les quotas. La taille apparente de vos fichiers est prise en compte alors que certaines configurations de Lustre compressent les fichiers de manière transparente et comptabilisent l'espace utilisé après compression.

!!! warning "Attention pour /scratch"
    Nibi utilise un nouveau mécanisme expérimental pour gérer /scratch. Comme sur tous les systèmes, vous disposez d'une limite souple et d'une limite stricte, mais sur Nibi, la limite souple est basse (1 TB) et vous disposez d'un délai de grâce de 60 jours. Après l'expiration de ce délai, la limite souple est imposée (plus aucune création ni extension de fichier). Pour résoudre ce problème, votre utilisation doit revenir sous la limite souple.

## Interconnexion

*   Ethernet Nokia, 200/400 G
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

| nœuds | cœurs | mémoire disponible | stockage local au nœud | CPU                                     | GPU                                                                                                                     |
| :---- | :---- | :----------------- | :--------------------- | :-------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- |
| 700   | 192   | 748G ou 766000M    | 3T                     | 2 x Intel 6972P @ 2.4GHz, cache L3 de 384Mo |                                                                                                                         |
| 10    | 192   | 6000G ou 6144000M  | 3T                     | 2 x Intel 6972P @ 2.4GHz, cache L3 de 384Mo |                                                                                                                         |
| 36    | 112   | 2000G ou 2048000M  | 11T                    | 2 x Intel 8570 @ 2.1GHz, cache L3 de 300Mo | 8 x Nvidia H100 SXM (80Go), connexion via NVLink                                                                        |
| 6     | 96    | 495G ou 507000M    | 3T                     | 4 x AMD MI300A @ 2.1GHz (Zen4+CDNA3)    | Les cœurs CPU et les GPU de l'architecture CDNA3 sont dans le même *socket* et partagent la même mémoire unifiée. |

### Instances GPU

**Noms des instances GPU disponibles**

| Modèle ou instance            | Nom court        | Sans l'unité | Par mémoire | Nom long                        |
| :---------------------------- | :--------------- | :----------- | :---------- | :------------------------------ |
| **GPU H100-80gb**             | `h100`           | `h100`       | `h100_80gb` | `nvidia_h100_80gb_hbm3`         |
| **MIG H100-1g.10gb**          | `h100_1g.10gb`   | `h100_1.10`  | `h100_10gb` | `nvidia_h100_80gb_hbm3_1g.10gb` |
| **MIG H100-2g.20gb**          | `h100_2g.20gb`   | `h100_2.20`  | `h100_20gb` | `nvidia_h100_80gb_hbm3_2g.20gb` |
| **MIG H100-3g.40gb**          | `h100_3g.40gb`   | `h100_3.40`  | `h100_40gb` | `nvidia_h100_80gb_hbm3_3g.40gb` |

Pour demander un ou plusieurs GPU H100 complets, utilisez une des options Slurm suivantes :

*   **un H100-80gb** : `--gpus=h100:1` ou `--gpus=h100_80gb:1`
*   **plusieurs H100-80gb** par nœud :
    *   `--gpus-per-node=h100:2`
    *   `--gpus-per-node=h100:3`
    *   `--gpus-per-node=h100:4`
*   **plusieurs GPU H100 complets** distribués arbitrairement : `--gpus=h100:n` (remplacer n par le nombre de GPUs que vous voulez)

Environ la moitié des nœuds GPU utilisent [la technologie MIG](multi-instance-gpu.md). Trois tailles d'instances sont disponibles :

*   **H100-1g.10gb**: 1/8<sup>e</sup> de la puissance de calcul, mémoire GPU de 10Go
*   **H100-2g.20gb**: 2/8<sup>e</sup> de la puissance de calcul, mémoire GPU de 20Go
*   **H100-3g.40gb**: 3/8<sup>e</sup> de la puissance de calcul, mémoire GPU de 40Go

Pour demander **une et une seule instance GPU** pour une tâche de calcul, utilisez l'option correspondante.

*   **H100-1g.10gb** : `--gpus=h100_1g.10gb:1`
*   **H100-2g.20gb** : `--gpus=h100_2g.20gb:1`
*   **H100-3g.40gb** : `--gpus=h100_3g.40gb:1`

Pour le nombre maximum de cœurs CPU et le maximum de mémoire recommandés par instance GPU, voir [Ratios dans les *bundles*](allocations-and-compute-scheduling.md#ratios-dans-les-bundles).

## Particularités

### Accès à l'internet

Tous les nœuds ont accès à l'internet; aucune autorisation de pare-feu spéciale ou proxy n'est nécessaire.

### Espace /project

Les répertoires des utilisateurs ne sont plus créés par défaut dans /project. Vous pouvez toujours créer vos propres répertoires dans l'espace /project du groupe à l'aide de `mkdir`. Ceci permet aux groupes de décider de l'organisation de leur espace /project pour le partage de données entre les membres.

### Quota pour l'espace /scratch

Un quota souple de 1 TB sur /scratch s'applique à chaque utilisateur. Ce quota souple peut être dépassé pendant 60 jours maximum, après quoi aucun fichier supplémentaire ne peut être écrit sur /scratch. Les fichiers peuvent être réécrits une fois que l'utilisateur a supprimé suffisamment de fichiers pour ramener son utilisation /scratch totale sous 1 TB. Pour plus d'information, voir [Stockage et gestion de fichiers](storage-and-file-management.md).

### Accès via Open OnDemand (OOD)

Il est possible d'accéder à la grappe Nibi simplement via un navigateur web. Nibi utilise Open OnDemand (OOD), une plateforme web qui simplifie l'accès en fournissant une interface web aux nœuds de connexion et un environnement de bureau à distance. Pour vous connecter à Nibi, rendez-vous sur [https://ondemand.sharcnet.ca/](https://ondemand.sharcnet.ca/) et connectez-vous avec l'authentification multifacteur. Une interface conviviale s'affichera, proposant des options pour ouvrir un terminal Bash ou lancer une session de bureau à distance.

### Utilisation de JupyterLab via OOD

Vous pouvez exécuter JupyterLab de manière interactive via le [portail Nibi Open OnDemand](https://ondemand.sharcnet.ca).

**Option 1** : travailler dans un environnement préconfiguré, le même que pour [JupyterHub](jupyterhub.md)

Quand la connexion au [portail Nibi Open OnDemand](https://ondemand.sharcnet.ca) est établie, cliquez sur *Compute Node* dans le menu du haut et sélectionnez *Nibi JupyterLab*. Une page sera affichée dans laquelle un formulaire vous permet de demander une nouvelle session Nibi JupyterLab.

Après avoir rempli le formulaire avec les détails, cliquez sur *Launch* pour soumettre votre demande. Quand l'état des modifications pour Nibi JupyterLab passe à *Running*, cliquez sur *Connect to Jupyter* pour ouvrir JupyterLab dans le navigateur web.

Pour les détails sur la préconfiguration, voir [Interface JupyterLab](jupyterlab.md#interface-jupyterlab).

**Option 2** : travailler dans un [environnement virtuel Python](python.md#créer-et-utiliser-un-environnement-virtuel-python) que vous avez créé

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

### Récupérer des fichiers supprimés

!!! tip "Récupération de fichiers"
    Nibi dispose d'un système de sauvegarde qui crée un instantané de vos fichiers dans /home et /project toutes les 30 minutes; ces instantanés sont sauvegardés pour une période de deux semaines. Si vous supprimez accidentellement un fichier, vous pourrez peut-être le récupérer à partir de ces instantanés, à condition qu'il ait été supprimé il y a moins de deux semaines. Cependant, si vous modifiez un fichier après la dernière sauvegarde, pour ensuite le supprimer, il ne pourra pas être récupéré.

Pour localiser un fichier supprimé, utilisez la commande `oops` pour vérifier le répertoire courant, ou spécifiez un autre répertoire où faire la recherche. Pour récupérer un fichier, copiez-le depuis le chemin retourné par la commande `oops` à l'aide d'un outil standard comme `cp`. Les instantanés sont en lecture seule; vous ne pouvez donc ni supprimer ni modifier les fichiers qu'ils contiennent, vous devez d'abord les copier.

!!! warning "Attention avec les instantanés"
    Ne faites pas référence aux fichiers des instantanés dans vos scripts de soumission de tâches.

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