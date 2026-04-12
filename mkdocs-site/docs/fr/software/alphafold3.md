---
title: "AlphaFold3/fr"
slug: "alphafold3"
lang: "fr"

source_wiki_title: "AlphaFold3/fr"
source_hash: "c044bb004a4c55c0f2a9f41f99302407"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:06:14.735026+00:00"

tags:
  - software

keywords:
  - "optimiser les ressources"
  - "bases de données"
  - "AlphaFold 3"
  - "Pipeline de données"
  - "virtual environment"
  - "étape d'inférence"
  - "pip install"
  - "exécution par étapes"
  - "pipeline de données"
  - "GPU A100"
  - "build_data"
  - "AlphaFold3"
  - "Inférence de modèle"
  - "Alphafold3"
  - "environnement virtuel"
  - "soumission de tâche"
  - "mémoire insuffisante GPU"
  - "modèle d'inférence"
  - "Scripts SLURM"
  - "mémoire unifiée"
  - "SLURM_TMPDIR"

questions:
  - "Quelles sont les étapes à suivre pour créer l'environnement virtuel et installer les dépendances requises pour AlphaFold3 ?"
  - "Comment obtenir les paramètres du modèle auprès de Google et dans quel répertoire les bases de données doivent-elles être obligatoirement stockées ?"
  - "Pourquoi est-il nécessaire d'exécuter AlphaFold3 par étapes en séparant le pipeline de données et le modèle d'inférence ?"
  - "Comment peut-on optimiser l'utilisation d'AlphaFold3 pour plusieurs inférences en réutilisant les résultats de recherche initiaux ?"
  - "Quelles sont les configurations et ressources CPU recommandées pour exécuter l'étape du pipeline de données via le script SLURM ?"
  - "Quelles sont les exigences matérielles strictes concernant les cartes graphiques (GPU) pour pouvoir lancer l'étape d'inférence du modèle ?"
  - "Quel est l'objectif principal de l'exécution par étapes d'Alphafold3 ?"
  - "Quelle partie du processus d'Alphafold3 est configurée pour fonctionner uniquement sur CPU ?"
  - "Quel composant spécifique d'Alphafold3 requiert l'utilisation d'un GPU ?"
  - "How is the virtual environment created and activated within the SLURM temporary directory?"
  - "What steps are taken to install AlphaFold and its dependencies without downloading from the package index?"
  - "How does the script address potential performance issues related to compilation time?"
  - "Comment configurer et soumettre des tâches dépendantes pour les étapes de données et d'inférence d'AlphaFold3 ?"
  - "Quels sont les paramètres et répertoires essentiels à spécifier lors du lancement du script run_alphafold.py ?"
  - "Quelles variables d'environnement faut-il modifier pour activer la mémoire unifiée en cas de mémoire GPU insuffisante ?"
  - "Comment configurer et soumettre des tâches dépendantes pour les étapes de données et d'inférence d'AlphaFold3 ?"
  - "Quels sont les paramètres et répertoires essentiels à spécifier lors du lancement du script run_alphafold.py ?"
  - "Quelles variables d'environnement faut-il modifier pour activer la mémoire unifiée en cas de mémoire GPU insuffisante ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Nous décrivons ici l'utilisation d'AlphaFold v3.0.

