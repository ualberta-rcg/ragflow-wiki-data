---
title: "Arbutus Migration Guide/fr"
slug: "arbutus_migration_guide"
lang: "fr"

source_wiki_title: "Arbutus Migration Guide/fr"
source_hash: "2409a3f543bf5db2e5c7f636b957a92c"
last_synced: "2026-05-02T23:50:34.269007+00:00"
last_processed: "2026-05-03T00:38:39.113483+00:00"

tags:
  - cloud

keywords:
  - "adresses IP flottantes"
  - "DNS entries"
  - "nuage Arbutus"
  - "configuration files"
  - "IP addresses"
  - "plan de migration"
  - "règles de sécurité SSH"
  - "copie de données"
  - "Arbutus"
  - "Swift or S3 API"
  - "Nuage Arbutus"
  - "Images Glance"
  - "Linux 'dd'"
  - "legacy shares"
  - "rsync + ssh"
  - "tenants"
  - "bucket name collisions"
  - "bucket sync"
  - "Ansible"
  - "Object Storage"
  - "Commande dd"
  - "règles de sécurité"
  - "OpenStack"
  - "serveur de migration temporaire"
  - "enregistrements DNS"
  - "clés SSH"
  - "nuage Ouest"
  - "commande dd"
  - "OpenStack CLI"
  - "Groupes de sécurité"
  - "object storage"
  - "demande de migration"
  - "Transfert de données"
  - "firewall rules"
  - "volumes"
  - "migration de volumes"
  - "métadonnées OpenStack"
  - "billet d'assistance"
  - "instances virtuelles"
  - "lancer des instances"
  - "data migration"
  - "CephFS Shared Filesystem"
  - "Arbutus Cloud"
  - "fichier RC"
  - "ressources infonuagiques"
  - "nouvelles instances"
  - "Nuage Ouest"
  - "règles Egress"
  - "groupes de sécurité"
  - "Globus Connect Personal"
  - "Volumes de données"
  - "post-transfer configurations"
  - "unauthenticated access"
  - "Migration d'instances"
  - "interface Arbutus"
  - "système Arbutus"
  - "interruption de service"
  - "instance"
  - "instance temporaire"
  - "Configuration post-migration"
  - "Cloud Object Storage"
  - "S3 credentials"
  - "volume amorçable"
  - "CLI OpenStack"
  - "migration"
  - "Copie de volume"
  - "instances et volumes"
  - "Volumes"
  - "rclone"
  - "retrait de votre projet"
  - "mise à jour des DNS"

