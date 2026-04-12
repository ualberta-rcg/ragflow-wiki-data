---
title: "Database servers"
slug: "database_servers"
lang: "base"

source_wiki_title: "Database servers"
source_hash: "3958354b58ed59f16ad2e192c41fb299"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:48:47.893632+00:00"

tags:
  - cloud

keywords:
  - "database backups"
  - "Alliance username"
  - "Hostname"
  - "CA certificate"
  - "Cedar"
  - "DBaaS host"
  - "mysql"
  - "PostgreSQL"
  - "MariaDB"
  - "Database servers"
  - "Cedar PostgreSQL server"
  - "PostGIS extension"
  - "PostgreSQL database"
  - "access request"
  - "Database sharing"
  - "PostgreSQL account"
  - "MySQL server"
  - "database sharing"
  - "SQL command"
  - "MySQL database"
  - "MySQL"
  - ".my.cnf"
  - "job scheduler"
  - "Graham"
  - "Database as a Service"
  - "database"
  - "MariaDB/MySQL database"
  - "psql client"
  - "Postgres"
  - "Technical support"
  - "head node"
  - "IP address"
  - "SSL connection"

questions:
  - "What database servers are available for researchers on the Cedar and Graham clusters, and how does the transition to the new Nibi system affect Graham's database services?"
  - "What specific information must be provided to Technical Support to request a MySQL account, and how are the resulting login credentials securely stored?"
  - "What are the correct procedures and restrictions for connecting to the Cedar MySQL server and running SQL commands or CPU-intensive scripts?"
  - "How does the mysql command automatically obtain the required password and server name without needing them as arguments?"
  - "Why is it acceptable to execute a long-running SQL command directly from the head node?"
  - "Under what circumstances must a script that issues SQL commands be submitted as a job to the scheduler?"
  - "What is the required naming convention for creating a new MySQL database on the Cedar server?"
  - "How can a user grant privileges to share specific tables from their MySQL database with other users?"
  - "What is the process for requesting and obtaining an account and database on the Cedar PostgreSQL server?"
  - "How do you securely connect to your PostgreSQL database and ensure you are using the latest version of the client?"
  - "What are the necessary steps and SQL commands to share a specific table in your PostgreSQL database with another user?"
  - "How can a user request access to the Database as a Service (DBaaS) offering, and what specific information must be included in the request?"
  - "What will be the username and default name of the PostgreSQL database assigned to a user?"
  - "Are users permitted to create their own databases within the system?"
  - "How can a user request additional databases or the PostGIS extension for their project?"
  - "Where can users download the CA certificate used to sign the host certificate for the service?"
  - "What type of connection is strictly enforced when connecting to the DBaaS host, and what happens if a plain text connection is attempted?"
  - "What specific command-line tools and flags are required to establish a secure connection to PostgreSQL and MariaDB/MySQL databases?"
  - "What is the frequency and retention period for the database backups?"
  - "What specific information must be included when contacting Technical support to request database access?"
  - "What are the hostnames and TCP ports used to connect to the MySQL and PostgreSQL databases?"
  - "Where can users download the CA certificate used to sign the host certificate for the service?"
  - "What type of connection is strictly enforced when connecting to the DBaaS host, and what happens if a plain text connection is attempted?"
  - "What specific command-line tools and flags are required to establish a secure connection to PostgreSQL and MariaDB/MySQL databases?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Database servers available for researchers

The Alliance offers access to MySQL and Postgres database servers for researchers on both Cedar and Graham.

