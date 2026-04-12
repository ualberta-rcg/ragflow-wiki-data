---
title: "Slicer/en"
slug: "slicer"
lang: "en"

source_wiki_title: "Slicer/en"
source_hash: "50239608fe7d75329c10f574e6af954b"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:31:16.849477+00:00"

tags:
  - software

keywords:
  - "X11 forwarding"
  - "batch processing"
  - "interactive node"
  - "3D Slicer"
  - "medical image informatics"

questions:
  - "What is 3D Slicer and what is the critical restriction regarding its use on login nodes?"
  - "What are the necessary steps and requirements to properly run the 3D Slicer GUI on an interactive node?"
  - "Under what circumstances is it recommended to use 3D Slicer's command-line interface rather than the graphical user interface?"
  - "What is 3D Slicer and what is the critical restriction regarding its use on login nodes?"
  - "What are the necessary steps and requirements to properly run the 3D Slicer GUI on an interactive node?"
  - "Under what circumstances is it recommended to use 3D Slicer's command-line interface rather than the graphical user interface?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[3D Slicer](https://www.slicer.org/) is an open source software platform for medical image informatics, image processing, and three-dimensional visualization. Built over two decades through support from the National Institutes of Health and a worldwide developer community, Slicer brings free, powerful cross-platform processing tools to physicians, researchers, and the general public.

!!! warning "Important"
    Never make intense use of Slicer on the login nodes! Submit jobs using the command line whenever possible and if you must visualize your data using the GUI, please do so on an interactive node. Using parallel rendering on the shared login nodes will result in the termination of your session.

## Using the GUI
Using the Slicer GUI requires X11 forwarding, which you should make sure is enabled.

You can find information on how to connect with MobaXTerm and use X11 fowarding at [Connecting with MobaXTerm](connecting-with-mobaxterm.md).

#### Use an interactive node

Runtime is limited on the login nodes, so you should request an [interactive job](running-jobs.md#interactive-jobs) to have more time for exploring and visualizing your data. Additionally, by doing so, you will be able to use more cores for faster processing.

Request an interactive job, ie.
```bash
[name@server ~]$ salloc --time=1:0:0 --ntasks=2 --x11 --account=def-someuser
```

This will connect you to a compute node. Note the `--x11` argument.

You can then load Slicer and run it on the interactive node.
```bash
module load slicer
```
```bash
Slicer
```

Once you are done and have closed Slicer, don't forget to terminate the interactive job:
```bash
exit
```

## Using the command line

If you have to perform the same task on a large number of images,
or if you don't need to see the processed images as they are created,
you should use the command line interface and batch processing.
For examples see
* https://discourse.slicer.org/t/rtstruct-to-label-map/2437
* https://discourse.slicer.org/t/slicer-batch-processing-question-no-main-window-python-script/1863