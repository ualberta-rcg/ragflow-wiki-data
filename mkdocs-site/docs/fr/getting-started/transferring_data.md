---
title: "Transferring data/fr"
tags:
  - connecting
  - se-connecter

keywords:
  []
---

Pour transférer des données à partir ou en direction des grappes, veuillez utiliser les nœuds de copie plutôt que les nœuds de connexion. Pour connaître l'adresse URL d'un nœud de copie, consultez le tableau au haut des pages pour chacune des grappes (cliquez sur le nom de la grappe dans la barre de gauche de la fenêtre principale).

[Globus](globus-fr.md) utilise automatiquement les nœuds de copie.

## Entre un ordinateur personnel et nos équipements
Pour télécharger ou téléverser des fichiers entre votre ordinateur et notre infrastructure, vous devez utiliser un logiciel offrant une fonctionnalité de transfert sécuritaire.
*Dans un environnement ligne de commande sous Linux ou Mac OS X, utilisez les commandes `scp` et `sftp`.
*Sous Windows, [MobaXterm](connecting-with-mobaxterm-fr.md) offre des fonctions de transfert de fichiers et une interface ligne de commande via  [SSH](ssh-fr.md); un autre programme gratuit pour le transfert de données est [WinSCP](https://winscp.net/eng/docs/lang:fr). Pour configurer une connexion via clés SSH avec WinSCP, voyez [ces directives](https://www.exavault.com/blog/import-ssh-keys-winscp).
Les commandes `pscp` et `psftp` de [PuTTY](connecting-with-putty-fr.md) fonctionnent sensiblement comme les commandes sous Linux et Mac.

S'il faut plus d'une minute pour transférer des fichiers entre votre ordinateur et nos serveurs, nous vous suggérons d'installer <i>Globus Connect Personal</i> et d'en faire l'essai; consultez la section [Ordinateurs personnels](globus-fr#ordinateurs_personnels.md). Le transfert avec Globus peut être configuré et fonctionner en arrière-plan, sans intervention.

## Entre nos systèmes 
[Globus](globus-fr.md) est l'outil privilégié et devrait être utilisé autant que possible.

D'autres outils de transfert connus peuvent être utilisés pour des transferts entre nos équipements et entre un autre ordinateur et nos équipements, soit
* [SFTP](transferring_data-fr#sftp.md)
* [SCP](transferring_data-fr#scp.md) ou Secure Copy Protocol
* [rsync](transferring_data-fr#rsync.md)

Remarque : Pour transférer des fichiers entre une autre grappe et Trilloium, utilisez l'indicateur SSH `-A` en vous connectant à l'autre grappe. Par exemple, pour copier des fichiers de Fir à Trillium, la commande serait

<pre>
ssh -A USERNAME@fir.alliancecan.ca
</pre>
ensuite, effectuez la copie
<pre>
[USERNAME@fir2 ~]$ scp file USERNAME@trillium.alliancecan.ca:
</pre>

## À partir du web
Pour transférer des données à partir d'un site web, utilisez [wget](https://fr.wikipedia.org/wiki/GNU_Wget). Un autre outil bien connu est [curl](https://curl.haxx.se/). Les deux outils sont comparés dans [cet article de StackExchange](https://unix.stackexchange.com/questions/47434/what-is-the-difference-between-curl-and-wget) ou sur  [le site DraculaServers](https://draculaservers.com/tutorials/wget-and-curl-for-files/). Même si notre sujet ici est le transfert entre les systèmes Linux de l'Alliance, nous voulons souligner [ce tutoriel](https://www.techtarget.com/searchnetworking/tutorial/Use-cURL-and-Wget-to-download-network-files-from-CLI) qui discute aussi de Mac et Windows. Les téléchargements interrompus peuvent être repris avec [wget](https://www.thegeekstuff.com/2009/09/the-ultimate-wget-download-guide-with-15-awesome-examples/) et [curl](https://www.thegeekstuff.com/2012/04/curl-examples/) en les relançant de nouveau en ligne de commande avec  [-c](https://www.cyberciti.biz/tips/wget-resume-broken-download.html) et [-C -](https://www.cyberciti.biz/faq/curl-command-resume-broken-download/) respectivement. Pour obtenir des données de services infonuagiques comme Google cloud, Google Drive et Google Photos, utilisez plutôt [rclone](https://rclone.org/).  Par défaut, nos grappes offrent wget, curl et rclone sans avoir à charger un  module. Pour les options en ligne de commande, voir la documentation officielle ou lancez l'outil avec les commandes `--help` ou `-h`.

## Synchroniser les données
La synchronisation de données a pour but de faire correspondre le contenu de deux sources de données situées à différents endroits. Il y a plusieurs façons de procéder; les plus courantes sont décrites ici.

### Transfert avec Globus
Globus est un outil performant et fiable.

Lors d'un transfert avec Globus, les données provenant de la source écrasent habituellement les données dans la destination; toutes les données de la source sont donc transférées. Dans certains cas, les fichiers existent déjà à la destination; s'ils sont identiques à ceux de la source, il n'est pas nécessaire de les transférer. Sous <i>Transfer Settings</i>, le paramètre `sync` détermine comment Globus choisit les fichiers à transférer.

[280px|thumb|left|alt="Globus file transfer sync options"](file:globus_transfer_sync_options.png.md)

Les options de sélection des fichiers sont :
{| class="wikitable"
|-
| <i>checksum is different</i>  || examine les sommes de contrôle (<i>checksum</i>) pour détecter un changement ou une erreur de contenu dans des fichiers de même taille. Cette option ralentit considérablement le transfert, mais offre la plus grande précision.
|-
| <i>file doesn't exist on destination</i> || transfère uniquement les fichiers créés depuis la dernière synchronisation. Cette option est utile si vos fichiers sont créés par incréments.
|-
| <i>file size is different</i> || transfère les fichiers dont la taille a été modifiée, assumant que le contenu aussi a été modifié. Cette option permet un test rapide.

|-
| <i>modification time is newer</i> || transfère uniquement les fichiers dont l'estampille temporelle (*timestamp*) de la source est postérieure à celle de la destination. Avec cette option, cochez *preserve source file modification times*.
|}

Pour plus d'information, consultez la page [Globus](globus-fr.md).

<br clear="all"/>

### rsync
L'utilitaire [rsync](https://fr.wikipedia.org/wiki/Rsync) vérifie la similitude entre deux jeux de données; il nécessite toutefois un temps considérable lorsqu'il y a un grand nombre de fichiers, que les sites sont à grande distance l'un de l'autre, ou qu'ils se trouvent sur des réseaux différents.

`rsync` compare les dates de modification et la taille des fichiers et fait le transfert uniquement si l'un des paramètres ne concorde pas.
Si les dates de modification sont susceptibles de différer, l'option `-c` analyse les checksums à la source et à la destination et transfère uniquement les fichiers dont les valeurs ne concordent pas. 

Quand vous transférez des données vers les systèmes de fichiers `/project`, n'utilisez pas les indicateurs `-p` et `-g`. Les quotas pour `/project` sont calculés selon la propriété de groupe et le fait de conserver la même propriété pourrait produire le message d'erreur [<i>Disk quota exceeded</i>](frequently_asked_questions-fr#message_disk_quota_exceeded.md). Puisque `-a` inclut par défaut à la fois `-p` et `-g`, il faut ajouter les options `--no-g --no-p` comme suit

```bash
rsync -avzh --no-g --no-p LOCALNAME someuser@nibi.alliancecan.ca:projects/def-professor/someuser/somedir/
```

où LOCALNAME est un répertoire ou un fichier précédés par leur chemin et où somedir sera créé s'il n'existe pas déjà.  L'option `-z` compresse les fichiers (dont les suffixes ne sont pas dans la liste  pour l'option `--skip-compress`) et exige des ressources CPU additionnelles, alors que l'option `-h` permet de simplifier les chiffres qui représentent la taille des fichiers.  Si vous transférez de très gros fichiers, ajoutez l'option `--partial` pour que les transferts interrompus soient redémarrés. 

```bash
rsync -avzh --no-g --no-p --partial --progress LOCALNAME someuser@nibi.alliancecan.ca:projects/def-professor/someuser/somedir/
```

L'option `--progress` affiche la progression du transfert de chaque fichier. Pour le transfert de plusieurs petits fichiers, il est préférable d'afficher la progression du transfert de l'ensemble des fichiers.

```bash

```
progress2 LOCALNAME someuser@nibi.alliancecan.ca:projects/def-professor/someuser/somedir/}}
Les exemples ci-dessus sont tous des transferts à partir d'un système local à destination d'un système à distance. Les transferts à partir d'un système à distance à destination du répertoire /project d'un système local fonctionnent de la même manière, par exemple

```bash
rsync -avzh --no-g --no-p someuser@nibi.alliancecan.ca:REMOTENAME ~/projects/def-professor/someuser/somedir/
```

où REMOTENAME est un répertoire ou un fichier précédés par leur chemin et où somedir sera créé s'il n'existe pas déjà. 
Plus simplement, pour transférer localement un répertoire ou un fichier (à partir de /home ou /scratch) à destination de /project dans le même système, n'indiquez pas le nom de la grappe.

```bash
rsync -avh --no-g --no-p LOCALNAME ~/projects/def-professor/someuser/somedir/
```

où somedir sera créé s'il n'existe pas déjà, avant d'y copier le contenu de LOCALNAME.
En comparaison, la commande de copie peut aussi être utilisée pour transférer  LOCALNAME de /home à /project comme suit

```bash

```
"mode,timestamps" LOCALNAME ~/projects/def-professor/someuser/somedir/}}
Cependant, contrairement à ce qui se produit avec rsync, si LOCALNAME est un répertoire, il sera renommé somedir si somedir n'existe pas déjà.

### Comparaison des sommes de contrôle (<i>checksums</i>)
Si vous ne pouvez p-as utiliser Globus pour synchroniser deux systèmes et si rsync est trop lent, les deux systèmes peuvent être comparés avec un utilitaire [checksum](https://fr.wikipedia.org/wiki/Somme_de_contr%C3%B4le). L'exemple suivant utilise `sha1sum`.

```bash

```
 xargs -0 sha1sum  tee checksum-result.log
}}

