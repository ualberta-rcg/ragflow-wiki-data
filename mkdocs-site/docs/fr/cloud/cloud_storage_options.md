---
title: "Cloud storage options/fr"
slug: "cloud_storage_options"
lang: "fr"

source_wiki_title: "Cloud storage options/fr"
source_hash: "1a526e905769f4380164ff7b8b83541e"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:26:39.486434+00:00"

tags:
  - cloud

keywords:
  - "volume"
  - "système de fichiers partagé"
  - "stockage objet"
  - "disque de stockage éphémère"
  - "types de stockage"

questions:
  - "Quels sont les quatre types de stockage infonuagique présentés et quelle est la fonction principale de chacun ?"
  - "Quel type de stockage est le plus adapté pour être monté simultanément sur plusieurs instances tout en bénéficiant de sauvegardes automatiques ?"
  - "Quelles sont les différences majeures entre un volume et un disque de stockage éphémère en matière de conservation des données lors de la suppression d'une instance ?"
  - "Quels sont les quatre types de stockage infonuagique présentés et quelle est la fonction principale de chacun ?"
  - "Quel type de stockage est le plus adapté pour être monté simultanément sur plusieurs instances tout en bénéficiant de sauvegardes automatiques ?"
  - "Quelles sont les différences majeures entre un volume et un disque de stockage éphémère en matière de conservation des données lors de la suppression d'une instance ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Nos nuages offrent les types de stockage suivants :

*   **[Volume](working-with-volumes.md#volumes)** : unité de stockage infonuagique standard qui peut être attachée et détachée d’une instance.
*   **Disque de stockage éphémère** : disque local virtuel associé au cycle de vie d’une instance sur un disque local d'un hyperviseur (un disque local de gabarit C pourrait être perdu).
*   **[Stockage objet](arbutus-object-storage.md)** : stockage non hiérarchique pour les données créées ou téléversées sous forme de fichier complet.
*   **[Système de fichiers partagé](cephfs.md)** : espace de stockage privé connecté au réseau (similaire aux partages NFS/SMB); doit être configuré sur chaque instance où il est monté.

## Comparaison des types de stockage

| | Volume | Disque de stockage éphémère | Stockage objet | Système de fichiers partagé |
|---|---|---|---|---|
| Stockage par défaut | oui | oui | non | non |
| Accès possible via un navigateur Web | non | non | oui | non |
| Restriction possible de l'accès pour un groupe d'IP sources | s.o. | s.o. | oui (S3 ACL) | s.o. |
| Peut être monté sur une instance | oui | oui | non | oui |
| Peut être monté simultanément sur plusieurs instances dans plusieurs projets | non | non | non | oui |
| Sauvegarde automatique | non (manuellement pour les instantanés) | non | non | oui (sur ruban tous les soirs) |
| Convient pour l’accès en écriture unique, en lecture seule et pour l’accès par le public | non | non | oui | non |
| Convient pour les données et/ou fichiers qui sont fréquemment modifiés | oui | oui | non | oui |
| Système de fichiers hiérarchique | oui | oui | non | oui |
| Convient au stockage à long terme | oui | non | oui | oui |
| Convient au stockage dédié pour serveurs individuels | oui | uniquement pour données temporaires | non | non |
| Supprimé automatiquement quand l'instance est supprimée | non | oui | non | non |
| Unité de mesure de l’espace alloué | Go | Go | To | To |
| Tolérance des pannes de plusieurs disques | oui | non pour les gabarits C; oui pour les gabarits P | oui | oui |
| Chiffrement physique des disques | non | non | non | non |