---
title: "AlphaFold2/fr"
slug: "alphafold2"
lang: "fr"

source_wiki_title: "AlphaFold2/fr"
source_hash: "8f13ad1bcddb9c1eea910133c5555666"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:04:23.460053+00:00"

tags:
  - software

keywords:
  - "SBATCH"
  - "SLURM batch script"
  - "hhblits"
  - "base de données"
  - "run_alphafold.py"
  - "GPU inference"
  - "uniref90"
  - "bases de données"
  - "dépannage"
  - "database paths"
  - "environnement virtuel Python"
  - "dependencies"
  - "bash"
  - "walltime"
  - "nœud de calcul"
  - "répertoire $SCRATCH"
  - "virtual environment"
  - "alphafold"
  - "pip install"
  - "repliement des protéines"
  - "alphafold-gpu.sh"
  - "use_gpu_relax"
  - "nœud de transfert de données"
  - "apprentissage automatique"
  - "script de soumission"
  - "nœud de connexion"
  - "environnement virtuel"
  - "AlphaFold"
  - "Broken pipe"
  - "ordonnanceur"
  - "téléchargement de données"
  - "cpus-per-task"
  - "fasta_paths"
  - "jackhmmer"
  - "SLURM"
  - "bash script"

questions:
  - "Qu'est-ce qu'AlphaFold et comment doit-on citer son utilisation dans une publication scientifique ?"
  - "Quelles sont les étapes requises pour installer AlphaFold dans un environnement virtuel Python sur les grappes de calcul ?"
  - "Où se trouvent les bases de données nécessaires au fonctionnement d'AlphaFold et comment y accéder ?"
  - "Où les bases de données doivent-elles être obligatoirement stockées ?"
  - "À partir de quels types de nœuds le répertoire de données doit-il être créé ?"
  - "Quelles commandes permettent de définir la variable d'environnement et de créer le répertoire de téléchargement ?"
  - "Quel type de nœud est recommandé pour télécharger les données d'AlphaFold et quel outil devrait être utilisé pour gérer la longue durée du téléchargement ?"
  - "Quelle est la structure générale et la taille totale approximative des bases de données requises pour la version 2.3 d'AlphaFold ?"
  - "Combien de cœurs (CPU) au maximum doivent être alloués lors de la soumission d'une tâche AlphaFold et pourquoi ?"
  - "What is the primary purpose of this SLURM batch script?"
  - "Which specific parameters in the script must the user adjust to match their own cluster account and job requirements?"
  - "Why does the script restrict the CPU allocation to a maximum of 8 cores?"
  - "What are the recommended SLURM resource allocations, such as CPUs, GPUs, and memory, for running an AlphaFold job?"
  - "How does the script set up the virtual environment and install the necessary software dependencies for AlphaFold?"
  - "What key arguments and database paths must be provided to the `run_alphafold.py` command to execute the prediction?"
  - "How are the Slurm job resources, such as CPU cores and memory, configured for the AlphaFold CPU job?"
  - "What steps are taken to set up the virtual environment and install dependencies before running the AlphaFold Python script?"
  - "Which specific genetic databases and binary paths must be defined as arguments when executing the run_alphafold.py command?"
  - "What command is used to install AlphaFold's dependencies from the requirements file?"
  - "What are the required arguments for running the `run_alphafold.py` script as shown in the text?"
  - "Which specific database and model presets are selected in the provided execution command?"
  - "Quels sont les chemins d'accès définis pour la base de données uniref90 et les différents outils bioinformatiques (hhblits, jackhmmer, kalign) ?"
  - "Quelles sont les valeurs attribuées aux paramètres de configuration tels que la date maximale des modèles (max_template_date) et l'utilisation du GPU pour la relaxation ?"
  - "Quel est le nom du fichier de script bash indiqué pour la configuration avec GPU dans l'interface à onglets ?"
  - "Quelles sont les ressources informatiques (CPU, GPU, mémoire) recommandées dans le script SLURM pour exécuter AlphaFold ?"
  - "Quelle commande doit être utilisée pour soumettre le script de la tâche AlphaFold à l'ordonnanceur ?"
  - "Quelles sont les solutions proposées pour contourner l'erreur \"Broken pipe\" lors du téléchargement des bases de données ?"
  - "Quelles sont les ressources informatiques (CPU, GPU, mémoire) recommandées dans le script SLURM pour exécuter AlphaFold ?"
  - "Quelle commande doit être utilisée pour soumettre le script de la tâche AlphaFold à l'ordonnanceur ?"
  - "Quelles sont les solutions proposées pour contourner l'erreur \"Broken pipe\" lors du téléchargement des bases de données ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

