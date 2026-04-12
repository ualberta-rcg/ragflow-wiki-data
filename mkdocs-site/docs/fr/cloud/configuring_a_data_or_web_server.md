---
title: "Configuring a data or web server/fr"
slug: "configuring_a_data_or_web_server"
lang: "fr"

source_wiki_title: "Configuring a data or web server/fr"
source_hash: "e4cffcf1822df9c3674eac6e4a95393b"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:33:47.526581+00:00"

tags:
  - cloud

keywords:
  - "Gabarits de type persistant"
  - "Instances"
  - "Service infonuagique"
  - "Serveurs FTP"
  - "Serveur web"

questions:
  - "Comment sont configurées et démarrées les instances destinées à fournir des données génériques ou du contenu Web ?"
  - "Où peut-on trouver les instructions pour créer un serveur de données partagées tel qu'un serveur FTP, HTTP ou SFTP ?"
  - "Quel guide doit-on consulter pour configurer spécifiquement un serveur web dans l'environnement infonuagique ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Page enfant de [Service infonuagique de Calcul Canada](cloud.md)*

Les instances (machines virtuelles ou VMs) utilisées pour fournir des données génériques ou du contenu Web sont configurées selon les gabarits de type persistant (voir [Gabarits d'instances](virtual-machine-flavors.md)) et sont [démarrées depuis un volume](working-with-volumes.md#démarrer-depuis-un-volume).

!!! tip "Ressources additionnelles"
    *   Pour créer un serveur de données partagées, consultez [Serveurs FTP dans notre environnement infonuagique](ftp-server-in-the-cloud.md) où il est aussi question de HTTP et SFTP.
    *   Pour créer un serveur web, consultez [Création d'un serveur web dans notre environnement infonuagique](creating-a-webserver-on-the-cloud.md).