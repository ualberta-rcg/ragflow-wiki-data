---
title: "AlphaFold3/fr"
slug: "alphafold3"
lang: "fr"

source_wiki_title: "AlphaFold3/fr"
source_hash: "a09076c658ef3cafd82afa32a82e279f"
last_synced: "2026-05-17T14:59:09.465984+00:00"
last_processed: "2026-05-17T15:04:30.351298+00:00"

tags:
  - software

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: true
  qa_generated: true
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

1. Chargez les dépendances de AlphaFold3.

```bash
module load StdEnv/2023 hmmer/3.4 rdkit/2024.03.5 python/3.12
```

2. Téléchargez le script d'exécution.

```bash
wget https://raw.githubusercontent.com/google-deepmind/alphafold3/refs/tags/v3.0.1/run_alphafold.py
```

```bash
wget https://raw.githubusercontent.com/google-deepmind/alphafold3/23e3d46d4ca126e8731e8c0cbb5673e9a848ceb5/run_alphafold.py
```

3. Créez et activez un environnement virtuel Python.

```bash
virtualenv --no-download ~/alphafold3_env
source ~/alphafold3_env/bin/activate
```

4. Installez une version de AlphaFold3 ainsi que ses dépendances Python.

```bash
(alphafold3_env) [name@server ~]$ pip install --no-index --upgrade pip
(alphafold3_env) [name@server ~]$ pip install --no-index alphafold3==X.Y.Z
```
où `X.Y.Z` est la version spécifique, par exemple `3.0.0`.
N'entrez pas le numéro de la version si vous voulez installer la plus récente.

5. Compilez les données nécessaires.

```bash
(alphafold3_env) [name@server ~]$ build_data
```
Ceci crée des fichiers de données dans l'environnement virtuel.

6. Validez.

```bash
(alphafold3_env) [name@server ~]$ python run_alphafold.py --help
```

7. Geler l'environnement et l'ensemble des dépendances.

```bash
(alphafold3_env) [name@server ~]$ pip freeze > ~/alphafold3-requirements.txt
```

8. Désactivez l'environnement.

```bash
(alphafold3_env) [name@server ~]$ deactivate
```

9. Nettoyer et supprimer l'environnement virtuel.

```bash
rm -r ~/alphafold3_env
```

L'environnement virtuel sera plutôt créé dans votre tâche.

## Modèle
Vous pouvez obtenir le modèle en en faisant la demande à Google. Ils s'efforcent de répondre aux demandes dans un délai de 2 à 3 jours ouvrables.
Veuillez consulter la page `Obtaining Model Parameters` sur [GitHub](https://github.com/google-deepmind/alphafold3?tab=readme-ov-file).

## Bases de données
AlphaFold3 nécessite un ensemble de bases de données.

**Important :** Les bases de données doivent résider dans le répertoire `$SCRATCH`.

1. Téléchargez le script de téléchargement.

```bash
wget https://raw.githubusercontent.com/google-deepmind/alphafold3/refs/heads/main/fetch_databases.sh
```

2. Téléchargez les bases de données.

```bash
mkdir -p $SCRATCH/alphafold/dbs
bash fetch_databases.sh $SCRATCH/alphafold/dbs
```

## Exécution par étapes
AlphaFold3 doit être [exécuté par étapes](https://github.com/google-deepmind/alphafold3/blob/main/docs/performance.md#running-the-pipeline-in-stages), c'est-à-dire :
1. séparer le pipeline de données (pour CPU seulement) et le modèle d'inférence (qui demande un GPU) pour optimiser les coûts et l'utilisation des ressources;
2. cacher les résultats de la recherche de MSA/modèle, pour ensuite réutiliser le JSON augmenté pour plusieurs inférences différentes ou pour des variations d'autres fonctionnalités (par exemple, un ligand).

Pour des références, consultez :
* [entrées](https://github.com/google-deepmind/alphafold3/blob/main/docs/input.md)
* [sorties](https://github.com/google-deepmind/alphafold3/blob/main/docs/output.md)
* [performance](https://github.com/google-deepmind/alphafold3/blob/main/docs/performance.md)

### 1. Pipeline de données (CPU)
Modifiez le script suivant selon vos besoins.

```bash title="alphafold3-data.sh"
#!/bin/bash

#SBATCH --job-name=alphafold3-data
#SBATCH --account=def-someprof    # ajustez ceci pour correspondre au groupe comptable que vous utilisez pour soumettre des tâches
#SBATCH --time=08:00:00           # ajustez ceci pour correspondre au temps d'exécution de votre tâche
#SBATCH --cpus-per-task=8         # un MAXIMUM de 8 cœurs, AlphaFold ne tire aucun avantage à en utiliser plus
#SBATCH --mem=64G                 # ajustez ceci en fonction de la mémoire dont vous avez besoin

# Charger les dépendances des modules.
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
    --norun_inference  # Exécutez l'étape des données

# recopiez
mkdir $SCRATCH/alphafold/output
cp -vr $OUTPUT_DIR $SCRATCH/alphafold/output
```

### 2. Inférence de modèle
Modifiez le script suivant selon vos besoins.

!!! warning "Compatibilité"
    AlphaFold3 prend en charge seulement la capacité de calcul des versions 8.0 et plus récentes, soit pour des **A100s et plus performants**.

```bash title="alphafold3-inference.sh"
#!/bin/bash

#SBATCH --job-name=alphafold3-inference
#SBATCH --account=def-someprof    # ajustez ceci pour correspondre au groupe comptable que vous utilisez pour soumettre des tâches
#SBATCH --time=08:00:00           # ajustez ceci pour correspondre au temps d'exécution de votre tâche
#SBATCH --cpus-per-task=1         # AlphaFold n'a aucun avantage à en utiliser plus pour l'étape d'inférence
#SBATCH --gpus=a100:1             # L'inférence d'AlphaFold3 ne s'exécute que sur UNE A100 ou plus.
#SBATCH --mem=20G                 # ajustez ceci en fonction de la mémoire dont vous avez besoin

# Charger les dépendances des modules.
module load StdEnv/2023 hmmer/3.4 rdkit/2024.03.5 python/3.12 cuda/12.2 cudnn/9.2

DOWNLOAD_DIR=$SCRATCH/alphafold/dbs    # définissez le chemin approprié vers vos données téléchargées
INPUT_DIR=$SCRATCH/alphafold/input     # définissez le chemin approprié vers vos données d'entrée, suite à l'étape de données.
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
Si vous voulez exécuter AlphaFold3 avec plus de 5120 jetons ou sur un GPU avec moins de mémoire (par exemple, sur un A100 avec 40 Go de mémoire), vous pouvez activer la fonctionnalité de [mémoire unifiée](https://github.com/google-deepmind/alphafold3/blob/main/docs/performance.md#unified-memory).

Dans le script de soumission à l'étape d'inférence, ajoutez les variables d'environnement suivantes :

```bash
export XLA_PYTHON_CLIENT_PREALLOCATE=false
export TF_FORCE_UNIFIED_MEMORY=true
export XLA_CLIENT_MEM_FRACTION=2.0  # 2 x 40GB = 80 GB
```

et ajustez en conséquence la quantité de mémoire allouée à la tâche, par exemple `#SBATCH --mem=80G`.