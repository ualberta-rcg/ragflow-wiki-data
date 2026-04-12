---
title: "Configuring WSL as a ControlMaster relay server/en"
slug: "configuring_wsl_as_a_controlmaster_relay_server"
lang: "en"

source_wiki_title: "Configuring WSL as a ControlMaster relay server/en"
source_hash: "ebb32cd2b898bdeec2576faeacc3df2c"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:32:57.399752+00:00"

tags:
  []

keywords:
  - "WSL"
  - "MobaXterm"
  - "Windows Subsystem for Linux"
  - "~/.ssh/config"
  - "SSH relay server"
  - "SSH configuration"
  - "Multi-Factor Authentication"
  - "Ubuntu VM"
  - "public key"
  - "authorized_keys"
  - "ControlMaster"
  - "Windows GUI apps"
  - "RemoteCommand"
  - "remote servers"

questions:
  - "What is the primary purpose of leveraging ControlMaster under WSL as described in the text?"
  - "What are the key configuration steps required on the Ubuntu VM to set up the SSH relay server and enable multiplexing?"
  - "How does the alternative setup modify the authorized keys to accommodate Windows GUI applications that do not support the RemoteCommand option?"
  - "How does the described SSH setup handle Multi-Factor Authentication (MFA) for multiple sessions on the remote server?"
  - "What challenge arises when using Windows applications to transfer files, and how can users locate their local Windows drives within the Ubuntu relay?"
  - "How is the `.ssh/config` file proposed to be configured to manage connections to multiple sites like Cedar, Graham, and Beluga?"
  - "Why is it necessary to set the RemoteCommand on the public key for certain Windows GUI applications like WinSCP?"
  - "How do you format the entry in the authorized_keys file to automatically execute a specific command upon SSH connection?"
  - "Which specific configuration files are mentioned for managing these remote SSH connections between Windows and Ubuntu?"
  - "How does the described SSH setup handle Multi-Factor Authentication (MFA) for multiple sessions on the remote server?"
  - "What challenge arises when using Windows applications to transfer files, and how can users locate their local Windows drives within the Ubuntu relay?"
  - "How is the `.ssh/config` file proposed to be configured to manage connections to multiple sites like Cedar, Graham, and Beluga?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! warning "Disclaimer"
    This is still an experimental procedure (work in progress).

    If you have suggestions, please write to [technical support](technical-support.md).

With this procedure you can leverage ControlMaster under WSL so you may log into the clusters with several apps under native Windows for a certain period without having to use multifactor authentication for every session.

## Install Linux on Windows with WSL
Please follow this link for more detailed instructions:
[Windows Subsystem for Linux (WSL)](https://docs.alliancecan.ca/wiki/Windows_Subsystem_for_Linux_(WSL))

This setup assumes the following on the sample config files:
*   you selected Ubuntu as your distribution
*   the hostname for the WSL instance is *ubuntu*: */etc/hostname* contains *ubuntu* and */etc/hosts* contains *127.0.0.1 localhost ubuntu*
*   the Windows system is named *smart* and the login name is *jaime*
*   the user name on the Ubuntu VM is also *jaime*
*   the Alliance user name is *pinto* and we want to connect to Cedar

## Install additional packages
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install openssh-server -y
```
You may log in from Windows to Ubuntu with `ssh localhost`.

## General idea of the setup
```text
[ssh client] ----> [ssh relay server] ----> [ssh target server]
your Windows     modified authorized_keys     using cedar for
  machine          in your Ubuntu VM           this exercise
 *smart*        *ubuntu*                 Cedar
```

## Log into the Ubuntu VM and create a *custom_ssh* folder
```bash
jaime@ubuntu:~$ cat custom_ssh/sshd_config
```
```ini title="custom_ssh/sshd_config"
Port 2222
HostKey /home/jaime/custom_ssh/ssh_host_ed25519_key
HostKey /home/jaime/custom_ssh/ssh_host_rsa_key
AuthorizedKeysFile /home/jaime/custom_ssh/authorized_keys
ChallengeResponseAuthentication no
UsePAM no
Subsystem sftp /usr/lib/openssh/sftp-server
PidFile /home/jaime/custom_ssh/sshd.pid
```
You may copy the *ssh_host* keys from */etc/ssh* with:
```bash
sudo cp /etc/ssh/ssh_host_ed25519_key /home/jaime/custom_ssh/
```

## Customize *.ssh/config* on Ubuntu
```bash
jaime@ubuntu:~$ cat ~/.ssh/config
```
```ini title="~/.ssh/config (Ubuntu)"
Host cedar
    ControlPath ~/.ssh/cm-%r@%h:%p
    ControlMaster auto
    ControlPersist 10m
    HostName cedar.alliancecan.ca
    User pinto
```

## Customize the authorized keys
```bash
jaime@ubuntu:~/custom_ssh$ cat /home/jaime/custom_ssh/authorized_keys
```
```text title="/home/jaime/custom_ssh/authorized_keys"
ssh-ed25519 AAAZDINzaC1lZDI1NTE5AAC1lZDIvqzlffkzcjRAaMQoTBrPe5FxlSAjRAaMQyVzN+A+
```

Use the same public SSH key that you uploaded to CCDB.

## Now start the sshd server on Ubuntu
```bash
jaime@ubuntu:~/custom_ssh$ /usr/sbin/sshd -f ${HOME}/custom_ssh/sshd_config
```

Make sure you start the server as yourself, not as root.
You will also need to start the sshd server every time you restart your computer, or after closing or restarting WSL.

## Customize *.ssh/config* on *smart* with `RemoteCommand`
```bash
jaime@smart ~/.ssh cat config
```
```ini title="~/.ssh/config (Windows)"
Host ubuntu
        Hostname localhost
        RemoteCommand ssh cedar
```

## You are now ready to try to log into Cedar
```bash
jaime@smart ~
$ ssh -t ubuntu -p 2222
```
```text title="Output"
Enter passphrase for key '/home/jaime/.ssh/id_ed25519':
Last login: Fri Mar 22 10:50:12 2024 from 99.239.174.157
================================================================================
Welcome to Cedar! / Bienvenue sur Cedar!
...
...
...
[pinto@cedar1 ~]$
```

## Alternative setup
There is another way in which you could customize the authorized keys on Ubuntu and the *~/.ssh/config* on Windows such that it may work better for some Windows GUI apps that don't let you explicitly set the `RemoteCommand` (such as WinSCP). In this case you set the `RemoteCommand` on the public key:
```bash
jaime@ubuntu:~/custom_ssh$ cat /home/jaime/custom_ssh/authorized_keys
```
```text title="/home/jaime/custom_ssh/authorized_keys (Alternative)"
command="ssh cedar" ssh-ed25519 AAAZDINzaC1lZDI1NTE5AAC1lZDIvqzlffkzcjRAaMQoTBrPe5FxlSAjRAaMQyVzN+A+
```
```bash
jaime@smart ~/.ssh cat config
```
```ini title="~/.ssh/config (Windows, Alternative)"
Host ubuntu
        Hostname localhost
        #RemoteCommand ssh cedar
```

You may still use `ssh ubuntu -p 2222` after that from a shell on Windows.

## Setup with MobaXterm