---
title: "Handling large collections of files/fr"
slug: "handling_large_collections_of_files"
lang: "fr"

source_wiki_title: "Handling large collections of files/fr"
source_hash: "6a84ff7f0afad1c86919f096a7d82039"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:55:14.789532+00:00"

tags:
  []

keywords:
  - "optimisation"
  - "Disque RAM"
  - "nœuds de calcul"
  - "Archivage"
  - "intelligence artificielle"
  - "SQLite"
  - "ensembles de données"
  - "systèmes de fichiers"
  - "Compression parallèle"
  - "système de fichiers"
  - "tmpfs"
  - "disque local"
  - "SLURM_TMPDIR"
  - "HDF5"

questions:
  - "Pourquoi un très grand nombre de petits fichiers pose-t-il problème sur les systèmes de fichiers partagés ?"
  - "Quelles commandes permettent d'identifier les répertoires contenant le plus de fichiers ou occupant le plus d'espace disque ?"
  - "Comment l'utilisation du disque local via la variable $SLURM_TMPDIR permet-elle d'optimiser le traitement des grands ensembles de données ?"
  - "Quelles sont les particularités et les contraintes liées à l'utilisation du répertoire `/tmp` (configuré en `tmpfs`) lors de l'exécution d'une tâche ?"
  - "Quels outils et formats (tels que dar, HDF5 et SQLite) sont recommandés pour archiver et stocker efficacement de grandes quantités de données ou des objets complexes ?"
  - "Quelles techniques peuvent être employées pour optimiser les performances lors de la manipulation de fichiers (comme la compression parallèle, l'extraction partielle d'archives ou l'utilisation de `git repack`) ?"
  - "Comment le script illustré sauvegarde-t-il les résultats des calculs à partir du répertoire temporaire ?"
  - "Quel répertoire ou système de fichiers est spécifiquement désigné pour être utilisé comme disque RAM sur les nœuds de calcul ?"
  - "Avec quelle technologie le disque RAM est-il implémenté selon le document ?"
  - "Quelles sont les particularités et les contraintes liées à l'utilisation du répertoire `/tmp` (configuré en `tmpfs`) lors de l'exécution d'une tâche ?"
  - "Quels outils et formats (tels que dar, HDF5 et SQLite) sont recommandés pour archiver et stocker efficacement de grandes quantités de données ou des objets complexes ?"
  - "Quelles techniques peuvent être employées pour optimiser les performances lors de la manipulation de fichiers (comme la compression parallèle, l'extraction partielle d'archives ou l'utilisation de `git repack`) ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! warning "Impact sur la performance du système de fichiers"

Un très grand nombre de fichiers, et particulièrement des fichiers de petite taille, cause d'importants problèmes à la performance des systèmes de fichiers et à la sauvegarde automatisée de `/home` et `/project`.

