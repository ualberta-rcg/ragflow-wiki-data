---
title: "Archiving and compressing files/fr"
tags:
  []

keywords:
  []
---

*Page enfant de: [Stockage et gestion de fichiers](storage_and_file_management-fr.md)*

[Archiver](https://fr.wikipedia.org/wiki/Archive_(informatique)) signifie créer un fichier qui contient plusieurs petits fichiers. Le fait de créer un fichier archive peut améliorer l'efficacité du stockage et vous aider à [respecter les quotas](storage_and_file_management-fr#quotas_et_politiques.md). L'archivage peut aussi rendre plus efficace le [transfert de fichiers](general-directives-for-migration-fr.md). Par exemple, le protocole [scp](https://fr.wikipedia.org/wiki/Secure_copy) (*secure copy protocol*) transfère plus rapidement un fichier archive de taille raisonnable que des milliers de petits fichiers totalisant la même taille.

[Compresser](https://fr.wikipedia.org/wiki/Compression_de_donn%C3%A9es) signifie modifier le code d'un fichier pour en réduire le nombre de bits. Les avantages sont évidents en ce qui concerne le stockage à long terme des données. Dans le cas du  [transfert de données](general-directives-for-migration-fr.md), il faut comparer le temps de compression au temps nécessaire pour déplacer une quantité moindre de bits; voyez [ce texte](https://bluewaters.ncsa.illinois.edu/data-transfer-doc) du National Center for Supercomputing Applications.

* Sous Linux, <tt>tar</tt> est un outil d'archivage et de compression bien connu; voyez le  [tutoriel <tt>tar</tt>](a-tutorial-on-'tar'-fr.md).
* Aussi pour l'archivage et la compression, <tt>dar</tt> offre certaines fonctions avantageuses; voyez le [tutoriel <tt>dar</tt>](dar-fr.md).  
* L'utilitaire <tt>zip</tt> est bien connu pour l'archivage et la compression dans l'environnement Windows, mais il est disponible avec les grappes de Calcul Canada.
* Les outils de compression <tt>gzip</tt>, <tt>bzip2</tt> et <tt>xz</tt> peuvent être utilisés par eux-mêmes ou avec <tt>tar</tt>.