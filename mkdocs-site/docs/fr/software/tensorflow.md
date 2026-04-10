---
title: "TensorFlow/fr"
tags:
  - software
  - ai-and-machine-learning

keywords:
  []
---

[TensorFlow](https://www.tensorflow.org/) est une bibliothèque logicielle <i>open source</i> d'apprentissage machine.

Si vous voulez porter un programme TensorFlow sur une de nos grappes, nous vous recommandons de prendre connaissance du [tutoriel sur l'apprentissage machine](tutoriel-apprentissage-machine.md).

<span id="Installing_TensorFlow"></span>
## Installation

Les directives suivantes servent à installer TensorFlow dans votre répertoire <i>home</i> à l'aide des ([<i>wheels</i> Python ](http://pythonwheels.com/)) qui se trouvent dans `/cvmfs/soft.computecanada.ca/custom/python/wheelhouse/`. 

Le wheel TensorFlow sera installé dans un [environnement virtuel Python](python-fr#créer_et_utiliser_un_environnement_virtuel.md) avec la commande `pip`.

<tabs>
<tab name="TF 2.x">

Chargez les modules requis par TensorFlow; dans certains cas, d'autres modules pourraient être requis (par exemple CUDA).

```bash
module load python/3
```

Créez un nouvel environnement Python.

```bash
virtualenv --no-download tensorflow
```

Activez le nouvel environnement.

```bash
source tensorflow/bin/activate
```

Installez TensorFlow dans votre nouvel environnement virtuel en utilisant la commande suivante.

```bash
pip install --no-index tensorflow
```

</tab>
<tab name="TF 1.x">

Chargez les modules requis par TensorFlow. TF 1.x requiert StdEnv/2018.

<b>Remarque : TF 1.x n'est pas disponible sur Narval, puisque cette grappe n'offre pas StdEnv/2018.</b>

```bash
module load StdEnv/2018 python/3
```

Créez un nouvel environnement Python.

```bash
virtualenv --no-download tensorflow
```

Activez le nouvel environnement.

```bash
source tensorflow/bin/activate
```

Installez TensorFlow dans votre nouvel environnement virtuel en utilisant une des commandes suivantes, dépendant de si vous avez besoin d'utiliser un GPU.

<b>N'installez pas</b> le paquet `tensorflow` sans le suffixe `_cpu` ou `_gpu` car il existe des problèmes de compatibilité avec d'autres bibliothèques.

<span id="CPU-only"></span>
### CPU seulement 

```bash

```
1.15.0}}

### GPU 

```bash

```
1.15.0}}
</tab>
</tabs>

<span id="R_package"></span>
### Le paquet R  

Pour utiliser TensorFlow en R, suivez les directives données ci-dessus pour créer un environnement virtuel et y installer TensorFlow. Suivez ensuite cette procédure ː

Chargez les modules requis.

```bash
module load gcc r
```

Activez votre environnement virtuel Python.

```bash
source tensorflow/bin/activate
```

Lancez R.

```bash
R
```

En R, installez le paquet devtools, puis TensorFlow. 
<syntaxhighlight lang="r">
install.packages('devtools', repos='https://cloud.r-project.org')
devtools::install_github('rstudio/tensorflow')
</syntaxhighlight>

Vous pouvez maintenant procéder. N'appelez pas `install_tensorflow()` en R puisque TensorFlow est déjà installé dans votre environnement virtuel avec `pip`. Pour utiliser TensorFlow tel qu'installé dans votre environnement virtuel, entrez les commandes suivantes en R, après que l'environnement est activé.

<syntaxhighlight lang="r">
library(tensorflow)
use_virtualenv(Sys.getenv('VIRTUAL_ENV'))
</syntaxhighlight>

## Soumettre une tâche TensorFlow avec un GPU
Soumettez une tâche TensorFlow ainsi 

```bash
sbatch tensorflow-test.sh
```

Le script contient

**`tensorflow-test.sh`**
```bash
#!/bin/bash
#SBATCH --gres=gpu:1        # request GPU "generic resource"
#SBATCH --cpus-per-task=6   # maximum CPU cores per GPU request. See https://docs.alliancecan.ca/wiki/Allocations_and_compute_scheduling#Ratios_in_bundles
#SBATCH --mem=32000M        # memory per node
#SBATCH --time=0-03:00      # time (DD-HH:MM)
#SBATCH --output=%N-%j.out  # %N for node name, %j for jobID

module load cuda cudnn 
source tensorflow/bin/activate
python ./tensorflow-test.py
```

