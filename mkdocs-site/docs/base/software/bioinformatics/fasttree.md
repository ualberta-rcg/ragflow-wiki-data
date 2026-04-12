---
title: "FastTree"
slug: "fasttree"
lang: "base"

source_wiki_title: "FastTree"
source_hash: "fab9c10c02a48051f7dae7b712fe5916"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:02:36.683888+00:00"

tags:
  []

keywords:
  - "FastTree"
  - "phylogenetic trees"
  - "double precision"
  - "maximum-likelihood"
  - "sequence alignments"

questions:
  - "What is the primary function of FastTree and what scale of sequence alignments can it handle?"
  - "Under what circumstances is it recommended to use the double precision module instead of the single precision module?"
  - "How can a user resolve the warning message indicating that the alignment consists of closely-related and very long sequences?"
  - "What is the primary function of FastTree and what scale of sequence alignments can it handle?"
  - "Under what circumstances is it recommended to use the double precision module instead of the single precision module?"
  - "How can a user resolve the warning message indicating that the alignment consists of closely-related and very long sequences?"

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

* !!! warning "Error message: WARNING! This alignment consists of closely-related and very long sequences"
    This likely results in very short and sometimes negative branch lengths. Use a `fasttree-double` module for double precision.

## References

* [FastTree Web page](https://morgannprice.github.io/fasttree/)