---
title: "Securing your account/fr"
slug: "securing_your_account"
lang: "fr"

source_wiki_title: "Securing your account/fr"
source_hash: "abb19a461735c60564c7b3cc2291371f"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T11:14:23.827196+00:00"

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

## Authentification
Les deux méthodes d'authentification pour accéder aux grappes sont par mot de passe et par clés SSH.

### Par mot de passe
Nous vous demandons d'employer des mots de passe uniques que vous n'utiliserez jamais par la suite.

!!! warning "Mesures de sécurité pour votre mot de passe"
    *   Votre mot de passe est confidentiel et critique; ne le dévoile à personne et ne le partagez pas avec d'autres utilisateurs. Évitez également de donner toute information qui permettrait de deviner votre mot de passe.
    *   Autant que possible, ne consignez pas par écrit votre mot de passe. Si vous devez l'écrire ou le sauvegarder sur un support quelconque, assurez-vous que les mesures de sécurité appropriées sont en place pour empêcher les accès non autorisés (chiffrement, mots de passe robustes, etc.). N'écrivez ou n'enregistrez jamais un mot de passe qui vous permet d'accéder à un système d'information ou de transférer des éléments entre ces systèmes.
    *   Il est déconseillé d'utiliser la fonction de votre navigateur ou de votre système d'exploitation qui se souvient de votre mot de passe.

#### Réinitialiser votre mot de passe
Si vous croyez que la sécurité de votre mot de passe a été compromise, vous pouvez le réinitialiser [dans la base de données CCDB par l'onglet *Mon compte*, option *Modifier le mot de passe*](https://ccdb.computecanada.ca/security/change_password).

### Par clés SSH
Une bonne manière de vous authentifier comme propriétaire de votre compte sans avoir chaque fois à entrer votre mot de passe est d'employer des clés SSH.

!!! warning "Sécurité des clés SSH"
    *   Pour assurer la sécurité, **il faut absolument utiliser une phrase de passe robuste**.
    *   Votre clé privée est comme un jeton de sécurité, même si elle est chiffrée avec un mot de passe. N'utilisez pas une clé privée sur un ordinateur que vous partagez avec d'autres utilisateurs. Sur une grappe, une clé privée qui n'est pas chiffrée représente un immense risque.

Pour les détails sur l'implémentation des clés SSH, consultez la page wiki [Clés SSH](ssh_keys.md).

### Authentification multifacteur
L'authentification multifacteur vous permet de protéger votre compte avec plus qu'un mot de passe ou une clé SSH. Si votre compte est configuré pour utiliser cette fonctionnalité et que vous voulez accéder à nos services, vous devez d'abord entrer votre nom d'utilisateur et mot de passe ou votre clé SSH, et ensuite vous authentifier avec un *deuxième facteur*. Il est fortement recommandé d'activer l'authentification multifacteur pour votre compte. Pour plus d'information, voyez [notre page wiki Authentification multifacteur](multifactor_authentication.md).

## Meilleures pratiques

### Partage des données
Quand plusieurs utilisateurs doivent partager les mêmes données, la solution la plus simple semble de modifier les permissions du système de fichier pour permettre à tous de lire et écrire dans les mêmes fichiers. Il faut cependant respecter certains principes pour éviter de compromettre la sécurité; consultez la page wiki [Partage des données](sharing_data.md).

### Ordinateur à partir duquel vous vous connectez

!!! important "Mesures préventives pour votre ordinateur local"
    L'accès par un tiers aux clés SSH (avec ou sans mot de passe) est souvent la cause des brèches de sécurité. Certaines mesures peuvent aider à les prévenir :
    *   connectez-vous à partir d'un ordinateur que vous savez sans risque;
    *   sous Windows, faites régulièrement des vérifications avec un analyseur de virus et de logiciels malveillants;
    *   peu importe votre système d'exploitation, effectuez régulièrement des mises à jour de sécurité pour tous vos logiciels;
    *   ne laissez jamais votre ordinateur sans surveillance.
    *   sur les clients qui utilisent OpenSSH (Linux, Mac et avec cette option sous Windows), vous pouvez configurer le comportement de SSH avec `~/.ssh/config`. En particulier, vous pouvez définir le comportement du système et même de certaines fonctionnalités relatives à l'utilisateur comme la sélection d'une clé particulière devant être utilisée, la sélection automatique de fonctions avancées comme la redirection X/port et même ProxyJump.

### Ordinateur auquel vous vous connectez
Un avantage important de l'utilisation de clés SSH est qu'un système distant n'a besoin que de votre clé publique, qui n'est pas une information sensible. Vous ne courez aucun risque si une clé publique est connue par d'autres; tout ce qui peut se produire c'est que vous obtiendrez plus d'accès.

!!! warning "Sécurité sur les machines distantes"
    *   Ne placez pas de clés privées sur une machine distante, même celles qui sont chiffrées. Une clé qui n'est pas chiffrée est comme un mot de passe qui peut être volé ou dévoilé involontairement. Une clé qui n'est pas chiffrée n'est pas sensible en soi, sauf quand vous l'utilisez sur la machine, ce qui voudrait dire que vous jugez cette machine comme étant sécuritaire.
    *   Si vous utilisez ssh-agent, ne le dirigez pas vers une machine distante à laquelle vous n'avez pas confiance.