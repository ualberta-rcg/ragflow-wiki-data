---
title: "A tutorial on 'tar'/fr"
slug: "a_tutorial_on__tar"
lang: "fr"

source_wiki_title: "A tutorial on 'tar'/fr"
source_hash: "5772acf6043103271051d74fea8b4a47"
last_synced: "2026-04-10T14:10:18.226633+00:00"
last_processed: "2026-04-10T14:30:51.649339+00:00"

tags:
  []

keywords:
  - "report.tar"
  - "option --exclude"
  - "Res-01"
  - "plusieurs fichiers"
  - "suffixe .dat"
  - "fichier archive compressé"
  - "option -r"
  - "ajouter des fichiers"
  - "archive existante"
  - "bzip2"
  - "fractionner des fichiers"
  - "lister"
  - "tar.bz2"
  - "décompression"
  - "new_results"
  - "gunzip"
  - "extension"
  - "localhost"
  - "options"
  - "chaîne de caractères"
  - "trait vertical"
  - "archive compressée"
  - "Extraire"
  - "commande tar"
  - "fichier archive"
  - "bunzip2"
  - "exclure les fichiers"
  - "exécuter tar"
  - "results.tar"
  - "extraction"
  - "archive"
  - "ajouter une archive"
  - "archive results.tar"
  - "caractères génériques"
  - "log1.dat"
  - "compresser"
  - "enregistrer les résultats"
  - "tar.gz"
  - "gz"
  - "concaténer"
  - "commande grep"
  - "exclure des fichiers"
  - "tar"
  - "commande"
  - "Combiner deux archives"
  - "lister le contenu"
  - "fichier compressé"
  - "fichiers archive"
  - "compression"
  - "chemin"
  - "répertoire de destination"
  - "extraire des fichiers"
  - "décompresser"
  - "console"
  - "fichier tar"
  - "results.tar.bz2"
  - "archivage"
  - "combiner deux archives"
  - "option -A"
  - "extraire un fichier"
  - "results.tar.gz"
  - "commandes"
  - "gzip"
  - "extraire"
  - "fichiers"
  - "taille des fichiers"
  - "archives compressées"
  - "répertoires"
  - "grep"
  - "répertoire"

questions:
  - "Comment utiliser la commande tar pour créer un fichier archive à partir d'un répertoire et comment en extraire les fichiers ?"
  - "Quelles sont les différences de performance et d'utilisation entre les méthodes de compression xz et gzip ?"
  - "Quelles sont les options principales de la commande tar pour lister, créer ou manipuler des archives ?"
  - "Quelle option doit-on utiliser pour indiquer le nom du fichier archive à manipuler ?"
  - "Quels paramètres permettent d'extraire les données d'une archive ou d'en lister le contenu ?"
  - "Comment peut-on spécifier l'algorithme de compression, tel que xz ou gzip, à appliquer sur l'archive ?"
  - "Comment peut-on combiner les options de la forme simple de la commande tar et comment obtenir la liste complète des options disponibles ?"
  - "Quelles options de la commande tar doit-on utiliser pour créer une archive d'un ou plusieurs répertoires tout en affichant les détails des fichiers ajoutés ?"
  - "Comment est-il possible d'archiver un ensemble de fichiers ou de répertoires en utilisant une chaîne de caractères ou un motif spécifique, comme ceux commençant par une lettre particulière ?"
  - "Quelle action spécifique est accomplie par la commande utilisant l'argument `r*` dans l'exemple donné ?"
  - "Comment est-il possible de regrouper des fichiers ou des répertoires en se basant sur une chaîne de caractères ?"
  - "Quels exemples de motifs de recherche sont fournis pour illustrer la sélection personnalisée d'éléments à archiver ?"
  - "Quelle option de la commande tar permet d'ajouter des fichiers ou des répertoires à une archive existante ?"
  - "Quelle est la restriction importante concernant le format de l'archive lors de l'ajout de nouveaux éléments ?"
  - "Quelle option doit-on utiliser pour combiner deux archives en ajoutant le contenu de l'une à l'autre ?"
  - "Comment utiliser la commande tar pour ajouter le contenu d'une archive à une autre ?"
  - "Quelle est la différence principale entre les options -r et -A lors de l'ajout d'une archive existante ?"
  - "Comment peut-on exclure un type spécifique de fichiers lors de la création d'une archive avec tar ?"
  - "Quelle option de commande permet d'ajouter une archive à une autre archive existante ?"
  - "Comment le texte illustre-t-il la combinaison de l'archive « report.tar » avec l'archive « results.tar » ?"
  - "Dans quelle situation est-il mentionné qu'il n'est pas nécessaire de voir les détails des fichiers ?"
  - "Quel est l'objectif principal de la commande présentée dans cet exemple ?"
  - "Quel est le rôle spécifique de l'option `--exclude=*.dat` lors de la création de l'archive ?"
  - "Quels répertoires et fichiers sont listés dans la console avant l'exécution de la commande d'archivage ?"
  - "Comment préserver les liens symboliques lors de la création d'une archive avec la commande tar ?"
  - "Quelle est la différence fondamentale entre le processus d'archivage et le processus de compression ?"
  - "Quelles options faut-il utiliser avec la commande tar pour archiver et compresser simultanément des fichiers avec gzip ou bzip2 ?"
  - "Comment procéder pour ajouter de nouveaux fichiers à une archive déjà compressée ?"
  - "Quelles options de la commande tar doit-on utiliser pour extraire une archive vers un répertoire de destination spécifique ?"
  - "Quelles commandes et options permettent de décompresser et d'extraire directement des archives aux formats .gz et .bz2 ?"
  - "Quelle commande permet de créer l'archive compressée \"results.tar.bz2\" dans l'exemple donné ?"
  - "Quels éléments sont listés dans le répertoire courant lors de l'exécution de la commande \"ls\" ?"
  - "Quelle opération spécifique sur les archives compressées (tar.gz/tar.bz2) est annoncée par le titre à la fin du texte ?"
  - "Quel est l'objectif principal des commandes présentées dans ce texte ?"
  - "Quelle est la différence entre les commandes `tar -xvzf` et `tar -xzf` illustrées dans l'exemple ?"
  - "À quoi sert l'option `-C` suivie d'un nom de répertoire lors de l'extraction de l'archive ?"
  - "Comment utiliser l'option \"-C\" lors de l'extraction d'une archive et quelle précaution faut-il prendre concernant le répertoire de destination ?"
  - "Quel est le rôle de l'option \"v\" dans la commande tar et comment faire pour afficher davantage de détails lors de l'extraction ?"
  - "Comment peut-on extraire un fichier archive compressé en deux étapes distinctes sans utiliser les options \"z\" ou \"j\" ?"
  - "Comment extraire un fichier spécifique d'une archive tar vers un répertoire de destination particulier sans décompresser toute l'archive ?"
  - "Quelles options spécifiques doivent être utilisées avec la commande tar pour extraire un fichier depuis une archive compressée au format .gz ou .bz2 ?"
  - "Comment utiliser les caractères génériques (wildcards) pour extraire simultanément plusieurs fichiers répondant à un critère précis, comme une extension particulière ?"
  - "What is the purpose of the `gunzip` command executed at the beginning of the terminal session?"
  - "How does the `-C ./new_results/` flag modify the behavior of the `tar` extraction command?"
  - "What specific files and directories are shown being extracted from the archive in the verbose output?"
  - "Comment extraire des fichiers situés dans un répertoire précis et possédant une extension particulière ?"
  - "À quoi servent les options \"j\" et \"z\" mentionnées pour la manipulation des archives ?"
  - "Comment procéder pour extraire tous les fichiers dont le nom commence par un préfixe spécifique ?"
  - "Comment peut-on lister le contenu et les métadonnées d'un fichier d'archive tar sans le décompresser ?"
  - "Quelle méthode permet de compter le nombre total d'entrées (fichiers et répertoires) présentes dans une archive tar ?"
  - "Comment peut-on rechercher un fichier spécifique à l'intérieur d'une archive tar en utilisant la ligne de commande ?"
  - "Quel est le rôle du trait vertical et de la commande grep lorsqu'ils sont associés à la commande tar ?"
  - "Quelle différence y a-t-il entre les résultats des commandes \"tar -tf\" et \"tar -tvf\" illustrées dans l'exemple ?"
  - "Comment formuler la commande exacte pour rechercher les informations détaillées d'un fichier spécifique à l'intérieur d'une archive ?"
  - "Comment utiliser la commande tar combinée à grep pour rechercher un fichier spécifique ou un motif de nom de fichier dans une archive ?"
  - "Quelle option permet d'afficher les détails supplémentaires (comme les permissions, la taille et la date) des fichiers listés dans une archive ?"
  - "Quelles sont les options spécifiques à ajouter à la commande tar pour lister directement le contenu des archives compressées avec gzip (.gz) ou bzip2 (.bz2) sans les décompresser ?"
  - "Comment peut-on vérifier la taille des fichiers, répertoires et archives à partir du terminal ?"
  - "Quelle est la procédure pour diviser un gros fichier en plusieurs petites parties et comment le reconstituer par la suite ?"
  - "Pourquoi est-il important de vérifier l'espace disque disponible avant d'utiliser des commandes de compression comme gzip, bzip2 ou tar ?"
  - "What is the purpose of the `tar -tvjf` command executed in the provided terminal snippet?"
  - "What specific files and directories are contained within the `results.tar.bz2` archive?"
  - "What are the file sizes and modification dates of the log files listed in the output?"
  - "Comment utiliser la commande tar pour rassembler plusieurs fichiers et répertoires dans une seule archive ?"
  - "Comment cibler uniquement les fichiers ou répertoires commençant par une lettre ou une chaîne de caractères spécifique lors de l'exécution de tar ?"
  - "Quelle est la syntaxe exacte illustrée pour créer une archive nommée \"your_archive.tar\" à partir d'une liste définie de dossiers et de fichiers ?"
  - "Comment peut-on explorer le contenu d'une archive tar (lister, compter ou rechercher des fichiers) sans avoir à la décompresser ?"
  - "Comment ajouter de nouveaux fichiers à une archive existante et quelle est la restriction majeure concernant les archives compressées ?"
  - "Quelles sont les options permettant d'extraire une archive dans un répertoire spécifique et de créer une archive compressée tout en excluant certains fichiers ?"
  - "Comment créer une archive compressée au format .tgz ou .tbz à l'aide de la commande tar ?"
  - "Quelle est la méthode pour exclure des fichiers spécifiques lors de la création d'une archive tar ?"
  - "Quel outil doit-on utiliser pour décompresser un fichier portant l'extension .gz ?"
  - "Comment lister le contenu d'une archive compressée sans procéder à son extraction ?"
  - "Quelles sont les commandes permettant d'extraire une archive compressée vers un répertoire de destination spécifique ?"
  - "Comment diviser un fichier d'archive volumineux en plusieurs parties et le reconstituer par la suite ?"
  - "Comment lister le contenu d'une archive compressée sans procéder à son extraction ?"
  - "Quelles sont les commandes permettant d'extraire une archive compressée vers un répertoire de destination spécifique ?"
  - "Comment diviser un fichier d'archive volumineux en plusieurs parties et le reconstituer par la suite ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Page enfant de [Archivage et compression de fichiers](archivage-et-compression-de-fichiers.md)*

