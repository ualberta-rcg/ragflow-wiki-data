<languages />
Dans vos espaces /project, vos données doivent être documentées pour bien décrire l'utilité de chaque fichier. Un fichier README est généralement la première référence.

L'utilisation de fichiers README sur nos grappes fait partie de la gestion active des données de recherche. Ils seront utiles pour les publications futures et pour que les membres de l'équipe sachent à quoi correspondent les fichiers contenus dans un répertoire.

<span id="What_to_write_in_a_README_file"></span>
= Contenu d'un fichier README =

* Source des fichiers
**  Site web ou base de données externe
**  Auteurs
**  Année
* Types de fichiers présents dans le répertoire
** Structure des répertoires
* Quels fichiers sont temporaires
* Quels fichiers sont activement utilisés
* Quels fichiers sont archivés
* Qui doit avoir accès à quoi et quand&nbsp;:
** Sur la grappe
** Sur un référentiel de données (dans le futur)

<span id="Formats_of_a_README_file"></span>
=Formats des fichiers README=

* <code>README</code> ou <code>README.txt</code>
** format texte libre
** mieux que rien, mais aucun style conventionnel n'est imposé
* <code>README.md</code> ([https://www.markdownguide.org/ Markdown]), <code>README.rst</code> ([https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html reStructuredText])
** format de texte structuré lisible par l'utilisateur
** peut être compilé en texte formaté (HTML ou PDF).
* <code>README.yaml</code> ([https://yaml.org YAML]), <code>README.json</code> ([https://fr.wikipedia.org/wiki/JavaScript_Object_Notation JSON]), <code>README.xml</code> ([https://developer.mozilla.org/fr/docs/Web/XML/Guides/XML_introduction XML])
** légèrement moins lisible par l'utilisateur
** lisible par machine, ce qui signifie qu'un programme peut valider le contenu du fichier README.
** peut être utilisé pour générer un fichier README dans un autre format

<span id="References"></span>
= Références =

* [https://rdm.mcmaster.ca/readme McMaster, README Generator]
* [https://ubc-library-rc.github.io/rdm/content/03_create_readme.html UBC, Create a README file]
* [https://subjectguides.uwaterloo.ca/rdm/basics#readme UWaterloo, README Files for Data Deposits]