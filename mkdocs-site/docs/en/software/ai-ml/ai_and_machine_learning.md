---
title: "AI and Machine Learning/en"
slug: "ai_and_machine_learning"
lang: "en"

source_wiki_title: "AI and Machine Learning/en"
source_hash: "0964d1b5bf8da464ff81680504416b4e"
last_synced: "2026-04-10T14:10:18.226633+00:00"
last_processed: "2026-04-10T14:21:35.490117+00:00"

tags:
  - ai-and-machine-learning

keywords:
  - "Machine learning"
  - "Clusters"
  - "Datasets"
  - "small files"
  - "compute node"
  - "Python"
  - "Checkpointing"
  - "Job farming"
  - "Machine Learning"
  - "Experiment tracking"
  - "filesystem quotas"
  - "distributed filesystem"
  - "Storage and file management"
  - "Hyperparameter optimization"
  - "single-file archives"

questions:
  - "Why are users advised to avoid Anaconda and use virtualenv for their Python machine learning environments on the clusters?"
  - "How should a user choose the appropriate storage location and method for their dataset based on its total size?"
  - "What problems arise when working with datasets containing hundreds of thousands of small files, and how should this data be formatted to avoid them?"
  - "Why is checkpointing recommended for long-running computations, and how does it affect job scheduling priority?"
  - "What tools and strategies should be used when running and tracking many similar jobs, such as during hyperparameter search?"
  - "How can users eliminate non-deterministic behavior in cuDNN when using RNN or multi-head attention APIs?"
  - "What problems are caused by having a large number of small files on the cluster's filesystem?"
  - "How does streaming many small files from storage to a compute node impact software performance?"
  - "What is the recommended best practice for storing data on a distributed filesystem to avoid these issues?"
  - "Why is checkpointing recommended for long-running computations, and how does it affect job scheduling priority?"
  - "What tools and strategies should be used when running and tracking many similar jobs, such as during hyperparameter search?"
  - "How can users eliminate non-deterministic behavior in cuDNN when using RNN or multi-head attention APIs?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

