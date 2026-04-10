---
title: "General directives for migration/fr"
slug: "general_directives_for_migration"
lang: "fr"

source_wiki_title: "General directives for migration/fr"
source_hash: "52866780b0ffe2a48aafbae98d72a018"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T06:57:08.562978+00:00"

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

Cette page traite des problèmes reliés au transfert de vos données entre nos équipements et ceux de nos partenaires régionaux.

Si vous avez besoin de conseils ou d'information supplémentaire, contactez le [soutien technique](technical-support.md).

## En préparation à la migration
Vérifiez si la migration de vos données doit être effectuée par vous-même ou par notre équipe technique. Pour toute question, contactez le [soutien technique](technical-support.md).

La migration des données se fait à l'aide de [Globus](globus.md); si vous ne connaissez pas encore ce service, informez-vous de son fonctionnement et assurez-vous qu'il est compatible avec votre système. Pour garantir l'intégrité de vos données, testez le fonctionnement des outils qui seront utilisés sur des données de test; ces outils sont, par exemple [tar](http://www.howtogeek.com/248780/how-to-compress-and-extract-files-using-the-tar-command-on-linux/), [gzip](https://www.gnu.org/software/gzip/manual/gzip.html) ou [zip](https://www.cyberciti.biz/faq/how-to-create-a-zip-file-in-unix/).

!!! note "Planification de la migration"
    Commencez le processus de migration le plus tôt possible. Le temps de migration peut être augmenté en raison de la quantité de données à migrer et de la charge de traitement exigée des ordinateurs ou du réseau. Le transfert de centaines de gigaoctets prendra plusieurs heures, mais prévoyez une journée complète en cas de difficulté. Le transfert de téraoctets nécessitera quelques jours.

### Élagage de vos fichiers
Peu d'entre nous avons adopté comme pratique l'inspection régulière de nos données pour en supprimer les éléments superflus. À l'occasion d'une opération majeure de migration, il importe de procéder au nettoyage de vos répertoires et de vos fichiers. Le temps de transfert est diminué d'autant et l'espace de stockage, denrée en grande demande, est ainsi mieux utilisé.
*   Si vous conservez le code source lorsque vous compilez vos applications, supprimez les fichiers intermédiaires.
    L'une ou l'autre des commandes `make clean`, `make realclean`, ou `rm *.o` pourrait être utile, selon votre fichier [makefile](make.md).
*   Si vous ignorez l'utilité de gros fichiers portant des noms comme `core.12345`, il s'agit probablement de [fichiers de vidange (core dumps)](https://en.wikipedia.org/wiki/Core_dump) qui peuvent être supprimés.

### Archivage et compression
La plupart des applications de transfert de données déplacent plus efficacement un seul gros fichier que plusieurs petits fichiers dont le total serait équivalent. Si vos répertoires ou arborescences de fichiers comprennent un grand nombre de petits fichiers, combinez-les pour archivage en utilisant [tar](archiving-and-compressing-files.md).

Dans certains cas, il peut être avantageux de compresser les gros fichiers; c'est le cas par exemple de fichiers texte, dont la taille est souvent considérablement réduite par l'opération de compression. Il n'y a cependant pas toujours un gain de temps significatif à compresser un fichier qui sera décompressé à son arrivée. Il faut considérer les points suivants : l'espace gagné par la compression du fichier, la durée du temps de compression et la disponibilité de la bande passante. Ces points sont discutés dans la section *Data Compression and transfer discussion* de [cette page web](https://bluewaters.ncsa.illinois.edu/data-transfer-doc) produite par le US National Center for Supercomputing Applications.

Si vous estimez que la compression est avantageuse, utilisez [tar](archiving-and-compressing-files.md) ou [gzip](https://www.gnu.org/software/gzip/manual/gzip.html).

### Élimination des doublons
Évitez de transférer vers un nouveau système plusieurs fichiers contenant des données identiques.

Certains fichiers possédant le même nom peuvent contenir des données différentes. Assurez-vous de donner des noms uniques à vos fichiers pour éviter que des données différentes soient écrasées.

## Processus de migration
Autant que possible, utilisez [Globus Online](globus.md) pour effectuer le transfert de vos données; c'est un outil efficace et convivial pour réaliser cette tâche. En cas d'interruption de réseau, Globus possède des fonctions de récupération automatique. Nous vous suggérons de sélectionner *conserver les dates de modification des fichiers source* dans les *Options de transfert et de minuterie*.
*   Vérifier l'intégrité des fichiers après le transfert

Il est d'autant plus important de compresser vos données et d'éviter les doublons si vous ne disposez pas de Globus. Si vous devez utiliser [scp](https://fr.wikipedia.org/wiki/Secure_copy), [sftp](https://fr.wikipedia.org/wiki/SSH_File_Transfer_Protocol), ou [rsync](https://fr.wikipedia.org/wiki/Rsync) :
*   Préparez des blocs de quelques centaines de gigaoctets que vous transférerez un bloc à la fois. S'il y a interruption, vous n'aurez qu'à reprendre l'opération de transfert sur le bloc affecté et les données transférées auparavant ne seront pas touchées. C'est ici qu'une liste de données à transférer s'avère utile.
*   Vérifiez régulièrement la progression du transfert. Une indication à surveiller est la taille des fichiers. S'il n'y a eu aucun changement depuis un certain temps, il est possible qu'il faille intervenir.
    S'il ne vous est pas possible de reprendre l'opération de transfert, contactez le [soutien technique](technical-support.md).

!!! note "Patience requise"
    Même en utilisant Globus, le transfert de données est une opération qui exige du temps. Il est impossible de déterminer exactement le temps de transfert, mais sachez que des centaines de gigaoctets prendront plusieurs heures et que des téraoctets prendront plusieurs jours.

## Après la migration
Si vous n'avez pas utilisé Globus ou si vous n'avez pas sélectionné l'option *vérifier l'intégrité des fichiers*, assurez-vous que les données transférées ne sont pas corrompues. Un moyen simple est de comparer la taille des fichiers de départ à la taille des fichiers à destination. Pour un examen plus poussé, utilisez [cksum](http://man7.org/linux/man-pages/man1/cksum.1.html) et [md5sum](http://man7.org/linux/man-pages/man1/md5sum.1.html) pour comparer les fichiers. Ceux dont la taille ou le *checksum* ne concordent pas devraient être transférés à nouveau.

## Soutien technique
*   Pour savoir comment utiliser les utilitaires d'archivage et de compression, utilisez la commande Linux `` `man <commande>` `` ou `` `<commande> --help` ``.
*   Contactez le [soutien technique](technical-support.md).