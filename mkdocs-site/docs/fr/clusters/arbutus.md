---
title: "Arbutus/fr"
slug: "arbutus"
lang: "fr"

source_wiki_title: "Arbutus/fr"
source_hash: "c1c3568dc5dd14c9f83c2c7af9c70893"
last_synced: "2026-10-04T02:27:33.201522+00:00"
last_processed: "2026-10-04T03:04:11.739742+00:00"

tags:
  []

keywords:
  - "Arbutus"
  - "GPU Nvidia H100"
  - "stockage Ceph"
  - "tableau de bord OpenStack"
  - "nuage IaaS"

questions:
  - "Quand le nuage Arbutus sera-t-il disponible et quels sont les principaux points d’accès (tableau de bord OpenStack, point de chute Globus, stockage objet) ?"
  - "Quelle est la capacité totale de stockage proposée par Arbutus, en distinguant le stockage de volumes, le stockage objet et le stockage NVMe ?"
  - "Quels sont les différents types de nœuds proposés (nombre de cœurs, mémoire, stockage, CPU et GPU) et leurs caractéristiques respectives ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! info "Infos clés sur Arbutus"

    *   **Disponibilité** : Fin du printemps de 2026
    *   **Tableau de bord OpenStack** : [https://arbutus.cloud.alliancecan.ca/](https://arbutus.cloud.alliancecan.ca/)
    *   **Point de chute Globus** : *à confirmer*
    *   **Stockage objet (S3 ou Swift)** : [https://object-arbutus.cloud.computecanada.ca/](https://object-arbutus.cloud.computecanada.ca/)

Arbutus est un nuage IaaS (*Infrastructure-as-a-Service*) hébergé à l'Université de Victoria.

## Stockage

*   7 Po de stockage [Ceph](https://en.wikipedia.org/wiki/Ceph_(software)) pour les volumes et les instantanés
*   26 Po de stockage [Ceph](https://en.wikipedia.org/wiki/Ceph_(software)) pour le stockage objet et les systèmes de fichiers partagés
*   3 Po de stockage [Ceph](https://en.wikipedia.org/wiki/Ceph_(software)) NVMe pour les volumes et les instantanés

## Caractéristiques des nœuds

| Nœuds | Cœurs | Mémoire disponible | Stockage | CPU | GPU |
| :---- | :---- | :----------------- | :------- | :-- | :-- |
| 338   | 96    | 768 Go DDR5        | 1 x NVMe SSD, 7.68 To | 2 x Intel Platinum 8568Y+ 2.3GHz, cache de 300 Mo |             |
| 22    | 96    | 1536 Go DDR5       | 1 x NVMe SSD, 7.68 To | 2 x Intel Platinum 8568Y+ 2.3GHz, cache de 300 Mo |             |
| 11    | 64    | 2048 Go DDR5       | 1 x NVMe SSD, 7.68 To | 2 x Intel Platinum 6548Y+ 2.5GHz, cache de 60 Mo  |             |
| 16    | 48    | 1024 Go DDR4       | 1 x NVMe SSD, 3.84 To | 2 x Intel Gold 6342 2.8 GHz, 36 Mo cache          | 4 x NVidia H100 PCIe Gen5 (94 Go) |
| 10    | 48    | 128 Go DDR5        | 1 x NVMe SSD, 3.84 To | 2 x Intel Gold 6542Y 2.9 GHz, cache de 60 Mo      | 1 x NVidia L40s PCIe Gen4 (48 Go) |

Voir le sommaire du matériel sur la page [*Ressources infonuagiques*](../cloud/cloud_resources.md#nuage-arbutus).