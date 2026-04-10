---
title: "Diskusage Explorer"
tags:
  []

keywords:
  []
---

==Content of folders== 

<span style="color:red">Warning: This tool is currently only available on [Narval](narval-en.md).</span>

You can get a breakdown by folder of how the disk space is being consumed in your /home, /scratch and /project spaces. That information is currently updated once a day and is stored in an [SQLite](sqlite.md) format for fast access. 

Here is how to explore your disk consumption, using the example of /project space `def-professor` as the particular directory to investigate.

### ncurse user interface 
Choose a /project space you have access to and want to analyze; for the purpose of this discussion we will use <tt>def-professor</tt>.

```bash
diskusage_explorer /project/def-professor
```

This command loads a browser that shows the resources consumed by all files under any directory tree.
[thumb|using|450px|frame|left| Navigating your project space with duc's ncurse tool](file:ncurse-duc.png.md)
<br clear=all> <!-- This is to prevent the next section from filling to the right of the image. -->

Type `c` to toggle between consumed disk space and the number of files, `q` or <code><esc></code> to quit and `h` for help.

If you are only interested in a subdirectory of this /project space and do not want to navigate the whole tree in the ncurse user interface, use 

```bash
diskusage_explorer /project/def-professor/subdirectory/
```

A complete manual page is available with the `man duc` command.

=== Graphical user interface === 

Note that when the login node is especially busy or if you have an especially large number of files in your /project space, the graphical interface mode can be slow and choppy. For a better experience, you can read the section below to run `diskusage_explorer` on your own machine.

Note that we recommend the use of the standard text-based ncurse mode on our cluster login nodes but `diskusage_explorer` does also include a nice graphical user interface (GUI). 

First, make sure that you are connected to the cluster in such a way that [SSH](ssh.md) is capable of correctly displaying GUI applications. You can then use a graphical interface by means of the command,

```bash
duc gui -d /project/.duc_databases/def-professor.sqlite  /project/def-professor
```

You can navigate the folders with the mouse and still type `c` to toggle between the size of the files and the number of files.

[thumb|using|450px|frame|left|Navigating your project space with duc's GUI tool](file:duc-gui-navigation.gif.md)
<br clear=all> <!-- This is to prevent the next section from filling to the right of the image. -->

=== Browse faster on your own machine === 

First, [install the diskusage_explorer software](http://duc.zevv.nl/#download) on your local machine and then, still on your local machine, download the SQLite file from your cluster and run `duc`.  

<pre>
rsync -v --progress username@beluga.calculcanada.ca:/project/.duc_databases/def-professor.sqlite  .
duc gui -d ./def-professor.sqlite  /project/def-professor
</pre>

This immediately leads to a smoother and more satisfying browsing experience.