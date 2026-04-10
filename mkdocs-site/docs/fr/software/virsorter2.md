---
title: "VirSorter2/fr"
slug: "virsorter2"
lang: "fr"

source_wiki_title: "VirSorter2/fr"
source_hash: "9f177cf2db0e8fecd29d8b9f8419f01b"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T12:43:21.046559+00:00"

tags:
  - software

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

L'outil [VirSorter2](https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-020-00990-y) permet d’identifier les nouvelles séquences de virus.

Nous abordons ici l’installation et l’utilisation de VirSorter2 v2.2.4.

Le code source et la documentation pour VirSorter2 se trouvent sur leur [page GitHub](https://github.com/jiarong/VirSorter2).

N’oubliez pas de [citer VirSorter2](https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-020-00990-y#citeas) si vous l’utilisez pour vos analyses.

## Installation dans un environnement virtuel Python
Les étapes ci-dessous servent à installer VirSorter2 dans votre répertoire `$HOME` avec nos [wheels Python](http://pythonwheels.com/) préconstruits. Les wheels personnalisés se trouvent dans `/cvmfs/soft.computecanada.ca/custom/python/wheelhouse/`. Pour installer un wheel VirSorter2 dans un [environnement virtuel Python](python.md#créer-et-utiliser-un-environnement-virtuel-python), nous utilisons la commande `pip`.

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
    (ENV_virsorter) [name@server ~] pip install --no-index --upgrade pip
    (ENV_virsorter) [name@server ~] pip install --no-index virsorter==2.2.4
    ```
4.  Validez l'installation.
    ```bash
    (ENV_virsorter) [name@server ~] virsorter -h
    ```
5.  Gelez l’environnement et les éléments requis (*requirements.txt*).
    ```bash
    (ENV_virsorter) [name@server ~] pip freeze > ~/virsorter-2.2.4-requirements.txt
    ```
6.  Téléchargez la base de données dans votre répertoire `$SCRATCH` en utilisant l'option `--skip-deps-install` pour ne pas installer conda et aussi parce que les dépendances sont déjà installées.
    ```bash
    (ENV_virsorter) [name@server ~] virsorter setup --db-dir $SCRATCH/db -j 4 --skip-deps-install
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
    salloc --mem-per-cpu=2G --cpus-per-task=2 --account=<your-account>
    ```
    ```bash
    salloc: Granted job allocation 1234567
    $ bash test-virsorter.sh             # Exécute le script de soumission
    $ exit                               # Termine l'allocation
    salloc: Relinquishing job allocation 1234567
    ```

Si le test est réussi, vous pouvez utiliser la commande `sbatch` pour soumettre une tâche avec votre propre ensemble de données.