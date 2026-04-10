---
title: "VisIt/fr"
slug: "visit"
lang: "fr"

source_wiki_title: "VisIt/fr"
source_hash: "0aaa094ff190b94bd07b6805bbe041e7"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T12:45:44.732973+00:00"

tags:
  - software

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

!!! warning "Incompatibilité de version"
La même version majeure doit être installée sur le client local et sur l'ordinateur hôte à distance; dans le cas contraire, certaines incompatibilités peuvent empêcher la connexion client-serveur.

Sélectionnez l'onglet approprié.

=== "Fir, Nibi, Rorqual"

## Visualisation client-serveur avec Fir, Nibi et Rorqual

Plusieurs versions de VisIt sont installées sur nos grappes; pour connaître les numéros des versions, lancez `module spider visit`. Pour utiliser VisIt à distance en mode client-serveur, votre ordinateur doit avoir la même version majeure que l'ordinateur hôte, soit 2.12.x ou 2.13.x ou 3.2.x.
Avant de démarrer VisIt, téléchargez le fichier de profil XML [host_fir.xml](https://nextcloud.computecanada.ca/index.php/s/aGeScGwF8RKJJji/download); ce fichier de configuration sert à vous connecter à VisIt 3.2.1.

*   Sous Linux et Mac, copiez le fichier dans `` ~/.visit/hosts/ ``.
*   Sous Windows, copiez le fichier dans `` My Documents\VisIt 3.2.1\hosts `` ou dans le répertoire similaire.

Lancez VisIt sur votre ordinateur. Dans le menu principal, sous *Options -> Profils d'hôtes*, vous devriez voir le profil hôte *fir*. Pour effectuer un rendu sur Nibi, utilisez :

```text
Host nickname = nibi
Remote host name = nibi.alliancecan.ca
```

Pour Fir et Nibi, entrez votre nom d'utilisateur tel que défini dans CCDB.

```text
Username = yourOwwUserName
```

À l'exception du nom d'utilisateur, votre configuration devrait être semblable à ceci :

En cliquant sur *Lancer les profils*, les profils *login* et *slurm* devraient se trouver dans la liste.

*   Le profil *login* est utilisé dans un nœud de connexion, ce qui n'est pas recommandé pour les visualisations intensives.
*   Le profil *slurm* est utilisé pour une tâche interactive dans un nœud de calcul. Si vous sélectionnez ce profil, cliquez sur l'onglet *Parallèle* puis sur l'onglet *Avancé* dessous. Dans le champ *Arguments du lanceur*, remplacez `` --account=def-someuser `` par votre allocation par défaut, comme montré ci-dessous.
*   Sur Fir uniquement, ajoutez l'indicateur `` --chdir=/scratch/username `` avec votre nom d'utilisateur pour lancer votre tâche à partir de votre répertoire /scratch.

Enregistrez les paramètres en cliquant sur *Options -> Enregistrer les paramètres* et quittez VisIt pour activer la configuration.

Si l'authentification multifacteur est configurée pour votre compte, vous devez [configurer votre client SSH client avec ControlMaster](../Multifactor_authentication/fr.md#configurer_votre_client_ssh) et vous assurer que *Hôte* utilise le nom complet de l'hôte, par exemple

```bash
Host fir.alliancecan.ca
    HostName fir.alliancecan.ca
    User <your user name on the cluster>
    ControlPath ~/.ssh/cm-%r@%h:%p
    ControlMaster auto
    ControlPersist 10m
```

Ensuite, connectez-vous à la grappe dans une fenêtre de terminal. Enfin, relancez VisIt sur votre ordinateur, ouvrez la boîte de dialogue d'ouverture de fichier et changez l'hôte local en *fir* (ou *Nibi*). La connexion devrait se faire et Component Launcher démarrer sur le nœud de connexion; vous devriez pouvoir voir le système de fichiers de la grappe, accéder à votre fichier et le sélectionner. Vous serez invité à sélectionner le profil *login* (rendu sur le nœud de connexion) ou *slurm* (rendu dans une tâche Slurm interactive sur un nœud de calcul). Si vous sélectionnez le profil *slurm*, il faut préciser le nombre de nœuds et de processeurs ainsi que la durée maximale.

Cliquez sur *OK* et attendez que le moteur VisIt soit en marche.
Si le rendu doit s'effectuer sur un nœud de calcul, le temps d'attente peut être plus long.
Une fois que le jeu de données est affiché dans *Source active*, le moteur fonctionne et vous pouvez commencer à travailler sur votre graphe.

=== "Trillium"

## Visualisation client-serveur avec Trillium

### Configuration de l'hôte

Pour que VisIt puisse se connecter à la grappe Trillium, vous devez configurer votre ordinateur hôte par une des méthodes suivantes :

#### Fichier de configuration

Téléchargez et enregistrez le fichier [host_trillium.xml](https://support.scinet.utoronto.ca/~mponce/viz/host_trillium.xml) et cliquez sur *Enregistrer sous*.
*   Sous Linux et Mac, copiez le fichier dans `` ~/.visit/hosts/ ``.
*   Sous Windows, copiez le fichier dans `` My Documents\VisIt 2.13.0\hosts/ ``.

Redémarrez VisIt et vérifiez que le profil pour Trillium se trouve sous *Options -> Profils d'hôtes*.

#### Configuration manuelle

Lanzez VisIt sur votre ordinateur. Dans le menu *Options*, cliquez sur *Profils d'hôtes*; cliquez sur *Nouvel hôte* et sélectionnez

```text
Host nickname = trillium
Remote host name = trillium.alliancecan.ca
Username = Enter_Your_OWN_username_HERE
Path to VisIt installation = /scinet/trillium/software/2018a/opt/base/visit/2.13.1
```

Sélectionnez *Tunneliser les connexions de données via SSH* et cliquez sur *Appliquer*.

Dans le haut de la fenêtre, cliquez sur *Lancer les profils* pour créer un profil:

*   *login* pour utiliser un nœud de connexion et accéder aux données;
*   *slurm* pour utiliser un nœud de calcul comme moteur de rendu.

Sous l'onglet *Parallèle* sélectionnez *Lancer le moteur parallèle*. Pour un profil Slurm, vous devrez configurer les paramètres.

Lorsque vous avez terminé, enregistrez les modifications avec *Options -> Enregistrer les paramètres*; elles seront en vigueur la prochaine fois que vous lancerez VisIt.

=== "Cloud"

## Visualisation client-serveur sur le cloud

### Prérequis

La page [Cloud : Guide de démarrage](../Cloud_Quick_Start/fr.md) décrit la création d'une instance. Une fois connecté à l’instance, vous devrez installer certains paquets pour pouvoir compiler ParaView et VisIt; par exemple, sur une instance CentOS,

```bash
sudo yum install xauth wget gcc gcc-c++ ncurses-devel python-devel libxcb-devel
sudo yum install patch imake libxml2-python mesa-libGL mesa-libGL-devel
sudo yum install mesa-libGLU mesa-libGLU-devel bzip2 bzip2-libs libXt-devel zlib-devel flex byacc
sudo ln -s /usr/include/GL/glx.h /usr/local/include/GL/glx.h
```

Si vous avez votre propre paire de clés SSH (et non la clé générée par OpenStack pour le nuage), vous pourriez copier la clé publique dans l'instance pour simplifier la connexion; pour ce faire, lancez la commande suivante sur votre ordinateur :

```bash
cat ~/.ssh/id_rsa.pub | ssh -i ~/.ssh/cloudwestkey.pem centos@vm.ip.address 'cat >>.ssh/authorized_keys'
```

### Compilation avec OSMesa

En mode non interactif, le rendu peut être effectué avec un seul script :

```bash
wget http://portal.nersc.gov/project/visit/releases/2.12.1/build_visit2_12_1
chmod u+x build_visit2_12_1
./build_visit2_12_1 --prefix /home/centos/visit --mesa --system-python \
    --hdf4 --hdf5 --netcdf --silo --szip --xdmf --zlib
```

Ceci peut nécessiter quelques heures. L’installation peut ensuite être testée avec

```bash
~/visit/bin/visit -cli -nowin
```

ce qui devrait lancer un interpréteur Python.

### Mode client-serveur

Sur votre ordinateur, démarrez VisIt. Sous *Options -> Profils d'hôtes*, modifiez les paramètres suivants : le nom de la connexion, le nom de l'instance hôte, le chemin vers VisIt (`` /home/centos/visit ``), votre nom d'utilisateur. Activez enfin le lien SSH. N’oubliez pas de sauvegarder les paramètres avec *Options -> Enregistrer les paramètres*.
En ouvrant un fichier (*Fichier -> Ouvrir un fichier... -> Hôte = Arbutus*), vous devriez voir le système de fichiers de l’instance. Chargez et visualisez un fichier. Le traitement des données et le rendu devraient s’effectuer sur l’instance alors que le résultat et les contrôles de l’interface utilisateur seront affichés sur votre ordinateur.