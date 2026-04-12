---
title: "Globus"
slug: "globus"
lang: "base"

source_wiki_title: "Globus"
source_hash: "1f4fa42a1e1d3413e6e8f17eb024a99e"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:43:30.955509+00:00"

tags:
  - connecting

keywords:
  - "Transfer & Sync Options"
  - "transfer"
  - "Sharing security"
  - "collections"
  - "Arbutus S3 buckets"
  - "Activity button"
  - "share with"
  - "sharing interface"
  - "access list"
  - "OpenStack command line client"
  - "permissions"
  - "Globus groups"
  - "Virtual machines"
  - "shared collection"
  - "monitor in-progress transfers"
  - "access ID"
  - "managing access"
  - "Globus"
  - "Shared collection"
  - "Globus Connect"
  - "secret key"
  - "Arbutus"
  - "openstack ec2 credentials"
  - "endpoint identifier"
  - "Permissions"
  - "GridFTP"
  - "Globus sharing"
  - "unique ID"
  - "Digital Research Alliance of Canada"
  - "file sharing"
  - "file or directory"
  - "Alliance cluster"
  - "Command line interface"
  - "compute clusters"
  - "backups"
  - "shared endpoint"
  - "personal endpoints"
  - "Globus Connect Personal"
  - "Object storage"
  - "storage access ID"
  - "Managing access"
  - "file transfer"
  - "AWS IAM Access Key"
  - "Globus Connect Personal for Linux"
  - "manage permissions"

questions:
  - "What is Globus and what features does it use to improve file transfer performance over standard protocols?"
  - "What specific credentials and steps are required to successfully log into the Alliance Globus portal?"
  - "How do you search for collections and initiate a file transfer using the Globus File Manager?"
  - "What are the available \"Transfer & Sync Options\" in Globus, and how does enabling encryption affect transfer performance?"
  - "How do you install, configure, and run Globus Connect Personal to enable file transfers on a personal computer?"
  - "How does the Globus sharing feature allow you to collaborate and share files with colleagues who do not have an account on the host cluster?"
  - "How do you select multiple files or directories and initiate a transfer?"
  - "How will you be notified when your transfer job is complete?"
  - "Where can you monitor in-progress transfers and view the details of completed jobs?"
  - "What is the primary benefit of using Globus sharing for collaboration?"
  - "What are the account requirements for someone to access files shared from an Alliance cluster?"
  - "Where can a user find instructions on how to share data and create a shared collection using Globus?"
  - "What are the default Globus sharing permissions for the different directories on general-purpose clusters, and how can a Principal Investigator request to enable sharing on a `/project` path?"
  - "Why must data be physically moved or copied to the chosen shared path rather than using symbolic links?"
  - "What are the specific steps required within the Globus portal to configure a new Guest Collection and grant access permissions to other users?"
  - "How can a user specify the directory path and configure access permissions for individuals or groups when creating a share?"
  - "What are the steps to delete a shared collection, and what happens to the files within it after deletion?"
  - "What are the recommended security best practices and potential risks to consider before granting others access to your files?"
  - "What is the function of the \"Browse\" button when preparing to share files?"
  - "Who is initially listed on the access list right after a shared collection is created?"
  - "How do you add specific people or groups to your shared collection's access list?"
  - "Why is it important to keep backups of files that are accessible on a shared endpoint?"
  - "What is the recommended directory level for restricting file sharing?"
  - "How do Globus groups simplify the process of managing access permissions for multiple users?"
  - "How do you create a new group and manage user memberships and roles within Globus?"
  - "What are the steps required to install the Globus command line interface (CLI) using a Python virtual environment?"
  - "Why do cloud VMs lack default Globus endpoints, and what are the two options available for installing an endpoint on them?"
  - "What are the prerequisites required before a user can access the object storage on Arbutus?"
  - "Which specific type of Arbutus Object Storage do these instructions apply to?"
  - "What tool must be used to generate the storage access ID and secret key?"
  - "How do you generate the storage access ID and secret key required for the setup?"
  - "What steps must be taken within the Globus portal to configure access to the Arbutus S3 buckets?"
  - "What specific information needs to be included when emailing the support team for help with the Globus service?"
  - "How do you generate the storage access ID and secret key required for the setup?"
  - "What steps must be taken within the Globus portal to configure access to the Arbutus S3 buckets?"
  - "What specific information needs to be included when emailing the support team for help with the Globus service?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Globus](https://www.globus.org/) is a service for fast, reliable, secure transfer of files. Designed specifically for researchers, Globus has an easy-to-use interface with background monitoring features that automate the management of file transfers between any two resources, whether they are on an Alliance cluster, another supercomputing facility, a campus cluster, lab server, desktop or laptop.

