---
title: "Trillium/fr"
slug: "trillium"
lang: "fr"

source_wiki_title: "Trillium/fr"
source_hash: "f2e88e514aaffa2bafd5ca63643a8af2"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:06:03.826516+00:00"

tags:
  []

keywords:
  - "sauvegarde et archivage"
  - "Système de stockage"
  - "Système de stockage VAST"
  - "Système de fichiers VAST"
  - "Empreinte énergétique"
  - "NVMe"
  - "Efficacité énergétique"
  - "Pool de stockage unifié"
  - "Grappe Trillium"
  - "IOPS"
  - "archivage sur ruban"
  - "Nœuds CPU et GPU"
  - "Réseau haute performance"
  - "mémoire flash"
  - "bande passante"

questions:
  - "Quelle est la fonction principale de la grappe Trillium et par quelle institution est-elle hébergée ?"
  - "Quelles sont les spécifications techniques des nœuds CPU et GPU ainsi que du réseau haute performance ?"
  - "Comment le système de refroidissement de Trillium est-il conçu pour optimiser l'efficacité énergétique ?"
  - "Quelles sont les performances et la capacité totale du système de stockage en mémoire flash ?"
  - "Quels sont les protocoles d'accès supportés et l'architecture matérielle dédiée aux services de données ?"
  - "Comment est structuré le système de sauvegarde et d'archivage, et quel logiciel en assure la gestion ?"
  - "Comment la chaleur est-elle réutilisée par les installations voisines pour minimiser l'empreinte énergétique ?"
  - "Quelle technologie matérielle soutient le système de fichiers VAST haute performance ?"
  - "Quelle est la capacité effective du système de stockage et quelle méthode d'optimisation est utilisée ?"
  - "Quelles sont les performances et la capacité totale du système de stockage en mémoire flash ?"
  - "Quels sont les protocoles d'accès supportés et l'architecture matérielle dédiée aux services de données ?"
  - "Comment est structuré le système de sauvegarde et d'archivage, et quel logiciel en assure la gestion ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

| Élément | Détails |
| :------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Disponibilité | 7 août 2025 |
| Nœuds de connexion | sous-grappe de CPU, **trillium.alliancecan.ca**<br>sous-grappe de GPU, **trillium-gpu.alliancecan.ca** |
| Collections Globus | [alliancecan#trillium](https://app.globus.org/file-manager?origin_id=ad462f99-8436-42b4-adc6-3644e36c1b67) (système de fichiers)<br>[alliancecan#hpss](https://app.globus.org/file-manager?origin_id=c55ce750-19d6-4a42-9c30-6a58f06bec7a) (archive/nearline) |
| Nœud de copie (rsync, scp, sftp,...) | **tri-dm{1,2,3,4}.scinet.utoronto.ca** |
| Nœud d'automatisation | **robot{1,2,3,4}.scinet.utoronto.ca** |
| Open OnDemand | [ondemand.scinet.utoronto.ca](https://ondemand.scinet.utoronto.ca) (inclut JupyterLab) |
| Portail | [my.scinet.utoronto.ca](https://my.scinet.utoronto.ca) |

La grappe Trillium est conçue pour prendre en charge des tâches massivement parallèles. Construite par Lenovo Canada, elle est hébergée par SciNet à l'Université de Toronto.

L'utilisation de Trillum est semblable à celle des autres grappes nationales avec cependant certaines particularités. Pour les détails, voir [Trillium : Guide de démarrage](trillium_quickstart.md).

Si vous aviez accès à Niagara, nous vous encourageons fortement de prendre connaissance de la page [Transition de Niagara à Trillium](transition_from_niagara_to_trillium.md).

## Installation et transition
En raison de la capacité d'alimentation électrique et de refroidissement, une portion importante de la grappe Niagara sera fermée pendant une période intermédiaire afin d'effectuer les tests d'acceptation et la transition vers le nouveau système. Nous vous tiendrons au courant lorsque nous aurons une meilleure idée du calendrier d'installation de Trillium.

## Stockage
Stockage parallèle : 29 pétaoctets, SSD NVMe de VAST Data.

## Réseau haute performance
*   Réseautique Infiniband Nvidia NDR
    *   400 Gbit/s pour les nœuds CPU
    *   800 Gbit/s pour les nœuds GPU
    *   réseau entièrement non bloquant; les nœuds peuvent communiquer entre eux simultanément sur toute la bande passante

## Caractéristiques des nœuds
| Nœud de connexion | Nœuds | Cœurs | Mémoire disponible | CPU | GPU |
| :------------------------------- | :--- | :--- | :------------------- | :------------------------------------------------------ | :--------------------------------------------------------------------------- |
| **trillium.alliancecan.ca** | 1224 | 192 | 749G ou 767000M | 2 x AMD EPYC 9655 (Zen 5) @ 2.6 GHz, cache L3 de 384MB | |
| trillium-**gpu**.alliancecan.ca | 63 | 96 | 749G ou 767000M | 1 x AMD EPYC 9654 (Zen 4) @ 2.4 GHz, cache L3 de 384MB | 4 x NVidia H100 SXM (80GB de mémoire), connexion via NVLink |

## Données techniques

### Refroidissement et efficacité énergétique

Le refroidissement se fait par une eau de 35 à 40 °C, ce qui a les effets suivants :

*   indicateur d'efficacité énergétique (PUE) sous 1.03;
*   refroidisseurs à sec en circuit fermé, sans tours d'évaporation et consommation de nouvelle eau;
*   excédent de chaleur utilisé par des installations voisines pour minimiser l'empreinte énergétique.

### Système de stockage

Le système de fichiers VAST haute performance est composé d'un pool de stockage unifié de 29PB soutenu par NVMe avec les caractéristiques suivantes :

*   capacité effective de 29PB (dédupliquée via VAST);
*   capacité de mémoire flash brute de 16.7PB;
*   bande passante de 714GB/s en lecture et de 275GB/s en écriture;
*   10 millions d'IOPS en lecture et 2 millions d'IOPS en écriture;
*   protocoles d'accès POSIX et S3 sous un espace de nommage unifié;
*   48 CBoxes et 14 DBox pour les services de données.

### Sauvegarde et archivage

L'archivage sur ruban /nearline HPSS dispose de 114PB additionnels.

*   Archivage en deux copies dans des bibliothèques géographiquement distinctes;
*   utilisé à des fins de sauvegarde et d'archivage;
*   sauvegardes gérées par le logiciel Atempo.