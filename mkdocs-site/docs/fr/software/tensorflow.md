---
title: "TensorFlow/fr"
slug: "tensorflow"
lang: "fr"

source_wiki_title: "TensorFlow/fr"
source_hash: "c32758f6b5ef273f97fef87e49eb947c"
last_synced: "2026-04-12T19:39:22.899801+00:00"
last_processed: "2026-04-12T19:58:30.159913+00:00"

tags:
  - software
  - ai-and-machine-learning

keywords:
  - "arrière-plan"
  - "script bash"
  - "plusieurs GPU"
  - "tf.keras.Sequential"
  - "puissance de calcul"
  - "libcupti.so"
  - "tâche"
  - "Dropout"
  - "Slurm"
  - "bibliothèque"
  - "strategy.scope"
  - "CPU et fils"
  - "TensorBoard"
  - "nœuds GPU"
  - "suivi de tâche"
  - "CUDA"
  - "script Python"
  - "processus TensorFlow"
  - "GPU distribués"
  - "Activation('relu')"
  - "points de contrôle"
  - "dépannage"
  - "Conv2D"
  - "connexion SSH"
  - "Nœuds multiples"
  - "nœud de connexion"
  - "Dense"
  - "TensorFlow"
  - "Keras"
  - "environnement virtuel"
  - "GPU"
  - "MaxPooling2D"
  - "sbatch"
  - "libiomp5.so"
  - "tf.keras.layers"
  - "Python"
  - "MultiWorkerMirroredStrategy"
  - "SparseCategoricalCrossentropy"
  - "entraînement"
  - "Stratégie miroir"
  - "apprentissage machine"

questions:
  - "Quelles sont les étapes pour installer les versions 1.x ou 2.x de TensorFlow dans un environnement virtuel Python ?"
  - "Comment configurer et utiliser la bibliothèque TensorFlow avec le langage R une fois l'environnement virtuel créé ?"
  - "Quelle est la procédure pour soumettre une tâche TensorFlow nécessitant l'utilisation d'un GPU à l'aide d'un script sbatch ?"
  - "Quelles sont les différences dans le code Python et les résultats de sortie entre les versions 1.x et 2.x de TensorFlow présentées dans le texte ?"
  - "Comment les fichiers de sortie générés par Slurm sont-ils nommés et quelles informations contiennent-ils généralement après l'exécution d'une tâche TensorFlow ?"
  - "Quelle est la méthode recommandée pour exécuter l'outil de visualisation TensorBoard sans surcharger les nœuds de connexion ?"
  - "Quelle commande permet de soumettre le script de la tâche TensorFlow ?"
  - "Comment le script configure-t-il la requête pour allouer un GPU ?"
  - "Combien de cœurs CPU sont demandés par tâche dans le script d'exemple ?"
  - "Pourquoi est-il déconseillé d'exécuter TensorBoard sur un nœud de connexion ?"
  - "Dans quel environnement est-il recommandé de faire tourner TensorBoard ?"
  - "Comment doit-on procéder pour lancer TensorBoard en arrière-plan avant l'exécution du script Python ?"
  - "Comment configurer une connexion SSH pour accéder à l'interface TensorBoard exécutée sur un nœud de calcul depuis un ordinateur local ?"
  - "Quelle API de haut niveau TensorFlow propose-t-il pour répartir l'entraînement d'un modèle sur plusieurs GPU ?"
  - "Comment structurer les scripts SLURM et Python pour exécuter un modèle avec la stratégie miroir (MirroredStrategy) sur un nœud unique ?"
  - "Quelle est la principale différence de syntaxe dans TensorFlow pour utiliser des GPU distribués sur plusieurs nœuds par rapport à un seul nœud ?"
  - "Pourquoi est-il nécessaire d'ajouter explicitement l'implémentation NCCL à la stratégie de distribution dans un environnement à nœuds multiples ?"
  - "Comment les scripts Bash fournis configurent-ils les ressources Slurm et l'environnement virtuel pour lancer l'entraînement distribué ?"
  - "What is the overall architecture and sequence of layers defined in this Keras model snippet?"
  - "How are the Dropout layers utilized within this neural network to prevent overfitting?"
  - "What does the use of SparseCategoricalCrossentropy with `from_logits=True` indicate about the model's final output layer and classification task?"
  - "What is the expected input shape for the first convolutional layer of the model?"
  - "How does the model utilize pooling and dropout layers to process the data after the initial convolutional layers?"
  - "What is the significance of building the Keras Sequential model within the `strategy.scope()` block?"
  - "Pourquoi est-il recommandé de créer des points de contrôle pendant l'entraînement d'un modèle d'apprentissage automatique ?"
  - "Comment peut-on configurer Keras pour sauvegarder automatiquement un point de contrôle à la fin de chaque époque ?"
  - "Comment résoudre l'erreur de conflit liée à la bibliothèque libiomp5.so lors de l'utilisation conjointe de TensorFlow et scikit-image ?"
  - "Comment l'installation de TensorFlow parvient-elle à utiliser la bibliothèque libiomp5.so selon le texte ?"
  - "Quel est le rôle spécifique de la bibliothèque libcupti.so au sein des fonctionnalités de TensorFlow ?"
  - "Quel message d'erreur s'affiche lorsque la bibliothèque libcupti.so n'est pas disponible sur le système ?"
  - "Comment résoudre l'erreur \"invalid ELF header\" liée au fichier libiomp5.so ?"
  - "Comment configurer le nombre de CPU et de fils d'exécution utilisés par TensorFlow ?"
  - "Quel bogue de performance affecte les couches d'augmentation de données Keras et dans quelle version a-t-il été corrigé ?"

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

