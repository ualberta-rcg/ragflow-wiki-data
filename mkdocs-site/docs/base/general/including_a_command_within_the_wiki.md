---
title: "Including a command within the wiki"
slug: "including_a_command_within_the_wiki"
lang: "base"

source_wiki_title: "Including a command within the wiki"
source_hash: "720ab1571801c304b646e0dd6f3ac669"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T07:19:43.669768+00:00"

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

To include a command within the wiki, you should use the `{{Command}}` template. This template detects the **bash** syntax. For example, the code
```text
{{Command|cd src; make && make install; cd ..}}
```
results in:
```bash
cd src; make && make install; cd ..
```

## Special characters "=" and "|"

!!! tip "Handling Special Characters in Templates"
    Since `{{Command}}` is a template, the "=" and "|" signs are interpreted by the wiki.

To include an equality sign, use the [meta-template "="](template-equal.md). For example, the code:
```text
{{Command|./configure --prefix{{=}}$HOME && make && make install}}
```
results in:
```bash
./configure --prefix=$HOME && make && make install
```
To include a pipe symbol, use `|`.

## Including a set of commands

You can use the `{{Commands}}` template to include a set of commands. You may then write each command on a separate line, and prepend the `|` character in front of each command. For example, the code
```text
{{Commands
|cd src
|make
|make install
|cd ..
}}
```
results in:
```bash
cd src
make
make install
cd ..
```

## Modifying the command prompt

If you want to modify the command prompt, you may do it by including a *prompt* argument to the template. For example,
```text
{{Command|prompt=[name@briaree ~]|cd src; make && make install; cd ..}}
```
results in
```bash
[name@briaree ~] cd src; make && make install; cd ..
```

In the same way,
```text
{{Commands
|prompt=[name@briaree $]
|cd src
|make
|make install
|cd ..
}}
```
results in
```bash
[name@briaree $] cd src
[name@briaree $] make
[name@briaree $] make install
[name@briaree $] cd ..
```

## Displaying the result of a command

You can display the result of a command (and only one) by adding the option `result`. For example,
```text
{{Command
|df -h .
|result=
Sys. de fich.         Tail. Occ. Disp. %Occ. Monté sur
/lustre2/home         516T  340T  150T  70% /home
}}
```
results in :
```bash
df -h .
```
```text
Sys. de fich.         Tail. Occ. Disp. %Occ. Monté sur
/lustre2/home         516T  340T  150T  70% /home