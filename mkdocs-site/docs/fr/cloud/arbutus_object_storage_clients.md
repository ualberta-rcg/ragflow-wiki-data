---
title: "Arbutus object storage clients/fr"
slug: "arbutus_object_storage_clients"
lang: "fr"

source_wiki_title: "Arbutus object storage clients/fr"
source_hash: "5159f1ada837bc70c92a773218a957b2"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T04:38:15.186042+00:00"

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

Pour de l'information sur comment obtenir de l'espace de stockage objet sur Arbutus, voir [cette page wiki](arbutus-object-storage.md). Voyez aussi de l'information sur les clients :
* [Stockage objet : Accès avec s3cmd](accessing-object-storage-with-s3cmd.md)
* [Stockage objet : Accès avec WinSCP](accessing-object-storage-with-winscp.md)
* [Stockage objet : Accès avec AWS CLI](accessing-the-arbutus-object-storage-with-aws-cli.md)
* [Stockage objet sur Arbutus : Accès via Globus](globus.md#stockage-objet-sur-arbutus)

Il faut noter que la solution de stockage objet sur Arbutus n'utilise pas l’approche [S3 Virtual Hosting](https://documentation.help/s3-dg-20060301/VirtualHosting.html) d’Amazon avec des *buckets* DNS, contrairement à ces clients qui l’offrent par défaut. Pour ne pas utiliser cette approche, il faut donc configurer les clients en conséquence.