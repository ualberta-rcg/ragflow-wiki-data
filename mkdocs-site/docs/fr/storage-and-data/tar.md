---
title: "Tar/fr"
slug: "tar"
lang: "fr"

source_wiki_title: "Tar/fr"
source_hash: "0c47972047c2367984986cbe46b4d0fc"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:49:03.135439+00:00"

tags:
  []

keywords:
  - "archive utilities"
  - "data migration"
  - "tar command"
  - "xz"
  - "compression"
  - "gzip"
  - "archive file"
  - "tar"
  - "disk usage"
  - "compress"
  - "single-letter options"
  - "data compression"

questions:
  - "What are the definitions and primary benefits of archiving and compressing data?"
  - "How do you use the tar command to create and extract archive files in Linux or Unix-like systems?"
  - "What are the differences between the xz and gzip compression methods when used with the tar command?"
  - "What terminal commands should be used to inspect the contents and sizes of files and directories before starting the archiving process?"
  - "How does the tar command differ from gzip and bzip2 in terms of preserving the original files and utilizing disk space?"
  - "What is the difference between tar and utilities like gzip or bzip2 regarding their ability to process multiple files or directories versus a single file?"
  - "What command-line option is used to list the contents of an archive file?"
  - "Which flags dictate whether the archive is compressed using xz or gzip?"
  - "How can multiple single-letter options be combined into a single command string?"
  - "What terminal commands should be used to inspect the contents and sizes of files and directories before starting the archiving process?"
  - "How does the tar command differ from gzip and bzip2 in terms of preserving the original files and utilizing disk space?"
  - "What is the difference between tar and utilities like gzip or bzip2 regarding their ability to process multiple files or directories versus a single file?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

L'archivage consiste à créer un fichier unique qui contient plusieurs fichiers plus petits. L'archivage de données peut améliorer l'efficacité du stockage et des transferts de fichiers. Il est plus rapide pour le protocole de copie sécurisée ([scp](https://en.wikipedia.org/wiki/Secure_copy)), par exemple, de transférer un seul fichier d'archive de taille raisonnable que des milliers de petits fichiers de taille totale équivalente.

La compression consiste à encoder un fichier de manière à ce que la même information soit contenue dans moins d'octets de stockage. L'avantage pour le stockage de données à long terme devrait être évident. Pour les transferts de données, le temps passé à compresser les données peut être contrebalancé par le temps économisé en déplaçant moins d'octets, comme décrit dans cette [discussion sur la compression et le transfert de données](https://bluewaters.ncsa.illinois.edu/data-transfer-doc) du National Center for Supercomputing Applications des États-Unis.

## Archiver des fichiers et des répertoires avec tar

L'utilitaire d'archivage principal sur tous les systèmes Linux et de type Unix est la commande [tar](https://www.gnu.org/software/tar/manual/tar.html). Elle regroupe un ensemble de fichiers ou de répertoires et génère un fichier unique, appelé *fichier d'archive* ou *fichier tar*. Par convention, un fichier d'archive porte l'extension de fichier `.tar`.

Lorsque vous archivez un répertoire avec `tar`, il inclura par défaut tous les fichiers et sous-répertoires qu'il contient, ainsi que les sous-sous-répertoires qu'ils contiennent, et ainsi de suite. Ainsi,
```bash
tar --create --file project1.tar project1
```
regroupera tout le contenu du répertoire `project1/` dans le fichier `project1.tar`. Le répertoire original restera inchangé, ce qui peut doubler l'espace disque occupé!

Vous pouvez extraire les fichiers de l'archive en utilisant la même commande avec une option différente :
```bash
tar --extract --file project1.tar
```
S'il n'y a pas de répertoire portant le nom d'origine, il sera créé. Si un répertoire de ce nom existe et contient des fichiers ayant les mêmes noms que dans le fichier d'archive, ils seront écrasés.

## Comment compresser et décompresser des fichiers tar

`tar` peut compresser un fichier d'archive en même temps qu'il le crée. Il existe plusieurs méthodes de compression parmi lesquelles choisir. Nous recommandons soit **`xz`** soit **`gzip`**, qui peuvent être utilisés comme suit :
```bash
tar --create --xz --file project1.tar.xz project1
tar --extract --xz --file project1.tar.xz
tar --create --gzip --file project1.tar.gz project1
tar --extract --gzip --file project1.tar.gz
```
Typiquement, `--xz` produira un fichier compressé plus petit (un "meilleur taux de compression") mais prendra plus de temps et utilisera plus de RAM pendant l'opération [Quick Benchmark: Gzip vs Bzip2 vs LZMA vs XZ vs LZ4 vs LZO](http://catchchallenger.first-world.info/wiki/Quick_Benchmark:_Gzip_vs_Bzip2_vs_LZMA_vs_XZ_vs_LZ4_vs_LZO). `--gzip` ne compresse généralement pas autant, mais peut être utilisé si vous rencontrez des difficultés dues à une mémoire insuffisante ou à un temps d'exécution excessif lors de `tar --create`.

Vous pouvez également exécuter `tar --create` d'abord sans compression, puis utiliser les commandes `xz` ou `gzip` dans une étape séparée, bien qu'il y ait rarement une raison de le faire. De même, vous pouvez exécuter `xz -d` ou `gzip -d` pour décompresser un fichier d'archive avant d'exécuter `tar --extract`, mais encore une fois, il y a rarement une raison de le faire.

## Options courantes de tar

Voici les options les plus courantes pour la commande tar. Il existe deux formes synonymes pour chacune : une forme à lettre unique précédée d'un seul tiret, et une forme en mot complet précédée d'un double tiret :

*   `-c` ou `--create` : Créer une nouvelle archive.
*   `-f` ou `--file=` : Indique le nom du fichier d'archive.
*   `-x` ou `--extract` : Extraire les fichiers de l'archive.
*   `-t` ou `--list` : Lister le contenu d'un fichier d'archive.
*   `-J` ou `--xz` : Compresser ou décompresser avec `xz`.
*   `-z` ou `--gzip` : Compresser ou décompresser avec `gzip`.

Les options à lettre unique peuvent être combinées avec un seul tiret, par exemple :
```bash
tar -cJf project1.tar.zx project1
```
est équivalent à
```bash
tar --create --xz --file=project1.tar.xz project1
```
Il existe de nombreuses autres options pour `tar`, et elles peuvent dépendre de la version que vous utilisez. Vous pouvez obtenir une liste complète des options disponibles sur votre système avec `man tar` ou `tar --help`. Notez en particulier que certains systèmes plus anciens pourraient ne pas prendre en charge la compression `--xz`.