---
title: "Transferring files with Aspera Connect/ascp"
slug: "transferring_files_with_aspera_connect_ascp"
lang: "base"

source_wiki_title: "Transferring files with Aspera Connect/ascp"
source_hash: "0a8639237526484d340452bb34ab0e8e"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:02:09.335441+00:00"

tags:
  []

keywords:
  - "data transfer"
  - "Linux"
  - "ascp"
  - "Aspera Connect"
  - "local installation"

questions:
  - "What is the primary purpose of the ascp software?"
  - "Why might a user encounter an authentication error when using older versions of ascp like 3.5.4?"
  - "What are the steps required to locally install the updated Aspera Connect software on a Linux system?"
  - "What is the primary purpose of the ascp software?"
  - "Why might a user encounter an authentication error when using older versions of ascp like 3.5.4?"
  - "What are the steps required to locally install the updated Aspera Connect software on a Linux system?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

ascp is a software used for transferring data to and from Aspera transfer servers where you have license credentials. A common use case is uploading a dataset to a data repository.

Many transfer servers will require an up-to-date version of the software (now called Aspera Connect). Due to changes in the software, you may need to install this updated version locally. Please see below for details.

## ascp 3.5.4

This software is available as a module in older software stacks.

If the server you are trying to transfer data to is incompatible with this older version, you may get an error such as:

!!! warning
    ```text
    Error with Aspera:

    ascp: failed to authenticate, exiting.

    Session Stop  (Error: failed to authenticate)
    ```

## Aspera Connect/ascp 4+

In order to use Aspera Connect (formerly ascp) you will need to [install it in one of your local directories](../getting-started/installing_software_in_your_home_directory.md).

1.  Copy the link for the latest Linux version of the software from the [Aspera Connect website](https://www.ibm.com/aspera/connect).
2.  Go to the directory where you want to install the software, e.g. your `/home` directory.
3.  Download the software in this directory with `wget`.
    ```bash
    wget link-i-copied-here
    ```
4.  Extract the software from the archive.
    ```bash
    tar -zxf ibm-aspera-connect_some_version_linux.tar.gz
    ```
5.  Run the setup script.
    ```bash
    bash ibm-aspera-connect_some_version_linux.sh
    ```
    a. Make the library files executable:
    ```bash
    chmod u+x ~/.aspera/connect/plugins/*/*.so ~/.aspera/connect/lib/*
    ```
6.  Run the setrpaths script.
    ```bash
    setrpaths.sh --path $HOME/.aspera
    ```
7.  (Optional) add the `ascp` binaries to your PATH:
    !!! tip
        ```bash
        export PATH=~/.aspera/connect/bin:$PATH