Les directives suivantes servent à installer TensorFlow dans votre répertoire *home* à l'aide des ([*wheels* Python](http://pythonwheels.com/)) qui se trouvent dans `/cvmfs/soft.computecanada.ca/custom/python/wheelhouse/`.
Le wheel TensorFlow sera installé dans un [environnement virtuel Python](python.md) avec la commande `pip`.

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

    !!! warning
        **N'installez pas** le paquet `tensorflow` sans le suffixe `_cpu` ou `_gpu` car il existe des problèmes de compatibilité avec d'autres bibliothèques.

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
(tensorflow)_[name@server ~]$ R
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
Soumettez une tâche TensorFlow ainsi :
```bash
sbatch tensorflow-test.sh
```
Le script contient :
```bash linenums="1"
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
Le script Python se lit :

=== "TF 2.x"
    ```python linenums="1"
    import tensorflow as tf
    node1 = tf.constant(3.0)
    node2 = tf.constant(4.0)
    print(node1, node2)
    print(node1 + node2)
    ```
=== "TF 1.x"
    ```python linenums="1"
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
    2017-07-10 12:35:19.491097: I tensorflow/core/common_runtime/gpu/gpu_device.cc:961] DMA: 0
    2017-07-10 12:35:19.491156: I tensorflow/core/common_runtime/gpu/gpu_device.cc:971] 0:   Y
    2017-07-10 12:35:19.520737: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1030] Creating TensorFlow device (/gpu:0) -> (device: 0, name: Tesla P100-PCIE-12GB, pci bus id: 0000:82:00.0)
    tf.Tensor(3.0, shape=(), dtype=float32) tf.Tensor(4.0, shape=(), dtype=float32)
    tf.Tensor(7.0, shape=(), dtype=float32)
    ```
=== "TF 1.x"
    ```text
    2017-07-10 12:35:19.491097: I tensorflow/core/common_runtime/gpu/gpu_device.cc:961] DMA: 0
    2017-07-10 12:35:19.491156: I tensorflow/core/common_runtime/gpu/gpu_device.cc:971] 0:   Y
    2017-07-10 12:35:19.520737: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1030] Creating TensorFlow device (/gpu:0) -> (device: 0, name: Tesla P100-PCIE-12GB, pci bus id: 0000:82:00.0)
    Tensor("Const:0", shape=(), dtype=float32) Tensor("Const_1:0", shape=(), dtype=float32)
    7.0
    ```

TensorFlow fonctionne sur tous les types de nœuds GPU. Pour plus d'information, voir [cette page](../running-jobs/using_gpus_with_slurm.md).

## Suivi

Il est possible de se connecter à un nœud sur lequel une tâche est en cours pour y exécuter des processus. On peut ainsi faire le suivi des ressources utilisées par TensorFlow et visualiser le déroulement de l'entraînement. Pour des exemples, consultez [Surveillance d'une tâche en cours](../running-jobs/running_jobs.md).

### TensorBoard

TensorFlow propose la suite d'outils de visualisation [TensorBoard](https://www.tensorflow.org/programmers_guide/summaries_and_tensorboard) qui lit les événements TensorFlow et modélise les fichiers. Pour savoir comment créer ces fichiers, consultez le [tutoriel TensorBoard sur les résumés](https://www.tensorflow.org/programmers_guide/summaries_and_tensorboard#serializing_the_data).

Sachez toutefois que TensorBoard exige trop de puissance de calcul pour être exécuté sur un nœud de connexion. Nous vous recommandons de l'exécuter dans la même tâche que le processus TensorFlow. Pour ce faire, lancez TensorBoard en arrière-plan en l'appelant avant le script Python, en y ajoutant le caractère (`&`).

```bash
 # Your SBATCH arguments here

 tensorboard --logdir=/tmp/your_log_dir --host 0.0.0.0 --load_fast false &
 python train.py  # example
