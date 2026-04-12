---
title: "Parabricks"
slug: "parabricks"
lang: "base"

source_wiki_title: "Parabricks"
source_hash: "089b18124db2ed10e3c161a355e3c819"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:14:23.952517+00:00"

tags:
  - bioinformatics
  - software
  - covid19_related_requests

keywords:
  - "Compute Canada"
  - "Parabricks"
  - "GPU"
  - "DNA data analysis"
  - "Next generation sequencing"

questions:
  - "What is Parabricks and how does it achieve its high-speed analysis of next-generation sequencing data?"
  - "What are the current licensing requirements for using Parabricks on Compute Canada clusters?"
  - "What are the common causes of failure when running Parabricks, and how should computational resources be allocated to prevent them?"
  - "What is Parabricks and how does it achieve its high-speed analysis of next-generation sequencing data?"
  - "What are the current licensing requirements for using Parabricks on Compute Canada clusters?"
  - "What are the common causes of failure when running Parabricks, and how should computational resources be allocated to prevent them?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Parabricks is a software suite for performing secondary analysis of next generation sequencing (NGS) DNA data. Parabricks is fast: its documentation claims that, thanks to its tight integration with GPUs, it is able to analyse 30x Whole Human Genome Sequencing (WGS) in hours as opposed to days with other techniques.

You can learn more at [www.nvidia.com/parabricks](http://www.nvidia.com/parabricks)

# Usage in Compute Canada Clusters

**This software was provided freely by NVidia to help with research on COVID19 until Sunday, 17 May 2020.**
Since this free period has expired, you must have your own license arrangement with NVidia in order to use Parabricks on Compute Canada equipment.

## Finding and loading Parabricks

Parabricks can be looked for as a regular module through module spider:

```bash
module spider parabricks
```

Likewise, it can be loaded through LMOD modules:

```bash
module load parabricks/2.5.0
```

## Example of use

Before you use Parabricks, make sure you have gone through the [Parabricks documentation](https://www.nvidia.com/en-us/docs/parabricks/), including their standalone tools and pipelines. Also make sure you know [how to request GPUs in Compute Canada clusters](../../running-jobs/using_gpus_with_slurm.md). Once you understand the above, you can submit a job like:

```bash
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --gres=gpu:1
#SBATCH --nodes=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=0
#SBATCH --time=5:00:00

module load parabricks/2.5.0

DATA_DIR=/path/to/data
OUT_DIR=/path/to/output
pbrun germline \
      --ref ${DATA_DIR}/Homo_sapiens_assembly38.fa \
      --in-fq ${DATA_DIR}/some_1.fastq ${DATA_DIR}/some_2.fastq \
      --knownSites ${DATA_DIR}/dbsnp_146.hg38.vcf.gz \
      --tmp-dir ${SLURM_TMPDIR}/ \
      --out-bam ${OUT_DIR}/output.bam \
      --out-variants ${OUT_DIR}/output.vcf \
      --out-recal-file ${OUT_DIR}/report.txt
```

!!! note
    Make the path to the files absolute real paths (i.e. with the command `realpath .`)

## Common issues

### Almost immediate failure

If your first test fails right away, there might be a missing module or some environmental variable clash. To solve this try:

```bash
module --force purge
```

```bash
module load StdEnv/2016.4 nixpkgs/16.09 parabricks/2.5.0
```

### Later failure

Often Parabricks may not give you a clear traceback of the failure. This usually means that you did not request enough memory. If you are reserving a full node already through `--nodes=1`, we suggest you also use all the memory in the node with `--mem=0`. Otherwise, make sure that your pipeline has enough memory to process your data.

## Hybrid usage

Parabricks uses both CPU and GPUs. During our tests, Parabricks used at least 10 CPUs, so we recommend to ask for at least that amount through `--cpus-per-task=10`

# References
[Parabricks Home](http://www.nvidia.com/parabricks)