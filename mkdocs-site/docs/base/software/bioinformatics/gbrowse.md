---
title: "GBrowse"
slug: "gbrowse"
lang: "base"

source_wiki_title: "GBrowse"
source_hash: "ac20e7b73104ab68613d4bc59a9c64a1"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:14:34.513636+00:00"

tags:
  []

keywords:
  - "Bio::DB::Sam"
  - "MySQL data"
  - "GBrowse"
  - "group ownership"
  - "db_adaptor"
  - "config files"
  - "shared account"
  - "database connection"
  - "BioPerl"
  - "FASTA file"
  - "Cedar"
  - "database upload"
  - ".bam file"
  - "config file"

questions:
  - "How does a research group request access to GBrowse on Cedar, and what are the security implications regarding file sharing?"
  - "What specific configurations are required in the GBrowse config files to successfully connect to either a MySQL or PostgreSQL database?"
  - "What file permissions, ownership, and directory settings must be applied in order for GBrowse to read .bam files directly?"
  - "What specific BioPerl command and file types are required to upload genomic sequences to the database?"
  - "What specific information must be included in the header file that accompanies the FASTA file?"
  - "What are the necessary procedures for executing the upload commands and configuring database access for GBrowse afterward?"
  - "How should the group ownership of the .bam file be correctly set?"
  - "What modification must be made to the configuration file to utilize the .bam file?"
  - "What is the correct format for specifying the database adaptor and arguments in the configuration file?"
  - "What specific BioPerl command and file types are required to upload genomic sequences to the database?"
  - "What specific information must be included in the header file that accompanies the FASTA file?"
  - "What are the necessary procedures for executing the upload commands and configuring database access for GBrowse afterward?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Introduction

GBrowse is a combination of database and interactive web pages for manipulating and displaying annotations on genomes. It requires a web interface to display. GBrowse is installed on [Cedar](cedar.md). The web address of the installation is https://gateway.cedar.computecanada.ca.

The Cedar installation differs in some ways from the standard GBrowse setup described at the official website: http://gmod.org/wiki/GBrowse, particularly with regard to authentication and authorization.

## Requesting access to GBrowse

!!! warning "Shared Account Implications"
    In order for GBrowse to be able to access your files and directories, our staff will create a shared account for each research group that requests access to GBrowse. While using GBrowse, any member of a research group can read GBrowse config files and input files belonging to any other member of that group. If you wish to use GBrowse, the Principal Investigator (PI) of your group must agree to this change from the usual file security practices. Have the PI write to our [technical support](technical-support.md) indicating that they want a GBrowse account to be created for the group, and that they understand the implications of a shared account.

You must also have a database account on Cedar. If you already have one, please give the name of the database in your email. If you do not already have a database account, please read [Database servers](database-servers.md) carefully and answer the questions given there for setting up a database.

## Setting up GBrowse

### Config files

Since GBrowse needs to be able to read config files of all users within a group, place your GBrowse config files in the following directory:

`/project/*GROUPID*/gbrowse/*USERNAME*/conf`

where `*GROUPID*` is your group id and `*USERNAME*` is your user name. We will create a symbolic link from `${HOME}/gbrowse-config/` to this directory for your convenience.

!!! warning "File Permissions"
    Files in this directory should be readable by all members of the group, so please do not change the group permission of files in this directory.

### Configuring the database connection

If you use MySQL, you need the following in your GBrowse config files:

```ini
[username_example_genome:database]
 db_adaptor    =     Bio::DB::SeqFeature::Store
 db_args       =    -adaptor DBI::mysql
 -dsn *DATABASE*;mysql_read_default_file=/home/*SHARED*/.my.cnf
```

where `*DATABASE*` is the name of your database and `*SHARED*` is the shared account. The `.my.cnf` file is a text file that is created by our staff. It contains information required for the shared account to make a connection to MySQL.

If you decide to use Postgres, you need the following in your GBrowse config files:

```ini
[username_example_genome:database]
 db_adaptor    = Bio::DB::SeqFeature::Store
 db_args       =  -adaptor DBI::Pg
 -dsn          =  dbi:Pg:dbname=*DATABASE*
```
where `*DATABASE*` is the name of your database.

## Using GBrowse

### Input files

GBrowse is able to read .bam files directly. You do not need to upload them to the database in order to display them. If you want GBrowse to read these .bam files directly:

*   Files need to be copied to your `/project` directory and they should be readable by the group.
*   The directory that contains the .bam files must have the `setgid` and `group-execute` bits turned on; that is, the output of `ls –l` must show a small "s" in the group-execute field (not a large "S").
*   Make sure that the .bam file's group ownership is set to your group and not to your username. For example, `jsmith:jsmith` is wrong, `jsmith:def-kjones` is right.
*   Edit your config file to specify the path to the .bam file. Here is an example:

```ini
[example_bam:database]
 db_adaptor        = Bio::DB::Sam
 db_args           = -bam /project/*GROUPID*/*USERNAME*/gbrowse_bam_files/example_file.bam
 search options    = default
```

### Uploading files to the database

This can be done using BioPerl. Here are commands that need to be run.

```bash
module load bioperl/1.7.1
bp_seqfeature_load.pl -c –d *DATABASE*:mysql_read_default_file=/home/*USERNAME*/.my.cnf \
    example_genomic_sequence.fa header_file
```

In this example `*DATABASE*` is the name of your database and `example_genomic_sequence.fa` is the [FASTA file](https://en.wikipedia.org/wiki/FASTA_format) containing the entire genome that you want to visualize with GBrowse. `header_file` contains details about the length of the chromosomes. Here is an example of a header file:

```text
##sequence-region I 1 15072434
##sequence-region II 1 15279421
##sequence-region III 1 13783801
##sequence-region IV 1 17493829
##sequence-region V 1 20924180
##sequence-region X 1 17718942
##sequence-region MtDNA 1 13794
```

!!! warning "Avoid Head Node"
    We remind you that the above commands should be run via the [job scheduler](running-jobs.md). Do not run these on the head node!

Once you uploaded your data to your database, you need to grant view access to the `*SHARED*` account so that GBrowse is able to access your database for reading. Please see [How to share your MySQL data](database-servers.md#how-to-share-your-mysql-data).