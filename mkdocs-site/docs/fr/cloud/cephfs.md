---
title: "CephFS/fr"
slug: "cephfs"
lang: "fr"

source_wiki_title: "CephFS/fr"
source_hash: "f624f2d171a2524668d8220b88ab99c7"
last_synced: "2026-08-07T19:46:17.777436+00:00"
last_processed: "2026-08-07T22:28:19.788101+00:00"

tags:
  - cloud

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: true
  qa_generated: false
---

Le système de fichiers CephFS peut être partagé par plusieurs hôtes d'instances OpenStack. Pour profiter de ce service, faites une demande à [nuage@tech.alliancecan.ca](mailto:nuage@tech.alliancecan.ca).

La procédure est plutôt technique et nécessite des compétences Linux de base pour créer et modifier des fichiers, définir des permissions et créer des points de montage. Si vous avez besoin d’assistance, écrivez à [nuage@tech.alliancecan.ca](mailto:nuage@tech.alliancecan.ca).

## Procédure

!!! note "Remarque"
    Plusieurs chaînes de caractères de l’interface OpenStack ne sont pas traduites en français.

## Demander l’accès aux points de partage (*shares*)

Si vous ne disposez pas déjà d’un quota pour ce service, écrivez à [nuage@tech.alliancecan.ca](mailto:nuage@tech.alliancecan.ca) et indiquez :

*   le nom du projet OpenStack
*   la capacité du quota requis (en Go)
*   le nombre de points de partage requis

## Configuration OpenStack : Créer un point de partage CephFS

### Créez un point de partage.

*   Dans *Projet --> Partage --> Partages*, cliquez sur *+Créer un partage*.
*   *Nom du partage* = entrez un nom significatif pour votre projet (par exemple *nom-du-projet-nom-du-partage*)
*   *Protocole de partage* = CephFS
*   *Taille* = taille requise pour le point de partage
*   *Type de partage* = cephfs (ou cephfs-ec42 pour SD4H/Juno)
*   *Zone de disponibilité* = nova
*   Ne sélectionnez pas *Rendre visible pour tous* ou *Rendre visible aux utilisateurs de tous les projets* pour SD4H/Juno, autrement le point de partage sera accessible par tous les utilisateurs dans tous les projets.
*   Cliquez sur le bouton *Créer*.

### Créez une règle pour générer une clé.

*   Dans *Projet --> Partage --> Partages --> colonne Actions*, sélectionnez *Gérer les règles* du menu déroulant.
*   Cliquez sur le bouton *+Ajouter une règle* à droite de la page.
*   *Type d'accès* = cephx
*   *Niveau d'accès* = sélectionnez *lecture-écriture* ou *lecture seule* (vous pouvez créer plusieurs règles à plusieurs niveaux)
*   *Accès à* = entrez un nom significatif pour la clé; ce nom est important parce qu'il sera utilisé dans la configuration du client CephFS (ici le nom est *MyCephFS-RW*).

### Prenez note des détails dont vous aurez besoin.

*   Dans *Projet --> Partage --> Partages*, cliquez sur le nom du point de partage.
*   Dans *Aperçu du partage*, notez les trois éléments suivants :
    *   *Chemin* qui servira à la commande `mount` pour l'instance;
    *   *Accès à* qui sera le nom du client;
    *   *Clé d'accès* qui permettra à l'instance cliente de se connecter.

## Attacher le réseau CephFS à votre instance

### Sur Arbutus