Dans certains domaines, particulièrement en [intelligence artificielle et en apprentissage machine](ai-and-machine-learning.md), on doit souvent composer avec des centaines de milliers de fichiers comprenant parfois plusieurs centaines de kilo-octets. Dans ces cas, il faut tenir compte des limites d’objets imposées par les [quotas des systèmes de fichiers](storage-and-file-management.md#quotas-et-politiques).

Nous présentons ici les avantages et les inconvénients de quelques solutions pour le stockage de ces grands ensembles de données.

## Localiser les répertoires qui contiennent un grand nombre de fichiers

Dans un souci d’optimisation, il est toujours préférable d’identifier d'abord les répertoires où des gains de performance sont possibles. Vous pouvez utiliser le code suivant pour compter récursivement les fichiers dans les sous-répertoires du répertoire courant.

```bash
for FOLDER in $(find . -maxdepth 1 -type d | tail -n +2); do
  echo -ne "$FOLDER:\t"
  find $FOLDER -type f | wc -l
done
```

## Localiser les répertoires qui occupent le plus d'espace disque

La commande suivante liste les 10 répertoires qui occupent le plus d'espace dans le répertoire courant.

```bash
du -sh * | sort -hr | head -10
```

## Solutions

### Disque local

Les disques locaux reliés aux nœuds de calcul sont des SSD SATA ou plus; de façon générale, leur performance est de loin supérieure à celle des systèmes de fichiers `/project` et `/scratch`. Un disque local est partagé par toutes les tâches qui sont exécutées simultanément sur un de ses nœuds de calcul, ce qui veut dire que l’ordonnanceur ne gère pas l'utilisation du disque.

!!! note "Capacité du disque local"
    La capacité réelle d'espace disque local n'est pas la même pour toutes les grappes et elle peut varier à l'intérieur d'une même grappe.

*   [Béluga](beluga.md) offre environ 370Go de disque local pour les nœuds CPU; les nœuds GPU ont un disque NVMe de 1.6To pour aider avec les jeux de données image en intelligence artificielle qui possèdent des millions de petits fichiers.
*   [Niagara](niagara.md) n'offre pas de stockage local sur ses nœuds de calcul.
*   Dans le cas des autres grappes, vous pouvez supposer que l'espace disque disponible est d'au moins 190Go.

Vous pouvez accéder au disque local de l'intérieur d'une tâche en utilisant la variable d'environnement `$SLURM_TMPDIR`. Une approche serait alors de conserver votre ensemble de données dans un seul fichier archive `tar` dans l'espace /project et de le copier ensuite sur le disque local au début de votre tâche, l'extraire et utiliser les données au cours de la tâche. S'il y a eu des changements, vous pourrez archiver le contenu dans un fichier `tar` et le recopier dans l'espace /project.

Le script de soumission suivant utilise un nœud entier.

```bash title="job_script.sh"
#!/bin/bash
#SBATCH --time=1-00:00        
#SBATCH --nodes=1             
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=0               


cd $SLURM_TMPDIR
mkdir work
cd work
tar -xf ~/projects/def-foo/johndoe/my_data.tar
# Maintenant, effectuez les calculs sur le disque local en utilisant le contenu de l'archive extraite...

# Les calculs sont terminés, nettoyez l'ensemble de données...
cd $SLURM_TMPDIR
tar -cf ~/projects/def-foo/johndoe/results.tar work
```

### Disque RAM

Le système de fichiers `/tmp` peut être utilisé comme disque RAM sur les nœuds de calcul. Il est implémenté avec [tmpfs](https://fr.wikipedia.org/wiki/Tmpfs).

*   `/tmp` est `tmpfs` sur toutes les grappes;
*   `/tmp` est vidé à la fin de la tâche;
*   comme toutes les autres utilisations de la mémoire par une tâche, compte dans la limite imposée pour le `cgroup` qui est associé à la requête `sbatch`;
*   la capacité de `tmpfs` est fixée à 100% via les options *mount*.

!!! warning "Comportement de /tmp (tmpfs)"
    La capacité de `tmpfs` étant fixée à 100% via les options *mount* peut nuire à certains scripts, car `MemTotal` représente alors la capacité du RAM physique, ce qui ne correspond pas à la requête `sbatch`.

### Archivage

#### dar

Utilitaire d’archivage sur disque conçu pour améliorer l’outil [tar](a-tutorial-on-tar.md); voir le [tutoriel dar](dar.md).

#### HDF5

Format de fichier binaire pour le stockage de plusieurs sortes de données dont les objets étendus comme les matrices et les images. Des outils pour la manipulation de ces fichiers sont disponibles avec plusieurs langages, tel Python ([h5py](https://www.h5py.org/)); voir [HDF5](hdf5.md).

#### SQLite

[SQLite](https://www.sqlite.org) permet d’utiliser les bases de données relationnelles contenues dans un seul fichier enregistré sur disque, sans l’entremise d’un serveur. La commande SQL `SELECT` sert d’accès aux données et des API sont disponibles pour plusieurs langages de programmation.

Avec les API, vous pouvez interagir avec votre base de données SQLite dans des programmes en C/C++, Python, R, Java ou Perl par exemple. Les bases de données relationnelles modernes ont des types de données pour la gestion du stockage des BLOB (*binary large objects*) comme le contenu des fichiers image; plutôt que de stocker 5 ou 10 millions de fichiers image PNG ou JPEG individuellement, il serait plus pratique de les grouper dans un fichier SQLite.

Cette solution demande toutefois de créer une base de données SQLite; vous devez donc connaître SQL et pouvoir créer une base de données relationnelle simple.

!!! warning "Performance de SQLite pour de grandes bases de données"
    La performance de SQLite peut se dégrader avec de très grandes bases de données (à partir de plusieurs gigaoctets); vous pourriez alors préférer une approche plus traditionnelle et utiliser [MySQL](https://www.mysql.com) ou [PostgreSQL](https://www.postgresql.org) avec un [serveur de bases de données](database-servers.md).

L'exécutable SQLite se nomme `sqlite3`. Il est disponible par le [module](utiliser-des-modules.md) `nixpkgs` qui est chargé par défaut sur nos systèmes.

#### Compression parallèle

Pour créer une archive avec un grand nombre de fichiers, il pourrait être avantageux d'en faire une archive compressée avec `pigz` plutôt que d'utiliser `gzip`.

```bash
tar -vc --use-compress-program="pigz -p 4" -f dir.tar.gz dir_to_tar
```

Ici, la compression utilise 4 cœurs.

#### Extraction partielle d'un fichier archive

Il n'est pas toujours nécessaire d'extraire tout le contenu d'un fichier archive. Par exemple, si une simulation ou une tâche ne nécessite que les fichiers d'un répertoire en particulier, le répertoire peut être extrait du fichier d'archive et sauvegardé sur le disque local avec

```bash
tar -zxf /path/to/archive.tar.gz dir/subdir --directory $SLURM_TMPDIR
```

### Fichiers cachés

### git

Si vous utilisez `git`, le nombre de fichiers dans le sous-répertoire caché peut augmenter de beaucoup avec le temps.

!!! tip "Optimiser Git avec `git repack`"
    Pour accélérer la performance, utilisez la commande `git repack` qui groupe plusieurs des fichiers dans quelques grandes bases de données.