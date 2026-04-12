---
title: "Using Conda in Apptainer/fr"
slug: "using_conda_in_apptainer"
lang: "fr"

source_wiki_title: "Using Conda in Apptainer/fr"
source_hash: "d3fda4001188c94aa7b7f68190984cac"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:16:02.245046+00:00"

tags:
  []

keywords:
  - "Conda"
  - "conteneur"
  - "micromamba"
  - "fichier de définition"
  - "Apptainer"

questions:
  - "Pourquoi le tutoriel recommande-t-il d'utiliser micromamba au lieu de Conda, et quelles sont les alternatives logicielles à privilégier ?"
  - "Quel est le rôle respectif des fichiers environment.yml et image.def dans la préparation et la configuration du conteneur ?"
  - "Comment procède-t-on pour construire l'image Apptainer finale et vérifier qu'un programme y est correctement installé ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Avant d'entamer ce tutoriel, prenez note de quelques points importants :

!!! info "Meilleures pratiques"
    Même dans un conteneur, Conda ne devrait pas être votre solution préférée. Accordez plutôt la priorité aux [modules](../../programming/modules.md) de notre [pile logicielle](../../programming/available_software.md) et aux [wheels Python](../python.md) parmi [ceux qui sont disponibles](../../programming/available_python_wheels.md). Ces modules et wheels sont optimisés en fonction de nos systèmes et nous pouvons fournir une meilleure assistance au besoin. Pour faire ajouter un module ou un paquet, contactez le [soutien technique](../../support/technical_support.md).

!!! warning "Conditions d'utilisation"
    Dans ce tutoriel, nous utilisons le gestionnaire de paquets [micromamba](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html) au lieu de Conda. Si vous voulez utiliser Conda, vous devez tenir compte des [conditions d'utilisation d'Anaconda](https://legal.anaconda.com/policies/en?name=terms-of-service#terms-of-service) et peut-être [détenir une licence commerciale](https://www.anaconda.com/pricing/terms-of-service-faqs).

!!! warning "Mise en garde importante"
    Dans ce tutoriel, nous créons une image en lecture seule, c'est-à-dire un fichier `.sif` qui contient un environnement Conda avec tout ce qu'il faut pour utiliser votre application. Il est fortement recommandé de **ne pas installer interactivement un logiciel dans un conteneur avec Conda** et aucune information ne sera donnée en ce sens.

La création d'une image Apptainer et l'installation d'un logiciel dans un conteneur avec Conda est un processus en trois étapes.
Il faut d'abord créer un fichier `.yml` qui décrit l'environnement Conda à créer dans le conteneur; dans l'exemple suivant, il s'agit de `environment.yml`. Ce fichier contient le nom de l'environnement à créer, la liste des paquets à installer et comment les trouver (le *canal*).

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

```apptainer title="image.def"
Bootstrap: docker
From: mambaorg/micromamba:latest

%files
    environment.yml /environment.yml

%post
    micromamba install -n base --file environment.yml && \
        micromamba clean --all --yes
```

La dernière étape est de construire l'image Apptainer à l'aide du fichier de définition ci-dessus :

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