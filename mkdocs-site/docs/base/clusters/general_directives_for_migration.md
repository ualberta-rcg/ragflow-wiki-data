---
title: "General directives for migration"
slug: "general_directives_for_migration"
lang: "base"

source_wiki_title: "General directives for migration"
source_hash: "ef57f929e83a2c38eb769247985d9b54"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:37:12.436310+00:00"

tags:
  []

keywords:
  - "Data compression"
  - "data migration"
  - "sftp"
  - "Data migration"
  - "technical support"
  - "scp"
  - "data transfer"
  - "File transfer"
  - "file integrity"
  - "rsync"
  - "file transfer"
  - "Archiving"
  - "file size"
  - "Globus"

questions:
  - "What essential preparatory steps and timeline considerations should be taken before starting a data migration?"
  - "How can users optimize their files through cleanup, archiving, and compression to make the transfer more efficient?"
  - "Which tools are recommended for executing the actual data transfer, and how should the process be managed if the primary tool is unsupported?"
  - "How can you monitor the progress of a data transfer and what should you do if it appears to have stopped?"
  - "What methods are recommended for verifying file integrity after a data migration is complete?"
  - "Where can you find additional help or documentation for using archiving and compression utilities?"
  - "What specific file transfer tools are mentioned as requiring a careful data migration strategy?"
  - "Why is it recommended to schedule data migration in blocks of a few hundred gigabytes at a time?"
  - "How does maintaining an organized list of files assist during the data transfer process?"
  - "How can you monitor the progress of a data transfer and what should you do if it appears to have stopped?"
  - "What methods are recommended for verifying file integrity after a data migration is complete?"
  - "Where can you find additional help or documentation for using archiving and compression utilities?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

This page explains issues related to transferring your data between our facilities and our regional partners.

If you are in any doubt about details of the following advice, contact our [technical support](../support/technical_support.md) for help.

## What to do before migrating?
Make sure you know whether you are responsible for your own data migration, or whether our staff will be migrating your data. If you are in any doubt, contact our [technical support](../support/technical_support.md).

If you haven't used [Globus](../getting-started/globus.md) before, read about it now and verify that it works on the system you are migrating from. Test any other tools you will use (like [tar](http://www.howtogeek.com/248780/how-to-compress-and-extract-files-using-the-tar-command-on-linux/), [gzip](https://www.gnu.org/software/gzip/manual/gzip.html), [zip](https://www.cyberciti.biz/faq/how-to-create-a-zip-file-in-unix/)) on test data to ensure you know how they work before using them on important data.

!!! warning "Plan your migration timeline"
    Do not wait until the last minute to start your migration. Depending on how much data you have and how much load there is on the machines and network, you may be surprised at how long it will take to finish a large transfer. Expect hundreds of gigabytes to take hours to transfer, but give yourself days in case there is a problem. Expect terabytes to take days.

### Clean up
It is a good practice to look at your files regularly and see what can be deleted, but unfortunately many of us do not have this habit. A major data migration is a good reminder to clean up your files and directories. Moving less data will take less time, and storage space even on new systems is in great demand and should not be wasted.

*   If you compile programs and keep source code, delete any intermediate files. One or more of `make clean`, `make realclean`, or `rm *.o` might be appropriate, depending on your [makefile](../programming/make.md).
*   If you find any large files named like `core.12345` and you don't know that they are, they are probably [core dumps](https://en.wikipedia.org/wiki/Core_dump) and can be deleted.

### Archive and compress
Most file transfer programs move one file of a reasonable size more efficiently than thousands of small files of equal total size. If you have directories or directory trees containing many small files, use [tar](../storage-and-data/archiving_and_compressing_files.md) to combine (archive) them.

Large files can benefit from compression in some cases, especially text files which can usually be compressed a great deal. Compressing a file **only** for the purpose of transferring it, and then decompressing it at the end of the transfer will not necessarily save time. It depends on how much the file can be compressed, how long it takes to compress it, and the transfer bandwidth. The calculation is described under *Data Compression and transfer discussion* in [this document](https://bluewaters.ncsa.illinois.edu/data-transfer-doc) from the US National Center for Supercomputing Applications.

If you decide compression is worthwhile, you can again use [tar](../storage-and-data/archiving_and_compressing_files.md) for this, or [gzip](https://www.gnu.org/software/gzip/manual/gzip.html).

### Avoid duplication
Try not to move the same data twice. If you are migrating from more than one existing system to one new system and you have data duplicated on the sources, choose one and only move the duplicate data from that one.

!!! warning "Avoid accidental overwrites"
    Beware of files with duplicate names, but which do not contain duplicate information. Ensure that you will not accidentally overwrite one file with another of the same name.

## What to do during the migration process
!!! tip "Use Globus for efficient transfers"
    If it is supported at your source site, use [Globus](../getting-started/globus.md) to set up your file transfer. It is the most user-friendly and efficient tool we know for this task. Globus is designed to recover from network interruptions automatically. We recommend you enable the setting to *preserve source file modification times* in the *Transfer & Timer Options*.

!!! note "Alternatives to Globus"
    If Globus is not supported at your source site, then compressing data and avoiding duplication is even more important. If you are using [scp](https://en.wikipedia.org/wiki/Secure_copy), [sftp](https://en.wikipedia.org/wiki/SSH_File_Transfer_Protocol), or [rsync](https://en.wikipedia.org/wiki/Rsync), then:

    *   Make a schedule to migrate your data in blocks of a few hundreds of GBs at a time. If the transfer stops for some reason, you will be able to try again starting from the incomplete file, but you will not have to re-transfer files that are already complete. An organized list of files will help here.
    *   Check regularly to see that the transfer process has not stopped. File size is a good indicator of progress. If no files have changed size for several minutes, then something may have gone wrong. If restarting the transfer does not work, contact our [technical support](../support/technical_support.md).

Be patient. Even with Globus, transferring large volumes of data can be time consuming. Specific transfer speeds will vary, but expect hundreds of gigabytes to take hours and terabytes to take days.

## What to do after migration
!!! tip "Verify data integrity after transfer"
    If you did not use Globus, or if you did but did not check *verify file integrity*, make sure that the data you have transferred are not corrupted. A crude way to do this is to compare file sizes at the source with file sizes at the destination. For greater assurance, you can use [cksum](http://man7.org/linux/man-pages/man1/cksum.1.html) or [md5sum](http://man7.org/linux/man-pages/man1/md5sum.1.html) at each end, and see if the results match. Any files with mismatching sizes or checksums should be transferred again.

## Where and how to get help
*   To know how to use different archiving and compression utilities, use a Linux command like `man <command>` or `<command> --help`.
*   Contact our [technical support](../support/technical_support.md)