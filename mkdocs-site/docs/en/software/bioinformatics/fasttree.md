---
title: "FastTree/en"
slug: "fasttree"
lang: "en"

source_wiki_title: "FastTree/en"
source_hash: "85ec7c389b3e14f8fe7ec5f645deaa8d"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T06:19:19.121126+00:00"

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

*   Error message *WARNING! This alignment consists of closely-related and very long sequences*: This likely results in very short and sometimes negative branch lengths. Use a `fasttree-double` module for double precision.

## References

*   [FastTree Web page](https://morgannprice.github.io/fasttree/)