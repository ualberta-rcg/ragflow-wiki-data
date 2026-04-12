---
title: "FTP server in the Cloud/fr"
slug: "ftp_server_in_the_cloud"
lang: "fr"

source_wiki_title: "FTP server in the Cloud/fr"
source_hash: "f292c6d542fcb64e641efd6e5368ed87"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:01:48.445794+00:00"

tags:
  - cloud

keywords:
  - "sécurité"
  - "SFTP"
  - "configuration des ports"
  - "transfert de fichiers"
  - "Serveur FTP"

questions:
  - "Quelles sont les alternatives recommandées au protocole FTP pour assurer un transfert de fichiers sécurisé ?"
  - "Pourquoi est-il fortement déconseillé d'utiliser une authentification par mot de passe, et quelle méthode devrait être privilégiée ?"
  - "Quels sont les ports réseau qui doivent être ouverts pour configurer un serveur FTP, et quels risques de sécurité cela implique-t-il ?"
  - "Quelles sont les alternatives recommandées au protocole FTP pour assurer un transfert de fichiers sécurisé ?"
  - "Pourquoi est-il fortement déconseillé d'utiliser une authentification par mot de passe, et quelle méthode devrait être privilégiée ?"
  - "Quels sont les ports réseau qui doivent être ouverts pour configurer un serveur FTP, et quels risques de sécurité cela implique-t-il ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Page enfant de [Services infonuagiques](cloud.md)*

## Meilleures options pour remplacer le protocole FTP

Si vous pouvez utiliser un autre protocole que FTP, il existe d'autres possibilités.

*   Dans un contexte de FTP acceptant les connexions anonymes
    *   pour un accès en lecture seulement (*lecture seulement*), utilisez HTTP (voir [Création d'un serveur web sur un nuage](creating_a_web_server_on_a_cloud.md));
    *   pour un accès en lecture et écriture (*lecture/écriture*), comme il est extrêmement risqué d'accepter des fichiers transférés de façon anonyme, contactez le [soutien technique](../support/technical_support.md); en connaissant votre cas particulier, nous pourrons vous aider à trouver une solution sécuritaire.
*   Si vous voulez que les utilisateurs FTP soient authentifiés par des identifiants et des mots de passe
    *   [SFTP](../getting-started/transferring_data.md#sftp) est une option plus sécuritaire et plus facile;
    *   [FTPS](https://fr.wikipedia.org/wiki/File_Transfer_Protocol_Secure), une extension de FTP, utilise [TLS](https://fr.wikipedia.org/wiki/Transport_Layer_Security) (*Transport Layer Security*) pour crypter les données en entrée et en sortie.

Quand l'authentification se fait par mot de passe, les données transmises devraient être cryptées pour éviter qu'une personne habile puisse décoder le mot de passe.

!!! warning "Authentification sécurisée"
    Nous recommandons fortement de ne pas permettre l'accès par mot de passe à votre instance (ou VM pour *virtual machine*) puisque toute machine connectée à l'internet est à risque de recevoir des *attaques par force brute*. L'authentification par [clés SSH](../getting-started/ssh_keys.md) est préférable et fonctionne avec [SFTP](../getting-started/transferring_data.md#sftp).

## Configurer un serveur FTP

Si vous devez utiliser FTP, consultez un des guides suivants, selon le système d'exploitation :
*   [Ubuntu](https://help.ubuntu.com/lts/serverguide/ftp-server.html)
*   [CentOS 6](https://www.digitalocean.com/community/tutorials/how-to-set-up-vsftpd-on-centos-6--2)

Les ports d'une instance utilisés par FTP doivent être ouverts; voyez [Groupes de sécurité](managing_your_cloud_resources_with_openstack.md) pour savoir comment ouvrir les ports. FTP utilise le port 21 pour lancer la requête de transfert de fichiers, mais le transfert comme tel peut s'effectuer sur un port aléatoire au-delà du port 1025; les détails varient toutefois selon le mode d'opération de FTP (par exemple, le port 20 pourrait être utilisé). Ceci signifie que, pour permettre un accès FTP à votre instance, vous devez ouvrir le port 21, possiblement le port 20 et probablement les ports au-delà de 1025.

!!! warning "Risque de sécurité lié aux ports ouverts"
    Chaque port ouvert représente un risque de sécurité et les protocoles autres que FTP sont à privilégier.

Pour plus d'information sur les ports utilisés par FTP, lisez [cet article](http://www.techrepublic.com/article/how-ftp-port-requests-challenge-firewall-security/5031026/).