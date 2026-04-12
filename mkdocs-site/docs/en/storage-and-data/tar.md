---
title: "Tar/en"
slug: "tar"
lang: "en"

source_wiki_title: "Tar/en"
source_hash: "0c47972047c2367984986cbe46b4d0fc"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:48:41.541516+00:00"

tags:
  []

keywords:
  - "archive utilities"
  - "data migration"
  - "tar command"
  - "xz"
  - "compression"
  - "gzip"
  - "archive file"
  - "tar"
  - "disk usage"
  - "compress"
  - "single-letter options"
  - "data compression"

questions:
  - "What are the definitions and primary benefits of archiving and compressing data?"
  - "How do you use the tar command to create and extract archive files in Linux or Unix-like systems?"
  - "What are the differences between the xz and gzip compression methods when used with the tar command?"
  - "What terminal commands should be used to inspect the contents and sizes of files and directories before starting the archiving process?"
  - "How does the tar command differ from gzip and bzip2 in terms of preserving the original files and utilizing disk space?"
  - "What is the difference between tar and utilities like gzip or bzip2 regarding their ability to process multiple files or directories versus a single file?"
  - "What command-line option is used to list the contents of an archive file?"
  - "Which flags dictate whether the archive is compressed using xz or gzip?"
  - "How can multiple single-letter options be combined into a single command string?"
  - "What terminal commands should be used to inspect the contents and sizes of files and directories before starting the archiving process?"
  - "How does the tar command differ from gzip and bzip2 in terms of preserving the original files and utilizing disk space?"
  - "What is the difference between tar and utilities like gzip or bzip2 regarding their ability to process multiple files or directories versus a single file?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Archiving means creating one file that contains a number of smaller files within it. Archiving data can improve the efficiency of file storage and of file transfers. It is faster for the secure copy protocol ([scp](https://en.wikipedia.org/wiki/Secure_copy)), for example, to transfer one archive file of a reasonable size than thousands of small files of equal total size.

[Compressing](https://en.wikipedia.org/wiki/Data_compression) means encoding a file such that the same information is contained in fewer bytes of storage. The advantage for long-term data storage should be obvious. For data transfers, the time spent compressing the data can be balanced against the time saved moving fewer bytes as described in this discussion of [data compression and transfer](https://bluewaters.ncsa.illinois.edu/data-transfer-doc) from the US National Center for Supercomputing Applications.

## Use tar to archive files and directories
The primary archiving utility on all Linux and Unix-like systems is the [tar](https://www.gnu.org/software/tar/manual/tar.html) command. It will bundle a bunch of files or directories together and generate a single file, called an *archive file* or *tar-file*. By convention, an archive file has `.tar` as the file name extension.

When you archive a directory with `tar`, it will by default include all files and sub-directories contained in it, and sub-sub-directories contained in those, and so on. So

```bash
tar --create --file project1.tar project1
```

will pack all the contents of directory `project1/` into the file `project1.tar`.

!!! note
    The original directory will be unchanged, so this may double the amount of disk space occupied!

You can extract files from the archive using the same command with a different option:

```bash
tar --extract --file project1.tar
```

If there is no directory with the original name, it will be created. If a directory of that name exists and contains files of the same names as in the archive file, they will be overwritten.

## How to compress and uncompress tar files
`tar` can compress an archive file at the same time it creates it. There are a number of compression methods to choose from. We recommend either **`xz`** or **`gzip`**, which can be used like so:

```bash
tar --create --xz --file project1.tar.xz project1
tar --extract --xz --file project1.tar.xz
tar --create --gzip --file project1.tar.gz project1
tar --extract --gzip --file project1.tar.gz
```

Typically, `--xz` will produce a smaller compressed file (a "better compression ratio") but takes longer and uses more RAM while working [Quick Benchmark: Gzip vs Bzip2 vs LZMA vs XZ vs LZ4 vs LZO](http://catchchallenger.first-world.info/wiki/Quick_Benchmark:_Gzip_vs_Bzip2_vs_LZMA_vs_XZ_vs_LZ4_vs_LZO). `--gzip` does not typically compress as small, but may be used if you encounter difficulties due to insufficient memory or excessive run time during `tar --create`.

You can also run `tar --create` first without compression and then use the commands `xz` or `gzip` in a separate step, although there is rarely a reason to do so. Similarly, you can run `xz -d` or `gzip -d` to decompress an archive file before running `tar --extract`, but again there is rarely a reason to do so.

## Common tar options
These are the most common options for `tar` command. There are two synonymous forms for each, a single-letter form prefixed with a single dash, and a whole-word form prefixed with a double dash:

*   `-c` or `--create`: Create a new archive.
*   `-f` or `--file=`: Following is the archive file name.
*   `-x` or `--extract`: Extract files from archive.
*   `-t` or `--list`: List the contents of an archive file.
*   `-J` or `--xz`: Compress or uncompress with `xz`.
*   `-z` or `--gzip`: Compress or uncompress with `gzip`.

Single-letter options can be combined with a single dash, so for example

```bash
tar -cJf project1.tar.zx project1
```

is equivalent to

```bash
tar --create --xz --file=project1.tar.xz project1
```

There are many more options for `tar`, and may depend on the version you are using. You can get a complete list of the options available on your system with `man tar` or `tar --help`. Note in particular that some older systems might not support `--xz` compression.