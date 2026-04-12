---
title: "Build tools"
slug: "build_tools"
lang: "base"

source_wiki_title: "Build tools"
source_hash: "75a44e1aa64373062e7f7dfaf34b0364"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:50:44.609490+00:00"

tags:
  []

keywords:
  - "CMake"
  - "build process"
  - "Autotools"
  - "Make"
  - "compilation"

questions:
  - "What is the primary purpose of build management tools?"
  - "What specific tasks and configuration issues are handled during the automated build process?"
  - "Which common build automation tools are provided on Linux and Compute Canada systems?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

These are tools for managing and to the extent possible automating the build process, i.e. the compilation and linking of an ensemble of source code files and libraries to create an executable file, which includes handling various platform-specific configuration issues. Linux provides a variety of different tools and Compute Canada systems include the most common:
* [Make](make.md)
* [Autotools](autotools.md)
* [CMake](cmake.md)