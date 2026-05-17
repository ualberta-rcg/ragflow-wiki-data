---
title: "Arbutus Migration Guide/fr"
slug: "arbutus_migration_guide"
lang: "fr"

source_wiki_title: "Arbutus Migration Guide/fr"
source_hash: "9f41f411a2b842b9fa463e98a627d16e"
last_synced: "2026-05-17T14:59:09.465984+00:00"
last_processed: "2026-05-17T15:14:51.958528+00:00"

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

Vous trouverez ici l'information sur la migration d'instances virtuelles (ou VM, pour *machines virtuelles*) à partir de l'ancien nuage Arbutus (de la précédente génération) vers le nouveau nuage Arbutus amélioré. Puisque vous maîtrisez bien votre travail, nous vous recommandons de gérer vous-mêmes la migration vers le nouveau nuage selon les logiciels que vous utilisez et selon votre disponibilité.

Il est important de migrer toutes vos ressources infonuagiques (instances, volumes de stockage, conteneurs de stockage d'objets, réseaux, clés, etc.) vers le nouveau nuage Arbutus, puisque le système précédent sera mis hors service courant 2026.

!!! warning "Date limite de migration"
    La date limite pour migrer vos ressources est le **31 août 2026**. Ceci s'applique autant aux ressources allouées par concours qu'à celles qui ont été obtenues par le service d'accès rapide.

Nous décrivons ici quelques méthodes de migration. Avec votre équipe de recherche, vous devez identifier la ou les approches en fonction de votre projet.

Cette information peut susciter des questions ou encore, vous voudrez peut-être discuter avec notre équipe technique de la meilleure approche dans votre cas particulier. Vous pouvez alors écrire à [cloud@tech.alliancecan.ca](mailto:cloud@tech.alliancecan.ca).

## Planifier la migration

Les questions suivantes sont en rapport avec les ressources qui se trouvent sur l'ancien nuage Arbutus. Elles vous aideront à planifier leur migration.

*   Quelles sont les ressources qui doivent être migrées vers le nouveau nuage Arbutus? Il n'est pas obligatoire de migrer toutes les ressources; par exemple, des volumes ou des instances qui ne sont plus nécessaires peuvent être supprimés.
    !!! info
        **Créez une liste de toutes les ressources qui doivent être migrées.**
*   Vos instances sont-elles éphémères ou sont-elles basées sur des volumes? Les instances basées sur des volumes démarrent à partir d'un volume (par exemple, `/dev/vda`) et peuvent également avoir d'autres volumes (par exemple, `/dev/vdb`). Les instances éphémères ne démarrent pas à partir d'un volume.
    !!! info
        **Listez les instances basées sur des volumes séparément des instances éphémères.**
*   Vos volumes font-ils plus de 150 Go? Si c'est le cas, ils doivent être migrés à l'aide de Globus.
    !!! info
        **Identifiez les volumes de plus de 150 Go.**
*   Avez-vous utilisé un système de déploiement automatisé (par exemple, Terraform ou Ansible) avec l'ancien nuage?
    !!! tip
        **Si c'est le cas, les mêmes outils d'automatisation doivent être utilisés pour la migration.**
*   Utilisez-vous des entrées DNS personnalisées? Ces entrées devront être mises à jour, car le nouveau nuage Arbutus utilise des plages d'adresses IP flottantes différentes de celles du système précédent.
*   Pour gérer vos ressources infonuagiques, utilisez-vous le tableau de bord OpenStack (interface web Horizon) ou l'interface en ligne de commande (CLI) OpenStack?
    !!! tip
        **Les migrations simples peuvent être effectuées via l'interface web; par contre, les migrations plus complexes peuvent nécessiter un accès à l'interface en ligne de commande.**
*   Les membres de votre équipe ont-ils tous un compte actif avec l'Alliance? Veuillez noter que le partage de compte est strictement interdit.
    !!! info
        **Toute personne ayant besoin d'un compte doit en [faire la demande sur CCDB](../getting-started/apply_for_a_ccdb_account.md).**
*   Comment gérerez-vous les interruptions de service requises pour la migration? Selon l'étendue de la migration,
    !!! warning
        **l'interruption peut durer de quelques heures à quelques jours. Qui devez-vous informer?**
*   Vos ressources ont-elles été allouées via le service d'accès rapide? Si c'est le cas,
    !!! note
        **vous devrez soumettre une demande de migration à [cloud@tech.alliancecan.ca](mailto:cloud@tech.alliancecan.ca).**

Avec les réponses à ces questions, vous pourrez élaborer votre plan de migration.

## Information de base

Utilisez les adresses URL suivantes pour obtenir le tableau de bord OpenStack :

*   **Ancien nuage Arbutus** : [https://arbutus.cloud.computecanada.ca](https://arbutus.cloud.computecanada.ca)
*   **Nouveau nuage Arbutus** : [https://arbutus.alliancecan.ca](https://arbutus.alliancecan.ca/)

Vous pouvez utiliser les navigateurs Firefox et Chrome; Safari et Edge pourraient fonctionner, mais ils n'ont pas été testés.

Votre projet (*tenant*), votre réseau et votre routeur auront été créés à l'avance sur le nouveau nuage et vous aurez accès aux mêmes projets que sur l'ancien nuage. Cependant, puisque le nouveau nuage utilise des plages d'adresses IP flottantes différentes de celles du système précédent, vous devrez peut-être créer de nouveaux groupes de sécurité, particulièrement pour les règles de sécurité d'OpenStack.

## Préparer l'environnement de migration

!!! danger "Important"
    Avant de commencer, faites une copie de sauvegarde des données importantes. Les nuages sont dotés de systèmes de stockage redondants, mais nous ne sauvegardons pas les instances. **La personne propriétaire du projet doit se charger de copier les données qui seront migrées.**

1.  Connectez-vous aux deux nuages avec les informations d'identification pour votre compte avec l'Alliance et téléchargez les fichiers RC dans `Projet -> Accès API -> Télécharger le fichier RC OpenStack`. Ces fichiers servent à configurer les variables d'environnement utilisées par les outils en ligne de commande OpenStack.
2.  Copiez les fichiers RC d'OpenStack sur l'hôte que vous utiliserez pour la migration et suivez les instructions de la section `Modifier le fichier RC du nouveau Arbutus` ci-dessous.
3.  Testez le ou les fichiers RC pour vérifier que vous avez accès à vos projets dans les deux nuages.
    *   Activez un fichier RC en l'exécutant (`source opensrc.sh`) dans une session shell. Un seul fichier RC à la fois peut être actif dans une session shell.
    *   Testez votre configuration en exécutant `openstack volume list`.
4.  Migrez les clés SSH :
    *   Depuis le tableau de bord Horizon de l'ancien nuage Arbutus, naviguez vers `Calcul -> Paires de clés`. Cliquez sur le nom de la paire de clés que vous voulez et copiez la valeur de la clé publique.
    *   Depuis le tableau de bord Horizon du nouveau nuage Arbutus, naviguez vers `Calcul -> Paires de clés`. Cliquez sur `Importer une clé publique`, nommez votre paire de clés et collez-la dans le champ pour la clé publique de l'ancien nuage.
    *   Votre paire de clés devrait maintenant être importée dans le nouveau nuage. Répétez les étapes ci-dessus pour chaque paire de clés nécessaire.
    *   Vous pouvez également générer de nouvelles paires de clés ou les importer avec la commande :
        ```bash
        openstack keypair create --public-key <fichier-clé-publique> <nom>
        ```
5.  Migrez les groupes de sécurité et les règles.
    *   Dans l'ancien nuage, naviguez vers `Réseau -> Groupes de sécurité` et notez les groupes de sécurité existants ainsi que leurs règles associées.
    *   Dans le nouveau nuage, naviguez vers `Réseau -> Groupes de sécurité` et recréez les groupes de sécurité et leurs règles associées, au besoin.
    !!! warning
        Ne supprimez aucune des règles de sécurité de Egress IPv4 et IPv6 créées par défaut. La suppression de ces règles peut empêcher vos instances de récupérer les données de configuration du service de métadonnées OpenStack en plus d'entraîner plusieurs autres problèmes.
    *   Les règles et les groupes de sécurité peuvent également être créés via l'interface en ligne de commande (CLI).
    !!! tip "Exemple pour le port HTTP 80"
        Notre exemple concerne uniquement le port HTTP 80. Modifiez-le selon vos besoins.
        ```bash
        openstack security group create <nom-du-groupe>
        openstack security group rule create --proto tcp --remote-ip 0.0.0.0/0 --dst-port 80 <nom-du-groupe>
        ```
    *   Pour afficher les règles via l'interface en ligne de commande (CLI) :
        *   exécutez `openstack security group list` pour lister les groupes de sécurité disponibles;
        *   exécutez `openstack security group rule list` pour afficher les règles du groupe.
6.  Planifiez une interruption de service. En général, l'arrêt des services suivi de la fermeture de l'instance est la meilleure façon d'éviter la corruption ou l'incohérence des données après la migration. Les petits volumes peuvent être copiés assez rapidement; par exemple, un volume de 10 Go sera copié en moins de cinq minutes, mais les volumes plus importants (par exemple, 100 Go) peuvent prendre de 30 à 40 minutes. Tenez-en bien compte.
    !!! tip
        De plus, les adresses IP flottantes seront différentes; assurez-vous donc que la durée de vie (TTL) de vos enregistrements DNS possède une valeur basse afin que les modifications se propagent le plus rapidement possible.

## Modifier le fichier RC du nouveau Arbutus

Après avoir téléchargé le fichier RC du nouveau nuage, modifiez-le en ajoutant les lignes suivantes :

```text
export OS_AUTH_TYPE=v3websso
export OS_IDENTITY_PROVIDER=atmosphere
export OS_PROTOCOL=openid
export OS_PROJECT_DOMAIN_NAME=default
```

Supprimez les lignes qui contiennent :

```text
export OS_USER_DOMAIN_NAME="atmosphere"
if [ -z "$OS_USER_DOMAIN_NAME" ]; then unset OS_USER_DOMAIN_NAME; fi
```

Supprimez aussi :

```text
echo "Please enter your OpenStack Password for project $OS_PROJECT_NAME as user $OS_USERNAME: "
read -sr OS_PASSWORD_INPUT
export OS_PASSWORD=$OS_PASSWORD_INPUT
```

Le fichier devrait maintenant contenir des lignes semblables à ceci :

```text
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

Créez ensuite un environnement virtuel pour installer le client OpenStack et les autres logiciels dont vous avez besoin.

```bash
$ python3 -m venv openstack
$ source openstack/bin/activate
$ pip install python-openstackclient keystoneauth-websso python-manilaclient
```

## Scénarios

Dépendant de votre configuration actuelle, vous pouvez utiliser un ou plusieurs des scénarios.

*   [Migration manuelle ou orchestrée](#migration-manuelle-ou-orchestrée)
*   [Migration d'instances associées à des volumes](#migration-dinstances-associées-à-des-volumes)
*   [Migration d'instances éphémères](#migration-dinstances-éphémères)

## Migration manuelle ou orchestrée

Ici, les nouvelles instances et les nouveaux volumes sont créés sur le nouveau nuage Arbutus, avec les mêmes caractéristiques que sur l'ancien nuage Arbutus. Les fichiers et données qui sont nécessaires sont copiés. En règle générale, les grandes lignes de la procédure sont :

1.  Si vous utilisez des images personnalisées, copiez les images Glance de l'ancien nuage Arbutus vers le nouveau nuage ou démarrez simplement avec une nouvelle image de base sur le nouveau nuage.
2.  Installez et configurez les services sur la ou les instances.
3.  Copiez les données des anciennes instances vers les nouvelles instances (voir [Copier les données](#copier-les-données) ci-dessous).
4.  Assignez des adresses IP flottantes aux nouvelles instances et faites la mise à jour des DNS.
5.  Mettez fin aux anciennes instances et supprimez les anciens volumes.

Ces étapes peuvent être effectuées manuellement ou être orchestrées avec [Ansible](https://docs.ansible.com/ansible/2.5/modules/list_of_cloud_modules.html), [Terraform](https://www.terraform.io/docs/providers/openstack/) ou [Heat](https://wiki.openstack.org/wiki/Heat). Le présent document ne traite pas de ces outils; cependant, si vous les utilisiez sur l'ancien nuage, ils devraient fonctionner de la même manière sur le nouveau nuage.

## Migration d'instances associées à des volumes

Comme leur nom l'indique, chacune de ces instances est liée à un volume persistant qui contient le système d'exploitation et les données nécessaires.

!!! tip "Bonne pratique"
    Il est une bonne pratique de créer des volumes distincts pour le système d'exploitation et pour les données.

### Migration avec des images Glance

!!! info
    Ce scénario est recommandé dans le cas de volumes de moins de 150 Go. Pour les volumes plus grands, la [migration manuelle ou orchestrée](#migration-manuelle-ou-orchestrée) est préférable.

1.  Ouvrez deux sessions SSH pour l'instance que vous prévoyez migrer.
2.  Dans une session, chargez le fichier RC d'OpenStack de l'ancien nuage. Dans l'autre session, chargez le fichier RC d'OpenStack du nouveau nuage.
    !!! tip
        L'utilisation de la commande `screen` est recommandée en cas de déconnexion SSH. Pour installer le paquet screen, exécutez `dnf install screen`.
3.  Dans l'instance de l'ancien nuage, installez l'interface en ligne de commande (CLI) OpenStack dans un shell *root*.
    ```bash
    dnf install epel-release
    dnf install python-devel python-pip gcc
    pip install python-openstackclient
    ```
4.  Dans l'interface web de l'ancien nuage, fermez l'instance et détachez le volume.
    Si le volume sert au démarrage d'une instance, supprimez l'instance, mais conservez le volume.
    Créez une image du volume (`Volumes -> Volumes` et `Téléverser vers l'image` du menu déroulant).
    !!! tip
        Assurez-vous de sélectionner RAW comme format de disque.
5.  Sur la ligne de commande, vous pouvez aussi entrer :
    ```bash
    openstack image create --volume <nom/ID du volume> <newimagename> --private
    ```
    Cette commande s'exécute en arrière-plan et peut prendre un certain temps. Une fois l'image créée, elle apparaît sous `Calcul -> Images` avec le nom que vous avez spécifié à l'étape précédente. Vous pouvez obtenir l'identifiant de l'image en cliquant sur son nom. L'état de la ligne de commande passera progressivement de *saving* à *active*; cela peut prendre une heure ou plus, selon la taille de votre volume.
    ```bash
    openstack image show <newimagename>
    ```
6.  Dans la session pour l'ancien nuage, téléchargez l'image (remplacez `<filename>` et `<image-id>` par leurs valeurs réelles).
    ```bash
    openstack image save --file <filename> <image-id>
    ```
7.  Dans la session pour le nouveau nuage, sur l'hôte de migration, chargez l'image (remplacez `<filename>` par le nom dans l'étape précédente; `<image-name>` peut être n'importe quel nom).
    ```bash
    openstack --os-cloud <cloud> image create --private --file <file> <newImageName>
    ```
8.  Vous pouvez maintenant créer un volume à partir de l'image chargée. Dans l'interface web pour le nouveau nuage, naviguez vers `Calcul -> Images`. L'image chargée à l'étape précédente devrait s'y trouver. Dans le menu déroulant pour l'image, sélectionnez `Créer un volume`. Ce volume peut ensuite être attaché à des instances ou utilisé pour démarrer une nouvelle instance.
9.  Une fois vos instances et volumes migrés et validés, et une fois que tous les enregistrements DNS associés sont à jour, veuillez supprimer vos instances et volumes de l'ancien nuage.

### Autre option avec l'outil Linux 'dd'

1.  Lancez une instance dans l'ancien nuage avec la plus petite configuration possible (p1-1.5gb). Appelons-la *hôte de migration temporaire*. Les instructions ci-dessous supposent que vous utilisez AlmaLinux 9, mais toute distribution Linux disposant de Python et de Pip devrait convenir.
2.  Connectez-vous à l'instance via SSH et installez l'interface en ligne de commande (CLI) OpenStack dans un shell *root*.
    ```bash
    dnf install epel-release
    dnf install python-devel python-pip gcc
    pip install python-openstackclient
    ```
3.  Pour vérifier l'installation, essayez d'exécuter OpenStack en ligne de commande. Pour plus d'information, notamment sur l'installation de la CLI OpenStack sur des systèmes autres qu'AlmaLinux, consultez [https://docs.openstack.org/newton/user-guide/common/cli-install-openstack-command-line-clients.html](https://docs.openstack.org/newton/user-guide/common/cli-install-openstack-command-line-clients.html).
4.  Copiez votre fichier RC OpenStack du nouveau nuage vers l'hôte de migration temporaire et activez-le. Vérifiez que vous pouvez vous connecter à l'API OpenStack sur le nouveau nuage avec la commande `openstack image list`.
5.  Supprimez l'instance à déplacer, mais **NE SUPPRIMEZ PAS** le volume auquel elle est attachée. Ce volume peut désormais être attaché à l'hôte de migration temporaire que nous avons créé.
6.  Dans l'interface web de l'ancien nuage, naviguez vers `Volumes -> Volumes`. Dans le menu déroulant, sélectionnez `Gérer les attachements` et attachez le volume à l'hôte de migration temporaire.
    !!! tip
        Notez le périphérique auquel le volume est attaché (généralement `/dev/vdb` ou `/dev/vdc`).
7.  À l'aide de l'utilitaire `dd`, créez une image à partir du disque identifié à l'étape précédente. Dans l'exemple suivant, nous l'avons nommée *volumemigrate*. Une fois la commande exécutée, vous recevrez un résultat affichant les détails de l'image créée.
    ```bash
    dd if=/dev/vdb | openstack image create --private --container-format bare --disk-format raw "volumemigrate"
    ```
8.  Dans l'interface web du nouveau nuage, naviguez vers `Calcul -> Images`. L'image peut désormais être utilisée pour lancer des instances. Si vous souhaitez que les données soient persistantes, assurez-vous de créer un nouveau volume lors du lancement de l'instance.
9.  Une fois vos instances et volumes migrés et validés, et les enregistrements DNS associés mis à jour, veuillez supprimer vos instances et volumes de l'ancien nuage.

### Migration de grands volumes avec l'outil Linux 'dd'

Dans le cas de volumes, l'utilisation des images n'est pas recommandée. Copiez plutôt vos données dans de nouveaux volumes avec rsync ou un autre outil de copie, lorsque possible. Si ce n'est pas possible, par exemple dans le cas d'un volume amorçable (*bootable*), vous pouvez utiliser la commande `dd` pour produire une copie identique sur le nouveau nuage.

!!! danger "Important"
    Sauvegardez les données importantes avant d'exécuter cette procédure.

1.  Créez une instance temporaire sur l'ancien nuage (1 à 1,5 Go devraient suffire) et faites de même sur le nouveau nuage.
2.  Attribuez des adresses IP flottantes aux deux instances temporaires mentionnées ci-dessus auxquelles vous pouvez vous connecter via SSH.
3.  Installez les paquets suivants sur l'instance temporaire de l'ancien nuage.
    ```bash
    dnf install epel-release
    dnf install pv
    dnf install screen
    ```
4.  Sur la nouvelle instance temporaire, exécutez :
    ```bash
    chmod u+s /bin/dd
    ```
5.  Copiez la clé privée SSH que vous utilisez pour vous connecter en tant qu'utilisateur sur la nouvelle instance temporaire, vers l'instance temporaire de l'ancien nuage.
6.  Assurez-vous que les règles de sécurité SSH autorisent l'instance temporaire de l'ancien nuage à se connecter via SSH à la nouvelle instance temporaire.
7.  Pour chaque volume que vous souhaitez déplacer de l'ancien nuage vers le nouveau nuage :
    *   créez un volume vide de même taille sur le nouveau nuage et marquez-le comme amorçable s'il s'agit d'un volume d'amorçage;
    *   attachez le volume ci-dessus à l'instance temporaire sur le nouveau nuage;
    *   attachez le volume que vous souhaitez copier de l'ancien nuage à l'instance temporaire. Remarque : vous devrez peut-être supprimer l'instance à laquelle il est actuellement attaché. **NE SUPPRIMEZ PAS** le volume.
8.  Sur l'instance temporaire, exécutez les commandes ci-dessous. Ceci suppose que le volume source sur l'ancien nuage est attaché à l'instance temporaire sous le nom `/dev/vdb`, que sa taille est de 96 Go, que la clé SSH utilisée pour se connecter à l'instance temporaire est `key.pem` et que le volume de destination sur Arbutus est attaché à l'instance temporaire sous le nom `/dev/vdb`. Remplacez également *xxx.xx.xx.xx* par l'adresse IP réelle de l'instance Arbutus à laquelle vous vous connecterez.
    ```bash
    screen
    sudo dd bs=16M if=/dev/vdb | pv -s 96G | ssh -i key.pem user@xxx.xx.xx.xx "sudo dd bs=16M of=/dev/vdb"
    ```
    !!! tip
        La commande `screen` est utilisée en cas de déconnexion de votre session SSH.

Dans le nouveau nuage, vous disposez maintenant d'une copie identique du volume de l'ancien nuage et vous pouvez l'utiliser pour y lancer des instances.

## Migration d'instances éphémères

Une instance éphémère n'est associée à aucun volume.

### Avec images et instantanés de volume Glance

Voir la section [Migration avec des images Glance](#migration-avec-des-images-glance) ci-dessus.

### Autre option avec l'outil Linux 'dd'

Voir la section [Autre option avec l'outil Linux 'dd'](#autre-option-avec-loutil-linux-dd) ci-dessus.

## Copier les données

Vous pouvez utiliser la méthode de copie que vous connaissez, mais nous recommandons les deux suivantes, selon la taille des volumes de votre projet.

## Grands volumes de données : Globus

Pour les très grands volumes (plus de 5 To), nous recommandons Globus.

La méthode la plus simple est d'utiliser le client Globus Connect Personal avec un abonnement Globus Plus.

**1. Abonnez-vous à Globus Connect Personal Plus.**
*   Écrivez à [globus@tech.alliancecan.ca](mailto:globus@tech.alliancecan.ca).
*   Répondez à l'invitation Globus Personal Plus et suivez les directives.

**2. Pour chaque instance concernée par le transfert de données, activez Globus Connect Personal.**
*   Prenez connaissance de [Globus, Ordinateurs personnels](../getting-started/globus.md#ordinateurs-personnels) et de [https://www.globus.org/globus-connect-personal](https://www.globus.org/globus-connect-personal).
*   Utilisez les directives appropriées pour installer Globus Connect Personal sur chaque instance. Pour Linux, consultez [https://docs.globus.org/how-to/globus-connect-personal-linux/](https://docs.globus.org/how-to/globus-connect-personal-linux/).
*   Modifiez la configuration de chacune des instances pour communiquer avec le service Globus.
    *   Vérifiez que chaque instance possède une adresse IP externe.
    *   Vérifiez que le coupe-feu des instances permet la [communication par les ports](https://docs.globus.org/how-to/configure-firewall-gcp/); (voir aussi [Groupes de sécurité](managing_your_cloud_resources_with_openstack.md#groupes-de-sécurité)).
    *   Pour exécuter Globus Connect Personal, vous devez avoir accès aux données dans les systèmes de fichiers de stockage.
*   Dans l'espace utilisateur, exécutez Globus Connect Personal en arrière-plan.
*   Comme abonné Globus Connect Personal Plus (étape 1), créez un point de chute partagé pour une ou les deux instances.

**3. Via l'interface Globus (globus.org, globus.calculcanada.ca), accédez aux points de chute et transférez les données.**
*   Voyez [https://docs.globus.org/how-to/get-started/](https://docs.globus.org/how-to/get-started/).
*   Des instructions supplémentaires se trouvent ici : [Transfert entre deux points de chute personnels](../getting-started/globus.md#transfert-entre-deux-points-de-chute-personnels).

Pour plus d'information sur la configuration, consultez [https://computecanada.github.io/DHSI-cloud-course/globus/](https://computecanada.github.io/DHSI-cloud-course/globus/).

En cas de difficulté, écrivez à [globus@tech.alliancecan.ca](mailto:globus@tech.alliancecan.ca).
!!! tip
    Il est fortement suggéré de soumettre aussi une demande d'assistance au service technique.

## Petits volumes de données : rsync + ssh

Vous pouvez utiliser une autre méthode pour transférer vos données, mais pour les plus petits volumes, rsync+ssh offre de bonnes vitesses de transfert et, à l'instar de Globus, travaille de manière incrémentale. Lors du transfert de données avec rsync, vous pouvez utiliser le réseau IPv6 GUA dans OpenStack. Il s'agit d'un réseau VLAN qui contourne le composant Neutron d'OpenStack, offrant potentiellement de meilleures performances.

Voici un exemple typique :

1.  Connectez-vous via SSH à l'instance de l'ancien nuage Arbutus, qui possède le volume principal. Prenez note du chemin absolu que vous voulez copier dans l'instance du nouveau nuage.
2.  Lancez rsync avec SSH. Dans l'exemple suivant, on suppose qu'il existe une connexion sans mot de passe via des [clés SSH](../getting-started/ssh_keys.md). Utilisez le code suivant avec les valeurs réelles.
    ```bash
    rsync -avzP -e 'ssh -i ~/.ssh/key.pem' /local/path/ remoteuser@remotehost:/path/to/files/
    ```
3.  Vérifiez que les données ont bien été copiées dans l'instance du nouveau nuage, puis supprimez les données de l'ancien nuage.

## Configuration post-migration

Après le transfert des données vers la nouvelle instance, certaines configurations seront peut-être requises, comme :

*   mise à jour des règles de pare-feu pour utiliser les nouvelles adresses IP et les nouveaux réseaux si un pare-feu hôte (par exemple, iptables, firewalld, etc.) est utilisé;
*   mise à jour des entrées DNS pour les domaines personnalisés (par exemple, www.myarbutusproject.ca) auprès de votre fournisseur DNS;
*   mise à jour des adresses IP dans les fichiers de configuration (par exemple, `/etc/hosts`, `/etc/resolv.conf`, `/etc/haproxy/haproxy.cfg`, `/var/www/`, `/var/lib/pgsql/data/pg_hba.conf`);
*   modification des noms d'utilisateur (par exemple, `root@192.168.65`) dans MySQL;
*   renouvellement des certificats TLS (*Transport Layer Security*) de Let's Encrypt à l'aide de certbot ou d'autres utilitaires si, par exemple, le nom alternatif du sujet (SAM) du certificat contient des adresses IP.

!!! tip
    Assurez-vous de tester la configuration avant d'informer les membres de votre équipe que la migration est terminée.

## Migration du système de fichiers partagé CephFS

Le système de fichiers partagé CephFS sur le nouveau nuage Arbutus est un service distinct; toutes les données souhaitées doivent y être intentionnellement migrées.

La gestion des points de partage (*shares*) existants, y compris les opérations de création, de suppression et de gestion des clés, est contrôlée dans l'ancien nuage Arbutus. Cependant, une fois qu'une clé et un point de partage existants sont créés, ces ressources sont accessibles depuis une machine virtuelle du nouveau nuage. De même, la création et la gestion des points de partage dans le nouveau nuage sont effectuées exclusivement dans ce dernier.

Les points de partage existants et les nouveaux points de partage peuvent être montés sur des machines virtuelles du nouveau nuage. La procédure suivante est recommandée pour garantir l'intégrité des données lors de la migration entre les points de partage :

1.  Pour chaque point de partage de l'ancien nuage, créez un point de partage équivalent dans le nouveau nuage.
2.  Montez les deux points de partage sur des emplacements de montage distincts sur la même machine virtuelle du nouveau nuage.
3.  Utilisez un outil de copie de données tel que rsync pour transférer les données de l'ancien vers le nouveau point de partage.

La procédure de montage des points de partage de l'ancien nuage est décrite dans [notre page wiki sur CephFS](cephfs.md).

La création d'un point de partage équivalent dans le nouveau nuage suit une procédure similaire, à quelques différences près :

1.  Vous devez créer le nouveau point de partage et les clés d'accès via la nouvelle interface web (Horizon).
2.  Vous devez créer un fichier `ceph.conf` distinct, avec un nom spécifique tel que `ceph-new.conf`.
3.  La valeur de configuration `mon_host` devra être mise à jour uniquement pour le nouveau point de partage, dans le fichier `ceph-new.conf`.
    *   Valeur précédente :
        ```text
        10.30.201.3:6789,10.30.202.3:6789,10.30.203.3:6789
        ```
    *   Nouvelle valeur :
        ```text
        [v2:134.87.15.61:3300/0,v1:134.87.15.61:6789/0] [v2:134.87.15.62:3300/0,v1:134.87.15.62:6789/0] [v2:134.87.15.63:3300/0,v1:134.87.15.63:6789/0]
        ```
4.  Lors du montage du nouveau point de partage, une valeur additionnelle est requise après l'option `-o` dans la commande `mount` afin de spécifier le nouveau fichier de configuration `conf=/etc/ceph/ceph-new.conf`.

Une fois les deux points de partage sont montés, utilisez rsync pour transférer les données. Les options `a`, `v` et `p` de rsync sont recommandées.

```bash
rsync -avp /mnt/old-share/ /mnt/new-share/
```

Notez que, selon la taille du point de partage, cette opération peut prendre un certain temps.
!!! tip
    Pour maintenir la session active en cas de déconnexion, utilisez un outil comme screen ou tmux.

## Migration du stockage objet

Le stockage d'objets sur le nouveau nuage est un service distinct; toutes les données souhaitées doivent y être intentionnellement migrées.

La gestion des conteneurs (*buckets*) et des objets de l'ancien nuage, y compris les opérations de création, de suppression, de manipulation d'objets et de gestion des clés, est contrôlée dans l'ancien nuage. De même, la création et la gestion des *buckets* et des objets dans le nouveau nuage sont effectuées exclusivement dans cet environnement.

La migration des données vers le stockage d'objets du nouveau nuage peut se faire par différentes méthodes et outils.
!!! tip
    Si vous connaissez les options, n'hésitez pas à utiliser la méthode la plus adaptée à vos données.

**Points d'accès pour le stockage d'objets :**
*   **Nouveau nuage Arbutus** : [https://object-arbutus.alliancecan.ca](https://object-arbutus.alliancecan.ca)
*   **Ancien nuage Arbutus** : [https://object-arbutus.cloud.computecanada.ca](https://object-arbutus.cloud.computecanada.ca)

!!! warning
    Si vous utilisez des listes de contrôle d'accès (ACL) pour les conteneurs, vérifiez que l'outil utilisé les copie correctement. Autrement, vous devrez les recréer dans le nouvel environnement. La plupart des outils ne conservent pas les ACL des conteneurs. Notez que si vous référencez des UUID d'utilisateur ou de projet, ceux-ci seront différents dans le nouveau nuage.

De plus, le stockage d'objets dans le nouveau nuage utilise des *tenants*; par conséquent, les conflits de noms de conteneur ne se produiront qu'au sein d'un même projet et non pour tous les projets. Lors de l'authentification avec l'API Swift ou S3, le *tenant* est déduit de l'utilisateur et de la clé qui sont fournis. Toutefois, pour un accès public aux conteneurs sans authentification, le *tenant* doit être spécifié. L'ID du *tenant* est identique à l'ID du projet OpenStack. L'URL pour un accès Swift non authentifié se trouve via l'interface Horizon, tandis que l'URL pour un accès S3 non authentifié est au format suivant :

```text
https://object-arbutus.alliancecan.ca/<ID-tenant>:<nom-conteneur>/<nom-objet>
```

!!! info "Utilisation de rclone"
    Nous recommandons rclone; les ACL du *bucket* ne seront pas copiées et tous les accès copiés seront par défaut privés, comme dans cet exemple.

1.  Installez rclone avec [https://rclone.org/install/](https://rclone.org/install/).
2.  Créez des identifiants S3 dans les deux nuages. Voir [notre page wiki sur le stockage d'objets Arbutus](arbutus_object_storage.md).
3.  Créez un fichier de configuration pour rclone.
    *   Emplacement du fichier sous Linux/macOS : `~/.config/rclone/rclone.conf`
    *   Contenu du fichier, en insérant vos valeurs pour l'accès et la confidentialité de chaque environnement :
        ```ini
        [new]
        type = s3
        access_key_id = <CLÉ D'ACCÈS DU NOUVEAU NUAGE>
        secret_access_key = <CLÉ SECRÈTE DU NOUVEAU NUAGE>
        endpoint = https://object-arbutus.alliancecan.ca
        [legacy]
        type = s3
        access_key_id = <CLÉ D'ACCÈS DE L'ANCIEN NUAGE>
        secret_access_key = <CLÉ SECRÈTE DE L'ANCIEN NUAGE>
        endpoint= https://object-arbutus.cloud.computecanada.ca
        ```
4.  Synchronisez les conteneurs avec :
    ```bash
    rclone sync legacy: renewal:
    ```

## Soutien technique

Pour une demande d'assistance technique, écrivez à [cloud@tech.alliancecan.ca](mailto:cloud@tech.alliancecan.ca).