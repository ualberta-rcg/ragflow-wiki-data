---
title: "Linux introduction"
slug: "linux_introduction"
lang: "base"

source_wiki_title: "Linux introduction"
source_hash: "f9738b6ecceb4ba26b1d1262806e75b6"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:31:02.397460+00:00"

tags:
  []

keywords:
  - "search within a file"
  - "grep command"
  - "permissions"
  - "read write execute"
  - "navigate document"
  - "Linux"
  - "diff command"
  - "search text"
  - "file permissions"
  - "chmod command"
  - "compare files"
  - "UNIX systems"
  - "console"
  - "write"
  - "owner group others"
  - "filesystem"
  - "UNIX environments"
  - "execute"
  - "UNIX commands"
  - "read"
  - "less command"
  - "regular expressions"
  - "wildcard"
  - "ls -la"

questions:
  - "How do users connect to the compute servers and access built-in help for UNIX commands?"
  - "What are the essential UNIX commands for navigating the filesystem and managing files or directories?"
  - "How do read, write, and execute permissions differ in their application to files versus directories?"
  - "How do you view and interpret the 10-character permission string for files and directories?"
  - "How does the `chmod` command work to add or remove specific permissions for owners, groups, and other users?"
  - "What commands are used to view a file in read-only mode and to compare the contents of two different files?"
  - "What are the three types of permissions supported by UNIX systems?"
  - "How do read, write, and execute permissions function when applied to a file?"
  - "What specific actions do the different permissions allow a user to perform on a directory?"
  - "How do you navigate and exit a document when using the `less` command?"
  - "What is the specific input required to search for text within a file while using `less`?"
  - "Which command and option should be used to compare two files side by side?"
  - "How can the grep command be used to search for a specific expression across single or multiple files?"
  - "What is the difference between the * and ? wildcards when specifying file names in Linux?"
  - "How do you use regular expressions with grep to search for variable text patterns, such as a specific range of numbers?"
  - "How can the grep command be used to search for a specific expression across single or multiple files?"
  - "What is the difference between the * and ? wildcards when specifying file names in Linux?"
  - "How do you use regular expressions with grep to search for variable text patterns, such as a specific range of numbers?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

This article is aimed at Windows and Mac users who do not have or have very little experience in UNIX environments. It should give you the necessary basics to access the compute servers and being quickly able to use them.

Connections to the servers use the [SSH](ssh.md) protocol, in text mode. You do not use a graphical interface (GUI) but a **console**.

!!! note
    Windows executables do not run on our servers without using an emulator.

