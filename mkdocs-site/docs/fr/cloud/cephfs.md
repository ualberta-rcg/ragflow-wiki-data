---
title: "CephFS/fr"
slug: "cephfs"
lang: "fr"

source_wiki_title: "CephFS/fr"
source_hash: "686517689b83bc496e8421c41d26616d"
last_synced: "2026-05-17T14:59:09.465984+00:00"
last_processed: "2026-05-17T15:21:30.002287+00:00"

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
  qa_generated: true
---

Le système de fichiers CephFS peut être partagé par plusieurs hôtes d'instances OpenStack. Pour profiter de ce service, faites une demande à [nuage@tech.alliancecan.ca](mailto:nuage@tech.alliancecan.ca).

La procédure est plutôt technique et nécessite des compétences Linux de base pour créer et modifier des fichiers, définir des permissions et créer des points de montage. Si vous avez besoin d’assistance, écrivez à [nuage@tech.alliancecan.ca](mailto:nuage@tech.alliancecan.ca).

# Procédure

!!! note "Remarque"
    Plusieurs chaînes de caractères de l’interface OpenStack ne sont pas traduites en français.

## Demander l’accès aux points de partage (*shares*)

Si vous ne disposez pas déjà d’un quota pour ce service, écrivez à [nuage@tech.alliancecan.ca](mailto:nauge@tech.alliancecan.ca) et indiquez :
*   le nom du projet OpenStack
*   la capacité du quota requise (en Go)
*   le nombre de points de partage requis

## Configuration OpenStack : Créer un point de partage CephFS

**Créez un point de partage :**
Dans *Projet --> Partages --> Partages*, cliquez sur *+Créer un point de partage*.
*   *Nom du point de partage* = entrez un nom significatif pour votre projet (par exemple *nom-du-projet-nomDuPartage*)
*   *Protocole de partage* = CephFS
*   *Taille* = taille requise pour le point de partage
*   *Type de point de partage* = cephfs (ou cephfs-ec42 pour SD4H/Juno)
*   *Zone de disponibilité* = nova
*   Ne sélectionnez pas *Rendre visible pour tous* ou *Rendre visible pour les utilisateurs de tous les projets* pour SD4H/Juno, autrement le point de partage sera accessible par tous les utilisateurs dans tous les projets.
*   Cliquez sur le bouton *Créer*.

**Créez une règle pour générer une clé :**
Dans *Projet --> Partages --> Partages --> colonne Actions*, sélectionnez *Gérer les règles* du menu déroulant.
Cliquez sur le bouton *+Ajouter une règle* à droite de la page.
*   *Type d'accès* = cephx
*   *Niveau d'accès* = sélectionnez *lecture-écriture* ou *lecture seule* (vous pouvez créer plusieurs règles à plusieurs niveaux)
*   *Accès à* = entrez un nom significatif pour la clé; ce nom est important parce qu'il sera utilisé dans la configuration du client CephFS (ici le nom est *MyCephFS-RW*).

**Prenez note des détails dont vous aurez besoin :**
Dans *Projet --> Partages --> Partages*, cliquez sur le nom du point de partage.
Dans *Aperçu du point de partage*, notez les trois éléments suivants :
*   *Chemin d'accès* qui servira à la commande `mount` pour l'instance;
*   *Accès à* qui sera le nom du client;
*   *Clé d'accès* qui permettra à l'instance client de se connecter.

## Attacher le réseau CephFS à votre instance

