---
title: "Linux introduction/en"
slug: "linux_introduction"
lang: "en"

source_wiki_title: "Linux introduction/en"
source_hash: "42539041e8e26cd8c29d254e39f11ce6"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:31:35.804028+00:00"

tags:
  []

keywords:
  - "directory"
  - "classes of users"
  - "grep command"
  - "permissions"
  - "searching within a file"
  - "Linux"
  - "chmod"
  - "search text"
  - "file permissions"
  - "less"
  - "command"
  - "Console"
  - "guide"
  - "grep"
  - "multiple files"
  - "File permissions"
  - "UNIX environments"
  - "UNIX commands"
  - "wildcard"
  - "regular expressions"
  - "ls -la"
  - "Filesystem"
  - "files"
  - "read/write/execute"

questions:
  - "How can a user access the built-in documentation and help manuals for UNIX commands directly from the console?"
  - "What are the primary commands used to navigate the filesystem, list directory contents, and manage files or folders?"
  - "How do read, write, and execute permissions function differently when applied to files versus directories in a UNIX system?"
  - "How do you interpret the 10-character permission string displayed by the `ls -la` command for files and directories?"
  - "What is the syntax for using the `chmod` command to add or remove specific permissions for different types of users?"
  - "Which commands can be used to view the contents of a file, compare two different files, and search for specific text patterns within them?"
  - "What specific actions do read, write, and execute permissions allow a user to perform on a directory?"
  - "What are the three distinct classes of users that file and directory permissions apply to?"
  - "How can a user view the permissions associated with the files and subdirectories located in their current directory?"
  - "How do you use the `grep` command to search for a specific expression across single or multiple files?"
  - "What is the difference in functionality between the `*` and `?` wildcards in Linux?"
  - "How can you search for variable text patterns, such as a specific range of numbers, within a file?"
  - "What specific command is provided to search for a number pattern within a file?"
  - "What type of format must be used for the search text in the given command?"
  - "Where can a user find the recommended guide to learn more about regular expressions?"
  - "What specific command is provided to search for a number pattern within a file?"
  - "What type of format must be used for the search text in the given command?"
  - "Where can a user find the recommended guide to learn more about regular expressions?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

This article is aimed at Windows and Mac users who do not have or have very little experience in UNIX environments. It should give you the necessary basics to access the compute servers and be quickly able to use them.

Connections to the servers use the [SSH](ssh.md) protocol, in text mode. You do not use a graphical interface (GUI) but a **console**. Note that Windows executables do not run on our servers without using an emulator.

There is a self-paced course available on this topic from SHARCNET: [Introduction to the Shell](https://training.sharcnet.ca/courses/enrol/index.php?id=182)

## Obtaining help
Generally, UNIX commands are documented in the reference manuals that are available on the servers. To access those from a terminal:
```bash
man command
```
`man` uses `less` (see the section [Viewing and editing files](#viewing-and-editing-files)), and you must press `q` to exit this program.

By convention, the executables themselves contain some help on how to use them.
Generally, you invoke this help using the command line argument `-h` or `--help`, or in certain cases, `-help`.
For example,
```bash
ls --help
```

## Orienting yourself on a system
Following your connection, you are directed to your `$HOME` directory (the UNIX word for *folder*) for your user account.
When your account is created, your `$HOME` only contains a few hidden configuration files that start with a period (.), and nothing else.

!!! warning "Filenaming Conventions"
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
!!! warning "Dangerous Option"
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

The 10 characters at the beginning of each line show the permissions.
The first character indicates the file type :
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

!!! note "Important Note: Directory Execute Permissions"
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
You can then use the arrow keys or the mouse wheel to navigate the document.
You can search for something in the document by typing `/what_to_search_for`.
You can quit `less` by pressing the `q` key.

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
Note that, in Linux, the `*` wildcard matches zero or more characters. The `?` wildcard matches exactly one character.

The text to be searched for can also be variable. For example, to look for
the text *number 10* or *number 11*, etc. with any number between 10 and 29,
the following command can be used:
```bash
grep 'number [1-2][0-9]' file
```
A regular expression must be used for the search text. To learn more, [see this guide to regular expressions](http://www.cyberciti.biz/faq/grep-regular-expressions/).