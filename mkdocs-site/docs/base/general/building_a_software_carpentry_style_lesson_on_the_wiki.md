---
title: "Building a Software Carpentry style lesson on the wiki"
slug: "building_a_software_carpentry_style_lesson_on_the_wiki"
lang: "base"

source_wiki_title: "Building a Software Carpentry style lesson on the wiki"
source_hash: "1eef5e27aa73c8c958300291e484ed25"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:51:12.797217+00:00"

tags:
  []

keywords:
  - "Markdown syntax"
  - "wiki"
  - "lessons"
  - "Software Carpentry"
  - "templates"

questions:
  - "What is the main advantage mentioned for hosting Software Carpentry-style lessons on a wiki rather than on GitHub?"
  - "What are the specific templates provided to help format the different sections of a lesson?"
  - "How is the syntax structured to implement these templates and generate the corresponding formatted boxes?"
  - "What is the main advantage mentioned for hosting Software Carpentry-style lessons on a wiki rather than on GitHub?"
  - "What are the specific templates provided to help format the different sections of a lesson?"
  - "How is the syntax structured to implement these templates and generate the corresponding formatted boxes?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

It may be interesting to use our wiki to host Software Carpentry-style lessons. Software Carpentry lessons, such as [this one](http://swcarpentry.github.io/shell-novice/), are usually hosted on GitHub. They can be written with a Markdown syntax, and provide many pre-formatted styles. Hosting a lesson on a wiki also offers the advantage of supporting translation. In order to facilitate the writing of such lesson, a few templates may be useful, and are listed below.

## Prerequisites
The typical SWC prerequisites box can be obtained using the `{{Prerequisites}}` template. For example, the following code

```text
{{Prerequisites
  |title=Prerequisites for this lesson
  |content=
This lesson requires you to first know X.
}}
```

results in the following box

!!! info "Prerequisites for this lesson"

    This lesson requires you to first know X.

## Getting Ready
The SWC "getting ready" box can be obtained using the `{{Getready}}` template. For example, the following code

```text
{{Getready
  |title=Getting ready for this lesson
  |content=
You should download the following files prior to starting the lesson.
}}
```

results in the following box

!!! info "Getting ready for this lesson"

    You should download the following files prior to starting the lesson.

## Learning Objectives
The SWC "objectives" box can be obtained using the `{{Objectives}}` template. For example, the following code

```text
{{Objectives
  |title=Learning Objectives
  |content=
* You will learn A
* You will also learn B
}}
```

results in the following box

!!! abstract "Learning Objectives"

    * You will learn A
    * You will also learn B

## Callouts
The SWC "callout" box can be obtained using the `{{Callout}}` template. For example, the following code

```text
{{Callout
  |title=Using auto completion
  |content=
You can use the <TAB> key to auto complete. 
}}
```

results in the following box

!!! tip "Using auto completion"

    You can use the <TAB> key to auto complete.

## Challenge
The SWC "challenge" box can be obtained using the `{{Challenge}}` template. For example, the following code

```text
{{Challenge
  |title=Practicing using the commands.
  |content=
Assuming a ...
}}
```

results in the following box

!!! question "Practicing using the commands"

    Assuming a ...