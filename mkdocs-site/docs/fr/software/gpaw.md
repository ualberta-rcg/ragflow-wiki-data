---
title: "GPAW/fr"
slug: "gpaw"
lang: "fr"

source_wiki_title: "GPAW/fr"
source_hash: "5ce867f729432c54db57cd5141f06f9d"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T06:42:46.419975+00:00"

tags:
  - software
  - computationalchemistry

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

## Description
[GPAW](https://wiki.fysik.dtu.dk/gpaw/) est un code de théorie de la fonctionnelle de la densité (DFT) [Python](python.md) basé sur la méthode des ondes augmentées par projecteur (PAW) et l'environnement de simulation atomique (ASE).

## Créer un environnement virtuel GPAW
Nous offrons des [wheels Python disponibles](available-python-wheels.md) précompilés pour GPAW qui peuvent être installés dans un [environnement virtuel Python](python.md#creer-et-utiliser-un-environnement-virtuel-python).

1.  Vérifiez quelles versions sont disponibles.
    ```bash
    [name@server ~]$ avail_wheels gpaw
    name    version    python    arch
    ------  ---------  --------  ------
    gpaw    22.8.0     cp39      avx2
    gpaw    22.8.0     cp38      avx2
    gpaw    22.8.0     cp310     avx2
    ```

2.  Chargez un module Python (ici python/3.10)
    ```bash
    (ENV) [name@server ~]$ module load python/3.10
    ```

3.  Créez un nouvel environnement virtuel.
    ```bash
    [name@server ~]$ virtualenv --no-download venv_gpaw
    created virtual environment CPython3.10.2.final.0-64 in 514ms
    [...]
    ```

4.  Activez l'environnement virtuel (venv).
    ```bash
    [name@server ~]$ source venv_gpaw/bin/activate
    ```

5.  Installez gpaw dans venv.
    ```bash
    (venv_gpaw) [name@server ~]$ pip install --no-index gpaw
    [...]
    Successfully installed ... gpaw-22.8.0+computecanada ...
    ```

6.  Téléchargez les données et installez-les dans le système de fichiers SCRATCH.
    ```bash
    (venv_gpaw) [name@server ~]$ gpaw install-data $SCRATCH 
    Available setups and pseudopotentials
      [*] https://wiki.fysik.dtu.dk/gpaw-files/gpaw-setups-0.9.20000.tar.gz
    [...]
    Setups installed into /scratch/name/gpaw-setups-0.9.20000.
    Register this setup path in /home/name/.gpaw/rc.py? [y/n] n
    As you wish.
    [...]
    Installation complete.
    ```

7.  Configurez GPAW_SETUP_PATH pour pointer vers le répertoire des données.
    ```bash
    (venv_gpaw) [name@server ~]$ export GPAW_SETUP_PATH=$SCRATCH/gpaw-setups-0.9.20000
    ```

8.  Lancez les tests, qui sont très rapides.
    ```bash
    (venv_gpaw) [name@server ~]$ gpaw test
     ------------------------------------------------------------------------------------------------------------
    | python-3.10.2     /home/name/venv_gpaw/bin/python                                                         |
    | gpaw-22.8.0       /home/name/venv_gpaw/lib/python3.10/site-packages/gpaw/                                 |
    | ase-3.22.1        /home/name/venv_gpaw/lib/python3.10/site-packages/ase/                                  |
    | numpy-1.23.0      /home/name/venv_gpaw/lib/python3.10/site-packages/numpy/                                |
    | scipy-1.9.3       /home/name/venv_gpaw/lib/python3.10/site-packages/scipy/                                |
    | libxc-5.2.3       yes                                                                                     |
    | _gpaw             /home/name/venv_gpaw/lib/python3.10/site-packages/_gpaw.cpython-310-x86_64-linux-gnu.so |
    | MPI enabled       yes                                                                                     |
    | OpenMP enabled    yes                                                                                     |
    | scalapack         yes                                                                                     |
    | Elpa              no                                                                                      |
    | FFTW              yes                                                                                     |
    | libvdwxc          no                                                                                      |
    | PAW-datasets (1)  /scratch/name/gpaw-setups-0.9.20000                                                     |
     -----------------------------------------------------------------------------------------------------------
    Doing a test calculation (cores: 1): ... Done
    Test parallel calculation with "gpaw -P 4 test".
    ```

    ```bash
    (venv_gpaw) [name@server ~]$ gpaw -P 4 test
     ------------------------------------------------------------------------------------------------------------
    | python-3.10.2     /home/name/venv_gpaw/bin/python                                                         |
    | gpaw-22.8.0       /home/name/venv_gpaw/lib/python3.10/site-packages/gpaw/                                 |
    | ase-3.22.1        /home/name/venv_gpaw/lib/python3.10/site-packages/ase/                                  |
    | numpy-1.23.0      /home/name/venv_gpaw/lib/python3.10/site-packages/numpy/                                |
    | scipy-1.9.3       /home/name/venv_gpaw/lib/python3.10/site-packages/scipy/                                |
    | libxc-5.2.3       yes                                                                                     |
    | _gpaw             /home/name/venv_gpaw/lib/python3.10/site-packages/_gpaw.cpython-310-x86_64-linux-gnu.so |
    | MPI enabled       yes                                                                                     |
    | OpenMP enabled    yes                                                                                     |
    | scalapack         yes                                                                                     |
    | Elpa              no                                                                                      |
    | FFTW              yes                                                                                     |
    | libvdwxc          no                                                                                      |
    | PAW-datasets (1)  /scratch/name/gpaw-setups-0.9.20000                                                     |
     -----------------------------------------------------------------------------------------------------------
    Doing a test calculation (cores: 4): ... Done
    ```

Les résultats du dernier test se trouvent dans le fichier `test.txt` qui se trouvera dans le répertoire courant.

## Exemple de script
Le script suivant est un exemple de parallélisation hybride OpenMP et MPI. Ici, virtualenv se trouve dans votre répertoire $HOME et les ensembles de données sont dans $SCRATCH comme ci-dessus.

```bash title="job_gpaw.sh"
#!/bin/bash
#SBATCH --ntasks=8
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=4000M
#SBATCH --time=0-01:00
module load gcc/9.3.0 openmpi/4.0.3
source ~/venv_gpaw/bin/activate

export OMP_NUM_THREADS="${SLURM_CPUS_PER_TASK:-1}"
export GPAW_SETUP_PATH=/scratch/$USER/gpaw-setups-0.9.20000

srun --cpus-per-task=$OMP_NUM_THREADS gpaw python my_gpaw_script.py
```
Le script utilise un nœud simple avec 8 rangs MPI (ntasks) et 4 fils OpenMP par rang MPI pour un total de 32 CPU. Vous voudrez probablement modifier ces valeurs pour que le produit corresponde au nombre de cœurs d'un nœud entier (soit 32 sur [Graham](graham.md), 40 sur [Béluga](beluga.md) et [Niagara](niagara.md), 48 sur [Cedar](cedar.md) ou 64 sur [Narval](narval.md)).

Le fait de configurer `OMP_NUM_THREADS` comme expliqué ci-dessus fait en sorte qu'il a toujours la même valeur que cpus-per-task ou 1 quand cpus-per-task n'est pas défini. Le chargement des modules `gcc/9.3.0` et `openmpi/4.0.3` fait en sorte que la bonne bibliothèque MPI est utilisée pour la tâche, la même qui a été utilisée pour construire les wheels.