Globus leverages GridFTP for its transfer protocol but shields the end user from complex and time-consuming tasks related to GridFTP and other aspects of data movement. It improves transfer performance over GridFTP, rsync, scp, and sftp, by automatically tuning transfer settings, restarting interrupted transfers, and checking file integrity.

Globus can be accessed via the main [Globus website](https://www.globus.org/) or via [the Alliance Globus portal](https://globus.alliancecan.ca/).

## Using Globus
Go to [the Alliance Globus portal](https://globus.alliancecan.ca/); the first page illustrated below. Ensure that *Digital Research Alliance of Canada* is selected in the drop-down box, then click on *Continue*. The second page illustrated below will appear. Supply your CCDB *username* (not your e-mail address or other identifier) and password there. This takes you to the web portal for Globus.

### To start a transfer

Globus transfers happen between collections (formerly known as *endpoints* in previous Globus versions). Most Alliance clusters have some standard collections set up for you to use. To transfer files to and from your computer, you need to create a collection for them. This requires a bit of set up initially, but once it has been done, transfers via Globus require little more than making sure the Globus Connect Personal software is running on your machine. More on this below under [Personal computers](#personal-computers).

If the [File Manager page in the Globus Portal](https://globus.alliancecan.ca/file-manager) is not already showing, select it from the left sidebar.

On the top right of the page, there are three buttons labelled *Panels*. Select the second button (this will allow you to see two collections at the same time).

Find collections by clicking where the page says *Search* and entering a collection name.

You can start typing a collection name to select it. For example, if you want to transfer data to or from the Rorqual cluster, type *rorqual*, wait two seconds for a list of matching sites to appear, and select `alliancecan#rorqual`.

All clusters have a Globus collection name specified in the table on top of their respective wiki page:

| General-purpose | Large parallel | AI oriented |
| :-------------- | :------------- | :---------- |
| [Fir](fir.md)<br>[Narval](narval.md)<br>[Nibi](nibi.md)<br>[Rorqual](rorqual.md) | [Trillium](trillium.md) | [Killarney](killarney.md)<br>[TamIA](tamia.md)<br>[Vulcan](vulcan.md) |

You may be prompted to authenticate to access the collection, depending on which site it is hosted. For example, if you are activating a collection hosted on Nibi, you will be asked for your Alliance username and password. The authentication of a collection remains valid for some time, typically one week for Alliance collections, while personal collections do not expire.

Now select a second collection, searching for it and authenticating if required.

Once a collection has been activated, you should see a list of directories and files. You can navigate these by double-clicking on directories and using the 'up one folder' button. Highlight a file or directory that you want to transfer by single-clicking on it. Control-click to highlight multiple things. Then click on one of the big blue buttons with white arrowheads to initiate the transfer. The transfer job will be given a unique ID and will begin right away. You will receive an email when the transfer is complete. You can also monitor in-progress transfers and view details of completed transfers by clicking on the [Activity button](https://globus.alliancecan.ca/activity) on the left.

See also [How To Log In and Transfer Files with Globus](https://docs.globus.org/how-to/get-started/) at the Globus.org site.

### Options

Globus provides several other options in *Transfer & Sync Options* between the two *Start* buttons in the middle of the screen. Here you can direct Globus to
*   sync to only transfer new or changed files
*   delete files on destinations that do not exist in source
*   preserve source file modification times
*   verify file integrity after transfer (on by default)
*   encrypt transfer

!!! warning
    Note that enabling encryption significantly reduces transfer performance, so it should only be used for sensitive data.

### Personal computers

Globus provides a desktop client, [Globus Connect Personal](https://www.globus.org/globus-connect-personal), to make it easy to transfer files to and from a personal computer running Windows, MacOS X, or Linux.

There are links on the [Globus Connect Personal](https://www.globus.org/globus-connect-personal) page which walks you through the setup of Globus Connect Personal on the various operating systems, including setting it up from the command line on Linux. If you are running Globus Connect Personal from the command line on Linux, this [FAQ on the Globus site](https://docs.globus.org/faq/globus-connect-endpoints/#how_do_i_configure_accessible_directories_on_globus_connect_personal_for_linux) describes configuring which paths you share and their permissions.

#### To install Globus Connect Personal

Go to the [Alliance Globus portal](https://globus.alliancecan.ca/collections?scope=administered-by-me) and log in if you have not already done so.

1.  From the *File Manager* screen click on the *Collections* icon on the left.
2.  Click on *Get Globus Connect Personal* in the top right of the screen.
3.  Click on the download link for your operating system (click on *Show me other supported operating systems* if downloading for another computer).
4.  Install Globus Connect Personal.
5.  You should now be able to access the endpoint through Globus. The full endpoint name is \[your username\]#\[name you give setup\]; for example, smith#WorkPC.

#### To run Globus Connect Personal

The above steps are only needed once to set up the endpoint. To transfer files, make sure Globus Connect Personal is running, i.e., start the program, and ensure that the endpoint isn't paused.

Note that if the Globus Connect Personal program at your endpoint is closed during a file transfer to or from that endpoint, the transfer will stop. To restart the transfer, simply re-open the program.

#### Transfer between two personal endpoints

Although you can create endpoints for any number of personal computers, transfer between two personal endpoints is not enabled by default. If you need this capability, please contact [globus@tech.alliancecan.ca](mailto:globus@tech.alliancecan.ca) to set up a Globus Plus account.

For more information see the [Globus.org how-to pages](https://docs.globus.org/how-to/), particularly:
*   [Globus Connect Personal for Mac OS X](https://docs.globus.org/how-to/globus-connect-personal-mac)
*   [Globus Connect Personal for Windows](https://docs.globus.org/how-to/globus-connect-personal-windows)
*   [Globus Connect Personal for Linux](https://docs.globus.org/how-to/globus-connect-personal-linux)

## Globus sharing

Globus sharing makes collaboration with your colleagues easy. Sharing enables people to access files stored on your account on an Alliance cluster even if the other user does not have an account on that system. Files can be shared with any user, anywhere in the world, who has a Globus account. See [How To Share Data Using Globus](https://docs.globus.org/how-to/share-files/).

### Creating a shared collection

#### Step 1 - Prepare a directory to be shared

Verify in the table below that the system hosting your files has sharing enabled.

| System | Sharing enabled |
| :----- | :-------------- |
| [Trillium](trillium.md) | No. |
| [General-purpose clusters](national-systems.md#compute-clusters) | Yes, in: `/home` (except Rorqual). No, in: `/scratch` (except Narval). `/project`, on demand (see below). |

On [general-purpose clusters](national-systems.md#compute-clusters), Globus sharing is enabled for the `/home` directory, except on the Rorqual cluster. If you would like to test a Globus share you can create one in your `/home` directory.

By default, we disable sharing on `/project` to prevent users accidentally sharing other users' files. To enable sharing on `/project`, **the PI needs to contact [globus@tech.alliancecan.ca](mailto:globus@tech.alliancecan.ca) with**:

*   confirmation that Globus sharing should be enabled,
*   the name of the cluster,
*   the path to enable,
*   whether the sharing will be read only, or sharing if it can be read and write.

We suggest using a path that makes it clear to everyone that files in the directory might be shared such as:

`/project/my-project-id/Sharing`

Once we have enabled sharing on the path, you will be able to create a new Globus shared endpoint for any subdirectory under that path. So for example, you will be able to create the subdirectories:

`/project/my-project-id/Sharing/Subdir-01`

and

`/project/my-project-id/Sharing/Subdir-02`

Create a different Globus Share for each and share them with different users.

#### Step 2 - Prepare the data to be shared

If not done already, the data to be shared needs to be moved or copied to the chosen path. Creating a symbolic link to the data will not allow access to the data.

Otherwise you will receive the error:

!!! error "Error message"
    *The backend responded with an error: You do not have permission to create a shared endpoint on the selected path. The administrator of this endpoint has disabled creation of shared endpoints on the selected path.*

#### Step 3 - Configure a shared collection on Globus

Log into [the Alliance Globus portal](https://globus.alliancecan.ca) with your Globus credentials. Once you are logged in, you will see a transfer window. In the *endpoint* field, type the endpoint identifier for the endpoint you wish to share from (e.g. alliancecan#fir, computecanada#graham-globus, alliancecan#rorqual, alliancecan#trillium_home etc.) and activate the endpoint if asked to.

Select a folder that you wish to share, then click the *Share* button to the right of the folder list.

Click on the *Add Guest Collection* button in the top right corner of the screen.

Give the new share a name that is easy for you and the people you intend to share it with to find. You can also adjust from where you want to share using the *Browse* button.

### Managing access

Once the shared collection is created, you will be shown the current access list, with only your account on it. Since sharing is of little use without someone to share with, click on the *Add Permissions -- Share With* button to add people or groups that you wish to share with.

In the following form, the *Path* is relative to the share and because in many cases you simply want to share the whole collection, the path will be `/`. However, if you want to share only a subdirectory called "Subdir-01" with a specific group of people, you may specify `/Subdir-01/` or use the *Browse* button to select it.

Next in the form, you are prompted to select whether to share with people via email, username, or group.
*   *User* presents a search box that allows you to provide an email address or to search by name or by Globus username.
    *   Email is a good choice if you don’t know a person’s username on Globus. It will also allow you to share with people who do not currently have a Globus account, though they will need to create one to be able to access your share.
    *   This is best if someone already has a Globus account, as it does not require any action on their part to be added to the share. Enter a name or Globus username (if you know it), and select the appropriate match from the list, then click *Use Selected*.
*   *Group* allows you to share with a number of people simultaneously. You can search by group name or UUID. Group names may be ambiguous, so be sure to verify you are sharing with the correct one. This can be avoided by using the group’s UUID, which is available on the Groups page (see the section on groups)

To enable the write permissions, click on the *write* checkbox in the form. Note that it is not possible to remove read access. Once the form is completed, click on the *Add Permission* button. In the access list, it is also possible to add or remove the write permissions by clicking the checkbox next to the name under the *WRITE* column.

Deleting users or groups from the list of people you are sharing with is as simple as clicking the ‘x’ at the end of the line containing their information.

### Removing a shared collection

You can remove a shared collection once you no longer need it. To do this:

*   Click on *Collections* on the left side of the screen, then click on the [Shareable by You tab](https://globus.alliancecan.ca/collections?scope=shared-by-me), and finally click on the title of the *Shared Collection* you want to remove;
*   Click on the *Delete Collection* button on the right side of the screen;
*   Confirm deleting it by clicking on the red button.

The collection is now deleted. Your files will not be affected by this action, nor will those others may have uploaded.

### Sharing security

Sharing files entails a certain level of risk. By creating a share, you are opening up files that up to now have been in your exclusive control to others. The following list is some things to think about before sharing, though it is far from comprehensive.

*   If you are not the data’s owner, make sure you have permission to share the files.
*   Make sure you are sharing with only those you intend to. Verify the person you add to the access list is the person you think, there are often people with the same or similar names. Remember that Globus usernames are not linked to Alliance usernames. The recommended method of sharing is to use the email address of the person you wish to share with, unless you have the exact account name.
*   If you are sharing with a group you do not control, make sure you trust the owner of the group. They may add people who are not authorized to access your files.
*   If granting write access, make sure that you have backups of important files that are not on the shared endpoint, as users of the shared endpoint may delete or overwrite files, and do anything that you yourself can do to a file.
*   It is highly recommended that sharing be restricted to a subdirectory, rather than your top-level home directory.

## Globus groups
Globus groups provide an easy way to manage permissions for sharing with multiple users. When you create a group, you can use it from the sharing interface easily to control access for multiple users.

### Creating a group
Click on the [Groups button](https://globus.alliancecan.ca/groups) on the left sidebar. Click on the *Create New Group* button on the top right of the screen; this brings up the *Create New Group* window.
*   Enter the name of the group in the *Group Name* field
*   Enter the group description in the *Group Description* field
*   Select if the group is visible to only group members (private group) or all Globus users.
*   Click on *Create Group* to add the group.

### Inviting users
Once a group has been created, users can be added by selecting *Invite users*, and then either entering an email address (preferred) or searching for the username. Once users have been selected, click on the Add button and they will be sent an email inviting them to join. Once they’ve accepted, they will be visible in the group.

### Modifying membership
Click on a user to modify their membership. You can change their role and status. Role allows you to grant permissions to the user, including Admin (full access), Manager (change user roles), or Member (no management functions). The *Save Changes* button commits the changes.

## Command line interface (CLI)
### Installing
The Globus command line interface is a Python module which can be installed using pip. Below are the steps to install Globus CLI on one of our clusters.
1.  Create a virtual environment to install the Globus CLI into (see [creating and using a virtual environment](python.md#creating-and-using-a-virtual-environment)).
    ```bash
    $ virtualenv $HOME/.globus-cli-virtualenv
    ```
2.  Activate the virtual environment.
    ```bash
    $ source $HOME/.globus-cli-virtualenv/bin/activate
    ```
3.  Install Globus CLI into the virtual environment (see [installing modules](python.md#installing-modules)).
    ```bash
    $ pip install globus-cli
    ```
4.  Then deactivate the virtual environment.
    ```bash
    $ deactivate
    ```
5.  To avoid having to load that virtual environment every time before using Globus, you can add it to your path.
    ```bash
    $ export PATH=$PATH:$HOME/.globus-cli-virtualenv/bin
    $ echo 'export PATH=$PATH:$HOME/.globus-cli-virtualenv/bin'>>$HOME/.bashrc
    ```

### Using
*   See the Globus [Command Line Interface (CLI) documentation](https://docs.globus.org/cli/) to learn about using the CLI.
### Scripting
*   There is also a Python API, see the [Globus SDK for Python documentation](https://globus-sdk-python.readthedocs.io/en/stable/).

## Virtual machines (cloud VMs such as Arbutus, Fir, Nibi)
Globus endpoints exist for the cluster systems (Fir, Nibi, Rorqual, Trillium, etc.) but not for cloud VMs. The reason for this is that there isn't a singular storage for each VM so we can't create a single endpoint for everyone.

If you need a Globus endpoint on your VM and can't use another transfer mechanism, there are two options for installing an endpoint: Globus Connect Personal, and Globus Connect Server.

### Globus Connect Personal
Globus Connect Personal is easier to install, manage and get through the firewall but is designed to be installed on laptops / desktops.

*   [Install Globus Connect Personal on Windows](https://docs.globus.org/how-to/globus-connect-personal-windows/).
*   [Install Globus Connect Personal on Linux](https://docs.globus.org/how-to/globus-connect-personal-linux/).

### Globus Connect Server
Server is designed for headless (command line only, no GUI) installations and has some additional features you most probably would not use (such as the ability to add multiple servers to the endpoint). It does require opening some ports to allow transfers to occur (see [https://docs.globus.org/globus-connect-server/v5/#open-tcp-ports_section](https://docs.globus.org/globus-connect-server/v5/#open-tcp-ports_section)).

## Object storage on Arbutus

**Please note that these instructions now refer to accessing Legacy Arbutus Object Storage only.** Accessing the object storage requires a cloud project with object storage allocated. The steps below are only needed once.
To access the Arbutus object storage, generate the storage **access ID** and **secret key** with the [OpenStack command line client](openstack-command-line-clients.md).
1.  Import your credentials with `source <project name>-openrc.sh`.
2.  Create the storage access ID and secret key with `openstack ec2 credentials create`.
3.  Log into the [Globus portal](#using-globus) at [https://www.globus.org/](https://www.globus.org/).
4.  In the *File Manager* window, enter or select *Arbutus S3 buckets*.
5.  Click on *Continue* to provide consent to allow data access.
6.  Click on *Allow*.
7.  Click on *Continue*. In the *AWS IAM Access Key ID* field, enter the access code generated by `openstack ec2 credentials create` above, and in the *AWS IAM Secret Key* field, enter the secret.
8.  Click on *Continue* to complete the setup.

## Support and more information
If you would like more information on the Alliance’s use of Globus, or require support in using this service, please send an email to [globus@tech.alliancecan.ca](mailto:globus@tech.alliancecan.ca) and provide the following information:

*   Name
*   Compute Canada Role Identifier (CCRI)
*   Institution
*   Inquiry or issue. Be sure to indicate which sites you want to transfer to and from.