---
title: "Database servers/fr"
slug: "database_servers"
lang: "fr"

source_wiki_title: "Database servers/fr"
source_hash: "93b019810e221611a8a80d72e3c6b2fd"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:50:01.245910+00:00"

tags:
  - cloud

keywords:
  - "client psql"
  - "cedar-pgsql-vm"
  - "base de données"
  - "Cedar"
  - "compte MySQL"
  - "PostgreSQL"
  - "MariaDB"
  - "client"
  - "compte"
  - "revoke connect"
  - "serveur"
  - "partage de données"
  - "connexion ssl"
  - "Bases de données à la demande"
  - "Serveurs de bases de données"
  - "nœud de connexion"
  - "PostGIS"
  - "MySQL"
  - "Serveurs infonuagiques"
  - "Serveur MySQL"
  - "Graham"
  - "MySQL/MariaDB"
  - "serveur Cedar"
  - "charger un module"
  - "mariadb"
  - "Postgres"

questions:
  - "Quel est l'impact de la transition vers le système Nibi sur la disponibilité des serveurs de bases de données de la grappe Graham à partir de janvier 2025 ?"
  - "Quels types de serveurs de bases de données et quelles versions logicielles sont spécifiquement disponibles sur les grappes Cedar et Graham ?"
  - "Quelle est la procédure à suivre pour obtenir un compte MySQL sur Cedar et comment s'y connecter de manière sécurisée ?"
  - "Pourquoi est-il recommandé de charger un module plutôt que d'utiliser le client disponible par défaut ?"
  - "Quelles commandes permettent de charger une version plus récente du client MariaDB et de vérifier sa version ?"
  - "Comment un utilisateur peut-il tester la configuration de son compte MySQL une fois le client lancé ?"
  - "Quelle est la convention de nommage obligatoire lors de la création d'une nouvelle base de données MySQL ?"
  - "Comment un utilisateur peut-il partager l'accès à une table spécifique de sa base de données avec une autre personne ?"
  - "Quelles sont les recommandations pour l'exécution de scripts SQL nécessitant une forte utilisation du CPU ?"
  - "Comment doit-on procéder pour demander la création d'un compte sur le serveur PostgreSQL de Cedar et quelles informations fournir ?"
  - "Quelle est la méthode recommandée pour se connecter à sa base de données PostgreSQL et l'utiliser depuis un nœud de connexion ?"
  - "Quelles sont les étapes et les commandes SQL requises pour partager l'accès à ses tables PostgreSQL avec un autre utilisateur ?"
  - "Quels logiciels et extensions sont offerts par le serveur Postgres sur Cedar ?"
  - "Quel est le nom de l'instance et le nom long du serveur PostgreSQL ?"
  - "Quels sont les seuls points d'accès permis pour se connecter au serveur PostgreSQL ?"
  - "Comment doit-on procéder pour demander l'accès à une base de données à la demande (DBaaS) et quelles informations sont requises ?"
  - "Quelle est la fréquence des copies de sauvegarde des bases de données et pendant combien de temps sont-elles conservées ?"
  - "Quel protocole de sécurité est exigé pour se connecter aux instances PostgreSQL ou MariaDB/MySQL, et quelle est la conséquence d'une tentative de connexion en texte brut ?"
  - "Quelles commandes SQL sont illustrées pour retirer les permissions de lecture et de connexion à un utilisateur spécifique ?"
  - "En quoi la procédure pour obtenir et utiliser un compte sur le serveur MySQL de Graham est-elle similaire à celle du serveur Cedar ?"
  - "Quelle modification spécifique concernant les modules est nécessaire pour configurer correctement le serveur MySQL sur Graham ?"
  - "Comment doit-on procéder pour demander l'accès à une base de données à la demande (DBaaS) et quelles informations sont requises ?"
  - "Quelle est la fréquence des copies de sauvegarde des bases de données et pendant combien de temps sont-elles conservées ?"
  - "Quel protocole de sécurité est exigé pour se connecter aux instances PostgreSQL ou MariaDB/MySQL, et quelle est la conséquence d'une tentative de connexion en texte brut ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Serveurs de bases de données pour la recherche

Les serveurs de bases de données MySQL et Postgres sont disponibles sur Cedar et Graham.

