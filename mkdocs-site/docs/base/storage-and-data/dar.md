---
title: "Dar"
slug: "dar"
lang: "base"

source_wiki_title: "Dar"
source_hash: "28d4b422d77d9da249a3c234d39d9722"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:43:05.959405+00:00"

tags:
  []

keywords:
  - "-g flags"
  - "dar"
  - "dar utility"
  - "extended attributes"
  - "dar command"
  - "write your own scripts"
  - "archiving"
  - "archive"
  - "limit size"
  - "extracting"
  - "Disk ARchive"
  - "archive slices"
  - "backups"
  - "incremental backups"
  - "sharedSnippets"
  - "flag -s"
  - "extract an entire directory"
  - "External scripts"
  - "bash functions"
  - "Lustre filesystem"
  - "Unix wild masks"
  - "creating an archive"
  - "slice"

questions:
  - "What are the main advantages and features of the `dar` utility compared to the classical Unix `tar` tool?"
  - "Where can the `dar` utility be found and accessed within the described cluster environment?"
  - "What are the basic commands and flags used in `dar` to create an archive, list its contents, and extract specific files?"
  - "How can you prevent error messages when extracting an archive containing Lustre filesystem extended attributes to a non-Lustre location?"
  - "What is the correct process for creating and fully restoring incremental backups using the dar command?"
  - "How do you limit the maximum file size of individual archive slices when creating a backup?"
  - "What command is used to extract an entire directory with the dar utility?"
  - "How can a user specify multiple directories and files when using the dar command?"
  - "What limitation exists regarding the use of Unix wild masks after the -g flag?"
  - "What flag and unit format are used to limit the maximum size of each backup slice?"
  - "How are the resulting slice files named when a backup is split into multiple parts?"
  - "What name should be used in the command when extracting data from a multi-slice archive?"
  - "What is the purpose of the `dar -O -x monday` command shown in the example?"
  - "How do the mentioned bash functions assist users in working with the `dar` utility?"
  - "Where can users access the shared bash functions to use as inspiration for their own scripts?"
  - "What is the purpose of the `dar -O -x monday` command shown in the example?"
  - "How do the mentioned bash functions assist users in working with the `dar` utility?"
  - "Where can users access the shared bash functions to use as inspiration for their own scripts?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Parent page: [Storage and file management](storage_and_file_management.md)*

