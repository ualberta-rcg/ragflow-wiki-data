---
title: "Including a source code file within the wiki/fr"
slug: "including_a_source_code_file_within_the_wiki"
lang: "fr"

source_wiki_title: "Including a source code file within the wiki/fr"
source_hash: "d742fdf390174e67bddf8f52a7d79442"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:00:44.444041+00:00"

tags:
  []

keywords:
  - "numéros de lignes"
  - "syntaxhighlight"
  - "caractères spéciaux"
  - "gabarit Fichier"
  - "code source"

questions:
  - "Quels sont les paramètres principaux requis pour utiliser le gabarit {{Fichier}} afin d'inclure du code source ?"
  - "Comment doit-on formater les caractères spéciaux comme le trait vertical ou le signe d'égalité pour éviter les conflits avec l'analyseur MediaWiki ?"
  - "Quelle option faut-il ajouter au gabarit pour que les numéros de lignes du code source s'affichent ?"
  - "Quels sont les paramètres principaux requis pour utiliser le gabarit {{Fichier}} afin d'inclure du code source ?"
  - "Comment doit-on formater les caractères spéciaux comme le trait vertical ou le signe d'égalité pour éviter les conflits avec l'analyseur MediaWiki ?"
  - "Quelle option faut-il ajouter au gabarit pour que les numéros de lignes du code source s'affichent ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Tel que mentionné à la page [Inclure du code source dans le wiki](https://docs.computecanada.ca/wiki/Including_source_code_within_the_wiki/fr), les balises `<syntaxhighlight>` servent à inclure du code. Si vous désirez que le code soit à part du texte, utilisez le gabarit `{{File}}`. Ce gabarit prend le nom (paramètre *name*), la langue (paramètre *lang*) et le contenu (paramètre *contents*) du fichier comme arguments. Ce gabarit utilise par défaut le langage bash.

Par exemple,
```text
{{Fichier
  |name=myfile.sh
  |lang="bash"
  |contents=
#!/bin/bash
echo "ceci est un script bash"
}}
```

donne le résultat suivant
```bash title="myfile.sh"
#!/bin/bash
echo "ceci est un script bash"
```

## Caractères spéciaux : Trait vertical et signe d'égalité
Les scripts bash contiennent souvent des caractères qui ont aussi une signification pour l'analyseur syntaxique (*parser*) MediaWiki.
* Si le code source contient un trait vertical (le caractère `|`), remplacez-le par `{{!}}`.
* Dans certains cas vous devez remplacer le signe d'égalité (le caractère `=`) par `{{!}}`.

## Affichage des numéros de lignes
Pour afficher les numéros de lignes, ajoutez l’option **lines=yes**, par exemple
```text
{{Fichier
  |name=monfichier.sh
  |lang="bash"
  |lines=yes
  |contents=
#!/bin/bash
echo "ceci est un script bash"
}}
```

donne le résultat suivant
```bash linenums="true" title="myfile.sh"
#!/bin/bash
echo "ceci est un script bash"