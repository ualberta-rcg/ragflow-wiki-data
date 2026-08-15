---
title: "Authoring guidelines/en"
slug: "authoring_guidelines"
lang: "en"

source_wiki_title: "Authoring guidelines/en"
source_hash: "af9ca6bef192d1fd6a310390b0dc9f90"
last_synced: "2026-08-15T23:22:43.108655+00:00"
last_processed: "2026-08-15T23:31:57.960496+00:00"

tags:
  []

keywords:
  - "synonyms"
  - "translation tags"
  - "Alliance account"
  - "code blocks and wiki markup"
  - "draft pages"
  - "precise word"
  - "security review"
  - "may take"
  - "mark page for translation"
  - "propagate"
  - "MediaWiki:Sidebar"
  - "Mark this version for translation"
  - "technical documentation"
  - "wiki page"
  - "Documentation column"
  - "human translation"
  - "do NOT edit translation tags"
  - "templates"
  - "screenshots"
  - "priority language"
  - "CVMFS"
  - "Available software"
  - "six hours"
  - "code blocks not translated"
  - "system"
  - "style guidelines"
  - "Compute Canada wiki_module_bot"
  - "layout style"
  - "module_wiki_page.json"
  - "Changes"
  - "interchangeable terms"
  - "new user"

questions:
  - "Who is allowed to edit the Alliance documentation wiki and what authentication is required?"
  - "What types of content are appropriate for this wiki versus other Alliance communication channels or sites?"
  - "What are the key style and formatting guidelines contributors should follow when creating or editing wiki pages?"
  - "Why can using interchangeable terms such as “machine,” “host,” “node,” and “server” confuse new users or readers of a second language?"
  - "What problems does the broad use of the word “system” create in computing documentation?"
  - "What strategy is suggested to increase clarity by choosing more precise terminology?"
  - "What are the main layout style guidelines for wiki pages, including spacing, heading capitalization, and image handling?"
  - "How should a newly written page be prepared and marked for translation using the MediaWiki Translate extension?"
  - "Which actions are prohibited when editing or handling translation tags in the wiki?"
  - "What steps should you follow if you see a solitary translation tag at the end of a section while editing a page?"
  - "How do you correctly mark a page’s changes for translation, including the use of <translate> tags and setting the priority language?"
  - "What are the recommended practices for dealing with code blocks and sidebar items to ensure they are properly excluded from or included in translation?"
  - "What value should be entered in the “Priority languages” field, and what does it indicate?"
  - "How does a user mark a page version for translation?"
  - "Which actions are explicitly prohibited when editing translation tags on a page?"
  - "How long can it take for changes to appear on the wiki page?"
  - "What factors could cause the propagation of changes to the wiki page to take up to six hours?"
  - "What steps should a user take if their changes have not shown up on the wiki page after the expected six‑hour period?"
  - "Where are the tables on the “Available software” page generated from?"
  - "How can a new link be added to the “Documentation” column of those tables?"
  - "Which file must be edited to add the entry, and where is this file located?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: false
  qa_generated: false
---

## Who can contribute to this Wiki?

Anyone with an Alliance account can contribute. Staff members have the primary responsibility to keep the documentation complete and correct, but this is the age of Wikipedia. An ordinary user who spots an obvious problem, like a dead link or a typographical error, is welcome to fix it. Equally so, a user who is willing to write an entire page on some piece of installed software with which they are very familiar, is also welcome to do that. The documentation team will review it once it’s posted to see that it meets these guidelines.

No anonymous editing is possible. You must log in with your Alliance credentials before you are allowed to edit, so we can tell who has done what.

## What belongs on this Wiki?

This Wiki is not the place for information that properly belongs in the purview of the Alliance communications team, which includes any communications intended for the general public, media, or funding agencies. Materials related to training and outreach also don’t belong on this technical documentation site. To that end, ask yourself before you publish a page or make a change:

*   Is this about what services or clusters are available? If so, has the service or cluster already been announced? If not, consult the Senior Manager, Communications & Marketing before publishing.
*   Status information which changes from day to day --- available, offline, in maintenance, *etc.*--- belongs on https://status.alliancecan.ca/.
*   Is this information useful to a user, as opposed to other CC technical staff? If technical staff, then it might belong at [https://wiki.computecanada.ca/staff/](https://wiki.computecanada.ca/staff/) rather than [https://docs.alliancecan.ca/](https://docs.alliancecan.ca/).
*   Does the information have implications for the security of our systems, or security of data on our systems? If so, consult the Director of Cybersecurity before publishing.
*   Is the information of interest only to a prospective user, as opposed to an existing account-holder? This is a grey area: A prospective user might want to know technical details about our services and facilities, the same as an account-holder, but if the information is only of interest to a prospective user then it properly belongs on [https://www.alliancecan.ca](https://www.alliancecan.ca) rather than [https://docs.alliancecan.ca/](https://docs.alliancecan.ca/).
*   External links may be appropriate, see *e.g.* "Getting an Account".
*   Is this about how to use an existing service, cluster, or application? If so, go ahead.

If you still have any doubt, staff members should use the #rsnt-documentation channel in Slack. Non-staff contributors should contact [Technical support](../support/technical_support.md).

## Style guidelines

To the extent possible, we encourage contributors to avoid simply uploading a PDF as this is less than ideal. A better approach is to copy over the relevant text from the PDF and add it to the page, with whatever formatting changes may be needed for a Wiki page, including for example the use of internal links that readers may follow.

### Drafts

If you wish to work on a new page in stages, or get feedback before deciding it is complete, you should mark the page as a draft by inserting the following at the top of the source on the MediaWiki site:

```
{{Draft}}
```

### Writing style

The purpose of a style guide is to support writers in preparing technical documentation that makes learning easier. Carefully crafted documentation appeals to the user and delivers a positive image of the writer.

There are several style guides in circulation that set standards for computer documentation. Pioneers in this area are the Apple Style Guide and the Microsoft Manual of Style.

There are no official writing guidelines for this wiki, but here are some simple and common practices we can readily adopt:

*   **Leave an empty line after each section title**. This prevents potential issues with the [translation tags](#things-not-to-do-with-translation-tags).
*   Design each paragraph around one idea.
*   Present the most important information first.
*   Address the reader directly.

!!! example
    *The user must click on the button* or *One must click on the button* becomes *Click on the button.*

*   Use [simple words and phrases](http://www.plainlanguage.gov/howto/wordsuggestions/simplewords.cfm).
*   Use the present tense.

!!! example
    *Doing this will launch the XYZ application* becomes *This launches the XYZ application.*

*   Use the active voice.

!!! example
    *The file is edited by the system administrator* becomes *The system administrator edits the file.*

*   Stay positive.

!!! example
    *Don't use the passive voice* becomes *Use the active voice.*

*   Use consistent terms.
    Yes, synonyms make a text less boring, but for a new user or one reading in a second language, interchangeable terms (*e.g.* "machine", "host", "node", "server") may be confusing.

!!! tip "Use precise words, not 'system'"
    The word "system" is used frequently in computing with different meanings (legacy system, new system, cloud system, file system, module system, job scheduling system, GPU system, storage system, *etc.*). It is not always clear to a new user what we are talking about. Whenever possible, please try to use a more precise word (cluster, storage space, scheduler, *etc.*).

#### External resources

*   Online self-guided [Technical Writing courses from Google](https://developers.google.com/tech-writing/overview).
*   [Documentation guide from Write the Docs](https://www.writethedocs.org/guide/).

### Layout style

When in doubt, imitate the masters. Look at an existing page you like and follow the style. If there isn’t one at [docs.alliancecan.ca/](https://docs.alliancecan.ca/), look for one at [Wikipedia](https://en.wikipedia.org/wiki/Main_Page).

*   Separate graphic design from content as much as possible. Don’t use extra line breaks to adjust vertical spacing. Don’t indent paragraphs with tabs or spaces or add extra spaces after a sentence. If we want to make any such style adjustments we will make them universally using stylesheets and templates.
*   Screenshots are useful resources, especially in how-tos and tutorials. On the MediaWiki site, full-sized screenshots should not be placed in-line as they interrupt the structure and flow of the text. Instead, they should float to the right-hand side and be scaled down. If important information becomes unreadable, a cropped picture might be better, or the reader should be reminded in the caption that they can "Click on the image for a larger version."
*   Leave one blank line at the end of each section before the following header. The translation package uses the blank line and header to determine the boundaries of translation units.
*   Links to other pages or sites should have a human-oriented description for display rather than the raw URL.
*   Capitalize only the first word and proper nouns in titles and headings. Following [Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Naming_conventions_(capitalization)), we prefer the [APA sentence case](https://apastyle.apa.org/style-grammar-guidelines/capitalization/sentence-case) for all titles, including page titles.

### Templates

Several templates are available on the MediaWiki site. Please use them as appropriate. Of particular interest are templates for [Including a command within the wiki](including_a_command_within_the_wiki.md) and for [Including a source code file within the wiki](including_a_source_code_file_within_the_wiki.md).

## Translation

To translate a page, one first writes the content in the original language. Second, the page is marked for translation. Then, a *human* translates the page using organisational tools provided by the wiki extension [Translate](https://www.mediawiki.org/wiki/Extension:Translate). Tutorials for this extension can be found [here](https://www.mediawiki.org/wiki/Help:Extension:Translate). Finally, a second human reviews the translation. If a page has not yet been translated, users can see the page in the original language. If a translation has not yet been reviewed, users can see the non-reviewed translation.

Marking a page for translation will trigger an analysis of the content of the wiki page. The page content will be split by the extension into so-called translation units. Translation units can be a title, a paragraph, an image, *etc.* These small units can then be translated one by one, ensuring that a modification to a page does not trigger the translation of the whole page. This also allows tracking of what percentage of a page is translated, or outdated.

### Mark a new page for translation

When you have written a page, you should tag it for translation. Here are the steps to do so:

1.  First, if the original language of the page is French, change it on Special:PageLanguage.
2.  Ensure that the content to be translated is enclosed within `<translate>` `</translate>` tags.
3.  Conversely, please enclose code blocks in `</translate>` `<translate>` tags so that they are excluded from translation.
4.  Likewise, try to exclude wiki markup (tables, tags, *etc.*) from translation.
5.  Ensure that the tag `<languages />` appears at the very top of the page. This will show a box with the list of languages the page is translated into.
6.  Go in “View” mode, and then click on the “Mark this page for translation”.
7.  Review the translation units. Check that code blocks and wiki markup are excluded, and all plain text is included.
8.  In the “Priority languages” section, write either “fr” or “en” as the priority language, that is, the language into which it needs to be translated.
9.  Click on “Mark this version for translation”.

### Things not to do with translation tags

Translation tags are what identify a unit of translation. They look like `<!--T:20-->`. They are **entirely** managed by the translation extension. When you edit a page:

*   do NOT edit translation tags
*   do NOT copy translation tags
*   do NOT move translation tags
*   do NOT create translation tags
*   do NOT duplicate translation tags

The only safe thing to do with translation tags is to DELETE them, and let the extension tag the page again when you mark it for translation.

If you start editing a section and you see a lonely translation tag at the end of the wikicode, stop there!, go back to the page and click to edit the whole page instead.

*   The system gives an error if you try to submit a change for a section with a translation tag at the end of the wikicode (even if this problem is coming from the wiki, in the first place -- this is a known issue).
*   Do NOT delete that translation tag at the end of the section, because this would invalidate an actual translation in production. Instead, copy and paste any edit you made in a local text editor, cancel your changes in the wikicode editor and start editing the wikicode of the whole page.
*   Do NOT add new content after the translation tag at the end of the wikicode of a section.

### Mark changes to a page for translation

First, try to mark a page for translation only once it is stable.
Second, if you do have to make a change to a page that has been translated, make sure you do NOT change the tags of the form `<!--T:3-->`. You must never manually edit those tags or copy them. Those are automatically generated.

Once you have done your edits, you can mark the changes to be translated by doing the following:

1.  Ensure that the new text to be translated is enclosed within `<translate>` `</translate>` tags.
2.  Conversely, please enclose code blocks in `</translate>` `<translate>` tags so that they are excluded from translation.
3.  Likewise, try to exclude wiki markup (tables, tags, *etc.*) from translation.
4.  Go in “View” mode. You should see the text “This page has changes since it was last marked for translation.” at the top of the page. Click on “marked for translation”.
5.  Review the translation units. Check that code blocks and wiki markup are excluded, and all plain text is included.
6.  In the “Priority languages” section, verify that “fr” or “en” appears as the priority language, that is, the language into which it needs to be translated.
7.  Click on “Mark this version for translation”.

Note that the "Page translation" page includes a checkbox for "Do not invalidate translations" in each changed unit. You should only select this option if the change is something like a typo - which shouldn't cause the other-language version to need adjustment.

### Code blocks are not translated

Our professional human translator is not a programmer.
They cannot distinguish between code and comments in every possible language,
so the documentation team has instructed the translator to exclude code blocks from translation.

Putting explanatory comments in code is excellent programming practice which we wish to encourage,
but the value of the comments is decreased if the comments aren't translated.
The documentation team has not found a solution for this that works in every case.
Here are some suggestions:

1.  Move the information contained in the comments outside the code block, into the surrounding text (which will then be translated).
2.  Leave an index comment (*e.g.* "NOTE 1", "NOTE 2") to connect the external text to the relevant line of code.
3.  If you're sufficiently bilingual, and familiar with the translation apparatus, you may translate the code block yourself.

Please *do not* leave example code uncommented, but please *do* remember that
comments will not normally be translated, and consider how this will affect the understanding
of the user reading the page in translation.

### Translating the sidebar

To add an item that is to be translated in the sidebar, use the following steps:

1.  Add the new content to MediaWiki:Sidebar. Any item which should be translated should be added as either `some-tag` or, if it is a link, `{{int:some-tag}}`.
2.  Add the tags to MediaWiki:Sidebar-messages.
3.  Define the content of the tag in English on MediaWiki:some-tag (replace `some-tag` by the actual tag).
4.  Translate the content of the tag on [this page](https://docs.alliancecan.ca/mediawiki/index.php?title=Special:Translate&language=fr&group=wiki-sidebar&filter=%21translated&action=translate).

## "Available software" page

Tables on the [Available software](../programming/available_software.md) page are automatically generated from module files in CVMFS. In order to add a link to a new page from the "Documentation" column of those tables, add an entry to [https://github.com/ComputeCanada/wiki_module_bot/blob/main/module_wiki_page.json](https://github.com/ComputeCanada/wiki_module_bot/blob/main/module_wiki_page.json). Please add this change to the definitive copy of the file.

Changes may take six hours to propagate to the wiki page.