---
title: "CephFS/fr"
slug: "cephfs"
lang: "fr"

source_wiki_title: "CephFS/fr"
source_hash: "0b958d798604aba3b02283aac6487c26"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:13:32.168557+00:00"

tags:
  - cloud

keywords:
  - "réseau"
  - "point de partage"
  - "Cloud"
  - "client CephFS"
  - "client Ceph"
  - "dépôt de paquets"
  - "attacher le réseau CephFS"
  - "instance"
  - "client OpenStack"
  - "Configuration d'une instance"
  - "Enterprise Linux 8"
  - "client ceph"
  - "Enterprise Linux 9"
  - "SD4H/Juno"
  - "OpenStack"
  - "fstab"
  - "règles d'accès"
  - "nom du client"
  - "ceph-fuse"
  - "dépôts de paquets"
  - "configuration"
  - "Category"
  - "Ceph"
  - "ceph.conf"
  - "informations de connexion"
  - "CephFS"
  - "configurations"
  - "point de montage"
  - "points de partage"
  - "clé d'accès"
  - "hôtes"
  - "Attach interface"
  - "système de fichiers"
  - "grappe OpenStack"
  - "lecture seule"

questions:
  - "Quelles sont les informations à fournir lors de la demande initiale pour obtenir un quota et l'accès au service CephFS ?"
  - "Quelles sont les étapes de configuration requises dans l'interface OpenStack pour créer un point de partage et générer une clé d'accès ?"
  - "Comment la procédure d'attachement du réseau CephFS à une instance varie-t-elle selon que l'on utilise l'environnement Arbutus ou SD4H/Juno ?"
  - "Quel réseau doit-on impérativement attacher à l'instance lors de la configuration sous SD4H/Juno ?"
  - "Quel est le chemin de navigation exact à suivre sur l'interface web pour lier ce réseau à l'instance ?"
  - "Quelle case spécifique ne faut-il surtout pas cocher lors de l'attachement de l'interface ?"
  - "Comment utiliser le client en ligne de commande OpenStack pour attacher un réseau CephFS à une instance spécifique ?"
  - "Comment identifier les versions stables récentes des paquets Ceph disponibles pour votre distribution Linux ?"
  - "Quelles sont les étapes pour configurer les dépôts de paquets YUM sur une instance de la famille Red Hat afin d'installer un client CephFS ?"
  - "Quelles sont les versions du système d'exploitation Enterprise Linux ciblées par ces exemples de configuration ?"
  - "Quel est l'objectif principal de l'installation décrite dans ce document ?"
  - "Quel est le chemin exact du fichier de configuration utilisé pour définir le dépôt Ceph sous Enterprise Linux 8 ?"
  - "Comment installer les paquets et les dépendances nécessaires pour le client Ceph selon la distribution Linux (Enterprise Linux ou Debian) utilisée ?"
  - "Quelles informations doivent être configurées dans le fichier ceph.conf et comment définir la valeur \"mon host\" selon le nuage (Arbutus, SD4H/Juno) ?"
  - "Où l'utilisateur peut-il récupérer le nom du client et la clé d'accès pour configurer correctement le fichier d'authentification ceph.keyring ?"
  - "Comment configurer le montage permanent d'un système de fichiers CephFS en utilisant le fichier fstab ?"
  - "Quelles sont les étapes nécessaires pour monter CephFS dans l'espace utilisateur avec l'outil ceph-fuse ?"
  - "Comment gérer les différents niveaux d'accès au point de partage et quelles sont les restrictions d'utilisation de ce service en dehors de la grappe OpenStack ?"
  - "Quel est le format requis pour renseigner le nom du client et la clé d'accès dans le fichier ceph.keyring ?"
  - "À quel endroit précis sur la page Web du projet peut-on récupérer la clé d'accès et le nom du client ?"
  - "Quelles sont les étapes de navigation dans l'interface pour accéder à la page contenant les informations de connexion du point de partage ?"
  - "Comment le système permet-il de restreindre ou de préciser l'accès au système de fichiers pour certains hôtes ?"
  - "Que doit faire un utilisateur s'il dispose de plusieurs clés pour un même point de partage ?"
  - "Quelles sont les limites de disponibilité de ce service pour les hôtes n'appartenant pas à l'infrastructure OpenStack ?"
  - "What is the specific purpose of the \"[[Category:Cloud]]\" tag within the structure of this document?"
  - "What types of information or topics are expected to be classified under this \"Cloud\" category?"
  - "How does assigning this text to the \"Cloud\" category impact its discoverability and organization?"
  - "What is the specific purpose of the \"[[Category:Cloud]]\" tag within the structure of this document?"
  - "What types of information or topics are expected to be classified under this \"Cloud\" category?"
  - "How does assigning this text to the \"Cloud\" category impact its discoverability and organization?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Le système de fichiers CephFS peut être partagé par plusieurs hôtes d'instances OpenStack. Pour profiter de ce service, faites une demande à [nuage@tech.alliancecan.ca](mailto:nuage@tech.alliancecan.ca).

