---
title: "VirSorter2/fr"
slug: "virsorter2"
lang: "fr"

source_wiki_title: "VirSorter2/fr"
source_hash: "92ab2b4043dc07d4b17d6b1c6b502eea"
last_synced: "2026-08-26T10:16:11.334907+00:00"
last_processed: "2026-08-26T11:23:01.746627+00:00"

tags:
  - software

keywords:
  - "environnement virtuel Python"
  - "--min-length 1500"
  - "installation via pip"
  - "test réussi"
  - "sbatch"
  - "base de données"
  - "script d'ordonnancement"
  - "salloc"
  - "--mem-per-cpu 2G"
  - "allocation"
  - "submission script"
  - "ensemble de données"
  - "virsorter"
  - "VirSorter2"

questions:
  - "Quelles sont les étapes détaillées pour installer VirSorter2 v2.2.4 dans un environnement virtuel Python sur le serveur ?"
  - "Comment préparer le jeu de données de test, créer le script d’exécution et soumettre une tâche VirSorter2 avec le planificateur SLURM ?"
  - "Pourquoi est‑il important de citer VirSorter2 dans vos travaux et comment le faire correctement ?"
  - "Quel rôle joue la commande `exit` dans le contexte d’une allocation `salloc` ?"
  - "Que signifie le message « salloc: Relinquishing job allocation 1234567 » affiché après l’exécution de la commande `exit` ?"
  - "Comment utiliser la commande `sbatch` pour soumettre une tâche avec votre propre jeu de données une fois le test réussi ?"
  - "Quelle rôle joue l’option `--min-length 1500` dans la commande `virsorter` ?"
  - "Comment la commande `salloc` alloue‑t‑elle la mémoire et les CPU pour la tâche interactive ?"
  - "Pourquoi la commande inclut‑elle `--use-conda-off` et quel est l’intérêt de spécifier `--db-dir $SCRATCH/db` ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

L'outil [VirSorter2](https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-020-00990-y) permet d’identifier les nouvelles séquences de virus.

Nous abordons ici l’installation et l’utilisation de VirSorter2 v2.2.4.

Le code source et la documentation pour VirSorter2 se trouvent sur leur [page GitHub](https://github.com/jiarong/VirSorter2).

N’oubliez pas de [citer VirSorter2](https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-020-00990-y#citeas) si vous l’utilisez pour vos analyses.

## Installation dans un environnement virtuel Python
Les étapes ci-dessous servent à installer VirSorter2 dans votre répertoire `$HOME` avec nos [wheels Python](http://pythonwheels.com/) préconstruits. Les wheels personnalisés se trouvent dans `/cvmfs/soft.computecanada.ca/custom/python/wheelhouse/`. Pour installer un wheel VirSorter2 dans un [environnement virtuel Python](python.md), nous utilisons la commande `pip`.

1.  Chargez les modules nécessaires.
    ```bash
    module load StdEnv/2020 python/3.8 hmmer/3.3.2 prodigal/2.6.3
    ```

2.  Créez et activez un environnement virtuel Python.
    ```bash
    virtualenv --no-download ~/ENV_virsorter
    source ~/ENV_virsorter/bin/activate
    ```

3.  Installez VirSorter2 v2.2.4 dans l’environnement virtuel.
    ```bash
    pip install --no-index --upgrade 'pip<25'
    pip install --no-index virsorter==2.2.4
    ```

4.  Validez l'installation.
    ```bash
    virsorter -h
    ```

5.  Gelez l’environnement et les éléments requis (*requirements.txt*).
    ```bash
    pip freeze > ~/virsorter-2.2.4-requirements.txt
    ```

6.  Téléchargez la base de données dans votre répertoire `$SCRATCH` en utilisant l'option `--skip-deps-install` pour ne pas installer conda et aussi parce que les dépendances sont déjà installées.
    ```bash
    virsorter setup --db-dir $SCRATCH/db -j 4 --skip-deps-install
    ```

## Tester VirSorter2
1.  Désactivez votre environnement virtuel.
    ```bash
    deactivate
    ```

2.  Téléchargez l’ensemble de données dans votre répertoire `$SCRATCH`.
    ```bash
    wget -O $SCRATCH/test.fa https://raw.githubusercontent.com/jiarong/VirSorter2/master/test/8seq.fa
    ```

3.  Créez un script pour soumettre une tâche à l’ordonnanceur.
    ```bash title="test-virsorter.sh"
    #!/bin/bash

    #SBATCH --time=00:30:00
    #SBATCH --mem-per-cpu=2G
    #SBATCH --cpus-per-task=2

    # Load modules dependencies
    module load StdEnv/2020 python/3.8 hmmer/3.3.2 prodigal/2.6.3

    # Generate your virtual environment in $SLURM_TMPDIR
    virtualenv --no-download $SLURM_TMPDIR/ENV
    source $SLURM_TMPDIR/ENV/bin/activate
    pip install --no-index --upgrade pip

    # Install VirSorter2 and its dependencies
    pip install --no-index -r ~/virsorter-2.2.4-requirements.txt

    # Run VirSorter2 with the test dataset, using at most $SLURM_CPUS_PER_TASK and ignore conda.
    # The database must already exist and you must specify its location.
    virsorter run -w $SCRATCH/test.out -i $SCRATCH/test.fa --min-length 1500 -j $SLURM_CPUS_PER_TASK --verbose --use-conda-off --db-dir $SCRATCH/db all
    ```

4.  Lancez une tâche interactive.
    ```bash
    salloc --mem-per-cpu=2G --cpus-per-task=2 --account=<votre-compte>
    ```
    ```text
    salloc: Granted job allocation 1234567
    $ bash test-virsorter.sh             # Exécute le script de soumission
    $ exit                               # Met fin à l'allocation
    salloc: Relinquishing job allocation 1234567
    ```

Si le test est réussi, vous pouvez utiliser la commande `sbatch` pour soumettre une tâche avec votre propre ensemble de données.