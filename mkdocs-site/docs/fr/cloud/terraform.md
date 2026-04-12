---
title: "Terraform/fr"
slug: "terraform"
lang: "fr"

source_wiki_title: "Terraform/fr"
source_hash: "ce79fd3cfff6a88bb4b1886778a45a8a"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:58:23.046759+00:00"

tags:
  - cloud

keywords:
  - "openstack_compute_floatingip_associate_v2"
  - "machines virtuelles"
  - "power_state"
  - "security_groups"
  - "Resources added"
  - "volume racine"
  - "Identifiants"
  - "réseau privé"
  - "UUID des images"
  - "nuages OpenStack"
  - "Horizon"
  - "Configuration"
  - "ressources OpenStack"
  - "informations d’identification"
  - "IP flottante"
  - "Creation complete"
  - "openstack_compute_instance_v2"
  - "instance"
  - "Adresse IP flottante"
  - "terraform plan"
  - "bonnes pratiques"
  - "machine virtuelle"
  - "UUID"
  - "instance_id"
  - "ressources"
  - "key_pair"
  - "syntaxe v0.12"
  - "Machine virtuelle"
  - "clé SSH"
  - "Infrastructure-en-code"
  - "instance persistante"
  - "floating_ip"
  - "volume de démarrage"
  - "Fichier d'état"
  - "réseau externe"
  - "OpenStack"
  - "variable d'environnement"
  - "mots de passe"
  - "VM OpenStack"
  - "access_ip_v4"
  - "configuration Terraform"
  - "VM"
  - "block_device"
  - "Références"
  - "known after apply"
  - "configuration réseau"
  - "Initialisation"
  - "état"
  - "configuration"
  - "forces replacement"
  - "Fournisseur OpenStack"
  - "Identifiants OpenStack"
  - "groupe d'IP"
  - "terraform apply"
  - "network"
  - "Informations d'identification"
  - "Terraform"
  - "fournisseur OpenStack"
  - "ressources existantes"
  - "$OS_CLOUD"
  - "instance de calcul"
  - "gabarits sous Horizon"
  - "clouds.yaml"
  - "tutoriel"
  - "gabarits"
  - "piratage"
  - "outils CLI"
  - "Apply complete"

