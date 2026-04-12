---
title: "Available Python wheels/fr"
slug: "available_python_wheels"
lang: "fr"

source_wiki_title: "Available Python wheels/fr"
source_hash: "b6f1923418732c499a4b67002812703c"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:38:14.655488+00:00"

tags:
  []

keywords:
  - "grappes nationales"
  - "wheels Python"
  - "avail_wheels"
  - "environnement logiciel"
  - "modules"

questions:
  - "Comment peut-on demander l'ajout ou la mise à jour d'un wheel Python sur les grappes nationales ?"
  - "Quelle commande doit-on utiliser pour trouver des wheels qui font partie de modules spécifiques ?"
  - "Comment peut-on vérifier si un wheel particulier est disponible dans l'environnement logiciel actif ?"
  - "Comment peut-on demander l'ajout ou la mise à jour d'un wheel Python sur les grappes nationales ?"
  - "Quelle commande doit-on utiliser pour trouver des wheels qui font partie de modules spécifiques ?"
  - "Comment peut-on vérifier si un wheel particulier est disponible dans l'environnement logiciel actif ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Vous trouverez à la dernière section les [*wheels* Python](https://pythonwheels.com/) qui sont disponibles sur nos grappes nationales. Ces listes sont mises à jour quand un nouveau wheel est ajouté. Pour demander l'ajout ou la mise à jour d'un wheel, contactez le [soutien technique](../support/technical_support.md).

!!! warning "Disponibilité"
    **Certains wheels ne sont peut-être pas disponibles dans l'environnement standard que vous avez chargé.**

    Pour connaître les wheels qui peuvent être installés dans votre StdEnv actif, utilisez la commande `avail_wheels` décrite dans [Wheels disponibles](../software/python.md#wheels-disponibles).

## Wheels faisant partie d'un module
Certains wheels ne paraissent pas dans les tableaux parce qu'ils font partie de modules, par exemple :
* [pyarrow (Arrow)](../software/arrow.md#pyarrow)
* pyqt5 (QT)
* petsc4py (PETSc)
* [opencv_python (OpenCV)](../software/opencv.md#python-bindings)

Pour trouver ces extensions, lancez la commande
```bash
module spider <python package>
```

## Lister un wheel dans votre environnement logiciel actif
1. Chargez l'environnement logiciel.
```bash
module load StdEnv/YYYY
```
où `YYYY` est `2020` ou `2023`

2. Cherchez un wheel en particulier.
```bash
avail_wheels <name>
```
où `name` est le nom du wheel que vous cherchez.

## Wheels disponibles dans tous nos environnements logiciels

=== "Python 3.14"

=== "Python 3.13"

=== "Python 3.12"

=== "Python 3.11"

=== "Python 3.10"

=== "Python 3.9 (non supporté)"

=== "Python 3.8 (non supporté)"