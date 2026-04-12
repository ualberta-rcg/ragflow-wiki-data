---
title: "Authoring guidelines/fr"
slug: "authoring_guidelines"
lang: "fr"

source_wiki_title: "Authoring guidelines/fr"
source_hash: "64e6f1ba9d477159413b459e83358b9e"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:33:41.805596+00:00"

tags:
  []

keywords:
  - "unités de traduction"
  - "Logiciels disponibles"
  - "mise en page"
  - "rédaction technique"
  - "balises <translate>"
  - "translating the sidebar"
  - "traduction"
  - "blocs de code"
  - "MediaWiki:Sidebar"
  - "Special:Translate"
  - "ligne de code"
  - "lecteur"
  - "wiki"
  - "CVMFS"
  - "vocabulaire simple"
  - "module_wiki_page.json"
  - "pratiques usuelles"
  - "guide de style"
  - "pourcentage de la page"
  - "marquer une page"
  - "marquer pour la traduction"
  - "contenu du wiki"
  - "commentaires"
  - "contribution au wiki"
  - "documentation technique"
  - "rédaction"
  - "gabarits"
  - "guides de style"
  - "extension Traduire"

questions:
  - "Quelles sont les conditions requises pour pouvoir contribuer au wiki de l'Alliance ?"
  - "Quels types d'informations sont autorisés ou interdits lors de la publication de contenu sur ce wiki ?"
  - "Quelles sont les bonnes pratiques et les règles de style à respecter lors de la rédaction d'une page ?"
  - "Quels sont les avantages d'une documentation bien préparée pour le lecteur et l'auteur ?"
  - "Quelle organisation répertorie des guides de style pour la documentation technique ?"
  - "Quelles sont les pratiques de rédaction usuelles à appliquer sur le wiki en l'absence de guide de style ?"
  - "Quelles sont les principales recommandations concernant le style de rédaction et le choix du vocabulaire pour assurer la clarté du texte ?"
  - "Quelles sont les bonnes pratiques de mise en page à respecter, notamment en ce qui concerne l'intégration des images et l'espacement ?"
  - "Comment fonctionne le processus de traduction des pages avec l'extension wiki et comment le contenu est-il divisé ?"
  - "Quelles sont les étapes et les balises requises pour préparer et signaler qu'une nouvelle page wiki est prête à être traduite ?"
  - "Comment doit-on gérer les modifications apportées à une page déjà marquée pour la traduction, notamment lors de corrections mineures ?"
  - "Quelles sont les recommandations pour traiter les blocs de code de programmation et leurs commentaires lors du processus de traduction ?"
  - "Que fait l'extension Traduire lorsqu'une page est marquée pour la traduction ?"
  - "Quels types d'éléments peuvent constituer une unité de traduction ?"
  - "Quels sont les avantages de traduire les unités de manière individuelle pour la gestion de la page ?"
  - "Quelles sont les étapes requises pour ajouter et traduire un nouvel élément dans la barre de navigation (Sidebar) de MediaWiki ?"
  - "À partir de quelle source les tableaux de la page des logiciels disponibles sont-ils générés ?"
  - "Comment ajouter un lien dans la colonne Documentation de la liste des logiciels et quel est le délai d'affichage de cette modification ?"
  - "Comment doit-on procéder pour relier un texte explicatif à sa ligne de code correspondante ?"
  - "Quels sont les critères à prendre en compte avant de décider de traduire un commentaire inséré dans le code ?"
  - "Quelles sont les étapes à suivre pour ajouter un élément à traduire dans la barre latérale ?"
  - "Quelles sont les étapes requises pour ajouter et traduire un nouvel élément dans la barre de navigation (Sidebar) de MediaWiki ?"
  - "À partir de quelle source les tableaux de la page des logiciels disponibles sont-ils générés ?"
  - "Comment ajouter un lien dans la colonne Documentation de la liste des logiciels et quel est le délai d'affichage de cette modification ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Qui peut contribuer à ce wiki?
Si vous avez un compte avec l'Alliance, vous pouvez contribuer. La principale tâche de notre équipe est de fournir une documentation complète et juste, mais nous sommes à l'ère Wikipédia. Si vous remarquez un problème évident comme un lien brisé ou une coquille, vous pouvez bien entendu le corriger. Si vous le souhaitez, vous pouvez aussi rédiger un article en rapport avec un logiciel que vous connaissez bien. Notre équipe de documentation révise les articles rédigés pour vérifier leur conformité aux présentes directives.