```

Pour accéder à TensorBoard avec un navigateur web une fois que la tâche est en cours, il faut créer un lien entre votre ordinateur et le nœud sur lequel TensorFlow et TensorBoard sont exécutés. Pour ce faire, vous avez besoin du *hostname* du nœud de calcul sur lequel le serveur TensorFlow se trouve. Pour le trouver, faites afficher la liste de vos tâches avec la commande `sq` et repérez la tâche; le *hostname* est la valeur qui se trouve dans la colonne NODELIST.

Pour créer la connexion, lancez la commande sur votre ordinateur local.

```bash
[name@my_computer ~]$ ssh -N -f -L localhost:6006:computenode:6006 userid@cluster.computecanada.ca
```

Remplacez `computenode` par le *hostname* obtenu à l'étape précédente; `userid` par votre nom d'utilisateur de l'Alliance et; `cluster` par le *hostname* de la grappe, soit `rorqual`, `fir`, `nibi`, etc. Si le port 6006 était déjà utilisé, TensorBoard va en utiliser un autre (p. ex. 6007, 6008...).

Une fois que la connexion est établie, allez à [http://localhost:6006](http://localhost:6006).

## Utiliser plusieurs GPU

TensorFlow offre des stratégies différentes pour utiliser plusieurs GPU avec l'API de haut niveau `tf.distribute`. Dans les sections qui suivent, nous montrons des exemples de code pour chacune des stratégies avec Keras. Pour plus d'information, consultez la [documentation officielle de TensorFlow](https://www.tensorflow.org/api_docs/python/tf/distribute).

### Stratégie miroir

#### Nœud unique

```bash linenums="1"
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

Le script Python `tensorflow-singleworker.py` a le format :
```python linenums="1"
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

La syntaxe pour utiliser des GPU distribués sur plusieurs nœuds ressemble beaucoup au cas du nœud unique; la différence principale est l'emploi de `MultiWorkerMirroredStrategy()`. Ici, nous utilisons `SlurmClusterResolver()` pour dire à TensorFlow d'obtenir par Slurm l'information sur la tâche plutôt que d'assigner manuellement un nœud principal et des nœuds secondaires (*workers*), par exemple. Nous devons aussi ajouter `CommunicationImplementation.NCCL` à la stratégie de distribution pour indiquer que nous voulons utiliser la bibliothèque NCCL de NVIDIA pour les communications entre les GPU. Ceci n'était pas nécessairement le cas pour un nœud unique puisque NCCL se trouve par défaut avec `MirroredStrategy()`.

```bash linenums="1"
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

