---
title: "Authoring guidelines"
slug: "authoring_guidelines"
lang: "base"

source_wiki_title: "Authoring guidelines"
source_hash: "c199f942c7eff5af5dfc724a588f1d21"
last_synced: "2026-08-07T19:46:17.777436+00:00"
last_processed: "2026-08-07T22:22:40.564816+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: true
  qa_generated: false
---

## Who can contribute to this Wiki?
Anyone with an Alliance account can contribute. Staff members have the primary responsibility to keep the documentation complete and correct, but this is the age of Wikipedia. An ordinary user who spots an obvious problem, like a dead link or a typographical error, is welcome to fix it. Equally so, a user who is willing to write an entire page on some piece of installed software with which they are very familiar, is also welcome to do that. The documentation team will review it once it’s posted to see that it meets these guidelines.

No anonymous editing is possible. You must log in with your Alliance credentials before you are allowed to edit, so we can tell who has done what.

## What belongs on this Wiki?
This Wiki is not the place for information that properly belongs in the purview of the Alliance communications team, which includes any communications intended for the general public, media, or funding agencies. Materials related to training and outreach also don’t belong on this technical documentation site. To that end, ask yourself before you publish a page or make a change:
* Is this about what services or clusters are available? If so, has the service or cluster already been announced? If not, consult the the Senior Manager, Communications & Marketing before publishing.
* Status information which changes from day to day --- available, offline, in maintenance, etc.--- belongs on [status.alliancecan.ca](https://status.alliancecan.ca/).
* Is this information useful to a user, as opposed to other CC technical staff? If technical staff, then it might belong at [wiki.computecanada.ca/staff/](https://wiki.computecanada.ca/staff/) rather than [docs.alliancecan.ca/](https://docs.alliancecan.ca/).
* Does the information have implications for the security of our systems, or security of data on our systems? If so, consult the Director of Cybersecurity before publishing.
* Is the information of interest only to a prospective user, as opposed to an existing account-holder? This is a gray area: A prospective user might want to know technical details about our services and facilities, the same as an account-holder, but if the information is only of interest to a prospective user then it properly belongs on [www.alliancecan.ca](https://www.alliancecan.ca) rather than [docs.alliancecan.ca/](https://docs.alliancecan.ca/).
* External links may be appropriate, see e.g. "Getting an Account".
* Is this about how to use an existing service, cluster, or application? If so, go ahead.

If you still have any doubt, staff members should use the #rsnt-documentation channel in Slack. Non-staff contributors should contact [Technical support](../support/technical_support.md).

## Style guidelines
To the extent possible, we encourage contributors to avoid simply uploading a PDF as this is less than ideal. A better approach is to copy over the relevant text from the PDF and add it to the page, with whatever formatting changes may be needed for a Wiki page, including for example the use of internal links that readers may follow.

### Drafts
If you wish to work on a new page in stages, or get feedback before deciding it is complete, you should clearly mark the page as a draft.

### Writing style
The purpose of a style guide is to support writers in preparing technical documentation that makes learning easier. Carefully crafted documentation appeals to the user and delivers a positive image of the writer.
There are several style guides in circulation that set standards for computer documentation. Pioneers in this area are the Apple Style Guide and the Microsoft Manual of Style.
There are no official writing guidelines for this wiki, but here are some simple and common practices we can readily adopt:
* **Leave an empty line after each section title**. This prevents potential issues with the [translation tags](#things-not-to-do-with-translation-tags).
* Design each paragraph around one idea.
* Present the most important information first.
* Address the reader directly.
  Example: *The user must click on the button* or *One must click on the button* becomes *Click on the button.*
* Use [simple words and phrases](http://www.plainlanguage.gov/howto/wordsuggestions/simplewords.cfm).
* Use the present tense.
  Example: *Doing this will launch the XYZ application* becomes *This launches the XYZ application.*
* Use the active voice.
  Example: *The file is edited by the system administrator* becomes *The system administrator edits the file.*
* Stay positive.
  Example: *Don't use the passive voice* becomes *Use the active voice.*
* Use consistent terms.
  Yes, synonyms make a text less boring, but for a new user or one reading in a second language, interchangeable terms (e.g. "machine", "host", "node", "server") may be confusing.

The word "system" is used frequently in computing with different meanings (legacy system, new system, cloud system, file system, module system, job scheduling system, GPU system, storage system, *etc.*). It is not always clear to a new user what we are talking about. Whenever possible, please try to use a more precise word (cluster, storage space, scheduler, *etc.*).

#### External resources
* Online self-guided [Technical Writing courses from Google](https://developers.google.com/tech-writing/overview).
* [Documentation guide from Write the Docs](https://www.writethedocs.org/guide/).

### Layout style
When in doubt, imitate the masters. Look at an existing page you like and follow the style. If there isn’t one at [docs.alliancecan.ca/](https://docs.alliancecan.ca/), look for one at [Wikipedia](https://en.wikipedia.org/wiki/Wikipedia).
* Separate graphic design from content as much as possible. Don’t use extra line breaks to adjust vertical spacing. Don’t indent paragraphs with tabs or spaces or add extra spaces after a sentence. If we want to make any such style adjustments we will make them universally using stylesheets and templates.
* Leave one blank line at the end of each section before the following header. The translation package uses the blank line and header to determine the boundaries of translation units.
* Links to other pages or sites should have a human-oriented description for display rather than the raw URL.
* Capitalize only the first word and [proper nouns](http://blog.apastyle.org/apastyle/2012/02/do-i-capitalize-this-word.html) in titles and headings. Following [Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Naming_conventions_(capitalization)), we prefer the [APA sentence case](http://blog.apastyle.org/apastyle/2012/03/title-case-and-sentence-case-capitalization-in-apa-style.html) for all titles, including page titles.

### Templates
There are multiple templates available. Please use them as appropriate. Of particular interest are templates for [Including a command within the wiki](including_a_command_within_the_wiki.md) and for [Including a source code file within the wiki](including_a_source_code_file_within_the_wiki.md).

## Translation
### Code blocks are not translated
Professional human translators are often not programmers. As such, they may not distinguish between code and comments in every language, and documentation teams typically instruct translators to exclude code blocks from translation.

Putting explanatory comments in code is excellent programming practice which we wish to encourage, but the value of the comments is decreased if the comments aren't translated. The documentation team has not found a solution for this that works in every case.
Here are some suggestions:
* Move the information contained in the comments outside the code block, into the surrounding text (which will then be translated).
* Leave an index comment (e.g. "NOTE 1", "NOTE 2") to connect the external text to the relevant line of code.
* If you're sufficiently bilingual, and familiar with the translation apparatus, you may translate the code block yourself.

Please *do not* leave example code uncommented, but please *do* remember that comments will not normally be translated, and consider how this will affect the understanding of the user reading the page in translation.

## "Available software" page
Tables on the [Available software](../programming/available_software.md) page are automatically generated from module files in CVMFS. In order to add a link to a new page from the "Documentation" column of those tables, add an entry to [https://github.com/ComputeCanada/wiki_module_bot/blob/main/module_wiki_page.json](https://github.com/ComputeCanada/wiki_module_bot/blob/main/module_wiki_page.json). Please add this change to the definitive copy of the file.

Changes may take six hours to propagate to the wiki page.