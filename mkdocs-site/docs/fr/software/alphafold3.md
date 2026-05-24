---
title: "AlphaFold3/fr"
slug: "alphafold3"
lang: "fr"

source_wiki_title: "AlphaFold3/fr"
source_hash: "285b8a2d1f1f6e5a9f9194ebf9507d3c"
last_synced: "2026-05-24T00:00:16.123503+00:00"
last_processed: "2026-05-24T00:34:26.266474+00:00"

tags:
  - software

keywords:
  - "AlphaFold3"
  - "SLURM_TMPDIR"
  - "Alphafold3"
  - "optimisation des coûts"
  - "inférence de modèle"
  - "bases de données"
  - "exécution par étapes"
  - "dépendances"
  - "Inférence"
  - "GPU A100"
  - "data paths"
  - "AlphaFold"
  - "Soumission de tâche"
  - "Ordonnanceur"
  - "Mémoire GPU"
  - "pipeline de données"
  - "google-deepmind"
  - "dependencies"
  - "fetch_databases.sh"
  - "virtual environment"
  - "environnement virtuel"

questions:
  - "Comment doit-on configurer l'environnement virtuel et installer les dépendances requises pour AlphaFold3 ?"
  - "Quelle est la procédure à suivre pour obtenir les paramètres du modèle auprès de Google et quel est le délai d'attente ?"
  - "Où les bases de données nécessaires à l'exécution d'AlphaFold3 doivent-elles être obligatoirement stockées et comment les télécharger ?"
  - "Pourquoi est-il recommandé de séparer le pipeline de données et le modèle d'inférence lors de l'utilisation d'AlphaFold3 ?"
  - "Comment doit-on configurer le script SLURM et les arguments de la commande pour exécuter uniquement l'étape de préparation des données sur CPU ?"
  - "Quelles sont les contraintes matérielles spécifiques requises concernant les cartes graphiques (GPU) pour l'étape d'inférence du modèle ?"
  - "Comment procéder au téléchargement des bases de données requises pour AlphaFold3 ?"
  - "Quelles sont les commandes spécifiques à exécuter pour préparer le répertoire de stockage ?"
  - "Quelle est la particularité concernant la méthode d'exécution d'AlphaFold3 mentionnée dans le texte ?"
  - "What are the specific directory paths that need to be configured for the downloaded data, input, and output?"
  - "Where is the virtual environment generated and how is it activated?"
  - "What specific software and its dependencies are being installed after the environment is set up?"
  - "Quels sont les arguments et répertoires nécessaires pour exécuter correctement le script d'inférence `run_alphafold.py` ?"
  - "Comment configurer l'ordonnanceur pour lancer automatiquement l'étape d'inférence uniquement après le succès de l'étape de préparation des données ?"
  - "Quelles modifications faut-il apporter aux variables d'environnement et aux ressources allouées pour éviter les erreurs de mémoire GPU insuffisante ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Nous décrivons ici l'utilisation de AlphaFold v3.0.

