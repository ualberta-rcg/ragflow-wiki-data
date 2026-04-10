---
title: "Available Python wheels/en"
slug: "available_python_wheels"
lang: "en"

source_wiki_title: "Available Python wheels/en"
source_hash: "a4a5fa8a8ddc49537f75e772bb3d908d"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T04:46:37.606639+00:00"

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

A current list of the [Python wheels](https://pythonwheels.com/) available from the wheelhouse on our national systems is presented below. This list changes as new wheels are added. You can request the installation or update of a particular wheel by contacting [technical support](technical-support.md).

!!! warning "Availability"
    **Some wheels may not be available in the specific StdEnv you have loaded.**

    To find out which wheels can be installed in your active StdEnv, use the `avail_wheels` command described in [Available wheels](python.md#available-wheels).

## Listing wheel from modules
Some wheels may not be listed, as they are part of modules. For example:
* [pyarrow (Arrow)](arrow.md#pyarrow)
* pyqt5 (QT)
* petsc4py (PETSc)
* [opencv_python (OpenCV)](opencv.md#python-bindings)

You can search for such an extension with:
```bash
module spider <python package>
```

## Listing wheel from current software environment
1. Load the software environment.
```bash
module load StdEnv/YYYY
```
   where `YYYY` is `2020` or `2023`

2. Look for a specific wheel.
```bash
avail_wheels <name>
```
   where `name` is the name of the wheel you are looking for.

## Available wheels across all software environments

=== "Python 3.14"

    *(Content from Wheels3.14 would be transcluded here)*

=== "Python 3.13"

    *(Content from Wheels3.13 would be transcluded here)*

=== "Python 3.12"

    *(Content from Wheels3.12 would be transcluded here)*

=== "Python 3.11"

    *(Content from Wheels3.11 would be transcluded here)*

=== "Python 3.10"

    *(Content from Wheels3.10 would be transcluded here)*

=== "Python 3.9 (no longer supported)"

    *(Content from Wheels3.9 would be transcluded here)*

=== "Python 3.8 (no longer supported)"

    *(Content from Wheels3.8 would be transcluded here)*