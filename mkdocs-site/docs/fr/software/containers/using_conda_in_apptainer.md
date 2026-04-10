---
title: "Using Conda in Apptainer/fr"
tags:
  []

keywords:
  []
---

<noinclude>

</noinclude>

Avant de commencer ce tutoriel, prenez note de quelques points importants&nbsp;:

* Même dans un conteneur, Conda ne devrait pas être votre solution préférée. Accordez plutôt la priorité aux [modules](modules-fr.md) de notre [pile logicielle](available-software-fr.md) et aux [wheels](python-fr.md) parmi [ceux qui sont disponibles](available-python-wheels-fr.md). Ces modules et wheels sont optimisés en fonction de nos systèmes et nous pouvons fournir une meilleure assistance au besoin. Pour faire ajouter un module ou un paquet, contactez le [soutien technique](technical-support-fr.md).
* Dans ce tutoriel, nous utilisons le gestionnaire de paquets [micromamba](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html) au lieu de Conda. Si vous voulez utiliser Conda, vous devez tenir compte des  [conditions d'utilisation d'Anaconda](https://legal.anaconda.com/policies/en?name=terms-of-service#terms-of-service) et peut-être  [détenir une licence commerciale](https://www.anaconda.com/pricing/terms-of-service-faqs).
* Dans ce tutoriel, nous créons une image pour lecture seule, c'est-à dire un fichier <tt>.sif</tt> qui contient un environnement Conda avec tout ce qu'il faut pour utiliser votre application. Il est fortement recommandé de <b>ne pas installer interactivement un logiciel dans un conteneur avec Conda</b> et aucune information ne sera donnée en ce sens.

La création d'une image Apptainer et l'installation d'un logiciel dans un conteneur avec Conda est un processus en trois étapes.

Il faut d'abord créer un fichier <tt>.yml</tt> qui décrit l'environnement Conda à créer dans le conteneur; dans l'exemple suivant, il s'agit de <tt>environment.yml</tt>. Ce fichier contient le nom de l'environnement à créer, la liste des paquets à installer et comment les trouver (<i>channel</i>).

**`environment.yml`**
```yaml
name: base
channels:
  - conda-forge
  - bioconda
  - defaults
dependencies:
  - python
  - pip
  - star
  - bwa
  - multiqc
```

Il faut ensuite créer un  [fichier de définition pour l'image](https://apptainer.org/docs/user/main/definition_files.html) (nommé ici <tt>image.def</tt>) qui décrit les étapes pour créer l'image avec Apptainer.
#Téléchargez une image Docker de DockerHub qui contient le gestionnaire de paquets micromamba préinstallé.
#Créez dans le conteneur une copie du fichier de définition <tt>environment.yml</tt>.
#Exécutez micromamba pour configurer l'environnement <tt>environment.yml</tt>.

**`image.def`**
```yaml
Bootstrap: docker
From: mambaorg/micromamba:latest

%files
    environment.yml /environment.yml

%post
    micromamba install -n base --file environment.yml && \
        micromamba clean --all --yes
```

La dernière étape est de construire l'image Apptainer à l'aide du fichier de définition ci-dessus&nbsp;:
   module load apptainer
   APPTAINER_BIND=' ' apptainer build image.sif image.def

Vous pouvez maintenant tester si `multiqc` est disponible avec, par exemple, la commande

```bash
apptainer run image.sif multiqc --help
```

```
/// MultiQC 🎃 v1.25.1
 
 Usage: multiqc [OPTIONS] [ANALYSIS DIRECTORY]
...
```