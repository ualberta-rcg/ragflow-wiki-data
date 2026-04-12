---
title: "Large Language Models (LLMs)"
slug: "large_language_models__llms"
lang: "base"

source_wiki_title: "Large Language Models (LLMs)"
source_hash: "029ca2850a42f1dbbf2489740a0eb6d9"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:28:43.603286+00:00"

tags:
  []

keywords:
  - "Large Language Models"
  - "huggingface_hub"
  - "Inference"
  - "Hugging Face Hub"
  - "Training"

questions:
  - "What are Large Language Models (LLMs) and what types of workloads does this guide help users set up?"
  - "Which repository and Python package are recommended for downloading models?"
  - "Why is it necessary to set the HF_HUB_DISABLE_XET variable when downloading models on this system?"
  - "What are Large Language Models (LLMs) and what types of workloads does this guide help users set up?"
  - "Which repository and Python package are recommended for downloading models?"
  - "Why is it necessary to set the HF_HUB_DISABLE_XET variable when downloading models on this system?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Large Language Models (LLMs) are generative models capable of generating sophisticated natural language text and can be used to power conversational systems. On this page, you will find resources and tutorials on how to set up and run LLM training or inference workloads on our systems.

## Downloading Models

At the time of this writing, [The Hugging Face Hub](https://huggingface.co/models) is the most common repository for LLMs.

The `huggingface_hub` Python package contains a command-line interface (CLI) which can be used to download models. For example, to download the model `Zephyr-7b-beta`, first install `huggingface_hub` in a [virtual environment](../python.md), then **on a login node** run:

```bash
HF_HUB_DISABLE_XET=1 hf download --max-workers=1 HuggingFaceH4/zephyr-7b-beta
```

!!! warning "Disable `hf_xet`"
    We set the variable `HF_HUB_DISABLE_XET` to avoid using the `hf_xet` package to download models. This package, meant to make downloading artifacts from the Hugging Face Hub more efficient, currently leads to failures on our systems and should not be used at this time.

For more options, please see our article on the [Hugging Face](huggingface.md) ecosystem.

## Inference

## Training