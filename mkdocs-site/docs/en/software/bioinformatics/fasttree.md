---
title: "FastTree/en"
slug: "fasttree"
lang: "en"

source_wiki_title: "FastTree/en"
source_hash: "85ec7c389b3e14f8fe7ec5f645deaa8d"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:02:46.654379+00:00"

tags:
  []

keywords:
  - "FastTree"
  - "phylogenetic trees"
  - "double precision"
  - "maximum-likelihood"
  - "sequence alignments"

questions:
  - "What is the primary function of the FastTree software and what scale of data can it handle?"
  - "What are the differences between the single precision and double precision modules, and when is double precision recommended?"
  - "How should a user resolve the warning message regarding alignments with closely-related and very long sequences?"
  - "What is the primary function of the FastTree software and what scale of data can it handle?"
  - "What are the differences between the single precision and double precision modules, and when is double precision recommended?"
  - "How should a user resolve the warning message regarding alignments with closely-related and very long sequences?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[FastTree](https://morgannprice.github.io/fasttree/) infers approximately-maximum-likelihood phylogenetic trees from alignments of nucleotide or protein sequences. FastTree can handle alignments with up to a million sequences in a reasonable amount of time and memory.

## Environment modules

We offer software modules for single precision and double precision calculations. Single precision is faster while double precision is more precise. Double precision is recommended when using a highly biased transition matrix, or if you want to resolve very short branches accurately.

To see the available FastTree modules:

```bash
module spider fasttree
```

To load a single precision module:

```bash
module load fasttree/2.1.11
```

To load a double precision module:

```bash
module load fasttree-double/2.1.11
```

## Troubleshooting

!!! warning "Warning: Closely-related and very long sequences"
    If you encounter the warning message "WARNING! This alignment consists of closely-related and very long sequences", this likely results in very short and sometimes negative branch lengths. To resolve this, use a `fasttree-double` module for double precision calculations.

## References

*   [FastTree Web page](https://morgannprice.github.io/fasttree/)