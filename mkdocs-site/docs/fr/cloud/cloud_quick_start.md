---
title: "Cloud Quick Start/fr"
slug: "cloud_quick_start"
lang: "fr"

source_wiki_title: "Cloud Quick Start/fr"
source_hash: "b609b6befefdc3ab84680244bd2a8c0b"
last_synced: "2026-09-06T00:43:13.954271+00:00"
last_processed: "2026-09-06T02:32:08.890166+00:00"

tags:
  - cloud

keywords:
  - "liste Disponible"
  - "IP flottante"
  - "colonne Tâche"
  - "groupes de sécurité"
  - "0.0.0.0/0"
  - "alerte"
  - "allocation projet"
  - "liste déroulante"
  - "adresse IP publique"
  - "projet cloud"
  - "licence Windows"
  - "SSH"
  - "Block Device Mapping"
  - "TODO"
  - "supprimer après terminaison"
  - "gabarits d'instances"
  - "Gérer les Associations d'IP flottantes"
  - "réseau par défaut"
  - "Volume persistant"
  - "Windows Server 2012"
  - "Importer une paire de clés"
  - "instance (machine virtuelle)"
  - "Importer une clé publique"
  - "Lancer une instance"
  - "navigateur compatible"
  - "Utiliser des clés SSH sous Linux"
  - "paire de clés SSH"
  - "MobaXterm"
  - "tableau de bord OpenStack"
  - "paires de clés SSH"
  - "Générer des clés SSH sous Windows"
  - "Administrator"
  - "liste Alloué"
  - "période d'évaluation de 180 jours"
  - "client Remmina"
  - "sauvegarde d'instance"
  - "nom d'utilisateur par défaut"
  - "Connexion Bureau à distance"
  - "public IP address"
  - "license information"
  - "lancer instance"
  - "VM existante"
  - "règles de sécurité"
  - "État de l'alimentation"
  - "localisation"
  - "taille du périphérique 30 Go"
  - "soutien technique"
  - "adresse IP privée"
  - "connexion SSH"
  - "Clés SSH"
  - "règle RDP"
  - "adresses IP"
  - "image Windows"
  - "gestion des ressources infonuagiques"
  - "image Ubuntu/Fedora"
  - "CIDR"
  - "mot de passe"
  - "création d'instance"
  - "Associer une adresse IP flottante"
  - "règle de connexion"
  - "Gabarit d'instance"
  - "Allocation d'IP"
  - "règle CIDR"
  - "Add PC"
  - "nom d'utilisateur"
  - "créer le volume"
  - "gabarit p2-3gb"
  - "attaque par force brute"
  - "licence cloud"
  - "Paires de clés"
  - "clé privée"
  - "liste des instances"

