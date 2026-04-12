---
title: "Arbutus object storage clients/fr"
slug: "arbutus_object_storage_clients"
lang: "fr"

source_wiki_title: "Arbutus object storage clients/fr"
source_hash: "5159f1ada837bc70c92a773218a957b2"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:29:29.665734+00:00"

tags:
  - cloud

keywords:
  - "Stockage objet"
  - "AWS CLI"
  - "Arbutus"
  - "s3cmd"
  - "S3 Virtual Hosting"

questions:
  - "Comment peut-on obtenir de l'espace de stockage objet sur le système Arbutus ?"
  - "Quels sont les différents logiciels clients mentionnés pour accéder à ce stockage objet ?"
  - "Quelle particularité technique concernant le \"S3 Virtual Hosting\" nécessite une configuration spécifique des clients ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Pour obtenir de l'information sur l'espace de stockage objet sur Arbutus, consultez [cette page wiki](arbutus_object_storage.md). Voyez aussi les pages d'information sur les clients :
*   [Stockage objet : Accès avec s3cmd](accessing_object_storage_with_s3cmd.md)
*   [Stockage objet : Accès avec WinSCP](accessing_object_storage_with_winscp.md)
*   [Stockage objet : Accès avec AWS CLI](accessing_the_arbutus_object_storage_with_aws_cli.md)
*   [Stockage objet sur Arbutus : Accès via Globus](../getting-started/globus.md#stockage-objet-sur-arbutus)

!!! attention
    Il faut noter que la solution de stockage objet sur Arbutus n'utilise pas l’approche [S3 Virtual Hosting](https://documentation.help/s3-dg-20060301/VirtualHosting.html) d’Amazon avec des buckets DNS. La plupart des clients S3 l’offrent par défaut; pour ne pas utiliser cette approche, il est donc essentiel de configurer les clients en conséquence.