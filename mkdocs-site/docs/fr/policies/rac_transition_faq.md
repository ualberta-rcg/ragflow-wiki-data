---
title: "RAC transition FAQ/fr"
slug: "rac_transition_faq"
lang: "fr"

source_wiki_title: "RAC transition FAQ/fr"
source_hash: "30d812ce57d21925df978515b0208b0e"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T10:39:39.141795+00:00"

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

Les ressources allouées suite aux concours pour 2021 seront disponibles à compter du 1er avril. La période de transition devrait se dérouler comme suit :

### Stockage
*   La période de transition pour les ressources de stockage sera de 30 jours à compter du 1er avril 2021.
*   Pendant la période de transition, le quota en vigueur sera celui de 2020 ou de 2021, selon lequel est le plus élevé.
*   Les utilisateurs sont responsables de déplacer leurs données avec Globus, `scp`, `rsync`, etc. Pour les détails, consultez [Transfert de données](transferring-data.md). L'équipe de [soutien technique](technical-support.md) peut vous conseiller ou vous assister si les données à déplacer sont de 200 To ou plus.
*   La mise en service ou hors service des différents systèmes de stockage ne s'effectuera pas au même moment. Pour la période de transition, le quota sera calculé avec SUM(2020, 2021).
*   Les quotas par défaut s'appliqueront pour chacun des autres chercheurs principaux.
*   À la fin de la période de transition, les quotas pour les sites d'origine seront fixés aux quotas par défaut. Les utilisateurs sont responsables de la suppression de leurs données dans les sites d'origine lorsque les niveaux d'utilisation dépassent le nouveau quota par défaut.

!!! warning "Suppression de données"
    Si les données ne sont pas supprimées, l'équipe technique pourrait en effectuer la suppression sans autre préavis.

*   Toute demande raisonnable d'extension de la période de transition sera acceptée. Cependant, il pourrait être impossible de prolonger cette période dans le cas des grappes qui seront mises hors service.

### Ordonnancement des tâches
*   L'équipe responsable de l'ordonnanceur prévoit archiver et compacter la base de données Slurm le 31 mars, avant l'implémentation des allocations qui se fera le 1er avril. Ces opérations devraient pouvoir s'effectuer au cours des heures creuses.

!!! note "Disponibilité de la base de données"
    Il est possible que la base de données ne réponde pas, particulièrement les commandes `sacct` et `sacctmgr`.

*   Nous devrions procéder au remplacement des allocations de 2020 par celles de 2021 à compter du 1er avril 2021.
*   Au cours de la période de transition, les allocations par défaut pourraient connaître une baisse de priorité.
*   Les tâches ordonnancées seront conservées. Les tâches en cours seront menées à terme. Les tâches en attente pourraient être retenues.

!!! warning "Tâches en attente non ordonnancées"
    Il est possible que les tâches en attente ne soient pas ordonnancées après la période de transition, dans le cas des allocations déplacées ou non renouvelées. L'information sur la façon d'identifier et de traiter ces cas suivra sous peu.