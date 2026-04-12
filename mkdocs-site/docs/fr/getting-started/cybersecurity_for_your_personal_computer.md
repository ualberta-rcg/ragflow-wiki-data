---
title: "Cybersecurity for your personal computer/fr"
slug: "cybersecurity_for_your_personal_computer"
lang: "fr"

source_wiki_title: "Cybersecurity for your personal computer/fr"
source_hash: "11c265e9b4a5ab61c6c6ea16269a180d"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:40:13.476392+00:00"

tags:
  []

keywords:
  - "permissions Linux"
  - "antivirus"
  - "chmod 777"
  - "mots de passe uniques"
  - "hameçonnage"
  - "gestionnaire de mots de passe"
  - "mises à jour"
  - "compromis"
  - "sticky bit"
  - "mots de passe"
  - "fichiers partagés"
  - "listes de contrôle d'accès"
  - "superordinateurs"
  - "renseignements exposés"
  - "sécurité informatique"
  - "Permissions Linux"
  - "password stuffing"
  - "authentification multifacteur"
  - "naviguer de façon sécuritaire"
  - "renseignements personnels"
  - "attaques d'hameçonnage"

questions:
  - "Quelles sont les principales mesures à adopter pour sécuriser son ordinateur personnel et ses connexions réseau ?"
  - "Pourquoi est-il recommandé d'utiliser des mots de passe longs et uniques plutôt que de les changer fréquemment ?"
  - "Comment peut-on repérer et éviter les tentatives d'hameçonnage dans les courriels et sur le web ?"
  - "Pourquoi est-il essentiel d'utiliser un gestionnaire de mots de passe et quelles règles de sécurité permet-il d'appliquer au quotidien ?"
  - "Quels outils et comportements spécifiques sont recommandés pour naviguer de façon sécuritaire et limiter le traçage de nos données personnelles sur le Web ?"
  - "Quelles stratégies d'authentification, incluant l'authentification multifacteur, doit-on adopter pour mieux protéger ses différents comptes en ligne ?"
  - "Pourquoi est-il dangereux d'utiliser le même mot de passe pour plusieurs services en ligne ?"
  - "Qu'est-ce que la pratique du « password stuffing » et en combien de temps peut-elle être exécutée après une compromission ?"
  - "Que démontrent les statistiques du site mentionné concernant la fréquence d'exposition des renseignements personnels ?"
  - "Quelles sont les mesures de sécurité recommandées pour protéger ses accès et ses renseignements personnels ?"
  - "Quels types d'attaques et de menaces informatiques ces bonnes pratiques permettent-elles de contrer ?"
  - "À quel type d'utilisateurs s'adresse la section portant sur les permissions Linux ?"
  - "Pourquoi est-il déconseillé d'utiliser la commande chmod 777 pour gérer l'accès à un fichier ?"
  - "Quel est le rôle de la protection \"sticky bit\" dans la gestion des fichiers et répertoires partagés ?"
  - "Pour quelle raison est-il préférable d'attribuer des permissions à un groupe plutôt qu'à plusieurs personnes individuellement ?"
  - "Pourquoi est-il déconseillé d'utiliser la commande chmod 777 pour gérer l'accès à un fichier ?"
  - "Quel est le rôle de la protection \"sticky bit\" dans la gestion des fichiers et répertoires partagés ?"
  - "Pour quelle raison est-il préférable d'attribuer des permissions à un groupe plutôt qu'à plusieurs personnes individuellement ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# Meilleures pratiques

Vous voulez savoir comment garder votre ordinateur personnel en sécurité? Vous voulez savoir à quel point votre ordinateur est protégé?
Vous trouverez ici quelques conseils pour améliorer la sécurité de votre ordinateur. Nous avons aussi préparé ce [court questionnaire](cybersecurity__personal_computer_health_check.md) pour vous permettre d’évaluer son niveau de sécurité.

## Mises à jour
Activez la fonction de mise à jour automatique du système d'exploitation et de vos applications.

