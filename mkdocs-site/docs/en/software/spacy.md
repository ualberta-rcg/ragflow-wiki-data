---
title: "SpaCy/en"
slug: "spacy"
lang: "en"

source_wiki_title: "SpaCy/en"
source_hash: "c21c08119ab8efbe93423816f903b262"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:33:02.723875+00:00"

tags:
  - software
  - ai-and-machine-learning

keywords:
  - "natural language processing"
  - "spaCy"
  - "Python"
  - "installation"
  - "GPU support"

questions:
  - "What is spaCy and how can users check the latest available versions of the package?"
  - "What are the recommended steps to install spaCy in a Python virtual environment for either CPU or GPU support?"
  - "What additional environment configurations and library installations are required to use the GPU version of spaCy and its PyTorch wrapper?"
  - "What is spaCy and how can users check the latest available versions of the package?"
  - "What are the recommended steps to install spaCy in a Python virtual environment for either CPU or GPU support?"
  - "What additional environment configurations and library installations are required to use the GPU version of spaCy and its PyTorch wrapper?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[spaCy](https://spacy.io/) is a Python package that provides industrial-strength natural language processing.

## Installation

### Latest available wheels

To see the latest version of `spaCy` that we have built:
```bash
avail_wheels spacy thinc thinc_gpu_ops
```
For more information on listing wheels, see [listing available wheels](python.md).

### Pre-build

The preferred option is to install it using the Python [wheel](https://pythonwheels.com/) that we compile, as follows:
1. Load Python 3.6 module: `python/3.6`
2. Create and activate a [virtual environment](python.md#creating-and-using-a-virtual-environment).
3. Install `spaCy` in the virtual environment with `pip install`. For both GPU and CPU support:
   ```bash
   (venv) [name@server ~]$ pip install spacy[cuda] --no-index
   ```
   If you only need CPU support:
   ```bash
   (venv) [name@server ~]$ pip install spacy --no-index
   ```

**GPU version**: At the present time, in order to use the GPU version you need to add the CUDA libraries to `LD_LIBRARY_PATH`:
```bash
(venv) [name@server ~]$ module load gcc/5.4.0 cuda/9
(venv) [name@server ~]$ export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH
```

If you want to use the [Pytorch](https://docs.computecanada.ca/wiki/PyTorch) wrapper with `thinc`, you'll also need to install the `torch_cpu` or `torch_gpu` wheel.