questions:
  - "Quelle est la date limite pour effectuer la migration vers le nouveau nuage Arbutus et pourquoi cette opération est-elle obligatoire ?"
  - "Quels éléments techniques spécifiques devez-vous évaluer pour planifier votre migration, tels que la taille des volumes, le type d'instances et les outils d'automatisation ?"
  - "Quelles sont les démarches administratives à accomplir auprès de l'équipe technique pour les ressources d'accès rapide et une fois la migration terminée ?"
  - "Quelles sont les adresses URL et les navigateurs recommandés pour accéder aux interfaces web de l'ancienne et de la nouvelle génération du nuage Arbutus ?"
  - "Comment doit-on configurer l'environnement de ligne de commande à l'aide des fichiers RC sur le serveur de migration ?"
  - "Quelles sont les étapes requises pour migrer correctement les clés SSH ainsi que les groupes et règles de sécurité vers le nouveau nuage ?"
  - "Qui doit être informé de l'interruption de service et à quel moment le projet peut-il la gérer ?"
  - "Quelle démarche faut-il suivre pour la migration si les ressources ont été allouées via le service d'accès rapide ?"
  - "Quelle action doit être entreprise concernant l'ancien système Arbutus une fois la migration terminée ?"
  - "Comment doit-on procéder pour identifier et reproduire les groupes de sécurité existants sur le nuage Arbutus ?"
  - "Quelles règles de sécurité spécifiques ne doivent en aucun cas être supprimées lors de la configuration ?"
  - "Quelles sont les conséquences potentielles de la suppression des règles Egress par défaut pour les instances OpenStack ?"
  - "Quelles sont les commandes CLI permettant de créer et de lister les groupes de sécurité et leurs règles dans OpenStack ?"
  - "Quelles modifications spécifiques doivent être apportées au fichier RC et à l'environnement virtuel pour configurer l'accès au nouveau nuage Arbutus ?"
  - "Quelles sont les étapes générales recommandées pour effectuer une migration manuelle ou orchestrée des instances et des volumes vers Arbutus ?"
  - "Quelles sont les méthodes mentionnées pour copier les données des anciennes vers les nouvelles instances ?"
  - "Quelles actions doivent être effectuées concernant les adresses IP, les DNS et les anciens volumes une fois les nouvelles instances prêtes ?"
  - "Quel outil d'orchestration peut être utilisé pour automatiser l'ensemble de ces étapes de migration au lieu de les faire manuellement ?"
  - "Quelle est la méthode recommandée pour la migration des volumes en fonction de leur taille ?"
  - "Quelles sont les étapes principales pour migrer une instance associée à un volume à l'aide des images Glance entre le nuage Ouest et Arbutus ?"
  - "En quoi consiste la méthode alternative de migration utilisant la commande Linux 'dd' et comment doit-elle être initiée ?"
  - "Quel outil Linux est utilisé dans cette méthode alternative pour effectuer la migration ?"
  - "Quel type d'instance doit être lancé sur le nuage Ouest pour servir de serveur de migration temporaire ?"
  - "Quels sont les prérequis logiciels nécessaires pour que la distribution Linux puisse être utilisée dans cette procédure ?"
  - "Comment installer et vérifier le client en ligne de commande (CLI) OpenStack sur l'instance de migration temporaire ?"
  - "Quelle est la procédure pour créer une image à partir d'un volume attaché en utilisant l'utilitaire dd et l'importer dans le nuage Arbutus ?"
  - "Quelles sont les étapes recommandées pour migrer de très grands volumes ou des volumes amorçables entre les nuages Ouest et Arbutus ?"
  - "Comment la commande `dd` est-elle utilisée conjointement avec SSH pour copier un volume de l'instance Ouest vers l'instance Arbutus ?"
  - "Quelles sont les étapes requises pour installer et configurer le CLI OpenStack sur une instance éphémère active avant sa migration ?"
  - "Comment créer une nouvelle image OpenStack directement à partir du disque racine d'une instance éphémère à l'aide de l'utilitaire `dd` ?"
  - "Comment doit-on configurer les règles de sécurité SSH pour autoriser la connexion de l'instance temporaire Ouest vers l'instance temporaire Arbutus ?"
  - "Quelles sont les caractéristiques requises lors de la création d'un nouveau volume dans Arbutus pour qu'il corresponde à celui déplacé depuis Ouest ?"
  - "Quelle action finale doit être effectuée avec le nouveau volume une fois qu'il a été créé et correctement identifié dans Arbutus ?"
  - "Comment lancer des instances sur Arbutus à partir d'une image ?"
  - "Quelles conditions préalables faut-il remplir avant de supprimer les anciennes ressources sur le nuage Ouest ?"
  - "Quelles sont les différentes méthodes disponibles pour la copie de données ?"
  - "Quelle méthode est recommandée pour transférer de très grands volumes de données et comment la configurer ?"
  - "Comment utiliser la méthode rsync avec SSH pour transférer de plus petits volumes de données entre les instances ?"
  - "Quelles sont les configurations post-migration à effectuer une fois le transfert de données vers la nouvelle instance terminé ?"
  - "What is the recommended procedure for migrating data from a legacy CephFS shared filesystem to the new Arbutus Cloud?"
  - "What specific changes must be made to the configuration file and mount command when setting up a new CephFS share?"
  - "What are the key differences and considerations, such as endpoints and tenant structures, to keep in mind when migrating to the new Arbutus Cloud Object Storage?"
  - "What specific updates need to be made to host-based firewall rules after transferring to a new instance?"
  - "How should you manage DNS entries for custom domains during the post-transfer configuration process?"
  - "Which system and application configuration files typically require IP address updates on the new instance?"
  - "How does the use of tenants in Cloud Object Storage prevent bucket name collisions across different projects?"
  - "What is the difference in how a tenant is identified for authenticated API access versus unauthenticated public access?"
  - "How do users determine the correct URL for unauthenticated access depending on whether they are using Swift or S3?"
  - "What tool is recommended for migrating object storage between the legacy and new Arbutus Cloud environments, and what is the command to sync all buckets?"
  - "How does the migration process affect the access control lists (ACLs) and default privacy settings of the copied buckets?"
  - "What specific credentials and endpoint information are required to properly configure the rclone settings file for both environments?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Vous trouverez ici l'information sur la migration d'instances virtuelles (ou VM pour *virtual machines*) à partir du nuage Arbutus de la génération précédente vers le nuage Arbutus amélioré de la nouvelle génération. Puisque vous connaissez bien vos opérations, nous vous recommandons de gérer vous-mêmes la migration vers le nouveau nuage en fonction des logiciels que vous utilisez et de votre disponibilité.

Il est important de migrer toutes vos ressources infonuagiques (instances, volumes de stockage, conteneurs de stockage objet, réseaux, clés, etc.) vers le nouveau nuage Arbutus puisque le système précédent deviendra hors service au cours de 2026. **La date limite pour migrer vos ressources est le 31 août 2026**. Ceci s'applique autant aux ressources allouées par concours qu'à celles qui ont été obtenues par le service d'accès rapide.

Nous décrivons ici quelques méthodes de migration. Avec votre équipe de recherche, vous devez identifier la ou les approches en fonction de votre projet.

Ces informations peuvent soulever des questions ou encore, vous voudrez peut-être discuter de la meilleure approche pour votre situation avec notre équipe technique. Vous pouvez alors écrire à cloud@tech.alliancecan.ca.

## Planifier la migration

Les questions suivantes vous aideront à planifier la migration.

