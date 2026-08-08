---
title: "AlphaFold3/fr"
slug: "alphafold3"
lang: "fr"

source_wiki_title: "AlphaFold3/fr"
source_hash: "a96505d0584f1343a9d7c6b3f6de2ed1"
last_synced: "2026-08-07T19:46:17.777436+00:00"
last_processed: "2026-08-07T22:14:54.716025+00:00"

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

1. Chargez les dépendances de AlphaFold3.
```bash
module load StdEnv/2023 hmmer-alphafold3/3.4 rdkit/2025.09.4 python/3.12
```

Les différentes versions d'AlphaFold3 requièrent différentes versions de RDKit. Si un message d'erreur s'affiche à l'installation du paquet Python `alphafold3` (voir ci-dessous), téléchargez de nouveau le module `rdkit` avec la version mentionnée dans le message d'erreur.

2. Téléchargez le script d'exécution.

   === "3.0.4"
       ```bash
       wget https://raw.githubusercontent.com/google-deepmind/alphafold3/refs/tags/v3.0.4/run_alphafold.py
       ```
   === "3.0.2"
       ```bash
       wget https://raw.githubusercontent.com/google-deepmind/alphafold3/refs/tags/v3.0.2/run_alphafold.py
       ```
   === "3.0.1"
       ```bash
       wget https://raw.githubusercontent.com/google-deepmind/alphafold3/refs/tags/v3.0.1/run_alphafold.py
       ```
   === "3.0.0"
       ```bash
       wget https://raw.githubusercontent.com/google-deepmind/alphafold3/23e3d46d4ca126e8731e8c0cbb5673e9a848ceb5/run_alphafold.py
       ```

3. Créez et activez un environnement virtuel Python.
```bash
virtualenv --no-download ~/alphafold3_env
source ~/alphafold3_env/bin/activate
```

4. Installez une version de AlphaFold3 ainsi que ses dépendances Python
```bash
pip install --no-index --upgrade pip
pip install --no-index alphafold3==X.Y.Z
```
où `X.Y.Z` est la version spécifique, par exemple `3.0.4`.
N'entrez pas le numéro de la version si vous voulez installer la plus récente.

5. Compilez les données nécessaires.
```bash
build_data
```
Ceci crée des fichiers de données dans l'environnement virtuel.

6. Validez.
```bash
python run_alphafold.py --help
```

7. Gelez l'environnement et l'ensemble des requis.
```bash
pip freeze > ~/alphafold3-requirements.txt
```

8. Désactivez l'environnement.
```bash
deactivate
```

9. Nettoyez et supprimez l'environnement virtuel.
```bash
rm -r ~/alphafold3_env
```

L'environnement virtuel sera plutôt créé dans votre tâche.

