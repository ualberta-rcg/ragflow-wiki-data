---
title: "Globus/fr"
slug: "globus"
lang: "fr"

source_wiki_title: "Globus/fr"
source_hash: "ac58c6ee7dac0ff38aba1568a08489fb"
last_synced: "2026-04-18T23:39:30.217451+00:00"
last_processed: "2026-04-19T00:47:47.821526+00:00"

tags:
  - connecting

keywords:
  - "portail Globus"
  - "usage général"
  - "Sécurité"
  - "point de chute Globus"
  - "clé d'accès et clé secrète"
  - "collection Globus"
  - "recherche"
  - "grappes"
  - "Globus Connect"
  - "ajouter des utilisateurs"
  - "nom d'utilisateur"
  - "installation"
  - "invitations"
  - "tâches massivement parallèles"
  - "collection partagée"
  - "partager le fichier"
  - "groupe"
  - "client ligne de commande OpenStack"
  - "point de chute"
  - "Partage de fichiers"
  - "gestion des accès"
  - "Use Selected"
  - "partage de fichiers"
  - "Soutien technique"
  - "permissions"
  - "collections"
  - "authentification"
  - "Globus"
  - "GridFTP"
  - "IA"
  - "openstack ec2 credentials"
  - "Arbutus S3 buckets"
  - "adresse courriel"
  - "sous-répertoire"
  - "identifiants"
  - "partage de données"
  - "partage"
  - "Groupes Globus"
  - "Alliance de recherche numérique du Canada"
  - "chemin"
  - "téléchargement"
  - "Arbutus S3"
  - "système d'exploitation"
  - "Interface ligne de commande"
  - "AWS IAM Access Key"
  - "Permissions"
  - "utilisateurs"
  - "Identifiant universel unique UUID"
  - "transfert de fichiers"
  - "Globus Connect Personal"
  - "Stockage objet"
  - "Machines virtuelles"
  - "Collection partagée"

