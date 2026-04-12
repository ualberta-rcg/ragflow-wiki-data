---
title: "Windows Subsystem for Linux (WSL)/en"
slug: "windows_subsystem_for_linux__wsl"
lang: "en"

source_wiki_title: "Windows Subsystem for Linux (WSL)/en"
source_hash: "3204d5bc9fce0f23768fe4a33230cdf5"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T13:37:19.040033+00:00"

tags:
  []

keywords:
  - "WSL"
  - "Windows Subsystem for Linux"
  - "Linux files"
  - "full path"
  - "forward slashes"
  - "/mnt/"
  - "File access"
  - "Ubuntu"
  - "FileZilla"
  - "Transferring data"
  - "Linux environment"
  - "Windows Explorer"

questions:
  - "What is the Windows Subsystem for Linux (WSL) and what are its primary benefits for Windows users?"
  - "What are the steps required to install and perform the initial configuration of WSL and Ubuntu on a Windows machine?"
  - "How does WSL handle file sharing and path differences between the Windows and Linux environments?"
  - "How can a user open and navigate to a specific WSL directory using Windows Explorer?"
  - "Why might a user choose to install and use a data transfer program like FileZilla within the WSL environment instead of natively on Windows?"
  - "Where are the local Windows files located when browsing the filesystem from within a Linux application in WSL?"
  - "How do you convert a Windows file path to its corresponding Linux path?"
  - "How many methods are mentioned for accessing Linux files from Windows?"
  - "What are the steps for Method 1 to access Linux files using Windows Explorer?"
  - "How can a user open and navigate to a specific WSL directory using Windows Explorer?"
  - "Why might a user choose to install and use a data transfer program like FileZilla within the WSL environment instead of natively on Windows?"
  - "Where are the local Windows files located when browsing the filesystem from within a Linux application in WSL?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# Introduction

Windows Subsystem for Linux (WSL) is a feature of the Windows operating system that allows you to run a Linux environment on your Windows machine, without requiring a full-featured Virtual Machine application or other complex method such as dual-booting. Using WSL allows you to have access to both Windows and Linux applications and files at the same time in a seamless, integrated manner.

This setup is of particular interest if you are running a Windows-based computer and require access to Linux-based Alliance resources. It allows you to use Linux-based tools to connect and transfer data to and from Alliance resources, while having access to your familiar Windows environment at the same time.

This article is a quick introduction to basic tasks that WSL can assist with. If more detailed documentation is required, please refer to the [documentation provided by Microsoft about WSL](https://learn.microsoft.com/en-us/windows/wsl/).

# Installing Windows Subsystem for Linux

The installation and setup of WSL is [covered in detail by Microsoft](https://learn.microsoft.com/en-us/windows/wsl/install).

To get started quickly on a Windows 10/11 machine that has not yet had WSL installed, the following steps will install WSL and Ubuntu (a popular version of Linux):
1.  Save your work, as this process requires a reboot.
2.  Click on the start button and begin typing *command prompt*.
3.  Right-click on the Command Prompt application and select *Run as administrator*. Accept any security prompt that appears.
4.  In the Command Prompt window, type the following command, and wait for it to complete:
    ```bash
    C:\>wsl --install
    ```
5.  Restart your machine.

# Launching Ubuntu for the first time

When your computer completes its reboot, you will have a new application available in the Start menu: *Ubuntu*. Upon launching this application for the first time, WSL will decompress some files and prepare the Ubuntu Linux environment for use. When complete, you will be asked to configure your Linux user and set a password.

!!! note
    *   This user name is **unique to the Linux system only**, and does not need to match the Windows username.
    *   If you later install multiple different Linux environments within WSL, each one of them will have its own users and passwords (they are not shared).

1.  At the prompt *Enter new UNIX username*, enter your desired username and press enter.
2.  At the prompt *Enter new UNIX password*, enter your desired password and press enter. You will not see characters as you type them; this is normal.

Your WSL/Ubuntu Linux setup is complete and you can now use it.

# File access between Windows and Linux

Linux environments operating in WSL are essentially equivalent to virtual machines. As such, they do not inherently share all of the same access to data stored within each environment; however, WSL has gone to great lengths to bridge this gap by two means:
1.  By automatically mounting (attaching) your Windows drives within the Linux folder structure at */mnt/*.
2.  By adding a Linux entry in the Windows Explorer sidebar that provides direct access to files stored within Linux.

These integrations allow you to transfer data easily between the two systems. As an example, the common Windows drive *C:\* would be available in Linux at */mnt/c*, and the Linux user’s home folder would be available in Windows Explorer at *Linux > Ubuntu > home > username*.

There are some notable differences between the way that Windows and Linux handle file paths:

*   Windows uses the backslash character (\) between directories, whereas Linux uses a forward slash (/).
*   Linux uses a case-sensitive approach to file and directory names, meaning that uppercase and lowercase letters are different: FILE.TXT, file.txt, and FILE.txt are all different files in Linux. Windows is case-insensitive, so all three of the examples given prior would point to the same file in Windows.

## Accessing Windows files from Linux (command line)

1.  Find the full path of the file or folder on Windows.
2.  Note the drive letter (e.g., *C:\*).
3.  Replace the drive letter with */mnt/{letter}/*.
4.  Transform all of the backslashes to forward slashes.

Examples:

*   *C:\Users\user1\Documents\File1.txt* is located at */mnt/c/Users/user1/Documents/File1.txt* in Linux.
*   *D:\Data\Project\Dataset\* is located at */mnt/d/Data/Project/Dataset/* in Linux.

## Accessing Linux files from Windows (2 methods)

### Method 1

1.  Find the full path of the file or folder on Linux.
2.  Use Windows Explorer’s sidebar to find the Linux entry (usually near the bottom) and expand it.
3.  Select the Linux environment that contains the file (*Ubuntu* by default).
4.  Navigate through the same folder structure from step 1 to find the file/folder.

Example:

*   */home/username/file1.txt* is located at *Linux > Ubuntu > home > username > file1.txt* in Windows Explorer.

### Method 2

1.  Open a WSL command line and change directory to where the file is stored.
2.  Run
    ```bash
    [name@ubuntu-wsl ~]$ explorer.exe .
    ```
    to open a Windows Explorer window at the intended directory (the trailing period is important, and directs Explorer to open the current directory).

# Transferring data using WSL

A common use case of WSL is to use it for transferring data to Alliance resources using programs such as [FileZilla](https://filezilla-project.org/). Often, support for [multifactor authentication](multifactor_authentication.md) is stronger inside Linux (and by extension WSL) due to various technical factors. You can easily install such programs inside the Ubuntu WSL environment; in the case of FileZilla:

```bash
[name@ubuntu-wsl ~]$ sudo apt install filezilla
```

The application is now installed and you can launch it from either from the Linux command line with `filezilla` or by the Windows start menu.

When you are browsing the filesystem of Linux using such tools, remember that your Windows files can be found under */mnt/{drive letter}* by default, and you can access them directly **without** needing to first copy them into the Linux environment.

For more information about transferring data to Alliance resources, please refer to the [Transferring data](transferring_data.md) page.