---
title: "AlphaFold2"
slug: "alphafold2"
lang: "base"

source_wiki_title: "AlphaFold2"
source_hash: "80f39ce5177edbd5d53cb6929821d13a"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:02:18.226698+00:00"

tags:
  - software

keywords:
  - "database download"
  - "SBATCH"
  - "hhblits"
  - "markup"
  - "code"
  - "run_alphafold.py"
  - "data folder"
  - "bfd_database_path"
  - "uniref90"
  - "database paths"
  - "download data"
  - "machine learning model"
  - "Submission script"
  - "virtual environment"
  - "alphafold"
  - "use_gpu_relax"
  - "translate"
  - "module dependencies"
  - "closing tag"
  - "download scripts"
  - "databases"
  - "Python virtual environment"
  - "GPU"
  - "XML"
  - "AlphaFold"
  - "protein folding"
  - "DOWNLOAD_DIR"
  - "Data transfer node"
  - "model_preset"
  - "download_pdb.sh"
  - "cpus-per-task"
  - "Directory structure"
  - "submit jobs"
  - "fasta_paths"
  - "jackhmmer"
  - "full database"
  - "$SCRATCH directory"
  - "SLURM"
  - "kalign"
  - "terminal"
  - "db_preset"
  - "troubleshooting"
  - "bash script"

questions:
  - "What is AlphaFold and how should researchers cite their use of its source code or model parameters?"
  - "What are the specific steps and dependencies required to install AlphaFold in a Python virtual environment on the cluster?"
  - "Where are the required AlphaFold databases located by default, and what directory must be used if downloading them locally?"
  - "What type of node should be used to download the AlphaFold data, and what tool is recommended to handle the long download time?"
  - "What are the expected total file sizes and main database directories for the downloaded AlphaFold datasets?"
  - "Why should users request a maximum of 8 CPU cores when submitting an AlphaFold job?"
  - "In which specific directory must the databases be stored?"
  - "What types of nodes should be used to create the data folder?"
  - "What conditions must be met before a user can proceed to download the data?"
  - "Why is the number of CPUs per task specifically limited to a maximum of 8 for this job?"
  - "How should a user adjust the walltime and memory settings to fit their specific job requirements?"
  - "What software modules and dependencies are required to be loaded before running the application?"
  - "What are the recommended SLURM resource allocations, such as CPUs, GPUs, and memory, for running an AlphaFold job?"
  - "How does the script handle the creation of the virtual environment and the installation of AlphaFold dependencies?"
  - "What specific database paths and input arguments must be configured when executing the `run_alphafold.py` command?"
  - "What are the recommended SLURM resource allocations, such as CPU cores and memory, for running an AlphaFold job according to the provided script?"
  - "How does the script handle the setup of the Python virtual environment and the installation of AlphaFold dependencies prior to execution?"
  - "Which specific biological databases and binary tool paths must be configured as arguments when executing the run_alphafold.py command?"
  - "How are the input sequence files and the output directory specified in the `run_alphafold.py` command?"
  - "What arguments are used to configure the database and model presets for the simulation?"
  - "How do you explicitly define the file path for the BFD database within the script arguments?"
  - "What specific bioinformatics binary tools and databases are being configured with file paths in this command snippet?"
  - "What is the purpose of setting the `--max_template_date` parameter to 2020-05-14 in this execution?"
  - "How does the `--use_gpu_relax=False` flag impact the hardware utilization of the pipeline?"
  - "What are the recommended SLURM resource allocations, such as CPUs and GPUs, for running an AlphaFold job?"
  - "How does the provided bash script set up the virtual environment and execute the AlphaFold Python script?"
  - "What are the three proposed solutions for resolving a \"Broken pipe\" error when downloading the AlphaFold database?"
  - "What is the alternative method provided for downloading the full database?"
  - "What specific actions must a user perform in the terminal to visualize all available download scripts?"
  - "Which example script is mentioned for manually downloading sections of the database?"
  - "What is the primary function of the `</translate>` closing tag within a markup or programming context?"
  - "How do parsers or translation systems process the content that immediately precedes this specific tag?"
  - "In which specific software frameworks or document formats is this tag typically implemented?"
  - "What is the primary function of the `</translate>` closing tag within a markup or programming context?"
  - "How do parsers or translation systems process the content that immediately precedes this specific tag?"
  - "In which specific software frameworks or document formats is this tag typically implemented?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[AlphaFold](https://deepmind.com/blog/article/alphafold-a-solution-to-a-50-year-old-grand-challenge-in-biology) is a machine learning model for the prediction of protein folding.

