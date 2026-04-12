---
title: "RAPIDS/fr"
slug: "rapids"
lang: "fr"

source_wiki_title: "RAPIDS/fr"
source_hash: "df2edcb3c886ddfc16eefad3f64b9bba"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:57:13.083391+00:00"

tags:
  []

keywords:
  - "notebooks"
  - "image Apptainer"
  - "RAPIDS"
  - "documentation"
  - "Jupyter Notebook"
  - "accélération GPU"
  - "nœud de calcul"
  - "Submission script"
  - "NVIDIA"
  - "apptainer"
  - "science des données"
  - "bibliothèques Python"
  - "disque local"
  - "environnement RAPIDS"
  - "ordonnanceur"
  - "serveur Jupyter notebook"
  - "conteneur"
  - "RAPIDS Notebooks"
  - "mode interactif"
  - "SLURM"
  - "nœud GPU"
  - "Apptainer"

questions:
  - "Quel est l'objectif principal de la suite de logiciels RAPIDS développée par NVIDIA ?"
  - "Quels sont les rôles spécifiques des différentes composantes incluses dans RAPIDS, telles que cuDF, cuML et cuGraph ?"
  - "Comment peut-on trouver et sélectionner les images Docker appropriées pour créer une image Apptainer pour RAPIDS ?"
  - "Comment construire une image Apptainer pour RAPIDS à partir d'une image Docker et quelles sont les contraintes de ressources à prévoir ?"
  - "Quelles sont les étapes pour démarrer une session interactive sur un nœud GPU, y lier le périphérique matériel et lancer un serveur Jupyter Notebook ?"
  - "Quelle est la bonne pratique recommandée pour la gestion du stockage lors de la soumission d'une tâche RAPIDS à l'ordonnanceur via un script ?"
  - "À quoi sert l'environnement RAPIDS de base décrit dans le texte ?"
  - "Quels éléments spécifiques sont ajoutés à l'image de base par la version \"RAPIDS Notebooks\" ?"
  - "Dans quel cas d'usage et pour quel mode de travail est-il recommandé d'utiliser l'image \"RAPIDS Notebooks\" ?"
  - "Quel espace de stockage temporaire est recommandé pour copier l'image du conteneur et les données sur un nœud de calcul ?"
  - "Quelles sont les ressources matérielles spécifiques (GPU, CPU, mémoire) demandées dans le script de soumission Slurm ?"
  - "Quel module logiciel doit être chargé dans le script pour pouvoir utiliser et gérer les conteneurs ?"
  - "Comment doit-on configurer et exécuter une tâche RAPIDS avec Apptainer dans un environnement SLURM ?"
  - "Quelle est la procédure à suivre pour la gestion des fichiers de données et la sauvegarde des résultats lors de l'exécution du script ?"
  - "Quelles sont les ressources externes recommandées pour consulter la documentation, trouver des exemples de code et lire des cas d'usage sur RAPIDS ?"
  - "Comment doit-on configurer et exécuter une tâche RAPIDS avec Apptainer dans un environnement SLURM ?"
  - "Quelle est la procédure à suivre pour la gestion des fichiers de données et la sauvegarde des résultats lors de l'exécution du script ?"
  - "Quelles sont les ressources externes recommandées pour consulter la documentation, trouver des exemples de code et lire des cas d'usage sur RAPIDS ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Description

