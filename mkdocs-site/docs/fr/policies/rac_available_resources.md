---
title: "RAC available resources/fr"
slug: "rac_available_resources"
lang: "fr"

source_wiki_title: "RAC available resources/fr"
source_hash: "c2dcb368d62368945332155d35494348"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T10:38:54.634823+00:00"

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

Le tableau suivant montre les ressources disponibles pour le **concours d'allocation de ressources pour 2026.**

Les ressources dans les grappes et les nuages sont organisées en sous-systèmes. Dans le tableau ci-dessus, chacun des sous-systèmes montre uniquement les ressources qui y sont disponibles. Par exemple, le sous-système *trillium-storage* n’offre que du stockage /project; le sous-système *hpss-storage* n’offre que du stockage /nearline; le sous-système *trillium-compute* n’offre que des CPU et de la mémoire; etc.

!!! warning "Important"
    Entrez les mêmes exigences en ressources dans le formulaire électronique que celles décrites dans le document de justification des ressources fourni avec votre demande. En cas de divergence, le formulaire électronique aura préséance.

| **Systèmes**      | **Sous-systèmes (comme indiqués dans CCDB)** | **Ressources de chaque sous-système**                                                                                                                                                             | **Stockage de sauvegarde** |
| :---------------- | :------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------- |
| Nuage Arbutus     | arbutus-compute-cloud                        | VCPU, VGPU, mémoire par cœur, disque local éphémère, volumes, instantanés, adresses IP flottantes, stockage de volumes et instantanés, stockage dans système de fichiers partagés*, stockage objet | non                        |
| Nuage Arbutus     | arbutus-persistent-cloud                     | VCPU, VGPU, mémoire par cœur, disque local éphémère, volumes, instantanés, adresses IP flottantes, stockage de volumes et instantanés, stockage dans système de fichiers partagés*, stockage objet | non                        |
| Nuage Arbutus     | arbutus-dcache                               | stockage dCache                                                                                                                                                                           | non                        |
| Grappe Rorqual    | rorqual-compute                              | CPU                                                                                                                                                                                       | non                        |
| Grappe Rorqual    | rorqual-gpu                                  | GPU                                                                                                                                                                                       | non                        |
| Grappe Rorqual    | rorqual-storage                              | stockage /project, stockage /nearline                                                                                                                                                     | oui                        |
| Nuage Béluga      | beluga-compute-cloud                         | VCPU, mémoire par cœur, disque local éphémère, volumes, instantanés, adresses IP flottantes, stockage de volumes et instantanés                                                           | non                        |
| Nuage Béluga      | beluga-persistent-cloud                      | VCPU, mémoire par cœur, disque local éphémère, volumes, instantanés, adresses IP flottantes, stockage de volumes et instantanés                                                           | non                        |
| Grappe Fir        | fir-compute                                  | CPU                                                                                                                                                                                       | non                        |
| Grappe Fir        | fir-gpu                                      | GPU                                                                                                                                                                                       | non                        |
| Grappe Fir        | fir-storage                                  | stockage /project, stockage /nearline, stockage dCache                                                                                                                                    | oui                        |
| Nuage Fir         | fir-persistent-cloud                         | VCPU, mémoire par cœur, disque local éphémère, volumes, instantanés, adresses IP flottantes, stockage de volumes et instantanés, stockage objet                                           | non                        |
| Nuage Fir         | fir-compute-cloud                            | VCPU, mémoire par cœur, disque local éphémère, volumes, instantanés, adresses IP flottantes, stockage de volumes et instantanés, stockage objet                                           | non                        |
| Grappe Nibi       | nibi-compute                                 | CPU                                                                                                                                                                                       | non                        |
| Grappe Nibi       | nibi-gpu                                     | GPU                                                                                                                                                                                       | non                        |
| Grappe Nibi       | nibi-storage                                 | stockage /project, stockage /nearline, stockage dCache                                                                                                                                    | oui                        |
| Nuage Nibi        | nibi-persistent-cloud                        | VCPU, mémoire par cœur, disque local éphémère, volumes, instantanés, adresses IP flottantes, stockage de volumes et instantanés                                                           | non                        |
| Grappe Narval     | narval-compute                               | CPU                                                                                                                                                                                       | non                        |
| Grappe Narval     | narval-gpu                                   | GPU                                                                                                                                                                                       | non                        |
| Grappe Narval     | narval-storage                               | stockage /project                                                                                                                                                                         | oui                        |
| Grappe Trillium   | trillium-compute                             | CPU                                                                                                                                                                                       | non                        |
| Grappe Trillium   | trillium-gpu                                 | GPU                                                                                                                                                                                       | non                        |
| Grappe Trillium   | trillium-storage                             | stockage /project                                                                                                                                                                         | oui                        |
| HPSS              | hpss-storage                                 | stockage /nearline                                                                                                                                                                        | non                        |

* Des copies de sauvegarde sont faites des systèmes de fichiers partagés.

## Formulaire électronique

!!! warning "Important"
    Entrez les mêmes exigences en ressources dans le formulaire électronique que celles décrites dans le document de justification des ressources fourni avec votre demande.

Dans le menu déroulant *Demander une nouvelle ressource*, sélectionnez le système ou sous-système qui correspond à votre besoin.
Si vous n’avez pas de préférence pour une ressource particulière, sous *Expliquez ce choix de système*, cochez *Je dois sélectionner un système mais je n'ai pas d'objection à recevoir une allocation sur tout autre système qui conviendrait.*

**1. Sélectionner des ressources dans les grappes :** Dans CCDB, les ressources de calcul et de stockage sont présentées comme sous-systèmes des grappes, selon la convention suivante :

*   system-compute (par exemple *rorqual-compute*) : ressources CPU. Indiquez précisément vos besoins en mémoire puisqu’ils seront considérés dans votre allocation.
*   system-gpu (par exemple *rorqual-gpu*) : ressources GPU.
*   system-storage (par exemple *rorqual-storage*) : ressources de stockage; les listes montrent uniquement les ressources disponibles (/project, /nearline, etc.) dans chacun des sous-systèmes.

Si par exemple vous avez besoin de ressources CPU et de ressources de stockage /project sur Rorqual, vous devez remplir deux demandes distinctes, soit une pour des cœurs-années et la mémoire avec le sous-système rorqual-compute et une autre pour l’espace de stockage /project en To avec le sous-système rorqual-storage.

**2. Sélectionner des ressources infonuagiques :** Si vous avez besoin de ressources infonuagiques dans des sites différents, vous devez remplir une demande distincte pour chacun des sites. Les ressources infonuagiques sont présentées selon la convention suivante :

*   system-compute-cloud ou system-persistent-cloud : dans les nuages Arbutus, Fir et Béluga, vous pouvez sélectionner des instances de calcul ou des instances persistantes et dans le nuage Nibi, seulement des instances persistantes; les listes montrent uniquement les gabarits (*flavors* OpenStack) disponibles pour chacun des nuages.

Si vous avez des questions sur comment demander des ressources, écrivez à allocations@tech.alliancecan.ca.