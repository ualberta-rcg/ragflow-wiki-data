---
title: "AI and Machine Learning/fr"
slug: "ai_and_machine_learning"
lang: "fr"

source_wiki_title: "AI and Machine Learning/fr"
source_hash: "fa0b451fbf57603820317535ead0fc6e"
last_synced: "2026-04-10T14:10:18.226633+00:00"
last_processed: "2026-04-10T14:22:07.466561+00:00"

tags:
  - ai-and-machine-learning

keywords:
  - "ensembles de données"
  - "$SLURM_TMPDIR"
  - "Mégadonnées"
  - "Optimisation des hyperparamètres"
  - "grappes de calcul"
  - "Apprentissage machine"
  - "TensorFlow"
  - "Python"
  - "mégadonnées"
  - "CUDA"
  - "nœud"
  - "répertoire temporaire"
  - "apprentissage à grande échelle"
  - "stockage"
  - "espace de stockage"
  - "cuDNN"
  - "comportement non déterministe"
  - "Ensembles de données"
  - "apprentissage machine"
  - "Tutoriel Apprentissage machine"
  - "Points de contrôle"
  - "CUBLAS_WORKSPACE_CONFIG"
  - "réseaux de neurones récurrents"
  - "scalabilité"

questions:
  - "Pourquoi est-il crucial d'adapter la gestion de ses ensembles de données et le choix du stockage (comme la mémoire ou $SLURM_TMPDIR) lors de l'utilisation des grappes de calcul ?"
  - "Pour quelles raisons est-il fortement recommandé d'utiliser virtualenv au lieu d'Anaconda pour configurer son environnement Python ?"
  - "Quelles sont les ressources, tutoriels et bibliothèques logicielles mis à la disposition des utilisateurs pour faciliter l'apprentissage machine sur ces systèmes ?"
  - "Comment optimiser le stockage et la gestion des ensembles de données contenant de nombreux petits fichiers sur le système de fichiers partagé ?"
  - "Quels sont les avantages d'utiliser des points de contrôle (checkpoints) pour la gestion des calculs de longue durée ?"
  - "Quelles stratégies et quels outils sont recommandés pour regrouper plusieurs tâches similaires et effectuer le suivi des expérimentations ?"
  - "Où se trouve le répertoire temporaire mis à disposition pour chaque tâche ?"
  - "Quel problème d'espace de stockage peut être causé par l'exécution d'une tâche appartenant à un autre utilisateur ?"
  - "Quelle quantité maximale d'espace de stockage un utilisateur pourrait-il obtenir sur un nœud dans le meilleur des cas ?"
  - "Quels outils sont mentionnés comme offrant des utilitaires et de nombreux tutoriels pour l'apprentissage à grande échelle ?"
  - "Quel sujet concernant l'apprentissage machine classique est considéré comme étant peu abordé ?"
  - "Vers quelle ressource le texte renvoie-t-il pour obtenir plus d'informations sur l'apprentissage machine avec les mégadonnées ?"
  - "Dans quelles conditions un comportement non déterministe peut-il apparaître dans les réseaux de neurones récurrents utilisant CUDA ?"
  - "Quelle variable d'environnement permet de corriger ce problème et quelles valeurs peuvent lui être attribuées ?"
  - "De quelle manière la configuration de cette variable modifie-t-elle l'allocation de la mémoire GPU par cuBLAS ?"
  - "Dans quelles conditions un comportement non déterministe peut-il apparaître dans les réseaux de neurones récurrents utilisant CUDA ?"
  - "Quelle variable d'environnement permet de corriger ce problème et quelles valeurs peuvent lui être attribuées ?"
  - "De quelle manière la configuration de cette variable modifie-t-elle l'allocation de la mémoire GPU par cuBLAS ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Pour tirer le maximum de vos applications d'apprentissage machine, il faut connaître certains aspects particuliers de nos grappes. Ces machines sont beaucoup plus complexes que l'ordinateur local avec lequel vous faites du prototypage. Entre autres, une grappe possède des systèmes de fichiers distribués qui vont d'un type de stockage à un autre de façon transparente. Bien que l'accès à un fichier dans `/project` **peut donner l'impression de se faire de la même manière** que s'il était situé dans le nœud courant, sous le capot les effets sur la performance sont bien différents. Il est donc important de prendre connaissance de la section [Gérer vos ensembles de données](ai_and_machine_learning.md#gérer-vos-ensembles-de-données) ci-dessous.

