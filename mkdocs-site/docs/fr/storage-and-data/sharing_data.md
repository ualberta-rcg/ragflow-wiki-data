---
title: "Sharing data/fr"
slug: "sharing_data"
lang: "fr"

source_wiki_title: "Sharing data/fr"
source_hash: "77ef192582da2b9930c11334a7d6a092"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:30:48.271366+00:00"

tags:
  []

keywords:
  - "répertoire parent"
  - "fichiers et sous-répertoires"
  - "Partage de données"
  - "groupe"
  - "groupe de partage de données"
  - "catégories d'utilisateurs"
  - "permissions"
  - "notation octale"
  - "exécuter"
  - "écrire"
  - "umask"
  - "dépannage"
  - "répertoire"
  - "session"
  - "permission"
  - "Grappes de calcul"
  - "chmod"
  - "permissions d'accès"
  - "liste de contrôle d'accès"
  - "catégorie d'utilisateur"
  - "droit de lecture"
  - "sticky bit"
  - "partage de données"
  - "Sécurité des données"
  - "listes de contrôle d'accès"
  - "création d'un groupe"
  - "Permissions par défaut"
  - "listes de règles d'accès"
  - "ACL"
  - "lire"
  - "fichiers"
  - "systèmes de fichiers"
  - "setfacl"
  - "groupe de partage"
  - "utilisateurs"
  - "setGID"
  - "propriétaire"
  - "groupes"
  - "Permissions des systèmes de fichiers"
  - "système Linux"
  - "listes de contrôle d'accès (ACL)"

questions:
  - "Pourquoi est-il fortement déconseillé d'utiliser la commande chmod -R 777 sur les grappes de calcul ?"
  - "Quelles sont les différentes méthodes recommandées pour partager des données selon le statut de la personne (membre du groupe, utilisateur externe ou autre utilisateur de la grappe) ?"
  - "Comment fonctionnent les catégories d'utilisateurs et les permissions des systèmes de fichiers, et quelles commandes permettent de les consulter ou de les modifier ?"
  - "Comment fonctionne la notation octale pour définir les permissions d'un fichier ou d'un répertoire avec la commande chmod ?"
  - "Quel est le rôle de la protection « sticky bit » dans un répertoire partagé et comment peut-on l'activer ou la désactiver ?"
  - "Quelle est l'utilité d'activer le bit setGID sur un répertoire parent lors de la création de nouveaux fichiers et sous-répertoires ?"
  - "À quoi servent les signes plus (+) et moins (-) lors de la modification des permissions ?"
  - "Quelles sont les différentes natures de permissions qu'il est possible d'attribuer ou de retirer ?"
  - "Que représentent les lettres `u`, `g` et `o` dans la définition des catégories d'utilisateurs ?"
  - "Pourquoi peut-il être utile d'associer automatiquement le groupe de nouveaux fichiers à celui de leur répertoire parent ?"
  - "Quel est l'effet précis de l'activation du bit setGID sur un répertoire ?"
  - "Quels types d'éléments sont affectés par l'héritage du groupe lorsqu'ils sont créés sous un répertoire configuré avec ce bit ?"
  - "Quel est l'effet de l'activation de la permission setGID sur un répertoire parent lors de la création de nouveaux fichiers ou sous-répertoires ?"
  - "Quelle est la différence entre un « s » minuscule et un « S » majuscule dans l'affichage des permissions d'un répertoire ?"
  - "Comment peut-on afficher les permissions par défaut du système de fichiers définies par l'attribut umask ?"
  - "Quel est le rôle de l'attribut umask et comment permet-il de définir les permissions par défaut des nouveaux fichiers ?"
  - "Comment modifier les permissions des fichiers et répertoires existants, et quelles autres conditions influencent leur accessibilité ?"
  - "Dans quel cas est-il nécessaire d'utiliser les listes de contrôle d'accès (ACL) plutôt que les permissions Unix standards pour partager des données ?"
  - "Quel attribut est utilisé pour définir les permissions par défaut des systèmes de fichiers ?"
  - "Comment la valeur par défaut des permissions est-elle attribuée sur les différents systèmes Linux ?"
  - "Quelle commande doit-on lancer pour afficher la valeur des permissions par défaut dans sa session ?"
  - "Quelles sont les trois catégories d'utilisateurs standards qui limitent la gestion des droits d'accès ?"
  - "Quel problème spécifique les listes de règles d'accès (ACL) permettent-elles de résoudre par rapport aux permissions classiques ?"
  - "Que signifie l'acronyme ACL et combien de commandes sont prévues pour les configurer selon le texte ?"
  - "Comment utiliser la commande setfacl pour accorder des permissions à un utilisateur sur un fichier unique ou un sous-répertoire (incluant les données existantes et futures) ?"
  - "Quelles sont les conditions préalables concernant les permissions des répertoires parents et l'utilisation des chemins physiques pour que le partage de fichiers fonctionne correctement ?"
  - "Comment supprimer récursivement les listes de contrôle d'accès d'un répertoire et quelle méthode privilégier pour partager des données plus complexes avec plusieurs collaborateurs ?"
  - "Dans quelles situations spécifiques est-il recommandé de créer un groupe de partage ?"
  - "De qui est exactement composé ce groupe de partage spécial ?"
  - "Quel mécanisme technique est utilisé pour gérer et attribuer les permissions d'accès à ce groupe ?"
  - "Quelles sont les étapes requises pour créer un groupe de partage de données et y ajouter de nouveaux membres ?"
  - "Comment configurer les permissions des répertoires parents et les listes de contrôle d'accès (ACL) pour partager des données avec un groupe ?"
  - "Quelle commande doit-on utiliser pour identifier rapidement les fichiers et sous-répertoires auxquels on n'a pas accès en lecture ?"
  - "Quelles sont les étapes requises pour créer un groupe de partage de données et y ajouter de nouveaux membres ?"
  - "Comment configurer les permissions des répertoires parents et les listes de contrôle d'accès (ACL) pour partager des données avec un groupe ?"
  - "Quelle commande doit-on utiliser pour identifier rapidement les fichiers et sous-répertoires auxquels on n'a pas accès en lecture ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Page enfant de [Gestion du stockage et des fichiers](storage-and-file-management.md)*

