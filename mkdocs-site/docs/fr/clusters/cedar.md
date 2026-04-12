---
title: "Cedar/fr"
slug: "cedar"
lang: "fr"

source_wiki_title: "Cedar/fr"
source_hash: "a02e5b5517fe46ca17dade69ca2fac84"
last_synced: "2026-04-12T15:59:52.668416+00:00"
last_processed: "2026-04-12T18:09:43.339461+00:00"

tags:
  []

keywords:
  - "Nœuds de calcul"
  - "nœuds entiers"
  - "stockage local"
  - "type de nœud"
  - "exécution de tâches"
  - "Grappe Cedar"
  - "système de fichiers"
  - "topologie réseau"
  - "partager des nœuds"
  - "cœurs"
  - "Stockage"
  - "Réseautique haute performance"
  - "Système de fichiers"
  - "CPU et GPU"
  - "réseautique non bloquante"
  - "performance"
  - "nœuds de 48 cœurs"
  - "tâches"
  - "Cedar"
  - "mémoire disponible"
  - "tâches parallèles"
  - "nœuds"
  - "caractéristiques des nœuds"

questions:
  - "Quand le service de la grappe de calcul Cedar prendra-t-il fin et où cette infrastructure est-elle située ?"
  - "Quelles sont les caractéristiques et les différences principales entre les trois espaces de stockage (/home, /scratch et /project) disponibles sur le système ?"
  - "Quelle technologie de réseautique haute performance est utilisée par Cedar pour supporter efficacement les tâches parallèles impliquant des milliers de cœurs ?"
  - "Quelles sont les capacités matérielles globales de la grappe Cedar en termes de cœurs CPU et de GPU ?"
  - "Pourquoi l'ordonnanceur limite-t-il la mémoire allouée à une valeur inférieure à la mémoire physique totale du nœud ?"
  - "Dans quelles conditions une tâche de calcul risque-t-elle de devoir partager un nœud avec d'autres tâches ?"
  - "Quelles sont les configurations de cœurs et d'architectures disponibles pour exécuter des tâches parallèles sur 32 nœuds ?"
  - "Comment le facteur de blocage du réseau évolue-t-il lors de l'exécution des plus grandes tâches ?"
  - "Pourquoi le système Cedar est-il considéré comme une bonne option pour les tâches nécessitant plusieurs milliers de cœurs ?"
  - "Pour quel type de tâches certains nœuds de 48 cœurs sont-ils spécifiquement réservés ?"
  - "Quelle est la politique de réservation concernant les nœuds de 32 cœurs pour les calculs sur des nœuds entiers ?"
  - "Quelle conséquence y a-t-il pour les tâches qui nécessitent moins de 48 cœurs par nœud ?"
  - "Comment doit-on procéder pour demander un type de nœud spécifique, tel qu'un nœud AVX512, pour l'exécution d'une application ?"
  - "Pourquoi l'exécution de tâches depuis le répertoire /home est-elle interdite et vers quels répertoires les fichiers doivent-ils être transférés ?"
  - "Quelles sont les caractéristiques techniques du système en termes de performance théorique maximale et de topologie réseau ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