*   Quelles sont les ressources qui doivent être migrées vers le nouveau nuage Arbutus? Il n'est pas obligatoire de migrer toutes les ressources; par exemple, des volumes ou des instances qui ne sont plus nécessaires peuvent être supprimés. **Créez une liste de toutes les ressources qui doivent être migrées.**
*   Vos instances sont-elles éphémères ou sont-elles basées sur des volumes? Les instances basées sur des volumes démarrent à partir d'un volume (par exemple, /dev/vda) et peuvent également avoir d'autres volumes (par exemple, /dev/vdb). Les instances éphémères ne démarrent pas à partir d'un volume. **Listez les instances basées sur des volumes séparément des instances éphémères.**
*   Vos volumes font-ils plus de 150 Go? Si c'est le cas, ils doivent être migrés à l'aide de Globus. **Identifiez les volumes de plus de 150 Go.**
*   Avez-vous utilisé un système de déploiement automatisé (par exemple, Terraform, Ansible) sur le nuage Arbutus de la génération précédente? **Si c'est le cas, les mêmes outils d'automatisation doivent être utilisés pour la migration.**
*   Utilisez-vous des entrées DNS personnalisées? Ces entrées devront être mises à jour, car le nouveau nuage Arbutus utilise des plages d'adresses IP flottantes différentes de celles du système précédent.
*   Pour gérer vos ressources infonuagiques, utilisez-vous le tableau de bord OpenStack (interface web Horizon) ou l'interface en ligne de commande (CLI) OpenStack? **Les migrations simples peuvent être effectuées via l'interface web; par contre, les migrations plus complexes peuvent nécessiter un accès à l'interface en ligne de commande.**
*   Les membres de votre équipe ont-ils tout un compte OpenStack? Veuillez noter que le partage de compte est strictement interdit. **Toute personne ayant besoin d'un compte doit en [faire la demande ici sur CCDB](../getting-started/apply_for_a_ccdb_account.md).**
*   Comment gérerez-vous les interruptions de service requises pour la migration? Selon l’étendue des éléments à migrer, **l’interruption peut durer de quelques heures à quelques jours. Qui doit en être informé? Quand votre projet est-il en mesure de gérer une interruption de service?**
*   Vos ressources ont-elles été allouées via le service d'accès rapide? Si c'est le cas, **vous devrez soumettre une demande de migration à cloud@tech.alliancecan.ca.**
*   Une fois la migration terminée, **veuillez soumettre un billet d'assistance pour demander le retrait de votre projet sur l'ancien système Arbutus.**

Avec les réponses à ces questions, vous pourrez élaborer un plan de migration.

## Information de base
Utilisez les adresses URL suivantes pour obtenir l'interface web Horizon :

