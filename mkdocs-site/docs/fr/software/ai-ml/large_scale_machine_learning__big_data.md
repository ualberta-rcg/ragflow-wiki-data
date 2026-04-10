---
title: "Large Scale Machine Learning (Big Data)/fr"
slug: "large_scale_machine_learning__big_data"
lang: "fr"

source_wiki_title: "Large Scale Machine Learning (Big Data)/fr"
source_hash: "2e1c849730019287f1a1cee83995b413"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T07:54:21.665034+00:00"

tags:
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

Dans le domaine de l’apprentissage profond, la scalabilité en termes de quantité de données est rendue possible par l'utilisation de stratégies de traitement en très petits lots et de solveurs itératifs du premier ordre. En apprentissage de réseaux de neurones profonds, le code s’effectue plus ou moins de la même manière qu’il s’agisse de quelques milliers ou de centaines de millions d’exemples : quelques exemples sont chargés à partir d’une source (disque, mémoire, source à distance, etc.), les gradients sont calculés pendant les itérations, ce qui modifie les paramètres du modèle au fur et à mesure. Par contre, avec plusieurs modules d’apprentissage machine traditionnel, notamment scikit-learn, écrire du code pour faire de l'entraînement à grande échelle n’est souvent pas évident. Pour plusieurs algorithmes qui conviennent à des modèles communs comme les modèles linéaires généralisés (GLM pour *Generalized Linear Models*) et les machines à vecteurs de support (SVM pour *Support Vector Machines*), leur implémentation par défaut exige que la totalité de l’ensemble d’apprentissage soit chargée en mémoire et n’offre aucune fonctionnalité de parallélisme par fils ou par processus. De plus, certaines de ces implémentations se basent sur des solveurs plutôt gourmands en mémoire qui, pour bien fonctionner, exigent une quantité de mémoire plusieurs fois supérieure à la taille de l’ensemble de données à entraîner.

Nous abordons ici des options permettant d’adapter les méthodes d’apprentissage machine traditionnel à de très grands ensembles de données dans les cas où un nœud de type Large Memory est insuffisant ou que le traitement séquentiel est excessivement long.

## Scikit-learn

