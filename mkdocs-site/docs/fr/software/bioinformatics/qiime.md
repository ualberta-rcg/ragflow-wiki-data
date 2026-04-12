---
title: "QIIME/fr"
slug: "qiime"
lang: "fr"

source_wiki_title: "QIIME/fr"
source_hash: "9cf4820a2e3a3c15c0e9aa1f8e336ce3"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:40:55.954927+00:00"

tags:
  - bioinformatics
  - user-installed-software

keywords:
  - "microbiome"
  - "séquençage d’ADN"
  - "importation de données"
  - "script SBATCH"
  - "QIIME 2"
  - "bind mount"
  - "apptainer exec"
  - "commande QIIME"
  - "qiime2-2021.11.sif"
  - "fuseau horaire"
  - "pipeline bioinformatique"
  - "Apptainer"

questions:
  - "Qu'est-ce que le pipeline bioinformatique QIIME et quelles sont ses principales fonctionnalités pour l'analyse de données ?"
  - "Comment les utilisateurs doivent-ils charger et exécuter QIIME2 sur les grappes de calcul à l'aide des modules et des variables d'environnement ?"
  - "Pourquoi est-il recommandé d'utiliser Apptainer pour l'installation de QIIME2 et comment procéder pour créer l'image requise ?"
  - "Pourquoi est-il important d'utiliser l'option bind (`-B`) lors de l'exécution de programmes dans un conteneur Apptainer ?"
  - "Comment peut-on contourner le message d'erreur lié au décalage du fuseau horaire lors de la première importation de données dans QIIME ?"
  - "Quelles sont les trois étapes de traitement de données QIIME 2 exécutées par le script Bash fourni ?"
  - "Comment peut-on conserver et réutiliser une image de conteneur telle que `qiime2-2021.11.sif` ?"
  - "Quelle est la syntaxe générale pour exécuter une commande QIIME à l'aide d'Apptainer ?"
  - "Comment doit-on structurer un script SBATCH pour lancer ces commandes Apptainer ?"
  - "Pourquoi est-il important d'utiliser l'option bind (`-B`) lors de l'exécution de programmes dans un conteneur Apptainer ?"
  - "Comment peut-on contourner le message d'erreur lié au décalage du fuseau horaire lors de la première importation de données dans QIIME ?"
  - "Quelles sont les trois étapes de traitement de données QIIME 2 exécutées par le script Bash fourni ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

