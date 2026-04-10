---
title: "Security considerations when running a VM/fr"
tags:
  - cloud

keywords:
  []
---

*Page enfant de [Service infonuagique de Calcul Canada ](https://docs.computecanada.ca/wiki/Cloud/fr)*

Vous êtes responsable de la sécurité pour vos instances virtuelles dans [l'environnement infonuagique de Calcul Canada](cloud-fr.md).

Sans être un guide complet pour la sécurité de vos instances, vous trouverez ici les règles de base pour créer une instance virtuelle.

## Information de base
La vidéo [Safety First!](https://youtu.be/l3CcXzaVpTs) (environ 90 minutes) aborde l'information de base; elle est disponible en anglais seulement.

Vous pouvez aller directement aux sujets suivants :
* [Talk overview](https://youtu.be/l3CcXzaVpTs?t=219)
* [Cloud service levels](https://youtu.be/l3CcXzaVpTs?t=354)
* [General security principles](https://youtu.be/l3CcXzaVpTs?t=563)
* [Key topics](https://youtu.be/l3CcXzaVpTs?t=789)
* [Creating a first VM (with some comments about security)](https://youtu.be/l3CcXzaVpTs?t=817)
* [OpenStack security groups](https://youtu.be/l3CcXzaVpTs?t=1530)
* [SSH security](https://youtu.be/l3CcXzaVpTs?t=1964)
* [Logs](https://youtu.be/l3CcXzaVpTs?t=3281)
* [Creating backups of VMs](https://youtu.be/l3CcXzaVpTs?t=4180)

## Sécurité du système d'exploitation
* Effectuez régulièrement les mises à jour de sécurité (voir [Mise à jour d'une instance virtuelle](security-considerations-when-running-a-vm-fr#mise_à_jour_d'une_instance_virtuelle.md) ci-dessous).
* Évitez d'utiliser des paquets de sources non réputées.
* Utilisez l'image la plus récente; par exemple, évitez d'utiliser Ubuntu 14.04 si Ubuntu 18.04 est disponible.
* Utilisez l’authentification qui se fait par défaut avec des  [clés SSH](https://docs.computecanada.ca/wiki/SSH_Keys/fr); elle est beaucoup plus sûre que par mots de passe. 
* Installez [fail2ban](https://www.fail2ban.org) pour parer les [attaques par force brute](https://fr.wikipedia.org/wiki/Attaque_par_force_brute).

## Sécurité du réseau
* Limitez l'accès à votre service. Évitez d’utiliser 0.0.0.0 dans le champ CIDR du formulaire pour le groupe de sécurité et, en particulier, ne créez pas des règles pour 0.0.0.0 pour le groupe de sécurité par défaut, ce qui permettrait l’accès à toutes les instances du projet.
** Portez attention aux adresses IP rendues disponibles par la configuration du *netmask*.
* Ne regroupez pas les ports d'accès.
* Portez attention aux règles de sécurité, en particulier pour :  
** les services qui ne devraient pas être accédés publiquement
*** ssh (22); ce service permet une connexion interactive avec votre instance et NE DOIT PAS être publiquement accessible. 
*** RDP (3389); ce service permet une connexion interactive avec votre instance et NE DOIT PAS être publiquement accessible.   
*** mysql (3306)
*** VNC (5900-5906); ce service permet une connexion interactive avec votre instance et NE DOIT PAS être publiquement accessible.   
*** postgresql (5432)
*** nosql
*** RDP (3389)
*** tomcat
*** et plusieurs autres
** les services qui devraient être accédés publiquement
*** Apache (80, 443)
*** Nginx (80, 443)
*** et autres
* Configurez le serveur Web pour HTTPS plutôt que HTTP.
* Dans plusieurs cas, HTTP ne devrait être utilisé que pour rediriger vers HTTPS.
* N'installez pas de serveur de courriel.
* N'installez pas un serveur BitTorrent.

## Mise à jour d'une instance virtuelle
Effectuez régulièrement des mises à jour du système d’exploitation de vos instances, idéalement chaque semaine ou chaque fois que de nouveaux paquets sont disponibles. Utilisez les commandes suivantes, selon la distribution Linux. Vous devrez redémarrer votre instance et vous connecter à nouveau.
### Ubuntu/Debian
<source lang="console">
$ sudo apt-get update
$ sudo apt-get dist-upgrade
$ sudo reboot
</source>
### CentOS
<source lang="console>
$ sudo yum update
$ sudo reboot
</source>
### Fedora
<source lang="console>
$ sudo dnf update
$ sudo reboot
</source>
## Références
[Tips for Securing Your EC2 Instance](https://aws.amazon.com/articles/1233/) (article Amazon).