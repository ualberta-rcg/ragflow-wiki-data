---
title: "National systems/fr"
tags:
  []

keywords:
  []
---

<span id="Compute_clusters"></span>
## Grappes de calcul

La plupart de nos grappes sont d'usage général et sont conçues pour l'exécution de plusieurs types de tâches. Elles comportent des nœuds qui présentent des caractéristiques différentes et qui sont classés selon trois groupes&nbsp;:
* nœuds de base (*base nodes*) qui ont typiquement environ 4Go de mémoire par cœur;
* nœuds de grande capacité (*large-memory nodes*) qui ont typiquement plus de 8Go par cœur;
* nœuds GPU (*GPU nodes*) qui ont des [processeurs graphiques](https://fr.wikipedia.org/wiki/Processeur_graphique).

Toutes les grappes disposent de stockage de haute performance. Dans le tableau ci-dessous, cliquez sur le nom d'une grappe pour connaître les détails sur le nombre de nœuds disponibles, le nombre et les modèles de CPU et de GPU le stockage, la mémoire et le stockage. 

<span id="List_of_compute_clusters"></span>
### Liste des grappes de calcul

{| class="wikitable"
|-
! Grappe !! Type !! Sous-systèmes !! État
|-
| [Béluga](béluga.md)
| Usage général
|
* beluga-compute
* beluga-gpu
* beluga-storage
| En fin de vie
|-
| [Cedar](cedar-fr.md)
| Usage général
|
* cedar-compute
* cedar-gpu
* cedar-storage
| En fin de vie
|-
| [Fir](fir-fr.md)
| Usage général
|
* fir-compute
* fir-gpu
* fir-storage
| En production
|-
| [Graham](graham-fr.md)
| Usage général
|
* graham-compute
* graham-gpu
* graham-storage
| En fin de vie
|-
| [Narval](narval.md)
| Usage général
|
* narval-compute
* narval-gpu
* narval-storage
| En production
|-
| [Niagara](niagara.md)
| Tâches massivement parallèles
|
* niagara-compute
* niagara-storage
* hpss-storage
| En fin de vie
|-
| [Nibi](nibi.md)
| Usage général
|
* nibi-compute
* nibi-storage
* nibi-storage
| En production
|-
| [Rorqual](rorqual.md)
| Usage général
|
* rorqual-compute
* rorqual-gpu
* rorqual-storage
| En production
|-
| [Trillium](trillium-fr.md)
| Tâches massivement parallèles
|
* trillium-compute
* trillium-gpu
* trillium-storage
| En production
|}

## Nuage (IaaS)
Notre service infonuagique est offert selon le modèle IaaS (*Infrastructure as a Service*) basé sur OpenStack.

{| class="wikitable"
|-
! Nuage !! Sous-systèmes !! Description !! État
|-
| [Nuage Arbutus](cloud_resources-fr#nuage_arbutus.md)
|
* arbutus-compute-cloud
* arbutus-persistent-cloud
* arbutus-dcache
|
* vCPU, VGPU, RAM
* Disque local éphémère
* Stockage de volumes et instantanés
* Stockage sur des systèmes de fichiers partagés
* Stockage objet
* Adresses IP flottantes
* Stockage dCache 
| En production
|-
| [Nuage Béluga](cloud_resources-fr#nuage_b.c3.a9luga.md)
|
* beluga-compute-cloud
* beluga-persistent-cloud
|
* vCPU, RAM
* Disque local éphémère
* Stockage de volumes et instantanés
* Adresses IP flottantes
| En production
|-
| [Nuage Cedar](cloud_resources-fr#nuage_cedar.md)
|
* cedar-persistent-cloud
* cedar-compute-cloud
|
* vCPU, RAM
* Disque local éphémère
* Stockage de volumes et instantanés
* Adresses IP flottantes
| En production
|-
| [Nuage Graham](cloud_resources-fr#nuage_graham.md)
|
* graham-persistent-cloud
|
* vCPU, RAM
* Disque local éphémère
* Stockage de volumes et instantanés
* Adresses IP flottantes
| En production
|}

<span id="PAICE_clusters"></span>
## Grappes EIPIA

Les [grappes de l'Environnement informatique pancanadien de l’IA (EIPIA)](https://www.alliancecan.ca/fr/nos-services/calcul-informatique-de-pointe/environnement-de-calcul-pan-canadien-pour-lintelligence-artificielle-ecpia) sont des systèmes dédiés aux besoins émergeants de la communauté de recherche canadienne en intelligence articifielle. 

{| class="wikitable"
|-
! Nom !! Institut !! État
|-
<!--| [TamIA](tamia.md)-->
| [TamIA](tamia.md)
| [Mila](https://mila.quebec/)
| en production
|-
| [Killarney](killarney.md)
| [Institut Vecteur](https://vectorinstitute.ai/)
| en production
|-
| [Vulcan](vulcan-fr.md)

| [Amii](https://www.amii.ca/)
| en production
|}