questions:
  - "Qu'est-ce que Terraform et quel est son rôle principal dans la gestion des infrastructures OpenStack ?"
  - "Quels sont les prérequis nécessaires avant de pouvoir commencer à utiliser Terraform selon ce tutoriel ?"
  - "Quelles sont les deux méthodes expliquées pour configurer et fournir ses identifiants OpenStack dans un environnement de ligne de commande ?"
  - "Pourquoi est-il utile de conserver une session d'interface de ligne de commande OpenStack ouverte lors de la configuration de Terraform ?"
  - "Quelles sont les différentes méthodes pour transmettre les informations de connexion OpenStack au fournisseur Terraform ?"
  - "Quelle est la meilleure pratique recommandée en matière de sécurité pour la gestion des mots de passe dans les configurations Terraform ?"
  - "Comment peut-on obtenir et installer le fichier clouds.yaml s'il n'est pas encore présent sur le système ?"
  - "Pourquoi est-il fortement recommandé de renommer le nuage dans le fichier de configuration ?"
  - "Quelle variable d'environnement est nécessaire pour utiliser les outils CLI avec le nuage OpenStack choisi ?"
  - "Pourquoi est-il considéré comme une mauvaise pratique de stocker ses informations d'identification dans la configuration Terraform ?"
  - "Quels risques spécifiques sont liés à la copie et au déplacement des fichiers de configuration sur un poste de travail local ?"
  - "Pourquoi faut-il maintenir les bonnes pratiques contre le piratage même lorsque l'on travaille seul sur un environnement isolé ?"
  - "À quoi sert la commande `terraform init` et pourquoi ne permet-elle pas de vérifier les informations d'identification ?"
  - "Pourquoi est-il crucial d'utiliser les identifiants (ID) plutôt que les noms pour définir les images et les gabarits d'une machine virtuelle ?"
  - "Quelle est la recommandation principale concernant la gestion des volumes pour les instances de calcul persistantes ?"
  - "Où peut-on consulter les informations relatives aux UUID des images et des gabarits sous Horizon ?"
  - "Pourquoi une instance persistante risque-t-elle d'échouer si aucun volume n'est fourni ?"
  - "Quelle est la méthode recommandée pour configurer le stockage des machines virtuelles qui utilisent des versions persistantes ?"
  - "Quel est le rôle principal de la commande `terraform plan` et quelles informations essentielles fournit-elle à l'utilisateur ?"
  - "Que signifie la mention `known after apply` pour les attributs des ressources affichées dans le plan d'exécution ?"
  - "Comment Terraform interagit-il avec les ressources OpenStack déjà existantes qui ne sont pas déclarées dans sa configuration ?"
  - "Pourquoi la première exécution de la commande `terraform apply` échoue-t-elle dans l'exemple présenté ?"
  - "Comment peut-on résoudre l'erreur de réseaux multiples lors de la création d'une machine virtuelle avec Terraform ?"
  - "Quelle précaution est-il conseillé de prendre pour protéger les ressources OpenStack existantes contre une manipulation involontaire ?"
  - "Terraform affecte-t-il les machines virtuelles déjà existantes dans un projet OpenStack ?"
  - "Sur quels éléments précis Terraform se base-t-il pour exécuter ses actions ?"
  - "Pourquoi Terraform ignore-t-il l'état des ressources préexistantes sur l'infrastructure ?"
  - "What are the primary configuration details, such as the name and key pair, assigned to the virtual machine being deployed?"
  - "Why are the fixed and floating IP addresses listed as \"known after apply\" in the network configuration?"
  - "What is the intended power state and security group assignment for this resource upon creation?"
  - "À quoi sert le fichier terraform.tfstate généré après l'application de la configuration et pourquoi est-il indispensable ?"
  - "Pourquoi la nouvelle machine virtuelle n'est-elle pas directement accessible depuis l'extérieur et quelle méthode alternative permet de s'y connecter ?"
  - "Comment une adresse IP flottante est-elle allouée et associée à une machine virtuelle dans OpenStack selon le document ?"
  - "Comment une adresse IP flottante est-elle concrètement associée à une machine virtuelle dans un environnement OpenStack ?"
  - "Quelle action doit être entreprise si aucune adresse IP flottante n'a encore été allouée au projet ?"
  - "Quelle est l'unique information requise pour pouvoir allouer une nouvelle adresse IP flottante ?"
  - "Comment allouer une nouvelle adresse IP flottante avec Terraform dans un environnement OpenStack ?"
  - "Quelle syntaxe permet de référencer les attributs d'une ressource existante pour associer une IP flottante à une instance ?"
  - "Pourquoi la documentation officielle du fournisseur OpenStack peut-elle différer de la syntaxe présentée dans cet exemple ?"
  - "What infrastructure tool is prompting the user for approval, and what input is required to proceed?"
  - "Which specific OpenStack resource is being created during this execution?"
  - "What is the final summary of resources added, changed, and destroyed after the apply is complete?"
  - "Comment peut-on se connecter à l'instance via SSH et quelle configuration de sécurité peut être nécessaire en cas d'échec ?"
  - "Pourquoi l'ajout d'un volume racine avec Terraform est-il considéré comme une opération destructrice nécessitant une lecture attentive des plans d'exécution ?"
  - "Pour quelle raison est-il crucial de supprimer l'attribut \"image_id\" de la définition de l'instance lors de la configuration d'un démarrage à partir d'un volume ?"
  - "Quelles sont les modifications annoncées par le plan d'exécution Terraform concernant les ressources de l'infrastructure ?"
  - "Quelles étapes l'utilisateur doit-il suivre pour se connecter à la nouvelle machine virtuelle et mettre à jour le système d'exploitation ?"
  - "Quels composants spécifiques sont déployés dans l'exemple complet de configuration Terraform pour OpenStack ?"
  - "What specific OpenStack resource is scheduled to be replaced according to this Terraform plan?"
  - "Which attribute change is explicitly marked as forcing the replacement of the virtual machine?"
  - "How are the network attributes, such as the IPv4 and IPv6 access IPs, expected to be resolved during the execution?"
  - "À qui s'adresse cette section d'annexe et de références ?"
  - "Quelle précision est apportée concernant la compatibilité des versions de syntaxe pour la documentation du fournisseur OpenStack ?"
  - "Quel concept ou outil le lien de référence proposé à la fin du texte permet-il de découvrir ?"
  - "Quels sont les exemples de projets et les ressources documentaires recommandés pour démarrer avec Terraform sur OpenStack ?"
  - "Comment peut-on trouver l'UUID d'une image spécifique en utilisant l'interface Web Horizon d'OpenStack ?"
  - "Quelles sont les deux méthodes suggérées pour obtenir l'ID d'un gabarit (flavor) étant donné que l'interface Horizon ne fournit que son nom ?"
  - "Quels sont les exemples de projets et les ressources documentaires recommandés pour démarrer avec Terraform sur OpenStack ?"
  - "Comment peut-on trouver l'UUID d'une image spécifique en utilisant l'interface Web Horizon d'OpenStack ?"
  - "Quelles sont les deux méthodes suggérées pour obtenir l'ID d'un gabarit (flavor) étant donné que l'interface Horizon ne fournit que son nom ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Terraform](https://www.terraform.io/) est un outil qui permet de définir et d'approvisionner l'infrastructure de centres de données, y compris des machines virtuelles. Terraform est de plus en plus utilisé au sein de l'Alliance. Son modèle d'infrastructure-en-code permet de maintenir les ressources OpenStack comme une collection de définitions qui peuvent être facilement mises à jour à l'aide des éditeurs de texte, partagées entre les membres d'un groupe et stockées dans un système de contrôle de version.

Cette page est écrite comme un tutoriel dans lequel nous présentons Terraform et démontrons son utilisation sur nos nuages OpenStack. Nous configurons notre espace de travail local pour Terraform et créons une machine virtuelle (VM pour *virtual machine*) avec une IP flottante et un volume attaché.

## Préparation

Avant de commencer avec Terraform, vous avez besoin :
* d'un accès à un projet OpenStack avec des ressources disponibles,
* d'installer le binaire `terraform`,
* d'effectuer quelques configurations sur votre poste de travail ou ordinateur portable.

### Accéder à OpenStack

