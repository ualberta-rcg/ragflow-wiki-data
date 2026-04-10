---
title: "Tar/fr"
slug: "tar"
lang: "fr"

source_wiki_title: "Tar/fr"
source_hash: "0c47972047c2367984986cbe46b4d0fc"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T11:38:33.520115+00:00"

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

L'[archivage](https://en.wikipedia.org/wiki/Archive_file) consiste à créer un fichier unique qui contient plusieurs fichiers plus petits. L'archivage de données peut améliorer l'efficacité du stockage et des transferts de fichiers. Il est plus rapide pour le [protocole de copie sécurisée (scp)](https://en.wikipedia.org/wiki/Secure_copy), par exemple, de transférer un fichier d'archive de taille raisonnable que des milliers de petits fichiers de taille totale équivalente.

La [compression](https://en.wikipedia.org/wiki/Data_compression) consiste à encoder un fichier de manière à ce que la même information soit contenue dans un nombre réduit d'octets de stockage. L'avantage pour le stockage de données à long terme devrait être évident. Pour les transferts de données, le temps passé à compresser les données peut être mis en balance avec le temps gagné en déplaçant moins d'octets, comme décrit dans cette discussion sur la [compression et le transfert de données](https://bluewaters.ncsa.illinois.edu/data-transfer-doc) du US National Center for Supercomputing Applications.

## Utilisation de `tar` pour archiver des fichiers et des répertoires

L'utilitaire d'archivage principal sur tous les systèmes Linux et de type Unix est la commande [tar](https://www.gnu.org/software/tar/manual/tar.html). Il regroupe plusieurs fichiers ou répertoires et génère un fichier unique, appelé *fichier d'archive* ou *fichier tar*. Par convention, un fichier d'archive a l'extension de nom de fichier ``.tar``.

Lorsque vous archivez un répertoire avec ``tar``, il inclura par défaut tous les fichiers et sous-répertoires qu'il contient, ainsi que les sous-sous-répertoires qu'ils contiennent, et ainsi de suite. Donc,

```bash
tar --create --file project1.tar project1
```

permettra d'empaqueter tout le contenu du répertoire ``project1/`` dans le fichier ``project1.tar``. Le répertoire original restera inchangé, ce qui peut doubler l'espace disque occupé !

Vous pouvez extraire des fichiers de l'archive en utilisant la même commande avec une option différente :

```bash
tar --extract --file project1.tar
```

S'il n'y a pas de répertoire portant le nom original, il sera créé. Si un répertoire de ce nom existe et contient des fichiers ayant les mêmes noms que ceux du fichier d'archive, ils seront écrasés.

## Comment compresser et décompresser des fichiers tar

``tar`` peut compresser un fichier d'archive en même temps qu'il le crée. Plusieurs méthodes de compression sont disponibles. Nous recommandons soit **``xz``** soit **``gzip``**, qui peuvent être utilisés comme suit :

```bash
tar --create --xz --file project1.tar.xz project1
tar --extract --xz --file project1.tar.xz
tar --create --gzip --file project1.tar.gz project1
tar --extract --gzip --file project1.tar.gz
```

Généralement, ``--xz`` produira un fichier compressé plus petit (un « meilleur taux de compression ») mais prendra plus de temps et utilisera plus de RAM lors de l'opération [Quick Benchmark: Gzip vs Bzip2 vs LZMA vs XZ vs LZ4 vs LZO](http://catchchallenger.first-world.info/wiki/Quick_Benchmark:_Gzip_vs_Bzip2_vs_LZMA_vs_XZ_vs_LZ4_vs_LZO). ``--gzip`` ne compresse généralement pas aussi bien, mais peut être utilisé si vous rencontrez des difficultés dues à une mémoire insuffisante ou à un temps d'exécution excessif lors de ``tar --create``.

Vous pouvez également exécuter ``tar --create`` d'abord sans compression, puis utiliser les commandes ``xz`` ou ``gzip`` dans une étape séparée, bien qu'il y ait rarement une raison de le faire. De même, vous pouvez exécuter ``xz -d`` ou ``gzip -d`` pour décompresser un fichier d'archive avant d'exécuter ``tar --extract``, mais encore une fois, il y a rarement une raison de le faire.

## Options courantes de `tar`

Voici les options les plus courantes pour la commande `tar`. Il existe deux formes synonymes pour chacune : une forme à une seule lettre précédée d'un seul tiret, et une forme en mot entier précédée d'un double tiret :

*   ``-c`` ou ``--create`` : Crée une nouvelle archive.
*   ``-f`` ou ``--file=`` : Indique le nom du fichier d'archive qui suit.
*   ``-x`` ou ``--extract`` : Extrait les fichiers de l'archive.
*   ``-t`` ou ``--list`` : Liste le contenu d'un fichier d'archive.
*   ``-J`` ou ``--xz`` : Compresse ou décompresse avec ``xz``.
*   ``-z`` ou ``--gzip`` : Compresse ou décompresse avec ``gzip``.

Les options à une seule lettre peuvent être combinées avec un seul tiret, par exemple :

```bash
tar -cJf project1.tar.zx project1
```

est équivalent à

```bash
tar --create --xz --file=project1.tar.xz project1
```

Il existe de nombreuses autres options pour ``tar``, et elles peuvent varier en fonction de la version que vous utilisez. Vous pouvez obtenir une liste complète des options disponibles sur votre système avec ``man tar`` ou ``tar --help``. Notez en particulier que certains systèmes plus anciens pourraient ne pas prendre en charge la compression ``--xz``.