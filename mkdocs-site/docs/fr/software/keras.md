---
title: "Keras/fr"
slug: "keras"
lang: "fr"

source_wiki_title: "Keras/fr"
source_hash: "a876916fbe563d0f491fce2e462a1197"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:23:40.415386+00:00"

tags:
  - software
  - ai-and-machine-learning

keywords:
  - "Keras"
  - "Environnement virtuel"
  - "Apprentissage machine"
  - "Python"
  - "TensorFlow"

questions:
  - "Qu'est-ce que la bibliothèque Keras et avec quelles applications dorsales permet-elle d'interagir ?"
  - "Quelles sont les étapes à suivre pour installer Keras dans un environnement virtuel Python ?"
  - "Comment configurer et utiliser Keras avec le langage R à partir d'un environnement virtuel existant ?"
  - "Qu'est-ce que la bibliothèque Keras et avec quelles applications dorsales permet-elle d'interagir ?"
  - "Quelles sont les étapes à suivre pour installer Keras dans un environnement virtuel Python ?"
  - "Comment configurer et utiliser Keras avec le langage R à partir d'un environnement virtuel existant ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Keras](https://fr.wikipedia.org/wiki/Keras) est une bibliothèque open source écrite en Python qui permet d'interagir avec les algorithmes de réseaux de neurones profonds et d'apprentissage machine, notamment TensorFlow, CNTK et Theano.

Si vous voulez porter un programme Keras sur l'une de nos grappes, il serait bon de prendre connaissance du [tutoriel sur le sujet](ai-ml/tutoriel_apprentissage_machine.md).

## Installation

1.  Installez [TensorFlow](tensorflow.md), CNTK ou Theano dans un [environnement virtuel Python](python.md#créer-et-utiliser-un-environnement-virtuel).
2.  Activez l'environnement virtuel (dans notre exemple, `$HOME/tensorflow`).
    ```bash
    source $HOME/tensorflow/bin/activate
    ```
3.  Installez Keras dans l'environnement virtuel.
    ```bash
    pip install keras
    ```

### Utilisation avec R

Pour installer Keras pour R avec TensorFlow comme application dorsale (*backend*) :

1.  Installez TensorFlow [suivant ces directives](tensorflow.md#le-paquet-r).
2.  Suivez les directives de la section parente.
3.  Chargez les modules nécessaires.
    ```bash
    module load gcc/7.3.0 r/3.5.2
    ```
4.  Lancez R.
    ```bash
    R
    ```
5.  Avec `devtools`, installez Keras dans R.
    ```r
    devtools::install_github('rstudio/keras')
    ```

!!! attention "Note importante"
    Puisque Keras et TensorFlow sont installés dans l'environnement virtuel avec `pip`, **n'utilisez pas** `install_keras()`.

Pour utiliser Keras, activez l'environnement virtuel et lancez les commandes :

```r
library(keras)
use_virtualenv(Sys.getenv('VIRTUAL_ENV'))
```

## Références

[Page Wikipédia sur Keras](https://fr.wikipedia.org/wiki/Keras)