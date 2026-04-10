---
title: "Anaconda/fr"
tags:
  - software

keywords:
  []
---

Anaconda est une distribution de Python. 

= Pourquoi Anaconda n'est pas recommandé sur une grappe de calcul ? =

Anaconda peut être problématique sur une grappe de calcul pour plusieurs raisons:

* Anaconda installe très souvent des logiciels (compilateurs, bibliothèques scientifiques etc.) qui existent déjà sur les grappes de l'Alliance comme modules, avec une configuration qui n'est pas optimale, et qui peut causer des conflits.
* installe des binaires qui ne sont pas optimisés pour les processeurs de nos grappes. Vos calculs pourraient donc être plus lents.
* fait de mauvaises suppositions sur l'emplacement de bibliothèques. Vous pourriez rencontrer des erreurs à l'exécution.
* s'installe dans le `$HOME` par défaut, où il place une énorme quantité de fichiers. L'installation d'Anaconda seule peut prendre près de la moitié de votre quota sur le nombre de fichiers dans votre espace personnel. 
* est plus lent pour installer des paquets
* modifie `$HOME/.bashrc`, ce qui peut causer des conflits.

= Quelles sont les alternatives ? =
La première étape que vous devriez faire est de contacter notre [soutien technique](technical-support-fr.md) afin que nos experts explorent avec vous la meilleure alternative pour votre besoin. Si vous préférez tenter par vous-même, deux options principales sont listées ci-dessous.

## Transitionner de Conda vers virtualenv 

[Virtualenv](python#creating_and_using_a_virtual_environment.md) vous offre toutes les fonctionnalités dont vous avez besoin pour utiliser Python sur nos grappes. Ceci devrait être le premier choix que vous explorez. Voici comment passer à virtualenv si vous utilisez Anaconda sur votre ordinateur personnel:

# Listez les dépendances (requis) de l'application que vous voulez utiliser. Afin de ce faire, vous pouver :
## Exécuter <code>pip show <nom_paquet></code> depuis votre environement virtuel (si le paquet existe sur [PyPI](https://pypi.org/))
## Ou, vérifier s'il existe un fichier <tt>requirements.txt</tt> dans le dépôt Git.
## Ou, vérifier la variable <tt>install_requires</tt> du fichier <tt>setup.py</tt> qui énumère les requis.
# Trouvez quelles dépendances sont des paquets Python, et lesquelles sont des librairies fournies par Anaconda. Par exemple, CUDA et CuDNN sont des librairies disponible sur l'Anaconda Cloud, mais que vous ne devez pas installer vous-même sur nos grappes. Elles sont déjà installées.
# Retirez de la liste de dépendance tout ce qui n'est pas un paquet Python (par exemple, retirez `cudatoolkit` et `cudnn`).
# Utilisez un [virtualenv](python#creating_and_using_a_virtual_environment.md), dans lequel vous installerez ces dépendances.

Votre application devrait fonctionner. Si ce n'est pas le cas, n'hésitez pas à contacter notre [soutien technique](technical-support-fr.md).

## Utiliser Apptainer 

Dans certaines situations, la complexité des dépendances d'un logiciel exige une solution où l'on peut maîtriser entièrement l'environnement. Pour ces situations, on recommande l'outil [Apptainer](apptainer-fr#travailler_avec_conda.md) : notez qu'une image Docker peut être convertie en image Apptainer. Le seul inconvénient de Apptainer, c'est que les images consomment beaucoup d'espace disque, alors si votre groupe de recherche prévoit d'utiliser plusieurs images, il serait sage de les regrouper ensemble dans un seul répertoire de l'espace projet du groupe pour éviter les doublons.