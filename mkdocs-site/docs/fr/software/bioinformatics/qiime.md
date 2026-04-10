---
title: "QIIME/fr"
tags:
  - bioinformatics
  - user-installed-software

keywords:
  []
---

QIIME (pour <i>Quantitative Insights Into [Microbial Ecology](https://fr.wikipedia.org/wiki/%C3%89cologie_microbienne)</i>) est un pipeline bioinformatique open source pour l’analyse de [microbiomes](https://fr.wikipedia.org/wiki/Microbiome). À partir de données brutes de séquençage d’ADN générées par des plateformes comme [Illumina](https://www.illumina.com/), QIIME produit des graphiques et statistiques de haute qualité pour, entre autres, le démultiplexage, le filtrage de qualité, la sélection d’OTU, l’attribution taxonomique, la reconstruction phylogénétique et l’analyse de la diversité.

<b>Remarque </b>: QIIME 2 a remplacé QIIME 1 en janvier 2018; la version 1 n'est plus supportée.

<b>Remarque </b>: Depuis février 2020, il n'est pas possible d'installer QIIME avec Anaconda ou Miniconda sur nos grappes en raison de plusieurs problèmes dus aux environnements Conda.</b>

## Module pour QIIME2 
QIIME2 est disponible en chargeant un module qui enveloppe un conteneur. Pour connaître les versions disponibles, lancez

```bash
module spider qiime2
```

 

Une fois le module chargé, vous pouvez lancer

```bash
qiime --help
```

### Exemple 
Voici un exemple simple d'un script pour soumettre une tâche&nbsp;:

**`qiime2-example.sh`**
```bash
#!/bin/bash
#SBATCH --account=def-someprof    # adjust this to match the accounting group you are using to submit jobs
#SBATCH --mem-per-cpu=4096M       # adjust this according to the memory you need
#SBATCH --cpus-per-task=1         # adjust this according to the number of core you need
#SBATCH --time=08:00:00           # adjust this to match the walltime of your job

module load StdEnv/2023 qiime2/2024.5

# Change directory to where our data live
cd $SCRATCH

# https://apptainer.org/docs/user/main/appendix.html
# Bind source:destination, bind current directory to /data
export APPTAINER_BIND=$PWD:/data
# Set the working directory to be used for /tmp, /var/tmp and $HOME
export APPTAINER_WORKDIR=$SLURM_TMPDIR

# run with /data mounted
qiime tools import --input-path /data/input.fasta --output-path /data/output.fasta.qza --type 'FeatureData[Sequence]'
```

## Installation 
L’installation peut se faire en utilisant [Apptainer](apptainer-fr.md) ou [EasyBuild](easybuild-fr.md). Il est préférable d'utiliser Apptainer pour éviter que plusieurs milliers de fichiers soient générés dans votre répertoire /home, ce qui risquerait de dépasser le quota sur le nombre de fichiers.

### Utilisation avec Apptainer 

Les développeurs de QIIME2 publient des images sur [Quay.io](https://quay.io/organization/qiime2).
Pour utiliser ces images avec nos ressources, il faut d'abord  créer une image Apptainer comme suit&nbsp;:

```bash
apptainer build qiime2-2021.11.sif docker://quay.io/qiime2/core:2021.11
```

Cette étape du build pourrait prendre plus d'une heure, mais il ne faut l'effectuer qu'une seule fois. Sauvegardez le fichier image (dans notre exemple `qiime2-2021.11.sif`) pour pouvoir le réutiliser plus tard. 

Exécutez ensuite votre programme comme décrit dans la [page Apptainer](apptainer-fr.md). De façon générale, chaque commande QIIME est exécutée dans un énoncé `apptainer exec` comme suit%nbsp;:

```bash
apptainer exec qiime2-2021.11.sif <your QIIME command>
```

Votre script [SBATCH](running-jobs-fr.md) ressemblerait à

<pre>
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
</pre>

Notez qu'il est important d'utiliser l'option [bind](apptainer-fr#bind_mount.md) (`-B`) avec chacun des répertoires avec lesquels vous voulez travailler quand des programmes sont exécutés dans votre conteneur. Pour plus d'information, voyez ce [webinaire Apptainer](https://www.youtube.com/watch?v=bpmrfVqBowY).

La première fois que des données sont importées en format QIIME, vous pourriez recevoir un message semblable à
<pre>
Timezone offset does not match system offset: 0 != -18000. Please, check your config files.
</pre>
Vous pouvez contourner ceci en définissant un fuseau horaire avant d'invoquer Apptainer, comme suit&nbsp;:

```bash

```
'UTC'
|apptainer exec qiime2-2021.11.sif qiime tools import ...
}}

=Références =

[Site web QIIME](http://qiime.org/)

<!--[Getting started with Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html)
-->