---
title: "Sharing data"
slug: "sharing_data"
lang: "base"

source_wiki_title: "Sharing data"
source_hash: "086474696b64686afc964624cabe7234"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:29:36.215462+00:00"

tags:
  []

keywords:
  - "directory sharing"
  - "ACL attributes"
  - "share data"
  - "directory"
  - "umask"
  - "groups"
  - "Globus"
  - "project filesystem"
  - "filesystem permissions"
  - "executable"
  - "setGID bit"
  - "Filesystem permissions"
  - "Access Control Lists (ACLs)"
  - "chmod"
  - "group"
  - "project directory"
  - "file permissions"
  - "sticky bit"
  - "owner"
  - "user categories"
  - "readable"
  - "octal notation"
  - "setfacl"
  - "data sharing group"
  - "octal values"
  - "Security risk"
  - "execute permission"
  - "access permissions"
  - "File permissions"
  - "Data sharing"
  - "setGID"
  - "current working directory"
  - "new file"
  - "writable"
  - "default group"
  - "group permissions"
  - "setUID"

questions:
  - "Why is issuing a bulk `chmod -R 777` command on your folders considered a major security risk on shared cluster facilities?"
  - "What are the recommended mechanisms for sharing data with colleagues depending on their account status and research group affiliation?"
  - "How do Linux filesystem permissions work, and why must a user have execute access to the entire directory chain to read a shared file?"
  - "What do the user category abbreviations `u`, `g`, `o`, and `a` stand for in the context of file permissions?"
  - "How does the command `chmod g+r file.txt` affect the access rights for the members of the file's group?"
  - "What is the specific outcome of executing the command `chmod o-x script.py` regarding execute permissions?"
  - "How is octal notation calculated and used to represent Unix filesystem permissions for different user categories?"
  - "What is the purpose of the sticky bit in a shared directory, and how can it be configured using the chmod command?"
  - "How does enabling the Set Group ID (setGID) bit affect the group ownership of newly created files and directories within a parent directory?"
  - "What are the two groups associated with the user in the provided example?"
  - "What are the permissions and group ownership of the existing directory before a new file is created?"
  - "Which group is automatically assigned to a newly created file within the directory?"
  - "How does enabling the setGID permission on a parent directory affect the group ownership of newly created files and subdirectories within it?"
  - "What does an uppercase 'S' indicate in directory permissions compared to a lowercase 's', and what potential access issues can it cause?"
  - "What is the function of the umask command, and how can it be used to view or change the default access permissions for newly created files?"
  - "Besides the umask, what other factors and directory-level permissions determine a user's ability to access a file?"
  - "How can the chmod command be used to change the permissions of existing files and entire directories?"
  - "What are Access Control Lists (ACLs), and how do commands like setfacl allow for more fine-grained, user-specific file sharing compared to standard Unix permissions?"
  - "What type of numerical values does the umask command accept according to the text?"
  - "What are the specific file permissions granted to the owner, group, and others when the umask is set to 077?"
  - "How does a umask value of 027 change the readability, writability, and executability of files for the group compared to the owner?"
  - "What specific permission must be granted on all parent directories to successfully share data with another user?"
  - "What commands can be used to apply the required execute permissions for a specific user or for everyone?"
  - "Is public read permission necessary for sharing data, and how does this apply to the main project directory?"
  - "Why must collaborators be given a physical directory path starting with `/project` rather than a symlink, and what command is used to find it?"
  - "What is the process for creating and adding members to a data sharing group for complex sharing scenarios?"
  - "How can a user recursively check a directory to list all items they do not have read access to?"
  - "Why must collaborators be given a physical directory path starting with `/project` rather than a symlink, and what command is used to find it?"
  - "What is the process for creating and adding members to a data sharing group for complex sharing scenarios?"
  - "How can a user recursively check a directory to list all items they do not have read access to?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Parent page: [Storage and file management](storage_and_file_management.md)*

