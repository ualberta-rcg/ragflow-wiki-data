---
title: "Arbutus object storage clients/fr"
tags:
  - cloud

keywords:
  []
---

Pour l'information sur comment obtenir de l'espace de stockage objet sur Arbutus, voir  [cette page wiki](arbutus-object-storage-fr.md). Voyez aussi l'information sur les clients&nbsp;:
* [Stockage objet : Accès avec s3cmd](accessing-object-storage-with-s3cmd-fr.md)
* [Stockage objet : Accès avec WinSCP](accessing-object-storage-with-winscp-fr.md)
* [Stockage objet : Accès avec AWS CLI](accessing-the-arbutus-object-storage-with-aws-cli-fr.md)
* [Stockage objet sur Arbutus : Accès via Globus](globus-fr#stockage_objet_sur_arbutus.md)

Il faut noter que la solution de stockage objet sur Arbutus n'utilise pas l’approche [S3 Virtual Hosting](https://documentation.help/s3-dg-20060301/VirtualHosting.html) d’Amazon avec des buckets DNS, contrairement à ces clients qui l’offrent par défaut. Pour ne pas utiliser cette approche, il faut donc configurer les clients en conséquence.