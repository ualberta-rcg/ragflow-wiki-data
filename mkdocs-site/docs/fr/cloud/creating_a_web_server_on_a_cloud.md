---
title: "Creating a web server on a cloud/fr"
slug: "creating_a_web_server_on_a_cloud"
lang: "fr"

source_wiki_title: "Creating a web server on a cloud/fr"
source_hash: "9aba64e2bacbf79940a9ec3de19eef81"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T05:51:22.258429+00:00"

tags:
  - cloud

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

!!! info "Page connexe"
Ce document est une page enfant du [Service infonuagique](https://docs.computecanada.ca/wiki/CC-Cloud/fr).

Nous décrivons ici une méthode très simple pour créer un serveur web dans notre environnement infonuagique en utilisant Ubuntu et Apache Web Server.

## Sécurité

!!! attention "Sécurité et responsabilités"
    La sécurité est un aspect important pour tout ordinateur qui permet un accès public, ce qui peut prendre plusieurs formes, par exemple permettre les connexions SSH, afficher du code HTML via HTTP, ou offrir un service qui utilise le logiciel d'une tierce partie (comme WordPress). On appelle [*daemons*](https://fr.wikipedia.org/wiki/Daemon_(informatique)) les programmes qui soutiennent des services tels que SSH ou HTTP; ces programmes sont en constante activité et reçoivent les requêtes de l'extérieur via des [ports](https://fr.wikipedia.org/wiki/Port_(logiciel)) spécifiques. [OpenStack](managing-your-cloud-resources-with-openstack.md) permet de gérer ces ports et d'en restreindre l'accès, par exemple en accordant l'accès à certaines [adresses IP en particulier](https://fr.wikipedia.org/wiki/Adresse_IP) ou à un groupe d'adresses; voir la section [Groupes de sécurité](managing-your-cloud-resources-with-openstack.md#groupes-de-securite).

    La sécurité d'une instance peut être grandement améliorée par le contrôle de son accès, mais ceci n'élimine pas tous les risques : si les données que vous envoyez ne sont pas chiffrées d'une quelconque manière (par exemple avec des mots de passe), une personne habile peut trouver le moyen de les consulter. Les données sont donc souvent chiffrées selon le protocole [Transport Layer Security](https://fr.wikipedia.org/wiki/Transport_Layer_Security) qui devrait être employé pour tous les sites web auxquels des personnes de l'extérieur peuvent se connecter (par exemple WordPress ou MediaWiki); à ce sujet, consultez [Configuration du serveur Apache pour utiliser SSL](configuring-apache-to-use-ssl.md).

    Il est aussi possible que des données transmises à partir de votre serveur web vers un client soient modifiées en route par un tiers, si elles ne sont pas chiffrées. Ceci n'est pas un problème pour le serveur web comme tel, mais pourrait l'être pour les clients. Dans la plupart des cas, il est recommandé d'utiliser le chiffrement sur votre serveur web. La sécurité de vos instances est votre responsabilité; nous vous rappelons de ne pas négliger cet aspect critique.

## Mettre en place Apache

1.  Suivez les directives dans la page [Cloud : Guide de démarrage](cloud-quick-start.md) pour créer une instance persistante sous Linux Ubuntu (voir [Démarrer depuis un volume](working-with-volumes.md#demarrer-depuis-un-volume)).
2.  Pour ouvrir le port 80 et permettre l'accès HTTP à votre instance, suivez [ces directives](cloud-quick-start.md#connexion-a-votre-instance-par-ssh). À partir du menu déroulant, sélectionnez HTTP au lieu de SSH.
3.  Une fois connecté à votre instance :
    *   Mettez à jour vos répertoires `apt-get` avec :
        ```bash
        sudo apt-get update
        ```
    *   Mettez à jour la version d'Ubuntu avec :
        ```bash
        sudo apt-get upgrade
        ```
        La version la plus à jour comprendra les toutes dernières rustines de sécurité.
    *   Installez le serveur web Apache avec :
        ```bash
        sudo apt-get install apache2
        ```
4.  Faites afficher la nouvelle page Apache temporaire en entrant l'adresse IP flottante de votre instance dans la barre d'adresses de votre fureteur; il s'agit de la même adresse IP que vous utilisez pour vous connecter avec SSH. Vous devriez voir une page test Apache.
5.  Modifiez le contenu des fichiers dans `/var/www/html` pour créer le site web et en particulier le fichier `index.html` qui en définit le point d'entrée.

### Modifier le répertoire racine du serveur web

Il est souvent plus facile de gérer un site web si la personne qui se connecte à l'instance est propriétaire des fichiers. Dans l'image Ubuntu de notre exemple, le propriétaire est `ubuntu`. Les étapes qui suivent indiquent à Apache de présenter les fichiers à partir de `/home/ubuntu/public_html` (par exemple) plutôt que de `/var/www/html`.

1.  Utilisez la commande suivante (ou un autre éditeur) pour modifier la ligne `<Directory /var/www/>` en `<Directory /home/ubuntu/public_html>` :
    ```bash
    sudo vim /etc/apache2/apache2.conf
    ```
2.  Utilisez la commande suivante pour modifier la ligne `DocumentRoot /var/www/html` en `DocumentRoot /home/ubuntu/public_html` :
    ```bash
    sudo vim /etc/apache2/sites-available/000-default.conf
    ```
3.  Créez le répertoire `public_html` dans le répertoire `/home` de l'utilisateur avec la commande :
    ```bash
    mkdir public_html
    ```
4.  Copiez la page par défaut dans le répertoire que vous venez de créer, c'est-à-dire `public_html` dans votre `/HOME`, avec la commande :
    ```bash
    cp /var/www/html/index.html /home/ubuntu/public_html
    ```
5.  Redémarrez le serveur Apache pour actualiser les modifications avec la commande :
    ```bash
    sudo service apache2 restart
    ```
Vous devriez pouvoir modifier le fichier `/home/ubuntu/public_html/index.html` sans utiliser `sudo`. Rafraîchissez la page chargée précédemment dans votre fureteur pour voir les modifications.

## Limiter la bande passante

Si votre serveur web est très sollicité, il est possible qu'il accapare beaucoup de ressources de la bande passante. Une bonne manière de limiter l'utilisation de la bande passante est d'utiliser [le module Apache](https://github.com/IvnSoft/mod_bw).

### Installation

```bash
sudo apt install libapache2-mod-bw
sudo a2enmod bw
```

### Configuration

L'exemple de configuration suivant limite la bande passante pour tous les clients à 100 Mbps.

```apacheconf
BandWidthModule On
ForceBandWidthModule On

#Exceptions to badwith of 100Mbps should go here above limit
#below in order to override it

#limit all connections to 100Mbps
#100Mbps *1/8(B/b)*1e6=12,500,000 bytes/s
BandWidth all 12500000
```

Ceci devrait être placé entre les balises `<VirtualHost></VirtualHost>` pour votre site. La configuration Apache par défaut se trouve dans le fichier `/etc/apache2/sites-enabled/000-default.conf`.

## Pour plus d'information

*   [Configuration du serveur Apache pour utiliser SSL](configuring-apache-to-use-ssl.md)
*   [Documentation Apache2](http://httpd.apache.org/docs/2.0/) (en anglais)
*   [Tutoriel HTML w3schools](http://www.w3schools.com/html/) (en anglais)