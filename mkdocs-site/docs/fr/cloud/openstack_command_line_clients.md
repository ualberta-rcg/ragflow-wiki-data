---
title: "OpenStack command line clients/fr"
slug: "openstack_command_line_clients"
lang: "fr"

source_wiki_title: "OpenStack command line clients/fr"
source_hash: "2b6988fac9f472f650195e8ae78a466d"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:06:06.330398+00:00"

tags:
  - cloud

keywords:
  - "Cloud"
  - "create"
  - "fichier RC"
  - "installation"
  - "OpenStackClient"
  - "commandes OpenStack"
  - "security group"
  - "image"
  - "Commandes server"
  - "OpenStack"
  - "ligne de commande"
  - "volume"
  - "Commandes"
  - "object"
  - "commandes"
  - "store account"
  - "message d'erreur"
  - "network"
  - "composants"
  - "Groupes de commandes"
  - "permissions d'administrateur"
  - "delete"
  - "list"
  - "interfaces"

questions:
  - "Comment installer le client en ligne de commande OpenStack sur différentes distributions Linux, avec ou sans droits d'administrateur ?"
  - "Quelle est la procédure pour connecter le client en ligne de commande à un projet OpenStack spécifique à l'aide du fichier RC ?"
  - "Comment exécuter des commandes OpenStack et obtenir de l'aide sur les différentes options et groupes de commandes disponibles ?"
  - "Quelles sont les différentes catégories de ressources pour lesquelles des commandes sont listées dans ce texte ?"
  - "Quelles actions spécifiques peuvent être exécutées à l'aide des commandes liées aux adresses IP (Commandes ip) ?"
  - "Quelles sont les deux catégories de commandes qui sont signalées comme n'étant pas largement publicisées ?"
  - "Comment peut-on obtenir de l'aide sur une commande ou un groupe de commandes spécifique ?"
  - "Que se passe-t-il si un utilisateur tente d'exécuter une commande sans avoir les permissions d'administrateur requises ?"
  - "Quelles sont les commandes du groupe \"server\" qui sont accessibles à tous les utilisateurs ?"
  - "What are the specific commands available for managing an \"object\" according to the provided text?"
  - "Which operations can be performed specifically on a \"store account\" within the object context?"
  - "What common actions, such as show or list, are shared between the different entities listed in the snippet?"
  - "Qu'apportent les commandes distinctes par rapport à la commande générale `openstack` ?"
  - "Comment s'effectue l'installation de ces interfaces spécifiques aux divers composants ?"
  - "Quelles sont les fonctions respectives des commandes `nova`, `glance`, `cinder` et `heat` ?"
  - "Qu'apportent les commandes distinctes par rapport à la commande générale `openstack` ?"
  - "Comment s'effectue l'installation de ces interfaces spécifiques aux divers composants ?"
  - "Quelles sont les fonctions respectives des commandes `nova`, `glance`, `cinder` et `heat` ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Appartenant à : [Gestion de vos ressources infonuagiques avec OpenStack](gestion-vos-ressources-infonuagiques-avec-openstack.md)

L'[OpenStackClient](http://docs.openstack.org/developer/python-openstackclient/) permet d'utiliser plusieurs fonctions du tableau de bord OpenStack, ainsi que d'autres fonctions qui ne sont pas disponibles par l'interface graphique. Pour l'utiliser sur tout type de machine, virtuelle ou autre, il suffit d'installer le client et de disposer d'une connexion Internet. Les exemples de cette page sont sous Linux.

