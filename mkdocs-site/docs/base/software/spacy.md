---
title: "SpaCy"
slug: "spacy"
lang: "base"

source_wiki_title: "SpaCy"
source_hash: "1de0ebb5277e978483e5e4ec94908e20"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T11:22:33.543628+00:00"

tags:
  - software
  - ai-and-machine-learning

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

[spaCy](https://spacy.io/) is a Python package that provides industrial-strength natural language processing.

## Installation

### Latest available wheels

To see the latest version of `spaCy` that we have built:

```bash
avail_wheels spacy thinc thinc_gpu_ops
```

For more information on listing wheels, see [listing available wheels](python.md#listing-available-wheels).

### Pre-build

The preferred option is to install it using the python [wheel](https://pythonwheels.com/) that we compile, as follows:

1.  Load python 3.6 module: `python/3.6`
2.  Create and activate a [virtual environment](python.md#creating-and-using-a-virtual-environment).
3.  Install `spaCy` in the virtual environment with `pip install`. For both GPU and CPU support:
    ```bash
    pip install spacy[cuda] --no-index
    ```
    If you only need CPU support:
    ```bash
    pip install spacy --no-index
    ```

**GPU version**: At the present time, in order to use the GPU version you need to add the CUDA libraries to `LD_LIBRARY_PATH`:

```bash
module load gcc/5.4.0 cuda/9
export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH
```

If you want to use the [Pytorch](https://docs.computecanada.ca/wiki/PyTorch) wrapper with `thinc`, you'll also need to install the `torch_cpu` or `torch_gpu` wheel.