!!! note
    As of January 13, 2025, the Graham cluster will be operating at approximately 25% capacity (see [details here](../clusters/graham.md#graham-reduction)) until [Nibi](../clusters/nibi.md) is available. No database server will be provided on Graham during the transition to the new system.

| Information | Cedar - MySQL | Cedar - Postgres | Graham - MySQL |
| :---------- | :------------ | :--------------- | :------------- |
| Description | General purpose server for the researcher wanting to set up SQL tables and issue SQL commands against them. | General purpose server for the researcher wanting to set up SQL tables and issue SQL commands against them. Includes a PostGIS extension available for those needing to do geocoding. | General purpose server for the researcher wanting to set up SQL tables and issue SQL commands against them. |
| Server name | cedar-mysql-vm.int.cedar.computecanada.ca | cedar-pgsql-vm.int.cedar.computecanada.ca | cc-gra-dbaas1.sharcnet.ca <br> IP: 199.241.163.99 |
| Short server name (can be used instead of long name) | cedar-mysql-vm | cedar-pgsql-vm | N/A |
| Latest version | [MariaDB version 11.5](https://mariadb.com/kb/en/mariadb-server-11-5/) | [PostgreSQL version 16](https://www.postgresql.org/docs/release/16.0/), PostGIS version 3.3 extension | [MariaDB version 11.5](https://mariadb.com/kb/en/mariadb-server-11-5/) |
| Documentation | [MariaDB website](https://www.mariadb.com) | [Postgres website](https://www.postgresql.org), [PostGIS documentation](https://postgis.net/documentation) | [MariaDB website](https://www.mariadb.com) |

## Cedar MySQL server

The Cedar MySQL server offers MariaDB which is compatible with other flavours of MySQL. For information on compatibility, see [MariaDB versus MySQL Compatibility](https://mariadb.com/kb/en/library/mariadb-vs-mysql-compatibility/).

The MariaDB server runs as a VM called "cedar-mysql-vm" (full name: cedar-mysql-vm.int.cedar.computecanada.ca). Users who have accounts on the MySQL server are able to connect only through the Cedar head node (cedar.computecanada.ca), Cedar compute nodes and [Cedar Portal](https://gateway.cedar.computecanada.ca).

For security, users cannot make an SSH connection to the database server directly.

### MySQL account and connection

If you need the privileges to create your own database, you will need a MySQL account. To get a MySQL account on the Cedar MySQL server, please send a request to our [Technical support](../support/technical_support.md) with the following information:

*   Your Alliance username
*   Amount of database space needed for your project

We will then create an MySQL account with the same username as your Alliance username and a 16-digit random string password. The username, password, database server name, and other information required to make a MySQL connection will be stored in a file called `.my.cnf` in your home directory. This file is confidential. You cannot change its contents but you can read it or delete it. If the file is deleted, you will lose access to your database.

Run the "mysql" client to connect to the MySQL server. An older version of the client may be available without loading a [module](../programming/utiliser_des_modules.md), but it will not give you access the latest features on the MySQL server. We recommend issuing the following commands to load a more recent version of the client:

```bash
[name@server ~]$ module load mariadb
[name@server ~]$ mariadb --version
```

You can use the following commands to test that your MySQL database account is set up correctly:

```bash
mysql
MariaDB [(none)]> show databases;
MariaDB [(none)]> quit
```

**Do not** use the `-p` or `-h` options as arguments when running `mysql`. The required password and server name are taken automatically from your `.my.cnf` file.

It is acceptable to submit a long-running SQL command from the head node, as most of the CPU usage is taken from the database server side. However, if you run a script which issues SQL commands and uses lots of CPU, then it needs to be submitted as a job to the scheduler. See [Running jobs](../running-jobs/running_jobs.md) for details.

### Set up your MySQL database

In order to be able to set up MySQL tables and query them, you need to create your own database. To create a database, the name of the database is arbitrary but it must start with "*username_*" where "*username*" is your MySQL username. For example, if your username were "david" the name of the database **must** start with "david_" and the commands to create a database called "david_db1", for example, would be:

```bash
mysql
MariaDB [(none)]> CREATE DATABASE david_db1;
MariaDB [(none)]> quit
```

You may create multiple MySQL databases as long as they all start with "*username_*". The created databases will automatically be accessible only to you from the Cedar head node, Cedar compute nodes, and [Cedar Portal](https://gateway.cedar.computecanada.ca). You will have full privileges to create SQL objects such as tables, views, etc.

### Work with your MySQL database

Suppose you have account "david" and have created a database called "david_db1" and want to use it. Here's how:

```bash
mysql
MariaDB [(none)]> -- List available databases. Confirm david_db1 is in the list
MariaDB [(none)]> SHOW DATABASES;
MariaDB [(none)]> -- Get into the database
MariaDB [(none)]> USE david_db1;
MariaDB [(none)]> ... Issue SQL commands. See below for information.
MariaDB [(none)]> quit
```

Resources for using MariaDB:

*   [MariaDB Knowledgebase](https://mariadb.com/kb/en/)
*   [MariaDB Training and Tutorials](https://mariadb.com/kb/en/library/training-tutorials/)
*   [MariaDB SQL Statement Structure](https://mariadb.com/kb/en/library/sql-statements-structure/)
*   [MariaDB Optimization and Indexes](https://mariadb.com/kb/en/library/optimization-and-indexes/)

### Share your MySQL data

All MySQL account holders on Cedar can share their own databases. To share a table of your database with other users:

1.  Run the command `mysql` to connect to MySQL.
2.  Run the command `USE *database*;`
    *   "*database*" is the name of the database that you would like to share a table from.
3.  Run the command `GRANT *priv_type* ON *mytable* TO '*user*'@'172.%';`
    *   "*priv_type*" is the type of privilege you would like to grant.
    *   "*mytable*" is the name of the table.
    *   "*user*" is the username you would like to share your table with.

#### MySQL sharing example

Username "david" would like to share his table, "mytable" from database, "david_db" with username "john" for reading only. Here are commands he needs to run:

```bash
mysql
MariaDB [(none)]> USE david_db;
MariaDB [(none)]> GRANT SELECT on mytable to 'john'@'172.%';
MariaDB [(none)]> quit;
```

## Cedar PostgreSQL server

The Cedar Postgres server has [Postgres](https://www.postgresql.org/) along with the [PostGIS](https://postgis.net/) extension.

The Cedar PostgreSQL server runs as a VM called "cedar-pgsql-vm" (full name: cedar-pgsql-vm.int.cedar.computecanada.ca). Users who have accounts on the PostgreSQL server are able to connect through the main Cedar head node (cedar.computecanada.ca), Cedar compute nodes, and [Cedar Portal](https://gateway.cedar.computecanada.ca).

For security, users cannot make an SSH connection to the database server directly.

To get an account and database on the Cedar PostgreSQL server, send a request to our [Technical support](../support/technical_support.md) with the following information:

*   Your Alliance username
*   Amount of database space needed for your project
*   If you need the PostGIS extension for the database

### PostgreSQL account and connection

The PostgreSQL account we create for you will have the same username as your Alliance username. You will be given a database. The name of the database will typically be "<username>_db" where <username> is your Alliance username. You cannot create a database yourself. If you need more than one database, please send a request to [Technical support](../support/technical_support.md).

You do not need to supply a password to access your PostgreSQL account. For security reasons your Alliance password must NEVER be required or used in a script. This also means that one user cannot access another user's database directly.

Run the "psql" client to connect to the PostgreSQL server. An older version of the client may be available without loading a [module](../programming/utiliser_des_modules.md), but it will not give you access to the latest features of PostgreSQL. We recommend loading the following module to use a more recent version of the client:

```bash
[name@server ~]$ module load postgresql
[name@server ~]$ psql --version
```

### Work with your PostgreSQL database

Suppose you have account "david" and have been assigned a database called "david_db". Here is an example of how to use it from the Cedar head node:

```bash
psql -h cedar-pgsql-vm -d david_db
david_db=> -- List names of tables in your database
david_db=> \dt
david_db=> ... Issue SQL commands. See below for more information.
david_db=> -- Quit
david_db=> \q
```

Resources for using PostgreSQL:

*   [PostgreSQL tutorials](https://www.postgresql.org/docs/current/static/tutorial.html)
*   [PostgreSQL manuals](https://www.postgresql.org/docs/)
*   [PostgreSQL release notes](https://www.postgresql.org/docs/release/)

### Share your PostgreSQL data

You can share your data in your PostgreSQL database with others. This is how:

*   The person with whom you want to share access must have a Postgres account on the system. They should apply for one as described above.
*   You will have to give the person `connect` access to your database.
*   For each table or view to be shared, you give the person one or more of `select`, `update`, `insert`, and `delete` access to it.
*   You can also revoke access to a table, view, or database.

Here is an example of user 'david' sharing a table with user 'kim':

```bash
psql -h cedar-pgsql-vm -d david_db
david_db=> -- Give kim connect access to the database
david_db=> grant connect on database david_db to kim;
david_db=> -- Give kim select-only access to a table called mytable
david_db=> grant select on mytable to kim;
david_db=> -- Quit
david_db=> \q
```

Here is an example of user 'kim' accessing the shared table:

```bash
psql -h cedar-pgsql-vm -d kim_db
kim_db=> -- Connect to the database containing the table to be accessed
kim_db=> \c david_db
david_db=> -- Display the rows in the shared table
david_db=> select * from mytable;
david_db=> -- Quit
david_db=> \q
```

Here is an example of user 'david' revoking access to 'kim':

```bash
psql -h cedar-pgsql-vm -d david_db
david_db=> -- Revoke kim's select-only access to a table called mytable
david_db=> revoke select on mytable from kim;
david_db=> -- Revoke kim's connect access to the database
david_db=> revoke connect on database david_db from kim;
david_db=> -- Quit
david_db=> \q
```

## Graham MySQL server

The steps for obtaining and using an account on the Graham MySQL server are similar to [those described above for Cedar](#cedar-mysql-server) except you will need to load the following module instead:

```bash
[name@server ~]$ module load mysql
```

## Cloud-based database servers

### Database as a Service (DBaaS)

If a VM is not sufficient to run a database load, a managed database can be used instead, the current offering includes MySQL/MariaDB and Postgres on a physical system.
The database systems as well as all databases are being backed up once a day. The backups are archived for 3 months.
To request access, please contact [Technical support](../support/technical_support.md).

**Please provide in your request the client network or IP address you will access the database from.**

| Type  | Hostname                          | TCP port |
| :---- | :-------------------------------- | :------- |
| mysql | dbaas101.arbutus.cloud.computecanada.ca | 3306     |
| pgsql | dbaas101.arbutus.cloud.computecanada.ca | 5432     |

The CA certificate which is used to sign the host certificate for the service, is available for download [here](https://docs.computecanada.ca/mediawiki/images/5/58/Dbaas-ca.pem.zip).

### PostgreSQL database

Your instance will use an ssl connection to connect to the DBaaS host.
The example below connects to the DBaaS host, as **user01** and uses the database **dbinstance** via an ssl connection.

```text
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

The ssl connection is enforced and plain text connections fail.

### MariaDB/MySQL database

Your instance will use an ssl connection to connect to the DBaaS host.
The example below connects to the DBaaS host, as **user01** and uses the database **dbinstance** via an ssl connection.

```text
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

If you try to use a plain text connection, your authentication will fail.

```text
mysql -h dbaas101.arbutus.cloud.computecanada.ca -u user01 -p dbinstance
Enter password: 
ERROR 1045 (28000): Access denied for user 'user01'@'client.arbutus' (using password: YES)