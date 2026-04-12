---
title: "Setting up GUI Desktop on a VM/en"
slug: "setting_up_gui_desktop_on_a_vm"
lang: "en"

source_wiki_title: "Setting up GUI Desktop on a VM/en"
source_hash: "fdb2571dc171271507795442cbf95c13"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:28:34.282789+00:00"

tags:
  - cloud

keywords:
  - "SSH tunnel"
  - "Remote desktop"
  - "GUI desktop"
  - "VNC server"
  - "Virtual machine"

questions:
  - "What are the necessary software components that must be installed on a Ubuntu virtual machine to set up a remote desktop environment?"
  - "How can a user establish a secure connection to their remote VNC server using an SSH tunnel?"
  - "What are the specific commands required to start the VNC server initially and to terminate the session when finished?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# Setting up a GUI Desktop on a VM

Some software that you can install on your virtual machine (VM, or instance) are only, or best accessed, through their graphical user interface (GUI). It is possible to use a GUI through SSH + X11 forwarding. However, you may observe better performance when using VNC to connect to a remote desktop running on your VM.

Below, we outline steps for setting up a remote desktop with VNC.

!!! note
    These instructions are for a VM running a Ubuntu operating system.

## 1. Install a GUI Desktop on Your VM

There are lots of different Desktop packages available. For example, some common Desktop packages available for the Ubuntu operating system are:
* [ubuntu-unity-desktop](https://ubuntuunity.org/)
* [ubuntu-mate-desktop](https://ubuntu-mate.org/)
* [lubuntu-desktop](https://lubuntu.net/)
* [xubuntu-desktop](https://xubuntu.org/screenshots/)
* [xfce4](https://www.xfce.org/)
* ubuntu-desktop
* [kde-plasma-desktop](https://kde.org/plasma-desktop/)
* ubuntu-desktop-minimal
* [cinnamon](https://en.wikipedia.org/wiki/Cinnamon_(desktop_environment))
* [icewm](https://ice-wm.org/)

[This article](https://cloudinfrastructureservices.co.uk/best-ubuntu-desktop-environments) shows a few of these different desktops. Below are the commands to install the MATE desktop.

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install ubuntu-mate-desktop
```

During the installation of the `ubuntu-mate-desktop` package, it will ask you to choose the default display manager; a good option is [lightdm](https://en.wikipedia.org/wiki/LightDM). Installing the `ubuntu-mate-desktop` package can take a fair amount of time (something like 15-30 minutes).

## 2. Install TigerVNC Server

This software runs on your VM and allows you to use the GUI desktop you installed in step 1 remotely using client software.

```bash
sudo apt install -y tigervnc-common tigervnc-standalone-server
```

This command will install the TigerVNC server and some supporting software. For details about using VNC servers and clients, see our documentation on [VNC](../interactive/vnc.md).

## 3. Start the VNC Server

```bash
vncserver
```
When you run `vncserver` for the first time, you will be prompted to set a password. This password is used later when connecting to the VNC desktop. You do not need a view-only password. The `vncpasswd` command can later be used to change your password.

## 4. Test Your Connection

To test your connection, you can open port `5901` (see [security groups](managing_your_cloud_resources_with_openstack.md#security-groups) for more information about opening ports to your VMs with OpenStack) and connect using a VNC viewer, for example [TigerVNC](https://tigervnc.org/).

!!! warning "Insecure Connection"
    This is not a secure connection; data sent to and from your VM will not be encrypted. This step is only meant to test your server-client connection before connecting securely with an SSH tunnel (the next step). If you are confident in your ability to set up an SSH tunnel, you may skip this step.

## 5. Connect Using an SSH Tunnel

See [SSH tunnelling](../getting-started/ssh_tunnelling.md) for general information. There is [an example of creating an SSH tunnel to a VNC server running on a compute node of one of our clusters](../interactive/vnc.md#compute-nodes).

Below are instructions for connecting using an SSH tunnel for Linux or macOS:
1. Open your terminal.
2. Type the following in your local terminal:
   ```bash
   SSH -i filepathtoyoursshkey/sshprivatekeyfile.key -L5901:localhost:5901 ubuntu@ipaddressofyourVM
   ```
3. Start your VNC viewer.
4. In the VNC server field, enter: `localhost:5901`.
5. Your GUI desktop for your remote session should now open.

## 6. Close Port 5901

!!! warning "Security Recommendation"
    Once you are connected to your VNC server using an SSH tunnel, you no longer require port `5901` to be open. It is recommended that you remove this rule from your security groups (see [security groups](managing_your_cloud_resources_with_openstack.md#security-groups) for more information).

## 7. Stop the VNC Server

Once you are finished using the remote desktop, you may stop the VNC server with:

```bash
vncserver -kill :1