[RAPIDS](https://rapids.ai/) est une suite de bibliothèques logicielles *open source* de NVIDIA qui sert principalement à l'exécution de pipelines d'analyse et de science des données en Python avec des GPU. La suite s'appuie sur CUDA pour l'optimisation des calculs de bas niveau et fournit des API Python conviviales, semblables à celles de Pandas ou Scikit-learn.

Les principales composantes sont :

*   **cuDF** : bibliothèque Python de trames de données GPU (basée sur le format Apache Arrow en colonnes) pour le chargement, la fusion, l'agrégation, la sélection et autres manipulations des données.
*   **cuML** : suite de bibliothèques pour l'implémentation d'algorithmes d'apprentissage automatique et de fonctions primitives, permettant le partage d'API compatibles avec d'autres projets RAPIDS.
*   **cuGraph** : bibliothèque pour l'analyse de graphiques accélérée par GPU, offrant une fonctionnalité similaire à NetworkX et étant parfaitement intégrée à la plateforme [de science des données] RAPIDS.
*   **Accélérateurs de journaux cyber (CLX ou « clicks »)** : collection d'exemples RAPIDS dans les domaines de la sécurité, de la science des données et du génie, permettant d'appliquer rapidement RAPIDS et l'accélération GPU à des cas concrets de cybersécurité.
*   **cuxFilter** : bibliothèque de connecteurs pour relier facilement des bibliothèques de visualisation et des trames de données GPU, permettant également d'utiliser des graphiques interactifs provenant de différentes bibliothèques dans le même tableau de bord.
*   **cuSpatial** : bibliothèque C++/Python avec accélération GPU pour les systèmes d'information géographique incluant la recherche de points à l'intérieur d'un polygone, les jointures spatiales, les systèmes de coordonnées, les primitives de forme, les distances et l'analyse de trajectoires.
*   **cuSignal** : accélération GPU dans le traitement des signaux avec CuPy, Numba et l'écosystème RAPIDS. Dans certains cas, cuSignal est un port direct de Scipy Signal pour utiliser les ressources de calcul via CuPy, mais il contient également des noyaux Numba CUDA pour une accélération accrue de certaines fonctions.
*   **cuCIM** : boîte à outils extensible pour l'accélération GPU des entrées/sorties, la vision par ordinateur et le traitement des primitives, principalement dans le domaine de l'imagerie médicale.
*   **RAPIDS Memory Manager (RMM)** : outil de gestion des allocations de mémoire pour cuDF (C++ et Python) et les autres bibliothèques RAPIDS. RMM gère également le remplacement des allocations de mémoire CUDA et de la mémoire des périphériques CUDA, et effectue rapidement les allocations et désallocations de manière asynchrone en réservant une quantité définie de mémoire.

## Images Apptainer

Pour créer une image Apptainer (auparavant [Singularity](../containers/apptainer.md)) pour RAPIDS, il faut d'abord trouver et choisir une image Docker fournie par NVIDIA.

### Trouver une image Docker

À compter de RAPIDS v23.08, les deux types d'images Docker pour RAPIDS sont *base* et *notebooks*. Pour chaque type, plusieurs images sont fournies pour les différentes combinaisons des versions de RAPIDS et de CUDA ainsi que plusieurs versions de Python. Pour trouver une image en particulier, allez à l'onglet **Tags** de chacun des sites.

*   [RAPIDS Base](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/rapidsai/containers/base) : contient un environnement RAPIDS prêt à l'emploi pour soumettre une tâche à l'ordonnanceur.
*   [RAPIDS Notebooks](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/rapidsai/containers/notebooks) : ajoute à l'image Base un serveur Jupyter Notebook et des exemples de notebooks. Utilisez ce type d'image pour travailler en mode interactif avec des notebooks et des exemples.

### Construire une image Apptainer

Par exemple, la balise d'une image Docker pour RAPIDS est la suivante :

```bash
nvcr.io/nvidia/rapidsai/notebooks:25.04-cuda12.0-py3.12
```

Avec un ordinateur qui prend en charge Apptainer, vous pouvez créer une image Apptainer (ici, `rapids.sif`) avec la commande suivante :

```bash
[name@server ~]$ apptainer build rapids.sif docker://nvcr.io/nvidia/rapidsai/notebooks:25.04-cuda12.0-py3.12
```

Le processus prend habituellement de 30 à 60 minutes. Étant donné que la taille de l'image est importante, assurez-vous d'avoir suffisamment de mémoire et d'espace disque sur le serveur.

## Utilisation sur une grappe

Une fois que vous avez une image Apptainer pour RAPIDS sur l'une de nos grappes, vous pouvez demander une session interactive sur un nœud GPU ou soumettre une tâche par lots à l'ordonnanceur lorsque votre code RAPIDS est prêt.

### Travailler en mode interactif sur un nœud GPU

Si l'image Apptainer a été construite avec une image Docker de type notebooks, elle inclut un serveur Jupyter Notebook et peut être utilisée pour explorer RAPIDS en mode interactif sur un nœud de calcul GPU.
Pour demander une session interactive sur un nœud de calcul GPU, par exemple :

```bash
[name@cluster-login ~]$ salloc --ntasks=1 --cpus-per-task=2 --mem=10G --gpus-per-node=1 --time=1:0:0 --account=def-someuser
```

Lorsque la ressource est allouée, lancez l'interpréteur RAPIDS sur le nœud GPU avec la commande suivante :

```bash
[name@compute-node#### ~]$ module load apptainer
[name@compute-node#### ~]$ apptainer shell --nv rapids.sif
```

*   L'option `--nv` effectue le *montage de liaison* du périphérique GPU de l'hôte sur le conteneur afin que l'accès au GPU puisse se faire depuis l'intérieur du conteneur Apptainer.

Lorsque l'invite de l'interpréteur passe à `Apptainer>`, vous pouvez consulter les statistiques du GPU dans l'interpréteur pour vous assurer d'avoir accès au GPU.

```bash
Apptainer> nvidia-smi
```

Une fois l'invite passée à `Apptainer>`, vous pouvez lancer le serveur Jupyter Notebook dans l'environnement RAPIDS; ceci affichera l'URL du serveur.

```bash
Apptainer> jupyter-lab --ip $(hostname -f) --no-browser
```

!!! note
    À compter de la version 23.08, RAPIDS n'a pas besoin d'être activé après le démarrage de Conda, puisque tous les paquets sont inclus dans l'environnement Conda de base qui est activé par défaut. Par exemple, vous pouvez lancer le serveur Jupyter Notebook directement dans l'interpréteur du conteneur.

Si un nœud de calcul n'est pas connecté directement à Internet, il faut configurer un tunnel SSH pour effectuer la redirection de port entre votre ordinateur et le nœud GPU. Pour plus de détails, consultez [comment se connecter à Jupyter Notebook](../../getting-started/advanced_jupyter_configuration.md).

### Soumettre une tâche RAPIDS à l'ordonnanceur

Quand votre code RAPIDS est prêt, vous pouvez soumettre une tâche à l'ordonnanceur. La bonne pratique consiste à [utiliser le disque local](../../storage-and-data/using_node-local_storage.md) lorsque vous travaillez avec un conteneur sur un nœud de calcul.

### Script de soumission

!!! info "Fichier : `submit.sh`"

```sh
#!/bin/bash
#SBATCH --gpus-per-node=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=10G
#SBATCH --time=dd:hh:mm
#SBATCH --account=def-someuser

module load apptainer

# Copiez votre image de conteneur, votre code RAPIDS et vos données sur le disque local d'un nœud de calcul via $SLURM_TMPDIR

cd $SLURM_TMPDIR
cp /path/to/rapids.sif ./
cp /path/to/your_rapids_code.py ./
cp -r /path/to/your_datasets ./

apptainer exec --nv rapids.sif python ./my_rapids_code.py

# Sauvegardez les résultats dans votre dossier /project avant de terminer le travail.
cp -r your_results ~/projects/def-someuser/username/
```

## Références

*   [Documentation RAPIDS](https://docs.rapids.ai/) : documentation complète de RAPIDS, comment rester en contact et signaler les problèmes;
*   [Notebooks RAPIDS](https://github.com/rapidsai/notebooks) : exemples sur GitHub que vous pouvez utiliser;
*   [RAPIDS sur Medium](https://medium.com/rapids-ai) : cas d'utilisation et blogues.