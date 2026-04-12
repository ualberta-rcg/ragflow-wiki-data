---
title: "VirSorter2/fr"
slug: "virsorter2"
lang: "fr"

source_wiki_title: "VirSorter2/fr"
source_hash: "9f177cf2db0e8fecd29d8b9f8419f01b"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:41:36.468234+00:00"

tags:
  - software

keywords:
  - "séquences de virus"
  - "salloc"
  - "virsorter"
  - "submission script"
  - "allocation"
  - "base de données"
  - "tâche interactive"
  - "job allocation"
  - "soumettre une tâche"
  - "sbatch"
  - "environnement virtuel Python"
  - "ensemble de données"
  - "installation"
  - "VirSorter2"

questions:
  - "À quoi sert l'outil VirSorter2 selon le texte ?"
  - "Quelles sont les étapes requises pour installer VirSorter2 et sa base de données dans un environnement virtuel Python ?"
  - "Comment doit-on procéder pour configurer et exécuter une tâche de test pour VirSorter2 via l'ordonnanceur ?"
  - "Quelle commande permet de terminer une allocation de ressources en cours ?"
  - "Quelle condition préalable est nécessaire avant de soumettre une tâche avec son propre ensemble de données ?"
  - "À quoi sert la commande sbatch dans ce contexte ?"
  - "Quels sont les paramètres et les chemins d'accès spécifiés pour configurer l'exécution de la commande `virsorter run` ?"
  - "Quelle commande SLURM permet de demander les ressources nécessaires pour lancer une tâche interactive ?"
  - "De quelle manière le script de soumission final (`test-virsorter.sh`) est-il exécuté une fois l'allocation obtenue ?"
  - "Quelle commande permet de terminer une allocation de ressources en cours ?"
  - "Quelle condition préalable est nécessaire avant de soumettre une tâche avec son propre ensemble de données ?"
  - "À quoi sert la commande sbatch dans ce contexte ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[VirSorter2](https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-020-00990-y) permet d’identifier les nouvelles séquences de virus.

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
    pip install --no-index --upgrade pip
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
    ```
    salloc: Granted job allocation 1234567
    ```
    ```bash
    bash test-virsorter.sh # Exécutez le script de soumission
    ```
    ```bash
    exit                   # Terminez l'allocation
    ```
    ```
    salloc: Relinquishing job allocation 1234567
    ```

Si le test est réussi, vous pouvez utiliser la commande `sbatch` pour soumettre une tâche avec votre propre ensemble de données.