!!! warning "Avertissement : Sécurité des données"
    **N'utilisez jamais la commande `chmod -R 777` dans vos répertoires, et surtout pas dans votre répertoire `/home`. Ce serait un ÉNORME risque pour la sécurité de vos données et c'est inacceptable sur des systèmes partagés tels que nos grappes de calcul. De plus, cette commande n'est jamais réellement nécessaire.**

Il arrive fréquemment de devoir partager ses données avec un collègue ou avec un autre groupe de recherche, et nos grappes offrent tous les moyens pour ce faire.

Pour partager des données avec un membre d'un groupe de recherche dont vous faites partie, la meilleure approche est d'utiliser [l'espace /project](project-layout.md) disponible aux membres du groupe. Si vous devez créer un groupe qui utilisera une des grappes nationales, communiquez avec le [soutien technique](technical-support.md), car les utilisateurs ne peuvent pas créer leurs propres groupes.

Pour partager des données avec une personne qui ne détient pas de compte sur la grappe que vous utiliserez, vous pouvez créer un [point de chute commun](globus.md#partage-de-fichiers-avec-globus) dans Globus.

Pour partager des données avec un autre utilisateur qui détient un compte sur la même grappe, mais qui ne fait pas partie du même groupe, le moyen le plus simple est de vous servir des permissions du système de fichiers en question, ce qui est le sujet principal ici.

La personne avec laquelle vous voulez partager vos données doit pouvoir accéder à tous les répertoires à partir des espaces `/scratch` ou `/project`, jusqu'au répertoire qui contient le fichier. Pour avoir accès, par exemple, à un document placé dans un coffre-fort situé dans une pièce de votre appartement, il ne suffit pas de me fournir la combinaison pour ouvrir le coffre-fort; je dois aussi pouvoir entrer dans l'édifice, puis dans votre appartement, puis dans la pièce où se trouve le coffre-fort. Dans le contexte d'un système de fichiers, ceci signifie accorder à l'autre utilisateur une permission d'exécution à tous les répertoires entre le répertoire racine (par exemple `/scratch` ou `/project`) et le répertoire qui contient le fichier en question.

## Permissions des systèmes de fichiers

À l'instar de la plupart des systèmes de fichiers modernes, ceux de nos grappes possèdent des fonctionnalités permettant de lire, écrire et exécuter des fichiers et des répertoires. Quand un utilisateur essaie avec la commande `cd` de lire, modifier ou supprimer un fichier, ou encore d'obtenir l'accès à un répertoire, le noyau Linux (*kernel*) vérifie d'abord les permissions. Si l'action est impossible, un message annonce que la permission n’est pas accordée.
Il existe trois catégories d'utilisateurs pour les objets fichiers ou répertoires d'un système de fichiers :
*   le propriétaire de l'objet, habituellement l'utilisateur ayant créé cet objet
*   les membres du groupe de l'objet, habituellement les mêmes que les membres du groupe par défaut du propriétaire
*   tous les autres

À chacune de ces catégories d'utilisateurs peuvent être associées les permissions de lecture, d'écriture et d'exécution de l'objet. Avec trois catégories d'utilisateurs et trois types de permissions, il y a donc une possibilité de neuf permissions pouvant être associées à chaque objet.

Pour connaître les permissions associées à un objet, utilisez :

```bash
ls -l name_of_object
```

Le résultat en sortie indique les permissions associées au propriétaire, au groupe et aux autres. Par exemple, `rw-r--r--` permet au propriétaire seulement la lecture et l'écriture (*read* et *write*); la lecture est permise aux membres du groupe et à tous les autres utilisateurs. Le résultat montre aussi le nom du propriétaire de l'objet et le groupe.

Pour modifier les permissions associées à un fichier ou à un répertoire, utilisez la commande `chmod` suivie de la catégorie d'utilisateur puis du signe plus (+) ou moins (-) pour soit allouer ou retirer la permission, et enfin, la nature de la permission, soit lire (`r`) pour *read*, écrire (`w`) pour *write* ou exécuter (`x`) pour *execute*. Les catégories d'utilisateur sont `u` (*user*) pour le propriétaire, `g` pour le groupe et `o` (*others*) pour tous les autres utilisateurs de la grappe. Ainsi, la commande :

```bash
chmod g+r file.txt
```

accorde la permission de lecture à tous les membres du groupe auquel appartient le fichier file.txt, alors que la commande :

```bash
chmod o-x script.py
```

retire la permission d'exécuter le fichier script.py à tous, à l'exception du propriétaire et du groupe. On utilise la catégorie d'utilisateur `a` pour signifier tous (*all*); ainsi :

```bash
chmod a+r file.txt
```

indique que tous les utilisateurs de la grappe peuvent lire le fichier file.txt.

Pour ce qui est des permissions sous Unix, plusieurs utilisent la notation octale, même si cette dernière est moins intuitive. Les permissions pour une catégorie d'utilisateur sont représentées par trois bits qui sont interprétés comme un chiffre de 0 à 7 avec la formule (*read_bit*)*4 + (*write_bit*)*2 + (*execute_bit*)*1. Dans notre exemple, la représentation octale serait 4+2+0 = 6 pour le propriétaire et 4+0+0 = 4 pour le groupe et les autres, soit la valeur 644.

Notez que pour avoir vos permissions reliées à un fichier, vous devez avoir accès au répertoire qui contient ce fichier; vous devrez donc avoir les permissions en lecture et en exécution (5 et 7 en notation octale) pour ce répertoire.

Pour modifier les permissions, utilisez la commande `chmod` avec la notation octale mentionnée plus haut; par exemple :

```bash
chmod 770 name_of_file
```

accorde à tous les utilisateurs de votre groupe les permissions d'écriture, de lecture et d'exécution. Bien entendu, vous pouvez seulement modifier les permissions associées à un fichier ou à un répertoire dont vous êtes propriétaire. Pour modifier le groupe, utilisez la commande `chgrp`.

### Protection *sticky bit*

Comme c'est souvent le cas lorsqu'un professeur travaille avec plusieurs étudiants et collaborateurs, [l'espace /project](project-layout.md) se trouve dans un répertoire partagé par plusieurs utilisateurs qui ont des permissions de lecture, d'écriture ou d'exécution : il faut donc s'assurer que les fichiers et les répertoires ne puissent être supprimés par un autre utilisateur que leur propriétaire. Le système de fichiers sous Unix comporte la fonctionnalité [sticky bit](https://en.wikipedia.org/wiki/Sticky_bit) qui empêche qu'un fichier soit supprimé ou renommé par un autre utilisateur que le propriétaire du fichier ou du répertoire. Sans ce *sticky bit*, les utilisateurs qui ont des permissions de lecture et d'écriture pour un répertoire peuvent renommer ou supprimer tous les fichiers du répertoire, même s'ils n'en sont pas les propriétaires.
Pour positionner les permissions `rwxrwxr--` et le *sticky bit* sur un répertoire, utilisez la commande `chmod` ainsi :

```bash
chmod +t <directory name>
```

ou en notation octale avec le mode 1000, ainsi :

```bash
chmod 1774 <directory name>
```

Dans `ls -l`, le *sticky bit* est représenté par la lettre t (ou T), à la fin du champ des permissions, comme suit :

```
$ ls -ld directory
drwxrws--T 2 someuser def-someuser 4096 Sep 25 11:25 directory
```

Il est désactivé par la commande :

```bash
chmod -t <directory name>
```

ou en octal :

```bash
chmod 0774 <directory name>
```

Pour l'espace projet, le propriétaire du répertoire est le chercheur principal qui parraine les étudiants et les collaborateurs.

### Bit pour l'ID du groupe

Lorsque des fichiers et des répertoires sont créés dans un répertoire parent, il est très utile dans certains cas de pouvoir associer automatiquement le propriétaire ou le groupe de ces nouveaux fichiers et répertoires au répertoire parent ou au groupe auquel ils sont reliés.

Si le bit `setGID` est activé pour un répertoire, les nouveaux fichiers et sous-répertoires créés sous celui-ci héritent du propriétaire du groupe auquel le répertoire est associé. Voyons un exemple.

Vérifiez d'abord quels sont les groupes auxquels `someuser` appartient avec la commande :

```console
[someuser@server]$ groups
someuser def-someuser
```

`someuser` appartient à deux groupes : `someuser` et `def-someuser`. Dans le répertoire actif, il y a un répertoire qui appartient au groupe `def-someuser`.

```console
[someuser@server]$ ls -l
drwxrwx---  2 someuser   def-someuser       4096 Oct 13 19:39 testDir
```

Si nous créons un fichier dans ce répertoire, nous voyons qu'il appartient à `someuser`, groupe par défaut de `someuser`.

```console
[someuser@server]$ touch dirTest/test01.txt
[someuser@server]$ ls -l dirTest/
-rw-rw-r-- 1 someuser   someuser    0 Oct 13 19:38 test01.txt
```

Nous ne voulons probablement pas nous trouver dans `/project`, mais nous voulons qu'un fichier nouvellement créé possède le même groupe que celui du répertoire parent. Activez la permission `setGID` du répertoire parent ainsi :

```console
[someuser@server]$ chmod g+s dirTest
[someuser@server]$ ls -l
drwxrws---  2 someuser   def-someuser       4096 Oct 13 19:39 dirTest
```

Remarquez que la permission `x` des permissions du groupe est maintenant `s`; les nouveaux fichiers créés dans `dirTest` seront associés au même groupe que le répertoire parent.

```console
[someuser@server]$ touch dirTest/test02.txt
[someuser@server]$ ls -l dirTest
-rw-rw-r-- 1 someuser   someuser      0 Oct 13 19:38 test01.txt
-rw-rw-r-- 1 someuser   def-someuser  0 Oct 13 19:39 test02.txt
```

Si nous créons un répertoire sous un répertoire où `setGID` est activé, ce nouveau répertoire sera associé au même groupe que le répertoire parent et `setGID` sera aussi activé.

```console
[someuser@server]$ mkdir dirTest/dirChild
[someuser@server]$ ls -l dirTest/
-rw-rw-r-- 1 someuser   someuser      0 Oct 13 19:38 test01.txt
-rw-rw-r-- 1 someuser   def-someuser  0 Oct 13 19:39 test02.txt
drwxrwsr-x 1 someuser   def-someuser  0 Oct 13 19:39 dirChild
```

Il peut être important de distinguer entre `S` (majuscule) et `s`. Le S majuscule indique que les permissions d'exécution ont été retirées du répertoire, mais que `setGID` est toujours activé. Il est facile de confondre les deux formes, ce qui peut créer des problèmes de permission inattendus, par exemple l'impossibilité pour les autres membres du groupe d'accéder à des fichiers de votre répertoire.

```console
[someuser@server]$ chmod g-x dirTest/
[someuser@server]$ ls -l
drwxrS---  3 someuser   def-someuser       4096 Oct 13 19:39 dirTest
```

### Bit pour l'ID de l'utilisateur

!!! warning "Attention"
    Le bit `setUID` **ne fonctionne pas** sur nos grappes. Il est désactivé pour des raisons de sécurité.

## Permissions par défaut des systèmes de fichiers

Les permissions par défaut sont définies par l'attribut [umask](https://fr.wikipedia.org/wiki/Umask). Une valeur par défaut est définie pour chaque système Linux. Pour faire afficher cette valeur dans votre session, lancez :

```bash
umask -S
```

Par exemple, le résultat sur nos grappes serait :

```console
[user@gra-login1]$ umask -S
u=rwx,g=rx,o=
```

Ceci signifie que par défaut, les nouveaux fichiers que vous créez peuvent être lus, modifiés et exécutés par vous-même; ils peuvent être lus et exécutés par les membres du groupe du fichier; les autres utilisateurs n'y ont pas accès.

!!! warning "Important"
    L'attribut `umask` ne s'applique qu'aux nouveaux fichiers; le fait de changer `umask` ne change pas les permissions d'accès aux fichiers existants.

Vous pourriez vouloir définir des permissions moins restrictives (par exemple pour permettre à d'autres utilisateurs de lire et exécuter les fichiers) ou plus restrictives (par exemple pour empêcher votre groupe de lire ou exécuter les fichiers). Vous pouvez définir votre attribut `umask` dans une session ou encore dans votre fichier `.bashrc` avec la commande :

```bash
umask <value>
```

où `<value>` est une valeur octale. Le tableau suivant montre des options utiles de `umask`.

| Valeur | Permissions   | Effet                                                                               |
| :----- | :------------ | :---------------------------------------------------------------------------------- |
| 077    | u=rwx,g=,o=   | Les fichiers peuvent être lus, modifiés et exécutés par le propriétaire seulement.  |
| 027    | u=rwx,g=rx,o= | Les fichiers peuvent être lus et exécutés par le propriétaire et par le groupe, mais peuvent être modifiés par le propriétaire seulement. |
| 007    | u=rwx,g=rwx,o=| Les fichiers peuvent être lus, modifiés et exécutés par le propriétaire et par le groupe. |
| 022    | u=rwx,g=rx,o=rx | Les fichiers peuvent être lus et exécutés par tous, mais peuvent être modifiés par le propriétaire seulement. |
| 002    | u=rwx,g=rwx,o=rx | Les fichiers peuvent être lus et exécutés par tous, mais peuvent être modifiés par le propriétaire et par le groupe. |

D'autres conditions déterminent l'accès aux fichiers.
*   L'utilisateur qui veut avoir accès à un fichier doit avoir la permission d'exécution pour tous les répertoires dans le chemin de ce fichier. Par exemple, un fichier pourrait avoir les permissions `o=rx`, mais un utilisateur régulier ne pourra le lire ni l'exécuter si le répertoire parent n'a pas aussi la permission `o=x`.
*   L'utilisateur qui veut avoir accès à un fichier ayant des permissions de groupe doit être membre du groupe du fichier.
*   Les permissions d'un fichier ou d'un répertoire peuvent être modifiées après leur création avec `chmod`.
*   L'accès aux fichiers est aussi déterminé par les listes de contrôle d'accès (ACL pour *Access Control List*).

Vos fichiers n'étaient pas plus à risque avant cette modification. Depuis le début, les permissions d'accès sont restrictives pour vos répertoires /home, /project et /scratch; ils ne peuvent être accédés par les autres utilisateurs à moins que vous leur ayez accordé le droit d'exécuter.

### Changer les permissions de fichiers existants

Pour que les permissions soient les mêmes que les nouvelles permissions par défaut, vous pouvez utiliser `chmod` comme suit :

```bash
chmod g-w,o-rx <file>
```

Pour le répertoire au complet, utilisez :

```bash
chmod -R g-w,o-rx <directory>
```

## Listes de contrôle d'accès

### Partage de données avec un autre utilisateur

Les systèmes d'exploitation de type Unix fonctionnent avec ces permissions depuis plusieurs années, mais les possibilités sont limitées. Comme il n'y a que trois catégories d'utilisateurs (propriétaire, groupe, autres), comment permettre la lecture à un utilisateur en particulier qui n'appartient pas à un groupe? Faut-il alors permettre à tous de lire le fichier? Heureusement, la réponse est non, puisque dans de tels cas, nos systèmes nationaux offrent des listes de règles d'accès (ACL pour *access control lists*) par utilisateur. Les deux commandes pour ce faire sont :
*   `getfacl` pour connaître les permissions définies dans la liste,
*   `setfacl` pour modifier ces permissions.

#### Partage d'un seul fichier

Par exemple, pour accorder à l'utilisateur `smithj` la permission de lire et exécuter le fichier `my_script.py`, la commande serait :

```console
$ setfacl -m u:smithj:rx my_script.py
```

#### Partage d'un sous-répertoire

Pour accorder un accès en lecture et écriture à un seul utilisateur dans un sous-répertoire, incluant les nouveaux fichiers qui y seront créés, utilisez les commandes suivantes :

```console
$ setfacl -d -m u:smithj:rwX /home/<user>/projects/def-<PI>/shared_data
$ setfacl -R -m u:smithj:rwX /home/<user>/projects/def-<PI>/shared_data
```

!!! note "Note"
    L'attribut X (majuscule) donne la permission *execute* seulement quand le répertoire ou le fichier possède déjà la permission d'exécution. Pour pouvoir être vu, un répertoire doit avoir la permission d'exécution.

La première commande détermine les règles d'accès au répertoire `/home/<user>/projects/def-<PI>/shared_data`; tous les fichiers et répertoires qui y seront créés hériteront de la même règle ACL. Elle est nécessaire pour les **nouvelles** données. La deuxième commande détermine les règles ACL pour le répertoire `/home/<user>/projects/def-<PI>/shared_data` et tout le contenu actuel. Elle ne s'applique qu'aux données **existantes**.

Pour que cette méthode fonctionne, il faut :
*   que vous soyez propriétaire du répertoire, `/home/smithj/projects/def-smithj/shared_data` dans notre exemple;
*   que les répertoires parents (et parents des parents, etc.) de celui que vous voulez partager accordent la permission d'exécuter à l'utilisateur avec qui vous voulez le partager. Dans notre exemple, vous pourriez utiliser `setfacl -m u:smithj:X ...` ou encore accorder la permission à tous les utilisateurs avec `chmod o+x ...`. Il n'est pas nécessaire d'accorder une permission de lecture publique. En particulier, vous devrez accorder une permission d'exécuter pour le répertoire (`/projects/def-<PI>`) soit à tous les utilisateurs, soit à chaque utilisateur (un à la fois) avec qui vous voulez partager vos données.
*   pour partager un répertoire du système de fichiers /project, donnez à vos collaborateurs un chemin qui commence par `/project` **et non** `/home/<user>/projects`. Ce dernier chemin contient des liens symboliques (simlinks ou raccourcis) vers les répertoires physiques de /project et le répertoire à trouver ne pourra pas être rejoint par d'autres qui n'auraient pas accès à votre répertoire /home. La commande `realpath` vous permet d'obtenir le chemin physique auquel pointe le simlink. Par exemple, `realpath /home/smithj/projects/def-smithj/shared_data` pourrait retourner `/project/9041430/shared_data`. Le chemin physique vers un répertoire /project n'est pas le même pour toutes nos grappes; si votre répertoire /project doit être partagé sur plus d'une grappe, vérifiez le chemin physique sur chacune avec `realpath`.

#### Supprimer les listes de contrôle d'accès

Pour supprimer récursivement tous les attributs dans un répertoire, utilisez :

```console
setfacl -bR /home/<user>/projects/def-<PI>/shared_data
```

### Partage de données avec un groupe

Dans les cas de partage de données plus complexes (avec plusieurs utilisateurs sur plusieurs grappes), il est possible de créer un **groupe de partage**. Il s'agit d'un groupe spécial composé des utilisateurs avec lesquels les données doivent être partagées. Le groupe obtient ses permissions d'accès via des listes de contrôle d'accès (ACL).

Vous aurez besoin d'un groupe dans des cas particuliers de partage de données.

#### Création d'un groupe de partage de données

La procédure suivante décrit la création du groupe `wg-datasharing`.

1.  Écrivez au [soutien technique](technical-support.md) pour demander la création du groupe; indiquez le nom du groupe et dites que vous en êtes le propriétaire.
2.  Quand vous recevez la confirmation de la création du groupe, allez à [ccdb.computecanada.ca/services/](https://ccdb.computecanada.ca/services/).
3.  Cliquez sur le nom du groupe en question pour faire afficher les détails de ce groupe.
4.  Ajoutez un membre (par exemple, Victor Van Doom avec son identifiant CCI vdv-888).

#### Utilisation d'un groupe de partage de données

Comme pour le partage avec un seul utilisateur, les répertoires parents des données que vous voulez partager doivent avoir la permission d'exécuter, soit pour tous, soit pour le groupe avec lequel vous voulez les partager. Ceci signifie que dans le répertoire /project, le chercheur principal doit consentir comme suit (à moins que vous n'ayez la permission de faire ceci vous-même) :

```bash
$ chmod  o+X /project/def-<PI>/
```

ou

```bash
$ setfacl -m g:wg_datasharing:X /project/def-<PI>/
```

Enfin, vous pouvez ajouter votre groupe à la liste de contrôle d'accès (ACL) pour le répertoire que vous voulez partager. Les commandes sont les mêmes que celles pour le partage avec un utilisateur :

```console
$ setfacl -d -m g:wg-datasharing:rwx /home/<user>/projects/def-<PI>/shared_data
$ setfacl -R -m g:wg-datasharing:rwx /home/<user>/projects/def-<PI>/shared_data
```

## Dépannage

### Vérification de votre droit de lecture

Pour connaître les fichiers et les sous-répertoires auxquels **vous **n'avez pas** droit de lecture**, utilisez la commande :

```bash
find <directory_name> ! -readable -ls