---
title: "GBrowse/en"
slug: "gbrowse"
lang: "en"

source_wiki_title: "GBrowse/en"
source_hash: "e670c877d281b4487f4d6041a4767586"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:14:52.415507+00:00"

tags:
  []

keywords:
  - "MySQL data"
  - "GBrowse"
  - "bp_seqfeature_load.pl"
  - "sequence-region"
  - "SHARED account"
  - "genome"
  - "Config files"
  - "header_file"
  - "FASTA file"
  - "Cedar"
  - "job scheduler"
  - "Database connection"
  - "Input files"

questions:
  - "What is the process and security requirement for a research group to request access to GBrowse on the Cedar cluster?"
  - "How must users configure their directories and database connections for MySQL or Postgres when setting up GBrowse?"
  - "What are the specific file permission requirements and methods for handling input files, such as reading .bam files directly or uploading sequences via BioPerl?"
  - "How should the commands be executed to ensure they are not run on the head node?"
  - "Which specific account must be granted view access after uploading data to the database?"
  - "What application requires read access to the MySQL database in order to function properly?"
  - "What is the overall purpose of using the bp_seqfeature_load.pl command in this context?"
  - "What kind of data is stored in the example_genomic_sequence.fa FASTA file?"
  - "What specific information is required to be included in the header_file?"
  - "How should the commands be executed to ensure they are not run on the head node?"
  - "Which specific account must be granted view access after uploading data to the database?"
  - "What application requires read access to the MySQL database in order to function properly?"

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

The Cedar installation differs in some ways from the standard GBrowse setup described at the [official website](http://gmod.org/wiki/GBrowse), particularly with regard to authentication and authorization.

## Requesting Access to GBrowse

In order for GBrowse to be able to access your files and directories, our staff will create a shared account for each research group that requests access to GBrowse. While using GBrowse, any member of a research group can read GBrowse config files and input files belonging to any other member of that group. If you wish to use GBrowse, the Principal Investigator (PI) of your group must agree to this change from the usual file security practices. Have the PI write to our [technical support](technical-support.md) indicating that they want a GBrowse account to be created for the group, and that they understand the implications of a shared account.

You must also have a database account on Cedar. If you already have one, please give the name of the database in your email. If you do not already have a database account, please read [Database servers](database-servers.md) carefully and answer the questions given there for setting up a database.

## Setting Up GBrowse

### Config Files

Since GBrowse needs to be able to read config files of all users within a group, place your GBrowse config files in the following directory:

`/project/`GROUPID`/gbrowse/`USERNAME`/conf`

where `` `GROUPID` `` is your group ID and `` `USERNAME` `` is your user name. We will create a symbolic link from `` `${HOME}/gbrowse-config/` `` to this directory for your convenience. Files in this directory should be readable by all members of the group, so please do not change the group permission of files in this directory.

### Configuring the Database Connection

If you use MySQL, you need the following in your GBrowse config files:

```ini
[username_example_genome:database]
db_adaptor    =     Bio::DB::SeqFeature::Store
db_args       =    -adaptor DBI::mysql
-dsn DATABASE;mysql_read_default_file=/home/SHARED/.my.cnf
```

where `` `DATABASE` `` is the name of your database and `` `SHARED` `` is the shared account. The `.my.cnf` file is a text file that is created by our staff. It contains information required for the shared account to make a connection to MySQL.

If you decide to use Postgres, you need the following in your GBrowse config files:

```ini
[username_example_genome:database]
db_adaptor    = Bio::DB::SeqFeature::Store
db_args       =  -adaptor DBI::Pg
-dsn          =  dbi:Pg:dbname=DATABASE
```

where `` `DATABASE` `` is the name of your database.

## Using GBrowse

### Input Files

GBrowse is able to read .bam files directly. You do not need to upload them to the database in order to display them. If you want GBrowse to read these .bam files directly:

*   Files need to be copied to your `/project` directory and they should be readable by the group.
*   The directory that contains the .bam files must have the `setgid` and `group-execute` bits turned on; that is, the output of `` `ls -l` `` must show a small "s" in the group-execute field (not a large "S").
*   Make sure that the .bam file's group ownership is set to your group and not to your username. For example, `` `jsmith:jsmith` `` is wrong, `` `jsmith:def-kjones` `` is right.
*   Edit your config file to specify the path to the .bam file. Here is an example:

```ini
[example_bam:database]
db_adaptor        = Bio::DB::Sam
db_args           = -bam /project/GROUPID/USERNAME/gbrowse_bam_files/example_file.bam
search options    = default
```

### Uploading Files to the Database

This can be done using BioPerl. Here are commands that need to be run.

```bash
module load bioperl/1.7.1
bp_seqfeature_load.pl -c -d DATABASE:mysql_read_default_file=/home/USERNAME/.my.cnf \
   example_genomic_sequence.fa header_file
```

In this example `` `DATABASE` `` is the name of your database and `example_genomic_sequence.fa` is the [FASTA file](https://en.wikipedia.org/wiki/FASTA_format) containing the entire genome that you want to visualize with GBrowse. `header_file` contains details about the length of the chromosomes. Here is an example of a header file:

```
##sequence-region I 1 15072434
##sequence-region II 1 15279421
##sequence-region III 1 13783801
##sequence-region IV 1 17493829
##sequence-region V 1 20924180
##sequence-region X 1 17718942
##sequence-region MtDNA 1 13794
```

!!! warning
    We remind you that the above commands should be run via the [job scheduler](running-jobs.md). Do not run these on the head node!

Once you uploaded your data to your database, you need to grant view access to the `` `SHARED` `` account so that GBrowse is able to access your database for reading. Please see [How to share your MySQL data](database-servers.md#how-to-share-your-mysql-data).