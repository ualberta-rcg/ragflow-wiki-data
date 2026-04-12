---
title: "Tesseract"
slug: "tesseract"
lang: "base"

source_wiki_title: "Tesseract"
source_hash: "79e327150ebe41d2c3f3c84635ac05be"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:58:30.360567+00:00"

tags:
  - software

keywords:
  - "language models"
  - "TESSDATA_PREFIX"
  - "OCR Engine"
  - "pytesseract"
  - "Tesseract"

questions:
  - "What is Tesseract and what is its primary function?"
  - "How do you configure Tesseract to locate downloaded language models?"
  - "Which wrapper package is used to integrate Tesseract with Python?"
  - "What is Tesseract and what is its primary function?"
  - "How do you configure Tesseract to locate downloaded language models?"
  - "Which wrapper package is used to integrate Tesseract with Python?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Tesseract](https://github.com/tesseract-ocr/tesseract) is an open source text recognition (OCR) Engine with support for over a hundred languages.

## Downloading language models
Tesseract needs language models to be able to transcribe images. These can be downloaded from https://github.com/tesseract-ocr/tessdata. Download the ones that you want and save them in a directory.

Then you need to tell Tesseract where to find the models using the environment variable `TESSDATA_PREFIX`. For example, if you save the models in `~/tessdata`, then you would use the following command:

```bash
export TESSDATA_PREFIX=~/tessdata
```

## Using from Python
Tesseract can be used from Python using the wrapper package "pytesseract".

!!! tip
    We recommend you install this in a [Virtualenv](virtualenv.md).