This page discusses how to use AlphaFold v2.0, the version that was entered in CASP14 and published in Nature.

Source code and documentation for AlphaFold can be found at their [GitHub page](https://github.com/deepmind/alphafold). Any publication that discloses findings arising from use of this source code or the model parameters should [cite](https://github.com/deepmind/alphafold#citing-this-work) the [AlphaFold paper](https://doi.org/10.1038/s41586-021-03819-2).

## Available versions
AlphaFold is available on our clusters as prebuilt Python packages (wheels). You can list available versions with `avail_wheels`.

```bash
avail_wheels alphafold --all-versions
```

```
name       version    python    arch
---------  ---------  --------  -------
alphafold  2.3.1      py3       generic
alphafold  2.3.0      py3       generic
alphafold  2.2.4      py3       generic
alphafold  2.2.3      py3       generic
alphafold  2.2.2      py3       generic
alphafold  2.2.1      py3       generic
alphafold  2.1.1      py3       generic
alphafold  2.0.0      py3       generic
```

## Installing AlphaFold in a Python virtual environment

1.  Load AlphaFold dependencies.
    ```bash
    module load StdEnv/2020 gcc/9.3.0 openmpi/4.0.3 cuda/11.4 cudnn/8.2.0 kalign/2.03 hmmer/3.2.1 openmm-alphafold/7.5.1 hh-suite/3.3.0 python/3.8
    ```
    As of July 2022, only Python 3.7 and 3.8 are supported.

2.  Create and activate a Python virtual environment.
    ```bash
    virtualenv --no-download ~/alphafold_env
    source ~/alphafold_env/bin/activate
    ```

3.  Install a specific version of AlphaFold and its Python dependencies.
    ```bash
    (alphafold_env) [name@server ~]$ pip install --no-index --upgrade pip
    (alphafold_env) [name@server ~]$ pip install --no-index alphafold==X.Y.Z
    ```
    where `X.Y.Z` is the exact desired version, for instance `2.2.4`. You can omit to specify the version in order to install the latest one available from the wheelhouse.

4.  Validate it.
    ```bash
    (alphafold_env) [name@server ~]$ run_alphafold.py --help
    ```

5.  Freeze the environment and requirements set.
    ```bash
    (alphafold_env) [name@server ~]$ pip freeze > ~/alphafold-requirements.txt
    ```

## Databases
Note that AlphaFold requires a set of databases.

The databases are available in `/cvmfs/bio.data.computecanada.ca/content/databases/Core/alphafold2_dbs/`.

AlphaFold databases on CVMFS undergo yearly updates. In January 2024, the database was updated and is accessible in folder `2024_01`.
```bash
(alphafold_env) [name@server ~]$ export DOWNLOAD_DIR=/cvmfs/bio.data.computecanada.ca/content/databases/Core/alphafold2_dbs/2024_01/
```

You can also choose to download the databases locally into your `$SCRATCH` directory.

**Important:** The databases must live in the `$SCRATCH` directory.

=== "General"

1.  From a DTN or login node, create the data folder.
    ```bash
    (alphafold_env) [name@server ~]$ export DOWNLOAD_DIR=$SCRATCH/alphafold/data
    (alphafold_env) [name@server ~]$ mkdir -p $DOWNLOAD_DIR
    ```

2.  With your modules loaded and virtual environment activated, you can download the data.
    ```bash
    (alphafold_env) [name@server ~]$ download_all_data.sh $DOWNLOAD_DIR
    ```

    Note that this step **cannot** be done from a compute node. It should be done on a data transfer node (DTN) on clusters that have them (see [Transferring data](transferring-data.md)). On clusters that have no DTN, use a login node instead. Since the download can take up to a full day, we suggest using a [terminal multiplexer](prolonging-terminal-sessions.md#terminal-multiplexers). You may encounter a `Client_loop: send disconnect: Broken pipe` error message. See [Troubleshooting](#broken-pipe-error-message) below.

=== "Graham only"

1.  Set `DOWNLOAD_DIR`.
    ```bash
    (alphafold_env) [name@server ~]$ export DOWNLOAD_DIR=/datashare/alphafold
    ```

Afterwards, the structure of your data should be similar to

=== "2.3"
```bash
(alphafold_env) [name@server ~]$ tree -d $DOWNLOAD_DIR
```

```
$DOWNLOAD_DIR/                             # ~ 2.6 TB (total)
    bfd/                                   # ~ 1.8 TB
        # 6 files
    mgnify/                                # ~ 120 GB
        mgy_clusters.fa
    params/                                # ~ 5.3 GB
        # LICENSE
        # 15 models
        # 16 files (total)
    pdb70/                                 # ~ 56 GB
        # 9 files
    pdb_mmcif/                             # ~ 246 GB
        mmcif_files/
            # 202,764 files
        obsolete.dat
    pdb_seqres/                            # ~ 237 MB
        pdb_seqres.txt
    uniprot/                               # ~ 111 GB
        uniprot.fasta
    uniref30/                              # ~ 206 GB
        # 7 files
    uniref90/                              # ~ 73 GB
        uniref90.fasta
```

=== "2.2"
```bash
(alphafold_env) [name@server ~]$ tree -d $DOWNLOAD_DIR
```

```
$DOWNLOAD_DIR/                             # Total: ~ 2.2 TB (download: 428 GB)
    bfd/                                   # ~ 1.8 TB (download: 271.6 GB)
        # 6 files.
    mgnify/                                # ~ 64 GB (download: 32.9 GB)
        mgy_clusters.fa
    params/                                # ~ 3.5 GB (download: 3.5 GB)
        # 5 CASP14 models,
        # 5 pTM models,
        # LICENSE,
        # = 11 files.
    pdb70/                                 # ~ 56 GB (download: 19.5 GB)
        # 9 files.
    pdb_mmcif/                             # ~ 206 GB (download: 46 GB)
        mmcif_files/
            # About 180,000 .cif files.
        obsolete.dat
    uniclust30/                            # ~ 87 GB (download: 24.9 GB)
        uniclust30_2018_08/
            # 13 files.
    uniref90/                              # ~ 59 GB (download: 29.7 GB)
        uniref90.fasta
```

## Running AlphaFold

!!! warning "Performance"
    You can request **at most 8 CPU cores** when running AlphaFold because it is hardcoded to not use more and does not benefit from using more.

Edit one of following submission scripts according to your needs.

=== "2.3 on CPU"
```bash title="alphafold-2.3-cpu.sh"
#!/bin/bash

#SBATCH --job-name=alphafold_run
#SBATCH --account=def-someprof    # adjust this to match the accounting group you are using to submit jobs
#SBATCH --time=08:00:00           # adjust this to match the walltime of your job
#SBATCH --cpus-per-task=8         # a MAXIMUM of 8 core, AlphaFold has no benefit to use more
#SBATCH --mem=20G                 # adjust this according to the memory you need

# Load modules dependencies.
module load StdEnv/2020 gcc/9.3.0 openmpi/4.0.3 cuda/11.4 cudnn/8.2.0 kalign/2.03 hmmer/3.2.1 openmm-alphafold/7.5.1 hh-suite/3.3.0 python/3.8

DOWNLOAD_DIR=$SCRATCH/alphafold/data   # set the appropriate path to your downloaded data
INPUT_DIR=$SCRATCH/alphafold/input     # set the appropriate path to your input data
OUTPUT_DIR=${SCRATCH}/alphafold/output # set the appropriate path to your output data

# Generate your virtual environment in $SLURM_TMPDIR.
virtualenv --no-download ${SLURM_TMPDIR}/env
source ${SLURM_TMPDIR}/env/bin/activate

# Install AlphaFold and its dependencies.
pip install --no-index --upgrade pip
pip install --no-index --requirement ~/alphafold-requirements.txt

# Edit with the proper arguments and run your commands.
# run_alphafold.py --help
run_alphafold.py \
   --fasta_paths=${INPUT_DIR}/YourSequence.fasta,${INPUT_DIR}/AnotherSequence.fasta \
   --output_dir=${OUTPUT_DIR} \
   --data_dir=${DOWNLOAD_DIR} \
   --db_preset=full_dbs \
   --model_preset=multimer \
   --bfd_database_path=${DOWNLOAD_DIR}/bfd/bfd_metaclust_clu_complete_id30_c90_final_seq.sorted_opt \
   --mgnify_database_path=${DOWNLOAD_DIR}/mgnify/mgy_clusters_2022_05.fa \
   --pdb70_database_path=${DOWNLOAD_DIR}/pdb70/pdb70 \
   --template_mmcif_dir=${DOWNLOAD_DIR}/pdb_mmcif/mmcif_files \
   --obsolete_pdbs_path=${DOWNLOAD_DIR}/pdb_mmcif/obsolete.dat \
   --pdb_seqres_database_path=${DOWNLOAD_DIR}/pdb_seqres/pdb_seqres.txt \
   --uniprot_database_path=${DOWNLOAD_DIR}/uniprot/uniprot.fasta \
   --uniref30_database_path=${DOWNLOAD_DIR}/uniref30/UniRef30_2021_03 \
   --uniref90_database_path=${DOWNLOAD_DIR}/uniref90/uniref90.fasta \
   --hhblits_binary_path=${EBROOTHHMINSUITE}/bin/hhblits \
   --hhsearch_binary_path=${EBROOTHHMINSUITE}/bin/hhsearch \
   --jackhmmer_binary_path=${EBROOTHMMER}/bin/jackhmmer \
   --kalign_binary_path=${EBROOTKALIGN}/bin/kalign \
   --max_template_date=2022-01-01 \
   --use_gpu_relax=False
```

=== "2.3 on GPU"
```bash title="alphafold-2.3-gpu.sh"
#!/bin/bash

#SBATCH --job-name=alphafold_run
#SBATCH --account=def-someprof    # adjust this to match the accounting group you are using to submit jobs
#SBATCH --time=08:00:00           # adjust this to match the walltime of your job
#SBATCH --cpus-per-task=8         # a MAXIMUM of 8 core, AlphaFold has no benefit to use more
#SBATCH --gres=gpu:1              # a GPU helps to accelerate the inference part only
#SBATCH --mem=20G                 # adjust this according to the memory you need

# Load modules dependencies.
module load StdEnv/2020 gcc/9.3.0 openmpi/4.0.3 cuda/11.4 cudnn/8.2.0 kalign/2.03 hmmer/3.2.1 openmm-alphafold/7.5.1 hh-suite/3.3.0 python/3.8

DOWNLOAD_DIR=$SCRATCH/alphafold/data   # set the appropriate path to your downloaded data
INPUT_DIR=$SCRATCH/alphafold/input     # set the appropriate path to your input data
OUTPUT_DIR=${SCRATCH}/alphafold/output # set the appropriate path to your output data

# Generate your virtual environment in $SLURM_TMPDIR.
virtualenv --no-download ${SLURM_TMPDIR}/env
source ${SLURM_TMPDIR}/env/bin/activate

# Install AlphaFold and its dependencies.
pip install --no-index --upgrade pip
pip install --no-index --requirement ~/alphafold-requirements.txt

# Edit with the proper arguments and run your commands.
# run_alphafold.py --help
run_alphafold.py \
   --fasta_paths=${INPUT_DIR}/YourSequence.fasta,${INPUT_DIR}/AnotherSequence.fasta \
   --output_dir=${OUTPUT_DIR} \
   --data_dir=${DOWNLOAD_DIR} \
   --db_preset=full_dbs \
   --model_preset=multimer \
   --bfd_database_path=${DOWNLOAD_DIR}/bfd/bfd_metaclust_clu_complete_id30_c90_final_seq.sorted_opt \
   --mgnify_database_path=${DOWNLOAD_DIR}/mgnify/mgy_clusters_2022_05.fa \
   --pdb70_database_path=${DOWNLOAD_DIR}/pdb70/pdb70 \
   --template_mmcif_dir=${DOWNLOAD_DIR}/pdb_mmcif/mmcif_files \
   --obsolete_pdbs_path=${DOWNLOAD_DIR}/pdb_mmcif/obsolete.dat \
   --pdb_seqres_database_path=${DOWNLOAD_DIR}/pdb_seqres/pdb_seqres.txt \
   --uniprot_database_path=${DOWNLOAD_DIR}/uniprot/uniprot.fasta \
   --uniref30_database_path=${DOWNLOAD_DIR}/uniref30/UniRef30_2021_03 \
   --uniref90_database_path=${DOWNLOAD_DIR}/uniref90/uniref90.fasta \
   --hhblits_binary_path=${EBROOTHHMINSUITE}/bin/hhblits \
   --hhsearch_binary_path=${EBROOTHHMINSUITE}/bin/hhsearch \
   --jackhmmer_binary_path=${EBROOTHMMER}/bin/jackhmmer \
   --kalign_binary_path=${EBROOTKALIGN}/bin/kalign \
   --max_template_date=2022-01-01 \
   --use_gpu_relax=True
```

=== "2.2 on CPU"
```bash title="alphafold-cpu.sh"
#!/bin/bash

#SBATCH --job-name=alphafold_run
#SBATCH --account=def-someprof    # adjust this to match the accounting group you are using to submit jobs
#SBATCH --time=08:00:00           # adjust this to match the walltime of your job
#SBATCH --cpus-per-task=8         # a MAXIMUM of 8 core, AlphaFold has no benefit to use more
#SBATCH --mem=20G                 # adjust this according to the memory you need

# Load modules dependencies.
module load StdEnv/2020 gcc/9.3.0 openmpi/4.0.3 cuda/11.4 cudnn/8.2.0 kalign/2.03 hmmer/3.2.1 openmm-alphafold/7.5.1 hh-suite/3.3.0 python/3.8

DOWNLOAD_DIR=$SCRATCH/alphafold/data   # set the appropriate path to your downloaded data
INPUT_DIR=$SCRATCH/alphafold/input     # set the appropriate path to your input data
OUTPUT_DIR=${SCRATCH}/alphafold/output # set the appropriate path to your output data

# Generate your virtual environment in $SLURM_TMPDIR.
virtualenv --no-download ${SLURM_TMPDIR}/env
source ${SLURM_TMPDIR}/env/bin/activate

# Install AlphaFold and its dependencies.
pip install --no-index --upgrade pip
pip install --no-index --requirement ~/alphafold-requirements.txt

# Edit with the proper arguments and run your commands.
# Note that the `--uniclust30_database_path` option below was renamed to
# `--uniref30_database_path` in 2.3.
# run_alphafold.py --help
run_alphafold.py \
   --fasta_paths=${INPUT_DIR}/YourSequence.fasta,${INPUT_DIR}/AnotherSequence.fasta \
   --output_dir=${OUTPUT_DIR} \
   --data_dir=${DOWNLOAD_DIR} \
   --model_preset=monomer_casp14 \
   --bfd_database_path=${DOWNLOAD_DIR}/bfd/bfd_metaclust_clu_complete_id30_c90_final_seq.sorted_opt \
   --mgnify_database_path=${DOWNLOAD_DIR}/mgnify/mgy_clusters_2018_12.fa \
   --pdb70_database_path=${DOWNLOAD_DIR}/pdb70/pdb70 \
   --template_mmcif_dir=${DOWNLOAD_DIR}/pdb_mmcif/mmcif_files \
   --obsolete_pdbs_path=${DOWNLOAD_DIR}/pdb_mmcif/obsolete.dat \
   --uniclust30_database_path=${DOWNLOAD_DIR}/uniclust30/uniclust30_2018_08/uniclust30_2018_08  \
   --uniref90_database_path=${DOWNLOAD_DIR}/uniref90/uniref90.fasta  \
   --hhblits_binary_path=${EBROOTHHMINSUITE}/bin/hhblits \
   --hhsearch_binary_path=${EBROOTHHMINSUITE}/bin/hhsearch \
   --jackhmmer_binary_path=${EBROOTHMMER}/bin/jackhmmer \
   --kalign_binary_path=${EBROOTKALIGN}/bin/kalign \
   --max_template_date=2020-05-14 \
   --use_gpu_relax=False
```

=== "2.2 on GPU"
```bash title="alphafold-gpu.sh"
#!/bin/bash

#SBATCH --job-name=alphafold_run
#SBATCH --account=def-someprof    # adjust this to match the accounting group you are using to submit jobs
#SBATCH --time=08:00:00           # adjust this to match the walltime of your job
#SBATCH --gres=gpu:1              # a GPU helps to accelerate the inference part only
#SBATCH --cpus-per-task=8         # a MAXIMUM of 8 core, AlphaFold has no benefit to use more
#SBATCH --mem=20G                 # adjust this according to the memory you need

# Load modules dependencies.
module load StdEnv/2020 gcc/9.3.0 openmpi/4.0.3 cuda/11.4 cudnn/8.2.0 kalign/2.03 hmmer/3.2.1 openmm-alphafold/7.5.1 hh-suite/3.3.0 python/3.8

DOWNLOAD_DIR=$SCRATCH/alphafold/data   # set the appropriate path to your downloaded data
INPUT_DIR=$SCRATCH/alphafold/input     # set the appropriate path to your input data
OUTPUT_DIR=${SCRATCH}/alphafold/output # set the appropriate path to your output data

# Generate your virtual environment in $SLURM_TMPDIR.
virtualenv --no-download ${SLURM_TMPDIR}/env
source ${SLURM_TMPDIR}/env/bin/activate

# Install AlphaFold and its dependencies.
pip install --no-index --upgrade pip
pip install --no-index --requirement ~/alphafold-requirements.txt

# Edit with the proper arguments and run your commands.
# Note that the `--uniclust30_database_path` option below was renamed to
# `--uniref30_database_path` in 2.3.
# run_alphafold.py --help
run_alphafold.py \
   --fasta_paths=${INPUT_DIR}/YourSequence.fasta,${INPUT_DIR}/AnotherSequence.fasta \
   --output_dir=${OUTPUT_DIR} \
   --data_dir=${DOWNLOAD_DIR} \
   --model_preset=monomer_casp14 \
   --bfd_database_path=${DOWNLOAD_DIR}/bfd/bfd_metaclust_clu_complete_id30_c90_final_seq.sorted_opt \
   --mgnify_database_path=${DOWNLOAD_DIR}/mgnify/mgy_clusters_2018_12.fa \
   --pdb70_database_path=${DOWNLOAD_DIR}/pdb70/pdb70 \
   --template_mmcif_dir=${DOWNLOAD_DIR}/pdb_mmcif/mmcif_files \
   --obsolete_pdbs_path=${DOWNLOAD_DIR}/pdb_mmcif/obsolete.dat \
   --uniclust30_database_path=${DOWNLOAD_DIR}/uniclust30/uniclust30_2018_08/uniclust30_2018_08  \
   --uniref90_database_path=${DOWNLOAD_DIR}/uniref90/uniref90.fasta  \
   --hhblits_binary_path=${EBROOTHHMINSUITE}/bin/hhblits \
   --hhsearch_binary_path=${EBROOTHHMINSUITE}/bin/hhsearch \
   --jackhmmer_binary_path=${EBROOTHMMER}/bin/jackhmmer \
   --kalign_binary_path=${EBROOTKALIGN}/bin/kalign \
   --max_template_date=2020-05-14 \
   --use_gpu_relax=True
```

Then, submit the job to the scheduler.
```bash
(alphafold_env) [name@server ~]$ sbatch --job-name alphafold-X alphafold-gpu.sh
```

## Troubleshooting

### Broken pipe error message
When downloading the database, you may encounter a `Client_loop: send disconnect: Broken pipe` error message. It is hard to find the exact cause for this error message. It could be as simple as an unusually high number of users working on the login node, leaving less space for you to upload data.

*   One solution is to use a [terminal multiplexer](prolonging-terminal-sessions.md#terminal-multiplexers). Note that you could still encounter this error message but the chances are lower.

*   A second solution is to use the database that is already present on the cluster: `/cvmfs/bio.data.computecanada.ca/content/databases/Core/alphafold2_dbs/2023_07/`.

*   Another option is to download the full database in sections. To have access to the different download scripts, after loading the module and activated your virtual environment, you simply enter `download_` in your terminal and tap twice on the `tab` keyboard key to visualize all the scripts that are available. You can manually download sections of the database by using the available script, as for instance `download_pdb.sh`.