---
title: "Connecting with PuTTY"
slug: "connecting_with_putty"
lang: "base"

source_wiki_title: "Connecting with PuTTY"
source_hash: "93d0de84c1fa2b08414f3ab40fa75113"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T05:49:43.321388+00:00"

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

Start up [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/) and enter the host name or IP address of the machine you wish to connect to. You may also save a collection of settings by entering a session name in the *Save Sessions* text box and clicking the *Save* button. You can set the username to use when logging into a particular host under the *Connection->Data* section in the *Auto-login username* text box to save typing the username when connecting.

## X11 forwarding
If working with graphical-based programs, X11 forwarding should be enabled. To do this, go to *Connection->SSH->X11* and check the *Enable X11 forwarding* checkbox. To use X11 forwarding one must install an X window server such as [Xming](http://www.straightrunning.com/xmingnotes/) or, for the recent versions of Windows, [VcXsrv](https://sourceforge.net/projects/vcxsrv/).

!!! important
    The X window server should be actually started prior to connecting with SSH.

Test that X11 forwarding is working by opening a PuTTY session and running a simple GUI-based program, such as typing the command `xclock`. If you see a popup window with a clock, X11 forwarding should be working.

## Using a key pair
To set the private key PuTTY uses when connecting to a machine, go to Connection->SSH->Auth and click the *Browse* button to find the private key file to use. PuTTY uses files with a *.ppk* suffix, which are generated using PuTTYGen (see [Generating SSH keys in Windows](generating-ssh-keys-in-windows.md) for instructions on how to create such a key).

In newer versions of PuTTY, you need to click the "+" sign next to *Auth* and then select *Credentials* to be able to browse for the *Private key file for authentication*.

!!! note
    The additional fields in that newer interface, i.e., *Certificate to use* and *Plugin to provide authentication response*, should be left blank.