---
title: "Version control/fr"
slug: "version_control"
lang: "fr"

source_wiki_title: "Version control/fr"
source_hash: "468967ec30e026781e24870e8a437b31"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T12:42:16.881459+00:00"

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

## Introduction

La gestion de code source est l'une des pierres angulaires du développement d'applications. Lorsque vient le temps de gérer le code source d'un projet sur lequel vous travaillez, deux approches s'offrent à vous. Vous pouvez faire des copies de sauvegarde multiples, envoyer le code source à vos collègues par courriel, et vous creuser la tête afin de savoir qui possède ou utilise quelle version du code et comment réconcilier les changements apportés par chaque collaborateur. Vous pouvez au contraire adopter une approche beaucoup plus saine en utilisant des outils de gestion de versions développés dans le but de faciliter ce processus.

Toutes les applications et bibliothèques d'envergure sont développées en utilisant de tels outils. En recherche, ces outils sont encore plus importants, car la traçabilité est essentielle afin de pouvoir reproduire des résultats donnés. Les outils de gestion de versions sont en quelque sorte le cahier de laboratoire du programmeur.

## Avantages

!!! note "Avantages"
    Les outils de gestion de versions vous offrent un grand nombre d'avantages qui dépassent largement leurs désavantages. Tout d'abord, ils vous permettent de collaborer plus facilement; ils éliminent le risque qu'un collaborateur écrase vos changements ou vice-versa, sans laisser de traces. Ces outils enregistrent en effet l'historique de tous les changements apportés au projet. Ils agissent aussi un peu comme une machine à remonter le temps, en vous permettant de réinitialiser votre projet à une version précédente, afin de reproduire vos résultats par exemple. Ils permettent aussi de documenter facilement ces changements, facilitant ainsi l'avis de ces changements à tous les utilisateurs du projet.

## Principe de base

Les outils de gestion de code source fonctionnent sur un principe de séparation entre les changements locaux faits par un utilisateur, dans son répertoire local, et ce que l'on nomme un dépôt. Un dépôt contient, de façon structurée, l'historique de tous les changements apportés par tous les contributeurs d'un projet. Le développement d'un projet en utilisant un gestionnaire de code source se voit ainsi modifié par rapport au développement local. Plutôt que de simplement enregistrer ses changements sur le disque dur local, un contributeur doit soumettre (*commit*) les changements vers le dépôt afin de les rendre accessibles aux autres développeurs. À l'inverse, les développeurs doivent s'assurer de disposer de la version la plus récente d'un fichier en allant le chercher dans le dépôt (*checkout*, *update*) avant d'y apporter leurs propres changements. Si deux développeurs modifient un fichier source en même temps, l'outil de gestion pourra soit afficher un conflit lors de la soumission des deux changements concurrents, ou encore résoudre ce conflit automatiquement si possible.

## Types d'outils de gestion de versions

Les principaux outils de gestion de versions peuvent se répartir en deux familles ou *générations*. Les outils de première génération, dont font partie [CVS](https://fr.wikipedia.org/wiki/Concurrent_versions_system) et [SVN](https://fr.wikipedia.org/wiki/Apache_Subversion), utilisent un dépôt central unique. Tous les changements sont ainsi soumis et récupérés à partir du dépôt.
Les outils de deuxième génération, dont font partie [Git](https://fr.wikipedia.org/wiki/Git), [Mercurial](https://fr.wikipedia.org/wiki/Mercurial) et [Bazaar](https://fr.wikipedia.org/wiki/Bazaar_(logiciel)), utilisent des dépôts locaux. L'avantage de ces derniers est que le développement peut se faire de façon indépendante de tout serveur à distance. Les *commit* et *checkout* peuvent ainsi être beaucoup plus rapides et exécuter des opérations plus complexes. Aussi, Git et Mercurial offrent une gestion avancée du développement par embranchements. Dans un modèle de développement par embranchements, chaque nouvelle fonctionnalité devrait correspondre à une branche de l'arbre de développement. La version de production du projet correspond à la branche principale et les fonctionnalités sont développées en parallèle jusqu'à ce qu'elles soient suffisamment matures pour être fusionnées à la branche principale, ou sont abandonnées et que leur branche *meurt*. Ce modèle de développement est particulièrement adapté aux grands projets comptant plusieurs développeurs.

En contrepartie, les changements qui doivent être poussés vers un dépôt externe doivent l'être en deux étapes : ils sont d'abord soumis dans le dépôt local (*commit*), puis ils sont *poussés* (*push*) vers le dépôt externe ou un autre dépôt. À l'inverse, pour récupérer des changements d'un dépôt externe, il faut d'abord aller les chercher (*pull* ou *get*) pour les importer dans son dépôt local, puis mettre à jour sa version de travail (*update* ou *checkout*).

## Choisir un outil

Si vous désirez contribuer à un projet existant, vous n'aurez pas d'autre choix que d'utiliser l'outil qui a été choisi initialement par les développeurs. Si vous démarrez votre propre projet, le choix dépendra de l'envergure de votre projet. S'il s'agit d'un projet avec seulement quelques collaborateurs, qui restera privé et pour lequel vous voulez simplement conserver un historique des changements, un outil de première génération comme [SVN](https://fr.wikipedia.org/wiki/Apache_Subversion) pourrait suffire. S'il s'agit d'un projet de plus grande envergure avec des collaborateurs externes, vous devrez probablement envisager les outils de deuxième génération comme [Git](https://fr.wikipedia.org/wiki/Git) ou [Mercurial](https://fr.wikipedia.org/wiki/Mercurial).

### Où situer le dépôt?

!!! tip "Où situer le dépôt?"
    Si vous et vos collaborateurs travaillez toujours sur le même ordinateur, le dépôt peut n'être visible que sur cet ordinateur. Par contre, si vous ou vos collaborateurs utilisez plusieurs ordinateurs, un accès par Internet serait souhaitable; le code peut ainsi être facilement synchronisé et le fait que le code soit distribué ajoute à sa sécurité.

Pour des détails sur la configuration d'un dépôt, vous pouvez consulter [svn](https://civicactions.com/blog/how-to-set-up-an-svn-repository-in-7-simple-steps/), [git](https://git-scm.com/book/en/v2/Git-on-the-Server-The-Protocols), [gitlab](https://about.gitlab.com/?utm_source=google&utm_medium=cpc&utm_campaign=Search%20-%20Brand&utm_content=GitLab%20-%20Open%20Source%20Git&utm_term=gitlab&gclid=CPWslub9vtACFZSEaQodwzoAew), [gitbucket](https://github.com/gitbucket/gitbucket). Pour connaître certains services disponibles en ligne qui ne nécessitent pas que votre serveur soit toujours accessible, consultez : [bitbucket](https://bitbucket.org/product), [github](https://github.com/), [gitlab](https://about.gitlab.com/), [sourceforge](https://sourceforge.net/)

## Référence

[Cette courte vidéo](https://www.youtube.com/watch?v=EmMNIMDl9hM) traite des notions de base avec Git.