questions:
  - "Qu'est-ce que le service Globus et quels sont les avantages de son utilisation pour le transfert de fichiers de recherche ?"
  - "Comment doit-on s'authentifier pour accéder au portail Globus de l'Alliance de recherche numérique du Canada ?"
  - "Quelles sont les étapes nécessaires pour configurer et lancer un transfert de données entre un ordinateur personnel et une grappe de calcul ?"
  - "Comment peut-on trouver le nom de la collection Globus associée à une grappe particulière ?"
  - "Quelles sont les différentes grappes informatiques disponibles pour un usage général ?"
  - "Quelles grappes sont spécifiquement dédiées à l'intelligence artificielle et aux tâches massivement parallèles ?"
  - "Comment s'authentifier sur une collection Globus et quelles sont les étapes pour lancer un transfert de fichiers ?"
  - "Quelles sont les options de transfert et de synchronisation disponibles, et quelle est la mise en garde concernant le chiffrement ?"
  - "Comment installer et configurer le client Globus Connect Personal sur un ordinateur personnel ?"
  - "Comment doit-on procéder pour autoriser le transfert de fichiers entre deux points de chute personnels ?"
  - "Quel est le principal avantage de la fonction de partage de fichiers Globus pour la collaboration ?"
  - "Quelles sont les démarches qu'un chercheur principal doit suivre pour activer le partage dans le répertoire /project ?"
  - "Comment trouver et télécharger le fichier d'installation de Globus Connect Personal pour un système d'exploitation spécifique ?"
  - "Quel est le format du nom complet attribué au point de chute une fois l'installation terminée ?"
  - "Quelle action le guide s'apprête-t-il à expliquer dans la section suivante du document ?"
  - "Que permet de faire l'activation du partage sur un chemin de répertoire principal ?"
  - "À quel niveau de l'arborescence peut-on créer un nouveau point de chute Globus partagé ?"
  - "Comment peut-on configurer des accès distincts pour différents utilisateurs au sein d'un même répertoire partagé ?"
  - "Pourquoi ne faut-il pas utiliser de lien symbolique lors de la préparation des données à partager ?"
  - "Comment configurer une nouvelle collection partagée (Guest Collection) à partir d'un point de chute sur le portail Globus ?"
  - "Quelles sont les différentes méthodes proposées pour attribuer des permissions d'accès à d'autres personnes ou groupes ?"
  - "À quoi sert l'option \"group\" lors du partage d'un fichier ?"
  - "Quels sont les deux critères de recherche permettant de trouver un groupe spécifique ?"
  - "Pourquoi est-il recommandé d'utiliser l'UUID plutôt que le nom du groupe, et où peut-on trouver cet identifiant ?"
  - "Comment peut-on gérer les permissions d'accès (lecture et écriture) et supprimer une collection partagée sans affecter les fichiers originaux ?"
  - "Quelles sont les principales précautions de sécurité à prendre en compte avant de partager des fichiers avec d'autres utilisateurs ?"
  - "Quelle est la procédure pour créer un groupe Globus et y inviter de nouveaux membres afin de faciliter la gestion des partages ?"
  - "Quelles sont les méthodes permettant de trouver et d'inviter des utilisateurs à rejoindre un groupe nouvellement créé ?"
  - "Sur quel bouton faut-il cliquer pour envoyer le message d'invitation aux personnes sélectionnées ?"
  - "À quelle condition le nom d'un utilisateur invité s'affichera-t-il officiellement dans le groupe ?"
  - "Comment installer l'interface en ligne de commande (CLI) Globus sur une grappe de calcul ?"
  - "Quelles sont les solutions recommandées pour créer un point de chute Globus sur une machine virtuelle infonuagique ?"
  - "Quelle est la procédure pour configurer l'accès au stockage objet sur Arbutus via Globus ?"
  - "Comment générer la clé d'accès et la clé secrète à l'aide du client en ligne de commande OpenStack ?"
  - "Quelle est la procédure pour se connecter au portail Globus ?"
  - "Que doit-on sélectionner dans la fenêtre du gestionnaire de fichiers une fois connecté à Globus ?"
  - "Quelles sont les étapes à suivre dans l'interface pour consentir à l'accès aux données et terminer la configuration ?"
  - "Comment générer et où entrer le code d'accès et la clé secrète requis pour le bucket Arbutus S3 ?"
  - "Quelles informations doivent être incluses lors de l'envoi d'une demande de soutien technique à l'équipe Globus ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Globus](https://www.globus.org/) est un service qui permet le transfert de fichiers de façon rapide, fiable et sécuritaire. Conçue expressément pour les besoins de la recherche, l'interface graphique de Globus comporte des fonctions de suivi en arrière-plan qui automatisent la gestion des transferts de fichiers entre deux supports, qu'il s'agisse de nos grappes ou d'un autre site, d'une grappe localisée sur un campus, d'un serveur de laboratoire, d'un microordinateur ou d'un ordinateur portatif.

Globus utilise le protocole de transfert GridFTP, mais vous permet d'éviter les tâches complexes et laborieuses qui s’y associent ainsi que d’autres aspects liés au déplacement des données. Le service améliore la performance des protocoles GridFTP, rsync, scp et sftp par le réglage automatique des paramètres de transfert, le redémarrage automatique lorsqu’il y a interruption du transfert et la vérification de l'intégrité des fichiers.

