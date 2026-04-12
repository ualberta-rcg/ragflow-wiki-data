---
title: "SSH tunnelling/fr"
slug: "ssh_tunnelling"
lang: "fr"

source_wiki_title: "SSH tunnelling/fr"
source_hash: "67945f0cef2bb533b514b71ce03b7d19"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:20:08.913683+00:00"

tags:
  []

keywords:
  - "localhost"
  - "application"
  - "Tunnel SSH"
  - "serveur de licence"
  - "port local"
  - "URL"
  - "port distant"
  - "Jupyter Notebook"
  - "serveur de base de données"
  - "PostgreSQL"
  - "MobaXTerm"
  - "nœud de calcul"
  - "tunnel SSH"
  - "variable d'environnement"
  - "port logiciel"
  - "MySQL"
  - "Redirection de port"
  - "port COMPUTEPORT"
  - "Nœud de calcul"
  - "redirection de port"
  - "Fir"

questions:
  - "Qu'est-ce qu'un tunnel SSH et dans quelles situations spécifiques est-il requis sur une grappe de calcul ?"
  - "Quelles informations préalables sont nécessaires pour établir une connexion avec un serveur de licence depuis un nœud de calcul ?"
  - "Quel est le rôle des paramètres -L, -N et -f dans la commande SSH utilisée pour configurer la redirection de port ?"
  - "Comment peut-on configurer un script pour établir un tunnel SSH vers un serveur de licences à partir d'un nœud de calcul ?"
  - "Quel outil est recommandé pour se connecter à une application exécutée sur un nœud de calcul depuis un système Linux ou MacOS X, et comment l'utiliser ?"
  - "Quelles sont les étapes à suivre dans MobaXTerm sous Windows pour créer un tunnel SSH et rediriger un port local vers un nœud de calcul ?"
  - "Quel est le but de la commande supplémentaire à ajouter concernant le port COMPUTEPORT ?"
  - "Que signifie le terme \"localhost\" et quelle erreur courante doit-on éviter lors de son utilisation ?"
  - "De quelle manière la procédure de configuration du serveur de licence s'effectue-t-elle généralement dans les scripts ?"
  - "Pourquoi est-il recommandé d'utiliser des numéros identiques pour le port local et le port distant ?"
  - "Quelle modification précise doit être apportée à l'URL obtenue lors de la session 1 ?"
  - "Quelle application est mentionnée comme exemple pour l'utilisation de cette URL dans le fureteur ?"
  - "Quelles commandes SSH permettent de créer un tunnel depuis un ordinateur local vers les serveurs PostgreSQL et MySQL sur Fir ?"
  - "Comment se connecte-t-on directement à la base de données depuis son ordinateur personnel une fois le tunnel établi ?"
  - "Où se trouve le mot de passe requis pour MySQL et de quoi dépend le maintien de la connexion à la base de données ?"
  - "Quelles commandes SSH permettent de créer un tunnel depuis un ordinateur local vers les serveurs PostgreSQL et MySQL sur Fir ?"
  - "Comment se connecte-t-on directement à la base de données depuis son ordinateur personnel une fois le tunnel établi ?"
  - "Où se trouve le mot de passe requis pour MySQL et de quoi dépend le maintien de la connexion à la base de données ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Page enfant de [SSH](ssh.md)*

## Description

Un tunnel SSH permet d’utiliser un ordinateur passerelle pour connecter deux ordinateurs qui ne peuvent pas être connectés directement l’un à l’autre.

Dans certains cas, il est nécessaire de mettre en place un tunnel puisque les nœuds de calcul de certaines grappes n’ont pas d’accès direct avec l’Internet ni ne peuvent être contactés directement via l’Internet.

Un tunnel sera requis dans les cas suivants :

* pour utiliser une application du commerce qui doit entrer en contact avec un serveur de licence via l’Internet;
* pour utiliser une application de [visualisation](visualization.md) sur un nœud de calcul avec lequel une application client sur l’ordinateur local d’un utilisateur doit entrer en contact;
* pour accéder à une base de données sur une grappe à partir d’un endroit autre que le nœud de connexion de cette grappe, par exemple votre ordinateur personnel.

Dans le premier cas, le serveur de licence est situé à l’extérieur de la grappe et est rarement contrôlé par l’utilisateur alors que dans les autres cas, le serveur se trouve dans le nœud de calcul et la difficulté est de s’y connecter à partir de l’extérieur. Nous traitons ici des deux situations.

