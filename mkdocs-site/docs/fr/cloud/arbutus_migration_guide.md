---
title: "Arbutus Migration Guide/fr"
slug: "arbutus_migration_guide"
lang: "fr"

source_wiki_title: "Arbutus Migration Guide/fr"
source_hash: "09229cc9bb2bf15801a4e099f3b6c814"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T04:36:04.182124+00:00"

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

Vous trouverez ici l'information sur la migration d'instances virtuelles (VM) à partir du nuage Arbutus de la génération précédente vers le nuage Arbutus amélioré de la nouvelle génération. Puisque vous connaissez bien votre travail, nous vous recommandons de gérer vous-mêmes la migration vers le nouveau nuage selon les logiciels que vous utilisez et votre disponibilité.

Il est important de migrer toutes vos ressources infonuagiques (instances, volumes de stockage, conteneurs de stockage objet, réseaux, clés, etc.) vers le nouveau nuage Arbutus puisque le système précédent deviendra hors service au cours de 2026. **La date limite pour migrer vos ressources est le 31 août 2026**. Ceci s'applique autant aux ressources allouées par concours qu'à celles qui ont été obtenues par le service d'accès rapide.

Nous décrivons ici quelques méthodes de migration. Avec votre équipe de recherche, vous devez identifier la ou les approches en fonction de votre projet.

Cette information peut susciter des questions ou encore, vous voudrez peut-être discuter avec notre équipe technique de la meilleure approche dans votre cas particulier. Vous pouvez alors écrire à cloud@tech.alliancecan.ca.

## Planifier la migration

Les questions suivantes vous aideront à planifier la migration.

*   Quelles sont les ressources qui doivent être migrées vers le nouveau nuage Arbutus? Il n'est pas obligatoire de migrer toutes les ressources; par exemple, des volumes ou des instances qui ne sont plus nécessaires peuvent être supprimés. **Créez une liste de toutes les ressources qui doivent être migrées.**
*   Vos instances sont-elles éphémères ou sont-elles basées sur des volumes? Les instances basées sur des volumes démarrent à partir d'un volume (par exemple, `/dev/vda`) et peuvent également avoir d'autres volumes (par exemple, `/dev/vdb`). Les instances éphémères ne démarrent pas à partir d'un volume. **Listez les instances basées sur des volumes séparément des instances éphémères.**
*   Vos volumes font-ils plus de 150 Go? Si c'est le cas, ils doivent être migrés à l'aide de Globus. **Identifiez les volumes de plus de 150 Go.**
*   Avez-vous utilisé un système de déploiement automatisé (par exemple, Terraform, Ansible) sur le nuage Arbutus de la génération précédente? **Si c'est le cas, les mêmes outils d'automatisation doivent être utilisés pour la migration.**
*   Utilisez-vous des entrées DNS personnalisées? Ces entrées devront être mises à jour, car le nouveau nuage Arbutus utilise des plages d'adresses IP flottantes différentes de celles du système précédent.
*   Pour gérer vos ressources infonuagiques, utilisez-vous le tableau de bord OpenStack (interface web Horizon) ou l’interface en ligne de commande (CLI) OpenStack? **Les migrations simples peuvent être effectuées via l’interface web; par contre, les migrations plus complexes peuvent nécessiter un accès à l'interface en ligne de commande.**
*   Les membres de votre équipe ont-ils tout un compte OpenStack? Veuillez noter que le partage de compte est strictement interdit. **Toute personne ayant besoin d’un compte doit en [faire la demande ici sur CCDB](apply-for-a-ccdb-account.md).**
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

Votre projet, votre réseau et votre routeur auront été créés sur Arbutus et vous aurez accès aux mêmes projets que sur le nuage de la génération précédente (anciennement appelé nuage Ouest).

Avant de migrer vos instances, nous vous recommandons d'effectuer les étapes suivantes pour bien configurer l'environnement.

1.  !!! warning "IMPORTANT"
    Faites une copie de sauvegarde des données importantes. Le nuage est doté de systèmes de stockage redondants, mais les instances ne sont pas sauvegardées.
