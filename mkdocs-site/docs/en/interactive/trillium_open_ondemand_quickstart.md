---
title: "Trillium Open OnDemand Quickstart/en"
slug: "trillium_open_ondemand_quickstart"
lang: "en"

source_wiki_title: "Trillium Open OnDemand Quickstart/en"
source_hash: "5c7cc71960ee39cb0b1b46c5314440a6"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:07:18.138033+00:00"

tags:
  []

keywords:
  - "core limit"
  - "Image Quality"
  - "job submission"
  - "hardware"
  - "node list"
  - "Open Composer"
  - "RAM"
  - "History tab"
  - "Open OnDemand"
  - "Terminal access"
  - "Slurm scheduler"
  - "Software modules"
  - "File management"
  - "myscinet portal"
  - "remote desktop environment"
  - "All Jobs"
  - "operating system"
  - "Image Compression"
  - "Trillium scheduler"
  - "column headers"
  - "Interactive sessions"
  - "CPU"
  - "Trillium"
  - "Octave"
  - "user quota alerts"
  - "Interactive applications"
  - "software stack"
  - "Slurm job templates"
  - "monitor submitted jobs"
  - "submit jobs"
  - "job monitoring"
  - "JupyterHub"
  - "Trillium Desktop"
  - "job status"
  - "memory limit"
  - "Job submission"
  - "job script"

questions:
  - "How can users fix their existing Python virtual environments to work correctly on the Trillium Open OnDemand site?"
  - "What is the file size limit for direct uploads in the file browser, and what alternative tool is recommended for transferring larger files?"
  - "How does the Open Composer application assist users in submitting and monitoring batch jobs on the Trillium cluster?"
  - "What scheduler does Open Composer submit jobs to directly?"
  - "How can users monitor their submitted jobs within the Open Composer interface?"
  - "What are the different navigation methods and templates used to access Open Composer?"
  - "How do the job parameters and extra fields on the job submission page interact to configure and submit a job script?"
  - "What steps are required to monitor, modify, and resubmit previously submitted jobs using the History tab in Open Composer?"
  - "How can users utilize the Active Jobs interface to filter, sort, and view detailed information about their queued jobs?"
  - "How can you sort the columns to organize jobs by their current status?"
  - "What specific information is revealed when clicking the `>` symbol next to an individual job?"
  - "Where can users go to access a more detailed and comprehensive view of their jobs?"
  - "What parameters can a user configure when submitting an interactive application job through Open OnDemand?"
  - "How can a user monitor, connect to, access the terminal for, or terminate an interactive session once it has been launched?"
  - "What steps should a user follow to run a graphical user interface (GUI) application that is not natively listed in the supported applications menu?"
  - "How can users access the web-based terminal in Open OnDemand to run commands and launch GUI applications like Octave?"
  - "What steps should a user take to locate error logs for an interactive session, and what specific information is required when submitting a support ticket?"
  - "What are the key feature differences, such as resource limits and supported software, between Open OnDemand and the decommissioned Jupyter Hub?"
  - "How do internet connection speeds affect the recommended settings for Image Quality and Image Compression in the desktop session?"
  - "What steps are required to launch the Trillium remote desktop environment?"
  - "Which specific modules need to be loaded in the terminal window to run Octave?"
  - "What are the differences in core and memory limits between the two computing environments?"
  - "How do the operating systems and supported software stacks compare across the two systems?"
  - "Which of the two configurations supports job submissions and provides system issue alerts?"
  - "What are the specific hardware differences, including CPU, RAM, and GPU configurations, between the two systems being compared?"
  - "Which of the two environments provides administrative features such as user quota alerts and error logs?"
  - "How do the systems manage resource limits, JupyterHub constraints, and software licensing requirements according to the provided footnotes?"
  - "What are the specific hardware differences, including CPU, RAM, and GPU configurations, between the two systems being compared?"
  - "Which of the two environments provides administrative features such as user quota alerts and error logs?"
  - "How do the systems manage resource limits, JupyterHub constraints, and software licensing requirements according to the provided footnotes?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

This page is specifically for the Open OnDemand service attached to Trillium. General information on the Open OnDemand instances in the clusters of the Alliance can be found on [Open OnDemand](open-ondemand.md).

## Porting existing virtual environments to Open OnDemand