Même si elles ne sont pas essentielles à l'utilisation de tunnels, vous pourriez vous familiariser avec les [clés SSH](ssh-keys.md).

## Entrer en contact avec un serveur de licence à partir d’un nœud de calcul

!!! tip "Qu’est-ce qu’un port?"
    Un port logiciel (identifié par son numéro) permet de distinguer différents interlocuteurs. Il s’agit en quelque sorte d’une fréquence radio ou d’un canal. Par obligation ou par convention, plusieurs de ces numéros sont réservés à des types particuliers de communication; pour plus d’information, consultez cette [liste de ports logiciels](https://fr.wikipedia.org/wiki/Liste_de_ports_logiciels).

Certaines applications du commerce doivent se connecter à un serveur de licence quelque part sur Internet à partir d’un port prédéterminé. Quand le nœud où une application est exécutée n’a pas accès à l’Internet, un serveur passerelle ayant accès est utilisé pour acheminer les communications par ce port, du nœud de calcul vers le serveur de licence. On met donc en place un tunnel SSH, pour effectuer une redirection de port (*port forwarding*).

Souvent, la mise en place d’un tunnel pour une tâche en série ne nécessite que deux ou trois commandes dans le script de la tâche. Vous aurez besoin

* de l’adresse IP ou nom du serveur de licence (ici LICSERVER);
* du numéro du port du serveur de licence (ici LICPORT).

Ces renseignements peuvent être obtenus de la personne qui gère le serveur de licence. Le serveur doit aussi permettre la connexion à partir des nœuds de connexion; dans le cas de Trillium, l’adresse IP vers l’extérieur est 142.150.188.58.

Le tunnel peut maintenant être mis en place. Sur Nibi, une autre solution serait de demander une exception de pare-feu pour LICSERVER et son port LICPORT. Le serveur de passerelle (GATEWAY) sur Trillium est tri-gw, tandis que sur Nibi vous devez choisir l'un des nœuds de connexion (l1, l2, ... l5). Vous devez également choisir le numéro de port (COMPUTEPORT) à utiliser sur le nœud de calcul. La commande SSH à exécuter dans le script de tâche est alors :

```bash
ssh GATEWAY -L COMPUTEPORT:LICSERVER:LICPORT -N -f
```

Les éléments à la suite du paramètre `-L` définissent les options de redirection :
* `-N` fait en sorte que SSH n’ouvre pas d’interpréteur sur GATEWAY;
* `-f` et `-N` empêchent SSH de lire les données en entrée (ce qui est néanmoins impossible pour une tâche de calcul);
* `-f` fait en sorte que SSH soit exécuté en arrière-plan et que les commandes qui suivent soient exécutées.

Une autre commande devrait être ajoutée pour que l’application sache que le serveur de licence se trouve sur le port COMPUTEPORT du serveur *localhost*. Le terme *localhost* est le nom avec lequel un ordinateur réfère à lui-même; il ne doit pas être remplacé par le nom de votre ordinateur. La procédure exacte varie selon l’application et le type de serveur de licence; par contre, il ne s’agit souvent que de définir une variable d’environnement dans le script, par exemple

```bash
export MLM_LICENSE_FILE=COMPUTEPORT@localhost
```

### Exemple de script

Le script suivant met en place un tunnel SSH pour entrer en contact avec `licenseserver.institution.ca` au port `9999`.

```bash
#!/bin/bash
#SBATCH --nodes 1
#SBATCH --ntasks 192
#SBATCH --time 3:00:00

REMOTEHOST=licenseserver.institution.ca
REMOTEPORT=9999
LOCALHOST=localhost
for ((i=0; i<10; ++i)); do
  LOCALPORT=$(shuf -i 1024-65535 -n 1)
  ssh tri-gw -L $LOCALPORT:$REMOTEHOST:$REMOTEPORT -N -f && break
done || { echo "Giving up forwarding license port after $i attempts..."; exit 1; }
export MLM_LICENSE_FILE=$LOCALPORT@$LOCALHOST

module load thesoftware/2.0
mpirun thesoftware .....
```

## Se connecter à une application qui est exécutée sur un nœud de calcul

Un tunnel crypté peut être mis en place dans un nœud de connexion d’une grappe pour connecter l’ordinateur d’un utilisateur à un nœud de calcul de cette grappe. L’ordinateur de l’utilisateur peut ainsi afficher de façon transparente des [visualisations](visualization.md) et des graphiques de [Jupyter Notebook](jupyter.md) exécutés dans un nœud de calcul de la grappe. Lorsque la seule façon d’accéder à un serveur de bases de données est par un nœud de connexion, un tunnel SSH peut transférer un port réseau arbitraire d’un nœud de calcul vers le nœud de connexion de la grappe et l’associer au serveur de bases de données.

Nibi et Fir effectuent une NAT (*network address translation*) pour que les utilisateurs puissent avoir accès à l’Internet à partir des nœuds de calcul.

### De Linux ou macOS X

Le paquet Python [sshuttle](https://sshuttle.readthedocs.io) est recommandé.

Sur votre ordinateur, ouvrez une nouvelle fenêtre de terminal et lancez la commande

```bash
sshuttle --dns -Nr userid@machine_name
```

Copiez et collez l’URL de l'application dans votre fureteur. Si votre application est [Jupyter Notebook](jupyter.md#lancer-jupyter-notebook) par exemple, l'URL comprendra un *token* :

```text
 http://fc3281.int.fir.alliancecan.ca:8888/?token=7ed7059fad64446f837567e32af8d20efa72e72476eb72ca
```

### De Windows

Un tunnel SSH peut être créé avec [MobaXTerm](connecting-with-mobaxterm.md) comme suit :

Lancez deux sessions MobaXterm.

*La session 1* devrait servir à la connexion à la grappe. Lancez ici votre tâche selon les directives de votre application, par exemple avec [Jupyter Notebook](jupyter.md#lancer-jupyter-notebook). Vous devriez recevoir une URL qui contient le nom et un port du nœud hôte, par exemple `fc3281.int.fir.alliancecan.ca:8888`.

*La session 2* est un terminal local dans lequel le tunnel SSH sera mis en place. Lancez la prochaine commande en remplaçant le nom du nœud par l'URL obtenue dans la session 1.

```bash
ssh -L 8888:fc3281.int.fir.alliancecan.ca:8888 someuser@fir.alliancecan.ca
```

Cette commande effectue une redirection des connexions au port local `8888` vers le port `8888` sur `fc3281.int.fir.alliancecan.ca`, nom donné au **port distant**. Il n'est pas nécessaire que les numéros soient identiques, mais il s'agit d'une convention qui permet d'identifier facilement le port local et le port distant.

Modifiez l'URL obtenue dans la session 1 en remplaçant le nom du nœud par `localhost`.
Suivant l'exemple avec [Jupyter Notebook](jupyter.md#lancer-jupyter-notebook), l'URL à copier dans le fureteur est :

```text
 http://localhost:8888/?token=7ed7059fad64446f837567e32af8d20efa72e72476eb72ca
```

### Se connecter à un serveur de base de données sur Fir à partir de votre ordinateur

Les commandes suivantes créent un tunnel SSH de votre ordinateur aux serveurs PostgreSQL et MySQL.

```bash
ssh -L PORT:cedar-pgsql-vm.int.cedar.computecanada.ca:5432 someuser@fir.alliancecan.ca
ssh -L PORT:cedar-mysql-vm.int.cedar.computecanada.ca:3306 someuser@fir.alliancecan.ca
```

Ces commandes connectent le numéro de port PORT de votre ordinateur local à `cedar.computecanada.ca:PORT`; la valeur du numéro de port doit être inférieure à `32768` (2^15). Dans cet exemple, *someuser* est le nom d’utilisateur associé à votre compte. En lançant une de ces commandes, vous serez connecté à Cedar comme toute autre connexion SSH. La seule différence entre cette connexion et une connexion SSH ordinaire est que vous pouvez ainsi utiliser un autre terminal pour vous connecter directement au serveur de base de données à partir de votre ordinateur personnel. Sur votre ordinateur personnel, exécuter la commande usuelle, par exemple pour PostgreSQL et MySQL :

```bash
psql -h 127.0.0.1 -p PORT -U <your username> -d <your database>
mysql -h 127.0.0.1 -P PORT -u <your username> --protocol=TCP -p
```

Un mot de passe est requis pour MySQL; il se trouve dans le fichier *.my.cnf* situé dans votre répertoire `/home` de Fir.
La connexion à la base de données est maintenue tant que la connexion SSH est active.