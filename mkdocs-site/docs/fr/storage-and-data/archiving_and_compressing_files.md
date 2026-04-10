---
title: "Archiving and compressing files/fr"
slug: "archiving_and_compressing_files"
lang: "fr"

source_wiki_title: "Archiving and compressing files/fr"
source_hash: "d5d496a90ca8264b02d1ba22ff6d0889"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T04:38:57.081606+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

*Page enfant de: [Stockage et gestion de fichiers](storage-and-file-management.md)*

[Archiver](https://fr.wikipedia.org/wiki/Archive_(informatique)) signifie créer un fichier qui contient plusieurs petits fichiers. Le fait de créer un fichier archive peut améliorer l'efficacité du stockage et vous aider à [respecter les quotas](storage-and-file-management.md#quotas-et-politiques). L'archivage peut aussi rendre plus efficace le [transfert de fichiers](general-directives-for-migration.md). Par exemple, le protocole [scp](https://fr.wikipedia.org/wiki/Secure_copy) (*secure copy protocol*) transfère plus rapidement un fichier archive de taille raisonnable que des milliers de petits fichiers totalisant la même taille.

[Compresser](https://fr.wikipedia.org/wiki/Compression_de_donn%C3%A9es) signifie modifier le code d'un fichier pour en réduire le nombre de bits. Les avantages sont évidents en ce qui concerne le stockage à long terme des données. Dans le cas du [transfert de données](general-directives-for-migration.md), il faut comparer le temps de compression au temps nécessaire pour déplacer une quantité moindre de bits; voyez [ce texte](https://bluewaters.ncsa.illinois.edu/data-transfer-doc) du National Center for Supercomputing Applications.

*   Sous Linux, `tar` est un outil d'archivage et de compression bien connu; voyez le [tutoriel `tar`](a-tutorial-on-tar.md).
*   Aussi pour l'archivage et la compression, `dar` offre certaines fonctions avantageuses; voyez le [tutoriel `dar`](dar.md).
*   L'utilitaire `zip` est bien connu pour l'archivage et la compression dans l'environnement Windows, mais il est disponible avec les grappes de Calcul Canada.
*   Les outils de compression `gzip`, `bzip2` et `xz` peuvent être utilisés par eux-mêmes ou avec `tar`.