### Sur Arbutus
Le réseau CephFS est déjà disponible pour vos instances et donc vous n'avez rien à faire. Allez à [Configuration d'une instance : installer et configurer un client CephFS](#configuration-dune-instance-installer-et-configurer-un-client-cephfs) ci-dessous.

### Sur SD4H/Juno
Vous devez attacher le réseau CephFS à l'instance.

**Sur le web :**
Pour chaque instance, sélectionnez *Instance --> Action --> Attacher une interface --> Réseau CephFS*. Ne cochez pas la case *Adresse IP fixe*.

**Avec le [client OpenStack](openstack_command_line_clients.md) :**
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

### Paquets requis pour la famille Red Hat (RHEL, CentOS, Fedora, Rocky, Alma)
Vérifiez quelles versions sont disponibles sur [https://download.ceph.com/](https://download.ceph.com/) et trouvez les répertoires `rpm-*` récents.
Depuis avril 2026, `tentacle` est la plus récente version stable.
Les distributions compatibles sont listées dans [https://download.ceph.com/rpm-tentacle/](https://download.ceph.com/rpm-tentacle/).
Nous montrons ici des exemples de configurations pour `Enterprise Linux 9` et ses dérivées. Depuis avril 2026, le client CephFS n'est plus disponible pour `Enterprise Linux 10` et ses dérivées.

**Installation des dépôts de paquets donnant accès aux paquets d'un client Ceph :**

```ini title="/etc/yum.repos.d/ceph.repo"
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

Le répertoire epel doit être présent.
```bash
sudo dnf install epel-release
```
Vous pouvez maintenant installer ceph lib, cephfs client et autres dépendances.
```bash
sudo dnf install -y libcephfs2 python3-cephfs ceph-common python3-ceph-argparse
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
    ```ini title="/etc/ceph/ceph.conf"
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

!!! warning "Avertissement"
    Les informations sur le moniteur se trouvent dans le champ *Chemin d'accès* des détails du point de partage qui sera utilisé pour monter le volume. Si la valeur affichée sur la page Web est différente de ce qui est présenté ici, cela signifie que cette page n'est pas à jour.

Entrez le nom du client et le secret dans le fichier `ceph.keyring`.

```ini title="/etc/ceph/ceph.keyring"
[client.MyCephFS-RW]
    key = <Access Key>
```

Encore une fois, la clé d'accès et le nom du client (ici *MyCephFS-RW*) se trouvent sous les règles d'accès sur la page Web de votre projet.
Cliquez sur *Projet --> Partages --> Partages*, puis cliquez sur le nom du point de partage.

**Récupérez les informations de connexion dans la page *Share* pour votre connexion :**
*   Ouvrez les détails en cliquant sur le nom du point de partage dans la page *Partages*.
*   De la page, copiez la partie de *Chemin d'accès* qui contient `:` que nous allons utiliser pour monter le système de fichiers (par exemple ici, `:/volumes/_nogroup/f6cb8f06-f0a4-4b88-b261-f8bd6b03582c`).

**Montez le système de fichiers :**
*   Créez un répertoire pour le point de montage quelque part dans votre hôte (ici `/cephfs`).
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

!!! note "Remarque"
    Le caractère `:` non standard devant le chemin d'accès au périphérique n'est pas une erreur de frappe.

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

Installez la bibliothèque `ceph-fuse`.

```bash
sudo dnf install ceph-fuse
```
Pour que le montage soit disponible dans votre espace utilisateur, décommentez `user_allow_other` dans le fichier `fuse.conf`.

```txt title="/etc/fuse.conf"
# mount_max = 1000
user_allow_other
```

Vous pouvez maintenant monter cephFS dans votre espace /home.
```bash
mkdir ~/my_cephfs
ceph-fuse my_cephfs/ --id=MyCephFS-RW --conf=~/ceph.conf --keyring=~/ceph.keyring   --client-mountpoint=/volumes/_nogroup/f6cb8f06-f0a4-4b88-b261-f8bd6b03582c
```
Notez que le nom du client est ici le `--id`. Le contenu de `ceph.conf` et de `ceph.keyring` est exactement le même que pour le montage du noyau ceph.

# Remarques

Un point de partage particulier peut disposer de plusieurs clés utilisateur. Cela permet un accès plus précis au système de fichiers, par exemple si vous avez besoin que certains hôtes accèdent au système de fichiers uniquement en lecture seule. Si vous disposez de plusieurs clés pour un point de partage, vous pouvez ajouter les clés supplémentaires à votre hôte et modifier la procédure de montage ci-dessus. Ce service n'est pas disponible pour les hôtes extérieurs à la grappe OpenStack.