!!! tip
    There is a self-paced course available on this topic from SHARCNET: [Introduction to the Shell](https://training.sharcnet.ca/courses/enrol/index.php?id=182)

## Obtaining help

Generally, UNIX commands are documented in the reference manuals that are available on the servers. To access those from a terminal:

```bash
man command
```

`man` uses `less` (see the section [Viewing and editing files](#viewing-and-editing-files)), and you must press `q` to exit this program.

By convention, the executables themselves contain some help on how to use them. Generally, you invoke this help using the command line argument `-h` or `--help`, or in certain cases, `-help`.
For example,

```bash
ls --help
```

## Orienting yourself on a system

Following your connection, you are directed to your `$HOME` directory (the UNIX word for *folder*) for your user account. When your account is created, your `$HOME` only contains a few hidden configuration files that start with a period (.), and nothing else.

!!! warning
    On a Linux system, you are strongly discouraged to create files or directories that contain names with spaces or special characters, including accents.

### Listing directory contents

To list all files in a directory in a terminal, use the `ls` (list) command:

```bash
ls
```

To include hidden files:

```bash
ls -a
```

To sort results by date (from newest to oldest) instead of alphabetically:

```bash
ls -t
```

And, to obtain detailed information on all files (permissions, owner, group, size and last modification date):

```bash
ls -l
```

The option `-h` gives the file sizes in human readable format.

You can combine options, for example:

```bash
ls -alth
```

### Navigating the filesystem

To move about in the filesystem, use the `cd` command (change directory).

So, to change to `my_directory`, type:

```bash
cd my_directory
```

To change to the parent folder, type:

```bash
cd ..
```

And, to move back to your home directory (`$HOME`):

```bash
cd
```

### Creating and removing directories

To create (make) a directory, use the `mkdir` command:

```bash
mkdir my_directory
```

To remove a directory, use the `rmdir` command:

```bash
rmdir my_directory
```

Deleting a directory like this only works if it is empty.

### Deleting files

You can remove files using the `rm` command:

```bash
rm my_file
```

You can also recursively remove a directory:

```bash
rm -r my_directory
```

!!! warning
    The (potentially dangerous!) `-f` option can be useful to bypass confirmation prompts and to continue the operation after an error.

### Copying and renaming files or directories

To copy a file use the `cp` command:

```bash
cp source_file destination_file
```

To recursively copy a directory:

```bash
cp -R source_directory destination_directory
```

To rename a file or a folder (directory), use the `mv` command (move):

```bash
mv source_file destination_file
```

This command also applies to directories. You should then replace `source_file` with `source_directory` and `destination_file` with `destination_directory`.

## File permissions

UNIX systems support 3 types of permissions : read (`r`), write (`w`) and execute (`x`). For files, a file should be readable to be read, writable to be modified, and executable to be run (if it's a binary executable or a script). For a directory, read permissions are necessary to list its contents, write permissions enable modification (adding or removing a file) and execute permissions enable changing to it.

Permissions apply to 3 different classes of users, the owner (`u`), the group (`g`), and all others or *the world* (`o`). To know which permissions are associated to files and subdirectories of the current directory, use the following command:

```bash
ls -la
```

The 10 characters at the beginning of each line show the permissions. The first character indicates the file type :
* `-`: a normal file
* `d`: a directory
* `l`: a symbolic link

Then, from left to right, this command shows read, write and execute permissions of the owner, the group and other users. Here are some examples :
* `drwxrwxrwx`: a world-readable and world-writable directory
* `drwxr-xr-x`: a directory that can be listed by everybody, but only the owner can add or remove files
* `-rwxr-xr-x`: a world-readable and world-executable file that can only be changed by its owner
* `-rw-r--r--`: a world-readable file that can only be changed by its owner.
* `-rw-rw----`: a file that can be read and changed by its owner and by its group
* `-rw-------`: a file that can only be read and changed by its owner
* `drwx--x--x`: a directory that can only be listed or modified by its owner, but all others can still pass it on their way to a deeper subdirectory
* `drwx-wx-wx`: a directory that everybody can enter and modify but where only the owner can list its contents

!!! important "Important note"
    To be able to read or write in a directory, you need to have execute permissions (`x`) set in all parent directories, all the way up to the filesystem's root (**`/`**). So if your home directory has `drwx------` permissions and contains a subdirectory with `drwxr-xr-x` permissions, other users cannot read the contents of this subdirectory because they do not have access (by the executable bit) to its parent directory.

After listing the permissions, `ls -la` command gives a number, followed by the file owner's name, the file group's name, its size, last modification date, and name.

The `chmod` command allows you to change file permissions. The simple way to use it is to specify which permissions you wish to add or remove to which type of user. To do this, you specify the list of users (`u` for the owner, `g` for the group, `o` for other users, `a` for all three), followed by a `+` to add permissions or `-` to remove permissions, which is then followed by a list of permissions to modify (`r` for read, `w` for write, `x` for execute). Non-specified permissions are not affected. Here are a few examples:

* Prevent group members and all others to read or modify the file `secret.txt`:
    ```bash
    chmod go-rwx secret.txt
    ```
* Allow everybody to read the file `public.txt`:
    ```bash
    chmod a+r public.txt
    ```
* Make the file `script.sh` executable:
    ```bash
    chmod a+x script.sh
    ```
* Allow group members to read and write in the directory `shared`:
    ```bash
    chmod g+rwx shared
    ```
* Prevent other users from reading or modifying your home directory:
    ```bash
    chmod go-rw ~
    ```

## Viewing and editing files

### Viewing a file

To view a file read-only, use the `less` command:

```bash
less file_to_view
```

You can then use the arrow keys or the mouse wheel to navigate the document. You can search for something in the document by typing `/what_to_search_for`. You can quit `less` by pressing the `q` key.

### Comparing two files

The `diff` command allows you to compare two files:

```bash
diff file1 file2
```

The `-y` option shows both files side by side.

### Searching within a file

The `grep` command allows you to look for a given expression in one file:

```bash
grep 'tata' file1
```

... or in multiple files:

```bash
grep 'tata' fil*
```

!!! note
    In Linux, the `*` wildcard matches zero or more characters. The `?` wildcard matches exactly one character.

The text to be searched for can also be variable. For example, to look for the text *number 10* or *number 11*, etc. with any number between 10 and 29, the following command can be used:

```bash
grep 'number [1-2][0-9]' file
```

A regular expression must be used for the search text. To learn more, [see this guide to regular expressions](http://www.cyberciti.biz/faq/grep-regular-expressions/).