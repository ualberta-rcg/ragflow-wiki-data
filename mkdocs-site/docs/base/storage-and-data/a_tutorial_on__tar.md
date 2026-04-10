---
title: "A tutorial on 'tar'"
slug: "a_tutorial_on__tar"
lang: "base"

source_wiki_title: "A tutorial on 'tar'"
source_hash: "0f76f5d7c56b7cf9a03cdd4293c26129"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T01:38:28.999613+00:00"

tags:
  []

keywords:
  - "console"
  - "bzip2"
  - "results"
  - "multiple files"
  - "tar file"
  - "Res-02"
  - "-A option"
  - "compress"
  - "extract files"
  - "exclude files"
  - "command line utilities"
  - "files"
  - "xz"
  - "extract file"
  - "compressed archives"
  - "split"
  - "determine size"
  - "grep"
  - "search without unpacking"
  - "archiving"
  - "report.tar"
  - "disk usage"
  - "bzip"
  - "pipe"
  - "splitting files"
  - "retrieve original file"
  - "archive files"
  - "extract"
  - "combine archives"
  - "list contents"
  - "tar archive"
  - "append files"
  - "archive"
  - "log.15Feb16.4"
  - "command options"
  - "compression"
  - "archive file"
  - "tar command"
  - "Res-01"
  - "bunzip2"
  - "tar -cvf"
  - "compressing files"
  - "gz and bz2"
  - "extract compressed archive"
  - "symbolic links"
  - "chain of characters"
  - "*.dat"
  - "append archive"
  - "decompress"
  - "-r option"
  - "*.bz2 files"
  - "compressed archive file"
  - "destination directory"
  - "gunzip"
  - "add files"
  - "unpacking compressed files"
  - "log1.dat"
  - "tar options"
  - "compressed file"
  - "bz2 extension"
  - "grep commands"
  - "results.tar"
  - "-tvjf"
  - "--exclude"
  - "cat"
  - "directory"
  - "compressed archive"
  - "results.tar.gz"
  - "gzip"
  - "Split a file"
  - "directories"
  - "create a tar file"
  - "tar"
  - "extracting archives"
  - ".dat extension"
  - "results.tar.bz2"
  - "wildcards"
  - "new_results"

questions:
  - "How do you use the tar command to create and extract an archive file from a directory?"
  - "What are the primary differences in performance and resource usage between the xz and gzip compression methods?"
  - "What are the most common command-line options used with tar to manage, list, and compress archive files?"
  - "Which flags are used to either create a new archive or extract files from an existing one?"
  - "How can a user specify the archive file name and list its contents without extracting them?"
  - "What flags should be used to compress or decompress the archive using either xz or gzip formats?"
  - "How can you combine single-letter options in the `tar` command, and where can you find a complete list of supported options for your system?"
  - "What specific command syntax and flags are used to create a single archive file containing one or multiple directories?"
  - "How can wildcards be utilized with the `tar` command to archive files or directories that match a specific naming pattern?"
  - "How can you append a new file or directory to an existing tar archive using the command line?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: true
---

*Parent page: [Archiving and compressing files](archiving-and-compressing-files.md)*

### Using `tar` to archive files and directories

