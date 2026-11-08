---
title: "Available Python wheels/en"
slug: "available_python_wheels"
lang: "en"

source_wiki_title: "Available Python wheels/en"
source_hash: "cade787eb3dfbe83c070195256d0a7b5"
last_synced: "2026-11-08T02:07:32.985064+00:00"
last_processed: "2026-11-08T02:48:58.234259+00:00"

tags:
  []

keywords:
  - "module spider"
  - "Wheels3.15"
  - "avail_wheels"
  - "StdEnv"
  - "Python wheels"

questions:
  - "How can I determine which Python wheels are available in my active StdEnv?"
  - "Which command should I use to list wheels that belong to loaded modules rather than the wheelhouse?"
  - "What is the procedure to request installation or an update of a particular wheel that is not listed?"

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

You can search for such extensions with:
```bash
module spider <python package>
```

## Listing wheels from your current software environment

1.  Load the software environment.
    ```bash
    module load StdEnv/YYYY
    ```
    where `YYYY` is `2026` or `2023`.

2.  Look for a specific wheel.
    ```bash
    avail_wheels <name>
    ```
    where `name` is the name of the wheel you are looking for.

## Available wheels across all software environments

You can find lists of available Python wheels for specific Python versions by following these links:

*   Python 3.15
*   Python 3.14
*   Python 3.13
*   Python 3.12
*   Python 3.11
*   Python 3.10