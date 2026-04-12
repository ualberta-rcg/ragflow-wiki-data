---
title: "Archiving and compressing files/en"
slug: "archiving_and_compressing_files"
lang: "en"

source_wiki_title: "Archiving and compressing files/en"
source_hash: "83c0f9461d73858d093e8599fe81c8dd"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:29:59.198649+00:00"

tags:
  []

keywords:
  - "Data compression"
  - "File storage"
  - "tar"
  - "Archiving"
  - "Data transfers"

questions:
  - "What is file archiving and how does it improve storage efficiency and data transfer speeds?"
  - "What is the primary advantage of file compression, and what tradeoff must be considered when using it for data transfers?"
  - "Which specific software utilities are mentioned in the text for archiving and compressing files?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! note "Parent page"
    [Storage and file management](storage-and-file-management.md)

[Archiving](https://en.wikipedia.org/wiki/Archive_file) means creating one file that contains a number of smaller files within it. Reducing the number of files by creating an archive can improve the efficiency of file storage and help you stay within [quota limits](storage-and-file-management.md#filesystem-quotas-and-policies). Archiving can also improve the efficiency of [file transfers](general-directives-for-migration.md). It is faster for the secure copy protocol ([scp](https://en.wikipedia.org/wiki/Secure_copy)), for example, to transfer one archive file of a reasonable size than thousands of small files of equal total size.

[Compressing](https://en.wikipedia.org/wiki/Data_compression) means encoding a file such that the same information is contained in fewer bytes of storage. The advantage for long-term data storage should be obvious. For [data transfers](general-directives-for-migration.md), the time spent for compressing data must be balanced against the time saved moving fewer bytes as described in this discussion of [data compression and transfer](https://bluewaters.ncsa.illinois.edu/data-transfer-doc) from the US National Center for Supercomputing Applications.

*   The best-known tool for archiving files in the Linux community is `tar`. Here is [a tutorial on 'tar'](a-tutorial-on-tar.md).
*   A replacement for `tar` called `dar` offers some advantages in functionality. Here is [a tutorial on 'dar'](dar.md). Both `tar` and `dar` can compress files as well as archive.
*   The `zip` utility, more commonly used in the Windows community but available on our clusters, also provides both archiving and compression.
*   Compression tools `gzip`, `bzip2`, and `xz` can be used in conjunction with `tar`, or by themselves.