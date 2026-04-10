---
title: "OpenCV/fr"
slug: "opencv"
lang: "fr"

source_wiki_title: "OpenCV/fr"
source_hash: "7c2478f2b64108f15ab708d583ba3eee"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T09:31:30.371573+00:00"

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

[La bibliothèque OpenCV](https://opencv.org/) (*Open Source Computer Vision*) est spécialisée dans le traitement d'images en temps réel.

## CUDA
OpenCV est aussi disponible avec CUDA.

```bash
module load gcc cuda opencv/X.Y.Z
```

où `X.Y.Z` désigne la version choisie.

## Modules additionnels
Le module contient aussi les [modules `contrib`](https://github.com/opencv/opencv_contrib/tree/4.x/modules#an-overview-of-the-opencv_contrib-modules).

## Interfaces Python
Le module contient des interfaces pour plusieurs versions de Python.
Pour connaître les interfaces compatibles avec votre version, lancez

```bash
module spider opencv/X.Y.Z
```

ou cherchez directement *opencv_python* avec

```bash
module spider opencv_python/X.Y.Z
```

où `X.Y.Z` désigne la version choisie.

### Utilisation
1. Chargez les modules requis.
   ```bash
   module load gcc opencv/X.Y.Z python scipy-stack
   ```
   où `X.Y.Z` désigne la version choisie.

2. Importez OpenCV.
   ```bash
   python -c "import cv2"
   ```
   L’importation est réussie si rien n’est affiché.

#### Paquets Python disponibles
Pour être installés, certains paquets Python exigent une interface OpenCV. Le module offre les paquets OpenCV suivants :
*   `opencv_python`
*   `opencv_contrib_python`
*   `opencv_python_headless`
*   `opencv_contrib_python_headless`

```bash
pip list | grep opencv
```

```text
opencv-contrib-python              4.5.5
opencv-contrib-python-headless     4.5.5
opencv-python                      4.5.5
opencv-python-headless             4.5.5
```

Quand le module `opencv` est chargé, la dépendance envers OpenCV est satisfaite.

## Utilisation avec OpenEXR
Pour que OpenCV puisse lire des fichiers EXR, le module doit être activé via une variable d'environnement.

```bash
OPENCV_IO_ENABLE_OPENEXR=1 python <fichier>
```

## Dépannage

## Il s'agit d'une erreur normale générée par cette roue factice.
Consultez [Il s'agit d'une erreur normale générée par cette roue factice](dummywheel.md#il-sagit-dune-erreur-normale-generée-par-cette-roue-factice).

## ModuleNotFoundError: Aucun module nommé 'cv2'
Lors de l'importation de `cv2`, l'erreur suivante peut survenir :

```bash
python -c "import cv2"
```

```text
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'cv2'
```

Ceci signifie généralement l'un des deux cas suivants :
1.  [Un module OpenCV n'a pas été chargé](#module-opencv-non-charge)
2.  [Un module Python n'a pas été chargé](#module-python-non-charge)

### Module OpenCV non chargé
Trouvez un module `OpenCV` *compatible* et chargez-le. Référez-vous à [interfaces Python](#interfaces-python).

### Module Python non chargé
Si vous omettez de charger un module Python et que vous activez un environnement virtuel, les interfaces Python ne seront pas disponibles, ce qui entraînera l'absence de `cv2`.

**Solutions**

1.  Désactivez tout environnement virtuel Python.
    ```bash
    test $VIRTUAL_ENV && deactivate
    ```

    !!! note "Remarque"
        Si un environnement virtuel est actif, il est important de le désactiver avant de charger le module. Une fois le module chargé, activez à nouveau votre environnement virtuel.

2.  Chargez le module.
    ```bash
    module load opencv/x.y.z python/x.y.z
    ```

3.  Vérifiez que le module est visible par `pip`
    ```bash
    pip list | grep mpi4py
    ```

    ```text
    opencv_python            4.13.0
    ```
    et que le module Python que vous avez chargé y a accès.

    ```bash
    python -c 'import mpi4py'
    ```
    Si aucune erreur ne survient, tout va bien.