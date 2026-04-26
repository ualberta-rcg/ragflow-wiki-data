---
title: "OpenStack command line clients/fr"
slug: "openstack_command_line_clients"
lang: "fr"

source_wiki_title: "OpenStack command line clients/fr"
source_hash: "002c5a0640412e6b8d869606ba8d656d"
last_synced: "2026-04-25T23:42:08.699101+00:00"
last_processed: "2026-04-26T00:23:10.326852+00:00"

tags:
  - cloud

keywords:
  - "installation"
  - "OpenStack"
  - "permissions d'administrateur"
  - "container"
  - "commandes"
  - "limits"
  - "Commandes network"
  - "composants"
  - "create"
  - "options et arguments"
  - "fichier RC"
  - "ligne de commande"
  - "Commandes volume"
  - "utilisateurs"
  - "object"
  - "help"
  - "OpenStackClient"
  - "Commandes server"
  - "interfaces"
  - "Cloud"
  - "Commandes image"
  - "Commandes"
  - "Groupes de commandes"
  - "Python"

questions:
  - "Comment installer le client en ligne de commande OpenStack selon le système d'exploitation ou les droits d'accès de l'utilisateur ?"
  - "Quelle est la procédure pour connecter et authentifier le client en ligne de commande à un projet OpenStack spécifique ?"
  - "De quelles manières peut-on exécuter les commandes OpenStack et comment obtenir de l'aide sur celles-ci ?"
  - "Quels sont les différents groupes de ressources gérés par ces commandes ?"
  - "Quelles sont les actions spécifiques qu'il est possible d'effectuer à l'aide du groupe de commandes \"server\" ?"
  - "Quelles sont les opérations de gestion de base qui sont communes à la majorité des groupes (comme \"volume\", \"image\" ou \"network\") ?"
  - "Comment peut-on afficher la liste des commandes associées à un groupe spécifique ?"
  - "Quelle est la syntaxe à utiliser pour connaître les options et les arguments d'une commande précise ?"
  - "Que se passe-t-il si un utilisateur tente d'exécuter une commande nécessitant des droits d'administrateur sans avoir les permissions requises ?"
  - "Quelles sont les commandes disponibles pour la gestion des conteneurs (\"container\") ?"
  - "Quelle commande unique est répertoriée sous la section des limites (\"limits\") ?"
  - "Quelles sont les deux catégories de commandes mentionnées comme n'étant pas largement rendues publiques ?"
  - "Pourquoi existe-t-il des commandes distinctes en plus de la commande globale openstack ?"
  - "Faut-il procéder à une installation supplémentaire pour pouvoir utiliser les commandes spécifiques aux divers composants ?"
  - "Quelles sont les fonctionnalités spécifiques gérées respectivement par les commandes nova, glance, cinder et heat ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Page enfant de [Gestion de vos ressources infonuagiques avec OpenStack](managing_your_cloud_resources_with_openstack.md)*