## Installation
Les outils OpenStack en ligne de commande sont conçus pour Python et fonctionnent sur un ordinateur personnel ou sur une instance infonuagique. Les différentes distributions Linux peuvent offrir des paquets précompilés; pour les détails, consultez la [documentation d'installation](https://docs.openstack.org/user-guide/common/cli-install-openstack-command-line-clients.html). Si vous avez les permissions d'administrateur, vous pouvez rapidement installer Python et les outils OpenStack en ligne de commande.

**Ubuntu**
```bash
sudo apt-get install python python-dev python-pip
sudo pip install python-openstackclient
```

**CentOS 7**
Exécuter en tant que `root`.
```bash
yum install epel-release
yum install gcc python python-dev python2-pip
pip install python-openstackclient
```

**Fedora**
```bash
sudo dnf install python-openstackclient
```

!!! note
    Si vous ne possédez pas les permissions d'administrateur, vous devez installer Python et [pip](https://pip.pypa.io/en/latest/installing/) autrement. Une fois l'installation complétée, vous pouvez installer les outils en ligne de commande dans votre espace *personnel* comme suit :
    ```bash
    pip install --user python-openstackclient
    ```
    La destination de l'installation est probablement incluse dans le `$PATH`; vous pouvez cependant vérifier si `~/.bashrc` ou `~/.bash_profile` inclut la ligne `PATH=$PATH:$HOME/.local/bin:$HOME/bin`.

Pour explorer les [API pour Python](http://docs.openstack.org/user-guide/sdk.html), ajoutez `export PYTHONPATH=${HOME}/.local/lib/python2.7/site-packages/:${PYTHONPATH}` et modifiez `python2.7` en fonction de la version de Python installée.

## Connecter le client en ligne de commande à OpenStack
Vous devez indiquer au client où trouver le projet OpenStack dans notre environnement infonuagique.
Le moyen le plus simple est de télécharger un fichier de configuration via le tableau de bord OpenStack, ainsi : *Projet > Accès API > Télécharger le fichier RC d’OpenStack*.

Exécutez ensuite la commande :
```bash
source <nom du projet>-openrc.sh
```
Lorsque vous devez entrer le mot de passe OpenStack, entrez votre mot de passe de notre base de données CCDB. Pour tester la configuration, entrez :
```bash
openstack image list
```

Si vous utilisez plusieurs fichiers RC, faites attention aux variables d'environnement qui pourraient subsister du dernier fichier RC utilisé, car elles pourraient empêcher l'exécution des commandes client OpenStack. Vous pouvez contourner ce problème de deux manières : en détruisant les variables avec `unset <nom-de-variable>` ou en démarrant une nouvelle session sans variables définies.

## Exécuter les commandes
Le client en ligne de commande peut être utilisé de manière interactive en entrant :
```bash
openstack
```

Entrez ensuite les commandes à l'invite. Chaque commande peut être entrée individuellement en la faisant précéder de `openstack`, par exemple :
```bash
openstack server list
```
En mode interactif, faites afficher la liste des commandes disponibles en entrant `help` à l'invite OpenStack. Les commandes disponibles sont classées en groupes; les plus communes sont présentées plus loin. Pour obtenir la liste des commandes appartenant à un groupe particulier, entrez `help <groupe de commandes>`. Pour obtenir les options et arguments liés à une commande, entrez `help <groupe de commandes> <commande>`. Sachez que plusieurs commandes ne sont disponibles qu'aux utilisateurs ayant les permissions d'administrateur et que dans le cas contraire, un message d'erreur s'affichera. Les commandes qui suivent sont disponibles pour tous les utilisateurs.

## Groupes de commandes
### Commandes `server`

| `add security group` | `migrate`             | `resume`          | `unlock`      |
| :------------------- | :-------------------- | :---------------- | :------------ |
| `add volume`         | `pause`               | `set`             | `unpause`     |
| `create`             | `reboot`              | `shelve`          | `unrescue`    |
| `delete`             | `rebuild`             | `show`            | `unset`       |
| `dump create`        | `remove security group` | `ssh`             | `unshelve`    |
| `image create`       | `remove volume`       | `start`           |               |
| `list`               | `rescue`              | `stop`            |               |
| `lock`               | `resize`              | `suspend`         |               |

### Commandes `volume`

| `create` | `set`   |
| :------- | :------ |
| `delete` | `show`  |
| `list`   | `unset` |

### Commandes `console`

| `log show` | `url show` |
| :--------- | :--------- |

### Commandes `flavor`

| `list` | `show` |
| :----- | :----- |

### Commandes `image`

| `create` | `save` |
| :------- | :----- |
| `delete` | `set`  |
| `list`   | `show` |

### Commandes `ip`

| `fixed add`       | `floating list`      |
| :---------------- | :------------------- |
| `fixed remove`    | `floating pool list` |
| `floating add`    | `floating remove`    |
| `floating create` | `floating show`      |
| `floating delete` |                      |

### Commandes `keypair`

| `create` | `list` |
| :------- | :----- |
| `delete` | `show` |

### Commandes `network`

| `create` | `set`  |
| :------- | :----- |
| `delete` | `show` |
| `list`   |        |

### Commandes `snapshot`

| `create` | `set`   |
| :------- | :------ |
| `delete` | `show`  |
| `list`   | `unset` |

### Commandes `security group`

| `create`      | `rule list` |
| :------------ | :---------- |
| `delete`      | `rule show` |
| `list`        | `set`       |
| `rule create` | `show`      |
| `rule delete` |             |

### Commandes `limits`

| `show` | |
| :----- | :- |

## Autres interfaces
En plus de la commande `openstack` (décrite ci-dessus) qui regroupe la plupart des fonctionnalités, il existe également des commandes distinctes pour les divers composants OpenStack, offrant des fonctionnalités supplémentaires. Ces commandes sont installées en même temps que la commande `openstack` et ne nécessitent aucune installation additionnelle. Ces commandes sont :
*   [`nova`](https://docs.openstack.org/python-novaclient/latest/cli/nova.html) pour travailler avec des serveurs;
*   [`glance`](https://docs.openstack.org/python-glanceclient/latest/cli/glance.html) pour travailler avec des images;
*   [`cinder`](https://docs.openstack.org/python-cinderclient/latest/user/shell.html) pour travailler avec des volumes;
*   [`heat`](https://docs.openstack.org/python-heatclient/latest/man/heat.html) pour travailler avec l'orchestration.