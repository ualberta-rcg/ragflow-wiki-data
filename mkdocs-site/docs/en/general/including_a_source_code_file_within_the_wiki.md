---
title: "Including a source code file within the wiki/en"
slug: "including_a_source_code_file_within_the_wiki"
lang: "en"

source_wiki_title: "Including a source code file within the wiki/en"
source_hash: "b3acb3c624b6aae3011feeae8eac213e"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:00:24.874001+00:00"

tags:
  []

keywords:
  - "Source code"
  - "Special characters"
  - "Line numbers"
  - "File template"
  - "syntaxhighlight tag"

questions:
  - "What are the main parameters used in the File template to display source code, and what is the default language?"
  - "How must special characters like pipes and equal signs be modified to work correctly within the Mediawiki template parser?"
  - "Which option needs to be added to the template in order to display line numbers next to the source code?"
  - "What are the main parameters used in the File template to display source code, and what is the default language?"
  - "How must special characters like pipes and equal signs be modified to work correctly within the Mediawiki template parser?"
  - "Which option needs to be added to the template in order to display line numbers next to the source code?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

As explained on the page [Including source code within the wiki](including-source-code-within-the-wiki.md), you can include source code within the wiki using the **`<syntaxhighlight>`** tag. If you want to separate the code a bit more from the rest of the text, you can use the `{{File}}` template. This template takes as argument the file name (**name** parameter), the language of the file (**lang** parameter) and the content of the file (**contents** parameter). The default language for this template is *bash*.

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

!!! tip
    Certain characters that frequently appear in bash scripts are also meaningful to the MediaWiki template parser.
    * If the source code contains a pipe character, `|`, replace it with `{{!}}`.
    * In some circumstances you may find it necessary to replace the equal sign, `=`, with `{{=}}`.

## Displaying line numbers

To display line numbers, you can add the option "|lines=yes". For example,
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
```bash title="myfile.sh" linenums="true"
#!/bin/bash
echo "this is a bash script"