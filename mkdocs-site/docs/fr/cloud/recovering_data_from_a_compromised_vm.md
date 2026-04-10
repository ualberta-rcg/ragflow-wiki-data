---
title: "Recovering data from a compromised VM/fr"
slug: "recovering_data_from_a_compromised_vm"
lang: "fr"

source_wiki_title: "Recovering data from a compromised VM/fr"
source_hash: "8f659481e7bdb44a880a89a2e2d1525f"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T10:46:28.492089+00:00"

tags:
  - cloud

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

*Page enfant de [Service infonuagique](cloud.md)*

Vous êtes responsable de récupérer les données d'une machine virtuelle qui a été compromise.

!!! note
    L'information donnée ici n'est pas complète, mais vous saurez quoi faire dans une telle situation.

## Que se passe-t-il quand une machine virtuelle est compromise?

1.  Ceci est confirmé par notre équipe de soutien technique après analyse des journaux du trafic et d'autres sources.
2.  La machine virtuelle est fermée au niveau sysadmin.
3.  Nous vous faisons parvenir un courriel à cet effet.

## Pourquoi devez-vous reconstruire la machine virtuelle?

*   Vous ne pouvez pas lancer une machine virtuelle qui a été verrouillée au niveau sysadmin.
*   Le contenu de la machine virtuelle n'est plus intègre, mais il est relativement sécuritaire d'en extraire les données.
*   Vous devez construire une nouvelle machine virtuelle.

## Comment devez-vous procéder?

1.  Écrivez à [nuage@tech.alliancecan.ca](mailto:nuage@tech.alliancecan.ca) en expliquant votre plan de récupération. S'il est nécessaire d'accéder aux systèmes de fichiers, le volume sera déverrouillé par notre équipe de soutien technique.
2.  Connectez-vous à la console OpenStack.
3.  Lancez une nouvelle instance pour servir à la récupération.
4.  Dans *Volumes*, sélectionnez *Gérer les attachements* de la liste déroulante à droite du volume compromis et cliquez sur le bouton *Détacher le volume*.
5.  Dans *Volumes*, sélectionnez *Gérer les attachements* de la liste déroulante à droite du volume compromis et cliquez sur le bouton *Attacher le volume* (sélectionnez l'instance que vous venez de lancer).
6.  Connectez-vous via SSH à la nouvelle instance. Le volume compromis est le disque `vdb`.
7.  Monter le bon système de fichiers à partir d'une partition ou d'un disque LVM (*gestionnaire de volumes logiques*) dépend largement de comment l'image de base du système d'exploitation a été créée. Vous aurez besoin d'une personne d'expérience pour terminer la récupération de vos données.