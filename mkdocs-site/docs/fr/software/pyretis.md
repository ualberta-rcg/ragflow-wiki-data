---
title: "PyRETIS/fr"
slug: "pyretis"
lang: "fr"

source_wiki_title: "PyRETIS/fr"
source_hash: "d53dcadf2c97b589b4022626b2b6dfd4"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T10:05:06.458131+00:00"

tags:
  - software
  - biomolecularsimulation

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

[PyRETIS](http://www.pyretis.org/) est une bibliothèque Python pour les simulations moléculaires d'événements rares avec des méthodes basées sur l'échantillonnage d'interfaces de transition (*TIS, transition interface sampling*) et l'échantillonnage d'interfaces de transition d'échange de répliques (*RETIS, replica exchange transition interface sampling*).

## Installation

Calcul Canada offre des roues Python précompilées pour PyRETIS ([voir les roues Python disponibles](available-python-wheels.md)) qui sont compatibles avec certaines versions de Python et peuvent être installées dans un [environnement virtuel Python](python.md#creer-et-utiliser-un-environnement-virtuel).

En date de juillet 2020, PyRETIS 2.5.0 est compatible avec les versions Python 3.6 et 3.7.

!!! attention "Ordre d'installation"
    Selon [les directives d'installation](http://www.pyretis.org/v2.5.0/user/install.html), la dépendance [MDTraj](http://mdtraj.org/) doit être installée **après** PyRETIS.

Pour créer un `virtualenv` Python, lancez les commandes suivantes, où les lignes commençant par `` `#` `` sont des commentaires, celles commençant par `` `$` `` sont des invites et celles commençant par `` `(env_PyRETIS) $` `` sont des invites avec le `virtualenv` activé.

```bash
# charger le module Python que nous voulons utiliser, par exemple python/3.7:
$ module load python/3.7

# créer un virtualenv
$ virtualenv --no-download ~/env_PyRETIS

# activer le virtualenv
$ source ~/env_PyRETIS/bin/activate

# installer PyRETIS puis mdtraj
(env_PyRETIS) $ pip install --no-index pyretis
(env_PyRETIS) $ pip install --no-index mdtraj

# lancer PyRETIS
(env_PyRETIS) $ pyretisrun --help
```

Pour utiliser `pyretisrun` (dans les scripts par exemple), nous n'avons qu'à activer le module à nouveau avec :

```bash
source ~/env_PyRETIS/bin/activate
pyretisrun --input INPUT.rst  --log_file LOG_FILE.log
```

PyRETIS offre aussi l'outil d'analyse PyVisA dont l'interface utilisateur nécessite que PyQt5 soit exécuté. PyQt5 est inclus dans le module Qt.

!!! attention "Chargement des modules pour PyVisA"
    Pour que la version Python de `virtualenv` puisse trouver PyQt5, il est important de charger d'abord les modules pour Python et Qt avant d'activer le `virtualenv` Python ainsi :

```bash
$ module load python/3.7 qt/5.11.3
$ source ~/env_PyRETIS/bin/activate
(env_PyRETIS) $ pyretisanalyse  -pyvisa  ...
```

## Utilisation

Consultez [la documentation sur le site web](http://www.pyretis.org/) et dans les articles suivants :

1.  Lervik A, Riccardi E, van Erp TS. PyRETIS: A well-done, medium-sized python library for rare events. J Comput Chem. 2017;38: 2439–2451. [doi:10.1002/jcc.24900](https://doi.org/10.1002/jcc.24900)
2.  Riccardi E, Lervik A, Roet S, Aarøen O, Erp TS. PyRETIS 2: An improbability drive for rare events. J Comput Chem. 2020;41: 370–377. [doi:10.1002/jcc.26112](http://doi.org/10.1002/jcc.26112)