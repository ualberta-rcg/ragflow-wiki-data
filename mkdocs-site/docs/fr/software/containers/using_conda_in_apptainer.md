---
title: "Using Conda in Apptainer/fr"
slug: "using_conda_in_apptainer"
lang: "fr"

source_wiki_title: "Using Conda in Apptainer/fr"
source_hash: "d3fda4001188c94aa7b7f68190984cac"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T12:14:40.710182+00:00"

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

Avant de commencer ce tutoriel, prenez note de quelques points importants :

*   Même dans un conteneur, Conda ne devrait pas être votre solution préférée. Accordez plutôt la priorité aux [modules](modules.md) de notre [pile logicielle](available-software.md) et aux [wheels](python.md) parmi [ceux qui sont disponibles](available-python-wheels.md). Ces modules et wheels sont optimisés pour nos systèmes et nous pouvons fournir une meilleure assistance au besoin. Pour faire ajouter un module ou un paquet, contactez le [soutien technique](technical-support.md).
*   Dans ce tutoriel, nous utilisons le gestionnaire de paquets [micromamba](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html) au lieu de Conda. Si vous voulez utiliser Conda, vous devez tenir compte des [conditions d'utilisation d'Anaconda](https://legal.anaconda.com/policies/en?name=terms-of-service#terms-of-service) et peut-être [détenir une licence commerciale](https://www.anaconda.com/pricing/terms-of-service-faqs).
*   Dans ce tutoriel, nous créons une image en lecture seule, c'est-à-dire un fichier `.sif` qui contient un environnement Conda avec tout ce qu'il faut pour utiliser votre application. Il est fortement recommandé de **ne pas installer interactivement un logiciel dans un conteneur avec Conda** et aucune information ne sera fournie à cet égard.

La création d'une image Apptainer et l'installation de logiciels dans un conteneur avec Conda se fait en trois étapes.
Il faut d'abord créer un fichier `.yml` qui décrit l'environnement Conda à créer dans le conteneur; dans l'exemple suivant, il s'agit de `environment.yml`. Ce fichier contient le nom de l'environnement à créer, la liste des paquets à installer et la manière de les trouver (*channel*).

```yaml title="environment.yml"
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

Il faut ensuite créer un [fichier de définition pour l'image](https://apptainer.org/docs/user/main/definition_files.html) (nommé ici `image.def`) qui décrit les étapes pour créer l'image avec Apptainer.
1.  Téléchargez une image Docker de DockerHub qui contient le gestionnaire de paquets micromamba préinstallé.
2.  Créez dans le conteneur une copie du fichier de définition `environment.yml`.
3.  Exécutez micromamba pour configurer l'environnement `environment.yml`.

```yaml title="image.def"
Bootstrap: docker
From: mambaorg/micromamba:latest

%files
    environment.yml /environment.yml

%post
    micromamba install -n base --file environment.yml && \
        micromamba clean --all --yes
```

La dernière étape consiste à construire l'image Apptainer à l'aide du fichier de définition ci-dessus :

```bash
module load apptainer
APPTAINER_BIND=' ' apptainer build image.sif image.def
```

Vous pouvez maintenant tester si `multiqc` est disponible avec, par exemple, la commande :

```bash
apptainer run image.sif multiqc --help
```

```text
/// MultiQC 🎃 v1.25.1

Usage: multiqc [OPTIONS] [ANALYSIS DIRECTORY]
...