The primary archiving utility on Linux and Unix-like systems is the [tar](https://www.gnu.org/software/tar/manual/tar.html) command. It will bundle several files or directories and generate a single file called an *archive file* or *tar file*, or humourously a *tarball*. By convention, an archive file has `.tar` as the file name extension. When you archive a directory with `tar`, it will, by default, include all the files and sub-directories contained within it, and sub-sub-directories contained in those, and so on. So the command `tar --create --file project1.tar project1` will pack all the content of directory *project1* into the file *project1.tar*. The original directory will remain unchanged, so this may double the amount of disk space occupied!

You can extract files from an archive file using the same command with a different option: `tar --extract --file project1.tar`. If there is no directory with the original name, it will be created. If a directory of that name exists and contains files of the same names as in the archive file, they will be overwritten. Another option can be added to specify the destination directory where to extract the archive's content.

### Compressing and decompressing

The `tar` archiving utility can compress an archive file at the same time it creates it. There are a number of compression methods to choose from. We recommend either `xz` or `gzip`, which can be used as follows:

```bash
tar --create --xz --file project1.tar.xz project1
tar --extract --xz --file project1.tar.xz
tar --create --gzip --file project1.tar.gz project1
tar --extract --gzip --file project1.tar.gz
```

Typically, `--xz` produces a smaller compressed file (i.e., with a better compression ratio) but takes longer and uses more RAM while working [Quick Benchmark: Gzip vs Bzip2 vs LZMA vs XZ vs LZ4 vs LZO](http://catchchallenger.first-world.info/wiki/Quick_Benchmark:_Gzip_vs_Bzip2_vs_LZMA_vs_XZ_vs_LZ4_vs_LZO). `--gzip` does not typically compress as much, but may be used if you encounter difficulties due to insufficient memory or excessive run time during `tar --create`.

You can also run `tar --create` first without compression and then use the commands `xz` or `gzip` in a separate step, although there is seldom a reason to do so. Similarly, you can run `xz -d` or `gzip -d` to decompress an archive file before running `tar --extract`, but again this is seldom necessary.

Once a `tar` file is created, it is also possible to use `gzip` or `bzip2` to compress the archive and reduce its size. The compressing utilities are used as follows:

```bash
gzip project1.tar
bzip2 project1.tar
```

These commands will produce the files *project1.tar.gz* and *project1.tar.bz2*.

### Common options

Here are the most common options for this command. There are two synonymous forms for each, a single-letter form prefixed with a single dash, and a whole-word form prefixed with a double dash:

*   `-c` or `--create`: Create a new archive.
*   `-f` or `--file=`: Following is the archive file name.
*   `-x` or `--extract`: Extract files from archive.
*   `-t` or `--list`: List the content of an archive file.
*   `-J` or `--xz`: Compress or decompress with `xz`.
*   `-z` or `--gzip`: Compress or decompress with `gzip`.

Single-letter options can be combined with a single dash, so for example: `tar -cJf project1.tar.zx project1` is equivalent to `tar --create --xz --file=project1.tar.xz project1`.

There are many more options for `tar`, but these may depend on the version you are using. You can get a complete list of the options available on your system with `man tar` or `tar --help`. Note in particular that some older systems might not support `--xz` compression.

## Examples

To illustrate the use of archiving and compressing utilities, we use a working directory that contains the following sub-directories and files [`bin/`, `documents/`, `jobs/`, `new.log.dat`, `programs/`, `report/`, `results/`, `tests/`, `work/`]. Your working directory may look very different but the idea is the same and this directory is used as a working example.

### Archiving files and directories

#### Archiving a directory

Perhaps the most common use of tar is to create an archive of a single directory. Let us take, for example, a directory named *results* and create from it an archive file named **results.tar**. On your terminal type:

```bash
ls
bin/  documents/  jobs/  new.log.dat  programs/  report/  results/  tests/  work/
tar -cvf results.tar results
results/
results/log1.dat
results/Res-01/
results/Res-01/log.15Feb16.1
results/Res-01/log.15Feb16.4
results/Res-02/
results/Res-02/log.15Feb16.balance.b.4
```

Using `ls`, we can see the new tar file created:

```bash
ls
bin/  documents/  jobs/  new.log.dat  programs/  report/  results/  results.tar  tests/  work/
```

In this example, we have invoked the `tar` command with the options *c* (for create), *v* (for verbosity) and *f* (for file). As for the archive's name, we have used *results.tar*; this name could be something else but it is better to have a similar name to the directory to archive. It makes it easier to recognize your data later.

More than one directory or file can be placed in a tar file. For example, to place the directories *results*, *report* and *documents* into an archive file called *full_results.tar*, we can proceed as follows:

```bash
tar -cvf full_results.tar results report documents/
results/
results/log1.dat
results/Res-01/
results/Res-01/log.15Feb16.1
results/Res-01/log.15Feb16.4
results/Res-02/
results/Res-02/log.15Feb16.balance.b.4
report/
report/report-2016.pdf
report/report-a.pdf
documents/
documents/1504.pdf
documents/ff.doc
```

Since the *v* option was used, the files added to the archive are shown. Those details could be hidden if *v* was not used.

To check out the created archive, use `ls`:

```bash
ls
bin/  documents/  full_results.tar  jobs/  new.log.dat  programs/  report/  results/  results.tar  tests/  work/
```

#### Archiving files or directories that start with a particular letter

In our working directory, we have two directories that start with "r" (*report*, *results*). In this example, we put together the content of these directories into one single archive [*archive.tar*].

```bash
tar -cvf archive.tar r*
report/
report/report-2016.pdf
report/report-a.pdf
results/
results/log1.dat
results/Res-01/
results/Res-01/log.15Feb16.1
results/Res-01/log.15Feb16.4
results/Res-02/
results/Res-02/log.15Feb16.balance.b.4
```

!!! note
    Here, we have put together all the directories that start with *r*. Similar commands can be used for files or directories that have a chain of characters [for example: `*r*`, `*.dat`, ... etc.].

#### Adding (appending) files to the end of an archive

The **-r** option is used to add files to existing archives without having to create new ones or unpack the archive and run tar again to create the new archive. Here is a quick example: let us add the file **new.log.dat** to the archive **results.tar**

```bash
tar -rf results.tar new.log.dat
```

Here, the tar command added the file **new.log.dat** at the end of the archive **results.tar**.

To check out, use the previous options to list the files in the tar file:

```bash
tar -tvf results.tar
drwxrwxr-x name name        0 2016-11-20 11:02 results/
-rw-r--r-- name name    10905 2016-11-16 16:31 results/log1.dat
drwxrwxr-x name name        0 2016-11-16 19:36 results/Res-01/
-rw-r--r-- name name    11672 2016-11-16 15:10 results/Res-01/log.15Feb16.1
-rw-r--r-- name name    11682 2016-11-16 15:10 results/Res-01/log.15Feb16.4
drwxrwxr-x name name        0 2016-11-16 19:37 results/Res-02/
-rw-r--r-- name name    34117 2016-11-16 15:10 results/Res-02/log.15Feb16.balance.b.4
-rw-r--r-- name name    10905 2016-11-20 11:16 new.log.dat
```

!!! note
    Files cannot be added to compressed archives (**\*.gz** or **\*.bz2**). Files can only be added to plain tar archives. The **-r** option in the tar command is also used to append or add a directory or directories to an existing tar file. Let us add the directory **report** to the archive **results.tar** from our previous example:

```bash
tar -rf results.tar report/
```

Let us now check the resulting tar file:

```bash
tar -tvf results.tar
drwxrwxr-x name name        0 2016-11-20 11:02 results/
-rw-r--r-- name name    10905 2016-11-16 16:31 results/log1.dat
drwxrwxr-x name name        0 2016-11-16 19:36 results/Res-01/
-rw-r--r-- name name    11672 2016-11-16 15:10 results/Res-01/log.15Feb16.1
-rw-r--r-- name name    11682 2016-11-16 15:10 results/Res-01/log.15Feb16.4
drwxrwxr-x name name        0 2016-11-16 19:37 results/Res-02/
-rw-r--r-- name name    34117 2016-11-16 15:10 results/Res-02/log.15Feb16.balance.b.4
-rw-r--r-- name name    10905 2016-11-20 11:16 new.log.dat
drwxrwxr-x name name        0 2016-11-20 11:02 report/
-rw-r--r-- name name   924729 2015-11-20 04:14 report/report-2016.pdf
-rw-r--r-- name name   924729 2015-11-20 04:14 report/report-a.pdf
```

!!! note
    Again, the **-v** option is not necessary if you do not want to show the details of the files.

#### Combining two archive files into one

As we can add a file to an archive, it is possible to add an archive to another archive. This can be done by invoking the **-A** option. Let us add the archive **report.tar** (for the directory report) to the existing archive **results.tar**.

Check out the existing archive:

```bash
ls
bin/  documents/  jobs/  new.log.dat  programs/  report/  report.tar  results/  results.tar  tests/  work/
tar -tvf results.tar
drwxr-xr-x name name        0 2016-11-20 16:16 results/
-rw-r--r-- name name    10905 2016-11-20 16:16 results/log1.dat
drwxr-xr-x name name        0 2016-11-20 16:16 results/Res-01/
-rw-r--r-- name name    11682 2016-11-20 16:16 results/Res-01/log.15Feb16.4
drwxr-xr-x name name        0 2016-11-20 16:16 results/Res-02/
-rw-r--r-- name name    34117 2016-11-20 16:16 results/Res-02/log.15Feb16.balance.b.4
```

Now, we add the archive and check out the resulting new archive:

```bash
tar -A -f results.tar report.tar
tar -tvf results.tar
drwxr-xr-x name name        0 2016-11-20 16:16 results/
-rw-r--r-- name name    10905 2016-11-20 16:16 results/log1.dat
drwxr-xr-x name name        0 2016-11-20 16:16 results/Res-01/
-rw-r--r-- name name    11682 2016-11-20 16:16 results/Res-01/log.15Feb16.4
drwxr-xr-x name name        0 2016-11-20 16:16 results/Res-02/
-rw-r--r-- name name    34117 2016-11-20 16:16 results/Res-02/log.15Feb16.balance.b.4
drwxrwxr-x name name        0 2016-11-20 11:02 report/
-rw-r--r-- name name   924729 2015-11-20 04:14 report/report-2016.pdf
-rw-r--r-- name name   924729 2015-11-20 04:14 report/report-a.pdf
```

In the above example, we have used the command `tar` with `-A` (for append) (`tar -A -f results.tar report.tar`) to add the archive `report.tar` to the archive `results.tar` as you can see from the comparison of output of the command (`tar -tvf results.tar`) before and after the append operation.

!!! note
    The options `-A`, `--catenate`, `--concatenate` are equivalent (depending on the system you are using, some options may not be available). The previous command can also be used as follows:

```bash
tar -A -f full-results.tar report.tar
tar -A --file=full-results.tar report.tar
tar --list --file=full-results.tar
```

!!! note
    There are two possibilities to add an archive **archive_2.tar** to another **archive_1.tar**. The first one is to use **-r** as seen previously when adding a regular file to an existing archive. In this case, the added archive [**archive_2.tar**] is seen like a regular file added to an existing archive. The option **-tvf** will reveal that the added archive appears at the end of the archive as a file. A second possibility consists of using the **-A** option. In this case, the added archive does not appear as an archive. This command creates a new archive, as we have used the tar command for the original directories.

#### Excluding particular files

From our previous example, let us create the archive **results.tar** for the directory `results` but without the files that have `.dat` as an extension. This can be done by adding the option: `--exclude=*.dat`

```bash
ls
bin/  documents/  jobs/  new.log.dat  programs/  report/  results/  tests/  work/
ls results/
log1.dat  log5.dat  Res-01/  Res-02/
tar -cvf results.tar --exclude=*.dat results/
results/
results/Res-01/
results/Res-01/log.15Feb16.4
results/Res-02/
results/Res-02/log.15Feb16.balance.b.4
tar -tvf results.tar
drwxr-xr-x name name        0 2016-11-20 16:16 results/
drwxr-xr-x name name        0 2016-11-20 16:16 results/Res-01/
-rw-r--r-- name name    11682 2016-11-20 16:16 results/Res-01/log.15Feb16.4
drwxr-xr-x name name        0 2016-11-20 16:16 results/Res-02/
-rw-r--r-- name name    34117 2016-11-20 16:16 results/Res-02/log.15Feb16.balance.b.4
```

#### Preserving symbolic links

If you have symbolic links in your directory and you want to preserve them, add the option `-h` to the tar command:

```bash
tar -cvhf results.tar results/
```

### Compressing files and archives

#### Compress a file, files, a tar archive

Compressing and archiving are two different processes. Archiving, or creating a tar file, puts together several files or directories into a single file. Compressing is a process applied to a single file or archive in order to reduce its size. This is achieved using compressing utilities like: **gzip** or **bzip2**. In the following example, we compress the files: **new.log.dat** and **results.tar**.

*   Using `gzip`:

```bash
ls
bin/  documents/  jobs/  new.log.dat  new_results/  programs/  report/  results/  results.tar  tests/  work/
gzip new.log.dat
gzip results.tar
ls
bin/  documents/  jobs/  new.log.dat.gz  new_results/  programs/  report/  results/  results.tar.gz  tests/  work/
```

*   Using `bzip2`:

```bash
ls
bin/  documents/  jobs/  new.log.dat  new_results/  programs/  report/  results/  results.tar  tests/  work/
bzip2 new.log.dat
bzip2 results.tar
ls
bin/  documents/  jobs/  new.log.dat.bz2  new_results/  programs/  report/  results/  results.tar.bz2  tests/  work/
```

!!! note
    In order to compress while the archive is created, use the **z** or **j** option for **gzip** or **bzip2** respectively. The extension of the file name does not really matter; `.tar.gz` and `.tgz` are common extensions for files compressed with **gzip**; `.tar.bz2` and `.tbz` are commonly used extensions for **bzip2** compressed files.

```bash
ls
bin/  documents/  jobs/  new.log.dat  programs/  report/  results/  tests/  work/
tar -cvzf results.tar.gz results/
results/
results/log1.dat
results/Res-01/
results/Res-01/log.15Feb16.4
results/Res-02/
results/Res-02/log.15Feb16.balance.b.4
ls
bin/  documents/  jobs/  new.log.dat  programs/  report/  results/  results.tar.gz  tests/  work/
```

```bash
tar -cvjf results.tar.bz2 results/
results/
results/log1.dat
results/Res-01/
results/Res-01/log.15Feb16.4
results/Res-02/
results/Res-02/log.15Feb16.balance.b.4
ls
bin/  documents/  jobs/  new.log.dat  programs/  report/  results/  results.tar.bz2  results.tar.gz  tests/  work/
```

#### Adding files to a compressed archive (tar.gz/tar.bz2)

We have already mentioned that we cannot add files to compressed archives. To do so, we need to decompress the files using `gunzip` or `bunzip2`. Once the tar file is obtained, we add the files to this archive by invoking the `r` option. After that, we can compress again using `gzip` or `bzip2`.

### Unpacking compressed files and archives

#### Extracting the whole archive

To unpack or extract an archive, we use **-x** (for extract) option with **-f** (for file); **-v** (for verbosity) can also be added. Let us extract the whole archive **results.tar**. If we want to extract it in the same directory, we have to make sure that there is no directory with this name, otherwise the extracted data go to that directory. To avoid overwriting the data if the directory already exists, we redirect the extracted data to another directory by adding the option **-C** and making sure that the destination directory already exists or is created before unpacking the archive. For example, we create a directory `new_results` and extract the data from the archive **results.tar** to this directory.

```bash
tar -xvf results.tar -C new_results/
results/
results/log1.dat
results/Res-01/
results/Res-01/log.15Feb16.1
results/Res-01/log.15Feb16.4
results/Res-02/
results/Res-02/log.15Feb16.balance.b.4
new.log.dat
report/
report/report-2016.pdf
report/report-a.pdf
ls new_results/
new.log.dat  report/  results/
```

!!! note
    The option **v** displays only the file names as they were extracted from the archive. To see more details, this option should be invoked twice (use **-xvvf** instead of **-xvf**).

#### Decompressing gz and bz2 files

For files with `.gz` extension, we use `gunzip` as follows:

```bash
ls
bin/  documents/  jobs/  new.log.dat.gz  new_results/  programs/  report/  results/  results.tar.gz  tests/  work/
gunzip new.log.dat.gz
gunzip results.tar.gz
ls
bin/  documents/  jobs/  new.log.dat  new_results/  programs/  report/  results/  results.tar  tests/  work/
```

For files with `.bz2` extension, we use `bunzip2` as follows:

```bash
ls
bin/  documents/  jobs/  new.log.dat.bz2  new_results/  programs/  report/  results/  results.tar.bz2  tests/  work/
bunzip2 new.log.dat.bz2
bunzip2 results.tar.bz2
ls
bin/  documents/  jobs/  new.log.dat  new_results/  programs/  report/  results/  results.tar  tests/  work/
```

#### Extracting a compressed archive file into another directory

As in the case of a **tar** file, a **compressed tar** file can be extracted into another directory by using `"-C"` to indicate the destination directory and adding the `"z"` option for `*.gz` files, or `"j"` for `*.bz2` files. We can use the same example as previously: extract the archive `results.tar.gz` (or `results.tar.bz2`) into the directory `new_results`. This can be achieved in one or two steps:

**Extract the compressed archive file in one step:**

**With gz:**

```bash
tar -xvzf results.tar.gz -C new_results/
results/
results/log1.dat
results/Res-01/
results/Res-01/log.15Feb16.1
results/Res-01/log.15Feb16.4
results/Res-02/
results/Res-02/log.15Feb16.balance.b.4
tar -xzf results.tar.gz -C new_results/
ls new_results/
results/
```

With **bz2** extension:

```bash
ls
bin/  documents/  jobs/  new.log.dat  new_results/  programs/  report/  results/  results.tar.bz2  tests/  work/
tar -xvjf results.tar.bz2 -C new_results/
results/
results/log1.dat
results/Res-01/
results/Res-01/log.15Feb16.1
results/Res-01/log.15Feb16.4
results/Res-02/
results/Res-02/log.15Feb16.balance.b.4
ls new_results/
results/
```

!!! note "Important Considerations"
    - In the previous example, it is possible to start with the option `"-C"` (the destination directory); however, first make sure that the destination directory exists, since `"tar"` is not going to create it for you and will fail if it does not exist. The command is:

```bash
tar -C new_results/ -xzf results.tar.gz
```

Or:

```bash
tar -C new_results/ -xvjf results.tar.bz2
```

    - If the option `"-C"` (destination directory) was not invoked, the files will be extracted in the same directory.
    - The option `"v"` is used for verbosity. In this case, it displays the files and directories as they are extracted to the new directory.
    - If you want to display more details (like the date, permissions ...), add a second `"v"` option as follows: `tar -C new_results/ -xvvzf results.tar.gz` or `tar -C new_results/ -xvvjf results.tar.bz2`.

**Extract the compressed archive file in two steps:**

Here, we use the same command as previously but without **z** or **j** options. First, we use `gunzip` or `bunzip2` to decompress the file, then we use `tar -xvf` to un-tar the archive as follows:

Let's suppose we have the compressed file: `results.tar.bz2`

```bash
ls
bin/  documents/  jobs/  new.log.dat  new_results/  programs/  report/  results/  results.tar.bz2  tests/  work/
bunzip2 results.tar.bz2
tar -C ./new_results/ -xvvf results.tar
drwxrwxr-x name name        0 2016-11-20 11:02 results/
-rw-r--r-- name name    10905 2016-11-16 16:31 results/log1.dat
drwxrwxr-x name name        0 2016-11-20 15:16 results/Res-01/
-rw-r--r-- name name    11682 2016-11-16 15:10 results/Res-01/log.15Feb16.4
drwxrwxr-x name name        0 2016-11-16 19:37 results/Res-02/
-rw-r--r-- name name    34117 2016-11-16 15:10 results/Res-02/log.15Feb16.balance.b.4
ls new_results/results/
log1.dat  Res-01/  Res-02/
```

For the **\*.gz** files:

```bash
ls
bin/  documents/  jobs/  new.log.dat  new_results/  programs/  report/  results/  results.tar.gz  tests/  work/
gunzip results.tar.gz
tar -C ./new_results/ -xvvf results.tar
drwxrwxr-x name name        0 2016-11-20 11:02 results/
-rw-r--r-- name name    10905 2016-11-16 16:31 results/log1.dat
drwxrwxr-x name name        0 2016-11-20 15:16 results/Res-01/
-rw-r--r-- name name    11682 2016-11-16 15:10 results/Res-01/log.15Feb16.4
drwxrwxr-x name name        0 2016-11-16 19:37 results/Res-02/
-rw-r--r-- name name    34117 2016-11-16 15:10 results/Res-02/log.15Feb16.balance.b.4
ls new_results/results/
log1.dat  Res-01/  Res-02/
```

#### Extracting one file from an archive or a compressed archive

Let us consider again the same example as previously. First, we create the archive **results.tar** for the directory archive and list all the files in it. Then we will extract one file into the directory `new_results`:

```bash
ls
bin/  documents/  jobs/  new.log.dat  new_results/  programs/  report/  results/  results.tar  tests/  work/
tar -tvf results.tar
drwxrwxr-x name name        0 2016-11-20 11:02 results/
-rw-r--r-- name name    10905 2016-11-16 16:31 results/log1.dat
drwxrwxr-x name name        0 2016-11-20 15:16 results/Res-01/
-rw-r--r-- name name    11682 2016-11-16 15:10 results/Res-01/log.15Feb16.4
drwxrwxr-x name name        0 2016-11-16 19:37 results/Res-02/
-rw-r--r-- name name    34117 2016-11-16 15:10 results/Res-02/log.15Feb16.balance.b.4
ls new_results/
tar -C ./new_results/ --extract --file=results.tar results/Res-01/log.15Feb16.4
ls new_results/results/Res-01/log.15Feb16.4
new_results/results/Res-01/log.15Feb16.4
```

In this example, we have extracted the file **results/Res-01/log.15Feb16.4** from the archive without decompressing the whole archive by using the option `--extract`. The command creates the same directories as in the archive but in the destination directory.

!!! note "Important Considerations"
    - It is mandatory to use `-C` (destination directory) for this command, otherwise the command will extract the file to the same directory as the archive. If the target directory does not exist, the command will create it.
    - It works to extract a file or a directory, but you need to provide the correct path for the file or directory.
    - The same command can be used to extract multiple files by adding their full paths, as in the previous example.

```bash
tar -C ./new_results/ --extract --file=results.tar "results/Res-01/log.15Feb16.4" "file2" "file3"
```

The same command can also be used to extract a file from a compressed tar file. For **\*.gz** files:

```bash
tar -C ./new_results/ --extract -z --file=results.tar.gz results/Res-01/log.15Feb16.4
ls new_results/results/Res-01/log.15Feb16.4
new_results/results/Res-01/log.15Feb16.4
```

From **\*.bz2** files:

```bash
tar -C ./new_results/ --extract -j --file=results.tar.bz2 results/Res-01/log.15Feb16.4
ls new_results/results/Res-01/log.15Feb16.4
new_results/results/Res-01/log.15Feb16.4
```

#### Extract multiple files using wildcards

```bash
tar -C ./new_results/ -xvf results.tar --wildcards "results/*.dat"
ls new_results/results/
log1.dat
```

With the above command, we have extracted the files that are in the directory **results** and with the extension `.dat`.

!!! note
    The command is also valid by invoking **j** or **z** options for compressed archives, as we have seen previously. From our previous example, we can extract all the files that start with `log` for example.

```bash
tar -C ./new_results/ -xvf results.tar --wildcards "results/log*"
ls new_results/results/
log1.dat
```

### Contents of archive files

#### Listing the contents

What if you have a tar file and don't remember what is in it? In this case, you can just list its content without unpacking the file. This can be achieved using `tar -t`:

```bash
tar -tf results.tar
results/
results/log1.dat
results/Res-01/
results/Res-01/log.15Feb16.1
results/Res-01/log.15Feb16.4
results/Res-02/
results/Res-02/log.15Feb16.balance.b.4
```

In addition, the use of `-v` option will also give "metadata" about the files, like permissions, date of last change, owner, just like you would see with `ls -l` on unarchived files:

```bash
tar -tvf results.tar
drwxrwxr-x name name        0 2016-11-20 11:02 results/
-rw-r--r-- name name    10905 2016-11-16 16:31 results/log1.dat
drwxrwxr-x name name        0 2016-11-16 19:36 results/Res-01/
-rw-r--r-- name name    11672 2016-11-16 15:10 results/Res-01/log.15Feb16.1
-rw-r--r-- name name    11682 2016-11-16 15:10 results/Res-01/log.15Feb16.4
drwxrwxr-x name name        0 2016-11-16 19:37 results/Res-02/
-rw-r--r-- name name    34117 2016-11-16 15:10 results/Res-02/log.15Feb16.balance.b.4
```

If for any reason you are interested in the number of files within a given tar file, it is possible to combine one of the previous commands with a pipe (`|`) and `wc -l` (word count with `-l` option to count only the number of lines). This command counts the number of lines in the output from the command before the pipe symbol.

```bash
tar -tvf results.tar | wc -l
7
```

Or:

```bash
tar -tf results.tar | wc -l
7
```

From this example, we have a total of 9 entries in the tar file. This number includes all the files and sub-directories that are in the directory `results`, including this directory itself. Let us mention that the details of the files are not shown even if the `-v` option was used. This is due to the fact that the results of the first command are filtered through the command `wc -l` that displays only the number of lines but not their details.

The options in the previous commands can be invoked separately. For example:

*   The option `-tvf` is equivalent to `-t -v -f`
*   The option `-v` is equivalent to `--verbose`
*   The option `-t` is equivalent to `--list`
*   The option `--file=results.tar` is equivalent to `-f results.tar`

!!! note
    The option `-f` or `--file=` always comes before the name of the tar file.

#### Searching for a file in an archive file without unpacking it

We have seen previously how to list the files in the archive. It is also possible to list the files and look for a particular file by using the list commands combined with pipe and grep commands. For example, let us see if we can find the file: **log.15Feb16.4** (the path to this file is: **results/Res-01/log.15Feb16.4**).

```bash
tar -tf results.tar | grep -a log.15Feb16.4
results/Res-01/log.15Feb16.4
tar -tvf results.tar | grep -a log.15Feb16.4
-rw-r--r-- name name   11682 2016-11-16 15:10 results/Res-01/log.15Feb16.4
```

Now, we can try to see if we can find another file called for example **pbs_file** (for information, this file does not exist in our archive):

```bash
tar -tf results.tar | grep -a pbs_file

tar -tvf results.tar | grep -a pbs_file

```

As you can see, the output of the commands is empty, meaning that the file does not exist in the archive.

If you want to list all the files that start, for example, with `log` (or any other chain of characters) in the archive, type on your terminal:

```bash
tar -tf results.tar | grep -a log*
results/log1.dat
results/Res-01/log.15Feb16.1
results/Res-01/log.15Feb16.4
results/Res-02/log.15Feb16.balance.b.4
```

Or add the **-v** option for more details:

```bash
tar -tvf results.tar | grep -a log*
-rw-r--r-- name name    10905 2016-11-16 16:31 results/log1.dat
-rw-r--r-- name name    11672 2016-11-16 15:10 results/Res-01/log.15Feb16.1
-rw-r--r-- name name    11682 2016-11-16 15:10 results/Res-01/log.15Feb16.4
-rw-r--r-- name name    34117 2016-11-16 15:10 results/Res-02/log.15Feb16.balance.b.4
```

!!! note
    The command `more` can also be invoked after the pipe symbol to list the files in the archive or the compressed file.

#### Listing the contents of a compressed file (*.gz or .bz2)

As in the case of a tar file we have seen previously, it is possible to combine `"tar"` command with `"z"` option to list the content of an archive compressed with `"gzip"` without decompressing the file; or `"j"` option to list the content of an archive compressed with `"bzip2"` without decompressing the file. For `*.gz` files:

```bash
tar -tvzf results.tar.gz
drwxrwxr-x name name        0 2016-11-20 11:02 results/
-rw-r--r-- name name    10905 2016-11-16 16:31 results/log1.dat
drwxrwxr-x name name        0 2016-11-16 19:36 results/Res-01/
-rw-r--r-- name name    11672 2016-11-16 15:10 results/Res-01/log.15Feb16.1
-rw-r--r-- name name    11682 2016-11-16 15:10 results/Res-01/log.15Feb16.4
drwxrwxr-x name name        0 2016-11-16 19:37 results/Res-02/
-rw-r--r-- name name    34117 2016-11-16 15:10 results/Res-02/log.15Feb16.balance.b.4
-rw-r--r-- name name    10905 2016-11-20 11:16 new.log.dat
drwxrwxr-x name name        0 2016-11-20 11:02 report/
-rw-r--r-- name name   924729 2015-11-20 04:14 report/report-2016.pdf
-rw-r--r-- name name   924729 2015-11-20 04:14 report/report-a.pdf
```

For **\*.bz2** files:

```bash
tar -tvjf results.tar.bz2
drwxrwxr-x name name        0 2016-11-20 11:02 results/
-rw-r--r-- name name    10905 2016-11-16 16:31 results/log1.dat
drwxrwxr-x name name        0 2016-11-16 19:36 results/Res-01/
-rw-r--r-- name name    11672 2016-11-16 15:10 results/Res-01/log.15Feb16.1
-rw-r--r-- name name    11682 2016-11-16 15:10 results/Res-01/log.15Feb16.4
drwxrwxr-x name name        0 2016-11-16 19:37 results/Res-02/
-rw-r--r-- name name    34117 2016-11-16 15:10 results/Res-02/log.15Feb16.balance.b.4
```

!!! note "Important Considerations"
    - Again, in this example, the option `"v"` is used to display all the details, but is not required.
    - The two previous commands can also be combined with the pipe (`|`) and `"wc"`; or pipe (`|`) and `grep`; as we have seen previously.

## Other useful utilities

### Size of a file, directory or archive

From your terminal, you can use the command `du -sh [your_file ...]` to see the size:

```bash
du -sh results.tar work tests
112K results.tar
58K  work
48K  tests
```

### Splitting files

By knowing the size of your files or directories, you can decide how to split them into different archives if necessary to avoid handling huge files. Splitting also works for archive files. A large file or tar file can be divided into small parts using the following syntax:

`split -b <Size-in-MB><file or tar-file-name><prefix-name>`
`split -b 100MB results.tar small-res`

The option **b** is invoked to fix the size of the small parts; and **prefix-name** is the name for the small files. The above command will split the file **results.tar** into smaller files, and the size of each one of them is 100 MB in the current working directory. Small file names will start from: `small-resaa`, `small-resab`, `small-resac`, `small-resad`, .... etc.

To recover the original file, we use the `cat` command as follows:

```bash
cat small_res* > your_archive_name.tar
```

Using the `split` command, it is possible to divide large files into smaller parts by invoking `split` with the size you want (e.g., `-b size in MB`), then transfer all the small parts. Once all the small parts are transferred, use the `cat` command to recover your original file or archive. If you want to append numbers in place of alphabets, use the **-d** option with the `split` command.

## Reminder of common commands

*   The `pwd` (present working directory) command to see the current working path.
*   The `ls` (list) command to see the files and sub-directories.
*   The command `du -sh` (disk usage) to see the size of the files, directories, or sub-directories.

!!! warning "Important Note on Disk Space"
    Applying the commands `gzip` or `bzip2` to a given file [**your_file** or **your_archive.tar**] requires the use of some free space, as in the case of the `tar` command, to create the final compressed file: [**your_file.gz** or **your_file.bz2**] or [**your_archive.tar.gz** or **your_archive.tar.bz2**]. These commands will fail if there is no space left in the device or if you are out of quota. On the CC clusters, use the command `quota` or `quota -s` from your terminal to see in more human-readable information if you have enough space to write additional data.

*   Apply `tar` to one directory [**results**]:

```bash
tar -cvf results.tar results
```

*   Apply `tar` to multiple files or directories in order to put them all together into a final single archive file.

```bash
tar -cvf your_archive.tar dir1 dir2 dir3 dir4 dir5 file1 file2 file3 file4 file5
```

*   Apply `tar` to all files or directories that start with a given letter **r** [or have a given chain of characters]:

```bash
tar -cvf your_archive.tar r*
```

*   List the content of a tar file [**results.tar**] including the details:

```bash
tar -tvf results.tar
```

*   List the content of a tar file [**results.tar**] without details:

```bash
tar -tf results.tar
```

*   Count the number of entries in the tar file:

```bash
tar -tvf results.tar | wc -l
tar -tf results.tar | wc -l
```

*   Search for a given file [**file_name_you_search**] in a tar archive file [**your_archive.tar**] without un-tarring the archive:

```bash
tar -tf your_archive.tar | grep -a file_name_you_search
tar -tvf your_archive.tar | grep -a file_name_you_search
```

*   List only files ending, starting, or containing a certain pattern in their names; for example, files starting with `log`:

```bash
tar -tf your_archive.tar | grep -a log*
tar -tvf your_archive.tar | grep -a log*
```

*   Append a file or files, or add a new file [**new_file**] to the end of a tar file [**your_archive.tar**]:

```bash
tar -rf your_archive.tar new_file
```

!!! note
    Files cannot be added to compressed archives [**\*.gz** or **\*.bzip2**]. Files can only be added to plain tar archives [**\*.tar**].

*   Add a directory [**new_dir**] to an existing tar file [**your_archive.tar**]:

```bash
tar -rf your_archive.tar new_dir
```

*   Add one archive [**archive_02.tar**] to another [**archive_01.tar**] with concatenate (**-A** option):

```bash
tar -A -f archive_01.tar archive_02.tar
```

*   Extract the whole archive file [**your_archive.tar**]:

```bash
tar -xvf your_archive.tar
```

*   Extract the whole archive file [**your_archive.tar**] into a specified directory [**destination_dir**]:

```bash
tar -xvf your_archive.tar -C destination_dir
```

*   Compress a file [**file0**], or files [**file1 file2 file3 file4 file5**], or an archive file [**your_archive.tar**] using the `gzip` command:

```bash
gzip file0
gzip file1 file2 file3 file4 file5
gzip your_archive.tar
```

*   Compress a file [**file0**], or files [**file1 file2 file3 file4 file5**], or an archive file [**your_archive.tar**] using the `bzip2` command:

```bash
bzip2 file0
bzip2 file1 file2 file3 file4 file5
bzip2 your_archive.tar
```

*   Compress with **z** or **j** option for `gzip` or `bzip2` respectively:

```bash
tar -cvzf results.tar.gz results/
tar -cvjf results.tar.bz2 results/
tar -cvzf results.tgz results
tar -cvjf results.tbz results/
```

*   Exclude particular files (for example, files with **\*.o**) while creating a tar file:

```bash
tar -cvf your_archive.tar your_directory --exclude=*.o
```

*   Decompress **\*.gz** or **\*.bz2** compressed files:

For files with `.gz` extension, use `gunzip` as follows:

```bash
gunzip your_file.gz
gunzip your_archive.gz
```

For files with `.bz2` extension, use `bunzip2` as follows:

```bash
bunzip2 your_file.bz2
bunzip2 your_archive.tar.bz2
```

*   List the content of a compressed file [**\*.gz** or **\*.bz2**]:

```bash
tar -tvzf your_archive.tar.gz
tar -tvjf your_archive.tar.bz2
```

!!! note "Important Considerations"
    Again, in this example, the option **v** is used to display all details but is not required. The two previous commands can also be combined with the [pipe (`|`) and `wc`] or [pipe (`|`) and `grep`] as we have seen previously.

*   Extract a compressed archive file in another directory:

```bash
tar -xvzf your_archive.tar.gz -C destination_dir
tar -xvjf your_archive.tar.bz2 -C destination_dir
tar -C destination_dir -xvzf your_archive.tar.gz
tar -C destination_dir -xvjf your_archive.tar.bz2
```

*   Extract and retrieve data from a compressed archive file in two steps:

For the **\*.bz2** files:

```bash
bunzip2 your_archive.tar.bz2
tar -C destination_dir -xvf your_archive.tar
```

For the **\*.gz** files:

```bash
gunzip your_archive.tar.gz
tar -C destination_dir -xvf your_archive.tar
```

*   Extract one file from an archive or a compressed archive file in another directory:

```bash
tar -C ./destination_dir/ --extract --file=your_archive.tar path-to-your-file
tar -C ./destination_dir/ --extract --file=results.tar "file1" "file2" "file3"
```

!!! note
    The path to the file to extract should be indicated explicitly.

*   The previous command can also be used to extract a file from a compressed tar file:

From a **gz** file:

```bash
tar -C ./destination_dir/ --extract -z --file=your_archive.tar.gz path-to-your-file
```

From a **bz2** file:

```bash
tar -C ./destination_dir/ --extract -j --file=your_archive.tar.bz2 path-to-your-file
```

*   Extract multiple files using wildcards (for example, files with **\*.dat**):

```bash
tar -C ./destination_dir/ -xvf your_archive.tar --wildcards "path-to-files/*.dat"
```

*   To preserve symbolic links using the `tar` command, use the **h** option:

```bash
tar -cvhf your_archive.tar your_directory
```

*   Add files to compressed archives [**\*.tar.gz** or **\*.tar.bz2**]:

Files cannot be added directly to compressed archives. To do so, decompress the archive file, add files as shown previously, then compress again.

*   Determine the size of the files or directories:

```bash
du -sh your_file your_archive.tar dir1 dir2 dir3
```

*   Split a file or a tar file:

`split -b <Size-in-MB><tar-file-name>.<extension> prefix-name`

For example, use a 1000MB for each small file:

```bash
split -b 1000MB your_archive.tar small-res
```

To retrieve the original file:

```bash
cat small_res* > your_archive_name.tar