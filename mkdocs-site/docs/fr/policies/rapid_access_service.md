---
title: "Rapid Access Service/fr"
slug: "rapid_access_service"
lang: "fr"

source_wiki_title: "Rapid Access Service/fr"
source_hash: "2aa40c11428f2dadce18603b0d2d0434"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:00:29.052043+00:00"

tags:
  []

keywords:
  - "ressources de calcul"
  - "ressources GPU"
  - "allocation de ressources"
  - "GPU"
  - "Service d'accès rapide"
  - "intelligence artificielle"
  - "CPU"
  - "ressources infonuagiques"
  - "disponibilité des GPU"
  - "ordonnancement"
  - "groupes de recherche"
  - "Stockage"
  - "Ressources de calcul"

questions:
  - "Quelles démarches préalables les chercheurs doivent-ils accomplir dans la plateforme CCDB pour obtenir l'accès aux systèmes de calcul de l'Alliance ?"
  - "Quelles sont les limites de stockage (/project et /nearline) disponibles sans passer par le concours d'allocation, et comment les chercheurs principaux peuvent-ils les demander ?"
  - "Comment fonctionne l'utilisation opportuniste des ressources CPU et GPU, et quelle est la capacité moyenne visée par grappe pour les groupes de recherche ?"
  - "Pourquoi la disponibilité des GPU varie-t-elle et à quels moments est-elle particulièrement limitée ?"
  - "Quels utilisateurs peuvent s'attendre à un usage soutenu des GPU malgré les périodes de forte demande ?"
  - "Quelle est la procédure à suivre pour demander l'accès à des ressources infonuagiques ?"
  - "Comment les tâches sont-elles ordonnancées sur les grappes et comment l'utilisation des CPU est-elle comptabilisée ?"
  - "Quel type d'utilisation s'applique aux ressources GPU offertes par l'Alliance ?"
  - "Quelle condition un groupe de recherche doit-il remplir pour avoir le droit d'utiliser les ressources GPU ?"
  - "Pourquoi la disponibilité des GPU varie-t-elle et à quels moments est-elle particulièrement limitée ?"
  - "Quels utilisateurs peuvent s'attendre à un usage soutenu des GPU malgré les périodes de forte demande ?"
  - "Quelle est la procédure à suivre pour demander l'accès à des ressources infonuagiques ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! warning "Important"
    Pour utiliser les ressources de calcul de l'Alliance, les chercheuses principales, chercheurs principaux et les personnes parrainées doivent en demander l'accès dans [CCDB](https://ccdb.alliancecan.ca/me/access_systems). Certains systèmes nécessitent l'acceptation d'ententes supplémentaires (par exemple, conditions d'utilisation, accords de niveau de service, etc.) avant d'accorder l'accès. Si cette étape n'est pas respectée, il ne sera pas possible de se connecter au système voulu.

## Ressources pour le calcul de haute performance

### Stockage
Certaines [ressources de stockage](storage-and-file-management.md) sont mises à la disposition des chercheurs principaux et de leurs utilisateurs parrainés dans le RAP par défaut dès la création d'un compte Alliance dans CCDB. Elles seront prêtes à être utilisées dès que l'accès au système correspondant sera demandé ici : https://ccdb.alliancecan.ca/me/access_systems. Consultez cette page pour plus de détails sur les ressources de stockage disponibles par défaut.

Les chercheuses principales et chercheurs principaux peuvent demander au plus 40 To d’espace de stockage /project et 100 To d’espace de stockage /nearline, sans avoir besoin de présenter une demande au concours pour l’allocation de ressources. Les ressources de stockage peuvent être sur une même grappe d’usage général ou être distribuées sur plusieurs, mais *le total ne doit pas dépasser 40 To d’espace /project et 100 To d’espace /nearline*. Les ressources allouées via le service d’accès rapide se trouveront dans le [RAP par défaut](frequently-asked-questions-about-the-ccdb.md#rap-resource-allocation-project).

| Grappe                     | Stockage /project                                   | Stockage /nearline                                  |
| :------------------------- | :-------------------------------------------------- | :-------------------------------------------------- |
| Fir, Nibi, Rorqual, Narval | 40 To ou moins (*sur toutes les grappes*)           | 100 To ou moins (*sur toutes les grappes*)          |
| Trillium, HPSS             | stockage non disponible via le service d'accès rapide | stockage non disponible via le service d'accès rapide |

Pour demander des ressources de stockage via le service d'accès rapide, les chercheuses principales et chercheurs principaux (et non les co-chercheuses et co-chercheurs) doivent fournir les détails des ressources de stockage voulues en écrivant à support@tech.alliancecan.ca.

### CPU
Les ressources CPU sont disponibles pour une **utilisation opportuniste** à tous les groupes de recherche qui possèdent un compte actif avec l’Alliance. La plupart des tâches soumises de cette manière sont exécutées, malgré le fait que leur priorité puisse être inférieure à celle des tâches soumises dans le cadre d’un projet auquel des ressources sont allouées par concours.

Via le RAP par défaut, les groupes de recherche qui ont un compte avec l’Alliance et qui ont besoin de CPU **devraient pouvoir utiliser en moyenne jusqu'à 200 cœurs-années sur chacune des grappes**. La valeur de 200 représente une cible variable et non un nombre réservé ou un maximum de cœurs-années, ce qui signifie qu’un groupe pourrait utiliser plus ou moins que 200 cœurs-années, dépendant de la forme et de la taille de la tâche et aussi de l’utilisation générale de la grappe.

La plupart des groupes peuvent satisfaire leurs besoins en CPU en soumettant des tâches de façon opportuniste avec leur RAP par défaut, sans avoir à présenter une demande au concours pour l’allocation de ressources. Les tâches qui nécessitent beaucoup de mémoire peuvent prendre plus de temps à être exécutées; dans ces cas, la meilleure option serait de présenter une demande au concours si le nombre total de ressources CPU excède le minimum requis pour présenter une demande.

Veuillez prendre connaissance de la page [Allocation et ordonnancement des ressources de calcul](allocations-and-compute-scheduling.md) pour mieux comprendre comment les tâches sont ordonnancées sur nos grappes et comment l’utilisation des CPU est comptabilisée.

### GPU
Les ressources GPU sont disponibles pour une utilisation opportuniste à tous les groupes de recherche qui possèdent un compte actif avec l’Alliance.

La demande en GPU s’accroît rapidement en raison de l’augmentation de la recherche en intelligence artificielle. La disponibilité des GPU varie grandement au cours d’une même année et est particulièrement limitée à l’approche de conférences majeures.

Nous ne pouvons donc pas garantir la disponibilité des GPU pour usage opportuniste à chacun des groupes, surtout pendant les périodes de forte demande. Les utilisatrices et utilisateurs ayant obtenu une allocation de ressources via concours devraient pouvoir en faire un usage soutenu.

## Ressources infonuagiques
Les chercheuses principales et chercheurs principaux peuvent demander l’accès à de petites quantités de ressources infonuagiques en tout temps en remplissant [ce formulaire](https://docs.google.com/forms/d/e/1FAIpQLSdLOro7wY__sFUBjRNu_ZQ7sgjUpTn7lvNuI2e015oAsFPWbQ/viewform?hl=fr).

Les autres personnes détenant un compte avec l’Alliance peuvent aussi obtenir la permission d'accès à ces ressources.

Si vous avez des questions ou avez besoin d’assistance, écrivez à nuage@tech.alliancecan.ca.