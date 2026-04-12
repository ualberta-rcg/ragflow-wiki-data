---
title: "Page translation/en"
slug: "page_translation"
lang: "en"

source_wiki_title: "Page translation/en"
source_hash: "483cb1eea81b7debabe0d96a2bc5cd4f"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:11:15.615691+00:00"

tags:
  []

keywords:
  - "translation units"
  - "Translate extension"
  - "mark for translation"
  - "translate tags"
  - "page translation"

questions:
  - "What is the overall workflow for translating a wiki page and how do translation units function within this process?"
  - "What specific tags and steps are required to mark a newly created page for translation?"
  - "How should users manage and mark edits made to an already translated page to ensure existing translation tags are not disrupted?"
  - "What is the overall workflow for translating a wiki page and how do translation units function within this process?"
  - "What specific tags and steps are required to mark a newly created page for translation?"
  - "How should users manage and mark edits made to an already translated page to ensure existing translation tags are not disrupted?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

To translate a page, one first writes the content in the original language. Second, the page is marked for translation. Then, a *human* translates the page using organizational tools provided by the wiki extension [Translate](https://www.mediawiki.org/wiki/Extension:Translate). Tutorials for this extension can be found [here](https://www.mediawiki.org/wiki/Help:Extension:Translate). Finally, a second human reviews the translation. If a page has not yet been translated, users can see the page in the original language. If a translation has not yet been reviewed, users can see the non-reviewed translation.

Marking a page for translation will trigger an analysis of the content of the wiki page. The page content will be split by the extension into so-called translation units. Translation units can be a title, a paragraph, an image, etc. These small units can then be translated one by one, ensuring that a modification to a page does not trigger the translation of the whole page. This also allows tracking of what percentage of a page is translated, or outdated.

## How to mark a new page for translation

When you have written a page, you should tag it for translation. Here are the steps to do so:

1.  Ensure that the wiki code to be translated is enclosed within ``<translate>`` ``</translate>`` tags.
2.  Ensure that the tag ``<languages />`` appears at the very top of the page. This will show a box.
3.  Go into "View" mode, and then click on the "Mark this page for translation".
4.  Review the translation units.
    *   Try to ensure that no wiki code (tables, tags, etc.) gets translated. This can be done by breaking the page into multiple ``<translate>`` ``</translate>`` sections.
5.  In the "Priority languages" section, write either "fr" or "en" as the priority language, that is, the language into which it needs to be translated.
6.  Click on "Mark this version for translation".

## How to mark changes to a page for translation

First, try to mark a page for translation only once it is stable.

!!! warning
    If you do have to make a change to a page that has been translated, make sure you do **NOT** change the tags of the form ``<!--T:3-->``. Those are automatically generated.

Once you have done your edits, you can mark the changes to be translated by doing the following:

1.  Ensure that the new text to be translated is enclosed within ``<translate>`` ``</translate>`` tags.
2.  Go into "View" mode. You should see the text "This page has changes since it was last marked for translation." at the top of the page. Click on "marked for translation".
3.  Review the translation units.
    *   Try to ensure that no wiki code (tables, tags, etc.) gets translated. This can be done by breaking the page into multiple ``<translate>`` ``</translate>`` sections.
4.  In the "Priority languages" section, write either "fr" or "en" as the priority language, that is, the language into which it needs to be translated.
5.  Click on "Mark this version for translation".