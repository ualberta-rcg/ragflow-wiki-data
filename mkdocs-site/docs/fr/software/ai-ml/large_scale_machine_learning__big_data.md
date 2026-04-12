---
title: "Large Scale Machine Learning (Big Data)/fr"
slug: "large_scale_machine_learning__big_data"
lang: "fr"

source_wiki_title: "Large Scale Machine Learning (Big Data)/fr"
source_hash: "2e1c849730019287f1a1cee83995b413"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:30:34.302971+00:00"

tags:
  - ai-and-machine-learning

keywords:
  - "solveurs du gradient stochastique"
  - "accélération de GPU"
  - "SGDRegressor"
  - "scikit-learn"
  - "Apprentissage hors mémoire"
  - "Multifil"
  - "Scikit-learn"
  - "entraînement distribué"
  - "implémentations distribuées"
  - "Entraînement sur GPU"
  - "Spark ML"
  - "Snap ML"
  - "Solveurs itératifs"
  - "Wheels"
  - "apprentissage machine"
  - "Vecteurs numpy"
  - "Mappage en mémoire"
  - "modèles linéaires généralisés"
  - "Apprentissage en lots"
  - "résultat unidimensionnel"
  - "ensembles de données"
  - "utilisation de la mémoire"
  - "algorithme du gradient stochastique"
  - "partial_fit"
  - "Apache Spark"
  - "Entraînement hors mémoire"

questions:
  - "Pourquoi la mise à l'échelle de l'apprentissage machine traditionnel est-elle souvent plus complexe que celle de l'apprentissage profond ?"
  - "Quelles sont les principales limitations de scikit-learn concernant la gestion de la mémoire pour les modèles comme les GLM et les SVM ?"
  - "Comment l'utilisation des solveurs du gradient stochastique permet-elle de résoudre les problèmes de mémoire insuffisante lors de l'entraînement ?"
  - "Quel est le principal avantage de l'utilisation de SGDRegressor par rapport au modèle Ridge ?"
  - "Quels types de modèles et quel algorithme de résolution la classe SGDRegressor implémente-t-elle ?"
  - "Quelle est la restriction majeure concernant le format du résultat lors de l'utilisation de SGDRegressor ?"
  - "Qu'est-ce que l'apprentissage hors mémoire (out-of-core learning) et quelle méthode spécifique de scikit-learn permet de l'utiliser ?"
  - "Quelles techniques de stockage et de lecture de fichiers sont illustrées dans les exemples pour charger des données par lots ?"
  - "Quelles sont les principales caractéristiques et avantages de la bibliothèque Snap ML développée par IBM ?"
  - "Quelles sont les étapes à suivre pour installer Snap ML à l'aide d'un wheel Python dans un environnement virtuel ?"
  - "Comment le paramètre n_jobs permet-il d'exploiter le parallélisme par fils pour optimiser les performances de Snap ML par rapport à scikit-learn ?"
  - "De quelle manière Snap ML gère-t-il l'accélération matérielle via un ou plusieurs GPU ainsi que l'entraînement hors mémoire pour les grands ensembles de données ?"
  - "Quelles sont les capacités techniques et les optimisations permises par cet outil ?"
  - "Dans quel cas spécifique est-il recommandé d'utiliser son API pour remplacer scikit-learn ?"
  - "Quelle commande doit-on exécuter pour connaître la version la plus récente de Snap ML disponible ?"
  - "Comment le code Python fourni utilise-t-il `numpy.memmap` avec `snapml` pour entraîner un modèle d'apprentissage automatique ?"
  - "Quelles commandes permettent d'exécuter les implémentations distribuées des estimateurs de Snap ML ?"
  - "Quels sont les principaux avantages et fonctionnalités de la bibliothèque Spark ML pour le traitement de données massives sur plusieurs nœuds ?"
  - "Quels types de solveurs sont utilisés par défaut par les estimateurs de Snap ML ?"
  - "Comment Snap ML permet-il de réaliser des entraînements en lots sans charger l'intégralité des données en mémoire ?"
  - "Quelle différence majeure existe-t-il entre Snap ML et scikit-learn concernant le traitement des vecteurs numpy ?"
  - "Comment le code Python fourni utilise-t-il `numpy.memmap` avec `snapml` pour entraîner un modèle d'apprentissage automatique ?"
  - "Quelles commandes permettent d'exécuter les implémentations distribuées des estimateurs de Snap ML ?"
  - "Quels sont les principaux avantages et fonctionnalités de la bibliothèque Spark ML pour le traitement de données massives sur plusieurs nœuds ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Dans le domaine de l’apprentissage profond, la mise à l'échelle en termes de quantité de données est rendue possible par l'utilisation de stratégies de traitement en très petits lots et de solveurs itératifs du premier ordre. En apprentissage de réseaux de neurones profonds, le code s’exécute plus ou moins de la même manière, qu’il s’agisse de quelques milliers ou de centaines de millions d’exemples : quelques exemples sont chargés à partir d’une source (disque, mémoire, source à distance, etc.), les gradients sont calculés pendant les itérations, ce qui modifie les paramètres du modèle au fur et à mesure. Par contre, avec plusieurs trousses logicielles d'apprentissage machine traditionnel, notamment scikit-learn, écrire du code pour faire de l'entraînement à large échelle est souvent complexe. Pour plusieurs algorithmes qui conviennent à des modèles communs comme les modèles linéaires généralisés (GLM pour *Generalized Linear Models*) et les machines à vecteurs de support (SVM pour *Support Vector Machines*), leur implémentation par défaut exige que la totalité de l’ensemble d’apprentissage soit chargée en mémoire et n’offre aucune fonctionnalité de parallélisme par fils ou par processus. De plus, certaines de ces implémentations se basent sur des solveurs plutôt exigeants en mémoire qui, pour bien fonctionner, exigent une quantité de mémoire plusieurs fois supérieure à la taille de l’ensemble de données à entraîner.

