---
title: "Tar/en"
tags:
  []

keywords:
  []
---

[Archiving](https://en.wikipedia.org/wiki/Archive_file) means creating one file that contains a number of smaller files within it. Archiving data can improve the efficiency of file storage, and of file transfers. It is faster for the secure copy protocol ([scp](https://en.wikipedia.org/wiki/Secure_copy)), for example, to transfer one archive file of a reasonable size than thousands of small files of equal total size.

[Compressing](https://en.wikipedia.org/wiki/Data_compression) means encoding a file such that the same information is contained in fewer bytes of storage. The advantage for long-term data storage should be obvious. For data transfers, the time spent compressing the data can be balanced against the time saved moving fewer bytes as described in this discussion of [data compression and transfer](https://bluewaters.ncsa.illinois.edu/data-transfer-doc) from the US National Center for Supercomputing Applications.

### Use tar to archive files and directories 
The primary archiving utility on all Linux and Unix-like systems is the [tar](https://www.gnu.org/software/tar/manual/tar.html) command. It will bundle a bunch of files or directories together and generate a single file, called an *archive file* or *tar-file*. By convention an archive file has `.tar` as the file name extension. 
 
When you archive a directory with `tar`, it will by default include all files and sub-directories contained in it, and sub-sub-directories contained in those, and so on. So

```bash
tar --create --file project1.tar project1
```

will pack all the contents of directory `project1/` into the file `project1.tar`. The original directory will be unchanged, so this may double the amount of disk space occupied!

You can extract files from the archive using the same command with a different option:

```bash
tar --extract --file project1.tar
```

If there is no directory with the original name, it will be created. If a directory of that name exists and contains files of the same names as in the archive file, they will be overwritten.

### How to compress and uncompress tar files 
`tar` can compress an archive file at the same time it creates it. There are a number of compression methods to choose from. We recommend either **`xz`** or **`gzip`**, which can be used like so:

```bash
tar --extract --gzip --file project1.tar.gz
```

Typically, `--xz` will produce a smaller compressed file (a "better compression ratio") but takes longer and uses more RAM while working [`--gzip` does not typically compress as small, but may be used if you encounter difficulties due to insufficient memory or excessive run time during `tar --create`.

You can also run `tar --create` first without compression and then use the commands `xz` or `gzip` in a separate step, although there is rarely a reason to do so. Similarly you can run `xz -d` or `gzip -d` to decompress an archive file before running `tar --extract`, but again there is rarely a reason to do so. 

### Common tar options 
These are the most common options for tar command. There are two synonymous forms for each, a single-letter form prefixed with a single dash, and a whole-word form prefixed with a double dash:
* `-c` or `--create`: Create a new archive.
* `-f` or `--file=`: Following is the archive file name.
* `-x` or `--extract`: Extract files from archive.
* `-t` or `--list`: List the contents of an archive file.
* `-J` or `--xz`: Compress or uncompress with `xz`.
* `-z` or `--gzip`: Compress or uncompress with `gzip`.
Single-letter options can be combined with a single dash, so for example

```bash
tar -cJf project1.tar.zx project1
```

is equivalent to

```bash

```
project1.tar.xz project1}}

There are many more options for `tar`, and may depend on the version you are using. You can get a complete list of the options available on your system with `man tar` or `tar --help`. Note in particular that some older systems might not support `--xz` compression.

<!--- Maybe there should be a section of examples here, but not specifically about migration.
Migration-specific advice should move to "General directives for migration"

## Common and useful commands to use to prepare your archives: 
To illustrate the different commands and how to use archive utilities, we use a given directory that looks like a home directory or any other directory that contains files, sub-directories ... etc. Let us suppose that you have already cleaned and removed the data you do not need and your data is ready for migration. Before that, there is one more step which is to compress your data. In the following, you will find the most common use of archiving and compressing utilities with adequate options. As an example, we use one directory called here **Migration** (or whatever is the name of your directory) and see how we can apply the different archiving and compressing utilities. 
On your terminal, change the directory to **Migration** (or the directory you want to work with) then: 

* Use pwd {present work directory} to see the current working path.
* Use ls {list} command to see the files and the sub-directories in the current working path.
* Use du -sh {disk usage} to see the size of the files, directories and sub-directories. This information will help you to see how to prepare your archives and which files to put together or to compress separately.
As shown in this example:

<source lang="console">
[user_name@localhost](http://catchchallenger.first-world.info/wiki/Quick_Benchmark:_Gzip_vs_Bzip2_vs_LZMA_vs_XZ_vs_LZ4_vs_LZO].)$  pwd
/global/scratch/user_name/Migration
</source>

<source lang="console">
[user_name@localhost]$  ls
bin/  documents/  jobs/  new.log.dat  programs/  report/  results/  tests/  work/
</source>

<source lang="console">
[user_name@localhost]$  du -sh * 
3,0K bin
876K documents
136K jobs
12K  new.log.dat
68K  programs
1,8M report
120K results
48K  tests
46K  work
</source>

This example shows that we are currently working on the directory called **Migration** and it contains the following files and directories (**bin**, **documents**, **jobs**, **new.log.dat**, **programs**, **report**, **results**, **tests**, **work**). The size of each file or directory is given by the use of the command `du -sh`. We will explain later why it is important to use this command to determine the size of your files or directories before starting compression.

In this example, we have used few directories and small files. In your case, you may have more directories, more files and large files. But the idea is the same and it consists on creating your archives using the `tar`, `gzip`, `bzip2` from your terminal. You can recover them later by `tar` {with specific options}, `gunzip` and `bunzip2`. We will explain how these utilities work by giving the most common and used commands and options.

**Notes:**
* Before starting compression, make sure you are not running out of space or quota because the tar command uses the free space to create the archive. At the end, it is like you have added data with the same size as the file or the directory you are trying to tar. When using tar, the original file stays without any change unless you make changes later or remove it. 
* For gzip and bzip2, they also use some free space to create the final archive but in this case the new file you will get is **your_file.gz** if you use gzip or **your_file.bz2** if you use bzip2; if it is a tar file; you will get the new file **your_archive.tar.gz** or **your_archive.tar.bz2**
* The tar command can be applied to multiple files or directories in order to put them together into a final one file archive.
* The gzip and bzip2 are applied to a single file or a single archive file but not a directory.
--->