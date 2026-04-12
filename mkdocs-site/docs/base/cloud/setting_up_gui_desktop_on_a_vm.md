---
title: "Setting up GUI Desktop on a VM"
slug: "setting_up_gui_desktop_on_a_vm"
lang: "base"

source_wiki_title: "Setting up GUI Desktop on a VM"
source_hash: "b2aa05f345bdf71c3b4f26c83446a950"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:28:07.368357+00:00"

tags:
  - cloud

keywords:
  - "security groups"
  - "Cloud"
  - "SSH tunnel"
  - "Remote desktop"
  - "GUI desktop"
  - "VNC server"
  - "port 5901"
  - "remote desktop"
  - "Category"
  - "Virtual machine"

questions:
  - "What is the primary advantage of using VNC over SSH + X11 forwarding, and what initial software must be installed on the Ubuntu VM to use it?"
  - "How can a user securely connect to their remote VNC desktop using an SSH tunnel?"
  - "What are the necessary commands to start the VNC server, set its password, and eventually terminate the session?"
  - "Why is it recommended to close port 5901 and remove its rule from the security groups?"
  - "How does connecting to the VNC server via an SSH tunnel affect the need for open ports?"
  - "What is the specific command used to terminate the VNC server after finishing a remote desktop session?"
  - "What is the specific purpose of the \"[[Category:Cloud]]\" tag within the structure of this document?"
  - "What types of information or topics are expected to be classified under this \"Cloud\" category?"
  - "How does assigning this text to the \"Cloud\" category impact its discoverability and organization?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Some software that you can install on your virtual machine (VM, or instance) are only, or best accessed, through their graphical user interface (GUI). It is possible to use a GUI through SSH + X11 forwarding. However, you may observe better performance when using VNC to connect to a remote desktop running on your VM.

Below, we outline steps for setting a remote desktop with VNC.

!!! note
    These instructions are for a VM running a Ubuntu operating system.

1.  **Install a GUI Desktop on your VM.**
    There are lots of different Desktop packages available. For example, some common Desktop packages available for the Ubuntu operating system are:
    *   [ubuntu-unity-desktop](https://ubuntuunity.org/)
    *   [ubuntu-mate-desktop](https://ubuntu-mate.org/)
    *   [lubuntu-desktop](https://lubuntu.net/)
    *   [xubuntu-desktop](https://xubuntu.org/screenshots/)
    *   [xfce4](https://www.xfce.org/)
    *   ubuntu-desktop
    *   [kde-plasma-desktop](https://kde.org/plasma-desktop/)
    *   ubuntu-desktop-minimal
    *   [cinnamon](https://en.wikipedia.org/wiki/Cinnamon_(desktop_environment))
    *   [icewm](https://ice-wm.org/)

    [This article](https://cloudinfrastructureservices.co.uk/best-ubuntu-desktop-environments) shows a few of these different desktops. Below are the commands to install the MATE desktop.

    ```bash
    sudo apt update
    sudo apt upgrade -y
    sudo apt install ubuntu-mate-desktop
    ```

    During the installation of the `ubuntu-mate-desktop` package, it will ask you to choose the default display manager; a good option is [`lightdm`](https://en.wikipedia.org/wiki/LightDM). Installing the `ubuntu-mate-desktop` package can take a fair amount of time (something like 15-30 mins).
2.  **Install TigerVNC server.**
    This software runs on your VM and allows you to use the GUI desktop you installed in step 1 remotely using a client software.

    ```bash
    sudo apt install -y tigervnc-common tigervnc-standalone-server
    ```

    This command will install the TigerVNC server and some supporting software. For details about using VNC servers and clients, see our docs on [VNC](../interactive/vnc.md).
3.  **Start the VNC server.**

    ```bash
    vncserver
    ```

    The first time you start a VNC server, it will ask you to set a password. This password is used later when connecting to the VNC desktop. You don't need a view-only password. You will see prompts similar to this:

    ```text
    You will require a password to access your desktops.

    Password:
    Verify:
    Would you like to enter a view-only password (y/n)? n
    ```

    The `vncpasswd` command can later be used to change your password.
4.  **Test your connection by opening port `5901`.**
    (See [security groups](managing_your_cloud_resources_with_openstack.md#security-groups) for more information about opening ports to your VMs with OpenStack.)
    Connect using a VNC viewer, for example [TigerVNC](https://tigervnc.org/).

    !!! warning
        This is not a secure connection; data sent to and from your VM will not be encrypted. This step is only meant to test your server-client connection before connecting securely with an SSH tunnel (the next step). If you are confident in your ability to set up an SSH tunnel, you may skip this step.
5.  **Connect using an SSH tunnel.**
    (See [SSH tunnelling](../getting-started/ssh_tunnelling.md) for more information.) There is [an example of creating an SSH tunnel to a VNC server running on a compute node of one of our clusters](../interactive/vnc.md#compute-nodes).

    Below are instructions for connecting using an SSH tunnel for Linux or macOS:
    *   Open your terminal.
    *   Type the following in your local terminal:
        ```bash
        SSH -i filepathtoyoursshkey/sshprivatekeyfile.key -L5901:localhost:5901 ubuntu@ipaddressofyourVM
        ```
    *   Start your VNC viewer.
    *   In the VNC server field, enter: `localhost:5901`.
    *   Your GUI desktop for your remote session should now open.
6.  **Close port `5901`.**
    Once you are connected to your VNC server using an SSH tunnel, you no longer require port 5901 open, so it is recommended that you remove this rule from your security groups. (See [security groups](managing_your_cloud_resources_with_openstack.md#security-groups) for more information.)
7.  Once you are finished using the remote desktop, you may stop the VNC server with:

    ```bash
    vncserver -kill :1