---
title: "GATK/fr"
slug: "gatk"
lang: "fr"

source_wiki_title: "GATK/fr"
source_hash: "78ca26964505ed572b582a86a389e4bc"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:14:10.860254+00:00"

tags:
  - bioinformatics
  - software

keywords:
  - "plusieurs cœurs"
  - "mémoire"
  - "base de données"
  - "analyse bioinformatique"
  - "OutOfMemoryError"
  - "${SLURM_TMPDIR}"
  - "script SBATCH"
  - "utilisation sur grappes"
  - "image Docker"
  - "image"
  - "opérations d'entrée-sortie"
  - "Java heap space"
  - "espace de stockage local"
  - "étiquette RG"
  - "GATK"
  - "charger un module"
  - "Spark"
  - "séminaire web"
  - "système de fichiers"
  - "séquençage haut débit"
  - "Apptainer"

questions:
  - "À quoi sert principalement la boîte d'outils GATK dans le domaine de la bioinformatique ?"
  - "Comment doit-on procéder pour trouver et charger une version spécifique du module GATK sur les grappes de calcul ?"
  - "Quelles sont les meilleures pratiques recommandées pour optimiser l'utilisation de GATK et la gestion des fichiers temporaires lors de l'exécution de tâches sur les grappes ?"
  - "Comment doit-on exécuter les versions de GATK antérieures à la version 4 puisqu'elles n'offrent pas la commande standard ?"
  - "Comment fonctionne la gestion des cœurs multiples dans GATK et quelle est la particularité des outils utilisant Apache Spark ?"
  - "Quelle est la procédure pour construire et exécuter une image Apptainer de GATK afin de contourner les erreurs liées aux modules standards ?"
  - "Quelle est la procédure recommandée concernant l'emplacement de la base de données lors de l'exécution de tâches ?"
  - "Pourquoi l'espace de stockage `${SLURM_TMPDIR}` est-il plus rapide pour les opérations d'entrée-sortie ?"
  - "Comment cette pratique permet-elle de protéger le système de fichiers et de ne pas perturber les autres utilisateurs ?"
  - "Comment construire une image Apptainer pour GATK à partir de sa version Docker ?"
  - "Quelles commandes doivent être incluses dans un script SBATCH pour exécuter un outil GATK via Apptainer ?"
  - "Où peut-on trouver des informations supplémentaires et une présentation vidéo sur l'utilisation d'Apptainer ?"
  - "Comment peut-on ajouter une étiquette de groupe de lecture (Read Group) à un fichier BAM en utilisant GATK/PICARD ?"
  - "Quelles sont les solutions recommandées pour résoudre l'erreur \"java.lang.OutOfMemoryError: Java heap space\" lors de l'exécution des sous-programmes GATK ?"
  - "Comment empêcher les applications GATK/JAVA d'utiliser plus de ressources (mémoire, CPU, fils) que ce qui a été initialement demandé ?"
  - "Comment peut-on ajouter une étiquette de groupe de lecture (Read Group) à un fichier BAM en utilisant GATK/PICARD ?"
  - "Quelles sont les solutions recommandées pour résoudre l'erreur \"java.lang.OutOfMemoryError: Java heap space\" lors de l'exécution des sous-programmes GATK ?"
  - "Comment empêcher les applications GATK/JAVA d'utiliser plus de ressources (mémoire, CPU, fils) que ce qui a été initialement demandé ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Le [Genome Analysis Toolkit (GATK)](https://bio.tools/gatk) est une boîte à outils conçue pour l'analyse bioinformatique des données de séquençage haut débit (HTS) et du format Variant Call (VCF). Elle est beaucoup employée pour la découverte des variantes courtes des lignées germinales à partir de données de séquençage du génome entier et de l'exome. GATK est à l'avant-plan de la recherche génomique en termes de [meilleures pratiques](https://gatk.broadinstitute.org/hc/en-us/sections/360007226651-Best-Practices-Workflows).

## Charger un module

Plusieurs versions sont disponibles sur nos grappes. Pour obtenir l'information sur la version, [lancez la commande](utiliser-des-modules.md) :

```bash
module spider gatk
```

Vous obtiendrez de l'information sur GATK et les versions :

```text
gatk/3.7
gatk/3.8
gatk/4.0.0.0
gatk/4.0.8.1
gatk/4.0.12.0
gatk/4.1.0.0
gatk/4.1.2.0
gatk/4.1.7.0
gatk/4.1.8.0
gatk/4.1.8.1
gatk/4.2.2.0
gatk/4.2.4.0
gatk/4.2.5.0
```

Pour plus d'information sur une version particulière, utilisez :

```bash
module spider gatk/4.1.8.1
```

Comme vous pouvez voir, seul le module `StdEnv/2020` est prérequis; chargez-le avec :

```bash
module load StdEnv/2020 gatk/4.1.8.1
```

Ou, puisque `StdEnv/2020` est chargé par défaut, simplement :

```bash
module load gatk/4.1.8.1
```

## Utilisation

