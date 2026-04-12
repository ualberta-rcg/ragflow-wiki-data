---
title: "PyRETIS/fr"
slug: "pyretis"
lang: "fr"

source_wiki_title: "PyRETIS/fr"
source_hash: "d53dcadf2c97b589b4022626b2b6dfd4"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:32:30.351748+00:00"

tags:
  - software
  - biomolecularsimulation

keywords:
  - "PyRETIS"
  - "événements rares"
  - "environnement virtuel"
  - "Python"
  - "simulations moléculaires"

questions:
  - "Qu'est-ce que la bibliothèque PyRETIS et pour quel type de simulations moléculaires est-elle conçue ?"
  - "Quelles sont les étapes et les contraintes spécifiques, notamment concernant MDTraj, pour installer correctement PyRETIS dans un environnement virtuel ?"
  - "Comment doit-on configurer les modules pour pouvoir exécuter l'outil d'analyse PyVisA avec son interface utilisateur ?"
  - "Qu'est-ce que la bibliothèque PyRETIS et pour quel type de simulations moléculaires est-elle conçue ?"
  - "Quelles sont les étapes et les contraintes spécifiques, notamment concernant MDTraj, pour installer correctement PyRETIS dans un environnement virtuel ?"
  - "Comment doit-on configurer les modules pour pouvoir exécuter l'outil d'analyse PyVisA avec son interface utilisateur ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[PyRETIS](http://www.pyretis.org/) est une bibliothèque Python pour les simulations moléculaires d'événements rares utilisant des méthodes basées sur l'échantillonnage d'interfaces de transition (*TIS, transition interface sampling*) et l'échantillonnage d'interfaces de transition par échange de répliques (*RETIS, replica exchange transition interface sampling*).

## Installation

L'Alliance de recherche numérique du Canada (l'Alliance) propose des *wheels* Python précompilés pour PyRETIS ([voir les *wheels* disponibles](../programming/available_python_wheels.md)) qui sont compatibles avec certaines versions de Python et peuvent être installés dans un [environnement virtuel Python](python.md#creer-et-utiliser-un-environnement-virtuel).

En date de juillet 2020, PyRETIS 2.5.0 est compatible avec les versions Python 3.6 et 3.7. Selon [les directives d'installation](http://www.pyretis.org/v2.5.0/user/install.html), la dépendance [MDTraj](http://mdtraj.org/) doit être installée **après** PyRETIS.

Pour créer un environnement virtuel Python, entrez les commandes suivantes. Les lignes débutant par `` # `` sont des commentaires, celles par `` $ `` indiquent une invite de commande standard, et celles par `` (env_PyRETIS) $ `` indiquent une invite avec l'environnement virtuel activé.

```bash
# Chargez le module Python que vous voulez utiliser, par exemple python/3.7 :
$ module load python/3.7

# Créez un environnement virtuel
$ virtualenv --no-download ~/env_PyRETIS

# Activez l'environnement virtuel
$ source ~/env_PyRETIS/bin/activate

# Installez PyRETIS puis mdtraj
(env_PyRETIS) $ pip install --no-index pyretis
(env_PyRETIS) $ pip install --no-index mdtraj

# Exécutez PyRETIS
(env_PyRETIS) $ pyretisrun --help
```

Pour utiliser `pyretisrun` (dans vos scripts par exemple), vous n'avez qu'à activer l'environnement virtuel à nouveau avec :

```bash
source ~/env_PyRETIS/bin/activate
pyretisrun --input INPUT.rst  --log_file LOG_FILE.log
```

!!! note "Configuration pour PyVisA"
    PyRETIS inclut l'outil d'analyse PyVisA, dont l'interface utilisateur graphique (GUI) requiert PyQt5 pour fonctionner. PyQt5 est fourni par le module Qt. Pour que votre environnement virtuel Python puisse détecter PyQt5, il est primordial de charger les modules Python et Qt *avant* d'activer votre environnement virtuel, comme ceci :

    ```bash
    $ module load python/3.7 qt/5.11.3
    $ source ~/env_PyRETIS/bin/activate
    (env_PyRETIS) $ pyretisanalyse  -pyvisa  ...
    ```

## Utilisation

Consultez [la documentation officielle](http://www.pyretis.org/) et les articles suivants :

1.  Lervik A, Riccardi E, van Erp TS. PyRETIS: A well-done, medium-sized python library for rare events. J Comput Chem. 2017;38: 2439–2451. [doi:10.1002/jcc.24900](https://doi.org/10.1002/jcc.24900)
2.  Riccardi E, Lervik A, Roet S, Aarøen O, Erp TS. PyRETIS 2: An improbability drive for rare events. J Comput Chem. 2020;41: 370–377. [doi:10.1002/jcc.26112](http://doi.org/10.1002/jcc.26112)