---
title: "Including a source code file within the wiki/en"
slug: "including_a_source_code_file_within_the_wiki"
lang: "en"

source_wiki_title: "Including a source code file within the wiki/en"
source_hash: "b3acb3c624b6aae3011feeae8eac213e"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T07:21:00.818213+00:00"

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

As explained on the page [Including source code within the wiki](including-source-code-within-the-wiki.md), you can include source code within the wiki using the **`<syntaxhighlight> </syntaxhighlight>`** tag. If you want to separate the code a bit more from the rest of the text, you can use the `{{File}}` template. This template takes as argument the file name (**name** parameter), the language of the file (**lang** parameter) and the content of the file (**contents** parameter). The default language for this template is *bash*.

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

```bash linenums title="myfile.sh"
#!/bin/bash
echo "this is a bash script"