---
title: "Bioinformatics/fr"
slug: "bioinformatics"
lang: "fr"

source_wiki_title: "Bioinformatics/fr"
source_hash: "d5e7df24aeaa40900dc69acdd623c4f8"
last_synced: "2026-05-02T23:50:34.269007+00:00"
last_processed: "2026-05-03T00:39:34.894621+00:00"

tags:
  []

keywords:
  - "génomes de référence"
  - "Kraken2"
  - "AlphaFold"
  - "bio-informatique"
  - "bases de données"
  - "BLAST du NCBI"
  - "référentiels CVMFS"
  - "calcul haute performance"
  - "ensembles de données"
  - "flux de travail"
  - "useGalaxy.ca"
  - "Centre canadien de génomique computationnelle"
  - "grappes"

questions:
  - "Qu'est-ce que la bio-informatique et comment l'Alliance accompagne-t-elle les chercheurs dans l'utilisation de ces flux de travail sur ses systèmes de calcul haute performance ?"
  - "Quelles sont les différentes méthodes permettant d'accéder aux logiciels de bio-informatique, que ce soit via les modules des grappes, les conteneurs ou l'interface web UseGalaxy.ca ?"
  - "Quelles bases de données biologiques sont mises à la disposition des utilisateurs sur les grappes et dans quels répertoires peut-on y accéder ?"
  - "Quelle est la politique de disponibilité des ensembles de données sur les différentes grappes du système ?"
  - "Quel est le rôle du Centre canadien de génomique computationnelle (C3G) au sein de la communauté de recherche ?"
  - "Quelles sont les différences de contenu entre les référentiels CVMFS \"soft.mugqic\" et \"ref.mugqic\" maintenus par le C3G ?"
  - "Quelles sont les principales bases de données spécifiquement mentionnées comme étant disponibles sur les grappes ?"
  - "Dans quel répertoire principal peut-on trouver les bases de données du NCBI, d'AlphaFold et de Kraken2 ?"
  - "Quels sont les autres chemins de répertoires indiqués pour accéder à des ensembles de données supplémentaires ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Généralités
La bio-informatique est l'application de méthodes de calcul en recherche biologique et biomédicale. Elle implique souvent des données à grande échelle générées par le séquençage de nouvelle génération (NGS), la protéomique, la métabolomique et d'autres technologies expérimentales à haut débit. Les flux de travail courants sur les systèmes de calcul haute performance incluent l'assemblage du génome et du transcriptome, l'appel de variants, la quantification de l'expression génétique, le profilage épigénomique et l'intégration multi-omique.

Bien que la bio-informatique recoupe des domaines comme la biologie computationnelle et la biologie des systèmes, l'utilisation d'outils spécialisés avec de vastes ensembles de données la rend particulièrement adaptée aux environnements de calcul haute performance. L'Alliance prend en charge un large éventail d'applications et de flux de travail bio-informatiques par des modules préinstallés, des environnements conteneurisés et des systèmes de gestion des flux de travail.

Une équipe nationale dédiée à la bio-informatique est disponible pour vous accompagner dans le choix d'outils, ainsi que dans le développement et l'optimisation des pipelines. Pour une liste détaillée des logiciels pris en charge, veuillez consulter la section ci-dessous.

## Logiciels disponibles

