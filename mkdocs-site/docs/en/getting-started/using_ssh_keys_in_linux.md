---
title: "Using SSH keys in Linux/en"
slug: "using_ssh_keys_in_linux"
lang: "en"

source_wiki_title: "Using SSH keys in Linux/en"
source_hash: "967d4fa9eb1c09dbfedd2333f422040e"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T12:18:51.690207+00:00"

tags:
  - connecting

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

*Parent page: [SSH](ssh.md)*

## Creating a key pair
Before creating a new key pair, check to see if you already have one. If you do, but cannot remember where you have used it, it is better to create a fresh one, since you should not install a key of unknown security.

Key pairs are typically located in the `.ssh/` directory in your `/home` directory. By default, a key is named with an "id_" prefix, followed by the key type ("rsa", "dsa", "ed25519"), and the public key also has a ".pub" suffix. So a common example is `id_rsa` and `id_rsa.pub`. A good practice is to give it a name that is meaningful to you and identifies on which system the key is used.

If you do need a new key, you can generate it with the `ssh-keygen` command:

```bash
[name@yourLaptop]$ ssh-keygen -t ed25519
```
or
```bash
[name@yourLaptop]$ ssh-keygen -b 4096 -t rsa
```
(This example explicitly asks for a 4-kbit RSA key, which is a reasonable choice.)

The output will be similar to the following:

```bash
Generating public/private rsa key pair.
Enter file in which to save the key (/home/username/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/username/.ssh/id_rsa.
Your public key has been saved in /home/username/.ssh/id_rsa.pub.
The key fingerprint is:
ef:87:b5:b1:4d:7e:69:95:3f:62:f5:0d:c0:7b:f1:5e username@hostname
The key's randomart image is:
+--[ RSA 2048]----+
|                 |
|                 |
|           .     |
|            o .  |
|        S    o o.|
|         .  + +oE|
|          .o O.oB|
|         .. +oo+*|
|          ... o..|
+-----------------+
```

!!! note "Passphrase and File Names"
    When prompted, enter a passphrase. If you already have key pairs saved with the default names, you should enter a different file name for the new keys to avoid overwriting existing key pairs.

