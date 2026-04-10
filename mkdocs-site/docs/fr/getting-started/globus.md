---
title: "Globus/fr"
tags:
  - connecting

keywords:
  []
---

[Globus](https://www.globus.org/) est un service qui permet le transfert de fichiers de façon rapide, fiable et sécuritaire. Conçue expressément pour les besoins de la recherche, l'interface graphique de Globus comporte des fonctions de suivi en arrière-plan qui automatisent la gestion des transferts de fichiers entre deux supports, qu'il s'agisse de nos grappes ou d'un autre site, d'une grappe localisée sur un campus, d'un serveur de laboratoire, d'un microordinateur ou d'un ordinateur portatif.

Globus utilise le protocole de transfert GridFTP, mais vous permet d'éviter les tâches complexes et laborieuses qui s’y associent ainsi que d’autres aspects liés au déplacement des données. Le service améliore la performance des protocoles GridFTP, rsync, scp et sftp par le réglage automatique des paramètres de transfert, le redémarrage automatique lorsqu’il y a interruption du transfert et la vérification de l’intégrité des fichiers.

Vous pouvez accéder au service par [le site web de Globus](https://www.globus.org/) ou par notre portail Globus sur  [https://globus.alliancecan.ca/](https://globus.alliancecan.ca/).

## Utilisation 
Rendez-vous sur [le portail Globus de l'Alliance](https://globus.alliancecan.ca/). Sélectionnez <i>Alliance de recherche numérique du Canada</i> ou <i>Digital Research Alliance of Canada</i> (<b>et non <i>Digital Research Alliance of Canada - Staff</i></b>) dans la liste déroulante et cliquez sur <i>Continuer</i>.  Entrez les informations d'identification pour votre compte CCDB.  Ceci vous conduit au portail web de Globus.

[400px|thumb|none| Page d'accueil du portail Globus de l'Alliance (cliquez pour agrandir)](file:globus-login-organization-fr.png.md)

[400px|thumb|none| Authentification Globus pour l'Alliance (cliquez pour agrandir.)](file:drac-shibboleth-login-fr.png.md)

<span id="To_start_a_transfer"></span>
=== Lancer un transfert === 

Les transferts de données se font entre collections (<i>points de chute</i> dans les versions précédentes). Des collections sont déjà définies pour la plupart de nos systèmes. Pour transférer des fichiers en provenance ou à destination de votre ordinateur, vous devez créer une collection. Une fois que cette étape quelque peu exigeante est accomplie, il ne restera qu'à vous assurer que l'application Globus Connect Personal est en opération sur votre ordinateur pour effectuer un transfert. Voir la section [<i>Ordinateurs personnels</i> ci-dessous](#ordinateurs-personnels.md).

Si la page [*File Manager* du portail Globus](https://globus.alliancecan.ca/file-manager) n'est pas affichée (voir l'image), sélectionnez-la à partir de la barre de gauche.

[400px|thumb|none| File Manager (cliquez pour agrandir)](file:globus-file-manager.png.md)

Trois boutons <i>Panels</i> se trouvent à droite dans le haut de la page; pour voir ensemble deux collections, cliquez sur le deuxième bouton.

Pour trouver une collection, cliquez sur <i>Search</i> et entrez le nom de la collection. 

[none|thumb|400x400px| Sélectionner une collection (cliquez pour agrandir)](file:globus-select-collection-rorqual.png.md)

Pour sélectionner une collection, vous pouvez commencer à entrer son nom. Par exemple, pour transférer des données en provenance ou à destination de Rorqual, entrez <i>rorqual</i>, attendez deux secondes et sélectionnez <`alliancecan#rorqual` dans la liste affichée. 

Toutes nos grappes ont une collection Globus dont le nom se trouve dans le haut de chacune des pages pour la grappe en particulier.

{| class="wikitable"
|-
! Usage général !! Pour les tâches massivement parallèles !! Pour l'IA
|-
|
* [Fir](fir-fr.md)
* [Narval](narval.md)
* [Nibi](nibi-fr.md)
* [Rorqual](rorqual.md)
|
* [Trillium](trillium-fr.md)
|
* [Killarney](killarney-fr.md)
* [TamIA](tamia.md)
* [Vulcan](vulcan-fr.md)
|}

Dépendant du site où se trouve la collection, vous pourriez devoir vous authentifier. Par exemple, si vous activez une collection qui se trouve sur Nibi, vous devrez entrer votre identifiant et votre mot de passe. L'authentification d'une de nos collections reste habituellement valide pour une semaine alors que celle des collections personnelles n'a pas d'échéance.

Faites une recherche pour sélectionner une deuxième collection et authentifiez-vous si requis.

Quand une collection est active, une liste des répertoires et des fichiers est affichée; vous pouvez double-cliquer sur les répertoires et utiliser le bouton pour naviguer dans la structure. Pour sélectionner un répertoire ou un fichier que vous voulez transférer, cliquez sur son nom; pour une sélection multiple, utilisez Ctrl + clic. Cliquez ensuite sur un des gros boutons bleus avec des flèches blanches pour lancer le transfert. Ceci crée une tâche avec un identifiant unique et le transfert commence immédiatement; vous recevrez un courriel quand le transfert sera terminé. Pour suivre le déroulement et voir les détails sur le transfert, cliquez sur [le bouton <i>Activity</i>](https://globus.alliancecan.ca/activity) dans la barre de gauche.

[400px|thumb|none| Lancer un transfert. Remarquez le fichier mis en évidence dans le volet de gauche (cliquez pour agrandir)](file:globus-initiate-transfer.png.md)

Voir aussi [How To Log In and Transfer Files with Globus](https://docs.globus.org/how-to/get-started/) sur le site web Globus.org.

=== Options === 

Plusieurs autres options se trouvent dans la zone <i>Transfer & Sync Options</i> entre les deux boutons <i>Start</i> du centre. Vous pouvez ici demander à Globus de
* synchroniser, pour transférer de nouveaux fichiers ou des fichiers modifiés,
* supprimer des fichiers à la destination qui sont inexistants à la source,
* conserver les renseignements quant au moment des modifications de fichiers,
* vérifier l'intégrité des données après un transfert (option sélectionnée par défaut),
* chiffrer le transfert.
Prenez note que la fonction de chiffrement diminue de beaucoup la performance du transfert et ne devrait être utilisée que pour des données sensibles.

<span id="Personal_computers"></span>
### Ordinateurs personnels 

Globus fournit un client pour utilisation avec un microordinateur sous Windows, macOS X ou Linux; voyez [Globus Connect Personal](https://www.globus.org/globus-connect-personal).

La page [Globus Connect Personal](https://www.globus.org/globus-connect-personal) contient des liens sur comment faire la configuration pour les différents systèmes d'exploitation, incluant comment procéder en ligne de commande sous Linux. Si vous utilisez Globus Connect Personal en ligne de commande sous Linux, voyez [cette foire aux questions](https://docs.globus.org/faq/globus-connect-endpoints/#how_do_i_configure_accessible_directories_on_globus_connect_personal_for_linux) pour connaître les chemins partagés et leurs permissions.

<span id="To_install_Globus_Connect_Personal"></span>
==== Pour installer Globus Connect Personal ==== 

[400px|thumb|none| Trouver le bouton pour l'installation (cliquez pour agrandir)](file:getglobusconnectpersonal.png.md)

[Connectez-vous au portail Globus de l'Alliance](https://globus.alliancecan.ca/collections?scope=administered-by-me), si ce n'est pas déjà fait.

# Dans la fenêtre <i>File Manager</i>, cliquez sur l'icône  <i>Collections</i> dans la barre de gauche.
# Cliquez sur le bouton <i>+ Get Globus Connect Personal</i> à droite, dans le haut de la fenêtre.
# Cliquez sur le lien de téléchargement pour votre système d'exploitation. Pour d'autres systèmes d'exploitation, cliquez sur <i>Show me other supported operating systems</i>.
# Installez Globus Connect Personal.
# Vous devriez maintenant avoir accès par Globus au point de chute. Le nom complet est [your username]#[name you give setup] par exemple, smith#WorkPC.

<span id="To_run_Globus_Connect_Personal"></span>
====Pour lancer Globus Connect Personal==== 

La procédure ci-dessus doit être suivie une fois seulement pour configurer le point de chute. Par la suite, pour effectuer des transferts de fichiers, assurez-vous que *Globus Connect Personal* est en opération, c'est-à-dire lancez l'application et vérifiez que le point de chute n'est pas en pause.

[400px|thumb|none| Globus Connect Personal pour un point de chute personnel](file:gcp-applet.png.md)

Remarque : Le transfert s'arrêtera si l'application Globus Connect Personal est fermée sur votre point de chute au cours d'un transfert en provenance ou à destination de ce point de chute. Pour reprendre le transfert, lancez l'application à nouveau.

<span id="Transfer_between_two_personal_endpoints"></span>
#### Transfert entre deux points de chute personnels

Même s'il est possible de créer des points de chute pour plusieurs ordinateurs personnels, le transfert entre deux points de chute personnels ne se fait pas par défaut. Pour ce type de transfert, contactez  
[mailto:globus@tech.alliancecan.ca globus@tech.alliancecan.ca] pour créer un compte Globus Plus.

Pour plus d'information, consultez [les pages d'aide de Globus](https://docs.globus.org/how-to/), en particulier :
* [Globus Connect Personal pour Mac OS X](https://docs.globus.org/how-to/globus-connect-personal-mac)
* [Globus Connect Personal pour Windows](https://docs.globus.org/how-to/globus-connect-personal-windows)
* [Globus Connect Personal pour Linux](https://docs.globus.org/how-to/globus-connect-personal-linux)

<span id="Globus_sharing"></span>
## Partage de fichiers avec Globus

<b>Globus sharing</b> facilite la collaboration entre collègues. La fonction de partage permet d'accéder aux fichiers enregistrés sur un de nos systèmes, même si l'autre utilisateur n'a pas de compte sur ce système. Les fichiers peuvent être partagés par quiconque possède un compte Globus, peu importe où cette personne se trouve.  Voir [How To Share Data Using Globus](https://docs.globus.org/how-to/share-files/).

<span id="Creating_a_shared_collection"></span>
### Création d’une collection partagée

<span id="Step_1_-_Prepare_a_directory_to_be_shared"></span>
#### Étape 1 - Préparation du répertoire à partager 

Dans le tableau suivant, vérifiez si le système qui héberge les fichiers peut autoriser le partage.

{| class="wikitable" style="margin: auto;"
|-
! scope="col"| Système
! scope="col"| Partage
|-
| [Trillium](trillium-fr.md)
| non
|-
| [Grappes d'usage général](national_systems-fr#grappes_de_calcul.md)
| dans <ul><li>`/home`, oui (sauf pour Rorqual)</li><li>`/scratch`, non (sauf pour Narval)</li><li>`/project`, sur demande (voir ci-dessous)</li></ul>
|}

Sur nos [grappes d'usage général](national_systems-fr#grappes_de_calcul.md), le partage est disponible pour le répertoire /home, sauf pour la grappe Rorqual. Vous pouvez tester la fonction de partage dans votre répertoire /home.

Par défaut, le partage sur /project n'est pas activé pour empêcher les utilisateurs de partager accidentellement des fichiers d'autres utilisateurs. Pour que le partage soit activé, la chercheuse principale ou le chercheur principal doit écrire à [mailto:globus@tech.alliancecan.ca globus@tech.alliancecan.ca] et indiquer </b>

* que le partage par Globus doit être activé,
* le nom de la grappe,
* le chemin,
* la permission (lecture seule ou lecture-écriture).

Nous vous suggérons d'utiliser un chemin dont le nom indique clairement que les fichiers pourraient y être partagés, par exemple

`/project/my-project-id/Sharing`

Une fois le partage activé pour le chemin, vous pourrez créer un nouveau point de chute Globus partagé pour tout sous-répertoire sous ce chemin. Par exemple, vous pourriez créer les sous-répertoires

`/project/my-project-id/Sharing/Subdir-01`

et

`/project/my-project-id/Sharing/Subdir-02`

Créez un *Share* différent pour chacun et partagez-les avec de différents utilisateurs.

<span id="Step_2_-_Prepare_the_data_to_be_shared"></span>
#### Étape 2 - Préparation des données à partager 

Si ce n'est pas déjà fait, les données qui seront partagées doivent être copiées ou déplacées dans le chemin sélectionné. La création d'un lien symbolique ne permettra pas d'accéder aux données.

Autrement, vous aurez l'erreur 

:: <i>The backend responded with an error: You do not have permission to create a shared endpoint on the selected path. The administrator of this endpoint has disabled creation of shared endpoints on the selected path.</i>

<span id="Step_3_-_Configure_a_shared_collection_on_Globus"></span>
#### Étape 3 - Configuration de la collection partagée 

Avec vos identifiants Globus, connectez-vous au [portail Globus de l'Alliance](https://globus.alliancecan.ca). Une fenêtre de transfert sera affichée. Dans le champ <i>endpoint</i>, entrez l'identifiant du point de chute que vous voulez partager (par exemple alliancecan#fir, computecanada#graham-globus, alliancecan#rorqual, alliancecan#trillium_home etc.) et activez le point de chute si on vous le demande.

[thumbnail|Option <i>Share</i> (cliquez pour agrandir)](file:globus-sharedendpoint1-1024x607.png.md)
Sélectionnez un répertoire que vous voulez partager et cliquez sur le bouton <i>Share</i> à la droite de la liste des répertoires.
<br clear=all>

[thumbnail|Bouton <i>Add a Guest Collection</i> (cliquez pour agrandir)](file:globus-sharedendpoint2.png.md)
Cliquez sur le bouton <i>Add a Guest Collection</i> dans le coin supérieur droit. 
<br clear=all>

[thumbnail|Collection partagée (cliquez pour agrandir)](file:globus-sharedendpoint3-1024x430.png.md)
Entrez un nom qui sera facilement reconnaissable. Vous pouvez aussi indiquer l'endroit à partir duquel se fera le partage avec le bouton <i>Browse</i>.	
<br clear=all>

### Gestion des accès
[thumbnail|Gestion des permissions pour les collections partagées (cliquez pour agrandir)](file:globus-managingaccess-1024x745-changed.png.md)
Après création d'une collection partagée, vous verrez la liste actuelle des accès autorisés, qui ne contiendra que votre compte. Le partage s’avérant peu utile sans une seconde personne, cliquez sur le bouton <i>Add Permissions -- Share With</i> afin d’ajouter les personnes ou les groupes avec qui vous voulez partager vos données.
<br clear="all">

[thumb|Envoi d'une invitation de partage (cliquez pour agrandir)](file:globus-add-permissions.png.md)

Dans le formulaire suivant, le champ <i>Path</i> sert à définir le partage; puisque dans la plupart des cas vous voudrez partager la collection au complet, ce champ contiendra `/`. Par contre pour partager le sous-répertoire <i>Subdir-01</i> avec certaines personnes en particulier, entrez `/Subdir-01/` ou utilisez le bouton <i>Browse</i> pour le sélectionner.

On vous demandera ensuite d’indiquer si vous voulez procéder au partage en utilisant une adresse courriel, un nom d’utilisateur ou un groupe.
*Si vous choisissez le nom d’utilisateur, une fenêtre vous permettra d’effectuer une recherche par nom propre ou par nom d’utilisateur Globus.
**L’adresse courriel est un bon choix si vous ignorez le nom d’utilisateur employé par la personne concernée sur Globus. Elle vous permettra également de partager les données avec des personnes qui ne possèdent pas de compte Globus, même si elles devront en créer un pour accéder aux fichiers partagés.
**Cette solution est idéale pour ceux qui possèdent déjà un compte Globus, car ces derniers n’auront rien à faire pour participer au partage. Saisissez le nom de la personne ou le nom d’utilisateur Globus (si vous le connaissez), choisissez le nom correspondant dans la liste puis cliquez sur <i>Use Selected</i>.
*Le choix <i>group</i> permet de partager le fichier simultanément avec plusieurs personnes. Il est possible d’effectuer une recherche d’après le nom du groupe ou son Identifiant universel unique UUID. Le nom d’un groupe pouvant être ambigu, assurez-vous que le partage s’effectue bien avec le groupe désiré. On évitera ce problème en employant l’UUID du groupe, indiqué à la page <i>Groups</i> (voir la partie Groupes).

Pour accorder la permission de lecture, cliquez sur la case <i>write</i> pour le groupe ou l'utilisateur. Prenez note qu'il n'est pas possible de retirer l'accès en lecture. Quand le formulaire est complet, cliquez sur le bouton <i>Add Permission</i>. Il est aussi possible d'ajouter ou de supprimer l'accès en écriture  en cliquant dans la case <i>WRITE</i>.

Pour supprimer un utilisateur ou un groupe de la liste de partage, il suffit de cliquer sur le <i>x</i> au bout de la ligne correspondante.

### Suppression d’une collection partagée
[thumbnail|Supprimer une collection partagée (cliquez pour agrandir)](file:globus-removingsharedendpoint-1024x322.png.md)
Lorsque vous n’en aurez plus besoin, vous pouvez supprimer la collection partagée.  Pour ce faire,

*Cliquez sur <i>Collections</i> à la gauche de l'écran, cliquez ensuite sur [<i>Shareable by You</i> tab](https://globus.alliancecan.ca/collections?scope=shared-by-me) et ensuite sur le titre de la collection à supprimer.
*Cliquez sur le bouton <i>Delete Endpoint</i> à la droite de l'écran.
*Confirmez en cliquant sur le bouton rouge.

La collection est maintenant supprimée. Ceci ne supprime pas vos fichiers ni ceux que d'autres pourraient avoir téléversés.

<span id="Sharing_security"></span>
### Sécurité

Partager des fichiers suppose un certain risque. En autorisant le partage, vous permettez à d’autres de consulter des fichiers que vous étiez seul à contrôler jusque là. Bien que non exhaustive, la liste ci-dessous énumère certains éléments à prendre en considération avant de procéder à un partage.

*Si vous n’en êtes pas le propriétaire, assurez-vous que vous avez le droit de partager les fichiers.
*Assurez-vous que vous ne partagez les fichiers qu’avec les bonnes personnes. Vérifiez si la personne que vous ajoutez à la liste est bien celle que vous pensez; certains noms peuvent se ressembler. Rappelez-vous que les noms d’utilisateur Globus n’ont aucun lien avec ceux de l'Alliance. Nous préconisons la méthode de partage reposant sur l’adresse courriel, à moins que vous ne connaissiez le nom exact du compte.
*Si le partage s’effectue avec un groupe sur lequel vous n’exercez aucun contrôle, assurez-vous que la personne qui dirige le groupe est digne de confiance, car des personnes non autorisées à consulter vos données pourraient s’y ajouter.
*Si vous accordez le droit de modifier les données, conservez une copie de sauvegarde des fichiers importants ailleurs que sur le point de chute partagé, car il se pourrait que des utilisateurs du point de chute partagé suppriment ou modifient les fichiers, ou en fassent tout ce que vous pourriez en faire personnellement.
*Nous recommandons vivement que le partage se limite à un répertoire secondaire et ne s’applique pas au répertoire du plus haut niveau.

## Groupes Globus 
Les groupes Globus sont un moyen facile de gérer les permissions pour le partage avec plusieurs utilisateurs. Quand vous créez un groupe, vous pouvez l'utiliser à partir de l'interface de partage pour contrôler l'accès des utilisateurs. 

### Création d’un groupe
Cliquez sur [le bouton <i>Groups</i>](https://globus.alliancecan.ca/groups) dans la barre de gauche. Cliquez sur le bouton <i>Create New Group</i> dans le coin supérieur droit. Ceci affiche la fenêtre <i>Create New Group</i>.
[thumbnail|Création d'un groupe Globus (cliquez pour agrandir)](file:globus-creatingnewgroup-1024x717.png.md)
*Entrez le nom du groupe dans le champ <i>Group Name</i>.
*Entrez la description du groupe dans le champ <i>Group Description</i>.
*Indiquez si le groupe sera visible uniquement aux yeux de ses membres (groupe privé) ou si tous les utilisateurs de Globus pourront le voir.
*Cliquez sur <i>Create Group</i> pour ajouter le groupe.

### Invitations
Après avoir créé le groupe, vous pouvez y ajouter des utilisateurs en sélectionnant <i>Invite Users</i> puis en ajoutant leur adresse courriel (méthode privilégiée) ou en cherchant leur nom d’utilisateur. Après avoir choisi les utilisateurs qui sont conviés à se joindre au groupe, cliquez sur le bouton <i>Add</i> afin qu’ils reçoivent un message les invitant à se joindre. Lorsqu’ils auront accepté l’invitation, leur nom figurera dans le groupe.

### Permissions
Cliquez sur un nom d'utilisateur pour modifier son rôle ou son statut. Les rôles confèrent les permissions <i>Admin</i> (toutes les permissions), <i>Manager</i> (modifier les rôles) et <i>Member</i> (aucune permission de gestion). Cliquez sur <i>Save</i>.

## Interface ligne de commande (CLI)
### Installation
L'interface ligne de commande Globus est un module Python qui s'installe avec pip. Voici la procédure d'installation sur une de nos grappes&nbsp;ː
# Créez un environnement virtuel pour y installer l'interface (voir [Créer et utiliser un environnement virtuel](python-fr#créer_et_utiliser_un_environnement_virtuel.md)).<source lang='console>$ virtualenv $HOME/.globus-cli-virtualenv</source>
# Activez l'environnement virtuel. <source lang='console>$ source $HOME/.globus-cli-virtualenv/bin/activate</source>
# Installez l'interface (voir [Installer des modules](python-fr#installer_des_modules.md)).<source lang='console>$ pip install globus-cli</source>
# Désactivez l'environnement virtuel.<source lang='console'>$ deactivate</source>
# Pour ne pas avoir à charger l'environnement virtuel à chaque utilisation de Globus, modifiez le chemin. <source lang='console>$ export PATH=$PATH:$HOME/.globus-cli-virtualenv/bin
$ echo 'export PATH=$PATH:$HOME/.globus-cli-virtualenv/bin'>>$HOME/.bashrc</source>

### Utilisation
* Consultez la page Globus [Command Line Interface (CLI)](https://docs.globus.org/cli/).
### Scripts
* Pour des renseignements sur l'API Python, consultez [Globus SDK for Python](https://globus-sdk-python.readthedocs.io/en/stable/).

## Machines virtuelles dans les nuages Arbutus, Fir et Nibi
Les points de chute Globus existent pour les grappes (Fir, Nibi, Rorqual, Trillium, etc.), mais pas pour les machines virtuelles infonuagiques. Il nous est impossible de créer un point de chute particulier parce qu'il n'y a pas d'espace de stockage réservé à chaque machine virtuelle.

Si vous avez besoin d'un point de chute pour votre machine virtuelle et que vous n'avez pas d'autre mécanisme de transfert, vous pouvez utiliser Globus Connect Personal ou Globus Connect Server.

### Globus Connect Personal 
Globus Connect Personal est plus facile à installer, à gérer et à passer le pare-feu, mais est conçu pour être installé sur les ordinateurs personnels.

* [Installation pour Windows](https://docs.globus.org/how-to/globus-connect-personal-windows/)

* [Installation pour Linux](https://docs.globus.org/how-to/globus-connect-personal-linux/)

### Globus Connect Server 
Globus Connect Server est conçu pour des environnements en ligne de commande (sans interface graphique) et comporte certaines fonctionnalités que vous n'utiliserez probablement pas, par exemple la possibilité d'ajouter plusieurs serveurs à un point de chute. Quelques ports doivent être ouverts pour permettre les transferts (voir https://docs.globus.org/globus-connect-server/v5/#open-tcp-ports_section).

<span id="Object_storage_on_Arbutus"></span>
## Stockage objet sur Arbutus 

<div class="mw-translate-fuzzy">
Pour utiliser le stockage objet sur Arbutus, votre projet infonuagique doit avoir une allocation de stockage. La procédure suivante est faite une seule fois.

Vous devez d'abord générer l'identifiant (<i>access ID</i>) et la clé secrète (<i>secret key</i>) avec un [client ligne de commande OpenStack](openstack-command-line-clients-fr.md).

1. Importez vos identifiants avec <code>source <project name>-openrc.sh</code>.

2. Créez la clé d'accès et la clé secrète avec `openstack ec2 credentials create`. 

3. Connectez-vous au [portail Globus](globus-fr#.md) avec [https://www.globus.org/](https://www.globus.org/).

4. Dans la fenêtre <i>File Manager</i>, entrez ou sélectionnez <i>Arbutus S3 buckets</i>.
 
[400px|thumb|none|alt=Globus Arbutus S3 bucket Endpoint|Collection  Arbutus S3 buckets (cliquer pour agrandir)](file:arbutuss3endpoint.png.md)
5. Cliquez sur <i>Continue</i> pour consentir à l'accès aux données.
 
6. Cliquez sur <i>Allow</i>.
 
7. Cliquez sur <i>Continue</i>. Dans le champ <i>AWS IAM Access Key ID</i>, entrez le code d'accès généré par `openstack ec2 credentials create`; dans le champ <i>AWS IAM Secret Key</i>, entrez la clé secrète. 
[400px|thumb|none|alt=Globus Arbutus S3 bucket S3 Keys|Arbutus S3, code d'accès et clé secrète (cliquer pour agrandir)](file:arbutusobjectstoragebucketkeys.png.md)
8. Cliquez sur <i>Continue</i> pour terminer la configuration.
</div>

==Soutien technique et renseignements additionnels== 
Pour en apprendre davantage sur comment nous utilisons Globus ou si vous avez besoin de soutien technique pour ce service, écrivez à [mailto:globus@tech.alliancecan.ca globus@tech.alliancecan.ca] en incluant les renseignements suivants&nbsp;:

* nom
* identifiant CCRI (Compute Canada Role Identifier)
* établissement
* demande ou problème; n'oubliez pas de mentionner les sites de provenance et de destination pour votre transfert