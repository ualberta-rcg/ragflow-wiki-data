---
title: "Including a source code file within the wiki/fr"
slug: "including_a_source_code_file_within_the_wiki"
lang: "fr"

source_wiki_title: "Including a source code file within the wiki/fr"
source_hash: "d742fdf390174e67bddf8f52a7d79442"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T07:21:18.780110+00:00"

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

Tel que mentionné à la page [Inclure du code source dans le wiki](https://docs.computecanada.ca/wiki/Including_source_code_within_the_wiki/fr), les balises `<syntaxhighlight> </syntaxhighlight>` servent à inclure du code. Si vous voulez que le code soit distinct du texte, utilisez le gabarit `{{Fichier}}`. Ce gabarit accepte le nom (paramètre **name**), la langue (paramètre **lang**) et le contenu (paramètre **contents**) du fichier comme arguments. Ce gabarit utilise **bash** comme langage par défaut.

Par exemple :

```
{{Fichier
  |name=myfile.sh
  |lang="bash"
  |contents=
#!/bin/bash
echo "ceci est un script bash"
}}
```

donne le résultat suivant :

```bash title="myfile.sh"
#!/bin/bash
echo "ceci est un script bash"
```

## Caractères spéciaux : Trait vertical et signe d'égalité

Les scripts bash contiennent souvent des caractères qui ont une signification particulière pour l'analyseur syntaxique (*parser*) de MediaWiki.

*   Si le code source contient un trait vertical (le caractère `|`), remplacez-le par `{{!}}`.
*   Dans certains cas, il faut remplacer le signe d'égalité (le caractère `=`) par `{{!}}`.

## Affichage des numéros de lignes

Pour afficher les numéros de lignes, ajoutez l’option **lines=yes**, par exemple :

```
{{Fichier
  |name=monfichier.sh
  |lang="bash"
  |lines=yes
  |contents=
#!/bin/bash
echo "ceci est un script bash"
}}
```

donne le résultat suivant :

```bash title="myfile.sh" linenums="1"
#!/bin/bash
echo "ceci est un script bash"