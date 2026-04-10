---
title: "RAPIDS/fr"
slug: "rapids"
lang: "fr"

source_wiki_title: "RAPIDS/fr"
source_hash: "df2edcb3c886ddfc16eefad3f64b9bba"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T10:41:13.563313+00:00"

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

# Description

[RAPIDS](https://rapids.ai/) est une suite de bibliothèques de logiciels *libres* de NVIDIA qui sert principalement à l'exécution de pipelines de science des données et d'analyse en Python avec des GPU. La suite s'appuie sur CUDA pour l'optimisation des calculs de bas niveau et fournit des API Python conviviales semblables à celles de Pandas ou Scikit-learn.

Les principales composantes sont :

*   **cuDF** : bibliothèque Python de DataFrames GPU (selon le format en colonne Apache Arrow) pour le chargement, la fusion, l'agrégation, la sélection et autres manipulations des données.

*   **cuML** : suite de bibliothèques pour l’implémentation d’algorithmes d’apprentissage machine et de fonctions primitives, qui permet le partage d’API compatibles avec d’autres projets RAPIDS.

*   **cuGraph** : bibliothèque pour l’analyse de graphiques accélérée par GPU, qui offre une fonctionnalité semblable à NetworkX et est parfaitement intégrée à la plateforme de science des données RAPIDS.

*   **Cyber Log Accelerators (CLX ou *clicks*)** : collection d’exemples RAPIDS dans les domaines de la sécurité, la science des données et le génie, qui permet d’appliquer rapidement RAPIDS et l’accélération GPU à des cas concrets de cybersécurité.

*   **cuxFilter** : bibliothèque de connecteurs pour relier facilement des bibliothèques de visualisation et des DataFrames GPU et permet aussi d’utiliser interactivement des graphiques de différentes bibliothèques dans le même tableau de bord.

*   **cuSpatial** : bibliothèque C++/Python avec accélération GPU pour les systèmes d’information géographique incluant la recherche de points à l’intérieur d’un polygone, la jointure spatiale, les systèmes de coordonnées, les primitives de forme, les distances et l’analyse de trajectoires.

*   **cuSignal** : accélération GPU dans le traitement des signaux avec CuPy, Numba et l’écosystème RAPIDS. Dans certains cas, cuSignal est un port direct de Scipy Signal pour utiliser des ressources de calcul via CuPy, mais qui contient aussi des *kernels* Numba CUDA pour plus d’accélération à des fonctions sélectionnées.

*   **cuCIM** : boîte à outils extensible pour l’accélération GPU des entrées/sorties, la vision par ordinateur et le traitement des primitives, principalement dans le domaine de l’imagerie médicale.

*   **RAPIDS Memory Manager (RMM)** : outil de gestion des allocations de mémoire pour cuDF (C++ et Python) et les autres bibliothèques RAPIDS. RMM gère aussi le remplacement des allocations de mémoire CUDA et de la mémoire des périphériques CUDA et effectue rapidement les allocations et désallocations de manière asynchrone en réservant une quantité définie de mémoire.

# Images Apptainer

Pour créer une image Apptainer (auparavant [Singularity](singularity.md#utilisez-plutot-apptainer)) pour RAPIDS, il faut d’abord trouver et sélectionner une image Docker fournie par NVIDIA.

## Trouver une image Docker

À partir de RAPIDS v23.08, les deux types d’images Docker pour RAPIDS sont *de base* et *carnets Jupyter*. Pour chaque type, plusieurs images sont fournies pour les différentes combinaisons des versions de RAPIDS et de CUDA ainsi que plusieurs versions de Python. Pour trouver une image en particulier, allez sous l'onglet *Étiquettes* de chacun des sites.

*   [RAPIDS De base](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/rapidsai/containers/base) : contient un environnement RAPIDS prêt à être utilisé pour soumettre une tâche à l'ordonnanceur.
*   [RAPIDS Carnets Jupyter](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/rapidsai/containers/notebooks) : ajoute à l'image de base un serveur Jupyter Notebook et des exemples de carnets. Utilisez ce type d'image pour travailler en mode interactif avec des carnets Jupyter et des exemples.

## Construire une image Apptainer

Par exemple, l'étiquette d'une image Docker pour RAPIDS est

```bash
nvcr.io/nvidia/rapidsai/notebooks:25.04-cuda12.0-py3.12
```

Avec un ordinateur qui prend en charge Apptainer, vous pouvez construire une image Apptainer (ici *rapids.sif*) avec la commande suivante :

```bash
[name@server ~]$ apptainer build rapids.sif docker://nvcr.io/nvidia/rapidsai/notebooks:25.04-cuda12.0-py3.12
```

Le processus prend habituellement de 30 à 60 minutes. Puisque la taille de l’image est grande, assurez-vous que vous avez assez de mémoire et d’espace disque sur le serveur.

# Travailler sur une grappe

Une fois que vous avez une image Apptainer pour RAPIDS sur une de nos grappes, vous pouvez demander une session interactive sur un nœud GPU ou soumettre une tâche en lot à l'ordonnanceur quand votre code RAPIDS est prêt.

## Travailler interactivement sur un nœud GPU

Si l’image Apptainer a été construite avec une image Docker de type *carnets Jupyter*, elle inclut un serveur Jupyter Notebook et peut être employée pour explorer RAPIDS interactivement sur un nœud de calcul GPU.
Pour demander une session interactive sur un nœud de calcul GPU, par exemple :

```bash
[name@cluster-login ~]$ salloc --ntasks=1 --cpus-per-task=2 --mem=10G --gpus-per-node=1 --time=1:0:0 --account=def-someuser
```

Quand la ressource est allouée, lancez l’interpréteur de commandes RAPIDS sur le nœud GPU avec :

```bash
[name@compute-node#### ~]$ module load apptainer
[name@compute-node#### ~]$ apptainer shell --nv rapids.sif
```
*   l'option `--nv` fait le *montage liant* du périphérique GPU de l’hôte sur le conteneur pour que l’accès au GPU puisse se faire de l’intérieur du conteneur Apptainer.

Lorsque l’invite de l’interpréteur de commandes change pour `Apptainer>`, vous pouvez consulter les statistiques pour le GPU dans l'interpréteur pour vous assurer que vous avez accès au GPU.

```bash
Apptainer> nvidia-smi
```

Lorsque l’invite change pour `Apptainer>`, vous pouvez lancer le serveur Jupyter Notebook dans l’environnement RAPIDS; ceci affichera l’URL du serveur.

```bash
Apptainer> jupyter-lab --ip $(hostname -f) --no-browser
```

!!! note
    À partir de la version 23.08, RAPIDS n'a pas besoin d'être activé après que Conda ait démarré puisque tous les paquets sont inclus dans l'environnement Conda de base qui est activé par défaut; par exemple, vous pouvez lancer le serveur Jupyter Notebook dans l'interpréteur de commandes du conteneur.

Si un nœud de calcul n’est pas connecté directement à l’internet, il faut configurer un tunnel SSH pour faire la redirection de port entre votre ordinateur et le nœud GPU. Pour les détails, voyez [comment se connecter à Jupyter Notebook](advanced-jupyter-configuration.md#se-connecter-a-jupyterlab).

## Soumettre une tâche RAPIDS à l'ordonnanceur

Quand votre code RAPIDS est prêt, vous pouvez soumettre une tâche à l'ordonnanceur. La bonne pratique est [d'utiliser le disque local](using-node-local-storage.md) quand vous travaillez avec un conteneur sur un nœud de calcul.

### Script de soumission

```sh linenums="1" title="submit.sh"
#!/bin/bash
#SBATCH --gpus-per-node=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=10G
#SBATCH --time=dd:hh:mm
#SBATCH --account=def-someuser

module load apptainer

# copier votre image de conteneur, votre code RAPIDS et vos données vers le disque local sur un nœud de calcul via $SLURM_TMPDIR

cd $SLURM_TMPDIR
cp /path/to/rapids.sif ./
cp /path/to/your_rapids_code.py ./
cp -r /path/to/your_datasets ./

apptainer exec --nv rapids.sif python ./my_rapids_code.py

# sauvegarder tous les résultats dans votre /project avant de terminer la tâche
cp -r your_results ~/projects/def-someuser/username/
```

# Références

*   [Documentation RAPIDS](https://docs.rapids.ai/) : documentation complète pour RAPIDS, comment rester en contact et rapporter les problèmes;
*   [Carnets Jupyter RAPIDS](https://github.com/rapidsai/notebooks) : exemples sur GitHub que vous pouvez utiliser;
*   [RAPIDS sur Medium](https://medium.com/rapids-ai/) : cas d’usage et blogues.