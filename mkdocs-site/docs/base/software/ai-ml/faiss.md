---
title: "Faiss"
slug: "faiss"
lang: "base"

source_wiki_title: "Faiss"
source_hash: "a33891f17e5301ef21c227cc2d17939c"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T06:18:27.931950+00:00"

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

[Faiss](https://github.com/facebookresearch/faiss/wiki) is a library for efficient similarity search and clustering of dense vectors. It contains algorithms that search in sets of vectors of any size, up to ones that possibly do not fit in RAM. It also contains supporting code for evaluation and parameter tuning. Faiss is written in C++ with complete wrappers for Python (versions 2 and 3). Some of the most useful algorithms are implemented on GPU. It is developed primarily at [Meta AI Research](https://research.facebook.com/) with help from external contributors.

## Python bindings
The module contains bindings for multiple Python versions.
To discover which are the compatible Python versions, run:
```bash
module spider faiss/X.Y.Z
```
Or search directly *faiss-cpu*, by running:
```bash
module spider faiss-cpu/X.Y.Z
```
where `X.Y.Z` represent the desired version.

### Usage
1. Load the required modules.
```bash
module load StdEnv/2023 gcc cuda faiss/X.Y.Z python/3.11
```
where `X.Y.Z` represent the desired version.

2. Import Faiss.
```bash
python -c "import faiss"
```

!!! note
    If the command displays nothing, the import was successful.

#### Available Python packages
Other Python packages depend on `faiss-cpu` or `faiss-gpu` bindings in order to be installed.
The `faiss` module provides:
* `faiss`
* `faiss-gpu`
* `faiss-cpu`

```bash
pip list | fgrep faiss
```
Output:
```
faiss-gpu                          1.7.4
faiss-cpu                          1.7.4
faiss                              1.7.4
```

With the `faiss` module loaded, package dependency for the above extensions will be satisfied.