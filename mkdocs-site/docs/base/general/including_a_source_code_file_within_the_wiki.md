---
title: "Including a source code file within the wiki"
tags:
  []

keywords:
  []
---

__NOTOC__

As explained on the page [Including source code within the wiki](including-source-code-within-the-wiki.md), you can include source code within the wiki using the **<nowiki><syntaxhighlight> </syntaxhighlight></nowiki>** tag. If you want to separate the code a bit more from the rest of the text, you can use the <nowiki>
**`file`**
```text

```
</nowiki> template. This template takes as argument the file name (**name** parameter), the language of the file (**lang** parameter) and the content of the file (**contents** parameter). The default language for this template is *bash*. 

For example,
<syntaxhighlight lang="text">

**`myfile.sh`**
```bash
#!/bin/bash
echo "this is a bash script"
```

</syntaxhighlight>

results in:

**`myfile.sh`**
```bash
#!/bin/bash
echo "this is a bash script"
```

== Special characters: Pipe, equals == 
Certain characters that frequently appear in bash scripts are also meaningful to the Mediawiki template parser. 
* If the source code contains a pipe character, <tt>|</tt>, replace it with <tt><nowiki></nowiki></tt>.
* In some circumstances you may find it necessary to replace the equal sign, <tt>=</tt>, with <tt><nowiki></nowiki></tt>.

== Displaying line numbers == 
To display line numbers, you can add the option "|lines=yes". For example, 
<syntaxhighlight lang="text">

**`monfichier.sh`**
```bash
#!/bin/bash
echo "this is a bash script"
```

</syntaxhighlight>

results in:

**`myfile.sh`**
```bash
#!/bin/bash
echo "this is a bash script"
```