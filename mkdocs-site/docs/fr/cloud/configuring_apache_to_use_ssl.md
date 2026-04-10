---
title: "Configuring Apache to use SSL/fr"
slug: "configuring_apache_to_use_ssl"
lang: "fr"

source_wiki_title: "Configuring Apache to use SSL/fr"
source_hash: "d53788ba749aa7946fda845328561f45"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T05:47:11.657787+00:00"

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

*Page enfant de [Création d'un serveur web sur un nuage](creation-dun-serveur-web-sur-un-nuage.md)*

Le terme SSL fait référence à la fois au protocole *Transport Layer Security (TLS)* et à son prédécesseur *Secure Sockets Layer (SSL)*. Ils servent au chiffrement des données communiquées sur les réseaux. Le chiffrement protège les données critiques qui transitent sur l'Internet, par exemple les mots de passe. Cependant, même si le serveur web envoie au client de l'information qui n'est pas sensible, le chiffrement empêchera une tierce partie d'intercepter et de modifier les données avant qu'elles ne se rendent à destination. Dans la plupart des cas, les certificats SSL sont utiles pour chiffrer les données qui proviennent de ou sont destinées à un serveur web via l'Internet.

Il y a deux types de certificats : les certificats signés par une tierce partie et les certificats autosignés. Dans la plupart des cas, vous voudrez un certificat signé par une tierce partie, ce qui se fait très facilement avec Let's Encrypt, comme expliqué ci-dessous. Par contre, d'autres cas (comme les tests) se prêtent mieux aux certificats autosignés. De cette manière, les données qui proviennent de et sont destinées à votre serveur sont chiffrées; par contre, aucune tierce partie ne confirme la validité de votre serveur web et un avertissement sera affiché quand on voudra s'y connecter. Vous ne voudrez probablement pas utiliser un certificat autosigné si votre site est ouvert au public.

Une fois que vous avez le certificat et que le serveur web est configuré, il est recommandé d'utiliser [l'outil ssltest](https://www.ssllabs.com/ssltest/) de ssllabs qui peut vous suggérer des modifications à votre configuration pour renforcer la sécurité.

## Certificat signé

Un certificat signé par une [Autorité de certification](https://en.wikipedia.org/wiki/Certificate_authority) (CA, pour *Certificate Authority*) permet aux utilisateurs d'un site web de s'assurer qu'un tiers (le CA) confirme l'identité du site et prévient ce qu'on appelle une [attaque de l'homme du milieu](https://fr.wikipedia.org/wiki/Attaque_de_l%27homme_du_milieu).

Plusieurs CA exigent des frais annuels, contrairement à [Let's Encrypt](https://letsencrypt.org/). Un certificat SSL signé par ce CA peut être créé et renouvelé automatiquement par l'outil Certbot qui configure aussi votre serveur web pour l'utilisation de ce même certificat. Pour un démarrage rapide, consultez la [page principale de Certbot](https://certbot.eff.org/). Les détails se trouvent dans la [documentation Certbot](https://certbot.eff.org/docs/).

!!! note
    Si vous configurez Certbot via Apache, ouvrez le port 443 (TCP entrant) pour que Certbot puisse se connecter au site (ceci n'est pas couvert dans la documentation de Certbot).

## Certificat autosigné

Cette section décrit la procédure de création d'un certificat SSL autosigné et la configuration d'Apache pour le chiffrement.

!!! warning
    Il n'est pas recommandé d'utiliser un certificat autosigné sur un site de production d'importance; ces certificats conviendront cependant à la production sur des sites restreints à usage local, ou encore dans un environnement de test.

Les étapes suivantes décrivent la procédure sous Ubuntu. On trouvera certaines différences sous d'autres systèmes d'exploitation, notamment en ce qui a trait aux commandes, aux localisations ou aux noms des fichiers de configuration.

1.  **Activer le module SSL**
    Installez Apache (voir [Installer Apache](creation-dun-serveur-web-sur-un-nuage.md#installer-apache)), puis activez le module SSL ainsi :
    ```bash
    sudo a2enmod ssl
    sudo service apache2 restart
    ```
2.  **Créer un certificat SSL autosigné**
    ```bash
    sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/server.key -out /etc/ssl/certs/server.crt
    ```
    Si on vous demande une phrase de passe, assurez-vous de relancer la commande avec la syntaxe correcte, y compris l'option `-nodes`. Vous devrez ensuite répondre aux questions qui suivent, pour lesquelles nous donnons des exemples de réponse.

    ```text
      Country Name (2 letter code) [AU]:CA
      State or Province Name (full name) [Some-State]:Nova Scotia
      Locality Name (eg, city) []:Halifax
      Organization Name (eg, company) [Internet Widgits Pty Ltd]:Alliance
      Organizational Unit Name (eg, section) []:ACENET
      Common Name (e.g. server FQDN or YOUR name) []:XXX-XXX-XXX-XXX.cloud.computecanada.ca
      Email Address []:<votre courriel>
    ```

    La réponse à *Common Name* est la plus importante; il s'agit du nom de domaine de votre serveur. Pour une machine virtuelle sur un de nos nuages, remplacez les X dans l'exemple par l'adresse IP flottante associée à la machine virtuelle.
3.  **Définir le propriétaire et les autorisations**
    Pour définir le propriétaire et les autorisations associés à la clé privée, entrez les commandes :
    ```bash
    sudo chown root:ssl-cert /etc/ssl/private/server.key
    sudo chmod 640 /etc/ssl/private/server.key
    ```
4.  **Configurer Apache pour utiliser le certificat**
    Modifiez le fichier de configuration SSL avec la commande :
    ```bash
    sudo vim /etc/apache2/sites-available/default-ssl.conf
    ```
    et remplacez les deux lignes suivantes :
    ```text
    SSLCertificateFile      /etc/ssl/certs/ssl-cert-snakeoil.pem
    SSLCertificateKeyFile /etc/ssl/private/ssl-cert-snakeoil.key
    ```
    par les trois lignes :
    ```text
    SSLCertificateFile      /etc/ssl/certs/server.crt
    SSLCertificateKeyFile /etc/ssl/private/server.key
    SSLCertificateChainFile /etc/ssl/certs/server.crt
    ```
    Vérifiez que le chemin pour `DocumentRoot` correspond au chemin défini dans `/etc/apache2/sites-available/000-default.conf`, pourvu que SSL s'applique à ce site.
5.  **Renforcer la sécurité**
    Redirigez les requêtes HTTP vers HTTPS; exigez des versions plus à jour de SSL; utilisez de meilleures options de chiffrement, d'abord en modifiant le fichier ainsi :
    ```bash
    sudo vim /etc/apache2/sites-available/default-ssl.conf
    ```
    et ensuite en ajoutant :
    ```apache
    ServerName XXX-XXX-XXX-XXX.cloud.computecanada.ca
    SSLProtocol all -SSLv2 -SSLv3
    SSLCipherSuite HIGH:MEDIUM:!aNULL:!MD5:!SEED:!IDEA:!RC4
    SSLHonorCipherOrder on
    ```
    dans le bas, à l'intérieur de la balise `<VirtualHost>`; remplacez les X aux deux endroits par l'IP de la machine virtuelle (notez qu'il faut utiliser des tirets dans l'IP plutôt que des points). Entrez une commande de redirection sur le serveur virtuel en modifiant le fichier de configuration du site web par défaut avec :
    ```bash
    sudo vim /etc/apache2/sites-available/000-default.conf
    ```
    et en ajoutant la ligne :
    ```apache
    Redirect permanent / https://XXX-XXX-XXX-XXX.cloud.computecanada.ca
    ```
    à l'intérieur de la balise `<VirtualHost>`.
6.  **Activer le site sécurisé**
    ```bash
    sudo a2ensite default-ssl.conf
    sudo service apache2 restart