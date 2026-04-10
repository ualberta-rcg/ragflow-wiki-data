---
title: "Setting up GUI Desktop on a VM"
slug: "setting_up_gui_desktop_on_a_vm"
lang: "base"

source_wiki_title: "Setting up GUI Desktop on a VM"
source_hash: "b2aa05f345bdf71c3b4f26c83446a950"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T11:17:14.673142+00:00"

tags:
  - cloud

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

Some software that you can install on your virtual machine (VM, or instance) are only, or best accessed, through their graphical user interface (GUI). It is possible to use a GUI through SSH + X11 forwarding. However, you may observe better performance when using VNC to connect to a remote desktop running on your VM.

Below, we outline steps for setting a remote desktop with VNC. Please note that these instructions are for a VM running a Ubuntu operating system.

1.  Install a GUI Desktop on your VM.
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

2.  Install TigerVNC server.
    This software runs on your VM and allows you to use the GUI desktop you installed in step 1 remotely using client software.

    ```bash
    sudo apt install -y tigervnc-common tigervnc-standalone-server
    ```

    This command will install the TigerVNC server and some supporting software. For details about using VNC servers and clients, see our docs on [VNC](vnc.md).

3.  Start the VNC server.

    ```bash
    vncserver
    ```

    You will be prompted to enter a password and then to enter "n" for a view-only password.
    The first time you start a VNC server, it will ask you to set a password. This password is used later when connecting to the VNC desktop. You do not need a view-only password. The `vncpasswd` command can later be used to change your password.

4.  Test your connection by opening port `5901` (see [security groups](managing-your-cloud-resources-with-openstack.md#security-groups) for more information about opening ports to your VMs with OpenStack) and connecting using a VNC viewer, for example, [TigerVNC](https://tigervnc.org/). However, this is not a secure connection; data sent to and from your VM will not be encrypted. This is only meant to test your server-client connection before connecting securely with an SSH tunnel (the next step). If you are confident in your ability to set up an SSH tunnel, you may skip this step.

5.  Connect using an SSH tunnel (see [SSH tunnelling](ssh-tunnelling.md)). There is [an example of creating an SSH tunnel to a VNC server running on a compute node of one of our clusters](vnc.md#compute-nodes).

    Below are instructions for connecting using an SSH tunnel for Linux or Mac:
    *   Open your terminal
    *   Type the following in your local terminal: `SSH -i filepathtoyoursshkey/sshprivatekeyfile.key -L5901:localhost:5901 ubuntu@ipaddressofyourVM`
    *   Start your VNC viewer.
    *   In the VNC server field, enter: `localhost:5901`.
    *   Your GUI desktop for your remote session should now open.

6.  Close port `5901`. Once you are connected to your VNC server using an SSH tunnel, you no longer require port `5901` open, so it is recommended that you remove this rule from your security groups (see [security groups](managing-your-cloud-resources-with-openstack.md#security-groups) for more information).

7.  Once you are finished using the remote desktop, you may stop the VNC server with:

    ```bash
    vncserver -kill :1