!!! warning "Important"
    Because of the change of operating system and software stack, your existing virtual environment kernels for Python may not work right away in the OnDemand site. You should be able to activate your Python environments in a Trillium terminal (see [Terminal access](#terminal-access)) below, with all required Trillium modules loaded, and then issue the command **`venv2jup`** to get them working correctly.

## Introduction

This guide will walk you through the basic steps to get started with the SciNet Open OnDemand portal.
Open OnDemand (OOD) is a web-based platform that provides access to a wide range of scientific applications and computing resources, such as Jupyter Lab, R Studio, and Visual Studio Code. It allows you to interact with Trillium through a web browser instead of via a terminal, without the need to install any software on your local machine. You will be able to perform file management, submit/monitor jobs and run applications interactively. More information on this project can be found at [https://openondemand.org](https://openondemand.org).

## Logging into the Open OnDemand portal

To access the Open OnDemand portal, open a web browser and navigate to the following page: https://ondemand.scinet.utoronto.ca. You will be prompted to enter your Alliance username and password, followed by a second factor authentication via Duo or Yubikey. Once you have logged in, you will be taken to the Open OnDemand dashboard. From here you can access the various tools and applications available on the platform.

## File management

The Open OnDemand platform provides a file browser that allows you to manage your files and directories on the filesystem. To access the file browser, click on the **Files** tab and select which directory you want to manage from the drop-down (``HOME``, ``SCRATCH`` or ``PROJECT``). You will be taken to the file browser interface, where you can:

*   Navigate through your directories
*   Upload/download files
*   Create new files/directories
*   Delete files/directories
*   Edit existing files

Storage quotas can also be displayed by clicking on the **Storage Quotas** link in the **Files** tab.

### Uploading files

The current file size upload limit is 10GB, if you need to upload a file larger than this or are facing upload issues due to a bad internet connection for example please try using [Globus](https://docs.scinet.utoronto.ca/index.php/Globus). There is a Globus button in the file browser at the top right, which will take you to the Globus web interface where you can log in with your Alliance username and password. The path navigated to in the Open OnDemand file browser will be the same path opened in Globus.

## Job submission

Open OnDemand also provides a job submission interface that allows you to submit batch jobs to Trillium. This can be useful when you need more resources than the interactive jobs provide, i.e. exclusive access to 192 cores and 755GB of memory on a Trillium compute node.

The [Open Composer](https://github.com/RIKEN-RCCS/OpenComposer) app provides a suite of Slurm job template scripts that can be submitted directly to the Trillium scheduler. It also provides an interface to monitor your submitted jobs, via the **History** tab. You can access Open Composer by navigating to the **Jobs** drop-down menu and selecting **Open Composer** or by clicking on one of the Slurm job templates e.g. **MPI Slurm Job**, **OpenMP Slurm Job** and **Hybrid MPI/OpenMP Slurm Job**.

Once you have selected a job template, you will be taken to the job submission page. This is split between the job parameters on the left and the job script itself on the right. The job parameters let you control how many resources your job will use, such as the number of nodes, number of tasks per node, wall clock time and output file name. The job script section displays the script that will be submitted to the scheduler. Any changes made to the job parameters will be reflected in the job script automatically. You may also edit the job script directly if you wish.

The extra fields at the top of the page allow you to change how your job is submitted:

*   **Script Location**: specifies the directory where the job script will be saved and where your job will be run from.
*   **Script Name**: specifies the name of the job script file.
*   **Job Name**: specifies the name of the job that will appear in the job queue.
*   **Cluster**: allows you to change which cluster to submit your job to, e.g. Trillium (default) or **Trillium-GPU**. Selecting **Trillium-GPU** will provide an additional job parameter to request GPU resources.

Once you are happy with your job script, click on the **Submit** button to submit the job to the scheduler and save your script to the **Script Location**. If your job was submitted successfully, you will see a confirmation message at the top of the page with your job ID.

Note: The template scripts provided in Open Composer are basic examples to get you started. You will need to modify the job script further to suit your specific needs, such as loading your required modules and specifying input/output files. The job script still needs to conform to the limits set by the Trillium Slurm scheduler. Please refer to the Trillium [documentation](https://docs.alliancecan.ca/wiki/Trillium_Quickstart#trillium-specific-restrictions) for more information on how to write job scripts.

### Monitoring jobs in Open Composer

To monitor your submitted jobs in Open Composer, navigate to the **History** tab. This will display a list of all your submitted jobs, along with their status: Queued, Running, Completed, Failed. You can filter the jobs by using the **Filter** text box at the top right or by using the checkboxes below. Clicking on different column fields will give different information about the job:

*   **Job ID**: opens the job in [my.SciNet](https://my.scinet.utoronto.ca/), which displays performance statistics and more detailed Slurm information about the job. Note: my.SciNet may show 'Not found or not permitted' if the job hasn't started yet or was cancelled.
*   **Application**: opens the job script editor of the template you used.
*   **Script Location**: opens an OOD file browser window at the location of the job script. Clicking on the small terminal icon will open a terminal in the job script location.
*   **Script Name**: displays the job script that was submitted to the scheduler.

To resubmit or modify a previously run job click on the job script under the **Script Name** column and click **Load Parameters**. This will take you back to the job submission page where further modifications can be made to the job.

### Supported applications

Open Composer currently supports the following applications:

*   **MPI Slurm Job**
*   **OpenMP Slurm Job**
*   **Hybrid MPI/OpenMP Slurm Job**
*   **Python Slurm Job**
*   **R Slurm Job**
*   **VASP Slurm Job**

## Job monitoring

To get an overview of all your jobs in the queue you can use the job monitoring interface. Navigate to the **Jobs** tab and select **Active Jobs**. You can filter the jobs by using the **Filter** text box at the top right. Columns can also be sorted by clicking on the column headers, for example you can sort by job status (running, completed, failed, etc.). Clicking on `>` to the left of a job will show you more details about the job, such as the start/end time, node list and account charged etc. You might also want to show all jobs in the queue, you can do this by clicking on the drop-down menu at the top right and selecting **All Jobs**. A more detailed view of your jobs can still be found using the [myscinet portal](https://my.scinet.utoronto.ca).

## Interactive applications

Open OnDemand also features interactive applications that can be run directly from your web browser. To access the applications, navigate to the **Interactive Apps** tab and select the application you want to run from the drop-down. This will then bring you to the job submission page where you can choose job parameters such as:

*   Length of job in hours
*   Number of cores
*   Amount of memory to allocate (GB)
*   GPU resources (**Note**: only the **h100_1.10** [MIG](https://docs.alliancecan.ca/wiki/Multi-Instance_GPU) profile is currently available, which provides 10GB of memory and 1/8 of the compute resources of a full NVIDIA H100 GPU.)
*   Notify me by email when the job starts

When you have chosen your job parameters click on the **Launch** button to submit your job to the queue. You will be taken to the **My Interactive Sessions** page where you can see the status of your job, i.e. queued, running or completed. Once the job has been assigned a node and is running, you can click on the **Connect to ...** button to launch the application. The application will open in a new tab in your browser, and you can interact with it as if it was running locally.

If you would like terminal access to the node where the application is running, to monitor the performance for example you can click on the button beside **Host** starting with ``>_``. This will open a terminal window in your browser where you can run commands on the node directly.

If for whatever reason you would like to kill the job, you can do so by clicking on the red **Delete** button in the job panel in the **My Interactive Sessions** page.

### Installed applications

We currently support the following applications:

*   [Jupyter Lab/Notebook](https://jupyter.org)
*   [Rstudio](https://posit.co/products/open-source/rstudio/?sid=1)
*   [VSCode](https://code.visualstudio.com)
*   Trillium Desktop
*   [ParaView](https://www.paraview.org)
*   [Forge DDT/MAP](https://www.linaroforge.com)
*   [MATLAB](https://www.mathworks.com/products/matlab.html)
*   [SAS](https://www.sas.com/en_ca/home.html)<sup>4</sup>
*   [Stata](https://www.stata.com)<sup>4</sup>
*   [Open Composer](https://github.com/RIKEN-RCCS/OpenComposer)

If you would like an application installed please email us at: [support@scinet.utoronto.ca](mailto:support@scinet.utoronto.ca).

## Running an application GUI

If you would like to run software that has a graphical user interface (GUI) and is not yet installed as an interactive application, such as Octave or Blender, you can do so using the **Trillium Desktop** application. This app provides a remote desktop environment that you can access through your web browser. In the following example, we will run Octave's GUI:

1.  Navigate to the **Interactive Apps** tab and select **Trillium Desktop** from the drop-down.
2.  You will be taken to the job submission page. Choose how many cores and amount of memory you would like to allocate for your session in addition to your job length in hours. Then click on the **Launch** button to submit your job to the queue.
3.  This will take you to the **My Interactive Sessions** page. Once your job is running, you have the option to improve the **Image Quality** and **Image Compression** of the desktop session. Depending on the speed of your internet connection, you may want to set these lower to improve performance and responsiveness of the desktop. Click on the **Connect to Trillium Desktop** button to launch the remote desktop environment in a new tab.
4.  Once the desktop environment has loaded, open a terminal window using the desktop shortcut and load the required modules for Octave:
    ```bash
    module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 octave/7.2.0
    ```
5.  Now launch Octave's GUI by typing ``octave --gui`` in the terminal window.

You should now see Octave's GUI appear in the remote desktop environment. You can use this method to run other GUI applications as well, just make sure to load the appropriate modules before launching the application. Applications may have different ways to launch their GUI, so please refer to the application's documentation for more information. You can see the list of binaries installed for a given application by looking at its environment variable, e.g. run ``ls $EBROOTOCTAVE/bin`` to see the list of Octave binaries.

## Terminal access

Sometimes you might prefer to use a terminal to interact with Trillium, Open OnDemand provides a web-based terminal that you can use to access the command-line interface. To access the terminal, navigate to the **Clusters** tab and select **Trillium Shell Access**. This will open a new tab in your browser with a terminal window where you can run commands as you would in a regular terminal session.

## Software modules
Trillium has a wide variety of software that can be accessed via modules. They can be loaded in your interactive sessions, terminal or job scripts in Open Composer. You can view the available modules and their versions using the **Module Browser** app, which can be accessed from the **Clusters** tab in the navigation bar. The module browser also provides a command that you can run in the terminal to load a particular module, which can be useful when writing job scripts for example.

## Debugging errors

If you encounter any errors while using an interactive Open OnDemand job, you can check the logs for more information. To access the logs, navigate to the **My Interactive Sessions** tab and find your active session. Click on the ``output.log`` link (see Figure. 13) to open a separate tab which displays the output of your job. This file contains the standard output and error messages generated by the job, which can help you identify any issues that may have occurred during the session. When submitting a ticket to SciNet support, please include the ``output.log`` file, your **Session ID**, which is displayed as a long string of characters, e.g. **8feb45fa-bc65-4846-8398-2a73c1bf8e5a**, and any other relevant information to help us assist you more effectively.

## Differences compared to the Jupyter Hub

| feature | Jupyter Hub (decommissioned) | Open OnDemand |
| :------ | :--------------------------- | :------------ |
| *authentication* | password | password + MFA |
| *first installed* | 2017 | 2025 |
| *last update* | 2021 | 2025 |
| *supports* | Jupyter Notebook, JupyterLab (R, Python, Julia) | Jupyter Notebook, JupyterLab (R, Python), Rstudio, VSCode, Desktop, SAS<sup>4</sup>, Stata<sup>4</sup>, ParaView, Forge DDT/MAP, MATLAB |
| *start and continue later* | Yes | Yes<sup>1</sup> |
| *command terminal* | No | Yes |
| *file management* | Yes (limited) | Yes |
| *monitor jobs* | No | Yes |
| *submit jobs* | No | Yes |
| *core limit* | 8 cores<sup>2</sup> | 20 cores (8 for high memory)<sup>3</sup> |
| *memory limit* | 48 GB<sup>2</sup> | 85 GB (500 GB for high memory)<sup>3</sup> |
| *time limits* | 3 days<sup>2</sup> | 3 days<sup>3</sup> |
| *operating system* | CentOS 7 | RockyLinux 9 |
| *software stack* | NiaEnv, CCEnv | CCEnv |
| *system issue alerts* | No | Yes |
| *user quota alerts* | No | Yes |
| *error logs* | No | Yes |
| *hardware* | 1 x CPU with 40 Intel "CascadeLake" cores at 2.5 GHz, 1TB RAM | 62 x CPU with 40 Intel "CascadeLake" cores at 2.5 GHz, 180GB RAM (default)<br>3 x CPU with 40 Intel "CascadeLake" cores at 2.5 GHz, 1TB RAM (high memory)<br>4 x NVIDIA H100 80GB GPUs, with 96-core AMD EPYC 9654 CPU at 2.4 GHz, 810GB RAM |

<sup>1</sup> Within the requested limits.

<sup>2</sup> Limits on JupyterHub were not implemented very strictly, so you could temporarily exceed these.

<sup>3</sup> Limits need to be requested before starting an application.

<sup>4</sup> Only for users with a license for these products.