---
title: "Available Python wheels/en"
slug: "available_python_wheels"
lang: "en"

source_wiki_title: "Available Python wheels/en"
source_hash: "a4a5fa8a8ddc49537f75e772bb3d908d"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:37:52.028736+00:00"

tags:
  []

keywords:
  - "wheelhouse"
  - "StdEnv"
  - "Python wheels"
  - "avail_wheels"
  - "modules"

questions:
  - "How can a user request the installation or update of a specific Python wheel?"
  - "What command should be used to check if a specific wheel is available in the currently loaded software environment?"
  - "How can a user search for Python wheels that are provided as part of system modules rather than the standard wheelhouse?"
  - "How can a user request the installation or update of a specific Python wheel?"
  - "What command should be used to check if a specific wheel is available in the currently loaded software environment?"
  - "How can a user search for Python wheels that are provided as part of system modules rather than the standard wheelhouse?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

A current list of the [Python wheels](https://pythonwheels.com/) available from the wheelhouse on our national systems is presented below. This list changes as new wheels are added. You can request the installation or update of a particular wheel by contacting [technical support](technical-support.md).

!!! warning "Availability"
    **Some wheels may not be available in the specific StdEnv you have loaded.**

    To find out which wheels can be installed in your active StdEnv, use the `avail_wheels` command described in [Available wheels](python.md#available-wheels).

## Listing wheels from modules
Some wheels may not be listed, as they are part of modules. For example:
*   [pyarrow (Arrow)](arrow.md#pyarrow)
*   pyqt5 (QT)
*   petsc4py (PETSc)
*   [opencv_python (OpenCV)](opencv.md#python-bindings)

You can search for such extension with:
```bash
module spider <python package>
```

## Listing wheels from current software environment
1.  Load the software environment.
    ```bash
    module load StdEnv/YYYY
    ```
    where `YYYY` is `2020` or `2023`

2.  Look for a specific wheel.
    ```bash
    avail_wheels <name>
    ```
    where `name` is the name the wheel you are looking for.

## Available wheels across all software environments

=== "Python 3.14"

=== "Python 3.13"

=== "Python 3.12"

=== "Python 3.11"

=== "Python 3.10"

=== "Python 3.9 (no longer supported)"

=== "Python 3.8 (no longer supported)"