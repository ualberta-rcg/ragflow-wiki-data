---
title: "Yt"
slug: "yt"
lang: "base"

source_wiki_title: "Yt"
source_hash: "45243199d939943b040f42d63ae8ef4f"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T13:42:22.471153+00:00"

tags:
  - software

keywords:
  - "MPI parallelism"
  - "CPU rendering"
  - "job submission script"
  - "Python"
  - "YT rendering"

questions:
  - "What are the necessary steps and commands to install the YT project and its dependencies in a local cluster directory?"
  - "How do you configure a Python script using YT to load a dataset, set up camera resolution, and generate a sequence of rotating frames?"
  - "What is the process for submitting the MPI rendering job to the cluster and subsequently converting the output frames into a video file?"
  - "What are the necessary steps and commands to install the YT project and its dependencies in a local cluster directory?"
  - "How do you configure a Python script using YT to load a dataset, set up camera resolution, and generate a sequence of rotating frames?"
  - "What is the process for submitting the MPI rendering job to the cluster and subsequently converting the output frames into a video file?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## YT Rendering on Clusters

To install [YT](http://yt-project.org) for CPU rendering on a cluster in your own directory, please do:

```bash
module load python mpi4py
virtualenv astro    # install Python tools in your $HOME/astro
source ~/astro/bin/activate
pip install cython
pip install numpy
pip install yt
```

Then, for normal use, simply load the environment and start Python:

```bash
source ~/astro/bin/activate   # load the environment
python
```

When finished, you can deactivate the environment:

```bash
deactivate
```

We assume that you have downloaded the sample dataset Enzo_64 from [http://yt-project.org/data](http://yt-project.org/data). Start with the following Python script, `grids.py`, to render 90 frames rotating the dataset around the vertical axis:

```python title="grids.py"
import yt
from numpy import pi
yt.enable_parallelism()   # turn on MPI parallelism via mpi4py
ds = yt.load("Enzo_64/DD0043/data0043")
sc = yt.create_scene(ds, ('gas', 'density'))
cam = sc.camera
cam.resolution = (1024, 1024)   # resolution of each frame
sc.annotate_domain(ds, color=[1, 1, 1, 0.005])   # draw the domain boundary [r,g,b,alpha]
sc.annotate_grids(ds, alpha=0.005)   # draw the grid boundaries
sc.save('frame0000.png', sigma_clip=4)
nspin = 90
for i in cam.iter_rotate(pi, nspin):   # rotate by 180 degrees over nspin frames
    sc.save('frame%04d.png' % (i+1), sigma_clip=4)
```

and the following job submission script, `yt-mpi.sh`:

```bash title="yt-mpi.sh"
#!/bin/bash
#SBATCH --time=0:30:00   # walltime in d-hh:mm or hh:mm:ss format
#SBATCH --ntasks=4       # number of MPI processes
#SBATCH --mem-per-cpu=3800
#SBATCH --account=...
source $HOME/astro/bin/activate
srun python grids.py
```

!!! important "Account Placeholder"
    Remember to replace `...` in `#SBATCH --account=...` with your actual Alliance account.

Then submit the job with `sbatch yt-mpi.sh`, wait for it to finish, and then create a movie at 30 frames per second (fps):

```bash
ffmpeg -r 30 -i frame%04d.png -c:v libx264 -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" grids.mp4