---
title: "SpaCy/en"
tags:
  - software
  - ai-and-machine-learning

keywords:
  []
---

[spaCy](https://spacy.io/) is a Python package that provides industrial-strength natural language processing.

= Installation =

## Latest available wheels

To see the latest version of <tt>spaCy</tt> that we have built:

```bash
avail_wheels spacy thinc thinc_gpu_ops
```

For more information on listing wheels, see [listing available wheels](python#listing_available_wheels.md).

## Pre-build

The preferred option is to install it using the python [wheel](https://pythonwheels.com/) that we compile, as follows: 
:1. Load python 3.6 module: <tt>python/3.6</tt>
:2. Create and activate a [virtual environment](python#creating_and_using_a_virtual_environment.md).
:3. Install <tt>spaCy</tt> in the virtual environment with `pip install`. For both GPU and CPU support:
:
```bash
pip install spacy[cuda] --no-index
```

:If you only need CPU support:
:
```bash
pip install spacy --no-index
```

**GPU version**: At the present time, in order to use the GPU version you need to add the CUDA libraries to <tt>LD_LIBRARY_PATH</tt>:

```bash

```
$CUDA_HOME/lib64:$LD_LIBRARY_PATH
}}

If you want to use the [Pytorch](https://docs.computecanada.ca/wiki/PyTorch) wrapper with <tt>thinc</tt>, you'll also need to install the <tt>torch_cpu</tt> or  <tt>torch_gpu</tt> wheel.