AlphaFold est un modèle d'apprentissage automatique pour la prédiction du repliement des protéines.

Nous expliquons ici comment utiliser la version AlphaFold v2.0 présentée au CASP14 et dont un compte-rendu a été publié dans Nature.

Le code source et la documentation se trouvent sur [cette page GitHub](https://github.com/deepmind/alphafold).
Toute publication mentionnant des résultats obtenus par l'utilisation du code source ou des paramètres de modèle doit [citer](https://github.com/deepmind/alphafold#citing-this-work) [cette publication](https://doi.org/10.1038/s41586-021-03819-2).

## Versions disponibles
AlphaFold est disponible sur nos grappes dans les paquets Python préconstruits (*wheels*). Vous pouvez afficher les versions disponibles avec la commande `avail_wheels`.

```bash
avail_wheels alphafold --all-versions
```

```text
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

## Installer AlphaFold dans un environnement virtuel Python

1.  Chargez les dépendances d'AlphaFold.

    ```bash
    module load StdEnv/2020 gcc/9.3.0 openmpi/4.0.3 cuda/11.4 cudnn/8.2.0 kalign/2.03 hmmer/3.2.1 openmm-alphafold/7.5.1 hh-suite/3.3.0 python/3.8
    ```
    Python 3.7 et 3.8 sont supportés depuis juillet 2022.

2.  Créez et activez un environnement virtuel Python.

    ```bash
    virtualenv --no-download ~/alphafold_env
    source ~/alphafold_env/bin/activate
    ```

3.  Installez une version spécifique d'AlphaFold et ses dépendances Python.

    ```bash
    (alphafold_env) [name@server ~] pip install --no-index --upgrade pip
    (alphafold_env) [name@server ~] pip install --no-index alphafold==X.Y.Z
    ```
    où `X.Y.Z` représente le numéro de la version, par exemple `2.2.4`.
    Pour installer la plus récente version disponible pour nos grappes, n'indiquez pas de version.

4.  Validez.

    ```bash
    (alphafold_env) [name@server ~] run_alphafold.py --help
    ```

5.  Figez l'environnement et les dépendances.

    ```bash
    (alphafold_env) [name@server ~] pip freeze > ~/alphafold-requirements.txt
    ```

## Bases de données
AlphaFold requiert un jeu de bases de données.

Les bases de données sont disponibles dans `/cvmfs/bio.data.computecanada.ca/content/databases/Core/alphafold2_dbs/2023_07/`.

Les bases de données AlphaFold sont mises à jour annuellement dans CVMFS. La mise à jour de janvier 2024 est disponible dans le répertoire `2024_01`.

```bash
(alphafold_env) [name@server ~] export DOWNLOAD_DIR=/cvmfs/bio.data.computecanada.ca/content/databases/Core/alphafold2_dbs/2023_07/
```

Vous pouvez aussi télécharger les bases de données localement dans votre répertoire /scratch.

!!! important "Important"
    Les bases de données doivent se trouver dans le répertoire `$SCRATCH`.

=== "En général"

1.  Créez le répertoire de données à partir d'un nœud de connexion ou d'un nœud de transfert de données (DTN).

    ```bash
    (alphafold_env) [name@server ~] export DOWNLOAD_DIR=$SCRATCH/alphafold/data
    (alphafold_env) [name@server ~] mkdir -p $DOWNLOAD_DIR
    ```

2.  Lorsque vos modules sont chargés et votre environnement virtuel est activé, vous pouvez télécharger les données.

    ```bash
    (alphafold_env) [name@server ~] download_all_data.sh $DOWNLOAD_DIR
    ```

    !!! warning "Attention"
        **Ceci ne doit pas se faire à partir d'un nœud de calcul.** Sur les grappes qui ont des nœuds de transfert de données (DTN), utilisez ce type de nœud (voir [la page Transfert de données](../getting-started/transferring_data.md)); autrement, utilisez un nœud de connexion. Puisque la durée du téléchargement peut prendre une journée complète, nous vous suggérons d'utiliser plutôt un [multiplexeur de terminal](../running-jobs/prolonging_terminal_sessions.md#multiplexeur-de-terminal). Il est possible que vous obteniez le message d'erreur `Client_loop: send disconnect: Broken pipe`; voir [Dépannage](#dépannage) ci-dessous.

=== "sur Graham uniquement"

1.  Configurez `DOWNLOAD_DIR`.

    ```bash
    (alphafold_env) [name@server ~] export DOWNLOAD_DIR=/datashare/alphafold
    ```

Par la suite, la structure des données sera semblable à ceci:

=== "2.3"

```bash
(alphafold_env) [name@server ~] tree -d $DOWNLOAD_DIR
```

```text
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
(alphafold_env) [name@server ~] tree -d $DOWNLOAD_DIR
```

```text
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

## Exécuter AlphaFold
!!! warning "Performance"
    Vous pouvez demander au plus 8 cœurs lors de l'exécution d'AlphaFold car il est codé en dur (*hardcoded*) pour ne pas en utiliser plus et ne bénéficie pas d'en utiliser davantage.

Modifiez un des scripts de soumission suivants, selon vos besoins.

=== "2.3 avec CPU"

```bash title="alphafold-2.3-cpu.sh"
#!/bin/bash

#SBATCH --job-name=alphafold_run
#SBATCH --account=def-someprof    # ajustez ce paramètre à votre groupe comptable
#SBATCH --time=08:00:00           # ajustez ce paramètre au temps d'exécution souhaité
#SBATCH --cpus-per-task=8         # un MAXIMUM de 8 cœurs, AlphaFold n'a aucun avantage à en utiliser plus
#SBATCH --mem=20G                 # ajustez ce paramètre en fonction de la mémoire nécessaire

# Chargez les dépendances des modules.
module load StdEnv/2020 gcc/9.3.0 openmpi/4.0.3 cuda/11.4 cudnn/8.2.0 kalign/2.03 hmmer/3.2.1 openmm-alphafold/7.5.1 hh-suite/3.3.0 python/3.8

DOWNLOAD_DIR=$SCRATCH/alphafold/data   # définissez le chemin approprié vers vos données téléchargées
INPUT_DIR=$SCRATCH/alphafold/input     # définissez le chemin approprié vers vos données d'entrée
OUTPUT_DIR=${SCRATCH}/alphafold/output # définissez le chemin approprié vers vos données de sortie

# Créez votre environnement virtuel dans $SLURM_TMPDIR.
virtualenv --no-download ${SLURM_TMPDIR}/env
source ${SLURM_TMPDIR}/env/bin/activate

# Installez AlphaFold et ses dépendances.
pip install --no-index --upgrade pip
pip install --no-index --requirement ~/alphafold-requirements.txt

# Modifiez avec les arguments appropriés et exécutez vos commandes.
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

=== "2.3 avec GPU"

```bash title="alphafold-2.3-gpu.sh"
#!/bin/bash

#SBATCH --job-name=alphafold_run
#SBATCH --account=def-someprof    # ajustez ce paramètre à votre groupe comptable
#SBATCH --time=08:00:00           # ajustez ce paramètre au temps d'exécution souhaité
#SBATCH --cpus-per-task=8         # un MAXIMUM de 8 cœurs, AlphaFold n'a aucun avantage à en utiliser plus
#SBATCH --gres=gpu:1              # une carte graphique (GPU) aide à accélérer la partie inférence seulement
#SBATCH --mem=20G                 # ajustez ce paramètre en fonction de la mémoire nécessaire

# Chargez les dépendances des modules.
module load StdEnv/2020 gcc/9.3.0 openmpi/4.0.3 cuda/11.4 cudnn/8.2.0 kalign/2.03 hmmer/3.2.1 openmm-alphafold/7.5.1 hh-suite/3.3.0 python/3.8

DOWNLOAD_DIR=$SCRATCH/alphafold/data   # définissez le chemin approprié vers vos données téléchargées
INPUT_DIR=$SCRATCH/alphafold/input     # définissez le chemin approprié vers vos données d'entrée
OUTPUT_DIR=${SCRATCH}/alphafold/output # définissez le chemin approprié vers vos données de sortie

# Créez votre environnement virtuel dans $SLURM_TMPDIR.
virtualenv --no-download ${SLURM_TMPDIR}/env
source ${SLURM_TMPDIR}/env/bin/activate

# Installez AlphaFold et ses dépendances.
pip install --no-index --upgrade pip
pip install --no-index --requirement ~/alphafold-requirements.txt

# Modifiez avec les arguments appropriés et exécutez vos commandes.
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

=== "2.2 avec CPU"

```bash title="alphafold-cpu.sh"
#!/bin/bash

#SBATCH --job-name=alphafold_run
#SBATCH --account=def-someprof    # ajustez ce paramètre à votre groupe comptable
#SBATCH --time=08:00:00           # ajustez ce paramètre au temps d'exécution souhaité
#SBATCH --cpus-per-task=8         # un MAXIMUM de 8 cœurs, AlphaFold n'a aucun avantage à en utiliser plus
#SBATCH --mem=20G                 # ajustez ce paramètre en fonction de la mémoire nécessaire

# Chargez les dépendances des modules.
module load StdEnv/2020 gcc/9.3.0 openmpi/4.0.3 cuda/11.4 cudnn/8.2.0 kalign/2.03 hmmer/3.2.1 openmm-alphafold/7.5.1 hh-suite/3.3.0 python/3.8

DOWNLOAD_DIR=$SCRATCH/alphafold/data   # définissez le chemin approprié vers vos données téléchargées
INPUT_DIR=$SCRATCH/alphafold/input     # définissez le chemin approprié vers vos données d'entrée
OUTPUT_DIR=${SCRATCH}/alphafold/output # définissez le chemin approprié vers vos données de sortie

# Créez votre environnement virtuel dans $SLURM_TMPDIR.
virtualenv --no-download ${SLURM_TMPDIR}/env
source ${SLURM_TMPDIR}/env/bin/activate

# Installez AlphaFold et ses dépendances.
pip install --no-index --upgrade pip
pip install --no-index --requirement ~/alphafold-requirements.txt

# Modifiez avec les arguments appropriés et exécutez vos commandes.
# Notez que l'option `--uniclust30_database_path` ci-dessous a été renommée
# `--uniref30_database_path` en version 2.3.
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

=== "2.2 avec GPU"

```bash title="alphafold-gpu.sh"
#!/bin/bash

#SBATCH --job-name=alphafold_run
#SBATCH --account=def-someprof    # ajustez ce paramètre à votre groupe comptable
#SBATCH --time=08:00:00           # ajustez ce paramètre au temps d'exécution souhaité
#SBATCH --gres=gpu:1              # une carte graphique (GPU) aide à accélérer la partie inférence seulement
#SBATCH --cpus-per-task=8         # un MAXIMUM de 8 cœurs, AlphaFold n'a aucun avantage à en utiliser plus
#SBATCH --mem=20G                 # ajustez ce paramètre en fonction de la mémoire nécessaire

# Chargez les dépendances des modules.
module load StdEnv/2020 gcc/9.3.0 openmpi/4.0.3 cuda/11.4 cudnn/8.2.0 kalign/2.03 hmmer/3.2.1 openmm-alphafold/7.5.1 hh-suite/3.3.0 python/3.8

DOWNLOAD_DIR=$SCRATCH/alphafold/data   # définissez le chemin approprié vers vos données téléchargées
INPUT_DIR=$SCRATCH/alphafold/input     # définissez le chemin approprié vers vos données d'entrée
OUTPUT_DIR=${SCRATCH}/alphafold/output # définissez le chemin approprié vers vos données de sortie

# Créez votre environnement virtuel dans $SLURM_TMPDIR.
virtualenv --no-download ${SLURM_TMPDIR}/env
source ${SLURM_TMPDIR}/env/bin/activate

# Installez AlphaFold et ses dépendances.
pip install --no-index --upgrade pip
pip install --no-index --requirement ~/alphafold-requirements.txt

# Modifiez avec les arguments appropriés et exécutez vos commandes.
# Notez que l'option `--uniclust30_database_path` ci-dessous a été renommée
# `--uniref30_database_path` en version 2.3.
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

Soumettez la tâche à l'ordonnanceur.

```bash
(alphafold_env) [name@server ~] sbatch --job-name alphafold-X alphafold-gpu.sh
```

## Dépannage
### Message d'erreur *Broken pipe*
Au téléchargement de la base de données, vous pourriez obtenir le message d'erreur `Client_loop: send disconnect: Broken pipe`. Il est difficile de déterminer la cause exacte de ce message. Il pourrait tout simplement s'agir qu'un nombre élevé d'utilisateurs travaillent sur le nœud de connexion en même temps, ce qui vous laisse moins de place pour téléverser des données.

*   Une solution est d'utiliser un [multiplexeur de terminal](../running-jobs/prolonging_terminal_sessions.md#multiplexeur-de-terminal). Il n'est pas impossible d'obtenir le message d'erreur, mais les chances sont moindres.

*   Une deuxième solution est d'utiliser la base de données qui se trouve sur la grappe : `/cvmfs/bio.data.computecanada.ca/content/databases/Core/alphafold2_dbs/2023_07/`.

*   Une autre solution est de télécharger la base de données par sections. Pour avoir accès aux scripts de téléchargement après avoir chargé le module et activé votre environnement virtuel, il faut simplement entrer `download_` dans votre terminal et taper deux fois sur la touche `tab` du clavier pour voir tous les scripts disponibles. Vous pouvez télécharger manuellement les sections de la base de données en utilisant le script disponible, par exemple `download_pdb.sh`.