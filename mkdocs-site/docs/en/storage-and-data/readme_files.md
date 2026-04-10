---
title: "README files/en"
slug: "readme_files"
lang: "en"

source_wiki_title: "README files/en"
source_hash: "309b539a35615d04fcc6148ae17222d3"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T10:42:29.214219+00:00"

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