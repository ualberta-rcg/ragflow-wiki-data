---
title: "FTP server in the Cloud/fr"
tags:
  - cloud

keywords:
  []
---

<i>Page enfant de [Services infonuagiques](cloud-fr.md)</i>

=Meilleures options en remplacement de FTP= 
Si vous pouvez utiliser un autre protocole que FTP, il existe d'autres possibilités.

* Dans un contexte de FTP acceptant les connexions anonymes
** pour un accès en lecture seulement (<i>read only</i>), utilisez HTTP (voir [Création d'un serveur web sur un nuage](creating-a-web-server-on-a-cloud-fr.md));
** pour un accès en lecture et écriture (<i>read/write</i>), comme il est extrêmement risqué d'accepter des fichiers transférés de façon anonyme, contactez le [soutien technique](technical_support-fr.md); en connaissant votre cas particulier, nous pourrons vous aider à trouver une solution sécuritaire.
* Si vous voulez que les utilisateurs FTP soient authentifiés par des identifiants et des mots de passe
** [SFTP](transferring-data-fr#sftp.md) est une option plus sécuritaire et plus facile; 
** [FTPS](https://fr.wikipedia.org/wiki/File_Transfer_Protocol_Secure), une extension de FTP, utilise [TLS](https://fr.wikipedia.org/wiki/Transport_Layer_Security) (<i>Transport Layer Security</i>) pour crypter les données en entrée et en sortie. 
Quand l'authentification se fait par mot de passe, les données transmises devraient être cryptées pour éviter qu'une personne habile puisse décoder le mot de passe. Nous recommandons fortement de ne pas permettre l'accès par mot de passe à votre instance (ou VM pour <i>virtual machine</i>) puisque toute machine connectée à l'internet est à risque de recevoir des attaques par force brute (<i>brute-force attacks</i>). L'authentification par [clés SSH](ssh_keys-fr.md) est préférable  et fonctionne avec [SFTP](transferring-data-fr#sftp.md).

=Configurer un serveur FTP= 
Si vous devez utiliser FTP, consultez un des guides suivants, selon le système d'exploitation&nbsp;:
*[Ubuntu](https://help.ubuntu.com/lts/serverguide/ftp-server.html)
*[CentOS 6](https://www.digitalocean.com/community/tutorials/how-to-set-up-vsftpd-on-centos-6--2)
Les ports d'une instance utilisés par FTP doivent être ouverts; voyez [Groupes de sécurité](managing-your-cloud-resources-with-openstack-fr#groupes_de_sécurité.md) pour savoir comment ouvrir les ports. FTP utilise le port 21 pour lancer la requête de transfert de fichiers, mais le transfert comme tel peut s'effectuer sur un port aléatoire au-delà du port 1025; les détails varient toutefois selon le mode d'opération de FTP (par exemple, le port 20 pourrait être utilisé). Ceci signifie que, pour permettre un accès FTP à votre instance, vous devez ouvrir le port 21, possiblement le port 20 et probablement les ports au-delà de 1025. Chaque port ouvert représente un risque de sécurité et les protocoles autres que FTP sont à privilégier.
Pour plus d'information sur les ports utilisés par FTP, lisez [cet article](http://www.techrepublic.com/article/how-ftp-port-requests-challenge-firewall-security/5031026/).