Le script Python se lit

<tabs>
<tab name="TF 2.x">

**`tensorflow-test.py`**
```python
import tensorflow as tf
node1 = tf.constant(3.0)
node2 = tf.constant(4.0)
print(node1, node2)
print(node1 + node2)
```

</tab>
<tab name="TF 1.x">

**`tensorflow-test.py`**
```python
import tensorflow as tf
node1 = tf.constant(3.0)
node2 = tf.constant(4.0)
print(node1, node2)
sess = tf.Session()
print(sess.run(node1 + node2))
```

</tab>
</tabs>

Une fois la tâche terminée, ce qui devrait nécessiter moins d'une minute, un fichier de sortie avec un nom semblable à `node_id-job_id.out` devrait être généré. Le contenu de ce fichier serait similaire à ce qui suit; il s'agit d'exemples de messages TensorFlow et il est possible que vous en ayez d'autres.

<tabs>
<tab name="TF 2.x">

**`node_id-job_id.out`**
```text
2017-07-10 12:35:19.491097: I tensorflow/core/common_runtime/gpu/gpu_device.cc:961] DMA: 0
2017-07-10 12:35:19.491156: I tensorflow/core/common_runtime/gpu/gpu_device.cc:971] 0:   Y
2017-07-10 12:35:19.520737: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1030] Creating TensorFlow device (/gpu:0) -> (device: 0, name: Tesla P100-PCIE-12GB, pci bus id: 0000:82:00.0)
tf.Tensor(3.0, shape=(), dtype=float32) tf.Tensor(4.0, shape=(), dtype=float32)
tf.Tensor(7.0, shape=(), dtype=float32)
```

</tab>
<tab name="TF 1.x">

**`node_id-job_id.out`**
```text
2017-07-10 12:35:19.491097: I tensorflow/core/common_runtime/gpu/gpu_device.cc:961] DMA: 0
2017-07-10 12:35:19.491156: I tensorflow/core/common_runtime/gpu/gpu_device.cc:971] 0:   Y
2017-07-10 12:35:19.520737: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1030] Creating TensorFlow device (/gpu:0) -> (device: 0, name: Tesla P100-PCIE-12GB, pci bus id: 0000:82:00.0)
Tensor("Const:0", shape=(), dtype=float32) Tensor("Const_1:0", shape=(), dtype=float32)
7.0
```

</tab>
</tabs>

TensorFlow fonctionne sur tous les types de nœuds GPU. Pour plus d'information, voir [cette page](using-gpus-with-slurm-fr.md).

<span id="Monitoring"></span>
## Suivi

