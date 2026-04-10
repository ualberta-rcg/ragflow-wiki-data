---
title: "Including a command within the wiki/en"
tags:
  []

keywords:
  []
---

To include a command within the wiki, you should use the <nowiki>
```bash

```
</nowiki> template. This template detects the **bash** syntax. For example, the code
<syntaxhighlight lang=text>

```bash
cd src; make && make install; cd ..
```

</syntaxhighlight>
results in:

```bash
cd src; make && make install; cd ..
```

== Special characters "" and "" ==
Since <nowiki>
```bash

```
</nowiki> is a template, the "=" and "|" signs are interpreted by the wiki.

To include an equality sign, use the [meta-template <nowiki></nowiki>](template:=.md). For example, the code:
<syntaxhighlight lang=text>

```bash

```
$HOME && make && make install}}
</syntaxhighlight>
results in:

```bash

```
$HOME && make && make install}}
To include a pipe symbol, use <nowiki></nowiki>.

## Including a set of commands 
You can use the <nowiki>
```bash

```
</nowiki> template to include a set of commands. You may then write each command on a separate line, and prepend the **|** character in front of each command. For example, the code
<syntaxhighlight lang=text>

```bash
cd ..
```

</syntaxhighlight>
results in:

```bash
cd ..
```

## Modifying the command prompt 
If you want to modify the command prompt, you may do it by including a *prompt* argument to the template. For example, 
<syntaxhighlight lang=text>
```bash
cd src; make && make install; cd ..
```
</syntaxhighlight>
results in 

```bash
cd src; make && make install; cd ..
```

In the same way, 
<syntaxhighlight lang=text>

```bash
cd ..
```

</syntaxhighlight>
results in

```bash
cd ..
```

## Displaying the result of a command 
You can display the result of a command (and only one) by adding the option <tt>result</tt>. For example, 
<syntaxhighlight>

```bash
df -h .
```

```
Sys. de fich.         Tail. Occ. Disp. %Occ. Monté sur
/lustre2/home         516T  340T  150T  70% /home
```

</syntaxhighlight>
results in : 

```bash
df -h .
```

```
Sys. de fich.         Tail. Occ. Disp. %Occ. Monté sur
/lustre2/home         516T  340T  150T  70% /home
```