To get the most out of our clusters for machine learning applications, special care must be taken. A cluster is a complicated beast that is very different from your local machine that you use for prototyping. Notably, a cluster uses a distributed filesystem, linking many storage devices seamlessly. Accessing a file on `/project` may *feel the same* as accessing one from the current node, but under the hood, these two IO operations have very different performance implications. In short, you need to [choose wisely where to put your data](#managing-your-datasets).

The sections below list links relevant to AI practitioners, and good practices to be observed on our clusters.

## Tutorials

A self-paced course on this topic is available from SHARCNET: [Introduction to Machine Learning](https://training.sharcnet.ca/courses/enrol/index.php?id=180).

If you are ready to port your program for using on one of our clusters, please take [our tutorial](tutoriel-apprentissage-machine.md).

A user-made tutorial showing all the steps necessary for setting up your local and Alliance environments for deep learning in Python is available [here](https://prashp.gitlab.io/post/compute-canada-tut/).

## Python

Python is very popular in the field of machine learning. If you (plan to) use it on our clusters, please refer to [our documentation about Python](python.md) to get important information about Python versions, virtual environments on login or on compute nodes, `multiprocessing`, Anaconda, Jupyter, etc.

### Avoid Anaconda

!!! warning "Avoid Anaconda"
    We ask our users to avoid using Anaconda, and use virtualenv instead. Reasons are explained on the [Anaconda](anaconda.md) page.

!!! tip "Switching to virtualenv is easy"
    Just install all the same packages, except CUDA, CuDNN and other low-level libraries, which are already installed on our clusters.

## Useful information about software packages

Please refer to the page of your machine learning package of choice for useful information about how to install, common pitfalls, etc.:

*   [TensorFlow](tensorflow.md)
*   [PyTorch](pytorch.md)
*   [Keras](keras.md)
*   [Torch](torch.md)
*   [SpaCy](spacy.md)
*   [Scikit-Learn](large-scale-machine-learning-big-data.md#scikit-learn)
*   [SnapML](large-scale-machine-learning-big-data.md#snap-ml)

## Managing your datasets

### Storage and file management

Our clusters have a wide range of storage options to cover the needs of our very diverse users. These storage solutions range from high-speed temporary local storage to different kinds of long-term storage, so you can choose the storage medium that best corresponds to your needs and usage patterns. Please refer to our documentation on [Storage and file management](storage-and-file-management.md).

### Choosing the right storage type for your dataset

*   If your dataset is around 10 GB or less, it can probably fit in the memory, depending on how much memory your job has. You should not read data from disk during your machine learning tasks.
*   If your dataset is around 100 GB or less, it can fit in the local storage of the compute node; please transfer it there at the beginning of the job. This storage is orders of magnitude faster and more reliable than shared storage (home, project, scratch). A temporary directory is available for each job at `$SLURM_TMPDIR`. An example is given in [our tutorial](tutoriel-apprentissage-machine.md). A caveat of local node storage is that a job from another user might be using it fully, leaving you no space (we are currently studying this problem). However, you might also get lucky and have a whole terabyte at your disposal.
*   If your dataset is larger, you may have to leave it in the shared storage. You can leave your datasets permanently in your project space. Scratch space can be faster, but it is not for permanent storage. Also, all shared storage (home, project, scratch) is for storing and reading at low frequencies (e.g. 1 large chunk every 10 seconds, rather than 10 small chunks every second).

### Datasets containing lots of small files (e.g. image datasets)

In machine learning, it is common to have to manage very large collections of files, meaning hundreds of thousands or more. The individual files may be fairly small, e.g. less than a few hundred kilobytes.

!!! warning "Problems with small files on distributed filesystems"
    In these cases, problems arise:

    *   filesystem [quotas](storage-and-file-management.md#filesystem-quotas-and-policies) on our clusters limit the number of filesystem objects;
    *   your software could be significantly slowed down from streaming lots of small files from `/project` (or `/scratch`) to a compute node.

!!! note "Recommended format for small files"
    On a distributed filesystem, data should be stored in large single-file archives. On this subject, please refer to [Handling large collections of files](handling-large-collections-of-files.md).

## Long running computations

!!! tip "Use checkpointing for long running jobs"
    If your computations are long, you should use checkpointing. For example, if your training time is 3 days, you should split it in 3 chunks of 24 hours. This will prevent you from losing all the work in case of an outage, and give you an edge in terms of priority (more nodes are available for short jobs). Most machine learning libraries natively support checkpointing; the typical case is covered in our [tutorial](tutoriel-apprentissage-machine.md#checkpointing-a-long-running-job). If your program does not natively support this, we provide a [general checkpointing solution](points-de-controle.md).

For more examples, please see

*   [Checkpointing with PyTorch](pytorch.md#creating-model-checkpoints)
*   [Checkpointing with TensorFlow](tensorflow.md#creating-model-checkpoints)

## Running many similar jobs

If you are in one of these situations:

*   Hyperparameter search
*   Training many variants of the same method
*   Running many optimization processes of similar duration

... you should consider grouping many jobs into one. [META](meta-a-package-for-job-farming.md), [GLOST](glost.md), and [GNU Parallel](gnu-parallel.md) are available to help you with this.

## Experiment tracking and hyperparameter optimization

[Weights & Biases (wandb)](weights-biases-wandb.md) and [Comet.ml](comet-ml.md) can help you get the most out of your compute allocation, by

*   allowing easier tracking and analysis of training runs;
*   providing Bayesian hyperparameter search.

## Large-scale machine learning (big data)

Modern deep learning packages like Pytorch and TensorFlow include utilities to handle large-scale training natively and tutorials on how to do it abound. Scaling classic machine learning (i.e., not deep learning) methods, however, is not as widely discussed and can often be a frustrating problem to solve. [This guide](large-scale-machine-learning-big-data.md) contains ideas and practical options, along with tutorials, to tackle training classic ML models on very large datasets.

## Troubleshooting

### Determinism with RNN using CUDA

RNN and multi-head attention API calls may exhibit non-deterministic behaviour when the cuDNN library is built with CUDA Toolkit 10.2 or higher. The user can eliminate the non-deterministic behaviour of cuDNN RNN and multi-head attention APIs by setting a single buffer size in the `CUBLAS_WORKSPACE_CONFIG` environmental variable.

For example, to set it to `:16:8` or `:4096:2`:

```bash
export CUBLAS_WORKSPACE_CONFIG=:16:8
# or
export CUBLAS_WORKSPACE_CONFIG=:4096:2
```

This instructs cuBLAS to allocate eight buffers of 16 KB each in GPU memory or two buffers of 4 MB each.