Il est possible de se connecter à un nœud sur lequel une tâche est en cours pour y exécuter des processus. On peut ainsi faire le suivi des ressources utilisées par TensorFlow et visualiser le déroulement de l'entraînement. Pour des exemples, consultez [Surveillance d'une tâche en cours](running-jobs-fr#surveillance_d'une_tâche_en_cours.md).

### TensorBoard

TensorFlow propose la suite d'outils de visualisation [TensorBoard](https://www.tensorflow.org/programmers_guide/summaries_and_tensorboard) qui lit les événements TensorFlow et modélise les fichiers. Pour savoir comment créer ces fichiers, consultez [TensorBoard tutorial on summaries](https://www.tensorflow.org/programmers_guide/summaries_and_tensorboard#serializing_the_data).

Sachez toutefois que TensorBoard exige trop de puissance de calcul pour être exécuté sur un nœud de connexion. Nous vous recommandons de l'exécuter dans la même tâche que le processus TensorFlow. Pour ce faire, lancez TensorBoard en arrière-plan en l'appelant avant le script Python, en y ajoutant le caractère (`&`).

 # Your SBATCH arguments here
 
 tensorboard --logdir=/tmp/your_log_dir --host 0.0.0.0 --load_fast false &
 python train.py  # example

Pour accéder TensorBoard avec un fureteur une fois que la tâche est en cours, il faut créer un lien entre votre ordinateur et le nœud sur lequel TensorFlow et TensorBoard sont exécutés. Pour ce faire, vous avez besoin du <i>hostname</i> du nœud de calcul sur lequel le serveur TensorFlow se trouve. Pour le trouver, faites afficher la liste de vos tâches avec la commande `sq` et repérez la tâche; le <i>hostname</i> est la valeur qui se trouve dans la colonne NODELIST.

Pour créer la connexion, lancez la commande sur votre ordinateur local.

```bash
ssh -N -f -L localhost:6006:computenode:6006 userid@cluster.computecanada.ca
```

Remplacez `computenode` par le <i>hostname</i> obtenu à l'étape précédente; `userid` par votre nom d'utilisateur de l'Alliance et; `cluster` par le <i>hostname</i> de la grappe, soit `rorqual`, `fir`, `nibi`, etc. Si le port 6006 était déjà utilisé, tensorboard va en utiliser un autre (p. ex. 6007, 6008...).

Une fois que la connexion est établie, allez à [http://localhost:6006](http://localhost:6006).

<span id="TensorFlow_with_multi-GPUs"></span>
## Utiliser plusieurs GPU

TensorFlow offre des stratégies différentes pour utiliser plusieurs GPU avec l'API de haut niveau `tf.distribute`. Dans les sections qui suivent, nous montrons des exemples de code pour chacune des stratégies avec Keras. Pour plus d'information, consultez la [documentation officielle de TensorFlow](https://www.tensorflow.org/api_docs/python/tf/distribute).

<span id="Mirrored_strategy"></span>
#### Stratégie miroir

<span id="Single_node"></span>
=====Nœud unique=====

**`tensorflow-singleworker.sh`**
```bash
#!/bin/bash
#SBATCH --nodes 1
#SBATCH --gres=gpu:4

#SBATCH --mem=8G      
#SBATCH --time=0-00:30
#SBATCH --output=%N-%j.out

module load python/3
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate
pip install --no-index tensorflow

export NCCL_BLOCKING_WAIT=1  #Set this environment variable if you wish to use the NCCL backend for inter-GPU communication.

python tensorflow-singleworker.py
```

Le script Python `tensorflow-singleworker.py` a le format

**`tensorflow-singleworker.py`**
```python
import tensorflow as tf
import numpy as np

import argparse

parser = argparse.ArgumentParser(description='cifar10 classification models, tensorflow MirroredStrategy test')
parser.add_argument('--lr', default=0.001, help='')
parser.add_argument('--batch_size', type=int, default=256, help='')

args = parser.parse_args()

strategy = tf.distribute.MirroredStrategy()

with strategy.scope():

    model = tf.keras.Sequential()

    model.add(tf.keras.layers.Conv2D(32, (3, 3), padding='same',
                 input_shape=(32,32,3)))
    model.add(tf.keras.layers.Activation('relu'))
    model.add(tf.keras.layers.Conv2D(32, (3, 3)))
    model.add(tf.keras.layers.Activation('relu'))
    model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
    model.add(tf.keras.layers.Dropout(0.25))

    model.add(tf.keras.layers.Conv2D(64, (3, 3), padding='same'))
    model.add(tf.keras.layers.Activation('relu'))
    model.add(tf.keras.layers.Conv2D(64, (3, 3)))
    model.add(tf.keras.layers.Activation('relu'))
    model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
    model.add(tf.keras.layers.Dropout(0.25))

    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(512))
    model.add(tf.keras.layers.Activation('relu'))
    model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Dense(10))

    model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
         optimizer=tf.keras.optimizers.SGD(learning_rate=args.lr),metrics=['accuracy'])

### This next line will attempt to download the CIFAR10 dataset from the internet if you don't already have it stored in ~/.keras/datasets. 
### Run this line on a login node prior to submitting your job, or manually download the data from 
### https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz, rename to "cifar-10-batches-py.tar.gz" and place it under ~/.keras/datasets

(x_train, y_train),_ = tf.keras.datasets.cifar10.load_data()

dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train)).batch(args.batch_size)

model.fit(dataset, epochs=2)
```

<span id="Multiple_nodes"></span>
=====Nœuds multiples=====

La syntaxe pour utiliser des GPU distribués sur plusieurs nœuds ressemble beaucoup au cas du nœud simple; la différence principale est l'emploi de `MultiWorkerMirroredStrategy()`. Ici, nous utilisons `SlurmClusterResolver()` pour dire à TensorFlow d'obtenir par Slurm l'information sur la tâche plutôt que d'assigner manuellement un nœud principal et des nœuds secondaires (*workers*), par exemple. Nous devons aussi ajouter `CommunicationImplementation.NCCL` à la stratégie de distribution pour indiquer que nous voulons utiliser la bibliothèque NCCL de NVIDIA pour les communications entre les GPU. Ceci n'était pas nécessairement le cas pour un nœud simple puisque NCCL se trouve par défaut avec `MirroredStrategy()`.

**`tensorflow-multiworker.sh`**
```bash
#!/bin/bash
#SBATCH --nodes 2              # Request 2 nodes so all resources are in two nodes.
#SBATCH --gres=gpu:2          # Request 2 GPU "generic resources”. You will get 2 per node.

#SBATCH --ntasks-per-node=2   # Request 1 process per GPU. You will get 1 CPU per process by default. Request more CPUs with the "cpus-per-task" parameter if your input pipeline can handle parallel data-loading/data-transforms

#SBATCH --mem=8G      
#SBATCH --time=0-00:30
#SBATCH --output=%N-%j.out

srun -N $SLURM_NNODES -n $SLURM_NNODES config_env.sh

module load gcc/9.3.0 cuda/11.8
export NCCL_BLOCKING_WAIT=1  #Set this environment variable if you wish to use the NCCL backend for inter-GPU communication.
export XLA_FLAGS=--xla_gpu_cuda_data_dir=$CUDA_HOME

srun launch_training.sh
```

où `config_env.sh` a la forme

**`config_env.sh`**
```bash
#!/bin/bash

module load python

virtualenv --no-download $SLURM_TMPDIR/ENV

source $SLURM_TMPDIR/ENV/bin/activate

pip install --upgrade pip --no-index

pip install --no-index tensorflow

echo "Done installing virtualenv!"
```

Le script `launch_training.sh` a la forme

**`launch_training.sh`**
```bash
#!/bin/bash

source $SLURM_TMPDIR/ENV/bin/activate

python tensorflow-multiworker.py
```

Le script Python `tensorflow-multiworker.py` a la forme suivante&nbsp;:

**`tensorflow-multiworker.py`**
```python
import tensorflow as tf
import numpy as np

import argparse

parser = argparse.ArgumentParser(description='cifar10 classification models, tensorflow MultiWorkerMirrored test')
parser.add_argument('--lr', default=0.001, help='')
parser.add_argument('--batch_size', type=int, default=256, help='')

args = parser.parse_args()

cluster_config = tf.distribute.cluster_resolver.SlurmClusterResolver()
comm_options = tf.distribute.experimental.CommunicationOptions(implementation=tf.distribute.experimental.CommunicationImplementation.NCCL)

strategy = tf.distribute.MultiWorkerMirroredStrategy(cluster_resolver=cluster_config, communication_options=comm_options)

with strategy.scope():

    model = tf.keras.Sequential()

    model.add(tf.keras.layers.Conv2D(32, (3, 3), padding='same',
                 input_shape=(32,32,3)))
    model.add(tf.keras.layers.Activation('relu'))
    model.add(tf.keras.layers.Conv2D(32, (3, 3)))
    model.add(tf.keras.layers.Activation('relu'))
    model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
    model.add(tf.keras.layers.Dropout(0.25))

    model.add(tf.keras.layers.Conv2D(64, (3, 3), padding='same'))
    model.add(tf.keras.layers.Activation('relu'))
    model.add(tf.keras.layers.Conv2D(64, (3, 3)))
    model.add(tf.keras.layers.Activation('relu'))
    model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
    model.add(tf.keras.layers.Dropout(0.25))

    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(512))
    model.add(tf.keras.layers.Activation('relu'))
    model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Dense(10))

    model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
         optimizer=tf.keras.optimizers.SGD(learning_rate=args.lr),metrics=['accuracy'])

### This next line will attempt to download the CIFAR10 dataset from the internet if you don't already have it stored in ~/.keras/datasets. 
### Run this line on a login node prior to submitting your job, or manually download the data from 
### https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz, rename to "cifar-10-batches-py.tar.gz" and place it under ~/.keras/datasets

(x_train, y_train),_ = tf.keras.datasets.cifar10.load_data()

dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train)).batch(args.batch_size)

model.fit(dataset, epochs=2)
```

## Créer des points de contrôle
Peu importe le temps que dure l'exécution de votre code, une bonne habitude à prendre est de créer des points de contrôle pendant l'entraînement. Un point de contrôle vous donne le portrait de votre modèle à un moment précis du processus d'entraînement (après un certain nombre d'itérations ou d'époques); le portrait est enregistré sur disque et vous pourrez le récupérer par la suite. Ceci est pratique pour diviser en petites tâches une tâche qui doit avoir un long temps d'exécution, ce qui pourrait faire qu'elles soient être allouées plus rapidement à une grappe. C'est aussi un bon moyen d'éviter de perdre votre travail en cas d'erreurs inattendues ou de panne du matériel.

<span id="With_Keras"></span>
### Avec Keras

Pour créer un point de contrôle dans un entraînement avec `keras`, nous recommandons le paramètre `callbacks` de la méthode `model.fit()`. Dans l'exemple suivant, nous demandons à TensorFlow de créer un point de contrôle à la fin de chacune des époques d'entraînement.

 callbacks = [tf.keras.callbacks.ModelCheckpoint(filepath="./ckpt",save_freq="epoch")] # Make sure the path where you want to create the checkpoint exists
 
 model.fit(dataset, epochs=10 , callbacks=callbacks)

Pour plus d'information, consultez la [documentation officielle de TensorFlow](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint).

<span id="With_a_custom_training_loop"></span>
### Avec une boucle d'entraînement personnalisée

Voyez la [documentation officielle de TensorFlow](https://www.tensorflow.org/guide/checkpoint#writing_checkpoints).

<span id="Troubleshooting"></span>
## Dépannage

<span id="scikit_image"></span>
### scikit-image

Si vous utilisez la bibliothèque scikit-image, vous pourriez recevoir l'erreur
`OMP: Error #15: Initializing libiomp5.so, but found libiomp5.so already initialized. `

Ceci se produit quand la bibliothèque TensorFlow essaie de charger une version de OMP incompatible avec la version du système. Pour contourner ceci&nbsp;:

```bash

```
$(strace python -c 'from skimage.transform import AffineTransform' 2>&1  grep -v ENOENT  grep -ohP -e '(?<")[^"]+libiomp5.so(?")'  xargs realpath)
|find -path '*_solib_local*' -name libiomp5.so -exec ln -sf $LIBIOMP_PATH {} \;
}}
L'installation de la bibliothèque TensorFlow pourra alors utiliser libiomp5.so.

### libcupti.so

Certaines fonctions de suivi de TensorFlow utilisent la bibliothèque libcupti.so; si cette dernière n'est pas disponible, l'erreur suivante pourrait survenir :

`I tensorflow/stream_executor/dso_loader.cc:142] Couldn't open CUDA library libcupti.so.9.0. LD_LIBRARY_PATH: /usr/local/cuda-9.0/lib64`

La solution est d'exécuter les commandes suivantes avant l'exécution du script.

```bash

```
$LD_LIBRARY_PATH:$CUDA_HOME/extras/CUPTI/lib64/
}}
Remplacez xxx par la version appropriée de CUDA que vous pouvez trouver avec `module av cuda`.

