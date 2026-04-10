---
title: "Available Python wheels"
tags:
  []

keywords:
  []
---

A current list of the [Python wheels](https://pythonwheels.com/) available from the wheelhouse on our national systems is presented below. This list changes as new wheels are added. You can request the installation or update of a particular wheel by contacting [technical support](technical-support.md).
__TOC__

= Listing wheel from modules =
Some wheels may not be listed, as they are part of modules. For example:
* [pyarrow (Arrow)](arrow#pyarrow.md)
* pyqt5 (QT)
* petsc4py (PETSc)
* [opencv_python (OpenCV)](opencv#python_bindings.md)

You can search for such extension with:

```bash
module spider <python package>
```

= Listing wheel from current software environment =
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

= Available wheels across all software environments = 

<tabs>
<tab name="Python 3.14">
 
</tab>
<tab name="Python 3.13">
 
</tab>
<tab name="Python 3.12">
 
</tab>
<tab name="Python 3.11">
 
</tab>
<tab name="Python 3.10">
 
</tab>
<tab name="Python 3.9 (no longer supported)">
 
</tab>
<tab name="Python 3.8 (no longer supported)">
 
</tab>
</tabs>