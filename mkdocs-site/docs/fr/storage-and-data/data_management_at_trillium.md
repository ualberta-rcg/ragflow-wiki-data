---
title: "Data management at Trillium/fr"
slug: "data_management_at_trillium"
lang: "fr"

source_wiki_title: "Data management at Trillium/fr"
source_hash: "059c9513f43bb548cc229bcca6b97a09"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T06:03:06.615492+00:00"

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

Pour travailler de façon optimale et faire bon usage des ressources, il faut bien connaître les divers systèmes de fichiers. Nous donnons ici des renseignements sur comment les utiliser correctement.

## Performance
À l'exception de `/archive`, les systèmes de fichiers hautement performants de SciNet sont de type [GPFS](http://en.wikipedia.org/wiki/IBM_General_Parallel_File_System); ils permettent des opérations parallèles de lecture et d'écriture rapides avec de grands ensembles de données, à partir de plusieurs nœuds. Par contre, de par sa conception, sa performance laisse beaucoup à désirer quand il s'agit d'accéder à des ensembles de données composés de plusieurs petits fichiers. En effet, il est beaucoup plus rapide de lire un fichier de 16 Mo que 400 fichiers de 40 Ko. Rappelons que dans ce dernier cas, autant de petits fichiers n'est pas une utilisation efficace de l'espace puisque la [capacité des blocs](https://en.wikipedia.org/wiki/Block_(data_storage)) est de 16 Mo pour les systèmes `scratch` et `project`. Tenez compte de ceci dans votre stratégie de lecture/écriture.

Par exemple, pour exécuter une tâche multiprocessus, le fait que chaque processus écrive dans son propre fichier n'est pas une solution I/O flexible; le répertoire est bloqué par le premier processus qui l'accède et les suivants doivent attendre. Non seulement cette solution rend-elle le code considérablement moins parallèle, mais le système de fichiers sera arrêté en attendant le prochain processus et votre programme se terminera mystérieusement.

!!! tip "Astuce"
    Utilisez plutôt MPI-IO (partie du standard MPI-2) qui permet à des processus différents d'ouvrir simultanément des fichiers, ou encore un processus I/O dédié qui écrit dans un seul fichier toutes les données envoyées par les autres processus.

## Utilisation des systèmes de fichiers
Trillium donne accès à plusieurs systèmes de fichiers différents, mais ils ne sont pas tous disponibles à tous les utilisateurs.

### /home ($HOME)
*   Utilisé d'abord pour les fichiers d'un utilisateur, les logiciels communs ou les petits ensembles de données partagés par le groupe d'utilisateurs, pourvu que le quota de l'utilisateur ne soit pas dépassé; dans le cas contraire utilisez plutôt /scratch ou /project.
*   En lecture seulement sur les nœuds de calcul.

### /scratch ($SCRATCH)
*   Utilisé d'abord pour les fichiers temporaires, les résultats de calcul et de simulations, et le matériel qui peut être obtenu ou recréé facilement. Peut aussi être utilisé pour une étape intermédiaire dans votre travail pourvu que cela ne cause pas trop d'opérations I/O ou trop de petits fichiers pour cette solution de stockage sur disque, auquel cas vous devriez utiliser /bb (*burst buffer*). Une fois que vous avez obtenu les résultats que vous voulez conserver à long terme, vous pouvez les transférer à /project ou /archive.
*   Purgé régulièrement; aucune copie de sauvegarde n'est faite.

### /project ($PROJECT)
/project est destiné aux logiciels de groupe courants, aux grands ensembles de données statiques ou à tout contenu très coûteux à acquérir ou à régénérer par le groupe.

!!! warning "Avertissement important"
    Le contenu de /project est censé rester relativement immuable au fil du temps.

Les fichiers temporaires ou transitoires doivent être conservés sur /scratch plutôt que sur /project. Les mouvements fréquents de données engendrent une surcharge et une consommation inutile des bandes sur le système de sauvegarde TSM, longtemps après leur suppression, et ceci en raison des politiques de conservation des sauvegardes et des versions supplémentaires conservées du même fichier. Le simple fait de renommer les répertoires principaux suffit à tromper le système et à lui faire croire qu'une arborescence de répertoires entièrement nouvelle a été créée et que l'ancienne a été supprimée. Réfléchissez donc soigneusement à vos conventions de nommage et respectez-les. Si vous abusez du système de fichiers /projet et l'utilisent comme /scratch, nous vous demanderons de procéder autrement. Notez que sur Trillium, /project est uniquement accessible aux groupes disposant de ressources allouées par concours.

### /bb ($BBUFFER)
*   [Burst buffer](https://docs.scinet.utoronto.ca/index.php/Burst_Buffer) est une alternative rapide et performante à /scratch, sur disque SSD. Utilisez cette ressource si vous prévoyez beaucoup d'opérations I/O ou si vous remarquez une faible performance d'une tâche sur /scratch ou /project en raison d'un goulot d'étranglement des opérations I/O.
*   Voir [cette page wiki de SciNet](https://docs.scinet.utoronto.ca/index.php/Burst_Buffer).

### /archive ($ARCHIVE)
*   Espace de stockage *nearline* pour une copie temporaire de matériel semi-actif du contenu des systèmes de fichiers décrits plus haut. En pratique, les utilisateurs déchargent et rappellent du matériel dans le cours de leur travail ou quand les quotas sont atteints sur /scratch ou /project. Ce matériel peut demeurer sur HPSS de quelques mois jusqu'à quelques années.
*   Réservé aux groupes qui ont obtenu une allocation par suite des concours.

### /dev/shm (RAM)
*   Les nœuds ont un [ramdisk](https://docs.scinet.utoronto.ca/index.php/User_Ramdisk) plus rapide qu'un disque réel et que *burst buffer*. Jusqu'à 70 % de la RAM du nœud (202 Go) peut être utilisé comme système de fichiers **local** temporaire. Ceci est très utile dans les premières étapes de migration de programmes d'un ordinateur personnel vers une plateforme de CHP comme Trillium, particulièrement quand le code utilise beaucoup d'opérations I/O. Dans ce cas, un goulot d'étranglement se forme, surtout avec les systèmes de fichiers parallèles comme GPFS (utilisé sur Trillium), puisque les fichiers sont synchronisés sur l'ensemble du réseau.

### $SLURM_TMPDIR (RAM)
Comme c'est le cas avec les grappes d'usage général, la variable d'environnement `$SLURM_TMPDIR` sera utilisée sur Trillium pour les tâches de calcul. Elle pointera sur RAMdisk et non sur les disques durs locaux. Le répertoire `$SLURM_TMPDIR` est vide lorsque la tâche commence et son contenu est supprimé après que la tâche est complétée.

### Espace tampon temporaire pour utilisation massive (*burst*) ($BB_JOB_DIR)
Pour chaque tâche sur Trillium, l'ordonnanceur crée un répertoire temporaire dans `$BB_JOB_DIR`. Ce répertoire est vide au lancement de la tâche et son contenu est supprimé une fois celle-ci terminée. Il est accessible à partir de tous les nœuds de la tâche.

`$BB_JOB_DIR` est un emplacement pour les applications qui génèrent plusieurs petits fichiers temporaires ou encore des fichiers qui sont fréquemment utilisés (c'est-à-dire avec des IOPS élevées), mais qui ne peuvent pas être contenus sur disque virtuel.

Il est important de noter que si ramdisk peut contenir les fichiers temporaires, c'est généralement un meilleur endroit que le *burst buffer* parce que la bande passante et les IOPS y sont beaucoup plus grands. Pour utiliser ramdisk, vous pouvez soit accéder /dev/shm directement, soit utiliser la variable d'environnement `$SLURM_TMPDIR`.

Les nœuds de calcul de Trillium n'ont pas de disques locaux; `$SLURM_TMPDIR` est en mémoire (ramdisk), contrairement aux grappes généralistes comme Fir et Nibi où cette variable pointe vers un répertoire sur le SSD d'un nœud local.

## Quotas et purge
Familiarisez-vous avec les différents systèmes de fichiers, leur utilité et leur utilisation correcte. Ce tableau récapitule les points principaux.

| Système de fichiers | Quota                                                                           | Taille des blocs | Durée      | Sauvegarde | Sur nœuds de connexion | Sur nœuds de calcul |
| :------------------ | :------------------------------------------------------------------------------ | :--------------- | :--------- | :--------- | :--------------------- | :---------------- |
| `$HOME`             | 100 Go par utilisateur                                                          | 1 Mo             |            | oui        | oui                    | lecture seule     |
| `$SCRATCH`          | 25 To par utilisateur (si quota du groupe non atteint)                          | 16 Mo            | 2 mois     | non        | oui                    | oui               |
|                     | Groupes de 4 utilisateurs ou moins : 50 To pour le groupe                       |                  |            |            |                        |                   |
|                     | Groupes de 11 utilisateurs ou moins : 125 To pour le groupe                     |                  |            |            |                        |                   |
|                     | Groupes de 28 utilisateurs ou moins : 250 To pour le groupe                     |                  |            |            |                        |                   |
|                     | Groupes de 60 utilisateurs ou moins : 400 To pour le groupe                     |                  |            |            |                        |                   |
|                     | Groupes de plus de 60 utilisateurs : 500 To pour le groupe                      |                  |            |            |                        |                   |
| `$PROJECT`          | allocation de groupe                                                            | 16 Mo            |            | oui        | oui                    | oui               |
| `$ARCHIVE`          | allocation de groupe                                                            |                  |            | 2 copies   | non                    | non               |
| `$BBUFFER`          | 10 To par utilisateur                                                           | 1 Mo             | très court | non        | oui                    | oui               |

*   [Voir **Inode vs. Space quota** (PROJECT et SCRATCH)](https://docs.scinet.utoronto.ca/images/9/9a/Inode_vs._Space_quota_-_v2x.pdf)
*   [Voir **dynamic quota per group** (SCRATCH)](https://docs.scinet.utoronto.ca/images/0/0e/Scratch-quota.pdf)
*   Les nœuds de calcul ne disposent pas de stockage local.
*   L'espace d'archivage se trouve sur [HPSS](https://docs.scinet.utoronto.ca/index.php/HPSS) et n'est pas accessible sur les nœuds de connexion, de calcul ou de copie de Trillium.
*   La sauvegarde est un instantané récent, et non une archive de toutes les données existantes.
*   L'espace tampon pour utilisation intensive [**$BBUFFER**](https://docs.scinet.utoronto.ca/index.php/Burst_Buffer) est un niveau de stockage parallèle plus rapide pour les données temporaires.

## Espace disque disponible
Disponible sur les nœuds de connexion et les nœuds de copie, la commande `diskUsage` fournit beaucoup d'information sur les systèmes de fichiers. Par exemple, vous pouvez connaître combien d'espace disque est utilisé par vous-même ou par votre groupe, voir comment votre utilisation évolue au cours d'une période, ou encore générer divers graphiques. Voir ci-dessous pour plus d'information.

```bash
Usage: diskUsage [-h|-?| [-a] [-u <user>]
       -h|-?: help
       -a: list usages of all members on the group
       -u <user>: as another user on your group
```

Utilisez les commandes suivantes pour vérifier l'espace qui vous reste :
*   `/scinet/niagara/bin/topUserDirOver1000list` pour identifier les répertoires qui contiennent plus de 1000 fichiers.
*   `/scinet/niagara/bin/topUserDirOver1GBlist` pour identifier les répertoires qui contiennent plus de 1 Go de matériel.

!!! note "Note"
    L'information sur l'utilisation et les quotas est mise à jour toutes les trois heures.

## Politique de purge du disque Scratch
Afin d'assurer qu'il y ait toujours un espace significatif disponible pour l'exécution des tâches, **nous supprimons automatiquement les fichiers dans /scratch qui n'ont pas été accédés ou modifiés depuis plus de 2 mois à la date de suppression réelle, le 15 de chaque mois**. Notez que nous avons récemment modifié la référence de suppression pour utiliser la plus récente des dates (*MostRecentOf(atime,ctime)*). Cette politique est sujette à révision en fonction de son efficacité. Plus de détails sur le processus de purge et comment les utilisateurs peuvent vérifier si leurs fichiers seront supprimés suivent. Si vous avez des fichiers programmés pour suppression, vous devriez les déplacer vers des emplacements plus permanents tels que votre serveur départemental, votre espace /project, ou vers HPSS (pour les chefs de projet qui ont obtenu une allocation d'espace de stockage par le CERA sur project ou HPSS).

Le **premier** de chaque mois, une liste des fichiers programmés pour la purge est produite, et une notification par courriel est envoyée à chaque utilisateur figurant sur cette liste. Vous recevez également une notification sur le terminal chaque fois que vous vous connectez à Trillium. De plus, vers le **12** de chaque mois, une deuxième analyse produit une évaluation plus actuelle et une autre notification par courriel est envoyée. Ainsi, les utilisateurs peuvent revérifier qu'ils ont bien déplacé tous les fichiers nécessaires avant la date limite de purge. Ces fichiers seront automatiquement supprimés le **15** du même mois, à moins qu'ils n'aient été accédés ou déplacés entre-temps. Si vous avez des fichiers programmés pour suppression, ils seront listés dans un fichier situé dans /scratch/t/todelete/current, dont le nom contient votre identifiant d'utilisateur (`userid`) et votre identifiant de groupe (`groupid`). Par exemple, si l'utilisateur `xxyz` veut vérifier s'il a des fichiers programmés pour suppression, il peut exécuter la commande suivante sur un système qui monte /scratch (p. ex. un nœud de connexion SciNet) : `**ls -1 /scratch/t/todelete/current | grep xxyz**`.

```text
 [xxyz@nia-login03 ~]$ ls -1 /scratch/t/todelete/current |grep xxyz
 -rw-r----- 1 xxyz     root       1733059 Jan 17 11:46 3110001___xxyz_______abc_________1.00T_____9560files
```

Dans l'exemple ci-dessus, le nom de ce fichier indique que l'utilisateur `xxyz` fait partie du groupe `abc`, a 9 560 fichiers programmés pour suppression, et qu'ils occupent 1,0 To d'espace.

Le fichier lui-même contient une liste de tous les fichiers programmés pour la suppression (dans la dernière colonne) et peut être visualisé avec des commandes standard comme `more`/`less`/`cat` - par exemple `**more /scratch/t/todelete/current/3110001___xxyz_______abc_________1.00T_____9560files**`.

De même, vous pouvez vérifier tous les autres membres de votre groupe en utilisant la commande `ls` avec `grep` pour votre groupe. Par exemple, `**ls -1 /scratch/t/todelete/current | grep abc**` listera les autres membres dont fait partie `xxyz` et dont les fichiers doivent être purgés le 15 du mois. Les membres d'un même groupe ont accès au contenu des autres.

!!! note "Note"
    La préparation de ces évaluations prend plusieurs heures. Si vous modifiez le temps d'accès ou de modification d'un fichier entre-temps, cela ne sera pas détecté avant le prochain cycle. Pour obtenir une rétroaction immédiate, utilisez la commande `**ls -lu**` sur le fichier pour vérifier le `ctime` et `**ls -lc**` pour le `mtime`. Si le `atime`/`ctime` du fichier a été mis à jour entre-temps, il ne sera plus supprimé à la date de purge du 15.

## Déplacer des données
Les données pour l'analyse et les résultats finaux doivent être déplacées de et vers Trillium. Il y a plusieurs façons d'y parvenir.

### Avec rsync/scp
**Déplacer moins de 10 Go par les nœuds de connexion**

*   Les nœuds de connexion et de copie sont visibles de l'extérieur de SciNet.
*   Utilisez `scp` ou `rsync` pour vous connecter à un des sites parmi `tri-dm{2,3,4}.scinet.utoronto.ca`.
*   Il y aura interruption dans le cas de plus d'environ 10 Go.

**Déplacer plus de 10 Go par les nœuds de copie**

*   À partir d'un nœud de connexion, utilisez `ssh` vers `nia-datamover1` ou `nia-datamover2`; de là, vous pouvez transférer de ou vers Trillium.
*   Vous pouvez aussi aller aux nœuds de copie de l'extérieur en utilisant `login`/`scp`/`rsync`.
    *   `nia-datamover1.scinet.utoronto.ca`
    *   `nia-datamover2.scinet.utoronto.ca`
*   Si vous faites souvent ceci, considérez utiliser [Globus](globus.md), un outil web pour le transfert de données.

### Utiliser Globus
Pour la documentation, consultez la [page wiki de Calcul Canada](globus.md) et la [page wiki de SciNet](https://docs.scinet.utoronto.ca/index.php/Globus).

Le point de chute Globus est :
*   *alliancecan#trillium* pour Trillium
*   *alliancecan#hpss* pour HPSS.

### Déplacer des données vers HPSS/Archive/Nearline
HPSS est conçu pour le stockage de longue durée.

*   [HPSS](https://docs.scinet.utoronto.ca/index.php/HPSS) est une solution de stockage sur bandes employée comme espace *nearline* par SciNet.
*   L'espace de stockage sur HPSS est alloué dans le cadre du [concours d'allocation de ressources](resource-allocation-competition.md).

## Propriété des fichiers et listes de contrôle d'accès
*   Sur SciNet, les utilisateurs d'un même groupe ont par défaut l'autorisation de lecture pour les fichiers des autres, mais pas celle d'écriture.
*   Vous pouvez utiliser une liste de contrôle d'accès (ACL) pour permettre à votre superviseur (ou à un autre utilisateur de votre groupe) de gérer vos fichiers (créer, déplacer, renommer, supprimer), tout en conservant vos droits d'accès et d'autorisation en tant que propriétaire initial des fichiers et répertoires. Vous pouvez également autoriser des utilisateurs d'autres groupes, voire des groupes entiers, à accéder à vos fichiers (lecture, exécution) grâce à ce même mécanisme.

### Commandes `mmputacl` et `mmgetacl`
*   Ces commandes de GPFS vous permettent de configurer le contrôle des permissions et [les ACL POSIX ou NFS v4](http://publib.boulder.ibm.com/infocenter/clresctr/vxrx/index.jsp?topic=%2Fcom.ibm.cluster.gpfs.doc%2Fgpfs31%2Fbl1adm1160.html) sont prises en charge. Vous devez d'abord créer un fichier `/tmp/supervisor.acl` avec le contenu suivant :

```text
user::rwxc
group::----
other::----
mask::rwxc
user:[owner]:rwxc
user:[supervisor]:rwxc
group:[othegroup]:r-xc
```

Lancez ensuite les deux commandes :

```bash
1) $ mmputacl -i /tmp/supervisor.acl /project/g/group/[owner]
2) $ mmputacl -d -i /tmp/supervisor.acl /project/g/group/[owner]
   (every *new* file/directory inside [owner] will inherit [supervisor] ownership by default as well as
   [owner] ownership, ie, ownership of both by default, for files/directories created by [supervisor])

$ mmgetacl /project/g/group/[owner]
   (to determine the current ACL attributes)

$ mmdelacl -d /project/g/group/[owner]
   (to remove any previously set ACL)

$ mmeditacl /project/g/group/[owner]
   (to create or change a GPFS access control list)
   (for this command to work set the EDITOR environment variable: export EDITOR=/usr/bin/vi)
```

!!! note "Remarque"
    Il n'est pas possible d'ajouter ou de supprimer récursivement des attributs ACL à des fichiers existants à l'aide d'une commande intégrée à GPFS. Vous devrez utiliser l'option `-i` comme indiqué ci-dessus pour chaque fichier ou répertoire individuellement. [Voici un exemple de script bash que vous pouvez utiliser à cette fin.](https://docs.scinet.utoronto.ca/index.php/Recursive_ACL_script)

*   La commande `mmputacl` ne remplacera pas les permissions de groupe Linux originales d'un répertoire lorsqu'il est copié vers un autre répertoire ayant déjà des ACLs; d'où la note « #effective:r-x » que vous pouvez voir de temps à autre avec `mmgetacl`. Si vous souhaitez accorder des permissions `rwx` à tous les membres de votre groupe, vous devriez simplement utiliser la commande Unix standard `chmod g+rwx`. Vous pouvez le faire avant ou après avoir copié le matériel original vers un autre dossier avec les ACLs.

*   Dans le cas de PROJECT, la personne responsable de votre groupe devra définir l'ACL appropriée au niveau `/project/G/GROUP` afin de permettre aux utilisateurs d'autres groupes d'accéder à vos fichiers.

*   ACL ne vous permet pas d'accorder des permissions pour des fichiers ou des répertoires qui ne vous appartiennent pas.

!!! warning "Avertissement important"
    Nous vous recommandons vivement de ne jamais accorder d'autorisation d'écriture à d'autres personnes au niveau supérieur de votre répertoire personnel (`/home/G/GROUP/[owner]`), car cela compromettrait gravement votre confidentialité, et de désactiver l'authentification par clé SSH, entre autres. Si nécessaire, créez des sous-répertoires spécifiques sous votre répertoire personnel afin que d'autres puissent y accéder et manipuler les fichiers.

Pour plus d'information, consultez [mmputacl](https://www.ibm.com/support/knowledgecenter/SSFKCN_4.1.0/com.ibm.cluster.gpfs.v4r1.gpfs100.doc/bl1adm_mmputacl.htm) et [mmgetacl](https://www.ibm.com/support/knowledgecenter/SSFKCN_4.1.0/com.ibm.cluster.gpfs.v4r1.gpfs100.doc/bl1adm_mmgetacl.htm).

### Script ACL récursif
Vous pouvez utiliser et adapter [cet exemple de script bash](https://docs.scinet.utoronto.ca/index.php/Recursive_ACL_script) pour ajouter ou supprimer récursivement des attributs ACL à l'aide des commandes intégrées de GPFS.

Gracieuseté de Agata Disks (http://csngwinfo.in2p3.fr/mediawiki/index.php/GPFS_ACL).