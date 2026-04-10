---
title: "Multifactor authentication/fr"
slug: "multifactor_authentication"
lang: "fr"

source_wiki_title: "Multifactor authentication/fr"
source_hash: "b6414511ea1ae4fc2cab12d0f3a99e85"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T09:05:15.196425+00:00"

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

L’authentification multifacteur permet de protéger votre compte avec plus qu’un simple mot de passe. Une fois que votre compte est configuré pour utiliser cette fonctionnalité, vous devrez entrer votre mot de passe comme d’habitude, mais en plus effectuer une deuxième action (le *deuxième facteur*), pour avoir accès à la plupart de nos services.

Sélectionnez cette deuxième étape d’authentification parmi ces facteurs :
* accepter une notification sur votre appareil intelligent dans l’application Duo Mobile;
* entrer un code généré sur demande;
* presser un bouton sur une clé matérielle (YubiKey).

L’authentification multifacteur sera déployée graduellement. Cette fonctionnalité ne sera donc pas disponible immédiatement pour tous nos services.

## Webinaires à voir
Ces deux webinaires ont été enregistrés en octobre 2023 :
* [Authentification multifacteur pour la communauté de recherche](https://www.youtube.com/watch?v=ciycOUbchl8&ab_channel=TheAlliance%7CL%E2%80%99Alliance) (en français)
* [Multifactor authentication for researchers](https://www.youtube.com/watch?v=qNsUsZ73HP0&ab_channel=TheAlliance%7CL%E2%80%99Alliance) (en anglais)

## Enregistrement des facteurs
### Enregistrer plusieurs facteurs

!!! tip "Enregistrer plusieurs facteurs d'authentification"
    Lorsque vous activez l'authentification multifacteur pour votre compte, nous vous **recommandons fortement** d’enregistrer au moins deux options pour votre deuxième facteur. Vous pouvez par exemple vous servir de votre téléphone et de codes à usage unique; de votre téléphone et d’une clé YubiKey; ou encore de deux clés YubiKey. De cette façon, si une de ces options ne peut pas être employée, vous aurez un autre facteur pour accéder à votre compte.

### Utiliser un téléphone ou une tablette

1. Installez l'application Duo Mobile à partir du [Apple Store](https://itunes.apple.com/us/app/duo-mobile/id422663827) ou de [Google Play](https://play.google.com/store/apps/details?id=com.duosecurity.duomobile). Assurez-vous d'avoir la bonne application. Les applications TOTP comme Aegis, Google Authenticator et Microsoft Authenticator **ne sont pas compatibles** avec Duo et ne peuvent pas balayer le code QR.
2. Connectez-vous à votre compte et cliquez sur *Mon compte → [Gestion de l'authentification multifacteur](https://ccdb.alliancecan.ca/multi_factor_authentications)*.
3. Sous *Enregistrer un appareil*, cliquez sur *Duo Mobile*.
4. Entrez un nom pour identifier votre appareil. Cliquez sur *Continuer* pour faire afficher un code QR.
5. Dans l'application Duo Mobile, cliquez sur le signe **+** ou sur *Ajouter un compte*.
6. Touchez *Utiliser un code QR*.
7. Balayez le code QR qui est affiché dans CCDB.

    !!! warning "Important"
        Pour balayer le code QR, votre appareil doit avoir accès à l'internet par Wi-Fi ou par réseau cellulaire.

### Utiliser une clé YubiKey
Les YubiKey sont des petites clés matérielles produites par [Yubico](https://www.yubico.com/). Si vous n'avez pas de téléphone intelligent ou de tablette qui prend en charge Duo, si vous ne voulez pas employer ces appareils pour l'authentification multifacteur, ou s'il vous est souvent impossible de les utiliser, une clé YubiKey est votre meilleur choix. Certains modèles de YubiKey existent pour les ports USB-A, USB-C et Lightning; d'autres modèles prennent en charge la communication en champ proche (NFC) pour utilisation avec un téléphone ou une tablette.

!!! note "Compatibilité YubiKey"
    Une YubiKey doit supporter la fonction YubiKey OTP pour être compatible avec nos systèmes.

Nous recommandons YubiKey, série 5, mais certains modèles moins récents pourraient aussi fonctionner. Pour savoir si un produit offre la fonction Yubico OTP, [voir ce lien](https://www.yubico.com/products/identifying-your-yubikey/).

Une fois qu'une clé est enregistrée à votre compte comme facteur d'authentification, quand vous tenterez de vous connecter à une de nos grappes, on vous demandera d'entrer un mot de passe à utilisation unique (OTP); notez que l'invite peut être formulée autrement, par exemple *Enter a passcode*. Appuyez alors sur le bouton de la clé, ce qui génère une chaîne de 32 caractères qui forme un mot de passe à entrer. Vous n'avez pas besoin du clavier; la clé se connecte à votre ordinateur et entre elle-même la chaîne de caractères quand vous touchez le bouton.

Pour enregistrer une YubiKey, entrez son identifiant public, son identifiant privé et sa clé secrète dans la page *[Gestion de l'authentification multifacteur](https://ccdb.alliancecan.ca/multi_factor_authentications)*. Si ces renseignements ne sont pas disponibles, configurez votre clé comme suit.

#### Configurer votre YubiKey pour Yubico OTP

1. Si votre ordinateur bloque les fenêtres contextuelles, désactivez cette fonction pour permettre leur affichage quand vous effectuez les autres étapes.
2. Téléchargez et installez YubiKey Authenticator à partir du [site Web de Yubico](https://www.yubico.com/products/yubico-authenticator/).
3. Insérez la clé YubiKey et lancez YubiKey Authenticator.
4. Dans YubiKey Authenticator, cliquez sur *Slots*.
5. Vous pouvez ici configurer l'une de deux options. *Short Touch (Slot 1)* identifie une touche brève (de 1 à 2,5 secondes) et *Long Touch (Slot 2)* correspond à une touche plus longue (de 3 à 5 secondes). L'option numéro 1 est généralement préenregistrée pour le mode Cloud. Si vous utilisez déjà cette option pour d'autres services, configurez plutôt l'option 2, ou cliquez sur *Swap slots* pour transférer la configuration de l'option 1 vers l'option 2 avant de configurer l'option 1.
6. Sélectionnez *Yubico OTP / Program a Yubico OTP credential*.
7. Dans le champ *Public ID*, cliquez sur *Use serial* pour générer un identifiant privé et une clé secrète.

    !!! warning "Important"
        Dans un endroit sécuritaire, **faites une copie de l'identifiant public, de l'identifiant privé et de la clé secrète** parce que vous en aurez besoin à la prochaine étape. (Note : L'identifiant public, l'identifiant privé et la clé secrète étaient nommés *Public ID*, *Private ID* et *Secret Key* dans l'application YubiKey Authenticator.)

8. !!! warning "Sauvegarde"
    **Assurez-vous d'avoir cliqué sur *Save*** (Sauvegarder) après la configuration.

9. Connectez-vous à CCDB et cliquez sur *Mon compte → [Gestion de l'authentification multifacteur](https://ccdb.alliancecan.ca/multi_factor_authentications)*.

Vous pouvez tester la configuration en appuyant sur le bouton de la clé YubiKey quand celle-ci est insérée dans votre ordinateur. Si la configuration est correcte, un code sera généré à l'invite ou sous le curseur.

## Authentification
### Connexion à une grappe via SSH
Quand vous vous connectez à une grappe via SSH, l'invite vous demande votre deuxième facteur après que vous avez entré votre mot de passe ou votre [clé SSH](ssh-keys.md).

````bash
ssh cluster.computecanada.ca
````
```text
Duo two-factor login for name

Enter a passcode or select one of the following options:

 1. Duo Push to My phone (iOS)

Passcode or option (1-1):
```

Vous pouvez maintenant indiquer le téléphone ou la tablette qui recevra une notification de la part de Duo. Si vous avez enregistré plusieurs appareils, une liste sera affichée, dans laquelle vous pouvez sélectionner l'appareil de votre choix. Vous n'avez qu'à accepter la notification pour confirmer votre deuxième authentification.

Si vous utilisez une YubiKey, vous n'avez qu'à la toucher quand l'invite pour le code de passe est affichée.
Si vous utilisez un code de contournement ou un code unique montré par Duo Mobile qui est valide pour un temps limité, vous devrez le coller ou l'entrer à l'invite.

````bash
ssh cluster.computecanada.ca
````
```text
Duo two-factor login for name

Enter a passcode or select one of the following options:

 1. Duo Push to My phone (iOS)

Passcode or option (1-1):vvcccbhbllnuuebegkkbcfdftndjijlneejilrgiguki
Success. Logging you in...
```

#### Configurer votre client SSH avec ControlMaster
##### Linux et MacOS
Si vous vous connectez avec OpenSSH, vous pouvez configurer votre client SSH pour diminuer la fréquence à laquelle vous devez utiliser la deuxième authentification. Modifiez `~/.ssh/config` en ajoutant les lignes suivantes :

````ini
Host HOSTNAME
    ControlPath ~/.ssh/cm-%r@%h:%p
    ControlMaster auto
    ControlPersist 10m
````
Remplacez `HOSTNAME` par le hostname du serveur que vous voulez configurer. Ceci vous permettra d'ouvrir une première session SSH avec le premier et le deuxième facteur, mais les connexions SSH suivantes à partir du même appareil utiliseront la connexion de la première session (sans vous demander de vous authentifier), même si votre première session est récente.

Sachez que le mécanisme multiplexeur de ControlMaster ne fonctionne pas sous Windows natif; dans ce cas vous aurez besoin du [sous-système Windows pour Linux](https://learn.microsoft.com/fr-fr/windows/wsl/about).

##### Windows
Voir [Utiliser WSL comme un serveur relais pour ControlMaster](configuring-wsl-as-a-controlmaster-relay-server.md).

### Pour vous connecter à votre compte
Si l'authentification multifacteur est activée pour votre compte, vous devez d’abord passer la première authentification avec votre nom d'utilisateur et votre mot de passe. Ce qui suit sera affiché pour la deuxième authentification :

(Remarque : *Ceci n'est pas la fenêtre définitive*.)

## Configuration de clients SSH courants
Les clients ligne de commande prennent généralement en charge l'authentification multifacteur sans plus de configuration. Par contre, ce n'est souvent pas le cas pour tous les clients. Vous trouverez ci-dessous des directives spécifiques à quelques-uns d’entre eux.

### FileZilla
FileZilla demande le mot de passe et le deuxième facteur chaque fois qu'un transfert est initié puisque par défaut, les transferts utilisent des connexions distinctes qui sont automatiquement fermées après un certain temps d'inactivité.

Pour ne pas avoir à saisir plusieurs fois le mot de passe et le deuxième facteur, vous pouvez limiter le nombre de connexions à chaque site à « 1 » dans *Gestionnaire de sites > Paramètres de transfert*; prenez note que vous perdrez ainsi la possibilité de parcourir le serveur lors des transferts.

1. Lancez FileZilla et sélectionnez *Gestionnaire de sites*.
2. Dans *Gestionnaire de sites*, modifiez un site existant ou créez un nouveau site.
3. Sous l'onglet *Général*, entrez les choix suivants :
    *   *Protocole : SFTP – SSH File Transfer Protocol*
    *   *Hôte :* [nom de l'hôte pour la grappe de connexion]
    *   *Type d'authentification : Interactive*
    *   *Identifiant :* [votre nom d'utilisateur]
4. Sous l'onglet *Paramètres de transfert* :
    *   cochez la case *Limiter le nombre de connexions simultanées*
    *   *Nombre maximum de connexions : 1*
5. Cliquez sur *OK* pour sauvegarder la connexion.
6. Testez la connexion.

#### Niagara, un cas particulier
FileZilla peut être configuré pour utiliser une clé SSH ou une invite interactive, mais non les deux à la fois. Puisqu’une clé SSH et un second facteur sont nécessaires pour se connecter à Niagara, ceci pose un problème. Nous vous recommandons d'utiliser un client SCP qui supporte mieux les invites interactives, ou encore

1. connectez-vous quand même avec une clé SSH; l'invite interactive fera échouer la connexion, mais FileZilla se souviendra de la clé;
2. modifiez ensuite la méthode de connexion pour une connexion interactive et connectez-vous de nouveau; l'invite pour votre deuxième facteur sera alors fonctionnelle.

### MobaXTerm
Installez la version 23.1 ou une version plus récente.
[La version 23.5](https://web.archive.org/web/20231214123606/mobaxterm.mobatek.net/download-home-edition.html) (sur Archive.org) est la dernière version pour laquelle les instructions suivantes fonctionnent pour la plupart des gens.

#### Invite lors d'un transfert de fichiers
En se connectant à un serveur distant, MobaXTerm établit par défaut deux connexions : une première pour le terminal et une seconde pour naviguer dans les fichiers à distance. Puisque le navigateur utilise par défaut le *protocole SFTP*, votre deuxième facteur d'authentification vous est demandé une seconde fois.

Ce comportement peut être amélioré en configurant le *Type de navigateur SSH* à *SCP (vitesse améliorée)* ou à *SCP (vitesse normale)* dans les *Paramètres SSH avancés* de la session.

#### Utiliser une clé SSH plutôt qu'un mot de passe
Vous pouvez résoudre les problèmes associés (1) aux téléchargements et (2) à l'utilisation d'une phrase de passe SSH plutôt que votre mot de passe avec l'Alliance en modifiant les paramètres de SSH comme suit (onglet *SSH* dialogue *Paramètres*) :

1. la case à cocher *GSSAPI Kerberos* doit être vide,
2. la case à cocher *Utiliser Pageant externe* doit être vide,
3. cochez *Utiliser l'agent SSH interne "MobAgent"*,
4. cliquez sur le bouton + pour sélectionner le fichier de clé SSH.

#### Problèmes connus
Le comportement de MobaXterm est étrange, dépendant plus ou moins de la version. Les fichiers peuvent être ouverts via le terminal, mais via la barre de navigation de gauche, l'ouverture, le téléchargement et le téléversement restent suspendus indéfiniment.

Pour utiliser MobaXterm, il faut initier et authentifier trois sessions indépendantes :

1. ouvrir le terminal ssh
2. faire afficher le contenu du répertoire dans le panneau de gauche
3. lancer le transfert des fichiers

Il est possible que quelques fenêtres de Duo qui attendent l'authentification soient cachées derrière d'autres fenêtres.

Aussi, quand vous naviguez vers un autre répertoire via le panneau de gauche, une autre transaction d'authentification peut être initiée, dépendant de la version.

### PuTTY
Installez la version 0.72 ou une version plus récente.

### WinSCP
Assurez-vous que vous utilisez des [clés SSH](ssh-keys.md).

### PyCharm
Vous devez configurer vos [clés SSH](ssh-keys.md) avant de vous connecter à nos grappes avec PyCharm.

Quand vous vous connectez à un hôte distant, entrez votre nom d'utilisateur et le nom de l'hôte auquel vous voulez vous connecter. Vous devez ensuite entrer un *mot de passe à usage unique* pour vous authentifier. Dépendant de comment votre compte est configuré, utilisez votre YubiKey ou le mot de passe généré dans Duo.

### Cyberduck
Par défaut, Cyberduck ouvre une nouvelle connexion pour chaque transfert de fichier et vous demande chaque fois votre deuxième facteur. Pour modifier ceci, utilisez les préférences, sous *Transferts*, onglet *Général* et dans le menu déroulant de *Transférer des fichiers*, sélectionnez *Utiliser la connexion du navigateur*.

Assurez-vous de ne pas cocher la case pour *Téléchargements segmentés avec plusieurs connexions par fichier*.

## Foire aux questions
### Est-ce que je peux utiliser Authy ou l'authentification par Google ou Microsoft?
Non, vous devez utiliser Duo Mobile.

### Je n'ai pas de tablette ni de téléphone intelligent et je ne veux pas acheter une YubiKey
Malheureusement, vous ne pourrez pas utiliser nos services quand l'authentification multifacteur sera obligatoire, ce qui est une exigence des organismes qui accordent du financement à l'Alliance. Une clé YubiKey est le moyen le plus économique de vous authentifier et compte parmi le matériel qui est généralement financé dans le cadre des projets de recherche.

### Pouvez-vous m'envoyer des codes de passe à usage unique via SMS?
Nous devrions alors assumer les frais d'envoi, ce que nous ne pouvons pas faire. Aussi, cette méthode n'est pas à toute épreuve selon l'opinion de la plupart des spécialistes en sécurité.

### Pouvez-vous m'envoyer des codes de passe à usage unique par courriel?
Non, ceci n'est pas supporté par Duo.

### J'ai un vieux téléphone Android et je ne trouve pas l'application Duo Mobile dans Google Play. Est-ce que je peux quand même utiliser Duo?
Duo Mobile est uniquement disponible pour les versions d'Android qui reçoivent les mises à jour de sécurité. Bien qu'il soit possible de la télécharger et de l'installer manuellement sur les versions plus anciennes d'Android en suivant [ces instructions](https://help.duo.com/s/article/2211?language=en_US), l'application risque de ne pas fonctionner correctement, voire pas du tout, et le service Duo pourrait refuser les tentatives d'authentification.

### Je veux désactiver l'authentification multifacteur. Comment dois-je procéder?
Cette fonctionnalité est maintenant obligatoire et ne peut pas être désactivée. Nous accordons des exceptions uniquement dans le cas de processus automatisés. Si l'authentification multifacteur vous dérange, nous vous suggérons d'employer une des configurations décrites ci-dessus, selon le client SSH que vous utilisez. Vous trouverez d'autres suggestions dans [ces webinaires](#webinaires-à-voir).

### Je n'ai pas de tablette ni de téléphone intelligent assez récent. Comment puis-je utiliser l'authentification multifacteur?
Vous pouvez [utiliser une clé YubiKey](#utiliser-une-clé-yubikey).

### J’ai perdu un appareil que j’utilisais comme deuxième facteur. Que puis-je faire?
*   Si vous avez configuré plusieurs appareils ou si vous avez généré des codes de contournement, utilisez une des méthodes suivantes pour [accéder à votre compte](https://ccdb.alliancecan.ca/multi_factor_authentications). Enregistrez tout nouvel appareil et supprimez celui que vous avez perdu. Si vous n'avez enregistré qu'un seul appareil, vous ne pouvez pas le supprimer.
*   Si vous n’avez sauvegardé aucun code de contournement et que vous avez perdu tous les appareils que vous avez enregistrés, copiez la liste suivante et ajoutez-y le plus de détails possible. Faites parvenir cette information à support@tech.alliancecan.ca.
    *   Quelle est l’adresse de courriel principale enregistrée dans votre compte?
    *   Depuis combien de temps détenez-vous un compte actif avec nous?
    *   Quel est votre domaine de recherche?
    *   Quelle est votre adresse IP? (pour connaître votre adresse IP, [cliquez sur ce lien](https://whatismyipaddress.com/))
    *   Quel est le nom de la chercheuse principale ou du chercheur principal qui vous parraine?
    *   Qui sont les membres de votre groupe?
    *   Avec qui pouvons-nous communiquer au sujet de votre demande?
    *   Quelles sont les grappes que vous utilisez le plus?
    *   Quels sont les modules logiciels que vous chargez le plus souvent sur nos grappes?
    *   À quand remonte la dernière tâche que vous avez soumise sur nos grappes?
    *   Mentionnez les identifiants de quelques-unes des tâches en lot que vous avez récemment soumises sur nos grappes.
    *   Décrivez les sujets et donnez les identifiants de vos plus récentes demandes de soutien technique.

### Quels clients SSH puis-je utiliser quand l'authentification multifacteur est configurée?
La plupart des clients qui utilisent une interface ligne de commande, comme sous Linux et macOS.
*   [Cyberduck](#cyberduck)
*   [FileZilla](#filezilla)
*   JuiceSSH sous Android
*   [MobaXTerm](#mobaxterm)
*   [PuTTY](#putty)
*   [PyCharm](#pycharm)
*   Termius sous iOS
*   VSCode
*   [WinSCP](#winscp)

### J'ai besoin de connexions SSH qui se font automatiquement aux grappes à partir de mon compte; est-ce que je peux utiliser l'authentification multifacteur?
Nous préparons actuellement des nœuds de connexion qui seront réservés aux processus automatisés. Pour plus d'information, voir [Flux de travail automatisés et authentification multifacteur](automation-in-the-context-of-multifactor-authentication.md).

### Message *Access denied. Duo Security does not provide services in your current location*
Duo bloque le processus d'authentification quand une adresse IP provient d'une région ou d'un pays soumis à des sanctions économiques et commerciales (voir [Duo help](https://help.duo.com/s/article/7544?language=en_US)).

## Fonctions avancées
### Configurer votre YubiKey pour Yubico OTP via la ligne de commande (`ykman`)
1. Installez le logiciel de ligne de commande YubiKey Manager (`ykman`) en suivant les directives pour votre système d'exploitation dans le [guide ykman](https://docs.yubico.com/software/yubikey/tools/ykman/Install_ykman.html#download-ykman).
2. Entrez votre YubiKey et prenez connaissance de l'information sur la clé avec la commande `ykman info`.
3. Prenez connaissance de l'information sur OTP avec la commande `ykman otp info`.
4. Choisissez entre Slot 1 et Slot 2 et lancez la commande `ykman otp yubiotp` pour programmer l'option.
5. !!! warning "Sauvegarde des identifiants YubiKey"
    **Dans un endroit sécuritaire, conservez une copie de l’identifiant public, l’identifiant privé et la clé secrète**; ils seront nécessaires à la prochaine étape.
6. Connectez-vous à la CCDB pour enregistrer votre clé dans la page *[Gestion de l'authentification multifacteur](https://ccdb.alliancecan.ca/multi_factor_authentications)*.

````console
[name@yourLaptop]$ ykman otp yubiotp -uGgP vvcccctffclk 2
Using a randomly generated private ID: bc3dd98eaa12
Using a randomly generated secret key: ae012f11bc5a00d3cac00f1d57aa0b12
Upload credential to YubiCloud? [y/N]: y
Upload to YubiCloud initiated successfully.
Program an OTP credential in slot 2? [y/N]: y
Opening upload form in browser: https://upload.yubico.com/proceed/4567ad02-c3a2-1234-a1c3-abe3f4d21c69
`