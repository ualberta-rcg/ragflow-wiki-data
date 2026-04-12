---
title: "Testing With Graphics"
slug: "testing_with_graphics"
lang: "base"

source_wiki_title: "Testing With Graphics"
source_hash: "bc9a03ba7249ab7ad0ef286c24a872c8"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:59:03.470766+00:00"

tags:
  []

keywords:
  - "salloc"
  - "ssh"
  - "graphics"
  - "debugjob"
  - "X-forwarding"

questions:
  - "How can a user utilize the debugjob command to automatically enable X-forwarding for graphical debugging?"
  - "What are the necessary steps to set up graphics using the regular queue and the salloc command across two terminals?"
  - "What specific software or command flag adjustments are required for Windows and Mac OS users to successfully use X-forwarding?"
  - "How can a user utilize the debugjob command to automatically enable X-forwarding for graphical debugging?"
  - "What are the necessary steps to set up graphics using the regular queue and the salloc command across two terminals?"
  - "What specific software or command flag adjustments are required for Windows and Mac OS users to successfully use X-forwarding?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

If you need to use graphics while testing your code, e.g., when using a debugger such as DDT or DDD, you have the following options:

## Use the `debugjob` command

- You can use the `debugjob` command which automatically provides X-forwarding support.

```bash
$ ssh niagara.scinet.utoronto.ca -X

USER@nia-login07:~$ debugjob
debugjob: Requesting 1 nodes for 60 minutes
xalloc: Granted job allocation 189857
xalloc: Waiting for resource configuration
xalloc: Nodes nia0030 are ready for job

[USER@nia1265 ~]$
```

## Use the regular queue

!!! note
    If `debugjob` is not suitable for your case due to the limitations either on time or resources (see above [Testing](#testing)), then you have to follow these steps:

You will need two terminals in order to achieve this:

1.  In the first terminal:
    -   SSH to `niagara.scinet.utoronto.ca` and issue your `salloc` command.
    -   Wait until your resources are allocated and you are assigned the nodes.
    -   Take note of the node where you are logged into, i.e., the head node. Let's say `niaWXYZ`.

```bash
$ ssh niagara.scinet.utoronto.ca
USER@nia-login07:~$ salloc --nodes 5 --time=2:00:00

.salloc: Granted job allocation 141862
.salloc: Waiting for resource configuration
.salloc: Nodes nia1265 are ready for job

[USER@nia1265 ~]$
```

2.  On the second terminal:
    -   SSH into `niagara.scinet.utoronto.ca` now using the `-X` flag in the SSH command.
    -   After that, `ssh -X niaWXYZ`, i.e., you will SSH carrying on the `-X` flag into the head node of the job.
    -   In `niaWXYZ`, you should be able to use graphics and should be redirected by X-forwarding to your local terminal.

```bash
ssh niagara.scinet.utoronto.ca -X
USER@nia-login07:~$ ssh -X nia1265
[USER@nia1265 ~]$ xclock   ## just an example to test the graphics; a clock should pop up. Close it to exit.
[USER@nia1265 ~]$ module load ddt  ## load corresponding modules, e.g., for DDT
[USER@nia1265 ~]$ ddt  ## launch DDT; the GUI should appear on your screen
```

!!! note "Observations"
    -   If you are using SSH from a Windows machine, you need to have an X-server. A good option is to use MobaXterm, which already includes an X-server.
    -   If you are on Mac OS, substitute `-X` with `-Y`.
    -   Instead of using two terminals, you could just use `screen` to request the resources and then detach the session and SSH into the head node directly.