Pour plus d’information, voir [Mises à jour logicielles : pourquoi elles sont essentielles pour votre cybersécurité](https://www.pensezcybersecurite.gc.ca/fr/blogues/mises-jour-logicielles-pourquoi-elles-sont-essentielles-pour-votre-cybersecurite).

## Mots de passe
Utilisez des mots de passe robustes. Voyez [Au sujet des mots de passe](#au-sujet-des-mots-de-passe) ci-dessous.

## Antivirus
Pour intercepter les logiciels malveillants, installez un antivirus et assurez-vous de toujours avoir la plus récente version.

## Hameçonnage
Avant de cliquer, portez attention aux hyperliens dans les courriels et les pages proposées par les moteurs de recherche. Un lien qui a un nom de domaine étrange est une indication probable d’une tentative d’hameçonnage.
Pour plus d’information, voir [Reconnaître les tentatives d'hameçonnage : comment se protéger](https://www.pensezcybersecurite.gc.ca/fr/blogues/reconnaitre-les-tentatives-dhameconnage-comment-se-proteger).

## Wi-Fi
Choisissez un mot de passe robuste et faites régulièrement la mise à jour du micrologiciel (*firmware*) de votre routeur.

Autant que possible, évitez de vous connecter aux réseaux Wi-Fi publics. Utilisez plutôt une solution de réseau privé virtuel (VPN) fiable.

Pour plus d'information, voir [Réseaux privés](https://www.pensezcybersecurite.gc.ca/fr/securisez-vos-connexions/reseaux) et [Réseaux Wi-Fi publics](https://www.pensezcybersecurite.gc.ca/fr/securisez-vos-connexions/reseaux-wi-fi-publics).

## Remarque
!!! note "Remarque"
    Ces conseils s’adressent surtout aux personnes soucieuses d’adopter de bonnes pratiques en matière de sécurité informatique pour leur ordinateur personnel.
    Les services informatiques des employeurs prennent généralement en charge la sécurité des ordinateurs utilisés pour le travail. Les mesures en place ne sont pas identiques et il est fortement recommandé de suivre les politiques de votre organisation.

# Au sujet des mots de passe
Malgré les nombreuses solutions pour protéger les données et les systèmes, les personnes malveillantes réussissent quand même à s’approprier les noms d'utilisateurs et les mots de passe. Que ce soit par manipulation psychosociale ou par hameçonnage, la raison tient souvent au fait que les mots de passe sont faibles, faciles à deviner ou qu’ils ont été employés par le passé.

Quel est le meilleur moyen d’assurer la sécurité de vos mots de passe?
A. les changer souvent
B. utiliser des caractères spéciaux et des majuscules
C. choisir un mot de passe long et unique

Le fait de changer souvent un mot de passe sans raison peut souvent rendre votre ordinateur plus vulnérable puisque la plupart des gens choisiront un mot de passe facile à retenir et basé sur un modèle prévisible.
Les longs mots de passe peuvent être sécuritaires, surtout s'ils sont uniques. La complexité peut aider, mais il semble que la longueur est plus importante que le type de caractères employé. La meilleure réponse est donc de créer des longs mots de passe ET d'avoir des mots de passe différents pour chaque service que vous utilisez. Pourquoi? Parce que les failles sont une réalité et il y a toujours la possibilité qu'un service présente une lacune et que vos renseignements soient exposés. Pour constater que ceci arrive plus souvent qu'on pense, voyez [ces statistiques](https://haveibeenpwned.com/). Si vos mots de passe ne sont pas uniques et qu'un d'eux se trouve exposé, il peut servir à accéder à tous les services que vous utilisez. Avec la pratique automatisée du *password stuffing*, ceci peut se produire après 12 heures qu'un mot de passe ait été compromis.

### Comment mieux se protéger

*   Utilisez un gestionnaire de mots de passe
    *   une telle application est essentielle et vous permettra d’appliquer toutes les règles qui suivent. Ces gestionnaires existent sous forme de programmes indépendants ou sont intégrés à un navigateur Web; ils sont des produits ou services obtenus du commerce ou disponibles comme logiciels libres (*open source*); le choix est vaste.
*   Utilisez des mots de passe différents pour tout
    *   avec un gestionnaire de mots de passe, rien de plus facile.
*   Allongez vos mots de passe à 15 caractères ou plus
    *   facile aussi avec un gestionnaire si vous lui permettez de générer vos mots de passe. Un mot de passe de 20 à 32 caractères n'est pas un problème puisque le gestionnaire s'en souvient pour vous.
*   Ne divulguez jamais vos mots de passe, à personne … mais vraiment … personne...
    *   Vos noms d'utilisateur et vos mots de passe servent à vous identifier et vous appartiennent. Si vous les partagez avec quelqu'un d'autre, votre identité devient à risque et vous contrevenez souvent en plus aux politiques du service ou du système que vous utilisez.
*   Changez un mot de passe uniquement quand il y a une excellente raison
    *   Vous devriez changer un mot de passe si vous pensez qu'il a été découvert, qu'il peut être réutilisé ou s'il n'est pas assez robuste. Ce n'est pas toujours une bonne raison de changer un mot de passe sur une base régulière comme l'exigent encore certaines organisations.

Si vous n'avez pas encore adopté ces mesures, **pas de panique!** Il n'est jamais trop tard pour commencer. Si vous avez des centaines de mots de passe, changez-en quelques uns chaque jour à l'heure du lunch par exemple. Chaque fois que vous augmentez le niveau de sécurité d'un cran, c'est un effort qui en vaut la peine.

# Naviguer de façon sécuritaire et utiliser l'authentification multifacteur
Nous comptons sur plusieurs ressources et plusieurs comptes pour bien accomplir les tâches exigées par notre travail. La manière dont nous accédons à ces outils ainsi que notre comportement en ligne peuvent avoir une grande importance pour notre sécurité personnelle et celles des ressources que nous partageons.

Nous pouvons protéger notre sécurité en contrôlant l'information que nous donnons aux fournisseurs de services, en limitant la capacité qu'ont les entités commerciales à suivre nos activités et en réfléchissant à l'authentification de nos comptes.

Nous pouvons commencer ici et maintenant en choisissant de partager moins de renseignements personnels quand on s'inscrit à un service ou quand on publie du contenu sur les médias sociaux. En divulguant un minimum de renseignements personnels, les pirates peuvent plus difficilement établir des liens entre l'information pour ensuite vous prendre comme cible.

Nous pouvons choisir d'utiliser des outils de recherche qui protègent davantage la confidentialité comme DuckDuckGo ([duckduckgo.com](https://duckduckgo.com/)); installer des extensions de navigateurs comme Privacy Badger ([privacybadger.org](https://privacybadger.org/)), HTTPS Everywhere ([eff.org/https-everywhere](https://www.eff.org/https-everywhere)) ou uBlock Origin ([ublockorigin.com](https://ublockorigin.com/)). Nous pouvons configurer les navigateurs pour limiter l'usage de témoins (*cookies*) ainsi que les liens et les outils de traçage des compagnies de médias sociaux ([mozilla.org/en-US/firefox/facebookcontainer](https://www.mozilla.org/en-US/firefox/facebookcontainer)).

En s'authentifiant à la création de comptes, nous pouvons utiliser des identifiants, noms d'utilisateur ou courriels différents; créer des comptes différents pour le travail et pour notre usage personnel; suivre les recommandations au sujet des mots de passe ci-dessus; et utiliser l'authentification multifacteur offerte par plusieurs fournisseurs de services.

Tout petit geste que vous posez peut faire en sorte que les pirates auront plus de difficulté à mener des attaques d'hameçonnage, réutiliser vos renseignements personnels ou deviner vos mots de passe et ceux de vos collègues.

# Permissions Linux

Cette section s'adresse à ceux et celles qui ont de bonnes connaissances techniques sur nos superordinateurs.

Les permissions Linux offrent une couche de protection à votre recherche. Évitez de faire les erreurs suivantes :

**Erreur n° 1** : Permettre l'accès général à un fichier avec la commande `chmod 777 name_of_file`.

Assurez-vous de bien comprendre le [fonctionnement des permissions Linux](../storage-and-data/sharing_data.md#permissions-des-syst%C3%A8mes-de-fichiers) et de limiter l'accès à vos fichiers en cas de besoin seulement.

**Erreur n° 2** : Ignorer le *sticky bit*, ce qui peut mener à la suppression de vos fichiers par un autre utilisateur ou utilisatrice.

Dans le cas de fichiers partagés où plusieurs ont les permissions de lecture et d'écriture, il y a toujours le risque qu'une personne supprime les fichiers ou les répertoires d'une autre. Utilisez [la protection sticky bit](../storage-and-data/sharing_data.md#protection-sticky-bit) quand elle est appropriée.

**Erreur n° 3** : Permettre l'accès à plusieurs personnes individuellement plutôt qu'à un groupe.

La [gestion des listes de contrôle d'accès](../storage-and-data/sharing_data.md#listes-de-contr%C3%B4le-d%27acc%C3%A8s) peut devenir rapidement complexe. La meilleure pratique est de donner des permissions à un groupe plutôt qu'à plusieurs personnes.