The [`dar`](http://dar.linux.free.fr) (stands for Disk ARchive) utility was written from the ground up as a modern replacement to the classical Unix `tar` tool. First released in 2002, `dar` is open source, is actively maintained, and can be compiled on any Unix-like system.

Similar to `tar`, `dar` supports full / differential / incremental backups. Unlike `tar`, each `dar` archive includes a file index for fast file access and restore — this is especially useful for large archives! `dar` has built-in compression on a file-by-file basis, making it more resilient against data corruption, and you can optionally tell it not to compress already highly compressed files such as `mp4` and `gz`. `dar` supports strong encryption, can split archives at 1-byte resolution, supports extended file attributes, sparse files, hard and symbolic (soft) links, can detect data corruption in both headers and saved data and recover with minimal data loss, and has many other desirable features. On the [`dar` page](http://dar.linux.free.fr) you can find a [detailed feature-by-feature `tar`-to-`dar` comparison](http://dar.linux.free.fr/doc/FAQ.html#tar).

## Where to find `dar`

On our clusters, `dar` is available on `/cvmfs`. With [StdEnv/2020](../programming/standard_software_environments.md):

```bash
[user_name@localhost]$ which dar
/cvmfs/soft.computecanada.ca/gentoo/2020/usr/bin/dar
[user_name@localhost]$ dar --version
dar version 2.5.11, Copyright (C) 2002-2052 Denis Corbin
...
```

## Using `dar` manually

### Basic archiving and extracting

Let's say, in the current directory you have a subdirectory `test`. To pack it into an archive, you can type in the current directory:

```bash
[user_name@localhost]$ dar -w -c all -g test
```

This will create an archive file `all.1.dar`, where `all` is the base name and `1` is the slice number. You can break a single archive into multiple slices (below). You can include multiple directories and files into an archive, e.g.

```bash
[user_name@localhost]$ dar -w -c all -g testDir1 -g testDir2 -g file1 -g file2
```

Please note that all paths should be relative to the current directory.

To list the archive's contents, use only the base name:

```bash
[user_name@localhost]$ dar -l all
```

To extract a single file into a subdirectory `restore`, use the base name and the file path:

```bash
[user_name@localhost]$ dar -R restore/ -O -w -x all -v -g test/filename
```

The flag `-O` will tell `dar` to ignore file ownership. Wrong ownership would be a problem if you are restoring someone else's files and you are not root. However, even if you are restoring your own files, `dar` will throw a message that you are doing this as non-root and will ask you to confirm. To disable this warning, use `-O`. The flag `-w` will disable a warning if `restore/test` already exists.

To extract an entire directory, type:

```bash
[user_name@localhost]$ dar -R restore/ -O -w -x all -v -g test
```

Similar to creating an archive, you can pass multiple directories and files by using multiple `-g` flags. Note that `dar` does not accept Unix wild masks after `-g`.

#### A note about the Lustre filesystem

!!! warning "Lustre Filesystem Extended Attributes"
    If the archived files are coming from a [Lustre filesystem](https://www.lustre.org/) (typically in `/home`, `/project` or `/scratch` on [our *general-purpose* compute clusters](../clusters/national_systems.md)), some *extended attributes* are saved automatically.
    To see which extended attributes are assigned to each archived file, use the `-alist-ea` flag:

    ```bash
    dar -l all -alist-ea
    ```

    You may see strings like: `Extended Attribute: [lustre.lov]`.
    With this attribute, any file extraction to a location formatted in Lustre will still work as usual. But if one tries to extract files to the [node local storage](using_node-local_storage.md) (also known as `$SLURM_TMPDIR`), the extraction will show error messages like: `Error while adding EA lustre.lov : Operation not supported`.

    To avoid these error messages, the `-u` flag can be used to exclude a specific type of attribute, while the "affected" files are still extracted. For example:

    ```bash
    dar -R restore/ -O -w -x all -v -g test -u 'lustre*'
    ```

    Another solution is to get rid of the `lustre.lov` attribute while creating the archive with the same `-u` flag:

    ```bash
    dar -w -c all -g test -u 'lustre*'
    ```

    In conclusion, this is necessary only if you intend to extract files to a location not formatted in Lustre.

### Incremental backups

You can create differential and incremental backups with `dar`, by passing the base name of the reference archive with `-A`. For example, let's say on Monday you create a full backup named `monday`:

```bash
[user_name@localhost]$ dar -w -c monday -g test
```

On Tuesday you modify some of the files and then include only these files into a new, incremental backup named `tuesday`, using the `monday` archive as a reference:

```bash
[user_name@localhost]$ dar -w -A monday -c tuesday -g test
```

On Wednesday you modify more files, and at the end of the day you create a new backup named `wednesday`, now using the `tuesday` archive as a reference:

```bash
[user_name@localhost]$ dar -w -A tuesday -c wednesday -g test
```

Now you have three files:

```bash
[user_name@localhost]$ ls *.dar
monday.1.dar     tuesday.1.dar    wednesday.1.dar
```

The file `wednesday.1.dar` contains only the files that you modified on Wednesday, but not the files from Monday or Tuesday. Therefore, the command

```bash
[user_name@localhost]$ dar -R restore -O -x wednesday
```

will only restore files that were modified on Wednesday. To restore everything, you have to go through all backups in the chronological order:

```bash
[user_name@localhost]$ dar -R restore -O -w -x monday      # restore the full backup
[user_name@localhost]$ dar -R restore -O -w -x tuesday     # restore the first incremental backup
[user_name@localhost]$ dar -R restore -O -w -x wednesday   # restore the second incremental backup
```

### Limiting the size of each slice

To limit the maximum size of each slice in bytes, use the flag `-s` followed by a number and one of k/M/G/T. For example, for a 1340 MB archive, the command

```bash
[user_name@localhost]$ dar -s 100M -w -c monday -g test
```

will create 14 slices named `monday.{1..14}.dar`. To extract from all of these, use their base name:

```bash
[user_name@localhost]$ dar -O -x monday
```

## External scripts

One of our team members has written bash functions that can facilitate the use of `dar`. You can use these functions as inspiration to write your own scripts. See [here](https://github.com/razoumov/sharedSnippets) for details.