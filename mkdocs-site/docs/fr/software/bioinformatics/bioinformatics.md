---
title: "Bioinformatics/fr"
slug: "bioinformatics"
lang: "fr"

source_wiki_title: "Bioinformatics/fr"
source_hash: "07229d0094c2cb8d664fe1109c211ad0"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:48:45.565469+00:00"

tags:
  []

keywords:
  - "CVMFS"
  - "Centre canadien de génomique computationnelle"
  - "site Web"
  - "computationalgenomics.ca"
  - "génomique"
  - "bio-informatique"
  - "ref.mugqic"
  - "bases de données"
  - "adresse web"
  - "outils de bio-informatique"
  - "génomes de référence"
  - "soft.mugqic"
  - "lien internet"
  - "logiciels"
  - "calcul haute performance"

questions:
  - "Comment l'Alliance accompagne-t-elle les chercheurs dans l'exécution de leurs flux de travail en bio-informatique sur les systèmes de calcul haute performance ?"
  - "Quelles sont les solutions recommandées pour accéder aux logiciels de bio-informatique ou les installer, compte tenu des restrictions liées à Conda ?"
  - "Où sont stockées les bases de données biologiques de référence sur les grappes et comment le Centre canadien de génomique computationnelle (C3G) contribue-t-il à ces ressources ?"
  - "Quelle est l'adresse exacte du site Web mentionné dans le texte ?"
  - "Quel domaine scientifique ou organisation est suggéré par le nom de domaine de ce site ?"
  - "Quelle méthode d'accès alternative est indiquée par l'utilisation du mot « ou » au début de la phrase ?"
  - "Que contient exactement le répertoire `soft.mugqic` ?"
  - "Quelles informations biologiques sont disponibles dans le répertoire `ref.mugqic` ?"
  - "Qui doit-on contacter et à quelle adresse pour toute question concernant les référentiels `mugqic` ?"
  - "Quelle est l'adresse exacte du site Web mentionné dans le texte ?"
  - "Quel domaine scientifique ou organisation est suggéré par le nom de domaine de ce site ?"
  - "Quelle méthode d'accès alternative est indiquée par l'utilisation du mot « ou » au début de la phrase ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# Généralités
La bio-informatique est l'application de méthodes de calcul en recherche biologique et biomédicale qui comporte souvent des données à grande échelle générées par le séquençage de nouvelle génération (NGS), la protéomique, la métabolomique et d'autres technologies expérimentales à haut débit. Les flux de travail courants sur les systèmes de calcul haute performance incluent l'assemblage du génome et du transcriptome, l'appel de variants, la quantification de l'expression génétique, le profilage épigénomique et l'intégration multi-omique.

Bien que la bio-informatique recoupe des domaines comme la biologie computationnelle et la biologie des systèmes, l'utilisation d'outils spécialisés avec de vastes ensembles de données la rend particulièrement adaptée aux environnements de calcul haute performance. L'Alliance prend en charge un large éventail d'applications et de flux de travail bio-informatiques par des modules préinstallés, des environnements conteneurisés et des systèmes de gestion des flux de travail.

Une équipe nationale dédiée à la bio-informatique est disponible pour vous accompagner dans le choix d'outils et le développement et l'optimisation des pipelines. Pour une liste détaillée des logiciels pris en charge, voir la liste ci-dessous.

## Logiciels disponibles

Voyez [la liste des modules disponibles sur nos grappes](available-software.md#modules-disponibles-sur-toutes-les-grappes). Cliquez sur l'entête de la colonne *Type*; le type *bio* identifie les applications en bio-informatique.

De nombreux logiciels peuvent être installés via Conda.
Nous ne prenons pas directement en charge l'utilisation de Conda sur nos systèmes pour des raisons expliquées à la page [Anaconda](anaconda.md).
Cependant, vous pouvez créer un environnement Conda dans un conteneur Apptainer; voir [Travailler avec Conda](apptainer.md#travailler-avec-conda) pour les détails.

Plusieurs de ces logiciels sont disponibles sous forme de paquets Python. Les paquets adaptés à nos systèmes se trouvent sur [notre page Wheels Python](available-python-wheels.md).
Vous trouverez d'autres paquets sur l'internet.
Pour plus d'information, voir [notre page Python](python.md#creer-et-utiliser-un-environnement-virtuel).

## Données

Plusieurs bases de données sont disponibles sur nos grappes, dont la base de données non redondante BLAST du NCBI, la base de données génétiques d'AlphaFold et la base de données standard de Kraken2:
* voir le répertoire **/cvmfs/bio.data.computecanada.ca**
Pour d'autres bases de données et ensembles de données, voir
* /cvmfs/ref.mugqic (prise en charge par C3G, voir ci-dessous)
* /cvmfs/ref.galaxy
* /cvmfs/public.data.computecanada.ca
* /datashare Graham Reference Dataset Repository, [documentation externe](https://helpwiki.sharcnet.ca/wiki/Graham_Reference_Dataset_Repository)

!!! important
    Veuillez noter que **ce ne sont pas tous les ensembles de données qui sont disponibles sur toutes nos grappes** et que le service de soutien technique peut varier selon le système. Cependant, nous tenterons de vous assister lorsque c'est possible.

## Ressource externe de soutien

Affilié à l'Université McGill, le Centre canadien de génomique computationnelle (C3G) collabore avec l'Alliance pour offrir des services de bio-informatique sur mesure et soutient la communauté de recherche en tant que membre de l'équipe nationale de bio-informatique de l'Alliance.
Le C3G maintient deux référentiels [CVFMS](cvmfs.md):
* `soft.mugqic` qui contient de nombreux outils de bio-informatiques *open source* installés sous forme de modules,
* `ref.mugqic` qui contient des génomes de référence et leurs indices et annotations pour de nombreux organismes modèles courants.
Pour toute demande ou question concernant les référentiels `mugqic`, contactez le C3G à [tech.dev@computationalgenomics.ca](mailto:tech.dev@computationalgenomics.ca)
ou via leur site Web [computationalgenomics.ca](https://computationalgenomics.ca/?lang=fr).