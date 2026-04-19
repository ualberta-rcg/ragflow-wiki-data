---
title: "Trillium Open OnDemand Quickstart"
slug: "trillium_open_ondemand_quickstart"
lang: "base"

source_wiki_title: "Trillium Open OnDemand Quickstart"
source_hash: "427f7899fe5b2afa80c0c6d89de89595"
last_synced: "2026-04-18T23:39:30.217451+00:00"
last_processed: "2026-04-19T01:08:47.336307+00:00"

tags:
  []

keywords:
  - "Image Quality"
  - "software stack"
  - "time limits"
  - "Interactive applications"
  - "core limit"
  - "Filter text box"
  - "job script"
  - "remote desktop environment"
  - "memory limit"
  - "Software modules"
  - "job monitoring"
  - "My Interactive Sessions"
  - "Slurm scheduler"
  - "Jupyter Notebook"
  - "Trillium"
  - "command terminal"
  - "operating system"
  - "Trillium Desktop"
  - "All Jobs"
  - "Open Composer"
  - "File management"
  - "MPI/OpenMP Slurm Job"
  - "job submission"
  - "Image Compression"
  - "Slurm job templates"
  - "Interactive Sessions"
  - "Job submission"
  - "History tab"
  - "myscinet portal"
  - "file management"
  - "Interactive sessions"
  - "hardware"
  - "job details"
  - "Trillium scheduler"
  - "Terminal access"
  - "VSCode"
  - "job status"
  - "Open OnDemand"

questions:
  - "How can users update their existing Python virtual environments to function correctly on the Trillium Open OnDemand site?"
  - "What is the maximum file size limit for direct uploads in the file browser, and what alternative method should be used for larger files?"
  - "How can users utilize the Open Composer application to submit and monitor batch jobs on the Trillium cluster?"
  - "What is the primary function of the Open Composer app and to which scheduler does it submit jobs?"
  - "How can users monitor the status of their submitted jobs within the application?"
  - "What are the different navigation methods users can use to access Open Composer?"
  - "How do you configure and submit a new job using the job parameters and extra fields in Open Composer?"
  - "What actions can you perform in the History tab to monitor, review, or resubmit previously submitted jobs?"
  - "How do you use the Active Jobs interface to filter, sort, and view detailed information about jobs currently in the queue?"
  - "How can users filter and sort the jobs displayed in the interface?"
  - "What specific information is revealed when clicking the \">\" symbol next to a job?"
  - "Where can users go to see all jobs in the queue or find a more comprehensive view of their jobs?"
  - "What parameters can be configured when submitting a job for an interactive application through Open OnDemand?"
  - "How can a user access the terminal of a running node or terminate an active interactive session?"
  - "How can a user run graphical user interface (GUI) software that is not natively supported as an installed interactive application?"
  - "How do you load required software modules and launch a graphical user interface (GUI) application, such as Octave, within the remote desktop environment?"
  - "What steps should you take to locate your session logs and Session ID when debugging errors or submitting a support ticket?"
  - "What are the key feature differences between the newly implemented Open OnDemand platform and the decommissioned JupyterHub system?"
  - "What steps are required to submit a job to the queue?"
  - "How can a user adjust the desktop session settings to improve performance based on their internet connection?"
  - "Which button must be clicked to open the remote desktop environment in a new tab?"
  - "What software applications and development environments are listed as supported in the text?"
  - "How do the two systems compare regarding job management, file management, and command terminal access?"
  - "What are the specific core limits and conditions for each of the compared environments?"
  - "What are the differences in hardware configurations and memory limits between the two systems?"
  - "How do the operating systems and supported software stacks compare across the two environments?"
  - "Which system provides monitoring features like error logs and alerts, and how is the enforcement of resource limits handled differently?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

This page is specifically for the Open OnDemand service attached to Trillium. General information on the Open OnDemand instances in the clusters of the Alliance can be found on [Open OnDemand](open_ondemand.md).

## Porting existing virtual environments to Open OnDemand

