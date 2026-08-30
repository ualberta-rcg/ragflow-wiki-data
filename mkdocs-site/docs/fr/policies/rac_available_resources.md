---
title: "RAC available resources/fr"
slug: "rac_available_resources"
lang: "fr"

source_wiki_title: "RAC available resources/fr"
source_hash: "61ec98823d4f75c572e76511e5e5745f"
last_synced: "2026-08-30T01:09:18.871111+00:00"
last_processed: "2026-08-30T01:35:25.457075+00:00"

tags:
  []

keywords:
  - "grappes"
  - "concours d'allocation de ressources 2027"
  - "rorqual-storage"
  - "system-compute-cloud"
  - "stockage /project"
  - "system-compute"
  - "formulaire électronique"
  - "besoins en mémoire"
  - "CCDB"
  - "sélectionner des ressources"
  - "sous-systèmes"
  - "system-storage"
  - "rorqual-compute"
  - "system-gpu"
  - "CPU"

questions:
  - "Quels sous‑systèmes offrent la possibilité de stockage de sauvegarde selon le tableau présenté ?"
  - "Comment doit‑on saisir les exigences en ressources dans le formulaire électronique pour qu’elles correspondent exactement au document de justification fourni ?"
  - "Quelles catégories de ressources (CPU, GPU, VCPU, mémoire, stockage, etc.) sont disponibles pour chaque sous‑système des grappes et des nuages répertoriés ?"
  - "Comment formuler deux demandes distinctes lorsqu’on a besoin à la fois de ressources CPU (cœurs‑années et mémoire) et de stockage /project sur le sous‑système rorqual ?"
  - "Quelles sont les distinctions entre les sous‑systèmes « system‑compute‑cloud » et « system‑persistent‑cloud » ainsi que les types d’instances disponibles dans les nuages Arbutus, Fir, Béluga et Nibi ?"
  - "À qui et comment doit‑on s’adresser pour obtenir de l’aide ou poser des questions sur la procédure de demande de ressources ?"
  - "Quels sont les sous‑systèmes présentés dans CCDB pour les grappes de calcul et de stockage ?"
  - "Comment la convention de nommage « system‑compute » (ex. rorqual‑compute) identifie‑t‑elle les ressources CPU ?"
  - "Pourquoi faut‑il indiquer précisément les besoins en mémoire lors de la sélection des ressources ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Voici la version convertie de votre document en français québécois, au format Markdown pour MkDocs Material :

Le tableau suivant présente les ressources disponibles pour le **concours d'allocation de ressources pour 2027.**

Les ressources au sein des grappes et des nuages sont organisées en sous-systèmes. Dans le tableau ci-dessous, chacun des sous-systèmes montre uniquement les ressources qui y sont disponibles. Par exemple, le sous-système `trillium-storage` n’offre que du stockage `/project`; le sous-système `hpss-storage` n’offre que du stockage `/nearline`; le sous-système `trillium-compute` n’offre que des CPU et de la mémoire, et ainsi de suite.

!!! important
    **Important :** Vous devez saisir les mêmes exigences en ressources dans le formulaire électronique que celles décrites dans le document de justification des ressources fourni avec votre demande. En cas de divergence, le formulaire électronique aura préséance.

