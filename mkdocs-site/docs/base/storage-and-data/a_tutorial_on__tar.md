---
title: "A tutorial on 'tar'"
slug: "a_tutorial_on__tar"
lang: "base"

source_wiki_title: "A tutorial on 'tar'"
source_hash: "0f76f5d7c56b7cf9a03cdd4293c26129"
last_synced: "2026-04-10T14:10:18.226633+00:00"
last_processed: "2026-04-10T14:27:48.153992+00:00"

tags:
  []

keywords:
  - "report.tar"
  - "bz2 extension"
  - "Res-02"
  - "destination directory"
  - "-A option"
  - "gz and bz2"
  - "gunzip"
  - "files"
  - "-r option"
  - "tar command"
  - "*.dat"
  - "extract"
  - "tar"
  - "command line utilities"
  - "results.tar.bz2"
  - "compressed file"
  - "results.tar.gz"
  - "create a tar file"
  - "*.bz2 files"
  - "results"
  - "splitting files"
  - "-tvjf"
  - "log.15Feb16.4"
  - "extracting archives"
  - "append files"
  - "retrieve original file"
  - "results.tar"
  - "decompress"
  - "compressed archive file"
  - "compressing files"
  - "disk usage"
  - "determine size"
  - "directory"
  - "grep commands"
  - "add files"
  - "split"
  - "archive files"
  - "compressed archive"
  - "cat"
  - "bunzip2"
  - "symbolic links"
  - "archive"
  - ".dat extension"
  - "--exclude"
  - "log1.dat"
  - "wildcards"
  - "tar options"
  - "compression"
  - "tar file"
  - "console"
  - "archiving"
  - "list contents"
  - "exclude files"
  - "Split a file"
  - "Res-01"
  - "xz"
  - "bzip"
  - "bzip2"
  - "compress"
  - "tar -cvf"
  - "unpacking compressed files"
  - "new_results"
  - "chain of characters"
  - "directories"
  - "archive file"
  - "extract file"
  - "extract compressed archive"
  - "command options"
  - "append archive"
  - "search without unpacking"
  - "tar archive"
  - "compressed archives"
  - "combine archives"
  - "pipe"
  - "multiple files"
  - "extract files"
  - "gzip"
  - "grep"

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
  - "What is the primary limitation regarding the type of tar archives that can be modified with the append command?"
  - "Which option should be used with the tar command to combine one existing archive file into another?"
  - "What is the purpose of the `tar -cvf archive.tar r*` command shown in the console example?"
  - "Which specific files and directories are included in the archive based on the provided output?"
  - "How can wildcards and character chains be utilized to archive specific groups of files or directories?"
  - "What command-line option is required to add an archive to another existing archive?"
  - "Which specific archives are being combined in the provided example?"
  - "What command is used to check the contents of the current directory to verify the presence of the archives?"
  - "How do you append the contents of one tar archive into another existing archive?"
  - "What is the functional difference between using the `-r` option and the `-A` option when adding an archive to another archive?"
  - "How can you use the `tar` command to create an archive of a directory while excluding files with a specific extension?"
  - "What is the purpose of the `tar` command executed in the provided console snippet?"
  - "How does the `--exclude=*.dat` flag affect the contents of the generated `results.tar` archive?"
  - "What subdirectories and files are present in the `results/` directory before the archive is created?"
  - "How can you preserve symbolic links when creating a directory archive using the tar command?"
  - "What is the difference between archiving and compressing, and which options can be used to compress an archive during its creation?"
  - "What steps must be taken to add new files to an already compressed archive like a .tar.gz or .tar.bz2 file?"
  - "Why must an archive be decompressed before new files can be added to it?"
  - "Which commands are used to decompress and subsequently recompress the archive?"
  - "What specific option is invoked to append files to the uncompressed tar archive?"
  - "How do you extract a standard `.tar` archive into a specific destination directory to prevent overwriting existing data?"
  - "What commands are used to decompress standalone files that have `.gz` and `.bz2` extensions?"
  - "Which specific options must be added to the `tar` command to extract `.tar.gz` and `.tar.bz2` compressed archives in a single step?"
  - "What is the purpose of the \"-C\" option when extracting an archive, and what prerequisite must be met before using it?"
  - "How do the \"-v\" and \"-vv\" options affect the output displayed during the file extraction process?"
  - "What are the specific commands required to extract a \".tar.gz\" or \".tar.bz2\" file using a two-step decompression and extraction method?"
  - "What command is used to extract a `.tar.gz` archive into a specific directory?"
  - "How does the extraction command change when dealing with a `.tar.bz2` file instead of a `.tar.gz` file?"
  - "What is the function of the `-C` flag used in the `tar` commands shown in the text?"
  - "What specific files and subdirectories are contained within the initial results directory shown in the output?"
  - "What are the file sizes and modification dates of the log files listed in the Res-01 and Res-02 subdirectories?"
  - "What command is the user attempting to execute at the end of the provided terminal snippet?"
  - "How do you extract a single file from a tar archive into a specific destination directory without decompressing the entire archive?"
  - "What specific command-line options must be added to extract a file from compressed archives such as .tar.gz or .tar.bz2?"
  - "How can the wildcards option be utilized to extract multiple files that share a specific naming pattern or extension?"
  - "How does the `--wildcards` option function when extracting specific files from a tar archive?"
  - "Which specific command options should be invoked to handle compressed archives?"
  - "Based on the provided console example, how do you direct the extracted files into a designated output directory?"
  - "How can you list the contents and view the metadata of a tar file without unpacking it?"
  - "What command combination allows you to count the total number of entries within a tar archive?"
  - "How can you search for a specific file inside a tar archive using the command line?"
  - "How can the tar, pipe, and grep commands be combined to search for a specific file within an archive?"
  - "What is the difference in the output generated by the `tar -tf` command compared to the `tar -tvf` command?"
  - "What is the exact name and directory path of the file being located in the provided example?"
  - "How can you use the command line to search for a specific file or a pattern of characters within an uncompressed tar archive?"
  - "What is the correct tar command option to list the contents of a gzip-compressed archive (*.gz) without extracting it?"
  - "How does the command differ when listing the contents of a bzip2-compressed archive (*.bz2) compared to a gzip-compressed one?"
  - "How can a user check the size of files, directories, or archives from the terminal?"
  - "What is the process for splitting a large file into smaller parts and later recovering the original file?"
  - "Why might compression commands like gzip or bzip2 fail, and how can a user verify they have enough disk space before running them?"
  - "What specific command and flags are used to view the contents of the .bz2 file?"
  - "What is the name of the main directory and the specific files contained within the compressed archive?"
  - "What type of metadata, such as file size and modification date, is displayed in the output of the command?"
  - "How do you use the `tar` command to create an archive from a single directory?"
  - "What is the syntax for combining multiple specific files and directories into a single tar archive?"
  - "How can you apply the `tar` command to archive files and directories based on a specific character pattern?"
  - "How can you list, count, or search for specific files within a tar archive without extracting its contents?"
  - "What is the process and limitation for appending new files, directories, or other archives to an existing tar file?"
  - "Which commands and options are used to extract tar archives to specific directories and apply gzip or bzip2 compression?"
  - "How do you decompress and extract entire `.gz` or `.bz2` archive files into a specific destination directory?"
  - "What is the process for extracting specific individual files or multiple files using wildcards from an existing tar archive?"
  - "How can a user list the contents of a compressed archive, preserve symbolic links when creating one, and determine the size of files or directories?"
  - "What is the difference between using the 'z' and 'j' options when creating a tar archive?"
  - "What are the common file extensions associated with gzip and bzip compressed tar files?"
  - "How can specific files or file types be excluded during the creation of a tar file?"
  - "What command syntax is used to archive a directory into a standard .tar file?"
  - "What are the necessary steps to add new files to an already compressed archive like .tar.gz or .tar.bz2?"
  - "Which command and flags should be used to determine the size of specific files or directories?"
  - "What command and syntax are used to split a file or tar archive into smaller parts?"
  - "How do you specify the exact file size and naming prefix for the newly created split files?"
  - "What is the process for recombining the smaller split files to retrieve the original archive?"
  - "What command and syntax are used to split a file or tar archive into smaller parts?"
  - "How do you specify the exact file size and naming prefix for the newly created split files?"
  - "What is the process for recombining the smaller split files to retrieve the original archive?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Parent page: [Archiving and compressing files](archiving-and-compressing-files.md)*

