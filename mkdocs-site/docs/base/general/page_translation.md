---
title: "Page translation"
slug: "page_translation"
lang: "base"

source_wiki_title: "Page translation"
source_hash: "49a29155d8aa8949faf60e190b984cd5"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T09:42:45.084160+00:00"

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

To translate a page, one first writes the content in the original language. Second, the page is marked for translation. Then, a *human* translates the page using organizational tools provided by the wiki extension [Translate](https://www.mediawiki.org/wiki/Extension:Translate). Tutorials for this extension can be found [here](https://www.mediawiki.org/wiki/Help:Extension:Translate). Finally, a second human reviews the translation. If a page has not yet been translated, users can see the page in the original language. If a translation has not yet been reviewed, users can see the non-reviewed translation.

Marking a page for translation will trigger an analysis of the content of the wiki page. The page content will be split by the extension into so-called translation units. Translation units can be a title, a paragraph, an image, etc. These small units can then be translated one by one, ensuring that a modification to a page does not trigger the translation of the whole page. This also allows tracking of what percentage of a page is translated, or outdated.

## How does one mark a new page for translation?
When you have written a page, you should tag it for translation. Here are the steps to do so:
1. Ensure that the wiki code to be translated is enclosed within `<translate></translate>` tags.
2. Ensure that the tag `<languages />` appear at the very top of the page. This will show a box.
3. Go in “View” mode, and then click on the “Mark this page for translation”
4. Review the translation units.
   1. Try to ensure that no wiki code (tables, tags, etc.) gets translated. This can be done by breaking the page in multiple `<translate></translate>` sections.
5. In the “Priority languages” section, write either “fr” or “en” as the priority language, that is, the language into which it needs to be translated.
6. Click on “Mark this version for translation”

## How does one mark changes to a page for translation?
First, try to mark a page for translation only once it is stable.
Second, if you do have to make a change to a page that has been translated, make sure you do NOT change the tags of the form `<!--T:3-->`. Those are automatically generated.

Once you have done your edits, you can mark the changes to be translated by doing the following:
1. Ensure that the new text to be translated is enclosed within `<translate></translate>` tags.
2. Go in “View” mode. You should see the text “This page has changes since it was last marked for translation.” at the top of the page. Click on “marked for translation”.
3. Review the translation units.
   1. Try to ensure that no wiki code (tables, tags, etc.) gets translated. This can be done by breaking the page in multiple `<translate></translate>` sections.
4. In the “Priority languages” section, write either “fr” or “en” as the priority language, that is, the language into which it needs to be translated.
5. Click on “Mark this version for translation”