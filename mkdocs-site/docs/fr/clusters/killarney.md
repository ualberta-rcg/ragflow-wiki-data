---
title: "Killarney/fr"
tags:
  []

keywords:
  []
---

{| class="wikitable"
|-
| Disponibilité : 2025-06-09
|-
| Nœud de connexion :  <b>killarney.alliancecan.ca</b>
|-
| Collection Globus : [en préparation]
|-
| Page d'état : https://status.alliancecan.ca/system/Killarney
|}

<b>Killarney</b> est une grappe qui répond aux besoins de la communauté scientifique canadienne en intelligence artificielle. Elle est située à [l'Université de Toronto](https://www.utoronto.ca/) et gérée par  [l'Institut Vecteur](https://vectorinstitute.ai/) et [SciNet](https://www.scinethpc.ca/). Son nom rappelle   [le parc provincial Killarney](https://www.ontarioparks.ca/park/killarney/fr) qui se trouve près de la baie Georgienne, en Ontario.

Killarney fait partie de ECPIA, l'environnement de calcul pan-canadien pour l'intelligence artificielle.

## Particularités
Killarney est présentement disponible pour les chercheuses principales et chercheurs principaux titulaires d'une chaire en intelligence artificielle (IACC) et affiliés à Vector, ainsi que celles et ceux qui sont dans un programme d'IA d'une université canadienne ou qui utilisent l'IA dans leurs travaux de recherche.

## Accès
[Demandez l'accès dans le portail CCDB](https://ccdb.alliancecan.ca/me/access_services).

Les chercheuses principales et chercheurs principaux doivent obtenir de la part de leur établissement un RAP (*Resource Allocation Project*) de type AIP (*Artificial Intelligence Project*); le nom du projet sera préfixé de `aip-`. Pour parrainer les personnes qui participent au projet RAP, la chercheuse principale ou le chercheur principal doit [demander l'accès à l'Environnement informatique pancanadien de l’IA (EIPIA)](https://ccdb.alliancecan.ca/paice/general_access_to_paice_systems).

Pour identifier les personnes que vous parrainez pour le projet, 
* Faites afficher le tableau <i>Projet(s) avec allocation de ressources</i> dans CCDB.
* Cliquez sur le RAPI de votre projet AIP (préfixé `aip-`).
* Au bas de la page <i>Détails pour le projet</i>, cliquez sur <i>Gérer l'appartenance aux projets</i>.
* Entrez le ou les CCRI des personnes que vous parrainez.

Dans le cadre de ses mesures de cybersécurité, Vector applique le blocage géographique à Killarney afin d'assurer l'intégrité et la sécurité. Vector restreint l'accès aux pays identifiés dans [Évaluation des cybermenaces nationales 2025-2026](https://www.cyber.gc.ca/fr/orientation/evaluation-cybermenaces-nationales-2025-2026) publié par le gouvernement du Canada.

<span id="Killarney_hardware_specifications"></span>
## Matériel

{| class="wikitable sortable"
!Performance|| Nœuds !! Modèle || CPU !! Cœurs !! Mémoire système !! GPU par nœud || Total de GPU 
|-
|  Calcul standard || 168 || Dell 750xa || 2 x Intel Xeon Gold 6338 || 64 || 512 GB || 4 x NVIDIA L40S 48GB || 672
|-
|  Calcul de performance || 10 || Dell XE9680 || 2 x Intel Xeon Gold 6442Y || 48 || 2048 GB || 8 x NVIDIA H100 SXM 80GB || 80
|}

<span id="Storage_system"></span>
## Stockage

Le système de stockage est une plateforme NVME VastData avec une capacité utilisable de 1.7Po.

{| class="wikitable sortable"
|-
| <b>/home</b>||
* emplacement des répertoires /home
* [quota fixe](storage-and-file-management-fr#quotas_et_politiques.md) pour chaque répertoire
* les demandes pour plus d'espace sont dirigées vers /project
* sauvegarde quotidienne
|-
| <b>/scratch</b>||
* conçu pour le stockage actif ou temporaire
* [grand quota fixe](storage-and-file-management-fr#quotas_et_politiques.md) par utilisateur
* les données inactives sont [purgées](scratch-purging-policy-fr.md)
|-
|<b>/project</b>
||
* [grand quota ajustable](storage-and-file-management-fr#quotas_et_politiques.md) par projet
* sauvegarde quotidienne
|}

<span id="Network_interconnects"></span>
## Réseautique

* Nœuds de calcul standard : Infiniband HDR100, débit de 100Gbps
* Nœuds de calcul de performance : 2 x HDR 200, débit agrégé de 400Gbps

## Ordonnancement
L'ordonnanceur Slurm exécute les tâches soumises par les utilisateurs. Les commandes Slurm de base sont semblables à celles pour les autres systèmes nationaux.

## Logiciel
* Pile logicielle de modules.
* Pile logicielle standard de l'Alliance et logiciels particuliers à chaque grappe.