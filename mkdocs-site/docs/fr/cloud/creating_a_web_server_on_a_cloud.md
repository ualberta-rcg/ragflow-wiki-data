---
title: "Creating a web server on a cloud/fr"
slug: "creating_a_web_server_on_a_cloud"
lang: "fr"

source_wiki_title: "Creating a web server on a cloud/fr"
source_hash: "9aba64e2bacbf79940a9ec3de19eef81"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:36:39.802150+00:00"

tags:
  - cloud

keywords:
  - "Apache"
  - "répertoire root"
  - "Service infonuagique"
  - "propriétaire des fichiers"
  - "Sécurité"
  - "Apache2"
  - "mod_bw"
  - "Ubuntu"
  - "configuration"
  - "bande passante"
  - "Serveur web"
  - "public_html"
  - "serveur web"

questions:
  - "Quels sont les principaux risques de sécurité liés à l'hébergement d'un serveur web public et comment peut-on les atténuer ?"
  - "Quelles sont les commandes et les étapes requises pour installer et tester un serveur web Apache sur une instance Ubuntu ?"
  - "Pourquoi est-il recommandé de modifier le répertoire racine par défaut d'Apache et comment cela facilite-t-il la gestion du site web ?"
  - "Quelles sont les étapes et les fichiers à modifier pour changer le répertoire racine par défaut d'Apache vers un dossier utilisateur comme public_html ?"
  - "Quel module doit-on installer et activer pour limiter l'utilisation de la bande passante sur un serveur web Apache très sollicité ?"
  - "Dans quel fichier de configuration et entre quelles balises doit-on insérer les directives pour appliquer une limite de bande passante spécifique à un site ?"
  - "Pourquoi est-il souvent plus facile de gérer un site web en modifiant le répertoire root du serveur ?"
  - "Quel est l'utilisateur propriétaire des fichiers dans l'image Ubuntu donnée en exemple ?"
  - "Quel nouveau chemin de répertoire est utilisé pour remplacer l'emplacement par défaut d'Apache ?"
  - "Quelles sont les étapes et les fichiers à modifier pour changer le répertoire racine par défaut d'Apache vers un dossier utilisateur comme public_html ?"
  - "Quel module doit-on installer et activer pour limiter l'utilisation de la bande passante sur un serveur web Apache très sollicité ?"
  - "Dans quel fichier de configuration et entre quelles balises doit-on insérer les directives pour appliquer une limite de bande passante spécifique à un site ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Page enfant de [Service infonuagique](https://docs.computecanada.ca/wiki/CC-Cloud/fr)*

Nous décrivons ici une méthode très simple pour créer un serveur web dans notre environnement infonuagique en utilisant Ubuntu et le serveur web Apache.

