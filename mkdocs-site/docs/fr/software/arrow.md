---
title: "Arrow/fr"
slug: "arrow"
lang: "fr"

source_wiki_title: "Arrow/fr"
source_hash: "8ff0cb3168edb4fab99c1bbee2e4e511"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T04:40:16.983004+00:00"

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
  ragflow_synced: false
  qa_generated: false
---

[Apache Arrow](https://arrow.apache.org/) est une plateforme de développement multilangage pour la gestion des données en mémoire. Elle utilise un format standardisé en colonnes qui organise les données hiérarchiques ou autres afin de permettre des opérations analytiques efficaces. La plateforme offre des bibliothèques de calcul, la transmission sans copie et en continu des données et la communication interprocessus. Parmi les langages pris en charge, on compte C, C++, C#, Go, Java, JavaScript, MATLAB, Python, R, Ruby et Rust.

## CUDA
Arrow est aussi disponible avec CUDA.

```bash
module load gcc arrow/X.Y.Z cuda
```

où X.Y.Z désigne la version.

## Liaisons Python
Le module contient des *liaisons* pour plusieurs versions de Python. Pour connaître les versions compatibles, lancez

```bash
module spider arrow/X.Y.Z
```

où X.Y.Z désigne la version.

Ou cherchez *pyarrow* directement avec

```bash
module spider pyarrow
```

### PyArrow
Les *liaisons* Python (appelées *PyArrow*) s’intègrent avec les objets de première classe NumPy, Pandas, et les objets natifs Python. Elles sont basées sur l'implémentation C++ de Arrow.

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
L'installation de certains paquets Python est dépendante de PyArrow.
Une fois le module `arrow` chargé, la dépendance à `pyarrow` sera satisfaite.

```bash
pip list | grep pyarrow
```

```text
pyarrow    17.0.0
```

!!! note
    Si la commande `pip list` affiche une entrée, alors `pyarrow` est disponible et reconnu par `pip`. Sinon, si aucune entrée n'est affichée, `pyarrow` n'est pas disponible.

#### Format Apache Parquet
Le format de fichier [Parquet](http://parquet.apache.org/) est disponible.

Pour importer le module Parquet, effectuez les étapes pour `pyarrow` ci-dessus et lancez ensuite

```bash
python -c "import pyarrow.parquet"
```

L’importation est réussie si rien n’est affiché.

## Liaisons R
Arrow possède une interface avec la bibliothèque Arrow C++ pour permettre l'accès en R de plusieurs de ses fonctionnalités. Ceci inclut l’analyse de grands ensembles de données multifichiers ([open_dataset()](https://arrow.apache.org/docs/r/reference/open_dataset.html)); la capacité de travailler avec des fichiers individuels de format Parquet ([read_parquet()](https://arrow.apache.org/docs/r/reference/read_parquet.html), [write_parquet()](https://arrow.apache.org/docs/r/reference/write_parquet.html)) et Feather ([read_feather()](https://arrow.apache.org/docs/r/reference/read_feather.html), [write_feather()](https://arrow.apache.org/docs/r/reference/write_feather.html)); l'accès à la mémoire et aux messages Arrow.

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

4.  Installez les *liaisons*.

    ```bash
    R -e 'install.packages("arrow", repos="https://cloud.r-project.org/")'
    ```

### Utilisation
Une fois les *liaisons* installées, il faut les charger.

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

# Dépannage

## Ceci est une erreur normale générée par cette roue factice.
Voir [Ceci est une erreur normale générée par cette roue factice.](dummy-wheel.md#ceci-est-une-erreur-normale-generee-par-cette-roue-factice).

## ModuleNotFoundError : Aucun module nommé 'pyarrow'
Lors de l'importation de `pyarrow`, l'erreur suivante peut survenir :

```bash
python -c "import pyarrow"
```

```text
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'pyarrow'
```

Cela signifie généralement l'un des deux cas suivants :
1.  [Le module Arrow n'est pas chargé](#le-module-arrow-nest-pas-charge)
2.  [Le module Python n'est pas chargé](#le-module-python-nest-pas-charge)

### Le module Arrow n'est pas chargé
Trouvez un module `arrow` *compatible* et chargez-le. Voir [PyArrow](#pyarrow).

### Le module Python n'est pas chargé
Si vous omettez de charger un module Python et que vous activez un environnement virtuel, les liaisons Python ne seront pas disponibles, ce qui fera en sorte que `pyarrow` ne sera pas reconnu.

Pour y remédier :

1.  Désactivez tout environnement virtuel Python.

    ```bash
    test $VIRTUAL_ENV && deactivate
    ```

    !!! note
        Si vous aviez un environnement virtuel activé, il est important de le désactiver en premier, puis de charger le module, avant de réactiver votre environnement virtuel.

2.  Chargez le module.

    ```bash
    module load arrow/x.y.z python/x.y.z
    ```

3.  Vérifiez qu'il est visible par `pip`

    ```bash
    pip list | grep pyarrow
    ```

    ```text
    pyarrow            23.0.1
    ```

    et qu'il est accessible pour votre module Python actuellement chargé.

    ```bash
    python -c 'import pyarrow'
    ```

    Si aucune erreur n'est affichée, alors tout est en ordre!