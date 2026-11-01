---
title: "RAPIDS/fr"
slug: "rapids"
lang: "fr"

source_wiki_title: "RAPIDS/fr"
source_hash: "890189491c881135fbcaf795b668b432"
last_synced: "2026-11-01T01:58:40.824100+00:00"
last_processed: "2026-11-01T02:33:34.395257+00:00"

tags:
  []

keywords:
  - "image RAPIDS"
  - "nœud GPU"
  - "RAPIDS Notebooks"
  - "serveur Jupyter Notebook"
  - "soumettre une tâche à l'ordonnanceur"
  - "cp -r"
  - "RAPIDS Docs"
  - "SLURM_TMPDIR"
  - "cuDF"
  - "apptainer exec --nv"
  - "ordonnanceur"
  - "Apptainer"
  - "cuGraph"
  - "RAPIDS Base"
  - "directives SBATCH"
  - "disque local"
  - "cuML"
  - "script de soumission"
  - "rapids.sif"
  - "$SLURM_TMPDIR"
  - "apptainer"
  - "serveur Jupyter notebook"
  - "RAPIDS"
  - "GPU"
  - "environnement RAPIDS"

questions:
  - "Quels sont les principaux modules de la suite RAPIDS et quelles fonctions offrent-ils pour le traitement des données sur GPU ?"
  - "Comment créer une image Apptainer pour RAPIDS et quelles sont les différences entre les images Docker « base » et « notebooks » proposées par NVIDIA ?"
  - "Où peut‑on consulter les dernières informations et mises à jour concernant RAPIDS ?"
  - "Quelle commande permet de construire une image Apptainer à partir d’une image Docker RAPIDS et quels sont les prérequis en termes de mémoire et d’espace disque ?"
  - "Comment lancer une session interactive sur un nœud GPU avec Apptainer, vérifier l’accès au GPU et démarrer le serveur Jupyter Notebook ?"
  - "Quelles sont les bonnes pratiques et les étapes essentielles pour soumettre un script RAPIDS à l’ordonnanceur en utilisant le stockage local du nœud ?"
  - "Quel est le rôle du conteneur **RAPIDS Base** et comment permet‑il de soumettre une tâche à l’ordonnanceur ?"
  - "En quoi le conteneur **RAPIDS Notebooks** diffère‑t‑il de l’image Base et quelles fonctionnalités supplémentaires il apporte ?"
  - "Comment doit‑on choisir entre l’image Base et l’image Notebooks selon qu’on souhaite travailler en mode batch ou en mode interactif avec des notebooks ?"
  - "Pourquoi est‑il conseillé d’utiliser le disque local ($SLURM_TMPDIR) lorsqu’on exécute un conteneur sur un nœud de calcul ?"
  - "Quels paramètres SLURM sont définis dans le script de soumission et quelle est leur fonction ?"
  - "Comment le script copie‑t‑il l’image du conteneur et le code/données RAPIDS vers le disque local du nœud ?"
  - "Comment copier les fichiers (le conteneur .sif, le script Python et les jeux de données) dans le répertoire temporaire $SLURM_TMPDIR avant d’exécuter le job ?"
  - "Quelle commande utilise apptainer pour lancer le script my_rapids_code.py à l’intérieur du conteneur rapids.sif avec le support GPU ?"
  - "Où faut‑il transférer les résultats générés avant de terminer le job afin qu’ils soient conservés dans le répertoire de projet ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# RAPIDS

## Description

