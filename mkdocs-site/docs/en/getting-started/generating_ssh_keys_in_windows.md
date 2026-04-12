---
title: "Generating SSH keys in Windows/en"
slug: "generating_ssh_keys_in_windows"
lang: "en"

source_wiki_title: "Generating SSH keys in Windows/en"
source_hash: "f3389602a7e0e6d3ccbb377bd4e27da8"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:38:47.208690+00:00"

tags:
  - connecting

keywords:
  - "OpenStack"
  - "SSH key pair"
  - "Public key"
  - "PuTTYgen"
  - "MobaXTerm"

questions:
  - "What are the steps to generate a new SSH key pair using PuTTYgen or MobaXTerm?"
  - "How can a user install the public part of their SSH key pair either globally via CCDB or locally on a specific cluster?"
  - "What is the process for converting an OpenStack .pem key into a format compatible with PuTTY?"
  - "What are the steps to generate a new SSH key pair using PuTTYgen or MobaXTerm?"
  - "How can a user install the public part of their SSH key pair either globally via CCDB or locally on a specific cluster?"
  - "What is the process for converting an OpenStack .pem key into a format compatible with PuTTY?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Parent page: [SSH](ssh.md)*

## Generating a Key Pair

The process of generating a key is nearly the same whether you are using PuTTY or MobaXTerm.

- With MobaXTerm, go to the menu item Tools->MobaKeyGen (SSH key generator).
- With PuTTY, run the PuTTYGen executable.

Both of these methods will cause a window to be displayed which can be used to generate a new key or to load an existing key.
The PuTTY window is illustrated in the original documentation. The MobaXTerm window looks almost exactly the same.

1.  For "Type of key to generate" select "Ed25519". (Type "RSA" is also acceptable, but set the "Number of bits" to 2048 or greater.)
2.  Click the "Generate" button. You will then be asked to move your mouse around to generate random data to be used to create the key.
3.  Enter a passphrase for your key.
    !!! important
        Remember this passphrase. You will need it every time you reload PuTTY or MobaXTerm to use this key pair.
4.  Click "Save private key" and choose a meaningful file name; the extension `.ppk` is added to the file name (e.g., `compute_canada.ppk`).
5.  Click "Save public key". It is conventional to save the public key with the same name as the private key, but here, the extension is `.pub`.

## Installing the Public Part of the Key Pair

### Installing via CCDB

We encourage you to register your SSH public key with the CCDB. This will let you use it to log in to any of our HPC clusters. Copy the contents of the box titled "Public key for pasting into OpenSSH ..." and paste it into the box at [CCDB -> Manage SSH Keys](https://ccdb.computecanada.ca/ssh_authorized_keys). For more about this, see [SSH Keys: Using CCDB](ssh-keys.md#using-ccdb).

### Installing Locally

If for some reason you do not want to use the CCDB method, you may upload your public key onto *each* cluster as follows:

1.  Copy the contents of the box titled "Public key for pasting into OpenSSH ..." and paste it as a single line at the end of `/home/USERNAME/.ssh/authorized_keys` on the cluster you wish to connect to.
2.  Ensure the permissions and ownership of the `~/.ssh` directory and files therein are correct, as described in [these instructions](using-ssh-keys-in-linux.md#installing-locally).

You may also use `ssh-copy-id` for this purpose, if it is available on your personal computer.

## Connecting Using a Key Pair

Test the new key by connecting to the server using SSH.
See [connecting with PuTTY using a key pair](connecting-with-putty.md#using-a-key-pair); [connecting with MobaXTerm using a key pair](connecting-with-mobaxterm.md#using-a-key-pair); or [connecting with WinSCP](https://winscp.net/eng/docs/ui_login_authentication).

Key generation and usage with PuTTY is demonstrated in this video: [Easily setup PuTTY SSH keys for passwordless logins using Pageant](https://www.youtube.com/watch?v=2nkAQ9M6ZF8).

## Converting an OpenStack Key

When a key is created on [OpenStack](managing-your-cloud-resources-with-openstack.md) you obtain a key with a ".pem" extension. This key can be converted to a format used by PuTTY by clicking the "Load" button in PuTTYGen. Then select the "All Files (*.*)" filter, select the ".pem" file you downloaded from OpenStack, and click "Open". You should also add a "Key passphrase" at this point to use when accessing your private key and then click "Save private key".

This private key can be used with PuTTY to connect to a VM created with OpenStack. For more about this, see "Launching a VM" on the [Cloud Quick Start](cloud-quick-start.md) page.