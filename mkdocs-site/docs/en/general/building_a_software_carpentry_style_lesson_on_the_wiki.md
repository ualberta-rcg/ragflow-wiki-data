---
title: "Building a Software Carpentry style lesson on the wiki/en"
slug: "building_a_software_carpentry_style_lesson_on_the_wiki"
lang: "en"

source_wiki_title: "Building a Software Carpentry style lesson on the wiki/en"
source_hash: "1b57baf912f7f2ea75e47f16574f81e7"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:51:27.168766+00:00"

tags:
  []

keywords:
  - "Markdown syntax"
  - "wiki"
  - "lessons"
  - "Software Carpentry"
  - "templates"

questions:
  - "What is the primary advantage of hosting Software Carpentry-style lessons on a wiki rather than on Github?"
  - "Which specific templates are provided to recreate the standard formatting boxes used in Software Carpentry lessons?"
  - "How is the syntax structured to implement these templates, such as the Prerequisites or Callout boxes, within the wiki?"
  - "What is the primary advantage of hosting Software Carpentry-style lessons on a wiki rather than on Github?"
  - "Which specific templates are provided to recreate the standard formatting boxes used in Software Carpentry lessons?"
  - "How is the syntax structured to implement these templates, such as the Prerequisites or Callout boxes, within the wiki?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

It may be interesting to use our wiki to host Software Carpentry-style lessons. Software Carpentry lessons, such as [this one](http://swcarpentry.github.io/shell-novice/), are usually hosted on GitHub. They can be written with a Markdown syntax and provide many pre-formatted styles. Hosting a lesson on a wiki also offers the advantage of supporting translation. In order to facilitate the writing of such a lesson, a few templates may be useful, and are listed below.

## Prerequisites
The typical SWC prerequisites box can be obtained using the Prerequisites template. For example, the following code

```markdown
{{Prerequisites
  |title=Prerequisites for this lesson
  |content=
This lesson requires you to first know X.
}}
```
results in the following box

!!! info "Prerequisites for this lesson"
    This lesson requires you to first know X.

## Getting ready
The SWC "getting ready" box can be obtained using the Getready template. For example, the following code

```markdown
{{Getready
  |title=Getting ready for this lesson
  |content=
You should download the following files prior to starting the lesson.
}}
```
results in the following box

!!! note "Getting ready for this lesson"
    You should download the following files prior to starting the lesson.

## Learning Objectives
The SWC "objectives" box can be obtained using the Objectives template. For example, the following code

```markdown
{{Objectives
  |title=Learning Objectives
  |content=
* You will learn A
* You will also learn B
}}
```
results in the following box

!!! note "Learning Objectives"
    * You will learn A
    * You will also learn B

## Callouts
The SWC "callout" box can be obtained using the Callout template. For example, the following code

```markdown
{{Callout
  |title=Using auto completion
  |content=
You can use the <TAB> key to auto complete.
}}
```
results in the following box

!!! note "Using auto completion"
    You can use the `<TAB>` key to auto complete.

## Challenge
The SWC "challenge" box can be obtained using the Challenge template. For example, the following code

```markdown
{{Challenge
  |title=Practicing using the commands.
  |content=
Assuming a ...
}}
```
results in the following box

!!! warning "Practicing using the commands"
    Assuming a ...