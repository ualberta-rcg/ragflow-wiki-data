---
title: "Including a source code file within the wiki"
slug: "including_a_source_code_file_within_the_wiki"
lang: "base"

source_wiki_title: "Including a source code file within the wiki"
source_hash: "ee9e08d4ee226039ae9b2f0807b2d049"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:00:10.373810+00:00"

tags:
  []

keywords:
  - "source code"
  - "File template"
  - "syntaxhighlight"
  - "line numbers"
  - "special characters"

questions:
  - "What are the main parameters used to configure the {{File}} template for displaying source code?"
  - "How must special characters like pipes and equal signs be modified when included in the template's content?"
  - "What option needs to be added to the template to enable the display of line numbers?"
  - "What are the main parameters used to configure the {{File}} template for displaying source code?"
  - "How must special characters like pipes and equal signs be modified when included in the template's content?"
  - "What option needs to be added to the template to enable the display of line numbers?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

As explained on the page [Including source code within the wiki](including_source_code_within_the_wiki.md), you can include source code within the wiki using the **`<syntaxhighlight> </syntaxhighlight>`** tag. If you want to separate the code a bit more from the rest of the text, you can use the `{{File}}` template. This template takes as argument the file name (**name** parameter), the language of the file (**lang** parameter) and the content of the file (**contents** parameter). The default language for this template is *bash*.

For example,

```text
{{File
  |name=myfile.sh
  |lang="bash"
  |contents=
#!/bin/bash
echo "this is a bash script"
}}
```

results in:

```bash title="myfile.sh"
#!/bin/bash
echo "this is a bash script"
```

## Special characters: Pipe, equals

Certain characters that frequently appear in bash scripts are also meaningful to the Mediawiki template parser.
* If the source code contains a pipe character, `|`, replace it with `{{!}}`.
* In some circumstances you may find it necessary to replace the equal sign, `=`, with `{{=}}`.

## Displaying line numbers

To display line numbers, you can add the option "`|lines=yes`". For example,

```text
{{File
  |name=monfichier.sh
  |lang="bash"
  |lines=yes
  |contents=
#!/bin/bash
echo "this is a bash script"
}}
```

results in:

```bash title="myfile.sh"
#!/bin/bash
echo "this is a bash script"