La collaboration au wiki ne se fait pas de façon anonyme. Vous devez vous connecter en utilisant les informations d'identification pour votre compte; ceci nous permet de savoir qui a rédigé ou modifié le contenu.

## Contenu du wiki
Ce wiki n'est pas l'endroit où afficher l'information qui relève de la responsabilité de la direction des communications et du marketing, ce qui inclut toute information pour communication au grand public, aux médias et aux agences de financement. Aussi, l'information touchant les activités de formation et de rayonnement ne convient pas au contenu de la documentation technique. Avant de publier une page ou de modifier le contenu du wiki, posez-vous les questions suivantes :
* Cette information est-elle au sujet de la disponibilité d'une grappe ou d'un service? Si c'est le cas, cette grappe ou ce service a-t-il fait l'objet d'une annonce? Autrement, communiquez avec la direction des communications et du marketing avant de publier.
* S'agit-il d'un état qui change de jour en jour (disponible, hors ligne, en maintenance, etc.)? Cette information doit paraître sur [https://status.alliancecan.ca/](https://status.alliancecan.ca/).
* L'information s'adresse-t-elle aux utilisateurs et utilisatrices ou à nos équipes techniques? Si elle s'adresse à une équipe technique, elle devrait se trouver sur [https://wiki.computecanada.ca/staff/](https://wiki.computecanada.ca/staff/) plutôt que sur [https://docs.alliancecan.ca/](https://docs.alliancecan.ca/).
* Cette information a-t-elle une incidence sur la sécurité de nos systèmes ou sur la sécurité des données présentes sur nos systèmes? Si c'est le cas, communiquez avec la direction de la sécurité de l'information avant de publier.
* L'information s'adresse-t-elle aux utilisateurs potentiels plutôt qu'aux détenteurs de compte? Il y a ici une zone grise : tout comme un utilisateur potentiel, un détenteur de compte pourrait vouloir connaître les détails techniques en rapport avec nos services et nos sites. Cependant, si l'information n'est d'intérêt que pour les utilisateurs potentiels, elle devrait se retrouver sur [https://www.alliancecan.ca](https://www.alliancecan.ca) plutôt que sur [https://docs.alliancecan.ca/](https://docs.alliancecan.ca/).
* Il est approprié de publier des liens externes; voir par exemple *Obtenir un compte*.
* L'information explique-t-elle comment utiliser une grappe, une application ou un service existants? Si c'est le cas, allez-y.

Si vous avez encore des doutes :
* si vous êtes à l'emploi de l'Alliance, utilisez le canal #rsnt-documentation dans Slack;
* si vous n'êtes pas à l'emploi de l'Alliance, communiquez avec le [soutien technique](technical-support.md).

## Guide de style
Dans la mesure du possible, évitez de téléverser des fichiers PDF. Copiez plutôt le texte sélectionné à partir d'un PDF et modifiez-le ensuite selon les normes du wiki en incluant par exemple les liens internes menant vers d'autres pages ou sections.

### Ébauches
!!! tip "Marquer une ébauche"
    Si vous développez une nouvelle page et qu'elle n'est pas complète, il est recommandé de la marquer comme une ébauche ou de ne pas la publier avant qu'elle ne soit terminée.

### Rédaction
Le guide de style aide les rédacteurs à produire une documentation technique qui facilite l'apprentissage. Une documentation bien préparée est agréable au lecteur et projette une image positive de l'auteur.
Il existe plusieurs guides de style pour la documentation technique. L'Office québécois de la langue française en liste quelques-uns.
Aucun guide de style n'existe pour notre wiki, mais il est important de retenir certaines pratiques usuelles :
* Énoncez une idée principale par paragraphe.
* Placez l'information en ordre d'importance.
* Adressez-vous directement au lecteur.
    * Par exemple, **Cliquez sur le bouton** plutôt que *L'utilisateur doit cliquer sur le bouton*.
* Utilisez le plus possible un vocabulaire courant et simple.
* Construisez vos phrases avec des verbes au présent.
* Utilisez la voix active.
    * Par exemple, **Le fichier contient les paramètres valides** plutôt que *Les paramètres valides sont contenus dans le fichier*.
* Utilisez la forme positive.
    * Par exemple, **Répondre OUI** plutôt que *Ne pas répondre NON*.
* Employez le mot juste.
    * Bien sûr, les synonymes rendent le texte moins ennuyant, mais ils peuvent créer de la confusion chez un nouvel utilisateur ou un utilisateur dont la langue maternelle est différente de celle du texte (par exemple, **machine**, **hôte**, **nœud**, **serveur**).

Le terme *système* est souvent employé de façon générique : il peut désigner entre autres un ordinateur, une grappe ou encore un environnement ou un logiciel. Veillez à utiliser le mot juste pour éviter toute confusion.

#### Autre ressource
* [Cours de rédaction technique de Google](https://developers.google.com/tech-writing/overview)
* [Guide de documentation de Write the Docs](https://www.writethedocs.org/guide/)

### Mise en page
Si vous doutez, imitez les maîtres. Utilisez le style d'une page existante. Si vous n'en trouvez pas sur [docs.alliancecan.ca/](https://docs.alliancecan.ca/), cherchez sur [Wikipédia](https://www.wikipedia.org).
* Autant que possible, gardez les images à part du contenu texte. N'utilisez pas des sauts de ligne pour ajuster l'espacement vertical. N'utilisez pas la tabulation ou des espaces pour mettre un paragraphe en retrait; n'ajoutez pas d'espace à la fin d'une phrase. Si ce type de formatage est souhaitable, nous préparerons des feuilles de style ou des gabarits, le cas échéant.
* Les captures d'écran sont utiles, surtout dans le cas de guides d'utilisation ou de tutoriels. Cependant, les captures plein écran incluses dans le texte nuisent à la lisibilité. Placez les images flottantes à la droite du texte. Réduisez aussi la taille de l'image. Si la visibilité n'est pas acceptable, peut-être devriez-vous rogner l'image? Vous pouvez aussi ajouter la mention *Cliquez pour agrandir*.
* Employez le moins de synonymes possible. Bien sûr, les synonymes rendent le texte moins ennuyant, mais ils peuvent créer de la confusion chez un nouvel utilisateur ou un utilisateur dont la langue maternelle est différente de celle du texte (par exemple, **machine**, **hôte**, **nœud**, **serveur**).
* Laissez une ligne vide à la fin d'une section, avant le titre de la prochaine section.

### Gabarits
Plusieurs gabarits sont disponibles. Veuillez les utiliser au besoin. Nous attirons votre attention particulièrement sur les gabarits pour [Inclure une commande dans une page wiki](including-a-command-within-the-wiki.md) et [Inclure un fichier de code source dans une page wiki](including-a-source-code-file-within-the-wiki.md).

## Traduction
!!! info "À propos de la traduction"
    Sur le site original de l'Alliance, la traduction est gérée par une extension spécifique de MediaWiki qui divise le contenu en unités de traduction. Cela permet des mises à jour incrémentales et de suivre le progrès de la traduction. Pour ce site, la gestion des traductions suit des pratiques différentes, souvent en utilisant des fichiers séparés par langue ou des outils de localisation intégrés à MkDocs Material (par exemple, [mkdocs-static-i18n](https://github.com/ultrabug/mkdocs-static-i18n)).

    Une documentation bien segmentée et organisée facilite toujours le processus de traduction, quelle que soit la plateforme.

### Traduction des blocs de code
Le contenu qui se présente sous forme de langage de programmation ne se traduit pas dans une autre langue. Il est recommandé d'isoler les blocs de code pour s'assurer qu'ils ne soient pas modifiés lors des processus de traduction.

Une excellente pratique en programmation est d'ajouter des commentaires explicatifs à même le code. Toutefois, cette information perd de sa valeur si elle n'est pas traduite. Il n'existe pas de solution unique qui fonctionnerait dans tous les cas, mais nous offrons les suggestions suivantes :
* placez les commentaires importants à l'extérieur des blocs de code;
* insérez un commentaire en index (par ex. NOTE 1, NOTE 2) pour relier le texte à la ligne de code correspondante;
* si vous maîtrisez bien l'autre langue et les outils de traduction, vous pouvez traduire les commentaires.

Pensez toujours à insérer des commentaires dans le code, mais demandez-vous si cette information est assez importante pour être traduite.

## Liste des logiciels disponibles
Les tableaux de la page wiki [Logiciels disponibles](available-software.md) sont générés à partir de fichiers de modules dans CVMFS. Pour ajouter un lien vers une nouvelle page dans la colonne *Documentation*, faites une nouvelle entrée dans [https://github.com/ComputeCanada/wiki_module_bot/blob/main/module_wiki_page.json](https://github.com/ComputeCanada/wiki_module_bot/blob/main/module_wiki_page.json). Ajoutez ensuite cette modification à la copie définitive du fichier.

Les modifications peuvent prendre jusqu'à six heures avant d'être affichées dans la page wiki.