Le code source et la documentation se trouvent sur [leur page GitHub](https://github.com/google-deepmind/alphafold3).
Toute publication qui divulgue des résultats découlant de l'utilisation de ce code source ou des paramètres du modèle [doit citer](https://github.com/google-deepmind/alphafold3#citing-this-work) le [document AlphaFold3](https://doi.org/10.1038/s41586-024-07487-w).

## Versions disponibles
Sur nos grappes, AlphaFold3 est disponible sous forme de paquets préconstruits (*wheels*). Pour les lister, utilisez `avail_wheels`.

```bash
avail_wheels alphafold3
```

AlphaFold2 est encore disponible ([voir la documentation](alphafold2.md)).

## Créer un fichier des dépendances requises

1.  Chargez les dépendances de AlphaFold3.
    ```bash
    module load StdEnv/2023 hmmer-alphafold3/3.4 rdkit/2024.03.5 python/3.12
    ```

2.  Téléchargez le script d'exécution.
    Plusieurs versions du script d'exécution sont disponibles. Téléchargez celle qui correspond à vos besoins :

    *   Version 3.0.2
        ```bash
        wget https://raw.githubusercontent.com/google-deepmind/alphafold3/refs/tags/v3.0.2/run_alphafold.py
        ```
    *   Version 3.0.1
        ```bash
        wget https://raw.githubusercontent.com/google-deepmind/alphafold3/refs/tags/v3.0.1/run_alphafold.py
        ```
    *   Version 3.0.0
        ```bash
        wget https://raw.githubusercontent.com/google-deepmind/alphafold3/23e3d46d4ca126e8731e8c0cbb5673e9a848ceb5/run_alphafold.py
        ```

3.  Créez et activez un environnement virtuel Python.
    ```bash
    virtualenv --no-download ~/alphafold3_env
    source ~/alphafold3_env/bin/activate
    ```

4.  Installez une version de AlphaFold3 ainsi que ses dépendances Python.
    ```bash
    (alphafold3_env) [name@server ~]$ pip install --no-index --upgrade pip
    (alphafold3_env) [name@server ~]$ pip install --no-index alphafold3==X.Y.Z
    ```
    où `X.Y.Z` est la version spécifique, par exemple `3.0.0`.
    N'entrez pas le numéro de la version si vous voulez installer la plus récente.

5.  Compilez les données nécessaires.
    ```bash
    (alphafold3_env) [name@server ~]$ build_data
    ```
    Ceci crée des fichiers de données dans l'environnement virtuel.

6.  Validez.
    ```bash
    (alphafold3_env) [name@server ~]$ python run_alphafold.py --help
    ```

7.  Gelez l'environnement et l'ensemble des requis.
    ```bash
    (alphafold3_env) [name@server ~]$ pip freeze > ~/alphafold3-requirements.txt
    ```

8.  Désactivez l'environnement.
    ```bash
    (alphafold3_env) [name@server ~]$ deactivate
    ```

9.  Nettoyez et supprimez l'environnement virtuel.
    ```bash
    rm -r ~/alphafold3_env
    ```

L'environnement virtuel sera plutôt créé dans votre tâche.

## Modèle
Vous pouvez demander le modèle à Google. Le délai de réponse est de 2 à 3 jours ouvrables.
Voir la documentation GitHub pour l'obtention des paramètres du modèle : [Obtaining Model Parameters](https://github.com/google-deepmind/alphafold3?tab=readme-ov-file#obtaining-model-parameters).

## Bases de données
AlphaFold3 nécessite un ensemble de bases de données.

!!! warning "Emplacement des bases de données"
    Les bases de données doivent obligatoirement résider dans le répertoire `$SCRATCH`.

1.  Téléchargez le script de téléchargement.
    ```bash
    wget https://raw.githubusercontent.com/google-deepmind/alphafold3/refs/heads/main/fetch_databases.sh
    ```

2.  Téléchargez les bases de données.
    ```bash
    mkdir -p $SCRATCH/alphafold/dbs
    bash fetch_databases.sh $SCRATCH/alphafold/dbs
    ```

## Exécution par étapes
AlphaFold3 doit être [exécuté par étapes](https://github.com/google-deepmind/alphafold3/blob/main/docs/performance.md#running-the-pipeline-in-stages), c'est-à-dire :

1.  séparer le pipeline de données pour CPU seulement et le modèle d'inférence (qui demande un GPU) pour optimiser les coûts et l'utilisation des ressources;
2.  cacher les résultats de la recherche de MSA/modèle, pour ensuite réutiliser le JSON augmenté pour plusieurs différentes inférences ou pour des variations d'autres fonctionnalités (par exemple un ligand).

Pour des références, voir :
*   [inputs](https://github.com/google-deepmind/alphafold3/blob/main/docs/input.md)
*   [outputs](https://github.com/google-deepmind/alphafold3/blob/main/docs/output.md)
*   [performance](https://github.com/google-deepmind/alphafold3/blob/main/docs/performance.md)

### 1. Pipeline de données (CPU)
Modifiez le script suivant selon vos besoins.

:::bash alphafold3-data.sh
```bash
#!/bin/bash

#SBATCH --job-name=alphafold3-data
#SBATCH --account=def-someprof    # adjust this to match the accounting group you are using to submit jobs
#SBATCH --time=08:00:00           # adjust this to match the walltime of your job
#SBATCH --cpus-per-task=8         # a MAXIMUM of 8 core, AlphaFold has no benefit to use more
#SBATCH --mem=64G                 # adjust this according to the memory you need

# Load modules dependencies.
module load StdEnv/2023 hmmer-alphafold3/3.4 rdkit/2024.03.5 python/3.12

DOWNLOAD_DIR=$SCRATCH/alphafold/dbs    # set the appropriate path to your downloaded data
INPUT_DIR=$SCRATCH/alphafold/input     # set the appropriate path to your input data
OUTPUT_DIR=$SLURM_TMPDIR/alphafold/output   # set the appropriate path to your output data

# Generate your virtual environment in $SLURM_TMPDIR.
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate

# Install AlphaFold and its dependencies.
pip install --no-index --upgrade pip
pip install --no-index --requirement ~/alphafold3-requirements.txt

# build data in $VIRTUAL_ENV
build_data

# https://github.com/google-deepmind/alphafold3/blob/main/docs/performance.md#compilation-time-workaround-with-xla-flags
export XLA_FLAGS="--xla_gpu_enable_triton_gemm=false"

# Edit with the proper arguments and run your commands.
# run_alphafold.py --help
python run_alphafold.py \
    --db_dir=$DOWNLOAD_DIR \
    --input_dir=$INPUT_DIR \
    --output_dir=$OUTPUT_DIR \
    --jax_compilation_cache_dir=$HOME/.cache \
    --nhmmer_n_cpu=$SLURM_CPUS_PER_TASK \
    --jackhmmer_n_cpu=$SLURM_CPUS_PER_TASK \
    --norun_inference  # Run data stage

# copy back
mkdir $SCRATCH/alphafold/output
cp -vr $OUTPUT_DIR $SCRATCH/alphafold/output
```

### 2. Inférence de modèle
Modifiez le script suivant selon vos besoins.

!!! warning "Compatibilité"
    AlphaFold3 prend en charge seulement la capacité de calcul des versions 8.0 et plus récentes, soit pour des GPU A100 et plus performants.

:::bash alphafold3-inference.sh
```bash
#!/bin/bash

#SBATCH --job-name=alphafold3-inference
#SBATCH --account=def-someprof    # adjust this to match the accounting group you are using to submit jobs
#SBATCH --time=08:00:00           # adjust this to match the walltime of your job
#SBATCH --cpus-per-task=1         # AlphaFold has no benefit to use more for the inference stage
#SBATCH --gpus=a100:1             # Alphafold3 inference only runs on ONE A100 or greater.
#SBATCH --mem=20G                 # adjust this according to the memory you need

# Load modules dependencies.
module load StdEnv/2023 hmmer-alphafold3/3.4 rdkit/2024.03.5 python/3.12 cuda/12.2 cudnn/9.2

DOWNLOAD_DIR=$SCRATCH/alphafold/dbs    # set the appropriate path to your downloaded data
INPUT_DIR=$SCRATCH/alphafold/input     # set the appropriate path to your input data, following the data stage.
OUTPUT_DIR=$SCRATCH/alphafold/output   # set the appropriate path to your output data

# Generate your virtual environment in $SLURM_TMPDIR.
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate

# Install AlphaFold and its dependencies.
pip install --no-index --upgrade pip
pip install --no-index --requirement ~/alphafold3-requirements.txt

# build data in $VIRTUAL_ENV
build_data

# https://github.com/google-deepmind/alphafold3/blob/main/docs/performance.md#compilation-time-workaround-with-xla-flags
export XLA_FLAGS="--xla_gpu_enable_triton_gemm=false"

# https://github.com/google-deepmind/alphafold3/blob/main/docs/performance.md#gpu-memory
export XLA_PYTHON_CLIENT_PREALLOCATE=true
export XLA_CLIENT_MEM_FRACTION=0.95

# Edit with the proper arguments and run your commands.
# run_alphafold.py --help
python run_alphafold.py \
    --db_dir=$DOWNLOAD_DIR \
    --input_dir=$INPUT_DIR \
    --output_dir=$OUTPUT_DIR \
    --jax_compilation_cache_dir=$HOME/.cache \
    --norun_data_pipeline  # Run inference stage
```

### 3. Soumettre une tâche

Soumettez la tâche à l'ordonnanceur.

#### Tâches indépendantes
```bash
sbatch alphafold3-data.sh
```

Attendez la fin et soumettez ensuite la deuxième étape.
```bash
sbatch alphafold3-inference.sh
```

#### Tâches dépendantes
```bash
jid1=$(sbatch alphafold3-data.sh)
jid2=$(sbatch --dependency=afterok:$jid1 alphafold3-inference.sh)
sq
```
Si la première étape échoue, vous devez annuler manuellement la deuxième étape.
```bash
scancel -u $USER -n alphafold3-inference
```

## Dépannage
### Mémoire insuffisante (GPU)
Si vous voulez exécuter AlphaFold3 avec plus de 5120 jetons ou sur un GPU de mémoire moindre (par exemple sur un A100 avec 40Go de mémoire), vous pouvez activer la fonctionnalité de [mémoire unifiée](https://github.com/google-deepmind/alphafold3/blob/main/docs/performance.md#unified-memory).

Dans le script de soumission à l'étape d'inférence, ajoutez les variables d'environnement suivantes :
```bash
export XLA_PYTHON_CLIENT_PREALLOCATE=false
export TF_FORCE_UNIFIED_MEMORY=true
export XLA_CLIENT_MEM_FRACTION=2.0  # 2 x 40GB = 80 GB
```
et ajustez en conséquence la quantité de mémoire allouée à la tâche, par exemple `#SBATCH --mem=80G`.