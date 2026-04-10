---
title: "Cloud Quick Start/fr"
slug: "cloud_quick_start"
lang: "fr"

source_wiki_title: "Cloud Quick Start/fr"
source_hash: "eb74632b04bd12473d4447c66da1ba5b"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T05:32:32.888745+00:00"

tags:
  - cloud

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

*Page enfant de [Service infonuagique](cloud.md)*

## Avant de commencer

1.  !!! warning "Posséder un projet infonuagique"
    **Vous devez posséder un projet infonuagique pour avoir accès à l'environnement infonuagique.** Si vous ne possédez pas de [projet cloud](managing-your-cloud-resources-with-openstack.md#projets), voyez [Obtenir un projet dans l'environnement infonuagique](cloud.md#obtenir-un-projet-dans-lenvironnement-infonuagique). Une fois qu'un projet infonuagique est associé à votre compte, vous recevrez un courriel de confirmation qui contient les détails sur comment accéder à votre projet; assurez-vous de savoir où trouver ces renseignements.

2.  !!! tip "Utiliser un navigateur compatible"
    L'accès aux projets infonuagiques se fait sans problème avec les navigateurs [Firefox](https://www.mozilla.org/en-US/firefox/new/) et [Chrome](https://www.google.com/chrome/). D'autres navigateurs peuvent aussi bien fonctionner, mais certains ne sont pas pris en charge par notre interface web et affichent le message `Danger: There was an error submitting the form. Please try again.`. C'est le cas notamment de Safari sous Mac; une mise à jour pourrait résoudre le problème, mais nous vous recommandons d'utiliser [Firefox](https://www.mozilla.org/en-US/firefox/new/) ou [Chrome](https://www.google.com/chrome/). Si vous avez toujours des problèmes, écrivez au [soutien technique](technical-support.md).

## Créer votre première instance

Votre projet infonuagique vous permettra de créer des instances (aussi appelées *machines virtuelles* ou *VM*) auxquelles vous pourrez accéder à partir de votre ordinateur via notre interface web.

1.  **Connectez-vous à l'interface infonuagique pour avoir accès à votre projet**
    Le lien à cette interface se trouve dans le courriel de confirmation qui vous a été envoyé. Cliquez sur le lien pour ouvrir votre projet dans votre navigateur. Si votre navigateur n'est pas compatible, ouvrez un navigateur compatible et collez l'URL dans la barre d'adresse. Si vous connaissez le nom du nuage où se trouve votre projet mais n'avez pas son adresse URL, consultez la liste dans [Ressources infonuagiques](cloud.md#ressources-infonuagiques). Connectez-vous avec vos identifiants (nom d'utilisateur et mot de passe) et non avec votre adresse de courriel.

2.  **Consultez le tableau de bord OpenStack**
    OpenStack est la plateforme qui permet l'accès web aux nuages. Une fois la connexion établie, le tableau de bord OpenStack affiche les ressources de votre projet. Pour des renseignements sur le tableau de bord et la navigation OpenStack, consultez [la documentation officielle de OpenStack](https://docs.openstack.org/horizon/latest/user/index.html).

Vous trouverez ci-dessous les directives pour démarrer des instances Linux et Windows. **Le système d'exploitation est celui de l'instance et non celui de l'ordinateur que vous utilisez pour vous connecter.** Votre planification préalable devrait indiquer le système d'exploitation que vous utiliserez; en cas de doute, écrivez au [soutien technique](technical-support.md).

::: tabs

## Linux

### Paires de clés SSH {#paires-de-clés-ssh}

À la création d’une instance, l'authentification par mot de passe est désactivée pour des raisons de sécurité.

OpenStack crée plutôt votre instance avec une clé SSH publique (*secure shell*) installée et pour vous connecter, vous devez utiliser cette paire de clés SSH. Si vous avez déjà utilisé des clés SSH, la clé publique peut provenir d'une paire de clés que vous avez déjà créée sur un autre nuage; si c'est le cas, voyez ci-dessous *Importer une paire de clés*. Si vous n'avez jamais utilisé une paire de clés SSH ou que vous ne voulez pas utiliser une paire existante, vous devez créer une paire de clés. Si vous travaillez sous Windows, voyez [Générer des clés SSH sous Windows](generating-ssh-keys-in-windows.md), autrement, voyez [Utiliser des clés SSH sous Linux](using-ssh-keys-in-linux.md). Pour plus d'information sur la création et la gestion des clés, consultez [Clés SSH](ssh-keys.md).

### Importer une clé publique

1.  Dans le menu OpenStack de gauche, sélectionnez *Compute->Paires de clés*.
2.  Cliquez sur le bouton *Importer une clé publique*.
3.  Entrez un nom pour la paire de clés.
4.  Collez votre clé publique (présentement, seules les clés SSH de type RSA sont valides).
    Assurez-vous que la clé publique que vous collez ne contient pas de caractère de fin de ligne ou d'espace.
5.  Cliquez sur le bouton *Importer une clé publique*.

!!! warning "Sécurité des paires de clés"
    **Il n'est pas recommandé de créer des paires de clés dans OpenStack parce qu'elles ne sont pas créées avec une phrase de passe, ce qui cause des problèmes pour la sécurité.**

### Lancer une instance

Pour créer une instance, sélectionnez *Compute->Instances* dans le menu de gauche, puis cliquez sur le bouton *Lancer une instance*.

Le formulaire de création d'une instance est affiché. Vous pouvez utiliser les spécifications décrites à l'étape de votre préplanification ou reproduire l'exemple ci-dessous.
La fenêtre *Lancer Instance* présente plusieurs options :

**Détails**
*   *Nom de l'instance* : Entrez le nom de l'instance, sans aucun caractère spécial ou espace; voir les [règles de nomenclature](https://fr.wikipedia.org/wiki/Nom_de_domaine).
*   *Description* : Ce champ est optionnel.
*   *Zone de disponibilité* : Laissez *Toute zone de disponibilité*.
*   *Nombre* : Entrez le nombre d'instances à créer. Si vous n'avez pas besoin de plusieurs instances, laissez la valeur 1.

**Source**
*   *Sélectionnez la source de démarrage* : Pour votre première instance, sélectionnez *Image*; voir l'information sur les autres options dans [Démarrer depuis un volume](working-with-volumes.md#démarrer-depuis-un-volume).
*   *Créer un nouveau volume* : Cliquez sur *Oui*; les données de l'instance seront enregistrées dans le volume du nuage (stockage persistant). Pour plus d'information sur l'utilisation et la gestion des volumes, voir [Travailler avec des volumes](working-with-volumes.md).
    *   *Taille du volume (Go)* : Entrez la taille planifiée; autrement, 30 Go est une taille raisonnable pour le système d'exploitation et une quantité modeste de données. Pour plus d'information sur l'utilisation et la gestion des volumes, voir [Travailler avec des volumes](working-with-volumes.md).
    *   *Supprimer le volume après terminaison de l'instance* : Cliquez sur *Non* pour empêcher que le volume soit supprimé accidentellement. Cliquez sur *Oui* si vous voulez que le volume soit toujours supprimé avec l'instance.
*   *Alloué* et *Disponible* : La liste sous *Disponible* montre les images que votre instance peut démarrer. Pour les débutants Linux, nous recommandons la plus récente image **Ubuntu**, mais vous pouvez sélectionner un des autres systèmes d'exploitation Linux. Pour sélectionner une image, cliquez sur la flèche à la fin de sa ligne et l'image sera déplacée sous *Alloué*. Il est important de se souvenir de l'image que vous avez sélectionnée, par exemple Ubuntu, Fedora, etc.

**Gabarit**
*   *Alloué* et *Disponible* : Le gabarit identifie le matériel utilisé par votre instance et donc la capacité de la mémoire et du traitement. La liste sous *Disponible* montre les gabarits pour l'image source de démarrage. Cliquez sur l'icône > au début de la ligne pour savoir si ce gabarit est conforme à l'allocation pour votre projet. Si cette ressource n'est pas suffisante, une alerte sera affichée. Sélectionnez un autre gabarit et cliquez sur la flèche à la fin de la ligne pour le déplacer vers la liste *Alloué*. Pour plus d'information, voir [Gabarits d'instances](virtual-machine-flavors.md).

**Réseaux** : Changez les valeurs uniquement si nécessaire. Sur Arbutus, sélectionnez le réseau par défaut qui commence habituellement par *def-project-name*.

**Ports réseaux** : Ne changez pas les valeurs pour l'instant.

**Groupes de sécurité** : Le groupe de sécurité par défaut devrait paraître dans la liste *Alloué*. Si ce n'est pas le cas, déplacez-le de la liste *Disponible* en cliquant sur la flèche à la fin de la ligne. Pour plus d'information, voir [Groupes de sécurité](managing-your-cloud-resources-with-openstack.md#groupes-de-sécurité).

**Paires de clés** : Sous *Disponible*, sélectionnez la paire de clés SSH que vous avez créée plus tôt et déplacez-la vers la liste *Alloué* en cliquant sur la flèche à la fin de la ligne. Si vous n'avez pas de paire de clés, vous pouvez la créer ou l'importer en cliquant sur les boutons dans le haut de la fenêtre (voir [Paires de clés SSH ci-dessus](#paires-de-clés-ssh)). Pour l'information sur la gestion et l'utilisation des paires de clés, voir [Clés SSH](ssh-keys.md).

**Configuration** : Ne changez pas les valeurs pour l'instant; pour l'information sur la personnalisation des scripts, voir [Utilisation de cloud-init](automating-vm-creation.md#utilisation-de-cloud-init).

**Groupes de serveurs** : Ne changez pas les valeurs pour l'instant.

**Scheduler Hints** : Ne changez pas les valeurs pour l'instant.

**Métadonnées** : Ne changez pas les valeurs pour l'instant.

Une fois que vous avez vérifié les options et défini votre instance, cliquez sur le bouton *Lancer Instance* pour créer votre instance. La liste de vos instances sera affichée. La colonne *Tâche* montre l'état de la tâche en cours qui sera probablement *Génération*. Une fois l'instance générée, l'état deviendra *En fonctionnement*, ce qui peut prendre quelques minutes.

### Configuration du réseau

La page *Instances* montre la liste des instances avec les adresses IP correspondantes dans la colonne *Adresse IP*. Chaque instance a au moins une adresse IP privée, mais certaines instances peuvent aussi avoir une deuxième adresse IP publique. Un réseau local est automatiquement créé quand vous créez votre projet OpenStack. Ce réseau local sert à connecter les instances entre elles et aussi à une passerelle internet à l'intérieur du projet pour que les instances communiquent avec l'externe. Chacune des instances créées dans votre projet possède une adresse IP privée qui lui est assignée par le réseau, selon le format `192.168.X.Y`; cette adresse privée empêche la communication en provenance de l'extérieur. Pour sa part, l'adresse IP publique permet à des services ou des outils externes de communiquer avec l'instance via votre ordinateur personnel, par exemple pour effectuer des tâches administratives ou pour recevoir du contenu web. Une adresse IP publique sert aussi aux accès par nom de domaine.

**Assigner une adresse IP publique**
1.  Faites afficher la page des instances avec *Compute->Instances*. Un menu déroulant se trouve à la fin de la ligne de votre instance.
2.  Cliquez sur l'icône &#x25BC; à la fin de la ligne pour votre instance et sélectionnez *Associer une adresse IP flottante* puis dans la fenêtre *Allouer une IP flottante*, cliquez sur le bouton *Allocation d'IP*. Si vous faites cette association pour la première fois, cliquez sur l'icône + de la fenêtre *Gérer les Associations d'IP flottantes*. Si plus tard vous devez allouer encore une adresse IP publique pour cette instance, vous pouvez en sélectionner une dans la liste déroulante du champ *Adresse IP*.
    *   Cliquez sur le bouton *Associer*.
    *   Vous devriez maintenant avoir deux adresses IP dans la colonne, une au format `192.168.X.Y` et l'autre, votre clé publique. La liste de vos adresses publiques et des projets associés se trouve aussi sous *Réseau->IP flottantes*. Vous aurez besoin de votre adresse IP publique pour vous connecter à votre instance.

**Configurer le pare-feu**
*   Faites afficher la page *Groupes de sécurité* avec *Réseau->Groupes de sécurité*.
*   Sur la ligne pour le groupe par défaut, cliquez sur le bouton *Gérer les Règles* à la droite.
*   Sur la page de gestion des règles, cliquez sur le bouton *+Ajouter une règle*.
*   Dans le menu déroulant *Règles*, sélectionnez *SSH*.
*   Laissez *CIDR* dans le champ *Distant*.
*   Remplacez le contenu du champ *CIDR* par `votre-ip/32`, ce qui est l'adresse IP de l'ordinateur physique que vous voulez utiliser pour vous connecter à votre instance. Pour connaître votre adresse IP courante, entrez [ipv4.icanhazip.com](http://ipv4.icanhazip.com) dans votre navigateur. Pour avoir accès à votre instance à partir d'une autre adresse IP, vous pouvez ajouter d'autres règles pour chacune des adresses. Pour indiquer une série d'adresses IP, utilisez [cet outil](https://www.ipaddressguide.com/cidr) pour calculer votre règle CIDR.
*   Cliquez sur le bouton *Ajouter* et la nouvelle règle sera affichée dans la liste des groupes de sécurité.

**Points importants**
*   !!! warning "Ne supprimez pas les règles par défaut"
    **Ne supprimez pas les règles de sécurité par défaut**; le fonctionnement de votre instance serait compromis (voir [Groupes de sécurité](managing-your-cloud-resources-with-openstack.md#groupes-de-sécurité)).
*   !!! tip "Modifier les règles de sécurité"
    **Ne modifiez pas les règles de sécurité**; pour ce faire, il faut les supprimer et les ajouter une fois modifiées. Si vous faites une erreur à la création d'une règle pour le groupe de sécurité, supprimez la règle en cliquant sur le bouton à gauche de la rangée dans la fenêtre des groupes de sécurité et ajoutez une nouvelle règle modifiée.
*   Si vous changez l'endroit à partir duquel vous travaillez (et par le fait même votre adresse IP), vous devez ajouter la règle décrite ici pour la nouvelle adresse. Sachez que quand vous changez votre lieu de travail physique, par exemple pour travailler de la maison plutôt que du travail, vous changez aussi de réseau.
*   Si vous n'avez pas d'adresse IP statique pour le réseau que vous utilisez, souvenez-vous que celle-ci peut changer. Si vous ne pouvez plus vous connecter à votre instance après un certain temps, vérifiez si votre adresse IP a changé en entrant [ipv4.icanhazip.com](http://ipv4.icanhazip.com) dans votre navigateur et vérifiez si elle correspond à ce qui se trouve dans votre règle de sécurité. Si votre adresse IP change souvent mais que les chiffres à l'extrême gauche restent les mêmes, il pourrait être plus raisonnable d'ajouter une plage d'adresses IP plutôt que d'avoir à modifier fréquemment les règles de sécurité. Pour déterminer une plage CIDR, [utilisez cet outil](https://www.ipaddressguide.com/cidr) ou consultez la [notation CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation).
*   Il pourrait être utile de fournir une description pour vos règles de sécurité, par exemple *bureau* ou *maison*. Vous pourrez ainsi savoir si une règle n'est plus nécessaire quand vous voulez ajouter une nouvelle règle pour vous connecter par exemple de la maison.

### Connexion à votre instance par SSH

À la première étape de ce guide, vous avez sauvegardé une clé privée sur votre ordinateur; il est important de savoir où trouver cette clé parce que vous en avez besoin pour vous connecter à votre instance. Vous devez aussi vous souvenir du type d'image que vous avez sélectionnée (Ubuntu, Fedora, etc.) et de l'adresse IP publique associée à votre instance.

### Connexion à partir de Linux ou Mac

Ouvrez un terminal et entrez la commande
```bash
ssh -i /path/where/your/private/key/is/my_key.key <user name>@<public IP of your server>
```
où `<user name>` est le nom de l'utilisateur qui se connecte et `<public IP of your VM>` est l'IP publique que vous avez associée à votre instance à l'étape précédente. Le nom de l'utilisateur par défaut dépend de l'image.

| Distribution | Nom d'utilisateur |
|--------------|-------------------|
| Debian       | debian            |
| Ubuntu       | ubuntu            |
| CentOS       | centos            |
| Fedora       | fedora            |
| AlmaLinux    | almalinux         |
| Rocky        | rocky             |

Ces utilisateurs par défaut possèdent tous les privilèges sudo. La connexion directe au compte racine via SSH est désactivée.

### Connexion à partir de Windows

La connexion SSH doit se faire par une application d'interface. Nous recommandons **MobaXterm** (voir les directives ci-dessous); vous pouvez aussi vous connecter par PuTTY (voir [Connexion à un serveur avec PuTTY](connecting-with-putty.md)).

[Téléchargez MobaXterm](http://mobaxterm.mobatek.net/).
Pour vous connecter :
1.  Lancez l'application MobaXterm.
2.  Cliquez sur *Sessions* puis sur *New session*.
3.  Sélectionnez une session SSH.
4.  Dans le champ *Remote host* entrez l'adresse IP publique de votre instance.
5.  Assurez-vous que la case *Specify username* est cochée et entrez le type d'image pour votre instance en minuscules (bas de casse).
6.  Cliquez sur l'onglet *Advanced SSH settings* et cliquez sur la case *Use private key*.
7.  Cliquez sur l'icône de la page à la droite du champ *Use private key*. Dans la fenêtre qui s'affiche, sélectionnez la paire de clés (fichier .pem) que vous avez enregistrée sur votre ordinateur au début de ce guide.
8.  Cliquez sur OK. MobaXterm enregistre l'information que vous avez entrée pour vous connecter à d'autres moments et ouvre une connexion SSH pour votre instance. Une connexion SFTP est aussi ouverte pour vous permettre de glisser-déplacer des fichiers dans les deux sens, via le panneau de gauche.

### Pour plus d'information

*   [Introduction à Linux](linux-introduction.md), sur comment travailler en ligne de commande sous Linux
*   [Sécurité des instances virtuelles](security-considerations-when-running-a-vm.md)
*   [Configuration d'un serveur de données ou d'un serveur web](configuring-a-data-or-web-server.md)
*   [Gestion des ressources infonuagiques avec OpenStack](managing-your-cloud-resources-with-openstack.md)
*   [Glossaire technique de l'infonuagique](cloud-technical-glossary.md)
*   [Automatiser la création d'instances](automating-vm-creation.md)
*   [Sauvegarder une instance](backing-up-your-vm.md)
*   [Soutien technique](technical-support.md)

## Windows

### Demande d'accès à une image Windows

Pour créer une instance Windows sur un de nos nuages, vous devez d'abord demander l'accès à une image Windows en écrivant au [soutien technique](technical-support.md).

L'accès à une image Windows Server 2012 et un nom d'utilisateur vous seront fournis; cet accès est valide pour une période d'évaluation de 180 jours. Il pourrait être possible d'associer une licence Windows à une instance créée avec l'image d'évaluation, mais nous ne fournissons pas ces licences.

### Paire de clés SSH {#paire-de-clés-ssh-windows}

Les instances Windows chiffrent les mots de passe des comptes administrateur avec une clé publique. La clé privée correspondante sert au déchiffrement.

Il est recommandé de créer une nouvelle paire de clés avec OpenStack plutôt que d'importer une paire de clés existante. Pour ce faire,
1.  Dans le menu de gauche, cliquez sur *Accès et Sécurité*.
2.  Cliquez sur l'onglet *Paires de clés*.
3.  Cliquez sur *+Créer une paire de clés*; ceci fait afficher la fenêtre de création.
4.  Entrez le nom de la paire de clés.
5.  Cliquez sur le bouton *Créer une paire de clés*.
6.  Sauvegardez le fichier .pem sur votre disque.

Si vous voulez utiliser une paire de clés existante, consultez d'abord les [remarques ci-dessous](#remarques-à-propos-des-paires-de-clés).

### Lancer une instance

Pour créer une instance, cliquez sur l'option *Instances* dans le menu de gauche, puis sur le bouton *Lancer une instance*.

Le formulaire de création d'une instance est affiché.

*   Onglet *Détails*
    *   *Zone de disponibilité* : Seule la zone *nova* est disponible; conservez ce nom.
    *   *Nom de l'instance* : Entrez le nom de votre instance en respectant les [conventions de nomenclature](https://fr.wikipedia.org/wiki/Nom_de_domaine).
    *   *Gabarit* : Le gabarit détermine les caractéristiques matérielles de l'instance; sélectionnez *p2-3gb*.
        L'image Windows est plutôt exigeante et nécessite un lecteur amorçable de grande capacité. Les gabarits de type c ont des disques racines de seulement 20Go alors que les gabarits de type p offrent plus de capacité. La mémoire vive du plus petit gabarit de type p est de 1.5Go, ce qui d'expérience n'est pas suffisant pour bien opérer Windows. La performance de l'instance sera meilleure si vous utilisez un gabarit un peu plus grand tel que *p2-3gb*.
    *   *Nombre d'instances* : Nombre d'instances à créer.
    *   *Source de démarrage de l'instance* : Source utilisée pour lancer l'instance; sélectionnez *Démarrage depuis une image (crée un nouveau volume)*.
    *   *Nom de l'image* : Nom de l'image Windows qui vous est allouée.
    *   *Taille du périphérique* : Taille du disque racine; entrez 30Go ou plus.
        À la fin, le système d'exploitation occupe environ 20Go, mais plus d'espace est requis pour les étapes préparatoires.
    *   *Supprimer après Terminaison* : Si cette case est cochée, le volume créé avec l'instance est supprimé quand l'instance est terminée.
        !!! warning "Supprimer après terminaison"
            De façon générale, il n'est pas recommandé de cocher la case puisque le volume peut être supprimé manuellement et que l'instance peut être terminée sans la suppression du volume.
    *   *Limites du projet* : Dans les barres de progression, la couleur verte montre la proportion des ressources utilisées par l'instance qui sera lancée. La couleur rouge indique que le gabarit utilise plus de ressources que celles allouées au projet. Le bleu montre les ressources utilisées par le projet.
*   Onglet *Accès et Sécurité*
    *   *Paires de clés* : Sélectionnez votre paire de clés SSH.
        S'il n'y a qu'une paire de clés, elle est affichée par défaut. Si vous n'avez pas de paire de clés, reportez-vous à la section [Paire de clés SSH](#paire-de-clés-ssh-windows) plus haut.
    *   *Groupes de sécurité* : Assurez-vous que la case *default* est cochée.
*   Onglet *Démarrage du réseau* : Ne modifiez pas le contenu de ce champ. L'information relative aux réseaux sera présentée après le lancement de l'instance.
*   Onglet *Post-Création* : Ne modifiez pas le contenu de ce champ.
*   Onglet *Options avancées* : Ne modifiez pas l'option *Automatique* dans le champ *Partitionnement du disque*.

Après avoir vérifié le contenu de tous les champs, cliquez sur *Démarrer* pour lancer l'instance. La liste des instances est affichée et la colonne *Tâche* montre la tâche en cours de l'instance; au départ, la colonne *Tâche* montrera probablement *Block Device Mapping*. Une fois l'instance créée et le démarrage amorcé, la colonne *État de l'alimentation* montre *En fonctionnement*. Pour créer le volume, y copier l'image et amorcer le démarrage, il faudra au moins 10 minutes.

### Localisation et licence

Le premier démarrage de l'instance ne sera pas complété tant que les paramètres de localisation, de langue et de clavier ne sont pas sélectionnés et que vous n'avez pas accepté les conditions de la licence via la console du tableau de bord OpenStack.

Pour faire afficher la console :
1.  Dans le menu de gauche, cliquez sur l'option *Instances*.
2.  Cliquez sur le nom de l'instance Windows.
3.  Cliquez sur l'onglet *Console* et attendez que la console soit affichée.
    Si rien ne s'affiche sur la console, l'écran est peut-être en état de veille; cliquez dans l'écran ou appuyez sur une touche du clavier pour réactiver l'écran.

Comme le curseur est souvent lent à réagir, utilisez plutôt les touches du clavier.
*   La touche de tabulation pour sélectionner les champs.
*   Les flèches *haut* et *bas* pour sélectionner les options.
*   Entrez les premières lettres du pays ou de la région pour positionner le menu déroulant près de la sélection.
*   Pour terminer, appuyez sur la touche de tabulation jusqu'à ce que le champ *next* (suivant) soit sélectionné et appuyez sur la touche Entrée.

On vous demandera d'accepter les conditions de la licence.
*   Appuyez sur la touche de tabulation jusqu'à ce que le champ *I accept* soit sélectionné.
*   Appuyez sur la touche Entrée.

L'instance redémarrera et la console affichera un écran de connexion avec la date et l'heure (UTC).

### Réseau

Sous l'onglet *Instances* se trouve la liste des instances avec les adresses IP correspondantes. Chaque instance a au moins une adresse IP privée, mais certaines instances peuvent aussi avoir une deuxième adresse IP publique.

#### Adresse IP privée

Lorsque vous créez un projet OpenStack, un réseau local est créé pour vous. Ce réseau sert à la communication des instances entre elles ainsi qu'à la communication des instances avec l'extérieur du projet. Une adresse IP privée ne permet pas l'accès à l'instance en provenance de l'extérieur. Pour chaque instance créée à l'intérieur d'un projet, le réseau lui associe une adresse privée qui lui est propre; cette adresse est selon le format `192.168.X.Y`.

#### Adresse IP publique

Les adresses IP publiques permettent aux outils et services externes d'entrer en contact avec l'instance, par exemple pour effectuer des tâches de gestion ou pour fournir du contenu web. Les noms de domaines peuvent aussi pointer sur une adresse IP publique.

Pour assigner une adresse IP publique à une instance, cliquez sur l'icône ▼ pour dérouler le menu dans la colonne *Actions*, puis sélectionnez *Associer une adresse IP flottante*. Si vous faites cet exercice pour la première fois, votre projet n'a pas encore reçu une adresse IP externe. Vous devez appuyer sur le bouton +; ceci fait afficher la fenêtre *Gérer les Associations d'IP flottantes*. Il n'y a qu'un groupe d'adresses publiques et le groupe approprié sera sélectionné par défaut; cliquez sur le bouton *Associer*. La fenêtre *Allouer une IP flottante* est affichée et montre l'adresse IP et le port de son [NAT](https://en.wikipedia.org/wiki/Network_address_translation); cliquez sur le bouton *Allocation d'IP*.

#### Pare-feu et règles autorisant le protocole RDP (*Remote Desktop Protocol*)

Pour vous connecter à votre instance avec un client à distance, vous devez d'abord autoriser le protocole RDP.

1.  Dans le menu de gauche, sélectionnez *Accès et Sécurité*. Sous l'onglet *Groupes de sécurité*, sélectionnez le groupe *default* et cliquez sur le bouton *Gérer les règles*.
2.  Dans la fenêtre de gestion des règles, cliquez sur le bouton *+Ajouter une règle*.
3.  Il existe une règle prédéfinie pour RDP; sélectionnez cette règle dans le menu déroulant du champ *Règle*; dans le champ *Distant*, laissez *CIDR*.
4.  Dans le champ *CIDR*, remplacez `0.0.0.0/0` par votre adresse IP.
    Si vous ne connaissez pas votre adresse IP courante, vous pouvez l'obtenir en entrant [ipv4.icanhazip.com](http://ipv4.icanhazip.com) dans votre fureteur. Le fait de laisser `0.0.0.0/0` permet l'accès possible à votre instance par quiconque et la rend vulnérable aux [attaques par force brute](https://fr.wikipedia.org/wiki/Attaque_par_force_brute). Pour permettre l'accès pour d'autres adresses IP, ajoutez des règles pour ces adresses ou indiquez un groupe d'adresses avec [cet outil](https://www.ipaddressguide.com/cidr).
    !!! warning "Ne laissez pas le champ CIDR à 0.0.0.0/0"
        **Si vous laissez `0.0.0.0/0` dans le champ `CIDR`, l'administrateur de la ressource peut bloquer tout accès à votre instance jusqu'à ce que les règles de sécurité soient adéquates.**
5.  Enfin, cliquez sur le bouton *Ajoutez*.

### Connexion bureau à distance

Pour se connecter à une instance Windows, nous utiliserons un client connecté à distance. Pour ce faire, nous devons fournir une adresse IP flottante, un nom d'utilisateur et un mot de passe.

#### Récupérer le mot de passe

Pour récupérer le mot de passe,
1.  Dans le menu de gauche, cliquez sur *Instances*.
2.  Dans le menu déroulant pour l'instance, sélectionnez *Récupérer le mot de passe*.

Le mot de passe a été chiffré avec la clé publique que vous avez sélectionnée à la création de l'instance. Pour le déchiffrer,
1.  Faites afficher le fichier où se trouve votre clé privée.
    Si vous avez suivi les directives pour les paires de clés SSH, une clé privée correspondant à la clé publique devrait être enregistrée sur votre ordinateur; le nom a le suffixe .pem.
2.  Sélectionnez la clé privée.
3.  Cliquez sur *Déchiffrer le mot de passe*.

Ne fermez pas cette fenêtre puisque nous utiliserons le mot de passe dans la prochaine étape. Le mot de passe peut être récupéré à nouveau en répétant ce processus.

#### À partir d'un client Windows

Plusieurs versions de Windows offrent par défaut la connexion Bureau à distance; si vous ne trouvez pas cette fonctionnalité, vous pouvez l'installer à partir de [ce site de Microsoft](https://www.microsoft.com/fr-ca/store/p/bureau-a-distance-microsoft/9wzdncrfj3ps) (l'installation est gratuite).

Lancez la connexion Bureau à distance et connectez-vous à votre instance Windows.
1.  Dans le champ *Ordinateur*, entrez l'adresse IP publique.
2.  Entrez votre *Nom d'utilisateur*.
3.  Cliquez sur le bouton *Connexion* dans le bas de la fenêtre.
4.  À l'invite, entrez le mot de passe récupéré à l'étape précédente.
5.  Cliquez sur *OK*.

Vous recevrez probablement un message indiquant que l'identité de l'ordinateur distant ne peut pas être vérifiée et vous demandant si vous voulez quand même poursuivre; ceci est normal, alors répondez *Oui*. Votre instance Windows sera affichée dans la fenêtre du client de connexion au bureau à distance.

[ À compléter ]
<!-- TODO: The specific certificate error is "The certificate is not from a trusted certifying authority". Is seeing this alert really normal? Do we want to register the windows image certificate with a signing authority? Could we use letsencrypt or should we just ignore this issue? -->

#### À partir d'un client Linux

Sous Linux, vous devez avoir un client de connexion à distance. Plusieurs clients sont disponibles; nous recommandons cependant Remmina qui semble bien fonctionner lorsque testé avec Ubuntu. Les directives pour Remmina et d'autres systèmes Linux dont Ubuntu, Debian et Fedora se trouvent [sur cette page web](https://github.com/FreeRDP/Remmina/wiki).

Une fois la connexion établie avec votre instance Windows,
1.  Cliquez sur *Create a new remote desktop file* (fichier avec le symbole plus (+) vert).
    Une fenêtre semblable à celle montrée à droite devrait paraître.
2.  Dans le champ *Server*, entrez l'adresse IP publique de votre instance Windows.
3.  Dans le champ *User name*, entrez votre nom d'utilisateur.
4.  Dans le champ *Password*, entrez le mot de passe obtenu à l'étape précédente.
5.  Cliquez sur *Connect*.

#### À partir d'un client Mac {#from-a-mac-client}

[ À compléter ]

#### Licence {#license-information}

[ À compléter ]
<!-- TODO: need to provide information which would be helpful for users to know what path to take to get a license. Should cover things like:
* Where to go to get a license
* What kind of license do I need/what licenses will work on the cloud
* How to apply my license to my existing cloud VM
* How to apply it to a new VM (if that is different than above bullet item) -->

### Remarques à propos des paires de clés {#remarques-à-propos-des-paires-de-clés}

Il existe différents formats pour les fichiers de clés et vous avez la possibilité de protéger ou non vos clés privées à l'aide de phrases de passe. Pour pouvoir déchiffrer le mot de passe pour votre instance Windows, votre clé privée doit être au format OpenSSH et ne pas être protégée avec une phrase de passe. Si votre paire de clés a été créée par OpenStack et que vous avez téléchargé le fichier de clés `.pem`, la clé privée sera déjà au format requis. Si vous avez créé votre paire de clés avec la [commande `ssh-keygen`](using-ssh-keys-in-linux.md) et que vous n'avez pas défini une phrase de passe, le format sera aussi fort probablement correct. Pour plus d'information sur les paires de clés, voyez la page [Clés SSH](ssh-keys.md).

Voici un exemple d'une clé privée appropriée au format OpenSSH, sans phrase de passe :

```
-----BEGIN RSA PRIVATE KEY-----
 MIIEowIBAAKCAQEAvMP5ziiOw9b5XMZUphATDZdnbFPCT0TKZwOI9qRNBJmfeLfe
 ...
 DrzXjRpzmTb4D1+wTG1u7ucpY04Q3KHmX11YJxXcykq4l5jRZTKj
 -----END RSA PRIVATE KEY-----
```

Au centre, `...` remplace plusieurs lignes de caractères semblables à celle qui précède et celle qui suit. Les deux exemples de clés privées ci-dessous ne fonctionneront pas pour des instances Windows avec OpenStack.

Format OpenSSH avec phrase de passe :

```
-----BEGIN RSA PRIVATE KEY-----
 Proc-Type: 4,ENCRYPTED
 DEK-Info: DES-EDE3-CBC,CA51DBE454ACC89A
 
 0oXD+6j5aiWIwrNMiGYDqoD0OqlURfKeQhy//FwHuyuithOSI8uwjSUqV9BM9vi1
 ...
 8XaBb/ALqh8zLQOXEUuTstlMWXnhzBWLvu7tob0QN7pI16g3CXuOag==
 -----END RSA PRIVATE KEY-----
```

Format ssh.com sans phrase de passe :

```
---- BEGIN SSH2 ENCRYPTED PRIVATE KEY ----
 Comment: "rsa-key-20171130"
 P2/56wAAA+wAAAA3aWYtbW9kbntzaWdue3JzYS1wa2NzMS1zaGExfSxlbmNyept%2F
 ...
 QJX/qgGp0=
 ---- END SSH2 ENCRYPTED PRIVATE KEY ----
```

### Pour plus d'information

*   [Sécurité des instances virtuelles](security-considerations-when-running-a-vm.md)
*   [Création d'une instance sous Linux](creating-a-linux-vm.md)
*   [Gestion des ressources infonuagiques avec OpenStack](managing-your-cloud-resources-with-openstack.md)
*   [Glossaire technique de l'infonuagique](cloud-technical-glossary.md)
*   [Automatiser les instances](automating-vm-creation.md)
*   [Sauvegarder une instance](backing-up-your-vm.md)
*   [Soutien technique](technical-support.md)
:::