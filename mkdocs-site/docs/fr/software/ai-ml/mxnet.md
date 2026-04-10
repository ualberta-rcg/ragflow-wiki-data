---
title: "MXNet/fr"
slug: "mxnet"
lang: "fr"

source_wiki_title: "MXNet/fr"
source_hash: "52f5d1215ceea4ff5e555a0b2e999fc9"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T08:22:22.086142+00:00"

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

[MXNet](https://mxnet.incubator.apache.org/) est une bibliothèque en apprentissage profond à la fois souple et efficace qui permet de combiner la programmation symbolique et impérative pour maximiser l'efficacité et la productivité. À la base, MXNet contient un planificateur de dépendances dynamique qui parallélise automatiquement les opérations symboliques et impératives comme elles se présentent. Une couche supérieure d'optimisation des graphes rend l'exécution symbolique rapide et économe en mémoire. MXNet est portable et léger, évolutif pour de nombreux GPU et machines.

## Paquets disponibles

Pour savoir quels paquets sont disponibles, utilisez la commande `avail_wheels`.

```bash
avail_wheels mxnet
```

```text
name    version    python    arch
------  ---------  --------  ------
mxnet   1.9.1      cp39      avx2
mxnet   1.9.1      cp38      avx2
mxnet   1.9.1      cp310     avx2
```

## Installation dans un environnement virtuel Python

1.  Créez et activez un environnement virtuel Python.

    ```bash
    module load python/3.10
    virtualenv --no-download ~/env
    source ~/env/bin/activate
    ```

2.  Installez MXNet et ses dépendances Python.

    ```bash
    pip install --no-index mxnet
    ```

3.  Validez.

    ```bash
    python -c "import mxnet as mx;print((mx.nd.ones((2, 3))*2).asnumpy());"
    ```

    ```text
    [[2. 2. 2.]
     [2. 2. 2.]]
    ```

## Exécution d'une tâche

Couche simple pour les convolutions :

```python title="mxnet-conv-ex.py"
#!/bin/env python

import mxnet as mx
import numpy as np

num_filter = 32
kernel = (3, 3)
pad = (1, 1)
shape = (32, 32, 256, 256)

x = mx.sym.Variable('x')
w = mx.sym.Variable('w')
y = mx.sym.Convolution(data=x, weight=w, num_filter=num_filter, kernel=kernel, no_bias=True, pad=pad)

device = mx.gpu() if mx.context.num_gpus() > 0 else mx.cpu()

# Sur CPU, utilisera MKLDNN; sur GPU, utilisera cuDNN
exe = y.simple_bind(device, x=shape)

exe.arg_arrays[0][:] = np.random.normal(size=exe.arg_arrays[0].shape)
exe.arg_arrays[1][:] = np.random.normal(size=exe.arg_arrays[1].shape)

exe.forward(is_train=False)
o = exe.outputs[0]
t = o.asnumpy()
print(t)
```

2.  Modifiez le script suivant selon les besoins de votre tâche.

=== "CPU"

    ```bash title="mxnet-conv.sh"
    #!/bin/bash

    #SBATCH --job-name=mxnet-conv
    #SBATCH --account=def-someprof    # ajustez ceci pour correspondre au groupe comptable que vous utilisez pour soumettre des tâches
    #SBATCH --time=01:00:00           # ajustez ceci pour correspondre à la durée d'exécution de votre tâche
    #SBATCH --cpus-per-task=2         # ajustez ceci pour correspondre au nombre de cœurs
    #SBATCH --mem=20G                 # ajustez ceci selon la mémoire dont vous avez besoin

    # Chargez les dépendances des modules
    module load python/3.10

    # Générez votre environnement virtuel dans $SLURM_TMPDIR
    virtualenv --no-download ${SLURM_TMPDIR}/env
    source ${SLURM_TMPDIR}/env/bin/activate

    # Installez MXNet et ses dépendances
    pip install --no-index mxnet==1.9.1

    # Utilisera MKLDNN
    python mxnet-conv-ex.py
    ```

=== "GPU"

    ```bash title="mxnet-conv.sh"
    #!/bin/bash

    #SBATCH --job-name=mxnet-conv
    #SBATCH --account=def-someprof    # ajustez ceci pour correspondre au groupe comptable que vous utilisez pour soumettre des tâches
    #SBATCH --time=01:00:00           # ajustez ceci pour correspondre à la durée d'exécution de votre tâche
    #SBATCH --cpus-per-task=2         # ajustez ceci pour correspondre au nombre de cœurs
    #SBATCH --mem=20G                 # ajustez ceci selon la mémoire dont vous avez besoin
    #SBATCH --gres=gpu:1              # ajustez ceci pour correspondre au nombre de GPU, à moins qu'il s'agisse d'entraînement distribué, utilisez 1

    # Chargez les dépendances des modules
    module load python/3.10

    # Générez votre environnement virtuel dans $SLURM_TMPDIR
    virtualenv --no-download ${SLURM_TMPDIR}/env
    source ${SLURM_TMPDIR}/env/bin/activate

    # Installez MXNet et ses dépendances
    pip install --no-index mxnet==1.9.1

    # Utilisera cuDNN
    python mxnet-conv-ex.py
    ```

3.  Soumettez la tâche à l'ordonnanceur.

    ```bash
    sbatch mxnet-conv.sh
    ```

## Haute performance

### Utiliser plusieurs CPU ou un seul GPU

Tout comme PyTorch et TensorFlow, MXNet offre des implémentations semblables d'opérateurs pour le travail avec CPU et GPU, dont les multiplications matricielles et les convolutions, soit avec OpenMP et MKLDNN (CPU) ou CUDA et CUDNN (GPU). Que votre code effectue ou non ces opérations, elles utiliseront automatiquement le mode multifils sur plusieurs cœurs CPU ou un GPU si la tâche le demande.

!!! warning "Utilisation optimale des ressources"
    Nous vous encourageons fortement à utiliser **plusieurs CPU plutôt qu'un seul GPU**. Si votre modèle et votre ensemble de données ne sont pas assez grands, l'entraînement sera certainement plus rapide avec un GPU (sauf dans le cas de très petits modèles), mais la différence avec la vitesse obtenue par les CPU ne sera pas bien importante et la tâche n'utilisera qu'un faible pourcentage de la capacité de calcul du GPU. Ce n'est peut-être pas un problème pour votre ordinateur, mais dans un environnement partagé comme nos grappes, vous bloquez sans raison valable une ressource qui pourrait être utilisée par d'autres pour effectuer des calculs à grande échelle, sans compter que vous utilisez l'allocation de votre groupe et avez un effet négatif sur la priorité accordée aux tâches de vos collègues.

Autrement dit, ne demandez pas un GPU si votre code est incapable de faire un usage raisonnable de sa capacité de calcul. L'exemple suivant montre l'entraînement d'un réseau neuronal convolutif avec ou sans GPU.

```bash title="mxnet-example.sh"
#!/bin/bash
#SBATCH --nodes 1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=1 # changez ce paramètre à 2,4,6,... pour voir l'effet sur la performance
#SBATCH --gres=gpu:1 # Enlevez cette ligne pour exécuter avec le CPU seulement

#SBATCH --mem=8G
#SBATCH --time=0:05:00
#SBATCH --output=%N-%j.out
#SBATCH --account=<votre_compte>

module load python # Utilisation de la version Python par défaut - assurez-vous de choisir une version qui convient à votre application

virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate
pip install mxnet --no-index

echo "démarrage de l'entraînement..."

python mxnet-example.py
```

```python title="mxnet-example.py"
import numpy as np
import time

from mxnet import context
from mxnet import autograd, gpu, cpu
from mxnet.gluon import nn, Trainer
from mxnet.gluon.loss import SoftmaxCrossEntropyLoss
from mxnet.gluon.data.vision import transforms
from mxnet.gluon.data.vision.datasets import CIFAR10
from mxnet.gluon.data import DataLoader

import argparse

parser = argparse.ArgumentParser(description='cifar10 classification models, cpu performance test')
parser.add_argument('--lr', default=0.1, help='')
parser.add_argument('--batch_size', type=int, default=512, help='')
parser.add_argument('--num_workers', type=int, default=0, help='')

def main():

    args = parser.parse_args()

    ctx = gpu() if context.num_gpus() > 0 else cpu()

    net = nn.Sequential()

    net.add(nn.Conv2D(channels=6, kernel_size=5, activation='relu'),
        nn.MaxPool2D(pool_size=2, strides=2),
        nn.Conv2D(channels=16, kernel_size=5, activation='relu'),
        nn.MaxPool2D(pool_size=2, strides=2),
        nn.Flatten(),
        nn.Dense(120, activation="relu"),
        nn.Dense(84, activation="relu"),
        nn.Dense(10))

    net.initialize(ctx=ctx)

    criterion = SoftmaxCrossEntropyLoss()
    trainer = Trainer(net.collect_params(),'sgd', {'learning_rate': args.lr})

    transform_train = transforms.Compose([transforms.ToTensor(),transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
    dataset_train = CIFAR10(root='./data', train=True).transform_first(transform_train)
    train_loader = DataLoader(dataset_train, batch_size=args.batch_size, shuffle=True, num_workers=args.num_workers)

    perf = []

    for inputs, targets in train_loader:

       inputs = inputs.as_in_context(ctx)
       targets = targets.as_in_context(ctx)

       start = time.time()

       with autograd.record():

          outputs = net(inputs)
          loss = criterion(outputs, targets)

       loss.backward()
       trainer.step(batch_size=args.batch_size)

       batch_time = time.time() - start
       images_per_sec = args.batch_size/batch_time
       perf.append(images_per_sec)

       print(f"Current Loss: {loss.mean().asscalar()}")

    print(f"Images processed per second: {np.mean(perf)}")

if __name__=='__main__':
   main()