## Archiver des fichiers et des répertoires

La commande [tar](https://www.gnu.org/software/tar/manual/tar.html) est l'utilitaire d'archivage principal sous Linux et autres systèmes de type Unix. Cette commande rassemble plusieurs fichiers ou répertoires et génère un *fichier archive* (aussi nommé *fichier tar* ou *tarball*). Par convention, un fichier archive possède le suffixe `.tar`. Le fichier archive d'un répertoire contient par défaut tous les fichiers et sous-répertoires avec leurs sous-répertoires, sous-sous-répertoires, et ainsi de suite. Par exemple, la commande `tar --create --file project1.tar project1` rassemble le contenu du répertoire *project1* dans le fichier *project1.tar*; le fichier d'origine est conservé, ce qui peut doubler l'espace disque utilisé.

Pour extraire des fichiers du fichier archive, utilisez la commande avec une option différente, soit `tar --extract --file project1.tar`. S'il n'existe pas de répertoire portant le nom d'origine, il sera créé. S'il existe un répertoire portant le nom d'origine et qu'il contient des fichiers du même nom que ceux du fichier archive, ces derniers seront remplacés. Il existe aussi une option pour spécifier le répertoire de destination pour le contenu extrait du fichier archive.

## Compression et décompression

L'utilitaire `tar` peut compresser un fichier archive en même temps que ce fichier est créé. Parmi les méthodes de compression, nous recommandons `xz` ou `gzip` qui s'utilisent comme suit :

```bash
[user_name@localhost]$ tar --create --xz --file project1.tar.xz project1
[user_name@localhost]$ tar --extract --xz --file project1.tar.xz
[user_name@localhost]$ tar --create --gzip --file project1.tar.gz project1
[user_name@localhost]$ tar --extract --gzip --file project1.tar.gz
```

De façon générale, `--xz` produit un fichier compressé plus petit (c'est-à-dire avec un meilleur taux de compression), mais utilise plus de mémoire vive (RAM) (voir [ce lien](http://catchchallenger.first-world.info/wiki/Quick_Benchmark:_Gzip_vs_Bzip2_vs_LZMA_vs_XZ_vs_LZ4_vs_LZO)).
`--gzip` ne compresse pas autant, mais vous pouvez l'utiliser si vous avez des problèmes de manque de mémoire ou de durée d'exécution avec `tar --create`.

Vous pouvez aussi exécuter `tar --create` d'abord sans compression et utiliser ensuite la commande `xz` ou `gzip` dans une étape distincte, mais il est rarement utile de procéder ainsi. De même, vous pouvez exécuter `xz -d` ou `gzip -d` pour décompresser un fichier archive avant d'exécuter `tar --extract`, mais ceci est aussi rarement utile.

Une fois que le fichier tar est créé, il est aussi possible d'utiliser `gzip` ou `bzip2` pour compresser l'archive et diminuer sa taille :

```bash
[user_name@localhost]$ gzip project1.tar
[user_name@localhost]$ bzip2 project1.tar
```

Ces commandes produisent les fichiers *project1.tar.gz* et *project1.tar.bz2*.

## Options fréquemment employées

Il y a deux formes pour chaque option.

*   `-c` ou `--create` pour créer une nouvelle archive
*   `-f` ou `--file=` précède le nom du fichier archive
*   `-x` ou `--extract` pour extraire des fichiers d'une archive
*   `-t` ou `--list` pour lister le contenu d'un fichier archive
*   `-J` ou `--xz` pour compresser ou décompresser avec `xz`
*   `-z` ou `--gzip` pour compresser ou décompresser avec `gzip`

Les options de la forme simple peuvent être combinées en les faisant précéder d'un seul tiret; par exemple `tar -cJf project1.tar.xz project1` équivaut à `tar --create --xz --file=project1.tar.xz project1`.

Plusieurs autres options sont disponibles, selon la version que vous utilisez. Pour obtenir la liste de toutes les options dont vous disposez, exécutez `man tar` ou `tar --help`. Notez que certaines versions moins récentes peuvent ne pas prendre en charge la compression avec `--xz`.

## Exemples

Dans les exemples qui suivent, nous supposons un répertoire qui contient les sous-répertoires et fichiers (*bin/*, *documents/*, *jobs/*, *new.log.dat*, *programs/*, *report/*, *results/*, *tests/*, *work/*). Comparez ces exemples avec le contenu de votre propre répertoire.

### Archivage

#### Répertoires particuliers

On utilise `tar` le plus fréquemment pour créer une archive d'un répertoire. Dans cet exemple, nous créons le fichier archive *results.tar* avec le répertoire *results*.

```bash
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat  programs/  report/  results/  tests/  work/
[user_name@localhost]$ tar -cvf results.tar results
results/
results/log1.dat
results/Res-01/
results/Res-01/log.15Feb16.1
results/Res-01/log.15Feb16.4
results/Res-02/
results/Res-02/log.15Feb16.balance.b.4
```

Avec la commande `ls`, nous voyons le nouveau fichier tar :

```bash
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat  programs/  report/  results/  results.tar  tests/  work/
```

Nous avons utilisé la commande `tar` avec les options **-c** (pour *create*), **-v** (pour *verbosity*) et **-f** (pour *file*). Nous avons nommé l'archive *results.tar*; le nom pourrait être différent, mais il est préférable qu'il soit semblable à celui du répertoire pour que vous puissiez plus facilement le reconnaître.

Vous pouvez placer plusieurs répertoires ou fichiers dans un fichier tar; par exemple, pour placer les répertoires *results*, *report* et *documents* dans le fichier archive *full_results.tar*, nous utilisons :

```bash
[user_name@localhost]$ tar -cvf full_results.tar results report documents/
results/
results/log1.dat
results/Res-01/
results/Res-01/log.15Feb16.1
results/Res-01/log.15Feb16.4
results/Res-02/
results/Res-02/log.15Feb16.balance.b.4
report/
report/report-2016.pdf
report/report-a.pdf
documents/
documents/1504.pdf
documents/ff.doc
```

L'option **v** permet d'afficher les fichiers qui ont été ajoutés; pour les masquer, omettez cette option.

Pour vérifier l'archive créée, utilisez `ls` :

```bash
[user_name@localhost]$ ls
bin/  documents/  full_results.tar  jobs/  new.log.dat  programs/  report/  results/  results.tar  tests/  work/
```

#### Fichiers et répertoires dont le nom commence par une lettre en particulier

Dans notre répertoire de travail se trouvent deux répertoires qui commencent par la lettre **r** (*reports* et *results*). Dans cet exemple, nous rassemblons le contenu de ces répertoires dans une seule archive (*archive.tar*).

```bash
[user_name@localhost]$ tar -cvf archive.tar r*
report/
report/report-2016.pdf
report/report-a.pdf
results/
results/log1.dat
results/Res-01/
results/Res-01/log.15Feb16.1
results/Res-01/log.15Feb16.4
results/Res-02/
results/Res-02/log.15Feb16.balance.b.4
```

Ici nous avons rassemblé tous les répertoires qui commencent par la lettre **r**. Il est aussi possible de rassembler des fichiers ou des répertoires avec une chaîne de caractères, par exemple `*r*`, `*.dat`, etc.

#### Ajouter (*append*) des fichiers à la fin d'une archive

L'option **-r** est utilisée pour ajouter des fichiers à une archive existante sans avoir à en créer une nouvelle ou à décompresser l'archive puis exécuter `tar` à nouveau pour créer une nouvelle archive. Dans le prochain exemple, nous ajoutons le fichier *new.log.dat* à l'archive *results.tar*.

```bash
[user_name@localhost]$ tar -rf results.tar new.log.dat
```

La commande `tar` a ajouté le fichier *new.log.dat* à la fin de l'archive *results.tar*.

Pour vérifier, utilisez les options précédentes pour lister les fichiers du fichier tar :

```bash
[user_name@localhost]$ tar -tvf results.tar
drwxrwxr-x name name        0 2016-11-20 11:02 results/
-rw-r--r-- name name    10905 2016-11-16 16:31 results/log1.dat
drwxrwxr-x name name        0 2016-11-16 19:36 results/Res-01/
-rw-r--r-- name name    11672 2016-11-16 15:10 results/Res-01/log.15Feb16.1
-rw-r--r-- name name    11682 2016-11-16 15:10 results/Res-01/log.15Feb16.4
drwxrwxr-x name name        0 2016-11-16 19:37 results/Res-02/
-rw-r--r-- name name    34117 2016-11-16 15:10 results/Res-02/log.15Feb16.balance.b.4
-rw-r--r-- name name    10905 2016-11-20 11:16 new.log.dat
```

!!! note "Note"
    Il n'est pas possible d'ajouter des fichiers à une archive compressée (*.gz ou *.bz2). Les fichiers peuvent être ajoutés uniquement à une archive tar ordinaire. L'option **-r** est aussi utilisée avec la commande `tar` pour ajouter un ou plusieurs répertoires à un fichier tar existant.

Nous allons maintenant ajouter le répertoire *report* à l'archive *results.tar* de l'exemple précédent :

```bash
[user_name@localhost]$ tar -rf results.tar report/
```

Voyons maintenant le fichier tar créé :

```bash
[user_name@localhost]$ tar -tvf results.tar
drwxrwxr-x name name        0 2016-11-20 11:02 results/
-rw-r--r-- name name    10905 2016-11-16 16:31 results/log1.dat
drwxrwxr-x name name        0 2016-11-16 19:36 results/Res-01/
-rw-r--r-- name name    11672 2016-11-16 15:10 results/Res-01/log.15Feb16.1
-rw-r--r-- name name    11682 2016-11-16 15:10 results/Res-01/log.15Feb16.4
drwxrwxr-x name name        0 2016-11-16 19:37 results/Res-02/
-rw-r--r-- name name    34117 2016-11-16 15:10 results/Res-02/log.15Feb16.balance.b.4
-rw-r--r-- name name    10905 2016-11-20 11:16 new.log.dat
drwxrwxr-x name name        0 2016-11-20 11:02 report/
-rw-r--r-- name name   924729 2015-11-20 04:14 report/report-2016.pdf
-rw-r--r-- name name   924729 2015-11-20 04:14 report/report-a.pdf
```

Rappelez-vous que l'option **-v** n'est pas nécessaire si vous n'avez pas besoin d'afficher les détails des fichiers.

#### Combiner deux archives

Comme on peut ajouter un fichier à une archive, on peut aussi ajouter une archive à une autre archive avec l'option **-A**. Ajoutons l'archive *report.tar* (pour le rapport du répertoire) à l'archive *results.tar* existante :

Pour vérifier l'archive existante :

```bash
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat  programs/  report/  report.tar  results/  results.tar  tests/  work/
[user_name@localhost]$ tar -tvf results.tar
drwxr-xr-x name name        0 2016-11-20 16:16 results/
-rw-r--r-- name name    10905 2016-11-20 16:16 results/log1.dat
drwxr-xr-x name name        0 2016-11-20 16:16 results/Res-01/
-rw-r--r-- name name    11682 2016-11-20 16:16 results/Res-01/log.15Feb16.4
drwxr-xr-x name name        0 2016-11-20 16:16 results/Res-02/
-rw-r--r-- name name    34117 2016-11-20 16:16 results/Res-02/log.15Feb16.balance.b.4
```

Ajoutons maintenant l'archive et vérifions la nouvelle archive :

```bash
[user_name@localhost]$ tar -A -f results.tar report.tar
[user_name@localhost]$ tar -tvf results.tar
drwxr-xr-x name name        0 2016-11-20 16:16 results/
-rw-r--r-- name name    10905 2016-11-20 16:16 results/log1.dat
drwxr-xr-x name name        0 2016-11-20 16:16 results/Res-01/
-rw-r--r-- name name    11682 2016-11-20 16:16 results/Res-01/log.15Feb16.4
drwxr-xr-x name name        0 2016-11-20 16:16 results/Res-02/
-rw-r--r-- name name    34117 2016-11-20 16:16 results/Res-02/log.15Feb16.balance.b.4
drwxrwxr-x name name        0 2016-11-20 11:02 report/
-rw-r--r-- name name   924729 2015-11-20 04:14 report/report-2016.pdf
-rw-r--r-- name name   924729 2015-11-20 04:14 report/report-a.pdf
```

Dans l'exemple précédent, nous avons utilisé l'option **-A** (pour *Append*) dans `tar -A -f results.tar report.tar` pour ajouter l'archive *report.tar* à l'archive *results.tar* comme vous pouvez le constater en comparant le résultat de la commande `tar -tvf results.tar` avant et après l'opération.

!!! note "Note"
    Les options **-A**, `--catenate` et `--concatenate` sont équivalentes; selon le système que vous utilisez, certaines options pourraient ne pas être disponibles. La commande précédente peut aussi être utilisée comme suit :

    ```bash
    [user_name@localhost]$ tar -A -f full-results.tar report.tar
    [user_name@localhost]$ tar -A --file=full-results.tar report.tar
    [user_name@localhost]$ tar --list --file=full-results.tar
    ```

!!! note "Note"
    Il existe deux possibilités pour ajouter l'archive *archive_2.tar* à l'archive *archive_1.tar*. La première est d'utiliser **-r** comme nous l'avons vu précédemment quand on ajoute un fichier à une archive existante. Dans ce cas, l'archive ajoutée *archive_2.tar* apparaîtra comme un fichier ajouté à une archive existante. L'option **-tvf** montrera que l'archive sera ajoutée comme un fichier à la fin de l'archive. La deuxième possibilité est d'utiliser l'option **-A**. Dans ce cas, l'archive ajoutée n'apparaîtra pas comme une archive; la commande créera une nouvelle archive.

#### Exclure certains fichiers

À partir de l'exemple précédent, créons l'archive *results.tar* pour y enregistrer les résultats, mais en y ajoutant l'option `--exclude=*.dat` pour exclure les fichiers avec le suffixe *.dat*.

```bash
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat  programs/  report/  results/  tests/  work/
[user_name@localhost]$ ls results/
log1.dat  log5.dat  Res-01/  Res-02/
[user_name@localhost]$ tar -cvf results.tar --exclude=*.dat results/
results/
results/Res-01/
results/Res-01/log.15Feb16.4
results/Res-02/
results/Res-02/log.15Feb16.balance.b.4
[user_name@localhost]$ tar -tvf results.tar
drwxr-xr-x name name        0 2016-11-20 16:16 results/
drwxr-xr-x name name        0 2016-11-20 16:16 results/Res-01/
-rw-r--r-- name name    11682 2016-11-20 16:16 results/Res-01/log.15Feb16.4
drwxr-xr-x name name        0 2016-11-20 16:16 results/Res-02/
-rw-r--r-- name name    34117 2016-11-20 16:16 results/Res-02/log.15Feb16.balance.b.4
```

#### Conserver les liens symboliques

Si vous avez des liens symboliques dans votre répertoire et que vous voulez les préserver, ajoutez l'option **-h** à la commande `tar`.

```bash
[user_name@localhost]$ tar -cvhf results.tar results/
```

### Compression

#### Compresser un fichier, des fichiers, un fichier archive tar

La compression et l'archivage sont deux processus différents. L'archivage ou la création d'un fichier tar rassemble plusieurs fichiers ou répertoires dans un même fichier. Le processus de compression s'effectue sur un seul fichier ou une seule archive pour en diminuer la taille, avec des utilitaires comme `gzip` ou `bzip2`. Dans l'exemple suivant, nous compressons *new.log.dat* et *results.tar*.

*   Avec `gzip` :

    ```bash
    [user_name@localhost]$ ls
    bin/  documents/  jobs/  new.log.dat  new_results/  programs/  report/  results/  results.tar  tests/  work/
    [user_name@localhost]$ gzip new.log.dat
    [user_name@localhost]$ gzip results.tar
    [user_name@localhost]$ ls
    bin/  documents/  jobs/  new.log.dat.gz  new_results/  programs/  report/  results/  results.tar.gz  tests/  work/
    ```

*   Avec `bzip2` :

    ```bash
    [user_name@localhost]$ ls
    bin/  documents/  jobs/  new.log.dat  new_results/  programs/  report/  results/  results.tar  tests/  work/
    [user_name@localhost]$ bzip2 new.log.dat
    [user_name@localhost]$ bzip2 results.tar
    [user_name@localhost]$ ls
    bin/  documents/  jobs/  new.log.dat.bz2  new_results/  programs/  report/  results/  results.tar.bz2  tests/  work/
    ```

!!! note "Note"
    Pour compresser en même temps que l'archive est créée, utilisez les options **z** ou **j** pour `gzip` ou `bzip2` respectivement. L'extension du nom du fichier n'a pas vraiment d'importance. Pour les fichiers compressés avec `gzip`, `*.tar.gz` et `*.tgz` sont des extensions communes; pour les fichiers compressés avec `bzip2`, `*.tar.bz2` et `*.tbz` sont des extensions communes.

```bash
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat  programs/  report/  results/  tests/  work/
[user_name@localhost]$ tar -cvzf results.tar.gz results/
results/
results/log1.dat
results/Res-01/
results/Res-01/log.15Feb16.4
results/Res-02/
results/Res-02/log.15Feb16.balance.b.4
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat  programs/  report/  results/  results.tar.gz  tests/  work/
```

```bash
[user_name@localhost]$ tar -cvjf results.tar.bz2 results/
results/
results/log1.dat
results/Res-01/
results/Res-01/log.15Feb16.4
results/Res-02/
results/Res-02/log.15Feb16.balance.b.4
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat  programs/  report/  results/  results.tar.bz2  results.tar.gz  tests/  work/
```

#### Ajouter des fichiers à une archive compressée (tar.gz/tar.bz2)

Nous avons déjà mentionné qu'il n'est pas possible d'ajouter des fichiers à des archives compressées. Si nous devons le faire, il faut décompresser les fichiers avec `gunzip` ou `bunzip2`. Une fois que nous avons obtenu le fichier tar, nous ajoutons les fichiers à cette archive en utilisant l'option **r**. Nous pouvons ensuite compresser à nouveau avec `gzip` ou `bzip2`.

### Décompression

#### Extraire l'archive en entier

Pour décompresser ou extraire une archive, utilisez l'option **-x** (pour *extract*) avec **-f** (pour *file*); vous pouvez aussi ajouter **-v** (pour *verbosity*). Nous allons maintenant extraire l'archive *results.tar*. Pour extraire dans le même répertoire, il faut s'assurer qu'aucun autre répertoire n'a ce même nom. Pour éviter de réécrire les données s'il existe déjà un répertoire avec ce nom, nous allons rediriger l'extraction vers un autre répertoire avec l'option **-C**, en s'assurant que le répertoire de destination existe ou est créé avant de décompresser l'archive. Par exemple, créons le répertoire *new_results* pour y extraire les données de l'archive *results.tar*.

```bash
[user_name@localhost]$ tar -xvf results.tar -C new_results/
results/
results/log1.dat
results/Res-01/
results/Res-01/log.15Feb16.1
results/Res-01/log.15Feb16.4
results/Res-02/
results/Res-02/log.15Feb16.balance.b.4
new.log.dat
report/
report/report-2016.pdf
report/report-a.pdf
[user_name@localhost]$ ls new_results/
new.log.dat  report/  results/
```

!!! note "Note"
    L'option **v** affiche uniquement les noms des fichiers qui ont été extraits de l'archive. Utilisez cette option deux fois pour obtenir plus de détails (utilisez `tar -xvvf` au lieu de `tar -xvf`).

#### Décompresser des fichiers gz et bz2

Pour les fichiers avec l'extension `*.gz`, utilisez `gunzip`.

```bash
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat.gz  new_results/  programs/  report/  results/  results.tar.gz  tests/  work/
[user_name@localhost]$ gunzip new.log.dat.gz
[user_name@localhost]$ gunzip results.tar.gz
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat  new_results/  programs/  report/  results/  results.tar  tests/  work/
```

Pour les fichiers avec l'extension `*.bz2`, utilisez `bunzip2`.

```bash
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat.bz2  new_results/  programs/  report/  results/  results.tar.bz2  tests/  work/
[user_name@localhost]$ bunzip2 new.log.dat.bz2
[user_name@localhost]$ bunzip2 results.tar.bz2
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat  new_results/  programs/  report/  results/  results.tar  tests/  work/
```

#### Extraire un fichier archive compressé vers un autre répertoire

Comme c'est le cas avec un fichier tar, un fichier *archive compressée* peut être extrait dans un autre répertoire avec l'option **-C** pour indiquer le répertoire de destination et l'option **z** pour les fichiers `*.gz` ou **j** pour les fichiers `*.bz2`. Avec le même exemple que précédemment, nous allons extraire l'archive *results.tar.gz* (ou *results.tar.bz2*) dans le répertoire *new_results* en une ou deux étapes.

**Extraire le fichier archive compressé en une étape**

Avec `gz`

```bash
[user_name@localhost]$ tar -xvzf results.tar.gz -C new_results/
results/
results/log1.dat
results/Res-01/
results/Res-01/log.15Feb16.1
results/Res-01/log.15Feb16.4
results/Res-02/
results/Res-02/log.15Feb16.balance.b.4
[user_name@localhost]$ tar -xzf results.tar.gz -C new_results/
[user_name@localhost]$ ls new_results/
results/
```

Avec l'extension `bz2`

```bash
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat  new_results/  programs/  report/  results/  results.tar.bz2  tests/  work/
[user_name@localhost]$ tar -xvjf results.tar.bz2 -C new_results/
results/
results/log1.dat
results/Res-01/
results/Res-01/log.15Feb16.1
results/Res-01/log.15Feb16.4
results/Res-02/
results/Res-02/log.15Feb16.balance.b.4
[user_name@localhost]$ ls new_results/
results/
```

!!! note "Notes"
    *   Dans l'exemple précédent, il est possible de commencer avec l'option **-C** (le répertoire de destination), cependant, assurez-vous d'abord que le répertoire de destination existe puisque `tar` ne va pas le créer pour vous et s'il n'existe pas, `tar` va échouer. La commande est :

        ```bash
        [user_name@localhost]$ tar -C new_results/ -xzf results.tar.gz
        ```

        ou

        ```bash
        [user_name@localhost]$ tar -C new_results/ -xvjf results.tar.bz2
        ```
    *   Si l'option **-C** (répertoire de destination) n'est pas utilisée, les fichiers seront extraits dans le même répertoire.
    *   L'option **v** (pour *verbosity*) affiche les fichiers et répertoires au fur et à mesure de leur extraction vers le nouveau répertoire.
    *   Pour afficher plus de détails (comme la date, la permission, etc.), ajoutez une autre option **v** comme suit : `tar -C new_results/ -xvvzf results.tar.gz` ou `tar -C new_results/ -xvvjf results.tar.bz2`. L'extraction du fichier archive compressé se fait en deux étapes.

Nous utilisons ici les mêmes commandes qu'auparavant, mais sans les options **z** ou **j**. D'abord, `gunzip` ou `bunzip2` décompresse le fichier et ensuite `tar -xvf` pour détarer l'archive comme suit :

En supposant que nous avons le fichier compressé *results.tar.bz2* :

```bash
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat  new_results/  programs/  report/  results/  results.tar.bz2  tests/  work/
[user_name@localhost]$ bunzip2 results.tar.bz2
[user_name@localhost]$ tar -C ./new_results/ -xvvf results.tar
drwxrwxr-x name name        0 2016-11-20 11:02 results/
-rw-r--r-- name name    10905 2016-11-16 16:31 results/log1.dat
drwxrwxr-x name name        0 2016-11-20 15:16 results/Res-01/
-rw-r--r-- name name    11682 2016-11-16 15:10 results/Res-01/log.15Feb16.4
drwxrwxr-x name name        0 2016-11-16 19:37 results/Res-02/
-rw-r--r-- name name    34117 2016-11-16 15:10 results/Res-02/log.15Feb16.balance.b.4
[user_name@localhost]$ ls new_results/results/
log1.dat  log5.dat  Res-01/   Res-02/
[user_name@localhost]$ ls new_results/results/
log1.dat  Res-01/  Res-02/
```

Pour les fichiers `*.gz`

```bash
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat  new_results/  programs/  report/  results/  results.tar.gz  tests/  work/
[user_name@localhost]$ gunzip results.tar.gz
[user_name@localhost]$ tar -C ./new_results/ -xvvf results.tar
drwxrwxr-x name name        0 2016-11-20 11:02 results/
-rw-r--r-- name name    10905 2016-11-16 16:31 results/log1.dat
drwxrwxr-x name name        0 2016-11-20 15:16 results/Res-01/
-rw-r--r-- name name    11682 2016-11-16 15:10 results/Res-01/log.15Feb16.4
drwxrwxr-x name name        0 2016-11-16 19:37 results/Res-02/
-rw-r--r-- name name    34117 2016-11-16 15:10 results/Res-02/log.15Feb16.balance.b.4
[user_name@localhost]$ ls new_results/results/
log1.dat  Res-01/  Res-02/
```

#### Extraire un fichier d'une archive ou d'une archive compressée

Avec l'exemple précédent, nous allons d'abord créer l'archive *results.tar* pour archiver le répertoire et lister tous les fichiers qu'il contient, puis extraire un fichier vers le répertoire *new_results*.

```bash
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat  new_results/  programs/  report/  results/  results.tar  tests/  work/
[user_name@localhost]$ tar -tvf results.tar
drwxrwxr-x name name        0 2016-11-20 11:02 results/
-rw-r--r-- name name    10905 2016-11-16 16:31 results/log1.dat
drwxrwxr-x name name        0 2016-11-20 15:16 results/Res-01/
-rw-r--r-- name name    11682 2016-11-16 15:10 results/Res-01/log.15Feb16.4
drwxrwxr-x name name        0 2016-11-16 19:37 results/Res-02/
-rw-r--r-- name name    34117 2016-11-16 15:10 results/Res-02/log.15Feb16.balance.b.4
[user_name@localhost]$ ls new_results/
[user_name@localhost]$ tar -C ./new_results/ --extract --file=results.tar results/Res-01/log.15Feb16.4
[user_name@localhost]$ ls new_results/results/Res-01/log.15Feb16.4
new_results/results/Res-01/log.15Feb16.4
```

Dans cet exemple, le fichier *results/Res-01/log.15Feb16.4* a été extrait de l'archive sans que l'archive soit décompressée en entier en utilisant l'option `--extract`. La commande crée les mêmes répertoires de l'archive dans le répertoire de destination.

!!! note "Notes"
    *   Avec cette commande, il faut absolument utiliser **-C** pour le répertoire de destination, autrement le fichier sera extrait vers le même répertoire que celui où se trouve l'archive, s'il existe.
    *   Ceci fonctionne pour extraire un fichier ou un répertoire, mais il faut indiquer le bon chemin.
    *   Cette commande peut être utilisée pour extraire plusieurs fichiers en y ajoutant le chemin complet, comme dans l'exemple précédent.

    ```bash
    [user_name@localhost]$ tar -C ./new_results/ --extract --file=results.tar "results/Res-01/log.15Feb16.4" "file2" "file3"
    ```

Vous pouvez utiliser la même commande pour extraire un fichier à partir d'un fichier tar compressé.
D'un fichier `*.gz`

```bash
[user_name@localhost]$ tar -C ./new_results/ --extract -z --file=results.tar.gz results/Res-01/log.15Feb16.4
[user_name@localhost]$ ls new_results/results/Res-01/log.15Feb16.4
new_results/results/Res-01/log.15Feb16.4
```

D'un fichier `*.bz2`

```bash
[user_name@localhost]$ tar -C ./new_results/ --extract -j --file=results.tar.bz2 results/Res-01/log.15Feb16.4
[user_name@localhost]$ ls new_results/results/Res-01/log.15Feb16.4
new_results/results/Res-01/log.15Feb16.4
```

#### Extraire plusieurs fichiers avec des caractères génériques (*wildcards*)

```bash
[user_name@localhost]$ tar -C ./new_results/ -xvf results.tar --wildcards "results/*.dat"
[user_name@localhost]$ ls new_results/results/
log1.dat
```

Avec la commande ci-dessus, nous avons extrait les fichiers qui sont dans le répertoire *results* et avec l'extension *.dat*.

!!! note "Note"
    La commande est aussi valide avec les options **j** ou **z** pour les archives compressées, comme nous l'avons déjà vu. Avec notre exemple précédent, nous pouvons extraire tous les fichiers qui commencent par *log*, par exemple :

    ```bash
    [user_name@localhost]$ tar -C ./new_results/ -xvf results.tar --wildcards "results/log*"
    [user_name@localhost]$ ls new_results/results/
    log1.dat
    ```

### Contenu des fichiers d'archive

#### Lister le contenu

Si vous avez oublié ce que contient un fichier tar, il suffit d'en lister le contenu sans avoir à le décompresser avec `tar -t` :

```bash
[user_name@localhost]$ tar -tf results.tar
results/
results/log1.dat
results/Res-01/
results/Res-01/log.15Feb16.1
results/Res-01/log.15Feb16.4
results/Res-02/
results/Res-02/log.15Feb16.balance.b.4
```

De plus, l'option **-v** fournit des métadonnées en rapport avec les fichiers comme les permissions, la date de la dernière modification, le propriétaire, comme vous le verriez avec `ls -l` pour des fichiers non archivés.

```bash
[user_name@localhost]$ tar -tvf results.tar
drwxrwxr-x name name        0 2016-11-20 11:02 results/
-rw-r--r-- name name    10905 2016-11-16 16:31 results/log1.dat
drwxrwxr-x name name        0 2016-11-16 19:36 results/Res-01/
-rw-r--r-- name name    11672 2016-11-16 15:10 results/Res-01/log.15Feb16.1
-rw-r--r-- name name    11682 2016-11-16 15:10 results/Res-01/log.15Feb16.4
drwxrwxr-x name name        0 2016-11-16 19:37 results/Res-02/
-rw-r--r-- name name    34117 2016-11-16 15:10 results/Res-02/log.15Feb16.balance.b.4
```

Si vous voulez connaître le nombre de fichiers dans un fichier tar, vous pouvez ajouter aux commandes précédentes le trait vertical `|` avec `wc -l` (pour *word count* et *lines*), ce qui fournit le nombre de lignes dans le résultat de la commande devant le trait vertical.

```bash
[user_name@localhost]$ tar -tvf results.tar | wc -l
7
```

ou

```bash
[user_name@localhost]$ tar -tf results.tar | wc -l
7
```

Avec cet exemple, nous voyons qu'il y a 7 entrées dans le fichier tar, ce qui inclut tous les fichiers et sous-répertoires pour le répertoire et avec le répertoire lui-même. Mentionnons que les détails des fichiers ne sont pas affichés même avec l'utilisation de l'option **–v** parce que les résultats de la première commande sont filtrés par la commande `wc –l` qui affiche le nombre de lignes sans les détails.

Pour les commandes précédentes, les options peuvent être utilisées séparément, par exemple :

*   l'option **-tvf** équivaut à **-t -v -f**
*   l'option **-v** équivaut à `--verbose`
*   l'option **-t** équivaut à `--list`
*   l'option `--file=results.tar` équivaut à `-f results.tar`

!!! note "Note"
    L'option **-f** ou `--file=` précède toujours le nom du fichier tar.

#### Chercher un fichier dans un fichier archive sans avoir à le décompresser

Nous avons vu comment lister les fichiers dans une archive. Il est aussi possible de lister les fichiers et de chercher un fichier particulier avec le trait vertical et la commande `grep`. Par exemple, pour trouver *log.15Feb16.4* (dont le chemin est *results/Res-01/log.15Feb16.4*) :

```bash
[user_name@localhost]$ tar -tf results.tar | grep -a log.15Feb16.4
results/Res-01/log.15Feb16.4
[user_name@localhost]$ tar -tvf results.tar | grep -a log.15Feb16.4
-rw-r--r-- name name   11682 2016-11-16 15:10 results/Res-01/log.15Feb16.4
```

Nous allons maintenant essayer de trouver un autre fichier nommé *pbs_file* (qui n'existe pas vraiment dans notre archive).

```bash
[user_name@localhost]$ tar -tf results.tar | grep -a pbs_file
[user_name@localhost]$ tar -tvf results.tar | grep -a pbs_file
```

Comme vous pouvez le constater, le résultat de la commande est vide, ce qui signifie que le fichier n'existe pas dans cette archive.

Pour lister par exemple les fichiers qui commencent par *log* (ou toute autre chaîne de caractères) dans l'archive, entrez :

```bash
[user_name@localhost]$ tar -tf results.tar | grep -a log*
results/log1.dat
results/Res-01/log.15Feb16.1
results/Res-01/log.15Feb16.4
results/Res-02/log.15Feb16.balance.b.4
```

Pour obtenir plus de détails, ajoutez l'option **-v** :

```bash
[user_name@localhost]$ tar -tvf results.tar | grep -a log*
-rw-r--r-- name name    10905 2016-11-16 16:31 results/log1.dat
-rw-r--r-- name name    11672 2016-11-16 15:10 results/Res-01/log.15Feb16.1
-rw-r--r-- name name    11682 2016-11-16 15:10 results/Res-01/log.15Feb16.4
-rw-r--r-- name name    34117 2016-11-16 15:10 results/Res-02/log.15Feb16.balance.b.4
```

!!! note "Note"
    Pour lister les fichiers dans une archive ou dans un fichier compressé, vous pouvez aussi utiliser la commande `more` après le trait vertical.

#### Lister le contenu d'un fichier compressé (*.gz ou .bz2)

Comme nous l'avons vu dans le cas d'un fichier tar, il est possible de combiner la commande `tar` avec l'option **z** pour lister le contenu d'une archive compressée avec `gzip` sans avoir à décompresser le fichier, ou encore l'option **j** pour lister le contenu d'une archive compressée avec `bzip2`.
Pour des fichiers `*.gz`

```bash
[user_name@localhost]$ tar -tvzf results.tar.gz
drwxrwxr-x name name        0 2016-11-20 11:02 results/
-rw-r--r-- name name    10905 2016-11-16 16:31 results/log1.dat
drwxrwxr-x name name        0 2016-11-16 19:36 results/Res-01/
-rw-r--r-- name name    11672 2016-11-16 15:10 results/Res-01/log.15Feb16.1
-rw-r--r-- name name    11682 2016-11-16 15:10 results/Res-01/log.15Feb16.4
drwxrwxr-x name name        0 2016-11-16 19:37 results/Res-02/
-rw-r--r-- name name    34117 2016-11-16 15:10 results/Res-02/log.15Feb16.balance.b.4
-rw-r--r-- name name    10905 2016-11-20 11:16 new.log.dat
drwxrwxr-x name name        0 2016-11-20 11:02 report/
-rw-r--r-- name name   924729 2015-11-20 04:14 report/report-2016.pdf
-rw-r--r-- name name   924729 2015-11-20 04:14 report/report-a.pdf
```

Pour les fichiers `*.bz2`

```bash
[user_name@localhost]$ tar -tvjf results.tar.bz2
drwxrwxr-x name name        0 2016-11-20 11:02 results/
-rw-r--r-- name name    10905 2016-11-16 16:31 results/log1.dat
drwxrwxr-x name name        0 2016-11-16 19:36 results/Res-01/
-rw-r--r-- name name    11672 2016-11-16 15:10 results/Res-01/log.15Feb16.1
-rw-r--r-- name name    11682 2016-11-16 15:10 results/Res-01/log.15Feb16.4
drwxrwxr-x name name        0 2016-11-16 19:37 results/Res-02/
-rw-r--r-- name name    34117 2016-11-16 15:10 results/Res-02/log.15Feb16.balance.b.4
```

!!! note "Notes"
    *   Encore une fois, dans cet exemple, nous utilisons l'option **v** pour afficher tous les détails, même si elle n'est pas obligatoire.
    *   Les deux commandes précédentes peuvent aussi être combinées avec le trait vertical (`|`) et `wc`; ou le trait vertical (`|`) et la commande `grep`, comme nous l'avons déjà vu.

## Autres utilitaires

### Taille des fichiers, répertoires et archives

À partir de votre terminal, utilisez la commande `du -sh [votre_fichier ...]`.

```bash
[user_name@localhost]$ du -sh results.tar work tests
112K results.tar
58K  work
48K  tests
```

### Fractionner des fichiers

En connaissant la taille de vos fichiers ou répertoires, vous pouvez les diviser en plusieurs fichiers d'archive pour ne pas avoir à travailler avec de trop gros fichiers. Ceci fonctionne également avec les fichiers archive. Vous pouvez diviser un gros fichier ou un fichier tar en plusieurs parties comme suit :

`split -b <Taille-en-Mo><nom-du-fichier-ou-fichier-tar><nom-préfixe>`
`split -b 100MB results.tar small-res`

L'option **b** détermine la taille des morceaux et *nom-préfixe* est le nom des petits fichiers. La commande ci-dessus divise le fichier *results.tar* en petits fichiers de 100 Mo chacun dans le répertoire courant et les noms des fichiers commencent par *small-resaa small-resab small-resac small-resad* .... etc.

Pour retrouver le fichier original, utilisez la commande `cat` comme suit :

```bash
[user_name@localhost]$ cat small_res* > your_archive_name.tar
```

La commande `split` permet de diviser les gros fichiers en petites portions en l'utilisant avec la taille des portions (`-b` taille en Mo) puis en transférant toutes les portions. Une fois le transfert effectué, utilisez la commande `cat` pour récupérer le fichier original ou l'archive. Pour ajouter des chiffres plutôt que des lettres, utilisez l'option **-d**.

## Commandes fréquemment employées

*   `pwd` montre le chemin de travail actuel (pwd pour *present work directory*)

*   `ls` liste les fichiers et sous-répertoires (ls pour *list*)

*   `du -sh` montre la taille des fichiers, répertoires et sous-répertoires (du pour *disk usage*)

*   `!!! important "Important"`
    Les commandes `gzip` ou `bzip2` ajoutées à un fichier (*votre_fichier* ou *votre_archive.tar*) exigent de l'espace libre, comme c'est le cas pour la commande `tar` pour créer le fichier compressé résultant (*votre_fichier.gz* ou *votre_fichier.bz2*) ou (*votre_archive.tar.gz* ou *votre_archive.tar.bz2*). Ces commandes échoueront s'il ne reste plus d'espace ou si votre quota est atteint. Sur nos grappes, utilisez la commande `quota` ou `quota –s` à partir de votre terminal pour savoir si vous avez suffisamment d'espace pour des données additionnelles.

*   Exécuter `tar` pour un répertoire (*results*) :

    ```bash
    [user_name@localhost]$ tar -cvf results.tar results
    ```

*   Exécuter `tar` pour plusieurs fichiers ou répertoires en les rassemblant dans un seul fichier archive :

    ```bash
    [user_name@localhost]$ tar -cvf your_archive.tar dir1 dir2 dir3 dir4 dir5 file1 file2 file3 file4 file5
    ```

*   Exécuter `tar` pour tous les fichiers ou répertoires qui commencent par la lettre *r* ou une chaîne de caractères :

    ```bash
    [user_name@localhost]$ tar -cvf your_archive.tar r*
    ```

*   Lister le contenu d'un fichier tar (*results.tar*) incluant les détails :

    ```bash
    [user_name@localhost]$ tar -tvf results.tar
    ```

*   Lister le contenu d'un fichier tar (*results.tar*) sans les détails :

    ```bash
    [user_name@localhost]$ tar -tf results.tar
    ```

*   Compter le nombre d'entrées dans le fichier tar :

    ```bash
    [user_name@localhost]$ tar -tvf results.tar | wc -l
    [user_name@localhost]$ tar -tf results.tar | wc -l
    ```

*   Chercher un fichier (*nom_du_fichier_recherché*) dans un fichier archive (*votre_archive.tar*) sans décompresser l'archive :

    ```bash
    [user_name@localhost]$ tar -tf your_archive.tar | grep -a file_name_you_search
    [user_name@localhost]$ tar -tvf your_archive.tar | grep -a file_name_you_search
    ```

*   Ne lister que les fichiers dont les noms contiennent (au début, à la fin ou à l'intérieur) une chaîne particulière; ici par exemple les fichiers qui commencent par *log* :

    ```bash
    [user_name@localhost]$ tar -tf your_archive.tar | grep -a log*
    [user_name@localhost]$ tar -tvf your_archive.tar | grep -a log*
    ```

*   Ajouter un ou plusieurs fichiers ou un nouveau fichier (ici *nouveau_fichier*) à la fin du fichier tar *votre_archive.tar* :

    ```bash
    [user_name@localhost]$ tar -rf your_archive.tar new_file
    ```

    !!! note "Note"
        Il n'est pas possible d'ajouter des fichiers à des archives compressées (*.gz ou *.bzip2). Des fichiers peuvent être ajoutés à des archives tar simples (`*.tar`).

*   Ajoutez le répertoire *nouveau_répertoire* au fichier *votre_archive.tar* existant :

    ```bash
    [user_name@localhost]$ tar -rf your_archive.tar new_dir
    ```

*   Concaténer des archives (*archive_02.tar* à *archive_01.tar*) avec l'option **-A** :

    ```bash
    [user_name@localhost]$ tar -A -f archive_01.tar archive_02.tar
    ```

*   Extraire tout le fichier archive (*votre_archive.tar*) :

    ```bash
    [user_name@localhost]$ tar -xvf your_archive.tar
    ```

*   Extraire tout le fichier archive (*votre_archive.tar*) dans un répertoire particulier (*répertoire_de_destination*) :

    ```bash
    [user_name@localhost]$ tar -xvf your_archive.tar -C destination_dir
    ```

*   Compresser un fichier (*fichier0*) ou des fichiers (*fichier1 fichier2 fichier3 fichier4 fichier5*) dans un fichier archive (*votre_archive.tar*) avec la commande `gzip` :

    ```bash
    [user_name@localhost]$ gzip file0
    [user_name@localhost]$ gzip file1 file2 file3 file4 file5
    [user_name@localhost]$ gzip your_archive.tar
    ```

*   Compresser un fichier (*fichier0*) ou des fichiers (*fichier1 fichier2 fichier3 fichier4 fichier5*) dans un fichier archive (*votre_archive.tar*) avec la commande `bzip2` :

    ```bash
    [user_name@localhost]$ bzip2 file0
    [user_name@localhost]$ bzip2 file1 file2 file3 file4 file5
    [user_name@localhost]$ bzip2 your_archive.tar
    ```

*   Compresser avec les options **z** ou **j** pour `gzip` ou `bzip` respectivement :

    ```bash
    [user_name@localhost]$ tar -cvzf results.tar.gz results
    [user_name@localhost]$ tar -cvjf results.tar.bz2 results/
    [user_name@localhost]$ tar -cvzf results.tgz results
    [user_name@localhost]$ tar -cvjf results.tbz results/
    ```

*   Exclure des fichiers particuliers (par exemple ceux qui commencent par la lettre *o*) à la création d'un fichier tar :

    ```bash
    [user_name@localhost]$ tar -cvf your_archive.tar your_directory --exclude=*.o
    ```

*   Décompresser des fichiers `*.gz` ou `*.bz2` :

    Pour les fichiers avec l'extension `*.gz`, utilisez `gunzip` :

    ```bash
    [user_name@localhost]$ gunzip your_file.gz
    [user_name@localhost]$ gunzip your_archive.gz
    ```

    Pour les fichiers avec l'extension `*.bz2`, utilisez `bunzip2` :

    ```bash
    [user_name@localhost]$ bunzip2 your_file.bz2
    [user_name@localhost]$ bunzip2 your_archive.tar.bz2
    ```

*   Lister le contenu d'un fichier compressé (`*.gz` ou `*.bz2`) :

    ```bash
    [user_name@localhost]$ tar -tvzf your_archive.tar.gz
    [user_name@localhost]$ tar -tvjf your_archive.tar.bz2
    ```

    !!! note "Notes"
        *   Encore une fois, dans cet exemple, nous utilisons l'option **v** pour afficher tous les détails, même si elle n'est pas obligatoire.
        *   Les deux commandes précédentes peuvent aussi être combinées avec le trait vertical (`|`) et `wc`; ou le trait vertical (`|`) et la commande `grep`, comme nous l'avons déjà vu.

*   Extraire un fichier archive compressé vers un autre répertoire :

    ```bash
    [user_name@localhost]$ tar -xvzf your_archive.tar.gz -C destination_dir
    [user_name@localhost]$ tar -xvjf your_archive.tar.bz2 -C destination_dir
    [user_name@localhost]$ tar -C destination_dir -xvzf your_archive.tar.gz
    [user_name@localhost]$ tar -C destination_dir -xvjf your_archive.tar.bz2
    ```

*   Extraire et récupérer des données d'un fichier archive compressé en deux étapes :

    Pour les fichiers `*.bz2`

    ```bash
    [user_name@localhost]$ bunzip2 your_archive.tar.bz2
    [user_name@localhost]$ tar -C destination_dir -xvf your_archive.tar
    ```

    Pour les fichiers `*.gz`

    ```bash
    [user_name@localhost]$ gunzip your_archive.tar.gz
    [user_name@localhost]$ tar -C destination_dir -xvf your_archive.tar
    ```

*   Extraire un fichier d'une archive ou d'une archive compressée dans un autre répertoire :

    ```bash
    [user_name@localhost]$ tar -C ./destination_dir/ --extract --file=your_archive.tar path-to-your-file
    [user_name@localhost]$ tar -C ./destination_dir/ --extract --file=results.tar "file1" "file2" "file3"
    ```

    !!! note "Note"
        Indiquez explicitement le chemin vers le fichier à extraire.

*   La commande précédente peut aussi être utilisée pour extraire un fichier à partir d'un fichier tar compressé :

    Pour un fichier `gz`

    ```bash
    [user_name@localhost]$ tar -C ./destination_dir/ --extract -z --file=your_archive.tar.gz path-to-your-file
    ```

    Pour un fichier `bz2`

    ```bash
    [user_name@localhost]$ tar -C ./destination_dir/ --extract -j --file=your_archive.tar.bz2 path-to-your-file
    ```

*   Extraire plusieurs fichiers en utilisant un caractère générique, par exemple les fichiers avec `*.dat` :

    ```bash
    [user_name@localhost]$ tar -C ./destination_dir/ -xvf your_archive.tar --wildcards "path-to-files/*.dat"
    ```

*   Pour conserver les liens symboliques avec la commande `tar`, utilisez l'option **h** :

    ```bash
    [user_name@localhost]$ tar -cvhf your_archive.tar your_directory
    ```

*   Ajouter des fichiers à des archives compressées (`*.tar.gz` ou `*.tar.bz2`) :

    Pour ajouter des fichiers directement à une archive compressée, décompressez d'abord le fichier archive, ajoutez les fichiers comme nous l'avons vu précédemment, puis compressez de nouveau.

*   Déterminer la taille des fichiers ou des répertoires :

    ```bash
    [user_name@localhost]$ du -sh your_file your_archive.tar dir1 dir2 dir3
    ```

*   Diviser un fichier ou un fichier tar :

    ```bash
    [user_name@localhost]$ split -b <Taille-en-Mo><nom-du-fichier-tar>.<extension> nom-préfixe
    ```

    Par exemple, utilisez 1000 Mo pour chaque petit fichier :

    ```bash
    [user_name@localhost]$ split -b 1000MB your_archive.tar small-res
    ```

    Pour retrouver le fichier original :

    ```bash
    [user_name@localhost]$ cat small_res* > your_archive_name.tar