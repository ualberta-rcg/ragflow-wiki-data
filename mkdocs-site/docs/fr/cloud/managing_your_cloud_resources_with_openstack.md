---
title: "Managing your cloud resources with OpenStack/fr"
tags:
  - cloud

keywords:
  []
---

<i>Page enfant de [Service infonuagique](cloud-fr.md)</i>

Notre service infonuagique utilise la suite logicielle OpenStack pour contrôler les ressources telles que les ordinateurs, l'espace de stockage et le matériel de réseautage. OpenStack permet de créer et de gérer des instances (ou VM pour <i>virtual machines</i>) qui fonctionnent comme des machines distinctes, par émulation. Vous maîtrisez complètement l'environnement de développement, à partir du choix du système d'exploitation jusqu'à l'installation et la configuration des logiciels. OpenStack sert des usages variés, dont l'hébergement de sites web et la création de grappes virtuelles. Vous trouverez des renseignements additionnels sur le [site web OpenStack](http://docs.openstack.org/).

Nous abordons ici plusieurs aspects du travail avec OpenStack en tenant compte que vous avez lu la page [Cloud&nbsp;:&nbsp;Guide de démarrage](cloud-quick-start-fr.md) et que vous connaissez les opérations de base pour lancer une instance et vous y connecter. Vous pouvez travailler à partir du tableau de bord OpenStack (voir les captures d'écran ci-dessous), par un [client en ligne de commande](openstack-command-line-clients-fr.md) ou en utilisant un outil comme [Terraform](terraform-fr.md). 
Cependant, certaines tâches ne s'effectuent qu'en ligne de commande, par exemple [partager une image avec un autre projet](working_with_images-fr#partager_une_image_avec_un_autre_projet.md).

=Tableau de bord=
Dans notre documentation, le tableau de bord (<i>dashboard</i>) est le nom donné à l'interface Web qui gère vos ressources infonuagiques. Le tableau de bord est un sous-projet OpenStack qu'on appelle parfois Horizon. Vous pouvez consulter [la documentation qui décrit le fonctionnement de Horizon](https://docs.openstack.org/horizon/latest/).

=Projets=
Les projets OpenStack groupent les instances et donnent droit à un quota pour la création des instances et des ressources qui y sont associées. Un projet OpenStack est situé dans un nuage particulier. Tous les comptes membres d'un projet possèdent les mêmes permissions et peuvent créer ou supprimer une instance pour ce projet. Pour connaître les projets auxquels vous êtes membre, connectez-vous au tableau de bord OpenStack dans le ou les nuages auxquels vous avez accès; pour la liste des URL, voyez [Ressources infonuagiques](cloud-fr#ressources_infonuagiques.md). Le nom du <b>projet actif</b> est affiché dans le menu déroulant situé à la droite du nom du nuage; si vous êtes membre de plusieurs projets dans le même nuage, ce menu vous permet de sélectionner un autre projet actif.

Selon les ressources qui vous sont allouées, votre projet pourrait être limité à certains [gabarits d'instances](virtual_machine_flavors-fr.md). Par exemple, les allocations de calcul n'ont généralement que des gabarits de type c alors que les allocations persistantes n'ont généralement que des gabarits de type p.

Les chercheuses principales et chercheurs principaux sont considérés comme étant propriétaires des projets et sont les seuls qui peuvent demander la création d'un nouveau projet ou l'ajustement d'un quota. Aussi, le droit d'accès à un projet ne peut être accordé que par une chercheuse principale ou un chercheur principal.

=Volumes=
Pour savoir comment créer et gérer le stockage avec les volumes, voyez [Travailler avec des volumes](working_with_volumes-fr.md).

=Images=
Pour savoir comment créer et gérer les fichiers des images de disques, voyez [Travailler avec des images](working_with_images-fr.md).

= Instances=
Pour savoir comment gérer certaines caractéristiques de vos instances, voyez  [Travailler avec des instances](working_with_vms-fr.md).

=Zones de disponibilité=
La zone de disponibilité indique le groupe de ressources matérielles utilisées pour l'exécution de l'instance. Avec les nuages Béluga et Graham, la seule zone disponible est `nova`. Par contre avec Arbutus, trois zones sont disponibles&nbsp;: <i>Compute</i> pour l'exécution des gabarits de calcul et <i>Persistent_01</i> et <i>Persistent_02</i> pour l'exécution des gabarits persistants (voir [Gabarits d'instances](virtual-machine-flavors-fr.md)). Le fait de disposer de deux zones persistantes peut être utile lorsque par exemple deux instances d'un site web sont situées dans deux zones différentes; ceci fait en sorte que le site demeure disponible en cas de problème dans une des zones.

=Groupes de sécurité=
Un groupe de sécurité est un ensemble de règles de gestion des intrants et extrants des instances. Pour définir les règles, sélectionnez <i>Projet->Réseau->Groupes de sécurité</i>; la page affichée montre la liste des groupes de sécurité qui existent. Si aucun groupe n'est encore défini, seul le groupe de sécurité par défaut paraît dans la liste. 

Pour ajouter une règle à un groupe ou pour la supprimer, cliquez sur le bouton  <i>Gérer les règles</i> correspondant au groupe. Lorsque la description du groupe est affichée, cliquez sur le bouton <i>+ Ajouter une règle</i>, en haut à droite. Pour supprimer une règle, cliquez sur le bouton <i>Supprimer une règle</i> correspondant. 

## Groupe de sécurité par défaut
[400px|thumb| Règles du groupe de sécurité par défaut (cliquez pour agrandir)](file:default_security_group_fr.png.md)
Les règles du <b>groupe de sécurité par défaut</b> permettent à une instance d'accéder à l'internet pour, par exemple, télécharger les mises à jour des systèmes d'exploitation ou pour installer des paquets. Ces règles empêchent les autres ordinateurs d'accéder à l'instance, à l'exception des autres instances qui appartiennent au même groupe de sécurité. Nous vous recommandons de ne pas supprimer ces règles pour éviter que des problèmes ne surviennent à la création d'une nouvelle instance. Les règles sont&nbsp;:
* 2 règles de sortie (<i>egress</i>) pour que l'instance dispose d'un accès illimité à l'extérieur du réseau. Il y a une règle pour IPV4 et une autre pour IPV6;
* 2 règles d'entrée (<i>ingress</i>) pour que toutes les instances qui appartiennent au groupe de sécurité puissent communiquer. Il y a une règle pour IPV4 et une autre pour IPV6.
Il est possible d'ajouter des règles pour vous connecter sans risque à une instance sous Linux pour [SSH](cloud_quick_start-fr#configuration_du_r.c3.a9seau.md) et [RDP (onglet Windows, sous <i>Pare-feu et règles autorisant le protocole RDP</i>)](cloud_quick_start-fr#créer_votre_première_instance.md); voyez la page [Cloud&nbsp;:&nbsp;Guide de démarrage](cloud-quick-start-fr.md).

## Gestion des groupes de sécurité
Plusieurs groupes de sécurité peuvent être définis et une instance peut appartenir à plus d'un groupe. Lorsque vous définissez vos groupes et vos règles, tenez bien compte de ce qui doit être accédé et des personnes qui auront besoin d'y accéder. Tentez de définir un minimum d'adresses IP et de ports dans vos règles de sortie; si par exemple vous utilisez toujours le même ordinateur avec la même adresse IP pour vous connecter à votre instance via SSH, il est logique de permettre l'accès SSH uniquement de cette adresse IP. Pour définir la ou les adresses IP qui peuvent accéder, utilisez la case [CIDR](managing-your-cloud-resources-with-openstack-fr#règles_cidr.md) dans la fenêtre d'ajout de la règle; cet outil web permet de [convertir un ensemble d'adresses IP en règles CIDR](http://www.ipaddressguide.com/cidr). De plus, si vous vous connectez de l'extérieur toujours à la même instance via SSH et que cette connexion vous sert de passerelle vers d'autres instances dans le nuage, il est logique que la règle SSH soit dans un groupe de sécurité distinct et que ce groupe soit associé uniquement à l'instance servant de passerelle. Il faut toutefois vous assurer que vos clés SSH soient configurées pour vous permettre de les utiliser pour plusieurs instances (voir [Clés SSH](ssh-keys-fr.md)). En plus des règles CIDR, d'autres règles de sécurité peuvent s'appliquer dans le cas d'un projet qui utilise les groupes. Par exemple, vous pouvez configurer une règle de sécurité pour une instance d'un projet utilisant une base de données MySQL afin que cette instance puisse être accédée par d'autres instances du groupe de sécurité par défaut.

Les groupes de sécurité auxquels appartient une instance peuvent être définis à deux moments&nbsp;:
* à la création du groupe, par <i>Projet->Calcul->Accès et sécurité</i>, onglet <i>Groupes de sécurité</i>;
* lorsque l'instance est active, par <i>Projet->Calcul->Instances</i>, liste déroulante de la colonne <i>Actions</i>, option <i>Editer les groupes de sécurité</i>.

## Règles CIDR
CIDR (pour <i>Classless Inter-Domain Routing</i>) est un moyen standard pour définir les ensembles d'adresses IP (voir aussi la page Wikipédia [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)).

Un exemple de règle CIDR est `192.168.1.1/24`. Ceci ressemble à une adresse IP normale à laquelle on a ajouté `/24`. Les adresses IP sont composées de quatre nombres entre 0 et 255, de un octet (8 bits) chacun. Dans notre exemple, la terminaison `/24` fait que cette règle comparera les 24 bits de gauche (3 octets) aux autres adresses IP; ainsi, toutes les adresses commençant par `192.168.1` respecteront cette règle. Avec la terminaison `/32`, ce sont les 32 bits de l'adresse IP qui doivent correspondre exactement et avec la terminaison, aucun bit ne doit correspondre et ainsi, toutes les adresses IP respecteront la règle.

=cloudInit=

<b>La première fois que votre instance est lancée,</b> vous pouvez la personnaliser avec cloudInit. Ceci peut se faire
* via l'interface ligne de commande d'OpenStack, ou
* en collant votre script cloudInit dans le champ <i>Script de personnalisation</i> du tableau de bord OpenStack (<i>Projet-->Compute-->Instances--></i> bouton <i>Lancer une instance</i>, option <i>Configuration</i>). 

## Ajouter des utilisateurs avec cloud-init à la création de l'instance
[400px|thumb| Ajout de plusieurs utilisateurs avec cloud-init (cliquez pour agrandir)](file:vm-multi-user-cloud-init.png.md)
Le script cloud-init suivant ajoute les utilisateurs `gretzky` avec les permissions sudo et `lemieux` sans les permissions sudo.

  #cloud-config
 users:
   - name: gretzky
     shell: /bin/bash
     sudo: ALL=(ALL) NOPASSWD:ALL
     ssh_authorized_keys:
       - <Gretzky's public key goes here>
   - name: lemieux
     shell: /bin/bash
     ssh_authorized_keys:
       - <Lemieux's public key goes here>

Pour de l'information sur le format YALM utilisé par cloud-init, consultez [YAML Preview](http://www.yaml.org/spec/1.2/spec.html#Preview).

Les espaces sont importantes dans le format YALM; il faut prendre garde de laisser une espace entre le tiret initial et la clé publique. Cette configuration remplace l'utilisateur par défaut qui est ajouté lorsqu'il n'y a pas de script cloud-init; les utilisateurs définis dans le script seront donc les seuls utilisateurs de la nouvelle instance et c'est pourquoi il faut s'assurer qu'au moins  un utilisateur possède les permissions sudo. Pour ajouter d'autres utilisateurs, insérez simplement dans le script d'autres sections `- name: username`.

Pour conserver l'utilisateur par défaut créé par la distribution (utilisateurs `debian, centos, ubuntu,` <i>etc.</i>), utilisez plutôt le script suivant&nbsp;:

  #cloud-config
 users:
   - default
   - name: gretzky
     shell: /bin/bash
     sudo: ALL=(ALL) NOPASSWD:ALL
     ssh_authorized_keys:
       - <Gretzky's public key goes here>
   - name: lemieux
     shell: /bin/bash
     ssh_authorized_keys:
       - <Lemieux's public key goes here>

Une fois l'instance démarrée, examinez le journal des opérations pour vérifier que les clés sont correctement associées aux utilisateurs. Pour consulter le journal, sélectionnez *Projet->Calcul->Instances* et cliquez sur le nom de l'instance. L'onglet *Journal* affiche le journal de la console de l'instance, qui ressemble à ceci&nbsp;:

 ci-info: ++++++++Authorized keys from /home/gretzky/.ssh/authorized_keys for user gretzky++++++++
 ci-info: +---------+-------------------------------------------------+---------+------------------+
 ci-info: | Keytype |                Fingerprint (md5)                | Options |     Comment      |
 ci-info: +---------+-------------------------------------------------+---------+------------------+
 ci-info: | ssh-rsa | ad:a6:35:fc:2a:17:c9:02:cd:59:38:c9:18:dd:15:19 |    -    | rsa-key-20160229 |
 ci-info: +---------+-------------------------------------------------+---------+------------------+
 ci-info: ++++++++++++Authorized keys from /home/lemieux/.ssh/authorized_keys for user lemieux++++++++++++
 ci-info: +---------+-------------------------------------------------+---------+------------------+
 ci-info: | Keytype |                Fingerprint (md5)                | Options |     Comment      |
 ci-info: +---------+-------------------------------------------------+---------+------------------+
 ci-info: | ssh-rsa | ad:a6:35:fc:2a:17:c9:02:cd:59:38:c9:18:dd:15:19 |    -    | rsa-key-20160229 |
 ci-info: +---------+-------------------------------------------------+---------+------------------+

Les utilisateurs peuvent maintenant se connecter à l'instance à l'aide de leur clé privée (voir [Clés SSH](ssh_keys-fr.md)).