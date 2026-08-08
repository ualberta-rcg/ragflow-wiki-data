---
title: "Authoring guidelines/fr"
slug: "authoring_guidelines"
lang: "fr"

source_wiki_title: "Authoring guidelines/fr"
source_hash: "68f4420da4e78b527792219803c71acd"
last_synced: "2026-08-07T19:46:17.777436+00:00"
last_processed: "2026-08-07T22:23:56.507891+00:00"

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

## Qui peut contribuer à ce wiki?
Si vous avez un compte avec l'Alliance, vous pouvez contribuer. La principale tâche de notre équipe est de fournir une documentation complète et juste, mais nous sommes à l'ère Wikipédia. Si vous remarquez un problème évident comme un lien brisé ou une coquille, vous pouvez bien entendu le corriger. Si vous le souhaitez, vous pouvez aussi rédiger un article en rapport avec un logiciel que vous connaissez bien. Notre équipe de documentation révise les articles rédigés pour vérifier leur conformité aux présentes directives.

La collaboration au wiki ne se fait pas de façon anonyme. Vous devez vous connecter en utilisant les informations d'identification de votre compte; ceci nous permet de savoir qui a rédigé ou modifié le contenu.

## Contenu du wiki
Ce wiki n'est pas l'endroit où afficher l'information qui relève de la responsabilité de l'équipe des communications et du marketing, ce qui inclut toute information pour communication au grand public, aux médias et aux agences de financement. Aussi, l'information touchant les activités de formation et de rayonnement ne convient pas au contenu de la documentation technique. Avant de publier une page ou de modifier le contenu du wiki, posez-vous les questions suivantes :

