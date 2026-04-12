---
title: "Anaconda"
slug: "anaconda"
lang: "base"

source_wiki_title: "Anaconda"
source_hash: "55e74e5650798fdea9f5f2f325ec3647"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:07:08.748591+00:00"

tags:
  - software

keywords:
  - "soutien technique"
  - "dépendances d'un logiciel"
  - "virtualenv"
  - "Conda"
  - "image Docker"
  - "espace disque"
  - "grappe de calcul"
  - "paquet Python"
  - "Anaconda"
  - "Python"
  - "dépendance"
  - "Apptainer"

questions:
  - "Quelle est la politique du soutien technique de l'Alliance concernant l'utilisation d'Anaconda sur ses grappes de calcul ?"
  - "Quels sont les problèmes techniques et les impacts sur les performances causés par l'installation d'Anaconda ?"
  - "Quelles sont les alternatives recommandées à Anaconda et comment procéder pour faire la transition vers un environnement virtuel (virtualenv) ?"
  - "Dans quelles situations est-il recommandé d'utiliser l'outil Apptainer ?"
  - "Comment les images Docker peuvent-elles être intégrées ou utilisées avec Apptainer ?"
  - "Quel est le principal inconvénient d'Apptainer et quelle solution est proposée pour le contourner au sein d'un groupe de recherche ?"
  - "Quels types de paquets doivent être retirés de la liste des dépendances ?"
  - "Quel outil est recommandé pour installer les dépendances Python ?"
  - "Que faut-il faire si l'application ne fonctionne pas après la configuration de l'environnement ?"
  - "Dans quelles situations est-il recommandé d'utiliser l'outil Apptainer ?"
  - "Comment les images Docker peuvent-elles être intégrées ou utilisées avec Apptainer ?"
  - "Quel est le principal inconvénient d'Apptainer et quelle solution est proposée pour le contourner au sein d'un groupe de recherche ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Anaconda is a Python distribution.

!!! warning "Before using Anaconda"
    We understand that Anaconda is widely used in several fields studied by our users (data science, AI, bioinformatics, etc.). Anaconda is an interesting solution for simplifying Python and library management on a personal computer. However, on a cluster like those maintained by the Alliance, library management must be handled by our staff to ensure maximum compatibility and performance. Furthermore, using Anaconda on a compute cluster can lead to several problems.
    Before using Anaconda, we ask you to contact our [technical support](technical-support.md) so our experts can explore alternatives with you. If you choose to use Anaconda, please note that our team will not be able to provide support if you encounter issues.

## Why Anaconda is Not Recommended on a Compute Cluster

Anaconda can be problematic on a compute cluster for several reasons:

*   Anaconda very often installs software (compilers, scientific libraries, etc.) that already exist on the Alliance clusters as modules, with sub-optimal configurations that can cause conflicts.
*   Installs binaries that are not optimized for our clusters' processors. Your computations could therefore be slower.
*   Makes incorrect assumptions about library locations. You might encounter runtime errors.
*   Installs into your default `$HOME` directory, where it places an enormous number of files. A standalone Anaconda installation can take up nearly half of your file count quota in your home directory.
*   Is slower for installing packages.
*   Modifies `$HOME/.bashrc`, which can cause conflicts.

## What Are the Alternatives?

The first step you should take is to contact our [technical support](technical-support.md) so our experts can explore the best alternative for your needs with you. If you prefer to try on your own, two main options are listed below.

### Transitioning from Conda to virtualenv

[Virtualenv](python.md#creating-and-using-a-virtual-environment) offers all the features you need to use Python on our clusters. This should be your first choice to explore. Here's how to switch to virtualenv if you're using Anaconda on your personal computer:

1.  List the dependencies (requirements) of the application you want to use. To do this, you can:
    *   Run `pip show <package_name>` from your virtual environment (if the package exists on [PyPI](https://pypi.org/))
    *   Or, check if a `requirements.txt` file exists in the Git repository.
    *   Or, check the `install_requires` variable in the `setup.py` file, which lists the requirements.
2.  Find which dependencies are Python packages and which are libraries provided by Anaconda. For example, CUDA and CuDNN are libraries available on Anaconda Cloud, but you should not install them yourself on our clusters. They are already installed.
3.  Remove anything that is not a Python package from the dependency list (e.g., remove `cudatoolkit` and `cudnn`).
4.  Use a [virtualenv](python.md#creating-and-using-a-virtual-environment) in which you will install these dependencies.

Your application should now work. If not, do not hesitate to contact our [technical support](technical-support.md).

### Using Apptainer

In some situations, the complexity of software dependencies requires a solution where the environment can be fully controlled. For these situations, we recommend the [Apptainer](apptainer.md#working-with-conda) tool: note that a Docker image can be converted into an Apptainer image. The only drawback of Apptainer is that images consume a lot of disk space, so if your research group plans to use multiple images, it would be wise to group them together in a single directory within the group's project space to avoid duplication.

[Using Conda in Apptainer](using-conda-in-apptainer.md)