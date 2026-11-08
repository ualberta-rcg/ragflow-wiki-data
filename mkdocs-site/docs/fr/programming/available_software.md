---
title: "Available software/fr"
slug: "available_software"
lang: "fr"

source_wiki_title: "Available software/fr"
source_hash: "a4b372d20863e9093bf673c656b7fe43"
last_synced: "2026-11-08T02:07:32.985064+00:00"
last_processed: "2026-11-08T02:51:02.775462+00:00"

tags:
  []

keywords:
  - "logiciels installés localement"
  - "paquets Python wheels"
  - "Apptainer"
  - "modules Lmod"
  - "Modules AVX/AVX2/AVX512"
  - "colonne Type"
  - "colonne Description"
  - "tri"
  - "bio‑informatique"
  - "prérequis"
  - "documentation"
  - "logiciels disponibles"
  - "chimie computationnelle"
  - "CVMFS"

questions:
  - "Comment demander l'installation ou la mise à jour d'un logiciel ou d'une bibliothèque sur la plateforme nationale ?"
  - "Quels sont les moyens d'utiliser les paquets Python, R ou Perl qui ne sont pas installés en tant que modules Lmod ?"
  - "Comment accéder aux logiciels sous licence ou disponibles uniquement sur certaines grappes ?"
  - "Quels logiciels sont installés localement sur les grappes spécifiques (Nibi, Fir, etc.) et quelles sont leurs descriptions ?"
  - "Comment les modules sont-ils répartis selon les architectures (AVX, AVX2, AVX512) et où accéder aux informations détaillées pour chaque architecture ?"
  - "Pourquoi certains paquets ne sont disponibles que sur certaines grappes et quels critères (par exemple licences) déterminent cette répartition ?"
  - "Comment accéder aux prérequis et à la description sommaire d’un logiciel dans la colonne « Description » ?"
  - "Où se trouve le lien permettant d’ouvrir la documentation spécifique d’un logiciel ?"
  - "Comment trier la liste des logiciels par type et quels sont les types disponibles ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

La liste ci-dessous présente les logiciels disponibles sur la plateforme nationale. Cette liste est mise à jour à l'ajout de tout nouveau logiciel. Pour demander l'installation ou la mise à jour d'un logiciel ou d'une bibliothèque, communiquez avec le [soutien technique](../support/technical_support.md). Pour utiliser notre environnement logiciel sur votre propre ordinateur, consultez [notre page wiki CVMFS](../software/cvmfs/accessing_cvmfs.md).

!!! warning "Disponibilité"
    **Certains logiciels ne sont peut-être pas disponibles dans l'environnement standard `StdEnv` que vous avez chargé.**

    `StdEnv/2020` est maintenant caché ou obsolète sur les nouveaux systèmes (voir [StdEnv/2020](standard_software_environments.md)).

## Notes
Pour utiliser un logiciel qui n'est pas déjà installé par défaut, vous devez charger le module qui s'applique. Pour plus d'information sur l'utilisation du système de modules Lmod, consultez [Utiliser des modules](utiliser_des_modules.md). Prenez note que certains modules prérequis sont chargés par défaut.

**Points à retenir à propos des logiciels disponibles**

