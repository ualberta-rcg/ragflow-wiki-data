---
title: "Authoring guidelines/fr"
slug: "authoring_guidelines"
lang: "fr"

source_wiki_title: "Authoring guidelines/fr"
source_hash: "d953eb0051150b9ed66d5d9a47987c7e"
last_synced: "2026-08-15T23:22:43.108655+00:00"
last_processed: "2026-08-15T23:32:26.352815+00:00"

tags:
  []

keywords:
  - "guide de style"
  - "voix active"
  - "marquer une page pour la traduction"
  - "mise en page"
  - "logiciels disponibles"
  - "MediaWiki:Sidebar"
  - "unités de traduction"
  - "documentation technique"
  - "page traduite"
  - "contribuer au wiki"
  - "mise à jour"
  - "Marquer cette page pour la traduction"
  - "Office québécois de la langue française"
  - "contenu du wiki"
  - "Ne pas invalider les traductions"
  - "langue prioritaire"
  - "traduction"
  - "balises <translate>"
  - "balises de traduction"
  - "commentaires explicatifs"
  - "ordre d'importance"
  - "CVMFS"
  - "adressez-vous directement au lecteur"
  - "unité de traduction"
  - "version cible"
  - "ne pas éditer les tags de traduction"
  - "équipe de documentation"
  - "blocs de code"
  - "pourcentage de traduction"
  - "idée principale par paragraphe"
  - "extension Traduire"
  - "forme positive"

questions:
  - "Qui peut contribuer au wiki et quelles sont les conditions d’authentification requises ?"
  - "Quel type d’information doit être publié sur ce wiki versus les informations à diriger vers d’autres sites ou services (communication, statut, sécurité, etc.) ?"
  - "Quelles sont les principales consignes du guide de style concernant la rédaction, le formatage et la gestion des ébauches sur le wiki ?"
  - "Quel rôle joue une documentation bien préparée dans la perception du lecteur et de l’auteur ?"
  - "Quels sont les guides de style mentionnés par l’Office québécois de la langue française pour la documentation technique ?"
  - "Quelles pratiques usuelles sont recommandées pour structurer le contenu d’un wiki, selon le texte ?"
  - "Quels sont les principes essentiels (adresse directe, vocabulaire simple, voix active, forme positive, usage du terme juste) à appliquer pour rédiger un texte technique clair ?"
  - "Comment doit‑on formater le contenu (sauts de ligne, retraits, images, captures d’écran) afin d’assurer une mise en page lisible et conforme aux consignes ?"
  - "Quelle est la procédure pour marquer une page, la traduire et la réviser à l’aide de l’extension « Translate » du wiki ?"
  - "Quelles sont les étapes à suivre pour marquer une page prête à être traduite, en incluant l’utilisation des balises <translate> </translate> et <languages /> ?"
  - "Quels comportements sont interdits avec les balises de traduction (ex. <!--T:20-->) et quelle procédure adopter lorsqu’une balise isolée apparaît en éditant une section ?"
  - "Comment identifier les modifications sur une page déjà marquée pour la traduction et décider d’utiliser l’option « Ne pas invalider les traductions » ?"
  - "Comment l'extension Traduire analyse et divise le contenu d’une page marquée pour la traduction ?"
  - "Quels bénéfices apporte la traduction individuelle des unités (titre, paragraphe, image, etc.) sur la gestion des modifications ?"
  - "De quelle manière l’extension indique‑t‑elle le pourcentage de la page déjà traduit ou à mettre à jour ?"
  - "Comment doit‑on isoler les blocs de code afin qu’ils ne soient pas traduits ?"
  - "Quelle est la procédure complète pour ajouter et traduire un nouvel élément dans la barre latérale du wiki ?"
  - "Quelles sont les étapes nécessaires pour ajouter un lien de documentation d’un nouveau logiciel dans la page « Logiciels disponibles » ?"
  - "Quelle est la procédure pour marquer une page afin qu’elle soit prise en compte par le système de traduction ?"
  - "Comment empêcher l’invalidation d’une traduction lorsqu’on corrige uniquement une coquille dans l’unité de traduction source ?"
  - "Pourquoi est‑il important de vérifier que la langue prioritaire sélectionnée correspond bien à la langue cible ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: false
  qa_generated: false
