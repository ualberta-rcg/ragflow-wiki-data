---
title: "README files/fr"
slug: "readme_files"
lang: "fr"

source_wiki_title: "README files/fr"
source_hash: "70f286be861d1f2c3dd6c56ea522d93f"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T10:42:40.352083+00:00"

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

Dans vos espaces `/project`, vos données doivent être documentées pour bien décrire l'utilité de chaque fichier. Un fichier README est généralement la première référence.

L'utilisation de fichiers README sur nos grappes fait partie de la gestion active des données de recherche. Ils seront utiles pour les publications futures et pour que les membres de l'équipe sachent à quoi correspondent les fichiers contenus dans un répertoire.

## Contenu d'un fichier README

*   Source des fichiers
    *   Site web ou base de données externe
    *   Auteurs
    *   Année
*   Types de fichiers présents dans le répertoire
    *   Structure des répertoires
*   Quels fichiers sont temporaires
*   Quels fichiers sont activement utilisés
*   Quels fichiers sont archivés
*   Qui doit avoir accès à quoi et quand :
    *   Sur la grappe
    *   Sur un référentiel de données (dans le futur)

## Formats des fichiers README

*   `README` ou `README.txt`
    *   Format texte libre
    *   Mieux que rien, mais aucun style conventionnel n'est imposé
*   `README.md` ([Markdown](https://www.markdownguide.org/)), `README.rst` ([reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html))
    *   Format de texte structuré lisible par l'utilisateur
    *   Peut être compilé en texte formaté (HTML ou PDF).
*   `README.yaml` ([YAML](https://yaml.org)), `README.json` ([JSON](https://fr.wikipedia.org/wiki/JavaScript_Object_Notation)), `README.xml` ([XML](https://developer.mozilla.org/fr/docs/Web/XML/Guides/XML_introduction))
    *   Légèrement moins lisible par l'utilisateur
    *   Lisible par machine, ce qui signifie qu'un programme peut valider le contenu du fichier README.
    *   Peut être utilisé pour générer un fichier README dans un autre format

## Références

*   [McMaster, README Generator](https://rdm.mcmaster.ca/readme)
*   [UBC, Create a README file](https://ubc-library-rc.github.io/rdm/content/03_create_readme.html)
*   [UWaterloo, README Files for Data Deposits](https://subjectguides.uwaterloo.ca/rdm/basics#readme)