*   La plupart des modules Python ne sont pas installés en tant que modules (Lmod), mais en tant que [paquets binaires](available_python_wheels.md) (*wheels*) localisés sous `/cvmfs/soft.computecanada.ca/custom/python/wheelhouse/`; [TensorFlow](../software/tensorflow.md) en est un exemple. Consultez la page [Python](../software/python.md) pour des détails sur la façon de lister les paquets Python et de les installer.
*   De même, la plupart des paquets R et Perl ne sont pas installés. Nous vous recommandons de les installer dans votre environnement personnel ou dans celui de votre groupe. Consultez les pages [R](../software/r.md) et [Perl](../software/perl.md) pour des détails sur l'installation des paquets.
*   Consultez la page [Algèbre symbolique](../software/symbolic_algebra_software.md) où il est question de SageMath.
*   Notez que [Docker](https://www.docker.com/) n'est pas disponible sur nos grappes, mais que [Apptainer](../software/containers/apptainer.md) peut être utilisé en chargeant le module `apptainer`. Pour convertir les contenants Docker, consultez [la documentation Apptainer](https://apptainer.org/docs/).
*   Certains logiciels listés dans les tableaux sont sous licence et donc non accessibles directement; vous pouvez en demander l'accès au besoin. En tentant de charger le module d'un tel logiciel, vous recevrez les consignes sur la façon d'en obtenir l'accès.
*   La plupart des paquets listés se trouvent sur toutes nos grappes. Certains cependant ne sont disponibles que sur un site en particulier en raison des restrictions liées à l'octroi des licences; voir [Modules disponibles uniquement sur certaines grappes](#modules-disponibles-uniquement-sur-certaines-grappes) ci-dessous.
*   Les paquets listés sont disponibles dans un ou plusieurs de nos environnements logiciels standards. Dans certains cas peu fréquents, vous devrez charger un environnement logiciel différent pour avoir accès à un paquet en particulier; voyez [Environnements logiciels standards](standard_software_environments.md).
*   Plusieurs paquets reliés au système d’exploitation comme [Autotools](autotools.md), [Make](make.md) et [Git](../software/git.md) ne sont pas installés en tant que modules, mais font partie de l'environnement par défaut; ils ne paraissent pas dans les tableaux.

## Modules disponibles sur toutes les grappes
Les tableaux suivants listent les logiciels pour lesquels un module d'environnement est disponible. Certains modules peuvent être chargés avec la commande `module load` alors que d'autres nécessitent des conditions particulières.

La colonne *Description* offre une description sommaire du logiciel (en anglais) et, le cas échéant, ses prérequis. La colonne *Documentation* fournit un lien vers la documentation spécifique sur le logiciel. Il est possible de lister les logiciels selon leur type pour un meilleur aperçu.

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
    La liste complète des modules disponibles pour les architectures AVX512 sur ces grappes sera affichée ici.

=== "AVX2 (Narval)"
    La liste complète des modules disponibles pour l'architecture AVX2 sur la grappe Narval sera affichée ici.

## Modules disponibles uniquement sur certaines grappes
La plupart des applications sont installées dans CVMFS, un système de fichiers qui facilite la gestion du grand nombre des paquets que nous offrons. Cependant, d'autres paquets ne sont installés que dans certains sites, principalement pour des raisons de licence.

Logiciels installés localement

| Module | Type | Documentation | Grappe | Description |
| :----- | :--- | :------------ | :----- | :---------- |
| adf/2016.106 | chem | [ADF](../software/adf.md) | Nibi | Amsterdam Density Functional Modeling Suite; recherche en chimie computationnelle |
| adf/2017.207 | chem | [ADF](../software/adf.md) | Nibi | Amsterdam Density Functional Modeling Suite; recherche en chimie computationnelle |
| adf/2018.104 | chem | [ADF](../software/adf.md) | Nibi | Amsterdam Density Functional Modeling Suite; recherche en chimie computationnelle |
| adf/2019.305 | chem | [ADF](../software/adf.md) | Nibi | Amsterdam Density Functional Modeling Suite; recherche en chimie computationnelle |
| ams/2020.102 | chem | [AMS](../software/ams.md) | Nibi | Amsterdam Modeling Suite |
| amber/16 | chem | [AMBER](../software/amber.md) | Nibi | ensemble d'applications pour effectuer des simulations en dynamique moléculaire |
| dirac/16.0 | phys | | Fir | Direct Iterative Relativistic All-electron Calculations; calcule les propriétés moléculaires avec des méthodes de chimie quantique relativiste (site web : [http://diracprogram.org](http://diracprogram.org)) |
| dirac/17.0 | phys | | Fir | Direct Iterative Relativistic All-electron Calculations; calcule les propriétés moléculaires avec des méthodes de chimie quantique relativiste (site web : [http://diracprogram.org](http://diracprogram.org)) |
| galaxy/20.01 | bio | | Fir | plateforme d'analyse, de gestion et d'archivage des données qui rend la bio-informatique accessible aux chercheurs sans compétences en programmation ou en administration de systèmes. Sur Cedar, chaque groupe peut avoir une instance de Galaxy qui est exécutée dans un compte partagé; ce compte est créé par une ou un administrateur de système. Contactez le [soutien technique](../support/technical_support.md). (site web : [https://usegalaxy.org/](https://usegalaxy.org/)) |
| gaussian/g03.d01 | chem | [Gaussian](../software/gaussian.md) | Nibi | paquet logiciel d'usage général en chimie computationnelle (site web : [http://gaussian.com/](http://gaussian.com/)) |
| gaussian/g09.e01 | chem | [Gaussian](../software/gaussian.md) | Nibi | paquet logiciel d'usage général en chimie computationnelle (site web : [http://gaussian.com/](http://gaussian.com/)) |
| gaussian/g16.b01 | chem | [Gaussian](../software/gaussian.md) | Nibi | paquet logiciel d'usage général en chimie computationnelle (site web : [http://gaussian.com/](http://gaussian.com/)) |
| gaussian/g16.c01 | chem | [Gaussian](../software/gaussian.md) | Nibi | paquet logiciel d'usage général en chimie computationnelle (site web : [http://gaussian.com/](http://gaussian.com/)) |
| gaussian/g03.d01 | chem | [Gaussian](../software/gaussian.md) | Fir | paquet logiciel d'usage général en chimie computationnelle (site web : [http://gaussian.com/](http://gaussian.com/)) |
| gaussian/g09.b01 | chem | [Gaussian](../software/gaussian.md) | Fir | paquet logiciel d'usage général en chimie computationnelle (site web : [http://gaussian.com/](http://gaussian.com/)) |
| gaussian/g09.e01 | chem | [Gaussian](../software/gaussian.md) | Fir | paquet logiciel d'usage général en chimie computationnelle (site web : [http://gaussian.com/](http://gaussian.com/)) |
| gaussian/g16.a03 | chem | [Gaussian](../software/gaussian.md) | Fir | paquet logiciel d'usage général en chimie computationnelle (site web : [http://gaussian.com/](http://gaussian.com/)) |
| gaussian/g16.b01 | chem | [Gaussian](../software/gaussian.md) | Fir | paquet logiciel d'usage général en chimie computationnelle (site web : [http://gaussian.com/](http://gaussian.com/)) |
| gaussian/g16.c01 | chem | [Gaussian](../software/gaussian.md) | Fir | paquet logiciel d'usage général en chimie computationnelle (site web : [http://gaussian.com/](http://gaussian.com/)) |
| gbrowse/2.56 | bio | [GBrowse](../software/bioinformatics/gbrowse.md) | Fir | outil composé d’une base de données combinée à des pages web interactives pour manipuler et visualiser des données génomiques (site web : [http://gmod.org/wiki/GBrowse](http://gmod.org/wiki/GBrowse)) |
| TPP/5.1.0 | bio | | Fir | Trans-Proteomic Pipeline (TPP) est une collection d'outils intégrés développée au SPC pour l'analyse de données protéomiques MS/MS. Fir offre aussi sur demande une interface web TPP (tpp_gui) pour les groupes. |