---

## Qui peut contribuer à ce wiki?
Si vous avez un compte avec l'Alliance, vous pouvez contribuer. La principale tâche de notre équipe est de fournir une documentation complète et juste, mais nous sommes à l'ère Wikipédia. Si vous remarquez un problème évident comme un lien brisé ou une coquille, vous pouvez bien entendu le corriger. Si vous le souhaitez, vous pouvez aussi rédiger un article en rapport avec un logiciel que vous connaissez bien. Notre équipe de documentation révise les articles rédigés pour vérifier leur conformité aux présentes directives.

La collaboration au wiki ne se fait pas de façon anonyme. Vous devez vous connecter en utilisant les informations d'identification pour votre compte; ceci nous permet de savoir qui a rédigé ou modifié le contenu.

## Contenu du wiki
Ce wiki n'est pas l'endroit où afficher l'information qui relève de la responsabilité de la direction des communications et du marketing, ce qui inclut toute information pour communication au grand public, aux médias et aux agences de financement. Aussi, l'information touchant les activités de formation et de rayonnement ne convient pas au contenu de la documentation technique. Avant de publier une page ou de modifier le contenu du wiki, posez-vous les questions suivantes :

*   Cette information est-elle au sujet de la disponibilité d'une grappe ou d'un service? Si c'est le cas, cette grappe ou ce service a-t-il fait l'objet d'une annonce? Si c'est le cas, communiquez avec la direction des communications et du marketing avant de publier.
*   S'agit-il d'un état qui change de jour en jour (disponible, hors ligne, en maintenance, etc.)? Cette information doit paraître sur [https://status.alliancecan.ca/](https://status.alliancecan.ca/).
*   L'information s'adresse-t-elle aux utilisateurs et utilisatrices ou à nos équipes techniques? Si elle s'adresse à une équipe technique, elle devrait se trouver sur [https://wiki.computecanada.ca/staff/](https://wiki.computecanada.ca/staff/) plutôt que sur [https://docs.alliancecan.ca/](https://docs.alliancecan.ca/).
*   Cette information a-t-elle une incidence sur la sécurité de nos systèmes ou sur la sécurité des données présentes sur nos systèmes? Si c'est le cas, communiquez avec la direction de la sécurité de l'information avant de publier.
*   L'information s'adresse-t-elle aux utilisateurs potentiels plutôt qu'aux détenteurs de compte? Il y a ici une zone grise : tout comme un utilisateur potentiel, un détenteur de compte pourrait vouloir connaître les détails techniques en rapport avec nos services et nos sites. Cependant, si l'information n'est d'intérêt que pour les utilisateurs potentiels, elle devrait se retrouver sur [https://www.alliancecan.ca](https://www.alliancecan.ca) plutôt que sur [https://docs.alliancecan.ca/](https://docs.alliancecan.ca/).
*   Il est approprié de publier des liens externes; voir par exemple *Obtenir un compte*.
*   L'information explique-t-elle comment utiliser une grappe, une application ou un service existants? Si c'est le cas, allez-y.

!!! note "En cas de doute"
    *   Si vous êtes à l'emploi de l'Alliance, utilisez le canal `#rsnt-documentation` dans Slack.
    *   Si vous n'êtes pas à l'emploi de l'Alliance, communiquez avec le [soutien technique](../support/technical_support.md).

## Style de rédaction
Dans la mesure du possible, évitez de téléverser des fichiers PDF. Copiez plutôt le texte sélectionné à partir d'un PDF et modifiez-le ensuite selon les normes du wiki en incluant par exemple les liens internes menant vers d'autres pages ou sections.

### Ébauches
Si vous développez une nouvelle page et qu'elle n'est pas complète, vous devriez la marquer comme étant une ébauche en insérant :

```
{{Draft}}
```

### Rédaction
Le présent guide aide les rédacteurs à produire une documentation technique qui facilite l'apprentissage. Une documentation bien préparée est agréable au lecteur et projette une image positive de l'auteur.
Il existe plusieurs guides de style pour la documentation technique.

Cependant, aucun guide de style n'existe pour notre wiki, mais il est important de retenir certaines pratiques usuelles :

*   **Après un titre de section, laissez une ligne vide**. Ceci prévient les problèmes possibles dus aux [balises de traduction](authoring_guidelines.md#balises-de-traduction).
*   Énoncez une idée principale par paragraphe.
*   Placez l'information en ordre d'importance.
*   Adressez-vous directement au lecteur.
    *   Par exemple, *Cliquez sur le bouton* plutôt que *L'utilisateur doit cliquer sur le bouton*.
*   Utilisez le plus possible un vocabulaire simple et courant.
*   Construisez les phrases avec des verbes au présent.
*   Utilisez la voix active.
    *   Par exemple, *Le fichier contient les paramètres valides* plutôt que *Les paramètres valides sont contenus dans le fichier*.
*   Utilisez la forme positive.
    *   Par exemple, *Répondre OUI* plutôt que *Ne pas répondre NON*.
*   Employez la terminologie appropriée.
    *   Bien sûr, les synonymes rendent le texte moins ennuyant, mais ils peuvent créer de la confusion chez un nouvel utilisateur ou un utilisateur dont la langue maternelle est différente de celle du texte (par exemple, *machine*, *hôte*, *nœud*, *serveur*).

Le terme *système* est souvent employé de façon générique : il peut désigner entre autres un ordinateur, une grappe ou encore un environnement ou un logiciel. Veillez à utiliser le mot juste pour éviter toute confusion.

#### Autres ressources pour la rédaction en anglais

*   [Technical Writing courses from Google](https://developers.google.com/tech-writing/overview)
*   [Documentation guide from Write the Docs](https://www.writethedocs.org/guide/)

### Mise en page
Si vous doutez, imitez les maîtres. Utilisez le style d'une page existante. Si vous n'en trouvez pas sur [docs.alliancecan.ca/](https://docs.alliancecan.ca/), cherchez sur [Wikipédia](http://www.wikipedia.org).

*   Autant que possible, gardez les éléments visuels à part du contenu texte. N'utilisez pas de sauts de ligne pour ajuster l'espacement vertical. N'utilisez pas la tabulation ou des espaces pour mettre un paragraphe en retrait; n'ajoutez pas d'espace à la fin d'une phrase. Si ce type de formatage est souhaitable, nous préparerons des feuilles de style ou des gabarits, le cas échéant.
*   Laissez une ligne vide à la fin d'une section, avant le titre de la prochaine section. La fonction de traduction utilise la ligne vide et le titre pour délimiter les unités de traduction.
*   Les liens vers d'autres pages ou d'autres sites doivent être bien décrits et non simplement être indiqués par leur adresse URL.
*   Dans les entêtes et titres en anglais, utilisez les majuscules pour le premier terme et les noms propres (voir [Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Naming_conventions_(capitalization))). Nous recommandons l'emploi du [*APA sentence case*](http://blog.apastyle.org/apastyle/2012/03/title-case-and-sentence-case-capitalization-in-apa-style.html) pour les titres de pages et de sections.

### Gabarits
Plusieurs gabarits sont disponibles. Veuillez les utiliser au besoin. Nous attirons votre attention particulièrement sur les gabarits pour [Inclure une commande dans une page wiki](including_a_command_within_the_wiki.md) et [Inclure un fichier de code source dans une page wiki](including_a_source_code_file_within_the_wiki.md).

## Traduction

Une page rédigée dans la langue source doit être marquée pour la traduction. Une personne peut alors traduire le contenu avec l'extension wiki [Translate](https://www.mediawiki.org/wiki/Help:Extension:Translate/Page_translation_example/fr); voir [ce tutoriel](https://www.mediawiki.org/wiki/Help:Extension:Translate/Page_translation_example/fr). Une page traduite peut ensuite être révisée. Une page qui n'est pas encore traduite est affichée dans la langue source. Une page qui n'a pas encore été révisée est affichée telle quelle.

Lorsqu'une page est marquée pour la traduction, l'extension Translate analyse son contenu et le divise en unités de traduction qui sont par exemple un titre, un paragraphe, un élément visuel ou autre. Les unités discrètes sont traduites individuellement : ainsi, une modification à une unité n'a pas d'effet sur le reste de la page. Il est possible de connaître le pourcentage de la page déjà traduit ou devant être mis à jour.

### Marquer une page pour la traduction
Quand vous avez terminé la rédaction d'une page, vous devez signaler qu'elle est prête à être traduite en suivant ces étapes :

1.  S'il y a lieu, modifiez la langue source avec Special:PageLanguage.
2.  Le contenu à traduire doit être compris entre les balises `` `translate` `` et `` `/translate` ``.
3.  Utilisez aussi les balises `` `translate` `` et `` `/translate` `` pour délimiter les parties en code qui ne doivent pas être traduites.
4.  Les balises `` `translate` `` et `` `/translate` `` servent aussi à isoler le code de marquage du wiki (par exemple les tableaux et les balises).
5.  La balise `languages` doit se trouver au tout début de la page. Ceci affiche une boîte au haut de la page contenant la liste des langages disponibles.
6.  Pour les pages source en anglais, par exemple, le mode « Lecture » affiche la fonction « Traduire cette page ».
7.  Révisez les unités de traduction. Assurez-vous que le texte est complet et que le code de programmation et le code wiki (tableaux, balises, etc.) sont exclus des unités de traduction.
8.  Sélectionnez la langue prioritaire pour la traduction; il s'agit de la langue cible.
9.  Cliquez sur « Marquer cette version pour la traduction ».

### Balises de traduction
Les balises de traduction délimitent le contenu en unités de traduction. Elles ressemblent à `` `<!--T:20-->` ``. Elles sont **entièrement** gérées par l'extension de traduction. Lorsque vous modifiez une page :

!!! warning
    *   **NE MODIFIEZ PAS** les balises de traduction.
    *   **NE COPIEZ PAS** les balises de traduction.
    *   **NE DÉPLACEZ PAS** les balises de traduction.
    *   **NE CRÉEZ PAS** de balises de traduction.
    *   **NE DUPLIQUEZ PAS** les balises de traduction.

Vous pouvez sans risque **SUPPRIMER** les balises de traduction et laisser l'extension baliser à nouveau la page quand elle sera marquée pour être traduite.

Si vous commencez à modifier une section et que vous voyez une balise de traduction isolée à la fin du code wiki, arrêtez-vous là! Retournez à la page et cliquez pour modifier la page entière.

*   Une erreur est affichée si vous tentez de soumettre une modification pour une section contenant une balise de traduction à la fin du code wiki (même si ce problème provient du wiki lui-même; il s'agit d'un problème connu).
*   **NE SUPPRIMEZ PAS** cette balise de traduction à la fin de la section, car cela invaliderait une traduction en production. Copiez et collez plutôt la modification effectuée dans un éditeur de texte local, annulez vos modifications dans l'éditeur de code wiki et commencez à modifier la page entière.
*   N'ajoutez **PAS** de nouveau contenu après la balise de traduction à la fin du code wiki d'une section.

### Modifications dans une page marquée pour la traduction
Il est recommandé de marquer une page pour la traduction une fois que le contenu en langue source est stable.
Si une page déjà traduite ne comporte pas de changements, évitez de modifier les codes tels que `` `<!--T:3-->` ``, qui sont des codes générés automatiquement. Vous ne devez jamais modifier ou copier ces codes.

Une fois la page corrigée, marquez les modifications à traduire comme suit :

1.  Le nouveau contenu à traduire doit être compris entre les codes `` `translate` `` et `` `/translate` ``.
2.  Utilisez aussi les balises `` `translate` `` `` `/translate` `` pour délimiter le code qui ne doit pas être traduit.
3.  Les balises `` `translate` `` `` `/translate` `` servent aussi à isoler le code de marquage du wiki (par exemple les tableaux et les balises).
4.  En mode « Lecture », un message au haut de la page vous informe que la page comporte des modifications faites après qu'elle ait été marquée pour la traduction.
5.  Révisez les unités de traduction. Assurez-vous que le texte est complet et que le code de programmation et le code wiki (tableaux, balises, etc.) sont exclus des unités de traduction.
6.  Vérifiez que la langue prioritaire est sélectionnée; il s'agit de la langue cible.
7.  Cliquez sur « Marquer cette page pour la traduction ».

Si la modification que vous faites à une unité de traduction dans la page source n'a pas d'impact sur la version cible, par exemple si vous ne corrigez qu'une coquille, cochez la case *Ne pas invalider les traductions* et la version cible ne sera pas identifiée comme devant être mise à jour.

### Traduction des blocs de code
Le contenu qui se présente sous forme de langage de programmation ne se traduit pas dans une autre langue. Il est recommandé d'isoler les blocs de code avec `` `/translate` `` pour marquer la fin du texte à traduire et le début du code et ensuite `` `translate` `` pour marquer la fin du code et la reprise du texte à traduire.

Une excellente pratique en programmation est d'ajouter des commentaires explicatifs à même le code. Toutefois, cette information perd de sa valeur si elle n'est pas traduite. Il n'existe pas de solution unique qui fonctionnerait dans tous les cas, mais nous offrons les suggestions suivantes :

*   placez les commentaires importants à l'extérieur des blocs de code;
*   insérez un commentaire en index (par ex. NOTE 1, NOTE 2) pour relier le texte à la ligne de code correspondante;
*   si vous maîtrisez bien l'autre langue et connaissez les fonctions de traduction du wiki, vous pouvez traduire les commentaires.

Pensez toujours à insérer des commentaires dans le code, mais demandez-vous si cette information est assez importante pour être traduite.

### Traduction de la barre latérale
Pour ajouter un élément à traduire dans la barre latérale, les étapes sont :

1.  Ajoutez le nouveau contenu à MediaWiki:Sidebar. Tout élément à traduire doit être ajouté sous la forme `` `some-tag` `` ou, s'il s'agit d'un lien, `` `{{(}}{{(}}int:some-tag{{)}}{{)}}` ``.
2.  Ajoutez les balises à MediaWiki:Sidebar-messages.
3.  Définissez le contenu de la balise en anglais sur MediaWiki:some-tag (remplacez `` `some-tag` `` par la balise correspondante).
4.  Traduisez le contenu de la balise [dans cette page](https://docs.alliancecan.ca/mediawiki/index.php?title=Special:Translate&language=fr&group=wiki-sidebar&filter=%21translated&action=translate).

## Liste des logiciels disponibles

Les tableaux de la page wiki [Logiciels disponibles](../programming/available_software.md) sont générés à partir de fichiers de modules dans CVMFS. Pour ajouter un lien vers une nouvelle page dans la colonne *Documentation*, faites une nouvelle entrée dans [https://github.com/ComputeCanada/wiki_module_bot/blob/main/module_wiki_page.json](https://github.com/ComputeCanada/wiki_module_bot/blob/main/module_wiki_page.json). Ajoutez ensuite cette modification à la copie définitive du fichier.

Les modifications peuvent prendre jusqu'à six heures avant d'être affichées dans la page wiki.