---
title: "A tutorial on 'tar'/fr"
slug: "a_tutorial_on__tar"
lang: "fr"

source_wiki_title: "A tutorial on 'tar'/fr"
source_hash: "5772acf6043103271051d74fea8b4a47"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T01:41:35.666513+00:00"

tags:
  []

keywords:
  - "fichier archive compressé"
  - "exclure des fichiers"
  - "console"
  - "décompresser"
  - "ajouter des fichiers"
  - "combiner deux archives"
  - "archive results.tar"
  - "bzip2"
  - "commandes"
  - "Combiner deux archives"
  - "compresser"
  - "results.tar"
  - "tar.gz"
  - "lister le contenu"
  - "option -r"
  - "fichier compressé"
  - "taille des fichiers"
  - "concaténer"
  - "archives compressées"
  - "fractionner des fichiers"
  - "localhost"
  - "répertoires"
  - "enregistrer les résultats"
  - "archive"
  - "tar.bz2"
  - "results.tar.gz"
  - "fichiers"
  - "gzip"
  - "répertoire"
  - "Extraire"
  - "compression"
  - "caractères génériques"
  - "tar"
  - "ajouter une archive"
  - "archive compressée"
  - "trait vertical"
  - "gunzip"
  - "gz"
  - "extraire"
  - "extraire un fichier"
  - "grep"
  - "commande"
  - "chemin"
  - "exécuter tar"
  - "lister"
  - "commande tar"
  - "report.tar"
  - "extension"
  - "fichier tar"
  - "bunzip2"
  - "répertoire de destination"
  - "results.tar.bz2"
  - "options"
  - "Res-01"
  - "fichiers archive"
  - "log1.dat"
  - "plusieurs fichiers"
  - "archivage"
  - "fichier archive"
  - "option -A"
  - "option --exclude"
  - "archive existante"
  - "suffixe .dat"
  - "extraction"
  - "exclure les fichiers"
  - "décompression"
  - "new_results"
  - "extraire des fichiers"
  - "commande grep"
  - "chaîne de caractères"

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

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: true
---

*Page enfant de [Archivage et compression de fichiers](archivage-et-compression-de-fichiers.md)*

## Archiver des fichiers et des répertoires

