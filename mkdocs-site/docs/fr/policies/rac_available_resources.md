---
title: "RAC available resources/fr"
slug: "rac_available_resources"
lang: "fr"

source_wiki_title: "RAC available resources/fr"
source_hash: "c2dcb368d62368945332155d35494348"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:55:24.981302+00:00"

tags:
  []

keywords:
  - "concours d'allocation de ressources"
  - "ressources de stockage"
  - "ressources GPU"
  - "ressources CPU"
  - "demandes de ressources"
  - "choix de système"
  - "exigences en ressources"
  - "grappes"
  - "grappes et nuages"
  - "CCDB"
  - "ressources infonuagiques"
  - "sous-systèmes"
  - "sélectionner des ressources"
  - "allocation"
  - "formulaire électronique"

questions:
  - "Que se passe-t-il en cas de divergence entre les exigences en ressources inscrites dans le formulaire électronique et celles du document de justification ?"
  - "Comment les ressources de calcul, de GPU et de stockage sont-elles réparties parmi les différents sous-systèmes des grappes et des nuages ?"
  - "Quelle option doit être sélectionnée dans le formulaire électronique si le demandeur n'a pas de préférence pour un système spécifique ?"
  - "Quelle est la procédure à suivre pour demander plusieurs types de ressources différentes, comme des ressources CPU et du stockage, sur un même système ?"
  - "Quelles sont les distinctions entre les types d'instances (de calcul ou persistantes) offertes dans les différents nuages tels qu'Arbutus, Fir, Béluga et Nibi ?"
  - "Pourquoi est-il crucial de spécifier précisément ses besoins en mémoire lors de la sélection de ressources de type « system-compute » ?"
  - "Que faut-il indiquer sous la rubrique « Expliquez ce choix de système » si l'on accepte une allocation sur un autre système ?"
  - "Comment les ressources de calcul et de stockage sont-elles structurées et présentées dans la base de données CCDB ?"
  - "Quelle est la première étape mentionnée pour effectuer la sélection des ressources dans les grappes ?"
  - "Quelle est la procédure à suivre pour demander plusieurs types de ressources différentes, comme des ressources CPU et du stockage, sur un même système ?"
  - "Quelles sont les distinctions entre les types d'instances (de calcul ou persistantes) offertes dans les différents nuages tels qu'Arbutus, Fir, Béluga et Nibi ?"
  - "Pourquoi est-il crucial de spécifier précisément ses besoins en mémoire lors de la sélection de ressources de type « system-compute » ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Le tableau suivant montre les ressources disponibles pour le **concours d'allocation de ressources pour 2026.**

Les ressources dans les grappes et les nuages sont organisées en sous-systèmes. Dans le tableau ci-dessus, chacun des sous-systèmes montre uniquement les ressources qui y sont disponibles. Par exemple, le sous-système `trillium-storage` n’offre que du stockage `/project`; le sous-système `hpss-storage` n’offre que du stockage `/nearline`; le sous-système `trillium-compute` n’offre que des `CPU` et de la mémoire; etc.

!!! important "Important"
    Entrez les mêmes exigences en ressources dans le formulaire électronique que celles décrites dans le document de justification des ressources fourni avec votre demande. En cas de divergence, le formulaire électronique aura préséance.

