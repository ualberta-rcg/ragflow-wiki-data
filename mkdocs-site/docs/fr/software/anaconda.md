---
title: "Anaconda/fr"
slug: "anaconda"
lang: "fr"

source_wiki_title: "Anaconda/fr"
source_hash: "dab380019581e5dde37eb02dd13ce0d8"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T04:14:11.137708+00:00"

tags:
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

Anaconda est une distribution de Python.

!!! warning "Avant d'utiliser Anaconda"
    Nous sommes conscients qu'Anaconda est largement utilisé dans plusieurs domaines étudiés par nos utilisateurs (la science des données, l'IA, la bioinformatique, etc.). Anaconda est une solution intéressante pour simplifier la gestion de Python et de bibliothèques sur un ordinateur personnel. Cependant, sur une grappe comme celles maintenues par l'Alliance, la gestion des bibliothèques doit être faite par notre personnel, afin d'assurer une compatibilité et une performance maximales. De plus, l'utilisation d'Anaconda sur une grappe de calcul peut mener à plusieurs problèmes.
    Avant d'utiliser Anaconda, nous vous demandons de contacter notre [soutien technique](technical-support.md) pour que nos experts puissent explorer les alternatives avec vous. Si vous choisissez d'utiliser Anaconda, notez que notre équipe ne pourra pas vous offrir de soutien si vous rencontrez des problèmes.

## Pourquoi Anaconda n'est pas recommandé sur une grappe de calcul ?

Anaconda peut être problématique sur une grappe de calcul pour plusieurs raisons :

*   Anaconda installe très souvent des logiciels (compilateurs, bibliothèques scientifiques, etc.) qui existent déjà sur les grappes de l'Alliance comme modules, avec une configuration qui n'est pas optimale et qui peut causer des conflits.
*   Installe des binaires qui ne sont pas optimisés pour les processeurs de nos grappes. Vos calculs pourraient donc être plus lents.
*   Fait de mauvaises suppositions sur l'emplacement de bibliothèques. Vous pourriez rencontrer des erreurs à l'exécution.
*   S'installe dans le `$HOME` par défaut, où il place une énorme quantité de fichiers. L'installation d'Anaconda seule peut prendre près de la moitié de votre quota sur le nombre de fichiers dans votre espace personnel.
*   Est plus lent pour installer des paquets.
*   Modifie `$HOME/.bashrc`, ce qui peut causer des conflits.

## Quelles sont les alternatives ?

La première étape que vous devriez faire est de contacter notre [soutien technique](technical-support.md) afin que nos experts explorent avec vous la meilleure alternative pour votre besoin. Si vous préférez tenter par vous-même, deux options principales sont listées ci-dessous.

### Transitionner de Conda vers virtualenv

[Virtualenv](python.md#creating-and-using-a-virtual-environment) vous offre toutes les fonctionnalités dont vous avez besoin pour utiliser Python sur nos grappes. Ceci devrait être le premier choix que vous explorez. Voici comment passer à Virtualenv si vous utilisez Anaconda sur votre ordinateur personnel :

1.  Listez les dépendances (requis) de l'application que vous voulez utiliser. Pour ce faire, vous pouvez :
    *   Exécuter `pip show <nom_paquet>` depuis votre environnement virtuel (si le paquet existe sur [PyPI](https://pypi.org/))
    *   Ou, vérifier s'il existe un fichier `requirements.txt` dans le dépôt Git.
    *   Ou, vérifier la variable `install_requires` du fichier `setup.py` qui énumère les requis.
2.  Trouvez quelles dépendances sont des paquets Python et lesquelles sont des bibliothèques fournies par Anaconda. Par exemple, CUDA et CuDNN sont des bibliothèques disponibles sur l'Anaconda Cloud, mais que vous ne devez pas installer vous-même sur nos grappes. Elles sont déjà installées.
3.  Retirez de la liste de dépendances tout ce qui n'est pas un paquet Python (par exemple, retirez `cudatoolkit` et `cudnn`).
4.  Utilisez un [virtualenv](python.md#creating-and-using-a-virtual-environment), dans lequel vous installerez ces dépendances.

Votre application devrait fonctionner. Si ce n'est pas le cas, n'hésitez pas à contacter notre [soutien technique](technical-support.md).

### Utiliser Apptainer

Dans certaines situations, la complexité des dépendances d'un logiciel exige une solution où l'on peut maîtriser entièrement l'environnement. Pour ces situations, on recommande l'outil [Apptainer](apptainer.md#travailler-avec-conda) : notez qu'une image Docker peut être convertie en image Apptainer. Le seul inconvénient d'Apptainer, c'est que les images consomment beaucoup d'espace disque. Alors, si votre groupe de recherche prévoit d'utiliser plusieurs images, il serait sage de les regrouper ensemble dans un seul répertoire de l'espace projet du groupe pour éviter les doublons.