Veuillez consulter [la liste des modules disponibles sur nos grappes](../../programming/available_software.md#modules-disponibles-sur-toutes-les-grappes). Cliquez sur l'en-tête de la colonne *Type*; le type *bio* identifie les applications en bio-informatique.

De nombreux logiciels peuvent être installés via Conda.
Nous ne prenons pas directement en charge l'utilisation de Conda sur nos systèmes pour des raisons expliquées à la page [Anaconda](../anaconda.md).
Cependant, vous pouvez créer un environnement Conda dans un conteneur Apptainer; consultez [Travailler avec Conda](../containers/apptainer.md#travailler-avec-conda) pour plus de détails.

Plusieurs de ces logiciels sont disponibles sous forme de paquets Python. Les paquets adaptés à nos systèmes se trouvent sur [notre page Wheels Python](../../programming/available_python_wheels.md).
Vous trouverez d'autres paquets sur l'internet.
Pour plus d'information, consultez [notre page Python](../python.md).

### useGalaxy.ca

[UseGalaxy.ca](https://starthere.usegalaxy.ca/) est le principal serveur public Galaxy canadien. Il offre une interface web pour effectuer des analyses bio-informatiques, des flux de travail et des tâches de visualisation de données sans que les utilisateurs aient à travailler directement sur la ligne de commande.

UseGalaxy.ca est utile pour les chercheurs qui souhaitent effectuer des analyses de données courantes en sciences de la vie via une interface graphique. Il donne accès à des outils, des flux de travail, des génomes de référence, des ensembles de données d'annotation et des ressources de formation maintenus par la communauté. Les utilisateurs peuvent se connecter en utilisant une authentification institutionnelle prise en charge ou l'authentification Google.

UseGalaxy.ca peut être une bonne option lorsque :

*   vous préférez une interface web aux outils en ligne de commande;
*   vous voulez exécuter des flux de travail bio-informatiques standards sans installer de logiciels localement;
*   vous voulez apprendre, enseigner ou partager des flux de travail bio-informatiques reproductibles;
*   votre analyse respecte les politiques et les limites de ressources du service public Galaxy.

Pour plus d'informations, veuillez consulter notre documentation technique (TUD) : [https://docs.alliancecan.ca/wiki/Galaxy](https://docs.alliancecan.ca/wiki/Galaxy)

Liens utiles :

*   [Page d'accueil de UseGalaxy.ca](https://starthere.usegalaxy.ca/)
*   [À propos de UseGalaxy.ca](https://starthere.usegalaxy.ca/about.html)
*   [Options de transfert de données](https://starthere.usegalaxy.ca/data_transfer.html)
*   [Politique d'utilisation acceptable](https://starthere.usegalaxy.ca/aup.html)
*   [Niveaux de service et conservation des données](https://starthere.usegalaxy.ca/service_levels.html)

## Données

Plusieurs bases de données sont disponibles sur nos grappes, dont la base de données non redondante BLAST du NCBI, la base de données génétiques d'AlphaFold et la base de données standard de Kraken2 :

*   `/cvmfs/bio.data.computecanada.ca`

Pour d'autres bases de données et ensembles de données, consultez :

*   `/cvmfs/ref.mugqic` (prise en charge par C3G, voir ci-dessous)
*   `/cvmfs/ref.galaxy`
*   `/cvmfs/public.data.computecanada.ca`
*   Graham Reference Dataset Repository, [documentation externe](https://helpwiki.sharcnet.ca/wiki/Graham_Reference_Dataset_Repository)

!!! warning "Disponibilité des ensembles de données"
    Veuillez noter que **ce ne sont pas tous les ensembles de données qui sont disponibles sur toutes nos grappes** et que le service de soutien technique peut varier selon le système. Cependant, nous tenterons de vous assister lorsque c'est possible.

## Ressource externe de soutien

Affilié à l'Université McGill, le Centre canadien de génomique computationnelle (C3G) collabore avec l'Alliance pour offrir des services de bio-informatique sur mesure et soutient la communauté de recherche en tant que membre de l'équipe nationale de bio-informatique de l'Alliance.
Le C3G maintient deux référentiels [CVMFS](../cvmfs/cvmfs.md) :

*   `soft.mugqic` qui contient de nombreux outils de bio-informatique *open source* installés sous forme de modules,
*   `ref.mugqic` qui contient des génomes de référence et leurs indices et annotations pour de nombreux organismes modèles courants.

Pour toute demande ou question concernant les référentiels `mugqic`, contactez le C3G à [tech.dev@computationalgenomics.ca](mailto:tech.dev@computationalgenomics.ca) ou via leur site Web [computationalgenomics.ca](https://computationalgenomics.ca/?lang=fr).