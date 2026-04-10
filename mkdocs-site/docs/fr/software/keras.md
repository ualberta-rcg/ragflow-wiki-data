---
title: "Keras/fr"
tags:
  - software
  - ai-and-machine-learning

keywords:
  []
---

[Keras](https://fr.wikipedia.org/wiki/Keras) est une bibliothèque open source écrite en Python qui permet d'interagir avec les algorithmes de réseaux de neurones profonds et d'apprentissage machine, notamment Tensorflow, CNTK et Theano.

Si vous voulez porter un programme Keras sur une de nos grappes, il serait bon de prendre connaissance du [tutoriel sur le sujet](tutoriel-apprentissage-machine.md).

## Installation

#Installez [TensorFlow](tensorflow-fr.md), CNTK ou Theano dans un [environnement virtuel Python](python-fr#créer_et_utiliser_un_environnement_virtuel.md).
#Activez l’environnement virtuel (dans notre exemple, <tt>$HOME/tensorflow</tt>).
#:
```bash
source $HOME/tensorflow/bin/activate
```

#Installez Keras dans l’environnement virtuel.
#:
```bash
pip install keras
```

### Utilisation avec R 

Pour installer Keras pour R avec TensorFlow comme application dorsale (<i>backend</i>) :

#Installez TensorFlow [suivant ces directives](tensorflow-fr#le_paquet_r.md).
#Suivez les directives de la section parent.
#Chargez les modules nécessaires.  
#:
```bash
module load gcc/7.3.0 r/3.5.2
```

# Lancez R.
#:
```bash
R
```

#Avec `devtools`, installez Keras dans R. 
#:<syntaxhighlight lang='r'>
devtools::install_github('rstudio/keras')
</syntaxhighlight>

Puisque Keras et TensorFlow sont installés dans l’environnement virtuel avec ` pip`, n’utilisez pas `install_keras()`.  

Pour utiliser Keras, activez l’environnement virtuel et lancez les commandes
<syntaxhighlight lang='r'>
library(keras)
use_virtualenv(Sys.getenv('VIRTUAL_ENV'))
</syntaxhighlight>

## Références 

[page Wikipédia sur Keras](https://fr.wikipedia.org/wiki/Keras)