Cette commande crée dans le répertoire courant un nouveau fichier nommé *checksum-result.log* contenant toutes les sommes de contrôle des fichiers situés dans /home/username/; les sommes sont affichées pendant que le processus se déroule.
Lorsqu'il y a un grand nombre de fichiers ou dans le cas de fichiers de très grande taille, rsync peut travailler en arrière-plan en mode [screen](https://fr.wikipedia.org/wiki/GNU_Screen), [tmux](https://fr.wikipedia.org/wiki/Tmux) ou tout autre moyen lui permettant d'opérer malgré un bris de la connexion [SSH](ssh.md).

Une fois l'opération terminée, l'utilitaire `diff` trouvera les fichiers qui ne concordent pas.

```bash
diff checksum-result-silo.log checksum-dtn.log
```

```
69c69
 < 017f14f6a1a194a5f791836d93d14beead0a5115  /home/username/file-0025048576-0000008
 ---
 > 8836913c2cc2272c017d0455f70cf0d698daadb3  /home/username/file-0025048576-0000008
```

Il est possible que la commande `find` emprunte un ordre différent, détectant ainsi de fausses différences; pour contrer ceci, lancez la commande `sort` sur les deux fichiers avant de lancer `diff`, comme suit :

```bash
sort -k2 checksum-dtn.log -o checksum-dtn.log
```

