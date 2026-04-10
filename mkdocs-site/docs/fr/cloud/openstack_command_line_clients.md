---
title: "OpenStack command line clients/fr"
tags:
  - cloud

keywords:
  []
---

*Page enfant de [Managing your cloud resources with OpenStack](managing-your-cloud-resources-with-openstack.md)*

[OpenStackClient](http://docs.openstack.org/developer/python-openstackclient/) permet d'utiliser plusieurs fonctions du tableau de bord OpenStack, ainsi que d'autres fonctions qui ne sont pas disponibles par l'interface graphique. Pour l'utiliser sur tout genre de machine, virtuelle ou autre, il suffit d'installer le client et de disposer d'une connexion Internet. Les exemples de cette page sont sous Linux.

## Installation
Les outils ligne de commande OpenStack sont pour Python et fonctionnent sur un ordinateur personnel ou sur une instance infonuagique. Les différentes distributions  de Linux peuvent offrir des paquets précompilés; pour les détails, consultez la [documentation d'installation](https://docs.openstack.org/user-guide/common/cli-install-openstack-command-line-clients.html). Si vous avez les permissions d'administrateur, vous pouvez rapidement installer Python et les outils ligne de commande OpenStack.

; Ubuntu
<pre>
sudo apt-get install python python-dev python-pip
sudo pip install python-openstackclient
</pre>
; CentOS 7
Exécuter en tant que root.
<pre>
yum install epel-release
yum install gcc python python-dev python2-pip
pip install python-openstackclient
</pre>
; Fedora
<pre>
sudo dnf install python-openstackclient
</pre>
; Note: Si vous ne possédez pas les permissions d'administrateur, vous devez installer Python et [pip](https://pip.pypa.io/en/latest/installing/) autrement. Une fois l'installation complétée, vous pouvez installer les outils ligne de commande dans votre espace *home* comme suit&nbsp;:
<pre>
pip install --user python-openstackclient
</pre>
: La destination de l'installation est probablement incluse dans le `$PATH`; vous pouvez cependant vérifier si `~/.bashrc` ou `~/.bash_profile` inclut la ligne `PATH=$PATH:$HOME/.local/bin:$HOME/bin`.

; SDK
Pour explorer les [APIs pour Python](http://docs.openstack.org/user-guide/sdk.html), ajoutez `export PYTHONPATH=${HOME}/.local/lib/python2.7/site-packages/:${PYTHONPATH}` et modifiez  `python2.7` en fonction de la version de Python installée.

## Connecter le client ligne de commande à OpenStack
Vous devez indiquer au client où trouver le projet OpenStack dans notre environnement infonuagique. 
Le moyen le plus simple est de télécharger un fichier de configuration via le tableau de bord OpenStack, ainsi&nbsp;: *Projet -> Accès API -> Télécharger le fichier RC d’OpenStack*. 

Exécutez ensuite la commande 
```bash
source <project name>-openrc.sh
```
. Lorsque vous devez entrer le mot de passe OpenStack, entrez votre mot de passe pour notre base de données CCDB. Pour tester la configuration, entrez 
```bash
openstack image list
```
.

Si vous utilisez plusieurs fichiers RC, méfiez-vous des variables d'environnement qui subsisteraient du dernier fichier RC utilisé car elles pourraient empêcher l'exécution des commandes client OpenStack. Vous pouvez contourner ce problème de deux manières&nbsp;: en détruisant les variables avec <code>unset <variable-name></code> ou en démarrant une nouvelle session sans variables définies.

## Exécuter les commandes
Le client ligne de commande peut être utilisé interactivement en entrant

```bash
openstack
```

Entrez ensuite les commandes à l'invite. Chaque commande peut être entrée individuellement en la faisant précéder de `openstack`, par exemple

```bash
openstack server list
```

En mode interactif, faites afficher la liste des commandes disponibles en entrant `help`  à l'invite OpenStack. Les commandes disponibles sont classées en groupes; les plus communes sont présentées plus loin. Pour obtenir la liste des commandes appartenant à un groupe particulier, entrez <code>help <command group></code>. Pour obtenir les options et arguments liés à une commande, entrez <code>help <command group> <command></code>. Sachez que plusieurs commandes ne sont disponibles qu'aux utilisateurs ayant les permissions d'administrateur et que dans le cas contraire, un message d'erreur sera affiché. Les commandes qui suivent sont disponibles pour tous les utilisateurs.

## Groupes de commandes
### Commandes `server`
{|-
|	`add security group`  ||	`migrate`	||	`resume`	||	`unlock`
|-
|	`add volume`	||	`pause`	||	`set`	||	`unpause`
|-
|	`create`	||	`reboot`	||	`shelve`	||	`unrescue`
|-
|	`delete`	||	`rebuild`	||	`show`	||	`unset`
|-
|	`dump create`	||	`remove security group`	||	`ssh`	||	`unshelve`
|-
|	`image create`	||	`remove volume`        	||	`start`	||	
|-
|	`list`	||	`rescue`  	||	`stop`		
|-
|	`lock`	||	`resize`	||	`suspend`		
|}

### Commandes `volume`
{|-
|`create`||`set`
|-
|`delete`||`show`
|-
|`list`||`unset`
|}

### Commandes `console`
{|-
|`log show`||`url show`
|}
### Commandes `flavor`
{|-
|`list`||`show`
|}
### Commandes `image`
{|-
|`create`
|`save`
|-
|`delete`
|`set`
|-
|`list`
|`show`
|}

### Commandes `ip`
{|-
|`fixed add`||`floating list`
|-
|`fixed remove`||`floating pool list`
|-
|`floating add`||`floating remove`
|-
|`floating create`||`floating show`
|-
|`floating delete`
|}
### Commandes `keypair`
{|-
|`create`||`list`
|-
|`delete`||`show`
|}

### Commandes `network`
{|-
|`create`||`set`
|-
|`delete`||`show`
|-
|`list`||
|}

### Commandes `snapshot`
{|-
|`create`||`set`
|-
|`delete`||`show`
|-
|`list`||`unset`
|}

### Commandes `security group`
{|-
|`create`||`rule list`
|-
|`delete`||`rule show`
|-
|`list`||`set`
|-
|`rule create`||`show`
|-
|`rule delete`||
|}

### Commandes `limits`
{|-
|`show`||
|}
<!--These two (container and object) are not widely publicized
### container
{|-
|`create`||`set`
|-
|`delete`||`show`
|-
|`list`||`unset`
|-
|`save`
|}
### object
{|-
|`create`||`show`
|-
|`delete`||`store account set`
|-
|`list`||`store account show`
|-
|`save`||`store account unset`
|-
|`set`||`unset`
|}
-->

## Autres interfaces
En plus de la commande `openstack` (décrite ci-dessus) qui incorpore dans une même commande la plupart des fonctionnalités, il existe aussi des commandes distinctes pour les divers composants OpenStack qui ajoutent d'autres fonctionnalités. Ces commandes sont installées en même temps que la commande `openstack` et aucune autre installation n'est nécessaire. Ces commandes sont :
* [`nova`](https://docs.openstack.org/python-novaclient/latest/cli/nova.html) pour travailler avec des serveurs;
* [`glance`](https://docs.openstack.org/python-glanceclient/latest/cli/glance.html) pour travailler avec des images;
* [`cinder`](https://docs.openstack.org/python-cinderclient/latest/user/shell.html) pour travailler avec des volumes;
* [`heat`](https://docs.openstack.org/python-heatclient/latest/man/heat.html) pour travailler avec l'orchestration.