## Using `tar` to archive files and directories

The primary archiving utility on Linux and Unix-like systems is the [tar](https://www.gnu.org/software/tar/manual/tar.html) command. It will bundle several files or directories and generate a single file called an *archive file* or *tar file*, or humorously a *tarball*. By convention an archive file has `.tar` as the file name extension. When you archive a directory with `tar`, it will, by default, include all the files and sub-directories contained within it, and sub-sub-directories contained in those, and so on. So the command `tar --create --file project1.tar project1` will pack all the content of directory *project1* into the file *project1.tar*. The original directory will remain unchanged, so this may double the amount of disk space occupied!

You can extract files from an archive file using the same command with a different option: `tar --extract --file project1.tar`. If there is no directory with the original name, it will be created. If a directory of that name exists and contains files of the same names as in the archive file, they will be overwritten. Another option can be added to specify the destination directory where to extract the archive's content.

## Compressing and decompressing

The `tar` archiving utility can compress an archive file at the same time it creates it. There are a number of compression methods to choose from. We recommend either `xz` or `gzip`, which can be used as follows:

```bash
[user_name@localhost]$ tar --create --xz --file project1.tar.xz project1
[user_name@localhost]$ tar --extract --xz --file project1.tar.xz
[user_name@localhost]$ tar --create --gzip --file project1.tar.gz project1
[user_name@localhost]$ tar --extract --gzip --file project1.tar.gz
```

Typically, `--xz` produces a smaller compressed file (i.e. with a better compression ratio) but takes longer and uses more RAM while working [http://catchchallenger.first-world.info/wiki/Quick_Benchmark:_Gzip_vs_Bzip2_vs_LZMA_vs_XZ_vs_LZ4_vs_LZO](http://catchchallenger.first-world.info/wiki/Quick_Benchmark:_Gzip_vs_Bzip2_vs_LZMA_vs_XZ_vs_LZ4_vs_LZO). `--gzip` does not typically compress as much, but may be used if you encounter difficulties due to insufficient memory or excessive run time during `tar --create`.

You can also run `tar --create` first without compression and then use the commands `xz` or `gzip` in a separate step, although there is seldom a reason to do so. Similarly, you can run `xz -d` or `gzip -d` to decompress an archive file before running `tar --extract`, but again this is seldom necessary.

Once a `tar` file is created, it is also possible to use `gzip` or `bzip2` to compress the archive and reduce its size. The compressing utilities are used as follows:

```bash
[user_name@localhost]$ gzip project1.tar
[user_name@localhost]$ bzip2 project1.tar
```

These commands will produce the files *project1.tar.gz* and *project1.tar.bz2*.

## Common options

Here are the most common options for this command. There are two synonymous forms for each, a single-letter form prefixed with a single dash, and a whole-word form prefixed with a double dash:

*   `-c` or `--create`: Create a new archive.
*   `-f` or `--file=`: Following is the archive file name.
*   `-x` or `--extract`: Extract files from archive.
*   `-t` or `--list`: List the content of an archive file.
*   `-J` or `--xz`: Compress or decompress with `xz`.
*   `-z` or `--gzip`: Compress or decompress with `gzip`.

Single-letter options can be combined with a single dash, so for example:
`tar -cJf project1.tar.zx project1` is equivalent to `tar --create --xz --file=project1.tar.xz project1`.

There are many more options for `tar`, but these may depend on the version you are using. You can get a complete list of the options available on your system with `man tar` or `tar --help`. Note in particular that some older systems might not support `--xz` compression.

## Examples

To illustrate the use of archiving and compressing utilities, we use a working directory that contains the following sub-directories and files [*bin/ documents/ jobs/ new.log.dat programs/ report/ results/ tests/ work*]. Your working directory may look very different but the idea is the same and this directory is used as a working example.

### Archiving files and directories

#### Archiving a directory

Perhaps the most common use of tar is to create an archive of a single directory. Let us take, for example, a directory named *results* and create from it an archive file named **results.tar**. On your terminal type:

```bash
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat  programs/  report/  results/  tests/  work/
[user_name@localhost]$ tar -cvf results.tar results
results
results/log1.dat
results/Res-01/
results/Res-01/log.15Feb16.1
results/Res-01/log.15Feb16.4
results/Res-02/
results/Res-02/log.15Feb16.balance.b.4
```

Using `ls`, command we can see the new tar file created:

```bash
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat  programs/  report/  results/  results.tar  tests/  work/
```

In this example, we have invoked the `tar` command with the options `c` (for create), `v` (for verbosity) and `f` (for file). As for the archive's name, we have used *results.tar*; this name could be something else but it is better to have a similar name to the directory to archive. It makes it easier to recognize your data later.

More than one directory or files can be placed in a tar file. For example, to place the directories *results*, *report* and *documents* into an archive file called *full_results.tar*, we can proceed as follows:

```bash
[user_name@localhost]$ tar -cvf full_results.tar results report documents/
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

Since the `v` option was used, the files added to the archive are shown. Those details could be hidden if `v` was not used.

To check out the created archive, use `ls`:

```bash
[user_name@localhost]$ ls
bin/  documents/  full_results.tar  jobs/  new.log.dat  programs/  report/  results/  results.tar  tests/  work/
```

#### Archiving files or directories that start with a particular letter

In our working directory, we have two directories that start with "r" (report, results). In this example, we put together the content of these directories into one single archive [*archive.tar*].

```bash
[user_name@localhost]$ tar -cvf archive.tar r*
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
    Here, we have put together all the directories that start with *r*. Similar command can be used for files or directories that have a chain of characters [for example: `*r*`, `*.dat`, ... etc].

#### Adding (appending) files to the end of an archive

The **-r** option is used to add files to existing archives without having to create new ones or unpack the archive and run tar again to create the new archive. Here is a quick example: let us add the file **new.log.dat** to the archive **results.tar**

```bash
[user_name@localhost]$ tar -rf results.tar new.log.dat
```

Here, the tar command added the file **new.log.dat** at the end of the archive **results.tar**.

To check out use the previous options to list the files in the tar file:

```bash
[user_name@localhost]$ tar -tvf results.tar
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
    Files cannot be added to compressed archives (**\*.gz** or **\*.bz2**). Files can only be added to plain tar archives.The **-r** option in the tar command is also used to append or add a directory or directories to existing tar file. Let us add the directory **report** to the archive **results.tar** from our previous example:

```bash
[user_name@localhost]$ tar -rf results.tar report/
```

Let us now check the resulting tar file:

```bash
[user_name@localhost]$ tar -tvf results.tar
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

As we can add a file to archive it is possible to add an archive to another archive. This can be done by invoking the **-A** option. Let us add the archive **report.tar** (for the directory report) to the existing archive **results.tar**.

Check out the existing archive:

```bash
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat  programs/  report/  report.tar  results/  results.tar  tests/  work/
[user_name@localhost]$ ar -tvf results.tar
drwxr-xr-x name name        0 2016-11-20 16:16 results/
-rw-r--r-- name name    10905 2016-11-20 16:16 results/log1.dat
drwxr-xr-x name name        0 2016-11-20 16:16 results/Res-01/
-rw-r--r-- name name    11682 2016-11-20 16:16 results/Res-01/log.15Feb16.4
drwxr-xr-x name name        0 2016-11-20 16:16 results/Res-02/
-rw-r--r-- name name    34117 2016-11-20 16:16 results/Res-02/log.15Feb16.balance.b.4
```

Now, we add the archive and check out the resulting new archive:

```bash
[user_name@localhost]$ tar -A -f results.tar report.tar
[user_name@localhost]$ tar -tvf results.tar
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

In the above example, we have used the command tar with `-A` {for append} (`tar -A -f results.tar report.tar`) to add the archive report.tar to the archive results.tar as you can see from the comparison of output of the command (`tar -tvf results.tar`) before and after the append operation.

!!! note
    The options `-A`, `--catenate`, `--concatenate` are equivalent (depending on the system you are using, some options may not be available).The previous command can also be used as follows:

```bash
[user_name@localhost]$ tar -A -f full-results.tar report.tar
[user_name@localhost]$ tar -A --file=full-results.tar report.tar
[user_name@localhost]$ tar --list --file=full-results.tar
```

!!! note
    There are two possibilities to add an archive *archive_2.tar* to another *archive_1.tar*. The first one is to use `-r` as seen previously when add a regular file to an existing archive. In this case, the added archive [*archive_2.tar*] is seen like a regular file added to an existing archive. The option `-tvf` will reveal that the added archive appears at the end of the archive as a file. A second possibility consists on using the `-A` option. In this case, the added archive does not appear as an archive. This command create a new archive as we have used tar command to the original directories.

#### Excluding particular files

From our previous example, let us create the archive **results.tar** for the directory results but without the files that have `".dat"` as extension. This can be done by adding the option: `--exclude=*.dat`

```bash
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat  programs/  report/  results/  tests/  work/
[user_name@localhost]$ ls results/
log1.dat  log5.dat  Res-01/  Res-02/
[user_name@localhost]$ tar -cvf results.tar --exclude=*.dat results/
results/
results/Res-01/
results/Res-01/log.15Feb16.4|results/Res-02/
results/Res-02/log.15Feb16.balance.b.4
[user_name@localhost]$ tar -tvf results.tar
drwxr-xr-x name name        0 2016-11-20 16:16 results/
drwxr-xr-x name name        0 2016-11-20 16:16 results/Res-01/
-rw-r--r-- name name    11682 2016-11-20 16:16 results/Res-01/log.15Feb16.4
drwxr-xr-x name name        0 2016-11-20 16:16 results/Res-02/
-rw-r--r-- name name    34117 2016-11-20 16:16 results/Res-02/log.15Feb16.balance.b.4
```

#### Preserving symbolic links

If you have symbolic links in your directory and you want to preserve them, add the option `-h` to the tar command:

```bash
[user_name@localhost]$ tar -cvhf results.tar results/
```

### Compressing files and archives

#### Compress a file, files, a tar archive

Compressing and are archiving are two different processes. Archiving or creating a tar file put together several files or directories into a single file. Compressing is a process applied to a single file or archive in order to reduce its size. This is achieved using compressing utilities like: **gzip** or **bzip2**. In the following example, we compress the files: **new.log.dat** and **results.tar**.

*   Using gzip:

```bash
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat  new_results/  programs/  report/  results/  results.tar  tests/  work/
[user_name@localhost]$ gzip new.log.dat
[user_name@localhost]$ gzip results.tar
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat.gz  new_results/  programs/  report/  results/  results.tar.gz  tests/  work/
```

*   Using bzip2:

```bash
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat  new_results/  programs/  report/  results/  results.tar  tests/  work/
[user_name@localhost]$ bzip2 new.log.dat
[user_name@localhost]$ bzip2 results.tar
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat.bz2  new_results/  programs/  report/  results/  results.tar.bz2  tests/  work/
```

!!! note
    In order to compress while the archive is created, use the **z** or **j** option for **gzip** or **bzip2** respectively.The extension of the file name does not really matter [*results.tar.gz* and *results.tgz*] are common extensions for files compressed with **gzip**; [*results.tar.bz2* and *results.tbz*] are commonly used extensions for **bzip2** compressed files.

```bash
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat  programs/  report/  results/  tests/  work/
[user_name@localhost]$ tar -cvzf results.tar.gz results
results/
results/log1.dat
results/Res-01/
results/Res-01/log.15Feb16.4|results/Res-02/
results/Res-02/log.15Feb16.balance.b.4
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat  programs/  report/  results/  results.tar.gz  tests/  work/
```

```bash
[user_name@localhost]$ tar -cvjf results.tar.bz2 results/
results/
results/log1.dat
results/Res-01/
results/Res-01/log.15Feb16.4
results/Res-02/
results/Res-02/log.15Feb16.balance.b.4
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat  programs/  report/  results/  results.tar.bz2  results.tar.gz  tests/  work/
```

#### Adding files to a compressed archive (\*.gz/\*.bz2)

We have already mentioned that we cannot add files to compressed archives. To do so, we need to decompress the files using **gunzip** or **bunzip2**. Once the tar file is obtained, we add the files to this archive by invoking the **r** option. After that, we can compress again using **gzip** or **bzip2**.

### Unpacking compressed files and archives

#### Extracting the whole archive

To unpack or extract an archive, we use **-x** {for extract} option with **-f** {for file}; **-v** {for verbosity} can also be added. Let us extract the whole archive **results.tar**. If we want to extract it in the same directory, we have to make sure that there is no directory with this name otherwise the extracted data go to that directory. To avoid rewriting the data if the directory exists already, we redirect to extracted data to another directory by adding the option **-C** and making sure that the destination directory exists already or created before unpacking the archive. For example, we create a directory **moved_results** and extract the data from the archive **results.tar** to this directory.

```bash
[user_name@localhost]$ tar -xvf results.tar -C new_results/
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
[user_name@localhost]$ ls new_results/
new.log.dat  report/  results/
```

!!! note
    The option **v** displays only the file names as they were extracted from the archive. To see more details, this option should be invoked twice (use **-xvvf** instead of **-xvf**).

#### Decompressing gz and bz2 files

For files with `".gz"` extension, we use `gunzip` as follows:

```bash
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat.gz  new_results/  programs/  report/  results/  results.tar.gz  tests/  work/
[user_name@localhost]$ gunzip new.log.dat.gz
[user_name@localhost]$ gunzip results.tar.gz
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat  new_results/  programs/  report/  results/  results.tar  tests/  work/
```

For files with `".bz2"` extension, we use `bunzip2` as follows:

```bash
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat.bz2  new_results/  programs/  report/  results/  results.tar.bz2  tests/  work/
[user_name@localhost]$ bunzip2 new.log.dat.bz2
[user_name@localhost]$ bunzip2 results.tar.bz2
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat  new_results/  programs/  report/  results/  results.tar  tests/  work/
```

#### Extracting a compressed archive file into another directory

As in the case of a **tar** file, a **compressed tar** file can be extracted into another directory by using **-C** to indicate the destination directory and adding the **z** option `z` for **\*.gz** files; or **j** for **\*.bz2** files. We can use the same example as previously: extract the archive **results.tar.gz** (or **results.tar.bz2**) into the directory **new_results**. This can be achieved in one or two steps:

**Extract the compressed archive file on one step:**

**With gz:**

```bash
[user_name@localhost]$ tar -xvzf results.tar.gz -C new_results/
results/
results/log1.dat
results/Res-01/
results/Res-01/log.15Feb16.1
results/Res-01/log.15Feb16.4
results/Res-02/log.15Feb16.balance.b.4
[user_name@localhost]$ tar -xzf results.tar.gz -C new_results/
[user_name@localhost]$ ls new_results/
results/
```

With **bz2** extension:

```bash
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat  new_results/  programs/  report/  results/  results.tar.bz2  tests/  work/
[user_name@localhost]$ tar -xvjf results.tar.bz2 -C new_results/
results/
results/log1.dat
results/Res-01/
results/Res-01/log.15Feb16.1
results/Res-01/log.15Feb16.4
results/Res-02/|results/Res-02/log.15Feb16.balance.b.4
[user_name@localhost]$ ls new_results/
results/
```

!!! note
    *   In the previous example, it is possible to start with the option **-C** {the destination directory}, however first make sure that the destination directory exists, since **tar** is not going to create it for you and will fail if it does not exist. The command is:

```bash
[user_name@localhost]$ tar -C new_results/ -xzf results.tar.gz
```

Or:

```bash
[user_name@localhost]$ tar -C new_results/ -xvjf results.tar.bz2
```

!!! note
    *   If the option **-C** {destination directory} was not invoked, the files will be extracted in the same directory.
    *   The option **v** is used for verbosity. In this case, it displays the files and directories as they are extracted to the new directory.
    *   If you want to display more details (like the date, permission ...), add a second **v** option as follows: `tar -C new_results/ -xvvzf results.tar.gz` or `tar -C new_results/ -xvvjf results.tar.bz2`.
    *   **Extract the compressed archive file on two steps:**

Here, we use the same command as previously but without **z** or **j** options. First we use **gunzip** or **bunzip2** to decompress the file, then we use `tar -xvf` to un-tar the archive as follows:

Let suppose we have the compressed file: *results.tar.bz2*

```bash
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat  new_results/  programs/  report/  results/  results.tar.bz2  tests/  work/
[user_name@localhost]$ bunzip2 results.tar.bz2
[user_name@localhost]$ tar -C ./new_results/ -xvvf results.tar
drwxrwxr-x name name        0 2016-11-20 11:02 results/
-rw-r--r-- name name    10905 2016-11-16 16:31 results/log1.dat
drwxrwxr-x name name        0 2016-11-20 15:16 results/Res-01/
-rw-r--r-- name name    11682 2016-11-16 15:10 results/Res-01/log.15Feb16.4
drwxrwxr-x name name        0 2016-11-16 19:37 results/Res-02/
-rw-r--r-- name name    34117 2016-11-16 15:10 results/Res-02/log.15Feb16.balance.b.4
[user_name@localhost]$ ls new_results/results/
log1.dat  log5.dat  Res-01/   Res-02/
[user_name@localhost]$ ls new_results/results/
log1.dat  Res-01/  Res-02/
```

For the **\*.gz** files:

```bash
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat  new_results/  programs/  report/  results/  results.tar.gz  tests/  work/
[user_name@localhost]$ gunzip results.tar.gz
[user_name@localhost]$ tar -C ./new_results/ -xvvf results.tar
drwxrwxr-x name name        0 2016-11-20 11:02 results/
-rw-r--r-- name name    10905 2016-11-16 16:31 results/log1.dat
drwxrwxr-x name name        0 2016-11-20 15:16 results/Res-01/
-rw-r--r-- name name    11682 2016-11-16 15:10 results/Res-01/log.15Feb16.4
drwxrwxr-x name name        0 2016-11-16 19:37 results/Res-02/
-rw-r--r-- name name    34117 2016-11-16 15:10 results/Res-02/log.15Feb16.balance.b.4
[user_name@localhost]$ ls new_results/results/
log1.dat  Res-01/  Res-02/
```

#### Extracting one file from an archive or a compressed archive

Let us consider again the same example as previously. First we create the archive **results.tar** for the directory archive and list all the files in it. Then we will extract one file into the directory **new_results:**

```bash
[user_name@localhost]$ ls
bin/  documents/  jobs/  new.log.dat  new_results/  programs/  report/  results/  results.tar  tests/  work/
[user_name@localhost]$ tar -tvf results.tar
drwxrwxr-x name name        0 2016-11-20 11:02 results/
-rw-r--r-- name name    10905 2016-11-16 16:31 results/log1.dat
drwxrwxr-x name name        0 2016-11-20 15:16 results/Res-01/
-rw-r--r-- name name    11682 2016-11-16 15:10 results/Res-01/log.15Feb16.4
drwxrwxr-x name name        0 2016-11-16 19:37 results/Res-02/
-rw-r--r-- name name    34117 2016-11-16 15:10 results/Res-02/log.15Feb16.balance.b.4  [user_name@localhost]$ ls new_results/
[user_name@localhost]$ tar -C ./new_results/ --extract --file=results.tar results/Res-01/log.15Feb16.4
[user_name@localhost]$ ls new_results/results/Res-01/log.15Feb16.4
new_results/results/Res-01/log.15Feb16.4
```

In this example, we have extracted the file **results/Res-01/log.15Feb16.4** from the archive without decompressing the whole archive by using the option **--extract**. The command creates the same directories as in the archive but in the destination directory.

!!! note
    *   It is mandatory to use the `-C` {destination directory} for this command otherwise the command will extract the file to the same directory as the archive created for if it exists. If not, the command will create the same directory.
    *   It works to extract a file or a directory but we need to give the right path for the file or directory.
    *   The same command can be used to extract multiple files y adding the full path as in the previous example.

```bash
[user_name@localhost]$ tar -C ./new_results/ --extract --file=results.tar "results/Res-01/log.15Feb16.4" "file2" "file3"
```

The same command can also be used to extract a file from a compressed tar file.
From **gz** files:

```bash
[user_name@localhost]$ tar -C ./new_results/ --extract -z --file=results.tar.gz results/Res-01/log.15Feb16.4
[user_name@localhost]$ ls new_results/results/Res-01/log.15Feb16.4new_results/results/Res-01/log.15Feb16.4
```

From **bz2 file:**

```bash
[user_name@localhost]$ tar -C ./new_results/ --extract -j --file=results.tar.bz2 results/Res-01/log.15Feb16.4
[user_name@localhost]$ ls new_results/results/Res-01/log.15Feb16.4
new_results/results/Res-01/log.15Feb16.4
```

#### Extract multiple files using wildcards

```bash
[user_name@localhost]$ tar -C ./new_results/ -xvf results.tar --wildcards "results/*.dat"
[user_name@localhost]$ ls new_results/results/
log1.dat
```

With the above command, we have extracted the files that are in the directory **results** and with the extension `*.dat`.

!!! note
    The command is also valid with invoking **j** or **z** options for compressed archives as we have seen previously.From our previous example, we can extract all the files that start by **log** for example.

```bash
[user_name@localhost]$ tar -C ./new_results/ -xvf results.tar --wildcards "results/log*"
[user_name@localhost]$ ls new_results/results/
log1.dat
```

### Contents of archive files

#### Listing the contents

What if you have a tar file and don't remember what is in it? In this case, you can just list its content without unpacking the file. This can be achieved using `tar -t`:

```bash
[user_name@localhost]$ tar -tf results.tar
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
[user_name@localhost]$ tar -tvf results.tar
drwxrwxr-x name name        0 2016-11-20 11:02 results/
-rw-r--r-- name name    10905 2016-11-16 16:31 results/log1.dat
drwxrwxr-x name name        0 2016-11-16 19:36 results/Res-01/
-rw-r--r-- name name    11672 2016-11-16 15:10 results/Res-01/log.15Feb16.1
-rw-r--r-- name name    11682 2016-11-16 15:10 results/Res-01/log.15Feb16.4
drwxrwxr-x name name        0 2016-11-16 19:37 results/Res-02/
-rw-r--r-- name name    34117 2016-11-16 15:10 results/Res-02/log.15Feb16.balance.b.4
```

If for any reason you are interested in the number of files within a given tar file, it is possible to combine one of the previous commands with a pipe { `|` } and `wc -l` { word count with `-l` option to count only the number of lines}. This command counts the number of lines in the output from the command before the pipe symbol.

```bash
[user_name@localhost]$ tar -tvf results.tar | wc -l
7
```

Or:

```bash
[user_name@localhost]$ tar -tf results.tar | wc -l
7
```

From this example, we have a total of 9 entries in the tar file. This number includes all the files and sub-directories that are in the directory results including this directory itself. Let us mention that the details of the files are not shown even if the –v option was used. This is due to the fact that the results of the first command are filtered through the command `wc -l` that displays only the number of lines but not their details.

The options in the previous commands can be invoked separately. For example:

*   The option `-tvf` is equivalent to `-t -v -f`
*   The option `-v` is equivalent to `--verbose`
*   The option `-t` is equivalent to `--list`
*   The option `--file=results.tar` is equivalent to `-f results.tar`

!!! note
    The option `-f` or `--file=` comes always before the name of tar file.

#### Searching for a file in an archive file without unpacking it

We have seen previously how to list the files in the archive. It also possible to list the files and look at look for a particular file by using the list commands combined with pipe and grep commands. For example, let us see if we can find the file: **log.15Feb16.4** (the path to this file is: **results/Res-01/log.15Feb16.4**).

```bash
[user_name@localhost]$ tar -tf results.tar | grep -a log.15Feb16.4
results/Res-01/log.15Feb16.4
[user_name@localhost]$ tar -tvf results.tar | grep -a log.15Feb16.4
-rw-r--r-- name name   11682 2016-11-16 15:10 results/Res-01/log.15Feb16.4
```

Now, we can try see if we can find another file called for example **pbs_file** (for information, this file does not exist in our archive):

```bash
[user_name@localhost]$ tar -tf results.tar | grep -a pbs_file
[user_name@localhost]$ tar -tvf results.tar | grep -a pbs_file
```

As you can see, the output of the commands is empty meaning that the file does not exist in the archive.

If you want to list all the files that start for example by **log** (or any other chain of characters) in the archive, type on your terminal:

```bash
[user_name@localhost]$ tar -tf results.tar | grep -a log*
results/log1.dat
results/Res-01/log.15Feb16.1
results/Res-01/log.15Feb16.4
results/Res-02/log.15Feb16.balance.b.4
```

Or add the `-v` option for more details:

```bash
[user_name@localhost]$ tar -tvf results.tar | grep -a log*
-rw-r--r-- name name    10905 2016-11-16 16:31 results/log1.dat
-rw-r--r-- name name    11672 2016-11-16 15:10 results/Res-01/log.15Feb16.1
-rw-r--r-- name name    11682 2016-11-16 15:10 results/Res-01/log.15Feb16.4
-rw-r--r-- name name    34117 2016-11-16 15:10 results/Res-02/log.15Feb16.balance.b.4
```

!!! note
    The command more can also be invoked after the pipe symbol to list the files in the archive or the compressed file.

#### Listing the contents of a compressed file (\*.gz or .bz2)

As in the case of a tar file we have seen previously, it is possible to combine **tar** command with **z** option to list the content of an archive compressed with **gzip** without decompressing the file; or **j** option to list the content of an archive compressed with **bzip2** without decompressing the file.
For **\*.gz** files:

```bash
[user_name@localhost]$ tar -tvzf results.tar.gz
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
[user_name@localhost]$ tar -tvjf results.tar.bz2
drwxrwxr-x name name        0 2016-11-20 11:02 results/
-rw-r--r-- name name    10905 2016-11-16 16:31 results/log1.dat
drwxrwxr-x name name        0 2016-11-16 19:36 results/Res-01/
-rw-r--r-- name name    11672 2016-11-16 15:10 results/Res-01/log.15Feb16.1
-rw-r--r-- name name    11682 2016-11-16 15:10 results/Res-01/log.15Feb16.4
drwxrwxr-x name name        0 2016-11-16 19:37 results/Res-02/
-rw-r--r-- name name    34117 2016-11-16 15:10 results/Res-02/log.15Feb16.balance.b.4
```

!!! note
    *   Again, in this example the option **v** is used to display all the details, but not required.
    *   The two previous commands can be also combined with the **pipe { | }** and **wc**; or **pipe { | }** and grep; as we have seen previously.

## Other useful utilities

### Size of a file, directory or archive

From your terminal, you can use the command `du -sh [your_file ...]` to see the size:

```bash
[user_name@localhost]$ du -sh results.tar work tests
112K results.tar
58K  work
48K  tests
```

### Splitting files

By knowing the size of your files or directories, you can decide how to split them on different archives if necessary to do not have to handle huge files. The splitting works also for archive files. A big file or tar file can be divided into small parts using the following syntax:

`split -b <Size-in-MB><file or tar-file-name><prefix-name>`
`split -b 100MB results.tar small-res`

The option **b** is invoked to fix the size of the small parts; and **prefix-name** is the name for the small files. The above command will split the file **results.tar** into smaller files and the size of each one of them is 100 MB in current working directory and small file names will starts from: small-resaa small-resab small-resac small-resad .... etc.

To recover the original file, we use the `cat` command as follows:

```bash
[user_name@localhost]$ cat small_res* > your_archive_name.tar
```

Using split command, it is possible to divide large files into smaller parts by invoking split with the size you want {-b size in MB} then transfer all the small parts. Once all the small parts are transferred, use the cat command to recover your original file or your archive. In case if you want to append numbers in place of alphabets, use `-d` option in above split command.

## Reminder of common commands

*   The `pwd` {present work directory} command to see the current working path.
*   The `ls` {list} command to see the files and the sub-directories.
*   The command `du -sh` {disk usage} to see the size of the files, directories or sub-directories.

!!! important
    Applying the commands `gzip` or `bzip2` to a given file [**your_file** or **your_archive.tar**] requires the use of some free space, as in the case of `tar` command, to create the final compressed file: [**your_file.gz** or **your_file.bz2**] or [**your_archive.tar.gz** or **your_archive.tar.bz2**]. These commands will fail if there is no space left in the device or if you are out of quota. On the CC clusters, use the command `quota` or `quota -s` from your terminal to see in more human readable information if you have enough space to write additional data.

*   Apply `tar` to one directory [**results**]:

```bash
[user_name@localhost]$ tar -cvf results.tar results
```

*   Apply `tar` to multiple files or directories in order to put them all together into a final single archive file.

```bash
[user_name@localhost]$ tar -cvf your_archive.tar dir1 dir2 dir3 dir4 dir5 file1 file2 file3 file4 file5
```

*   Apply `tar` to all files or directories that start with a given a letter **r** [or have a given chain of characters]:

```bash
[user_name@localhost]$ tar -cvf your_archive.tar r*
```

*   List the content of a tar file [**results.tar**] including the details:

```bash
[user_name@localhost]$ tar -tvf results.tar
```

*   List the content of a tar file [**results.tar**] without details:

```bash
[user_name@localhost]$ tar -tf results.tar
```

*   Count the number of entries in the tar file:

```bash
[user_name@localhost]$ tar -tvf results.tar | wc -l
[user_name@localhost]$ tar -tf results.tar | wc -l
```

*   Search for a given file [**file_name_you_search**] in a tar archive file [**your_archive.tar**] without un-tarring the archive:

```bash
[user_name@localhost]$ tar -tf your_archive.tar | grep -a file_name_you_search
[user_name@localhost]$ tar -tvf your_archive.tar | grep -a file_name_you_search
```

*   List only file ending, or starting, or containing a certain pattern in their names: for examples files starting with **log**:

```bash
[user_name@localhost]$ tar -tf your_archive.tar | grep -a log*
[user_name@localhost]$ tar -tvf your_archive.tar | grep -a log*
```

*   Append a file or files or add a new file [**new_file**] to the end of a tar file [**your_archive.tar**]:

```bash
[user_name@localhost]$ tar -rf your_archive.tar new_file
```

!!! note
    Files cannot be added to compressed archives [**\*.gz** or **\*.bzip2**]. Files can only be added to plain tar archives [**\*.tar**].
*   Add a directory [**new_dir**] to an existing tar file [**your_archive.tar**]:

```bash
[user_name@localhost]$ tar -rf your_archive.tar new_dir
```

*   Add one archive [**archive_02.tar**] to another [**archive_01.tar**] with concatenate (**-A** option):

```bash
[user_name@localhost]$ tar -A -f archive_01.tar archive_02.tar
```

*   Extract the whole archive file [**your_archive.tar**]:

```bash
[user_name@localhost]$ tar -xvf your_archive.tar
```

*   Extract the whole archive file [**your_archive.tar**] into a specified directory [**destination_dir**]:

```bash
[user_name@localhost]$ tar -xvf your_archive.tar -C destination_dir
```

*   Compress a file [**file0**], or files [**file1 file2 file3 file4 file5**] or an archive file [**your_archive.tar**] using `gzip` command:

```bash
[user_name@localhost]$ gzip file0
[user_name@localhost]$ gzip file1 file2 file3 file4 file5
[user_name@localhost]$ gzip your_archive.tar
```

*   Compress a file [**file0**], or files [**file1 file2 file3 file4 file5**] or an archive file [**your_archive.tar**] using `bzip2` command:

```bash
[user_name@localhost]$ bzip2 file0
[user_name@localhost]$ bzip2 file1 file2 file3 file4 file5
[user_name@localhost]$ bzip2 your_archive.tar
```

*   Compress with **z** or **j** option for `gzip` or `bzip` respectively:

```bash
[user_name@localhost]$ tar -cvzf results.tar.gz results
[user_name@localhost]$ tar -cvjf results.tar.bz2 results/
[user_name@localhost]$ tar -cvzf results.tgz results
[user_name@localhost]$ tar -cvjf results.tbz results/
```

*   Exclude particular files [for example files with **\*.o**] while creating a tar file:

```bash
[user_name@localhost]$ tar -cvf your_archive.tar your_directory --exclude=*.o
```

*   Decompress **\*.gz** or **\*.bz2** compressed files:

For files with `*.gz` extension, use `gunzip` as follows:

```bash
[user_name@localhost]$ gunzip your_file.gz
[user_name@localhost]$ gunzip your_archive.gz
```

For files with `*.bz2` extension, use `bunzip2` as follows:

```bash
[user_name@localhost]$ bunzip2 your_file.bz2
[user_name@localhost]$ bunzip2 your_archive.tar.bz2
```

*   List the content of a compressed file [**\*.gz** or **\*.bz2**]:

```bash
[user_name@localhost]$ tar -tvzf your_archive.tar.gz
[user_name@localhost]$ tar -tvjf your_archive.tar.bz2
```

!!! note
    Again, in this example the option **v** is used to display all detail but not required. The two previous commands can be also combined with the [**pipe { | }** and **wc**] or [**pipe { | }** and **grep**] as we have seen previously.

*   Extract a compressed archive file in another directory:

```bash
[user_name@localhost]$ tar -xvzf your_archive.tar.gz -C destination_dir
[user_name@localhost]$ tar -xvjf your_archive.tar.bz2 -C destination_dir
[user_name@localhost]$ tar -C destination_dir -xvzf your_archive.tar.gz
[user_name@localhost]$ tar -C destination_dir -xvjf your_archive.tar.bz2
```

*   Extract and retrieve data from a compressed archive file on two steps:

For the **\*.bz2** files:

```bash
[user_name@localhost]$ bunzip2 your_archive.tar.bz2
[user_name@localhost]$ tar -C destination_dir -xvf your_archive.tar
```

For the **\*.gz** files:

```bash
[user_name@localhost]$ gunzip your_archive.tar.gz
[user_name@localhost]$ tar -C destination_dir -xvf your_archive.tar
```

*   Extract one file from an archive or a compressed archive file in another directory:

```bash
[user_name@localhost]$ tar -C ./destination_dir/ --extract --file=your_archive.tar path-to-your-file
[user_name@localhost]$ tar -C ./destination_dir/ --extract --file=results.tar "file1" "file2" "file3"
```

!!! note
    The path to the file to extract should be indicated explicitly.

*   The previous command can also be used to extract a file from a compressed tar file:

From a **gz** file:

```bash
[user_name@localhost]$ tar -C ./destination_dir/ --extract -z --file=your_archive.tar.gz path-to-your-file
```

From a **bz2** file:

```bash
[user_name@localhost]$ tar -C ./destination_dir/ --extract -j --file=your_archive.tar.bz2 path-to-your-file
```

*   Extract multiple files using wildcards [for example files with **\*.dat**]:

```bash
[user_name@localhost]$ tar -C ./destination_dir/ -xvf your_archive.tar --wildcards "path-to-files/*.dat"
```

*   To preserve symbolic links using tar command, use **h** option:

```bash
[user_name@localhost]$ tar -cvhf your_archive.tar your_directory
```

*   Add files to compressed archives [**\*.tar.gz** or **\*.tar.bz2**]:

Files can be added directly to compressed archives. To do so, decompress the archive file, add files as shown previously then compress again.

*   Determine the size of the files or directories:

```bash
[user_name@localhost]$ du -sh your_file your_archive.tar dir1 dir2 dir3
```

*   Split a file or a tar file:

```bash
[user_name@localhost]$ split -b <Size-in-MB><tar-file-name>.<extension> prefix-name
```

For example, use a 1000MB for each small file:

```bash
[user_name@localhost]$ split -b 1000MB your_archive.tar small-res
```

To retrieve the original file:

```bash
[user_name@localhost]$ cat small_res* > your_archive_name.tar