Les versions plus récentes (>=4.0.0.0) offrent un enveloppeur (*wrapper*) pour les exécutables Java (.jar). En chargeant les modules GATK, vous obtiendrez la plupart des variables d'environnement nécessaires.

La commande `module spider` fournit des renseignements sur l'utilisation ainsi que des exemples.

```text
      Usage
      =====
      gatk [--java-options "-Xmx4G"] ToolName [GATK args]
      
      
      Examples
      ========
      gatk --java-options "-Xmx8G" HaplotypeCaller -R reference.fasta -I input.bam -O output.vcf
```

Dans cet exemple, vous avez probablement remarqué que certains arguments sont directement passés à Java avec les `--java-options`, comme la mémoire maximale du tas (*heap memory*) de `-Xmx8G` réservée pour l'instance.

!!! tip
    Nous recommandons de **toujours** utiliser `-DGATK_STACKTRACE_ON_USER_EXCEPTION=true` puisque vous obtiendrez plus d'information pour le débogage en cas d'échec du programme. Assurez-vous que toutes les options passées par `--java-options` sont entre guillemets (").

### Utilisation sur nos grappes

!!! tip "Optimisation des fichiers temporaires et des E/S"
    Pour les tâches `sbatch`, nous recommandons l'option `--tmp-dir` avec la configuration `${SLURM_TMPDIR}`; les fichiers temporaires sont alors redirigés vers le stockage local.

    Si vous utilisez `GenomicsDBImport`, assurez-vous que l'option `--genomicsdb-shared-posixfs-optimizations` est activée; ceci peut optimiser l'utilisation et la performance avec des systèmes de fichiers partagés Posix comme NFS et Lustre. Si ce n'est pas possible ou si vous utilisez GNU Parallel pour exécuter plusieurs intervalles simultanément, copiez votre base de données dans `${SLURM_TMPDIR}` et lancez-y l'exécution afin d'éviter que les opérations d'entrée-sortie perturbent le système de fichiers; comme `${SLURM_TMPDIR}` est un espace de stockage local, il est plus rapide et les opérations d'entrées-sortie n'affectent pas les autres utilisateurs et utilisatrices.

### Versions antérieures à GATK 4

Les versions antérieures n'offrent pas la commande `gatk`; invoquez plutôt le fichier `jar`.

```text
java -jar GenomeAnalysisTK.jar PROGRAM OPTIONS
```

GenomeAnalysisTK.jar doit se trouver dans PATH. Sur nos grappes, les variables d'environnement `$EBROOTPICARD` pour Picard (dans GATK >= 4) et `$EBROOTGATK` pour GATK contiennent le chemin vers le fichier jar. Ainsi, pour appeler GATK <= 3, lancez :

```bash
module load nixpkgs/16.09 gatk/3.8
java -jar "${EBROOTGATK}"/GenomeAnalysisTK.jar PROGRAM OPTIONS
```

Pour les particularités de GATK <= 3, voyez [le guide GATK3](https://github.com/broadinstitute/gatk-docs/tree/master/gatk3-tooldocs).

### Utilisation avec plusieurs cœurs

La plupart des outils GATK (>=4) ne peuvent pas utiliser plusieurs cœurs par défaut; vous devriez donc demander un seul cœur quand vous faites appel à ce type d'outil. Pour certains calculs, quelques outils utilisent des fils (par exemple `Mutect2` avec `--native-pair-hmm-threads`) et donc vous pouvez demander plus de CPU, dans certains cas jusqu'à 4 fils. Quelques commandes Spark sont cependant disponibles avec GATK4.

> **Spark n'est pas utilisé par tous les outils GATK.**
>
> Les outils qui utilisent GATK le mentionnent dans leur documentation respective.
>
> *   Certains outils GATK ont des versions qui supportent Spark et d'autres non. Les noms des versions pouvant travailler avec Spark ont le suffixe *spark*. Plusieurs de ces versions sont encore au stade expérimental, mais nous prévoyons éventuellement n'offrir qu'une version par outil.
>
> *   Certains outils GATX n'ont qu'une version qui supporte Spark; leurs noms n'ont pas le suffixe *spark*.
>
> --- tiré de [GATK et SPARK](https://gatk.broadinstitute.org/hc/en-us/articles/360035890591-)

Avec les commandes qui utilisent Spark, vous pouvez demander plusieurs CPU. Veuillez indiquer le nombre exact de CPU dans la commande Spark; par exemple, si vous demandez 10 CPU, utilisez `--spark-master local[10]` plutôt que `--spark-master local[*]`. Pour travailler en multinœuds, vous devez d'abord [déployer une grappe Spark](apache-spark.md) puis configurer les variables appropriées dans la commande GATK.

## Travailler avec Apptainer

Si vous obtenez des erreurs comme [IllegalArgumentException](https://gatk.broadinstitute.org/hc/en-us/community/posts/360067054832-GATK-4-1-7-0-error-java-lang-IllegalArgumentException-malformed-input-off-17635906-length-1) dans votre utilisation des modules installés sur nos grappes, nous vous recommandons d'essayer de travailler autrement en passant par [Apptainer](apptainer.md).

Vous pouvez trouver [une image Docker ici](https://hub.docker.com/r/broadinstitute/gatk) ainsi que [d'autres versions sur cette page](https://hub.docker.com/r/broadinstitute/gatk/tags). Vous devez d'abord construire une image Apptainer à partir d'une image Docker. Pour obtenir les plus récentes versions, lancez les commandes suivantes sur la grappe :

```bash
module load apptainer
apptainer build gatk.sif docker://broadinstitute/gatk
```

ou, pour une [version spécifique](https://hub.docker.com/r/broadinstitute/gatk/tags) :

```bash
module load apptainer
apptainer build gatk_VERSION.sif docker://broadinstitute/gatk:VERSION
```

Dans votre [script SBATCH](running-jobs.md), vous devriez utiliser quelque chose comme :

```bash
module load apptainer
apptainer exec -B /home -B /project -B /scratch -B /localscratch \
    <path to the image>/gatk.sif gatk [--java-options "-Xmx4G"] ToolName [GATK args]
```

Pour plus d'information sur Apptainer, visionnez ce [séminaire web](https://www.youtube.com/watch?v=bpmrfVqBowY).

## Foire aux questions

### Ajouter une étiquette RG (*read group*) dans un fichier bam

Pour ajouter une étiquette (nommée ici *tag*) au fichier *input.bam*, vous pouvez utiliser la commande GATK/PICARD [AddOrReplaceReadGroups](https://gatk.broadinstitute.org/hc/en-us/articles/360037226472-AddOrReplaceReadGroups-Picard-) :

```bash
gatk  AddOrReplaceReadGroups \
    -I input.bam \
    -O output.bam \
    --RGLB tag \
    --RGPL ILLUMINA \
    --RGPU tag \
    --RGSM tag \
    --SORT_ORDER 'coordinate' \
    --CREATE_INDEX true
```

Ceci suppose que votre fichier en entrée est trié selon les coordonnées et qu'un index est généré avec le résultat annoté (`--CREATE_INDEX true`).

### Message `java.lang.OutOfMemoryError: Java heap space`

Les sous-programmes GATK nécessitent souvent plus de mémoire pour traiter vos fichiers. Si vous n'utilisiez pas la commande `-Xms`, ajoutez-la à `--java-options`. Par exemple, vous lanceriez :

```bash
gatk MarkDuplicates \
    -I input.bam \
    -O marked_duplicates.bam \
    -M marked_dup_metrics.txt 
```

Si vous obtenez l'erreur `java.lang.OutOfMemoryError: Java heap space`, essayez ceci :

```bash
gatk MarkDuplicates \
    --java-options "-Xmx8G -DGATK_STACKTRACE_ON_USER_EXCEPTION=true" \
    -I input.bam \
    -O marked_duplicates.bam \
    -M marked_dup_metrics.txt 
```

Si ça ne fonctionne toujours pas, essayez d'augmenter la mémoire jusqu'à ce que vous trouviez la capacité nécessaire à votre ensemble de données.

!!! warning
    **N'oubliez pas** de demander suffisamment de mémoire quand vous travaillez dans nos systèmes.

Pour en apprendre davantage au sujet du tas avec Java, [lisez ceci](https://plumbr.io/outofmemoryerror/java-heap-space).

### Augmenter la mémoire pour le tas donne toujours l'erreur `java.lang.OutOfMemoryError: Java heap space`

Dans certains cas, le fait d'augmenter la mémoire ne résout pas le problème. Ceci se produit souvent avec des organismes qui ne sont pas des modèles et quand vos références sont trop échafaudées. Nous vous recommandons alors de supprimer les niveaux moins importants et de créer des sous-ensembles pour vos références. Par conséquent, vous devrez effectuer plusieurs MAPS et exécuter les pipelines dans chacun des sous-ensembles.

!!! warning "Approche de sous-ensembles"
    **Cette approche ne fonctionne pas pour tous les pipelines**, donc révisez bien les résultats obtenus. La boîte à outils GATK est conçue en fonction du génome humain; plusieurs paramètres et pipelines doivent être adaptés pour d'autres organismes.

### Utiliser plus de ressources que ce qui a été demandé

Les applications GATK/JAVA utilisent souvent plus de mémoire ou de CPU et de fils que ce qui a été demandé. Ceci est souvent dû au processus de *Garbage Collection* de Java. Pour contourner ceci, vous pouvez ajouter `-XX:ConcGCThreads=1` à l'argument `--java-options`.

### Foire aux questions de GATK

Voir [Troubleshooting GATK4 Issues](https://gatk.broadinstitute.org/hc/en-us/sections/360007226791-Troubleshooting-GATK4-Issues).

## Références

*   [Site web GATK](https://gatk.broadinstitute.org/hc/en-us)
*   [GATK et SPARK](https://gatk.broadinstitute.org/hc/en-us/articles/360035532012-Parallelism-Multithreading-Scatter-Gather)
*   [Faire fonctionner les outils GATK plus rapidement](https://gatk.broadinstitute.org/hc/en-us/articles/360035889611-How-can-I-make-GATK-tools-run-faster-)