[OpenStackClient](http://docs.openstack.org/developer/python-openstackclient/) permet d'utiliser plusieurs fonctions du tableau de bord OpenStack, ainsi que d'autres fonctions qui ne sont pas disponibles par l'interface graphique. Pour l'utiliser sur tout genre de machine, virtuelle ou autre, il suffit d'installer le client et de disposer d'une connexion Internet. Les exemples de cette page sont sous Linux.

## Installation

Les outils en ligne de commande OpenStack sont conçus pour Python et fonctionnent sur un ordinateur personnel ou sur une instance infonuagique. Les différentes distributions de Linux peuvent offrir des paquets précompilés; pour les détails, consultez la [documentation d'installation](https://docs.openstack.org/user-guide/common/cli-install-openstack-command-line-clients.html). Si vous avez les permissions d'administrateur, vous pouvez rapidement installer Python et les outils en ligne de commande OpenStack.

### Ubuntu

```bash
sudo apt-get install python python-dev python-pip
sudo pip install python-openstackclient
```

### CentOS 7

Exécutez en tant que `root`.

```bash
yum install epel-release
yum install gcc python python-dev python2-pip
pip install python-openstackclient
```

### Fedora

```bash
sudo dnf install python-openstackclient
```

!!! note "Installation sans permissions d'administrateur"
    Si vous ne possédez pas les permissions d'administrateur, vous devez installer Python et [pip](https://pip.pypa.io/en/latest/installing/) autrement. Une fois l'installation complétée, vous pouvez installer les outils en ligne de commande dans votre espace `home` comme suit :

    ```bash
    pip install --user python-openstackclient
    ```

    La destination de l'installation est probablement incluse dans le `$PATH`; vous pouvez cependant vérifier si `~/.bashrc` ou `~/.bash_profile` inclut la ligne `PATH=$PATH:$HOME/.local/bin:$HOME/bin`.

### SDK

Pour explorer les [API Python](http://docs.openstack.org/user-guide/sdk.html), ajoutez `export PYTHONPATH=${HOME}/.local/lib/python2.7/site-packages/:${PYTHONPATH}` et modifiez `python2.7` en fonction de la version de Python installée.

## Connecter le client en ligne de commande à OpenStack

Vous devez indiquer au client où trouver le projet OpenStack dans notre environnement infonuagique.

!!! tip "Télécharger le fichier RC"
    Le moyen le plus simple est de télécharger un fichier de configuration via le tableau de bord OpenStack : `Projet > Accès API > Télécharger le fichier RC d’OpenStack`.

Si vous vous connectez au nouveau nuage Arbutus (et non à Arbutus d'avant les améliorations), vous devrez faire des modifications additionnelles à votre fichier RC; voir [Connecter le client en ligne de commande à OpenStack](arbutus_migration_guide.md).

Exécutez ensuite la commande suivante :

```bash
source <nom_du_projet>-openrc.sh
```

Lorsque vous devez entrer le mot de passe OpenStack, entrez votre mot de passe pour notre base de données CCDB. Pour tester la configuration, entrez :

```bash
openstack image list
```

Si vous utilisez plusieurs fichiers RC, méfiez-vous des variables d'environnement qui subsisteraient du dernier fichier RC utilisé, car elles pourraient empêcher l'exécution des commandes client OpenStack. Vous pouvez contourner ce problème de deux manières : en détruisant les variables avec `unset <nom_de_la_variable>` ou en démarrant une nouvelle session sans variables définies.

## Exécuter les commandes

Le client en ligne de commande peut être utilisé de manière interactive en entrant :

```bash
openstack
```

Entrez ensuite les commandes à l'invite. Chaque commande peut être entrée individuellement en la faisant précéder de `openstack`, par exemple :

```bash
openstack server list
```

En mode interactif, faites afficher la liste des commandes disponibles en entrant `help` à l'invite OpenStack. Les commandes disponibles sont classées en groupes; les plus communes sont présentées plus loin. Pour obtenir la liste des commandes appartenant à un groupe particulier, entrez `help <groupe_de_commandes>`. Pour obtenir les options et arguments liés à une commande, entrez `help <groupe_de_commandes> <commande>`. Sachez que plusieurs commandes ne sont disponibles qu'aux utilisateurs ayant les permissions d'administrateur et que dans le cas contraire, un message d'erreur sera affiché. Les commandes qui suivent sont disponibles pour tous les utilisateurs.

## Groupes de commandes

### Commandes `server`

| Commande                | Commande                |
| :---------------------- | :---------------------- |
| `add security group`    | `migrate`               |
| `add volume`            | `pause`                 |
| `create`                | `reboot`                |
| `delete`                | `rebuild`               |
| `dump create`           | `remove security group` |
| `image create`          | `remove volume`         |
| `list`                  | `rescue`                |
| `lock`                  | `resize`                |
| `resume`                | `unlock`                |
| `set`                   | `unpause`               |
| `shelve`                | `unrescue`              |
| `show`                  | `unset`                 |
| `ssh`                   | `unshelve`              |
| `start`                 |                         |
| `stop`                  |                         |
| `suspend`               |                         |

### Commandes `volume`

| Commande | Commande |
| :------- | :------- |
| `create` | `set`    |
| `delete` | `show`   |
| `list`   | `unset`  |

### Commandes `console`

| Commande | Commande |
| :------- | :------- |
| `log show` | `url show` |

### Commandes `flavor`

| Commande | Commande |
| :------- | :------- |
| `list`   | `show`   |

### Commandes `image`

| Commande | Commande |
| :------- | :------- |
| `create` | `save`   |
| `delete` | `set`    |
| `list`   | `show`   |

### Commandes `ip`

| Commande            | Commande            |
| :------------------ | :------------------ |
| `fixed add`         | `floating list`     |
| `fixed remove`      | `floating pool list`|
| `floating add`      | `floating remove`   |
| `floating create`   | `floating show`     |
| `floating delete`   |                     |

### Commandes `keypair`

| Commande | Commande |
| :------- | :------- |
| `create` | `list`   |
| `delete` | `show`   |

### Commandes `network`

| Commande | Commande |
| :------- | :------- |
| `create` | `set`    |
| `delete` | `show`   |
| `list`   |          |

### Commandes `snapshot`

| Commande | Commande |
| :------- | :------- |
| `create` | `set`    |
| `delete` | `show`   |
| `list`   | `unset`  |

### Commandes `security group`

| Commande    | Commande    |
| :---------- | :---------- |
| `create`    | `rule list` |
| `delete`    | `rule show` |
| `list`      | `set`       |
| `rule create` | `show`      |
| `rule delete` |             |

### Commandes `limits`

| Commande |
| :------- |
| `show`   |

## Autres interfaces

En plus de la commande `openstack` (décrite ci-dessus) qui incorpore dans une même commande la plupart des fonctionnalités, il existe aussi des commandes distinctes pour les divers composants OpenStack qui ajoutent d'autres fonctionnalités. Ces commandes sont installées en même temps que la commande `openstack` et aucune autre installation n'est nécessaire. Ces commandes sont :

*   [`nova`](https://docs.openstack.org/python-novaclient/latest/cli/nova.html) pour travailler avec des serveurs;
*   [`glance`](https://docs.openstack.org/python-glanceclient/latest/cli/glance.html) pour travailler avec des images;
*   [`cinder`](https://docs.openstack.org/python-cinderclient/latest/user/shell.html) pour travailler avec des volumes;
*   [`heat`](https://docs.openstack.org/python-heatclient/latest/man/heat.html) pour travailler avec l'orchestration.