---
title: "Bioinformatics/fr"
slug: "bioinformatics"
lang: "fr"

source_wiki_title: "Bioinformatics/fr"
source_hash: "ae586530b4d56e0f347d689465cad4aa"
last_synced: "2026-05-17T14:59:09.465984+00:00"
last_processed: "2026-05-17T15:17:34.792174+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: true
  qa_generated: true
---

## Généralités
La bio-informatique est l'application de méthodes de calcul en recherche biologique et biomédicale qui comporte souvent des données à grande échelle générées par le séquençage de nouvelle génération (NGS), la protéomique, la métabolomique et d'autres technologies expérimentales à haut débit. Les flux de travail courants sur les systèmes de calcul haute performance incluent l'assemblage du génome et du transcriptome, l'appel de variants, la quantification de l'expression génétique, le profilage épigénomique et l'intégration multiomique.

Bien que la bio-informatique recoupe des domaines comme la biologie computationnelle et la biologie des systèmes, l'utilisation d'outils spécialisés avec de vastes ensembles de données la rend particulièrement adaptée aux environnements de calcul haute performance. L'Alliance prend en charge un large éventail d'applications et de flux de travail bio-informatiques par des modules préinstallés, des environnements conteneurisés et des systèmes de gestion des flux de travail.

Une équipe nationale dédiée à la bio-informatique peut vous accompagner dans le choix d'outils et le développement et l'optimisation des pipelines.

## Logiciels disponibles

Voyez la liste des modules disponibles sur nos grappes. Cliquez sur l'entête de la colonne *Type*; le type *bio* identifie les applications en bio-informatique.

De nombreux logiciels peuvent être installés via Conda.
Nous ne prenons pas directement en charge l'utilisation de Conda sur nos systèmes pour des raisons expliquées à la page Anaconda.
Cependant, vous pouvez créer un environnement Conda dans un conteneur Apptainer; voir Travailler avec Conda pour les détails.

Plusieurs de ces logiciels sont disponibles sous forme de paquets Python. Les paquets adaptés à nos systèmes se trouvent sur notre page Wheels Python.
Vous trouverez d'autres paquets sur l'internet.
Pour plus d'information, voir notre page Python.

### useGalaxy.ca

[UseGalaxy.ca](https://starthere.usegalaxy.ca/) est le principal serveur Galaxy pour le Canada. Son interface web permet les analyses, les flux de travail et la visualisation, évitant ainsi de travailler en ligne de commande.

UseGalaxy.ca est un bon outil pour les analyses de données courantes en sciences de la vie via une interface graphique. Il donne accès à des outils, des flux de travail, des génomes de référence, des jeux de données d'annotation et des ressources de formation maintenus par la communauté. Vous pouvez vous connecter avec votre authentification institutionnelle ou via votre compte Google.

UseGalaxy.ca est un bon choix si

*   vous préférez une interface web;
*   vos flux de travail standards ne nécessitent pas l'installation locale de logiciels;
*   vous utilisez vos flux de travail reproductibles pour apprendre, enseigner ou partager avec d'autres;
*   vos analyses respectent les politiques et les limites de ressources du service public de Galaxy.

Pour plus d'information, voir notre page wiki pour Galaxy.

**Autres références**

*   [Page d'accueil du site web UseGalaxy](https://starthere.usegalaxy.ca/index_fr.html)
*   [A propos de UseGalaxy Canada](https://starthere.usegalaxy.ca/about_fr.html)
*   [Transfert de données](https://starthere.usegalaxy.ca/data_transfer_fr.html)
*   [Politique d'utilisation acceptable](https://starthere.usegalaxy.ca/aup_fr.html)
*   [Niveaux de service](https://starthere.usegalaxy.ca/service_levels_fr.html)

## Données

Plusieurs bases de données sont disponibles sur nos grappes, dont la base de données sans redondance BLAST du NCBI, la base de données génétiques d'AlphaFold et la base de données standard de Kraken2 :
*   voir le répertoire `**`/cvmfs/bio.data.computecanada.ca`**`
Pour d'autres bases de données et ensembles de données, voir
*   `/cvmfs/ref.mugqic` (prise en charge par C3G, voir ci-dessous)
*   `/cvmfs/ref.galaxy`
*   `/cvmfs/public.data.computecanada.ca`
*   `/datashare` Graham Reference Dataset Repository, [documentation externe](https://helpwiki.sharcnet.ca/wiki/Graham_Reference_Dataset_Repository)

!!! note
    Veuillez noter que **ce ne sont pas tous les ensembles de données qui sont disponibles sur toutes nos grappes** et que le service de soutien technique peut varier selon le système. Cependant, nous tenterons de vous assister lorsque c'est possible.

## Ressource externe de soutien

Affilié à l'Université McGill, le Centre canadien de génomique computationnelle (C3G) collabore avec l'Alliance pour offrir des services de bio-informatique sur mesure et soutient la communauté de recherche en tant que membre de l'équipe nationale de bio-informatique de l'Alliance.
Le C3G maintient deux référentiels CVFMS :
*   `soft.mugqic` qui contient de nombreux outils de bio-informatiques *open source* installés sous forme de modules,
*   `ref.mugqic` qui contient des génomes de référence et leurs indices et annotations pour de nombreux organismes modèles courants.
Pour toute demande ou question concernant les référentiels `mugqic`, contactez le C3G à [tech.dev@computationalgenomics.ca](mailto:tech.dev@computationalgenomics.ca)
ou via leur site Web [computationalgenomics.ca](https://computationalgenomics.ca/?lang=fr).