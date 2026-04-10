---
title: "PyTorch/fr"
slug: "pytorch"
lang: "fr"

source_wiki_title: "PyTorch/fr"
source_hash: "a390055b7c397e5d3a09b03d658cb0e9"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T10:09:45.538493+00:00"

tags:
  - software
  - ai-and-machine-learning

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

PyTorch est un package Python qui offre deux fonctionnalités de haut niveau :
* le calcul tensoriel (semblable à celui effectué par NumPy) avec une forte accélération de GPU, et
* des réseaux de neurones d'apprentissage profond dans un système de gradients conçu sur le modèle d'un magnétophone.

Si vous voulez porter un programme PyTorch sur une de nos grappes de calcul, il serait bon de prendre connaissance [de ce tutoriel](tutoriel-apprentissage-machine.md).

## Clarification

Il y a une certaine ressemblance entre PyTorch et [Torch](torch.md), mais pour des raisons pratiques, vous pouvez considérer que ce sont des projets différents.

Les développeurs PyTorch offrent aussi [LibTorch](#libtorch) qui permet d'implémenter des extensions à PyTorch à l'aide de C++ et d'implémenter des applications d'apprentissage machine en C++ pur. Les modèles Python écrits avec PyTorch peuvent être convertis et utilisés en C++ avec [TorchScript](https://pytorch.org/tutorials/advanced/cpp_export.html).

## Installation

### Wheels récemment ajoutés

Pour connaître la dernière version de PyTorch, utilisez :

```bash
avail_wheels torch
```

Pour plus d'information, voyez [Wheels disponibles](python.md#wheels-disponibles).

### Installation du wheel

La meilleure option est d'installer avec [Python wheels](https://pythonwheels.com/) comme suit :

1.  [Chargez un module](utiliser-des-modules.md#sous-commande-load) Python avec `module load python`.
2.  Créez et démarrez un [environnement virtuel](python.md#créer-et-utiliser-un-environnement-virtuel).
3.  Installez PyTorch dans l'environnement virtuel avec `pip install`.

#### GPU et CPU

```bash
(venv) [nom@serveur ~]$ pip install --no-index torch
```

!!! note "Remarque"
    Avec les GPU H100, utilisez Torch 2.3 et versions plus récentes.

#### En supplément

En plus de `torch`, vous pouvez aussi installer `torchvision`, `torchtext` et `torchaudio`.

```bash
(venv) [nom@serveur ~]$ pip install --no-index torch torchvision torchtext torchaudio
```

## Soumettre une tâche

Le script suivant est un exemple de soumission d'une tâche utilisant le wheel Python avec un environnement virtuel.

```bash title="pytorch-test.sh"
#!/bin/bash
#SBATCH --gres=gpu:1       # Demande de ressources génériques GPU
#SBATCH --cpus-per-task=6  # Cœurs proportionnels aux GPU.
#SBATCH --mem=32000M       # Mémoire proportionnelle aux GPU.
#SBATCH --time=0-03:00
#SBATCH --output=%N-%j.out

module load python/<select version> # Assurez-vous de choisir une version adaptée à votre application
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate
pip install torch --no-index

python pytorch-test.py
```

Pour plus d'information sur le nombre de CPU et la mémoire des GPU sur nos grappes, voir [Ratios dans les bundles](allocations-and-compute-scheduling.md#ratios-dans-les-bundles).

Le script Python `pytorch-test.py` a la forme suivante :

```python title="pytorch-test.py"
import torch
x = torch.Tensor(5, 3)
print(x)
y = torch.rand(5, 3)
print(y)
# n'exécutons ce qui suit que si CUDA est disponible
if torch.cuda.is_available():
    x = x.cuda()
    y = y.cuda()
    print(x + y)
```

Vous pouvez alors soumettre une tâche PyTorch avec :

```bash
sbatch pytorch-test.sh
```

## Haute performance

### TF32 : Performance vs précision

Avec sa version 1.7.0, PyTorch a ajouté le support pour le [mode TensorFloat-32 (TF32) de Nvidia](https://blogs.nvidia.com/blog/2020/05/14/tensorfloat-32-precision-format/) et est seulement disponible pour les architectures GPU d'Ampere et de Nvidia. Avec ce mode qui est offert par défaut dans les versions 1.7.x à 1.11.x, les opérations tensorielles se font jusqu'à 20x plus rapidement que les opérations équivalentes en simple précision (FP32). Cependant, ce gain en performance peut engendrer une baisse dans la précision du résultat des opérations, ce qui pose problème avec les modèles d'apprentissage profond qui utilisent à l'occasion des matrices mal conditionnées ou qui effectuent de longues séquences d'opérations tensorielles. Suite aux commentaires de la communauté des utilisateurs, TF32 est **désactivé par défaut pour les multiplications matricielles et activé par défaut pour les convolutions** à partir de la version 1.12.0.

Sur les grappes équipées de GPU A100, H100 ou Nvidia plus récents, sachez que :
* vous pourriez remarquer un fort ralentissement dans l'exécution sur GPU du même code avec `torch < 1.12.0` et `torch >= 1.12.0`;
* vous pourriez obtenir des résultats différents dans l'exécution sur GPU du même code avec `torch < 1.12.0` et `torch >= 1.12.0`.

Pour activer ou désactiver TF32 pour `torch >= 1.12.0`, donnez la valeur `True` ou `False` aux indicateurs suivants :

```python
torch.backends.cuda.matmul.allow_tf32 = False # Activer/désactiver TF32 pour les multiplications matricielles
torch.backends.cudnn.allow_tf32 = False # Activer/désactiver TF32 pour les convolutions
```

Pour plus d'information, consultez [cette partie de la documentation PyTorch](https://pytorch.org/docs/stable/notes/cuda.html#tf32-on-ampere).

### Travailler avec un CPU

Par défaut, PyTorch permet le parallélisme avec plusieurs CPU de deux façons :
* **intra-op**, par l’implémentation parallèle d’opérateurs souvent utilisés en apprentissage profond comme le produit matriciel ou le produit de convolution, en utilisant [OpenMP](https://www.openmp.org) directement ou avec des bibliothèques de bas niveau comme [MKL](https://en.wikipedia.org/wiki/Math_Kernel_Library) et [OneDNN](https://www.intel.com/content/www/us/en/develop/documentation/oneapi-programming-guide/top/api-based-programming/intel-oneapi-deep-neural-network-library-onednn.html). Quand du code PyTorch doit effectuer de telles opérations, elles utilisent automatiquement de multiples fils avec tous les cœurs CPU disponibles.
* **inter-op**, par la capacité d’exécuter différentes parties de code de manière concurrente. Ce mode de parallélisme nécessite habituellement que le programme soit conçu de manière à exécuter plusieurs parties en parallèle, par exemple en faisant usage du compilateur en temps réel `torch.jit` pour exécuter des tâches asynchrones dans un programme [TorchScript](https://pytorch.org/docs/stable/jit.html#built-in-functions-and-modules).

Pour les petits modèles, nous recommandons fortement **d’utiliser plusieurs CPU plutôt qu’un GPU**. L’entraînement sera certainement plus rapide avec un GPU (sauf dans les cas de très petits modèles), mais si le modèle et le jeu de données ne sont pas assez grands, la vitesse gagnée avec le GPU ne sera probablement pas très importante et la tâche n’utilisera qu’une petite part de la capacité de calcul. Ce n’est peut-être pas grave sur votre propre ordinateur, mais dans un environnement partagé comme sur nos grappes, vous bloqueriez une ressource qui pourrait servir à effectuer de calculs de grande échelle par un autre projet. De plus, l’utilisation d’un GPU contribuerait à la diminution de l’allocation de votre groupe et aurait une incidence sur la priorité accordée aux tâches de vos collègues.

Dans le code suivant, il y a plusieurs occasions d’utiliser le parallélisme intra-op.

```python title="cifar10-cpu.py"
import numpy as np
import time

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

import torchvision
import torchvision.transforms as transforms
from torchvision.datasets import CIFAR10
from torch.utils.data import DataLoader

import argparse
import os

parser = argparse.ArgumentParser(description='cifar10 classification models, cpu performance test')
parser.add_argument('--lr', default=0.1, help='')
parser.add_argument('--batch_size', type=int, default=512, help='')
parser.add_argument('--num_workers', type=int, default=0, help='')

def main():

    args = parser.parse_args()
    torch.set_num_threads(int(os.environ['SLURM_CPUS_PER_TASK']))
    class Net(nn.Module):

       def __init__(self):
          super(Net, self).__init__()

          self.conv1 = nn.Conv2d(3, 6, 5)
          self.pool = nn.MaxPool2d(2, 2)
          self.conv2 = nn.Conv2d(6, 16, 5)
          self.fc1 = nn.Linear(16 * 5 * 5, 120)
          self.fc2 = nn.Linear(120, 84)
          self.fc3 = nn.Linear(84, 10)

       def forward(self, x):
          x = self.pool(F.relu(self.conv1(x)))
          x = self.pool(F.relu(self.conv2(x)))
          x = x.view(-1, 16 * 5 * 5)
          x = F.relu(self.fc1(x))
          x = F.relu(self.fc2(x))
          x = self.fc3(x)
          return x

    net = Net()

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=args.lr)

    transform_train = transforms.Compose([transforms.ToTensor(),transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    ### Cette ligne suivante tentera de télécharger le jeu de données CIFAR10 depuis Internet si vous ne l'avez pas déjà stocké dans ./data
    ### Exécutez cette ligne sur un nœud de connexion avec "download=True" avant de soumettre votre tâche, ou téléchargez manuellement les données depuis
    ### https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz et placez-les sous ./data

    dataset_train = CIFAR10(root='./data', train=True, download=False, transform=transform_train)

    train_loader = DataLoader(dataset_train, batch_size=args.batch_size, num_workers=args.num_workers)

    perf = []

    total_start = time.time()

    for batch_idx, (inputs, targets) in enumerate(train_loader):

       start = time.time()

       outputs = net(inputs)
       loss = criterion(outputs, targets)

       optimizer.zero_grad()
       loss.backward()
       optimizer.step()

       batch_time = time.time() - start

       images_per_sec = args.batch_size/batch_time

       perf.append(images_per_sec)

    total_time = time.time() - total_start

if __name__=='__main__':
   main()
```

Avant de tester le code ci-dessus, vous devez d'abord télécharger les données.

```bash
mkdir -p data && cd data
```

```bash title="Commandes"
[nom@serveur data]$ wget https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz
[nom@serveur data]$ tar zxf cifar-10-python.tar.gz
[nom@serveur data]$ cd ..
```

En demandant plus de CPU et sans changer le code, on peut constater l’effet sur la performance.

```bash title="pytorch-multi-cpu.sh"
#!/bin/bash
#SBATCH --nodes 1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=1 # change this parameter to 2,4,6,... to see the effect on performance

#SBATCH --mem=8G
#SBATCH --time=0:05:00
#SBATCH --output=%N-%j.out
#SBATCH --account=<your account>

module load python # Using Default Python version - Make sure to choose a version that suits your application
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate
pip install torch torchvision --no-index

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

echo "starting training..."

time python cifar10-cpu.py
```

### Travailler avec un GPU

On entend souvent dire qu’il faut absolument entraîner un modèle avec un GPU s’il y en a un à notre disposition. Ceci est *presque toujours* vrai (l'entraînement de très petits modèles est souvent plus rapide avec un ou plusieurs CPU) sur un poste de travail local, mais ce n’est pas le cas sur nos grappes.

Autrement dit, vous **ne devriez pas demander un GPU** si votre code ne peut pas faire un usage raisonnable de sa capacité de calcul.

La performance avantageuse des GPU pour les tâches d’apprentissage profond provient de deux sources :

1.  La capacité de paralléliser l’exécution de certaines opérations clés, par exemple le [multiplieur-accumulateur](https://fr.wikipedia.org/wiki/Multiplieur-accumulateur), sur plusieurs milliers de cœurs de calcul, en comparaison du très petit nombre de cœurs disponibles avec la plupart des CPU.
2.  Une bande passante de mémoire beaucoup plus grande que pour un CPU, ce qui permet aux GPU d’utiliser efficacement leur très grand nombre de cœurs pour traiter une plus grande quantité de données par cycle de calcul.

Comme c’est le cas avec plusieurs CPU, PyTorch offre des implémentations parallèles d’opérateurs souvent utilisés en apprentissage profond, comme le produit matriciel et le produit de convolution et utilise des bibliothèques spécialisées pour les GPU comme [CUDNN](https://developer.nvidia.com/cudnn) ou [MIOpen](https://github.com/ROCmSoftwarePlatform/MIOpen), selon la plateforme matérielle. Ceci signifie que pour qu’il vaille la peine d’utiliser un GPU pour une tâche d’apprentissage, elle doit être composée d’éléments qui peuvent être élargis à une application massive du parallélisme de par le nombre d’opérations pouvant être parallélisées, de par la quantité des données à traiter ou idéalement de par les deux. Un exemple concret serait un grand modèle qui a un grand nombre d’unités et de couches ou qui a beaucoup de données en entrée, et idéalement qui présente ces deux caractéristiques.

Dans l’exemple ci-dessous, nous adaptons le code de la section précédente pour utiliser un GPU et nous examinons la performance. Nous observons que deux paramètres jouent un rôle important : `batch_size` et `num_workers`. Le premier paramètre améliore la performance en augmentant la taille des entrées à chaque itération et en utilisant mieux la capacité du GPU. Dans le cas du second paramètre, la performance est améliorée en facilitant le mouvement des données entre la mémoire de l’hôte (le CPU) et la mémoire du GPU, ce qui réduit la durée d’inactivité du GPU en attente de données à traiter.

Nous pouvons tirer deux conclusions :

1.  Augmenter la valeur de `batch_size` au maximum qu’il est possible pour la mémoire du GPU optimise la performance.
2.  Utiliser un `DataLoader` avec autant de workers que `cpus-per-task` facilite l’apport de données au GPU.

Bien entendu, le paramètre `batch_size` a aussi un impact sur la performance d’un modèle dans une tâche (c.-à-d. l’exactitude, l’erreur, etc.) et il existe différentes écoles de pensée sur l’utilisation de grands lots. Nous n’abordons pas le sujet ici, mais si vous croyez qu’un petit lot conviendrait mieux à votre application, allez à la section [Parallélisme des données avec un seul GPU](#parallélisme-des-données-avec-un-seul-gpu) pour savoir comment maximiser l’utilisation du GPU avec de petites entrées de données.

```bash title="pytorch-single-gpu.sh"
#!/bin/bash
#SBATCH --nodes 1
#SBATCH --gres=gpu:1 # demande un GPU
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=1 # modifiez ce paramètre à 2,4,6,... et augmentez "--num_workers" en conséquence pour voir l'effet sur la performance
#SBATCH --mem=8G
#SBATCH --time=0:05:00
#SBATCH --output=%N-%j.out
#SBATCH --account=<your account>

module load python # Utilisation de la version Python par défaut - assurez-vous de choisir une version adaptée à votre application
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate
pip install torch torchvision --no-index

echo "starting training..."
time python cifar10-gpu.py --batch_size=512 --num_workers=0
```

```python title="cifar10-gpu.py"
import numpy as np
import time

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

import torchvision
import torchvision.transforms as transforms
from torchvision.datasets import CIFAR10
from torch.utils.data import DataLoader

import argparse

parser = argparse.ArgumentParser(description='cifar10 classification models, single gpu performance test')
parser.add_argument('--lr', default=0.1, help='')
parser.add_argument('--batch_size', type=int, default=512, help='')
parser.add_argument('--num_workers', type=int, default=0, help='')


def main():

    args = parser.parse_args()

    class Net(nn.Module):

       def __init__(self):
          super(Net, self).__init__()

          self.conv1 = nn.Conv2d(3, 6, 5)
          self.pool = nn.MaxPool2d(2, 2)
          self.conv2 = nn.Conv2d(6, 16, 5)
          self.fc1 = nn.Linear(16 * 5 * 5, 120)
          self.fc2 = nn.Linear(120, 84)
          self.fc3 = nn.Linear(84, 10)

       def forward(self, x):
          x = self.pool(F.relu(self.conv1(x)))
          x = self.pool(F.relu(self.conv2(x)))
          x = x.view(-1, 16 * 5 * 5)
          x = F.relu(self.fc1(x))
          x = F.relu(self.fc2(x))
          x = self.fc3(x)
          return x

    net = torch.compile(Net())
    net = net.cuda() # Charger le modèle sur le GPU

    criterion = nn.CrossEntropyLoss().cuda() # Charger la fonction de perte sur le GPU
    optimizer = optim.SGD(net.parameters(), lr=args.lr)

    transform_train = transforms.Compose([transforms.ToTensor(),transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    dataset_train = CIFAR10(root='./data', train=True, download=False, transform=transform_train)

    train_loader = DataLoader(dataset_train, batch_size=args.batch_size, num_workers=args.num_workers, pin_memory=True)

    perf = []

    total_start = time.time()

    for batch_idx, (inputs, targets) in enumerate(train_loader):

       start = time.time()

       inputs = inputs.cuda()
       targets = targets.cuda()

       outputs = net(inputs)
       loss = criterion(outputs, targets)

       optimizer.zero_grad()
       loss.backward()
       optimizer.step()

       batch_time = time.time() - start

       images_per_sec = args.batch_size/batch_time

       perf.append(images_per_sec)

    total_time = time.time() - total_start

if __name__=='__main__':
   main()
```

### Parallélisme des données

Dans ce contexte, le parallélisme des données désigne les méthodes permettant d'entraîner un modèle sur plusieurs copies (*replicas*) en parallèle, chaque copie recevant un ensemble différent de données d'entraînement à chaque itération. Les gradients sont ensuite agrégés à la fin de chaque itération et les paramètres de toutes les copies sont mis à jour de manière synchrone ou asynchrone, selon la méthode utilisée.

Cette approche pourrait permettre un gain de vitesse significatif en parcourant tous les exemples d'un grand ensemble de données environ N fois plus rapidement, où N est le nombre de copies du modèle.

Un inconvénient majeur de cette approche est que, pour obtenir un modèle entraîné équivalent à celui entraîné sans parallélisme de données, il faut ajuster le taux d'apprentissage ou la taille des lots en fonction du nombre de copies. Voir [cette discussion](https://discuss.pytorch.org/t/should-we-split-batch-size-according-to-ngpu-per-node-when-distributeddataparallel/72769/13) pour plus d'information.

Avec plusieurs GPU, chaque GPU héberge une copie de votre modèle. Par conséquent, le modèle doit être **suffisamment petit pour occuper la mémoire d'un seul GPU**.

Il existe plusieurs manières de paralléliser les données avec PyTorch. Nous présentons ici des tutoriels avec la classe **DistributedDataParallel** avec un ou plusieurs GPU en utilisant le package **PyTorch Lightning**.

#### Parallélisme des données avec plusieurs GPU

Avec plusieurs GPU, la classe **DistributedDataParallel** est [recommandée par les développeurs PyTorch](https://pytorch.org/tutorials/intermediate/ddp_tutorial.html#comparison-between-dataparallel-and-distributeddataparallel), que ce soit avec un nœud unique ou avec plusieurs nœuds. Dans le cas qui suit, plusieurs GPU sont distribués sur deux nœuds.

```bash title="pytorch-ddp-test.sh"
#!/bin/bash
#SBATCH --nodes 1
#SBATCH --gres=gpu:2          # Demande de 2 ressources génériques GPU.
#SBATCH --tasks-per-node=2   # Demande 1 processus par GPU. Vous obtiendrez 1 CPU par processus par défaut. Demandez plus de CPU avec le paramètre "cpus-per-task" pour permettre à plusieurs workers de charger les données en parallèle.
#SBATCH --mem=8G
#SBATCH --time=0-03:00
#SBATCH --output=%N-%j.out

module load python # Utilisation de la version Python par défaut - assurez-vous de choisir une version adaptée à votre application
srun -N $SLURM_NNODES -n $SLURM_NNODES bash << EOF
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate
pip install torch torchvision --no-index
EOF

export TORCH_NCCL_ASYNC_HANDLING=1
export MASTER_ADDR=$(hostname) # Stocke l'adresse IP du nœud maître dans la variable d'environnement MASTER_ADDR.

echo "r$SLURM_NODEID master: $MASTER_ADDR"
echo "r$SLURM_NODEID Launching python script"

# La variable $((SLURM_NTASKS_PER_NODE * SLURM_JOB_NUM_NODES)) indique au script combien de processus sont disponibles pour cette exécution. "srun" exécute le script <tasks-per-node * nodes> fois

source $SLURM_TMPDIR/env/bin/activate

srun python pytorch-ddp-test.py --init_method tcp://$MASTER_ADDR:3456 --world_size $((SLURM_NTASKS_PER_NODE * SLURM_JOB_NUM_NODES))  --batch_size 256
```

Le script Python `pytorch-ddp-test.py` a la forme suivante :

```python title="pytorch-ddp-test.py"
import os
import time
import datetime

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.backends.cudnn as cudnn

import torchvision
import torchvision.transforms as transforms
from torchvision.datasets import CIFAR10
from torch.utils.data import DataLoader

import torch.distributed as dist
import torch.utils.data.distributed

import argparse

parser = argparse.ArgumentParser(description='cifar10 classification models, distributed data parallel test')
parser.add_argument('--lr', default=0.1, help='')
parser.add_argument('--batch_size', type=int, default=768, help='')
parser.add_argument('--max_epochs', type=int, default=4, help='')
parser.add_argument('--num_workers', type=int, default=0, help='')

parser.add_argument('--init_method', default='tcp://127.0.0.1:3456', type=str, help='')
parser.add_argument('--dist-backend', default='nccl', type=str, help='')
parser.add_argument('--world_size', default=1, type=int, help='')
parser.add_argument('--distributed', action='store_true', help='')

def main():
    print("Starting...")

    args = parser.parse_args()

    local_rank = int(os.environ.get("SLURM_LOCALID"))
    rank = int(os.environ.get("SLURM_PROCID"))
    current_device = local_rank

    torch.cuda.set_device(current_device)

    """ ce bloc initialise un groupe de processus et initie les communications
        entre tous les processus s'exécutant sur tous les nœuds """

    print('From Rank: {}, ==> Initializing Process Group...'.format(rank))
    # initialisation du groupe de processus
    dist.init_process_group(backend=args.dist_backend, init_method=args.init_method, world_size=args.world_size, rank=rank)
    print("process group ready!")

    print('From Rank: {}, ==> Making model..'.format(rank))

    class Net(nn.Module):

       def __init__(self):
          super(Net, self).__init__()

          self.conv1 = nn.Conv2d(3, 6, 5)
          self.pool = nn.MaxPool2d(2, 2)
          self.conv2 = nn.Conv2d(6, 16, 5)
          self.fc1 = nn.Linear(16 * 5 * 5, 120)
          self.fc2 = nn.Linear(120, 84)
          self.fc3 = nn.Linear(84, 10)

       def forward(self, x):
          x = self.pool(F.relu(self.conv1(x)))
          x = self.pool(F.relu(self.conv2(x)))
          x = x.view(-1, 16 * 5 * 5)
          x = F.relu(self.fc1(x))
          x = F.relu(self.fc2(x))
          x = self.fc3(x)
          return x

    net = torch.compile(Net())

    net.cuda()
    net = torch.nn.parallel.DistributedDataParallel(net, device_ids=[current_device])

    print('From Rank: {}, ==> Preparing data..'.format(rank))

    transform_train = transforms.Compose([transforms.ToTensor(),transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    dataset_train = CIFAR10(root='./data', train=True, download=False, transform=transform_train)

    train_sampler = torch.utils.data.distributed.DistributedSampler(dataset_train)
    train_loader = DataLoader(dataset_train, batch_size=args.batch_size, shuffle=(train_sampler is None), num_workers=args.num_workers, sampler=train_sampler, pin_memory=True)

    criterion = nn.CrossEntropyLoss().cuda()
    optimizer = optim.SGD(net.parameters(), lr=args.lr, momentum=0.9, weight_decay=1e-4)

    for epoch in range(args.max_epochs):

        train_sampler.set_epoch(epoch)

        train(epoch, net, criterion, optimizer, train_loader, rank)

def train(epoch, net, criterion, optimizer, train_loader, train_rank):

    train_loss = 0
    correct = 0
    total = 0

    epoch_start = time.time()

    for batch_idx, (inputs, targets) in enumerate(train_loader):

       start = time.time()

       inputs = inputs.cuda()
       targets = targets.cuda()
       outputs = net(inputs)
       loss = criterion(outputs, targets)

       optimizer.zero_grad()
       loss.backward()
       optimizer.step()

       train_loss += loss.item()
       _, predicted = outputs.max(1)
       total += targets.size(0)
       correct += predicted.eq(targets).sum().item()
       acc = 100 * correct / total

       batch_time = time.time() - start

       elapse_time = time.time() - epoch_start
       elapse_time = datetime.timedelta(seconds=elapse_time)
       print("From Rank: {}, Training time {}".format(train_rank, elapse_time))

if __name__=='__main__':
   main()
```

#### PyTorch Lightning

Ce package fournit des interfaces à PyTorch afin de simplifier plusieurs tâches communes exigeant beaucoup de code; ceci inclut les tâches d'entraînement de modèles avec plusieurs GPU. Dans le tutoriel suivant avec PyTorch Lightning, nous reprenons le même exemple que ci-dessus, mais sans avoir explicitement recours à la classe DistributedDataParallel.

```bash title="pytorch-ddp-test-pl.sh"
#!/bin/bash
#SBATCH --nodes 1
#SBATCH --gres=gpu:2          # Demande de 2 ressources génériques GPU.
#SBATCH --tasks-per-node=2    # Demande 1 processus par GPU. Vous obtiendrez 1 CPU par processus par défaut. Demandez plus de CPU avec le paramètre "cpus-per-task" pour permettre à plusieurs workers de charger les données en parallèle.
#SBATCH --mem=8G
#SBATCH --time=0-03:00
#SBATCH --output=%N-%j.out

module load python # Utilisation de la version Python par défaut - assurez-vous de choisir une version adaptée à votre application
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate
pip install torchvision pytorch-lightning --no-index

export TORCH_NCCL_ASYNC_HANDLING=1

# PyTorch Lightning interrogera l'environnement pour savoir s'il s'exécute dans une tâche par lot SLURM
# Si c'est le cas, il s'attend à ce que l'utilisateur ait demandé une tâche par GPU.
# Si vous ne demandez pas 1 tâche par GPU, et que vous n'exécutez pas votre script avec "srun", votre tâche échouera !

srun python pytorch-ddp-test-pl.py  --batch_size 256
```

```python title="pytorch-ddp-test-pl.py"
import datetime

import torch
from torch import nn
import torch.nn.functional as F

import pytorch_lightning as pl

import torchvision
import torchvision.transforms as transforms
from torchvision.datasets import CIFAR10
from torch.utils.data import DataLoader

import argparse

parser = argparse.ArgumentParser(description='cifar10 classification models, pytorch-lightning parallel test')
parser.add_argument('--lr', default=0.1, help='')
parser.add_argument('--max_epochs', type=int, default=4, help='')
parser.add_argument('--batch_size', type=int, default=768, help='')
parser.add_argument('--num_workers', type=int, default=0, help='')


def main():
    print("Starting...")

    args = parser.parse_args()

    class Net(pl.LightningModule):

       def __init__(self):
          super(Net, self).__init__()

          self.conv1 = nn.Conv2d(3, 6, 5)
          self.pool = nn.MaxPool2d(2, 2)
          self.conv2 = nn.Conv2d(6, 16, 5)
          self.fc1 = nn.Linear(16 * 5 * 5, 120)
          self.fc2 = nn.Linear(120, 84)
          self.fc3 = nn.Linear(84, 10)

       def forward(self, x):
          x = self.pool(F.relu(self.conv1(x)))
          x = self.pool(F.relu(self.conv2(x)))
          x = x.view(-1, 16 * 5 * 5)
          x = F.relu(self.fc1(x))
          x = F.relu(self.fc2(x))
          x = F.relu(self.fc3(x))
          return x

       def training_step(self, batch, batch_idx):
          x, y = batch
          y_hat = self(x)
          loss = F.cross_entropy(y_hat, y)
          return loss

       def configure_optimizers(self):
          return torch.optim.Adam(self.parameters(), lr=args.lr)

    net = Net()

    """ Ici, nous initialisons un Trainer() explicitement avec 1 nœud et 2 GPU par nœud.
        Pour rendre ce script plus générique, vous pouvez utiliser torch.cuda.device_count() pour définir le nombre de GPU
        et vous pouvez utiliser int(os.environ.get("SLURM_JOB_NUM_NODES")) pour définir le nombre de nœuds.
        Nous définissons également progress_bar_refresh_rate=0 pour éviter d'écrire une barre de progression dans les journaux,
        ce qui peut causer des problèmes en raison de mises à jour trop fréquentes des journaux. """

    trainer = pl.Trainer(accelerator="gpu", devices=2, num_nodes=1, strategy='ddp', max_epochs = args.max_epochs, enable_progress_bar=False)

    transform_train = transforms.Compose([transforms.ToTensor(),transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    dataset_train = CIFAR10(root='./data', train=True, download=False, transform=transform_train)

    train_loader = DataLoader(dataset_train, batch_size=args.batch_size, num_workers=args.num_workers)

    trainer.fit(net,train_loader)


if __name__=='__main__':
   main()
```

### Parallélisme des données avec un seul GPU

Il **n’est pas conseillé d’utiliser un GPU** avec un modèle de taille relativement petite qui n’utilise pas une grande part de la mémoire du GPU et une part raisonnable de sa capacité de calcul; utilisez plutôt [un ou plusieurs CPU](#travailler-avec-un-cpu). Par contre, profiter du parallélisme du GPU devient une bonne option si vous avez un tel modèle avec un très grand jeu de données et que vous voulez effectuer l’entraînement avec des lots de petite taille.

Dans l'exemple suivant, nous adaptons le code de la section précédente pour l'exécuter sur un seul GPU. Cette tâche est relativement simple : avec un lot de 512 images, notre modèle occupe environ 1 Go de mémoire GPU et n'utilise qu'environ 6% de sa capacité de calcul pendant l'entraînement. Ce modèle **ne devrait pas être entraîné** sur un seul GPU de nos grappes. Cependant, avec le parallélisme des données, nous pouvons exécuter plusieurs copies (*replicas*) de ce modèle sur un seul GPU et optimiser l'utilisation des ressources, tout en obtenant un gain de vitesse appréciable. Nous utilisons [le service Multi-Process (MPS)](https://docs.nvidia.com/deploy/mps/index.html) de Nvidia ainsi que [MPI](mpi.md) pour déployer efficacement plusieurs copies du modèle sur un seul GPU.

```bash title="pytorch-gpu-mps.sh"
#!/bin/bash
#SBATCH --nodes 1
#SBATCH --gres=gpu:1 # demande un GPU
#SBATCH --tasks-per-node=8 # C'est le nombre de réplicas de modèles que nous allons placer sur le GPU. Changez-le à 10,12,14,... pour voir l'effet sur la performance
#SBATCH --cpus-per-task=1 # augmentez ce paramètre et augmentez "--num_workers" en conséquence pour voir l'effet sur la performance
#SBATCH --mem=8G
#SBATCH --time=0:05:00
#SBATCH --output=%N-%j.out
#SBATCH --account=<your account>

module load python # Utilisation de la version Python par défaut - assurez-vous de choisir une version adaptée à votre application
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate
pip install torch torchvision --no-index

# Activer Nvidia MPS :
export CUDA_MPS_PIPE_DIRECTORY=/tmp/nvidia-mps
export CUDA_MPS_LOG_DIRECTORY=/tmp/nvidia-log
nvidia-cuda-mps-control -d

echo "starting training..."
time srun --cpus-per-task=$SLURM_CPUS_PER_TASK python cifar10-gpu-mps.py --batch_size=512 --num_workers=0
```

```python title="cifar10-gpu-mps.py"
import os
import time
import datetime
import numpy as np

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

import torchvision
import torchvision.transforms as transforms
from torchvision.datasets import CIFAR10
from torch.utils.data import DataLoader

import torch.distributed as dist
import torch.utils.data.distributed

import argparse

parser = argparse.ArgumentParser(description='cifar10 classification models, distributed data parallel maps test')
parser.add_argument('--lr', default=0.1, help='')
parser.add_argument('--batch_size', type=int, default=512, help='')
parser.add_argument('--num_workers', type=int, default=0, help='')
parser.add_argument('--init_method', default='tcp://127.0.0.1:3456', type=str, help='')

def main():
    print("Starting...")

    args = parser.parse_args()

    rank = os.environ.get("SLURM_LOCALID")

    current_device = 0
    torch.cuda.set_device(current_device)

    """ ce bloc initialise un groupe de processus et initie les communications
                entre tous les processus qui exécuteront une réplica de modèle """

    print('From Rank: {}, ==> Initializing Process Group...'.format(rank))

    dist.init_process_group(backend="mpi", init_method=args.init_method) # Utilisez backend="mpi" ou "gloo". NCCL ne fonctionne pas sur un seul GPU en raison d'une vérification de topologie multi-GPU codée en dur.
    print("process group ready!")

    print('From Rank: {}, ==> Making model..'.format(rank))

    class Net(nn.Module):

       def __init__(self):
          super(Net, self).__init__()

          self.conv1 = nn.Conv2d(3, 6, 5)
          self.pool = nn.MaxPool2d(2, 2)
          self.conv2 = nn.Conv2d(6, 16, 5)
          self.fc1 = nn.Linear(16 * 5 * 5, 120)
          self.fc2 = nn.Linear(120, 84)
          self.fc3 = nn.Linear(84, 10)

       def forward(self, x):
          x = self.pool(F.relu(self.conv1(x)))
          x = self.pool(F.relu(self.conv2(x)))
          x = x.view(-1, 16 * 5 * 5)
          x = F.relu(self.fc1(x))
          x = F.relu(self.fc2(x))
          x = F.relu(self.fc3(x))
          return x

    net = Net()

    net.cuda()
    net = torch.nn.parallel.DistributedDataParallel(net, device_ids=[current_device]) # Enveloppe le modèle avec DistributedDataParallel

    criterion = nn.CrossEntropyLoss().cuda()
    optimizer = optim.SGD(net.parameters(), lr=args.lr)

    print('From Rank: {}, ==> Preparing data..'.format(rank))

    transform_train = transforms.Compose([transforms.ToTensor(),transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    dataset_train = CIFAR10(root='~/data', train=True, download=False, transform=transform_train)

    train_sampler = torch.utils.data.distributed.DistributedSampler(dataset_train)
    train_loader = DataLoader(dataset_train, batch_size=args.batch_size, shuffle=(train_sampler is None), num_workers=args.num_workers, sampler=train_sampler)

    perf = []

    total_start = time.time()

    for batch_idx, (inputs, targets) in enumerate(train_loader):

       start = time.time()

       inputs = inputs.cuda()
       targets = targets.cuda()

       outputs = net(inputs)
       loss = criterion(outputs, targets)

       optimizer.zero_grad()
       loss.backward()
       optimizer.step()

       batch_time = time.time() - start

       images_per_sec = args.batch_size/batch_time

       perf.append(images_per_sec)

    total_time = time.time() - total_start

if __name__=='__main__':
   main()
```

### Parallélisme de données entièrement fragmentées (FSDP)

Similaire à DeepSpeed, le parallélisme de données entièrement fragmentées ([FSDP](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html)) permet le stockage et le calcul distribués de différents éléments d'une tâche d'entraînement – tels que les états d'optimiseur, les poids du modèle, les gradients du modèle et les activations du modèle – sur plusieurs appareils, y compris le GPU, le CPU, le disque dur local, et/ou des combinaisons de ces appareils. Cette "mise en commun" des ressources, notamment pour le stockage, permet d'entraîner efficacement des modèles avec des quantités massives de paramètres, sur plusieurs nœuds.

Notez qu'avec FSDP, une couche de modèle qui est fragmentée sur plusieurs appareils peut être collectée dans un seul appareil pendant un passage avant ou arrière. Vous ne devriez pas utiliser FSDP si votre modèle a des couches qui ne rentrent pas entièrement dans la mémoire d'un seul GPU. Consultez la section sur le [Parallélisme tensoriel](#parallélisme-tensoriel) pour savoir comment gérer ce cas.

### Parallélisme tensoriel

Le parallélisme tensoriel (TP) est une approche de fragmentation de modèle qui diffère du FSDP en ce que le calcul d'un passage avant ou arrière à travers une couche de modèle est divisé avec les poids des couches sur plusieurs appareils. En d'autres termes, alors que FSDP fragmente les poids du modèle sur plusieurs appareils, il doit toujours collecter les fragments dans le même appareil pendant certaines étapes de calcul. Cela introduit une surcharge due au déplacement des fragments de modèle entre les appareils, et cela implique que les couches FSDP individuelles, ou les blocs de modèle fragmentés, doivent s'adapter entièrement à la mémoire d'un seul appareil. Avec le TP, par contre, les étapes de calcul sont effectuées localement dans l'appareil où un fragment de modèle est placé.

### Parallélisme de pipeline

Le parallélisme de pipeline (PP) est une approche de fragmentation de modèle où les fragments sont des groupes de couches consécutives d'un modèle. Chaque fragment, ou bloc de couches séquentielles, est placé sur un appareil différent, de sorte qu'un passage avant ou arrière à travers le modèle signifie effectuer des calculs sur chaque appareil *en séquence*. Cela signifie que plus un bloc de couches est éloigné du bloc courant utilisé dans un calcul à un moment donné, plus l'appareil qui l'héberge devra attendre son tour pour effectuer des calculs. Pour atténuer cela, en PP, chaque lot d'entrée est divisé en "*micro-lots*", qui sont introduits dans le modèle en séquence. Cela garantit que tous les appareils restent occupés dès que le premier micro-lot atteint le dernier bloc de modèle.

## Créer des points de contrôle

Que votre code s'exécute ou non pendant de longues périodes, il est recommandé de créer des points de contrôle pendant l'entraînement. Un point de contrôle est un instantané de votre modèle à un moment donné du processus d'entraînement (après un certain nombre d'itérations ou d'époques), enregistré sur disque et pouvant être chargé ultérieurement. C'est un moyen pratique de découper les tâches de longue durée en plusieurs tâches plus courtes, qui peuvent être allouées plus rapidement sur la grappe. C'est également un bon moyen d'éviter de perdre le déroulement en cas d'erreurs inattendues dans votre code ou de panne du nœud.

### Avec PyTorch Lightning

Nous recommandons d'utiliser le paramètre de rappels (*callbacks parameter*) de la classe `Trainer()`. Dans l'exemple suivant, on demande à PyTorch de créer un point de contrôle à la fin de chacune des époques d'entraînement. Vérifiez que le chemin où créer le point de contrôle existe.

```python
callbacks = [pl.callbacks.ModelCheckpoint(dirpath="./ckpt",every_n_epochs=1)]
trainer = pl.Trainer(callbacks=callbacks)
trainer.fit(model)
```

Ce bout de code chargera un point de contrôle de `./ckpt` (s'il en existe) et poursuivra l'entraînement à partir de ce point. Pour plus d'information, consultez la [documentation PyTorch Lightning](https://pytorch-lightning.readthedocs.io/en/stable/api/pytorch_lightning.callbacks.model_checkpoint.html).

### Avec des boucles d'entraînement personnalisées

Pour des exemples, consultez [la documentation PyTorch](https://pytorch.org/tutorials/recipes/recipes/saving_and_loading_a_general_checkpoint.html).

### Pendant l’entraînement distribué

Les points de contrôle peuvent être utilisés pendant l’exécution d’un programme d’entraînement distribué. Avec PyTorch Lightning, aucun code supplémentaire n’est requis, autre que d’insérer le paramètre de rappels (*callbacks parameter*) comme mentionné ci-dessus. Cependant, si vous utilisez DistributedDataParallel ou Horovod, les points de contrôle devront être créés par un seul processus (*rank*) de votre programme puisque tous les processus auront le même état après chaque itération. Dans cet exemple, le premier processus (*rank 0*) crée un point de contrôle.

```python
if global_rank == 0:
       torch.save(ddp_model.state_dict(), "./checkpoint_path")
```

Faites attention aux points de contrôle ainsi créés. Si un processus tente de charger un point de contrôle qui n’a pas encore été sauvegardé par un autre, des erreurs peuvent survenir ou de mauvais résultats peuvent être produits. Pour éviter ceci, vous pouvez ajouter une barrière à votre code pour faire en sorte que le processus qui crée le point de contrôle a terminé son écriture sur le disque avant que d’autres processus tentent de le charger. Remarquez aussi que `torch.load` essaiera par défaut de charger les tenseurs sur le GPU sur lequel ils étaient initialement sauvegardés, dans notre cas `cuda:0`. Pour éviter les problèmes, passez `map_location` à `torch.load` pour charger les tenseurs sur le GPU identifié par chaque processus.

```python
torch.distributed.barrier()
map_location = f"cuda:{local_rank}"
ddp_model.load_state_dict(
torch.load("./checkpoint_path", map_location=map_location))
```

## Dépannage

### Erreur CUDA : no kernel image is available for execution on the device

Cette exception signifie que l'installation courante de Torch ne prend pas en charge l'architecture de calcul ou le GPU utilisé.
Vous pouvez installer une version plus récente de `torch` ou demander un GPU compatible avec la version que vous utilisez.

## LibTorch

LibTorch permet d'implémenter à PyTorch des extensions C++ et des **applications d'apprentissage machine en C++ pur**. La distribution LibTorch possède les en-têtes, bibliothèques et fichiers de configuration CMake nécessaires pour travailler avec PyTorch, tel que décrit dans la [documentation](https://pytorch.org/cppdocs/installing.html).

### Utiliser LibTorch

#### Configurer l'environnement

Chargez les modules requis par LibTorch, puis installez PyTorch dans un environnement virtuel Python.

=== "StdEnv/2023"

    ```bash
    module load StdEnv/2023 gcc cuda/12.2 cmake protobuf cudnn python/3.11 abseil  cusparselt  opencv/4.8.1
    virtualenv --no-download --clear ~/ENV && source ~/ENV/bin/activate
    pip install --no-index torch numpy
    ```

    Vous devrez peut-être ajuster les versions des modules abseil, cusparselt et opencv, dépendant du package torch que vous utilisez. Pour savoir quelle version d'un module a été utilisée pour compiler le wheel Python, lancez la commande :

    ```bash
    $ ldd $VIRTUAL_ENV/lib/python3.11/site-packages/torch/lib/libtorch_cuda.so | sed -n 's&^.*/\(\(opencv\|abseil\|cusparselt\)/[^/]*\).*&\1&p' | sort -u
    ```

    ```text title="Résultat"
    abseil/20230125.3
    cusparselt/0.5.0.1
    opencv/4.8.1
    ```

=== "StdEnv/2020"

    ```bash
    module load gcc cuda/11.4 cmake protobuf cudnn python/3.10
    virtualenv --no-download --clear ~/ENV && source ~/ENV/bin/activate
    pip install --no-index torch numpy
    ```

#### Compiler un exemple simple

Créez les deux fichiers suivants :

```cpp title="example.cpp"
#include <torch/torch.h>
#include <iostream>

int main()
{
    torch::Device device(torch::kCPU);
    if (torch::cuda::is_available())
    {
        std::cout << "CUDA is available! Using GPU." << std::endl;
        device = torch::Device(torch::kCUDA);
    }

    torch::Tensor tensor = torch::rand({2, 3}).to(device);
    std::cout << tensor << std::endl;
}
```

```text title="CMakeLists.txt"
cmake_minimum_required(VERSION 3.0 FATAL_ERROR)
project(example)

find_package(Torch REQUIRED)

add_executable(example example.cpp)
target_link_libraries(example "${TORCH_LIBRARIES}")
set_property(TARGET example PROPERTY CXX_STANDARD 14)
```

Activez l'environnement virtuel Python, configurez le projet et compilez le programme.

=== "StdEnv/2023"

    ```bash
    cmake -B build -S . -DCMAKE_PREFIX_PATH=$VIRTUAL_ENV/lib/python3.11/site-packages \
                        -DCMAKE_EXE_LINKER_FLAGS=-Wl,-rpath=$VIRTUAL_ENV/lib/python3.11/site-packages/torch/lib,-L$EBROOTCUDA/extras/CUPTI/lib64 \
                        -DCMAKE_SKIP_RPATH=ON -DTORCH_CUDA_ARCH_LIST="6.0;7.0;7.5;8.0;9.0"
    cmake --build build
    ```

=== "StdEnv/2020"

    ```bash
    cmake -B build -S . -DCMAKE_PREFIX_PATH=$VIRTUAL_ENV/lib/python3.10/site-packages \
                        -DCMAKE_EXE_LINKER_FLAGS=-Wl,-rpath=$VIRTUAL_ENV/lib/python3.10/site-packages/torch/lib \
                        -DCMAKE_SKIP_RPATH=ON
    cmake --build build
    ```

Lancez le programme avec :

```bash
build/example
```

Pour tester une application avec CUDA, demandez une [tâche interactive](running-jobs.md#tâches-interactives) avec [GPU](using-gpus-with-slurm.md).

## rTorch

Pour installer `rTorch` à partir d'un nœud de connexion :

1.  Chargez les modules requis.

    ```bash
    module load r/4.5 cuda/12.6 cudnn
    ```

2.  Créez votre répertoire d'installation avec les instructions dans [Installation pour une ou plusieurs versions de R](r.md#installation-pour-une-ou-plusieurs-versions-de-r) :

    ```bash
    mkdir -p ~/.local/R/$EBVERSIONR/
    export R_LIBS=~/.local/R/$EBVERSIONR/
    ```

3.  Installez la plus récente version disponible de rtorch.

    ```bash
    R -e 'install.packages("torch", repos="https://cloud.r-project.org/")'
    ```

4.  Installez les dépendances.

    ```bash
    R -e 'torch::install_torch()'
    ```

5.  Corrigez la bibliothèque partagée qui a été téléchargée (*lantern*).

    ```bash
    setrpaths.sh --path $R_LIBS/torch/lib/liblantern.so --add_path $EBROOTCUDACORE/lib --any_interpreter
    ```

6.  Effectuez un test rapide de CPU.

    ```bash
    R -e 'torch::torch_tensor(1);'
    ```

    ```text title="Résultat"
    > torch::torch_tensor(1);
    torch_tensor
     1
    [ CPUFloatType{1} ]
    ```

7.  Effectuez un test de GPU.

    ```bash
    srun --mem=3500M --gpus=h100_1g.10gb:1 -- R -e 'torch::torch_tensor(1)$cuda()'
    ```

    ```text title="Résultat"
    > torch::torch_tensor(1)$cuda();
    torch_tensor
     1
    [ CUDAFloatType{1} ]
    ```

## Ressources

[Documentation PyTorch C++](https://pytorch.org/cppdocs/)