!!! warning "Important"
    Because of the change of operating system and software stack, your existing virtual environment kernels for Python may not work right away in the OnDemand site. You should be able to activate your Python environments in a Trillium terminal (see [Terminal access](#terminal-access)) below, with all required Trillium modules loaded, and then issue the command **`venv2jup`** to get them working correctly.

## Introduction

This guide will walk you through the basic steps to get started with the SciNet Open OnDemand portal.
Open OnDemand (OOD) is a web-based platform that provides access to a wide range of scientific applications and computing resources, such as JupyterLab, R Studio, and Visual Studio Code. It allows you to interact with Trillium through a web browser instead of via a terminal, without the need to install any software on your local machine. You will be able to perform file management, submit/monitor jobs and run applications interactively. More information on this project can be found at [https://openondemand.org](https://openondemand.org).

## Logging into the Open OnDemand portal

To access the Open OnDemand portal, open a web browser and navigate to the following page: https://ondemand.scinet.utoronto.ca. You will be prompted to enter your Alliance username and password, followed by a second factor authentication via Duo or Yubikey. Once you have logged in, you will be taken to the Open OnDemand dashboard. From here you can access the various tools and applications available on the platform.

## File management

The Open OnDemand platform provides a file browser that allows you to manage your files and directories on the filesystem. To access the file browser, click on the **Files** tab and select which directory you want to manage from the drop-down (`HOME`, `SCRATCH` or `PROJECT`). You will be taken to the file browser interface, where you can:

*   Navigate through your directories
*   Upload/download files
*   Create new files/directories
*   Delete files/directories
*   Edit existing files

Storage quotas can also be displayed by clicking on the **Storage Quotas** link in the **Files** tab.

### Uploading files

The current file size upload limit is 10GB. If you need to upload a file larger than this, or are facing upload issues due to a bad internet connection for example, please try using [Globus](https://docs.scinet.utoronto.ca/index.php/Globus). There is a Globus button in the file browser at the top right, which takes you to the Globus web interface where you can log in with your Alliance username and password. The path navigated to in the Open OnDemand file browser will be the same path opened in Globus.

## Job submission

Open OnDemand also provides a job submission interface that allows you to submit batch jobs to Trillium. This can be useful when you need more resources than the interactive jobs provide, i.e. exclusive access to 192 cores and 755GB of memory on a Trillium compute node.

The [Open Composer](https://github.com/RIKEN-RCCS/OpenComposer) app provides a suite of Slurm job template scripts that can be submitted directly to the Trillium scheduler. It also provides an interface to monitor your submitted jobs, via the **History** tab. You can access Open Composer by navigating to the **Jobs** drop-down menu and selecting **Open Composer** or by clicking on one of the Slurm job templates e.g. **MPI Slurm Job**, **OpenMP Slurm Job** and **Hybrid MPI/OpenMP Slurm Job**.

Once you have selected a job template, you will be taken to the job submission page. This is split between the job parameters on the left and the job script itself on the right. The job parameters let you control how many resources your job will use, such as the number of nodes, number of tasks per node, wall clock time and output file name. The job script section displays the script that will be submitted to the scheduler. Any changes made to the job parameters will be reflected in the job script automatically. You may also edit the job script directly if you wish.

The extra fields at the top of the page allow you to change how your job is submitted:

*   **Script Location**: specifies the directory where the job script will be saved and where your job will be run from.
*   **Script Name**: specifies the name of the job script file.
*   **Job Name**: specifies the name of the job that will appear in the job queue.
*   **Cluster**: allows you to change which cluster to submit your job to, e.g. Trillium (default) or Trillium-GPU. Selecting Trillium-GPU will provide an additional job parameter to request GPU resources.

Once you are happy with your job script, click on the **Submit** button to submit the job to the scheduler and save your script to the **Script Location**. If your job was submitted successfully, you will see a confirmation message at the top of the page with your job ID.

Note: The template scripts provided in Open Composer are basic examples to get you started. You will need to modify the job script further to suit your specific needs, such as loading your required modules and specifying input/output files. The job script still needs to conform to the limits set by the Trillium Slurm scheduler. Please refer to the Trillium [documentation](https://docs.alliancecan.ca/wiki/Trillium_Quickstart#trillium-specific-restrictions) for more information on how to write job scripts.

### Monitoring jobs in Open Composer

To monitor your submitted jobs in Open Composer, navigate to the **History** tab. This will display a list of all your submitted jobs, along with their status: Queued, Running, Completed, Failed. You can filter the jobs by using the **Filter** text box at the top right or by using the checkboxes below. Clicking on different column fields will give different information about the job:

*   **Job ID**: opens the job in [my.SciNet](https://my.scinet.utoronto.ca/), which displays performance statistics and more detailed Slurm information about the job. Note: my.SciNet may show *Not found or not permitted* if the job hasn't started yet or was cancelled.
*   **Application**: opens the job script editor of the template you used.
*   **Script Location**: opens an OOD file browser window at the location of the job script. Clicking on the small terminal icon will open a terminal in the job script location.
*   **Script Name**: displays the job script that was submitted to the scheduler.

To resubmit or modify a previously run job click on the job script under the **Script Name** column and click **Load Parameters**. This will take you back to the job submission page where further modifications can be made to the job.

### Supported applications

Open Composer currently supports the following applications for Slurm jobs:

*   [MPI](../software/mpi.md)
*   [OpenMP](../programming/openmp.md)
*   Hybrid MPI/OpenMP
*   [Python](../software/python.md)
*   [R](../software/r.md)
*   [VASP](../software/vasp.md)

## Job monitoring

To get an overview of all your jobs in the queue you can use the job monitoring interface. Navigate to the **Jobs** tab and select **Active Jobs**. You can filter the jobs by using the **Filter** text box at the top right. Columns can also be sorted by clicking on the column headers, for example you can sort by job status (running, completed, failed, etc.). Clicking on `>` to the left of a job will show you more details about the job, such as the start/end time, node list and account charged, etc. You might also want to show all jobs in the queue; you can do this by clicking on the drop-down menu at the top right and selecting **All Jobs**. A more detailed view of your jobs can still be found using the [myscinet portal](https://my.scinet.utoronto.ca).

## Interactive applications

Open OnDemand also features interactive applications that can be run directly from your web browser. To access the applications, navigate to the **Interactive Apps** tab and select the application you want to run from the drop-down. This will then bring you to the job submission page where you can choose job parameters such as:

*   Length of job in hours
*   Number of cores
*   Amount of memory to allocate (GB)
*   GPU resources (!!! note "Note"
        Only the **h100_1.10** [MIG](../programming/multi-instance_gpu.md) profile is currently available, which provides 10GB of memory and 1/8 of the compute power of a full NVIDIA H100 GPU.)
*   Notify me by email when the job starts

When you have chosen your job parameters click on the **Launch** button to submit your job to the queue. You will be taken to the **My Interactive Sessions** page where you can see the status of your job, i.e. queued, running or completed. Once the job has been assigned a node and is running, you can click on the **Connect to ...** button to launch the application. The application will open in a new tab in your browser, and you can interact with it as if it was running locally.

If you would like terminal access to the node where the application is running, to monitor the performance for example you can click on the button beside **Host** starting with `>_`. This will open a terminal window in your browser where you can run commands on the node directly.

If for whatever reason you would like to kill the job, you can do so by clicking on the red **Delete** button in the job panel in the **My Interactive Sessions** page.

### Installed applications

We currently support the following applications:

*   [JupyterLab/Notebook](https://jupyter.org)
*   [Rstudio](https://posit.co/products/open-source/rstudio/?sid=1)
*   [VSCode](https://code.visualstudio.com)
*   Trillium Desktop
*   [ParaView](https://www.paraview.org)
*   [Forge DDT/MAP](https://www.linaroforge.com)
*   [MATLAB](https://www.mathworks.com/products/matlab.html)
*   [SAS](https://www.sas.com/en_ca/home.html)[^4^]
*   [Stata](https://www.stata.com)[^4^]
*   [Open Composer](https://github.com/RIKEN-RCCS/OpenComposer)

If you would like an application installed please email us at [support@scinet.utoronto.ca](mailto:support@scinet.utoronto.ca).

## Running an application GUI

If you would like to run software that has a graphical user interface (GUI) and is not yet installed as an interactive application, such as Octave or Blender, you can do so using the **Trillium Desktop** application. This app provides a remote desktop environment that you can access through your web browser. In the following example, we will run Octave's GUI:

1.  Navigate to the **Interactive Apps** tab and select **Trillium Desktop** from the drop-down.
2.  You will be taken to the job submission page. Choose how many cores and amount of memory you would like to allocate for your session in addition to your job length in hours. Then click on the **Launch** button to submit your job to the queue.
3.  This will take you to the **My Interactive Sessions** page. Once your job is running, you have the option to improve the **Image Quality** and **Image Compression** of the desktop session. Depending on the speed of your internet connection, you may want to set these lower to improve performance and responsiveness of the desktop. Click on the **Connect to Trillium Desktop** button to launch the remote desktop environment in a new tab.
4.  Once the desktop environment has loaded, open a terminal window using the desktop shortcut and load the required modules for Octave:
    ```bash
    $ module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 octave/7.2.0
    ```
5.  Now launch Octave's GUI by typing `octave --gui` in the terminal window.

You should now see Octave's GUI appear in the remote desktop environment. You can use this method to run other GUI applications as well, just make sure to load the appropriate modules before launching the application. Applications may have different ways to launch their GUI, so please refer to the application's documentation for more information. You can see the list of binaries installed for a given application by looking at its environment variable, e.g. run `ls $EBROOTOCTAVE/bin` to see the list of Octave binaries.

## Terminal access

Sometimes you might prefer to use a terminal to interact with Trillium. Open OnDemand provides a web-based terminal that you can use to access the command-line interface. To access the terminal, navigate to the **Clusters** tab and select **Trillium Shell Access**. This will open a new tab in your browser with a terminal window where you can run commands as you would in a regular terminal session.

## Software modules

Trillium has a wide variety of software that can be accessed via modules. They can be loaded in your interactive sessions, terminal or job scripts in Open Composer. You can view the available modules and their versions using the **Module Browser** app, which can be accessed from the **Clusters** tab in the navigation bar. The module browser also provides a command that you can run in the terminal to load a particular module, which can be useful when writing job scripts for example.

## Debugging errors

If you encounter any errors while using an interactive Open OnDemand job, you can check the logs for more information. To access the logs, navigate to the **My Interactive Sessions** tab and find your active session. Click on the `output.log` link to open a separate tab which displays the output of your job. This file contains the standard output and error messages generated by the job, which can help you identify any issues that may have occurred during the session. When submitting a ticket to SciNet support ([support@scinet.utoronto.ca](mailto:support@scinet.utoronto.ca)), please include the `output.log` file, your **Session ID**, which is displayed as a long string of characters, e.g. `8feb45fa-bc65-4846-8398-2a73c1bf8e5a`, and any other relevant information to help us assist you more effectively.

## Differences compared to the JupyterHub

| Feature                    | JupyterHub (decommissioned)                                     | Open OnDemand                                                                                                                                                                                                                                                                                                |
|:---------------------------|:----------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Authentication*           | password                                                        | password + MFA                                                                                                                                                                                                                                                                                             |
| *First installed*          | 2017                                                            | 2025                                                                                                                                                                                                                                                                                                       |
| *Last update*              | 2021                                                            | 2025                                                                                                                                                                                                                                                                                                       |
| *Supports*                 | Jupyter Notebook, JupyterLab (R, Python, Julia)                 | Jupyter Notebook, JupyterLab (R, Python), Rstudio, VSCode, Desktop, SAS^4^, Stata^4^, ParaView, Forge DDT/MAP, MATLAB                                                                                                                                                                                          |
| *Start and continue later* | Yes                                                             | Yes[^1^]                                                                                                                                                                                                                                                                                                   |
| *Command terminal*         | No                                                              | Yes                                                                                                                                                                                                                                                                                                        |
| *File management*          | Yes (limited)                                                   | Yes                                                                                                                                                                                                                                                                                                        |
| *Monitor jobs*             | No                                                              | Yes                                                                                                                                                                                                                                                                                                        |
| *Submit jobs*              | No                                                              | Yes                                                                                                                                                                                                                                                                                                        |
| *Core limit*               | 8 cores[^2^]                                                    | 20 cores (8 for high memory)[^3^]                                                                                                                                                                                                                                                                          |
| *Memory limit*             | 48 GB[^2^]                                                      | 85 GB (500 GB for high memory)[^3^]                                                                                                                                                                                                                                                                        |
| *Time limits*              | 3 days[^2^]                                                     | 3 days[^3^]                                                                                                                                                                                                                                                                                                |
| *Operating system*         | CentOS 7                                                        | RockyLinux 9                                                                                                                                                                                                                                                                                               |
| *Software stack*           | NiaEnv, CCEnv                                                   | CCEnv                                                                                                                                                                                                                                                                                                      |
| *System issue alerts*      | No                                                              | Yes                                                                                                                                                                                                                                                                                                        |
| *User quota alerts*        | No                                                              | Yes                                                                                                                                                                                                                                                                                                        |
| *Error logs*               | No                                                              | Yes                                                                                                                                                                                                                                                                                                        |
| *Hardware*                 | 1 x CPU with 40 Intel "CascadeLake" cores at 2.5 GHz, 1TB RAM | 62 x CPU with 40 Intel "CascadeLake" cores at 2.5 GHz, 180GB RAM (default)<br>3 x CPU with 40 Intel "CascadeLake" cores at 2.5 GHz, 1TB RAM (high memory)<br>4 x NVIDIA H100 80GB GPUs, with 96-core AMD EPYC 9654 CPU at 2.4 GHz, 810GB RAM |

[^1^]: Within the requested limits.
[^2^]: Limits on JupyterHub were not implemented very strictly, so you could temporarily exceed these.
[^3^]: Limits need to be requested before starting an application.
[^4^]: Only for users with a license for these products.