## Modèle
AlphaFold3 utilise des paramètres de modèle pour l'inférence. Avant de télécharger le modèle, il faut accepter les conditions d'utilisation; voir [les conditions d'utilisation](https://github.com/google-deepmind/alphafold3/blob/main/WEIGHTS_TERMS_OF_USE.md).

!!! attention "Important"
    Les paramètres du modèle doivent résider dans votre répertoire `$SCRATCH`.

Téléchargez le modèle avec

```bash
mkdir -p $SCRATCH/alphafold/models
wget https://storage.googleapis.com/alphafold3/af3.bin.zst -P $SCRATCH/alphafold/models/
```

## Bases de données
AlphaFold3 utilise un ensemble de bases de données pour son pipeline de données.

!!! attention "Important"
    Les bases de données doivent résider dans votre répertoire `$SCRATCH`.

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
Alphafold3 doit être [exécuté par étapes](https://github.com/google-deepmind/alphafold3/blob/main/docs/performance.md#running-the-pipeline-in-stages), c'est-à-dire
1. séparer le pipeline de données pour CPU seulement et le modèle d'inférence (qui demande un GPU) pour optimiser les coûts et l'utilisation des ressources;
2. cacher les résultats de la recherche de MSA/modèle, pour ensuite réutiliser le JSON augmenté pour plusieurs différentes inférences ou pour des variations d'autres fonctionnalités (par exemple un ligand).

Pour des références, voir
* [inputs](https://github.com/google-deepmind/alphafold3/blob/main/docs/input.md)
* [outputs](https://github.com/google-deepmind/alphafold3/blob/main/docs/output.md)
* [performance](https://github.com/google-deepmind/alphafold3/blob/main/docs/performance.md)

L'exemple suivant montre comment replier une protéine homodimère de 70kDa (identifiant PDB [2PV7](https://www.rcsb.org/structure/2PV7)). Il s'agit du [même exemple](https://github.com/google-deepmind/alphafold3/tree/main#installation-and-running-your-first-prediction) que celui fourni dans la documentation d'AlphaFold3, mais adapté à nos grappes et divisé en deux étapes.

### Fichier d'entrée

Créez un répertoire pour le fichier d'entrée.

```bash
mkdir -p $SCRATCH/alphafold/input
```

Dans le nouveau répertoire, ajoutez le fichier d'entrée suivant.

```json title="fold_input.json"
{
  "name": "2PV7",
  "sequences": [
    {
      "protein": {
        "id": ["A", "B"],
        "sequence": "GMRESYANENQFGFKTINSDIHKIVIVGGYGKLGGLFARYLRASGYPISILDREDWAVAESILANADVVIVSVPINLTLETIERLKPYLTENMLLADLTSVKREPLAKMLEVHTGAVLGLHPMFGADIASMAKQVVVRCDGRFPERYEWLLEQIQIWGAKIYQTNATEHDHNMTYIQALRHFSTFANGLHLSKQPINLANLLALSSPIYRLELAMIGRLFAQDAELYADIIMDKSENLAVIETLKQTYDEALTFFENNDRQGFIDAFHKVRDWFGDYSEQFLKESRQLLQQANDLKQG"
      }
    }
  ],
  "modelSeeds": [1],
  "dialect": "alphafold3",
  "version": 1
}
```

### Pipeline de données (CPU)
Modifiez le script de tâche selon vos besoins.
```bash title="alphafold3-data.sh"
#!/bin/bash

#SBATCH --job-name=alphafold3-data
#SBATCH --account=def-someprof    # ajustez à votre groupe de compte
#SBATCH --time=08:00:00           # ajustez à la durée maximale de votre tâche
#SBATCH --cpus-per-task=8         # UN MAXIMUM de 8 cœurs, AlphaFold ne tire aucun avantage à en utiliser davantage
#SBATCH --mem=64G                 # ajustez selon la mémoire dont vous avez besoin

# Chargez les dépendances des modules.
module load StdEnv/2023 hmmer-alphafold3/3.4 rdkit/2024.03.5 python/3.12

DOWNLOAD_DIR=$SCRATCH/alphafold/dbs    # définissez le chemin approprié vers vos données téléchargées
INPUT_DIR=$SCRATCH/alphafold/input     # définissez le chemin approprié vers vos données d'entrée
OUTPUT_DIR=$SLURM_TMPDIR/alphafold/output   # définissez le chemin approprié vers vos données de sortie

# Générez votre environnement virtuel dans $SLURM_TMPDIR.
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate

# Installez AlphaFold et ses dépendances.
pip install --no-index --upgrade pip
pip install --no-index --requirement ~/alphafold3-requirements.txt

# construisez les données dans $VIRTUAL_ENV
build_data

# https://github.com/google-deepmind/alphafold3/blob/main/docs/performance.md#compilation-time-workaround-with-xla-flags
export XLA_FLAGS="--xla_gpu_enable_triton_gemm=false"

# Modifiez avec les arguments appropriés et exécutez vos commandes.
# run_alphafold.py --help
python run_alphafold.py \
    --db_dir=$DB_DIR \
    --input_dir=$INPUT_DIR \
    --output_dir=$OUTPUT_DIR \
    --jax_compilation_cache_dir=$HOME/.cache \
    --nhmmer_n_cpu=$SLURM_CPUS_PER_TASK \
    --jackhmmer_n_cpu=$SLURM_CPUS_PER_TASK \
    --norun_inference  # Exécutez l'étape de données
```

Le pipeline de données enregistre dans un sous-répertoire de `$OUTPUT_DIR`, nommé selon la balise `name` du fichier d'entrée, ici `2PV7`.

### Inférence de modèle (GPU)
Modifiez le script de tâche suivant selon vos besoins.

```bash title="alphafold3-inference.sh"
#!/bin/bash

#SBATCH --job-name=alphafold3-inference
#SBATCH --account=def-someprof  # définissez le groupe de compte que vous utilisez pour soumettre des tâches
#SBATCH --time=08:00:00         # définissez la durée maximale pour votre tâche
#SBATCH --cpus-per-task=1       # L'inférence d'AlphaFold3 utilise un seul cœur
#SBATCH --gpus=a100:1           # L'inférence d'AlphaFold3 utilise un seul GPU (A100 ou plus récent)
#SBATCH --mem=20G               # définissez la mémoire nécessaire pour votre tâche

# Chargez les dépendances des modules.
module load StdEnv/2023 hmmer-alphafold3/3.4 rdkit/2025.09.4 python/3.12 cuda/12.2 cudnn/9.2

MODEL_DIR=$SCRATCH/alphafold/models             # paramètres du modèle téléchargés
INPUT_DIR=$SCRATCH/alphafold/data-output/2PV7   # répertoire intermédiaire créé par le pipeline de données
OUTPUT_DIR=$SCRATCH/alphafold/inference-output  # répertoire de sortie final pour l'inférence
mkdir -p $OUTPUT_DIR

# Générez votre environnement virtuel dans $SLURM_TMPDIR.
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate

# Installez AlphaFold et ses dépendances.
pip install --no-index --upgrade pip
pip install --no-index --requirement ~/alphafold3-requirements.txt

# construisez les données dans $VIRTUAL_ENV
build_data

# https://github.com/google-deepmind/alphafold3/blob/main/docs/performance.md#compilation-time-workaround-with-xla-flags
export XLA_FLAGS="--xla_gpu_enable_triton_gemm=false"

# https://github.com/google-deepmind/alphafold3/blob/main/docs/performance.md#gpu-memory
export XLA_PYTHON_CLIENT_PREALLOCATE=true
export XLA_CLIENT_MEM_FRACTION=0.95

# Modifiez avec les arguments appropriés et exécutez vos commandes.
# run_alphafold.py --help
python run_alphafold.py \
    --model_dir=$MODEL_DIR \
    --input_dir=$INPUT_DIR \
    --output_dir=$OUTPUT_DIR \
    --jax_compilation_cache_dir=$HOME/.cache \
    --norun_data_pipeline  # Exécutez l'étape d'inférence
```

### Soumettre une tâche

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

et ajuster en conséquence la quantité de mémoire allouée à la tâche, par exemple `#SBATCH --mem=80G`.