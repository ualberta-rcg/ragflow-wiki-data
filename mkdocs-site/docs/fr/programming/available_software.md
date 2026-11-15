---
title: "Available software/fr"
slug: "available_software"
lang: "fr"

source_wiki_title: "Available software/fr"
source_hash: "a34f1bd7797c1ad8c78d8348418823e5"
last_synced: "2026-11-15T02:27:25.182546+00:00"
last_processed: "2026-11-15T03:23:41.210263+00:00"

tags:
  []

keywords:
  - "Gaussian"
  - "paquets Python wheels"
  - "prérequis"
  - "documentation"
  - "colonne Type"
  - "Modules AVX512"
  - "modules Lmod"
  - "logiciels disponibles"
  - "colonne Description"
  - "environnement StdEnv"
  - "tri"
  - "Apptainer"
  - "CVMFS"
  - "logiciels installés localement"
  - "Amsterdam Density Functional Modeling Suite"

questions:
  - "Comment peut‑on demander l’installation ou la mise à jour d’un logiciel ou d’une bibliothèque sur la plateforme nationale ?"
  - "Où et comment installer les paquets Python, R ou Perl qui ne sont pas fournis en tant que modules Lmod ?"
  - "Quel outil est disponible pour exécuter des conteneurs Docker sur les grappes et comment le charger ?"
  - "Quels logiciels sont installés localement sur les grappes spécifiques (Nibi, Fir, etc.) et à quels domaines scientifiques (chimie, physique, etc.) ils sont associés ?"
  - "Pourquoi certains paquets ne sont disponibles que sur des grappes particulières et ne sont pas distribués via le système de fichiers CVMFS ?"
  - "Où peut‑on accéder à la documentation ou aux sites web officiels des logiciels listés (ADF, AMS, AMBER, DIRAC, Gaussian) ?"
  - "Comment accéder aux prérequis et à la description sommaire d’un logiciel dans la colonne « Description » ?"
  - "Où se trouve le lien permettant d’accéder à la documentation spécifique d’un logiciel ?"
  - "Comment trier la liste des logiciels par type et quels sont les différents types disponibles ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Le tableau ci-dessous présente la liste des logiciels disponibles sur la plateforme nationale. Cette liste est mise à jour à l'ajout de tout nouveau logiciel. Pour demander l'installation ou la mise à jour d'un logiciel ou d'une bibliothèque, communiquez avec le [soutien technique](../support/technical_support.md). Pour utiliser notre environnement logiciel sur votre propre ordinateur, consultez [notre page wiki CVMFS](../software/cvmfs/accessing_cvmfs.md).

!!! warning "Disponibilité"
    **Certains logiciels ne sont peut-être pas disponibles dans l'environnement standard `StdEnv` que vous avez chargé.**

    `StdEnv/2020` est maintenant caché ou obsolète sur les nouveaux systèmes (voir [StdEnv/2020](standard_software_environments.md)).

## Notes
Pour utiliser un logiciel qui n'est pas déjà installé par défaut, vous devez charger le module qui s'applique. Pour plus d'information sur comment utiliser le système de modules Lmod, consultez [Utiliser des modules](utiliser_des_modules.md). Prenez note que certains modules prérequis sont chargés par défaut.

**Points à retenir à propos des logiciels disponibles**

