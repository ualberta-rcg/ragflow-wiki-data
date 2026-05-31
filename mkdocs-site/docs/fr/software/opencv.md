---
title: "OpenCV/fr"
slug: "opencv"
lang: "fr"

source_wiki_title: "OpenCV/fr"
source_hash: "6ca9ffcca03ac7420bfdb2823b6090d4"
last_synced: "2026-05-31T00:03:42.418098+00:00"
last_processed: "2026-05-31T00:50:38.910466+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: true
  qa_generated: false
---

[La bibliothèque OpenCV](https://opencv.org/) (*Open Source Computer Vision*) est spécialisée dans le traitement d'images en temps réel.

## CUDA
OpenCV est également disponible avec CUDA.
```bash
module load gcc cuda opencv/X.Y.Z
```
où `X.Y.Z` désigne la version que vous souhaitez utiliser.

## Modules additionnels
Le module inclut également les [modules `contrib`](https://github.com/opencv/opencv_contrib/tree/4.x/modules#an-overview-of-the-opencv_contrib_modules).

## Interfaces Python
Le module inclut des interfaces (*bindings*) pour différentes versions de Python.
Pour connaître les interfaces compatibles avec votre version, lancez la commande suivante :
```bash
module spider opencv/X.Y.Z
```
ou recherchez directement *opencv_python* avec :
```bash
module spider opencv_python/X.Y.Z
```
où `X.Y.Z` représente la version désirée.

### Utilisation
1. Chargez les modules requis.
```bash
module load gcc opencv/X.Y.Z python scipy-stack
```
où `X.Y.Z` représente la version désirée.

2. Importez OpenCV.
```bash
python -c "import cv2"
```
L’importation est considérée comme réussie si aucune sortie n’est affichée.

#### Paquets Python disponibles
Pour être installés, certains paquets Python nécessitent une interface OpenCV. Le module propose les paquets OpenCV suivants :
* `opencv_python`
* `opencv_contrib_python`
* `opencv_python_headless`
* `opencv_contrib_python_headless`

```bash
pip list | grep opencv
```
Output :
```
opencv-contrib-python              4.5.5                  
opencv-contrib-python-headless     4.5.5                  
opencv-python                      4.5.5                  
opencv-python-headless             4.5.5 
```
Lorsque le module `opencv` est chargé, la dépendance envers OpenCV est résolue.

## Utilisation avec OpenEXR
Pour qu'OpenCV puisse lire des fichiers EXR, le module doit être activé via une variable d'environnement.
```bash
OPENCV_IO_ENABLE_OPENEXR=1 python <fichier>
```

# Dépannage

## Erreur normale générée par cette roue factice.
Veuillez consulter [la page Dummy wheel](dummy_wheel.md).

## ModuleNotFoundError: Aucun module nommé 'cv2'
Une erreur peut survenir lors de l'importation de `cv2`.
```bash
python -c "import cv2"
```
Output :
```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'cv2'
```
Ceci se produit généralement dans l'un des cas suivants :
1. [Un module OpenCV n'est pas chargé](opencv.md),
2. [Un module Python n'est pas chargé](opencv.md).

### Module OpenCV pas chargé
Chargez un module `OpenCV` compatible (veuillez consulter les [Interfaces Python](opencv.md#interfaces-python)).

### Module Python pas chargé
Lorsqu'un module Python n'est pas chargé et qu'un environnement virtuel est actif, les *bindings* Python ne sont pas disponibles, et par conséquent `cv2` n'est pas visible.

!!! solution "Solution"
    1. Désactivez l'environnement virtuel Python.
    ```bash
    test $VIRTUAL_ENV && deactivate
    ```

!!! important "Remarque importante"
    Si un environnement virtuel est actif, il est essentiel de le désactiver avant de charger le module. Une fois le module chargé, vous pouvez réactiver l'environnement virtuel.

    2. Chargez le module.
    ```bash
    module load opencv/x.y.z python/x.y.z
    ```

    3. Vérifiez que le module est visible par `pip`.
    ```bash
    pip list | grep mpi4py
    ```
    Output :
    ```
    opencv_python            4.13.0
    ```
    et que le module Python que vous avez chargé y a accès.
    ```bash
    python -c 'import mpi4py'
    ```
    Si aucune erreur ne survient, cela indique que tout fonctionne correctement.