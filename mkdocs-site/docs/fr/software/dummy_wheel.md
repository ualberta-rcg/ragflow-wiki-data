---
title: "Dummy wheel/fr"
slug: "dummy_wheel"
lang: "fr"

source_wiki_title: "Dummy wheel/fr"
source_hash: "93a7107f3d48c822760efa46cafc7f7b"
last_synced: "2026-05-02T23:50:34.269007+00:00"
last_processed: "2026-05-03T00:53:08.629588+00:00"

tags:
  - software

keywords:
  - "pip"
  - "Python packages"
  - "pyarrow"
  - "markup"
  - "python module"
  - "div"
  - "pip list"
  - "available"
  - "Dummy Wheel"
  - "closing tag"
  - "element"
  - "HTML"
  - "virtual environment"

questions:
  - "What is the primary purpose of a \"Dummy Wheel\" in the wheelhouse infrastructure?"
  - "What are the three main reasons pip might select a dummy wheel and raise an error during package installation?"
  - "How can a user verify if the required Python bindings for a loaded module are available and recognized by pip?"
  - "What is the primary function of the `</div>` tag within an HTML document?"
  - "How does the placement of a closing div tag affect the structural hierarchy and CSS styling of a webpage?"
  - "What are the potential rendering issues or errors that occur if a `</div>` tag is used without a corresponding opening tag?"
  - "What specific command can be used to check if the pyarrow module is recognized by pip?"
  - "How can you determine from the command output that pyarrow is available and seen by pip?"
  - "What does the absence of an entry in the pip list output indicate about the pyarrow module?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

La roue factice (Dummy Wheel) existe dans le dépôt de roues (wheelhouse) afin de fournir des substituts pour certains paquets Python populaires qui sont disponibles sur PyPI mais sous forme de modules sur notre infrastructure. Ils sont tous étiquetés avec une version locale (`dummy`), par exemple : `pyarrow-23.0.1+dummy.computecanada-py3-none-any.whl`.

Voici quelques exemples :
* [pyarrow (Arrow)](arrow.md#pyarrow)
* [opencv-python (OpenCV)](opencv.md)
* [MPI4py](../programming/mpi4py.md)

Lorsqu'une roue factice est sélectionnée par `pip`, une erreur sera levée, car `pip` n'aura pas trouvé de correspondance pour cette exigence.

## Dépannage
### Il s'agit d'une erreur normale générée par cette roue factice.

!!! note "Remarque"
    Dans l'exemple ci-dessous, `pyarrow` est utilisé comme exemple, mais la même logique s'applique à d'autres paquets également.

Lorsque la dépendance à `pyarrow` n'est pas satisfaite, une erreur sera levée lorsque la roue factice est sélectionnée. **Ceci est normal**.
Cela signifie que :
1.  le module Arrow n'a pas été chargé, et donc `pip` n'a pas pu trouver `pyarrow`
2.  la version d'Arrow chargée ne satisfait pas la version requise par le paquet dépendant
3.  le module Arrow chargé ne supporte pas la version de Python utilisée

#### Module non chargé
Dans ce cas, désactivez tout environnement virtuel, chargez le module, réactivez l'environnement virtuel et réexécutez votre commande `pip install`.

1. Désactivez votre environnement virtuel Python.
    ```bash
    test $VIRTUAL_ENV && deactivate
    ```

2. Chargez le module Arrow.
    ```bash
    module load gcc arrow/x.y.z python/x.y.z
    ```
    où `x.y.z` est la version requise.

3. Réactivez votre environnement virtuel précédemment créé.
    ```bash
    source <env>/bin/activate
    ```

4. Et réexécutez votre commande `pip install`.
    ```bash
    pip install <paquet>
    ```

#### Version du paquet/module
Le module Arrow chargé ne satisfait pas l'exigence. Par exemple, `(from pyarrow>=21.0.0->datasets)` signifie que cette version du paquet `datasets` nécessite `pyarrow` en version supérieure ou égale à `21.0.0`.

Autrement dit, l'utilisation de toute version antérieure avec cette version de `datasets` entraînera l'installation de la roue factice.

Vous pouvez trouver l'exigence (version) recherchée en examinant la ligne (`pyarrow_noinstall`) :
```bash
pip install --no-index datasets
```
```text
...
Processing /cvmfs/soft.computecanada.ca/custom/python/wheelhouse/generic/pyarrow_noinstall-9999+dummy.computecanada.tar.gz (from pyarrow>=21.0.0->datasets)
```

#### Pas de liaisons Python

Le module chargé pourrait ne pas avoir les liaisons Python pour le module Python utilisé.
Vous pouvez rapidement vérifier en utilisant :
```bash
python -c "import pyarrow"
```
Si la commande n'affiche rien, l'importation a réussi et le module fournit `pyarrow` pour le module Python utilisé.

Ou l'on peut vérifier si `pip` le détecte :
```bash
pip list | grep pyarrow
```
```text
pyarrow    23.0.0
```

Si `pip list` affiche une entrée, alors `pyarrow` est disponible et détecté par `pip`. Autrement, en l'absence d'entrée, `pyarrow` n'est pas disponible.