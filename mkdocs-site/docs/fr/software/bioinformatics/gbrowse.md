---
title: "GBrowse/fr"
tags:
  []

keywords:
  []
---

## Introduction 

GBrowse est un outil pour manipuler et visualiser des données génomiques par une interface web. Il est formé d’une base de données combinée à des pages web interactives. GBrowse est disponible sur [Cedar](cedar-fr.md) et peut être installé à partir de https://gateway.cedar.computecanada.ca.

Notre installation diffère de celle décrite sur la [page web GBrowse](http://gmod.org/wiki/GBrowse), particulièrement en ce qui a trait à l’autorisation et à l’authentification.

<span id="Requesting_access_to_GBrowse"></span>
## Accéder à GBrowse

Notre équipe technique créera un compte partagé pour chaque groupe de recherche demandant l’accès à GBrowse. Les données et les fichiers de configuration seront lisibles par tous les membres du groupe. Le chercheur principal ou la chercheuse principale doit écrire au [soutien technique](technical-support-fr.md) pour demander la création du compte partagé et attester qu’il ou elle comprend les conditions d’utilisation d'un compte partagé.

Il faut aussi indiquer le nom de la base de données utilisée sur Cedar. Si vous n’avez pas de compte de base de données, consultez la page [Serveurs de bases de données](database-servers-fr.md).

<span id="Setting_up_GBrowse"></span>
## Installation

<span id="Config_files"></span>
### Fichiers de configuration

Pour qu’ils soient visibles par tous les membres du groupe, placez les fichiers de configuration dans le répertoire

 /project/*GROUPID*/gbrowse/*USERNAME*/conf

où `*GROUPID*` est l’identifiant du groupe et `*USERNAME*` est votre nom d’utilisateur. Nous créerons un lien symbolique de `${HOME}/gbrowse-config/` vers ce répertoire. Veuillez vous assurer que les permissions de lecture du groupe pour ces fichiers sont activées.

<span id="Configuring_the_database_connection"></span>
### Connexion à la base de données

Avec MySQL, les fichiers de configuration GBrowse doivent contenir

 [username_example_genome:database]
 db_adaptor    =     Bio::DB::SeqFeature::Store
 db_args       =    -adaptor DBI::mysql
 -dsn *DATABASE*;mysql_read_default_file=/home/*SHARED*/.my.cnf

où `*DATABASE*` est le nom de la base de données et `*SHARED*` est le compte partagé. Le fichier texte `.my.cnf` est créé par notre équipe technique et contient les renseignements nécessaires pour se connecter à MySQL. 

Avec Postgres, les fichiers de configuration GBrowse doivent contenir

 [username_example_genome:database]
 db_adaptor    = Bio::DB::SeqFeature::Store
 db_args       =  -adaptor DBI::Pg
 -dsn          =  dbi:Pg:dbname=*DATABASE*
                     
où `*DATABASE*` est le nom de la base de données.

<span id="Using_GBrowse"></span>
## Utilisation

<span id="Input_files"></span>
### Fichiers de données

Il n’est pas nécessaire de téléverser les fichiers .bam pour pouvoir les visualiser. Pour que GBrowse puisse lire directement les fichiers .bam%nbsp;:
* les fichiers doivent être copiés dans votre répertoire `/project`  et être lisibles par le groupe;
* le répertoire qui contient les fichiers .bam doit avoir le <tt>setgid</tt> et la permission <tt>group-execute</tt> d'exécution par le groupe activés, c’est-à-dire que le résultat de `ls –l`  doit avoir un s minuscule (bas de casse) en lieu et place du x de l'exécution de groupe;
* la propriété de groupe du fichier .bam  doit indiquer le nom du groupe et non le nom de l’utilisateur, par exemple `jsmith:def-kjones`  plutôt que j`jsmith:jsmith`;
*  le chemin vers le fichier .bam doit être modifié dans le fichier de configuration, par exemple

 [example_bam:database]
 db_adaptor        = Bio::DB::Sam
 db_args           = -bam /project/*GROUPID*/*USERNAME*/gbrowse_bam_files/example_file.bam
 search options    = default

<span id="Uploading_files_to_the_database"></span>
### Téléverser des fichiers vers la base de données

Avec BioPerl, exécutez 

 module load bioperl/1.7.1
 bp_seqfeature_load.pl -c –d *DATABASE*:mysql_read_default_file=/home/*USERNAME*/.my.cnf \
    example_genomic_sequence.fa header_file

où `*DATABASE*` est le nom de la base de données, `example_genomic_sequence.fa` est le [fichier FASTA](https://fr.wikipedia.org/wiki/FASTA_(format_de_fichier)) qui contient le génome complet et `header_file` contient les détails sur la longueur des chromosomes. 
Voici un exemple d’un fichier d'en-tête :

<pre>
##sequence-region I 1 15072434
##sequence-region II 1 15279421
##sequence-region III 1 13783801
##sequence-region IV 1 17493829
##sequence-region V 1 20924180
##sequence-region X 1 17718942
##sequence-region MtDNA 1 13794
</pre>

N’exécutez pas ce fichier sur un nœud principal, mais exécutez ces commandes en passant par [l’ordonnanceur](running-jobs-fr.md).

Une fois que les données sont téléversées dans la base de données, vous devez accorder l'accès en lecture au compte partagé (`*SHARED*` ) pour que GBrowse puisse lire la base de données; voyez [Partager vos données MySQL](database-servers-fr#partager_vos_données_mysql.md).