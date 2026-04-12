---
title: "Available software/fr"
slug: "available_software"
lang: "fr"

source_wiki_title: "Available software/fr"
source_hash: "0465529914aadabb1de6d429b6ecbd2f"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:39:50.113791+00:00"

tags:
  []

keywords:
  - "logiciels disponibles"
  - "interface web"
  - "gestion des données"
  - "colonne Description"
  - "outils intégrés"
  - "Trans-Proteomic Pipeline (TPP)"
  - "chimie computationnelle"
  - "Cedar"
  - "documentation"
  - "logiciels"
  - "grappes"
  - "prérequis"
  - "analyse de données protéomiques MS/MS"
  - "bio-informatique"
  - "SAS/9.4"
  - "tri"
  - "suite logicielle"
  - "plateforme nationale"
  - "analyse prédictive"
  - "environnement logiciel"
  - "système de modules Lmod"
  - "modules"

questions:
  - "Comment peut-on demander l'installation ou la mise à jour d'un logiciel sur la plateforme nationale ?"
  - "Quelle est la procédure à suivre pour utiliser un logiciel non installé par défaut et pour gérer les paquets spécifiques à Python, R ou Perl ?"
  - "Quelle alternative à Docker est recommandée pour l'utilisation de contenants sur les grappes de calcul ?"
  - "Quelles sont les différentes catégories de domaines scientifiques pour lesquelles des logiciels sont disponibles ?"
  - "Pourquoi certains paquets logiciels sont-ils installés localement sur des grappes spécifiques plutôt que dans le système de fichiers global CVMFS ?"
  - "Quelle est la procédure à suivre pour qu'un groupe de recherche puisse obtenir et utiliser une instance de la plateforme Galaxy sur la grappe Cedar ?"
  - "Comment peut-on consulter les prérequis et la description d'un logiciel dans l'interface ?"
  - "Où se trouve le lien permettant d'accéder à la documentation spécifique d'un logiciel ?"
  - "Quelle est la manipulation à effectuer pour trier et lister les logiciels en fonction de leur type ?"
  - "Quelles sont les principales applications et fonctionnalités de la suite logicielle SAS/9.4 ?"
  - "Quelle organisation est responsable du développement de cette suite logicielle ?"
  - "Quelles sont les conditions et l'origine de la licence permettant d'utiliser SAS sur le système Cedar ?"
  - "Qu'est-ce que le Trans-Proteomic Pipeline (TPP) et quel type de données permet-il d'analyser ?"
  - "Par quelle entité cette collection d'outils intégrés a-t-elle été développée ?"
  - "Comment les groupes peuvent-ils accéder à l'interface web du TPP (tpp_gui) sur le système Cedar ?"
  - "Qu'est-ce que le Trans-Proteomic Pipeline (TPP) et quel type de données permet-il d'analyser ?"
  - "Par quelle entité cette collection d'outils intégrés a-t-elle été développée ?"
  - "Comment les groupes peuvent-ils accéder à l'interface web du TPP (tpp_gui) sur le système Cedar ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Le tableau présenté ci-dessous montre la liste des logiciels disponibles sur la plateforme nationale. Cette liste est modifiée à l'ajout de tout nouveau logiciel. Pour demander l'installation ou la mise à jour d'un logiciel ou d'une bibliothèque, communiquez avec le [soutien technique](../support/technical_support.md). Pour utiliser notre environnement logiciel sur votre propre ordinateur, voyez notre page wiki CVMFS.