| Systèmes | Sous-systèmes (comme indiqués dans CCDB) | Ressources par sous-système                                                                                                                                                                                                                                                             | Stockage de sauvegarde |
|:---------|:-----------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------:|
| Nuage Arbutus | arbutus-compute-cloud                    | VCPU, VGPU, mémoire par cœur, disque local éphémère, volumes, instantanés, adresses IP flottantes, stockage de volumes et instantanés, stockage dans système de fichiers partagés\*, stockage objet                                                                                     | non                    |
| Nuage Arbutus | arbutus-persistent-cloud                 | VCPU, VGPU, mémoire par cœur, disque local éphémère, volumes, instantanés, adresses IP flottantes, stockage de volumes et instantanés, stockage dans système de fichiers partagés\*, stockage objet                                                                                     | non                    |
| Nuage Arbutus | arbutus-dcache                           | stockage dCache                                                                                                                                                                                                                                                                         | non                    |
| Grappe Rorqual | rorqual-compute                          | CPU                                                                                                                                                                                                                                                                                     | non                    |
| Grappe Rorqual | rorqual-gpu                              | GPU                                                                                                                                                                                                                                                                                     | non                    |
| Grappe Rorqual | rorqual-storage                          | stockage /project, stockage /nearline                                                                                                                                                                                                                                                   | oui                    |
| Grappe Fir     | fir-compute                              | CPU                                                                                                                                                                                                                                                                                     | non                    |
| Grappe Fir     | fir-gpu                                  | GPU                                                                                                                                                                                                                                                                                     | non                    |
| Grappe Fir     | fir-storage                              | stockage /project, stockage /nearline, stockage dCache                                                                                                                                                                                                                                  | oui                    |
| Nuage Fir      | fir-persistent-cloud                     | VCPU, mémoire par cœur, disque local éphémère, volumes, instantanés, adresses IP flottantes, stockage de volumes et instantanés, stockage objet                                                                                                                                        | non                    |
| Nuage Fir      | fir-compute-cloud                        | VCPU, mémoire par cœur, disque local éphémère, volumes, instantanés, adresses IP flottantes, stockage de volumes et instantanés, stockage objet                                                                                                                                        | non                    |
| Grappe Nibi    | nibi-compute                             | CPU                                                                                                                                                                                                                                                                                     | non                    |
| Grappe Nibi    | nibi-gpu                                 | GPU                                                                                                                                                                                                                                                                                     | non                    |
| Grappe Nibi    | nibi-storage                             | stockage /project, stockage /nearline, stockage dCache                                                                                                                                                                                                                                  | oui                    |
| Nuage Nibi     | nibi-persistent-cloud                    | VCPU, mémoire par cœur, disque local éphémère, volumes, instantanés, adresses IP flottantes, stockage de volumes et instantanés                                                                                                                                                        | non                    |
| Grappe Narval  | narval-compute                           | CPU                                                                                                                                                                                                                                                                                     | non                    |
| Grappe Narval  | narval-gpu                               | GPU                                                                                                                                                                                                                                                                                     | non                    |
| Grappe Narval  | narval-storage                           | stockage /project                                                                                                                                                                                                                                                                       | oui                    |
| Grappe Trillium | trillium-compute                         | CPU                                                                                                                                                                                                                                                                                     | non                    |
| Grappe Trillium | trillium-gpu                             | GPU                                                                                                                                                                                                                                                                                     | non                    |
| Grappe Trillium | trillium-storage                         | stockage /project                                                                                                                                                                                                                                                                       | oui                    |
| HPSS           | hpss-storage                             | stockage /nearline                                                                                                                                                                                                                                                                      | non                    |

\* Des copies de sauvegarde sont faites des systèmes de fichiers partagés.

## Formulaire électronique

!!! important
    Vous devez saisir les mêmes exigences en ressources dans le formulaire électronique que celles décrites dans le document de justification des ressources fourni avec votre demande.

Dans le menu déroulant *Demander une nouvelle ressource*, sélectionnez le système ou le sous-système qui correspond à votre besoin.
Si vous n’avez pas de préférence pour une ressource particulière, sous *Expliquez ce choix de système*, cochez l’option « Je dois sélectionner un système mais je n'ai pas d'objection à recevoir une allocation sur tout autre système qui conviendrait. »

1.  **Sélectionner des ressources dans les grappes :** Dans le CCDB, les ressources de calcul et de stockage sont présentées comme des sous-systèmes des grappes, selon la convention suivante :
    *   `system-compute` (par exemple `rorqual-compute`) : ressources CPU. Indiquez précisément vos besoins en mémoire puisqu’ils seront considérés dans votre allocation.
    *   `system-gpu` (par exemple `rorqual-gpu`) : ressources GPU.
    *   `system-storage` (par exemple `rorqual-storage`) : ressources de stockage; les listes montrent uniquement les ressources disponibles (`/project`, `/nearline`, etc.) dans chacun des sous-systèmes.

    Si, par exemple, vous avez besoin de ressources CPU et de ressources de stockage `/project` sur Rorqual, vous devez remplir deux demandes distinctes, soit une pour des cœurs-années et la mémoire avec le sous-système `rorqual-compute`, et une autre pour l’espace de stockage `/project` en To avec le sous-système `rorqual-storage`.

2.  **Sélectionner des ressources infonuagiques :** Si vous avez besoin de ressources infonuagiques dans des sites différents, vous devez remplir une demande distincte pour chacun des sites. Les ressources infonuagiques sont présentées selon la convention suivante :
    *   `system-compute-cloud` ou `system-persistent-cloud` : dans les nuages Arbutus, Fir et Béluga, vous pouvez sélectionner des instances de calcul ou des instances persistantes; et dans le nuage Nibi, seulement des instances persistantes. Les listes montrent uniquement les gabarits (*flavors* OpenStack) disponibles pour chacun des nuages.

Si vous avez des questions sur la manière de demander des ressources, écrivez à allocations@tech.alliancecan.ca.