---
title: "Project layout"
slug: "project_layout"
lang: "base"

source_wiki_title: "Project layout"
source_hash: "f7498c5691cd82bf020bccbab69392fc"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:27:05.119773+00:00"

tags:
  []

keywords:
  - "group membership"
  - "disk quota"
  - "sponsored user"
  - "quota"
  - "chgrp"
  - "setgid"
  - "directory structure"
  - "project space"
  - "file permissions"
  - "scratch space"
  - "RAC award"
  - "project filesystem"
  - "sharing data"

questions:
  - "How is the project filesystem organized, and how can users configure directories to allow write access for all group members?"
  - "What are the default storage quotas for a project group, and how can users check their current disk usage?"
  - "How can users resolve \"disk quota exceeded\" errors caused by files being associated with the wrong group?"
  - "What are the specific purposes and characteristics of the scratch, home, and project spaces?"
  - "How do users within the same sponsored research group share data and access shared project directories?"
  - "What methods and permission adjustments are required to share files with researchers who do not have a sponsored role or a cluster account?"
  - "What command is provided to find and change the group membership of specific files?"
  - "Why is it recommended to assign these files to a group like `def-profname`?"
  - "How does the text use the example of PI \"Sue\" and sponsored user \"Bob\" to illustrate directory structures?"
  - "What are the specific purposes and characteristics of the scratch, home, and project spaces?"
  - "How do users within the same sponsored research group share data and access shared project directories?"
  - "What methods and permission adjustments are required to share files with researchers who do not have a sponsored role or a cluster account?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Parent page: [Storage and file management](storage_and_file_management.md)*
