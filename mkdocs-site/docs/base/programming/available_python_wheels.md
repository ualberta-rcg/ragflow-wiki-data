---
title: "Available Python wheels"
slug: "available_python_wheels"
lang: "base"

source_wiki_title: "Available Python wheels"
source_hash: "6aca1600199adef94d3b1d823814a03e"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:37:33.624672+00:00"

tags:
  []

keywords:
  - "software environment"
  - "wheelhouse"
  - "StdEnv"
  - "Python wheels"
  - "avail_wheels"

questions:
  - "How can a user request the installation or update of a specific Python wheel?"
  - "What command should be used to check which wheels are available in the currently loaded software environment?"
  - "How can users search for Python wheels that are not listed directly because they are part of other modules?"
  - "How can a user request the installation or update of a specific Python wheel?"
  - "What command should be used to check which wheels are available in the currently loaded software environment?"
  - "How can users search for Python wheels that are not listed directly because they are part of other modules?"

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

# Listing wheel from modules
Some wheels may not be listed, as they are part of modules. For example:
* [pyarrow (Arrow)](../software/arrow.md#pyarrow)
* pyqt5 (QT)
* petsc4py (PETSc)
* [opencv_python (OpenCV)](../software/opencv.md#python-bindings)

You can search for such extension with:
```bash
module spider <python package>
```

# Listing wheel from current software environment
1. Load the software environment.
```bash
module load StdEnv/YYYY
```
where `YYYY` is `2020` or `2023`

2. Look for a specific wheel.
```bash
avail_wheels <name>
```
where `name` is the name the wheel you are looking for.

# Available wheels across all software environments

=== "Python 3.14"
    {{:Wheels3.14}}
=== "Python 3.13"
    {{:Wheels3.13}}
=== "Python 3.12"
    {{:Wheels3.12}}
=== "Python 3.11"
    {{:Wheels3.11}}
=== "Python 3.10"
    {{:Wheels3.10}}
=== "Python 3.9 (no longer supported)"
    {{:Wheels3.9}}
=== "Python 3.8 (no longer supported)"
    {{:Wheels3.8}}