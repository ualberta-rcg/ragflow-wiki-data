<languages />
In your project spaces, your data should be documented such that you know the purpose of each file. A README file is usually the first reference point.

Using README files on clusters is part of active research data management. It will be useful for future publications and for team members wondering what are the files in some directory.

= What to write in a README file =

* Source of the files
** Website or external database
** Authors
** Year
* Types of files present in the directory
** Structure of directories
* Which files are temporary
* Which files are actively used
* Which files could be archived
* Who should be able to access what and when:
** On the cluster;
** On a data repository (in some future).

= Formats of a README file =

* <code>README</code> or <code>README.txt</code>
** Free text format.
** Better than nothing, but no conventional style is enforced.
* <code>README.md</code> ([https://www.markdownguide.org/ Markdown]), <code>README.rst</code> ([https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html reStructuredText])
** Structured text format that remains human readable.
** Can be compiled into formatted text (HTML or PDF).
* <code>README.yaml</code> ([https://yaml.org YAML]), <code>README.json</code> ([https://en.wikipedia.org/wiki/JSON JSON]), <code>README.xml</code> ([https://developer.mozilla.org/en-US/docs/Web/XML/Guides/XML_introduction XML])
** Slightly less human-readable.
** Machine-readable, which means a program can validate the contents of the README file.
** Could be used to generate a README file in another format.

= References =

* [https://rdm.mcmaster.ca/readme McMaster - README Generator]
* [https://ubc-library-rc.github.io/rdm/content/03_create_readme.html UBC - Create a README file]
* [https://subjectguides.uwaterloo.ca/rdm/basics#readme UWaterloo - README Files for Data Deposits]