### libiomp5.so invalid ELF header

Le fichier objet partagé `libiomp5.so` est quelquefois par erreur installé en tant que fichier texte, ce qui peut produire des erreurs comme ceci :

`/home/username/venv/lib/python3.6/site-packages/tensorflow/python/../../_solib_local/_U@mkl_Ulinux_S_S_Cmkl_Ulibs_Ulinux___Uexternal_Smkl_Ulinux_Slib/libiomp5.so: invalid ELF header`

Pour solutionner ces erreurs, accédez au répertoire indiqué dans le message (soit `[...]/_U@mkl_Ulinux_S_S_Cmkl_Ulibs_Ulinux___Uexternal_Smkl_Ulinux_Slib`) et lancez la commande

```bash
ln -sf $(cat libiomp5.so) libiomp5.so
```

Le fichier texte sera remplacé par le bon lien symbolique.

<span id="Controlling_the_number_of_CPUs_and_threads"></span>
## Contrôle du nombre de CPU et de fils

Les paramètres de configuration `intra_op_parallelism_threads` et `inter_op_parallelism_threads` ont un effet sur le nombre de fils utilisés par TensorFlow; ces paramètres peuvent être définis comme suit&nbsp;:

 tf.config.threading.set_inter_op_parallelism_threads(num_threads)
 tf.config.threading.set_intra_op_parallelism_threads(num_threads)

## Problèmes connus
Un bogue s'est introduit dans l'implémentation Keras de Tensorflow après la version 2.8.3. Il affecte la performance des layers d'augmentation des données <i>tf.keras.layers.Random</i> (comme <i>tf.keras.layers.RandomRotation</i>, <i>tf.keras.layers.RandomTranslation</i>, etc.). Le processus d'entraînement est ralenti d'un facteur de plus de 100. <b>Ce bogue a été corrigé dans la version 2.12.