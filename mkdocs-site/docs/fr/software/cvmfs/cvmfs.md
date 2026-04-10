---
title: "CVMFS/fr"
slug: "cvmfs"
lang: "fr"

source_wiki_title: "CVMFS/fr"
source_hash: "ab278a91942391c1568a1cd76cf706ae"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T05:18:32.792987+00:00"

tags:
  - cvmfs

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

Nous utilisons CVMFS (CERN Virtual Machine File System) pour distribuer les logiciels, les données et d'autres contenus. Pour plus d'information, voir [le site web](https://cernvm.cern.ch/fs/) et [la section documentation](https://cvmfs.readthedocs.io/). Pour savoir comment configurer un client CVMFS, voir notre page wiki [Accès à CVMFS](accessing-cvmfs.md).

## Introduction
CVMFS est un système de distribution de logiciels distribué en lecture seule, implémenté en tant que système de fichiers POSIX dans l'espace utilisateur (FUSE) à l'aide du transport HTTP. Il a été développé à l'origine pour les expériences du grand collisionneur de hadrons au CERN afin de fournir des logiciels aux machines virtuelles et de remplacer diverses zones d'installation de logiciels partagés et des systèmes de gestion de paquets sur de nombreux sites informatiques. Conçu pour fournir des logiciels de manière rapide, évoluable et fiable, son utilisation s'est rapidement développée ces dernières années pour inclure des dizaines de projets, ~10<sup>10</sup> fichiers et répertoires, ~10<sup>2</sup> sites de calcul et ~10<sup>5</sup> clients à travers le monde. Le [CernVM Monitor](https://cvmfs-monitor-frontend.web.cern.ch/) montre plusieurs groupes de recherche qui utilisent CVMFS et les sites des strates qui répliquent leurs référentiels.

### Description
*   Une seule copie du logiciel doit être conservée et peut être propagée et utilisée sur plusieurs sites. Les logiciels couramment utilisés peuvent être installés sur CVMFS afin de minimiser la gestion des logiciels à distance.
*   Les applications logicielles et leurs prérequis peuvent être exécutés à partir de CVMFS, éliminant ainsi toute exigence sur le type de distribution Linux ou le niveau de la version d'un nœud client.
*   La pile logicielle du projet et le système d’exploitation peuvent être découplés. Dans le cas particulier du nuage (cloud), ceci permet d'accéder au logiciel dans une machine virtuelle sans être à l’intérieur de l'image de la machine virtuelle, ce qui permet aux images et aux logiciels d'être mis à jour et distribués séparément.
*   La gestion des versions du contenu se fait via les révisions du catalogue du référentiel. Les mises à jour sont validées dans des transactions et peuvent être restaurées à un état antérieur.
*   Les mises à jour sont propagées aux clients de manière automatique et atomique.
*   Les clients peuvent voir les versions historiques du contenu du référentiel.
*   Les fichiers sont récupérés à l'aide du protocole HTTP standard. Les nœuds clients ne nécessitent pas l'ouverture de ports ou de pare-feu.
*   La tolérance aux pannes et la fiabilité sont obtenues en utilisant plusieurs serveurs proxy et serveurs de strates redondants. Les clients basculent de manière transparente vers le prochain proxy ou serveur disponible.
*   La mise en cache hiérarchique rend le modèle CVMFS hautement évoluable et robuste, et minimise le trafic réseau. Il peut y avoir plusieurs niveaux dans la hiérarchie de diffusion et de mise en cache du contenu :
    *   La strate 0 contient la copie principale du référentiel.
    *   Plusieurs serveurs de strate 1 répliquent le contenu du référentiel à partir de la strate 0.
    *   Les serveurs proxy HTTP mettent en cache les requêtes réseau des clients vers les serveurs de la strate 1.
    *   Le client CVMFS télécharge les fichiers à la demande dans le ou les caches clients locaux.
        *   Deux niveaux de cache local peuvent être utilisés, par exemple un cache SSD rapide et un grand cache HDD. Un système de fichiers d’une grappe peut également être utilisé comme cache partagé pour tous les nœuds.
*   Les clients CVMFS ont un accès en lecture au système de fichiers.
*   En utilisant les arborescences Merkle et le stockage adressable par le contenu, et en codant les métadonnées dans les catalogues, toutes les métadonnées sont traitées comme des données, et sont pratiquement toutes immuables et se prêtent parfaitement à la mise en cache.
*   Le stockage des métadonnées et les opérations évoluent à l'aide de catalogues imbriqués, permettant la résolution des requêtes de métadonnées à effectuer localement par le client.
*   L'intégrité et l'authenticité des fichiers sont vérifiées à l'aide de hachages cryptographiques signés, évitant ainsi la corruption ou la falsification des données.
*   Côté serveur, la déduplication et la compression automatiques minimisent l'utilisation du stockage. Côté client, la segmentation des fichiers et l'accès à la demande minimisent l'utilisation du stockage.
*   Des configurations polyvalentes peuvent être déployées en écrivant des assistants d'autorisation ou des extensions de cache pour interagir avec des fournisseurs externes d'autorisation ou de stockage.

## Références
*   [2018-01-31 Compute Canada Software Installation and Distribution](https://indico.cern.ch/event/608592/contributions/2858287/), atelier (2018)
*   [2019-06-03 CVMFS at Compute Canada](https://indico.cern.ch/event/757415/contributions/3433887/), atelier (2019)
*   [2019-06-20 Providing A Unified User Environment for Canada’s National Advanced Computing Centers](https://guidebook.com/g/canheitarc2019/#/session/23411098), CANHEIT (2019)
*   [2019-07-28 Providing a Unified Software Environment for Canada’s National Advanced Computing Centers](https://dl.acm.org/doi/10.1145/3332186.3332210), Practice and Experience in Advanced Research Computing (2019)
    *   [version PDF](https://ssl.linklings.net/conferences/pearc/pearc19_program/views/includes/files/pap139s3-file1.pdf)
*   [2019-08-01 Providing a Unified Software Environment for Canada’s National Advanced Computing Centers](https://ssl.linklings.net/conferences/pearc/pearc19_program/views/includes/files/pap139s3-file1.pdf), PEARC (2019)
*   [2020-09-24 Distributing software across campuses and the world with CVMFS](https://bc.net/distributing-software-across-campuses-and-world-cernvm-fs-0), BCNET Connect (2020)
*   [2021-01-26 CVMFS Tutorial](https://cvmfs-contrib.github.io/cvmfs-tutorial-2021/) EasyBuild User Meeting (2021)
    *   [diapositives](https://cvmfs-contrib.github.io/cvmfs-tutorial-2021/eum21-cvmfs-tutorial-slides.pdf)
*   [Unlimited scientific libraries and applications in Kubernetes, instantly!](https://towardsdatascience.com/unlimited-scientific-libraries-and-applications-in-kubernetes-instantly-b69b192ec5e5) article dans Towards Data Science (2021-09-27)
    *   démontre l'approche de Calcul Canada pour la distribution des applications de recherche (le déploiement décrit est utilisé pour une seule grappe de démonstration et utilise CephFS plutôt que CVMFS)
*   [2022-02-16 EESSI: A cross-platform ready-to-use optimised scientific software stack](https://onlinelibrary.wiley.com/doi/10.1002/spe.3075), Journal of Software: Practice and Experience (2022)
    *   démontre l'approche de Calcul Canada pour la distribution de logiciels à la communauté de la recherche au sens large, avec plus de soutien en rapport avec le matériel
*   [2022-09-13 CVMFS in Canadian Advanced Research Computing](https://indico.cern.ch/event/1079490/contributions/4939532/), atelier (2022)