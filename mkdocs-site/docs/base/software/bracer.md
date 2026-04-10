---
title: "BraCeR"
slug: "bracer"
lang: "base"

source_wiki_title: "BraCeR"
source_hash: "f51acda1ca5c530b62fb3a22b789264d"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T04:59:39.576726+00:00"

tags:
  - software
  - bioinformatics

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

[BraCeR](https://github.com/Teichlab/bracer) - reconstruction of B cell receptor sequences from single-cell RNA-seq data.

## Installation
The following will install parts of BraCeR in the following locations:

*   Content of the BraCeR Git-repository: `$HOME/bracer`
*   Virtual Python environment: `$HOME/venv_bracer`
*   Transcriptome databases for Kallisto: `/scratch/$USER/GRCh38` and `/scratch/$USER/GRCm38`

However, it could also be structured differently. Please refer to our [Storage and file management](storage-and-file-management.md#storage_types) page for a comparison of the different storage types available.

```bash
# BraCeR installation instructions as of August 2022.
# Get bracer
cd ~/
git clone https://github.com/Teichlab/bracer.git

# load modules
module load StdEnv/2020
module load python/3.8
module load gcc/9.3.0 bowtie2/2.4.1 bowtie/1.3.0 trinity/2.14.0 samtools/1.15.1
module load igblast/1.17.0   blast+/2.12.0    kallisto/0.46.1
module load samtools/1.15.1  jellyfish/2.3.0
module load salmon/1.7.0     fastqc/0.11.9

# create a virtualenv for bracer and install dependencies
virtualenv --no-download  ~/venv_bracer
source ~/venv_bracer/bin/activate
pip install --no-index biopython==1.77
pip install --no-index -r ~/bracer/requirements.txt
pip install --no-index graphviz

# install bracer into venv
cd ~/bracer/
python setup.py install

# install Trim Galore
pusd $VIRTUAL_ENV/
## download and extract Trim Galore
wget https://github.com/FelixKrueger/TrimGalore/archive/refs/tags/0.6.7.tar.gz \
    -O TrimGalore-0.6.7.tar.gz
tar xzf TrimGalore-0.6.7.tar.gz
# tweak the Perl "hashbang":
sed -i 's&#!/usr/bin/perl&#!/usr/bin/env perl&'  TrimGalore-0.6.7/trim_galore
# copy  the trim_galore Perl-script into the virtualenv's "bin" directory:
cp  TrimGalore-0.6.7/trim_galore  $VIRTUAL_ENV/bin
popd

# Base transcriptomes for Kallisto
# adapted https://github.com/Teichlab/bracer#base-transcriptomes-for-kallisto
# to download from https://www.gencodegenes.org/
# This downloads the latest releases 41 (Human) and M30 (mouse) respectively
cd ~/scratch
mkdir GRCh38
cd GRCh38
wget https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_41/gencode.v41.transcripts.fa.gz
gunzip gencode.v41.transcripts.fa.gz
python3 ~/bracer/docker_helper_files/gencode_parse.py gencode.v27.transcripts.fa
cd ..

mkdir GRCm38
cd GRCm38
wget https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_mouse/release_M30/gencode.vM30.transcripts.fa.gz
gunzip gencode.vM30.transcripts.fa.gz
python3 ~/bracer/docker_helper_files/gencode_parse.py gencode.vM30.transcripts.fa
cd ~/
```

## Running BraCeR
!!! note "Configuration"
    Make sure to replace `USERNAME` with your username in the `bracer.conf`:

### bracer.conf
!!! config "bracer.conf"
    ```ini
    # Configuration file for BraCeR#

    [tool_locations]
    # paths to tools used by BraCeR for alignment, quantitation, etc
    # As all tools are in the PATH this section can be empty

    [trinity_options]
    # line below specifies maximum memory for Trinity Jellyfish component.
    # Set it appropriately for your environment.
    max_jellyfish_memory = 15G

    # undocumented option
    trinity_version = 2

    [kallisto_transcriptomes]
    Hsap = /scratch/USERNAME/GRCh38
    Mmus = /scratch/USERNAME/GRCm38

    [bracer_location]
    #Path to where BraCeR was originally installed
    bracer_path = /home/USERNAME/bracer/
    ```

### Job Script
!!! bash "bracer_job.sh"
    ```bash
    #!/bin/bash
    #SBATCH --time=0-00:30  # 30 minutes  (D-hh:mm)
    #SBATCH --cpus-per-task=4
    #SBATCH --mem-per-cpu=4000M

    module load StdEnv/2020
    module load gcc/9.3.0 bowtie2/2.4.1 bowtie/1.3.0 trinity/2.14.0 samtools/1.15.1
    module load igblast/1.17.0   blast+/2.12.0    kallisto/0.46.1
    module load samtools/1.15.1  jellyfish/2.3.0
    module load salmon/1.7.0     fastqc/0.11.9

    echo "---------------------------------------------------------------------"
    module -w 80 list
    echo "---------------------------------------------------------------------"

    source ~/venv_bracer/bin/activate

    bracer assemble  --ncores ${SLURM_CPUS_PER_TASK:-1} --config_file bracer.conf  \
           my_cell_name   ./my_output_directory/   file_001.fastq   file_002.fastq \