Cette page décrit les bonnes pratiques dans l'utilisation des grappes ainsi que des références à de l'information utile.

## Tutoriels

SHARCNET offre un tutoriel de formation autonome; cliquez sur [Introduction to Machine Learning](https://training.sharcnet.ca/courses/enrol/index.php?id=180).

Si votre programme est prêt à être exécuté sur nos grappes, voyez [notre tutoriel](tutoriel_apprentissage_machine.md).

Voyez aussi ce [tutoriel préparé par un utilisateur](https://prashp.gitlab.io/post/compute-canada-tut/), qui décrit les étapes pour configurer votre environnement et celui de l'Alliance avec Python.

## Python

[Python](../python.md) est un logiciel populaire en apprentissage machine. Prenez connaissance de [notre page wiki](../python.md) pour des renseignements importants sur les versions, les environnements virtuels, les nœuds de connexion et de calcul, le `multiprocessing`, Anaconda, Jupyter, etc.

### Éviter Anaconda

!!! attention "Éviter Anaconda"
    Nous vous recommandons d'utiliser `virtualenv` pour éviter les problèmes suivants causés par Anaconda et évoqués sur [cette page](../anaconda.md).

    **Dans la plupart des cas, il est facile de passer à `virtualenv`. Vous n'avez qu'à installer les mêmes paquets, à l'exception de CUDA, CuDNN et d'autres bibliothèques de bas niveau qui sont déjà sur nos grappes.**

## Information sur les paquets logiciels disponibles

Pour des renseignements sur l'installation et les problèmes fréquents, voyez la page wiki pour chacun des paquets suivants :

*   [TensorFlow](../tensorflow.md)
*   [PyTorch](../pytorch.md)
*   [Keras](../keras.md)
*   [Torch](../torch.md)
*   [SpaCy](../spacy.md)
*   [Scikit-Learn](large_scale_machine_learning__big_data.md#scikit-learn)
*   [SnapML](large_scale_machine_learning__big_data.md#snap-ml)

## Gérer vos ensembles de données

### Stockage et gestion de fichiers

Les besoins pour la recherche sont diversifiés; nous offrons donc plusieurs solutions qui vont du stockage local temporaire haute vitesse au stockage à long terme sur différents supports. Pour plus d'information, voyez [Stockage et gestion de fichiers](../../storage-and-data/storage_and_file_management.md).

### Choisir le type de stockage selon la taille de votre ensemble de données

*   Si votre ensemble de données est d'environ 10Go ou moins, il entre probablement dans la mémoire, dépendant de la quantité de mémoire de votre tâche. Vos tâches d'apprentissage machine ne devraient pas lire de données sur disque.
*   Si votre ensemble de données est d'environ 100Go ou moins, il entre dans l'espace de stockage local du nœud de calcul; transférez-le dans cet espace au début de la tâche puisqu'il est beaucoup plus rapide et fiable que les espaces partagés que sont `/home`, `/project` et `/scratch`. Pour chaque tâche, un répertoire temporaire est disponible à `$SLURM_TMPDIR`; voyez l'exemple de [notre tutoriel](tutoriel_apprentissage_machine.md). Il faut toutefois savoir qu'une tâche d'un autre utilisateur peut occuper pleinement l'espace de stockage du nœud et ne vous laisser aucune place (nous cherchons une solution à ce problème); par contre, si c'est votre jour de chance, vous pourriez avoir un téraoctet juste pour vous.
*   Si votre ensemble de données est plus grand, vous pourriez devoir le laisser dans un espace partagé. Vous pouvez stocker des données de façon permanente dans votre espace `/project`; l'espace `/scratch` est parfois plus rapide, mais n'est pas conçu pour du stockage permanent. Tous les espaces de stockage partagés (`/home`, `/project` et `/scratch`) servent à lire et à stocker des données à faible fréquence (par exemple, 1 gros bloc par 10 secondes plutôt que 10 petits blocs par seconde).

### Ensembles de données composés de plusieurs petits fichiers

En apprentissage machine, il est fréquent d'avoir des ensembles de données composés de centaines et même de milliers de fichiers, par exemple dans le cas des ensembles de données d'images. Chacun des fichiers peut être de petite taille, souvent en deçà de quelques centaines de kilo-octets et dans ces cas, certains problèmes peuvent survenir :

*   le système de fichiers impose un [quota](../../storage-and-data/storage_and_file_management.md#quotas-et-politiques) qui restreint le nombre de fichiers,
*   l'application pourrait être considérablement ralentie par le transfert des fichiers de `/project` ou `/scratch` vers un nœud de calcul.

Avec un système de fichiers distribué, les données devraient être rassemblées dans un seul fichier d'archive; voyez [Travailler avec un grand nombre de fichiers](../../storage-and-data/handling_large_collections_of_files.md).

## Calculs de longue durée

Si vos calculs exigent beaucoup de temps, il est recommandé d'utiliser des points de contrôle (*checkpoints*); par exemple, plutôt que trois jours d'entraînement, vous pourriez avoir trois blocs de 24 heures chacun. De cette manière, votre travail ne serait pas perdu en cas de panne et vous pourriez bénéficier d'une meilleure priorisation de vos tâches puisqu'il y a plus de nœuds qui sont réservés pour les tâches courtes.
Votre bibliothèque préférée supporte probablement les *checkpoints*; voyez le cas type présenté dans [notre tutoriel](tutoriel_apprentissage_machine.md). Si votre programme ne le permet pas, consultez la [solution générique](points-de-controle.md).

Voir les autres exemples dans

[Points de contrôle PyTorch](../pytorch.md#créer-des-points-de-contrôle)

[Points de contrôle TensorFlow](../tensorflow.md#créer-des-points-de-contrôle)

## Exécution de plusieurs tâches similaires

Dans un des cas suivants :

*   recherche d'hyperparamètres,
*   entraînement de plusieurs variantes d'une même méthode,
*   exécution de plusieurs processus d'optimisation de même durée,

vous devriez grouper plusieurs tâches pour n'en former qu'une avec un outil comme [META](../../running-jobs/meta-farm.md), [GLOST](../../running-jobs/glost.md) ou [GNU Parallel](../../running-jobs/gnu_parallel.md).

## Suivi de l'expérimentation et optimisation des hyperparamètres

[Weights & Biases (wandb)](weights-and-biases-wandb.md) et [Comet.ml](comet.ml.md) peuvent vous aider à optimiser votre allocation de calcul en

*   facilitant le suivi et l'analyse des processus d'apprentissage,
*   permettant une optimisation bayésienne d'hyperparamètres.

## Apprentissage machine à grande échelle (mégadonnées)

Les paquets d'apprentissage profond modernes comme PyTorch et TensorFlow offrent des utilitaires pour les travaux natifs d’apprentissage à grande échelle et les tutoriels sont nombreux. Un sujet peu abordé par contre est la scalabilité des méthodes classiques d’apprentissage machine (et non d’apprentissage profond) pour le travail avec de grands ensembles de données; à ce sujet, voir la page wiki [Apprentissage machine à grande échelle (mégadonnées)](large_scale_machine_learning__big_data.md).

## Dépannage

### Déterminisme dans les réseaux de neurones récurrents avec CUDA

Quand la bibliothèque cuDNN est présente dans CUDA Toolkit versions 10.2 et plus, il est possible de voir un comportement non déterministe dans les réseaux de neurones récurrents (RNN) et les appels à l’API d’auto-attention multitêtes. Pour éviter ce problème, vous pouvez configurer la variable d’environnement CUBLAS_WORKSPACE_CONFIG avec une seule taille pour la mémoire tampon, par exemple `:16:8` ou `:4096:2`. Ainsi, cuBLAS fixe la mémoire GPU à 8 tampons de 16Ko chacun ou à 2 tampons de 4Mo chacun.