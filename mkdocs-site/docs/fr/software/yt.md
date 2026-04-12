---
title: "Yt/fr"
slug: "yt"
lang: "fr"

source_wiki_title: "Yt/fr"
source_hash: "e9adfcc6b2e77034e9222768a15a64ea"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T13:42:53.007517+00:00"

tags:
  - software

keywords:
  - "ffmpeg"
  - "rendu sur une grappe"
  - "Python"
  - "MPI"
  - "YT"

questions:
  - "Quelles sont les étapes et commandes requises pour installer l'outil YT dans un environnement virtuel Python ?"
  - "Comment le script Python configure-t-il la scène et la caméra pour générer les 90 images en rotation de l'ensemble de données ?"
  - "Quelle est la procédure pour soumettre la tâche de rendu via SLURM et convertir les images générées en une vidéo avec ffmpeg ?"
  - "Quelles sont les étapes et commandes requises pour installer l'outil YT dans un environnement virtuel Python ?"
  - "Comment le script Python configure-t-il la scène et la caméra pour générer les 90 images en rotation de l'ensemble de données ?"
  - "Quelle est la procédure pour soumettre la tâche de rendu via SLURM et convertir les images générées en une vidéo avec ffmpeg ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Effectuer un rendu sur une grappe

Pour installer [YT](http://yt-project.org) dans votre répertoire afin d'effectuer des rendus avec CPU, exécutez les commandes suivantes :

```bash
module load python mpi4py
virtualenv astro    # installe les outils Python dans votre répertoire $HOME/astro
source ~/astro/bin/activate
pip install cython
pip install numpy
pip install yt
```

Ensuite, chargez l'environnement et démarrez Python.

```bash
source ~/astro/bin/activate   # charge l'environnement
python
...
deactivate
```

Nous supposons que vous avez téléchargé l'ensemble de données Enzo_64 à partir de [http://yt-project.org/data](http://yt-project.org/data). Soumettez d'abord le script `grids.py` ci-dessous pour obtenir un rendu de l'ensemble de données en 90 images, en rotation sur l'axe vertical :

```python
import yt
from numpy import pi
yt.enable_parallelism()   # active le parallélisme MPI via mpi4py
ds = yt.load("Enzo_64/DD0043/data0043")
sc = yt.create_scene(ds, ('gas', 'density'))
cam = sc.camera
cam.resolution = (1024, 1024)   # résolution de chaque image
sc.annotate_domain(ds, color=[1, 1, 1, 0.005])   # dessine la bordure du domaine [r,v,b,alpha]
sc.annotate_grids(ds, alpha=0.005)   # dessine les bordures de la grille
sc.save('frame0000.png', sigma_clip=4)
nspin = 90
for i in cam.iter_rotate(pi, nspin):   # pivote de 180 degrés sur nspin images
    sc.save('frame%04d.png' % (i+1), sigma_clip=4)
```

ainsi que le script `yt-mpi.sh` :

```bash
#!/bin/bash
#SBATCH --time=0:30:00   # temps d'exécution en format j-hh:mm ou hh:mm:ss
#SBATCH --ntasks=4       # nombre de processus MPI
#SBATCH --mem-per-cpu=3800
#SBATCH --account=...
source $HOME/astro/bin/activate
srun python grids.py
```

Soumettez ensuite la tâche avec `sbatch yt-mpi.sh`. Une fois la tâche terminée, créez une vidéo à 30 images par seconde :

```bash
ffmpeg -r 30 -i frame%04d.png -c:v libx264 -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" grids.mp4