questions:
  - "Que faut‑il faire pour obtenir un projet cloud et où trouver les informations d’accès ?"
  - "Quels navigateurs sont recommandés pour accéder à l’interface web du cloud et que faire en cas d’erreur avec d’autres navigateurs ?"
  - "Comment créer et gérer une paire de clés SSH lors de la création d’une instance Linux sur OpenStack ?"
  - "Quelles sont les étapes à suivre pour importer une clé publique RSA dans OpenStack et quelles précautions doit‑on prendre lors du collage de la clé ?"
  - "Quels paramètres doivent être renseignés dans le formulaire « Lancer une instance », notamment concernant le nom, la source de démarrage, le volume et le gabarit ?"
  - "Pourquoi est‑il déconseillé de créer des paires de clés directement dans OpenStack et quelles sont les implications de choisir de supprimer ou de conserver le volume à la terminaison de l’instance ?"
  - "Que faut‑il faire si vous n’avez jamais utilisé de paire de clés SSH ou si vous ne souhaitez pas utiliser une paire existante ?"
  - "Où pouvez‑vous trouver les instructions pour générer une paire de clés SSH sous Windows ?"
  - "Où consulter des informations supplémentaires sur la création et la gestion des clés SSH ?"
  - "Que indique l’icône > placée au début d’une ligne dans la liste « Disponible » ?"
  - "Que se produit‑il lorsqu’une alerte signale qu’une ressource n’est pas suffisante pour le gabarit choisi ?"
  - "Comment déplacer un gabarit de la liste « Disponible » vers la liste « Alloué » ?"
  - "Comment sélectionner le réseau par défaut et le groupe de sécurité dans la liste « Alloué » sur Arbutus ?"
  - "Quelle est la procédure pour associer une adresse IP flottante (publique) à une instance existante ?"
  - "Comment gérer les paires de clés SSH (création, importation ou allocation) avant de lancer une instance ?"
  - "Comment associer une adresse IP flottante à une instance pour la première fois ?"
  - "Quel bouton faut‑il cliquer dans la fenêtre « Allouer une IP flottante » pour créer l’allocation ?"
  - "Comment sélectionner une adresse IP publique supplémentaire pour une instance déjà configurée ?"
  - "Comment associer une adresse IP publique à votre instance et où la retrouver dans le tableau de bord OpenStack ?"
  - "Quelles sont les étapes pour créer ou modifier une règle de sécurité SSH dans le groupe de sécurité, en spécifiant votre adresse IP ou une plage CIDR ?"
  - "Quels éléments (clé privée, type d’image, adresse IP publique) devez‑vous connaître pour vous connecter à votre instance via SSH ?"
  - "Quelle règle devez‑vous ajouter pour autoriser la connexion SSH depuis votre domicile ?"
  - "Où se trouve la clé privée que vous avez sauvegardée et comment l’utiliser pour vous connecter à votre instance ?"
  - "Quel type d’image (Ubuntu, Fedora, etc.) et quelle adresse IP publique sont associés à votre instance ?"
  - "Quelle commande SSH doit‑on utiliser depuis Linux ou macOS pour se connecter à une instance, et comment déterminer le nom d’utilisateur à spécifier ?"
  - "Quelles sont les étapes à suivre dans MobaXterm pour établir une connexion SSH à une instance depuis Windows, y compris la configuration de la clé privée ?"
  - "Comment obtenir l’accès à une image Windows pour créer une instance, et quelles sont les limitations liées à la licence d’évaluation ?"
  - "Quels paramètres doivent être renseignés dans l'onglet « Détails », notamment le gabarit, la taille du disque racine et l'option « Supprimer après Terminaison » ?"
  - "Comment configurer les options d’accès et de sécurité, comme la paire de clés SSH et les groupes de sécurité, avant de lancer l’instance ?"
  - "Après avoir cliqué sur « Démarrer », quelles informations suivre dans la colonne « Tâche » et « État de l’alimentation », et quel délai prévoir pour que l’instance soit pleinement opérationnelle ?"
  - "Comment faut‑il procéder pour obtenir l’accès à une image Windows via le soutien technique ?"
  - "Quelle est la durée de validité de l’accès fourni à l’image Windows Server 2012 et au nom d’utilisateur ?"
  - "Est‑il possible d’obtenir une licence Windows pour une instance créée à partir de l’image d’évaluation ?"
  - "Quelle information la colonne « Tâche » affiche‑t‑elle lors de la création d’une instance ?"
  - "Comment la colonne « État de l’alimentation » indique‑t‑elle que l’instance est opérationnelle ?"
  - "Quel est le délai minimum requis pour créer le volume, copier l’image et amorcer le démarrage de l’instance ?"
  - "Quels paramètres devez‑vous sélectionner et quelle action devez‑vous valider avant que le premier démarrage d’une instance Windows ne soit complet ?"
  - "Comment associer une adresse IP flottante à une instance et quelle différence y a‑t‑il entre une adresse IP privée et une adresse IP publique dans OpenStack ?"
  - "Quelles étapes sont nécessaires pour autoriser le protocole RDP via le groupe de sécurité « default », et pourquoi ne faut‑il pas laisser le CIDR à 0.0.0.0/0 ?"
  - "Quels paramètres (adresse IP publique, nom d'utilisateur, mot de passe) sont requis pour établir une connexion Bureau à distance vers une instance Windows ?"
  - "Quels clients de connexion à distance sont recommandés pour Windows, Linux (Remmina) et macOS (Windows App), et quelles sont les étapes de configuration spécifiques à chaque système ?"
  - "Comment gérer l’avertissement « The certificate is not from a trusted certifying authority » lors de la connexion RDP et quelles solutions sont envisagées (enregistrement du certificat, utilisation de Let’s Encrypt, ou simple ignorance) ?"
  - "Pourquoi laisser « 0.0.0.0/0 » dans le champ CIDR peut‑il rendre votre instance vulnérable aux attaques par force brute ?"
  - "Comment ajouter des règles pour autoriser l’accès à votre instance depuis d’autres adresses IP ?"
  - "Quel outil est recommandé pour définir un groupe d’adresses au format CIDR ?"
  - "What are the steps to add a new PC using its public IP address in the described interface?"
  - "Which credentials should be entered when prompted after double‑clicking the newly created tile?"
  - "Where can users find information on obtaining a license for the software?"
  - "Quel type de licence est requis pour exécuter une VM sur le cloud et quelles licences sont compatibles ?"
  - "Comment appliquer une licence existante à une machine virtuelle déjà déployée dans le cloud ?"
  - "La procédure d’application d’une licence diffère‑t‑elle entre une VM existante et la création d’une nouvelle VM ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Page enfant de [Service infonuagique](cloud.md)*

## Avant de commencer

