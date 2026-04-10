---
title: "DummyWheel/fr"
slug: "dummywheel"
lang: "fr"

source_wiki_title: "DummyWheel/fr"
source_hash: "93a7107f3d48c822760efa46cafc7f7b"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T06:11:17.838827+00:00"

tags:
  - software

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

Les roues factices (`dummy wheels`) sont présentes dans le dépôt de roues afin de fournir des substituts pour certains paquets Python populaires qui sont disponibles sur PyPI, mais qui sont plutôt offerts comme modules sur notre infrastructure. Elles sont toutes étiquetées avec une version locale (`dummy`), par exemple : `pyarrow-23.0.1+dummy.computecanada-py3-none-any.whl`.

Voici quelques exemples :
*   [pyarrow (Arrow)](arrow.md#pyarrow)
*   [opencv_python (OpenCV)](opencv.md#python-bindings)
*   [MPI4py](mpi4py.md)

Lorsqu'une roue factice est sélectionnée par `pip`, une erreur sera levée étant donné que `pip` n'a pas pu trouver de correspondance pour cette exigence.

## Dépannage
### Cette erreur est normale et est générée par cette roue factice.

!!! note "Note"
    Dans l'exemple ci-dessous, `pyarrow` est utilisé, mais la même logique s'applique aux autres paquets.

Lorsqu'une dépendance `pyarrow` n'est pas satisfaite, une erreur sera levée lorsque la roue factice est sélectionnée. **Ceci est normal**.
Cela signifie que :
1.  le module Arrow n'a pas été chargé; `pip` n'a donc pas pu trouver `pyarrow`
2.  la version d'Arrow chargée ne satisfait pas la version requise par le paquet dépendant
3.  le module Arrow chargé ne prend pas en charge la version de Python utilisée

#### Module non chargé
Dans ce cas, désactivez tout environnement virtuel, chargez le module, réactivez l'environnement virtuel et réexécutez votre commande `pip install`.

1.  Désactivez votre environnement virtuel Python.
    ```bash
    test $VIRTUAL_ENV && deactivate
    ```

2.  Chargez le module Arrow.
    ```bash
    module load gcc arrow/x.y.z python/x.y.z
    ```
    où `x.y.z` est la version requise.

3.  Réactivez votre environnement virtuel précédemment créé :
    ```bash
    source <env>/bin/activate
    ```

4.  Et réexécutez votre commande `pip install`.
    ```bash
    pip install <package>
    ```

#### Version du paquet ou du module
Le module Arrow chargé ne satisfait pas l'exigence. Par exemple, `(from pyarrow>=21.0.0->datasets)` signifie que cette version du paquet `datasets` requiert `pyarrow` d'une version supérieure ou égale à `21.0.0`.

En d'autres termes, l'utilisation de toute version antérieure avec cette version de `datasets` entraînera l'installation de la roue factice.

Vous pouvez trouver l'exigence (version) demandée en examinant la ligne (`pyarrow_noinstall`) :
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

Ou on peut vérifier si `pip` le détecte :
```bash
pip list | grep pyarrow
```
```text
pyarrow    23.0.0
```

Si `pip list` affiche une entrée, alors `pyarrow` est disponible et détecté par `pip`. Sinon, en l'absence d'entrée, `pyarrow` n'est pas disponible.