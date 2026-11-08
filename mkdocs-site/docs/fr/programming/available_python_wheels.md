---
title: "Available Python wheels/fr"
slug: "available_python_wheels"
lang: "fr"

source_wiki_title: "Available Python wheels/fr"
source_hash: "422fa00b89ff0e8e760f7b80216b4bdc"
last_synced: "2026-11-08T02:07:32.985064+00:00"
last_processed: "2026-11-08T02:49:17.697745+00:00"

tags:
  []

keywords:
  - "module spider"
  - "commande avail_wheels"
  - "wheels Python"
  - "soutien technique"
  - "environnement logiciel"

questions:
  - "Comment vérifier quels wheels sont disponibles dans l’environnement StdEnv actif ?"
  - "Quelle procédure suivre pour demander l’ajout ou la mise à jour d’un wheel sur les grappes nationales ?"
  - "Pourquoi certains wheels n’apparaissent pas dans les tableaux et comment les retrouver ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Vous trouverez à la dernière section les [*wheels* Python](https://pythonwheels.com/) qui sont disponibles sur nos grappes nationales. Ces listes sont mises à jour quand un nouveau *wheel* est ajouté. Pour demander l'ajout ou la mise à jour d'un *wheel*, contactez le [soutien technique](../support/technical_support.md).

!!! warning "Disponibilité"
    **Certains *wheels* ne sont peut-être pas disponibles dans l'environnement standard que vous avez chargé.**

    Pour connaître les *wheels* qui peuvent être installés dans votre StdEnv actif, utilisez la commande `avail_wheels` décrite dans [Wheels disponibles](../software/python.md).

## Wheels faisant partie d'un module
Certains *wheels* ne paraissent pas dans les tableaux parce qu'ils font partie de modules, par exemple :
* [pyarrow (Arrow)](../software/arrow.md#pyarrow)
* pyqt5 (QT)
* petsc4py (PETSc)
* [opencv_python (OpenCV)](../software/opencv.md)

Pour trouver ces extensions, lancez la commande :
```bash
module spider <python package>
```

## Lister un wheel dans votre environnement logiciel actif
1.  Chargez l'environnement logiciel.
    ```bash
    module load StdEnv/YYYY
    ```
    où `YYYY` est `2026` ou `2023`

2.  Cherchez un *wheel* en particulier.
    ```bash
    avail_wheels <name>
    ```
    où `name` est le nom du *wheel* que vous cherchez.

## Wheels disponibles dans tous nos environnements logiciels
=== "Python 3.15"
    <!-- Le contenu de la liste des wheels pour Python 3.15 (transclus du wiki depuis {{:Wheels3.15}}) devrait être ici. -->
=== "Python 3.14"
    <!-- Le contenu de la liste des wheels pour Python 3.14 (transclus du wiki depuis {{:Wheels3.14}}) devrait être ici. -->
=== "Python 3.13"
    <!-- Le contenu de la liste des wheels pour Python 3.13 (transclus du wiki depuis {{:Wheels3.13}}) devrait être ici. -->
=== "Python 3.12"
    <!-- Le contenu de la liste des wheels pour Python 3.12 (transclus du wiki depuis {{:Wheels3.12}}) devrait être ici. -->
=== "Python 3.11"
    <!-- Le contenu de la liste des wheels pour Python 3.11 (transclus du wiki depuis {{:Wheels3.11}}) devrait être ici. -->
=== "Python 3.10"
    <!-- Le contenu de la liste des wheels pour Python 3.10 (transclus du wiki depuis {{:Wheels3.10}}) devrait être ici. -->