1.  **Posséder un projet infonuagique**
    !!! important "Posséder un projet infonuagique"
        Vous devez posséder un projet infonuagique pour avoir accès à l'environnement infonuagique. Si vous ne possédez pas de [projet infonuagique](managing_your_cloud_resources_with_openstack.md#projets), voyez [Obtenir un projet dans l'environnement infonuagique](cloud.md#obtenir-un-projet-dans-lenvironnement-infonuagique). Une fois qu'un projet infonuagique est associé à votre compte, vous recevrez un courriel de confirmation qui contient les détails sur comment accéder à votre projet; assurez-vous de savoir où trouver ces renseignements.

2.  **Utiliser un navigateur compatible**
    !!! note "Utiliser un navigateur compatible"
        L'accès aux projets infonuagiques se fait sans problème avec les navigateurs [Firefox](https://www.mozilla.org/en-US/firefox/new/) et [Chrome](https://www.google.com/chrome/). D'autres navigateurs peuvent aussi bien fonctionner, mais certains ne sont pas pris en charge par notre interface web et affichent le message `Danger: There was an error submitting the form. Please try again.`. C'est le cas notamment de Safari sous Mac; une mise à jour pourrait résoudre le problème, mais nous vous recommandons d'utiliser [Firefox](https://www.mozilla.org/en-US/firefox/new/) ou [Chrome](https://www.google.com/chrome/). Si vous avez toujours des problèmes, écrivez au [soutien technique](../support/technical_support.md).

## Créer votre première instance

Votre projet infonuagique vous permettra de créer des instances (aussi appelées *machines virtuelles* ou *MV*) auxquelles vous pourrez accéder à partir de votre ordinateur via notre interface web.

1.  **Connectez-vous à l'interface du nuage pour avoir accès à votre projet**
    Le lien à cette interface se trouve dans le courriel de confirmation qui vous a été envoyé. Cliquez sur le lien pour ouvrir votre projet dans votre navigateur. Si votre navigateur n'est pas compatible, ouvrez un navigateur compatible et collez l'URL dans la barre d'adresse. Si vous connaissez le nom du nuage où se trouve votre projet mais n'avez pas son adresse URL, consultez la liste dans [Ressources infonuagiques](cloud.md#ressources-infonuagiques). Connectez-vous avec vos identifiants (nom d'utilisateur et mot de passe) et non avec votre adresse de courriel.

2.  **Consultez le tableau de bord OpenStack**
    OpenStack est la plateforme qui permet l'accès web aux nuages. Une fois la connexion établie, le tableau de bord OpenStack affiche les ressources de votre projet. Pour des renseignements sur le tableau de bord et la navigation OpenStack, consultez [la documentation officielle de OpenStack](https://docs.openstack.org/horizon/latest/user/index.html).

Vous trouverez ci-dessous les directives pour démarrer des instances Linux et Windows.

!!! note "Système d'exploitation de l'instance"
    Le système d'exploitation est celui de l'instance et non celui de l'ordinateur que vous utilisez pour vous connecter. Votre planification préalable devrait indiquer le système d'exploitation que vous utiliserez; en cas de doute, écrivez au [soutien technique](../support/technical_support.md).

# mkdocs-material-tabs
=== Linux ===

### Paires de clés SSH

À la création d’une instance, l'authentification par mot de passe est désactivée pour des raisons de sécurité.

OpenStack crée plutôt votre instance avec une clé SSH publique (*secure shell*) installée et pour vous connecter, vous devez utiliser cette paire de clés SSH. Si vous avez déjà utilisé des clés SSH, la clé publique peut provenir d'une paire de clés que vous avez déjà créée sur un autre nuage; si c'est le cas, voyez ci-dessous *Importer une paire de clés*. Si vous n'avez jamais utilisé une paire de clés SSH ou que vous ne voulez pas utiliser une paire existante, vous devez créer une paire de clés. Si vous travaillez sous Windows, voyez [Générer des clés SSH sous Windows](../getting-started/generating_ssh_keys_in_windows.md), autrement, voyez [Utiliser des clés SSH sous Linux](../getting-started/using_ssh_keys_in_linux.md). Pour plus d'information sur la création et la gestion des clés, consultez [Clés SSH](../getting-started/ssh_keys.md).

#### Importer une clé publique

1.  Dans le menu OpenStack de gauche, sélectionnez **Calcul** > **Paires de clés**.
2.  Cliquez sur le bouton **Importer une clé publique**.
3.  Entrez un nom pour la paire de clés.
4.  Collez votre clé publique (présentement, seules les clés SSH de type RSA sont valides).
    Assurez-vous que la clé publique que vous collez ne contient pas de caractère de fin de ligne ou d'espace.
5.  Cliquez sur le bouton **Importer une clé publique**.

!!! warning "Sécurité des paires de clés"
    Il n'est pas recommandé de créer des paires de clés dans OpenStack parce qu'elles ne sont pas créées avec une phrase de passe, ce qui cause des problèmes pour la sécurité.

### Lancer une instance

Pour créer une instance, sélectionnez **Calcul** > **Instances** dans le menu de gauche, puis cliquez sur le bouton **Lancer une instance**.

Le formulaire de création d'une instance est affiché. Vous pouvez utiliser les spécifications décrites à l'étape de votre préplanification ou reproduire l'exemple ci-dessous.
La fenêtre « Lancer une instance » présente plusieurs options :

#### Détails

*   *Nom de l'instance* : Entrez le nom de l'instance, sans aucun caractère spécial ou espace; voir les [règles de nomenclature](https://fr.wikipedia.org/wiki/Nom_de_domaine).
*   *Description* : Ce champ est optionnel.
*   *Zone de disponibilité* : Laissez *Toute zone de disponibilité*.
*   *Nombre* : Entrez le nombre d'instances à créer. Si vous n'avez pas besoin de plusieurs instances, laissez la valeur 1.

#### Source

*   *Sélectionnez la source de démarrage* : Pour votre première instance, sélectionnez *Image*; voir l'information sur les autres options dans [Démarrer depuis un volume](working_with_volumes.md).
*   *Créer un nouveau volume* : Cliquez sur *Oui*; les données de l'instance seront enregistrées dans le volume du nuage (stockage persistant). Pour plus d'information sur l'utilisation et la gestion des volumes, voir [Travailler avec des volumes](working_with_volumes.md).
    *   *Taille du volume (Go)* : Entrez la taille planifiée; autrement, 30 Go est une taille raisonnable pour le système d'exploitation et une quantité modeste de données. Pour plus d'information sur l'utilisation et la gestion des volumes, voir [Travailler avec des volumes](working_with_volumes.md).
    *   *Supprimer le volume après terminaison de l'instance* : Cliquez sur *Non* pour empêcher que le volume soit supprimé accidentellement. Cliquez sur *Oui* si vous voulez que le volume soit toujours supprimé avec l'instance.
*   **Alloué** et **Disponible** : La liste sous **Disponible** montre les images que votre instance peut démarrer. Pour les débutants Linux, nous recommandons la plus récente image **Ubuntu**, mais vous pouvez sélectionner un des autres systèmes d'exploitation Linux. Pour sélectionner une image, cliquez sur la flèche à la fin de sa ligne et l'image sera déplacée sous **Alloué**. Il est important de se souvenir de l'image que vous avez sélectionnée, par exemple Ubuntu, Fedora, etc.

#### Gabarit

*   **Alloué** et **Disponible** : Le gabarit identifie le matériel utilisé par votre instance et donc la capacité de la mémoire et du traitement. La liste sous **Disponible** montre les gabarits pour l'image source de démarrage. Cliquez sur l'icône > au début de la ligne pour savoir si ce gabarit est conforme à l'allocation pour votre projet. Si cette ressource n'est pas suffisante, une alerte sera affichée. Sélectionnez un autre gabarit et cliquez sur la flèche à la fin de la ligne pour le déplacer vers la liste **Alloué**. Pour plus d'information, voir [Gabarits d'instances](virtual_machine_flavors.md).

#### Réseaux :

Changez les valeurs uniquement si nécessaire. Sur Arbutus, sélectionnez le réseau par défaut qui commence habituellement par *def-project-name*.

#### Ports réseaux :

Ne changez pas les valeurs pour l'instant.

#### Groupes de sécurité :

Le groupe de sécurité par défaut devrait paraître dans la liste **Alloué**. Si ce n'est pas le cas, déplacez-le de la liste **Disponible** en cliquant sur la flèche à la fin de la ligne. Pour plus d'information, voir [Groupes de sécurité](managing_your_cloud_resources_with_openstack.md).

#### Paires de clés :

Sous **Disponible**, sélectionnez la paire de clés SSH que vous avez créée plus tôt et déplacez-la vers la liste **Alloué** en cliquant sur la flèche à la fin de la ligne. Si vous n'avez pas de paire de clés, vous pouvez la créer ou l'importer en cliquant sur les boutons dans le haut de la fenêtre (voir [Paires de clés SSH ci-dessus](#paires-de-cles-ssh)). Pour l'information sur la gestion et l'utilisation des paires de clés, voir [Clés SSH](../getting-started/ssh_keys.md).

#### Configuration :

Ne changez pas les valeurs pour l'instant; pour l'information sur la personnalisation des scripts, voir [Utilisation de cloud-init](automating_vm_creation.md#utilisation-de-cloud-init).

#### Groupes de serveurs :

Ne changez pas les valeurs pour l'instant.

#### Scheduler Hints :

Ne changez pas les valeurs pour l'instant.

#### Métadonnées :

Ne changez pas les valeurs pour l'instant.

Une fois que vous avez vérifié les options et défini votre instance, cliquez sur le bouton **Lancer une instance** pour créer votre instance. La liste de vos instances sera affichée. La colonne **Tâche** montre l'état de la tâche en cours qui sera probablement *Génération*. Une fois l'instance générée, l'état deviendra *En fonctionnement*, ce qui peut prendre quelques minutes.

### Configuration du réseau

La page **Instances** montre la liste des instances avec les adresses IP correspondantes dans la colonne **Adresse IP**. Chaque instance a au moins une adresse IP privée, mais certaines instances peuvent aussi avoir une deuxième adresse IP publique. Un réseau local est automatiquement créé quand vous créez votre projet OpenStack. Ce réseau local sert à connecter les instances entre elles et aussi à une passerelle Internet à l'intérieur du projet pour que les instances communiquent avec l'externe. Chacune des instances créées dans votre projet possède une adresse IP privée qui lui est assignée par le réseau, selon le format `192.168.X.Y`; cette adresse privée empêche la communication en provenance de l'extérieur. Pour sa part, l'adresse IP publique permet à des services ou des outils externes de communiquer avec l'instance via votre ordinateur personnel, par exemple pour effectuer des tâches administratives ou pour recevoir du contenu web. Une adresse IP publique sert aussi aux accès par nom de domaine.

#### Assigner une adresse IP publique

1.  Faites afficher la page des instances avec **Calcul** > **Instances**. Un menu déroulant se trouve à la fin de la ligne de votre instance.
2.  Cliquez sur l'icône ▼ à la fin de la ligne pour votre instance et sélectionnez **Associer une adresse IP flottante**, puis dans la fenêtre « Allouer une IP flottante », cliquez sur le bouton **Allocation d'IP**. Si vous faites cette association pour la première fois, cliquez sur l'icône + de la fenêtre « Gérer les Associations d'IP flottantes ». Si plus tard vous devez allouer encore une adresse IP publique pour cette instance, vous pouvez en sélectionner une dans la liste déroulante du champ **Adresse IP**.
3.  Cliquez sur le bouton **Associer**.
4.  Vous devriez maintenant avoir deux adresses IP dans la colonne, une au format `192.168.X.Y` et l'autre, votre clé publique. La liste de vos adresses publiques et des projets associés se trouve aussi sous **Réseau** > **IP flottantes**. Vous aurez besoin de votre adresse IP publique pour vous connecter à votre instance.

#### Configurer le pare-feu

1.  Faites afficher la page **Groupes de sécurité** avec **Réseau** > **Groupes de sécurité**.
2.  Sur la ligne pour le groupe par défaut, cliquez sur le bouton **Gérer les Règles** à la droite.
3.  Sur la page de gestion des règles, cliquez sur le bouton **+Ajouter une règle**.
4.  Dans le menu déroulant **Règles**, sélectionnez *SSH*.
5.  Laissez **CIDR** dans le champ **Distant**.
6.  Remplacez le contenu du champ **CIDR** par `` `votre-ip/32` ``, ce qui est l'adresse IP de l'ordinateur physique que vous voulez utiliser pour vous connecter à votre instance. Pour connaître votre adresse IP courante, entrez [ipv4.icanhazip.com](http://ipv4.icanhazip.com) dans votre navigateur. Pour avoir accès à votre instance à partir d'une autre adresse IP, vous pouvez ajouter d'autres règles pour chacune des adresses. Pour indiquer une série d'adresses IP, utilisez [cet outil](https://www.ipaddressguide.com/cidr) pour calculer votre règle CIDR.
7.  Cliquez sur le bouton **Ajouter** et la nouvelle règle sera affichée dans la liste des groupes de sécurité.

#### Points importants

!!! warning "Ne supprimez pas les règles de sécurité par défaut"
    Le fonctionnement de votre instance serait compromis (voir [Groupes de sécurité](managing_your_cloud_resources_with_openstack.md)).

!!! warning "Ne modifiez pas les règles de sécurité"
    Pour ce faire, il faut les supprimer et les ajouter une fois modifiées. Si vous faites une erreur à la création d'une règle pour le groupe de sécurité, supprimez la règle en cliquant sur le bouton à gauche de la rangée dans la fenêtre des groupes de sécurité et ajoutez une nouvelle règle modifiée.

*   Si vous changez l'endroit à partir duquel vous travaillez (et par le fait même votre adresse IP), vous devez ajouter la règle décrite ici pour la nouvelle adresse. Sachez que quand vous changez votre lieu de travail physique, par exemple pour travailler de la maison plutôt que du travail, vous changez aussi de réseau.
*   Si vous n'avez pas d'adresse IP statique pour le réseau que vous utilisez, souvenez-vous que celle-ci peut changer. Si vous ne pouvez plus vous connecter à votre instance après un certain temps, vérifiez si votre adresse IP a changé en entrant [ipv4.icanhazip.com](http://ipv4.icanhazip.com) dans votre navigateur et vérifiez si elle correspond à ce qui se trouve dans votre règle de sécurité. Si votre adresse IP change souvent mais que les chiffres à l'extrême gauche restent les mêmes, il pourrait être plus raisonnable d'ajouter une plage d'adresses IP plutôt que d'avoir à modifier fréquemment les règles de sécurité. Pour déterminer une plage CIDR, [utilisez cet outil](https://www.ipaddressguide.com/cidr) ou consultez la [notation CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation).
*   Il pourrait être utile de fournir une description pour vos règles de sécurité, par exemple *bureau* ou *maison*. Vous pourrez ainsi savoir si une règle n'est plus nécessaire quand vous voulez ajouter une nouvelle règle pour vous connecter par exemple de la maison.

### Connexion à votre instance par SSH

À la première étape de ce guide, vous avez sauvegardé une clé privée sur votre ordinateur; il est important de savoir où trouver cette clé parce que vous en avez besoin pour vous connecter à votre instance. Vous devez aussi vous souvenir du type d'image que vous avez sélectionnée (Ubuntu, Fedora, etc.) et de l'adresse IP publique associée à votre instance.

#### Connexion à partir de Linux ou Mac

Ouvrez un terminal et entrez la commande

```bash
ssh -i /chemin/vers/votre/cle/privee/ma_cle.key <nom_utilisateur>@<IP_publique_de_votre_serveur>
```

où `` `<nom_utilisateur>` `` est le nom de l'utilisateur qui se connecte et `` `<IP_publique_de_votre_serveur>` `` est l'IP publique que vous avez associée à votre instance à l'étape précédente. Le nom de l'utilisateur par défaut dépend de l'image.

| Distribution | Nom d'utilisateur |
| :----------- | :---------------- |
| Debian       | debian            |
| Ubuntu       | ubuntu            |
| CentOS       | centos            |
| Fedora       | fedora            |
| AlmaLinux    | almalinux         |
| Rocky        | rocky             |

Ces utilisateurs par défaut possèdent tous les privilèges `sudo`. La connexion directe au compte racine via SSH est désactivée.

#### Connexion à partir de Windows

La connexion SSH doit se faire par une application d'interface. Nous recommandons **MobaXterm** (voir les directives ci-dessous); vous pouvez aussi vous connecter par PuTTY (voir [Connexion à un serveur avec PuTTY](../getting-started/connecting_with_putty.md)).

[Téléchargez MobaXterm](http://mobaxterm.mobatek.net/).
Pour vous connecter :

1.  Lancez l'application MobaXterm.
2.  Cliquez sur **Sessions** puis sur **New session**.
3.  Sélectionnez une session SSH.
4.  Dans le champ *Remote host*, entrez l'adresse IP publique de votre instance.
5.  Assurez-vous que la case *Specify username* est cochée et entrez le type d'image pour votre instance en minuscules (bas de casse).
6.  Cliquez sur l'onglet *Advanced SSH settings* et cliquez sur la case *Use private key*.
7.  Cliquez sur l'icône de la page à la droite du champ *Use private key*. Dans la fenêtre qui s'affiche, sélectionnez la paire de clés (fichier .pem) que vous avez enregistrée sur votre ordinateur au début de ce guide.
8.  Cliquez sur **OK**. MobaXterm enregistre l'information que vous avez entrée pour vous connecter à d'autres moments et ouvre une connexion SSH pour votre instance. Une connexion SFTP est aussi ouverte pour vous permettre de glisser-déplacer des fichiers dans les deux sens, via le panneau de gauche.

## Pour plus d'information

*   [Introduction à Linux](../getting-started/linux_introduction.md), sur comment travailler en ligne de commande sous Linux
*   [Sécurité des instances virtuelles](security_considerations_when_running_a_vm.md)
*   [Configuration d'un serveur de données ou d'un serveur web](configuring_a_data_or_web_server.md)
*   [Gestion des ressources infonuagiques avec OpenStack](managing_your_cloud_resources_with_openstack.md)
*   [Glossaire technique de l'infonuagique](cloud_technical_glossary.md)
*   [Automatiser la création d'instances](automating_vm_creation.md)
*   [Sauvegarder une instance](backing_up_your_vm.md)
*   [Soutien technique](../support/technical_support.md)

=== Windows ===

### Demande d'accès à une image Windows

Pour créer une instance Windows sur un de nos nuages, vous devez d'abord demander l'accès à une image Windows en écrivant au [soutien technique](../support/technical_support.md).

L'accès à une image Windows Server 2012 et un nom d'utilisateur vous seront fournis; cet accès est valide pour une période d'évaluation de 180 jours. Il pourrait être possible d'associer une licence Windows à une instance créée avec l'image d'évaluation, mais nous ne fournissons pas ces licences.

### Lancer une instance

Pour créer une instance, cliquez sur l'option **Instances** dans le menu de gauche, puis sur le bouton **Lancer une instance**.

Le formulaire de création d'une instance est affiché.

#### Onglet « Détails »

*   *Zone de disponibilité* : Seule la zone *nova* est disponible; conservez ce nom.
*   *Nom de l'instance* : Entrez le nom de votre instance en respectant les [conventions de nomenclature](https://fr.wikipedia.org/wiki/Nom_de_domaine).
*   *Gabarit* : Le gabarit détermine les caractéristiques matérielles de l'instance; sélectionnez *p2-3gb*.
    L'image Windows est plutôt exigeante et nécessite un lecteur amorçable de grande capacité. Les gabarits de type c ont des disques racines de seulement 20 Go alors que les gabarits de type p offrent plus de capacité. La mémoire vive du plus petit gabarit de type p est de 1,5 Go, ce qui d'expérience n'est pas suffisant pour bien opérer Windows. La performance de l'instance sera meilleure si vous utilisez un gabarit un peu plus grand tel que *p2-3gb*.
*   *Nombre d'instances* : Nombre d'instances à créer.
*   *Source de démarrage de l'instance* : Source utilisée pour lancer l'instance; sélectionnez *Démarrage depuis une image (crée un nouveau volume)*.
*   *Nom de l'image* : Nom de l'image Windows qui vous est allouée.
*   *Taille du périphérique* : Taille du disque racine; entrez 30 Go ou plus.
    À la fin, le système d'exploitation occupe environ 20 Go, mais plus d'espace est requis pour les étapes préparatoires.
*   *Supprimer après Terminaison* : Si cette case est cochée, le volume créé avec l'instance est supprimé quand l'instance est terminée.

    !!! note "Supprimer le volume après terminaison"
        De façon générale, il n'est pas recommandé de cocher la case puisque le volume peut être supprimé manuellement et que l'instance peut être terminée sans la suppression du volume.

*   *Limites du projet* : Dans les barres de progression, la couleur verte montre la proportion des ressources utilisées par l'instance qui sera lancée. La couleur rouge indique que le gabarit utilise plus de ressources que celles allouées au projet. Le bleu montre les ressources utilisées par le projet.

#### Onglet « Accès et Sécurité »

*   *Paires de clés* : Sélectionnez votre paire de clés SSH.
    S'il n'y a qu'une paire de clés, elle est affichée par défaut. Si vous n'avez pas de paire de clés, reportez-vous à la section [Paires de clés SSH (voir ci-dessus dans l'onglet Linux)](#paires-de-cles-ssh).
*   *Groupes de sécurité* : Assurez-vous que la case *default* est cochée.

#### Onglet « Démarrage du réseau » :

Ne modifiez pas le contenu de ce champ. L'information relative aux réseaux sera présentée après le lancement de l'instance.

#### Onglet « Post-Création » :

Ne modifiez pas le contenu de ce champ.

#### Onglet « Options avancées » :

Ne modifiez pas l'option *Automatique* dans le champ *Partitionnement du disque*.

Après avoir vérifié le contenu de tous les champs, cliquez sur **Démarrer** pour lancer l'instance. La liste des instances est affichée et la colonne **Tâche** montre la tâche en cours de l'instance; au départ, la colonne **Tâche** montrera probablement *Block Device Mapping*. Une fois l'instance créée et le démarrage amorcé, la colonne **État de l'alimentation** montre *En fonctionnement*. Pour créer le volume, y copier l'image et amorcer le démarrage, il faudra au moins 10 minutes.

### Localisation et licence

Le premier démarrage de l'instance ne sera pas complété tant que les paramètres de localisation, de langue et de clavier ne sont pas sélectionnés et que vous n'avez pas accepté les conditions de la licence via la console du tableau de bord OpenStack.

Pour faire afficher la console :

1.  Dans le menu de gauche, cliquez sur l'option **Instances**.
2.  Cliquez sur le nom de l'instance Windows.
3.  Cliquez sur l'onglet **Console** et attendez que la console soit affichée.
    Si rien ne s'affiche sur la console, l'écran est peut-être en état de veille; cliquez dans l'écran ou appuyez sur une touche du clavier pour réactiver l'écran.

L'instance redémarrera et la console affichera un écran de connexion avec la date et l'heure (UTC).

### Réseau

Sous l'onglet **Instances** se trouve la liste des instances avec les adresses IP correspondantes. Chaque instance a au moins une adresse IP privée, mais certaines instances peuvent aussi avoir une deuxième adresse IP publique.

#### Adresse IP privée

Lorsque vous créez un projet OpenStack, un réseau local est créé pour vous. Ce réseau sert à la communication des instances entre elles ainsi qu'à la communication des instances avec l'extérieur du projet. Une adresse IP privée ne permet pas l'accès à l'instance en provenance de l'extérieur. Pour chaque instance créée à l'intérieur d'un projet, le réseau lui associe une adresse privée qui lui est propre; cette adresse est selon le format `192.168.X.Y`.

#### Adresse IP publique

Les adresses IP publiques permettent aux outils et services externes d'entrer en contact avec l'instance, par exemple pour effectuer des tâches de gestion ou pour fournir du contenu web. Les noms de domaines peuvent aussi pointer sur une adresse IP publique.

Pour assigner une adresse IP publique à une instance, cliquez sur l'icône ▼ pour dérouler le menu dans la colonne **Actions**, puis sélectionnez **Associer une adresse IP flottante**. Si vous faites cet exercice pour la première fois, votre projet n'a pas encore reçu une adresse IP externe. Vous devez appuyer sur le bouton **+**; ceci fait afficher la fenêtre « Gérer les Associations d'IP flottantes ». Il n'y a qu'un groupe d'adresses publiques et le groupe approprié sera sélectionné par défaut; cliquez sur le bouton **Associer**. La fenêtre « Allouer une IP flottante » est affichée et montre l'adresse IP et le port de son [NAT](https://en.wikipedia.org/wiki/Network_address_translation); cliquez sur le bouton **Allocation d'IP**.

#### Pare-feu et règles autorisant le Protocole Bureau à distance (RDP)

Pour vous connecter à votre instance avec un client à distance, vous devez d'abord autoriser le protocole RDP.

1.  Dans le menu de gauche, sélectionnez **Accès et Sécurité**. Sous l'onglet **Groupes de sécurité**, sélectionnez le groupe *default* et cliquez sur le bouton **Gérer les règles**.
2.  Dans la fenêtre de gestion des règles, cliquez sur le bouton **+Ajouter une règle**.
3.  Il existe une règle prédéfinie pour RDP; sélectionnez cette règle dans le menu déroulant du champ **Règle**; dans le champ **Distant**, laissez **CIDR**.
4.  Dans le champ **CIDR**, remplacez `` `0.0.0.0/0` `` par votre adresse IP.
    Si vous ne connaissez pas votre adresse IP courante, vous pouvez l'obtenir en entrant [ipv4.icanhazip.com](http://ipv4.icanhazip.com) dans votre fureteur. Le fait de laisser `` `0.0.0.0/0` `` permet l'accès possible à votre instance par quiconque et la rend vulnérable aux [attaques par force brute](https://fr.wikipedia.org/wiki/Attaque_par_force_brute). Pour permettre l'accès pour d'autres adresses IP, ajoutez des règles pour ces adresses ou indiquez un groupe d'adresses avec [cet outil](https://www.ipaddressguide.com/cidr).

    !!! warning "Sécurité : Ne pas utiliser `0.0.0.0/0`"
        Si vous laissez `` `0.0.0.0/0` `` dans le champ **CIDR**, l'administrateur de la ressource peut bloquer tout accès à votre instance jusqu'à ce que les règles de sécurité soient adéquates.

5.  Enfin, cliquez sur le bouton **Ajouter**.

### Connexion Bureau à distance

Pour se connecter à une instance Windows, nous utiliserons un client connecté à distance. Pour ce faire, nous devons fournir une adresse IP flottante, un nom d'utilisateur et un mot de passe.

#### À partir d'un client Windows

Plusieurs versions de Windows offrent par défaut la connexion Bureau à distance; si vous ne trouvez pas cette fonctionnalité, vous pouvez l'installer à partir de [ce site de Microsoft](https://www.microsoft.com/fr-ca/store/p/bureau-a-distance-microsoft/9wzdncrfj3ps) (l'installation est gratuite).

Lancez la connexion Bureau à distance et connectez-vous à votre instance Windows.

1.  Dans le champ *Ordinateur*, entrez l'adresse IP publique.
2.  Entrez votre *Nom d'utilisateur*.
3.  Cliquez sur le bouton **Connexion** dans le bas de la fenêtre.
4.  À l'invite, entrez le mot de passe récupéré à l'étape précédente.
5.  Cliquez sur **OK**.

Si vous utilisez l'application Windows, vous devriez voir une fenêtre similaire à celle illustrée à droite (dans la version originale du document). Pour vous connecter à votre MV Windows :

1.  Sélectionnez **Ajouter** dans le menu de gauche.
2.  Entrez l'adresse IP publique à côté de **Nom de l'ordi**.
3.  Cliquez sur le bouton **Ajouter et connecter** en bas.
4.  Entrez le mot de passe lorsque vous y êtes invité.
5.  Cliquez sur le bouton **OK**.

Vous recevrez probablement un message indiquant que l'identité de l'ordinateur distant ne peut pas être vérifiée et vous demandant si vous voulez quand même poursuivre; ceci est normal, alors répondez **Oui**. Votre instance Windows sera affichée dans la fenêtre du client de connexion au bureau à distance.

#### À partir d'un client Linux

Sous Linux, vous devez avoir un client de connexion à distance. Plusieurs clients sont disponibles; nous recommandons cependant Remmina qui semble bien fonctionner lorsque testé avec Ubuntu. Les directives pour Remmina et d'autres systèmes Linux dont Ubuntu, Debian et Fedora se trouvent [sur cette page web](https://github.com/FreeRDP/Remmina/wiki).

Une fois la connexion établie avec votre instance Windows :

1.  Cliquez sur **Create a new remote desktop file** (fichier avec le symbole plus (+) vert).
    Une fenêtre semblable à celle montrée à droite (dans la version originale du document) devrait paraître.
2.  Dans le champ *Serveur*, entrez l'adresse IP publique de votre instance Windows.
3.  Dans le champ *Nom d'utilisateur*, entrez votre nom d'utilisateur.
4.  Dans le champ *Mot de passe*, entrez le mot de passe obtenu à l'étape précédente.
5.  Cliquez sur **Connecter**.

#### À partir d'un client Mac

Pour vous connecter via RDP à partir de MacOS, vous aurez besoin d'un client de bureau à distance. Il existe plusieurs clients, mais l'application Windows App semble bien fonctionner. Pour installer le client, allez sur l'App Store et recherchez « Windows App ».

Une fois que vous avez installé et lancé l'application Windows App, pour vous connecter à votre MV Windows :

1.  Sélectionnez **Appareils** dans le menu de gauche.
2.  Sélectionnez **+** dans le coin supérieur droit et sélectionnez **Ajouter un PC**.
3.  Entrez l'adresse IP publique à côté de **Nom de l'ordi**.
4.  Cliquez sur le bouton **Ajouter** en bas.
5.  Double-cliquez sur la tuile nouvellement créée.
6.  Entrez le nom d'utilisateur **Administrateur** et le mot de passe lorsque vous y êtes invité.
7.  Cliquez sur le bouton **Continuer**.

### Licence

[ À compléter ]

## Pour plus d'information

*   [Sécurité des instances virtuelles](security_considerations_when_running_a_vm.md)
*   [Création d'une instance](cloud_quick_start.md)
*   [Gestion des ressources infonuagiques avec OpenStack](managing_your_cloud_resources_with_openstack.md)
*   [Glossaire technique de l'infonuagique](cloud_technical_glossary.md)
*   [Automatiser les instances](automating_vm_creation.md)
*   [Sauvegarder une instance](backing_up_your_vm.md)
*   [Soutien technique](../support/technical_support.md)