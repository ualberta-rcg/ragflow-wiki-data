---
title: "AI and Machine Learning/fr"
tags:
  - ai-and-machine-learning

keywords:
  []
---

Pour tirer le maximum de vos applications d'apprentissage machine, il faut connaître certains aspects particuliers de nos grappes. Ces machines sont beaucoup plus complexes que l'ordinateur local avec lequel vous faites du prototypage. Entre autres, une grappe possède des systèmes de fichiers distribués qui vont d'un type de stockage à un autre de façon transparente. Bien que l'accès à un fichier dans `/project` <b>peut donner l'impression de se faire de la même manière</b> que s'il était situé dans le nœud courant, sous le capot les effets sur la performance sont bien différents. Il est donc important de prendre connaissance de la section [Gérer vos ensembles de données](ai-and-machine-learning-fr#gérer_vos_ensembles_de_données.md) ci-dessous.

Cette page décrit les bonnes pratiques dans l'utilisation des grappes ainsi que des références à de l'information utile.

<span id="Tutorials"></span>
## Tutoriels 

SHARCNET offre un tutoriel de formation autonome; cliquez sur [Introduction to Machine Learning](https://training.sharcnet.ca/courses/enrol/index.php?id=180).

Si votre programme est prêt à être exécuté sur nos grappes, voyez [notre tutoriel](tutoriel-apprentissage-machine.md).

Voyez aussi ce [tutoriel préparé par un utilisateur](https://prashp.gitlab.io/post/compute-canada-tut/), qui décrit les étapes pour configurer votre environnement et celui de l'Alliance avec Python.

## Python 

[Python](python-fr.md) est un logiciel populaire en apprentissage machine. Prenez connaissance de [notre page wiki](python-fr.md) pour des renseignements importants sur les versions, les environnements virtuels, les nœuds de connexion et de calcul, le `multiprocessing`, Anaconda, Jupyter, etc.

<span id="Avoid_Anaconda"></span>
### Éviter Anaconda 

Nous vous recommandons d'utiliser `virtualenv` pour éviter les problèmes suivants causés par Anaconda et évoqués sur [cette page](anaconda.md).

<b>Dans la plupart des cas, il est facile de passer à `virtualenv`. Vous n'avez qu'à installer les mêmes paquets, à l'exception de CUDA, CuDNN et d'autres bibliothèques de bas niveau qui sont déjà sur nos grappes.</b>

<span id="Useful_information_about_software_packages"></span>
## Information sur les paquets logiciels disponibles 

Pour des renseignements sur l'installation et les problèmes fréquents, voyez la page wiki pour chacun des paquets suivants&nbsp;:

* [TensorFlow](tensorflow-fr.md)
* [PyTorch](pytorch-fr.md)
* [Keras](keras-fr.md)
* [Torch](torch-fr.md)
* [SpaCy](spacy-fr.md)
* [Scikit-Learn](large_scale_machine_learning_(big_data)-fr#scikit-learn.md)
* [SnapML](large_scale_machine_learning_(big_data)-fr#snap_ml.md)

<span id="Managing_your_datasets"></span>
## Gérer vos ensembles de données 

<span id="Storage_and_file_management"></span>
### Stockage et gestion de fichiers 

Les besoins pour la recherche sont diversifiés; nous offrons donc plusieurs solutions qui vont du stockage local temporaire haute vitesse au stockage à long terme sur différents supports. Pour plus d'information, voyez [Stockage et gestion de fichiers](storage-and-file-management-fr.md).

<span id="Choosing_the_right_storage_type_for_your_dataset"></span>
### Choisir le type de stockage selon la taille de votre ensemble de données

* Si votre ensemble de données est d'environ 10Go ou moins, il entre probablement dans la mémoire, dépendant de la quantité de mémoire de votre tâche. Vos tâches d'apprentissage machine ne devraient pas lire de données sur disque.
* Si votre ensemble de données est d'environ 100Go ou moins, il entre dans l'espace de stockage local du nœud de calcul; transférez-le dans cet espace au début de la tâche puisqu'il est beaucoup plus rapide et fiable que les espaces partagés que sont /home, /project et /scratch. Pour chaque tâche, un répertoire temporaire est disponible à $SLURM_TMPDIR; voyez l'exemple de [notre tutoriel](tutoriel-apprentissage-machine.md). Il faut toutefois savoir qu'une tâche d'un autre utilisateur peut occuper pleinement l'espace de stockage du nœud et ne vous laisser aucune place (nous cherchons une solution à ce problème); par contre, si c'est votre jour de chance, vous pourriez avoir un téraoctet juste pour vous.
* Si votre ensemble de données est plus grand, vous pourriez devoir le laisser dans un espace partagé. Vous pouvez stocker des données de façon permanente dans votre espace /project; l'espace /scratch est parfois plus rapide, mais n'est pas conçu pour du stockage permanent. Tous les espaces de stockage partagés (/home, /project et /scratch) servent à lire et à stocker des données à faible fréquence (par exemple, 1 gros bloc par 10 secondes plutôt que 10 petits blocs par seconde).

<span id="Datasets_containing_lots_of_small_files_(e.g._image_datasets)"></span>
### Ensembles de données composés de plusieurs petits fichiers 

En apprentissage machine, il est fréquent d'avoir des ensembles de données composés de centaines et même de milliers de fichiers, par exemple dans le cas des ensembles de données d'images. Chacun des fichiers peut être de petite taille, souvent en deçà de quelques centaines de kilo-octets et dans ces cas, certains problèmes peuvent survenir&nbsp;:

* le système de fichiers impose un [quota](storage-and-file-management-fr#quotas_et_politiques.md) qui restreint le nombre de fichiers,
* l'application pourrait être considérablement ralentie par le transfert des fichiers de `/project` ou `/scratch` vers un nœud de calcul.

Avec un système de fichiers distribué, les données devraient être rassemblées dans un seul fichier d'archive; voyez [Travailler avec un grand nombre de fichiers](handling-large-collections-of-files-fr.md).

<span id="Long_running_computations"></span>
## Calculs de longue durée 

Si vos calculs exigent beaucoup de temps, il est recommandé d'utiliser des points de contrôle (<i>checkpoints</i>); par exemple, plutôt que trois jours d'entraînement, vous pourriez avoir trois blocs de 24 heures chacun. De cette manière, votre travail ne serait pas perdu en cas de panne et vous pourriez bénéficier d'une meilleure priorisation de vos tâches puisqu'il y a plus de nœuds qui sont réservés pour les tâches courtes.
Votre bibliothèque préférée supporte probablement les <i>checkpoints</i>; voyez le cas type présenté dans [notre tutoriel](tutoriel-apprentissage-machine.md). Si votre programme ne le permet pas, consultez la [solution générique](points-de-contrôle.md).

Voir les autres exemples dans 

[Points de contrôle PyTorch](pytorch-fr#créer_des_points_de_contrôle.md)

[Points de contrôle TensorFlow](tensorflow-fr#créer_des_points_de_contrôle.md)

<span id="Running_many_similar_jobs"></span>
## Exécution de plusieurs tâches similaires 

Dans un des cas suivants :

* recherche d'hyperparamètres,
* entraînement de plusieurs variantes d'une même méthode,
* exécution de plusieurs processus d'optimisation de même durée,

vous devriez grouper plusieurs tâches pour n'en former qu'une avec un outil comme [META](meta-farm-fr.md), [GLOST](glost-fr.md) ou [GNU Parallel](gnu-parallel-fr.md).

<span id="Experiment_tracking_and_hyperparameter_optimization"></span>
## Suivi de l'expérimentation et optimisation des hyperparamètres 

[Weights & Biases (wandb)](weights-&-biases-(wandb)-fr.md)  et [Comet.ml](comet.ml-fr.md) peuvent vous aider à optimiser votre allocation de calcul en

* facilitant le suivi et l'analyse des processus d'apprentissage,
* permettant une optimisation bayésienne d'hyperparamètres.

<span id="Large-scale_machine_learning_(big_data)"></span>
## Apprentissage machine à grande échelle (mégadonnées)

Les paquets d'apprentissage profond modernes comme PyTorch et TensorFlow offrent des utilitaires pour les travaux natifs d’apprentissage à grande échelle et les tutoriels sont nombreux. Un sujet peu abordé par contre est la scalabilité des méthodes classiques d’apprentissage machine (et non d’apprentissage profond) pour le travail avec de grands ensembles de données; à ce sujet, voir la page wiki [Apprentissage machine à grande échelle (mégadonnées)](large_scale_machine_learning_(big_data)-fr.md).

<span id="Troubleshooting"></span>
## Dépannage 

<span id="Determinism_with_RNN_using_CUDA"></span>
### Déterminisme dans les réseaux de neurones récurrents avec CUDA

Quand la bibliothèque cuDNN est présente dans CUDA Toolkit versions 10.2 et plus, il est possible de voir un comportement non déterministe dans les réseaux de neurones récurrents (RNN) et les appels à l’API d’auto-attention multitêtes.
Pour éviter ce problème, vous pouvez configurer la variable d’environnement CUBLAS_WORKSPACE_CONFIG avec une seule taille pour la mémoire tampon, par exemple `:16:8` ou `:4096:2`. Ainsi, cuBLAS fixe la mémoire GPU à 8 tampons de 16Ko chacun ou à 2 tampons de 4Mo chacun.