*   Cette information est-elle au sujet de la disponibilité d'une grappe ou d'un service? Si c'est le cas, cette grappe ou ce service a-t-il fait l'objet d'une annonce? Autrement, communiquez avec l'équipe des communications et du marketing avant de publier.
*   S'agit-il d'un état qui change de jour en jour (disponible, hors ligne, en maintenance, etc.)? Cette information doit paraître sur [https://status.alliancecan.ca/](https://status.alliancecan.ca/).
*   L'information s'adresse-t-elle aux utilisateurs et utilisatrices ou à nos équipes techniques? Si elle s'adresse à une équipe technique, elle devrait se trouver sur [https://wiki.computecanada.ca/staff/](https://wiki.computecanada.ca/staff/) plutôt que sur [https://docs.alliancecan.ca/](https://docs.alliancecan.ca/).
*   Cette information a-t-elle une incidence sur la sécurité de nos systèmes ou sur la sécurité des données présentes sur nos systèmes? Si c'est le cas, communiquez avec l'équipe de la sécurité de l'information avant de publier.
*   L'information s'adresse-t-elle aux utilisateurs potentiels plutôt qu'aux détenteurs de compte? Il y a ici une zone grise : tout comme un utilisateur potentiel, un détenteur de compte pourrait vouloir connaître les détails techniques en rapport avec nos services et nos sites. Cependant, si l'information n'est d'intérêt que pour les utilisateurs potentiels, elle devrait se retrouver sur [https://www.alliancecan.ca](https://www.alliancecan.ca) plutôt que sur [https://docs.alliancecan.ca/](https://docs.alliancecan.ca/).
*   Il est approprié de publier des liens externes; voir par exemple *Obtenir un compte*.
*   L'information explique-t-elle comment utiliser une grappe, une application ou un service existants? Si c'est le cas, allez-y.

Si vous avez encore des doutes :

*   si vous êtes à l'emploi de l'Alliance, utilisez le canal #rsnt-documentation dans Slack;
*   si vous n'êtes pas à l'emploi de l'Alliance, communiquez avec le [soutien technique](../support/technical_support.md).

## Guide de style
Dans la mesure du possible, évitez de téléverser des fichiers PDF. Copiez plutôt le texte sélectionné à partir d'un PDF et modifiez-le ensuite selon les normes du wiki en incluant par exemple les liens internes menant vers d'autres pages ou sections.

### Ébauches
Autrefois, si une nouvelle page était en développement et incomplète, on la marquait comme une ébauche dans le wiki en utilisant le gabarit `{{Draft}}`.

### Rédaction
Le guide de style aide les rédacteurs à produire une documentation technique qui facilite l'apprentissage. Une documentation bien préparée est agréable au lecteur et projette une image positive de l'auteur.
Il existe plusieurs guides de style pour la documentation technique. L'Office québécois de la langue française en liste quelques-uns.
Aucun guide de style n'existe pour notre wiki, mais il est important de retenir certaines pratiques usuelles :

*   Énoncez une idée principale par paragraphe.
*   Placez l'information en ordre d'importance.
*   Adressez-vous directement au lecteur.
    *   Par exemple, *Cliquez sur le bouton* plutôt que *L'utilisateur doit cliquer sur le bouton*.
*   Utilisez le plus possible un vocabulaire courant et simple.
*   Construisez vos phrases avec des verbes au présent.
*   Utilisez la voix active.
    *   Par exemple, *Le fichier contient les paramètres valides* plutôt que *Les paramètres valides sont contenus dans le fichier*.
*   Utilisez la forme positive.
    *   Par exemple, *Répondre OUI* plutôt que *Ne pas répondre NON*.
*   Employez le mot juste.
    *   Bien sûr, les synonymes rendent le texte moins ennuyant, mais ils peuvent créer de la confusion chez un nouvel utilisateur ou un utilisateur dont la langue maternelle est différente de celle du texte (par exemple, *machine*, *hôte*, *nœud*, *serveur*).

Le terme *système* est souvent employé de façon générique : il peut désigner entre autres un ordinateur, une grappe ou encore un environnement ou un logiciel. Veillez à utiliser le mot juste pour éviter toute confusion.

#### Autres ressources

*   [Cours de rédaction technique de Google](https://developers.google.com/tech-writing/overview)
*   [Guide de documentation de Write the Docs](https://www.writethedocs.org/guide/)

### Mise en page
Si vous doutez, imitez les maîtres. Utilisez le style d'une page existante. Si vous n'en trouvez pas sur [docs.alliancecan.ca/](https://docs.alliancecan.ca/), cherchez sur [Wikipédia](http://www.wikipedia.org).

*   N'utilisez pas des sauts de ligne pour ajuster l'espacement vertical. N'utilisez pas la tabulation ou des espaces pour mettre un paragraphe en retrait; n'ajoutez pas d'espace à la fin d'une phrase. Si ce type de formatage est souhaitable, nous préparerons des feuilles de style ou des gabarits, le cas échéant.
*   Employez le moins de synonymes possible. Bien sûr, les synonymes rendent le texte moins ennuyant, mais ils peuvent créer de la confusion chez un nouvel utilisateur ou un utilisateur dont la langue maternelle est différente de celle du texte (par exemple, *machine*, *hôte*, *nœud*, *serveur*).
*   Laissez une ligne vide à la fin d'une section, avant le titre de la prochaine section.

### Gabarits
Plusieurs gabarits sont disponibles. Veuillez les utiliser au besoin. Nous attirons votre attention particulièrement sur les gabarits pour Inclure une commande dans une page wiki et Inclure un fichier de code source dans une page wiki.

## Traduction
!!! note "Note sur la traduction"
    Le contenu de cette section décrit le processus de traduction tel qu'il était géré dans l'ancien système MediaWiki. Pour les pratiques de traduction du site actuel basé sur MkDocs Material, veuillez vous référer aux directives spécifiques à cette plateforme, qui ne sont pas détaillées ici.

La page dans la langue source devait être marquée pour la traduction. Toute personne pouvait traduire une page marquée pour traduction avec les outils de l'extension wiki [Traduire](https://www.mediawiki.org/wiki/Help:Extension:Translate/Page_translation_example/fr). Vous trouverez un tutoriel [ici](https://www.mediawiki.org/wiki/Help:Extension:Translate/Page_translation_example/fr). Une page traduite pouvait ensuite être révisée.

Lorsqu'une page était marquée pour la traduction, l'extension Traduire analysait son contenu et le divisait en unités de traduction qui étaient par exemple un titre, un paragraphe, un élément visuel ou autre. Les unités discrètes étaient traduites individuellement : ainsi, une modification à une unité n'avait pas d'effet sur le reste de la page et il était possible de connaître le pourcentage de la page déjà traduit ou devant être mis à jour.

### Marquer une page pour la traduction (ancien système MediaWiki)
Quand vous aviez terminé la rédaction d'une page, vous deviez signaler qu'elle était prête à être traduite en suivant ces étapes :

1.  Le contenu à traduire devait être délimité par des balises `<translate>`.
2.  Les balises `<translate>` étaient aussi utilisées pour délimiter le code qui ne devait pas être traduit.
3.  Elles servaient également à isoler le code de marquage du wiki (par exemple, les tableaux et les balises).
4.  La balise `<languages />` devait apparaître au tout début de la page pour afficher une boîte listant les langues disponibles.
5.  En mode « Affichage », il fallait cliquer sur « Marquer cette page pour la traduction ».
6.  Il fallait ensuite réviser les unités de traduction pour s'assurer que le texte était complet et que le code de programmation et le code wiki (tableaux, balises, etc.) étaient exclus.
7.  La langue prioritaire (cible) devait être sélectionnée.
8.  Puis, on cliquait sur « Marquer cette page pour la traduction ».

### Ce qu'il ne fallait pas faire avec les balises de traduction (ancien système MediaWiki)
Les balises de traduction sont ce qui identifie une unité de traduction. Elles ressemblent à `--T:20--`. Elles sont **entièrement** gérées par l'extension de traduction. Lorsque vous éditiez une page :

*   il ne fallait PAS éditer les balises de traduction
*   il ne fallait PAS copier les balises de traduction
*   il ne fallait PAS déplacer les balises de traduction
*   il ne fallait PAS créer de balises de traduction
*   il ne fallait PAS dupliquer les balises de traduction

La seule chose sûre à faire avec les balises de traduction était de les SUPPRIMER, et de laisser l'extension baliser la page à nouveau lorsque vous la marquiez pour la traduction.

Si vous commenciez à éditer une section et que vous voyiez une balise de traduction isolée à la fin du wikicode, vous deviez vous arrêter là! Revenir à la page et cliquer pour éditer la page entière à la place.

*   Le système donnait une erreur si vous essayiez de soumettre un changement pour une section avec une balise de traduction à la fin du wikicode (même si ce problème venait du wiki, en premier lieu – c'est un problème connu).
*   Il ne fallait PAS supprimer cette balise de traduction à la fin de la section, car cela invaliderait une traduction réelle en production. Au lieu de cela, vous deviez copier-coller toute modification que vous aviez faite dans un éditeur de texte local, annuler vos changements dans l'éditeur de wikicode et commencer à éditer le wikicode de la page entière.
*   Il ne fallait PAS ajouter de nouveau contenu après la balise de traduction à la fin du wikicode d'une section.

### Identifier les modifications dans une page marquée pour la traduction (ancien système MediaWiki)
Il était recommandé de marquer une page pour la traduction une fois que le contenu en langue source était stable.
Si une page déjà traduite ne comportait pas de changements, il fallait éviter de modifier les codes tels que `--T:3--`, qui sont des codes générés automatiquement. Vous ne deviez jamais éditer ou copier ces codes.

Une fois la page corrigée, les modifications à traduire devaient être marquées comme suit :

1.  Le nouveau contenu à traduire devait être délimité par les balises `<translate>`.
2.  Les balises `<translate>` étaient aussi utilisées pour délimiter le code qui ne devait pas être traduit.
3.  Les balises `<translate>` servaient également à isoler le code de marquage du wiki (par exemple les tableaux et les balises).
4.  En mode « Affichage », un message au haut de la page vous informait que la page comportait des modifications faites après qu'elle ait été marquée pour la traduction.
5.  Il fallait réviser les unités de traduction. Vous deviez vous assurer que le texte était complet et que le code de programmation et le code wiki (tableaux, balises, etc.) étaient exclus des unités de traduction.
6.  Vous deviez vérifier que la langue prioritaire était sélectionnée; il s'agissait de la langue cible.
7.  Puis, on cliquait sur « Marquer cette page pour la traduction ».

Si la modification que vous faisiez à une unité de traduction dans la page source n'avait pas d'impact sur la version cible, par exemple si vous ne corrigiez qu'une coquille, vous pouviez cocher la case *Ne pas invalider les traductions* et la version cible n'était pas identifiée comme devant être mise à jour.

### Traduction des blocs de code (ancien système MediaWiki)
Le contenu qui se présente sous forme de langage de programmation ne se traduit pas dans une autre langue. Il était recommandé d'isoler les blocs de code avec `</translate>` pour marquer la fin du texte à traduire et le début du code, et ensuite `<translate>` pour marquer la fin du code et la reprise du texte à traduire.

Une excellente pratique en programmation est d'ajouter des commentaires explicatifs à même le code. Toutefois, cette information perd de sa valeur si elle n'est pas traduite. Il n'existe pas de solution unique qui fonctionnerait dans tous les cas, mais nous offrons les suggestions suivantes :

*   placez les commentaires importants à l'extérieur des blocs de code;
*   insérez un commentaire en index (par ex. NOTE 1, NOTE 2) pour relier le texte à la ligne de code correspondante;
*   si vous maîtrisez bien l'autre langue et connaissez les fonctions de traduction du wiki, vous pouvez traduire les commentaires.

Pensez toujours à insérer des commentaires dans le code, mais demandez-vous si cette information est assez importante pour être traduite.

### Traduction de la barre latérale (ancien système MediaWiki)
!!! warning "Note: Méthode de traduction de la barre latérale dans MediaWiki"
    Cette section détaille la procédure pour traduire les éléments de la barre latérale dans l'environnement MediaWiki. Cette information n'est pas applicable au système de documentation actuel basé sur MkDocs Material.

Pour ajouter un élément à traduire dans la barre latérale dans MediaWiki, il fallait suivre les étapes suivantes :

1.  Ajouter le nouveau contenu à [[MediaWiki:Sidebar]]. Tout élément à traduire devait être ajouté soit comme `some-tag`, soit, s'il s'agissait d'un lien, comme `{{int:some-tag}}`.
2.  Ajouter les balises à [[MediaWiki:Sidebar-messages]].
3.  Définir le contenu de la balise en anglais sur [[MediaWiki:some-tag]] (remplacer `some-tag` par la balise réelle).
4.  Traduire le contenu de la balise sur [cette page de traduction spécialisée](https://docs.alliancecan.ca/mediawiki/index.php?title=Special:Translate&language=fr&group=wiki-sidebar&filter=%21translated&action=translate).

## Liste des logiciels disponibles

Les tableaux de la page wiki [Logiciels disponibles](../programming/available_software.md) sont générés à partir de fichiers de modules dans CVMFS. Pour ajouter un lien vers une nouvelle page dans la colonne *Documentation*, faites une nouvelle entrée dans [https://github.com/ComputeCanada/wiki_module_bot/blob/main/module_wiki_page.json](https://github.com/ComputeCanada/wiki_module_bot/blob/main/module_wiki_page.json). Ajoutez ensuite cette modification à la copie définitive du fichier.

Les modifications peuvent prendre jusqu'à six heures avant d'être affichées dans la page wiki.