QIIME (pour *Quantitative Insights Into [Microbial Ecology](https://fr.wikipedia.org/wiki/%C3%89cologie_microbienne)*) est un pipeline bioinformatique *open source* pour l’analyse de [microbiomes](https://fr.wikipedia.org/wiki/Microbiome). À partir de données brutes de séquençage d’ADN générées par des plateformes comme [Illumina](https://www.illumina.com/), QIIME produit des graphiques et statistiques de haute qualité pour, entre autres, le démultiplexage, le filtrage de qualité, la sélection d’OTU, l’attribution taxonomique, la reconstruction phylogénétique et l’analyse de la diversité.

!!! note
    QIIME 2 a remplacé QIIME 1 en janvier 2018; la version 1 n'est plus supportée.

!!! note
    Depuis février 2020, il n'est pas possible d'installer QIIME avec Anaconda ou Miniconda sur nos grappes en raison de plusieurs problèmes dus aux environnements Conda.

## Module pour QIIME2

QIIME2 est disponible en chargeant un module qui encapsule un conteneur. Pour connaître les versions disponibles, lancez :

```bash
module spider qiime2
```

Une fois le module chargé, vous pouvez lancer :

```bash
qiime --help
```

!!! note
    Étant donné que la commande `qiime` appelle un conteneur, il se peut que vous deviez définir la variable d'environnement `APPTAINER_BIND` pour attacher des répertoires particuliers dans ce conteneur pour avoir accès à vos données, par exemple `APPTAINER_BIND=/home qiime ...`.

### Exemple

Voici un exemple simple d'un script pour soumettre une tâche :

```bash
# qiime2-example.sh
#!/bin/bash
#SBATCH --account=def-someprof    # ajustez-le pour qu'il corresponde au groupe comptable que vous utilisez pour soumettre des tâches
#SBATCH --mem-per-cpu=4096M       # ajustez-le en fonction de la mémoire dont vous avez besoin
#SBATCH --cpus-per-task=1         # ajustez-le en fonction du nombre de cœurs dont vous avez besoin
#SBATCH --time=08:00:00           # ajustez-le pour qu'il corresponde au temps d'exécution de votre tâche

module load StdEnv/2023 qiime2/2024.5

# Changez de répertoire pour l'endroit où se trouvent nos données.
cd $SCRATCH

# https://apptainer.org/docs/user/main/appendix.html
# Lie source:destination, lie le répertoire courant à /data
export APPTAINER_BIND=$PWD:/data
# Définissez le répertoire de travail à utiliser pour /tmp, /var/tmp et $HOME
export APPTAINER_WORKDIR=$SLURM_TMPDIR

# exécutez avec /data monté
qiime tools import --input-path /data/input.fasta --output-path /data/output.fasta.qza --type 'FeatureData[Sequence]'
```

## Installation

L’installation peut se faire en utilisant [Apptainer](../containers/apptainer.md) ou [EasyBuild](../../programming/easybuild.md). Il est préférable d'utiliser Apptainer pour éviter que plusieurs milliers de fichiers soient générés dans votre répertoire `/home`, ce qui risquerait de dépasser le quota sur le nombre de fichiers.

### Utilisation avec Apptainer

Les développeurs de QIIME2 publient des images sur [Quay.io](https://quay.io/organization/qiime2).
Pour utiliser ces images avec nos ressources, il faut d'abord créer une image Apptainer comme suit :

```bash
module load apptainer
apptainer build qiime2-2021.11.sif docker://quay.io/qiime2/core:2021.11
```

Cette étape du *build* pourrait prendre plus d'une heure, mais il ne faut l'effectuer qu'une seule fois. Sauvegardez le fichier image (dans notre exemple `qiime2-2021.11.sif`) pour pouvoir le réutiliser plus tard.

Exécutez ensuite votre programme comme décrit dans la [page Apptainer](../containers/apptainer.md). De façon générale, chaque commande QIIME est exécutée dans un énoncé `apptainer exec` comme suit :

```bash
apptainer exec qiime2-2021.11.sif <votre commande QIIME>
```

Votre script [SBATCH](../../running-jobs/running_jobs.md) ressemblerait à :

```bash
#!/bin/bash
#SBATCH --time=15:00:00
#SBATCH --account=def-someuser

apptainer exec -B $PWD:/home -B /scratch/someuser:/outputs \
  -B /project/def-somePI/someuser/path/to/inputs:/inputs qiime2-2021.11.sif \
  qiime tools import --type 'FeatureData[Sequence]' \
  --input-path /inputs/some_fastafile.fa \
  --output-path /outputs/some_output_feature.qza

apptainer exec -B $PWD:/home -B /scratch/someuser:/outputs \
  -B /project/def-somePI/someuser/path/to/inputs:/inputs qiime2-2021.11.sif \
  qiime tools import \
  --type 'FeatureData[Taxonomy]' \
  --input-format HeaderlessTSVTaxonomyFormat \
  --input-path /inputs/some_taxonomy_file.tax \
  --output-path /outputs/some_output_ref-taxonomy.qza

apptainer exec -B $PWD:/home -B /scratch/someuser:/outputs \
  -B /project/def-somePI/someuser/path/to/inputs:/inputs qiime2-2021.11.sif \
  qiime feature-classifier fit-classifier-naive-bayes \
  --i-reference-reads  /outputs/some_output_feature.qza \
  --i-reference-taxonomy /outputs/some_output_ref-taxonomy.qza \
  --o-classifier /outputs/some_output_classifier.qza
```

Notez qu'il est important d'utiliser l'option [bind](../containers/apptainer.md) (`-B`) avec chacun des répertoires avec lesquels vous voulez travailler quand des programmes sont exécutés dans votre conteneur. Pour plus d'information, voyez ce [webinaire Apptainer](https://www.youtube.com/watch?v=bpmrfVqBowY).

La première fois que des données sont importées en format QIIME, vous pourriez recevoir un message semblable à :

```
Timezone offset does not match system offset: 0 != -18000. Please, check your config files.
```

Vous pouvez contourner ceci en définissant un fuseau horaire avant d'invoquer Apptainer, comme suit :

```bash
export TZ='UTC'
apptainer exec qiime2-2021.11.sif qiime tools import ...
```

## Références

[Site web QIIME](http://qiime.org/)