| **Systèmes** | **Sous-systèmes** (comme indiqués dans CCDB) | **Ressources de chaque sous-système** | **Stockage de sauvegarde** |
|---|---|---|---|
| Nuage `Arbutus` | `arbutus-compute-cloud` | `VCPU`, `VGPU`, mémoire par cœur, disque local éphémère, volumes, instantanés, adresses `IP` flottantes, stockage de volumes et instantanés, stockage dans système de fichiers partagés*, stockage objet | non |
| | `arbutus-persistent-cloud` | `VCPU`, `VGPU`, mémoire par cœur, disque local éphémère, volumes, instantanés, adresses `IP` flottantes, stockage de volumes et instantanés, stockage dans système de fichiers partagés*, stockage objet | non |
| | `arbutus-dcache` | stockage `dCache` | non |
| Grappe `Rorqual` | `rorqual-compute` | `CPU` | non |
| | `rorqual-gpu` | `GPU` | non |
| | `rorqual-storage` | stockage `/project`, stockage `/nearline` | oui |
| Nuage `Béluga` | `beluga-compute-cloud` | `VCPU`, mémoire par cœur, disque local éphémère, volumes, instantanés, adresses `IP` flottantes, stockage de volumes et instantanés | non |
| | `beluga-persistent-cloud` | `VCPU`, mémoire par cœur, disque local éphémère, volumes, instantanés, adresses `IP` flottantes, stockage de volumes et instantanés | non |
| Grappe `Fir` | `fir-compute` | `CPU` | non |
| | `fir-gpu` | `GPU` | non |
| | `fir-storage` | stockage `/project`, stockage `/nearline`, stockage `dCache` | oui |
| Nuage `Fir` | `fir-persistent-cloud` | `VCPU`, mémoire par cœur, disque local éphémère, volumes, instantanés, adresses `IP` flottantes, stockage de volumes et instantanés, stockage objet | non |
| | `fir-compute-cloud` | `VCPU`, mémoire par cœur, disque local éphémère, volumes, instantanés, adresses `IP` flottantes, stockage de volumes et instantanés, stockage objet | non |
| Grappe `Nibi` | `nibi-compute` | `CPU` | non |
| | `nibi-gpu` | `GPU` | non |
| | `nibi-storage` | stockage `/project`, stockage `/nearline`, stockage `dCache` | oui |
| Nuage `Nibi` | `nibi-persistent-cloud` | `VCPU`, mémoire par cœur, disque local éphémère, volumes, instantanés, adresses `IP` flottantes, stockage de volumes et instantanés | non |
| Grappe `Narval` | `narval-compute` | `CPU` | non |
| | `narval-gpu` | `GPU` | non |
| | `narval-storage` | stockage `/project` | oui |
| Grappe `Trillium` | `trillium-compute` | `CPU` | non |
| | `trillium-gpu` | `GPU` | non |
| | `trillium-storage` | stockage `/project` | oui |
| `HPSS` | `hpss-storage` | stockage `/nearline` | non |

*Des copies de sauvegarde sont faites des systèmes de fichiers partagés.

## Formulaire électronique

!!! important "Important"
    Entrez les mêmes exigences en ressources dans le formulaire électronique que celles décrites dans le document de justification des ressources fourni avec votre demande.

Dans le menu déroulant *Demander une nouvelle ressource*, sélectionnez le système ou sous-système qui correspond à votre besoin.
Si vous n’avez pas de préférence pour une ressource particulière, sous *Expliquez ce choix de système*, cochez *Je dois sélectionner un système mais je n'ai pas d'objection à recevoir une allocation sur tout autre système qui conviendrait.*

1.  **Sélectionner des ressources dans les grappes :** Dans `CCDB`, les ressources de calcul et de stockage sont présentées comme sous-systèmes des grappes, selon la convention suivante :
    *   `system-compute` (par exemple `rorqual-compute`) : ressources `CPU`. Indiquez précisément vos besoins en mémoire puisqu’ils seront considérés dans votre allocation.
    *   `system-gpu` (par exemple `rorqual-gpu`) : ressources `GPU`.
    *   `system-storage` (par exemple `rorqual-storage`) : ressources de stockage; les listes montrent uniquement les ressources disponibles (`/project`, `/nearline`, etc.) dans chacun des sous-systèmes.

    Si par exemple vous avez besoin de ressources `CPU` et de ressources de stockage `/project` sur `Rorqual`, vous devez remplir deux demandes distinctes, soit une pour des cœurs-années et la mémoire avec le sous-système `rorqual-compute` et une autre pour l’espace de stockage `/project` en `To` avec le sous-système `rorqual-storage`.

2.  **Sélectionner des ressources infonuagiques :** Si vous avez besoin de ressources infonuagiques dans des sites différents, vous devez remplir une demande distincte pour chacun des sites. Les ressources infonuagiques sont présentées selon la convention suivante :
    *   `system-compute-cloud` ou `system-persistent-cloud` : dans les nuages `Arbutus`, `Fir` et `Béluga`, vous pouvez sélectionner des instances de calcul ou des instances persistantes et dans le nuage `Nibi`, seulement des instances persistantes; les listes montrent uniquement les gabarits (`OpenStack`) disponibles pour chacun des nuages.

Si vous avez des questions sur la façon de demander des ressources, écrivez à [allocations@tech.alliancecan.ca](mailto:allocations@tech.alliancecan.ca).