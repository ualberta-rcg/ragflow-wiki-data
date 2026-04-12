---
title: "SSH"
slug: "ssh"
lang: "base"

source_wiki_title: "SSH"
source_hash: "4a41f72eeb6184a537a38a86e487dbe1"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:12:55.947525+00:00"

tags:
  - connecting

keywords:
  - "connection"
  - "Secure Shell (SSH)"
  - "SSH client"
  - "X11"
  - "host key fingerprint"
  - "key exchange algorithm"
  - "man-in-the-middle attack"
  - "SSH host keys"
  - "SSH keys"
  - "post-quantum key exchange"
  - "security upgrade"
  - "remote connection"
  - "error messages"

questions:
  - "What are the essential prerequisites and credentials a user needs to successfully connect to a remote machine using an SSH client?"
  - "How can a user run graphical applications over an SSH connection, and what specific software is required for different operating systems?"
  - "What does the \"remote host identification has changed\" error indicate, and how should a user verify the connection's security if this occurs?"
  - "What should a user do if the host key fingerprint does not match the published list during an SSH connection?"
  - "Which specific operating systems and SSH clients are known to fail and require an upgrade to support strong ciphers?"
  - "Why might a user see a warning about a \"post-quantum key exchange algorithm,\" and how can they suppress it?"
  - "What specific error messages related to key exchange and host identification are listed in the text?"
  - "What are the two potential causes indicated by the \"remote host identification has changed\" error message?"
  - "How should a user verify their connection if they receive a host identification error?"
  - "What should a user do if the host key fingerprint does not match the published list during an SSH connection?"
  - "Which specific operating systems and SSH clients are known to fail and require an upgrade to support strong ciphers?"
  - "Why might a user see a warning about a \"post-quantum key exchange algorithm,\" and how can they suppress it?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Secure Shell (SSH) is a widely used standard to connect to remote machines securely. The SSH connection is encrypted, including the username and password. SSH is the standard way for you to connect in order to execute commands, submit jobs, check the progress of jobs, and in some cases, transfer files.

## What you need 

You will need an SSH client program. One or more clients exist for most operating systems.
* On macOS and Linux, the most widely used client is OpenSSH, a command-line application installed by default.
* For recent versions of Windows, SSH is available in the PowerShell terminal, in the `cmd` prompt, or through Windows Subsystem for Linux (WSL). There are also 3rd-party SSH clients that are popular, such as [PuTTY](connecting_with_putty.md), [MobaXTerm](connecting_with_mobaxterm.md), [WinSCP](https://winscp.net/eng/download.php), and [Bitvise](https://www.bitvise.com/ssh-client-download). 

To use any of these SSH clients successfully, you must:
* **know the name of the machine to which you want to connect.** This will be something like `fir.alliancecan.ca` or `trillium.alliancecan.ca`.
* **know your username**, typically something like `ansmith`. The `username` is **not** your CCI, like `abc-123`, nor a CCRI like `abc-123-01`, nor your email address.
* **know your password, or have an [SSH key](ssh_keys.md).** Your password is the same one you use to log in to [CCDB](https://ccdb.alliancecan.ca/). You may register and use an SSH key instead of a password; we highly recommend this since it provides better security.
* **be registered for [multifactor authentication](multifactor_authentication.md) and have your 2nd factor available.**
* **have requested access to the system** [here](https://ccdb.alliancecan.ca/me/access_systems).

From a command-line client (*e.g.* /Applications/Utilities/Terminal.app for macOS, cmd or PowerShell for Windows), use the `ssh` command like this:
```bash
ssh username@machine_name
```

For graphical clients such as MobaXterm or PuTTY, see:
* [Connecting with MobaXTerm](connecting_with_mobaxterm.md)
* [Connecting with PuTTY](connecting_with_putty.md)

The first time that you connect to a machine you'll be asked to store a copy of its *host key*, a unique identifier that allows the SSH client to verify, when connecting next time, that this is the same machine. 

For more on generating key pairs, see:
* [SSH Keys](ssh_keys.md)
  * [Generating SSH keys in Windows](generating_ssh_keys_in_windows.md)
  * [Using SSH keys in Linux](using_ssh_keys_in_linux.md)
For how to use SSH to allow communication between compute nodes and the internet, see:
* [SSH tunnelling](ssh_tunnelling.md)
For how to use an SSH configuration file to simplify the login procedure, see:
* [SSH configuration file](ssh_configuration_file.md)

## X11 for graphical applications 

SSH supports graphical applications via the [X protocol](https://en.wikipedia.org/wiki/X_Window_System), now usually called "X11". In order to use X11 you must have an X11 server installed on your computer. Under Linux, an X11 server will normally already be installed, but users of macOS will typically need to install an external package such as [XQuartz](https://www.xquartz.org). Under Windows, MobaXterm comes with an X11 server, while for PuTTY users, there is [VcXsrv](https://sourceforge.net/projects/vcxsrv/).

Using the SSH command line, add the `-Y` option to enable X11 communications:
```bash
ssh -Y username@machine_name
```

## Connection errors
While connecting to one of our clusters, you might get an error message such as:
* no matching cipher found
* no matching MAC found
* unable to negotiate a key exchange method
* couldn't agree a key exchange algorithm
* remote host identification has changed.

!!! warning "Remote Host Identification Has Changed"
    The last of these error messages can point to a man-in-the-middle attack, or to an upgrade of security of the cluster you are trying to connect to.
    If you get this, verify that the host key fingerprint mentioned in the message matches one of the host key fingerprints published at [SSH host keys](ssh_host_keys.md).
    If it does, it is safe to continue connecting. If the host key fingerprint does not appear on our published list, terminate the connection and [contact support](../support/technical_support.md).

One such upgrade occurred on the Niagara cluster on May 31, 2019. See [this page](https://docs.scinet.utoronto.ca/index.php/SSH_Changes_in_May_2019) for the one-time action required from users after the security upgrade. Further upgrades of this type were made on all clusters in September/October 2019; see [SSH security improvements](ssh_security_improvements.md) for more information.

If you see any of the other error messages, you will have to upgrade your OS and/or SSH client that supports strong ciphers, key exchange protocols and MAC (message authentication code) algorithms.

Here are known versions that will fail and will have to be upgraded:
* OpenSSH on CentOS/RHEL 5
* [PuTTY](connecting_with_putty.md) v0.64 and earlier on Windows

## Warnings 

### *connection is not using a post-quantum key exchange algorithm* 

!!! note
    We recommend you ignore this warning. It warns that if encrypted traffic is recorded today, some hypothetical future computer (e.g., a quantum computer) may be able to decode the contents. This is really just a matter of what key length can be brute-forced, so is nothing new or urgent. We do not plan to reconfigure our systems immediately. You can suppress the warning by configuring your SSH client with `WarnWeakCrypto no` as described at the [link](https://www.openssh.org/pq.html) given in the warning message.