---
title: "National systems/fr"
slug: "national_systems"
lang: "fr"

source_wiki_title: "National systems/fr"
source_hash: "2d96226a3f11a3a6ba23cf4c7a70ec32"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:43:11.244812+00:00"

tags:
  []

keywords:
  - "Amii"
  - "TamIA"
  - "intelligence artificielle"
  - "Institut Vecteur"
  - "Intelligence artificielle"
  - "Stockage"
  - "Grappes de calcul"
  - "systèmes dédiés"
  - "Grappes EIPIA"
  - "communauté de recherche canadienne"
  - "Nœuds GPU"
  - "Nuage IaaS"
  - "Mila"
  - "Environnement informatique pancanadien de l’IA"
  - "Vulcan"

questions:
  - "Quelles sont les trois catégories de nœuds qui composent les grappes de calcul d'usage général ?"
  - "Sur quel modèle de service et quelle technologie l'infrastructure infonuagique (Nuage) est-elle basée ?"
  - "À quelle communauté de recherche spécifique les grappes EIPIA sont-elles dédiées ?"
  - "Quels sont les noms des trois projets ou systèmes répertoriés dans ce tableau ?"
  - "À quels instituts de recherche ces différents projets sont-ils respectivement associés ?"
  - "Quel est l'état actuel d'avancement ou de déploiement de l'ensemble de ces systèmes ?"
  - "Que représentent exactement les grappes de l'Environnement informatique pancanadien de l’IA (EIPIA) ?"
  - "À quelle communauté spécifique ces systèmes informatiques sont-ils dédiés ?"
  - "Quels types de besoins ces infrastructures visent-elles à combler ?"
  - "Quels sont les noms des trois projets ou systèmes répertoriés dans ce tableau ?"
  - "À quels instituts de recherche ces différents projets sont-ils respectivement associés ?"
  - "Quel est l'état actuel d'avancement ou de déploiement de l'ensemble de ces systèmes ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Grappes de calcul

La plupart de nos grappes sont d'usage général et sont conçues pour l'exécution de plusieurs types de tâches. Elles comportent des nœuds qui présentent des caractéristiques différentes et qui sont classés selon trois groupes :
* nœuds de base (*base nodes*) qui ont typiquement environ 4 Go de mémoire par cœur;
* nœuds de grande capacité (*large-memory nodes*) qui ont typiquement plus de 8 Go par cœur;
* nœuds GPU (*GPU nodes*) qui ont des [processeurs graphiques](https://fr.wikipedia.org/wiki/Processeur_graphique).

Toutes les grappes disposent de stockage de haute performance. Dans le tableau ci-dessous, cliquez sur le nom d'une grappe pour connaître les détails sur le nombre de nœuds disponibles, le nombre et les modèles de CPU et de GPU, la mémoire et le stockage.

### Liste des grappes de calcul

| Grappe | Type | Sous-systèmes | État |
|---|---|---|---|
| [Béluga](béluga.md) | Usage général | * beluga-compute<br>* beluga-gpu<br>* beluga-storage | En fin de vie |
| [Cedar](cedar.md) | Usage général | * cedar-compute<br>* cedar-gpu<br>* cedar-storage | En fin de vie |
| [Fir](fir.md) | Usage général | * fir-compute<br>* fir-gpu<br>* fir-storage | En production |
| [Graham](graham.md) | Usage général | * graham-compute<br>* graham-gpu<br>* graham-storage | En fin de vie |
| [Narval](narval.md) | Usage général | * narval-compute<br>* narval-gpu<br>* narval-storage | En production |
| [Niagara](niagara.md) | Tâches massivement parallèles | * niagara-compute<br>* niagara-storage<br>* hpss-storage | En fin de vie |
| [Nibi](nibi.md) | Usage général | * nibi-compute<br>* nibi-storage<br>* nibi-storage | En production |
| [Rorqual](rorqual.md) | Usage général | * rorqual-compute<br>* rorqual-gpu<br>* rorqual-storage | En production |
| [Trillium](trillium.md) | Tâches massivement parallèles | * trillium-compute<br>* trillium-gpu<br>* trillium-storage | En production |

## Nuage (IaaS)

Notre service infonuagique est offert selon le modèle IaaS (*Infrastructure as a Service*) basé sur OpenStack.

| Nuage | Sous-systèmes | Description | État |
|---|---|---|---|
| [Nuage Arbutus](cloud-resources.md#nuage-arbutus) | * arbutus-compute-cloud<br>* arbutus-persistent-cloud<br>* arbutus-dcache | * vCPU, VGPU, RAM<br>* Disque local éphémère<br>* Stockage de volumes et instantanés<br>* Stockage sur des systèmes de fichiers partagés<br>* Stockage objet<br>* Adresses IP flottantes<br>* Stockage dCache | En production |
| [Nuage Béluga](cloud-resources.md#nuage-beluga) | * beluga-compute-cloud<br>* beluga-persistent-cloud | * vCPU, RAM<br>* Disque local éphémère<br>* Stockage de volumes et instantanés<br>* Adresses IP flottantes | En production |
| [Nuage Cedar](cloud-resources.md#nuage-cedar) | * cedar-persistent-cloud<br>* cedar-compute-cloud | * vCPU, RAM<br>* Disque local éphémère<br>* Stockage de volumes et instantanés<br>* Adresses IP flottantes | En production |
| [Nuage Graham](cloud-resources.md#nuage-graham) | * graham-persistent-cloud | * vCPU, RAM<br>* Disque local éphémère<br>* Stockage de volumes et instantanés<br>* Adresses IP flottantes | En production |

## Grappes EIPIA

Les [grappes de l'Environnement informatique pancanadien de l’IA (EIPIA)](https://www.alliancecan.ca/fr/nos-services/calcul-informatique-de-pointe/environnement-de-calcul-pan-canadien-pour-lintelligence-artificielle-ecpia) sont des systèmes dédiés aux besoins émergents de la communauté de recherche canadienne en intelligence artificielle.

| Nom | Institut | État |
|---|---|---|
| [TamIA](tamia.md) | [Mila](https://mila.quebec/) | en production |
| [Killarney](killarney.md) | [Institut Vecteur](https://vectorinstitute.ai/) | en production |
| [Vulcan](vulcan.md) | [Amii](https://www.amii.ca/) | en production |