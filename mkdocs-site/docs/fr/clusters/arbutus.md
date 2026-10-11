---
title: "Arbutus/fr"
slug: "arbutus"
lang: "fr"

source_wiki_title: "Arbutus/fr"
source_hash: "caf21f8700e2a4806f44c1fdc3a03465"
last_synced: "2026-10-11T01:39:35.690021+00:00"
last_processed: "2026-10-11T02:22:11.056504+00:00"

tags:
  []

keywords:
  - "fermeture 15 octobre 2026"
  - "caractéristiques des nœuds"
  - "Migration vers Arbutus"
  - "nuage Arbutus"
  - "stockage Ceph"

questions:
  - "Quand la version Legacy d’Arbutus sera‑t‑elle définitivement fermée et quelles sont les démarches de migration à suivre ?"
  - "Quels services (tableau de bord OpenStack, stockage objet, etc.) et quelles capacités de stockage sont proposés par le nouveau nuage Arbutus ?"
  - "Quelles sont les caractéristiques matérielles des nœuds d’Arbutus (cœurs, mémoire, CPU, GPU, stockage) ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! warning "Important"
    La première version du nuage Arbutus (*Legacy Arbutus*) fermera définitivement le 15 octobre 2026. Veuillez migrer tout contenu que vous voulez conserver tel que décrit dans [Migration vers Arbutus](../cloud/arbutus_migration_guide.md).

    Liens vers la première version d'Arbutus :
    *   Tableau de bord OpenStack : [https://arbutus.cloud.alliancecan.ca](https://arbutus.cloud.alliancecan.ca/)
    *   Stockage objet (S3 ou Swift) : [https://object-arbutus.cloud.computecanada.ca/](https://object-arbutus.cloud.computecanada.ca/)

*   Disponibilité : fin du printemps de 2026
*   Tableau de bord OpenStack : [https://arbutus.alliancecan.ca](https://arbutus.alliancecan.ca/auth/login/?next=/)
*   Point de chute Globus : *à confirmer*
*   Stockage objet (S3 ou Swift) : `https://object-arbutus.alliancecan.ca/<tenant-id>:<bucket-name>/<object-name>`

Arbutus est un nuage IaaS (*Infrastructure-as-a-Service*) hébergé à l'Université de Victoria.

## Stockage
*   7 Po de stockage [Ceph](https://en.wikipedia.org/wiki/Ceph_(software)) pour les volumes et les instantanés
*   26 Po de stockage [Ceph](https://en.wikipedia.org/wiki/Ceph_(software)) pour le stockage objet et les systèmes de fichiers partagés
*   3 Po de stockage [Ceph](https://en.wikipedia.org/wiki/Ceph_(software)) NVMe pour les volumes et les instantanés

## Caractéristiques des nœuds

| nœuds | cœurs | mémoire disponible | stockage | CPU | GPU |
|---|---|---|---|---|---|
| 338 | 96 | 768Go DDR5 | 1 x NVMe SSD, 7.68To | 2 x Intel Platinum 8568Y+ 2.3GHz, cache de 300Mo | |
| 22 | 96 | 1536GB DDR5 | 1 x NVMe SSD, 7.68To | 2 x Intel Platinum 8568Y+ 2.3GHz, cache de 300Mo | |
| 11 | 64 | 2048Go DDR5 | 1 x NVMe SSD, 7.68To | 2 x Intel Platinum 6548Y+ 2.5GHz, cache de 60Mo | |
| 16 | 48 | 1024Go DDR4 | 1 x NVMe SSD, 3.84To | 2 x Intel Gold 6342 2.8 GHz, 36MB cache | 4 x NVidia H100 PCIe Gen5 (94Go) |
| 10 | 48 | 128GB DDR5 | 1 x NVMe SSD, 3.84To | 2 x Intel Gold 6542Y 2.9 GHz, cache de 60Mo | 1 x NVidia L40s PCIe Gen4 (48Go) |

Voir le sommaire du matériel sur la page [*Ressources infonuagiques*](../cloud/cloud_resources.md#nuage-arbutus).