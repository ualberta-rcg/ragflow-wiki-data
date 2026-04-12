---
title: "RAC transition FAQ/fr"
slug: "rac_transition_faq"
lang: "fr"

source_wiki_title: "RAC transition FAQ/fr"
source_hash: "30d812ce57d21925df978515b0208b0e"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:56:07.298296+00:00"

tags:
  []

keywords:
  - "stockage"
  - "quotas"
  - "période de transition"
  - "ordonnancement des tâches"
  - "ressources allouées"

questions:
  - "Quelles sont les responsabilités des utilisateurs concernant le transfert et la suppression de leurs données lors de la transition ?"
  - "Comment les quotas de stockage seront-ils déterminés pendant la période de transition débutant le 1er avril ?"
  - "Quel sera l'impact de la mise en place des nouvelles allocations de 2021 sur les tâches en cours et en attente dans l'ordonnanceur ?"
  - "Quelles sont les responsabilités des utilisateurs concernant le transfert et la suppression de leurs données lors de la transition ?"
  - "Comment les quotas de stockage seront-ils déterminés pendant la période de transition débutant le 1er avril ?"
  - "Quel sera l'impact de la mise en place des nouvelles allocations de 2021 sur les tâches en cours et en attente dans l'ordonnanceur ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Les ressources allouées par suite des concours pour 2021 seront disponibles à compter du 1 avril. La période de transition devrait se dérouler comme suit :

## Stockage
* La période de transition pour les ressources de stockage sera de 30 jours à compter du 1 avril 2021.
* Pendant la période de transition, le quota en vigueur sera celui de 2020 ou de 2021, dépendant duquel est le plus élevé.
* Les utilisateurs sont responsables de déplacer leurs données avec `Globus`, `scp`, `rsync`, etc.; pour les détails, consultez [Transfert de données](../getting-started/transferring_data.md). L’équipe de [soutien technique](../support/technical_support.md) peut vous conseiller ou vous assister si les données à déplacer sont de 200 To ou plus.
* La mise en service ou hors service des différents systèmes de stockage ne s’effectuera au même moment. Pour la période de transition, le quota sera calculé avec `SUM(2020, 2021)`.
* Les quotas par défaut s’appliqueront pour chacun des autres chercheurs principaux.
* À la fin de la période de transition, les quotas pour les sites d’origine seront fixés aux quotas par défaut. Les utilisateurs sont responsables de la suppression de leurs données dans les sites d’origine quand les niveaux d’utilisation dépassent le nouveau quota par défaut.

!!! attention "Important : Suppression de données"
    Si les données ne sont pas supprimées, l’équipe technique pourrait en effectuer la suppression sans autre préavis.

* Toute demande raisonnable d’extension de la période de transition sera acceptée.

!!! note "Note : Prolongation de la période de transition"
    Cependant, il pourrait être impossible de prolonger cette période dans le cas des grappes qui seront mises hors service.

## Ordonnancement des tâches
* L’équipe responsable de l’ordonnanceur prévoit archiver et compacter la base de données `Slurm` le 31 mars, avant l’implémentation des allocations qui se fera le 1 avril. Ces opérations devraient pouvoir s’effectuer au cours des heures creuses.

!!! avertissement "Avertissement : Indisponibilité de la base de données Slurm"
    Il est possible que la base de données ne réponde pas, particulièrement `sacct` et `sacctmgr`.

* Nous devrions procéder au remplacement des allocations de 2020 par celles de 2021 à compter du 1 avril 2021.
* Au cours de la période de transition, les allocations par défaut pourraient connaître une baisse de priorité.
* Les tâches ordonnancées seront conservées. Les tâches en cours seront menées à terme. Les tâches en attente pourraient être retenues.

!!! attention "Important : Impact sur les tâches en attente"
    Il est possible que les tâches en attente ne soient pas ordonnancées après la période de transition, dans le cas des allocations déplacées ou non renouvelées. L’information sur comment identifier et traiter ces cas suivra sous peu.