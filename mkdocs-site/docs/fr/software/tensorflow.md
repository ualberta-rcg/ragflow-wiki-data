---
title: "TensorFlow/fr"
slug: "tensorflow"
lang: "fr"

source_wiki_title: "TensorFlow/fr"
source_hash: "c32758f6b5ef273f97fef87e49eb947c"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:55:14.698870+00:00"

tags:
  - software
  - ai-and-machine-learning

keywords:
  - "tf.keras.Sequential"
  - "MultiWorkerMirroredStrategy"
  - "dépannage"
  - "sbatch"
  - "suivi de tâche"
  - "environnement virtuel Python"
  - "installation"
  - "bogue Keras"
  - "TensorBoard"
  - "Keras"
  - "Slurm"
  - "entraînement"
  - "SparseCategoricalCrossentropy"
  - "Dropout"
  - "arrière-plan"
  - "script Python"
  - "nœud de calcul"
  - "tf.keras.layers"
  - "points de contrôle"
  - "Nœuds multiples"
  - "Stratégie miroir"
  - "plusieurs GPU"
  - "bibliothèque"
  - "nombre de CPU et de fils"
  - "GPU distribués"
  - "GPU"
  - "Dense"
  - "nœud de connexion"
  - "apprentissage machine"
  - "CUDA"
  - "script bash"
  - "processus TensorFlow"
  - "Conv2D"
  - "Activation"
  - "tâche"
  - "MaxPooling2D"
  - "libcupti.so"
  - "libiomp5.so"
  - "nœud GPU"
  - "TensorFlow"
  - "Activation('relu')"

questions:
  - "Comment créer et activer un environnement virtuel Python pour installer TensorFlow sur les grappes de calcul ?"
  - "Quelle est la procédure à suivre pour configurer et utiliser TensorFlow avec le langage R ?"
  - "Comment soumettre une tâche TensorFlow nécessitant un GPU à l'aide d'un script Slurm ?"
  - "Comment peut-on vérifier les résultats et les messages générés une fois la tâche TensorFlow terminée avec Slurm ?"
  - "Quelles sont les différences d'implémentation et de format de sortie entre TensorFlow 1.x et TensorFlow 2.x illustrées dans les exemples ?"
  - "Quelle est la méthode recommandée pour exécuter l'outil de visualisation TensorBoard sans surcharger les nœuds de connexion ?"
  - "Comment soumettre une tâche TensorFlow utilisant un GPU via la ligne de commande ?"
  - "Quelle directive SBATCH permet de demander l'allocation d'un GPU dans le script ?"
  - "Comment définir le nombre maximal de cœurs CPU alloués par GPU dans le fichier de configuration ?"
  - "Pourquoi est-il déconseillé d'exécuter TensorBoard sur un nœud de connexion ?"
  - "Dans quel environnement est-il recommandé de faire tourner TensorBoard ?"
  - "Quelle est la méthode pour lancer TensorBoard en arrière-plan avant l'exécution du script Python ?"
  - "Comment configurer un tunnel SSH pour accéder à TensorBoard exécuté sur un nœud de calcul depuis un ordinateur local ?"
  - "Quelle stratégie TensorFlow est utilisée dans l'exemple de code pour distribuer l'entraînement d'un modèle sur plusieurs GPU au sein d'un nœud unique ?"
  - "Quelles sont les étapes de préparation de l'environnement virtuel et des variables d'environnement illustrées dans le script Bash de soumission de tâche ?"
  - "Quelle stratégie TensorFlow et quel résolveur de cluster sont utilisés pour configurer l'entraînement distribué sur plusieurs nœuds ?"
  - "Pourquoi doit-on ajouter explicitement `CommunicationImplementation.NCCL` à la stratégie de distribution dans un environnement multi-nœuds ?"
  - "Quel est le rôle des scripts bash fournis (`config_env.sh` et `launch_training.sh`) dans la préparation de l'environnement et l'exécution de la tâche sur la grappe de calcul Slurm ?"
  - "What is the overall architecture and sequence of layers defined in this TensorFlow Keras model?"
  - "How does the model utilize Dropout layers to prevent overfitting during training?"
  - "What does the final Dense layer of size 10 and the SparseCategoricalCrossentropy loss function indicate about the model's intended classification task?"
  - "What is the expected input shape and type of data for the first convolutional layer in this model?"
  - "What sequence of layers and activation functions are used to construct this Convolutional Neural Network?"
  - "What is the purpose of defining the Keras Sequential model within the `strategy.scope()` context manager?"
  - "Pourquoi est-il recommandé de créer des points de contrôle (checkpoints) pendant l'entraînement d'un modèle ?"
  - "Quelle méthode et quel paramètre doit-on utiliser pour sauvegarder automatiquement l'état du modèle à la fin de chaque époque avec Keras ?"
  - "Comment peut-on résoudre l'erreur de conflit liée à la bibliothèque `libiomp5.so` lors de l'utilisation conjointe de scikit-image et TensorFlow ?"
  - "Comment permettre à l'installation de TensorFlow d'utiliser la bibliothèque libiomp5.so ?"
  - "Quel est le rôle de la bibliothèque libcupti.so dans le fonctionnement de TensorFlow ?"
  - "Quel message d'erreur s'affiche si la bibliothèque libcupti.so n'est pas disponible sur le système ?"
  - "Comment résoudre l'erreur \"invalid ELF header\" liée au fichier libiomp5.so ?"
  - "Quels paramètres doivent être modifiés pour contrôler le nombre de CPU et de fils d'exécution dans TensorFlow ?"
  - "Quel problème de performance affecte les couches d'augmentation de données Keras entre les versions 2.8.3 et 2.12 de TensorFlow ?"
  - "Comment résoudre l'erreur \"invalid ELF header\" liée au fichier libiomp5.so ?"
  - "Quels paramètres doivent être modifiés pour contrôler le nombre de CPU et de fils d'exécution dans TensorFlow ?"
  - "Quel problème de performance affecte les couches d'augmentation de données Keras entre les versions 2.8.3 et 2.12 de TensorFlow ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[TensorFlow](https://www.tensorflow.org/) est une bibliothèque logicielle *open source* d'apprentissage machine.