| | |
|:---|:---|
| Disponibilité : | **FIN DU SERVICE LE 12 SEPTEMBRE 2025** |
| Nœud de connexion : | **cedar.alliancecan.ca** |
| Collection Globus : | **computecanada#cedar-globus** |
| État de la grappe : | [État de la grappe](https://status.alliancecan.ca/) |

Cedar est une grappe hétérogène adaptée pour plusieurs types de tâches; elle est située à l'Université Simon-Fraser. Son nom rappelle le [cèdre de l'Ouest](https://fr.wikipedia.org/wiki/Thuja_plicata), arbre officiel de la Colombie-Britannique dont la signification spirituelle est importante pour les Premières Nations de la région.

Le fournisseur est Scalar Decisions Inc.; les nœuds sont des produits Dell; le système de fichiers de stockage /scratch haute performance est de DDN; la réseautique est d'Intel. Un système de refroidissement liquide utilise des échangeurs de chaleur à même les portes arrière.

!!! warning "IMPORTANT"
    La version 4 de Globus ne supporte plus les points de chute et **computecanada#cedar-dtn** n'est plus disponible. Veuillez utiliser le point de chute de la version 5, **computecanada#cedar-globus**.

[Introduction à Cedar](../getting-started/getting_started.md)
[Exécuter des tâches](../running-jobs/running_jobs.md)
[Transférer des données](../getting-started/transferring_data.md)

## Stockage

| | |
|:---|:---|
| **espace /home** <br/>volume total 526 To |
    * localisation des répertoires /home
    * chaque répertoire /home a un petit [quota](../storage-and-data/storage_and_file_management.md#quotas-et-politiques) fixe
    * non alloué via le [service d'accès rapide](https://alliancecan.ca/fr/services/calcul-informatique-de-pointe/acces-aux-ressources/service-dacces-rapide) ou le [concours d'allocation de ressources](https://alliancecan.ca/fr/services/calcul-informatique-de-pointe/acces-aux-ressources/concours-pour-lallocation-de-ressources); le stockage de grande envergure se fait sur /project
    * est sauvegardé chaque jour |
| **espace /scratch**, <br/>volume total 5.4 Po <br/>système de fichiers parallèle de haute performance |
    * stockage actif ou temporaire
    * non alloué
    * grand [quota](../storage-and-data/storage_and_file_management.md#quotas-et-politiques) fixe, par utilisateur
    * les données inactives sont [purgées](../storage-and-data/scratch_purging_policy.md) |
| **espace /project** <br/>volume total 23 Po <br/>stockage persistant externe |
    * ne convient pas aux tâches d'écriture et de lecture parallèles; utiliser plutôt l'espace /scratch
    * grand [quota](../storage-and-data/storage_and_file_management.md#quotas-et-politiques) ajustable, par projet
    * est sauvegardé chaque jour |

Le stockage temporaire (/scratch) est un système de fichiers Lustre basé sur la technologie DDN, modèle ES14K. Il est composé de 640 disques NL-SAS de 8 To chacun, avec un double contrôleur de métadonnées dont les disques sont des SSD.

## Réseautique haute performance

*Réseautique Intel OmniPath (version 1, bande passante de 100 Gbit/s).*

Une réseautique à faible latence et haute performance pour tous les nœuds de calcul et le stockage temporaire.

L'architecture a été planifiée pour supporter de multiples tâches parallèles utilisant jusqu'à 1024 cœurs Broadwell (32 nœuds) ou 1536 cœurs Skylake (32 nœuds) ou 1536 cœurs Cascade Lake (32 nœuds) grâce à une réseautique non bloquante. Pour les plus grandes tâches, le réseau a un facteur de blocage de 2:1. Même pour les tâches de plusieurs milliers de cœurs, Cedar est une bonne option.

## Caractéristiques des nœuds

Cedar offre 100 400 cœurs CPU pour le calcul et 1352 GPU. TurboBoost est désactivé sur tous les nœuds.

| nœuds | cœurs | mémoire disponible | CPU | stockage | GPU |
|:---|:---|:---|:---|:---|:---|
| 256 | 32 | 125 G ou 128 000 M | 2 x Intel E5-2683 v4 Broadwell @ 2.1 GHz | 2 x SSD 480 G | - |
| 256 | 32 | 250 G ou 257 000 M | 2 x Intel E5-2683 v4 Broadwell @ 2.1 GHz | 2 x SSD 480 G | - |
| 40 | 32 | 502 G ou 515 000 M | 2 x Intel E5-2683 v4 Broadwell @ 2.1 GHz | 2 x SSD 480 G | - |
| 16 | 32 | 1510 G ou 1 547 000 M | 2 x Intel E5-2683 v4 Broadwell @ 2.1 GHz | 2 x SSD 480 G | - |
| 6 | 32 | 4000 G ou 409 600 M | 2 x AMD EPYC 7302 @ 3.0 GHz | 2 x SSD 480 G | - |
| 2 | 40 | 6000 G ou 614 400 M | 4 x Intel Gold 5215 Cascade Lake @ 2.5 GHz | 2 x SSD 480 G | - |
| 96 | 24 | 125 G ou 128 000 M | 2 x Intel E5-2650 v4 Broadwell @ 2.2 GHz | 1 x SSD 800 G | 4 x NVIDIA P100 Pascal (mémoire HBM2 12 G) |
| 32 | 24 | 250 G ou 257 000 M | 2 x Intel E5-2650 v4 Broadwell @ 2.2 GHz | 1 x SSD 800 G | 4 x NVIDIA P100 Pascal (mémoire HBM2 16 G) |
| 192 | 32 | 187 G ou 192 000 M | 2 x Intel Silver 4216 Cascade Lake @ 2.1 GHz | 1 x SSD 480 G | 4 x NVIDIA V100 Volta (mémoire HBM2 32 G) |
| 608 | 48 | 187 G ou 192 000 M | 2 x Intel Platinum 8160F Skylake @ 2.1 GHz | 2 x SSD 480 G | - |
| 768 | 48 | 187 G ou 192 000 M | 2 x Intel Platinum 8260 Cascade Lake @ 2.4 GHz | 2 x SSD 480 G | - |

Remarquez que la quantité de mémoire disponible est moindre que la valeur arrondie suggérée par la configuration matérielle. Par exemple, les nœuds de type *base 128 G* ont effectivement 128 Gio de mémoire vive, mais une certaine quantité est utilisée en permanence par le noyau (*kernel*) et le système d'exploitation. Pour éviter la perte de temps encourue par le *swapping* ou le *paging*, l'ordonnanceur n'allouera jamais une tâche dont les exigences dépassent la quantité de mémoire disponible indiquée dans le tableau ci-dessus.

Tous les nœuds ont de l'espace de stockage local temporaire. Les nœuds de calcul (à l'exception des nœuds GPU) ont deux disques SSD de 480 Go pour une capacité totale de 960 Go. Les nœuds GPU ont un disque SSD de 800 Go ou de 480 Go. Utilisez le stockage local sur le nœud par le biais du répertoire créé pour la tâche par l'ordonnanceur. Voir [Stockage local sur les nœuds de calcul](../storage-and-data/using_node-local_storage.md).

### Sélectionner un type de nœud
Un certain nombre de nœuds de 48 cœurs sont réservés pour les tâches qui nécessitent des nœuds entiers. Aucun nœud de 32 cœurs n'est réservé pour les calculs avec des nœuds entiers. **Les tâches qui nécessitent moins de 48 cœurs par nœud pourraient donc avoir à partager des nœuds avec d'autres tâches**.

La plupart des applications peuvent être exécutées sur les nœuds Broadwell, Skylake ou Cascade Lake et la différence en performance ne devrait pas être significative en comparaison des temps d'attente. Nous vous recommandons de ne pas spécifier le type de nœud pour vos tâches. Par contre, s'il est nécessaire de demander un type particulier, utilisez `--constraint=cascade`, `--constraint=skylake` ou `--constraint=broadwell`. Si vous avez besoin d'un nœud AVX512, utilisez `--constraint=[skylake|cascade]`.

## Modification à la politique de soumission et exécution de tâches

!!! warning
    Depuis le **17 avril 2019**, les tâches ne peuvent plus être exécutées dans le système de fichiers `/home`. Cette modification a pour but de diminuer la charge et d'améliorer le temps de réponse en mode interactif dans `/home`. Si le message `Submitting jobs from directories residing in /home is not permitted` s'affiche, transférez les fichiers vers votre répertoire `/project` ou `/scratch` et soumettez la tâche à partir du nouvel emplacement.

### Performance
La performance théorique maximale en double précision est de 6547 téraflops pour les CPU auxquels s'ajoutent 7434 téraflops pour les GPU, pour un total de près de 14 pétaflops.

La topologie réseau est une composition d'îlots avec un facteur de blocage de 2:1 entre chacun. La plupart des îlots ont 32 nœuds entièrement reliés par une interconnexion (*Omni-Path fabric*) non bloquante.

La plupart des îlots ont 32 nœuds :
* 16 îlots de 32 nœuds Broadwell chacun avec 32 cœurs, soit 1024 cœurs par îlot;
* 43 îlots de 32 nœuds Skylake ou Cascade Lake chacun avec 48 cœurs, soit 1536 cœurs par îlot;
* 4 îlots avec 32 nœuds GPU P100;
* 6 îlots avec 32 nœuds GPU V100;
* 2 îlots de 32 nœuds Broadwell de grande mémoire chacun; de ces 64 nœuds, 40 sont de 0.5 To, 16 sont de 1.5 To, 6 sont de 4 To et 2 sont de 6 To.