More details on best practices can be found [here](ssh_keys.md#best-practices-for-key-pairs).

### Creating a key pair backed by a hardware security key
Some sites now support the use of SSH keys backed by a hardware security key (e.g., YubiKey). If you need one of these keys, you can generate it with the `ssh-keygen` command:

```bash
[name@yourLaptop]$ ssh-keygen -t ecdsa-sk
```

The output will be similar to the following:

```bash
Generating public/private ecdsa-sk key pair.
You may need to touch your authenticator to authorize key generation.
Enter file in which to save the key (/home/username/.ssh/id_ecdsa_sk):
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/username/.ssh/id_ecdsa_sk
Your public key has been saved in /home/username/.ssh/id_ecdsa_sk.pub
The key fingerprint is:
SHA256:P051NAesYSxF7NruGLfnyAFMUBmGLwCaSRiXDwUY6Ts username@hostname
The key's randomart image is:
+-[ECDSA-SK 256]--+
|o*++o.  .o+Bo..  |
|+oo+  . .oo = .. |
|. +o   . ..+ oo .|
| .  .   .o. o. o |
|  .     S.oo. .  |
| E       ..o..   |
|  .       =.o    |
|         o *.+.  |
|          o.=o.  |
+----[SHA256]-----+
```

You will be prompted to both enter a passphrase and activate a hardware security key as part of the key creation process.

## Installing the public part of the key

### Installing via CCDB
!!! note "Using CCDB"
    We encourage all users to leverage the new CCDB feature to install their SSH public key. This will make the key available to all our clusters.

Grab the content of your public key (called *id_rsa.pub* in the above case) and upload it to CCDB as per step 3 of [these instructions](ssh_keys.md#using-ccdb).

The simplest, safest way to install a key to a remote system is by using the `ssh-copy-id` command:
```bash
ssh-copy-id -i ~/.ssh/mynewkey.pub graham.computecanada.ca
```
This assumes that the new keypair is named "mynewkey" and "mynewkey.pub", and that your username on the remote machine is the same as your local username.

!!! tip "Benefits of `ssh-copy-id`"
    If necessary, you can do this "manually" - in fact, `ssh-copy-id` is not doing anything very magical. It is simply connecting to the remote machine, and placing the public key into `.ssh/authorized_keys` in your `/home` directory there. The main benefit from using `ssh-copy-id` is that it will create files and directories if necessary, and will ensure that the permissions on them are correct.

You can do it entirely yourself by copying the public key file to the remote server, then:
```bash
mkdir ~/.ssh
cat id_rsa.pub >> ~/.ssh/authorized_keys
chmod --recursive go-rwx ~/.ssh
chmod go-w ~
```

!!! warning "SSH Permissions Are Strict"
    SSH is picky about permissions, on both the client and the server. SSH will fail if the following conditions are not met:
    *   The private key file must not be accessible to others. `chmod go-rwx id_rsa`
    *   Your remote `/home` directory must not be writable by others. `chmod go-w ~`
    *   Same for your remote `~/.ssh` and `~/.ssh/authorized_keys`. `chmod --recursive go-rwx ~/.ssh`.

!!! note
    Debugging the remote conditions may not be obvious without the help of the remote machine's system administrators.

## Connecting using a key pair
1.  Finally, test the new key by sshing to the remote machine from the local machine with
    ```bash
    [name@yourLaptop]$ ssh -i /path/to/your/privatekey USERNAME@ADDRESS
    ```
    where
    *   `/path/to/your/privatekey` specifies your private key file, e.g., `/home/ubuntu/.ssh/id_rsa`;
    *   `USERNAME` is the username on the remote machine;
    *   `ADDRESS` is the address of the remote machine.

!!! warning "Do Not Disclose Private Keys"
    If you have administrative access on the server and created the account for other users, they should test the connection out themselves and not disclose their private key.

## Using ssh-agent
Having successfully created a key pair and installed the public key on a cluster, you can now log in using the key pair. While this is a better solution than using a password to connect to our clusters, it still requires you to type in a passphrase, needed to unlock your private key, every time that you want to log in to a cluster. There is, however, the `ssh-agent` program, which stores your private key in memory on your local computer and provides it whenever another program on this computer needs it for authentication. This means that you only need to unlock the private key once, after which you can log in to a remote cluster many times without having to type in the passphrase again.

You can start the `ssh-agent` program using the command
```bash
eval `ssh-agent`
```
After you have started the `ssh-agent`, which will run in the background while you are logged in at your local computer, you can add your key pair to those managed by the agent using the command
```bash
ssh-add
```
Assuming you installed your key pair in one of the standard locations, the `ssh-add` command should be able to find it, though if necessary you can explicitly add the full path to the private key as an argument to `ssh-add`.

!!! tip
    Using the `ssh-add -l` option will show which private keys are currently accessible to the `ssh-agent`.

!!! note "Agent Forwarding"
    While using `ssh-agent` will allow automatically negotiating the key exchange between your personal computer and the cluster, if you need to use your private key on the cluster itself, for example when interacting with a remote GitHub repository, you will need to enable *agent forwarding*.

To enable this on the [Béluga](beluga.md) cluster, you can add the following lines to your `$HOME/.ssh/config` file on your personal computer,
```yaml {file="config"}
Host beluga.computecanada.ca
    ForwardAgent yes
```
!!! warning
    You should never use the line `Host *` for agent forwarding in your SSH configuration file.

### Installing locally
!!! tip "Graphical Keychain Managers"
    Many contemporary Linux distributions, as well as macOS, now offer graphical "keychain managers" that can easily be configured to also manage your SSH key pair. This means that logging in on your local computer is enough to store the private key in memory and have the operating system automatically provide it to the SSH client during login on a remote cluster. You will then be able to log in to our clusters without ever typing in any kind of passphrase.