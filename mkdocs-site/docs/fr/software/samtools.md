---
title: "Samtools/fr"
slug: "samtools"
lang: "fr"

source_wiki_title: "Samtools/fr"
source_hash: "debed46bd1cd1b81726329f88a07e26d"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:20:58.756698+00:00"

tags:
  - software

keywords:
  - "plusieurs cœurs"
  - "samtools"
  - "multithreading"
  - "fichiers SAM et BAM"
  - "bash"
  - "SBATCH"
  - "conversion de fichiers"
  - "séquençage à haut débit"
  - "tri et indexation"
  - "Samtools"
  - "GNU Parallel"
  - "fichiers SAM"

questions:
  - "Quelles sont les principales fonctionnalités et différences entre Samtools, BCFtools et HTSlib pour le traitement des données de séquençage ?"
  - "Comment procéder à la conversion d'un fichier d'alignement SAM en fichier compressé BAM, que le fichier contienne un en-tête ou non ?"
  - "Quelles sont les commandes et méthodes recommandées pour trier, indexer et traiter efficacement plusieurs fichiers simultanément (notamment via le multifil ou GNU parallel) ?"
  - "Quel indicateur permet d'activer le multithreading directement au sein des commandes Samtools ?"
  - "Quel outil externe est suggéré pour exécuter des opérations sur plusieurs fichiers SAM de manière simultanée ?"
  - "Quel paramètre de configuration faut-il ajuster dans le script si le nombre de fichiers d'entrée varie ?"
  - "Quelle est l'action principale effectuée par la boucle sur les fichiers `.sam` dans le script fourni ?"
  - "Quelles sont les ressources de calcul (processeur, mémoire, temps) demandées via les directives SLURM (`#SBATCH`) ?"
  - "Quelles méthodes sont suggérées dans le texte pour améliorer les performances de Samtools au-delà de son fonctionnement par défaut sur un seul cœur ?"
  - "Quel indicateur permet d'activer le multithreading directement au sein des commandes Samtools ?"
  - "Quel outil externe est suggéré pour exécuter des opérations sur plusieurs fichiers SAM de manière simultanée ?"
  - "Quel paramètre de configuration faut-il ajuster dans le script si le nombre de fichiers d'entrée varie ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Description
Samtools est un ensemble de programmes permettant d'interagir avec des données de séquençage à haut débit. Samtools est étroitement lié à BCFtools et HTSlib. Au besoin, [consultez la documentation](https://www.htslib.org/).

*   Samtools permettent la lecture, l'écriture, l'édition, l'indexation et l'affichage des formats SAM, BAM et CRAM;
*   BCFtools permettent la lecture et l'écriture des fichiers BCF2, VCF et gVCF, en plus de l'appel, le filtrage et le résumé des variants de séquences courtes de SNP et indel;
*   HTSlib est une bibliothèque en C pour lire et écrire les données de séquençage haut débit avec Samtools et BCFtools.

!!! note "Remarque"
    Nous n'abordons pas ici toutes les fonctionnalités. Pour la liste de tous les outils, [consultez Samtools](http://www.htslib.org/doc/samtools.html).

Pour charger la version par défaut, lancez la commande suivante :

```bash
module load samtools
samtools

Program: samtools (Tools for alignments in the SAM format)
Version: 1.20 (using htslib 1.20)

Usage:   samtools <command> [options]
```

Pour plus d'information sur la commande `module` et sur comment trouver d'autres versions de Samtools, voir [Utiliser des modules](../programming/utiliser_des_modules.md).

## Utilisation

Samtools propose divers outils pour manipuler les alignements dans les formats SAM et BAM. La tâche la plus courante consiste à convertir vos fichiers SAM (*Sequence Alignment/Map*) en fichiers BAM (version binaire de SAM). Les fichiers BAM sont des versions compressées des fichiers SAM et sont beaucoup plus compacts. Ils sont faciles à manipuler et un excellent choix pour le stockage de grands alignements de séquences nucléotidiques.

CRAM est un format plus récent pour le même type de données et offre encore plus de compression.

### Conversion de SAM à BAM

Avant la conversion, vérifiez si votre fichier BAM a un en-tête avec le caractère « @ ». Vous pouvez vérifier ceci avec la commande `view`.

```bash
samtools view -H my_sample.sam
```

Si le fichier SAM a un en-tête, vous pouvez utiliser l'une des options suivantes pour le convertir en BAM.

```bash
samtools view -bo my_sample.bam my_sample.sam
samtools view -b my_sample.sam -o my_sample.bam
```

Si les en-têtes sont absents, vous pouvez utiliser le fichier de référence FASTA pour mapper les lectures.

```bash
samtools view -bt ref_seq.fa -o my_sample.bam my_sample.sam
```

### Tri et indexation des fichiers BAM

Vous devrez peut-être trier et indexer les fichiers BAM pour plusieurs applications que vous utiliserez par la suite.

```bash
samtools sort my_sample.bam -o my_sample_sorted.bam
samtools index my_sample_sorted.bam
```

Les fichiers SAM peuvent être directement convertis en fichiers BAM triés avec la fonction `|` (barre verticale) de l'interpréteur.

```bash
[name@server ~]$ samtools view -b my_sample.sam | samtools sort -o my_sample_sorted.bam
```

Un fichier BAM trié accompagné de son fichier index (extension `.bai`) est souvent un prérequis à d'autres processus tels que les appels de variantes, le décompte des fonctionnalités, etc.

### Multifil et/ou GNU parallel

Plusieurs fichiers SAM sont souvent traités simultanément.
Un script comportant une boucle est une bonne solution, comme suit :

```bash title="samtools.sh"
#!/bin/bash            
#SBATCH --cpus-per-task 1
#SBATCH --mem-per-cpu=4G      
#SBATCH --time=3:00:00 

module load samtools/1.20

for FILE in *.sam
do
  time samtools view -b ${FILE} | samtools sort -o ${FILE%.*}_mt_sorted.bam
done
```

Samtools fonctionne généralement sur un seul cœur par défaut, mais dans certains cas il est possible d'améliorer la performance en travaillant sur plusieurs cœurs ou avec GNU Parallel.

Samtools peut travailler sur plusieurs cœurs (*multithreading*) avec l'indicateur `-@`.

```bash title="samtools_multithreading.sh"
#!/bin/bash
#SBATCH --cpus-per-task 4
#SBATCH --mem-per-cpu=4G
#SBATCH --time=3:00:00

module load samtools/1.20

for FILE in *.sam
do
  time samtools view -@ ${SLURM_CPUS_PER_TASK} -b ${FILE} | samtools sort -o ${FILE%.*}_mt_sorted.bam
done
```

Un autre moyen de travailler sur plusieurs cœurs est d'utiliser GNU Parallel pour traiter plusieurs fichiers simultanément.

```bash title="samtools_gnuparallel.sh"
#!/bin/bash
#SBATCH --cpus-per-task 4
#SBATCH --mem-per-cpu=4G
#SBATCH --time=3:00:00

module load samtools/1.20

find . -name "*.sam" | parallel -j ${SLURM_CPUS_PER_TASK} "time samtools view -bS {} | samtools sort -o {.}_mt_sorted.bam"
```

Le script ci-dessus exécutera `view` et `sort` sur quatre fichiers SAM simultanément. Si vous avez plusieurs fichiers d'entrée, modifiez la requête `--cpus-per-task`.