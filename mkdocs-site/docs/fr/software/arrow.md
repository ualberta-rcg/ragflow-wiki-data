---
title: "Arrow/fr"
slug: "arrow"
lang: "fr"

source_wiki_title: "Arrow/fr"
source_hash: "786f7008a29759098f66f6c2112227f9"
last_synced: "2026-05-31T00:03:42.418098+00:00"
last_processed: "2026-05-31T00:41:43.607366+00:00"

tags:
  - software
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

[Apache Arrow](https://arrow.apache.org/) est une plateforme de développement multilingue pour la gestion des données en mémoire. Elle utilise un format standardisé en colonnes qui organise les données hiérarchiques ou autres afin de permettre des opérations analytiques efficaces. La plateforme offre des bibliothèques de calcul, la transmission sans copie et en continu des données et la communication interprocessus. Parmi les langages pris en charge, on compte C, C++, C#, Go, Java, JavaScript, MATLAB, Python, R, Ruby et Rust.

## CUDA

Arrow est aussi disponible avec CUDA.

```bash
module load gcc arrow/X.Y.Z cuda
```

où X.Y.Z désigne la version.

## Interfaces Python

Le module contient des interfaces pour plusieurs versions de Python. Pour connaître les versions compatibles, lancez

```bash
module spider arrow/X.Y.Z
```

où X.Y.Z désigne la version.

Ou cherchez *pyarrow* directement avec

```bash
module spider pyarrow
```

### PyArrow

Les interfaces Python (appelées *PyArrow*) s’intègrent avec les objets de première classe NumPy, Pandas, et les objets natifs Python. Elles sont basées sur l'implémentation C++ de Arrow.

1.  Chargez les modules requis.

    ```bash
    module load gcc arrow/X.Y.Z python/3.11
    ```

    où X.Y.Z désigne la version.

2.  Importez PyArrow.

    ```bash
    python -c "import pyarrow"
    ```

    L’importation est réussie si rien n’est affiché.

Pour plus d'information, consultez [la documentation Python](https://arrow.apache.org/docs/python/).

#### Autres paquets Python dépendants

L'installation de certains paquets Python dépend de PyArrow.
Une fois le module `arrow` chargé, la dépendance à `pyarrow` sera satisfaite.

```bash
pip list | grep pyarrow
```

```text
pyarrow    17.0.0
```

Si `pip list` affiche une entrée, alors `pyarrow` est disponible et visible par `pip`. S'il n'y a pas d'entrée, `pyarrow` n'est pas disponible.

#### Format Apache Parquet

Le format de fichier [Parquet](http://parquet.apache.org/) est disponible.

Pour importer le module Parquet, effectuez les étapes pour `pyarrow` ci-dessus et lancez ensuite

```bash
python -c "import pyarrow.parquet"
```

L’importation est réussie si rien n’est affiché.

## Interfaces R

Arrow possède une interface avec la bibliothèque Arrow C++ pour permettre l'accès en R à plusieurs de ses fonctionnalités. Ceci inclut l’analyse de grands ensembles de données multifichiers ([open_dataset()](https://arrow.apache.org/docs/r/reference/open_dataset.html)); la capacité de travailler avec des fichiers individuels de format Parquet ([read_parquet()](https://arrow.apache.org/docs/r/reference/read_parquet.html), [write_parquet()](https://arrow.apache.org/docs/r/reference/write_parquet.html)) et Feather ([read_feather()](https://arrow.apache.org/docs/r/reference/read_feather.html), [write_feather()](https://arrow.apache.org/docs/r/reference/write_feather.html)); l'accès à la mémoire et aux messages Arrow.

### Installation

1.  Chargez les modules requis.

    ```bash
    module load StdEnv/2020 gcc/9.3.0 arrow/8 r/4.1 boost/1.72.0
    ```

2.  Spécifiez le répertoire d’installation local.

    ```bash
    mkdir -p ~/.local/R/$EBVERSIONR/
    export R_LIBS=~/.local/R/$EBVERSIONR/
    ```

3.  Exportez les variables requises pour vous assurer d’utiliser l'installation du système.

    ```bash
    export PKG_CONFIG_PATH=$EBROOTARROW/lib/pkgconfig
    export INCLUDE_DIR=$EBROOTARROW/include
    export LIB_DIR=$EBROOTARROW/lib
    ```

4.  Installez les interfaces.

    ```bash
    R -e 'install.packages("arrow", repos="https://cloud.r-project.org/")'
    ```

### Utilisation

Une fois les interfaces installées, il faut les charger.

1.  Chargez les modules requis.

    ```bash
    module load StdEnv/2020 gcc/9.3.0 arrow/8 r/4.1
    ```

2.  Chargez la bibliothèque.

    ```bash
    R -e "library(arrow)"
    ```

    ```text
    > library("arrow")
    Attaching package: ‘arrow’
    ```

Pour plus d'information, consultez la [documentation Arrow sur R](https://arrow.apache.org/docs/r/index.html).

## Dépannage

## Ceci est une erreur normale générée par cette roue factice.

Voir [la page Dummy wheel](dummy_wheel.md).

## Erreur : ModuleNotFoundError: No module named 'pyarrow'

Une erreur peut survenir à l'importation de `pyarrow`.

```bash
python -c "import pyarrow"
```

```text
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'pyarrow'
```

Ceci se produit habituellement dans l'un ou l'autre cas suivant :

1.  [un module Arrow n'est pas chargé](#module-arrow-non-charge),
2.  [un module Python n'est pas chargé](#module-python-non-charge).

### Module Arrow non chargé

Chargez un module `arrow` compatible (voir [PyArrow](#pyarrow)).

### Module Python non chargé

Quand un module Python n'est pas chargé et qu'un environnement virtuel est activé, les interfaces Python ne sont pas disponibles et donc `pyarrow` n'est pas visible.

!!! tip "Solution"

1.  Désactivez l'environnement virtuel Python.

    ```bash
    test $VIRTUAL_ENV && deactivate
    ```

    !!! note "Remarque"
        Si un environnement virtuel est actif, il est important de le désactiver avant de charger le module. Une fois le module chargé, activez à nouveau l'environnement virtuel.

2.  Chargez le module.

    ```bash
    module load arrow/x.y.z python/x.y.z
    ```

3.  Vérifiez que le module est visible par `pip`.

    ```bash
    pip list | grep pyarrow
    ```

    ```text
    pyarrow            23.0.1
    ```

    et que le module Python que vous avez chargé lui a accès.

    ```bash
    python -c 'import pyarrow'
    ```

    Si aucune erreur ne survient, tout va bien.