---
title: "Tesseract"
slug: "tesseract"
lang: "base"

source_wiki_title: "Tesseract"
source_hash: "79e327150ebe41d2c3f3c84635ac05be"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T11:50:42.547287+00:00"

tags:
  - software

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

[Tesseract](https://github.com/tesseract-ocr/tesseract) is an open source text recognition (OCR) Engine with support for over a hundred languages.

## Downloading language models
Tesseract needs language models to be able to transcribe images. These can be downloaded from https://github.com/tesseract-ocr/tessdata. Download the ones that you want and save them in a directory.

Then you need to tell Tesseract where to find the models using the environment variable `TESSDATA_PREFIX`. For example, if you save the models in `~/tessdata`, then you would use the following command:

```bash
export TESSDATA_PREFIX=~/tessdata
```

## Using from Python
Tesseract can be used from Python using the wrapper package "pytesseract". We recommend you install this in a [Virtualenv](virtualenv.md).