---
title: "Accessing object storage with WinSCP/fr"
slug: "accessing_object_storage_with_winscp"
lang: "fr"

source_wiki_title: "Accessing object storage with WinSCP/fr"
source_hash: "46fb197e248e0756eeca96cd31276da0"
last_synced: "2026-04-10T14:10:18.226633+00:00"
last_processed: "2026-04-10T14:39:17.484010+00:00"

tags:
  - cloud

keywords:
  - "configuration"
  - "Arbutus"
  - "stockage objet"
  - "WinSCP"
  - "Amazon S3"

questions:
  - "Quelles sont les informations de base requises pour configurer une nouvelle session WinSCP vers le stockage objet Arbutus ?"
  - "Quel paramètre avancé doit être sélectionné dans le style d'URL pour que WinSCP fonctionne correctement et évite les erreurs de connexion ?"
  - "Comment l'utilisateur peut-il consulter les listes de contrôle d'accès (ACL) d'un fichier via l'interface de WinSCP ?"
  - "Quelles sont les informations de base requises pour configurer une nouvelle session WinSCP vers le stockage objet Arbutus ?"
  - "Quel paramètre avancé doit être sélectionné dans le style d'URL pour que WinSCP fonctionne correctement et évite les erreurs de connexion ?"
  - "Comment l'utilisateur peut-il consulter les listes de contrôle d'accès (ACL) d'un fichier via l'interface de WinSCP ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Cette page contient les renseignements sur la configuration et l'accès au [stockage objet sur Arbutus](arbutus_object_storage.md) avec WinSCP, l'un des [clients pour le stockage de ce type](arbutus_object_storage_clients.md).

## Installation
Installez WinSCP à partir de [https://winscp.net/](https://winscp.net/).

## Configuration
Sous *Nouvelle session*, entrez les informations suivantes :
*   Protocole de fichier : Amazon S3
*   Nom d'hôte : `object-arbutus.alliancecan.ca`
*   Numéro de port : `443`
*   ID de clé d'accès : `20_DIGIT_ACCESS_KEY`

Cliquez ensuite sur le bouton *Enregistrer*.

Cliquez ensuite sur le bouton *Modifier* et sur *Avancé...*. Sous *Environnement*, sélectionnez *S3*. Dans les options pour le protocole, sélectionnez *Chemin* dans le champ *Style d'URL*.

!!! warning "Configuration importante"
    Le choix de *Chemin* est important pour que WinSCP fonctionne correctement et évite les erreurs de connexion. En effet, sans ce paramètre, WinSCP pourrait afficher des messages d'erreur.

## Utilisation
Cliquez sur le bouton *Connexion* et utilisez l’interface de WinSCP pour créer des « buckets » (compartiments) et y transférer des fichiers.

## Listes de contrôle d'accès (ACL) et politiques
Cliquez avec le bouton droit sur le nom du fichier pour obtenir la liste des accès.