!!! warning "Disponibilité"
    **Certains logiciels ne sont peut-être pas disponibles dans l'environnement standard `StdEnv` que vous avez chargé.**

    `StdEnv/2020` est maintenant caché ou obsolète sur les nouveaux systèmes (voir [StdEnv/2020](standard_software_environments.md#stdenv2020)).

## Notes
Pour utiliser un logiciel qui n'est pas déjà installé par défaut, vous devez charger le module qui s'applique. Pour plus d'information sur comment utiliser le système de modules Lmod, consultez [Utiliser des modules](utiliser_des_modules.md). Prenez note que certains modules prérequis sont chargés par défaut.

**Points à retenir à propos des logiciels disponibles**

*   La plupart des modules Python ne sont pas installés en tant que modules (Lmod), mais en tant que [paquets binaires](available_python_wheels.md) (_wheels_) localisés sous `/cvmfs/soft.computecanada.ca/custom/python/wheelhouse/`; [TensorFlow](../software/tensorflow.md) en est un exemple. Voyez la page [Python](../software/python.md) pour des détails sur comment lister les paquets Python et les installer.
*   De même, la plupart des paquets R et Perl ne sont pas installés. Nous vous recommandons de les installer dans votre environnement personnel ou dans celui de votre groupe. Voyez les pages [R](../software/r.md) et [Perl](../software/perl.md) pour des détails sur l'installation des paquets.
*   Voyez la page Algèbre symbolique où il est question de SageMath.
*   Notez que [Docker](https://www.docker.com/) n'est pas disponible sur nos grappes, mais que [Apptainer](../software/containers/apptainer.md) peut être utilisé en chargeant le module `apptainer`. Pour convertir les contenants Docker, consultez [la documentation Apptainer](https://apptainer.org/docs/).
*   Certains logiciels listés dans le tableau ci-dessous sont sous licence et donc non accessibles directement; vous pouvez en demander l'accès au besoin. En tentant de charger le module d'un tel logiciel, vous recevrez les consignes sur comment en obtenir l'accès.
*   La plupart des paquets listés se trouvent sur toutes nos grappes. Certains cependant ne sont disponibles que sur un site en particulier en raison des restrictions liées à l'octroi des licences; voir [Modules disponibles uniquement sur certaines grappes](#modules-disponibles-uniquement-sur-certaines-grappes) ci-dessous.
*   Les paquets listés sont disponibles dans un ou plusieurs de nos environnements logiciels standards. Dans certains cas peu fréquents, vous devrez charger un environnement logiciel différent pour avoir accès à un paquet en particulier; voyez [Environnements logiciels standards](standard_software_environments.md).
*   Plusieurs paquets reliés au système d’exploitation comme [Autotools](autotools.md), [Make](make.md) et [Git](../software/git.md) ne sont pas installés en tant que modules, mais font partie de l'environnement par défaut; ils ne paraissent pas dans le tableau.

## Modules disponibles sur toutes les grappes
Le tableau suivant liste les logiciels pour lesquels un module d'environnement est disponible. Certains modules peuvent être chargés avec la commande `module load` alors que d'autres nécessitent des conditions particulières.
Dans la colonne *Description*, cliquez sur l'option pour afficher les détails afin de connaître les prérequis et lire une description sommaire du logiciel (en anglais).
Un lien dans la colonne *Documentation* conduit à la documentation spécifique sur le logiciel.
Pour lister les logiciels selon leur type, effectuez un tri en cliquant sur l'en-tête de la colonne *Type*.

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
*   vis (visualisation).

Les logiciels pour les architectures obsolètes se trouvent respectivement dans AVX et SSE3.

=== "AVX512 (Fir, Nibi, Rorqual, Trillium, Killarney, tamIA, Vulcan)"
    <!-- Le contenu du tableau des modules AVX512 serait ici -->
=== "AVX2 (Narval)"
    <!-- Le contenu du tableau des modules AVX2 serait ici -->

## Modules disponibles uniquement sur certaines grappes
La plupart des applications sont installées dans CVMFS, un système de fichiers qui facilite la gestion du grand nombre des paquets que nous offrons. Cependant, d'autres paquets ne sont installés que dans certains sites, principalement pour des raisons de licence.

### Logiciels installés localement

| Module             | Type | Documentation     | Grappe | Description                                                                                                                                                                                                                                                                                                                                                                |
| :----------------- | :--- | :---------------- | :----- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| adf/2016.106       | chem | [ADF](../software/adf.md)     | Nibi   | Amsterdam Density Functional Modeling Suite; recherche en chimie computationnelle                                                                                                                                                                                                                                                                                  |
| adf/2017.207       | chem | [ADF](../software/adf.md)     | Nibi   | Amsterdam Density Functional Modeling Suite; recherche en chimie computationnelle                                                                                                                                                                                                                                                                                  |
| adf/2018.104       | chem | [ADF](../software/adf.md)     | Nibi   | Amsterdam Density Functional Modeling Suite; recherche en chimie computationnelle                                                                                                                                                                                                                                                                                  |
| adf/2019.305       | chem | [ADF](../software/adf.md)     | Nibi   | Amsterdam Density Functional Modeling Suite; recherche en chimie computationnelle                                                                                                                                                                                                                                                                                  |
| ams/2020.102       | chem | [AMS](../software/ams.md)     | Nibi   | Amsterdam Modeling Suite                                                                                                                                                                                                                                                                                                                                           |
| amber/16           | chem | [AMBER](../software/amber.md) | Nibi   | ensemble d'applications pour effectuer des simulations en dynamique moléculaire                                                                                                                                                                                                                                                                                    |
| dirac/16.0         | phys |                   | Cedar  | Direct Iterative Relativistic All-electron Calculations; calcule les propriétés moléculaires avec des méthodes de chimie quantique relativiste ([site web](http://diracprogram.org))                                                                                                                                                                                   |
| dirac/17.0         | phys |                   | Cedar  | Direct Iterative Relativistic All-electron Calculations; calcule les propriétés moléculaires avec des méthodes de chimie quantique relativiste ([site web](http://diracprogram.org))                                                                                                                                                                                   |
| galaxy/20.01       | bio  |                   | Cedar  | plateforme d'analyse, de gestion et d'archivage des données qui rend la bio-informatique accessible aux chercheurs sans compétences en programmation ou en administration de systèmes. Sur Cedar, chaque groupe peut avoir une instance de Galaxy qui est exécutée dans un compte partagé; ce compte est créé par une ou un administrateur de système. Contactez le [soutien technique](../support/technical_support.md). ([site web](https://usegalaxy.org/)) |
| gaussian/g03.d01   | chem | [Gaussian](../software/gaussian.md) | Nibi   | paquet logiciel d'usage général en chimie computationnelle ([site web](http://gaussian.com/))                                                                                                                                                                                                                                                                        |
| gaussian/g09.e01   | chem | [Gaussian](../software/gaussian.md) | Nibi   | paquet logiciel d'usage général en chimie computationnelle ([site web](http://gaussian.com/))                                                                                                                                                                                                                                                                        |
| gaussian/g16.b01   | chem | [Gaussian](../software/gaussian.md) | Nibi   | paquet logiciel d'usage général en chimie computationnelle ([site web](http://gaussian.com/))                                                                                                                                                                                                                                                                        |
| gaussian/g16.c01   | chem | [Gaussian](../software/gaussian.md) | Nibi   | paquet logiciel d'usage général en chimie computationnelle ([site web](http://gaussian.com/))                                                                                                                                                                                                                                                                        |
| gaussian/g03.d01   | chem | [Gaussian](../software/gaussian.md) | Fir    | paquet logiciel d'usage général en chimie computationnelle ([site web](http://gaussian.com/))                                                                                                                                                                                                                                                                        |
| gaussian/g09.b01   | chem | [Gaussian](../software/gaussian.md) | Fir    | paquet logiciel d'usage général en chimie computationnelle ([site web](http://gaussian.com/))                                                                                                                                                                                                                                                                        |
| gaussian/g09.e01   | chem | [Gaussian](../software/gaussian.md) | Fir    | paquet logiciel d'usage général en chimie computationnelle ([site web](http://gaussian.com/))                                                                                                                                                                                                                                                                        |
| gaussian/g16.a03   | chem | [Gaussian](../software/gaussian.md) | Fir    | paquet logiciel d'usage général en chimie computationnelle ([site web](http://gaussian.com/))                                                                                                                                                                                                                                                                        |
| gaussian/g16.b01   | chem | [Gaussian](../software/gaussian.md) | Fir    | paquet logiciel d'usage général en chimie computationnelle ([site web](http://gaussian.com/))                                                                                                                                                                                                                                                                        |
| gaussian/g16.c01   | chem | [Gaussian](../software/gaussian.md) | Fir    | paquet logiciel d'usage général en chimie computationnelle ([site web](http://gaussian.com/))                                                                                                                                                                                                                                                                        |
| gbrowse/2.56       | bio  | [GBrowse](../software/bioinformatics/gbrowse.md) | Cedar  | outil composé d’une base de données combinée à des pages web interactives pour manipuler et visualiser des données génomiques ([site web](http://gmod.org/wiki/GBrowse))                                                                                                                                                                                              |
| sas/9.4            | math |                   | Cedar  | suite logicielle développée par le *SAS Institute for advanced analytics* pour l'analyse multivariée, l'intelligence d'affaires, la gestion des données et l'analyse prédictive. Sur Cedar, une licence de l'*Alberta School of Business* permet l'utilisation de SAS à quiconque est admissible. ([site web](https://www.sas.com/en_ca/home.html0))                            |
| TPP/5.1.0          | bio  |                   | Cedar  | Trans-Proteomic Pipeline (TPP) est une collection d'outils intégrés développée au SPC pour l'analyse de données protéomiques MS/MS. Cedar offre aussi sur demande une interface web TPP (tpp_gui) par groupe.                                                                                                                                                               |