!!! warning "REMARQUE"
    À compter du 13 janvier 2025, la capacité de la grappe Graham sera réduite à 25 % (voir [Réduction de la capacité](../clusters/graham.md#réduction-de-la-capacité)) jusqu'à ce que le nouveau système [Nibi](../clusters/nibi.md) soit disponible. Aucun serveur de bases de données ne sera offert pendant la transition.

| Information | Cedar, MySQL | Cedar, Postgres | Graham, MySQL |
| :---------- | :----------- | :-------------- | :------------ |
| Description | serveur d’usage général pour configurer et traiter des tables SQL | serveur d’usage général pour configurer et traiter des tables SQL; comprend l’extension PostGIS pour les données spatiales | serveur d’usage général pour configurer et traiter des tables SQL |
| Nom long    | cedar-mysql-vm.int.cedar.computecanada.ca | cedar-pgsql-vm.int.cedar.computecanada.ca | cc-gra-dbaas1.sharcnet.ca <br> IP: 199.241.163.99 |
| Nom court   | cedar-mysql-vm | cedar-pgsql-vm | --- |
| Récente version | [MariaDB version 11.5](https://mariadb.com/kb/en/mariadb-server-11-5/) | [PostgreSQL version 16](https://www.postgresql.org/docs/release/16.0/), PostGIS version 3.3 (extension) | [MariaDB version 11.5](https://mariadb.com/kb/en/mariadb-server-11-5/) |
| Documentation | [site web MariaDB](https://www.mariadb.com) | [site web Postgres](https://www.postgresql.org), [documentation PostGIS](https://postgis.net/documentation) | [site web MariaDB](https://www.mariadb.com) |

## Serveur MySQL sur Cedar

Le serveur MySQL sur Cedar offre MariaDB 10.4 qui est compatible avec les autres versions MySQL. Pour l'information sur la compatibilité, consultez [MariaDB versus MySQL : Compatibilité](https://mariadb.com/kb/en/library/mariadb-vs-mysql-compatibility/).

Le serveur MariaDB est l'instance `cedar-mysql-vm` (nom long, cedar-mysql-vm.int.cedar.computecanada.ca). Si vous possédez un compte sur le serveur MySQL, vous pouvez y accéder uniquement par le nœud de connexion (cedar.computecanada.ca), les nœuds de calcul ou le [portail Cedar](https://gateway.cedar.computecanada.ca).

Pour des raisons de sécurité, vous ne pouvez pas vous connecter directement au serveur de base de données via SSH.

### Compte et connexion

Vous devez détenir un compte MySQL pour avoir le privilège requis pour créer une base de données. Pour obtenir un compte sur le serveur MySQL de Cedar, contactez le [soutien technique](../support/technical_support.md) en indiquant

*   le nom d'utilisateur pour votre compte avec l'Alliance et
*   l'espace nécessaire pour la base de données de votre projet.

Nous créerons un compte MySQL pour lequel le nom d'utilisateur sera celui de votre compte avec l'Alliance ainsi qu'une chaîne de 16 nombres aléatoires comme mot de passe. Un fichier nommé `.my.cnf` sera enregistré dans votre répertoire /home contenant le nom d'utilisateur, le mot de passe, le nom du serveur de base de données et d'autres renseignements nécessaires pour vous connecter. Ce fichier est confidentiel. Son contenu ne peut pas être modifié, mais le fichier peut être lu ou supprimé. En supprimant ce fichier, vous perdrez l’accès à votre base de données.

Lancez le client `mysql` pour vous connecter au serveur MySQL. Une version moins récente du client est disponible sans que vous ayez à [charger un module](../programming/utiliser_des_modules.md), mais vous n'aurez pas les dernières fonctionnalités du serveur. Nous vous recommandons de charger une version plus récente du client avec

```bash
[name@server ~]$ module load mariadb
[name@server ~]$ mariadb --version
```

Testez la configuration de votre compte MySQL avec

```bash
mysql
MariaDB [(none)]> show databases;
MariaDB [(none)]> quit
```

N'utilisez pas les options `-p` ou `-h` en argument en lançant `mysql`. Le mot de passe et le nom du serveur proviendront automatiquement du fichier `.my.cnf`.

Vous pouvez soumettre une commande SQL à partir du nœud de connexion puisque l'utilisation du CPU provient pour une grande part du côté du serveur de base de données. Toutefois, si votre script contient plusieurs commandes SQL et utilise beaucoup le CPU, il doit faire partie d'une tâche soumise à l'ordonnanceur; voyez [Exécuter des tâches](../running-jobs/running_jobs.md) pour plus d'information.

### Configuration

Pour créer des tables et faire des requêtes, vous devez créer votre propre base de données dont le nom doit commencer par *nom de l'utilisateur_*, soit votre nom d'utilisateur MySQL. Si votre nom d'utilisateur est *david*, le nom de la base de données doit commencer par *david_* et les commandes pour créer *david_db1* seraient

```bash
mysql
MariaDB [(none)]> CREATE DATABASE david_db1;
MariaDB [(none)]> quit
```

Vous pouvez créer plusieurs bases de données, mais leurs noms doivent commencer par *nom d'utilisateur_*. Ces bases de données seront accessibles uniquement par vous à partir du nœud de connexion (cedar.computecanada.ca), des nœuds de calcul ou du [portail Cedar](https://gateway.cedar.computecanada.ca) et vous aurez tous les privilèges pour la création d'objets, par exemple les tables et les vues.

### Utilisation de votre base de données

Supposons que votre compte est *david* et que vous avez créé la base de données *david_db1*. Pour l'utiliser, lancez

```bash
mysql
MariaDB [(none)]> -- List available databases. Confirm david_db1 is in the list
MariaDB [(none)]> SHOW DATABASES;
MariaDB [(none)]> -- Get into the database
MariaDB [(none)]> USE david_db1;
MariaDB [(none)]> ... Issue SQL commands. See below for information.
MariaDB [(none)]> quit
```

Consultez les sites web suivants pour plus de renseignements sur MariaDB :
*   [Base de connaissances](https://mariadb.com/kb/en/)
*   [Formations et tutoriels](https://mariadb.com/kb/en/library/training-tutorials/)
*   [Énoncés et structure SQL](https://mariadb.com/kb/en/library/sql-statements-structure/)
*   [Optimisation et index](https://mariadb.com/kb/en/library/optimization-and-indexes/)

### Partager vos données MySQL

Si vous avez un compte MySQL sur Cedar, vous pouvez partager vos données. Pour partager une table :

1.  Connectez-vous à MySQL avec `mysql`.
2.  Lancez la commande `USE 'database';`
    *   *database* est le nom de la base de données où se trouve la table que vous voulez partager
3.  Lancez la commande `GRANT 'priv_type' ON 'mytable' TO 'user'@'172.%';`
    *   *priv_type* est le type de privilège que vous voulez accorder
    *   *mytable* est le nom de la table
    *   *user* est le nom d'utilisateur de la personne avec qui vous voulez partager la table

#### Exemple de partage

Ici, l'utilisateur *david* veut partager la table *mytable* de la base de données *david_db* avec *john* en lecture seulement.

```bash
mysql
MariaDB [(none)]> USE david_db;
MariaDB [(none)]> GRANT SELECT on mytable to 'john'@'172.%';
MariaDB [(none)]> quit;
```

## Serveur PostgreSQL sur Cedar

Le serveur Postgres sur Cedar offre [Postgres](https://www.postgresql.org/) et [l'extension PostGIS](https://postgis.net/).

Le serveur PostgreSQL est l'instance `cedar-pgsql-vm` (nom long, cedar-pgsql-vm.int.cedar.computecanada.ca). Si vous possédez un compte sur le serveur PostgreSQL, vous pouvez y accéder uniquement par le nœud de connexion (cedar.computecanada.ca), les nœuds de calcul ou le [portail Cedar](https://gateway.cedar.computecanada.ca).

Pour des raisons de sécurité, vous ne pouvez pas vous connecter directement au serveur de base de données via SSH.

Pour obtenir un compte sur le serveur PostgreSQL de Cedar, contactez le [soutien technique](../support/technical_support.md) en indiquant
*   votre nom d'utilisateur,
*   l'espace nécessaire pour la base de données de votre projet,
*   si vous avez besoin de l'extension PostGIS.

### Compte et connexion

Nous créerons un compte PostgreSQL pour lequel le nom d'utilisateur sera celui de votre compte avec l'Alliance. Vous aurez accès à une base de données dont le nom sera *<nom d'utilisateur>_db*. Vous ne pouvez pas créer une base de données, mais si vous en avez besoin de plus d'une, écrivez au [soutien technique](../support/technical_support.md).

Vous n'avez pas besoin d'un mot de passe pour accéder à votre compte PostgreSQL sur Cedar. Pour des raisons de sécurité, le mot de passe pour votre compte avec l'Alliance ne doit JAMAIS être requis ou utilisé dans un script. Les utilisateurs n'ont ainsi pas d'accès direct aux bases de données des autres utilisateurs.

Lancez le client `psql` pour vous connecter au serveur PostgreSQL. Une version moins récente du client est disponible sans que vous ayez à [charger un module](../programming/utiliser_des_modules.md), mais vous n'aurez pas les dernières fonctionnalités de la version 10. Nous vous recommandons le charger une version plus récente avec

```bash
[name@server ~]$ module load postgresql
[name@server ~]$ psql --version
```

### Utilisation de votre base de données

Supposons que votre compte est *david* et qu'on vous a assigné la base de données *david_db*. Pour l'utiliser à partir d’un nœud de connexion, lancez

```bash
psql -h cedar-pgsql-vm -d david_db
david_db=> -- List names of tables in your database
david_db=> \dt
david_db=> ... Issue SQL commands. See below for more information.
david_db=> -- Quit
david_db=> \q
```

Consultez les sites web suivants pour plus de renseignements sur PostgreSQL :
*   [tutoriel](https://www.postgresql.org/docs/current/static/tutorial.html)
*   [manuels](https://www.postgresql.org/docs/)
*   [notes de mise à jour](https://www.postgresql.org/docs/release/)

### Partager vos données PostgreSQL

Pour partager les données de votre base de données PostgreSQL,
*   la personne avec laquelle vous voulez partager vos données doit détenir un compte PostgreSQL sur la grappe (voir ci-dessus),
*   donnez à cette personne un accès `connect` à votre base de données,
*   pour chaque table ou vue que vous voulez partager, donnez aussi un ou plusieurs des accès `select, update, insert` et `delete`,
*   l'accès à une table, une vue ou à la base de données peut être révoqué.

Dans cet exemple, David partage une table avec Kim :

```bash
psql -h cedar-pgsql-vm -d david_db
david_db=> -- Give kim connect access to the database
david_db=> grant connect on database david_db to kim;
david_db=> -- Give kim select-only access to a table called mytable
david_db=> grant select on mytable to kim;
david_db=> -- Quit
david_db=> \q
```

Ici, Kim accède à la table partagée :

```bash
psql -h cedar-pgsql-vm -d kim_db
kim_db=> -- Connect to the database containing the table to be accessed
kim_db=> \c david_db
david_db=> -- Display the rows in the shared table
david_db=> select * from mytable;
david_db=> -- Quit
david_db=> \q
```

Ici, David révoque le droit d'accès de Kim :

```bash
psql -h cedar-pgsql-vm -d david_db
david_db=> -- Revoke kim's select-only access to a table called mytable
david_db=> revoke select on mytable from kim;
david_db=> -- Revoke kim's connect access to the database
david_db=> revoke connect on database david_db from kim;
david_db=> -- Quit
david_db=> \q
```

## Serveur MySQL sur Graham

Les étapes pour obtenir et utiliser un compte sur le serveur MySQL de Graham sont semblables à [celles décrites ci-dessus pour Cedar](database_servers.md#serveur-mysql-sur-cedar), sauf qu'il faut remplacer le module avec

```bash
[name@server ~]$ module load mysql
```

## Serveurs infonuagiques

### Bases de données à la demande (DBaaS)

Si vous avez besoin de plus qu'une instance pour traiter votre base de données, vous pouvez utiliser MySQL/MariaDB ou Postgres sur un ordinateur physique.
Les copies de sauvegarde se font chaque jour et sont conservées pour trois mois.
Pour y accéder, contactez le [soutien technique](../support/technical_support.md).

!!! note "IMPORTANT"
    Dans votre demande, indiquez le réseau client ou l'adresse IP à partir de laquelle vous voulez accéder à la base de données.

| Type  | Nom de l'hôte                          | Port TCP |
| :---- | :------------------------------------- | :------- |
| mysql | dbaas101.arbutus.cloud.computecanada.ca | 3306     |
| pgsql | dbaas101.arbutus.cloud.computecanada.ca | 5432     |

[Téléchargez le certificat de l'autorité d'authentification](https://docs.computecanada.ca/mediawiki/images/5/58/Dbaas-ca.pem.zip).

### PostgreSQL

Votre instance utilisera une connexion SSL pour se connecter à l'hôte DBaaS.
Dans l'exemple suivant, la connexion se fait à l'hôte DBaaS par **user01** et utilise la base de données **dbinstance** via une connexion SSL.

```console
psql --set "sslmode=require" -h dbaas101.arbutus.cloud.computecanada.ca -U user01 -d dbinstance
Password for user user01:
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
dbinstance=> \l dbinstance
                               List of databases
    Name    | Owner  | Encoding |   Collate   |    Ctype    | Access privileges
------------+--------+----------+-------------+-------------+-------------------
 dbinstance | user01 | UTF8     | en_US.UTF-8 | en_US.UTF-8 | user01=CTc/user01
(1 row)
```

La connexion SSL s'applique et les connexions en texte brut échoueront.

### MariaDB/MySQL

Votre instance utilisera une connexion SSL pour se connecter à l'hôte DBaaS.
Dans l'exemple suivant, la connexion se fait à l'hôte DBaaS par **user01** et utilise la base de données **dbinstance** via une connexion SSL.

```console
mysql --ssl -h dbaas101.arbutus.cloud.computecanada.ca -u user01 -p dbinstance
Enter password:
MariaDB [dbinstance]> show databases;
+--------------------+
| Database           |
+--------------------+
| dbinstance         |
| information_schema |
+--------------------+
2 rows in set (0.001 sec)
```

Si vous essayez de vous connecter avec du texte brut, votre authentification échouera.

```console
mysql -h dbaas101.arbutus.cloud.computecanada.ca -u user01 -p dbinstance
Enter password:
ERROR 1045 (28000): Access denied for user 'user01'@'client.arbutus' (using password: YES)