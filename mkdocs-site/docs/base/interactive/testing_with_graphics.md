---
title: "Testing With Graphics"
slug: "testing_with_graphics"
lang: "base"

source_wiki_title: "Testing With Graphics"
source_hash: "bc9a03ba7249ab7ad0ef286c24a872c8"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T11:51:19.788094+00:00"

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

If you need to use graphics while testing your code, e.g. when using a debugger such as DDT or DDD, you have the following options:

## Use the debugjob command

* You can use the `debugjob` command which automatically provides X-forwarding support.

```bash
$ ssh  niagara.scinet.utoronto.ca -X

USER@nia-login07:~$ debugjob
debugjob: Requesting 1 nodes for 60 minutes
xalloc: Granted job allocation 189857
xalloc: Waiting for resource configuration
xalloc: Nodes nia0030 are ready for job

[USER@nia1265 ~]$
```

## Use the regular queue

* If `debugjob` is not suitable for your case due to the limitations either on time or resources (see above [Testing](#testing)), then you have to follow these steps:

!!! note

    You will need two terminals in order to achieve this:

    1. In the 1st terminal
        * ssh to `niagara.scinet.utoronto.ca` and issue your `salloc` command
        * wait until your resources are allocated and you are assigned the nodes
        * take note of the node where you are logged to, i.e., the head node, let's say `niaWXYZ`

    ```bash
    $ ssh  niagara.scinet.utoronto.ca
    USER@nia-login07:~$ salloc --nodes 5 --time=2:00:00

    .salloc: Granted job allocation 141862
    .salloc: Waiting for resource configuration
    .salloc: Nodes nia1265 are ready for job

    [USER@nia1265 ~]$
    ```

    2. On the second terminal:
        * ssh into `niagara.scinet.utoronto.ca` now using the `-X` flag in the ssh command
        * after that `ssh -X niaWXYZ`, i.e., you will ssh carrying on the `-X` flag into the head node of the job
        * in the `niaWXYZ` you should be able to use graphics and should be redirected by x-forwarding to your local terminal

    ```bash
    ssh niagara.scinet.utoronto.ca -X
    USER@nia-login07:~$ ssh -X nia1265
    [USER@nia1265 ~]$ xclock   ## just an example to test the graphics, a clock should pop up, close it to exit
    [USER@nia1265 ~]$ module load ddt  ## load corresponding modules, eg. for DDT
    [USER@nia1265 ~]$ ddt  ## launch DDT, the GUI should appear in your screen
    ```

!!! tip "Observations"

    * If you are using ssh from a Windows machine, you need to have an X-server; a good option is to use MobaXterm, which already includes an X-server.
    * If you are in Mac OS, substitute `-X` by `-Y`.
    * Instead of using two terminals, you could just use `screen` to request the resources and then detach the session and ssh into the head node directly.