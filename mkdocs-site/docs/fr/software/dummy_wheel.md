---
title: "Dummy wheel/fr"
slug: "dummy_wheel"
lang: "fr"

source_wiki_title: "Dummy wheel/fr"
source_hash: "3ca14d31c228e2edb8c2ba6514d610d8"
last_synced: "2026-05-31T00:03:42.418098+00:00"
last_processed: "2026-05-31T01:00:08.609626+00:00"

tags:
  - software

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: true
  qa_generated: false
---

Un *wheel* factice est un *wheel* bidon, ou factice, qui remplace certains paquets Python populaires disponibles sur PyPI, mais qui fonctionnent comme des modules sur notre infrastructure. Ils sont tous étiquetés `dummy` avec une version locale, par exemple `pyarrow-23.0.1+dummy.computecanada-py3-none-any.whl`.

Voici quelques exemples :
*   [pyarrow (Arrow)](arrow.md#pyarrow)
*   [opencv_python (OpenCV)](opencv.md#interfaces-python)
*   [MPI4py](../programming/mpi4py.md)

# Dépannage

!!! note
    Dans le cas ci-dessous, `pyarrow` sert d'exemple, mais le résultat est le même pour d'autres paquets.

L'erreur suivante se produit quand pip sélectionne un *wheel* factice parce que pip ne lui trouve pas de correspondance.

## Ceci est une erreur normale générée par ce wheel factice.

Si la dépendance `pyarrow` n'est pas satisfaite, une erreur est générée lors de la sélection du *wheel* factice. Ceci est normal.
Les causes possibles sont :
1.  le module Arrow n'a pas été chargé et donc pip n'a pas pu trouver pyarrow;
2.  la version d'Arrow chargée ne correspond pas à la version requise par le paquet dépendant;
3.  le module Arrow chargé n'est pas compatible avec la version de Python utilisée.

### Module non chargé

Dans ce cas, désactivez l'environnement virtuel, chargez le module, réactivez l'environnement virtuel et relancez la commande `pip install`.

1.  Désactivez votre environnement virtuel.
    ```bash
    test $VIRTUAL_ENV && deactivate
    ```

2.  Chargez le module Arrow.
    ```bash
    module load gcc arrow/x.y.z python/x.y.z
    ```
    où `x.y.z` est la version requise.

3.  Réactivez l'environnement virtuel précédent.
    ```bash
    source <env>/bin/activate
    ```

4.  Lancez `pip install` de nouveau.
    ```bash
    pip install <package>
    ```

### Version du paquet/module

Le module Arrow chargé ne répond pas à l'exigence. Par exemple, `(from pyarrow>=21.0.0->datasets)` signifie que cette version du paquet d'ensembles de données exige une version de `pyarrow` supérieure ou égale à `21.0.0`.

Autrement dit, l'utilisation d'une version antérieure avec cette version des ensembles de données fera l'installation du *wheel* factice.

Vous pouvez trouver la version requise dans la ligne `pyarrow_noinstall`.
```bash
pip install --no-index datasets
```

```text
...
Processing /cvmfs/soft.computecanada.ca/custom/python/wheelhouse/generic/pyarrow_noinstall-9999+dummy.computecanada.tar.gz (from pyarrow>=21.0.0->datasets)
```

### Aucune interface (*binding*) Python

Le module chargé ne dispose peut-être pas les interfaces Python nécessaires.
Vous pouvez le vérifier rapidement avec
```bash
python -c "import pyarrow"
```
Si la commande ne retourne rien, l'importation a réussi et le module fournit `pyarrow` pour le module Python utilisé.

Vous pouvez aussi vérifier si pip le trouve.
```bash
pip list | grep pyarrow
```

```text
pyarrow    23.0.0
```

Si `pip list` affiche une entrée, alors `pyarrow` est disponible et visible par `pip`. S'il n'y a pas d'entrée, `pyarrow` n'est pas disponible.