où `config_env.sh` a la forme :
```bash linenums="1"
#!/bin/bash

module load python

virtualenv --no-download $SLURM_TMPDIR/ENV

source $SLURM_TMPDIR/ENV/bin/activate

pip install --upgrade pip --no-index

pip install --no-index tensorflow

echo "Done installing virtualenv!"
```

Le script `launch_training.sh` a la forme :

```bash linenums="1"
#!/bin/bash

source $SLURM_TMPDIR/ENV/bin/activate

python tensorflow-multiworker.py
```

Le script Python `tensorflow-multiworker.py` a la forme suivante :
```python linenums="1"
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

Si vous utilisez la bibliothèque scikit-image, vous pourriez recevoir l'erreur :
```text
OMP: Error #15: Initializing libiomp5.so, but found libiomp5.so already initialized.
```

Ceci se produit quand la bibliothèque TensorFlow essaie de charger une version de OMP incompatible avec la version du système. Pour contourner ceci :
```bash
(tf_skimage_venv) name@server $ cd tf_skimage_venv
(tf_skimage_venv) name@server $ export LIBIOMP_PATH=$(strace python -c 'from skimage.transform import AffineTransform' 2>&1 | grep -v ENOENT | grep -ohP -e '(?<=")[^"]+libiomp5.so(?=")' | xargs realpath)
(tf_skimage_venv) name@server $ find -path '*_solib_local*' -name libiomp5.so -exec ln -sf $LIBIOMP_PATH {} \;
```
L'installation de la bibliothèque TensorFlow pourra alors utiliser `libiomp5.so`.

### libcupti.so

Certaines fonctions de suivi de TensorFlow utilisent la bibliothèque `libcupti.so`; si cette dernière n'est pas disponible, l'erreur suivante pourrait survenir :

```text
I tensorflow/stream_executor/dso_loader.cc:142] Couldn't open CUDA library libcupti.so.9.0. LD_LIBRARY_PATH: /usr/local/cuda-9.0/lib64
```

La solution est d'exécuter les commandes suivantes avant l'exécution du script.
```bash
module load cuda/9.0.xxx
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CUDA_HOME/extras/CUPTI/lib64/
```
Remplacez `xxx` par la version appropriée de CUDA que vous pouvez trouver avec `module av cuda`.

### libiomp5.so invalid ELF header

Le fichier objet partagé `libiomp5.so` est quelquefois par erreur installé en tant que fichier texte, ce qui peut produire des erreurs comme ceci :

```text
/home/username/venv/lib/python3.6/site-packages/tensorflow/python/../../_solib_local/_U@mkl_Ulinux_S_S_Cmkl_Ulibs_Ulinux___Uexternal_Smkl_Ulinux_Slib/libiomp5.so: invalid ELF header
```

Pour solutionner ces erreurs, accédez au répertoire indiqué dans le message (soit `[...]/_U@mkl_Ulinux_S_S_Cmkl_Ulibs_Ulinux___Uexternal_Smkl_Ulinux_Slib`) et lancez la commande :

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
Un bogue s'est introduit dans l'implémentation Keras de TensorFlow après la version 2.8.3. Il affecte la performance des *layers* d'augmentation des données `tf.keras.layers.Random` (comme `tf.keras.layers.RandomRotation`, `tf.keras.layers.RandomTranslation`, etc.). Le processus d'entraînement est ralenti d'un facteur de plus de 100. **Ce bogue a été corrigé dans la version 2.12.**