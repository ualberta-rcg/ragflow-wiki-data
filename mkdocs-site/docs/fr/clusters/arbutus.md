---
title: "Arbutus/fr"
slug: "arbutus"
lang: "fr"

source_wiki_title: "Arbutus/fr"
source_hash: "ef003514c85e802ead8bfe5f93aca3d2"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T04:32:43.299539+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

| Caractéristique | Valeur |
| :-------------- | :----- |
| Disponibilité | fin du printemps de 2026 |
| Tableau de bord OpenStack | [https://arbutus.cloud.alliancecan.ca](https://arbutus.cloud.alliancecan.ca) |
| Point de chute Globus | *à confirmer* |
| Stockage objet (S3 ou Swift) | [https://object-arbutus.cloud.computecanada.ca](https://object-arbutus.cloud.computecanada.ca/) |

Arbutus est un nuage IaaS (*Infrastructure-as-a-Service*) hébergé à l'Université de Victoria.

## Stockage
7 Po de stockage [Ceph](https://en.wikipedia.org/wiki/Ceph_(software)) pour les volumes et les instantanés
26 Po de stockage [Ceph](https://en.wikipedia.org/wiki/Ceph_(software)) pour le stockage objet et les systèmes de fichiers partagés
3 Po de stockage [Ceph](https://en.wikipedia.org/wiki/Ceph_(software)) NVMe pour les volumes et les instantanés

## Caractéristiques des nœuds

| Nœuds | Cœurs | Mémoire disponible | Stockage | CPU | GPU |
| :---- | :---- | :----------------- | :------- | :-- | :-- |
| 338 | 96 | 768Go DDR5 | 1 x NVMe SSD, 7.68To | 2 x Intel Platinum 8568Y+ 2.3GHz, cache de 300Mo | |
| 22 | 96 | 1536GB DDR5 | 1 x NVMe SSD, 7.68To | 2 x Intel Platinum 8568Y+ 2.3GHz, cache de 300Mo | |
| 11 | 64 | 2048Go DDR5 | 1 x NVMe SSD, 7.68To | 2 x Intel Platinum 6548Y+ 2.5GHz, cache de 60Mo | |
| 16 | 48 | 1024Go DDR4 | 1 x NVMe SSD, 3.84To | 2 x Intel Gold 6342 2.8 GHz, 36MB cache | 4 x NVidia H100 PCIe Gen5 (94Go) |
| 10 | 48 | 128GB DDR5 | 1 x NVMe SSD, 3.84To | 2 x Intel Gold 6542Y 2.9 GHz, cache de 60Mo | 1 x NVidia L40s PCIe Gen4 (48Go) |

Voir le sommaire du matériel sur la page [*Ressources infonuagiques*](cloud-resources.md#nuage-arbutus).