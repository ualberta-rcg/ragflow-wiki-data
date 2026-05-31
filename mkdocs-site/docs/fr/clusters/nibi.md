---
title: "Nibi/fr"
slug: "nibi"
lang: "fr"

source_wiki_title: "Nibi/fr"
source_hash: "f1543c16fcadd17234582ebcb5573bec"
last_synced: "2026-05-31T00:03:42.418098+00:00"
last_processed: "2026-05-31T00:49:35.366154+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: true
  qa_generated: false
---

| Disponibilité | 31 juillet 2025 |
| :------------ | :-------------- |
| Nœud de connexion SSH | nibi.alliancecan.ca |
| Nœud d'automatisation | *robot.nibi.alliancecan.ca* |
| Interface web | [ondemand.sharcnet.ca](https://ondemand.sharcnet.ca) |
| Collection Globus | [alliancecan#nibi](https://app.globus.org/file-manager?origin_id=07baf15f-d7fd-4b6a-bf8a-5b5ef2e229d3) |
| Nœud de copie (rsync, scp, sftp, etc.) | utiliser les nœuds de connexion |
| Portail | [portal.nibi.sharcnet.ca](https://portal.nibi.sharcnet.ca) |

Dans la langue anishinaabe, Nibi est un terme qui désigne l'eau. Cette nouvelle grappe offre 134 400 CPU et 288 GPU H100 de NVIDIA. Conçue par [Hypertec](https://www.hypertec.com/), Nibi est hébergée et exploitée par [SHARCNET](https://www.sharcnet.ca/) à l'Université de Waterloo.

## Stockage

Stockage parallèle : 25 Po, [SSD (Solid-State Drive)](https://fr.wikipedia.org/wiki/SSD) de [VAST Data](https://www.vastdata.com/) pour `/home`, `/project` et `/scratch`.

!!! note
    Vast comptabilise différemment l'espace utilisé pour calculer les quotas. La taille apparente de vos fichiers est prise en compte alors que certaines configurations de Lustre compressent les fichiers de manière transparente et comptabilisent l'espace utilisé après compression.

!!! note
    Nibi utilise un nouveau mécanisme expérimental pour gérer `/scratch`. Comme sur tous les systèmes, vous disposez d'une limite souple et d'une limite stricte, mais sur Nibi, la limite souple est basse (1 To) et vous disposez d'un délai de grâce de 60 jours. Après l'expiration de ce délai, la limite souple est imposée (plus aucune création ni extension de fichier). Pour corriger ceci, votre utilisation doit revenir sous la limite souple.

## Interconnexion

*   Ethernet Nokia, 200/400 Gbit/s
    *   Bande passante pour nœuds CPU, 200 Gbit/s
    *   Bande passante non bloquante pour tous les nœuds GPU Nvidia, 200 Gbit/s
    *   Bande passante pour tous les nœuds GPU AMD, 200 Gbit/s
    *   Connexion aux nœuds de stockage VAST, 24x100 Gbit/s
    *   Liaisons montantes pour tous les nœuds, 400 Gbit/s; blocage 2:1

La topologie du réseau est décrite dans le fichier

```text
/etc/slurm/topology.conf
```

Pour améliorer la performance des tâches multi-nœuds fortement couplées, vous pouvez forcer l'utilisation d'un seul commutateur réseau en ajoutant l'option suivante au script de la tâche.

```bash
#SBATCH --switches=1
```

## Caractéristiques des nœuds

| nœuds | cœurs | mémoire disponible | stockage local | CPU | GPU |
| :---- | :---- | :----------------- | :------------- | :-- | :-- |
| 700 | 192 | 748 Go ou 766 000 Mo | 3 To | 2 x Intel 6972P à 2.4 GHz, cache L3 de 384 Mo | |
| 10 | 192 | 6000 Go ou 6 144 000 Mo | 3 To | 2 x Intel 6972P à 2.4 GHz, cache L3 de 384 Mo | |
| 36 | 112 | 2000 Go ou 2 048 000 Mo | 11 To | 2 x Intel 8570 à 2.1 GHz, cache L3 de 300 Mo | 8 x Nvidia H100 SXM (80 Go), connecté via NVLink |
| 6 | 96 | 495 Go ou 507 000 Mo | 3 To | 4 x AMD MI300A à 2.1 GHz (Zen4+CDNA3) | Les cœurs CPU et les GPU CDNA3 sont dans le même *socket*, avec une mémoire unifiée. Voir les instructions ci-dessous. |

### Instances GPU

**Noms des instances GPU**

| Catégorie | Modèle ou instance | Nom court | Sans unité | Par sa mémoire | Nom complet |
| :-------- | :----------------- | :-------- | :--------- | :------------- | :---------- |
| **GPU** | **H100-80gb** | `h100` | `h100` | `h100_80gb` | `nvidia_h100_80gb_hbm3` |
| **MIG** | **H100-1g.10gb** | `h100_1g.10gb` | `h100_1.10` | `h100_10gb` | `nvidia_h100_80gb_hbm3_1g.10gb` |
| **MIG** | **H100-2g.20gb** | `h100_2g.20gb` | `h100_2.20` | `h100_20gb` | `nvidia_h100_80gb_hbm3_2g.20gb` |
| **MIG** | **H100-3g.40gb** | `h100_3g.40gb` | `h100_3.40` | `h100_40gb` | `nvidia_h100_80gb_hbm3_3g.40gb` |

Pour demander un ou plusieurs GPU H100 complets, utilisez une des options Slurm suivantes :

*   **un H100-80gb** : `--gpus=h100:1` ou `--gpus=h100_80gb:1`
*   **plusieurs H100-80gb** par nœud :
    *   `--gpus-per-node=h100:2`
    *   `--gpus-per-node=h100:3`
    *   `--gpus-per-node=h100:4`
*   **plusieurs GPU H100 complets** distribués arbitrairement : `--gpus=h100:n` (remplacer n par le nombre de GPU que vous voulez)

Environ la moitié des nœuds GPU utilisent [la technologie MIG](../programming/multi-instance_gpu.md). Trois tailles d'instances sont disponibles :

*   **H100-1g.10gb** : 1/8e de la puissance de calcul, mémoire GPU de 10 Go
*   **H100-2g.20gb** : 2/8e de la puissance de calcul, mémoire GPU de 20 Go
*   **H100-3g.40gb** : 3/8e de la puissance de calcul, mémoire GPU de 40 Go

Pour demander **une et une seule instance GPU** pour une tâche de calcul, utilisez l'option correspondante.

*   **H100-1g.10gb** : `--gpus=h100_1g.10gb:1`
*   **H100-2g.20gb** : `--gpus=h100_2g.20gb:1`
*   **H100-3g.40gb** : `--gpus=h100_3g.40gb:1`

Pour le nombre maximum de cœurs CPU et le maximum de mémoire recommandés par instance GPU, voir [Ratios dans les *bundles*](../running-jobs/allocations_and_compute_scheduling.md#ratios-dans-les-bundles).

## Particularités

### Accès à l'internet

Tous les nœuds ont accès à l'internet; aucune autorisation de pare-feu spéciale ou proxy n'est nécessaire.

### /project et /nearline

Les répertoires des utilisateurs ne sont plus créés par défaut dans `/project` et `/nearline`. Vous pouvez toujours créer vos propres répertoires dans les espaces `/project` et `/nearline` du groupe à l'aide de `mkdir`. Ceci permet aux groupes de décider de l'organisation de leurs espaces `/project` et `/nearline` pour le partage de données entre les membres.

### Quota pour /scratch

Un quota souple de 1 To sur `/scratch` s'applique à chaque utilisateur. Ce quota souple peut être dépassé pendant 60 jours maximum, après quoi aucun fichier supplémentaire ne peut être écrit sur `/scratch`. Les fichiers peuvent être réécrits une fois que l'utilisateur a supprimé suffisamment de fichiers pour ramener son utilisation `/scratch` totale sous 1 To. Pour plus d'information, voir [Stockage et gestion de fichiers](../storage-and-data/storage_and_file_management.md).

### Accès via Open OnDemand (OOD)

Il est possible d'accéder à la grappe Nibi simplement via un navigateur web. Nibi utilise Open OnDemand (OOD), une plateforme web qui simplifie l'accès en fournissant une interface web aux nœuds de connexion et un environnement de bureau à distance. Pour vous connecter à Nibi, rendez-vous sur [ondemand.sharcnet.ca](https://ondemand.sharcnet.ca) et connectez-vous avec [l'authentification multifacteur](../getting-started/multifactor_authentication.md). Une interface conviviale s'affichera, proposant des options pour ouvrir un terminal Bash ou lancer une session de bureau à distance.

### Utilisation de JupyterLab via OOD

Vous pouvez exécuter JupyterLab de manière interactive via le [portail Nibi Open OnDemand](https://ondemand.sharcnet.ca).

**Option 1** : Travailler dans un environnement préconfiguré (même que [JupyterHub](../interactive/jupyterhub.md))

Quand la connexion au [portail Nibi Open OnDemand](https://ondemand.sharcnet.ca) est établie, cliquez sur *Nœud de calcul* dans le menu du haut et sélectionnez *JupyterLab Nibi*. Une page sera affichée dans laquelle un formulaire vous permet de demander une nouvelle session JupyterLab Nibi.

Après avoir rempli le formulaire avec les détails, cliquez sur *Lancer* pour soumettre votre demande. Quand l'état des modifications pour JupyterLab Nibi passe à *En cours d'exécution*, cliquez sur *Se connecter à Jupyter* pour ouvrir JupyterLab dans le navigateur web.

Pour les détails sur la préconfiguration, voir [Interface JupyterLab](../interactive/jupyterlab.md#interface-jupyterlab).

**Option 2** : Travailler dans un [environnement virtuel Python](../software/python.md) que vous avez créé

Quand la connexion au [portail Nibi Open OnDemand](https://ondemand.sharcnet.ca) est établie, cliquez sur *Nœud de calcul* dans le menu du haut et sélectionnez *Bureau de calcul*. Une page sera affichée dans laquelle un formulaire vous permet de demander une nouvelle session Bureau de calcul.

Après avoir rempli le formulaire avec les détails, cliquez sur *Lancer* pour soumettre votre demande. Quand le bureau de calcul passe à *En cours d'exécution*, cliquez sur *Lancer le bureau de calcul* pour vous connecter au bureau. Un bureau Linux sera affiché.

Sur le bureau de calcul, faites un clic droit dans une zone vide; un menu contextuel apparaît. Sélectionnez *Ouvrir dans un terminal* pour ouvrir une fenêtre de terminal où vous pouvez créer ou activer votre environnement virtuel Python dans lequel JupyterLab est installé.

Si JupyterLab n'est pas installé dans l'environnement virtuel Python que vous souhaitez utiliser, vous pouvez l'installer avec la commande

```bash
# (your_python_ENV) [username@<node>.nibi]$
pip install --no-index jupyterlab
```

Vous pouvez ensuite lancer JupyterLab à partir de votre environnement virtuel Python avec

```bash
# (your_python_ENV) [username@<node>.nibi]$
jupyter-lab --notebook-dir $HOME
```

JupyterLab s'ouvre dans le navigateur sur le bureau et le contenu de votre espace `$HOME` est listé dans le panneau de gauche.

### Prise en charge de VDI via OOD

Nibi n'offre plus d'infrastructure de bureau virtuel (VDI), mais fournit un environnement de bureau à distance via le [portail Open OnDemand (OOD)](https://ondemand.sharcnet.ca/) avec des performances matérielles et une prise en charge logicielle améliorées.

### Nœuds AMD MI300A

Il faut présentement demander les MI300A comme des nœuds entiers. Vous avez la responsabilité de vous assurer que les processus de votre tâche sont exécutés avec les liaisons correctes des cœurs et de la mémoire. Dans l'exemple ci-dessous, le script utilise quatre processus.

!!! warning "REMARQUE"
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
# [username@<node>.nibi]$
ls
```
```text
dont_delete_me.txt
```
```bash
# [username@<node>.nibi]$
rm dont_delete_me.txt
```
```bash
# [username@<node>.nibi]$
ls
```
```bash
# [username@<node>.nibi]$
oops
```
```text
Deleted files found in snapshots:
./.snapshot/backup_2026-04-01_18_00_00_UTC/dont_delete_me.txt
Files created less than 9 min ago (2026-04-01 14:00:00-04:00) are not yet backed up
Files deleted more than 0 days ago (2026-04-01 13:30:00-04:00) please submit a help ticket
```
```bash
# [username@<node>.nibi]$
cp ./.snapshot/backup_2026-04-01_18_00_00_UTC/dont_delete_me.txt .
```
```bash
# [username@<node>.nibi]$
ls
```
```text
dont_delete_me.txt