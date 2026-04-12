---
title: "MXNet/fr"
slug: "mxnet"
lang: "fr"

source_wiki_title: "MXNet/fr"
source_hash: "52f5d1215ceea4ff5e555a0b2e999fc9"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:56:01.126781+00:00"

tags:
  []

keywords:
  - "Ordonnanceur SLURM"
  - "Trainer"
  - "SBATCH"
  - "environnement virtuel Python"
  - "SoftmaxCrossEntropyLoss"
  - "installation"
  - "Haute performance"
  - "walltime"
  - "transforms"
  - "MXNet"
  - "virtual environment"
  - "CPU et GPU"
  - "trainer.step"
  - "Réseau neuronal convolutif"
  - "apprentissage profond"
  - "GPUs"
  - "CIFAR10"
  - "images_per_sec"
  - "exécution de tâche"
  - "nn.Dense"
  - "DataLoader"
  - "loss.backward"
  - "cpus-per-task"
  - "autograd.record"

questions:
  - "Qu'est-ce que la librairie MXNet et quelles sont ses principales caractéristiques en matière d'apprentissage profond ?"
  - "Quelles sont les étapes requises pour installer MXNet et ses dépendances dans un environnement virtuel Python ?"
  - "Comment configurer et soumettre une tâche MXNet sur un nœud de calcul en utilisant des scripts adaptés pour CPU ou GPU ?"
  - "Pourquoi est-il fortement recommandé d'utiliser plusieurs CPU plutôt qu'un seul GPU pour l'entraînement de petits modèles sur la grappe de calcul ?"
  - "Quelles bibliothèques sous-jacentes MXNet utilise-t-il pour optimiser les opérations mathématiques sur les processeurs (CPU) et les cartes graphiques (GPU) ?"
  - "Comment le script Python d'exemple détecte-t-il et assigne-t-il automatiquement le contexte d'exécution (CPU ou GPU) pour l'entraînement du réseau de neurones ?"
  - "What hardware resources, such as CPUs, memory, and GPUs, are allocated in this job script?"
  - "Which specific software module and version is loaded to run the job?"
  - "In which directory is the virtual environment generated according to the script?"
  - "What is the architecture of the neural network defined in the code snippet?"
  - "Which loss function and optimization algorithm are configured for training the model?"
  - "How is the CIFAR10 training dataset transformed and normalized before being fed into the network?"
  - "What is the primary purpose of this code snippet and what specific machine learning processes does it execute?"
  - "How does the script calculate and track the performance metric of the training loop in terms of images processed per second?"
  - "What is the role of the `autograd.record()` block in relation to the loss calculation and the subsequent model weight updates?"
  - "What is the primary purpose of this code snippet and what specific machine learning processes does it execute?"
  - "How does the script calculate and track the performance metric of the training loop in terms of images processed per second?"
  - "What is the role of the `autograd.record()` block in relation to the loss calculation and the subsequent model weight updates?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[MXNet](https://mxnet.incubator.apache.org/) est une bibliothèque d'apprentissage profond à la fois souple et efficace, qui permet de combiner la programmation symbolique et impérative pour maximiser l'efficacité et la productivité. À la base, MXNet intègre un ordonnanceur de dépendances dynamique qui parallélise automatiquement les opérations symboliques et impératives au fur et à mesure de leur apparition. Une couche d'optimisation des graphes de niveau supérieur rend l'exécution symbolique rapide et économe en mémoire. MXNet est portable, léger et évolutif pour de nombreux GPU et machines.

## Paquets disponibles

Pour savoir quels paquets sont offerts, utilisez la commande `avail_wheels`.

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

3.  Validation de l'installation.

    ```bash
    python -c "import mxnet as mx;print((mx.nd.ones((2, 3))*2).asnumpy());"
    ```

    ```text
    [[2. 2. 2.]
     [2. 2. 2.]]
    ```

## Exécution d'une tâche