La procédure est plutôt technique et nécessite des compétences Linux de base pour créer et modifier des fichiers, définir des permissions et créer des points de montage. Si vous avez besoin d’assistance, écrivez à [nuage@tech.alliancecan.ca](mailto:nuage@tech.alliancecan.ca).

## Procédure

!!! warning "Remarque"
    Plusieurs chaînes de caractères de l’interface OpenStack ne sont pas traduites en français.

## Demander l’accès aux points de partage (partages)

Si vous ne disposez pas déjà d’un quota pour ce service, écrivez à [nuage@tech.alliancecan.ca](mailto:nuage@tech.alliancecan.ca) et indiquez :
*   le nom du projet OpenStack
*   la capacité du quota requis (en Go)
*   le nombre de points de partage requis

## Configuration OpenStack : Créer un point de partage CephFS

**Créez un point de partage.**
Dans *Projet --> Partage --> Partages*, cliquez sur *+Créer un partage*.
*   *Nom du partage* = entrez un nom significatif pour votre projet (par exemple *nom-du-projet-nom-du-partage*)
*   *Protocole de partage* = CephFS
*   *Taille* = taille requise pour le point de partage
*   *Type de partage* = cephfs (ou cephfs-ec42 pour SD4H/Juno)
*   *Zone de disponibilité* = nova
*   Ne sélectionnez pas *Rendre visible pour tous* ou *Rendre visible aux utilisateurs de tous les projets* pour SD4H/Juno, autrement le point de partage sera accessible par tous les utilisateurs dans tous les projets.
*   Cliquez sur le bouton *Créer*.

**Créez une règle pour générer une clé.**
Dans *Projet --> Partage --> Partages --> colonne Actions*, sélectionnez *Gérer les règles* du menu déroulant.
*   Cliquez sur le bouton *+Ajouter une règle* à droite de la page.
*   *Type d'accès* = cephx
*   *Niveau d'accès* = sélectionnez *lecture-écriture* ou *lecture seule* (vous pouvez créer plusieurs règles à plusieurs niveaux)
*   *Accéder à* = entrez un nom significatif pour la clé; ce nom est important parce qu'il sera utilisé dans la configuration du client CephFS (ici le nom est *MyCephFS-RW*).

**Prenez note des détails dont vous aurez besoin.**
Dans *Projet --> Partage --> Partages*, cliquez sur le nom du point de partage.
Dans *Aperçu du partage*, notez les trois éléments encerclés en rouge dans l'image ci-dessus :
*Chemin d'accès* qui servira à la commande `mount` pour l'instance; *Accéder à* qui sera le nom du client; et *Clé d'accès* qui permettra à l'instance client de se connecter.

## Attacher le réseau CephFS à votre instance

### Sur Arbutus

