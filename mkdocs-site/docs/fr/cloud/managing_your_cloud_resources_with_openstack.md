---
title: "Managing your cloud resources with OpenStack/fr"
slug: "managing_your_cloud_resources_with_openstack"
lang: "fr"

source_wiki_title: "Managing your cloud resources with OpenStack/fr"
source_hash: "c0962c2a6193bca760f1e88302d05f98"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:00:31.596784+00:00"

tags:
  - cloud

keywords:
  - "Cloud"
  - "gabarits persistants"
  - "Journal de la console"
  - "Fingerprint"
  - "clé privée"
  - "Service infonuagique"
  - "instances"
  - "règle de sécurité"
  - "Projet"
  - "instance"
  - "Règles de sécurité"
  - "projet"
  - "Projets"
  - "zones"
  - "Gabarits d'instances"
  - "Compute"
  - "Règles CIDR"
  - "OpenStack"
  - "se connecter à l'instance"
  - "base de données MySQL"
  - "Tableau de bord"
  - "Authorized keys"
  - "disponibilité"
  - "Groupes de sécurité"
  - "Accès réseau"
  - "cloud-init"
  - "utilisateurs"
  - "authorized_keys"
  - "Instances"
  - "groupes de sécurité"
  - "Instance"
  - "Clés SSH"

questions:
  - "Quel est le rôle principal de la suite logicielle OpenStack au sein de ce service infonuagique ?"
  - "Comment les projets OpenStack sont-ils gérés en termes de permissions, de quotas et de rôles des chercheurs principaux ?"
  - "Qu'est-ce qu'une zone de disponibilité et quel est l'avantage d'en utiliser plusieurs pour héberger un service comme un site web ?"
  - "Quelles sont les trois zones disponibles et à quels types d'exécution sont-elles respectivement dédiées ?"
  - "Quel est l'avantage principal de posséder deux zones persistantes distinctes pour héberger un site web ?"
  - "Vers quelle ressource le texte renvoie-t-il pour obtenir plus de détails sur les gabarits d'instances ?"
  - "Qu'est-ce qu'un groupe de sécurité et comment procéder pour y ajouter ou en supprimer des règles via l'interface ?"
  - "Quelles sont les règles appliquées par le groupe de sécurité par défaut et pourquoi est-il fortement recommandé de ne pas les supprimer ?"
  - "Quelles sont les bonnes pratiques de gestion recommandées pour restreindre l'accès à vos instances, notamment via l'utilisation des règles CIDR et des passerelles SSH ?"
  - "Comment fonctionnent les règles CIDR et que signifient les terminaisons telles que /24 ou /32 dans le filtrage des adresses IP ?"
  - "Quelles sont les différentes méthodes permettant d'utiliser cloudInit pour personnaliser une instance lors de son tout premier lancement ?"
  - "Comment doit-on structurer un script cloud-init en format YAML pour ajouter de nouveaux utilisateurs (avec ou sans accès sudo) tout en conservant l'utilisateur par défaut de la distribution ?"
  - "Comment les règles de sécurité permettent-elles de gérer l'accès entre les instances au sein d'un projet utilisant des groupes ?"
  - "Quel exemple concret est mentionné concernant la configuration d'une instance utilisant une base de données MySQL ?"
  - "Quel est le chemin de navigation exact dans l'interface pour définir les groupes de sécurité lors de leur création ?"
  - "Pour quel utilisateur spécifique la clé SSH a-t-elle été ajoutée dans le fichier des clés autorisées ?"
  - "Quelle méthode d'authentification les utilisateurs doivent-ils désormais utiliser pour se connecter à l'instance ?"
  - "Vers quelle page de documentation les utilisateurs sont-ils renvoyés pour obtenir plus d'informations sur cette configuration ?"
  - "Quel est le chemin de navigation exact pour accéder au journal de la console d'une instance ?"
  - "Quel type d'information générale est affiché dans l'onglet \"Journal\" selon le texte ?"
  - "À quel utilisateur et à quel fichier correspondent les clés SSH autorisées montrées dans l'exemple du journal ?"
  - "Pour quel utilisateur spécifique la clé SSH a-t-elle été ajoutée dans le fichier des clés autorisées ?"
  - "Quelle méthode d'authentification les utilisateurs doivent-ils désormais utiliser pour se connecter à l'instance ?"
  - "Vers quelle page de documentation les utilisateurs sont-ils renvoyés pour obtenir plus d'informations sur cette configuration ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Page enfant de [Service infonuagique](cloud.md)*

