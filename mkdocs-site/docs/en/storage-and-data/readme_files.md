---
title: "README files/en"
slug: "readme_files"
lang: "en"

source_wiki_title: "README files/en"
source_hash: "309b539a35615d04fcc6148ae17222d3"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:58:22.436661+00:00"

tags:
  []

keywords:
  - "file documentation"
  - "file formats"
  - "research data management"
  - "project spaces"
  - "README file"

questions:
  - "Why is it important to use README files for active research data management in project spaces?"
  - "What specific information should be included in a README file to properly document the files in a directory?"
  - "What are the different file formats available for creating a README, and how do they differ in terms of human and machine readability?"
  - "Why is it important to use README files for active research data management in project spaces?"
  - "What specific information should be included in a README file to properly document the files in a directory?"
  - "What are the different file formats available for creating a README, and how do they differ in terms of human and machine readability?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

In your project spaces, your data should be documented such that you know the purpose of each file. A README file is usually the first reference point.

Using README files on clusters is part of active research data management. It will be useful for future publications and for team members wondering what are the files in some directory.

## What to write in a README file

*   Source of the files
    *   Website or external database
    *   Authors
    *   Year
*   Types of files present in the directory
    *   Structure of directories
*   Which files are temporary
*   Which files are actively used
*   Which files could be archived
*   Who should be able to access what and when:
    *   On the cluster;
    *   On a data repository (in some future).

## Formats of a README file

*   `README` or `README.txt`
    *   Free text format.
    *   Better than nothing, but no conventional style is enforced.
*   `README.md` ([Markdown](https://www.markdownguide.org/)), `README.rst` ([reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html))
    *   Structured text format that remains human readable.
    *   Can be compiled into formatted text (HTML or PDF).
*   `README.yaml` ([YAML](https://yaml.org)), `README.json` ([JSON](https://en.wikipedia.org/wiki/JSON)), `README.xml` ([XML](https://developer.mozilla.org/en-US/docs/Web/XML/Guides/XML_introduction))
    *   Slightly less human-readable.
    *   Machine-readable, which means a program can validate the contents of the README file.
    *   Could be used to generate a README file in another format.

## References

*   [McMaster - README Generator](https://rdm.mcmaster.ca/readme)
*   [UBC - Create a README file](https://ubc-library-rc.github.io/rdm/content/03_create_readme.html)
*   [UWaterloo - README Files for Data Deposits](https://subjectguides.uwaterloo.ca/rdm/basics#readme)