*See also: [Disk quota exceeded error on /project filesystems](../getting-started/frequently_asked_questions.md#disk-quota-exceeded-error-on-project-filesystems)*

The project filesystem on our compute clusters is organized on the basis of **groups**. The normal method to access the project space is by means of symbolic links which exist in your home directory. These will have the form `$HOME/projects/group_name` apart from the clusters [Rorqual](../clusters/rorqual.md) and [Trillium](../clusters/trillium.md) where the path will take the form `$HOME/links/projects/group_name`.

The permissions on the group space are such that it is owned by the principal investigator (PI) for this group and members have read and write permission on this directory. However, by default a newly created file will only be readable by group members. If the group wishes to have writeable files, the best approach is to create a special directory for that, for example:

```bash
mkdir $HOME/projects/def-profname/group_writable
```

followed by:

```bash
setfacl -d -m g::rwx $HOME/projects/def-profname/group_writable
```

For more on sharing data, file ownership, and access control lists (ACLs), see [Sharing data](sharing_data.md).

The project space is subject to a default quota of 1 TB and 500,000 files per group, which can be increased up to 40 TB of space upon request to [Technical support](../support/technical_support.md). Certain groups may have been awarded significantly higher quotas through the annual [Resource Allocation Competition](https://alliancecan.ca/en/services/advanced-research-computing/accessing-resources/resource-allocation-competition). In this case, you will already have been notified of your group's quota for the coming year. Note that this storage allocation is specific to a particular cluster and cannot normally be transferred to another cluster.

To check current usage and available disk space, use:

```bash
diskusage_report
```

In order to ensure that files which are copied or moved to a given project space acquire the appropriate group membership - and thus are counted against the expected quota - it can be useful to set the `setgid` bit on the directory in question. This will have the effect of ensuring that every new file and subdirectory created below the directory will inherit the same group as the ambient directory; equally so, new subdirectories will also possess this same `setgid` bit. However, existing files and subdirectories will not have their group membership changed - this should be done with the `chgrp` command - and any files moved to the directory will also continue to retain their existing group membership. You can set the `setgid` bit on a directory with the command:

```bash
chmod g+s <directory name>
```

If you want to apply this command to the existing subdirectories of a directory, you can use the command:

```bash
find <directory name> -type d -print0 | xargs -0 chmod g+s
```

More information on the `setgid` is available from this [page](https://en.wikipedia.org/wiki/Setuid#setuid_and_setgid_on_directories).

You can also use the command `newgrp` to modify your default group during an interactive session, for example:

```bash
newgrp rrg-profname-ab
```

and then to copy any data to the appropriate project directory. This will only change your default group for this particular session however - at your next login you will need to reuse the `newgrp` command if you wish to change the default group again.

!!! warning "Disk quota exceeded errors"
    Note that if you are getting *disk quota exceeded* error messages (see [Disk quota exceeded error on /project filesystems](../getting-started/frequently_asked_questions.md#disk-quota-exceeded-error-on-project-filesystems)), this may well be due to files being associated with the wrong group, notably your personal group, i.e. the one with the same name as your username and which has a quota of only 2 MB. To find and fix the group membership of such files you can use the command:

    ```bash
    find <directory name> -group $USER -print0 | xargs -0 chgrp -h <group>
    ```

    where `<group>` is something like `def-profname`, thus a group with a reasonable quota of a terabyte or more.

## An explanatory example

Imagine that we have a PI (“Sue”) who has a sponsored user under her (“Bob”). Both Sue and Bob start with a directory structure that on the surface looks similar:

*   `/home/sue/scratch` (symbolic link)
*   `/home/sue/projects` (directory)
*   `/home/bob/scratch` (symbolic link)
*   `/home/bob/projects` (directory)

The `scratch` link points to a different location for Sue (`/scratch/sue`) and Bob (`/scratch/bob`).

If Bob's only role was the one sponsored by Sue, then Bob's `projects` directory would have the same contents as Sue's `projects` directory. Further, if neither Sue nor Bob have any other roles or projects with the Alliance, then each one's `projects` directory would just contain one subdirectory, `def-sue`.

Each of `/home/sue/projects/def-sue` and `/home/bob/projects/def-sue` would point to the same location, `/project/<some random number>`. This project directory is the best place for Sue and Bob to share data. They can both create directories in it, read it, and write to it. Sue for instance could do:

```bash
cd ~/projects/def-sue
mkdir foo
```

and Bob could then copy a file into the directory `~/projects/def-sue/foo`, where it will be visible to both of them.

If Sue were to get a RAC award with storage (as is often the case these days), both she and Bob would find that there is a new entry in their respective `projects` directory, something like `~/projects/rrg-sue-ab`. They should use this directory to store and share data related to the research carried out under the RAC award.

For sharing data with someone who doesn't have a role sponsored by Sue --- let's say Heather --- the simplest thing to do is to change the file permissions so that Heather can read a particular directory or file. See [Sharing data](sharing_data.md) for more details. The best idea is usually to use ACLs to let Heather read a directory. Note that these filesystem permissions can be changed for almost any directory or file, not just those in your `project` space --- you could share a directory in your `scratch` too, or just a particular subdirectory of `projects`, if you have several (a default one, one for a RAC, *etc.*). Best practice is to restrict file sharing to `/project` and `/scratch`.

One thing to keep in mind when sharing a directory is that Heather will need to be able to descend the entire filesystem structure down to this directory and so she will need to have read and execute permission on each of the directories between `~/projects/def-sue` and the directory containing the file(s) to be shared. We have implicitly assumed here that Heather has an account on the cluster but you can even share with researchers who don't have an Alliance account using a [Globus shared endpoint](../getting-started/globus.md#globus-sharing).

If Heather is pursuing a serious and ongoing collaboration with Sue then it may naturally make sense for Sue to sponsor a role for Heather, thereby giving Heather access similar to Bob's, described earlier.

!!! info "Summary"
    *   `scratch` space is for (private) temporary files
    *   `home` space is normally for small amounts of relatively private data (e.g. a job script)
    *   Shared data for a research group should normally go in that group's `project` space, as it is persistent, backed up, and fairly large (up to 40 TB, or more with a RAC).