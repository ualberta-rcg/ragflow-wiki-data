---
title: "Parasail/fr"
slug: "parasail"
lang: "fr"

source_wiki_title: "Parasail/fr"
source_hash: "ddd4e6b957abb53c9333fd759cea1ac4"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T09:52:53.447386+00:00"

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

[parasail](https://github.com/jeffdaily/parasail) est une bibliothèque SIMD C (C99) qui contient des implémentations d'algorithmes d'alignement de séquences par paires Smith-Waterman (alignement local), Needleman-Wunsch (alignement global) et autres alignements semi-globaux.

!!! note
    Depuis StdEnv/2023, l'extension parasail-python fait partie du module parasail. Avec StdEnv/2020, le module doit cependant être chargé pour que l'extension Python soit installée dans un environnement virtuel.

## Utilisation

Pour connaître la version disponible, utilisez

```bash
module spider parasail
```

Chargez la bibliothèque avec

```bash
module load parasail/2.6.2
```

### Avec le binaire `parasail_aligner`

Il est important de définir le nombre de fils selon le nombre de cœurs alloués à votre tâche, par exemple

```bash
parasail_aligner -t ${SLURM_CPUS_PER_TASK:-1} ...
```

## Extension Python

Le module contient des liaisons pour plusieurs versions de Python.
Pour connaître les versions compatibles de Python, lancez

```bash
module spider parasail/1.3.4
```

### Utiliser l'extension

1.  Chargez les modules requis.
    ```bash
    module load parasail/2.6.2 python/3.11 scipy-stack/2023b
    ```

2.  Importez parasail 1.3.4.
    ```bash
    python -c "import parasail"
    ```

L'importation est réussie quand la commande ne retourne rien.

### Exemple

Comparez les résultats d'un alignement local avec BioPython et parasail.

1.  Préparez le script Python.
    ```python title="parasail-sw.py"
    import parasail
    from Bio.Align import PairwiseAligner

    A = "ACGT" * 1000

    # parasail
    matrix = parasail.matrix_create("ACGT", 1, 0)
    parasail_score = parasail.sw(A, A, 1, 1, matrix).score

    # biopython
    bio_score = PairwiseAligner().align(A, A)[0].score

    print('parasail:', parasail_score)
    print('biopython:', bio_score)
    ```

2.  Préparez le script de soumission selon votre environnement.

=== "StdEnv par défaut"

    ```sh title="submit-parasail.sh"
    #!/bin/bash
    #SBATCH --account=def-someuser  # replace with your PI account
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=3G      # increase as needed
    #SBATCH --time=1:00:00

    module load parasail/2.6.2 python/3.11 scipy-stack/2023b

    # Install any other requirements, such as Biopython
    virtualenv --no-download $SLURM_TMPDIR/env
    source $SLURM_TMPDIR/env/bin/activate
    pip install --no-index --upgrade pip
    pip install --no-index biopython==1.83

    python parasail-sw.py
    ```

=== "StdEnv/2020"

    2.1. Identifiez les versions disponibles :
    ```bash
    avail_wheel parasail
    ```
    ```text
    name      version    python    arch
    --------  ---------  --------  -------
    parasail  1.2.4      py2,py3   generic
    ```

    Installez maintenant la version choisie dans votre environnement virtuel.
    ```sh title="submit-parasail.sh"
    #!/bin/bash
    #SBATCH --account=def-someuser  # replace with your PI account
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=3G      # increase as needed
    #SBATCH --time=1:00:00

    module load StdEnv/2020 gcc parasail/2.5 python/3.10

    # Install any other requirements, such as Biopython
    virtualenv --no-download $SLURM_TMPDIR/env
    source $SLURM_TMPDIR/env/bin/activate
    pip install --no-index --upgrade pip
    pip install --no-index parasail==1.2.4 biopython==1.83

    python parasail-sw.py
    ```

3.  Soumettez la tâche avec
    ```bash
    sbatch submit-parasail.sh
    ```

4.  Une fois la tâche terminée, vérifiez le résultat dans le fichier de sortie de l'ordonnanceur Slurm.
    ```bash
    less slurm-*.out
    ```
    ```text
    parasail: 4000
    biopython: 4000.0
    ```

#### Paquets Python disponibles

Les exigences des paquets Python qui dépendent de parasail seront satisfaites en chargeant le module parasail.
```bash
pip list | grep parasail
```
```text
parasail                           1.3.4