Le code source et la documentation se trouvent sur [leur page GitHub](https://github.com/google-deepmind/alphafold3).
Toute publication qui divulgue des résultats découlant de l'utilisation de ce code source ou des paramètres du modèle [doit citer](https://github.com/google-deepmind/alphafold3#citing-this-work) le [document AlphaFold3](https://doi.org/10.1038/s41586-024-07487-w).

## Versions disponibles

Sur nos grappes, AlphaFold3 est disponible sous forme de paquets préconstruits (*wheels*). Pour les lister, utilisez `avail_wheels`.

```bash
avail_wheels alphafold3
```

AlphaFold2 est encore disponible ([voir la documentation](alphafold2.md)).

## Créer un fichier des dépendances requises

1.  Chargez les dépendances d'AlphaFold3.

    ```bash
    module load StdEnv/2023 hmmer/3.4 rdkit/2024.03.5 python/3.12
    ```

2.  Téléchargez le script d'exécution. Veuillez choisir la version que vous souhaitez télécharger :

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

4.  Installez une version d'AlphaFold3 ainsi que ses dépendances Python.

    ```bash
    (alphafold3_env) [name@server ~] pip install --no-index --upgrade pip
    (alphafold3_env) [name@server ~] pip install --no-index alphafold3==X.Y.Z
    ```

    où `X.Y.Z` est la version spécifique, par exemple `3.0.0`.
    N'entrez pas le numéro de la version si vous voulez installer la plus récente.

5.  Compilez les données nécessaires.

    ```bash
    (alphafold3_env) [name@server ~] build_data
    ```

    Ceci crée des fichiers de données dans l'environnement virtuel.

6.  Validez.

    ```bash
    (alphafold3_env) [name@server ~] python run_alphafold.py --help
    ```

7.  Gelez l'environnement et l'ensemble des requis.

    ```bash
    (alphafold3_env) [name@server ~] pip freeze > ~/alphafold3-requirements.txt
    ```

8.  Désactivez l'environnement.

    ```bash
    (alphafold3_env) [name@server ~] deactivate
    ```

9.  Nettoyez et supprimez l'environnement virtuel.

    ```bash
    rm -r ~/alphafold3_env
    ```

    L'environnement virtuel sera plutôt créé dans votre tâche.

## Modèle

Vous pouvez obtenir le modèle de Google, qui répond habituellement dans les 2 ou 3 jours ouvrables; voir [Obtaining Model Parameters](https://github.com/google-deepmind/alphafold3?tab=readme-ov-file).

## Bases de données

AlphaFold3 nécessite un ensemble de bases de données.

!!! note "Important"
    Les bases de données doivent résider dans le répertoire `$SCRATCH`.

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

```bash linenums="1" title="alphafold3-data.sh"
#!/bin/bash

#SBATCH --job-name=alphafold3-data
#SBATCH --account=def-someprof    # ajustez ceci pour qu'il corresponde à votre groupe comptable
#SBATCH --time=08:00:00           # ajustez ceci pour qu'il corresponde au temps de mur de votre tâche
#SBATCH --cpus-per-task=8         # UN MAXIMUM de 8 cœurs, AlphaFold n'a aucun avantage à en utiliser plus
#SBATCH --mem=64G                 # ajustez ceci selon la mémoire dont vous avez besoin

# Chargez les dépendances des modules.
module load StdEnv/2023 hmmer/3.4 rdkit/2024.03.5 python/3.12

DOWNLOAD_DIR=$SCRATCH/alphafold/dbs    # définissez le chemin approprié vers vos données téléchargées
INPUT_DIR=$SCRATCH/alphafold/input     # définissez le chemin approprié vers vos données d'entrée
OUTPUT_DIR=$SLURM_TMPDIR/alphafold/output   # définissez le chemin approprié vers vos données de sortie

# Générez votre environnement virtuel dans $SLURM_TMPDIR.
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate

# Installez AlphaFold et ses dépendances.
pip install --no-index --upgrade pip
pip install --no-index --requirement ~/alphafold3-requirements.txt

# compilez les données dans $VIRTUAL_ENV
build_data

# https://github.com/google-deepmind/alphafold3/blob/main/docs/performance.md#compilation-time-workaround-with-xla-flags
export XLA_FLAGS="--xla_gpu_enable_triton_gemm=false"

# Modifiez avec les arguments appropriés et exécutez vos commandes.
# run_alphafold.py --help
python run_alphafold.py \
    --db_dir=$DOWNLOAD_DIR \
    --input_dir=$INPUT_DIR \
    --output_dir=$OUTPUT_DIR \
    --jax_compilation_cache_dir=$HOME/.cache \
    --nhmmer_n_cpu=$SLURM_CPUS_PER_TASK \
    --jackhmmer_n_cpu=$SLURM_CPUS_PER_TASK \
    --norun_inference  # Exécutez l'étape de données

# copiez de nouveau
mkdir -p $SCRATCH/alphafold/output
cp -vr $OUTPUT_DIR $SCRATCH/alphafold/output
```

### 2. Inférence de modèle

Modifiez le script suivant selon vos besoins.

!!! warning "Compatibilité"
    AlphaFold3 prend en charge seulement la capacité de calcul des versions 8.0 et plus récentes, soit pour des **A100s et plus performants**.

```bash linenums="1" title="alphafold3-inference.sh"
#!/bin/bash

#SBATCH --job-name=alphafold3-inference
#SBATCH --account=def-someprof    # ajustez ceci pour qu'il corresponde à votre groupe comptable
#SBATCH --time=08:00:00           # ajustez ceci pour qu'il corresponde au temps de mur de votre tâche
#SBATCH --cpus-per-task=1         # AlphaFold n'a aucun avantage à en utiliser plus pour l'étape d'inférence
#SBATCH --gpus=a100:1             # L'inférence d'AlphaFold3 ne s'exécute que sur UN A100 ou un GPU plus puissant.
#SBATCH --mem=20G                 # ajustez ceci selon la mémoire dont vous avez besoin

# Chargez les dépendances des modules.
module load StdEnv/2023 hmmer/3.4 rdkit/2024.03.5 python/3.12 cuda/12.2 cudnn/9.2

DOWNLOAD_DIR=$SCRATCH/alphafold/dbs    # définissez le chemin approprié vers vos données téléchargées
INPUT_DIR=$SCRATCH/alphafold/input     # définissez le chemin approprié vers vos données d'entrée, suite à l'étape des données.
OUTPUT_DIR=$SCRATCH/alphafold/output   # définissez le chemin approprié vers vos données de sortie

# Générez votre environnement virtuel dans $SLURM_TMPDIR.
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate

# Installez AlphaFold et ses dépendances.
pip install --no-index --upgrade pip
pip install --no-index --requirement ~/alphafold3-requirements.txt

# compilez les données dans $VIRTUAL_ENV
build_data

# https://github.com/google-deepmind/alphafold3/blob/main/docs/performance.md#compilation-time-workaround-with-xla-flags
export XLA_FLAGS="--xla_gpu_enable_triton_gemm=false"

# https://github.com/google-deepmind/alphafold3/blob/main/docs/performance.md#gpu-memory
export XLA_PYTHON_CLIENT_PREALLOCATE=true
export XLA_CLIENT_MEM_FRACTION=0.95

# Modifiez avec les arguments appropriés et exécutez vos commandes.
# run_alphafold.py --help
python run_alphafold.py \
    --db_dir=$DOWNLOAD_DIR \
    --input_dir=$INPUT_DIR \
    --output_dir=$OUTPUT_DIR \
    --jax_compilation_cache_dir=$HOME/.cache \
    --norun_data_pipeline  # Exécutez l'étape d'inférence
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