Notre service infonuagique utilise la suite logicielle OpenStack pour contrôler les ressources telles que les ordinateurs, l'espace de stockage et le matériel de réseautage. OpenStack permet de créer et de gérer des instances (ou machines virtuelles) qui fonctionnent comme des machines distinctes, par émulation. Vous maîtrisez complètement l'environnement de développement, à partir du choix du système d'exploitation jusqu'à l'installation et la configuration des logiciels. OpenStack sert des usages variés, dont l'hébergement de sites web et la création de grappes virtuelles. Vous trouverez des renseignements additionnels sur le [site web OpenStack](http://docs.openstack.org/).

Nous abordons ici plusieurs aspects du travail avec OpenStack en tenant compte que vous avez lu la page [Cloud : Guide de démarrage](cloud_quick_start.md) et que vous connaissez les opérations de base pour lancer une instance et vous y connecter. Vous pouvez travailler à partir du tableau de bord OpenStack (voir les captures d'écran ci-dessous), par un [client en ligne de commande](openstack_command_line_clients.md) ou en utilisant un outil comme [Terraform](terraform.md).
Cependant, certaines tâches ne s'effectuent qu'en ligne de commande, par exemple [partager une image avec un autre projet](working_with_images.md#partager-une-image-avec-un-autre-projet).

## Tableau de bord
Dans notre documentation, le tableau de bord est le nom donné à l'interface Web qui gère vos ressources infonuagiques. Le tableau de bord est un sous-projet OpenStack qu'on appelle parfois Horizon. Vous pouvez consulter [la documentation qui décrit le fonctionnement de Horizon](https://docs.openstack.org/horizon/latest/).

## Projets
Les projets OpenStack groupent les instances et donnent droit à un quota pour la création des instances et des ressources qui y sont associées. Un projet OpenStack est situé dans un nuage particulier. Tous les comptes membres d'un projet possèdent les mêmes permissions et peuvent créer ou supprimer une instance pour ce projet. Pour connaître les projets auxquels vous êtes membre, connectez-vous au tableau de bord OpenStack dans le ou les nuages auxquels vous avez accès; pour la liste des URL, voyez [Ressources infonuagiques](cloud.md#ressources-infonuagiques). Le nom du **projet actif** est affiché dans le menu déroulant situé à la droite du nom du nuage; si vous êtes membre de plusieurs projets dans le même nuage, ce menu vous permet de sélectionner un autre projet actif.

Selon les ressources qui vous sont allouées, votre projet pourrait être limité à certains [gabarits d'instances](virtual_machine_flavors.md). Par exemple, les allocations de calcul n'ont généralement que des gabarits de type c alors que les allocations persistantes n'ont généralement que des gabarits de type p.

Les chercheuses principales et chercheurs principaux sont considérés comme étant propriétaires des projets et sont les seuls qui peuvent demander la création d'un nouveau projet ou l'ajustement d'un quota. Aussi, le droit d'accès à un projet ne peut être accordé que par une chercheuse principale ou un chercheur principal.

## Volumes
Pour savoir comment créer et gérer le stockage avec les volumes, voyez [Travailler avec des volumes](working_with_volumes.md).

## Images
Pour savoir comment créer et gérer les fichiers des images de disques, voyez [Travailler avec des images](working_with_images.md).

## Instances
Pour savoir comment gérer certaines caractéristiques de vos instances, voyez [Travailler avec des instances](working_with_vms.md).

## Zones de disponibilité
La zone de disponibilité indique le groupe de ressources matérielles utilisées pour l'exécution de l'instance. Avec les nuages Béluga et Graham, la seule zone disponible est `nova`. Par contre avec Arbutus, trois zones sont disponibles : *Calcul* pour l'exécution des gabarits de calcul et *Persistent_01* et *Persistent_02* pour l'exécution des gabarits persistants (voir [Gabarits d'instances](virtual_machine_flavors.md)). Le fait de disposer de deux zones persistantes peut être utile lorsque par exemple deux instances d'un site web sont situées dans deux zones différentes; ceci fait en sorte que le site demeure disponible en cas de problème dans une des zones.

## Groupes de sécurité
Un groupe de sécurité est un ensemble de règles de gestion des intrants et extrants des instances. Pour définir les règles, sélectionnez *Projet*->*Réseau*->*Groupes de sécurité*; la page affichée montre la liste des groupes de sécurité qui existent. Si aucun groupe n'est encore défini, seul le groupe de sécurité par défaut paraît dans la liste.

Pour ajouter une règle à un groupe ou pour la supprimer, cliquez sur le bouton *Gérer les règles* correspondant au groupe. Lorsque la description du groupe est affichée, cliquez sur le bouton *+ Ajouter une règle*, en haut à droite. Pour supprimer une règle, cliquez sur le bouton *Supprimer une règle* correspondant.

### Groupe de sécurité par défaut
Les règles du **groupe de sécurité par défaut** permettent à une instance d'accéder à l'internet pour, par exemple, télécharger les mises à jour des systèmes d'exploitation ou pour installer des paquets. Ces règles empêchent les autres ordinateurs d'accéder à l'instance, à l'exception des autres instances qui appartiennent au même groupe de sécurité. Nous vous recommandons de ne pas supprimer ces règles pour éviter que des problèmes ne surviennent à la création d'une nouvelle instance. Les règles sont :
*   2 règles de sortie pour que l'instance dispose d'un accès illimité à l'extérieur du réseau. Il y a une règle pour IPV4 et une autre pour IPV6;
*   2 règles d'entrée pour que toutes les instances qui appartiennent au groupe de sécurité puissent communiquer. Il y a une règle pour IPV4 et une autre pour IPV6.
Il est possible d'ajouter des règles pour vous connecter sans risque à une instance sous Linux pour [SSH](cloud_quick_start.md#configuration-du-réseau) et [RDP (onglet Windows, sous *Pare-feu et règles autorisant le protocole RDP*)](cloud_quick_start.md#créer-votre-première-instance); voyez la page [Cloud : Guide de démarrage](cloud_quick_start.md).

### Gestion des groupes de sécurité
Plusieurs groupes de sécurité peuvent être définis et une instance peut appartenir à plus d'un groupe. Lorsque vous définissez vos groupes et vos règles, tenez bien compte de ce qui doit être accédé et des personnes qui auront besoin d'y accéder. Tentez de définir un minimum d'adresses IP et de ports dans vos règles de sortie; si par exemple vous utilisez toujours le même ordinateur avec la même adresse IP pour vous connecter à votre instance via SSH, il est logique de permettre l'accès SSH uniquement de cette adresse IP. Pour définir la ou les adresses IP qui peuvent accéder, utilisez la case [CIDR](managing_your_cloud_resources_with_openstack.md#règles-cidr) dans la fenêtre d'ajout de la règle; cet outil web permet de [convertir un ensemble d'adresses IP en règles CIDR](http://www.ipaddressguide.com/cidr). De plus, si vous vous connectez de l'extérieur toujours à la même instance via SSH et que cette connexion vous sert de passerelle vers d'autres instances dans le nuage, il est logique que la règle SSH soit dans un groupe de sécurité distinct et que ce groupe soit associé uniquement à l'instance servant de passerelle. Il faut toutefois vous assurer que vos clés SSH soient configurées pour vous permettre de les utiliser pour plusieurs instances (voir [Clés SSH](../getting-started/ssh_keys.md)). En plus des règles CIDR, d'autres règles de sécurité peuvent s'appliquer dans le cas d'un projet qui utilise les groupes. Par exemple, vous pouvez configurer une règle de sécurité pour une instance d'un projet utilisant une base de données MySQL afin que cette instance puisse être accédée par d'autres instances du groupe de sécurité par défaut.

Les groupes de sécurité auxquels appartient une instance peuvent être définis à deux moments :
*   à la création du groupe, par *Projet*->*Calcul*->*Accès et sécurité*, onglet *Groupes de sécurité*;
*   lorsque l'instance est active, par *Projet*->*Calcul*->*Instances*, liste déroulante de la colonne *Actions*, option *Editer les groupes de sécurité*.

### Règles CIDR
CIDR (pour *Classless Inter-Domain Routing*) est un moyen standard pour définir les ensembles d'adresses IP (voir aussi la page Wikipédia [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)).

Un exemple de règle CIDR est `192.168.1.1/24`. Ceci ressemble à une adresse IP normale à laquelle on a ajouté `/24`. Les adresses IP sont composées de quatre nombres entre 0 et 255, de un octet (8 bits) chacun. Dans notre exemple, la terminaison `/24` fait que cette règle comparera les 24 bits de gauche (3 octets) aux autres adresses IP; ainsi, toutes les adresses commençant par `192.168.1` respecteront cette règle. Avec la terminaison `/32`, ce sont les 32 bits de l'adresse IP qui doivent correspondre exactement et avec la terminaison, aucun bit ne doit correspondre et ainsi, toutes les adresses IP respecteront la règle.

## cloud-init

**La première fois que votre instance est lancée,** vous pouvez la personnaliser avec cloud-init. Ceci peut se faire :
*   via l'interface ligne de commande d'OpenStack, ou
*   en collant votre script cloud-init dans le champ *Script de personnalisation* du tableau de bord OpenStack (*Projet*->*Calcul*->*Instances*-> bouton *Lancer une instance*, option *Configuration*).

### Ajouter des utilisateurs avec cloud-init à la création de l'instance
Le script cloud-init suivant ajoute les utilisateurs `gretzky` avec les permissions sudo et `lemieux` sans les permissions sudo.

```yaml
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
```

Pour de l'information sur le format YAML utilisé par cloud-init, consultez [YAML Preview](http://www.yaml.org/spec/1.2/spec.html#Preview).

Les espaces sont importantes dans le format YAML; il faut prendre garde de laisser une espace entre le tiret initial et la clé publique. Cette configuration remplace l'utilisateur par défaut qui est ajouté lorsqu'il n'y a pas de script cloud-init; les utilisateurs définis dans le script seront donc les seuls utilisateurs de la nouvelle instance et c'est pourquoi il faut s'assurer qu'au moins un utilisateur possède les permissions sudo. Pour ajouter d'autres utilisateurs, insérez simplement dans le script d'autres sections `- name: username`.

Pour conserver l'utilisateur par défaut créé par la distribution (utilisateurs `debian`, `centos`, `ubuntu`, *etc.*), utilisez plutôt le script suivant :

```yaml
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
```

Une fois l'instance démarrée, examinez le journal des opérations pour vérifier que les clés sont correctement associées aux utilisateurs. Pour consulter le journal, sélectionnez *Projet*->*Calcul*->*Instances* et cliquez sur le nom de l'instance. L'onglet *Journal* affiche le journal de la console de l'instance, qui ressemble à ceci :

```text
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
```

Les utilisateurs peuvent maintenant se connecter à l'instance à l'aide de leur clé privée (voir [Clés SSH](../getting-started/ssh_keys.md)).