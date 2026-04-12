---
title: "Security considerations when running a VM/fr"
slug: "security_considerations_when_running_a_vm"
lang: "fr"

source_wiki_title: "Security considerations when running a VM/fr"
source_hash: "578140fc3e3520b7cbdf7a28e5d687c0"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:25:56.983742+00:00"

tags:
  - cloud

keywords:
  - "paquets"
  - "Cloud"
  - "instances virtuelles"
  - "mise à jour"
  - "sécurité"
  - "distribution Linux"
  - "commandes"
  - "Fedora"
  - "sécurité du réseau"
  - "système d'exploitation"
  - "instances"
  - "Amazon EC2"
  - "Calcul Canada"

questions:
  - "Quelles sont les meilleures pratiques recommandées pour assurer la sécurité du système d'exploitation d'une instance virtuelle ?"
  - "Comment doit-on configurer les groupes de sécurité et les accès réseau pour protéger efficacement son instance ?"
  - "Quelle est la procédure à suivre pour effectuer les mises à jour régulières d'une instance virtuelle selon la distribution Linux utilisée ?"
  - "Quelles commandes doivent être exécutées pour mettre à jour et redémarrer une distribution Fedora ?"
  - "Quel est le sujet principal de l'article d'Amazon fourni dans la section des références ?"
  - "À quelle catégorie technologique globale ces instructions de maintenance appartiennent-elles ?"
  - "À quelle fréquence est-il recommandé de mettre à jour le système d'exploitation des instances ?"
  - "Quelles sont les commandes spécifiques à exécuter pour mettre à jour une distribution Ubuntu ou Debian ?"
  - "Quelle action indispensable doit être effectuée sur l'instance après l'installation des nouveaux paquets ?"
  - "Quelles commandes doivent être exécutées pour mettre à jour et redémarrer une distribution Fedora ?"
  - "Quel est le sujet principal de l'article d'Amazon fourni dans la section des références ?"
  - "À quelle catégorie technologique globale ces instructions de maintenance appartiennent-elles ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Ce document fait partie de la documentation sur le [Service infonuagique de l'Alliance du Canada](https://docs.alliancecan.ca/wiki/Cloud/fr).

Vous êtes responsable de la sécurité de vos instances virtuelles dans [l'environnement infonuagique de l'Alliance](cloud.md).

Sans être un guide complet pour la sécurité de vos instances, vous trouverez ici les règles de base pour créer une instance virtuelle.

## Information de base

La vidéo [Safety First!](https://youtu.be/l3CcXzaVpTs) (environ 90 minutes) aborde l'information de base; elle est disponible en anglais seulement.

Vous pouvez aller directement aux sujets suivants :

*   [Aperçu de la présentation](https://youtu.be/l3CcXzaVpTs?t=219)
*   [Niveaux de service infonuagique](https://youtu.be/l3CcXzaVpTs?t=354)
*   [Principes généraux de sécurité](https://youtu.be/l3CcXzaVpTs?t=563)
*   [Sujets clés](https://youtu.be/l3CcXzaVpTs?t=789)
*   [Création d'une première VM (avec quelques commentaires sur la sécurité)](https://youtu.be/l3CcXzaVpTs?t=817)
*   [Groupes de sécurité OpenStack](https://youtu.be/l3CcXzaVpTs?t=1530)
*   [Sécurité SSH](https://youtu.be/l3CcXzaVpTs?t=1964)
*   [Journaux](https://youtu.be/l3CcXzaVpTs?t=3281)
*   [Création de copies de sauvegarde des VM](https://youtu.be/l3CcXzaVpTs?t=4180)

## Sécurité du système d'exploitation

*   Effectuez régulièrement les mises à jour de sécurité (voir [Mise à jour d'une instance virtuelle](#mise-%C3%A0-jour-dune-instance-virtuelle) ci-dessous).
*   Évitez d'utiliser des paquets de sources non réputées.
*   Utilisez l'image la plus récente; par exemple, évitez d'utiliser Ubuntu 14.04 si Ubuntu 18.04 est disponible.
*   Utilisez l’authentification qui se fait par défaut avec des [clés SSH](https://docs.computecanada.ca/wiki/SSH_Keys/fr); elle est beaucoup plus sûre que par mots de passe.
*   Installez [fail2ban](https://www.fail2ban.org) pour parer les [attaques par force brute](https://fr.wikipedia.org/wiki/Attaque_par_force_brute).

## Sécurité du réseau

*   Limitez l'accès à votre service. Évitez d’utiliser 0.0.0.0 dans le champ CIDR du formulaire pour le groupe de sécurité et, en particulier, ne créez pas de règles pour 0.0.0.0 pour le groupe de sécurité par défaut, ce qui permettrait l’accès à toutes les instances du projet.
    *   Portez attention aux adresses IP rendues disponibles par la configuration du *netmask*.
*   Ne regroupez pas les ports d'accès.
*   Portez attention aux règles de sécurité, en particulier pour :
    *   les services qui ne devraient pas être accédés publiquement
        *   ssh (22); ce service permet une connexion interactive avec votre instance et NE DOIT PAS être publiquement accessible.
        *   RDP (3389); ce service permet une connexion interactive avec votre instance et NE DOIT PAS être publiquement accessible.
        *   mysql (3306)
        *   VNC (5900-5906); ce service permet une connexion interactive avec votre instance et NE DOIT PAS être publiquement accessible.
        *   postgresql (5432)
        *   nosql
        *   RDP (3389)
        *   tomcat
        *   et plusieurs autres
    *   les services qui devraient être accédés publiquement
        *   Apache (80, 443)
        *   Nginx (80, 443)
        *   et autres
*   Configurez le serveur Web pour HTTPS plutôt que HTTP.
*   Dans plusieurs cas, HTTP ne devrait être utilisé que pour rediriger vers HTTPS.
*   N'installez pas de serveur de courriel.
*   N'installez pas un serveur BitTorrent.

## Mise à jour d'une instance virtuelle

!!! note
    Effectuez régulièrement des mises à jour du système d’exploitation de vos instances, idéalement chaque semaine ou chaque fois que de nouveaux paquets sont disponibles. Utilisez les commandes suivantes, selon la distribution Linux. Vous devrez redémarrer votre instance et vous connecter à nouveau.

### Ubuntu/Debian

```bash
$ sudo apt-get update
$ sudo apt-get dist-upgrade
$ sudo reboot
```

### CentOS

```bash
$ sudo yum update
$ sudo reboot
```

### Fedora

```bash
$ sudo dnf update
$ sudo reboot
```

## Références

[Tips for Securing Your EC2 Instance](https://aws.amazon.com/articles/1233/) (article Amazon).