!!! warning "Important Note"
    Do **not** ever issue a bulk `chmod -R 777` on your home folder, in fact on any of your folders for that matter. This is a **huge** security risk and is completely unacceptable on shared facilities such as our clusters. In addition, it's never necessary.

Having to share some but not all of your data with a colleague or another research group is a common occurrence. Our systems provide a variety of mechanisms to facilitate this data sharing with colleagues. If the person you want to share the data with is a member of the same research group as you, then the best approach may be to make use of the [project space](project_layout.md) that each research group has in common; if your research requires the creation of a group on one of the national clusters, you can request this by contacting [technical support](../support/technical_support.md) since users cannot create their own groups. At the opposite extreme, if the person you need to share the data with doesn't even have an account on the cluster, you can use [Globus](../getting-started/globus.md) and in particular what is called a [shared endpoint](../getting-started/globus.md#globus-sharing) to share the data. To handle the scenario of sharing with a colleague who has an account on the cluster but doesn't belong to a common research group with you, the simplest approach is to use the permissions available in the filesystem to share the data, the principal topic of this page.

When sharing a file, it's important to realize that the individual you want to share it with must have access to the entire chain of directories leading from `/scratch` or `/project` to the directory in which the file is located. If we consider the metaphor of a document locked in a safe in the bedroom of your apartment in a large building, giving me the combination to the safe will not allow me to read this document if I do not also have the necessary keys to enter the apartment building, your apartment and finally your bedroom. In the context of a filesystem, this means having execute permission for each directory between the root (e.g. `/scratch` or `/project`) and the directory containing the file.

## Filesystem permissions

Like most modern filesystems, those used on our clusters support the idea of permissions to read, write, and execute files and directories. When you attempt to read, modify or delete a file, or access a directory, e.g. with `cd`, the Linux kernel first verifies that you have the right to do this. If not, you'll see the error message *Permission denied*. For each filesystem object (file or directory) there are three categories of users:
* the object's owner --- normally the user who created the object,
* members of the object's group --- normally the same as the owner's default group, and
* everyone else.
Each of these categories of users may have the right to read, write, or execute the object. Three categories of users times three types of permission means there are nine permissions associated with each object.

You can see what the current permissions are for a filesystem object with the command
```bash
ls -l name_of_object
```
which will print out the permissions for the owner, the group, and everyone else. For example, a file with permissions `-rw-r--r--` means the owner can read it and write it but not execute it, and the group members and everyone else can only read the file. You'll also see printed out the name of the object's owner and the group.

To change the permissions of a file or directory you can use the command `chmod` along with the user category, a plus or minus sign indicating that permission is granted or withdrawn, and the nature of the permission: read (`r`), write (`w`) or execute (`x`). For the user category, we use the abbreviations `u` for the owner (user), `g` for the group and `o` for others, i.e. everyone else on the cluster. So a command like
```bash
chmod g+r file.txt
```
would grant read permission to all members of the group that file.txt belongs to, while
```bash
chmod o-x script.py
```
would withdraw execute permission for the file script.py to everyone but the owner and the group. We can also use the user category `a` to denote everyone (all), thus
```bash
chmod a+r file.txt
```
grants everyone on the cluster the right to read file.txt.

It's also common for people to use *octal notation* when referring to Unix filesystem permissions even if this is somewhat less intuitive than the above symbolic notation. In this case, we use three bits to represent the permissions for each category of user, with these three bits then interpreted as a number from 0 to 7 using the formula (read_bit)\*4 + (write_bit)\*2 + (execute_bit)\*1. In the above example, the octal representation would be 4+2+0 = 6 for the owner and 4+0+0 = 4 for the group and everyone else, so 644 overall.

Note that to be able to exercise your rights on a file, you also need to be able to access the directory in which it resides. This means having both read and execute permission ("5" or "7" in octal notation) on the directory in question.

You can alter these permissions using the command `chmod` in conjunction with the octal notation discussed above, so for example
```bash
chmod 770 name_of_file
```
means that everyone in your group now has the right to read, write and execute this file. Naturally, you can only modify the permissions of a file or directory you own. You can also alter the group by means of the command `chgrp`.