Nous examinons ici des options pour adapter les méthodes d'apprentissage machine traditionnel à de très grands ensembles de données, particulièrement lorsque l'utilisation d'un nœud à grande mémoire s'avère insuffisante ou que le traitement séquentiel est excessivement long.

## Scikit-learn

[Scikit-learn](https://scikit-learn.org/stable/index.html) est un module Python pour l’apprentissage machine basé sur SciPy et distribué sous la licence BSD-3-Clause. La trousse logicielle est dotée d’une interface de programmation (API) intuitive qui simplifie la construction de chaînes de traitement complexes pour l'apprentissage machine. Toutefois, plusieurs implémentations des méthodes GLM et SVM supposent que l’ensemble d’entraînement est complètement chargé en mémoire, ce qui n'est pas toujours souhaitable. De plus, certains de ces algorithmes utilisent par défaut des solveurs très exigeants en mémoire. Dans certains cas, les suggestions suivantes permettent de contourner ces limitations.

## Solveurs du gradient stochastique

Si votre ensemble de données est assez petit pour être chargé au complet en mémoire, mais que pendant l’entraînement vous obtenez des erreurs de mémoire insuffisante (OOM pour *Out-Of-Memory*), le problème est probablement dû à un solveur trop exigeant en mémoire. Avec scikit-learn, plusieurs méthodes offrent en option des variations de l’[algorithme du gradient stochastique](https://fr.wikipedia.org/wiki/Algorithme_du_gradient_stochastique) et le remplacement du solveur par défaut par un solveur du gradient stochastique est souvent une solution facile.

Dans les exemples suivants, une [régression de crête (*ridge regression*)](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html) utilise le solveur par défaut et un solveur du gradient stochastique. Pour observer l’utilisation de la mémoire, lancez la commande `htop` dans le terminal lorsque le programme Python s’exécute.

```python title="ridge-default.py"
from sklearn.datasets import make_regression
from sklearn.linear_model import Ridge

X,y = make_regression(n_samples=100000, n_features=10000, n_informative=50)

model = Ridge()

model.fit(X,y)
```

```python title="ridge-saga.py"
from sklearn.datasets import make_regression
from sklearn.linear_model import Ridge

X,y = make_regression(n_samples=100000, n_features=10000, n_informative=50)

model = Ridge(solver='saga')

model.fit(X,y)
```

Une autre option qui réduit encore plus l'utilisation de la mémoire est de travailler avec [SGDRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html) plutôt qu’avec Ridge. Cette classe implémente plusieurs types de modèles linéaires généralisés (GLM) pour les régressions avec comme solveur l’algorithme du gradient stochastique (SGD). Il est cependant important de noter que SGDRegressor fonctionne uniquement lorsque le résultat est unidimensionnel (scalaire).

```python title="ridge-sgd_regressor.py"
from sklearn.datasets import make_regression
from sklearn.linear_model import SGDRegressor

X,y = make_regression(n_samples=100000, n_features=10000, n_informative=50)

model = SGDRegressor(penalty='l2') # set penalty='l2' to perform a ridge regression

model.fit(X,y)
```

## Apprentissage en lots

Dans les cas où votre ensemble de données est trop grand pour la mémoire disponible, ou juste assez grand pour ne pas laisser assez de mémoire pour l'entraînement, il est possible de garder les données sur disque et de les charger par lots, comme c’est le cas avec les trousses logicielles d’apprentissage profond. Scikit-learn appelle cette technique l'*out-of-core learning* (apprentissage hors mémoire) et c’est une option viable quand l’estimateur offre la [méthode `partial_fit`](https://scikit-learn.org/stable/computing/scaling_strategies.html?highlight=partial_fit#incremental-learning). Dans les exemples ci-dessous, l’apprentissage hors mémoire se fait par des itérations sur des ensembles de données enregistrés sur disque.

Dans le premier exemple, nous utilisons [SGDClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html) pour ajuster un classifieur linéaire SVM avec des lots de données en provenance d’une paire de vecteurs **numpy**. Les vecteurs sont stockés sur disque dans des [fichiers npy](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.html#npy-format) qui seront [mappés en mémoire](https://numpy.org/doc/stable/reference/generated/numpy.memmap.html). Puisque `SGDClassifier` possède la méthode `partial_fit`, les itérations peuvent se faire dans les grands fichiers en mémoire en ne chargeant que des petits lots à la fois en provenance des vecteurs. Chaque appel à `partial_fit` exécutera alors une époque de l’algorithme du gradient stochastique sur un lot de données.

```python title="svm-sgd-npy.py"
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

Une autre méthode de stockage des données est d’utiliser des fichiers CSV. Dans le prochain exemple, l'entraînement d’un modèle de régression lasso se fait par la lecture par lots de données à partir d’un fichier CSV avec la trousse logicielle [pandas](https://pandas.pydata.org).

```python title="lasso-sgd-csv.py"
import pandas as pd
from sklearn.linear_model import SGDRegressor

model = SGDRegressor(penalty='l1')

for batch in pd.read_csv("./data.csv", chunksize=512, iterator=True):
    X = batch.drop('target', axis=1)
    y = batch['target']
    model.partial_fit(X,y)
```

## Snap ML
[Snap ML](https://snapml.readthedocs.io/en/latest/) est une bibliothèque d'apprentissage machine propriétaire développée par IBM, qui prend en charge plusieurs modèles classiques et s'adapte facilement à des ensembles de données comportant des milliards d'exemples et/ou de variables. Elle permet l'entraînement distribué, l'accélération par GPU et l'utilisation de structures creuses. Son interface de programmation (API) est très similaire à celle de scikit-learn et peut la remplacer pour la gestion d'ensembles de données massifs.

## Installation 

### Wheels ajoutés récemment
Pour connaître la plus récente version de Snap ML que nous avons construite, exécutez :
```bash
avail_wheels "snapml"
```
Pour plus d'information, voir [Wheels disponibles](../python.md#wheels-disponibles).

### Installer le wheel

L'option à privilégier est d'utiliser le [wheel Python](https://pythonwheels.com/) comme suit :
1. [Chargez un module](../../programming/utiliser_des_modules.md#sous-commande-load) Python avec `module load python`.
2. Créez et activez un [environnement virtuel Python](../python.md#créer-et-utiliser-un-environnement-virtuel).
3. Installez Snap ML dans l'environnement virtuel avec `pip install`. 

```bash
(venv) [name@server ~]$ pip install --no-index snapml
```

## Multifil

Tous les estimateurs de Snap ML prennent en charge le parallélisme par *threads*, contrôlé par le paramètre `n_jobs`. En définissant ce paramètre à la valeur correspondant au nombre de cœurs disponibles pour votre tâche, on peut généralement observer une accélération par rapport à l'implémentation du même estimateur avec scikit-learn. Voici comment se compare la performance de Ridge entre scikit-learn et Snap ML.

```python title="ridge-snap-vs-sklearn.py"
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

## Entraînement sur GPU

Tous les estimateurs de Snap ML prennent en charge l'accélération d’un ou plusieurs GPU. Pour l’entraînement avec un GPU, le paramètre est `use_gpu=True`. Pour l’entraînement avec plusieurs GPU, le paramètre est aussi `use_gpu`, et la liste des ID des GPU disponibles est passée à `device_ids`. Par exemple, pour une tâche qui demande deux GPU, `device_ids=[0,1]` utilisera les deux GPU. Le prochain exemple fait la même comparaison que dans la section précédente, mais pour l'entraînement d'un classifieur SVM avec un noyau non linéaire.

```python title="ridge-snap-vs-sklearn2.py"
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

## Entraînement hors mémoire

Tous les estimateurs de Snap ML utilisent par défaut des solveurs itératifs du premier ordre, tels que le SGD. Il est donc possible de faire des entraînements par lots sans avoir à charger en mémoire les ensembles de données au complet. Par contre, Snap ML accepte les entrées de vecteurs **numpy** par mappage en mémoire, contrairement à scikit-learn.

```python title="snap-npy.py"
import numpy as np
from snapml import LogisticRegression

X = np.memmap('./x_array.npy',dtype='float64',shape=(100000,10000))
y = np.memmap('./y_array.npy',dtype='int8',shape=(100000,))

model = LogisticRegression(n_jobs=4)

model.fit(X,y)
```

## MPI

Snap ML offre des implémentations distribuées de plusieurs estimateurs. Pour utiliser le mode distribué, exécutez un script Python avec `mpirun` ou `srun`.

## Spark ML

[Spark ML](https://spark.apache.org/docs/latest/ml-guide.html) est une bibliothèque basée sur [Apache Spark](../apache_spark.md) qui permet la mise à l'échelle de plusieurs méthodes d'apprentissage machine pour d'énormes quantités de données et sur plusieurs nœuds, sans qu'il soit nécessaire de distribuer des ensembles de données ou de créer du code distribué ou parallèle. Elle inclut plusieurs outils utiles en algèbre linéaire et en statistique. Avant de reproduire les exemples de la [documentation Spark ML](https://spark.apache.org/docs/latest/ml-guide.html), consultez notre [tutoriel sur la soumission de tâches Spark](../apache_spark.md#utilisation).