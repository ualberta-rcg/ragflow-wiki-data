---
title: "Building a Software Carpentry style lesson on the wiki/en"
slug: "building_a_software_carpentry_style_lesson_on_the_wiki"
lang: "en"

source_wiki_title: "Building a Software Carpentry style lesson on the wiki/en"
source_hash: "1b57baf912f7f2ea75e47f16574f81e7"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T05:00:30.749945+00:00"

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

It may be interesting to use our wiki to host Software Carpentry-style lessons. Software Carpentry lessons, such as [this one](http://swcarpentry.github.io/shell-novice/), are usually hosted on Github. They can be written with a Markdown syntax and provide many pre-formatted styles. Hosting a lesson on a wiki also offers the advantage of supporting translation. In order to facilitate the writing of such a lesson, a few templates may be useful, and are listed below.

## Prerequisites
The typical SWC prerequisites box can be obtained using a suitable admonition. For example, the following code in MediaWiki:

```mediawiki
{{Prerequisites
  |title=Prerequisites for this lesson
  |content=
This lesson requires you to first know X.
}}
```

results in the following box in MediaWiki. In MkDocs Material, this would be an `!!! note` admonition:

!!! note "Prerequisites for this lesson"
    This lesson requires you to first know X.

## Getting ready
The SWC "getting ready" box can be obtained using a suitable admonition. For example, the following code in MediaWiki:

```mediawiki
{{Getready
  |title=Getting ready for this lesson
  |content=
You should download the following files prior to starting the lesson.
}}
```

results in the following box in MediaWiki. In MkDocs Material, this would be an `!!! note` admonition:

!!! note "Getting ready for this lesson"
    You should download the following files prior to starting the lesson.

## Learning Objectives
The SWC "objectives" box can be obtained using a suitable admonition. For example, the following code in MediaWiki:

```mediawiki
{{Objectives
  |title=Learning Objectives
  |content=
* You will learn A
* You will also learn B
}}
```

results in the following box in MediaWiki. In MkDocs Material, this would be an `!!! info` admonition:

!!! info "Learning Objectives"
    * You will learn A
    * You will also learn B

## Callouts
The SWC "callout" box can be obtained using a suitable admonition. For example, the following code in MediaWiki:

```mediawiki
{{Callout
  |title=Using auto completion
  |content=
You can use the <TAB> key to auto complete. 
}}
```

results in the following box in MediaWiki. In MkDocs Material, this would be an `!!! tip` admonition:

!!! tip "Using auto completion"
    You can use the <TAB> key to auto complete.

## Challenge
The SWC "challenge" box can be obtained using a suitable admonition. For example, the following code in MediaWiki:

```mediawiki
{{Challenge
  |title=Practicing using the commands.
  |content=
Assuming a ...
}}
```

results in the following box in MediaWiki. In MkDocs Material, this would be an `!!! question` admonition:

!!! question "Practising using the commands"
    Assuming a ...