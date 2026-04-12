---
title: "Globus Command Line Interface"
slug: "globus_command_line_interface"
lang: "base"

source_wiki_title: "Globus Command Line Interface"
source_hash: "fd2eaf2a84062a19ede2778d9a530a2f"
last_synced: "2026-04-12T21:18:48.865179+00:00"
last_processed: "2026-04-12T21:23:39.877570+00:00"

tags:
  []

keywords:
  - "Draft"

questions:
  - "What is the primary purpose and core message of this draft?"
  - "Who is the target audience, and how does the draft address their needs?"
  - "What specific changes, additions, or feedback are needed to finalize this document?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: true
---

## Globus Command Line Interface

The Globus Command Line Interface (CLI) is an alternative to the Globus web interface or Globus Connect Personal application for managing your Globus files and transfers.

The CLI is useful for:
* Automating transfers with scripts
* Interacting with Globus in a programmatic way
* Managing files and folders without a graphical user interface (GUI)

!!! note "Note"
    This documentation assumes that you have already installed the Globus CLI and authenticated to your Globus account. If you have not, please see the Globus [Web Interface](https://docs.alliancecan.ca/wiki/Globus_Web_Interface) documentation.

## Setup

Before you can use the Globus CLI, you must first authenticate to Globus. The first time you use the CLI, a Uniform Resource Locator (URL) will be presented to you that you must visit to get an authorization code. Subsequent uses will not require this step unless your authentication token expires.

```bash
globus login
```

When you run the command, a message similar to the following will be displayed:

```text title="Globus CLI login prompt"
Please authenticate with Globus here:
https://auth.globus.org/v2/oauth2/authorize?client_id=...
...
Enter the authorization code here:
```

## Globus Endpoints

Globus Endpoints are the locations where your data resides. These can be servers, clusters, or even your personal computer. When using the Globus CLI, you will need to know the endpoint ID or name of the endpoints you wish to interact with.

### Listing Endpoints

To list all endpoints you have access to, use the `globus endpoint search` command:

```bash
globus endpoint search
```

This command will return a list of all endpoints you have access to, along with their IDs and names. You can filter the results by adding a search term:

```bash
globus endpoint search "University of Alberta"
```

You can also get more details about an endpoint using the `globus endpoint show` command and the endpoint ID. For example, to show details about the University of Alberta Globus endpoint, you would use:

```bash
globus endpoint show 93c9d747-d510-11e7-8b94-22000a92ce73
```

## Transferring Files

The most common use of Globus is to transfer files between endpoints. The `globus transfer` command is used for this purpose.

### Initiating a Transfer

To initiate a transfer, you need to specify the source endpoint, destination endpoint, and the paths to the files or folders you want to transfer. The basic syntax is:

```bash
globus transfer <source_endpoint_id>:<source_path> <destination_endpoint_id>:<destination_path>
```

For example, to transfer a file named `my_data.txt` from your local machine (using Globus Connect Personal) to the University of Alberta Globus endpoint, you would use:

First, find your Globus Connect Personal endpoint ID by running:

```bash
globus endpoint search <your_username>
```

Then, initiate the transfer:

```bash
globus transfer <your_connect_personal_id>:/path/to/my_data.txt 93c9d747-d510-11e7-8b94-22000a92ce73:/path/to/destination/my_data.txt
```

This command will return a task ID. You can use this ID to monitor the transfer's progress.

### Monitoring Transfers

To monitor the status of a transfer, use the `globus task show` command followed by the task ID:

```bash
globus task show <task_id>
```

To list all your active and completed tasks, use:

```bash
globus task list
```

### Transfer Options

The `globus transfer` command has several useful options:
* `--recursive`: Transfer directories recursively.
* `--sync-level`: Synchronize files based on modification time, size, or checksum. Options are `mtime`, `size`, `checksum`, `delete` (deletes files at destination that don't exist at source), and `none`.
* `--label`: Add a label to the transfer task for easier identification.
* `--verify-checksum`: Verify file integrity using checksums after transfer.

For a complete list of options, see the Globus CLI documentation or use `globus transfer --help`.

## Managing Files and Directories

The Globus CLI allows you to manage files and directories on your endpoints. These commands are similar to standard Unix commands.

### Listing Contents (ls)

To list the contents of a directory on an endpoint, use the `globus ls` command:

```bash
globus ls <endpoint_id>:<path>
```

For example:

```bash
globus ls 93c9d747-d510-11e7-8b94-22000a92ce73:/home/user
```

### Creating Directories (mkdir)

To create a new directory on an endpoint, use the `globus mkdir` command:

```bash
globus mkdir <endpoint_id>:<path>
```

For example:

```bash
globus mkdir 93c9d747-d510-11e7-8b94-22000a92ce73:/home/user/new_project
```

### Deleting Files and Directories (rm)

To delete files or directories on an endpoint, use the `globus rm` command.

!!! warning "Note"
    Deleting files is permanent and cannot be undone. Use with caution.

```bash
globus rm <endpoint_id>:<path>
```

To delete a directory and its contents recursively, use the `--recursive` option:

```bash
globus rm --recursive 93c9d747-d510-11e7-8b94-22000a92ce73:/home/user/old_data
```

## Other Useful Commands

* `globus whoami`: Display information about the currently authenticated user.
* `globus logout`: Log out of the Globus CLI and revoke your authentication token.
* `globus version`: Display the version of the Globus CLI.