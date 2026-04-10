---
title: "GPAW/fr"
tags:
  - software
  - computationalchemistry

keywords:
  []
---

__TOC__
= Description =
[GPAW](https://wiki.fysik.dtu.dk/gpaw/) est un code de théorie de la fonctionnelle de la densité (DFT) [Python](python-fr.md) basé sur
la méthode des ondes augmentées par projecteur (PAW) et l'environnement de simulation atomique (ASE).

= Créer un environnement virtuel GPAW =
Nous offrons des [wheels Python](available-python-wheels-fr.md) précompilés pour GPAW qui peuvent être installés dans un  [environnement virtuel Python](python-fr#créer_et_utiliser_un_environnement_virtuel_python.md).

1. Vérifiez quelles versions sont disponibles.

```bash
avail_wheels gpaw
```

```
name    version    python    arch
------  ---------  --------  ------
gpaw    22.8.0     cp39      avx2
gpaw    22.8.0     cp38      avx2
gpaw    22.8.0     cp310     avx2
```

2. Chargez un module Python (ici python/3.10)

```bash
module load python/3.10
```

3. Créez un nouvel environnement virtuel.

```bash
virtualenv --no-download venv_gpaw
```

```
created virtual environment CPython3.10.2.final.0-64 in 514ms
[...]
```

4. Activez l'environnement virtuel (venv).

```bash
source venv_gpaw/bin/activate
```

5. Installez gpaw dans venv.

```bash
pip install --no-index gpaw
```

```
[...]
Successfully installed ... gpaw-22.8.0+computecanada ...
```

6. Téléchargez les données et installez-les dans le système de fichiers SCRATCH.

```bash
gpaw install-data $SCRATCH
```

```
Available setups and pseudopotentials
  [*] https://wiki.fysik.dtu.dk/gpaw-files/gpaw-setups-0.9.20000.tar.gz
[...]
Setups installed into /scratch/name/gpaw-setups-0.9.20000.
Register this setup path in /home/name/.gpaw/rc.py? [y/n] n
As you wish.
[...]
Installation complete.
```

7. Configurez GPAW_SETUP_PATH pour pointer vers le répertoire des données.

```bash

```
$SCRATCH/gpaw-setups-0.9.20000
}}

8. Lancez les tests, qui sont très rapides.

```bash
gpaw test
```

```
------------------------------------------------------------------------------------------------------------

 gpaw-22.8.0       /home/name/venv_gpaw/lib/python3.10/site-packages/gpaw/                                 
 ase-3.22.1        /home/name/venv_gpaw/lib/python3.10/site-packages/ase/                                  
 numpy-1.23.0      /home/name/venv_gpaw/lib/python3.10/site-packages/numpy/                                
 scipy-1.9.3       /home/name/venv_gpaw/lib/python3.10/site-packages/scipy/                                
 libxc-5.2.3       yes                                                                                     
 _gpaw             /home/name/venv_gpaw/lib/python3.10/site-packages/_gpaw.cpython-310-x86_64-linux-gnu.so 
 MPI enabled       yes                                                                                     
 OpenMP enabled    yes                                                                                     
 scalapack         yes                                                                                     
 Elpa              no                                                                                      
 FFTW              yes                                                                                     
 libvdwxc          no                                                                                      
 PAW-datasets (1)  /scratch/name/gpaw-setups-0.9.20000                                                     
 -----------------------------------------------------------------------------------------------------------
Doing a test calculation (cores: 1): ... Done
Test parallel calculation with "gpaw -P 4 test".
}}

```bash
gpaw -P 4 test
```

```
------------------------------------------------------------------------------------------------------------

 gpaw-22.8.0       /home/name/venv_gpaw/lib/python3.10/site-packages/gpaw/                                 
 ase-3.22.1        /home/name/venv_gpaw/lib/python3.10/site-packages/ase/                                  
 numpy-1.23.0      /home/name/venv_gpaw/lib/python3.10/site-packages/numpy/                                
 scipy-1.9.3       /home/name/venv_gpaw/lib/python3.10/site-packages/scipy/                                
 libxc-5.2.3       yes                                                                                     
 _gpaw             /home/name/venv_gpaw/lib/python3.10/site-packages/_gpaw.cpython-310-x86_64-linux-gnu.so 
 MPI enabled       yes                                                                                     
 OpenMP enabled    yes                                                                                     
 scalapack         yes                                                                                     
 Elpa              no                                                                                      
 FFTW              yes                                                                                     
 libvdwxc          no                                                                                      
 PAW-datasets (1)  /scratch/name/gpaw-setups-0.9.20000                                                     
 -----------------------------------------------------------------------------------------------------------
Doing a test calculation (cores: 4): ... Done
}}

Les résultats du dernier test se trouvent dans le fichier `test.txt` qui se trouvera dans le répertoire courant.

= Exemple de script =
Le script suivant est un exemple de parallélisation hybride OpenMP et MPI.
Ici, virtualenv se trouve dans votre répertoire $HOME et les ensembles de données sont dans  $SCRATCH comme ci-dessus.
{{File
|language=bash
|name=job_gpaw.sh
|contents=
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
}}
Le scrip utilise un nœud simple avec 8 rangs MPI (ntasks) et 4 fils OpenMP par rang MPI  pour un total de 32 CPU.
Vous voudrez probablement modifier ces valeurs pour que le produit corresponde au nombre de cœurs d'un nœud entier 
(soit 32 sur [Graham](graham-fr.md), 40 sur [Béluga](béluga.md) et [Niagara](niagara-fr.md), 48 sur [Cedar](cedar-fr.md) ou 64 sur [Narval](narval.md)).

Le fait de configurer  `OMP_NUM_THREADS` comme expliqué ci-dessus fait en sorte qu'il a toujours la même valeur que cpus-per-task ou 1 quand cpus-per-task n'est pas défini.
Le chargement des modules `gcc/9.3.0` et  `openmpi/4.0.3` fait en sorte que la bonne bibliothèque MPI est utilisée pour la tâche, la même qui a été utilisée pour construire les wheels.