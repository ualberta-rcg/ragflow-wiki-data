---
title: "Page translation/fr"
slug: "page_translation"
lang: "fr"

source_wiki_title: "Page translation/fr"
source_hash: "efd73b20550fe5b51d5637ab657487bb"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:11:42.395738+00:00"

tags:
  []

keywords:
  - "marquer pour traduction"
  - "traduction"
  - "unités de traduction"
  - "balises"
  - "extension Translate"

questions:
  - "Quel est le processus global de traduction d'une page et pourquoi l'extension sépare-t-elle le contenu en unités de traduction ?"
  - "Quelles sont les balises et les étapes nécessaires pour préparer et marquer une nouvelle page pour la traduction ?"
  - "Quelles précautions particulières faut-il prendre lors de la modification du contenu d'une page déjà traduite ?"
  - "Quel est le processus global de traduction d'une page et pourquoi l'extension sépare-t-elle le contenu en unités de traduction ?"
  - "Quelles sont les balises et les étapes nécessaires pour préparer et marquer une nouvelle page pour la traduction ?"
  - "Quelles précautions particulières faut-il prendre lors de la modification du contenu d'une page déjà traduite ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Pour traduire une page, il faut d'abord rédiger le contenu original. Une fois que c'est fait, on marque la page pour traduction. Une personne procède ensuite à la traduction de la page en utilisant les outils fournis par l'extension [Translate](https://www.mediawiki.org/wiki/Extension:Translate). Des tutoriels pour cette extension peuvent être consultés [ici](https://www.mediawiki.org/wiki/Help:Extension:Translate). Finalement, une deuxième personne révise la traduction. Si une page n'a pas encore été traduite, elle est affichée dans la langue originale. Si la traduction n'a pas encore été révisée, la version non révisée est affichée.

Marquer une page pour la traduction déclenche une analyse de son contenu. L'extension séparera le contenu en plusieurs unités de traduction. Celles-ci peuvent être un titre, un paragraphe, une image, etc. Ces petites unités peuvent ensuite être traduites une par une. Cette séparation assure que la modification d'une page ne nécessite pas de la traduire à nouveau dans son entièreté. Cela permet aussi de suivre le pourcentage d'une page qui n'est pas traduite, ou dont le contenu a été modifié depuis la dernière traduction.

## Traduire une nouvelle page

Lorsque vous avez terminé de rédiger une page, vous devriez la marquer pour la traduction. Voici les étapes à suivre :

1.  Assurez-vous que le texte qui doit être traduit est inclus dans des balises `<translate> </translate>`.
2.  Assurez-vous que la balise `<languages />` apparaît au haut de la page. Ceci affichera une boîte contenant les différentes langues.
3.  Allez en mode *visualisation*, et cliquez sur *Marquer cette page pour traduction*.
4.  Révisez les unités de traduction.
    *   Essayez d'éviter la traduction de code wiki (tables, balises, etc.); cela peut être fait en séparant la page en plusieurs sections `<translate> </translate>`.
5.  Dans la section *Langages prioritaires*, inscrivez *fr* ou *en* comme langue prioritaire. Ceci identifie la langue vers laquelle la page doit être traduite.
6.  Cliquez sur *Marquer cette page pour traduction*.

## Traduire les modifications à une page existante

!!! tip "Conseil"
    Pour de meilleurs résultats, tentez de marquer une page pour la traduction seulement lorsque son contenu est stable.

!!! warning "Attention"
    Si vous devez modifier une page déjà traduite, *ne changez PAS* les balises de la forme `<!--T:3-->`. Celles-ci sont générées automatiquement par l'extension de traduction.

Lorsque vous avez terminé vos changements, vous pouvez marquer ceux-ci pour être traduits en suivant les étapes suivantes :

1.  Assurez-vous que le nouveau texte à être traduit est inclus à l'intérieur des balises `<translate> </translate>`.
2.  Allez en mode *visualisation*. Vous devriez voir le texte *Cette page a eu des modifications depuis qu’elle a été dernièrement marquée pour être traduite.* au haut de la page. Cliquez sur *marquée pour être traduite*.
3.  Révisez les unités de traduction.
    *   Essayez d'éviter la traduction de code wiki (tables, balises, etc.); cela peut être fait en séparant la page en plusieurs sections `<translate> </translate>`.
4.  Dans la section *Langages prioritaires*, inscrivez *fr* ou *en* comme langue prioritaire. Ceci identifie la langue vers laquelle la page doit être traduite.
5.  Cliquez sur *Marquer cette page pour traduction*.