Le réseau CephFS est déjà disponible pour vos instances et donc vous n'avez rien à faire. Allez à [Configuration d'une instance : installer et configurer un client CephFS](#configuration-dune-instance-installer-et-configurer-un-client-cephfs) ci-dessous.

### Sur SD4H/Juno

Vous devez attacher le réseau CephFS à l'instance.

#### Sur l'interface web

Pour chaque instance, sélectionnez *Instance --> Action --> Attacher une interface --> Réseau CephFS*. Ne cochez pas la case *Adresse IP fixe*.

#### Avec le [client OpenStack](openstack_command_line_clients.md)

Faites afficher la liste des serveurs et sélectionnez l'identifiant de celui que vous voulez attacher à CephFS.

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

Sélectionnez l'identifiant de l'instance que vous voulez attacher, choisissez la première et lancez :

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

### Paquets requis pour la famille Red Hat Enterprise Linux (RHEL, CentOS, Fedora, Rocky, Alma)

Vérifiez quelles versions sont disponibles sur [https://download.ceph.com/](https://download.ceph.com/) et trouvez les répertoires `rpm-*` récents.
Depuis juin 2026, `tentacle` est la plus récente version stable.
Les distributions compatibles sont listées dans [https://download.ceph.com/rpm-tentacle/](https://download.ceph.com/rpm-tentacle/).

#### Ajouter le dépôt de logiciels

Selon la version de Enterprise Linux que vous utilisez, ajoutez le fichier suivant :

=== "el9"

    ```ini {data="name=/etc/yum.repos.d/ceph.repo"}
    [Ceph]
    name=Ceph packages for $basearch
    baseurl=http://download.ceph.com/rpm-tentacle/el9/$basearch
    enabled=1
    gpgcheck=1
    type=rpm-md
    gpgkey=https://download.ceph.com/keys/release.asc

    [Ceph-noarch]
    name=Ceph noarch packages
    baseurl=http://download.ceph.com/rpm-tentacle/el9/noarch
    enabled=1
    gpgcheck=1
    type=rpm-md
    gpgkey=https://download.ceph.com/keys/release.asc

    [ceph-source]
    name=Ceph source packages
    baseurl=http://download.ceph.com/rpm-tentacle/el9/SRPMS
    enabled=1
    gpgcheck=1
    type=rpm-md
    gpgkey=https://download.ceph.com/keys/release.asc
    ```

=== "el10"

    ```ini {data="name=/etc/yum.repos.d/ceph.repo"}
    [Ceph]
    name=Ceph packages for $basearch
    baseurl=http://download.ceph.com/rpm-tentacle/el10/$basearch
    enabled=1
    gpgcheck=1
    type=rpm-md
    gpgkey=https://download.ceph.com/keys/release.asc

    [Ceph-noarch]
    name=Ceph noarch packages
    baseurl=http://download.ceph.com/rpm-quincy/el9/noarch
    enabled=1
    gpgcheck=1
    type=rpm-md
    gpgkey=https://download.ceph.com/keys/release.asc

    [ceph-source]
    name=Ceph source packages
    baseurl=http://download.ceph.com/rpm-quincy/el9/SRPMS
    enabled=1
    gpgcheck=1
    type=rpm-md
    gpgkey=https://download.ceph.com/keys/release.asc
    ```

#### Installer les dépendances nécessaires pour accéder aux paquets

Installez le dépôt Extra Packages for Enterprise Linux (EPEL).

```bash
sudo dnf install epel-release
```

Si vous utilisez el10, vous devez désactiver temporairement la politique de chiffrement par défaut à cause du mode de signature des paquets Ceph.

Importez la clé publique du projet Ceph nécessaire pour vérifier les signatures de chiffrement des paquets logiciels.

```bash
sudo rpm --import 'https://download.ceph.com/keys/release.asc'
```

Vous pouvez maintenant installer ceph lib, cephfs client et autres dépendances.

```bash
sudo dnf install -y libcephfs2 python3-cephfs ceph-common python3-ceph-argparse
```

Si vous avez désactivé la politique de chiffrement par défaut, vous devez la rétablir avec :

```bash
sudo update-crypto-policies --set DEFAULT
```

### Paquets requis pour la famille Debian (Debian, Ubuntu, Mint, etc.)

Pour avoir le dépôt de paquets, trouvez le `{codename}` pour votre distribution avec `lsb_release -sc`.

```bash
sudo apt-add-repository 'deb https://download.ceph.com/debian-tentacle/ {codename} main'
```

Si la commande précédente produit une erreur, utilisez plutôt la commande suivante, puis passez à la prochaine étape.

```bash
sudo add-apt-repository -r 'deb https://download.ceph.com/debian-tentacle/ {codename} main'
```

Vous pouvez maintenant installer ceph lib, cephfs client et les autres dépendances.

```bash
sudo apt-get install -y libcephfs2 python3-cephfs ceph-common python3-ceph-argparse
```

### Configurer le client Ceph

Quand le client est installé, créez le fichier `ceph.conf`.
La valeur de `mon host` est différente selon le nuage.

=== "Arbutus"

    ```ini {data="name=/etc/ceph/ceph.conf"}
    [global]
    admin socket = /var/run/ceph/$cluster-$name-$pid.asok
    client reconnect stale = true
    debug client = 0/2
    fuse big writes = true
    mon host = [v2:134.87.15.61:3300/0,v1:134.87.15.61:6789/0] [v2:134.87.15.62:3300/0,v1:134.87.15.62:6789/0] [v2:134.87.15.63:3300/0,v1:134.87.15.63:6789/0]
    [client]
    quota = true
    ```

=== "SD4H/Juno"

    ```ini {data="name=/etc/ceph/ceph.conf"}
    [global]
    admin socket = /var/run/ceph/$cluster-$name-$pid.asok
    client reconnect stale = true
    debug client = 0/2
    fuse big writes = true
    mon host = 10.65.0.10:6789,10.65.0.12:6789,10.65.0.11:6789
    [client]
    quota = true
    ```

Les informations sur le moniteur se trouvent dans le champ *Chemin* des détails du partage qui sera utilisé pour monter le volume. Si la valeur de l'interface web est différente de ce qui est montré ici, cela signifie que la page wiki n'est pas à jour.

Entrez le nom du client et le secret dans le fichier `ceph.keyring`.

```ini {data="name=/etc/ceph/ceph.keyring"}
[client.MyCephFS-RW]
    key = <Access Key>
```

Encore une fois, la clé d'accès et le nom du client (ici *MyCephFS-RW*) se trouvent sous les règles d'accès sur l'interface web de votre projet.
Cliquez sur *Projet --> Partage --> Partages*, puis cliquez sur le nom du point de partage.

#### Récupérer les informations de connexion pour votre partage :

*   Ouvrez les détails en cliquant sur le nom du point de partage dans la page *Partages*.
*   De la page, copiez la partie du *Chemin* qui contient `:` que nous allons utiliser pour monter le système de fichiers (par exemple ici, `:/volumes/_nogroup/f6cb8f06-f0a4-4b88-b261-f8bd6b03582c`).

#### Monter le système de fichiers

*   Créez un répertoire pour le point de montage quelque part sur votre hôte (ici `/cephfs`).

```bash
mkdir /cephfs
```

*   Vous pouvez utiliser le pilote Ceph pour monter votre périphérique CephFS de façon permanente en ajoutant ce qui suit dans le fstab de l'instance.

=== "Arbutus"

    ```text {data="name=/etc/fstab"}
    :/volumes/_nogroup/f6cb8f06-f0a4-4b88-b261-f8bd6b03582c /cephfs/ ceph name=MyCephFS-RW,nofail 0  2
    ```

=== "SD4H/Juno"

    ```text {data="name=/etc/fstab"}
    :/volumes/_nogroup/f6cb8f06-f0a4-4b88-b261-f8bd6b03582c /cephfs/ ceph name=MyCephFS-RW,mds_namespace=cephfs_4_2,x-systemd.device-timeout=30,x-systemd.mount-timeout=30,noatime,_netdev,rw,nofail 0  2
    ```

**Remarque** : le caractère `:` non standard devant le chemin d'accès au périphérique n'est pas une erreur de frappe.
Les options de montage sont différentes selon les systèmes.
L'option `namespace` est requise pour SD4H/Juno, tandis que les autres options sont des ajustements de performance. L'option `nofail` fait en sorte que le système pourra être amorcé dans le cas peu probable où CephFS n'est pas disponible ou ne puisse pas être rejoint.

Vous pouvez aussi faire le montage directement en ligne de commande.

=== "Arbutus"

    ```bash
    sudo mount -t ceph :/volumes/_nogroup/f6cb8f06-f0a4-4b88-b261-f8bd6b03582c /cephfs/ -o name=MyCephFS-RW
    ```

=== "SD4H/Juno"

    ```bash
    sudo mount -t ceph :/volumes/_nogroup/f6cb8f06-f0a4-4b88-b261-f8bd6b03582c /cephfs/ -o name=MyCephFS-RW,mds_namespace=cephfs_4_2,x-systemd.device-timeout=30,x-systemd.mount-timeout=30,noatime,_netdev,rw
    ```

CephFS peut aussi être monté directement dans votre espace de travail via ceph-fuse.

Installez la bibliothèque ceph-fuse.

```bash
sudo dnf install ceph-fuse
```

Pour que le montage soit disponible dans votre espace utilisateur, décommentez `user_allow_other` dans le fichier `fuse.conf`.

```text {data="name=/etc/fuse.conf"}
# mount_max = 1000
user_allow_other
```

Vous pouvez maintenant monter cephFS dans votre espace `/home`.

```bash
mkdir ~/my_cephfs
ceph-fuse my_cephfs/ --id=MyCephFS-RW --conf=~/ceph.conf --keyring=~/ceph.keyring   --client-mountpoint=/volumes/_nogroup/f6cb8f06-f0a4-4b88-b261-f8bd6b03582c
```

Notez que le nom du client est ici le `--id`. Le contenu de `ceph.conf` et de `ceph.keyring` est exactement le même que pour le montage du noyau Ceph.

## Remarques

Un point de partage particulier peut disposer de plusieurs clés utilisateur. Cela permet un accès plus précis au système de fichiers, par exemple si vous avez besoin que certains hôtes accèdent au système de fichiers uniquement en lecture seule. Si vous disposez de plusieurs clés pour un point de partage, vous pouvez ajouter les clés supplémentaires à votre hôte et modifier la procédure de montage ci-dessus. Ce service n'est pas disponible pour les hôtes extérieurs à la grappe OpenStack.