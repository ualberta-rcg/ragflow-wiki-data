---
title: "Uv"
slug: "uv"
lang: "base"

source_wiki_title: "Uv"
source_hash: "f2f9d8f57d26951a4c850e3b5a6cc22e"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:29:52.215244+00:00"

tags:
  []

keywords:
  - "uv"
  - "Python package manager"
  - "pip"
  - "not supported"
  - "cache"

questions:
  - "Why is the uv package manager currently not supported on the clusters and what specific issues might arise from using it?"
  - "What is the recommended tool and version for installing Python packages on the clusters instead of uv?"
  - "How can users clear the uv cache and configure the tool to avoid using the cache in the future?"
  - "Why is the uv package manager currently not supported on the clusters and what specific issues might arise from using it?"
  - "What is the recommended tool and version for installing Python packages on the clusters instead of uv?"
  - "How can users clear the uv cache and configure the tool to avoid using the cache in the future?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! warning "Not supported"
    uv is currently **not** supported on our clusters.

uv is an extremely fast Python package and project manager written in Rust. While you may be able to use it to install some packages, it will likely fail for others.

Some issues and pitfalls you may encounter:
* some packages are distributed in a format that is incompatible with our clusters, but uv tries to install them nonetheless;
* uv is unaware of the Python packages provided by loaded modules;
* uv can quickly fill up your /home directory quota since it stores a very large number of files in its cache.

## Installing Python packages
To install packages on our clusters, use `pip`; see [Python](python.md).

Make sure to use at least `pip>=25.0`.
```bash
pip install --no-index --upgrade pip
```

## Troubleshooting

### Clearing the cache
To clear the uv cache, use
```bash
uv cache clean
```
Then, to avoid using the cache, use `uv --no-cache`.