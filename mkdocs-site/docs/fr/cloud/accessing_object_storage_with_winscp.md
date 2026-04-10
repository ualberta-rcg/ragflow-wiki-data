---
title: "Accessing object storage with WinSCP/fr"
tags:
  - cloud

keywords:
  - configuration
  - stockage objet
  - Amazon S3
  - WinSCP
  - Arbutus
---

Cette page contient les renseignements sur la configuration et l'accès au [stockage objet sur Arbutus](arbutus-object-storage-fr.md) avec WinSCP, l'un des [clients pour le stockage de ce type](arbutus_object_storage_clients-fr.md).

## Installation 
Installez WinSCP à partir de https://winscp.net/.

## Configuration 
Sous <i>New Session</i>, entrez
<ul>
<li>File protocol: Amazon S3</li>
<li>Host name: object-arbutus.alliancecan.ca</li>
<li>Port number: 443</li>
<li>Access key ID: 20_DIGIT_ACCESS_KEY</li>
</ul>
Cliquez ensuite sur le bouton <i>Save</i>

[600px|thumb|center|Fenêtre de configuration](file:winscp-configuration.png.md)

Cliquez ensuite sur le bouton <i>Edit</i> et sur <i>Advanced...</i>. Sous <i>Environment</i> sélectionnez <i>S3</i>. Dans les options pour le protocole, sélectionnez <i>Path</i> dans le champ <i>URL style</i>.

[600px|thumb|center|Fenêtre de configuration du chemin](file:winscp-path-configuration.png.md)

Le choix de <i>Path</i> est important pour que WinSCP fonctionne et évite les erreurs comme 
[400px|thumb|center|Message d'erreur](file:winscp-resolve-error.png.md)

## Utilisation 
Cliquez sur le bouton *Login* et utilisez l’interface de WinSCP pour créer des buckets et y transférer des fichiers.

[800px|thumb|center|Fenêtre de transfert de fichiers](file:winscp-transfers.png.md)

## Listes de contrôle d'accès (ACL) et politiques 
Cliquez avec le bouton droit sur le nom du fichier pour obtenir la liste des accès, par exemple
[400px|thumb|center|Lite des ACL](file:winscp-acl.png.md)