[RAPIDS](https://rapids.ai/) est une suite de bibliothèques de logiciels *open source* de NVIDIA qui sert principalement à l'exécution de pipelines de science des données et d'analyse en Python avec des GPU. La suite s'appuie sur CUDA pour l'optimisation des calculs de bas niveau et fournit des API Python conviviales semblables à celles de Pandas ou Scikit-learn.

Les principales composantes sont :

*   **cuDF** : bibliothèque Python de DataFrames GPU (selon le format en colonne Apache Arrow) pour le chargement, la fusion, l'agrégation, la sélection et autres manipulations des données.
*   **cuML** : suite de bibliothèques pour l’implémentation d’algorithmes d’apprentissage machine et de fonctions primitives, qui permet le partage d’API compatibles avec d’autres projets RAPIDS.
*   **cuGraph** : bibliothèque pour l’analyse de graphiques accélérée par GPU, qui offre une fonctionnalité semblable à NetworkX et est parfaitement intégrée à la plateforme RAPIDS [de science des données].
*   **Cyber Log Accelerators (CLX ou *clicks*)** : collection d’exemples RAPIDS dans les domaines de la sécurité, la science des données et le génie, qui permet d’appliquer rapidement RAPIDS et l’accélération GPU à des cas concrets de cybersécurité.
*   **cuxFilter** : bibliothèque de connecteurs pour relier facilement des bibliothèques de visualisation et des DataFrames GPU et permet aussi d’utiliser interactivement des graphiques de différentes bibliothèques dans le même tableau de bord.
*   **cuSpatial** : bibliothèque C++/Python avec accélération GPU pour les systèmes d’information géographique incluant la recherche de points à l’intérieur d’un polygone, la jointure spatiale, les systèmes de coordonnées, les primitives de forme, les distances et l’analyse de trajectoires.
*   **cuSignal** : accélération GPU dans le traitement des signaux avec CuPy, Numba et l’écosystème RAPID. Dans certains cas, cuSignal est un port direct de Scipy Signal pour utiliser des ressources de calcul via CuPy, mais qui contient aussi des kernels Numba CUDA pour plus d’accélération à des fonctions sélectionnées.
*   **cuCIM** : boîte à outils extensible pour l’accélération GPU des entrées/sorties, la vision par ordinateur et le traitement des primitives, principalement dans le domaine de l’imagerie médicale.
*   **RAPIDS Memory Manager (RMM)** : outil de gestion des allocations de mémoire pour cuDF (C++ et Python) et les autres bibliothèques RAPIDS. RMM gère aussi le remplacement des allocations de mémoire CUDA et de la mémoire des périphériques CUDA et effectue rapidement les allocations et désallocations de manière asynchrone en réservant une quantité définie de mémoire.

!!! note "Remarque"
    Pour connaître les informations et les modifications les plus récentes, voir [RAPIDS Notices](https://docs.nvidia.com/datascience/notices/) (en anglais).

## Images Apptainer

Pour créer une image Apptainer (auparavant [Singularity](../containers/apptainer.md)) pour RAPIDS, il faut d’abord trouver et sélectionner une image Docker fournie par NVIDIA.

### Trouver une image Docker

À partir de RAPIDS v23.08, les deux types d’images Docker pour RAPIDS sont *base* et *notebooks*. Pour chaque type, plusieurs images sont fournies pour les différentes combinaisons des versions de RAPIDS et de CUDA ainsi que plusieurs versions de Python. Pour trouver une image en particulier, allez sous l'onglet *Tags* de chacun des sites.

*   [RAPIDS Base](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/rapidsai/containers/base) : contient un environnement RAPIDS prêt à être utilisé pour soumettre une tâche à l'ordonnanceur.
*   [RAPIDS Notebooks](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/rapidsai/containers/notebooks) : ajoute à l'image Base un serveur Jupyter notebook et des exemples de notebooks. Utilisez ce type d'image pour travailler en mode interactif avec des notebooks et des exemples.

### Construire une image Apptainer

Par exemple, le tag d'une image Docker pour RAPIDS est :

```bash
nvcr.io/nvidia/rapidsai/notebooks:25.04-cuda12.0-py3.12
```

Avec un ordinateur qui prend en charge Apptainer, vous pouvez construire une image Apptainer (ici *rapids.sif*) avec la commande suivante :

```bash
[name@server ~]$ apptainer build rapids.sif docker://nvcr.io/nvidia/rapidsai/notebooks:25.04-cuda12.0-py3.12
```

Le processus prend habituellement de 30 à 60 minutes. Puisque la taille de l’image est grande, assurez-vous que vous avez assez de mémoire et d’espace disque sur le serveur.

## Travailler sur une grappe

Une fois que vous avez une image Apptainer pour RAPIDS sur une de nos grappes, vous pouvez demander une session interactive sur un nœud GPU ou soumettre une tâche en lot à l'ordonnanceur quand votre code RAPIDS est prêt.

### Travailler interactivement sur un nœud GPU

Si l’image Apptainer a été construite avec une image Docker de type notebooks, elle inclut un serveur Jupyter Notebook et peut être employée pour explorer RAPIDS interactivement sur un nœud de calcul GPU. Pour demander une session interactive sur un nœud de calcul GPU, par exemple :

```bash
[name@cluster-login ~]$ salloc --ntasks=1 --cpus-per-task=2 --mem=10G --gpus-per-node=1 --time=1:0:0 --account=def-someuser
```

Quand la ressource est allouée, lancez l’interpréteur RAPIDS sur le nœud GPU avec :

```bash
[name@compute-node#### ~]$ module load apptainer
[name@compute-node#### ~]$ apptainer shell --nv rapids.sif
```
*   l'option `--nv` fait le *bind mount* du périphérique GPU de l’hôte sur le conteneur pour que l’accès au GPU puisse se faire de l’intérieur du conteneur Apptainer.

Lorsque l’invite de l’interpréteur change pour `Apptainer>`, vous pouvez consulter les statistiques pour le GPU dans l'interpréteur pour vous assurer que vous avez accès au GPU.

```bash
Apptainer> nvidia-smi
```

Lorsque l’invite change pour `Apptainer>`, vous pouvez lancer le serveur Jupyter Notebook dans l’environnement RAPIDS; ceci affichera l’URL du serveur.

```bash
Apptainer> jupyter-lab --ip $(hostname -f) --no-browser 
```

!!! note "Remarque"
    À partir de la version 23.08, RAPIDS n'a pas besoin d'être activé après que Conda ait démarré puisque tous les paquets sont inclus dans l'environnement Conda de base qui est activé par défaut dans Apptainer; par exemple, vous pouvez lancer le serveur Jupyter Notebook dans l'interpréteur du conteneur.

Si un nœud de calcul n’est pas connecté directement à l’internet, il faut configurer un tunnel SSH pour faire la redirection de port entre votre ordinateur et le nœud GPU. Pour les détails, voyez [comment se connecter à Jupyter Notebook](../../getting-started/advanced_jupyter_configuration.md).

### Soumettre une tâche RAPIDS à l'ordonnanceur

Quand votre code RAPIDS est prêt, vous pouvez soumettre une tâche à l'ordonnanceur. La bonne pratique est [d'utiliser le disque local](../../storage-and-data/using_node-local_storage.md) quand vous travaillez avec un conteneur sur un nœud de calcul.

### Script de soumission

```sh hl_lines="1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20" title="submit.sh"
#!/bin/bash
#SBATCH --gpus-per-node=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=10G
#SBATCH --time=dd:hh:mm
#SBATCH --account=def-someuser

module load apptainer

# copy your container image and your rapids code and data to the local disk on a compute node via $SLURM_TMPDIR

cd $SLURM_TMPDIR 
cp /path/to/rapids.sif ./
cp /path/to/your_rapids_code.py ./
cp -r /path/to/your_datasets ./
 
apptainer exec --nv rapids.sif python ./my_rapids_code.py 
 
# save any results to your /project before terminating the job
cp -r your_results ~/projects/def-someuser/username/
```

## Références

*   [RAPIDS Docs](https://docs.rapids.ai/) : documentation complète pour RAPIDS, comment rester en contact et rapporter les problèmes.
*   [RAPIDS Notebooks](https://github.com/rapidsai/notebooks) : exemples sur GitHub que vous pouvez utiliser.
*   [RAPIDS sur Medium](https://medium.com/rapids-ai) : cas d’usage et blogues.