---
title: "Recovering data from a compromised VM/fr"
slug: "recovering_data_from_a_compromised_vm"
lang: "fr"

source_wiki_title: "Recovering data from a compromised VM/fr"
source_hash: "8f659481e7bdb44a880a89a2e2d1525f"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:01:55.461350+00:00"

tags:
  - cloud

keywords:
  - "machine virtuelle"
  - "OpenStack"
  - "volume"
  - "récupération de données"
  - "compromise"

questions:
  - "Quelles sont les actions entreprises par l'équipe de soutien technique lorsqu'une machine virtuelle est compromise ?"
  - "Pour quelles raisons est-il nécessaire de construire une nouvelle machine virtuelle au lieu de réutiliser celle qui a été compromise ?"
  - "Quelles sont les étapes techniques à suivre pour attacher le volume compromis à une nouvelle instance et récupérer les données ?"
  - "Quelles sont les actions entreprises par l'équipe de soutien technique lorsqu'une machine virtuelle est compromise ?"
  - "Pour quelles raisons est-il nécessaire de construire une nouvelle machine virtuelle au lieu de réutiliser celle qui a été compromise ?"
  - "Quelles sont les étapes techniques à suivre pour attacher le volume compromis à une nouvelle instance et récupérer les données ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Service infonuagique](cloud.md)

Vous êtes responsable de récupérer les données d'une machine virtuelle qui a été compromise.

!!! note "Renseignements importants"
    Les renseignements fournis ici ne sont pas exhaustifs, mais vous aurez une idée de la marche à suivre dans une telle situation.

## Que se passe-t-il quand une machine virtuelle est compromise?
1. Ceci est confirmé par notre équipe de soutien technique après analyse des journaux du trafic et d'autres sources.
2. La machine virtuelle est fermée au niveau de l'administration système.
3. Nous vous enverrons un courriel à cet effet.

## Pourquoi faut-il rebâtir la machine virtuelle?
* Vous ne pouvez pas démarrer une machine virtuelle qui a été verrouillée au niveau de l'administration système.
* Le contenu de la machine virtuelle n'est plus intègre, mais il est relativement sécuritaire d'en extraire les données.
* Il faut construire une nouvelle machine virtuelle.

## Comment faut-il procéder?
1. Écrivez à [nuage@tech.alliancecan.ca](mailto:nuage@tech.alliancecan.ca) en expliquant votre plan de récupération. S'il est nécessaire d'accéder aux systèmes de fichiers, le volume sera déverrouillé par notre équipe de soutien technique.
2. Connectez-vous à la console OpenStack.
3. Démarrez une nouvelle instance pour servir à la récupération.
4. Dans *Volumes*, sélectionnez *Gérer les attachements* dans le menu déroulant à droite du volume compromis et cliquez sur le bouton *Détacher le volume*.
5. Dans *Volumes*, sélectionnez *Gérer les attachements* dans le menu déroulant à droite du volume compromis et cliquez sur le bouton *Attacher le volume*. (Sélectionnez l'instance que vous venez de démarrer).
6. Connectez-vous par SSH à la nouvelle instance. Le volume compromis est le disque `vdb`.
7. Le montage du bon système de fichiers à partir d'une partition ou d'un disque LVM (gestionnaire de volumes logiques) dépend grandement de la manière dont l'image de base du système d'exploitation a été créée. Vous aurez besoin de l'aide d'une personne expérimentée pour mener à bien la récupération de vos données.