Vous pouvez accéder au service par [le site web de Globus](https://www.globus.org/) ou par notre portail Globus sur [https://globus.alliancecan.ca/](https://globus.alliancecan.ca/).

## Utilisation
Rendez-vous sur [le portail Globus de l'Alliance](https://globus.alliancecan.ca/). Sélectionnez *Alliance de recherche numérique du Canada* ou *Digital Research Alliance of Canada* (**et non *Digital Research Alliance of Canada - Staff***) dans la liste déroulante et cliquez sur *Continuer*. Entrez les informations d'identification pour votre compte CCDB. Ceci vous conduit au portail web de Globus.

### Lancer un transfert
Les transferts de données se font entre collections (points de chute dans les versions précédentes). Des collections sont déjà définies pour la plupart de nos systèmes. Pour transférer des fichiers en provenance ou à destination de votre ordinateur, vous devez créer une collection. Une fois que cette étape quelque peu exigeante est accomplie, il ne restera qu'à vous assurer que l'application Globus Connect Personal est en opération sur votre ordinateur pour effectuer un transfert. Voir la section [Ordinateurs personnels](#ordinateurs-personnels) ci-dessous.

Si le [Gestionnaire de fichiers du portail Globus](https://globus.alliancecan.ca/file-manager) n'est pas affiché, sélectionnez-le à partir de la barre de gauche.

Trois boutons *Volets* se trouvent à droite dans le haut de la page; pour voir ensemble deux collections, cliquez sur le deuxième bouton.

Pour trouver une collection, cliquez sur *Rechercher* et entrez le nom de la collection.

Pour sélectionner une collection, vous pouvez commencer à entrer son nom. Par exemple, pour transférer des données en provenance ou à destination de Rorqual, entrez `rorqual`, attendez deux secondes et sélectionnez `alliancecan#rorqual` dans la liste affichée.

Toutes nos grappes ont une collection Globus dont le nom se trouve dans le haut de chacune des pages pour la grappe en particulier.

| Usage général | Pour les tâches massivement parallèles | Pour l'IA |
| :------------ | :----------------------------------- | :-------- |
| * [Fir](../software/fir.md) | * [Trillium](../clusters/trillium.md)             | * [Killarney](../clusters/killarney.md) |
| * [Narval](../clusters/narval.md) |                                      | * [TamIA](../clusters/tamia.md)     |
| * [Nibi](../clusters/nibi.md) |                                      | * [Vulcan](../clusters/vulcan.md)   |
| * [Rorqual](../clusters/rorqual.md) |                                      |           |

Dépendant du site où se trouve la collection, vous pourriez devoir vous authentifier. Par exemple, si vous activez une collection qui se trouve sur Nibi, vous devrez entrer votre identifiant et votre mot de passe. L'authentification d'une de nos collections reste habituellement valide pour une semaine alors que celle des collections personnelles n'a pas d'échéance.

Faites une recherche pour sélectionner une deuxième collection et authentifiez-vous si requis.

Quand une collection est active, une liste des répertoires et des fichiers est affichée; vous pouvez double-cliquer sur les répertoires et utiliser le bouton pour naviguer dans la structure. Pour sélectionner un répertoire ou un fichier que vous voulez transférer, cliquez sur son nom; pour une sélection multiple, utilisez Ctrl + clic. Cliquez ensuite sur un des gros boutons bleus avec des flèches blanches pour lancer le transfert. Ceci crée une tâche avec un identifiant unique et le transfert commence immédiatement; vous recevrez un courriel quand le transfert sera terminé. Pour suivre le déroulement et voir les détails sur le transfert, cliquez sur [le bouton Activité](https://globus.alliancecan.ca/activity) dans la barre de gauche.

Voir aussi [Comment se connecter et transférer des fichiers avec Globus](https://docs.globus.org/how-to/get-started/) sur le site web Globus.org.

### Options
Plusieurs autres options se trouvent dans la zone *Options de transfert et de synchronisation* entre les deux boutons *Lancer* du centre. Vous pouvez ici demander à Globus de
*   synchroniser, pour transférer de nouveaux fichiers ou des fichiers modifiés,
*   supprimer des fichiers à la destination qui sont inexistants à la source,
*   conserver les renseignements quant au moment des modifications de fichiers,
*   vérifier l'intégrité des données après un transfert (option sélectionnée par défaut),
*   chiffrer le transfert.

!!! warning "Chiffrement"
    Prenez note que la fonction de chiffrement diminue de beaucoup la performance du transfert et ne devrait être utilisée que pour des données sensibles.

### Ordinateurs personnels
Globus fournit un client pour utilisation avec un microordinateur sous Windows, macOS ou Linux; voyez [Globus Connect Personal](https://www.globus.org/globus-connect-personal).

La page [Globus Connect Personal](https://www.globus.org/globus-connect-personal) contient des liens sur comment faire la configuration pour les différents systèmes d'exploitation, incluant comment procéder en ligne de commande sous Linux. Si vous utilisez Globus Connect Personal en ligne de commande sous Linux, voyez [cette foire aux questions](https://docs.globus.org/faq/globus-connect-endpoints/#how_do_i_configure_accessible_directories_on_globus_connect_personal_for_linux) pour connaître les chemins partagés et leurs permissions.

#### Pour installer Globus Connect Personal
[Connectez-vous au portail Globus de l'Alliance](https://globus.alliancecan.ca/collections?scope=administered-by-me), si ce n'est pas déjà fait.

1.  Dans la fenêtre *Gestionnaire de fichiers*, cliquez sur l'icône *Collections* dans la barre de gauche.
2.  Cliquez sur le bouton *+ Obtenir Globus Connect Personal* à droite, dans le haut de la fenêtre.
3.  Cliquez sur le lien de téléchargement pour votre système d'exploitation. Pour d'autres systèmes d'exploitation, cliquez sur *Afficher les autres systèmes d'exploitation pris en charge*.
4.  Installez Globus Connect Personal.
5.  Vous devriez maintenant avoir accès par Globus au point de chute. Le nom complet est `[votre nom d'utilisateur]#[nom que vous donnez à la configuration]` par exemple, `smith#PosteDeTravail`.

#### Pour lancer Globus Connect Personal
La procédure ci-dessus doit être suivie une fois seulement pour configurer le point de chute. Par la suite, pour effectuer des transferts de fichiers, assurez-vous que Globus Connect Personal est en opération, c'est-à-dire lancez l'application et vérifiez que le point de chute n'est pas en pause.

!!! warning "Interruption du transfert"
    Le transfert s'arrêtera si l'application Globus Connect Personal est fermée sur votre point de chute au cours d'un transfert en provenance ou à destination de ce point de chute. Pour reprendre le transfert, lancez l'application à nouveau.

#### Transfert entre deux points de chute personnels
Même s'il est possible de créer des points de chute pour plusieurs ordinateurs personnels, le transfert entre deux points de chute personnels ne se fait pas par défaut. Pour ce type de transfert, contactez [globus@tech.alliancecan.ca](mailto:globus@tech.alliancecan.ca) pour créer un compte Globus Plus.

Pour plus d'information, consultez [les pages d'aide de Globus](https://docs.globus.org/how-to/), en particulier :
*   [Globus Connect Personal pour macOS](https://docs.globus.org/how-to/globus-connect-personal-mac)
*   [Globus Connect Personal pour Windows](https://docs.globus.org/how-to/globus-connect-personal-windows)
*   [Globus Connect Personal pour Linux](https://docs.globus.org/how-to/globus-connect-personal-linux)

## Partage de fichiers avec Globus
**Le partage Globus** facilite la collaboration entre collègues. La fonction de partage permet d'accéder aux fichiers enregistrés sur un de nos systèmes, même si l'autre utilisateur n'a pas de compte sur ce système. Les fichiers peuvent être partagés par quiconque possède un compte Globus, peu importe où cette personne se trouve. Voir [Comment partager des données à l'aide de Globus](https://docs.globus.org/how-to/share-files/).

### Création d’une collection partagée
#### Étape 1 - Préparation du répertoire à partager
Dans le tableau suivant, vérifiez si le système qui héberge les fichiers peut autoriser le partage.

| Système                       | Partage                                                                                 |
| :---------------------------- | :-------------------------------------------------------------------------------------- |
| [Trillium](../clusters/trillium.md)       | non                                                                                     |
| [Grappes d'usage général](../clusters/national_systems.md#grappes-de-calcul) | dans <ul><li>`/home`, oui (sauf pour Rorqual)</li><li>`/scratch`, non (sauf pour Narval)</li><li>`/project`, sur demande (voir ci-dessous)</li></ul> |

Sur nos [grappes d'usage général](../clusters/national_systems.md#grappes-de-calcul), le partage est disponible pour le répertoire `/home`, sauf pour la grappe Rorqual. Vous pouvez tester la fonction de partage dans votre répertoire `/home`.

Par défaut, le partage sur `/project` n'est pas activé pour empêcher les utilisateurs de partager accidentellement des fichiers d'autres utilisateurs. Pour que le partage soit activé, la chercheuse principale ou le chercheur principal doit écrire à [globus@tech.alliancecan.ca](mailto:globus@tech.alliancecan.ca) et indiquer
*   que le partage par Globus doit être activé,
*   le nom de la grappe,
*   le chemin,
*   la permission (lecture seule ou lecture-écriture).

Nous vous suggérons d'utiliser un chemin dont le nom indique clairement que les fichiers pourraient y être partagés, par exemple

`/project/my-project-id/Sharing`

Une fois le partage activé pour le chemin, vous pourrez créer un nouveau point de chute Globus partagé pour tout sous-répertoire sous ce chemin. Par exemple, vous pourriez créer les sous-répertoires

`/project/my-project-id/Sharing/Subdir-01`

et

`/project/my-project-id/Sharing/Subdir-02`

Créez un *Partage* différent pour chacun et partagez-les avec de différents utilisateurs.

#### Étape 2 - Préparation des données à partager
Si ce n'est pas déjà fait, les données qui seront partagées doivent être copiées ou déplacées dans le chemin sélectionné. La création d'un lien symbolique ne permettra pas d'accéder aux données.

Autrement, vous aurez l'erreur

!!! error
    *The backend responded with an error: You do not have permission to create a shared endpoint on the selected path. The administrator of this endpoint has disabled creation of shared endpoints on the selected path.*

#### Étape 3 - Configuration de la collection partagée
Avec vos identifiants Globus, connectez-vous au [portail Globus de l'Alliance](https://globus.alliancecan.ca). Une fenêtre de transfert sera affichée. Dans le champ *point de chute*, entrez l'identifiant du point de chute que vous voulez partager (par exemple `alliancecan#fir`, `computecanada#graham-globus`, `alliancecan#rorqual`, `alliancecan#trillium_home` etc.) et activez le point de chute si on vous le demande.

Sélectionnez un répertoire que vous voulez partager et cliquez sur le bouton *Partager* à la droite de la liste des répertoires.

Cliquez sur le bouton *Ajouter une collection invitée* dans le coin supérieur droit.

Entrez un nom qui sera facilement reconnaissable. Vous pouvez aussi indiquer l'endroit à partir duquel se fera le partage avec le bouton *Naviguer*.

### Gestion des accès
Après création d'une collection partagée, vous verrez la liste actuelle des accès autorisés, qui ne contiendra que votre compte. Le partage s’avérant peu utile sans une seconde personne, cliquez sur le bouton *Ajouter des permissions -- Partager avec* afin d’ajouter les personnes ou les groupes avec qui vous voulez partager vos données.

Dans le formulaire suivant, le champ *Chemin* sert à définir le partage; puisque dans la plupart des cas vous voudrez partager la collection au complet, ce champ contiendra `/`. Par contre pour partager le sous-répertoire `/Subdir-01/` avec certaines personnes en particulier, entrez `/Subdir-01/` ou utilisez le bouton *Naviguer* pour le sélectionner.

On vous demandera ensuite d’indiquer si vous voulez procéder au partage en utilisant une adresse courriel, un nom d’utilisateur ou un groupe.
*   Si vous choisissez le nom d’utilisateur, une fenêtre vous permettra d’effectuer une recherche par nom propre ou par nom d’utilisateur Globus.
    *   L’adresse courriel est un bon choix si vous ignorez le nom d’utilisateur employé par la personne concernée sur Globus. Elle vous permettra également de partager les données avec des personnes qui ne possèdent pas de compte Globus, même si elles devront en créer un pour accéder aux fichiers partagés.
    *   Cette solution est idéale pour ceux qui possèdent déjà un compte Globus, car ces derniers n’auront rien à faire pour participer au partage. Saisissez le nom de la personne ou le nom d’utilisateur Globus (si vous le connaissez), choisissez le nom correspondant dans la liste puis cliquez sur *Utiliser la sélection*.
*   Le choix *groupe* permet de partager le fichier simultanément avec plusieurs personnes. Il est possible d’effectuer une recherche d’après le nom du groupe ou son Identifiant universel unique UUID. Le nom d’un groupe pouvant être ambigu, assurez-vous que le partage s’effectue bien avec le groupe désiré. On évitera ce problème en employant l’UUID du groupe, indiqué à la page *Groupes* (voir la partie Groupes).

Pour accorder la permission de lecture, cliquez sur la case *écriture* pour le groupe ou l'utilisateur. Prenez note qu'il n'est pas possible de retirer l'accès en lecture. Quand le formulaire est complet, cliquez sur le bouton *Ajouter la permission*. Il est aussi possible d'ajouter ou de supprimer l'accès en écriture en cliquant dans la case *ÉCRIRE*.

Pour supprimer un utilisateur ou un groupe de la liste de partage, il suffit de cliquer sur le `x` au bout de la ligne correspondante.

### Suppression d’une collection partagée
Lorsque vous n’en aurez plus besoin, vous pouvez supprimer la collection partagée. Pour ce faire,
*   Cliquez sur *Collections* à la gauche de l'écran, cliquez ensuite sur [l'onglet Partageables par vous](https://globus.alliancecan.ca/collections?scope=shared-by-me) et ensuite sur le titre de la collection à supprimer.
*   Cliquez sur le bouton *Supprimer le point de chute* à la droite de l'écran.
*   Confirmez en cliquant sur le bouton.

La collection est maintenant supprimée. Ceci ne supprime pas vos fichiers ni ceux que d'autres pourraient avoir téléversés.

### Sécurité
!!! warning "Considérations de sécurité"
    Partager des fichiers suppose un certain risque. En autorisant le partage, vous permettez à d’autres de consulter des fichiers que vous étiez seul à contrôler jusque là. Bien que non exhaustive, la liste ci-dessous énumère certains éléments à prendre en considération avant de procéder à un partage.

    *   Si vous n’en êtes pas le propriétaire, assurez-vous que vous avez le droit de partager les fichiers.
    *   Assurez-vous que vous ne partagez les fichiers qu’avec les bonnes personnes. Vérifiez si la personne que vous ajoutez à la liste est bien celle que vous pensez; certains noms peuvent se ressembler. Rappelez-vous que les noms d’utilisateur Globus n’ont aucun lien avec ceux de l'Alliance. Nous préconisons la méthode de partage reposant sur l’adresse courriel, à moins que vous ne connaissiez le nom exact du compte.
    *   Si le partage s’effectue avec un groupe sur lequel vous n’exercez aucun contrôle, assurez-vous que la personne qui dirige le groupe est digne de confiance, car des personnes non autorisées à consulter vos données pourraient s’y ajouter.
    *   Si vous accordez le droit de modifier les données, conservez une copie de sauvegarde des fichiers importants ailleurs que sur le point de chute partagé, car il se pourrait que des utilisateurs du point de chute partagé suppriment ou modifient les fichiers, ou en fassent tout ce que vous pourriez en faire personnellement.
    *   Nous recommandons vivement que le partage se limite à un répertoire secondaire et ne s’applique pas au répertoire du plus haut niveau.

## Groupes Globus
Les groupes Globus sont un moyen facile de gérer les permissions pour le partage avec plusieurs utilisateurs. Quand vous créez un groupe, vous pouvez l'utiliser à partir de l'interface de partage pour contrôler l'accès des utilisateurs.

### Création d’un groupe
Cliquez sur [le bouton Groupes](https://globus.alliancecan.ca/groups) dans la barre de gauche. Cliquez sur le bouton *Créer un nouveau groupe* dans le coin supérieur droit. Ceci affiche la fenêtre *Créer un nouveau groupe*.
*   Entrez le nom du groupe dans le champ *Nom du groupe*.
*   Entrez la description du groupe dans le champ *Description du groupe*.
*   Indiquez si le groupe sera visible uniquement aux yeux de ses membres (groupe privé) ou si tous les utilisateurs de Globus pourront le voir.
*   Cliquez sur *Créer le groupe* pour ajouter le groupe.

### Invitations
Après avoir créé le groupe, vous pouvez y ajouter des utilisateurs en sélectionnant *Inviter des utilisateurs* puis en ajoutant leur adresse courriel (méthode privilégiée) ou en cherchant leur nom d’utilisateur. Après avoir choisi les utilisateurs qui sont conviés à se joindre au groupe, cliquez sur le bouton *Ajouter* afin qu’ils reçoivent un message les invitant à se joindre. Lorsqu’ils auront accepté l’invitation, leur nom figurera dans le groupe.

### Permissions
Cliquez sur un nom d'utilisateur pour modifier son rôle ou son statut. Les rôles confèrent les permissions *Administrateur* (toutes les permissions), *Gestionnaire* (modifier les rôles) et *Membre* (aucune permission de gestion). Cliquez sur *Enregistrer*.

## Interface de ligne de commande (CLI)
### Installation
L'interface de ligne de commande Globus est un module Python qui s'installe avec pip. Voici la procédure d'installation sur une de nos grappes :
1.  Créez un environnement virtuel pour y installer l'interface (voir [Créer et utiliser un environnement virtuel](../software/python.md)).
    ```bash
    virtualenv $HOME/.globus-cli-virtualenv
    ```
2.  Activez l'environnement virtuel.
    ```bash
    source $HOME/.globus-cli-virtualenv/bin/activate
    ```
3.  Installez l'interface (voir [Installer des modules](../software/python.md)).
    ```bash
    pip install globus-cli
    ```
4.  Désactivez l'environnement virtuel.
    ```bash
    deactivate
    ```
5.  Pour ne pas avoir à charger l'environnement virtuel à chaque utilisation de Globus, modifiez le chemin.
    ```bash
    export PATH=$PATH:$HOME/.globus-cli-virtualenv/bin
    echo 'export PATH=$PATH:$HOME/.globus-cli-virtualenv/bin'>>$HOME/.bashrc
    ```

### Utilisation
*   Consultez la page Globus [Interface de ligne de commande (CLI)](https://docs.globus.org/cli/).

### Scripts
*   Pour des renseignements sur l'API Python, consultez [SDK Globus pour Python](https://globus-sdk-python.readthedocs.io/en/stable/).

## Machines virtuelles dans les nuages Arbutus, Fir et Nibi
Les points de chute Globus existent pour les grappes (Fir, Nibi, Rorqual, Trillium, etc.), mais pas pour les machines virtuelles infonuagiques. Il nous est impossible de créer un point de chute particulier parce qu'il n'y a pas d'espace de stockage réservé à chaque machine virtuelle.

Si vous avez besoin d'un point de chute pour votre machine virtuelle et que vous n'avez pas d'autre mécanisme de transfert, vous pouvez utiliser Globus Connect Personal ou Globus Connect Server.

### Globus Connect Personal
Globus Connect Personal est plus facile à installer, à gérer et à passer le pare-feu, mais est conçu pour être installé sur les ordinateurs personnels.

*   [Installation pour Windows](https://docs.globus.org/how-to/globus-connect-personal-windows/)
*   [Installation pour Linux](https://docs.globus.org/how-to/globus-connect-personal-linux/)

### Globus Connect Server
Globus Connect Server est conçu pour des environnements en ligne de commande (sans interface graphique) et comporte certaines fonctionnalités que vous n'utiliserez probablement pas, par exemple la possibilité d'ajouter plusieurs serveurs à un point de chute. Quelques ports doivent être ouverts pour permettre les transferts (voir [https://docs.globus.org/globus-connect-server/v5/#open-tcp-ports_section](https://docs.globus.org/globus-connect-server/v5/#open-tcp-ports_section)).

## Stockage objet sur Arbutus
**Les instructions ci-dessous sont valides pour le stockage objet avec la configuration d'avant le renouvellement de l'infrastructure (''Legacy Arbutus'').** Vous devez avoir une allocation de stockage objet pour un projet sur un nuage. La procédure suivante se fait une seule fois.
Vous devez d'abord générer l'identifiant (ID d'accès) et la clé secrète avec un [client de ligne de commande OpenStack](../cloud/openstack_command_line_clients.md).
1.  Importez vos identifiants avec `source <nom-du-projet>-openrc.sh`.
2.  Créez la clé d'accès et la clé secrète avec `openstack ec2 credentials create`.
3.  Connectez-vous au [portail Globus](#) avec [https://www.globus.org/](https://www.globus.org/).
4.  Dans la fenêtre *Gestionnaire de fichiers*, entrez ou sélectionnez *Conteneurs S3 d'Arbutus*.
5.  Cliquez sur *Continuer* pour consentir à l'accès aux données.
6.  Cliquez sur *Autoriser*.
7.  Cliquez sur *Continuer*. Dans le champ *ID de clé d'accès AWS IAM*, entrez le code d'accès généré par `openstack ec2 credentials create`; dans le champ *Clé secrète AWS IAM*, entrez la clé secrète.
8.  Cliquez sur *Continuer* pour terminer la configuration.

## Soutien technique et renseignements additionnels
Pour en apprendre davantage sur comment nous utilisons Globus ou si vous avez besoin de soutien technique pour ce service, écrivez à [globus@tech.alliancecan.ca](mailto:globus@tech.alliancecan.ca) en incluant les renseignements suivants :

*   nom
*   identifiant CCRI (identifiant de rôle Compute Canada)
*   établissement
*   demande ou problème; n'oubliez pas de mentionner les sites de provenance et de destination pour votre transfert