Si vous voulez porter un programme TensorFlow sur une de nos grappes, nous vous recommandons de prendre connaissance du [tutoriel sur l'apprentissage machine](ai-ml/tutoriel_apprentissage_machine.md).

## Installation

Les directives suivantes servent à installer TensorFlow dans votre répertoire *home* à l'aide des [*wheels* Python](http://pythonwheels.com/) qui se trouvent dans `/cvmfs/soft.computecanada.ca/custom/python/wheelhouse/`.
Le wheel TensorFlow sera installé dans un [environnement virtuel Python](../python/#creer-et-utiliser-un-environnement-virtuel) avec la commande `pip`.

=== "TF 2.x"

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
(tensorflow) [name@server ~]$ pip install --no-index tensorflow
```

=== "TF 1.x"

Chargez les modules requis par TensorFlow. TF 1.x requiert StdEnv/2018.

!!! warning "Remarque"
    TF 1.x n'est pas disponible sur Narval, puisque cette grappe n'offre pas StdEnv/2018.

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

!!! warning "Attention"
    N'installez **pas** le paquet `tensorflow` sans le suffixe `_cpu` ou `_gpu` car il existe des problèmes de compatibilité avec d'autres bibliothèques.

#### CPU seulement
```bash
(tensorflow) [name@server ~]$ pip install --no-index tensorflow_cpu==1.15.0
```

#### GPU
```bash
(tensorflow) [name@server ~]$ pip install --no-index tensorflow_gpu==1.15.0
```

### Le paquet R

Pour utiliser TensorFlow en R, suivez les directives données ci-dessus pour créer un environnement virtuel et y installer TensorFlow. Suivez ensuite cette procédure :

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
(tensorflow) [name@server ~]$ R
```
En R, installez le paquet devtools, puis TensorFlow.
```r
install.packages('devtools', repos='https://cloud.r-project.org')
devtools::install_github('rstudio/tensorflow')
```

Vous pouvez maintenant procéder. N'appelez pas `install_tensorflow()` en R puisque TensorFlow est déjà installé dans votre environnement virtuel avec `pip`. Pour utiliser TensorFlow tel qu'installé dans votre environnement virtuel, entrez les commandes suivantes en R, après que l'environnement est activé.

```r
library(tensorflow)
use_virtualenv(Sys.getenv('VIRTUAL_ENV'))
```

## Soumettre une tâche TensorFlow avec un GPU

Soumettez une tâche TensorFlow ainsi
```bash
sbatch tensorflow-test.sh
```
Le script contient
```bash
::: tensorflow-test.sh
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

=== "TF 2.x"
```python
::: tensorflow-test.py
import tensorflow as tf
node1 = tf.constant(3.0)
node2 = tf.constant(4.0)
print(node1, node2)
print(node1 + node2)
```

=== "TF 1.x"
```python
::: tensorflow-test.py
import tensorflow as tf
node1 = tf.constant(3.0)
node2 = tf.constant(4.0)
print(node1, node2)
sess = tf.Session()
print(sess.run(node1 + node2))
```

Une fois la tâche terminée, ce qui devrait nécessiter moins d'une minute, un fichier de sortie avec un nom semblable à `node_id-job_id.out` devrait être généré. Le contenu de ce fichier serait similaire à ce qui suit; il s'agit d'exemples de messages TensorFlow et il est possible que vous en ayez d'autres.

=== "TF 2.x"
```text
::: node_id-job_id.out
2017-07-10 12:35:19.491097: I tensorflow/core/common_runtime/gpu/gpu_device.cc:961] DMA: 0
2017-07-10 12:35:19.491156: I tensorflow/core/common_runtime/gpu/gpu_device.cc:971] 0:   Y
2017-07-10 12:35:19.520737: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1030] Creating TensorFlow device (/gpu:0) -> (device: 0, name: Tesla P100-PCIE-12GB, pci bus id: 0000:82:00.0)
tf.Tensor(3.0, shape=(), dtype=float32) tf.Tensor(4.0, shape=(), dtype=float32)
tf.Tensor(7.0, shape=(), dtype=float32)
```

=== "TF 1.x"
```text
::: node_id-job_id.out
2017-07-10 12:35:19.491097: I tensorflow/core/common_runtime/gpu/gpu_device.cc:961] DMA: 0
2017-07-10 12:35:19.491156: I tensorflow/core/common_runtime/gpu/gpu_device.cc:971] 0:   Y
2017-07-10 12:35:19.520737: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1030] Creating TensorFlow device (/gpu:0) -> (device: 0, name: Tesla P100-PCIE-12GB, pci bus id: 0000:82:00.0)
Tensor("Const:0", shape=(), dtype=float32) Tensor("Const_1:0", shape=(), dtype=float32)
7.0
```

TensorFlow fonctionne sur tous les types de nœuds GPU. Pour plus d'information, voir [cette page](../using-gpus-with-slurm/).

## Suivi

Il est possible de se connecter à un nœud sur lequel une tâche est en cours pour y exécuter des processus. On peut ainsi faire le suivi des ressources utilisées par TensorFlow et visualiser le déroulement de l'entraînement. Pour des exemples, consultez [Surveillance d'une tâche en cours](../running-jobs/#surveillance-dune-tache-en-cours).

### TensorBoard

TensorFlow propose la suite d'outils de visualisation [TensorBoard](https://www.tensorflow.org/programmers_guide/summaries_and_tensorboard) qui lit les événements TensorFlow et modélise les fichiers. Pour savoir comment créer ces fichiers, consultez le [tutoriel TensorBoard sur les résumés](https://www.tensorflow.org/programmers_guide/summaries_and_tensorboard#serializing_the_data).

Sachez toutefois que TensorBoard exige trop de puissance de calcul pour être exécuté sur un nœud de connexion. Nous vous recommandons de l'exécuter dans la même tâche que le processus TensorFlow. Pour ce faire, lancez TensorBoard en arrière-plan en l'appelant avant le script Python, en y ajoutant le caractère (`&`).

```bash
# Your SBATCH arguments here