2.  Connectez-vous au nuage avec les informations d'identification pour votre compte et téléchargez les fichiers RC pour configurer les variables d'environnement utilisées par les outils en ligne de commande OpenStack.
    *   Ancienne génération : `Calcul -> Accès et sécurité` -> onglet `Accès à l'API`, cliquez sur le bouton `Télécharger le fichier RC OpenStack`.
    *   Arbutus : `Projet -> Accès à l'API`, cliquez sur le bouton `Télécharger le fichier RC OpenStack`, sélectionnez `Fichier OpenStack RC (Identity API v3)`.
3.  Copiez les fichiers RC sur le serveur de migration `cloudmigration.calculcanada.ca`. Pour vous connecter, utilisez le nom d’utilisateur et le mot de passe de votre compte.
4.  Ouvrez deux sessions sur le serveur de migration, une pour le nuage de la génération précédente et l’autre pour le nuage Arbutus. Nous vous recommandons d’utiliser la commande `screen` pour éviter de perdre ces sessions en cas de problème avec la connexion SSH; au besoin, consultez [ces tutoriels](https://www.google.com/search?q=screen+ssh) pour la commande `screen`. Dans la session pour la génération précédente, faites un *source* du fichier RC du nuage avec `source oldcloudrc.sh`. Dans la session pour Arbutus, faites un *source* du fichier RC du nuage Arbutus avec `source newcloudrc.sh`. Testez la configuration avec une commande OpenStack simple, par exemple `openstack volume list`.
5.  Migrez les paires de clés SSH :
    *   Avec le tableau de bord Horizon sur le nuage de la génération précédente, sélectionnez `Accès et sécurité -> Paires de clés`. Cliquez sur le nom de la paire de clés que vous voulez et copiez la valeur de la clé publique.
    *   Avec le tableau de bord Horizon sur le nuage Arbutus, sélectionnez `Calcul -> Paires de clés`.
    *   Cliquez sur `Importer une paire de clés`, donnez un nom à votre paire de clés et collez la clé publique dans le champ approprié du formulaire.
    *   Votre paire de clé devrait maintenant être importée dans Arbutus. Répétez ces étapes pour toutes les clés dont vous avez besoin.
    *   Vous pouvez aussi générer de nouvelles paires de clés.
    *   Les paires de clés peuvent aussi être importées via le CLI comme suit :
        ```bash
        openstack keypair create --public-key <fichier-clé-publique> <nom>
        ```
6.  Migrez les groupes de sécurité et les règles :
    *   Sur le nuage de la génération précédente, sélectionnez `Calcul -> Accès et sécurité -> Groupes de sécurité` et prenez note des groupes existants et des règles qui leur sont associées.
    *   Sur le nuage Arbutus, sélectionnez `Réseau -> Groupes de sécurité` et reproduisez les groupes et règles qui s’appliquent.
    *   Ne supprimez pas les règles de sécurité de sortie (Egress) créées par défaut pour IPv4 et IPv6; ceci pourrait créer plusieurs problèmes, entre autres empêcher vos instances d’obtenir les données de configuration du service de métadonnées OpenStack.
    *   Les groupes et les règles peuvent aussi être créés via le CLI. Dans cet exemple, nous utilisons le port HTTP 80; modifiez les commandes selon vos besoins.
        ```bash
        openstack security group create <nom-du-groupe>
        openstack security group rule create --proto tcp --remote-ip 0.0.0.0/0 --dst-port 80 <nom-du-groupe>
        ```
    *   Pour voir les règles via le CLI, listez les groupes de sécurité avec `openstack security group list` et les règles du groupe avec `openstack security group rule list`.
7.  Prévoyez une période d'indisponibilité. De façon générale, le meilleur moyen d’éviter que les données soient corrompues ou non conformes après une migration est de fermer les services et ensuite fermer l’instance. Les petits volumes se copient relativement rapidement; par exemple, un volume de 10 Go prendra moins de 5 minutes, mais un volume de 100 Go peut prendre de 30 à 40 minutes. De plus, les adresses IP flottantes seront modifiées; assurez-vous donc que le TTL de vos enregistrements DNS est bas afin que les modifications soient propagées le plus rapidement possible.

Trois scénarios de migration sont possibles :
*   [Migration manuelle ou orchestrée](#migration-manuelle-ou-orchestrée)
*   [Migration d’instances associées à des volumes](#migration-dinstances-associées-à-des-volumes)
*   [Migration d’instances éphémères](#migration-dinstances-éphémères)

Dépendant de votre configuration actuelle, vous pouvez utiliser certains ou tous ces scénarios pour migrer du nuage de la génération précédente au nouveau nuage Arbutus.

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

Le fichier RC final devrait donc contenir des lignes qui ressemblent à ceci :

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

Et créez un environnement virtuel pour installer le client OpenStack et d'autres paquets nécessaires :

```bash
python3 -m venv openstack 
source openstack/bin/activate 
pip install python-openstackclient keystoneauth-websso python-manilaclient
```

## Scénarios de migration

Trois scénarios de migration généraux sont à considérer.
*   [Migration manuelle ou orchestrée](#migration-manuelle-ou-orchestrée)
*   [Migration d'instances associées à des volumes](#migration-dinstances-associées-à-des-volumes)
*   [Migration d'instances éphémères](#migration-dinstances-éphémères)
Selon votre configuration actuelle, vous pouvez utiliser certains ou tous ces scénarios pour migrer de l'ancien Arbutus au nouveau Arbutus.

## Migration manuelle ou orchestrée

Les instances et volumes sont créés sur Arbutus avec les mêmes caractéristiques que sur le nuage de la génération précédente. Règle générale, les grandes lignes de la procédure sont :

1.  Si vous utilisez des images personnalisées, copiez les images Glance du nuage de la génération précédente à Arbutus. Vous pouvez aussi simplement commencer avec une nouvelle image de base sur Arbutus.
2.  Installez et configurez les services sur la ou les instances.
3.  Copiez les données des anciennes instances vers les nouvelles instances (voir [Méthodes de copie de données](#méthodes-de-copie-de-données) ci-dessous).
4.  Assignez des adresses IP flottantes aux nouvelles instances et faites la mise à jour des DNS.
5.  Mettez fin aux anciennes instances et supprimez les anciens volumes.

Ces étapes peuvent être effectuées manuellement ou être orchestrées avec
[Ansible](https://docs.ansible.com/ansible/2.5/modules/list_of_cloud_modules.html),
[Terraform](https://www.terraform.io/docs/providers/openstack/ Terraform) ou
[Heat](https://wiki.openstack.org/wiki/Heat).
Le présent document ne traite pas de ces outils; cependant, si vous les utilisez sur le nuage de la génération précédente, ils devraient fonctionner de la même manière sur Arbutus.

## Migration d'instances associées à des volumes

Comme leur nom l’indique, chacune de ces instances est associée à un volume persistant qui contient le système d’exploitation et les données nécessaires. Une bonne pratique est de créer des volumes distincts pour le système d’exploitation et pour les données.

### Migration avec des images Glance

Ce scénario est recommandé dans le cas de volumes de moins de 150 Go. Pour les volumes plus grands, la [migration manuelle ou orchestrée](#migration-manuelle-ou-orchestrée) est préférable.

1.  Ouvrez deux sessions sur le serveur de migration `cloudmigration.calculcanada.ca` avec le nom d’utilisateur et le mot de passe de votre compte.
2.  Dans la session pour la génération précédente, faites un *source* du fichier RC du nuage avec `source oldcloudrc.sh`. Dans la session pour Arbutus, faites un *source* du fichier RC du nuage Arbutus avec `source newcloudrc.sh`. Nous vous recommandons d’utiliser la commande `screen` pour éviter de perdre ces sessions en cas de problème avec la connexion SSH; au besoin, consultez [ces tutoriels](https://www.google.com/search?q=screen+ssh) pour la commande `screen`.
3.  Dans l’interface utilisateur du nuage de la génération précédente, créez une image du volume voulu par `Calcul -> Volumes` et `Télécharger dans l'image` du menu déroulant. Le volume ne devrait pas être actif à ce moment, mais s’il l’est, vous pouvez utiliser l’option `force`. Assurez-vous de sélectionner le format de disque QCOW2. Ceci peut aussi se faire en ligne de commande :
    ```bash
    cinder --os-volume-api-version 2 upload-to-image <nom-du-volume> <nom-de-l-image> --force
    ```
4.  Une fois créée, l’image sera listée sous `Calcul -> Images` avec le nom que vous avez utilisé à l’étape précédente. Pour obtenir l’identifiant de l’image, cliquez sur son nom.
5.  Sur le serveur de migration, dans la session pour le nuage de la génération précédente, téléchargez l’image (remplacez `<filename>` et `<image-id>` avec les valeurs appropriées) :
    ```bash
    glance image-download --progress --file <nom-de-fichier> <identifiant-image>
    ```
6.  Sur le serveur de migration, dans la session pour le nuage Arbutus, téléchargez l’image (remplacez `<nom-de-fichier>` par le nom donné à l’étape précédente; la valeur de `<nom-image>` importe peu).
    ```bash
    glance image-create --progress --visibility private --container-format bare --disk-format qcow2 --name <nom-image> --file <nom-de-fichier>
    ```
7.  Vous pouvez maintenant créer un volume à partir de l’image téléversée. Dans l’interface utilisateur du nuage Arbutus, allez à `Calcul -> Images`. L’image téléversée à l’étape précédente devrait paraître. Dans le menu déroulant pour l’image, sélectionnez l’option `Créer le volume` pour créer le volume à partir de l’image. Le volume ainsi créé peut maintenant être associé à des instances ou utilisé pour démarrer une nouvelle instance.
8.  Une fois que vos instances et volumes ont été migrés et testés et que tous vos enregistrements DNS ont été mis à jour, veuillez supprimer les anciens volumes et instances sur le nuage de la génération précédente.

### Autre option avec Linux 'dd'

1.  Lancez une instance sur le nuage de la génération précédente avec le plus petit gabarit possible (par exemple p1-1.5gb). Nous pouvons considérer ceci comme étant un serveur de migration temporaire. Dans les étapes qui suivent, nous avons sélectionné CentOS 7, mais les distributions Linux avec Python et Pip devraient fonctionner de même.
2.  Connectez-vous à l’instance avec SSH et installez le CLI OpenStack en tant qu'utilisateur `root`.
    ```bash
    yum install epel-release
    yum install python-devel python-pip gcc
    pip install python-openstackclient
    ```
3.  Le CLI OpenStack devrait maintenant être installé. Pour vérifier, lancez la commande `openstack` en ligne de commande. Pour plus d’information sur l’installation du CLI, consultez [https://docs.openstack.org/newton/user-guide/common/cli-install-openstack-command-line-clients.html](https://docs.openstack.org/newton/user-guide/common/cli-install-openstack-command-line-clients.html)
4.  Copiez le fichier RC d’Arbutus vers le serveur de migration temporaire et faites un *source*. Pour vérifier si vous pouvez vous connecter à l’API OpenStack sur Arbutus, lancez la commande :
    ```bash
    openstack image list
    ```
5.  Supprimez l’instance à déplacer, mais **NE SUPPRIMEZ PAS** le volume qui y est associé.
6.  Le volume peut maintenant être associé au serveur de migration temporaire que nous avons créé : sur l’interface utilisateur du nuage de la génération précédente, allez à `Calcul -> Volumes`, sélectionnez `Gérer les pièces jointes` du menu déroulant et attachez le volume au serveur de migration temporaire.
7.  Prenez note de l’accélérateur auquel le volume est attaché (généralement `/dev/vdb` ou `/dev/vdc`).
8.  Avec l’utilitaire `dd`, créez une image à partir du disque attaché à l’instance. Dans l’exemple suivant, le nom de l’image est `volumemigrate`. Lorsque l’opération est terminée, les détails de l’image seront affichés.
    ```bash
    dd if=/dev/vdb | openstack image create --private --container-format bare --disk-format raw "volumemigrate"
    ```
9.  Vous devriez maintenant voir l’image en allant à `Calcul -> Images` dans l’interface Arbutus. Cette image peut être utilisée pour lancer des instances sur Arbutus. Pour que les données soient persistantes, assurez-vous de créer un nouveau volume au lancement de l’instance.
10. Une fois que vos instances et volumes ont été migrés et testés et que tous vos enregistrements DNS ont été mis à jour, veuillez supprimer les anciens volumes et instances sur le nuage de la génération précédente.

### Migration de gros volumes avec Linux 'dd'

Dans le cas de gros volumes, l'utilisation des images n'est pas recommandée. Copiez plutôt vos données dans de nouveaux volumes avec `rsync` ou un autre outil de copie, lorsque possible. Dans le cas contraire, par exemple pour un volume amorçable, vous pouvez utiliser la commande `dd` pour produire une copie identique.

Sauvegardez les données importantes avant d'exécuter cette procédure.

1.  Créez une instance temporaire sur la génération précédente (p1-1.5gb devrait convenir). Faites de même sur Arbutus. Utilisez le système d'exploitation CentOS 7.
2.  Assignez aux deux instances des adresses IP flottantes par lesquelles vous pourrez vous connecter via SSH.
3.  Dans l'instance temporaire sur la génération précédente, installez les paquets :
    ```bash
    yum install epel-release
    yum install pv
    yum install screen
    ```
4.  Dans l'instance temporaire sur Arbutus :
    ```bash
    chmod u+s /bin/dd
    ```
5.  Copiez dans l'instance temporaire de la génération précédente la clé privée SSH qui sert à vous connecter en tant qu'utilisateur `centos` à l'instance temporaire Arbutus.
6.  Vérifiez que les règles de sécurité SSH permettent à l'instance temporaire de la génération précédente de se connecter à l'instance temporaire Arbutus.
7.  Pour chacun des volumes à déplacer de la génération précédente à Arbutus :
    *   Créez un volume vide de la même taille dans Arbutus; s'il s'agit d'un volume amorçable, identifiez-le comme tel (`amorçable`).
    *   Attachez ce volume à l'instance temporaire Arbutus.
    *   Attachez le volume à copier de la génération précédente à l'instance temporaire de la génération précédente. Vous devrez peut-être supprimer l'instance à laquelle le volume est présentement attaché. **Ne supprimez pas le volume.**
8.  Dans l'instance temporaire de la génération précédente, exécutez les commandes ci-dessous. La commande `screen` est utilisée au cas où vous seriez déconnecté de la session SSH. Pour ce qui est de la seconde commande, nous supposons que le volume source `/dev/vdb` dans la génération précédente est attaché à l'instance temporaire de la génération précédente, que la taille du volume est de 96 Go, que la clé SSH pour se connecter à l'instance temporaire Arbutus est `key.pem`, et que le volume de destination dans Arbutus `/dev/vdb` est attaché à l'instance temporaire Arbutus. Remplacez l'adresse IP par celle de l'instance Arbutus à laquelle vous voulez vous connecter.
    ```bash
    screen
    sudo dd bs=16M if=/dev/vdb | pv -s 96G | ssh -i key.pem centos@xxx.xx.xx.xx "dd bs=16M of=/dev/vdb"
    ```

Vous disposez maintenant dans Arbutus d'une copie identique du volume de la génération précédente et vous pouvez l'utiliser pour lancer des instances dans Arbutus.

## Migration d'instances éphémères

Une instance éphémère n'est associée à aucun volume.

### Avec images et instantanés de volume Glance

Voir ci-dessus la section [Migration avec des images Glance](#migration-avec-des-images-glance).

### Autre option avec Linux 'dd'

1.  Connectez-vous à l’instance active sur le nuage de la génération précédente avec SSH. Avant de migrer une instance éphémère, il est important de fermer le plus de services possible (par exemple httpd, bases de données, etc.) et de ne garder que SSH.
2.  Avec le rôle d’administrateur (`root`), installez le CLI OpenStack si ce n’est pas déjà fait.
    ```bash
    yum install epel-release
    yum install python-devel python-pip gcc
    pip install python-openstackclient
    ```
3.  Le CLI OpenStack devrait maintenant être installé. Pour vérifier, lancez la commande `openstack` en ligne de commande. Pour plus d’information sur l’installation du CLI, consultez [https://docs.openstack.org/newton/user-guide/common/cli-install-openstack-command-line-clients.html](https://docs.openstack.org/newton/user-guide/common/cli-install-openstack-command-line-clients.html)
4.  Copiez le fichier RC d’Arbutus vers l’instance et faites un *source*. Pour vérifier si vous pouvez vous connecter à l’API OpenStack sur Arbutus, lancez la commande :
    ```bash
    openstack image list
    ```
5.  Le disque racine de l’instance est généralement `/dev/vda1`; vérifiez ceci en lançant la commande `df`.
6.  Avec l’utilitaire `dd`, créez une image à partir du disque racine attaché à l’instance. Dans l’exemple suivant, le nom de l’image est `ephemeralmigrate`. Lorsque l’opération est terminée, les détails de l’image seront affichés.
    ```bash
    dd if=/dev/vda | openstack image create --private --container-format bare --disk-format raw "ephemeralmigrate"
    ```
7.  Vous devriez maintenant voir l’image en allant à `Calcul -> Images` dans l’interface Arbutus. Cette image peut être utilisée pour lancer des instances sur Arbutus.
8.  Une fois que vos instances et volumes ont été migrés et testés et que tous vos enregistrements DNS ont été mis à jour, veuillez supprimer les anciens volumes et instances sur le nuage de la génération précédente.

## Méthodes de copie de données

Vous pouvez utiliser une méthode de copie avec laquelle vous êtes familier, mais nous recommandons les deux suivantes, selon la taille des volumes dans votre projet.

### Gros volumes de données : Globus

Pour les très gros volumes (plus de 5 To), nous recommandons Globus.

La méthode la plus simple est d'utiliser le client Globus Connect Personal avec un abonnement Globus Plus.
1.  **Abonnez-vous à Globus Connect Personal Plus.**
    *   Écrivez à globus@tech.alliancecan.ca.
    *   Répondez à l'invitation Globus Personal Plus et suivez les directives.
2.  **Pour chacune des instances touchées par le transfert de données, activez Globus Connect Personal.**
    *   Prenez connaissance de [Globus, Ordinateurs personnels](globus.md#ordinateurs-personnels) et de [https://www.globus.org/globus-connect-personal](https://www.globus.org/globus-connect-personal).
    *   Utilisez les directives appropriées pour installer Globus Connect Personal dans chaque instance. Pour Linux, consultez [https://docs.globus.org/how-to/globus-connect-personal-linux/](https://docs.globus.org/how-to/globus-connect-personal-linux/).
    *   Modifiez la configuration de chacune des instances pour communiquer avec le service Globus.
        *   Vérifiez que chaque instance possède une adresse IP externe.
        *   Vérifiez que le pare-feu des instances permet la [communication par les ports](https://docs.globus.org/how-to/configure-firewall-gcp/); voir aussi [Groupes de sécurité](managing-your-cloud-resources-with-openstack.md#groupes-de-sécurité).
        *   L'utilisateur qui exécute Globus Connect Personal doit avoir accès aux données dans les systèmes de fichiers de stockage.
    *   Dans l'espace utilisateur, exécutez Globus Connect Personal en arrière-plan.
    *   Comme abonné Globus Connect Personal Plus (étape 1), créez un point d'accès partagé pour une ou les deux instances.
3.  **Par l'interface Globus (globus.org, globus.calculcanada.ca) accédez aux points d'accès et transférez les données.**
    *   Voyez [https://docs.globus.org/how-to/get-started/](https://docs.globus.org/how-to/get-started/)

Pour plus d'information sur la configuration, consultez [https://computecanada.github.io/DHSI-cloud-course/globus/](https://computecanada.github.io/DHSI-cloud-course/globus/).

En cas de difficulté, contactez le [soutien technique](technical-support.md) (globus@tech.alliancecan.ca). Il est fortement suggéré de soumettre aussi une demande d’assistance au service technique.

### Petits volumes de données : rsync + ssh

Pour les plus petits volumes, `rsync + ssh` offre de bonnes vitesses de transfert et, comme Globus, travaille de manière incrémentale.

Voici un exemple de cas type :

1.  Connectez-vous avec SSH à l’instance sur le nuage de la génération précédente qui possède le volume principal. Prenez note du chemin absolu que vous voulez copier dans l’instance sur Arbutus.
2.  Lancez `rsync` sur SSH. Dans l’exemple suivant, on suppose qu’il existe une connexion sans mot de passe via des [clés SSH](ssh-keys.md). Utilisez les valeurs appropriées.
    ```bash
    rsync -avzP -e 'ssh -i ~/.ssh/key.pem' /local/path/ remoteuser@remotehost:/path/to/files/
    ```
3.  Vérifiez que les données ont bien été copiées dans l’instance sur Arbutus, puis supprimez les données sur le nuage de la génération précédente.

Vous pouvez aussi déplacer vos données par une autre méthode que vous connaissez bien.

## Configuration après la migration

Une fois que vous avez transféré vos données vers la nouvelle instance, certaines configurations post-transfert pourraient être requises. Ces activités pourraient inclure :

1.  La mise à jour des règles de pare-feu pour utiliser de nouvelles adresses IP et réseaux si un pare-feu basé sur l'hôte (par exemple `iptables`, `firewalld`, etc.) est utilisé.
2.  La collaboration avec votre fournisseur DNS pour mettre à jour les entrées DNS pour tous les domaines personnalisés (par exemple `www.monprojetarbutus.ca`).
3.  La mise à jour des adresses IP dans les fichiers de configuration (par exemple `/etc/hosts`, `/etc/resolv.conf`, `/etc/haproxy/haproxy.cfg`, `/var/www/`, `/var/lib/pgsql/data/pg_hba.conf`).
4.  La modification des noms d'utilisateur (par exemple `'root'@'192.168.65.%`) dans MySQL.
5.  Le renouvellement des certificats TLS (Transport Layer Security) Let’s Encrypt à l'aide de `certbot` ou d'autres utilitaires, par exemple si des adresses IP sont présentes dans le Nom alternatif de sujet (Subject Alternative Name - SAN) du certificat.
6.  Le test de la configuration.

Quand les tests auront été faits, informez les membres de votre équipe que la migration est terminée.

## Migration d'un système de fichiers partagé CephFS

Le système de fichiers partagé CephFS du nouveau nuage Arbutus est un service distinct et séparé, et toutes les données souhaitées doivent être migrées intentionnellement.

La gestion des partages hérités, y compris les opérations de création, de suppression et de gestion des clés, est contrôlée via le nuage Arbutus de la génération précédente. Cependant, une fois qu'un partage et une clé hérités sont créés, ces ressources peuvent être accessibles à partir d'une machine virtuelle dans le nouveau nuage Arbutus. De même, la création et la gestion des partages dans le nouveau nuage Arbutus se font exclusivement dans l'environnement du nouveau nuage Arbutus.

Les partages hérités et les nouveaux partages peuvent être montés sur des machines virtuelles du nouveau nuage Arbutus. Voici une procédure recommandée pour migrer les données entre les partages hérités et les nouveaux partages.
1.  Pour chaque partage dans le nuage Arbutus de la génération précédente, créez un partage équivalent dans le nouveau Arbutus.
2.  Montez les deux partages à des emplacements de montage distincts sur la même machine virtuelle dans le nouveau nuage Arbutus.
3.  Utilisez un outil de copie de données tel que `rsync` pour transférer les données de l'ancien partage vers le nouveau et assurez-vous de l'intégrité des données.

La procédure de montage des partages hérités demeure inchangée et peut être trouvée ici : [https://docs.alliancecan.ca/wiki/CephFS](https://docs.alliancecan.ca/wiki/CephFS)

La création du partage équivalent dans le nouveau nuage Arbutus suivra la même procédure, avec quelques différences essentielles :
1.  Vous devez créer le nouveau partage et les clés d'accès en utilisant l'interface web du nouveau nuage Arbutus.
2.  Vous devez créer un fichier `ceph.conf` séparé, avec un nom distinct tel que `ceph-new.conf`.
3.  La valeur de configuration `mon_host` devra être mise à jour pour le nouveau partage uniquement, dans le fichier `ceph-new.conf` :
    *   Valeur héritée : `10.30.201.3:6789,10.30.202.3:6789,10.30.203.3:6789`
    *   Nouvelle valeur : `134.87.15.61:6789,134.87.15.62:6789,134.87.15.63:6789`
4.  Lors du montage du nouveau partage, une valeur supplémentaire dans la commande de montage est requise après le `-o` pour spécifier le nouveau fichier de configuration : `conf=/etc/ceph/ceph-new.conf`.

Une fois les deux partages montés, utilisez `rsync` pour transférer les données. Les drapeaux `a`, `v` et `P` pour `rsync` sont recommandés.

```bash
rsync -avp /mnt/old-share/ /mnt/new-share/
```

Gardez à l'esprit qu'en fonction de la taille de votre partage, cela peut prendre beaucoup de temps. Il est conseillé d'utiliser un outil tel que `screen` ou `tmux` pour maintenir la session active en cas de perte de connexion.

## Migration de stockage objet

Le stockage objet du nouveau nuage Arbutus est un service distinct et séparé de celui de la génération précédente, et toutes les données souhaitées doivent être intentionnellement migrées.

La gestion des conteneurs (buckets) et objets hérités, y compris les opérations de création, de suppression, de manipulation d'objets et de gestion des clés, est contrôlée via le nuage Arbutus de la génération précédente. De même, la création et la gestion des conteneurs et objets dans le nouveau nuage Arbutus se font exclusivement dans l'environnement du nouveau nuage Arbutus.

La migration des données vers le stockage objet du nouveau nuage Arbutus peut être effectuée en utilisant diverses méthodes et outils. Si vous êtes familier avec les options, n'hésitez pas à utiliser la méthode qui convient le mieux à vos données.

**Point d'accès du stockage objet du nouveau nuage Arbutus :** [https://object-arbutus.alliancecan.ca](https://object-arbutus.alliancecan.ca)

**Point d'accès du stockage objet de la génération précédente d'Arbutus :** [https://object-arbutus.cloud.computecanada.ca](https://object-arbutus.cloud.computecanada.ca)

Soyez prudent si vous utilisez des listes de contrôle d'accès (ACL) de conteneurs; assurez-vous que l'outil que vous utilisez les copie correctement, ou recréez-les dans le nouvel environnement. La plupart des outils ne conservent pas les ACL de conteneurs. Gardez à l'esprit que si vous référencez des UUID d'utilisateur ou de projet, ils seront différents dans le nouveau nuage Arbutus.

De plus, le stockage objet du nouveau nuage Arbutus utilise des locataires. Les collisions de noms de conteneurs ne se produiront donc qu'au sein d'un projet individuel plutôt que sur tous les projets Arbutus. Lors de l'authentification avec l'API Swift ou S3, le locataire est déduit de l'utilisateur/clé fourni. Cependant, pour l'accès public aux conteneurs sans authentification, le locataire doit être spécifié. L'ID du locataire est identique à l'ID du projet OpenStack. L'URL pour l'accès Swift non authentifié peut être trouvée via l'interface Horizon, tandis que l'URL pour l'accès S3 non authentifié aura le format suivant :

`https://object-arbutus.alliancecan.ca/<id-locataire>:<nom-conteneur>/<nom-objet>`

Si vous ne savez pas quel outil utiliser, nous pouvons recommander `rclone`. `rclone` ne copiera pas les ACL de conteneurs, de sorte que tout accès sera initialement privé dans le nouvel emplacement.

Exemple `rclone` :

1.  Installez `rclone` : [https://rclone.org/install/](https://rclone.org/install/)
2.  Créez des informations d'identification S3 dans le nuage Arbutus de la génération précédente et dans le nouveau nuage Arbutus : [Stockage objet Arbutus](arbutus-object-storage.md)
3.  Créez un fichier de configuration pour `rclone` :
    *   Emplacement du fichier sur Linux/MacOS : `~/.config/rclone/rclone.conf`
    *   Contenu du fichier, insérant vos valeurs d'accès et de secret pour chaque environnement :
        ```ini
        [new] 
        type = s3 
        access_key_id = <CLÉ D'ACCÈS DU NOUVEAU SYSTÈME> 
        secret_access_key = <CLÉ SECRÈTE DU NOUVEAU SYSTÈME> 
        endpoint = https://object-arbutus.alliancecan.ca 
        [legacy] 
        type = s3 
        access_key_id = <CLÉ D'ACCÈS HÉRITÉE> 
        secret_access_key = <CLÉ SECRÈTE HÉRITÉE> 
        endpoint = https://object-arbutus.cloud.computecanada.ca
        ```
4.  Synchronisez tous les conteneurs avec la commande suivante :
    ```bash
    rclone sync legacy: new:
    ```

## Soutien technique

Pour une demande d'assistance technique, écrivez à [cloud@tech.alliancecan.ca](mailto:cloud@tech.alliancecan.ca).