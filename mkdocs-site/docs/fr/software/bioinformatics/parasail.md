---
title: "Parasail/fr"
slug: "parasail"
lang: "fr"

source_wiki_title: "Parasail/fr"
source_hash: "ddd4e6b957abb53c9333fd759cea1ac4"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:21:06.977048+00:00"

tags:
  []

keywords:
  - "Slurm"
  - "fichier de sortie"
  - "pip list"
  - "module parasail"
  - "extension Python"
  - "parasail"
  - "sbatch"
  - "alignement de séquences"
  - "biopython"
  - "bibliothèque SIMD C"
  - "paquets Python"
  - "BioPython"

questions:
  - "Qu'est-ce que la bibliothèque parasail et quels types d'algorithmes d'alignement de séquences propose-t-elle ?"
  - "Comment doit-on configurer le nombre de fils d'exécution lors de l'utilisation du binaire parasail_aligner dans une tâche Slurm ?"
  - "Quelles sont les étapes requises pour configurer et utiliser l'extension Python de parasail dans un environnement virtuel selon la version de StdEnv ?"
  - "Quels sont les paquets Python spécifiques mentionnés comme étant disponibles dans le système ?"
  - "Comment les dépendances des paquets nécessitant parasail sont-elles gérées ou satisfaites ?"
  - "Quelle commande doit-on utiliser pour vérifier la présence et la version du paquet parasail ?"
  - "Quelles sont les dépendances Python requises pour exécuter le script parasail-sw.py ?"
  - "Quelle commande permet de soumettre la tâche à l'ordonnanceur Slurm ?"
  - "Comment l'utilisateur peut-il consulter les résultats une fois l'exécution de la tâche terminée ?"
  - "Quels sont les paquets Python spécifiques mentionnés comme étant disponibles dans le système ?"
  - "Comment les dépendances des paquets nécessitant parasail sont-elles gérées ou satisfaites ?"
  - "Quelle commande doit-on utiliser pour vérifier la présence et la version du paquet parasail ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[parasail](https://github.com/jeffdaily/parasail) est une bibliothèque SIMD C (C99) qui contient des implémentations d'algorithmes d'alignement de séquences par paires Smith-Waterman (alignement local), Needleman-Wunsch (alignement global) et d'autres alignements semi-globaux.

!!! note
    Depuis StdEnv/2023, l'extension parasail-python fait partie du module parasail. Avec StdEnv/2020, le module doit cependant être chargé pour que l'extension Python soit installée dans un environnement virtuel.

## Utilisation

Pour connaître la version disponible, utilisez :

```bash
module spider parasail
```

Chargez la bibliothèque avec :

```bash
module load parasail/2.6.2
```

## Avec le binaire `parasail_aligner`

Il est important de définir le nombre de fils selon le nombre de cœurs alloués à votre tâche, par exemple :

```bash
parasail_aligner -t ${SLURM_CPUS_PER_TASK:-1} ...
```

## Extension Python

Le module contient des liaisons pour plusieurs versions de Python.
Pour connaître les versions compatibles de Python, lancez :

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
        #SBATCH --account=def-someuser  # remplacer par votre compte de projet de recherche
        #SBATCH --cpus-per-task=1
        #SBATCH --mem-per-cpu=3G      # augmentez au besoin
        #SBATCH --time=1:00:00

        module load parasail/2.6.2 python/3.11 scipy-stack/2023b

        # Installez toute autre dépendance, comme Biopython
        virtualenv --no-download $SLURM_TMPDIR/env
        source $SLURM_TMPDIR/env/bin/activate
        pip install --no-index --upgrade pip
        pip install --no-index biopython==1.83

        python parasail-sw.py
        ```

    === "StdEnv/2020"

        2.1. Identifiez d'abord les roues disponibles :

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
        #SBATCH --account=def-someuser  # remplacer par votre compte de projet de recherche
        #SBATCH --cpus-per-task=1
        #SBATCH --mem-per-cpu=3G      # augmentez au besoin
        #SBATCH --time=1:00:00

        module load StdEnv/2020 gcc parasail/2.5 python/3.10

        # Installez toute autre dépendance, comme Biopython
        virtualenv --no-download $SLURM_TMPDIR/env
        source $SLURM_TMPDIR/env/bin/activate
        pip install --no-index --upgrade pip
        pip install --no-index parasail==1.2.4 biopython==1.83

        python parasail-sw.py
        ```

3.  Soumettez la tâche avec :

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