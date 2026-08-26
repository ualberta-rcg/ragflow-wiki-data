---
title: "Open OnDemand/en"
slug: "open_ondemand"
lang: "en"

source_wiki_title: "Open OnDemand/en"
source_hash: "73083ae3a7733dfdbde743da1453a816"
last_synced: "2026-08-26T10:16:11.334907+00:00"
last_processed: "2026-08-26T11:15:16.955884+00:00"

tags:
  []

keywords:
  - "column headers"
  - "file browser"
  - "web-based terminal"
  - "job status"
  - "My Interactive Sessions"
  - "Open OnDemand"
  - "job submission"
  - "Interactive Apps"
  - "All Jobs"
  - "Globus"
  - "Filter text box"
  - "drop-down menu"
  - "job monitoring"

questions:
  - "What steps are required to log into the Open OnDemand portal and what authentication methods are used?"
  - "How can users manage files and upload large files (over 10 GB) using the Open OnDemand interface?"
  - "What features does the Open OnDemand job submission and monitoring system provide for creating, submitting, and tracking batch jobs?"
  - "How do you submit and configure an interactive application job using Open OnDemand?"
  - "What steps are required to access a terminal on the node where an interactive job is running, and how can you terminate the job if needed?"
  - "Where can you find error logs for a failed interactive session, and what information should be included when reporting the issue to SciNet support?"
  - "How can you filter the jobs using the interface?"
  - "What steps allow you to sort the job columns, and which job attributes can be sorted?"
  - "How do you expand a job to see its details and display all jobs in the queue?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Introduction

This guide will walk you through the basic steps to get started with Open OnDemand (OOD) on our systems. Open OnDemand is a web-based platform that provides access to a wide range of scientific applications and computing resources, such as Jupyter Lab, R Studio, and VS Code. It allows you to interact with a cluster through a web browser instead of via a terminal, without the need to install any software on your local machine. You will be able to perform file management, submit/monitor jobs and run applications interactively. More information on this project can be found at [https://openondemand.org](https://openondemand.org). For cluster specific documentation please see:

*   [Trillium Open OnDemand Quickstart](trillium_open_ondemand_quickstart.md)
*   [Nibi Open OnDemand Quickstart](../clusters/nibi.md#access-through-open-ondemand-ood)

## Logging into the Open OnDemand portal

To access the Open OnDemand portal, open a web browser and navigate to the OnDemand instance you would like to access, e.g. [Trillium](https://ondemand.scinet.utoronto.ca), [Vulcan](../clusters/vulcan.md), [Nibi](https://ondemand.sharcnet.ca). You will be prompted to enter your Alliance username and password, followed by a second factor authentication via Duo or Yubikey. Once you have logged in, you will be taken to the Open OnDemand dashboard. From here you can access the various tools and applications available on the platform.

## File management

The Open OnDemand platform provides a file browser that allows you to manage your files and directories on the filesystem. To access the file browser, click on the **Files** tab and select which directory you want to manage from the drop-down (`HOME`, `SCRATCH` or `PROJECT`). You will be taken to the file browser interface, where you can:

*   Navigate through your directories
*   Upload/download files
*   Create new files/directories
*   Delete files/directories
*   Edit existing files

### Uploading files

!!! tip "Large File Uploads"
    The current file size upload limit is 10GB; if you need to upload a file larger than this or are facing upload issues due to a bad internet connection for example, please try using [Globus](../getting-started/globus.md).

There is a Globus button in the file browser at the top right, which will take you to the Globus web interface where you can log in with your Alliance username and password. The path navigated to in the Open OnDemand file browser will be the same path opened in Globus.

## Job submission

Open OnDemand also provides a job submission interface that allows you to submit batch jobs. Navigate to the **Jobs** tab and select **Job Composer**; this will take you to the job submission form. From here click on the **New Job** button which will offer you the following options:

*   **From Default Template** - allows you to create a job from scratch
*   **From Template** - allows you to select from some example jobs, e.g. MPI and OpenMP
*   **From Specified Path** - allows you to use an existing job that you already have on the file system
*   **From Selected Job** - copies the current job for you.

You can specify job parameters such as the job script and account name using the **Job Options** button. The remaining parameters such as the number of nodes, number of cores, wall clock time, etc. can be modified by editing the job script directly with the **Open Editor** button. Once you have filled in the required fields, click on the **Submit** button to submit the job.

The page also shows the status of your job so you can see whether it is queued, running or completed. You can also view the output and error logs of the job once it is finished by clicking on the relevant files under the **Folder Contents** section of the **Job Details** panel to the right.

## Job monitoring

To get an overview of all your jobs in the queue you can use the job monitoring interface. Navigate to the **Jobs** tab and select **Active Jobs**. You can filter the jobs by using the **Filter** text box at the top right. Columns can also be sorted by clicking on the column headers, for example you can sort by job status (running, completed, failed, etc.). Clicking on `>` to the left of a job will show you more details about the job, such as the start/end time, node list and account charged etc. You might also want to show all jobs in the queue; you can do this by clicking on the drop-down menu at the top right and selecting **All Jobs**.

## Interactive Applications

Open OnDemand also features interactive applications that can be run directly from your web browser. To access the applications, navigate to the **Interactive Apps** tab and select the application you want to run from the drop-down. This will then bring you to the job submission page where you can choose job parameters such as:

*   Length of job in hours
*   Number of cores
*   Amount of memory to allocate (GB)
*   Notify me by email when the job starts

When you have chosen your job parameters click on the **Launch** button to submit your job to the queue. You will be taken to the **My Interactive Sessions** page where you can see the status of your job, i.e. queued, running or completed. Once the job has been assigned a node and is running, you can click on the **Connect to ...** button to launch the application. The application will open in a new tab in your browser, and you can interact with it as if it was running locally.

If you would like terminal access to the node where the application is running, to monitor the performance for example, you can click on the button beside **Host** starting with `>_`. This will open a terminal window in your browser where you can run commands on the node directly.

If for whatever reason you would like to kill the job, you can do so by clicking on the red **Cancel** button in the job panel in the **My Interactive Sessions** page.

## Terminal Access

If you prefer to use a terminal to interact with the cluster, Open OnDemand provides a web-based terminal to access the command line interface. To access the terminal, navigate to the **Clusters** tab and select **Cluster_Name Shell Access**. This will open a new tab in your browser with a terminal window where you can run commands as you would in a terminal application.

## Debugging Errors

If you encounter any errors while using an interactive Open OnDemand job, you can check the logs for more information. To access the logs, navigate to the **My Interactive Sessions** tab and find your active session. Click on the `output.log` link to open a separate tab which displays the output of your job. This file contains the standard output and error messages generated by the job, which can help you identify any issues that may have occurred during the session.

!!! note "Support Ticket Information"
    When submitting a ticket to SciNet support, please include the `output.log` file, your **Session ID**, which is displayed as a long string of characters, e.g. `8feb45fa-bc65-4846-8398-2a73c1bf8e5a`, and any other relevant information to help us assist you more effectively.