tensorboard --logdir=/tmp/your_log_dir --host 0.0.0.0 --load_fast false &
python train.py  # example
```

Pour accéder à TensorBoard avec un fureteur une fois que la tâche est en cours, il faut créer un lien entre votre ordinateur et le nœud sur lequel TensorFlow et TensorBoard sont exécutés. Pour ce faire, vous avez besoin du *hostname* du nœud de calcul sur lequel le serveur TensorFlow se trouve. Pour le trouver, faites afficher la liste de vos tâches avec la commande `sq` et repérez la tâche; le *hostname* est la valeur qui se trouve dans la colonne NODELIST.

Pour créer la connexion, lancez la commande sur votre ordinateur local.

```bash
[name@my_computer ~]$ ssh -N -f -L localhost:6006:computenode:6006 userid@cluster.computecanada.ca
```

Remplacez `computenode` par le *hostname* obtenu à l'étape précédente; `userid` par votre nom d'utilisateur de l'Alliance et; `cluster` par le *hostname* de la grappe, soit `rorqual`, `fir`, `nibi`, etc. Si le port 6006 était déjà utilisé, tensorboard va en utiliser un autre (p. ex. 6007, 6008...).

Une fois que la connexion est établie, allez à [http://localhost:6006](http://localhost:6006).

## Utiliser plusieurs GPU

TensorFlow offre des stratégies différentes pour utiliser plusieurs GPU avec l'API de haut niveau `tf.distribute`. Dans les sections qui suivent, nous montrons des exemples de code pour chacune des stratégies avec Keras. Pour plus d'information, consultez la [documentation officielle de TensorFlow](https://www.tensorflow.org/api_docs/python/tf/distribute).

### Stratégie miroir

#### Nœud unique

```bash
::: tensorflow-singleworker.sh
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
```python
::: tensorflow-singleworker.py
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

#### Nœuds multiples

La syntaxe pour utiliser des GPU distribués sur plusieurs nœuds ressemble beaucoup au cas du nœud simple; la différence principale est l'emploi de `MultiWorkerMirroredStrategy()`. Ici, nous utilisons `SlurmClusterResolver()` pour dire à TensorFlow d'obtenir par Slurm l'information sur la tâche plutôt que d'assigner manuellement un nœud principal et des nœuds secondaires (*workers*), par exemple. Nous devons aussi ajouter `CommunicationImplementation.NCCL` à la stratégie de distribution pour indiquer que nous voulons utiliser la bibliothèque NCCL de NVIDIA pour les communications entre les GPU. Ceci n'était pas nécessairement le cas pour un nœud simple puisque NCCL se trouve par défaut avec `MirroredStrategy()`.

```bash
::: tensorflow-multiworker.sh
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
```bash
::: config_env.sh
#!/bin/bash

module load python

virtualenv --no-download $SLURM_TMPDIR/ENV

source $SLURM_TMPDIR/ENV/bin/activate

pip install --upgrade pip --no-index

pip install --no-index tensorflow

echo "Done installing virtualenv!"
```