==SFTP== 
Pour transférer des fichiers, [SFTP](https://en.wikipedia.org/wiki/SSH_File_Transfer_Protocol) (pour *Secure File Transfer Protocol*) utilise le protocole SSH qui chiffre les données transférées.

Dans l'exemple suivant, l'utilisateur `USERNAME` transfère des fichiers à distance vers `ADDRESS`.

<source lang="console">
[name@server]$ sftp USERNAME@ADDRESS
The authenticity of host 'ADDRESS (###.###.###.##)' can't be established.
RSA key fingerprint is ##:##:##:##:##:##:##:##:##:##:##:##:##:##:##:##.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'ADDRESS,###.###.###.##' (RSA) to the list of known hosts.
USERNAME@ADDRESS's password:
Connected to ADDRESS.
sftp>
</source>
L'authentification avec l'option  `-i` peut se faire en utilisant une [clé SSH](https://docs.computecanada.ca/wiki/SSH_Keys/fr).
<source lang="console">
[name@server]$ sftp -i /home/name/.ssh/id_rsa USERNAME@ADDRESS
Connected to ADDRESS.
sftp>
</source>

À l'invite `sftp>`, vous entrez les commandes de transfert; utilisez la commande `help` pour obtenir la liste des commandes disponibles.

Des applications graphiques sont aussi disponibles : 
*[WinSCP](https://winscp.net/eng/index.php) et [MobaXterm](http://mobaxterm.mobatek.net/) sous Windows,
*[filezilla](https://filezilla-project.org) sous Windows, Mac et Linux,
*[cyberduck](https://cyberduck.io/?l=en), sous Mac et Windows.

==SCP== 

SCP est l'abréviation de [<i>secure copy protocol</i>](https://fr.wikipedia.org/wiki/Secure_copy). Comme SFTP, SCP utilise le protocole SSH pour chiffrer les données qui sont transférées. Contrairement à [Globus](https://docs.alliancecan.ca/wiki/Globus/fr) ou [rsync](https://docs.alliancecan.ca/wiki/Transferring_data/fr#rsync), SCP ne gère pas la synchronisation. Les cas d'utilisation de SCP suivants sont parmi les plus fréquents :

```bash
scp foo.txt username@rorqual.alliancecan.ca:work/
```
	
Cette commande transfère le fichier `foo.txt` qui se trouve dans le répertoire courant de mon ordinateur vers le répertoire `$HOME/work` de la grappe [Rorqual](rorqual.md). Pour transférer le fichier `output.dat` qui se trouve dans mon espace /project de la grappe [Fir](fir-fr.md) vers mon ordinateur local, je pourrais utiliser une commande comme

```bash
scp username@fir.alliancecan.ca:projects/def-jdoe/username/results/output.dat .
```
	
[Voyez d'autres exemples](http://www.hypexr.org/linux_scp_help.php). Prenez note que vous lancez toujours la commande `scp` à partir de votre ordinateur et non à partir de la grappe&nbsp;: la connexion SCP doit toujours être initiée à partir de votre ordinateur, peu importe la direction dans laquelle vous transférez les données. 

L'option `-r` permet de faire un transfert récursif d'un groupe de répertoires et fichiers. <b>Il n'est pas recommandé d'utiliser `scp -r`</b> pour transférer des données vers `/project` parce que le bit <tt>setGID</tt> est désactivé dans les répertoires qui sont créés, ce qui peut générer des erreurs semblables à `Disk quota exceeded` lors de la création ultérieure de fichiers; voyez [Message <i>Disk quota exceeded</i>](frequently_asked_questions-fr#message_disk_quota_exceeded.md).

<b><big>***Attention :***</big></b> si vous utilisez un nom de clé SSH personnalisé, <i>c'est-à-dire</i> autre chose que les noms par défaut `id_dsa`, `id_ecdsa`, `id_ed25519` et `id_rsa`, vous devez utiliser l'option scp `-i`, suivie du chemin vers votre clé privée ainsi

```bash
scp -i /path/to/key foo.txt username@rorqual.alliancecan.ca:work/
```

<span id="Prevention_and_Troubleshooting"></span>
## Mesures préventives et dépannage

<span id="Unable_to_read_data"></span>
### Problème de lecture

Assurez-vous que vous pouvez lire tout le contenu des répertoires <b><u>avant de les transférer</b></u>. Sous Linux, la commande suivante liste tous les éléments que vous n'avez pas en lecture.

```bash
find <directory_name> ! -readable -ls
```

<span id="Unable_to_write_new_data"></span>
### Problème d'écriture de nouvelles données

* Vérifiez encore <b>[l'utilisation du stockage](storage_and_file_management-fr#introduction.md)</b> pour vous assurer qu'assez d'espace et assez de fichiers sont disponibles.
** Sur certaines grappes, le système de fichiers compresse les données automatiquement et indique l'espace disque utilisé par les données compressées. Sur d'autres grappes, l'espace disque utilisé représente la taille apparente des fichiers. Ceci explique pourquoi 1To de données compressées sur une grappe devient 2To de données sur une autre grappe.
** Avant de transférer un ensemble de données, vous pouvez connaître sa taille apparente avec l'option `-b` de la commande `du`.

```bash
du dataset; du -b dataset
```

```
443087696       dataset  # Size of the compressed data
1048576000      dataset  # Apparent size of the data
```

* Vérifiez encore <b>[les permissions des systèmes de fichiers](sharing_data-fr.md)</b> pour vous assurer que vous avez la permission d'écriture à l'endroit où vous transférez les nouveaux fichiers.