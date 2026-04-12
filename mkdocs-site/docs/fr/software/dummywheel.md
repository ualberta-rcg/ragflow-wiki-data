---
title: "DummyWheel/fr"
slug: "dummywheel"
lang: "fr"

source_wiki_title: "DummyWheel/fr"
source_hash: "93a7107f3d48c822760efa46cafc7f7b"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:54:51.179255+00:00"

tags:
  - software

keywords:
  - "Dummy Wheel"
  - "pyarrow"
  - "python module"
  - "pip list"
  - "available"
  - "HTML"
  - "div"
  - "virtual environment"
  - "Python packages"
  - "markup"
  - "code"
  - "pip"
  - "closing tag"

questions:
  - "What is the purpose of a \"Dummy Wheel\" in the wheelhouse infrastructure?"
  - "What are the three main reasons why pip might select a dummy wheel and raise an error during package installation?"
  - "How can a user verify if the required module has the correct Python bindings and is recognized by pip?"
  - "What is the structural purpose of the `</div>` tag in the context of an HTML document?"
  - "What specific content or elements were intended to be enclosed before this closing tag?"
  - "How does the presence of this isolated closing tag affect the rendering or validation of the web page?"
  - "What specific command can be executed to verify if pip recognizes the pyarrow module?"
  - "How does the output of the pip list command indicate that the pyarrow module is successfully installed and available?"
  - "What conclusion can be drawn if the pip list command returns no entry for pyarrow?"
  - "What is the structural purpose of the `</div>` tag in the context of an HTML document?"
  - "What specific content or elements were intended to be enclosed before this closing tag?"
  - "How does the presence of this isolated closing tag affect the rendering or validation of the web page?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Les wheels factices sont présents dans l'entrepôt de wheels pour servir de substituts à certains paquets Python populaires qui sont disponibles sur PyPI, mais qui existent comme modules sur notre infrastructure. Ils sont tous étiquetés avec une version locale (`dummy`), par exemple : `pyarrow-23.0.1+dummy.computecanada-py3-none-any.whl`.

Des exemples incluent :
*   [pyarrow (Arrow)](arrow.md#pyarrow)
*   [opencv_python (OpenCV)](opencv.md#python-bindings)
*   [MPI4py](../programming/mpi4py.md)

Lorsqu'un wheel factice est sélectionné par pip, il lèvera l'erreur ci-dessous car pip n'a pas pu trouver de correspondance pour cette exigence.

# Dépannage
## Ceci est une erreur normale générée par ce wheel factice.

!!! note "Remarque"
    Dans le cas ci-dessous, `pyarrow` est utilisé comme exemple, mais la même chose s'applique à d'autres paquets également.

Lorsque la dépendance `pyarrow` n'est pas satisfaite, une erreur sera levée lorsque le wheel factice est sélectionné. **Ceci est normal**.
Cela signifie que soit :
1.  le module `arrow` n'a pas été chargé, par conséquent pip n'a pas pu trouver `pyarrow`
2.  la version d'Arrow chargée ne correspond pas à la version requise par le paquet dépendant
3.  le module Arrow chargé ne supporte pas la version Python utilisée

### Module non chargé
Dans ce cas, désactivez tout environnement virtuel, chargez le module, réactivez l'environnement virtuel, puis réexécutez votre commande d'installation pip.

1.  Désactivez votre environnement virtuel Python.
    ```bash
    test $VIRTUAL_ENV && deactivate
    ```

2.  Chargez le module Arrow.
    ```bash
    module load gcc arrow/x.y.z python/x.y.z
    ```
    où `x.y.z` est la version requise.

3.  Réactivez votre environnement virtuel créé précédemment :
    ```bash
    source <env>/bin/activate
    ```

4.  Et réexécutez votre commande d'installation pip.
    ```bash
    pip install <package>
    ```

### Version du paquet/module
Le module `arrow` chargé ne satisfait pas l'exigence. Par exemple, `(from pyarrow>=21.0.0->datasets)` signifie que cette version du paquet `datasets` requiert `pyarrow` supérieur ou égal à la version `21.0.0`.

Autrement dit, l'utilisation de toute version antérieure avec cette version de `datasets` entraînera l'installation du wheel factice.

Vous pouvez trouver l'exigence (version) demandée en examinant la ligne (`pyarrow_noinstall`) :
```bash
pip install --no-index datasets
...
Processing /cvmfs/soft.computecanada.ca/custom/python/wheelhouse/generic/pyarrow_noinstall-9999+dummy.computecanada.tar.gz (from pyarrow>=21.0.0->datasets)
```

### Pas de liaisons Python
Le module chargé pourrait ne pas avoir les liaisons Python pour le module Python utilisé.
Vous pouvez rapidement vérifier en utilisant :
```bash
python -c "import pyarrow"
```
Si la commande n'affiche rien, l'importation a réussi et le module fournit `pyarrow` pour le module Python utilisé.

Ou on peut vérifier si pip le détecte :
```bash
pip list | grep pyarrow
pyarrow    23.0.0
```
Si `pip list` affiche une entrée, alors `pyarrow` est disponible et détecté par `pip`. Autrement, en l'absence d'entrée, `pyarrow` n'est pas disponible.