Le script `launch_training.sh` a la forme

```bash
::: launch_training.sh
#!/bin/bash

source $SLURM_TMPDIR/ENV/bin/activate

python tensorflow-multiworker.py
```

Le script Python `tensorflow-multiworker.py` a la forme suivante :
```python
::: tensorflow-multiworker.py
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

Peu importe le temps que dure l'exécution de votre code, une bonne habitude à prendre est de créer des points de contrôle pendant l'entraînement. Un point de contrôle vous donne le portrait de votre modèle à un moment précis du processus d'entraînement (après un certain nombre d'itérations ou d'époques); le portrait est enregistré sur disque et vous pourrez le récupérer par la suite. Ceci est pratique pour diviser en petites tâches une tâche qui doit avoir un long temps d'exécution, ce qui pourrait faire qu'elles soient allouées plus rapidement à une grappe. C'est aussi un bon moyen d'éviter de perdre votre travail en cas d'erreurs inattendues ou de panne du matériel.

### Avec Keras

Pour créer un point de contrôle dans un entraînement avec `keras`, nous recommandons le paramètre `callbacks` de la méthode `model.fit()`. Dans l'exemple suivant, nous demandons à TensorFlow de créer un point de contrôle à la fin de chacune des époques d'entraînement.

```python
callbacks = [tf.keras.callbacks.ModelCheckpoint(filepath="./ckpt",save_freq="epoch")] # Make sure the path where you want to create the checkpoint exists

