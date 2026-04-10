---
title: "MetaPhlAn/fr"
slug: "metaphlan"
lang: "fr"

source_wiki_title: "MetaPhlAn/fr"
source_hash: "08c84908bdb1d2104941243e73c02832"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T08:30:18.922226+00:00"

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

[MetaPhlAn](https://github.com/biobakery/MetaPhlAn) est un outil informatique permettant de profiler la composition des communautés microbiennes (bactéries, archées et eucaryotes) à partir de données de séquençage métagénomique (c'est-à-dire non 16S) au niveau de l'espèce. Avec StrainPhlAn, il est possible d'effectuer un profilage microbien précis au niveau de la souche. Bien que la pile logicielle de nos grappes contienne des modules pour quelques versions plus anciennes (2.2.0 et 2.8), nous attendons désormais des utilisateurs qu'ils installent les versions récentes à l'aide d'un [environnement virtuel Python](python/creer-etd-utiliser-un-environnement-virtuel.md).

Pour plus d'information, voir [le site wiki de MetaPhlan](https://github.com/biobakery/MetaPhlAn/wiki/MetaPhlAn-4).

## Wheels disponibles
Pour connaître les wheels disponibles, utilisez la commande `avail_wheels`.

```bash
avail_wheels metaphlan --all-versions
```

```text
name       version    python    arch
---------  ---------  --------  -------
MetaPhlAn  4.0.3      py3       generic
MetaPhlAn  3.0.7      py3       generic
```

## Télécharger les bases de données
MetaPhlAn exige qu'un ensemble de bases de données soit téléchargé dans `$SCRATCH`.

!!! warning "Important"
    La base de données doit se trouver dans `$SCRATCH`.

Téléchargez les bases de données à partir du [Segatalab FTP](http://cmprod1.cibio.unitn.it/biobakery4/metaphlan_databases).

1.  À partir d'un nœud de connexion, créez le répertoire pour les données.
    ```bash
    export DB_DIR=$SCRATCH/metaphlan_databases
    mkdir -p $DB_DIR
    cd $DB_DIR
    ```

2.  Téléchargez les données.
    ```bash
    parallel wget ::: http://cmprod1.cibio.unitn.it/biobakery4/metaphlan_databases/mpa_vJan21_CHOCOPhlAnSGB_202103.tar http://cmprod1.cibio.unitn.it/biobakery4/metaphlan_databases/mpa_vJan21_CHOCOPhlAnSGB_202103_marker_info.txt.bz2 http://cmprod1.cibio.unitn.it/biobakery4/metaphlan_databases/mpa_vJan21_CHOCOPhlAnSGB_202103_species.txt.bz2
    ```

    !!! note "Remarque"
        Cette étape doit se faire à partir d'un nœud de connexion et non à partir d'un nœud de calcul.

3.  Faites l'extraction des données téléchargées en utilisant par exemple une tâche interactive.
    ```bash
    salloc --account=<your account> --cpus-per-task=2 --mem=10G
    ```
    Décompressez les bases de données.
    ```bash
    tar -xf mpa_vJan21_CHOCOPhlAnSGB_202103.tar
    parallel bunzip2 ::: *.bz2
    ```

## Utiliser MetaPhlAn
Une fois que les fichiers des bases de données ont été téléchargés et extraits, vous pouvez soumettre une tâche. Le script suivant peut servir d'exemple :

```sh title="metaphlan-job.sh"
#!/bin/bash

#SBATCH --account=def-someuser
#SBATCH --time=01:00:00
#SBATCH --cpus-per-task=4        # Number of cores
#SBATCH --mem=15G                # requires at least 15 GB of memory

# Chargez les modules requis.
module load gcc blast samtools bedtools bowtie2 python/3.14

# Allez au scratch
cd $SCRATCH

DB_DIR=$SCRATCH/metaphlan_databases

# Générez votre environnement virtuel dans $SLURM_TMPDIR
virtualenv --no-download ${SLURM_TMPDIR}/env
source ${SLURM_TMPDIR}/env/bin/activate

# Installez metaphlan et ses dépendances.
pip install --no-index --upgrade pip
pip install --no-index metaphlan==X.Y.Z  # EDIT: the required version here, e.g. 4.0.3

# Réutilisez le nombre de cœurs (--cpus-per-task=4) alloués à votre tâche.
# Il est important d'utiliser --index et --bowtie2db pour que MetaPhlAn soit exécuté à l'intérieur de la tâche.
metaphlan metagenome.fastq --input_type fastq -o profiled_metagenome.txt --nproc $SLURM_CPUS_PER_TASK --index mpa_vJan21_CHOCOPhlAnSGB_202103 --bowtie2db $DB_DIR --bowtie2out metagenome.bowtie2.bz2
```

Soumettez ensuite la tâche à l'ordonnanceur.
```bash
sbatch metaphlan-job.sh