[Scikit-learn](https://scikit-learn.org/stable/index.html) est un module Python pour l’apprentissage machine basé sur SciPy et distribué sous licence BSD-3-Clause. Le paquet est doté d’une API intuitive qui simplifie la construction de pipelines complexes d’apprentissage machine. Toutefois, plusieurs implémentations des méthodes GLM et SVM supposent que l’ensemble d’entraînement est complètement chargé en mémoire, ce qui n'est pas toujours souhaitable. De plus, certains de ces algorithmes utilisent par défaut des solveurs très exigeants en mémoire. Dans certains cas, les suggestions qui suivent vous permettront de contourner ces limitations.

### Solveurs du gradient stochastique

Si votre ensemble de données est assez petit pour être chargé au complet en mémoire, mais que pendant l’entraînement vous obtenez des erreurs de mémoire insuffisante (OOM pour *Out-Of-Memory*), le problème est probablement dû à un solveur trop gourmand en mémoire. Avec scikit-learn, plusieurs méthodes offrent en option des variations de l’[algorithme du gradient stochastique](https://fr.wikipedia.org/wiki/Algorithme_du_gradient_stochastique) et le remplacement du solveur par défaut par un solveur du gradient stochastique est souvent une solution facile.

Dans les exemples suivants, une [régression de crête (*ridge regression*)](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html) utilise le solveur par défaut et un solveur du gradient stochastique. Pour observer l’utilisation de la mémoire, lancez la commande `htop` dans le terminal lorsque le programme Python s’exécute.

```python linenums="1" title="ridge-default.py"
from sklearn.datasets import make_regression
from sklearn.linear_model import Ridge

X,y = make_regression(n_samples=100000, n_features=10000, n_informative=50)

model = Ridge()

model.fit(X,y)
```

```python linenums="1" title="ridge-saga.py"
from sklearn.datasets import make_regression
from sklearn.linear_model import Ridge

X,y = make_regression(n_samples=100000, n_features=10000, n_informative=50)

model = Ridge(solver='saga')

model.fit(X,y)
```

Une autre option qui réduit encore plus l'utilisation de la mémoire est de travailler avec [SGDRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html) plutôt qu’avec Ridge. Cette classe implémente plusieurs types de modèles linéaires généralisés (GLM) pour les régressions avec comme solveur l’algorithme du gradient stochastique (SGD). Il faut cependant noter que SGDRegressor ne fonctionne que si le résultat est unidimensionnel (scalaire).

```python linenums="1" title="ridge-sgd_regressor.py"
from sklearn.datasets import make_regression
from sklearn.linear_model import SGDRegressor

X,y = make_regression(n_samples=100000, n_features=10000, n_informative=50)

model = SGDRegressor(penalty='l2') # set penalty='l2' to perform a ridge regression

model.fit(X,y)
```

### Apprentissage en lots

Dans les cas où votre ensemble de données est trop grand pour la mémoire disponible, ou juste assez grand pour ne pas laisser assez de mémoire pour l'entraînement, il est possible de garder les données sur disque et de les charger en lots, comme c’est le cas avec les modules d’apprentissage profond. Scikit-learn nomme cette technique [*out-of-core learning*](https://scikit-learn.org/stable/computing/scaling_strategies.html) (apprentissage hors mémoire) et c’est une option viable quand l’estimateur offre la [méthode `partial_fit`](https://scikit-learn.org/stable/computing/scaling_strategies.html?highlight=partial_fit#incremental-learning). Dans les exemples ci-dessous, l’apprentissage hors mémoire se fait par des itérations sur des ensembles de données enregistrés sur disque.

Dans le premier exemple, nous utilisons [SGDClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html) pour ajuster un classifieur linéaire SVM avec des lots de données en provenance d’une paire de vecteurs **numpy**. Les vecteurs sont stockés sur disque dans des [fichiers npy](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.html#npy-format) qui seront [mappés en mémoire](https://numpy.org/doc/stable/reference/generated/numpy.memmap.html). Puisque SGDClassifier possède la méthode `partial_fit`, les itérations peuvent se faire dans les grands fichiers en mémoire en ne chargeant que des petits lots à la fois en provenance des vecteurs. Chaque appel à `partial_fit` exécutera alors une époque de l’algorithme du gradient stochastique sur un lot de données.

```python linenums="1" title="svm-sgd-npy.py"
import numpy as np
from sklearn.linear_model import SGDClassifier

def batch_loader(X, y, batch_size):
    return ((X[idx:idx + batch_size],y[idx:idx + batch_size]) for idx in range(0, len(X), batch_size)) # function returns a Generator

inputs = np.memmap('./x_array.npy',dtype='float64',shape=(100000,10000))
targets = np.memmap('./y_array.npy',dtype='int8',shape=(100000,))

model = SGDClassifier(loss='hinge') # Using loss='hinge' is equivalent to fitting a Linear SVM

for batch in batch_loader(inputs, targets, batch_size=512):
    X,y = batch
    model.partial_fit(X,y)
```

Une autre méthode de stockage des données est d’utiliser des fichiers CSV. Dans le prochain exemple, l'entraînement d’un modèle de régression lasso se fait par la lecture en lots de données à partir d’un fichier CSV avec le paquet [pandas](https://pandas.pydata.org).

```python linenums="1" title="lasso-sgd-csv.py"
import pandas as pd
from sklearn.linear_model import SGDRegressor

model = SGDRegressor(penalty='l1')

for batch in pd.read_csv("./data.csv", chunksize=512, iterator=True):
    X = batch.drop('target', axis=1)
    y = batch['target']
    model.partial_fit(X,y)
```

## Snap ML

[Snap ML](https://snapml.readthedocs.io/en/latest/) est une bibliothèque d’apprentissage machine propriétaire développée par IBM qui prend en charge plusieurs modèles classiques et s’adapte facilement à des ensembles de données contenant des milliards d’exemples et/ou de variables. Elle permet l’entraînement distribué, l’accélération GPU et l’utilisation de structures creuses. Une de ses API est très semblable à celle de scikit-learn et peut la remplacer dans le cas d’ensembles de données massifs.

### Installation

#### Wheels ajoutés récemment
Pour connaître la plus récente version de Snap ML que nous avons construite, lancez
```bash
avail_wheels "snapml"
```
Pour plus d'information, voir [Wheels disponibles](python.md#wheels-disponibles).

#### Installer le wheel

L'option à privilégier est d'utiliser le [wheel Python](https://pythonwheels.com/) comme suit :
1.  [Chargez un module](utiliser-des-modules.md#sous-commande-load) Python avec `module load python`.
2.  Créez et lancez un [environnement virtuel Python](python.md#creer-et-utiliser-un-environnement-virtuel).
3.  Installez Snap ML dans l'environnement virtuel avec `pip install`.

```bash
(venv) [name@server ~]$ pip install --no-index snapml
```

### Multifil

Tous les estimateurs de Snap ML prennent en charge le parallélisme par fils qui est contrôlé avec le paramètre `n_jobs`. En définissant ce paramètre comme étant égal au nombre de cœurs disponibles pour votre tâche, on peut typiquement observer une accélération comparativement à l’implémentation du même estimateur avec scikit-learn. Voici comment se compare la performance de Ridge entre scikit-learn et Snap ML.

```python linenums="1" title="ridge-snap-vs-sklearn.py"
from sklearn.datasets import make_regression
from sklearn.linear_model import Ridge
from snapml import LinearRegression
import time

X,y = make_regression(n_samples=100000, n_features=10000, n_informative=50)

model_sk = Ridge(solver='saga')

print("Running Ridge with sklearn...")
tik = time.perf_counter()
model_sk.fit(X,y)
tok = time.perf_counter()

print(f"sklearn took {tok-tik:0.2f} seconds to fit.")

model_snap = LinearRegression(penalty='l2',n_jobs=4)

print("Running Ridge with SnapML...")
tik = time.perf_counter()
model_snap.fit(X,y)
tok = time.perf_counter()

print(f"SnapML took {tok-tik:0.2f} seconds to fit.")
```

### Entraînement sur GPU

Tous les estimateurs de Snap ML prennent en charge l'accélération d’un ou plusieurs GPU. Pour l’entraînement avec un GPU, le paramètre est `use_gpu=True`. Pour l’entraînement avec plusieurs GPU, le paramètre est aussi `use_gpu`, et la liste des ID des GPU disponibles est passée à `device_ids`. Par exemple, pour une tâche qui demande deux GPU, `device_ids=[0,1]` utilisera les deux GPU. Le prochain exemple fait la même comparaison que dans la section précédente, mais pour l’entraînement d’un classifieur SVM avec un noyau non linéaire.

```python linenums="1" title="ridge-snap-vs-sklearn2.py"
from sklearn.datasets import make_classification
from sklearn.svm import SVC
from snapml import SupportVectorMachine
import time

X,y = make_classification(n_samples=100000, n_features=10000, n_classes=3, n_informative=50)

model_sk = SVC(kernel='rbf') #sklearn's SVM fit-time scales at least quadratically with the number of samples... this will take a loooong time.

print("Running SVM Classifier with sklearn...")
tik = time.perf_counter()
model_sk.fit(X,y)
tok = time.perf_counter()

print(f"sklearn took {tok-tik:0.2f} seconds to fit.")

model_snap = SupportVectorMachine(kernel='rbf',n_jobs=4)

print("Running SVM Classifier with SnapML without GPU...")
tik = time.perf_counter()
model_snap.fit(X,y)
tok = time.perf_counter()

print(f"SnapML took {tok-tik:0.2f} seconds to fit without GPU.")

model_snap_gpu = SupportVectorMachine(kernel='rbf',n_jobs=4, use_gpu=True)

print("Running SVM Classifier with SnapML with GPU...")
tik = time.perf_counter()
model_snap_gpu.fit(X,y)
tok = time.perf_counter()

print(f"SnapML took {tok-tik:0.2f} seconds to fit with GPU.")
```

### Entraînement hors mémoire

Tous les estimateurs de Snap ML utilisent par défaut des solveurs itératifs du premier ordre comme SGD. Il est donc possible de faire des entraînements en lots sans avoir à charger en mémoire les ensembles de données au complet. Par contre, Snap ML accepte les entrées de vecteurs numpy par le mappage en mémoire, contrairement à scikit-learn.

```python linenums="1" title="snap-npy.py"
import numpy as np
from snapml import LogisticRegression

X = np.memmap('./x_array.npy',dtype='float64',shape=(100000,10000))
y = np.memmap('./y_array.npy',dtype='int8',shape=(100000,))

model = LogisticRegression(n_jobs=4)

model.fit(X,y)
```

### MPI

Snap ML offre des implémentations distribuées de plusieurs estimateurs. Pour utiliser le mode distribué, appelez un script Python avec `mpirun` ou `srun`.

## Spark ML

[Spark ML](https://spark.apache.org/docs/latest/ml-guide.html) est une bibliothèque basée sur [Apache Spark](apache-spark.md) qui permet la scalabilité de plusieurs méthodes d’apprentissage machine à d’énormes quantités de données et sur plusieurs nœuds, sans avoir à distribuer des ensembles de données ou à créer du code distribué ou parallèle. Elle inclut plusieurs outils utiles en algèbre linéaire et en statistique. Avant de reproduire les exemples de la [documentation Spark ML](https://spark.apache.org/docs/latest/ml-guide.html), voyez notre [tutoriel sur comment soumettre une tâche Spark](apache-spark.md#utilisation).