Pour accéder au nuage, voir [Obtenir un projet dans l'environnement infonuagique](cloud.md#obtenir-un-projet-dans-lenvironnement-infonuagique). Si vous n'avez jamais utilisé OpenStack auparavant, vous devriez d'abord vous familiariser avec ce système en créant une machine virtuelle, en attachant un volume, en associant une IP flottante et en vous assurant que vous pouvez vous connecter à la machine virtuelle par la suite. Ce tutoriel suppose également que vous avez déjà créé une paire de clés SSH et que la clé publique a été importée dans OpenStack.

Si vous ne savez pas encore comment faire cela, le [Guide de démarrage](cloud_quick_start.md) est une bonne introduction. La création de ces ressources à l'aide de l'interface web d'OpenStack vous permettra de comprendre le fonctionnement et l'utilité de Terraform.

### Installer Terraform

Consultez la [page de téléchargement](https://www.terraform.io/downloads.html) de Terraform pour obtenir la dernière version du binaire. Nous utilisons ici Terraform 0.12.

### S'identifier pour OpenStack

Il y a deux façons de fournir vos identifiants OpenStack dans un environnement de ligne de commande : via des variables d'environnement ou dans un fichier de configuration. Nous utiliserons une des méthodes décrites dans la [section suivante](#definir-le-fournisseur-openstack). Quelle que soit votre méthode préférée, OpenStack propose un moyen simple de télécharger les identifiants. Une fois la connexion établie, cliquez sur *Accès à l'API* dans la barre de navigation; sur cette page se trouve le menu déroulant intitulé *Télécharger le fichier RC OpenStack*. À partir de là, vous pouvez télécharger un fichier `clouds.yaml` ou un fichier RC qui peut être obtenu à partir de votre session de l'interpréteur (*shell*).

Le fichier RC contient une liste de commandes pour l'interpréteur qui servent à exporter les variables d'environnement dans votre session active. Il ne s'agit pas d'un script indépendant et il doit recevoir de l'information par :

```bash
$ source openrc.sh
```
Vous devez alors entrer votre mot de passe OpenStack qui sera enregistré dans une variable d'environnement préfixée par `OS_`. D'autres variables d'environnement seront créées avec certains renseignements sur vous, votre projet et le nuage auquel vous voulez vous connecter.

L’autre méthode est de créer une configuration dans `$HOME/.config/openstack/clouds.yaml`. Si vous n’avez pas déjà un tel fichier, vous pouvez télécharger `clouds.yaml` comme décrit ci-dessus et le copier à l’emplacement souhaité. Nous vous recommandons de modifier le nom donné au nuage dans le fichier téléchargé en un nom significatif, surtout si vous utilisez plusieurs nuages OpenStack. Ensuite, pour utiliser les outils CLI décrits ci-dessous, créez simplement une variable d’environnement `$OS_CLOUD` avec le nom du nuage que vous souhaitez utiliser.

```bash
$ export OS_CLOUD=arbutus
```

Peu importe ce que vous choisissez, vous utiliserez ceci pour configurer Terraform.

### Session OpenStack

Il est utile d'avoir une fenêtre de terminal ouverte qui exécute l'interface de ligne de commande OpenStack. Cela fournit une référence pratique pour les spécifications que vous allez créer, car vous aurez besoin des identifiants de gabarits (*flavors*) et d'image pour vérifier les actions effectuées par Terraform. Horizon peut être utilisé pour rechercher des images et pour vérifier en général que Terraform produit les effets escomptés, mais il n'est pas possible de rechercher directement les identifiants des gabarits.

OpenStack CLI (aussi appelé *OSC*) est un client Python qui peut être installé avec Python Pip et qui [est disponible pour plusieurs distributions et systèmes d'exploitation](https://docs.openstack.org/newton/user-guide/common/cli-install-openstack-command-line-clients.html).

### Espace de travail

Créez enfin un répertoire pour vos fichiers de configuration et d'état qui servira de point de départ.

## Définir le fournisseur OpenStack

Décrivez d'abord le fournisseur : c'est ici que vous dites à Terraform d'utiliser OpenStack et comment l'utiliser. Lors de l'initialisation, la version la plus récente du plugiciel du fournisseur OpenStack sera installée dans le répertoire de travail et lors des opérations Terraform suivantes, les informations d'identification incluses seront utilisées pour se connecter au nuage spécifié.

Vos informations de connexion et d'identification pour OpenStack peuvent être fournies à Terraform dans la spécification, dans l'environnement ou partiellement dans la spécification avec le reste dans l'environnement.

Voici un exemple de spécification du fournisseur avec des informations de connexion et d'identification :

```terraform
terraform {
  required_providers {
    openstack = {
      source  = "terraform-provider-openstack/openstack"
    }
  }
}

provider "openstack" {
  tenant_name = "some_tenant"
  tenant_id   = "1a2b3c45678901234d567890fa1b2cd3"
  auth_url    = "https://cloud.example.org:5000/v3"
  user_name   = "joe"
  password    = "sharethiswithyourfriends!"
  user_domain_name = "CentralID"
}
```

Pour certaines instances OpenStack, ce qui précède spécifierait l'ensemble complet des informations nécessaires pour se connecter à l'instance et gérer les ressources dans le projet locataire (*tenant*) donné. Cependant, Terraform prend en charge les informations d'identification partielles dans lesquelles vous pouvez laisser certaines valeurs en dehors de la configuration Terraform et les fournir d'une autre manière. Cela nous permettrait, par exemple, de laisser le mot de passe en dehors du fichier de configuration, auquel cas il devrait être spécifié dans l'environnement avec `$OS_PASSWORD`.

Si vous préférez, vous pouvez aussi utiliser `clouds.yaml` et spécifier `cloud`.

```terraform
provider "openstack" {
  cloud = "my_cloud"
}
```

Il n'est pas nécessaire d'entrer une définition pour *provider*.

```terraform
provider "openstack" {
}
```

Dans ce cas, soit `$OS_CLOUD`, soit les variables définies par le fichier RC approprié doivent se trouver dans l'environnement d'exécution pour que Terraform puisse continuer.

Les options disponibles sont décrites en détail dans [cette page de Terraform](https://www.terraform.io/docs/providers/openstack/index.html).

### Ce que vous devriez utiliser

Il peut être tentant de laisser certains détails dans l'environnement afin que la configuration Terraform soit plus portable ou réutilisable, mais comme nous le verrons plus tard, la configuration Terraform contiendra et doit contenir des détails spécifiques à chaque nuage, tels que les UUID de gabarit et d'image, les noms de réseau et les locataires.

Le plus important pour votre configuration est la sécurité. Vous voudrez probablement éviter de stocker vos informations d’identification dans la configuration Terraform, même si vous ne les partagez avec personne, même si elles se trouvent sur votre propre poste de travail et que personne d’autre que vous n’y a accès. Même si vous n’avez pas peur du piratage, ce n’est certainement pas une bonne pratique de stocker des mots de passe et autres dans des fichiers de configuration qui peuvent finir par être copiés et déplacés dans votre système de fichiers lorsque vous essayez des choses. Mais aussi, n’oubliez jamais les bonnes pratiques pour contrer le piratage.

### Initialiser Terraform

Pour nous assurer que le fournisseur est correctement configuré, initialisez Terraform et vérifiez la configuration jusqu'à présent. Avec la définition du fournisseur dans un fichier appelé, par exemple, `nodes.tf`, exécutez `terraform init`.

```bash
$ terraform init
Initializing the backend...

Initializing provider plugins...
- Checking for available provider plugins...
- Downloading plugin for provider "openstack" (terraform-providers/openstack)
  1.19.0...

The following providers do not have any version constraints in configuration,
so the latest version was installed.

To prevent automatic upgrades to new major versions that may contain breaking
changes, it is recommended to add version = "..." constraints to the
corresponding provider blocks in configuration, with the constraint strings
suggested below.

* provider.openstack: version = "~> 1.19"

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```

Cela montre que l'initialisation de Terraform et le téléchargement du plugiciel du fournisseur ont ​​réussi donc que le code OpenStack est géré correctement. Cela ne teste pas les informations d'identification, car cette opération n'essaie pas réellement de se connecter au fournisseur défini.

## Définir une VM

Définissons maintenant une VM de base.

!!! warning "Important"
    Il est recommandé de **toujours** spécifier les gabarits et les images à l'aide de leurs identifiants, même lorsque Terraform prend en charge l'utilisation du nom. Bien que le nom soit plus lisible, l'identifiant est ce qui définit réellement l'état de la ressource et l'identifiant d'une image ou d'un gabarit donné **ne changera jamais**. Il est toutefois possible que **name** change. Si un gabarit ou une image est retirée, par exemple, et remplacée par une autre du même nom, la prochaine fois que vous exécuterez Terraform, l'identifiant mis à jour sera détecté et Terraform déterminera que vous souhaitez **reconstruire ou redimensionner la ressource associée**. Il s'agit d'une opération pour détruire (et reconstruire).

Une machine virtuelle OpenStack minimale peut être définie comme suit dans Terraform :

```terraform
resource "openstack_compute_instance_v2" "myvm" {
  name = "myvm"
  image_id = "80ceebef-f9aa-462e-a793-d3c1cf96123b"
  flavor_id = "0351ddb0-00d0-4269-80d3-913029d1a111"
  key_pair = "Aluminum"
  security_groups = ["default"]
}
```

Ceci crée une VM ayant le nom, l'image et le gabarit indiqués et associe la VM avec une paire de clés et le groupe de sécurité par défaut.

!!! note "Remarque"
    Si vous avez suivi le tutoriel jusqu'ici (ce qu'il serait bon de faire), utilisez vos propres valeurs pour `image_id`, `flavor_id` et `key_pair`, sinon cela échouera probablement.

Les valeurs pour `image_id` et `flavor_id` sont l’une des raisons pour lesquelles j’aime avoir une session de terminal ouverte qui exécute l’interface de ligne de commande OpenStack, connectée au nuage que je cible avec Terraform : dans le terminal je peux utiliser `flavor list` ou `image list` pour répertorier les noms et les identifiants.

Si vous utilisez Horizon (l'interface Web d'OpenStack), cela est en partie possible; voir [UUID des images et gabarits sous Horizon](#uuid-des-images-et-gabarits-sous-horizon) en annexe.

Notez qu'aucun volume n'est fourni. Une instance de calcul sur nos nuages aura déjà un volume qui lui est associé, mais une instance persistante échouera probablement à moins qu'il n'y ait assez d'espace vide dans l'image elle-même. Il est recommandé de [créer un volume de démarrage](working_with_volumes.md#demarrer-depuis-un-volume) pour les machines virtuelles qui utilisent des versions persistantes.

### Tester

La commande `terraform plan` compile la définition de Terraform, tente de déterminer comment réconcilier l'état résultant avec l'état actuel du nuage et produit un plan des modifications qui s'appliqueraient.

```bash
$ terraform plan
Refreshing Terraform state in-memory prior to plan...
The refreshed state will be used to calculate this plan, but will not be
persisted to local or remote state storage.


------------------------------------------------------------------------

An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # openstack_compute_instance_v2.myvm will be created
  + resource "openstack_compute_instance_v2" "myvm" {
      + access_ip_v4        = (known after apply)
      + access_ip_v6        = (known after apply)
      + all_metadata        = (known after apply)
      + availability_zone   = (known after apply)
      + flavor_id           = "0351ddb0-00d0-4269-80d3-913029d1a111"
      + flavor_name         = (known after apply)
      + force_delete        = false
      + id                  = (known after apply)
      + image_id            = "80ceebef-f9aa-462e-a793-d3c1cf96123b"
      + image_name          = (known after apply)
      + key_pair            = "Aluminum"
      + name                = "myvm"
      + power_state         = "active"
      + region              = (known after apply)
      + security_groups     = [
          + "default",
        ]
      + stop_before_destroy = false

      + network {
          + access_network = (known after apply)
          + fixed_ip_v4    = (known after apply)
          + fixed_ip_v6    = (known after apply)
          + floating_ip    = (known after apply)
          + mac            = (known after apply)
          + name           = (known after apply)
          + port           = (known after apply)
          + uuid           = (known after apply)
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

------------------------------------------------------------------------

Note: You didn't specify an "-out" parameter to save this plan, so Terraform
can't guarantee that exactly these actions will be performed if
"terraform apply" is subsequently run.
```

Prenez connaissance du résultat. Même s'il contient beaucoup d'information, *il est nécessaire d'en connaître le contenu* avant d'accepter les modifications afin d'éviter les mauvaises surprises.

!!! warning
    Si vous obtenez une erreur concernant des informations d'identification incomplètes, vous avez peut-être oublié de définir `OS_CLOUD` ou de sourcer le fichier RC, ou encore, votre fichier `clouds.yaml` est peut-être absent.

Ces valeurs sont celles des ressources telles qu'elles seraient définies dans OpenStack. Tout ce qui est marqué comme `known after apply` sera déterminé à partir de l'état des ressources nouvellement créées interrogées à partir d'OpenStack. Les autres valeurs sont définies en fonction de ce que nous avons défini ou déterminé par Terraform et le plugiciel OpenStack comme valeurs calculées ou par défaut.

Si vous n'avez pas le temps et que ce n'est pas grave de détruire accidentellement des ressources ou de les reconstruire, **prenez au moins le temps** de vérifier la dernière ligne du plan.

```bash
Plan: 1 to add, 0 to change, 0 to destroy.
```

Dans ce cas, nous savons que nous ajoutons une ressource, donc cela semble correct. Si les autres valeurs étaient différentes de zéro, nous ferions mieux de réexaminer notre configuration, notre état et ce qui est réellement défini dans OpenStack, pour ensuite effectuer les corrections nécessaires.

### Que se passe-t-il avec les ressources OpenStack déjà existantes?

Si des VM sont déjà définies dans votre projet OpenStack, vous vous demandez peut-être si Terraform affectera ces ressources.

Eh bien non. Terraform ne connaît pas les ressources qui sont déjà définies pour le projet et n'essaie pas d'en déterminer l'état. Les actions de Terraform se basent sur la configuration fournie et sur l'état précédemment déterminé dans la configuration. Les ressources existantes ne sont pas représentées dans Terraform et lui sont invisibles.

Il est possible d'importer des ressources OpenStack précédemment définies dans Terraform, mais [ce n'est pas une mince affaire](https://dleske.gitlab.io/posts/terraform-import-manually/) et cela sort du cadre de ce tutoriel. L'important ici est que toutes les ressources existantes dans votre projet OpenStack soient protégées contre toute manipulation involontaire via Terraform, mais pourquoi ne pas lire attentivement les plans de sortie pour votre tranquillité d'esprit? :)

### Appliquer la configuration

Utilisez `terraform apply` pour effectuer le changement décrit dans le plan.

```bash
$ terraform apply

An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

[... repeat of the plan from above ...]

Plan: 1 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

openstack_compute_instance_v2.myvm: Creating...

Error: Error creating OpenStack server: Expected HTTP response code [] when
accessing [POST
https://cloud.example.org:8774/v2.1/43b86742c5ee4eaf800a36d7d234d95c/servers],
but got 409 instead
{"conflictingRequest": {"message": "Multiple possible networks found, use a
Network ID to be more specific.", "code": 409}}

  on nodes.tf line 4, in resource "openstack_compute_instance_v2" "myvm":
   4: resource "openstack_compute_instance_v2" "myvm" {
```

Dans notre exemple, ceci échoue. Il y a au moins deux réseaux qui sont définis pour un projet OpenStack : un privé et un public. Terraform a besoin de savoir lequel utiliser.

## Ajouter un réseau

Le nom du réseau privé diffère d'un projet à l'autre et la convention de nommage peut différer d'un nuage à l'autre, mais ils se trouvent généralement sur un réseau 192.168.X.Y et peuvent être trouvés dans la CLI à l'aide de `network list` ou sur Horizon sous *Réseau → Réseaux*. Si le réseau privé de votre projet est `my-tenant-net`, vous ajouterez un sous-bloc de ressources `network` à votre définition de VM similaire à ce qui suit :

```terraform
resource "openstack_compute_instance_v2" "myvm" {
  name = "myvm"
  image_id = "80ceebef-f9aa-462e-a793-d3c1cf96123b"
  flavor_id = "0351ddb0-00d0-4269-80d3-913029d1a111"
  key_pair = "Aluminum"
  security_groups = ["default"]

  network {
    name = "my-tenant-net"
  }
}
```

Essayez de nouveau.

```bash
$ terraform apply

An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # openstack_compute_instance_v2.myvm will be created
  + resource "openstack_compute_instance_v2" "myvm" {
      + access_ip_v4        = (known after apply)
      + access_ip_v6        = (known after apply)
      + all_metadata        = (known after apply)
      + availability_zone   = (known after apply)
      + flavor_id           = "0351ddb0-00d0-4269-80d3-913029d1a111"
      + flavor_name         = (known after apply)
      + force_delete        = false
      + id                  = (known after apply)
      + image_id            = "80ceebef-f9aa-462e-a793-d3c1cf96123b"
      + image_name          = (known after apply)
      + key_pair            = "Aluminum"
      + name                = "myvm"
      + power_state         = "active"
      + region              = (known after apply)
      + security_groups     = [
          + "default",
        ]
      + stop_before_destroy = false

      + network {
          + access_network = false
          + fixed_ip_v4    = (known after apply)
          + fixed_ip_v6    = (known after apply)
          + floating_ip    = (known after apply)
          + mac            = (known after apply)
          + name           = "my-tenant-net"
          + port           = (known after apply)
          + uuid           = (known after apply)
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

openstack_compute_instance_v2.myvm: Creating...
openstack_compute_instance_v2.myvm: Still creating... [10s elapsed]
openstack_compute_instance_v2.myvm: Still creating... [20s elapsed]
openstack_compute_instance_v2.myvm: Still creating... [30s elapsed]
openstack_compute_instance_v2.myvm: Creation complete after 32s [id=1f7f73ff-b9b5-40ad-9ddf-d848efe13e42]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

Vous avez maintenant une machine virtuelle créée par Terraform. Vous devriez voir votre nouvelle machine virtuelle sur Horizon ou dans la sortie de `server list` dans votre fenêtre de terminal OpenStack.

```text
(openstack) server list -c ID -c Name -c Status
+--------------------------------------+--------+--------+
| ID                                   | Name   | Status |
+--------------------------------------+--------+--------+
| 1f7f73ff-b9b5-40ad-9ddf-d848efe13e42 | myvm   | ACTIVE |
| c3fa7d11-4122-412a-ad19-32e52cbb8f66 | store  | ACTIVE |
| f778f65f-c9d5-4808-930b-9f50d82a8c9c | puppet | ACTIVE |
| 9b42cbf3-3782-4472-bdd0-9028bbb73460 | lbr    | ACTIVE |
+--------------------------------------+--------+--------+
```

Dans ce résultat, trois instances précédemment créées ont survécu sans être touchées par Terraform.

### Récapitulation

Notez qu'il existe désormais un fichier dans votre espace de travail appelé `terraform.tfstate`. Il a été créé par Terraform lors de l'application de la nouvelle configuration et de la confirmation de sa réussite. Le fichier d'état contient des détails sur les ressources gérées que Terraform utilise pour déterminer comment arriver à un nouvel état décrit par les mises à jour de configuration. En général, vous n'aurez pas besoin de consulter ce fichier, mais sachez que sans lui, Terraform ne peut pas gérer correctement les ressources et si vous le supprimez, vous devrez le restaurer ou le recréer, ou gérer ces ressources sans Terraform.

Vous avez maintenant une machine virtuelle opérationnelle qui a été initialisée avec succès et qui se trouve sur le réseau privé. Cependant, vous ne pouvez pas vous y connecter et la consulter, car vous n'avez pas attribué d'adresse IP flottante à cet hôte. Elle n'est donc pas directement accessible depuis l'extérieur du locataire.

Si vous aviez un autre hôte dans ce locataire avec une adresse IP flottante, vous pourriez l'utiliser comme bastion (*bastion host*) pour la nouvelle machine virtuelle, car ils seront tous deux sur le même réseau privé. Il s'agit d'une bonne stratégie à utiliser pour les nœuds qui n'ont pas besoin d'être directement accessibles depuis Internet, comme un serveur de base de données, ou simplement pour préserver les ressources limitées que sont les adresses IP flottantes.

Pour l'instant, ajoutez une IP flottante à votre nouvelle VM.

## Ajouter une adresse IP flottante

Une IP flottante n'est pas créée directement sur une VM OpenStack, mais est allouée au projet à partir d'un groupe d'IP et associée à l'interface du réseau privé de l'IP.

En supposant que vous n'avez pas déjà d'IP flottante allouée à cette utilisation, déclarez une ressource IP flottante comme dans l'exemple suivant. La seule chose dont vous avez besoin est de connaître le pool à partir duquel allouer l'IP flottante; sur nos nuages, il s'agit du réseau externe (`ext_net` dans cet exemple).

```terraform
resource "openstack_networking_floatingip_v2" "myvm_fip" {
  pool = "ext_net"
}
```

Acceptez ce changement maintenant ou utilisez `terraform plan` pour voir ce qui se produirait.

```bash
$ terraform apply
openstack_compute_instance_v2.myvm: Refreshing state...
[id=1f7f73ff-b9b5-40ad-9ddf-d848efe13e42]

An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # openstack_networking_floatingip_v2.myvm_fip will be created
  + resource "openstack_networking_floatingip_v2" "myvm_fip" {
      + address   = (known after apply)
      + all_tags  = (known after apply)
      + fixed_ip  = (known after apply)
      + id        = (known after apply)
      + pool      = "provider-199-2"
      + port_id   = (known after apply)
      + region    = (known after apply)
      + tenant_id = (known after apply)
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

openstack_networking_floatingip_v2.myvm_fip: Creating...
openstack_networking_floatingip_v2.myvm_fip: Creation complete after 9s
[id=20190061-c2b6-4740-bbfc-6facbb300dd4]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

Cette IP flottante est maintenant *allouée*, mais pas encore associée à votre instance. Ajoutez la définition suivante :

```terraform
resource "openstack_compute_floatingip_associate_v2" "myvm_fip" {
  floating_ip = openstack_networking_floatingip_v2.myvm_fip.address
  instance_id = openstack_compute_instance_v2.myvm.id
}
```

Les attributs de cette nouvelle ressource sont définis par des références à d'autres ressources et leurs attributs.

!!! note "Remarque"
    La documentation actuelle du fournisseur OpenStack utilise une syntaxe différente de celle présentée ici, car elle n'a pas encore été mise à jour pour les modifications apportées à Terraform v.12.

Des références comme celle-ci sont généralement `<resource type>.<resource name>.<attribute>`. D'autres références que vous pourriez voir bientôt incluent `var.<variable name>`. Dans tous les cas, cette ressource forme une association entre la ressource créée précédemment et l'IP flottante allouée à l'étape suivante.

```bash
$ terraform apply
openstack_networking_floatingip_v2.myvm_fip: Refreshing state...
[id=20190061-c2b6-4740-bbfc-6facbb300dd4]
openstack_compute_instance_v2.myvm: Refreshing state...
[id=1f7f73ff-b9b5-40ad-9ddf-d848efe13e42]

An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # openstack_compute_floatingip_associate_v2.myvm_fip will be created
  + resource "openstack_compute_floatingip_associate_v2" "myvm_fip" {
      + floating_ip = "X.Y.Z.W"
      + id          = (known after apply)
      + instance_id = "1f7f73ff-b9b5-40ad-9ddf-d848efe13e42"
      + region      = (known after apply)
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

openstack_compute_floatingip_associate_v2.myvm_fip: Creating...
openstack_compute_floatingip_associate_v2.myvm_fip: Creation complete after 5s
[id=X.Y.Z.W/1f7f73ff-b9b5-40ad-9ddf-d848efe13e42/]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

S'il y a une IP flottante, vous pouvez probablement vous connecter à l'instance via SSH maintenant.

```bash
$ ssh centos@X.Y.Z.W hostname
The authenticity of host 'X.Y.Z.W (X.Y.Z.W)' can't be established.
ECDSA key fingerprint is SHA256:XmN5crnyxvE1sezdpo5tG5Z2nw0Z+2pspvkNSGpB99A.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'X.Y.Z.W' (ECDSA) to the list of known hosts.
myvm.novalocal
```

Autrement, il est possible que vous deviez ajouter l'adresse IP de votre ordinateur au groupe de sécurité par défaut du projet.

## Ajouter un volume

Ajoutez ensuite un volume racine à la machine virtuelle. Étant donné que cela remplacera son disque de démarrage, *c'est une opération destructrice*. Ceci est un élément auquel vous devez faire attention dans Terraform et l’une des principales raisons pour lesquelles vous devez lire attentivement vos plans avant de les appliquer. Il est peu probable que vous provoquiez accidentellement des problèmes critiques lors de la création de nouvelles ressources, mais il peut être incroyablement facile de créer accidentellement des modifications de configuration qui nécessitent la reconstruction des machines virtuelles existantes.

Puisque c'est un volume racine, créez-le dans l'instance de calcul en tant que sous-bloc avec le sous-bloc du réseau.

```terraform
  block_device {
    uuid = "80ceebef-f9aa-462e-a793-d3c1cf96123b"
    source_type = "image"
    destination_type = "volume"
    volume_size = 10
    boot_index = 0
    delete_on_termination = true
  }
```

Définissez l'attribut `uuid` comme l'UUID de l'image que vous souhaitez utiliser et supprimez `image_id` de la définition du bloc externe. Les autres attributs sont explicites, à l'exception de `destination_type`, qui est ici défini sur `volume` pour indiquer que le stockage doit être effectué avec un volume fourni par OpenStack plutôt que d'utiliser un disque sur l'hyperviseur. `delete_on_termination` est important : pour les tests, vous souhaiterez probablement que ce paramètre soit `true` afin de ne pas avoir à vous rappeler de nettoyer constamment les volumes restants, mais pour une utilisation réelle, vous devriez envisager de le définir sur `false` comme dernière défense contre une suppression accidentelle de ressources.

!!! note "Remarque"
    Ne laissez pas l'attribut `image_id` défini dans la définition de l'instance de calcul externe. Cela fonctionnera, mais Terraform changera de *démarrage à partir du volume* à *démarrage directement à partir de l'image* à chaque exécution, et tentera donc toujours de reconstruire votre instance. (Il s'agit probablement d'un défaut du fournisseur OpenStack.)

Voici à quoi ressemble le plan :

```bash
An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # openstack_compute_floatingip_associate_v2.myvm_fip must be replaced
-/+ resource "openstack_compute_floatingip_associate_v2" "myvm_fip" {
        floating_ip = "199.241.167.122"
      ~ id          = "199.241.167.122/1f7f73ff-b9b5-40ad-9ddf-d848efe13e42/" -> (known after apply)
      ~ instance_id = "1f7f73ff-b9b5-40ad-9ddf-d848efe13e42" -> (known after apply) # forces replacement
      ~ region      = "RegionOne" -> (known after apply)
    }

  # openstack_compute_instance_v2.myvm must be replaced
-/+ resource "openstack_compute_instance_v2" "myvm" {
      ~ access_ip_v4        = "192.168.2.11" -> (known after apply)
      + access_ip_v6        = (known after apply)
      ~ all_metadata        = {} -> (known after apply)
      ~ availability_zone   = "nova" -> (known after apply)
        flavor_id           = "0351ddb0-00d0-4269-80d3-913029d1a111"
      ~ flavor_name         = "p1-3gb" -> (known after apply)
        force_delete        = false
      ~ id                  = "1f7f73ff-b9b5-40ad-9ddf-d848efe13e42" -> (known after apply)
        image_id            = "80ceebef-f9aa-462e-a793-d3c1cf96123b"
      ~ image_name          = "CentOS-7-x64-2018-05" -> (known after apply)
        key_pair            = "Aluminum"
        name                = "myvm"
        power_state         = "active"
      ~ region              = "RegionOne" -> (known after apply)
        security_groups     = [
            "default",
        ]
        stop_before_destroy = false

      + block_device {
          + boot_index            = 0 # forces replacement
          + delete_on_termination = true # forces replacement
          + destination_type      = "volume" # forces replacement
          + source_type           = "image" # forces replacement
          + uuid                  = "80ceebef-f9aa-462e-a793-d3c1cf96123b" # forces replacement
          + volume_size           = 10 # forces replacement
        }

      ~ network {
            access_network = false
          ~ fixed_ip_v4    = "192.168.2.11" -> (known after apply)
          + fixed_ip_v6    = (known after apply)
          + floating_ip    = (known after apply)
          ~ mac            = "fa:16:3e:3b:79:27" -> (known after apply)
            name           = "my-tenant-net"
          + port           = (known after apply)
          ~ uuid           = "5c96bf54-a396-47c5-ab12-574f630bcb80" -> (known
after apply)
        }
    }
```

Notez qu'il y a plusieurs avertissements qui vous informent de ce qui sera modifié, sans oublier :

```bash
Plan: 2 to add, 0 to change, 2 to destroy.
```

Votre VM sera créée avec une nouvelle clé SSH. Si vous vous êtes déjà connecté, vous devrez donc supprimer la clé SSH de votre fichier `known_hosts` (ou équivalent). Après cela, la première chose à faire est de vous connecter et d'appliquer toutes les mises à jour disponibles.

```bash
[centos@myvm ~]$ sudo yum update -y
...
[ goes for ages ]
```

Vous avez maintenant une VM terraformée fonctionnelle, un moyen d'y accéder, un endroit où enregistrer les données et les dernières mises à jour du système d'exploitation.

## Exemple complet

```terraform
provider "openstack" {
}

resource "openstack_compute_instance_v2" "myvm" {
  name = "myvm"
  flavor_id = "0351ddb0-00d0-4269-80d3-913029d1a111"
  key_pair = "Aluminum"
  security_groups = ["default"]

  network {
    name = "my-tenant-net"
  }

  block_device {
    uuid = "80ceebef-f9aa-462e-a793-d3c1cf96123b"
    source_type = "image"
    destination_type = "volume"
    volume_size = 10
    boot_index = 0
    delete_on_termination = true
  }
}

resource "openstack_networking_floatingip_v2" "myvm_fip" {
  pool = "provider-199-2"
}

resource "openstack_compute_floatingip_associate_v2" "myvm_fip" {
  floating_ip = openstack_networking_floatingip_v2.myvm_fip.address
  instance_id = openstack_compute_instance_v2.myvm.id
}
```

## Annexe

### Références

Ce qui suit pourrait intéresser ceux qui veulent explorer plus en profondeur et développer le travail effectué dans ce tutoriel. Notez qu’au moment de la rédaction de cet article, la documentation du fournisseur OpenStack utilise la syntaxe v0.11, mais cela devrait fonctionner sans problème sous v0.12.

*   [What is Terraform?](https://www.terraform.io/intro/index.html)
*   [OpenStack Provider](https://www.terraform.io/docs/providers/openstack/index.html)
*   [OpenStack compute instance v2](https://www.terraform.io/docs/providers/openstack/r/compute_instance_v2.html) : plusieurs cas d'usage pour la création d'instances dans OpenStack avec Terraform
*   [La page wiki sur notre service infonuagique](cloud.md) et la page [Cloud : Guide de démarrage](cloud_quick_start.md)

### Exemples

*   Projet [Magic Castle](https://github.com/ComputeCanada/magic_castle)
*   [diodonfrost/terraform-openstack-examples](https://github.com/diodonfrost/terraform-openstack-examples) sur GitHub

### UUID des images et gabarits sous Horizon

Si vous êtes plus à l’aise avec l’interface Web d’OpenStack, voici un aide-mémoire rapide pour trouver les UUID de gabarits et d’images dans Horizon. Vous devrez vous connecter à l’interface Web du nuage pour obtenir ces informations.

Pour trouver l’UUID d’une image, recherchez l’élément de menu *Images* sous *Calcul*.

Vous obtiendrez une liste des images disponibles pour votre projet. Cliquez sur celle que vous voulez utiliser.

… et vous avez l'ID.

C'est un peu plus compliqué pour les gabarits.

Pour cela, vous devez simuler le lancement d'une instance, mais cela ne vous donne même pas l'ID du gabarit. Mais vous connaîtrez au moins le nom du gabarit que vous voulez.

Sur la page de l'instance, sélectionnez *Gabarit*.

Vous devriez maintenant avoir une liste de gabarits et voir ceux qui correspondent à vos quotas. Par contre, tout ce que vous avez ici, c'est le nom.

Pour obtenir l'ID, il y a deux options :

1.  Utilisez le nom pour la première exécution de Terraform, puis récupérez l'ID à partir du fichier de sortie ou d'état, et enfin, changez votre configuration pour utiliser l'ID à la place. Cela ne devrait pas tenter de recréer la VM, mais vérifiez avant d'accepter `terraform apply`.
2.  Passez à l'utilisation de l'interface de ligne de commande OpenStack. (Recommandé.)