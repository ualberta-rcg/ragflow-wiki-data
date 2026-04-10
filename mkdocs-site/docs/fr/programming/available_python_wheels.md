---
title: "Available Python wheels/fr"
slug: "available_python_wheels"
lang: "fr"

source_wiki_title: "Available Python wheels/fr"
source_hash: "b6f1923418732c499a4b67002812703c"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T04:47:03.418227+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

Vous trouverez à la dernière section les [*wheels* Python](https://pythonwheels.com/) qui sont disponibles sur nos grappes nationales. Ces listes sont mises à jour quand un nouveau wheel est ajouté. Pour demander l'ajout ou la mise à jour d'un wheel, contactez le [soutien technique](soutien-technique.md).

!!! attention "Disponibilité"
    **Certains *wheels* ne sont peut-être pas disponibles dans l'environnement standard que vous avez chargé.**

    Pour connaître les *wheels* qui peuvent être installés dans votre `StdEnv` actif, utilisez la commande `avail_wheels` décrite dans [Wheels disponibles](python.md#wheels-disponibles).

## Wheels faisant partie d'un module
Certains *wheels* ne paraissent pas dans les tableaux parce qu'ils font partie de modules, par exemple :
*   [pyarrow (Arrow)](arrow.md#pyarrow)
*   pyqt5 (QT)
*   petsc4py (PETSc)
*   [opencv_python (OpenCV)](opencv.md#python-bindings)

Pour trouver ces extensions, lancez la commande
```bash
module spider <python package>
```

## Lister un wheel dans votre environnement logiciel actif
1.  Chargez l'environnement logiciel.
    ```bash
    module load StdEnv/YYYY
    ```
    où `YYYY` est `2020` ou `2023`.

2.  Cherchez un *wheel* en particulier.
    ```bash
    avail_wheels <name>
    ```
    où `name` est le nom du *wheel* que vous cherchez.

## Wheels disponibles dans tous nos environnements logiciels

=== "Python 3.14"
    Les wheels pour Python 3.14 seraient listés ici (contenu de la page `Wheels3.14`).

=== "Python 3.13"
    Les wheels pour Python 3.13 seraient listés ici (contenu de la page `Wheels3.13`).

=== "Python 3.12"
    Les wheels pour Python 3.12 seraient listés ici (contenu de la page `Wheels3.12`).

=== "Python 3.11"
    Les wheels pour Python 3.11 seraient listés ici (contenu de la page `Wheels3.11`).

=== "Python 3.10"
    Les wheels pour Python 3.10 seraient listés ici (contenu de la page `Wheels3.10`).

=== "Python 3.9 (n'est plus supporté)"
    Les wheels pour Python 3.9 seraient listés ici (contenu de la page `Wheels3.9`).

=== "Python 3.8 (n'est plus supporté)"
    Les wheels pour Python 3.8 seraient listés ici (contenu de la page `Wheels3.8`).