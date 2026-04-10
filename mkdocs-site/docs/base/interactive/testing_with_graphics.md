---
title: "Testing With Graphics"
tags:
  []

keywords:
  []
---

If you need to use graphics while testing your code, e.g. when using a debugger such as DDT or DDD, you have the following options:

= Use the debugjob command = 
<ul>
<li> You can use the `debugjob` command which automatically provides X-forwarding support.
<source lang="bash">
$ ssh  niagara.scinet.utoronto.ca -X

USER@nia-login07:~$ debugjob
debugjob: Requesting 1 nodes for 60 minutes
xalloc: Granted job allocation 189857
xalloc: Waiting for resource configuration
xalloc: Nodes nia0030 are ready for job

[USER@nia1265 ~]$
</source>

= Use the regular queue = 
<li> If `debugjob` is not suitable for your case due to the limitations either on time or resources (see above [#Testing](#testing.md)), then you have to follow these steps:

You will need two terminals in order to achieve this:
<ol>
<li>In the 1st terminal
<ul>
<li> ssh to `niagara.scinet.utoronto.ca` and issue your `salloc` command
<li> wait until your resources are allocated and you are assigned the nodes
<li> take note of the node where you are logged to, ie. the head node, let's say `niaWXYZ`
</ul>
<source lang="bash">
$ ssh  niagara.scinet.utoronto.ca
USER@nia-login07:~$ salloc --nodes 5 --time=2:00:00

.salloc: Granted job allocation 141862
.salloc: Waiting for resource configuration
.salloc: Nodes nia1265 are ready for job

[USER@nia1265 ~]$
</source>

<li> On the second terminal:
<ul>
<li> ssh into `niagara.scinet.utoronto.ca` now using the `-X` flag in the ssh command

<li> after that `ssh -X niaWXYZ`, ie. you will ssh carrying on the '-X' flag into the head node of the job

<li> in the `niaWXYZ` you should be able to use graphics and should be redirected by x-forwarding to your local terminal
</ul>

<source lang="bash">
ssh niagara.scinet.utoronto.ca -X
USER@nia-login07:~$ ssh -X nia1265
[USER@nia1265 ~]$ xclock   ## just an example to test the graphics, a clock should pop up, close it to exit
[USER@nia1265 ~]$ module load ddt  ## load corresponding modules, eg. for DDT
[USER@nia1265 ~]$ ddt  ## launch DDT, the GUI should appear in your screen
</source>

</ol>
</ul>

Observations:
<ul>
<li> If you are using ssh from a Windows machine, you need to have an X-server, a good option is to use MobaXterm, that already brings an X-server included.
<li> If you are in Mac OS, substitute -X by -Y
<li> Instead of using two terminals, you could just use `screen` to request the resources and then detach the session and ssh into the head node directly.
</ul>