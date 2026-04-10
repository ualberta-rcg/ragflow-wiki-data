---
title: "Configuring WSL as a ControlMaster relay server"
slug: "configuring_wsl_as_a_controlmaster_relay_server"
lang: "base"

source_wiki_title: "Configuring WSL as a ControlMaster relay server"
source_hash: "b0157125f41a890133bbb08530fbec9d"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T05:47:38.207574+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

!!! warning "Disclaimer"
    This is still an experimental procedure (work in progress).

    If you have suggestions, please write to [technical support](technical-support.md).

With this procedure you can leverage ControlMaster under WSL so you may log into the clusters with several apps under native Windows for a certain period without having to use multifactor authentication for every session.

### Install Linux on Windows with WSL
Please follow [this link](https://docs.alliancecan.ca/wiki/Windows_Subsystem_for_Linux_(WSL)) for more detailed instructions:

This setup assumes the following on the sample config files:
*   you selected Ubuntu as your distribution
*   the hostname for the WSL instance is *ubuntu*: `/etc/hostname` contains `ubuntu` and `/etc/hosts` contains `127.0.0.1 localhost ubuntu`
*   the Windows system is named *smart* and the login name is *jaime*
*   the user name on the Ubuntu VM is also *jaime*
*   the Alliance user name is *pinto* and we want to connect to Cedar

### Install additional packages
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install openssh-server -y
```
You may log in from Windows to Ubuntu with `ssh localhost`.

### General idea of the setup
```
[ssh client] ----> [ssh relay server] ----> [ssh target server]
your Windows     modified authorized_keys     using cedar for
  machine          in your Ubuntu VM           this exercise
 *smart*        *ubuntu*                 Cedar
```

### Log into the Ubuntu VM and create a *custom_ssh* folder
```bash
jaime@ubuntu:~$ cat custom_ssh/sshd_config
Port 2222
HostKey /home/jaime/custom_ssh/ssh_host_ed25519_key
HostKey /home/jaime/custom_ssh/ssh_host_rsa_key
AuthorizedKeysFile /home/jaime/custom_ssh/authorized_keys
ChallengeResponseAuthentication no
UsePAM no
Subsystem sftp /usr/lib/openssh/sftp-server
PidFile /home/jaime/custom_ssh/sshd.pid
```
You may copy the *ssh_host* keys from `/etc/ssh` with:
```bash
sudo cp /etc/ssh/ssh_host_ed25519_key /home/jaime/custom_ssh/
```

### Customize *.ssh/config* on Ubuntu
```bash
jaime@ubuntu:~$ cat ~/.ssh/config
Host cedar
    ControlPath ~/.ssh/cm-%r@%h:%p
    ControlMaster auto
    ControlPersist 10m
    HostName cedar.alliancecan.ca
    User pinto
```

### Customize the authorized keys
```bash
jaime@ubuntu:~/custom_ssh$ cat /home/jaime/custom_ssh/authorized_keys
ssh-ed25519 AAAZDINzaC1lZDI1NTE5AAC1lZDIvqzlffkzcjRAaMQoTBrPe5FxlSAjRAaMQyVzN+A+
```

Use the same public SSH key that you uploaded to CCDB.

### Now start the sshd server on Ubuntu
```bash
jaime@ubuntu:~/custom_ssh$ /usr/sbin/sshd -f ${HOME}/custom_ssh/sshd_config
```

Make sure you start the server as yourself, not as root.
You will also need to start the sshd server every time you restart your computer, or after closing or restarting WSL.

### Customize *.ssh/config* on *smart* with `RemoteCommand`
```bash
jaime@smart ~/.ssh cat config
Host ubuntu
        Hostname localhost
        RemoteCommand ssh cedar
```

### You are now ready to try to log into Cedar
```bash
jaime@smart ~
$ ssh -t ubuntu -p 2222
Enter passphrase for key '/home/jaime/.ssh/id_ed25519':
Last login: Fri Mar 22 10:50:12 2024 from 99.239.174.157
================================================================================
Welcome to Cedar! / Bienvenue sur Cedar!
...
...
...
[pinto@cedar1 ~]$
```

### Alternative setup
There is another way in which you could customize the authorized keys on Ubuntu and the *~/.ssh/config* on Windows such that it may work better for some Windows GUI apps that don't let you explicitly set the `RemoteCommand` (such as WinSCP). In this case you set the `RemoteCommand` on the public key:
```bash
jaime@ubuntu:~/custom_ssh$ cat /home/jaime/custom_ssh/authorized_keys
command="ssh cedar" ssh-ed25519 AAAZDINzaC1lZDI1NTE5AAC1lZDIvqzlffkzcjRAaMQoTBrPe5FxlSAjRAaMQyVzN+A+
```
```bash
jaime@smart ~/.ssh cat config
Host ubuntu
        Hostname localhost
        #RemoteCommand ssh cedar
```

You may still use `ssh ubuntu -p 2222` after that from a shell on Windows.

### Setup with MobaXterm