1.  Exemple de couche de convolution simple :

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

    # On CPU will use MKLDNN, or will use cuDNN
    exe = y.simple_bind(device, x=shape)

    exe.arg_arrays[0][:] = np.random.normal(size=exe.arg_arrays[0].shape)
    exe.arg_arrays[1][:] = np.random.normal(size=exe.arg_arrays[1].shape)

    exe.forward(is_train=False)
    o = exe.outputs[0]
    t = o.asnumpy()
    print(t)
    ```

2.  Modifiez le script ci-dessous selon les besoins de votre tâche.

    === "CPU"

        ```bash title="mxnet-conv.sh"
        #!/bin/bash

        #SBATCH --job-name=mxnet-conv
        #SBATCH --account=def-someprof    # ajustez ceci pour correspondre au groupe de calcul que vous utilisez
        #SBATCH --time=01:00:00           # ajustez ceci pour correspondre à la durée d'exécution demandée pour votre tâche
        #SBATCH --cpus-per-task=2         # ajustez ceci pour correspondre au nombre de cœurs
        #SBATCH --mem=20G                 # ajustez ceci en fonction de la mémoire dont vous avez besoin

        # Chargement des dépendances des modules
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
        #SBATCH --account=def-someprof    # ajustez ceci pour correspondre au groupe de calcul que vous utilisez
        #SBATCH --time=01:00:00           # ajustez ceci pour correspondre à la durée d'exécution demandée pour votre tâche
        #SBATCH --cpus-per-task=2         # ajustez ceci pour correspondre au nombre de cœurs
        #SBATCH --mem=20G                 # ajustez ceci en fonction de la mémoire dont vous avez besoin
        #SBATCH --gres=gpu:1              # ajustez ceci pour correspondre au nombre de GPU, sauf pour l'entraînement distribué, utilisez 1

        # Chargement des dépendances des modules
        module load python/3.10

        # Générez votre environnement virtuel dans $SLURM_TMPDIR
        virtualenv --no-download ${SLURM_TMPDIR}/env
        source ${SLURM_TMPDIR}/env/bin/activate

        # Installez MXNet et ses dépendances
        pip install --no-index mxnet==1.9.1

        # Utilisera cuDNN
        python mxnet-conv-ex.py
        ```

3.  Soumettez la tâche à l'ordonnanceur SLURM.

    ```bash
    sbatch mxnet-conv.sh
    ```

## Optimisation des performances

### Utiliser plusieurs CPU ou un seul GPU

!!! warning "Utilisation des ressources"
    À l'instar de PyTorch et TensorFlow, MXNet propose des implémentations similaires d'opérateurs pour les CPU et les GPU, incluant les multiplications matricielles et les convolutions, que ce soit avec OpenMP et MKLDNN (pour les CPU) ou CUDA et cuDNN (pour les GPU). Que votre code effectue ou non ces opérations, elles utiliseront automatiquement le mode multithread sur plusieurs cœurs de CPU ou un GPU si la tâche le requiert.

    Cela dit, nous vous encourageons **fortement** à privilégier l'utilisation de **plusieurs CPU plutôt qu'un seul GPU**. Si votre modèle et votre ensemble de données ne sont pas assez grands, l'entraînement sera certainement plus rapide avec un GPU (sauf pour de très petits modèles), mais la différence de vitesse par rapport aux CPU ne sera pas significative, et la tâche n'utilisera qu'un faible pourcentage de la capacité de calcul du GPU. Ce n'est peut-être pas un problème pour votre ordinateur personnel, mais dans un environnement partagé comme nos grappes de calcul, vous bloquez sans raison valable une ressource qui pourrait être utilisée par d'autres pour effectuer des calculs à grande échelle. De plus, vous consommez l'allocation de votre groupe de calcul et avez un effet négatif sur la priorité accordée aux tâches de vos collègues.

    Autrement dit, ne demandez pas un GPU si votre code est incapable de faire un usage raisonnable de sa capacité de calcul. L'exemple suivant montre l'entraînement d'un réseau neuronal convolutif avec ou sans GPU.

```bash title="mxnet-example.sh"
#!/bin/bash
#SBATCH --nodes 1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=1 # change this parameter to 2,4,6,... to see the effect on performance
#SBATCH --gres=gpu:1 # Remove this line to run using CPU only

#SBATCH --mem=8G
#SBATCH --time=0:05:00
#SBATCH --output=%N-%j.out
#SBATCH --account=<your account>

module load python # Using Default Python version - Make sure to choose a version that suits your application

virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate
pip install mxnet --no-index

echo "starting training..."

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