*   La plupart des modules Python ne sont pas installés en tant que modules (Lmod), mais en tant que [paquets binaires](available_python_wheels.md) (*wheels*) localisés sous `/cvmfs/soft.computecanada.ca/custom/python/wheelhouse/`; [TensorFlow](../software/tensorflow.md) en est un exemple. Voyez la page [Python](../software/python.md) pour des détails sur comment lister les paquets Python et les installer.
*   De même, la plupart des paquets R et Perl ne sont pas installés. Nous vous recommandons de les installer dans votre environnement personnel ou dans celui de votre groupe. Voyez les pages [R](../software/r.md) et [Perl](../software/perl.md) pour des détails sur l'installation des paquets.
*   Voyez la page [Algèbre symbolique](../software/symbolic_algebra_software.md) où il est question de SageMath.
*   Notez que [Docker](https://www.docker.com/) n'est pas disponible sur nos grappes, mais que [Apptainer](../software/containers/apptainer.md) peut être utilisé en chargeant le module `apptainer`. Pour convertir les conteneurs Docker, consultez [la documentation Apptainer](https://apptainer.org/docs/).
*   Certains logiciels listés dans le tableau ci-dessous sont sous licence et donc non accessibles directement; vous pouvez en demander l'accès au besoin. En tentant de charger le module d'un tel logiciel, vous recevrez les consignes sur comment en obtenir l'accès.
*   La plupart des paquets listés se trouvent sur toutes nos grappes. Certains cependant ne sont disponibles que sur un site en particulier en raison des restrictions liées à l'octroi des licences; voir [Modules disponibles uniquement sur certaines grappes](#modules-disponibles-uniquement-sur-certaines-grappes) ci-dessous.
*   Les paquets listés sont disponibles dans un ou plusieurs de nos environnements logiciels standards. Dans certains cas peu fréquents, vous devrez charger un environnement logiciel différent pour avoir accès à un paquet en particulier; voyez [Environnements logiciels standards](standard_software_environments.md).
*   Plusieurs paquets reliés au système d’exploitation comme [Autotools](autotools.md), [Make](make.md) et [Git](../software/git.md) ne sont pas installés en tant que modules, mais font partie de l'environnement par défaut; ils ne paraissent pas dans le tableau.

## Modules disponibles sur toutes les grappes
Le tableau suivant liste les logiciels pour lesquels un module d'environnement est disponible. Certains modules peuvent être chargés avec la commande `module load` alors que d'autres nécessitent des conditions particulières.
Dans la colonne *Description*, vous trouverez les prérequis et une description sommaire du logiciel (en anglais).
Un lien dans la colonne *Documentation* conduit à la documentation spécifique sur le logiciel.

Les types sont :
*   ai (intelligence artificielle)
*   bio (biologie, bio-informatique)
*   chem (chimie)
*   geo (sciences de la Terre)
*   io (input/output)
*   math (mathématiques)
*   mpi ([MPI](../software/mpi.md))
*   phys (physique et génie)
*   tools (langages et bibliothèques)
*   vis ([visualisation](../software/visualization.md)).

Les logiciels pour les architectures obsolètes se trouvent respectivement dans AVX et SSE3.

=== "AVX512 (Fir, Nibi, Rorqual, Trillium, Killarney, tamIA, Vulcan)"

Le contenu de la page Modules_avx512 devrait apparaître ici.

=== "AVX2 (Narval)"

Le contenu de la page Modules_avx2 devrait apparaître ici.

## Modules disponibles uniquement sur certaines grappes
La plupart des applications sont installées dans CVMFS, un système de fichiers qui facilite la gestion du grand nombre des paquets que nous offrons. Cependant, d'autres paquets ne sont installés que dans certains sites, principalement pour des raisons de licence.

### Logiciels installés localement

| Module | Type | Documentation | Grappe | Description |
| :----- | :--- | :------------ | :----- | :---------- |
| adf/2016.106 | chem | [ADF](../software/adf.md) | Nibi | Amsterdam Density Functional Modeling Suite; recherche en chimie computationnelle |
| adf/2017.207 | chem | [ADF](../software/adf.md) | Nibi | Amsterdam Density Functional Modeling Suite; recherche en chimie computationnelle |
| adf/2018.104 | chem | [ADF](../software/adf.md) | Nibi | Amsterdam Density Functional Modeling Suite; recherche en chimie computationnelle |
| adf/2019.305 | chem | [ADF](../software/adf.md) | Nibi | Amsterdam Density Functional Modeling Suite; recherche en chimie computationnelle |
| ams/2020.102 | chem | [AMS](../software/ams.md) | Nibi | Amsterdam Modeling Suite |
| amber/16 | chem | [AMBER](../software/amber.md) | Nibi | ensemble d'applications pour effectuer des simulations en dynamique moléculaire |
| dirac/16.0 | phys | | Fir | Direct Iterative Relativistic All-electron Calculations; calcule les propriétés moléculaires avec des méthodes de chimie quantique relativiste (site web : [diracprogram.org](http://diracprogram.org)) |
| dirac/17.0 | phys | | Fir | Direct Iterative Relativistic All-electron Calculations; calcule les propriétés moléculaires avec des méthodes de chimie quantique relativiste (site web : [diracprogram.org](http://diracprogram.org)) |
| gaussian/g03.d01 | chem | [Gaussian](../software/gaussian.md) | Nibi | paquet logiciel d'usage général en chimie computationnelle (site web : [gaussian.com](http://gaussian.com/)) |
| gaussian/g09.e01 | chem | [Gaussian](../software/gaussian.md) | Nibi | paquet logiciel d'usage général en chimie computationnelle (site web : [gaussian.com](http://gaussian.com/)) |
| gaussian/g16.b01 | chem | [Gaussian](../software/gaussian.md) | Nibi | paquet logiciel d'usage général en chimie computationnelle (site web : [gaussian.com](http://gaussian.com/)) |
| gaussian/g16.c01 | chem | [Gaussian](../software/gaussian.md) | Nibi | paquet logiciel d'usage général en chimie computationnelle (site web : [gaussian.com](http://gaussian.com/)) |
| gaussian/g03.d01 | chem | [Gaussian](../software/gaussian.md) | Fir | paquet logiciel d'usage général en chimie computationnelle (site web : [gaussian.com](http://gaussian.com/)) |
| gaussian/g09.b01 | chem | [Gaussian](../software/gaussian.md) | Fir | paquet logiciel d'usage général en chimie computationnelle (site web : [gaussian.com](http://gaussian.com/)) |
| gaussian/g09.e01 | chem | [Gaussian](../software/gaussian.md) | Fir | paquet logiciel d'usage général en chimie computationnelle (site web : [gaussian.com](http://gaussian.com/)) |
| gaussian/g16.a03 | chem | [Gaussian](../software/gaussian.md) | Fir | paquet logiciel d'usage général en chimie computationnelle (site web : [gaussian.com](http://gaussian.com/)) |
| gaussian/g16.b01 | chem | [Gaussian](../software/gaussian.md) | Fir | paquet logiciel d'usage général en chimie computationnelle (site web : [gaussian.com](http://gaussian.com/)) |
| gaussian/g16.c01 | chem | [Gaussian](../software/gaussian.md) | Fir | paquet logiciel d'usage général en chimie computationnelle (site web : [gaussian.com](http://gaussian.com/))