La commande [tar](https://www.gnu.org/software/tar/manual/tar.html) est l'utilitaire d'archivage principal sous Linux et autres systèmes de type Unix. La commande rassemble plusieurs fichiers ou répertoires et génère un *fichier archive* (nommé aussi *fichier tar* ou *archive tar*). Par convention, un fichier archive possède le suffixe `.tar`. Le fichier archive d'un répertoire contient par défaut tous les fichiers et sous-répertoires avec leurs sous-répertoires, sous-sous-répertoires et ainsi de suite. Par exemple, la commande `tar --create --file project1.tar project1` rassemble le contenu du répertoire *project1* dans le fichier *project1.tar*; le fichier d'origine est conservé, ce qui peut doubler l'espace disque utilisé.

Pour extraire des fichiers du fichier archive, utilisez la commande avec une option différente, soit `tar --extract --file project1.tar`. S'il n'existe pas de répertoire avec le nom d'origine, il sera créé. S'il existe un répertoire avec le nom d'origine et qu'il contient des fichiers portant le même nom que ceux du fichier archive, ils seront remplacés. Il y a aussi une option pour spécifier le répertoire de destination pour le contenu extrait du fichier archive.

## Compression et décompression

L'utilitaire `tar` peut compresser un fichier archive en même temps que ce fichier est créé. Parmi les méthodes de compression, nous recommandons `xz` ou `gzip` qui s'utilisent comme suit :

```bash
[user_name@localhost]$ tar --create --xz --file project1.tar.xz project1
[user_name@localhost]$ tar --extract --xz --file project1.tar.xz
[user_name@localhost]$ tar --create --gzip --file project1.tar.gz project1
[user_name@localhost]$ tar --extract --gzip --file project1.tar.gz
```

De façon générale, `--xz` produit un fichier compressé plus petit (c'est-à-dire avec un meilleur taux de compression), mais utilise plus de mémoire vive.
`--gzip` ne compresse pas autant, mais vous pouvez l'utiliser si vous avez des problèmes de manque de mémoire ou de durée d'exécution avec `tar --create`.

Vous pouvez aussi lancer `tar --create` d'abord sans compression et utiliser ensuite la commande `xz` ou `gzip` dans une étape distincte, mais il est rarement utile de procéder ainsi. De même, vous pouvez lancer `xz -d` ou `gzip -d` pour décompresser un fichier archive avant de lancer `tar --extract`, mais ceci est aussi rarement utile.

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

Les options de la forme simple peuvent être combinées en les faisant précéder d'un seul tiret; par exemple `tar -cJf project1.tar.zx project1` équivaut à `tar --create --xz --file=project1.tar.xz project1`.

Plusieurs autres options sont disponibles, dépendant de la version que vous utilisez. Pour obtenir la liste de toutes les options dont vous disposez, lancez `man tar` ou `tar --help`. Notez que certaines versions moins récentes peuvent ne pas supporter la compression avec `--xz`.

## Exemples

Dans les exemples qui suivent, nous supposons un répertoire qui contient les sous-répertoires et fichiers (*bin/* *documents/* *jobs/* *new.log.dat* *programs/* *report/* *results/* *tests/* *work*). Comparez ces exemples avec le contenu de votre propre répertoire.

### Archivage

#### Répertoires particuliers

On utilise `tar` le plus fréquemment pour créer une archive d'un répertoire. Dans cet exemple, nous créons le fichier archive *results.tar* avec le répertoire *results*.

```bash
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat  programs/  report/  results/  tests/  work/
[user_name@localhost]$ tar -cvf results.tar results
results
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

L'option **v** permet de voir les fichiers qui ont été ajoutés; pour les cacher, omettez cette option.

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

Ici nous avons rassemblé tous les répertoires qui commencent par la lettre **r**. Il est aussi possible de rassembler des fichiers ou des répertoires avec une chaîne de caractères, par exemple *r*, `*.dat`, etc.

#### Ajouter des fichiers à la fin d'une archive

L'option **-r** est utilisée pour ajouter des fichiers à une archive existante sans avoir à en créer une autre ou à décompresser l'archive puis lancer `tar` à nouveau pour créer une nouvelle archive. Dans le prochain exemple, nous ajoutons le fichier *new.log.dat* à l'archive *results.tar*.

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

!!! note
    Il n'est pas possible d'ajouter des fichiers à une archive compressée (`*.gz*` ou `*.bz2*`). Les fichiers peuvent être ajoutés uniquement à une archive tar ordinaire. L'option **-r** est aussi utilisée avec la commande `tar` pour ajouter un ou plusieurs répertoires à un fichier tar existant. Nous allons maintenant ajouter le répertoire *report* à l'archive *results.tar* de l'exemple précédent :

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

Rappelez-vous que l'option **-v** n'est pas nécessaire si vous n'avez pas besoin de voir les détails pour les fichiers.

#### Combiner deux archives

Comme on peut ajouter un fichier à une archive, on peut aussi ajouter une archive à une autre archive avec l'option **-A**. Ajoutons l'archive *report.tar* (pour le rapport du répertoire) à l'archive *results.tar* existante :

Pour vérifier l'archive existante :

```bash
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat  programs/  report/  report.tar  results/  results.tar  tests/  work/
[user_name@localhost]$ ar -tvf results.tar
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

Dans l'exemple précédent, nous avons utilisé l'option **-A** (pour *Append*) dans `tar -A -f results.tar report.tar` pour ajouter l'archive *report.tar* à l'archive *results.tar* comme vous pouvez voir en comparant le résultat de la commande `tar -tvf results.tar` avant et après l'opération.

!!! note
    Les options **-A**, **--catenate** et **--concatenate** sont équivalentes; dépendant du système que vous utilisez, certaines options pourraient ne pas être disponibles. La commande précédente peut aussi être utilisée comme suit :

    ```bash
    [user_name@localhost]$ tar -A -f full-results.tar report.tar
    [user_name@localhost]$ tar -A --file=full-results.tar report.tar
    [user_name@localhost]$ tar --list --file=full-results.tar
    ```

!!! note
    Il existe deux possibilités pour ajouter l'archive *archive_2.tar* à l'archive *archive_1.tar*. La première est d'utiliser **-r** comme nous avons vu précédemment quand on ajoute un fichier à une archive existante. Dans ce cas, l'archive ajoutée *archive_2.tar* paraîtra comme un fichier ajouté à une archive existante. L'option **-tvf** montrera que l'archive sera ajoutée comme un fichier à la fin de l'archive. La deuxième possibilité est d'utiliser l'option **-A**. Dans ce cas, l'archive ajoutée ne paraîtra pas comme une archive; la commande créera une nouvelle archive.

#### Exclure certains fichiers

À partir de l'exemple précédent, créons l'archive *results.tar* pour y enregistrer les résultats, mais en y ajoutant l'option `--exclude=*.dat` pour exclure les fichiers avec le suffixe `.dat`.

```bash
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat  programs/  report/  results/  tests/  work/
[user_name@localhost]$ ls results/
log1.dat  log5.dat  Res-01/  Res-02/
[user_name@localhost]$ tar -cvf results.tar --exclude=*.dat results/
results/
results/Res-01/
results/Res-01/log.15Feb16.4|results/Res-02/
results/Res-02/log.15Feb16.balance.b.4
[user_name@localhost]$ tar -tvf results.tar
drwxr-xr-x name name        0 2016-11-20 16:16 results/
drwxr-xr-x name name        0 2016-11-20 16:16 results/Res-01/
-rw-r--r-- name name    11682 2016-11-20 16:16 results/Res-01/log.15Feb16.4
drwxr-xr-x name name        0 2016-11-20 16:16 results/Res-02/
-rw-r--r-- name name    34117 2016-11-20 16:16 results/Res-02/log.15Feb16.balance.b.4
```

#### Conserver les liens symboliques

Si vous avez des liens symboliques dans votre répertoire et que vous voulez les préserver, ajouter l'option **-h** à la commande `tar`.

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

!!! note
    Pour compresser en même temps que l'archive est créée, utilisez les options **z** ou **j** pour `gzip` ou `bzip2` respectivement. L'extension du nom du fichier n'a pas vraiment d'importance. Pour les fichiers compressés avec `gzip`, `*.tar.gz*` et `*.tgz*` sont des extensions communes; pour les fichiers compressés avec `bzip2`, `*.tar.bz2*` et `*.tbz*` sont des extensions communes.

    ```bash
    [user_name@localhost]$ ls
    bin/  documents/  jobs/  new.log.dat  programs/  report/  results/  tests/  work/
    [user_name@localhost]$ tar -cvzf results.tar.gz results/
    results/
    results/log1.dat
    results/Res-01/
    results/Res-01/log.15Feb16.4|results/Res-02/
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

Nous avons déjà mentionné qu'il n'est pas possible d'ajouter des fichiers à des archives compressées. Si nous devons le faire, il faut décompresser les fichiers avec `gunzip` ou `bunzip2`. Une fois que nous avons obtenu le fichier tar, nous ajoutons les fichiers à cette archive en invoquant l'option **r**. Nous pouvons ensuite compresser à nouveau avec `gzip` ou `bzip2`.

### Décompression

#### Extraire l'archive au complet

Pour décompresser ou extraire une archive, utilisez l'option **-x** (pour *extract*) avec **-f** (pour *file*); vous pouvez aussi ajouter **-v** (pour *verbosity*). Nous allons maintenant extraire l'archive *results.tar*. Pour extraire dans le même répertoire, il faut s'assurer qu'aucun autre répertoire ne possède ce même nom. Pour éviter d'avoir à ré-écrire les données s'il existe déjà un répertoire avec ce nom, nous allons rediriger l'extraction vers un autre répertoire avec l'option **-C**, en s'assurant que le répertoire de destination existe ou est créé avant de décompresser l'archive. Par exemple, créons le répertoire *new_results* pour y extraire les données de l'archive *results.tar*.

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

!!! note
    L'option **v** fait afficher uniquement les noms des fichiers qui ont été extraits de l'archive. Invoquez cette option deux fois pour obtenir plus de détails (utilisez `tar -xvvf` au lieu de `tar -xvf`).

#### Décompresser des fichiers gz et bz2

Pour les fichiers avec l'extension `*.gz*`, utilisez `gunzip`.

```bash
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat.gz  new_results/  programs/  report/  results/  results.tar.gz  tests/  work/
[user_name@localhost]$ gunzip new.log.dat.gz
[user_name@localhost]$ gunzip results.tar.gz
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat  new_results/  programs/  report/  results/  results.tar  tests/  work/
```

Pour les fichiers avec l'extension `*.bz2*`, utilisez `bunzip2`.

```bash
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat.bz2  new_results/  programs/  report/  results/  results.tar.bz2  tests/  work/
[user_name@localhost]$ bunzip2 new.log.dat.bz2
[user_name@localhost]$ bunzip2 results.tar.bz2
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat  new_results/  programs/  report/  results/  results.tar  tests/  work/
```

#### Extraire un fichier archive compressé vers un autre répertoire

Comme c'est le cas avec un fichier tar, une *archive tar compressée* peut être extraite dans un autre répertoire avec l'option **-C** pour indiquer le répertoire de destination et l'option **z** pour les fichiers `*.gz*` ou **j** pour les fichiers `*.bz2*`. Avec le même exemple que précédemment, nous allons extraire l'archive *results.tar.gz* (ou *results.tar.bz2*) dans le répertoire *new_results* en une ou deux étapes.

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
results/Res-02/|results/Res-02/log.15Feb16.balance.b.4
[user_name@localhost]$ ls new_results/
results/
```

!!! note
    *   Dans l'exemple précédent, il est possible de commencer avec l'option **-C** (le répertoire de destination), cependant, assurez-vous d'abord que le répertoire de destination existe puisque `tar` ne va pas le créer pour vous et s'il n'existe pas, `tar` va échouer. La commande est

        ```bash
        [user_name@localhost]$ tar -C new_results/ -xzf results.tar.gz
        ```

        ou

        ```bash
        [user_name@localhost]$ tar -C new_results/ -xvjf results.tar.bz2
        ```

!!! note
    *   Si l'option **-C** (répertoire de destination) n'est pas invoquée, les fichiers seront extraits dans le même répertoire.
    *   L'option **v** (pour *verbosity*) fait afficher les fichiers et répertoires comme ils sont extraits vers le nouveau répertoire.
    *   Pour faire afficher plus de détails (comme la date, la permission, etc.), ajoutez une autre option **v** comme suit : `tar -C new_results/ -xvvzf results.tar.gz` ou `tar -C new_results/ -xvvjf results.tar.bz2`. L'extraction du fichier archive compressé se fait en deux étapes.

Nous utilisons ici les mêmes commandes qu'auparavant, mais sans les options **z** ou **j**. D'abord, `gunzip` ou `bunzip2` décompresse le fichier et ensuite `tar -xvf` pour *dé-tarer* l'archive comme suit :

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

Pour les fichiers `*.gz*`

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

Avec l'exemple précédent, nous allons d'abord créer l'archive *results.tar* pour archiver le répertoire et lister tous les fichiers qu'il contient et ensuite extraire un fichier vers le répertoire *new_results*.

```bash
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat  new_results/  programs/  report/  results/  results.tar  tests/  work/
[user_name@localhost]$ tar -tvf results.tar
drwxrwxr-x name name        0 2016-11-20 11:02 results/
-rw-r--r-- name name    10905 2016-11-16 16:31 results/log1.dat
drwxrwxr-x name name        0 2016-11-20 15:16 results/Res-01/
-rw-r--r-- name name    11682 2016-11-16 15:10 results/Res-01/log.15Feb16.4
drwxrwxr-x name name        0 2016-11-16 19:37 results/Res-02/
-rw-r--r-- name name    34117 2016-11-16 15:10 results/Res-02/log.15Feb16.balance.b.4  [user_name@localhost]$ ls new_results/
[user_name@localhost]$ tar -C ./new_results/ --extract --file=results.tar results/Res-01/log.15Feb16.4
[user_name@localhost]$ ls new_results/results/Res-01/log.15Feb16.4
new_results/results/Res-01/log.15Feb16.4
```

Dans cet exemple, le fichier *results/Res-01/log.15Feb16.4* a été extrait de l'archive sans que l'archive soit décompressée au complet en utilisant l'option **--extract**. La commande crée les mêmes répertoires de l'archive dans le répertoire de destination.

!!! note
    *   Avec cette commande, il faut absolument utiliser **-C** pour le répertoire de destination, autrement le fichier sera extrait vers le même répertoire que celui où se trouve l'archive, s'il existe.
    *   Ceci fonctionne pour extraire un fichier ou un répertoire, mais il faut indiquer le bon chemin.
    *   Cette commande peut être utilisée pour extraire plusieurs fichiers en y ajoutant le chemin complet, comme dans l'exemple précédent.

    ```bash
    [user_name@localhost]$ tar -C ./new_results/ --extract --file=results.tar "results/Res-01/log.15Feb16.4" "file2" "file3"
    ```

Vous pouvez utiliser la même commande pour extraire un fichier à partir d'un fichier tar compressé.
D'un fichier `*.gz*`

```bash
[user_name@localhost]$ tar -C ./new_results/ --extract -z --file=results.tar.gz results/Res-01/log.15Feb16.4
[user_name@localhost]$ ls new_results/results/Res-01/log.15Feb16.4new_results/results/Res-01/log.15Feb16.4
```

D'un fichier `*.bz2*`

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

Avec la commande ci-dessus, nous avons extrait les fichiers qui sont dans le répertoire *results* et avec l'extension `*.dat*`.

!!! note
    La commande est aussi valide avec les options **j** ou **z** pour les archives compressées, comme nous avons déjà vu. Avec notre exemple précédent, nous pouvons extraire tous les fichiers qui commencent par *log*, par exemple :

    ```bash
    [user_name@localhost]$ tar -C ./new_results/ -xvf results.tar --wildcards "results/log*"
    [user_name@localhost]$ ls new_results/results/
    log1.dat
    ```

### Contenu des fichiers d'archive

#### Lister le contenu

Si vous avez oublié ce que contient un fichier tar, vous n'avez qu'à en lister le contenu sans avoir à le décompresser avec `tar -t` :

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

Si vous voulez connaître le nombre de fichiers dans un fichier tar, vous pouvez ajouter aux commandes précédentes le trait vertical ` | ` avec `wc -l` (pour *nombre de mots* et *lignes*), ce qui fournit le nombre de lignes dans le résultat de la commande devant le trait vertical.

```bash
[user_name@localhost]$ tar -tvf results.tar | wc -l
7
```

ou

```bash
[user_name@localhost]$ tar -tf results.tar | wc -l
7
```

Avec cet exemple, nous voyons qu'il y a 9 entrées dans le fichier tar, ce qui inclut tous les fichiers et sous-répertoires pour le répertoire et avec le répertoire lui-même. Mentionnons que les détails des fichiers ne sont pas montrés même avec l'utilisation de l'option **-v** parce que les résultats de la première commande sont filtrés par la commande `wc -l` qui affiche le nombre de lignes sans les détails.

Pour les commandes précédentes, les options peuvent être invoquées séparément, par exemple :

*   L'option **-tvf** équivaut à **-t -v -f**
*   L'option **-v** équivaut à **--verbose**
*   L'option **-t** équivaut à **--list**
*   L'option **--file=results.tar** équivaut à **-f results.tar**

!!! note
    L'option **-f** ou **--file=** précède toujours le nom du fichier tar.

#### Chercher un fichier dans un fichier archive sans avoir à le décompresser

Nous avons vu comment lister les fichiers dans une archive. Il est aussi possible de lister les fichiers et de chercher un fichier particulier avec le trait vertical et la commande `grep`. Par exemple, pour trouver *log.15Feb16.4* (dont le chemin est *results/Res-01/log.15Feb16.4*) :

```bash
[user_name@localhost]$ tar -tf results.tar | grep -a log.15Feb16.4
results/Res-01/log.15Feb16.4
[user_name@localhost]$ tar -tvf results.tar | grep -a log.15Feb16.4
-rw-r--r-- name name   11682 2016-11-16 15:10 results/Res-01/log.15Feb16.4
```

Nous allons maintenant essayer de trouver un autre fichier nommé *pbs_file* (qui n'existe pas en fait dans notre archive).

```bash
[user_name@localhost]$ tar -tf results.tar | grep -a pbs_file
[user_name@localhost]$ tar -tvf results.tar | grep -a pbs_file
```

Comme vous pouvez voir, le résultat de la commande est vide, ce qui signifie que le fichier n'existe pas dans cette archive.

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

!!! note
    Pour lister les fichiers dans une archive ou dans un fichier compressé, vous pouvez aussi utiliser la commande `more` après le trait vertical.

#### Lister le contenu d'un fichier compressé (`*.gz*` ou `*.bz2*`)

Comme nous avons vu dans le cas d'un fichier tar, il est possible de combiner la commande `tar` avec l'option **z** pour lister le contenu d'une archive compressée avec `gzip` sans avoir à décompresser le fichier, ou encore l'option **j** pour lister le contenu d'une archive compressée avec `bzip2`.

Pour des fichiers `*.gz*`

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

Pour les fichiers `*.bz2*`

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

!!! note
    *   Encore une fois, dans cet exemple, nous utilisons l'option **v** pour faire afficher tous les détails, même si elle n'est pas obligatoire.
    *   Les deux commandes précédentes peuvent aussi être combinées avec le trait vertical (` | `) et `wc`; ou le trait vertical (` | `) et la commande `grep`, comme nous avons déjà vu.

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

En connaissant la taille de vos fichiers ou répertoires, vous pouvez les diviser en plusieurs archives pour ne pas avoir à travailler avec de trop gros fichiers. Ceci fonctionne également avec les fichiers archive. Vous pouvez diviser un gros fichier ou un fichier tar en plusieurs parties comme suit :

`split -b <Taille-en-Mo> <nom-de-fichier-ou-archive-tar> <nom-prefixe>`
`split -b 100MB results.tar small-res`

L'option **b** détermine la taille des portions et *nom-préfixe* est le nom des petits fichiers. La commande ci-dessus divise le fichier *results.tar* en petits fichiers de 100Mo chacun dans le répertoire courant et les noms des fichiers commencent par *small-resaa small-resab small-resac small-resad* .... etc.

Pour retrouver le fichier original, utilisez la commande `cat` comme suit :

```bash
[user_name@localhost]$ cat small_res* > your_archive_name.tar
```

La commande `split` permet de diviser les gros fichiers en petites portions en l'invoquant avec la taille des portions (**-b** taille en Mo) puis en transférant toutes les portions. Une fois le transfert effectué, utilisez la commande `cat` pour récupérer le fichier original ou l'archive. Pour ajouter des chiffres plutôt que des lettres, utilisez l'option **-d**.

## Commandes fréquemment employées

*   `pwd` montre le répertoire de travail actuel (pwd pour *present work directory*)

*   `ls` liste les fichiers et sous-répertoires (ls pour *list*)

*   `du -sh` montre la taille des fichiers, répertoires et sous-répertoires (du pour *disk usage*)

*   !!! important "Important"
        Les commandes `gzip` ou `bzip2` ajoutées à un fichier (*votre_fichier* ou *votre_archive.tar*) exigent de l'espace libre, comme c'est le cas pour la commande `tar` pour créer le fichier compressé résultant (*votre_fichier.gz* ou *votre_fichier.bz2*) ou (*votre_archive.tar.gz* ou *votre_archive.tar.bz2*). Ces commandes échoueront s'il ne reste plus d'espace ou si votre quota est atteint. Sur nos grappes, utilisez la commande `quota` ou `quota -s` à partir de votre terminal pour savoir si vous avez suffisamment d'espace pour des données additionnelles.

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

    !!! note
        Il n'est pas possible d'ajouter des fichiers à des archives compressées (`*.gz*` ou `*.bz2*`). Des fichiers peuvent être ajoutés à des archives tar simples (`*.tar*`).

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
    [user_name@localhost]$ tar -cvzf results.tar.gz results|
    [user_name@localhost]$ tar -cvjf results.tar.bz2 results/
    [user_name@localhost]$ tar -cvzf results.tgz results
    [user_name@localhost]$ tar -cvjf results.tbz results/
    ```

*   Exclure des fichiers particuliers (par exemple ceux qui commencent par la lettre *o*) à la création d'un fichier tar :

    ```bash
    [user_name@localhost]$ tar -cvf your_archive.tar your_directory --exclude=*.o
    ```

*   Décompresser des fichiers `*.gz*` ou `*.bz2*` :

    Pour les fichiers avec l'extension `*.gz*`, utilisez `gunzip` :

    ```bash
    [user_name@localhost]$ gunzip your_file.gz
    [user_name@localhost]$ gunzip your_archive.gz
    ```

    Pour les fichiers avec l'extension `*.bz2*`, utilisez `bunzip2` :

    ```bash
    [user_name@localhost]$ bunzip2 your_file.bz2
    [user_name@localhost]$ bunzip2 your_archive.tar.bz2
    ```

*   Lister le contenu d'un fichier compressé [`*.gz*` ou `*.bz2*`] :

    ```bash
    [user_name@localhost]$ tar -tvzf your_archive.tar.gz
    [user_name@localhost]$ tar -tvjf your_archive.tar.bz2
    ```

    !!! note
        *   Encore une fois, dans cet exemple, nous utilisons l'option **v** pour faire afficher tous les détails, même si elle n'est pas obligatoire.
        *   Les deux commandes précédentes peuvent aussi être combinées avec le trait vertical (` | `) et `wc`; ou le trait vertical (` | `) et la commande `grep`, comme nous avons déjà vu.

*   Extraire un fichier archive compressé vers un autre répertoire :

    ```bash
    [user_name@localhost]$ tar -xvzf your_archive.tar.gz -C destination_dir
    [user_name@localhost]$ tar -xvjf your_archive.tar.bz2 -C destination_dir
    [user_name@localhost]$ tar -C destination_dir -xvzf your_archive.tar.gz
    [user_name@localhost]$ tar -C destination_dir -xvjf your_archive.tar.bz2
    ```

*   Extraire et récupérer des données d'un fichier archive compressé en deux étapes :

    Pour les fichiers `*.bz2*`

    ```bash
    [user_name@localhost]$ bunzip2 your_archive.tar.bz2
    [user_name@localhost]$ tar -C destination_dir -xvf your_archive.tar
    ```

    Pour les fichiers `*.gz*`

    ```bash
    [user_name@localhost]$ gunzip your_archive.tar.gz
    [user_name@localhost]$ tar -C destination_dir -xvf your_archive.tar
    ```

*   Extraire un fichier d'une archive ou d'une archive compressée dans un autre répertoire :

    ```bash
    [user_name@localhost]$ tar -C ./destination_dir/ --extract --file=your_archive.tar path-to-your-file
    [user_name@localhost]$ tar -C ./destination_dir/ --extract --file=results.tar "file1" "file2" "file3"
    ```

    !!! note
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

*   Extraire plusieurs fichiers en utilisant un caractère générique, par exemple les fichiers avec `*.dat*` :

    ```bash
    [user_name@localhost]$ tar -C ./destination_dir/ -xvf your_archive.tar --wildcards "path-to-files/*.dat"
    ```

*   Pour conserver les liens symboliques avec la commande `tar`, utilisez l'option **h** :

    ```bash
    [user_name@localhost]$ tar -cvhf your_archive.tar your_directory
    ```

*   Ajouter des fichiers à des archives compressées (`*.tar.gz*` ou `*.tar.bz2*`) :

    Pour ajouter des fichiers directement à une archive compressée, décompressez d'abord le fichier archive, ajoutez les fichiers comme nous avons vu précédemment, puis compressez de nouveau.

*   Déterminer la taille des fichiers ou des répertoires :

    ```bash
    [user_name@localhost]$ du -sh your_file your_archive.tar dir1 dir2 dir3
    ```

*   Diviser un fichier ou un fichier tar :

    ```bash
    [user_name@localhost]$ split -b <Size-in-MB><tar-file-name>.<extension> prefix-name
    ```

    Par exemple, utilisez 1000Mo pour chaque petit fichier :

    ```bash
    [user_name@localhost]$ split -b 1000MB your_archive.tar small-res
    ```

    Pour récupérer le fichier original :

    ```bash
    [user_name@localhost]$ cat small_res* > your_archive_name.tar