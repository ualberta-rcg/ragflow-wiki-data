---
title: "Authoring guidelines/fr"
slug: "authoring_guidelines"
lang: "fr"

source_wiki_title: "Authoring guidelines/fr"
source_hash: "64e6f1ba9d477159413b459e83358b9e"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T04:42:20.795378+00:00"

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

## Qui peut contribuer à ce wiki?
Si vous avez un compte avec l'Alliance, vous pouvez contribuer. La principale tâche de notre équipe est de fournir une documentation complète et juste, mais nous sommes à l'ère Wikipédia. Si vous remarquez un problème évident comme un lien brisé ou une coquille, vous pouvez bien entendu le corriger. Si vous le souhaitez, vous pouvez aussi rédiger un article en rapport avec un logiciel que vous connaissez bien. Notre équipe de documentation révise les articles rédigés pour vérifier leur conformité aux présentes directives.

La collaboration au wiki ne se fait pas de façon anonyme. Vous devez vous connecter en utilisant les informations d'identification pour votre compte; ceci nous permet de savoir qui a rédigé ou modifié le contenu.

## Contenu du wiki
Ce wiki n'est pas l'endroit où afficher l'information qui relève de la responsabilité de la direction des communications et du marketing, ce qui inclut toute information pour communication au grand public, aux médias et aux agences de financement. Aussi, l'information touchant les activités de formation et de rayonnement ne convient pas au contenu de la documentation technique. Avant de publier une page ou de modifier le contenu du wiki, posez-vous les questions suivantes :
* Cette information est-elle au sujet de la disponibilité d'une grappe ou d'un service? Si c'est le cas, cette grappe ou ce service a-t-il fait l'objet d'une annonce? Autrement, communiquez avec la direction des communications et du marketing avant de publier.
* S'agit-il d'un état qui change de jour en jour (disponible, hors ligne, en maintenance, etc.)? Cette information doit paraître sur [status.alliancecan.ca](https://status.alliancecan.ca/).
* L'information s'adresse-t-elle aux utilisateurs et utilisatrices ou à nos équipes techniques? Si elle s'adresse à une équipe technique, elle devrait se trouver sur [wiki.computecanada.ca/staff/](https://wiki.computecanada.ca/staff/) plutôt que sur [docs.alliancecan.ca/](https://docs.alliancecan.ca/).
* Cette information a-t-elle une incidence sur la sécurité de nos systèmes ou sur la sécurité des données présentes sur nos systèmes? Si c'est le cas, communiquez avec la direction de la sécurité de l'information avant de publier.
* L'information s'adresse-t-elle aux utilisateurs potentiels plutôt qu'aux détenteurs de compte? Il y a ici une zone grise : tout comme un utilisateur potentiel, un détenteur de compte pourrait vouloir connaître les détails techniques en rapport avec nos services et nos sites. Cependant, si l'information n'est d'intérêt que pour les utilisateurs potentiels, elle devrait se retrouver sur [www.alliancecan.ca](https://www.alliancecan.ca) plutôt que sur [docs.alliancecan.ca/](https://docs.alliancecan.ca/).
* Il est approprié de publier des liens externes; voir par exemple *Obtenir un compte*.
* L'information explique-t-elle comment utiliser une grappe, une application ou un service existants? Si c'est le cas, allez-y.

Si vous avez encore des doutes :
* si vous êtes à l'emploi de l'Alliance, utilisez le canal #rsnt-documentation dans Slack;
* si vous n'êtes pas à l'emploi de l'Alliance, communiquez avec le [soutien technique](technical-support.md).

## Guide de style
Dans la mesure du possible, évitez de téléverser des fichiers PDF. Copiez plutôt le texte sélectionné à partir d'un PDF et modifiez-le ensuite selon les normes du wiki en incluant par exemple les liens internes menant vers d'autres pages ou sections.

### Ébauches
!!! note "Page d'ébauche"
    Si vous développez une nouvelle page et qu'elle n'est pas complète, vous devriez marquer la page comme une ébauche.

### Rédaction
Le guide de style aide les rédacteurs à produire une documentation technique qui facilite l'apprentissage. Une documentation bien préparée est agréable au lecteur et projette une image positive de l'auteur.
Il existe plusieurs guides de style pour la documentation technique. L'Office québécois de la langue française en liste quelques-uns.
Aucun guide de style n'existe pour notre wiki, mais il est important de retenir certaines pratiques usuelles :
* Énoncez une idée principale par paragraphe.
* Placez l'information en ordre d'importance.
* Adressez-vous directement au lecteur.
  * Par exemple, *Cliquez sur le bouton* plutôt que *L'utilisateur doit cliquer sur le bouton*.
* Utilisez le plus possible un vocabulaire courant et simple.
* Construisez vos phrases avec des verbes au présent.
* Utilisez la voix active.
  * Par exemple, *Le fichier contient les paramètres valides* plutôt que *Les paramètres valides sont contenus dans le fichier*.
* Utilisez la forme positive.
  * Par exemple, *Répondre OUI* plutôt que *Ne pas répondre NON*.
* Employez le mot juste.
  * Bien sûr, les synonymes rendent le texte moins ennuyant, mais ils peuvent créer de la confusion chez un nouvel utilisateur ou un utilisateur dont la langue maternelle est différente de celle du texte (par exemple, *machine*, *hôte*, *nœud*, *serveur*).

Le terme *système* est souvent employé de façon générique : il peut désigner entre autres un ordinateur, une grappe ou encore un environnement ou un logiciel. Veillez à utiliser le mot juste pour éviter toute confusion.

#### Autre ressource
* [Cours de rédaction technique de Google](https://developers.google.com/tech-writing/overview)
* [Guide de documentation de Write the Docs](https://www.writethedocs.org/guide/)

### Mise en page
Si vous doutez, imitez les maîtres. Utilisez le style d'une page existante. Si vous n'en trouvez pas sur [docs.alliancecan.ca/](https://docs.alliancecan.ca/), cherchez sur [Wikipédia](http://www.wikipedia.org).
* Autant que possible, gardez les images à part du contenu texte. N'utilisez pas des sauts de ligne pour ajuster l'espacement vertical. N'utilisez pas la tabulation ou des espaces pour mettre un paragraphe en retrait; n'ajoutez pas d'espace à la fin d'une phrase. Si ce type de formatage est souhaitable, nous préparerons des feuilles de style ou des gabarits, le cas échéant.
* Les captures d'écran sont utiles, surtout dans le cas de guides d'utilisation ou de tutoriels. Cependant, les captures plein écran incluses dans le texte nuisent à la lisibilité. Placez les images flottantes à la droite du texte. Réduisez aussi la taille de l'image. Si la visibilité n'est pas acceptable, peut-être devriez-vous rogner l'image? Vous pouvez aussi ajouter la mention *Cliquez pour agrandir*.
* Employez le moins de synonymes possible. Bien sûr, les synonymes rendent le texte moins ennuyant, mais ils peuvent créer de la confusion chez un nouvel utilisateur ou un utilisateur dont la langue maternelle est différente de celle du texte (par exemple, *machine*, *hôte*, *nœud*, *serveur*).
* Laissez une ligne vide à la fin d'une section, avant le titre de la prochaine section. La fonction de traduction utilise la ligne vide et le titre pour délimiter les unités de traduction.

### Gabarits
Plusieurs [gabarits](special-uncategorizedtemplates.md) sont disponibles. Veuillez les utiliser au besoin. Nous attirons votre attention particulièrement sur les gabarits pour [Inclure une commande dans une page wiki](including-a-command-within-the-wiki.md) et [Inclure un fichier de code source dans une page wiki](including-a-source-code-file-within-the-wiki.md).

## Traduction
La page dans la langue source doit être marquée pour la traduction. Toute personne peut traduire une page marquée pour traduction avec les outils de l'extension wiki [Traduire](https://www.mediawiki.org/wiki/Help:Extension:Translate/Page_translation_example/fr). Vous trouverez un tutoriel [ici](https://www.mediawiki.org/wiki/Help:Extension:Translate/Page_translation_example/fr). Une page traduite peut ensuite être révisée.

Lorsqu'une page est marquée pour la traduction, l'extension Traduire analyse son contenu et le divise en unités de traduction qui sont par exemple un titre, un paragraphe, une image ou autre. Les unités discrètes sont traduites individuellement : ainsi, une modification à une unité n'a pas d'effet sur le reste de la page et il est possible de connaître le pourcentage de la page déjà traduit ou devant être mis à jour.

### Marquer une page pour la traduction
Quand vous avez terminé la rédaction d'une page, vous devez signaler qu'elle est prête à être traduite en suivant ces étapes :
1. Le contenu à traduire doit être compris entre les balises `<translate>` et `</translate>`.
2. Utilisez aussi les balises `<translate>` et `</translate>` pour délimiter le code qui ne doit pas être traduit.
3. Les balises `<translate>` et `</translate>` servent aussi à isoler le code de marquage du wiki (par exemple les tableaux et les balises).
4. La balise `<languages />` doit paraître au tout début de la page. Ceci affichera une boîte au haut de la page contenant la liste des langages disponibles pour la page.
5. En mode 'View', cliquez sur 'Marquer cette page pour la traduction'.
6. Révisez les unités de traduction. Assurez-vous que le texte est complet et que le code de programmation et le code wiki (tableaux, balises, etc.) sont exclus des unités de traduction.
7. Sélectionnez la langue prioritaire pour la traduction; il s'agit de la langue cible.
8. Cliquez sur 'Marquer cette page pour la traduction'.

### Identifier les modifications dans une page marquée pour la traduction
Il est recommandé de marquer une page pour la traduction une fois que le contenu en langue source est stable.
Si une page déjà traduite ne comporte pas de changements, évitez de modifier les codes tels que `<!--T:3-->`, qui sont des codes générés automatiquement. Vous ne devez jamais éditer ou copier ces codes.

Une fois la page corrigée, marquez les modifications à traduire comme suit :
1. Le nouveau contenu à traduire doit être compris entre les codes `<translate>` et `</translate>`.
2. Utilisez aussi les balises `<translate>` et `</translate>` pour délimiter le code qui ne doit pas être traduit.
3. Les balises `<translate>` et `</translate>` servent aussi à isoler le code de marquage du wiki (par exemple les tableaux et les balises).
4. En mode 'View', un message au haut de la page vous informe que la page comporte des modifications faites après qu'elle ait été marquée pour la traduction.
5. Révisez les unités de traduction. Assurez-vous que le texte est complet et que le code de programmation et le code wiki (tableaux, balises, etc.) sont exclus des unités de traduction.
6. Vérifiez que la langue prioritaire est sélectionnée; il s'agit de la langue cible.
7. Cliquez sur 'Marquer cette page pour la traduction'.

Si la modification que vous faites à une unité de traduction dans la page source n'a pas d'impact sur la version cible, par exemple si vous ne corrigez qu'une coquille, cochez la case *Ne pas invalider les traductions* et la version cible ne sera pas identifiée comme devant être mise à jour.

### Traduction des blocs de code
Le contenu qui se présente sous forme de langage de programmation ne se traduit pas dans une autre langue. Il est recommandé d'isoler les blocs de code avec `</translate>` pour marquer la fin du texte à traduire et le début du code et ensuite `<translate>` pour marquer la fin du code et la reprise du texte à traduire.

Une excellente pratique en programmation est d'ajouter des commentaires explicatifs à même le code. Toutefois, cette information perd de sa valeur si elle n'est pas traduite. Il n'existe pas de solution unique qui fonctionnerait dans tous les cas, mais nous offrons les suggestions suivantes :
* placez les commentaires importants à l'extérieur des blocs de code;
* insérez un commentaire en index (par ex. NOTE 1, NOTE 2) pour relier le texte à la ligne de code correspondante;
* si vous maîtrisez bien l'autre langue et connaissez les fonctions de traduction du wiki, vous pouvez traduire les commentaires.

Pensez toujours à insérer des commentaires dans le code, mais demandez-vous si cette information est assez importante pour être traduite.

### Traduction de la barre latérale
Pour ajouter un élément à traduire dans la barre latérale, suivez les étapes suivantes :
1. ajoutez le nouveau contenu à [[MediaWiki:Sidebar]]. Tout élément qui devrait être traduit doit être ajouté soit comme `` `some-tag` `` ou, s'il s'agit d'un lien, `` `{{(}}{{(}}int:some-tag{{)}}{{)}}` ``
2. ajoutez les balises à [[MediaWiki:Sidebar-messages]]
3. définissez le contenu de la balise en anglais sur [[MediaWiki:some-tag]] (remplacez `` `some-tag` `` par la balise réelle)
4. traduisez le contenu de la balise sur [cette page](https://docs.alliancecan.ca/mediawiki/index.php?title=Special:Translate&language=fr&group=wiki-sidebar&filter=%21translated&action=translate)

## Liste des logiciels disponibles
Les tableaux de la page wiki [Logiciels disponibles](available-software.md) sont générés à partir de fichiers de modules dans CVMFS. Pour ajouter un lien vers une nouvelle page dans la colonne 'Documentation', faites une nouvelle entrée dans [https://github.com/ComputeCanada/wiki_module_bot/blob/main/module_wiki_page.json](https://github.com/ComputeCanada/wiki_module_bot/blob/main/module_wiki_page.json). Ajoutez ensuite cette modification à la copie définitive du fichier.

Les modifications peuvent prendre jusqu'à six heures avant d'être affichées dans la page wiki.