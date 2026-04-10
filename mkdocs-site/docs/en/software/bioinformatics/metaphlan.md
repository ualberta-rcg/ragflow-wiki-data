---
title: "MetaPhlAn/en"
slug: "metaphlan"
lang: "en"

source_wiki_title: "MetaPhlAn/en"
source_hash: "38e02414b6e681a5d7b7cd5d9a3f99ca"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T08:29:55.775561+00:00"

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

MetaPhlAn is a "computational tool for profiling the composition of microbial communities (Bacteria, Archaea and Eukaryotes) from metagenomic shotgun sequencing data (i.e. not 16S) with species-level. With StrainPhlAn, it is possible to perform accurate strain-level microbial profiling", according to its [GitHub repository](https://github.com/biobakery/MetaPhlAn). While the software stack on our clusters does contain modules for a couple of older versions (2.2.0 and 2.8) of this software, we now expect users to install recent versions using a [Python virtual environment](python.md#creating-and-using-a-virtual-environment).

For more information on how to use MetaPhlan, see their [wiki](https://github.com/biobakery/MetaPhlAn/wiki/MetaPhlAn-4)

## Available wheels
You can list available wheels using the `avail_wheels` command:

```bash
avail_wheels metaphlan --all-versions
```

```text
name       version    python    arch
---------  ---------  --------  -------
MetaPhlAn  4.0.3      py3       generic
MetaPhlAn  3.0.7      py3       generic
```

## Downloading databases
Note that MetaPhlAn requires a set of databases to be downloaded into the `$SCRATCH`.

!!! important "Important"
    The database must live in the `$SCRATCH`

Databases can be downloaded from [Segatalab FTP](http://cmprod1.cibio.unitn.it/biobakery4/metaphlan_databases).

1.  From a login node, create the data folder:
    ```bash
    export DB_DIR=$SCRATCH/metaphlan_databases
    mkdir -p $DB_DIR
    cd $DB_DIR
    ```

2.  Download the data:
    ```bash
    parallel wget ::: http://cmprod1.cibio.unitn.it/biobakery4/metaphlan_databases/mpa_vJan21_CHOCOPhlAnSGB_202103.tar http://cmprod1.cibio.unitn.it/biobakery4/metaphlan_databases/mpa_vJan21_CHOCOPhlAnSGB_202103_marker_info.txt.bz2 http://cmprod1.cibio.unitn.it/biobakery4/metaphlan_databases/mpa_vJan21_CHOCOPhlAnSGB_202103_species.txt.bz2
    ```
    Note that this step **cannot** be done from a compute node but must be done from a login node.

3.  Extract the downloaded data, for example using an interactive job:
    ```bash
    salloc --account=<your account> --cpus-per-task=2 --mem=10G
    ```
    Untar and unzip the databases:
    ```bash
    tar -xf mpa_vJan21_CHOCOPhlAnSGB_202103.tar
    parallel bunzip2 ::: *.bz2
    ```

## Running MetaPhlAn
Once the database files have been downloaded and extracted, you can submit a job. You may edit the following job submission script
according to your needs:

```sh title="metaphlan-job.sh"
#!/bin/bash

#SBATCH --account=def-someuser
#SBATCH --time=01:00:00
#SBATCH --cpus-per-task=4        # Number of cores
#SBATCH --mem=15G                # requires at least 15 GB of memory

# Load the required modules
module load gcc blast samtools bedtools bowtie2 python/3.14

# Move to the scratch
cd $SCRATCH

DB_DIR=$SCRATCH/metaphlan_databases

# Generate your virtual environment in $SLURM_TMPDIR
virtualenv --no-download ${SLURM_TMPDIR}/env
source ${SLURM_TMPDIR}/env/bin/activate

# Install metaphlan and its dependencies
pip install --no-index --upgrade pip
pip install --no-index metaphlan==X.Y.Z  # EDIT: the required version here, e.g. 4.0.3

# Reuse the number of core allocated to our job from `--cpus-per-task=4`
# It is important to use --index and --bowtie2db so that MetaPhlAn can run inside the job
metaphlan metagenome.fastq --input_type fastq -o profiled_metagenome.txt --nproc $SLURM_CPUS_PER_TASK --index mpa_vJan21_CHOCOPhlAnSGB_202103 --bowtie2db $DB_DIR --bowtie2out metagenome.bowtie2.bz2
```

Then submit the job to the scheduler:

```bash
sbatch metaphlan-job.sh