## Sécurité
La sécurité est un aspect important pour tout ordinateur qui permet un accès public, ce qui peut prendre plusieurs formes, par exemple permettre les connexions SSH, afficher du code HTML via HTTP, ou offrir un service qui utilise le logiciel d'une tierce partie (comme WordPress). On appelle *[daemons](https://fr.wikipedia.org/wiki/Daemon_(informatique))* les programmes qui soutiennent des services tels que SSH ou HTTP; ces programmes sont en constante activité et reçoivent les requêtes de l'extérieur via des [ports](https://fr.wikipedia.org/wiki/Port_(logiciel)) spécifiques. [OpenStack](managing_your_cloud_resources_with_openstack.md) permet de gérer ces ports et d'en restreindre l'accès, par exemple en accordant l'accès à certaines [adresses IP en particulier](https://fr.wikipedia.org/wiki/Adresse_IP) ou à un groupe d'adresses; voir la section [Groupes de sécurité](managing_your_cloud_resources_with_openstack.md). La sécurité d'une instance peut être grandement améliorée par le contrôle de son accès, mais ceci n'élimine pas tous les risques : si les données que vous envoyez ne sont pas cryptées d'une quelconque manière (par exemple avec des mots de passe), une personne habile peut trouver le moyen de les consulter. Les données sont donc souvent cryptées selon le protocole [Transport Layer Security](https://fr.wikipedia.org/wiki/Transport_Layer_Security) qui devrait être employé pour tous les sites web auxquels des personnes de l'extérieur peuvent se connecter (par exemple WordPress ou MediaWiki); à ce sujet, consultez [Configuration du serveur Apache pour utiliser SSL](configuring_apache_to_use_ssl.md). Il est aussi possible que des données transmises à partir de votre serveur web vers un client soient modifiées en route par un tiers, si elles ne sont pas cryptées. Ceci n'est pas un problème pour le serveur web comme tel, mais pourrait l'être pour les clients. Dans la plupart des cas, il est recommandé d'utiliser le cryptage sur votre serveur web. La sécurité de vos instances est votre responsabilité; nous vous rappelons de ne pas négliger cet aspect critique.

## Installer Apache

1.  Suivez les directives dans la page [Cloud : Guide de démarrage](cloud_quick_start.md) pour créer une instance persistante sous Linux Ubuntu (voir [Démarrer depuis un volume](working_with_volumes.md)).
2.  Pour ouvrir le port 80 et permettre l'accès HTTP à votre instance, suivez [ces directives](cloud_quick_start.md). À partir du menu déroulant, sélectionnez HTTP au lieu de SSH.
3.  Une fois connecté à votre instance,
    1.  Faites la mise à jour de vos répertoires apt-get avec
        ````bash
        sudo apt-get update
        ````
    2.  Faites la mise à jour de la version d'Ubuntu avec
        ````bash
        sudo apt-get upgrade
        ````
        La version la plus à jour comprendra les toutes dernières rustines de sécurité.
    3.  Installez le serveur web Apache avec
        ````bash
        sudo apt-get install apache2
        ````
4.  Faites afficher la nouvelle page Apache temporaire en entrant l'adresse IP flottante de votre instance dans la barre d'adresses de votre fureteur; il s'agit de la même adresse IP que vous utilisez pour vous connecter avec SSH. Vous devriez voir une page test.
5.  Modifiez le contenu des fichiers dans `/var/www/html` pour créer le site web et en particulier le fichier `index.html` qui en définit le point d'entrée.

## Modifier le répertoire racine du serveur web
Il est souvent plus facile de gérer un site web si l'utilisateur qui se connecte à l'instance est propriétaire des fichiers. Dans l'image Ubuntu de notre exemple, le propriétaire est `ubuntu`. Les étapes qui suivent indiquent à Apache de présenter les fichiers à partir de `/home/ubuntu/public_html` (par exemple) plutôt que de `/var/www/html`.

1.  Utilisez la commande
    ````bash
    sudo vim /etc/apache2/apache2.conf
    ````
    (ou un autre éditeur) pour modifier la ligne `<Directory /var/www/>` en `<Directory /home/ubuntu/public_html>`.
2.  Utilisez la commande
    ````bash
    sudo vim /etc/apache2/sites-available/000-default.conf
    ````
    pour modifier la ligne `DocumentRoot /var/www/html` en `DocumentRoot /home/ubuntu/public_html`.
3.  Créez le répertoire dans le répertoire `/home` de l'utilisateur avec la commande
    ````bash
    mkdir public_html
    ````
4.  Copiez la page par défaut dans le répertoire que vous venez de créer, c'est-à-dire `public_html` dans votre `/HOME`, avec la commande
    ````bash
    cp /var/www/html/index.html /home/ubuntu/public_html
    ````
5.  Redémarrez le serveur Apache pour actualiser les modifications avec la commande
    ````bash
    sudo service apache2 restart
    ````

Vous devriez pouvoir modifier le fichier `/home/ubuntu/public_html/index.html` sans utiliser `sudo`. Rafraîchissez la page chargée précédemment dans votre fureteur pour voir les modifications.

## Limiter la bande passante
Si votre serveur web est très sollicité, il est possible qu'il occupe beaucoup des ressources de la bande passante. Une bonne manière de limiter l'utilisation de la bande passante est d'utiliser [le module Apache](https://github.com/IvnSoft/mod_bw).

### Installation
````bash
sudo apt install libapache2-mod-bw
sudo a2enmod bw
````

### Configuration
L'exemple de configuration suivant limite la bande passante pour tous les clients à 100 Mbps.

````apache
BandWidthModule On
ForceBandWidthModule On

#Exceptions to badwith of 100Mbps should go here above limit
#below in order to override it

#limit all connections to 100Mbps
#100Mbps *1/8(B/b)*1e6=12,500,000 bytes/s
BandWidth all 12500000
````

Ceci devrait être placé entre les balises `<VirtualHost></VirtualHost>` pour votre site. La configuration Apache par défaut se trouve dans le fichier `/etc/apache2/sites-enabled/000-default.conf`.

## Pour plus d'information
*   [Configuration du serveur Apache pour utiliser SSL](configuring_apache_to_use_ssl.md)
*   [Documentation Apache2](http://httpd.apache.org/docs/2.0/) (en anglais)
*   [Tutoriel HTML w3schools](http://www.w3schools.com/html/) (en anglais)