### The sticky bit
When dealing with a shared directory where multiple users have read, write and execute permission, as would be common in the [project space](project_layout.md) for a professor with several active students and collaborators, the issue of ensuring that an individual cannot delete the files or directories of another can arise. For preventing this kind of behaviour, the Unix filesystem developed the concept of the [sticky bit](https://en.wikipedia.org/wiki/Sticky_bit) by means of which the filesystem permissions for a directory can be restricted so that a file in that directory can only be renamed or deleted by the file's owner or the directory's owner. Without this sticky bit, users with write and execute permission for that directory can rename or delete any files that it may contain even if they are not the file's owner. The sticky bit can be set using the command `chmod`, for example
```bash
chmod +t <directory name>
```
or if you prefer to use the octal notation discussed above by using the mode 1000, hence
```bash
chmod 1774 <directory name>
```
to set the sticky bit and `rwxrwxr--` permissions on the directory.

The sticky bit is represented in `ls -l` output by the letter "t" or "T" in the last place of the permissions field, like so:
```bash
$ ls -ld directory
drwxrws--T 2 someuser def-someuser 4096 Sep 25 11:25 directory
```

The sticky bit can be unset by the command
```bash
chmod -t <directory name>
```
or via octal notation,
```bash
chmod 0774 <directory name>
```
In the context of the project space, the directory owner will be the PI who sponsors the roles of the students and collaborators.

### Set Group ID bit
When creating files and directories within a parent directory, it is often useful to match the group ownership of the new files or directories to the parent directory's owner or group automatically.

If the `setGID` bit is enabled for a directory, new files and directories in that directory will be created with the same group ownership as the directory. To illustrate the use of this mode, let us walk through an example.

Start by checking the groups that `someuser` belongs to with the `groups` command.
```bash
[someuser@server]$ groups
someuser def-someuser
```
`someuser` belongs to two groups `someuser` and `def-someuser`. In the current working directory there is a directory which belongs to the group `def-someuser`.
```bash
[someuser@server]$ ls -l
drwxrwx---  2 someuser   def-someuser       4096 Oct 13 19:39 testDir
```
If we create a new file in that directory we can see that it is created belonging to `someuser`'s default group `someuser`.
```bash
[someuser@server]$ touch dirTest/test01.txt
[someuser@server]$ ls -l dirTest/
-rw-rw-r-- 1 someuser   someuser    0 Oct 13 19:38 test01.txt
```
If we are in `/project` this is probably not what we want. We want a newly created file to belong to the same group as the parent folder. Enable the `setGID` permission on the parent directory like so:
```bash
[someuser@server]$ chmod g+s dirTest
[someuser@server]$ ls -l
drwxrws---  2 someuser   def-someuser       4096 Oct 13 19:39 dirTest
```
Notice that the `x` permission on the group permissions has changed to an `s`. Now newly created files in `dirTest` will have the same group as the parent directory.
```bash
[someuser@server]$ touch dirTest/test02.txt
[someuser@server]$ ls -l dirTest
-rw-rw-r-- 1 someuser   someuser      0 Oct 13 19:38 test01.txt
-rw-rw-r-- 1 someuser   def-someuser  0 Oct 13 19:39 test02.txt
```
If we create a directory inside a directory with the `setGID` enabled, it will have the same group as the parent folder and also have its `setGID` enabled.
```bash
[someuser@server]$ mkdir dirTest/dirChild
[someuser@server]$ ls -l dirTest/
-rw-rw-r-- 1 someuser   someuser      0 Oct 13 19:38 test01.txt
-rw-rw-r-- 1 someuser   def-someuser  0 Oct 13 19:39 test02.txt
drwxrwsr-x 1 someuser   def-someuser  0 Oct 13 19:39 dirChild
```
Finally, it can be important to note the difference between `S` (uppercase S) and `s`. The uppercase S indicates that execute permissions have been removed from the directory but the `setGID` is still in place. It can be easy to miss this and may result in unexpected problems, such as others in the group not being able to access files within your directory.
```bash
[someuser@server]$ chmod g-x dirTest/
[someuser@server]$ ls -l
drwxrS---  3 someuser   def-someuser       4096 Oct 13 19:39 dirTest
```

### Set User ID bit
!!! warning "SetUID Disabled"
    The `setUID` bit **will not work** on our clusters. Its usual behaviour is completely disabled, for security reasons.

## Default filesystem permissions

Default filesystem permissions are defined by something called the [`umask`](https://en.wikipedia.org/wiki/Umask). There is a default value that is defined on any Linux system. To display the current value in your session, you can run the command
```bash
umask -S
```
For example, on our clusters, you would get
```bash
umask -S
# u=rwx,g=rx,o=
```
This means that, by default, new files that you create can be read, written and executed by yourself, they can be read and executed by members of the group of the file, and they cannot be accessed by other people. **The `umask` only applies to new files. Changing the `umask` does not change the access permissions of existing files.**

There may be reasons to define default permissions more permissive (for example, to allow other people to read and execute files), or more restrictive (not allowing your group to read or execute files). Setting your own `umask` can be done either in a session, or in your `.bashrc` file, by calling the command
```bash
umask <value>
```
where the `<value>` can take a number of octal values. Below is a table of useful options, depending on your use case:

| `umask` value | `umask` meaning | Human-readable explanation |
| :------------ | :-------------- | :-------------------------------------------------------------------------------------- |
| 077           | u=rwx,g=,o=     | Files are readable, writable and executable by the owner only                             |
| 027           | u=rwx,g=rx,o=   | Files are readable and executable by the owner and the group, but writable only by the owner |
| 007           | u=rwx,g=rwx,o=  | Files are readable, writable and executable by the owner and the group                  |
| 022           | u=rwx,g=rx,o=rx | Files are readable and executable by everyone, but writable only by the owner             |
| 002           | u=rwx,g=rwx,o=rx| Files are readable and executable by everyone, but writable only by the owner and the group |

The umask is not the only thing that determines who can access a file.
* A user trying to access a file must have execute permission on all directories in the path to the file. For example, a file might have `o=rx` permissions but an arbitrary user could not read or execute it if the parent directory does not also have `o=x` permission.
* The user trying to access a file based on its group permissions must be a member of the file's group.
* You can explicitly change the permissions on a file or directory after it is created, using `chmod`.
* Access Control Lists (ACLs) also determine who can access a file.

Note that this change does *not* mean that your files have been inappropriately exposed in the past. Restrictive access permissions have been set on your home, project, and scratch directories since the beginning. Unless the permissions were changed to give *execute* permission to other users on these folders, they still cannot be accessed by them.

### Changing the permissions of existing files
If you want to change the permissions of existing files to match the new default permissions, you can use the `chmod` command as follow:
```bash
chmod g-w,o-rx <file>
```
or, if you want to do it for a whole directory, you can run
```bash
chmod -R g-w,o-rx <directory>
```

## Access control lists (ACLs)

### Sharing access with an individual

The file permissions discussed above have been available in Unix-like operating systems for decades now but they are very coarse-grained. The whole set of users is divided into just three categories: the owner, the group, and everyone else. What if you want to allow someone who isn't in a group to read a file - do you really need to make the file readable by everyone in that case? The answer, happily, is no. Our national systems offer *access control lists* (ACLs) to enable permissions to be set on a user-by-user basis if desired. The two commands needed to manipulate these extended permissions are
* `getfacl` to see the ACL permissions, and
* `setfacl` to alter them.

#### Sharing a single file
To allow a single person with username `smithj` to have read and execute permission on the file `my_script.py`, use:
```bash
$ setfacl -m u:smithj:rx my_script.py
```

#### Sharing a subdirectory

To allow read and write access to a single user in a whole subdirectory, including new files created in it, you can run the following commands:

```bash
$ setfacl -d -m u:smithj:rwX /home/<user>/projects/def-<PI>/shared_data
$ setfacl -R -m u:smithj:rwX /home/<user>/projects/def-<PI>/shared_data
```
!!! note
    The `X` attribute above (compared to `x`) sets the *execute* permission only when the item is already executable (either a directory or a file with the execute permission). A directory needs the execute permission to allow it to be browsed.

The first command sets default access rules to directory `/home/<user>/projects/def-<PI>/shared_data`, so any file or directory created within it will inherit the same ACL rule. It is required for **new** data. The second command sets ACL rules to directory `/home/<user>/projects/def-<PI>/shared_data` and all its content currently in it. So it is applicable only to **existing** data.

In order for this method to work the following things need to be in place:
* The directory, `/home/smithj/projects/def-smithj/shared_data` in our example, must be owned by you.
* Parent directories (and parents of parents, etc.) of the one you are trying to share must allow execute permission to the user you are trying to share with. This can be supplied with `setfacl -m u:smithj:X ...` in this example, or it can be supplied by allowing everyone entry, i.e. `chmod o+x ...`. They do not need to have public read permission. In particular you will need to grant execute permission on the project directory (`/projects/def-<PI>`) either for everyone, or one-by-one to all the people you are trying to share your data with.
* When sharing a directory in the project filesystem, you must provide your collaborators with a path that starts with `/project`, **not** with `/home/<user>/projects`. The latter contains symbolic links (symlinks, or shortcuts) to the physical directories in `/project`, and these symlinks will not be reachable by your collaborators unless they also have access to your home directory. You can get the physical path a symlink points to using the `realpath` command. For example, `realpath /home/smithj/projects/def-smithj/shared_data` could return `/project/9041430/shared_data`. The physical path to a project directory is not the same on all clusters. If you wish to share a project directory on more than one cluster, check its physical path with `realpath` on each cluster.

#### Removing ACL
To remove all extended ACL attributes from a directory recursively, use:
```bash
setfacl -bR /home/<user>/projects/def-<PI>/shared_data
```

### Data sharing groups

For more complicated data sharing scenarios (those involving multiple people on multiple clusters), it is also possible to create a **data sharing group**. A data sharing group is a special group to which all people with whom certain data is to be shared are added. This group is then given access permissions through ACLs.

You do not need a data sharing group except in specialized sharing circumstances.

#### Creating a data sharing group

The steps below describe how to create a data sharing group. In this example it is called `wg-datasharing`

1.  Send email to our [technical support](../support/technical_support.md) requesting creation of data sharing group, indicate name of the group you would like to have and that you should be the owner.
2.  When you receive confirmation from the technical support team that the group has been created, go to [ccdb.computecanada.ca/services/](https://ccdb.computecanada.ca/services/) and access it:
    (Image removed)
3.  Click on the group's name and enter the group management screen:
    (Image removed)
4.  Add member (Victor Van Doom with CCI vdv-888, for example) to the group as a member:
    (Image removed)

#### Using a data sharing group

Just as with individual user sharing, the parent directories of the data you are trying to share must have execute permissions either for everyone or for the data sharing group. In your project directory, this implies that your PI must give consent as follows (unless you have permission to do this yourself):

```bash
$ chmod  o+X /project/def-<PI>/
```
or
```bash
$ setfacl -m g:wg_datasharing:X /project/def-<PI>/
```

Finally, you can add your group to the ACL for the directory you are trying to share. The commands parallel those needed to share with an individual:

```bash
$ setfacl -d -m g:wg-datasharing:rwx /home/<user>/projects/def-<PI>/shared_data
$ setfacl -R -m g:wg-datasharing:rwx /home/<user>/projects/def-<PI>/shared_data
```

## Troubleshooting

### Testing read access recursively

To make sure you have the read access to everything in a specific directory, you can use the following command which lists all items not readable to you:

```bash
find <directory_name> ! -readable -ls