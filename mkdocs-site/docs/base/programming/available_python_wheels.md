---
title: "Available Python wheels"
slug: "available_python_wheels"
lang: "base"

source_wiki_title: "Available Python wheels"
source_hash: "8959c6ad728ea4a0690b98da224e17da"
last_synced: "2026-11-08T02:07:32.985064+00:00"
last_processed: "2026-11-08T02:48:45.845586+00:00"

tags:
  []

keywords:
  - "module spider"
  - "avail_wheels"
  - "StdEnv"
  - "software environment"
  - "Python wheels"

questions:
  - "How can you check which Python wheels are available in the active StdEnv you have loaded?"
  - "Which command should be used to search for wheels that are part of modules rather than listed directly?"
  - "Where can you find the current lists of wheels for each supported Python version (e.g., 3.15, 3.14, 3.13, etc.)?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

A current list of the [Python wheels](https://pythonwheels.com/) available from the wheelhouse on our national systems is presented below. This list changes as new wheels are added. You can request the installation or update of a particular wheel by contacting [technical support](../support/technical_support.md).

!!! warning "Availability"
    **Some wheels may not be available in the specific StdEnv you have loaded.**

    To find out which wheels can be installed in your active StdEnv, use the `avail_wheels` command described in [Available wheels](../software/python.md#available-wheels).

## Listing wheels from modules
Some wheels may not be listed, as they are part of modules. For example:
* [pyarrow (Arrow)](../software/arrow.md#pyarrow)
* pyqt5 (QT)
* petsc4py (PETSc)
* [opencv_python (OpenCV)](../software/opencv.md#python-bindings)

You can search for such extension with:
```bash
module spider <python package>
```

## Listing wheels from current software environment
1. Load the software environment.
```bash
module load StdEnv/YYYY
```
where `YYYY` is `2026` or `2023`.

2. Look for a specific wheel.
```bash
avail_wheels <name>
```
where `name` is the name of the wheel you are looking for.

## Available wheels across all software environments

=== "Python 3.15"
    This section would list available wheels for Python 3.15.
=== "Python 3.14"
    This section would list available wheels for Python 3.14.
=== "Python 3.13"
    This section would list available wheels for Python 3.13.
=== "Python 3.12"
    This section would list available wheels for Python 3.12.
=== "Python 3.11"
    This section would list available wheels for Python 3.11.
=== "Python 3.10"
    This section would list available wheels for Python 3.10.