model.fit(dataset, epochs=10 , callbacks=callbacks)
```

Pour plus d'information, consultez la [documentation officielle de TensorFlow](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint).

### Avec une boucle d'entraînement personnalisée

Voyez la [documentation officielle de TensorFlow](https://www.tensorflow.org/guide/checkpoint#writing_checkpoints).

## Dépannage

### scikit-image

Si vous utilisez la bibliothèque scikit-image, vous pourriez recevoir l'erreur
`OMP: Error #15: Initializing libiomp5.so, but found libiomp5.so already initialized.`

Ceci se produit quand la bibliothèque TensorFlow essaie de charger une version de OMP incompatible avec la version du système. Pour contourner ceci :
```bash
(tf_skimage_venv) name@server $ cd tf_skimage_venv
(tf_skimage_venv) name@server $ export LIBIOMP_PATH=$(strace python -c 'from skimage.transform import AffineTransform' 2>&1 | grep -v ENOENT | grep -ohP -e '(?<=")[^"]+libiomp5.so(?=")' | xargs realpath)
(tf_skimage_venv) name@server $ find -path '*_solib_local*' -name libiomp5.so -exec ln -sf $LIBIOMP_PATH {} \;
```
L'installation de la bibliothèque TensorFlow pourra alors utiliser libiomp5.so.

### libcupti.so

Certaines fonctions de suivi de TensorFlow utilisent la bibliothèque libcupti.so; si cette dernière n'est pas disponible, l'erreur suivante pourrait survenir :

```text
I tensorflow/stream_executor/dso_loader.cc:142] Couldn't open CUDA library libcupti.so.9.0. LD_LIBRARY_PATH: /usr/local/cuda-9.0/lib64
```

La solution est d'exécuter les commandes suivantes avant l'exécution du script.
```bash
module load cuda/9.0.xxx
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CUDA_HOME/extras/CUPTI/lib64/
```
Remplacez xxx par la version appropriée de CUDA que vous pouvez trouver avec `module av cuda`.

### libiomp5.so invalid ELF header

Le fichier objet partagé `libiomp5.so` est quelquefois par erreur installé en tant que fichier texte, ce qui peut produire des erreurs comme ceci :

```text
/home/username/venv/lib/python3.6/site-packages/tensorflow/python/../../_solib_local/_U@mkl_Ulinux_S_S_Cmkl_Ulibs_Ulinux___Uexternal_Smkl_Ulinux_Slib/libiomp5.so: invalid ELF header
```

Pour solutionner ces erreurs, accédez au répertoire indiqué dans le message (soit `[...]/_U@mkl_Ulinux_S_S_Cmkl_Ulibs_Ulinux___Uexternal_Smkl_Ulinux_Slib`) et lancez la commande

```bash
[name@server ...Ulinux_Slib] $ ln -sf $(cat libiomp5.so) libiomp5.so
```

Le fichier texte sera remplacé par le bon lien symbolique.

## Contrôle du nombre de CPU et de fils

Les paramètres de configuration `intra_op_parallelism_threads` et `inter_op_parallelism_threads` ont un effet sur le nombre de fils utilisés par TensorFlow; ces paramètres peuvent être définis comme suit :

```python
tf.config.threading.set_inter_op_parallelism_threads(num_threads)
tf.config.threading.set_intra_op_parallelism_threads(num_threads)
```

## Problèmes connus

Un bogue s'est introduit dans l'implémentation Keras de Tensorflow après la version 2.8.3. Il affecte la performance des layers d'augmentation des données *tf.keras.layers.Random* (comme *tf.keras.layers.RandomRotation*, *tf.keras.layers.RandomTranslation*, etc.). Le processus d'entraînement est ralenti d'un facteur de plus de 100. **Ce bogue a été corrigé dans la version 2.12.**