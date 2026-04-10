---
title: "DBaaS/en"
slug: "dbaas"
lang: "en"

source_wiki_title: "DBaaS/en"
source_hash: "d86f53be2571f1044ba3fdf5cac8c993"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T05:55:02.161859+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

## Database as a Service (DBaaS)
If a VM is not sufficient to run a database load, a managed database can be used instead. The current offering includes MySQL/MariaDB and Postgres on a physical system.
The database systems as well as all databases are being backed up once a day. The backups are archived for 3 months.
To request access, please contact [Technical support](technical-support.md).

!!! warning
    **Please provide in your request the client network or IP address you will access the database from.**

| Type | Hostname | TCP port |
|---|---|---|
| mysql | dbaas101.arbutus.cloud.computecanada.ca | 3306 |
| pgsql | dbaas101.arbutus.cloud.computecanada.ca | 5432 |

The CA certificate which is used to sign the host certificate for the service, is available for download [here](http://repo.arbutus.cloud.computecanada.ca/dbaas-ca.pem).

## PostgreSQL Database
Your instance will use an SSL connection to connect to the DBaaS host.
The example below connects to the DBaaS host, as **user01** and uses the database **dbinstance** via an SSL connection.

```bash
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

The SSL connection is enforced and plain text connections fail.

## MariaDB/MySQL Database
Your instance will use an SSL connection to connect to the DBaaS host.
The example below connects to the DBaaS host, as **user01** and uses the database **dbinstance** via an SSL connection.

```bash
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

```bash
mysql -h dbaas101.arbutus.cloud.computecanada.ca -u user01 -p dbinstance
Enter password: 
ERROR 1045 (28000): Access denied for user 'user01'@'client.arbutus' (using password: YES)