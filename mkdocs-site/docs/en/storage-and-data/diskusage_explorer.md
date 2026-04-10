---
title: "Diskusage Explorer/en"
slug: "diskusage_explorer"
lang: "en"

source_wiki_title: "Diskusage Explorer/en"
source_hash: "a9c21c6191be2eb65bb867cbd89b4613"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T06:09:57.849125+00:00"

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

## Content of folders

!!! warning
    This tool is currently only available on [Narval](narval.md).

You can get a breakdown by folder of how the disk space is being consumed in your /home, /scratch, and /project spaces. That information is currently updated once a day and is stored in an [SQLite](sqlite.md) format for fast access.

Here is how to explore your disk consumption, using the example of /project space `def-professor` as the particular directory to investigate.

### ncurse user interface
Choose a /project space you have access to and want to analyze; for the purpose of this discussion we will use `def-professor`.

```bash
diskusage_explorer /project/def-professor
```

This command loads a browser that shows the resources consumed by all files under any directory tree.

Type `c` to toggle between consumed disk space and the number of files, `q` or `<esc>` to quit, and `h` for help.

If you are only interested in a subdirectory of this /project space and do not want to navigate the whole tree in the ncurse user interface, use:

```bash
diskusage_explorer /project/def-professor/subdirectory/
```

A complete manual page is available with the `man duc` command.

### Graphical user interface

!!! note
    When the login node is especially busy or if you have an especially large number of files in your /project space, the graphical interface mode can be slow and choppy. For a better experience, you can read the section below to run `diskusage_explorer` on your own machine.

!!! note
    We recommend the use of the standard text-based ncurse mode on our cluster login nodes, but `diskusage_explorer` does also include a nice graphical user interface (GUI).

First, make sure that you are connected to the cluster in such a way that [SSH](ssh.md) is capable of correctly displaying GUI applications. You can then use a graphical interface by means of the command:

```bash
duc gui -d /project/.duc_databases/def-professor.sqlite /project/def-professor
```

You can navigate the folders with the mouse and still type `c` to toggle between the size of the files and the number of files.

### Browse faster on your own machine

First, [install the diskusage_explorer software](http://duc.zevv.nl/#download) on your local machine and then, still on your local machine, download the SQLite file from your cluster and run `duc`.

```bash
rsync -v --progress username@beluga.calculcanada.ca:/project/.duc_databases/def-professor.sqlite .
duc gui -d ./def-professor.sqlite /project/def-professor
```

This immediately leads to a smoother and more satisfying browsing experience.