**Génération précédente** [https://arbutus.cloud.computecanada.ca](https://arbutus.cloud.computecanada.ca)

**Nouveau nuage Arbutus :**
[https://arbutus.alliancecan.ca](https://arbutus.alliancecan.ca/)

Vous pouvez utiliser les navigateurs Firefox et Chrome; Safari et Edge pourraient fonctionner, mais ils n'ont pas été testés.

Votre projet, votre réseau et votre routeur auront été créés sur Arbutus et vous aurez accès aux mêmes projets que sur le nuage Ouest.

Avant de migrer vos instances, nous vous recommandons d'effectuer les étapes suivantes pour bien configurer l'environnement.

1.  !!! warning "Important"
    Faites une copie de sauvegarde des données importantes. Le nuage est doté de systèmes de stockage redondants, mais les instances ne sont pas sauvegardées.

2.  Connectez-vous au nuage avec les informations d'identification pour votre compte et téléchargez les fichiers RC pour configurer les variables d'environnement utilisées par les outils en ligne de commande OpenStack.
    *   Ouest : *Compute -> Accès et Sécurité* -> onglet *Accès API*, cliquez sur le bouton *Télécharger le fichier RC d'OpenStack*.
    *   Arbutus : *Projet -> Accès API*, cliquez sur le bouton *Télécharger le fichier RC d'OpenStack*, sélectionnez *Fichier OpenStack RC (Identity API v3)*.
3.  Copiez les fichiers RC sur le serveur de migration `cloudmigration.calculcanada.ca`. Pour vous connecter, utilisez le nom d’utilisateur et le mot de passe de votre compte.
4.  Ouvrez deux sessions sur le serveur de migration, une pour le nuage Ouest et l’autre pour le nuage Arbutus. Nous vous recommandons d’utiliser la commande `screen` pour éviter de perdre ces sessions en cas de problème avec la connexion SSH; au besoin, consultez [ces tutoriels](https://www.google.com/search?q=screen+ssh) pour la commande `screen`. Dans la session pour Ouest, faites un source du fichier RC du nuage Ouest avec `source oldcloudrc.sh`. Dans la session pour Arbutus, faites un source du fichier RC du nuage Arbutus avec `source newcloudrc.sh`. Testez la configuration avec une commande OpenStack simple, par exemple `openstack volume list`.
5.  Migrez les clés SSH :
    *   Avec le tableau de bord Horizon sur le nuage Ouest, sélectionnez *Accès et Sécurité -> Paires de clés*. Cliquez sur le nom de la paire de clés que vous voulez et copiez la valeur de la clé publique.
    *   Avec le tableau de bord Horizon sur le nuage Arbutus, sélectionnez *Compute -> Paires de clés*.
    *   Cliquez sur *Importer une paire de clés*, donnez un nom à votre paire de clés et collez la clé publique dans le champ approprié du formulaire.
    *   Votre paire de clé devrait maintenant être importée dans Arbutus. Répétez ces étapes pour toutes les clés dont vous avez besoin.
    *   Vous pouvez aussi générer de nouvelles paires de clés.
    *   Les paires de clés peuvent aussi être importées via le CLI comme suit :
        ```bash
        openstack keypair create --public-key <fichier-clé-publique> <nom>
        ```
6.  Migrez les groupes de sécurité et les règles :
    *   Sur le nuage Ouest, sélectionnez *Compute -> Accès et Sécurité -> Groupes de sécurité* et notez les groupes existants et les règles qui y sont associées.
    *   Sur le nuage Arbutus, sélectionnez *Réseau -> Groupes de sécurité* et reproduisez les groupes et règles qui s’appliquent.
    *   !!! warning
        Ne supprimez pas les règles de sécurité Egress créées par défaut pour IPv4 et IPv6; ceci pourrait créer plusieurs problèmes, entre autres empêcher vos instances d’obtenir les données de configuration du service de métadonnées OpenStack.
    *   Les groupes et les règles peuvent aussi être créés via le CLI. Dans cet exemple, nous utilisons le port HTTP 80; modifiez les commandes selon vos besoins.
        ```bash
        openstack security group create <nom-du-groupe>
        openstack security group rule create --proto tcp --remote-ip 0.0.0.0/0 --dst-port 80 <nom-du-groupe>
        ```
    *   Pour voir les règles via le CLI, listez les groupes de sécurité avec `openstack security group list` et les règles du groupe avec `openstack security group rule list`.
7.  En général, pour éviter la corruption ou l'incohérence des données après une migration, il est préférable de fermer les services, puis d'éteindre l'instance. Les petits volumes se copient relativement rapidement; par exemple, un volume de 10 Go prendra moins de 5 minutes, mais un volume de 100 Go peut prendre de 30 à 40 minutes. De plus, les adresses IP flottantes seront modifiées; assurez-vous donc que le TTL de vos enregistrements DNS est bas afin que les modifications soient propagées le plus rapidement possible.

## Modifier le fichier RC dans le nouveau nuage Arbutus
Après avoir téléchargé un nouveau fichier RC du nouveau nuage Arbutus, vous devez le modifier en ajoutant les lignes suivantes :

```bash
export OS_AUTH_TYPE=v3websso
export OS_IDENTITY_PROVIDER=atmosphere
export OS_PROTOCOL=openid
export OS_PROJECT_DOMAIN_NAME=default
```

Supprimez les lignes qui contiennent :

```bash
export OS_USER_DOMAIN_NAME="atmosphere" 
if [ -z "$OS_USER_DOMAIN_NAME" ]; then unset OS_USER_DOMAIN_NAME; fi
```

Supprimez aussi :

```bash
echo "Please enter your OpenStack Password for project $OS_PROJECT_NAME as user $OS_USERNAME: " 
read -sr OS_PASSWORD_INPUT 
export OS_PASSWORD=$OS_PASSWORD_INPUT
```

Le fichier RC final devrait contenir des lignes qui ressemblent à celles-ci :
```bash
export OS_AUTH_URL=https://identity.arbutus.alliancecan.ca/ 
export OS_PROJECT_ID=xIDx 
export OS_PROJECT_NAME=" xIDx " 
export OS_PROJECT_DOMAIN_ID=" xIDx " 
unset OS_TENANT_ID 
unset OS_TENANT_NAME 
export OS_USERNAME=" xIDx " 
export OS_REGION_NAME="RegionOne" 
export OS_INTERFACE=public 
export OS_IDENTITY_API_VERSION=3 
export OS_AUTH_TYPE=v3websso  
export OS_IDENTITY_PROVIDER=atmosphere  
export OS_PROTOCOL=openid 
export OS_PROJECT_DOMAIN_NAME=default 
```

Maintenant, créez un environnement virtuel pour installer le client OpenStack et les autres paquets nécessaires.
```bash
python3 -m venv openstack 
source openstack/bin/activate 
pip install python-openstackclient keystoneauth-websso python-manilaclient
```

## Scénarios de migration
Il y a trois scénarios de migration généraux à considérer.
*   [Migration manuelle ou orchestrée](#migration-manuelle-ou-orchestrée)
*   [Migration d'instances associées à des volumes](#migration-dinstances-associées-à-des-volumes)
*   [Migration d'instances éphémères](#migration-dinstances-éphémères)
Selon votre configuration actuelle, vous pouvez utiliser l'un ou l'autre de ces scénarios, ou tous.

### Migration manuelle ou orchestrée

Les instances et volumes sont créés sur Arbutus avec les mêmes caractéristiques que sur le nuage Ouest. Règle générale, les grandes lignes de la procédure sont :

1.  Si vous utilisez des images personnalisées, copiez les images Glance du nuage Ouest à Arbutus. Vous pouvez aussi simplement commencer avec une nouvelle image de base sur Arbutus.
2.  Installez et configurez les services sur la ou les instances.
3.  Copiez les données des anciennes instances vers les nouvelles instances (voir [Méthodes de copie de données](#méthodes-de-copie-de-données) ci-dessous).
4.  Assignez des adresses IP flottantes aux nouvelles instances et faites la mise à jour des DNS.
5.  Mettez fin aux anciennes instances et supprimez les anciens volumes.

Ces étapes peuvent être effectuées manuellement ou être orchestrées avec [Ansible](https://docs.ansible.com/ansible/2.5/modules/list_of_cloud_modules.html), [Terraform](https://www.terraform.io/docs/providers/openstack/ Terraform) ou [Heat](https://wiki.openstack.org/wiki/Heat).
Le présent document ne traite pas de ces outils; cependant, si vous les utilisez sur le nuage Ouest, ils devraient fonctionner de la même manière sur Arbutus.

### Migration d'instances associées à des volumes

Comme leur nom l’indique, chacune de ces instances est associée à un volume persistant qui contient le système d’exploitation et les données nécessaires. Une bonne pratique est de créer des volumes distincts pour le système d’exploitation et pour les données.

#### Migration avec des images Glance

Ce scénario est recommandé dans le cas de volumes de moins de 150 Go. Pour les volumes plus grands, la [migration manuelle ou orchestrée](#migration-manuelle-ou-orchestrée) est préférable.

1.  Ouvrez deux sessions sur le serveur de migration `cloudmigration.calculcanada.ca` avec le nom d’utilisateur et le mot de passe de votre compte.
2.  Dans la session pour Ouest, faites un source du fichier RC du nuage Ouest avec `source oldcloudrc.sh`. Dans la session pour Arbutus, faites un source du fichier RC du nuage Arbutus avec `source newcloudrc.sh`. Nous vous recommandons d’utiliser la commande `screen` pour éviter de perdre ces sessions en cas de problème avec la connexion SSH; au besoin, consultez [ces tutoriels](https://www.google.com/search?q=screen+ssh) pour la commande `screen`.
3.  Dans l’interface utilisateur du nuage Ouest, créez une image du volume voulu par *Compute -> Volumes* et *Télécharger dans l'image* du menu déroulant. Le volume ne devrait pas être actif à ce moment, mais s’il l’est, vous pouvez utiliser l’option *force*. Assurez-vous de sélectionner le format de disque QCOW2. Ceci peut aussi se faire en ligne de commande :
    ```bash
    cinder --os-volume-api-version 2 upload-to-image <nom-du-volume> <nom-de-l-image> --force
    ```
4.  Une fois créée, l’image sera listée sous *Compute -> Images* avec le nom que vous avez utilisé à l’étape précédente. Pour obtenir l’identifiant de l’image, cliquez sur son nom.
5.  Sur le serveur de migration, dans la session pour le nuage Ouest, téléchargez l’image (remplacez `<nom-du-fichier>` et `<id-de-l-image>` avec les valeurs appropriées) :
    ```bash
    glance image-download --progress --file <nom-du-fichier> <id-de-l-image>
    ```
6.  Sur le serveur de migration, dans la session pour le nuage Arbutus, téléchargez l’image (remplacez `<nom-du-fichier>` par le nom donné à l’étape précédente; la valeur de `<nom-de-l-image>` importe peu).
    ```bash
    glance image-create --progress --visibility private --container-format bare --disk-format qcow2 --name <nom-de-l-image> --file <nom-du-fichier>
    ```
7.  Vous pouvez maintenant créer un volume à partir de l’image téléversée. Dans l’interface utilisateur du nuage Arbutus, allez à *Compute -> Images*. L’image téléversée à l’étape précédente devrait paraître. Dans le menu déroulant pour l’image, sélectionnez l’option *Créer le volume* pour créer le volume à partir de l’image. Le volume ainsi créé peut maintenant être associé à des instances ou utilisé pour démarrer une nouvelle instance.
8.  Une fois que vos instances et volumes ont été migrés et testés et que tous vos enregistrements DNS ont été mis à jour, veuillez supprimer les anciens volumes et instances sur le nuage Ouest.

#### Autre option avec Linux 'dd'

1.  Lancez une instance sur le nuage Ouest avec le plus petit gabarit possible (par exemple p1-1.5gb). Nous pouvons considérer ceci comme étant un serveur de migration temporaire. Dans les étapes qui suivent, nous avons sélectionné CentOS 7, mais les distributions Linux avec Python et Pip devraient fonctionner de même.
2.  Connectez-vous à l’instance avec SSH et installez le CLI OpenStack en tant que superutilisateur (root).
    ```bash
    yum install epel-release
    yum install python-devel python-pip gcc
    pip install python-openstackclient
    ```
3.  Le CLI OpenStack devrait maintenant être installé. Pour vérifier, lancez la commande `openstack` en ligne de commande. Pour plus d’information sur l’installation du CLI, consultez [https://docs.openstack.org/newton/user-guide/common/cli-install-openstack-command-line-clients.html](https://docs.openstack.org/newton/user-guide/common/cli-install-openstack-command-line-clients.html).
4.  Copiez le fichier RC d’Arbutus vers le serveur de migration temporaire et faites un source. Pour vérifier si vous pouvez vous connecter à l’API OpenStack sur Arbutus, lancez la commande :
    ```bash
    openstack image list
    ```
5.  Supprimez l’instance à déplacer mais **NE SUPPRIMEZ PAS** le volume qui y est associé.
6.  Le volume peut maintenant être associé au serveur de migration temporaire que nous avons créé : sur l’interface utilisateur du nuage Ouest, allez à *Compute -> Volumes*, sélectionnez *Gérer les pièces jointes* du menu déroulant et attachez le volume au serveur de migration temporaire.
7.  Notez le chemin d'accès au périphérique auquel le volume est attaché (généralement /dev/vdb ou /dev/vdc).
8.  Avec l’utilitaire `dd` créez une image à partir du disque attaché à l’instance. Dans l’exemple suivant, le nom de l’image est `volumemigrate`. Lorsque l’opération est terminée, les détails de l’image seront affichés.
    ```bash
    dd if=/dev/vdb | openstack image create --private --container-format bare --disk-format raw "volumemigrate"
    ```
9.  Vous devriez maintenant voir l’image en allant à *Compute -> Images* dans l’interface Arbutus. Cette image peut être utilisée pour lancer des instances sur Arbutus. Pour que les données soient persistantes, assurez-vous de créer un nouveau volume au lancement de l’instance.
10. Une fois que vos instances et volumes ont été migrés et testés et que tous vos enregistrements DNS ont été mis à jour, veuillez supprimer les anciens volumes et instances sur le nuage Ouest.

#### Migration de grands volumes avec Linux 'dd'
Dans le cas de volumes, l'utilisation des images n'est pas recommandée. Copiez plutôt vos données dans de nouveaux volumes avec rsync ou un autre outil de copie, lorsque possible. Dans le cas contraire, par exemple pour un volume amorçable (*bootable*), vous pouvez utiliser la commande `dd` pour produire une copie identique.

!!! warning
    Sauvegardez les données importantes avant d'exécuter cette procédure.

1.  Créez une instance temporaire sur Ouest (p1-1.5gb devrait convenir). Faites de même sur Arbutus. Utilisez le système d'exploitation CentOS 7.
2.  Assignez aux deux instances des adresses IP flottantes par lesquelles vous pourrez vous connecter via SSH.
3.  Dans l'instance temporaire sur Ouest, installez les paquets :
    ```bash
    yum install epel-release
    yum install pv
    yum install screen
    ```
4.  Dans l'instance temporaire sur Arbutus :
    ```bash
    chmod u+s /bin/dd
    ```
5.  Copiez dans l'instance temporaire Ouest la clé privée SSH qui sert à vous connecter en tant qu'utilisateur centos à l'instance temporaire Arbutus.
6.  Vérifiez que les règles de sécurité SSH permettent à l'instance temporaire Ouest de se connecter à l'instance temporaire Arbutus.
7.  Pour chacun des volumes à déplacer de Ouest à Arbutus :
    *   Créez un volume vide de la même taille dans Arbutus; s'il s'agit d'un volume amorçable, identifiez-le comme tel (*bootable*).
    *   Attachez ce volume à l'instance temporaire Arbutus.
    *   Attachez le volume à copier de Ouest à l'instance temporaire Ouest. Vous devrez peut-être supprimer l'instance à laquelle le volume est présentement attaché. **Ne supprimez pas le volume.**
8.  Dans l'instance temporaire Ouest, exécutez les commandes ci-dessous. La commande `screen` est utilisée au cas où vous seriez déconnecté de la session SSH. Pour ce qui est de la seconde commande, nous supposons que le volume source /dev/vdb dans Ouest est attaché à l'instance temporaire Ouest, que la taille du volume est de 96 Go, que la clé SSH pour se connecter à l'instance temporaire Arbutus est key.pem, et que le volume de destination dans Arbutus /dev/vdb est attaché à l'instance temporaire Arbutus. Remplacez l'adresse IP par celle de l'instance Arbutus à laquelle vous voulez vous connecter.
    ```bash
    screen
    sudo dd bs=16M if=/dev/vdb | pv -s 96G | ssh -i key.pem centos@xxx.xx.xx.xx "dd bs=16M of=/dev/vdb"
    ```

Vous disposez maintenant dans Arbutus d'une copie identique du volume Ouest et vous pouvez l'utiliser pour lancer des instances dans Arbutus.

### Migration d'instances éphémères

Une instance éphémère n'est associée à aucun volume.

#### Avec images et instantanés de volume Glance

Voir ci-dessus la section [Migration avec des images Glance](#migration-avec-des-images-glance).

#### Autre option avec Linux 'dd'

1.  Connectez-vous à l’instance active sur le nuage Ouest avec SSH. Avant de migrer une instance éphémère, il est important de fermer le plus de services possible (par exemple httpd, bases de données, etc.) et de ne garder que SSH.
2.  Avec le rôle d’administrateur (*root*) installez le CLI OpenStack si ce n’est pas déjà fait.
    ```bash
    yum install epel-release
    yum install python-devel python-pip gcc
    pip install python-openstackclient
    ```
3.  Le CLI OpenStack devrait maintenant être installé. Pour vérifier, lancez la commande `openstack` en ligne de commande. Pour plus d’information sur l’installation du CLI, consultez [https://docs.openstack.org/newton/user-guide/common/cli-install-openstack-command-line-clients.html](https://docs.openstack.org/newton/user-guide/common/cli-install-openstack-command-line-clients.html).
4.  Copiez le fichier RC d’Arbutus vers l’instance et faites un source. Pour vérifier si vous pouvez vous connecter à l’API OpenStack sur Arbutus, lancez la commande :
    ```bash
    openstack image list
    ```
5.  Le disque racine de l’instance est généralement `/dev/vda1`; vérifiez ceci en lançant la commande `df`.
6.  Avec l’utilitaire `dd`, créez une image à partir du disque racine attaché à l’instance. Dans l’exemple suivant, le nom de l’image est `ephemeralmigrate`. Lorsque l’opération est terminée, les détails de l’image seront affichés.
    ```bash
    dd if=/dev/vda | openstack image create --private --container-format bare --disk-format raw "ephemeralmigrate"
    ```
7.  Vous devriez maintenant voir l’image en allant à *Compute -> Images* dans l’interface Arbutus. Cette image peut être utilisée pour lancer des instances sur Arbutus.
8.  Une fois que vos instances et volumes ont été migrés et testés et que tous vos enregistrements DNS ont été mis à jour, veuillez supprimer les anciens volumes et instances sur le nuage Ouest.

### Méthodes de copie de données

Vous pouvez utiliser une méthode de copie avec laquelle vous êtes familier, mais nous recommandons les deux suivantes, selon la taille des volumes dans votre projet.

#### Grands volumes de données : Globus
Pour les très grands volumes (plus de 5 To), nous recommandons Globus.

La méthode la plus simple est d'utiliser le client Globus Connect Personal avec un abonnement Globus Plus.

1.  **Abonnez-vous à Globus Connect Personal Plus.**
    *   Écrivez à globus@tech.alliancecan.ca.
    *   Répondez à l'invitation Globus Personal Plus et suivez les directives.
2.  **Pour chacune des instances touchées par le transfert de données, activez Globus Connect Personal.**
    *   Prenez connaissance de [Globus, Ordinateurs personnels](../getting-started/globus.md#ordinateurs-personnels) et de [https://www.globus.org/globus-connect-personal](https://www.globus.org/globus-connect-personal).
    *   Utilisez les directives appropriées pour installer Globus Connect Personal dans chaque instance. Pour Linux, consultez [https://docs.globus.org/how-to/globus-connect-personal-linux/](https://docs.globus.org/how-to/globus-connect-personal-linux/).
    *   Modifiez la configuration de chacune des instances pour communiquer avec le service Globus.
        *   Vérifiez que chaque instance possède une adresse IP externe.
        *   Vérifiez que le pare-feu des instances permet la [communication par les ports](https://docs.globus.org/how-to/configure-firewall-gcp/); voir aussi [Groupes de sécurité](managing_your_cloud_resources_with_openstack.md#groupes-de-sécurité).
        *   L'utilisateur qui exécute Globus Connect Personal doit avoir accès aux données dans les systèmes de fichiers de stockage.
    *   Dans l'espace utilisateur, exécutez Globus Connect Personal en arrière-plan.
    *   Comme abonné Globus Connect Personal Plus (étape 1), créez un point d'accès partagé pour une ou les deux instances.
3.  **Par l'interface Globus (globus.org, globus.calculcanada.ca) accédez aux points d'accès et transférez les données.**
    *   Voyez [https://docs.globus.org/how-to/get-started/](https://docs.globus.org/how-to/get-started/)

Pour plus d'information sur la configuration, consultez [https://computecanada.github.io/DHSI-cloud-course/globus/](https://computecanada.github.io/DHSI-cloud-course/globus/).

!!! tip
    En cas de difficulté, contactez le [soutien technique](../support/technical_support.md) (globus@tech.alliancecan.ca). Il est fortement suggéré de soumettre aussi une demande d’assistance au service technique.

#### Petits volumes de données : rsync + ssh
Pour les plus petits volumes, rsync + ssh offre de bonnes vitesses de transfert et, comme Globus, travaille de manière incrémentale.

Voici un exemple de cas type :

1.  Connectez-vous avec SSH à l’instance sur le nuage Ouest qui possède le volume principal. Prenez note du chemin absolu que vous voulez copier dans l’instance sur Arbutus.
2.  Lancez rsync sur SSH. Dans l’exemple suivant, on suppose qu’il existe une connexion sans mot de passe via des [clés SSH](../getting-started/ssh_keys.md). Utilisez les valeurs appropriées.
    ```bash
    rsync -avzP -e 'ssh -i ~/.ssh/key.pem' /local/path/ remoteuser@remotehost:/path/to/files/
    ```
3.  Vérifiez que les données ont bien été copiées dans l’instance sur Arbutus, puis supprimez les données sur le nuage Ouest.

### Configuration post-migration

Une fois que vous avez transféré vos données vers la nouvelle instance, certaines configurations post-transfert peuvent être requises. Ces activités pourraient inclure :

1.  Mettre à jour les règles de pare-feu pour utiliser de nouvelles adresses IP et réseaux si un pare-feu basé sur l'hôte (par exemple iptables, firewalld, etc.) est utilisé.
2.  Collaborer avec votre fournisseur DNS pour mettre à jour les entrées DNS pour tous les domaines personnalisés (par exemple, www.monprojetarbutus.ca).
3.  Mettre à jour les adresses IP dans les fichiers de configuration (par exemple, /etc/hosts, /etc/resolv.conf, /etc/haproxy/haproxy.cfg, /var/www/, /var/lib/pgsql/data/pg_hba.conf).
4.  Modifier les noms d'utilisateur (par exemple, 'root'@'192.168.65.%') dans MySQL.
5.  Renouveler les certificats Let's Encrypt Transport Layer Security (TLS) à l'aide de certbot ou d'autres utilitaires, par exemple s'il y a des adresses IP dans le Subject Alternate Name (SAN) du certificat.
6.  Tester la configuration.

Quand les tests auront été faits, informez les membres de votre équipe que la migration est terminée.

### Migration d'un système de fichiers partagé CephFS

Le nouveau système de fichiers partagé CephFS du nuage Arbutus est un service distinct et séparé, et toute donnée souhaitée doit être intentionnellement migrée.

La gestion des partages existants (*legacy shares*), y compris les opérations de création, de suppression et de gestion des clés, est contrôlée via l'ancien nuage Arbutus. Cependant, une fois qu'un partage et une clé existants sont créés, ces ressources peuvent être accédées depuis une machine virtuelle dans le nouveau nuage Arbutus. De même, la création et la gestion des partages dans le nouveau nuage Arbutus se font exclusivement dans l'environnement du nouveau nuage Arbutus.

Les partages existants et les nouveaux partages peuvent être montés sur des machines virtuelles du nouveau nuage Arbutus. La procédure suivante est l'une des méthodes recommandées pour migrer des données entre les partages existants et les nouveaux partages.

1.  Pour chaque partage dans l'ancien nuage Arbutus, créez un partage équivalent dans le nouveau Arbutus.
2.  Montez les deux partages à des emplacements de montage distincts sur la même machine virtuelle dans le nouveau nuage Arbutus.
3.  Utilisez un outil de copie de données tel que "rsync" pour transférer les données de l'ancien partage vers le nouveau et assurez l'intégrité des données.

La procédure pour monter les partages existants est inchangée et peut être trouvée ici : https://docs.alliancecan.ca/wiki/CephFS

La création du partage équivalent dans le nouveau nuage Arbutus suivra la même procédure, avec quelques différences essentielles :

1.  Vous devez créer le nouveau partage et les clés d'accès en utilisant l'interface web du nouveau nuage Arbutus.
2.  Vous devez créer un fichier `ceph.conf` séparé, avec un nom distinct tel que "ceph-new.conf".
3.  La valeur de configuration "mon_host" devra être mise à jour pour le nouveau partage seulement, dans le fichier "ceph-new.conf" :
    *   Ancienne valeur :
        ```text
        10.30.201.3:6789,10.30.202.3:6789,10.30.203.3:6789
        ```
    *   Nouvelle valeur :
        ```text
        134.87.15.61:6789,134.87.15.62:6789,134.87.15.63:6789
        ```
4.  Lors du montage du nouveau partage, une valeur supplémentaire dans la commande de montage est requise après le "-o" pour spécifier le nouveau fichier de configuration : "conf=/etc/ceph/ceph-new.conf".

Une fois les deux partages montés, utilisez rsync pour transférer les données. Les drapeaux `a`, `v`, et `P` pour rsync sont recommandés.

```bash
rsync -avp /mnt/ancien-partage/ /mnt/nouveau-partage/
```

Gardez à l'esprit qu'en fonction de la taille de votre partage, cela peut prendre beaucoup de temps. Il est conseillé d'utiliser un outil tel que "screen" ou "tmux" pour maintenir la session active en cas de perte de connexion.

### Migration de stockage objet

Le nouveau service de stockage objet du nuage Arbutus est un service distinct et séparé de l'ancien, et toute donnée souhaitée doit être intentionnellement migrée.

La gestion des conteneurs (*buckets*) et objets existants, y compris les opérations de création, de suppression, de manipulation d'objets et de gestion des clés, est contrôlée via l'ancien nuage Arbutus. De même, la création et la gestion des conteneurs et des objets dans le nouveau nuage Arbutus se font exclusivement dans l'environnement du nouveau nuage Arbutus.

La migration des données vers le nouveau service de stockage objet du nuage Arbutus peut être effectuée en utilisant diverses méthodes et outils. Si vous êtes familier avec les options, n'hésitez pas à utiliser la méthode qui convient le mieux à vos données.

**Point d'accès (Endpoint) du nouveau stockage objet Arbutus :** `https://object-arbutus.alliancecan.ca`

**Point d'accès (Endpoint) de l'ancien stockage objet Arbutus :** `https://object-arbutus.cloud.computecanada.ca`

Soyez prudent si vous utilisez des ACLs de conteneurs; assurez-vous que l'outil que vous utilisez les copie correctement, ou recréez-les dans le nouvel environnement. La plupart des outils ne préservent pas les ACLs de conteneurs. Gardez à l'esprit que si vous référencez des UUIDs d'utilisateurs ou de projets, ils seront différents dans le nouveau nuage Arbutus.

De plus, le nouveau stockage objet du nuage Arbutus utilise des projets (locataires). Ainsi, les conflits de noms de conteneurs ne se produiront qu'au sein d'un projet individuel, et non pas sur tous les projets d'Arbutus. Lors de l'authentification avec l'API Swift ou S3, le projet est déduit de l'utilisateur/clé fourni. Cependant, pour un accès public aux conteneurs sans authentification, le projet doit être spécifié. L'ID du projet est identique à l'ID du projet OpenStack. L'URL pour l'accès Swift non authentifié peut être trouvée via l'interface Horizon, tandis que l'URL pour l'accès S3 non authentifié aura le format suivant :

```text
https://object-arbutus.alliancecan.ca/<id-projet>:<nom-du-conteneur>/<nom-de-l-objet>
```

Si vous n'êtes pas sûr de l'outil à utiliser, nous vous recommandons d'utiliser rclone. Rclone ne copiera pas les ACLs de conteneurs, de sorte que tous les accès seront initialement privés dans le nouvel emplacement.

Exemple rclone :

1.  Installez rclone : [https://rclone.org/install/](https://rclone.org/install/)
2.  Créez des informations d'identification S3 dans l'ancien et le nouveau nuage Arbutus : [https://docs.alliancecan.ca/wiki/Arbutus_object_storage](https://docs.alliancecan.ca/wiki/Arbutus_object_storage)
3.  Créez un fichier de configuration pour rclone :
    *   Emplacement du fichier sous Linux/MacOS : `~/.config/rclone/rclone.conf`
    *   Contenu du fichier, insérant vos valeurs d'accès et secrètes pour chaque environnement :
        ```ini
        [renewal] 
        type = s3 
        access_key_id = <CLÉ_D_ACCÈS_RENOUVELLEMENT> 
        secret_access_key = <CLÉ_SECRÈTE_RENÉGOCIÉE> 
        endpoint = https://object-arbutus.alliancecan.ca 
        [legacy] 
        type = s3 
        access_key_id = <ANCIENNE_CLÉ_D_ACCÈS> 
        secret_access_key = <ANCIENNE_CLÉ_SECRÈTE> 
        endpoint = https://object-arbutus.cloud.computecanada.ca 
        ```
4.  Synchronisez tous les conteneurs avec la commande suivante :
    ```bash
    rclone sync legacy: renewal:
    ```

### Soutien technique

Pour une demande d'assistance technique, écrivez à [cloud@tech.alliancecan.ca](mailto:cloud@tech.alliancecan.ca).