Le réseau CephFS est déjà disponible pour vos instances et donc vous n'avez rien à faire. Allez à [Configuration d'une instance : installer et configurer un client CephFS](#configuration-dune-instance-installer-et-configurer-un-client-cephfs) ci-dessous.

### Sur SD4H/Juno

Vous devez attacher le réseau CephFS à l'instance.

**Sur le web**
Pour chaque instance, sélectionnez *Instance --> Action --> Attacher une interface --> Réseau CephFS*. Ne cochez pas la case *Adresse IP fixe*.

**Avec le [client OpenStack](openstack-command-line-clients.md)**
Faites afficher la liste des serveurs et sélectionnez l'identifiant de celui que vous voulez attacher au réseau CephFS.
```bash
$ openstack  server list 
+--------------------------------------+--------------+--------+-------------------------------------------+--------------------------+----------+
| ID                                   | Name         | Status | Networks                                  | Image                    | Flavor   |
+--------------------------------------+--------------+--------+-------------------------------------------+--------------------------+----------+
| 1b2a3c21-c1b4-42b8-9016-d96fc8406e04 | prune-dtn1   | ACTIVE | test_network=172.16.1.86, 198.168.189.3   | N/A (booted from volume) | ha4-15gb |
| 0c6df8ea-9d6a-43a9-8f8b-85eb64ca882b | prune-mgmt1  | ACTIVE | test_network=172.16.1.64                  | N/A (booted from volume) | ha4-15gb |
| 2b7ebdfa-ee58-4919-bd12-647a382ec9f6 | prune-login1 | ACTIVE | test_network=172.16.1.111, 198.168.189.82 | N/A (booted from volume) | ha4-15gb |
+--------------------------------------+--------------+--------+----------------------------------------------+--------------------------+----------+
```
Sélectionnez l'identifiant de l'instance que vous voulez attacher (par exemple, la première) et lancez :
```bash
$ openstack  server add network 1b2a3c21-c1b4-42b8-9016-d96fc8406e04 CephFS-Network
$ openstack  server list 
+--------------------------------------+--------------+--------+---------------------------------------------------------------------+--------------------------+----------+
| ID                                   | Name         | Status | Networks                                                            | Image                    | Flavor   |
+--------------------------------------+--------------+--------+---------------------------------------------------------------------+--------------------------+----------+
| 1b2a3c21-c1b4-42b8-9016-d96fc8406e04 | prune-dtn1   | ACTIVE | CephFS-Network=10.65.20.71; test_network=172.16.1.86, 198.168.189.3 | N/A (booted from volume) | ha4-15gb |
| 0c6df8ea-9d6a-43a9-8f8b-85eb64ca882b | prune-mgmt1  | ACTIVE | test_network=172.16.1.64                                            | N/A (booted from volume) | ha4-15gb |
| 2b7ebdfa-ee58-4919-bd12-647a382ec9f6 | prune-login1 | ACTIVE | test_network=172.16.1.111, 198.168.189.82                           | N/A (booted from volume) | ha4-15gb |
+--------------------------------------+--------------+--------+------------------------------------------------------------------------+--------------------------+----------+
```
Nous remarquons que le réseau CephFS est attaché à la première instance.

## Configuration d'une instance : installer et configurer un client CephFS

### Paquets requis pour la famille Red Hat (RHEL, CentOS, Fedora, Rocky, Alma Linux)

Vérifiez quelles versions sont disponibles sur [https://download.ceph.com/](https://download.ceph.com/) et trouvez les répertoires `rpm-*` récents.
Depuis juillet 2024, `quincy` est la version stable la plus récente.
Les distributions compatibles sont listées dans [https://download.ceph.com/rpm-quincy/](https://download.ceph.com/rpm-quincy/).
Nous montrons ici des exemples de configurations pour `Enterprise Linux 8` et `Enterprise Linux 9`.

**Installation des dépôts de paquets donnant accès aux paquets d'un client Ceph**

=== "Enterprise Linux 8 - el8"

    ```ini title="/etc/yum.repos.d/ceph.repo"
    [Ceph]
    name=Ceph packages for $basearch
    baseurl=http://download.ceph.com/rpm-quincy/el8/$basearch
    enabled=1
    gpgcheck=1
    type=rpm-md
    gpgkey=https://download.ceph.com/keys/release.asc

    [Ceph-noarch]
    name=Ceph noarch packages
    baseurl=http://download.ceph.com/rpm-quincy/el8/noarch
    enabled=1
    gpgcheck=1
    type=rpm-md
    gpgkey=https://download.ceph.com/keys/release.asc

    [ceph-source]
    name=Ceph source packages
    baseurl=http://download.ceph.com/rpm-quincy/el8/SRPMS
    enabled=1
    gpgcheck=1
    type=rpm-md
    gpgkey=https://download.ceph.com/keys/release.asc
    ```

=== "Enterprise Linux 9 - el9"

    ```ini title="/etc/yum.repos.d/ceph.repo"
    [Ceph]
    name=Ceph packages for $basearch
    baseurl=http://download.ceph.com/rpm-quincy/el9/$basearch
    enabled=1
    gpgcheck=1
    type=rpm-md
    gpgkey=https://download.ceph.com/keys/release.asc
    ```

Le dépôt EPEL doit être présent.
```bash
sudo dnf install epel-release
```
Vous pouvez maintenant installer la bibliothèque Ceph, le client CephFS et d'autres dépendances.
```bash
sudo dnf install -y libcephfs2 python3-cephfs ceph-common python3-ceph-argparse
```

### Paquets requis pour la famille Debian (Debian, Ubuntu, Mint, etc.)

Pour configurer le dépôt de paquets, trouvez le `codename` pour votre distribution avec `lsb_release -sc`.
```bash
sudo apt-add-repository 'deb https://download.ceph.com/debian-quincy/ {codename} main'
```
Si la commande précédente produit une erreur, utilisez plutôt la commande suivante, puis passez à la prochaine étape.
```bash
sudo add-apt-repository -r 'deb https://download.ceph.com/debian-quincy/ {codename} main'
```
Vous pouvez maintenant installer la bibliothèque Ceph, le client CephFS et les autres dépendances.
```bash
sudo apt-get install -y libcephfs2 python3-cephfs ceph-common python3-ceph-argparse
```

### Configurer le client Ceph

Une fois le client installé, créez le fichier `ceph.conf`.
La valeur de `mon host` diffère selon l'environnement infonuagique.

=== "Arbutus"

    ```ini title="/etc/ceph/ceph.conf"
    [global]
    admin socket = /var/run/ceph/$cluster-$name-$pid.asok
    client reconnect stale = true
    debug client = 0/2
    fuse big writes = true
    mon host = 10.30.201.3:6789,10.30.202.3:6789,10.30.203.3:6789
    [client]
    quota = true
    ```

=== "SD4H/Juno"

    ```ini title="/etc/ceph/ceph.conf"
    [global]
    admin socket = /var/run/ceph/$cluster-$name-$pid.asok
    client reconnect stale = true
    debug client = 0/2
    fuse big writes = true
    mon host = 10.65.0.10:6789,10.65.0.12:6789,10.65.0.11:6789
    [client]
    quota = true
    ```

Les informations sur le moniteur se trouvent dans le champ *Chemin d'accès* des détails du partage qui sera utilisé pour monter le volume. Si la valeur affichée sur la page web diffère de ce qui est présenté ici, cela signifie que la page wiki n'est pas à jour.

Entrez le nom du client et la clé secrète dans le fichier `ceph.keyring`.

```ini title="/etc/ceph/ceph.keyring"
[client.MyCephFS-RW]
    key = <Access Key>
```

Encore une fois, la clé d'accès et le nom du client (ici *MyCephFS-RW*) se trouvent sous les règles d'accès sur la page web de votre projet.
Cliquez sur *Projet --> Partage --> Partages*, puis cliquez sur le nom du point de partage.

**Récupérez les informations de connexion dans la page *Partages* pour votre connexion :**
*   Ouvrez les détails en cliquant sur le nom du point de partage dans la page *Partages*.
*   De la page, copiez la partie de *Chemin d'accès* qui contient `:` que nous allons utiliser pour monter le système de fichiers (par exemple ici, `:/volumes/_nogroup/f6cb8f06-f0a4-4b88-b261-f8bd6b03582c`).

**Montez le système de fichiers**
*   Créez un répertoire pour le point de montage quelque part sur votre hôte (ici `/cephfs`).
```bash
mkdir /cephfs
```
*   Vous pouvez utiliser le pilote Ceph pour monter votre périphérique CephFS de façon permanente en ajoutant ce qui suit dans le fichier fstab de l'instance.

=== "Arbutus"

    ```txt title="/etc/fstab"
    :/volumes/_nogroup/f6cb8f06-f0a4-4b88-b261-f8bd6b03582c /cephfs/ ceph name=MyCephFS-RW,nofail 0  2
    ```

=== "SD4H/Juno"

    ```txt title="/etc/fstab"
    :/volumes/_nogroup/f6cb8f06-f0a4-4b88-b261-f8bd6b03582c /cephfs/ ceph name=MyCephFS-RW,mds_namespace=cephfs_4_2,x-systemd.device-timeout=30,x-systemd.mount-timeout=30,noatime,_netdev,rw,nofail 0  2
    ```

!!! tip "Remarque"
    Le caractère `:` non standard devant le chemin d'accès au périphérique n'est pas une erreur de frappe.
    Les options de montage sont différentes selon les systèmes.
    L'option `namespace` est requise pour SD4H/Juno, tandis que les autres options sont des ajustements de performance. L'option `nofail` fait en sorte que le système pourra être amorcé dans le cas peu probable où CephFS n'est pas disponible ou ne peut pas être rejoint.

Vous pouvez aussi faire le montage directement en ligne de commande.

=== "Arbutus"

    ```bash
    sudo mount -t ceph :/volumes/_nogroup/f6cb8f06-f0a4-4b88-b261-f8bd6b03582c /cephfs/ -o name=MyCephFS-RW
    ```

=== "SD4H/Juno"

    ```bash
    sudo mount -t ceph :/volumes/_nogroup/f6cb8f06-f0a4-4b88-b261-f8bd6b03582c /cephfs/ -o name=MyCephFS-RW,mds_namespace=cephfs_4_2,x-systemd.device-timeout=30,x-systemd.mount-timeout=30,noatime,_netdev,rw
    ```

CephFS peut aussi être monté directement dans votre espace de travail via `ceph-fuse`.

Installez la bibliothèque `ceph-fuse`.

```bash
sudo dnf install ceph-fuse
```
Pour que le montage soit disponible dans votre espace utilisateur, retirez le commentaire de l'option `user_allow_other` dans le fichier `fuse.conf`.

```txt title="/etc/fuse.conf"
# mount_max = 1000
user_allow_other
```

Vous pouvez maintenant monter CephFS dans votre espace /home.
```bash
mkdir ~/my_cephfs
ceph-fuse my_cephfs/ --id=MyCephFS-RW --conf=~/ceph.conf --keyring=~/ceph.keyring   --client-mountpoint=/volumes/_nogroup/f6cb8f06-f0a4-4b88-b261-f8bd6b03582c
```
Notez que le nom du client est ici l'argument `--id`. Le contenu de `ceph.conf` et de `ceph.keyring` est exactement le même que pour le montage du noyau Ceph.

## Remarques

Un point de partage particulier peut disposer de plusieurs clés d'utilisateur. Cela permet un accès plus précis au système de fichiers; par exemple, si vous avez besoin que certains hôtes accèdent au système de fichiers uniquement en lecture seule. Si vous disposez de plusieurs clés pour un point de partage, vous pouvez ajouter les clés supplémentaires à votre hôte et modifier la procédure de montage ci-dessus. Ce service n'est pas disponible pour les hôtes extérieurs à la grappe OpenStack.