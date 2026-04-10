---
title: "Arbutus object storage/fr"
slug: "arbutus_object_storage"
lang: "fr"

source_wiki_title: "Arbutus object storage/fr"
source_hash: "adaa450b7724e6ebbef06ba1cc8702a9"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T04:37:40.679206+00:00"

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

## Introduction

L'entreposage d'objets est une installation de stockage plus simple qu'un système de fichiers hiérarchique normal, mais qui permet d'éviter certains goulots d'étranglement de la performance. Les objets peuvent être créés, remplacés ou supprimés, mais ne peuvent pas être modifiés sur place, comme c'est le cas avec le stockage traditionnel. Ce type de stockage est devenu très populaire en raison de sa capacité de gérer plusieurs fichiers et des fichiers de grande taille, ainsi que l'existence de nombreux outils compatibles.

Un objet est un fichier dans un espace de nommage (*namespace*) plat : un objet peut être créé ou téléchargé dans son ensemble, mais vous ne pouvez pas modifier les octets qu’il contient. Un objet utilise la nomenclature bucket:tag sans qu’il soit imbriqué davantage. Puisque les opérations sur les *buckets* concernent l’entièreté d’un fichier, le fournisseur peut utiliser une représentation interne plus simple. L’espace de nommage plat permet au fournisseur d’éviter les goulots d’étranglement des métadonnées; on peut dire que c’est une sorte de stockage de clés et de valeurs.

La meilleure façon d’utiliser l'entreposage d'objets est de stocker et d’exporter des éléments qui ne sont pas nommés dans une structure hiérarchique; auxquels on accède principalement de manière totale et en lecture seule; et pour lesquels les règles d’accès et de contrôle sont simples. Nous recommandons son utilisation avec des plateformes ou des logiciels qui sont conçus pour travailler avec des données qui *vivent* dans un espace d’entreposage d’objets.

Sur Arbutus, chaque projet dispose par défaut de 1 To d’entreposage d’objets. Si ceci est insuffisant, vous pouvez soit utiliser notre [service d'accès rapide](https://alliancecan.ca/fr/services/calcul-informatique-de-pointe/acces-aux-ressources/service-dacces-rapide). Si vous avez besoin de plus de 10 To, présentez une demande au prochain [concours pour l'allocation des ressources](https://alliancecan.ca/fr/services/calcul-informatique-de-pointe/acces-aux-ressources/concours-pour-lallocation-de-ressources).

Contrairement à un environnement de calcul sur une grappe, les fonctions d'administration du système pour l'entreposage d’objets d'un utilisateur sont la responsabilité de cet utilisateur, ce qui signifie que les opérations comme [la sauvegarde](backing-up-your-vm.md) doivent être effectuées par l'utilisateur. Pour plus d'information, voyez [Options d'entreposage infonuagique](cloud-storage-options.md).

Nous offrons deux protocoles différents pour accéder à l'entreposage d'objets dans OpenStack : Swift et Amazon Simple Storage Service (S3).

Ces protocoles se ressemblent beaucoup et sont interchangeables dans la plupart des cas. Il n’est pas nécessaire de vous en tenir toujours au même protocole puisque les conteneurs ou compartiments (*buckets*) et les objets sont accessibles par les protocoles Swift et S3. Certaines différences existent toutefois dans le contexte de l'entreposage d’objets sur Arbutus.

Swift est le protocole par défaut et est le plus simple à utiliser; vous n’avez pas à gérer les identifiants puisque l’accès se fait avec votre compte Arbutus. Par contre, Swift n’offre pas toutes les fonctionnalités de S3. Le principal cas d'usage est que vous devez utiliser S3 pour gérer vos conteneurs avec des politiques d'accès parce que Swift ne prend pas en charge ces politiques. De plus, S3 vous permet de créer et de gérer vos propres clés, ce qui peut être nécessaire si par exemple vous voulez créer un compte en lecture seule pour une application en particulier. Consultez la [liste des compatibilités dans S3/Swift REST API Comparison Matrix](https://docs.openstack.org/swift/latest/s3_compat.html).

## Accès et gestion de l'entreposage d'objets

Pour gérer l'entreposage d'objets, vous avez besoin de votre propre identifiant ainsi que de la clé secrète pour accéder au stockage. Générez-les avec votre ID d'accès S3 et la clé secrète pour le protocole avec le [client de ligne de commande OpenStack](openstack-command-line-clients.md).

```bash
openstack ec2 credentials create
```

### Accès à l'entreposage d'objets

Les politiques d'accès ne peuvent pas se faire via un navigateur web, mais par [un client compatible SWIFT ou S3](arbutus-object-storage-clients.md). L'accès aux conteneurs de données peut se faire de plusieurs façons :

1.  [via un client compatible avec S3](arbutus-object-storage-clients.md) (par exemple s3cmd);
2.  [via Globus](globus.md#entreposage-dobjet-sur-arbutus);
3.  via un point HTTPS dans un navigateur, pourvu que vos politiques soient configurées comme étant publiques et non par défaut.

```bash
https://object-arbutus.alliancecan.ca/PROJECT_ID:DATA_CONTAINER/FILENAME
```

## Gestion de l'entreposage d'objets sur Arbutus

La manière recommandée de gérer les conteneurs et les objets dans le **Stockage d'Objet** d'Arbutus est d'utiliser l'outil `s3cmd`, qui est disponible sous Linux.
Notre documentation fournit des instructions spécifiques sur la [configuration et la gestion des accès](accessing-object-storage-with-s3cmd.md) avec le client `s3cmd`.
Il est également possible d'utiliser d'autres [clients compatibles S3](arbutus-object-storage-clients.md) qui sont également compatibles avec l'entreposage d’objets d'Arbutus.

De plus, nous pouvons effectuer certaines tâches de gestion pour notre entreposage d'objets en utilisant la section [Conteneurs](https://arbutus.cloud.computecanada.ca/project/containers) sous l'onglet **Stockage d'Objet** dans le [Tableau de bord OpenStack d'Arbutus](https://arbutus.cloud.computecanada.ca).

Cette interface fait référence aux *conteneurs de données*, également appelés *buckets* dans d'autres systèmes d'entreposage d'objets.

En utilisant le tableau de bord, nous pouvons créer de nouveaux conteneurs de données, téléverser des fichiers et créer des dossiers. Nous pouvons également créer des conteneurs de données en utilisant un [client compatible S3](arbutus-object-storage-clients.md).

!!! note
    Veuillez noter que les conteneurs de données appartiennent à l'utilisateur qui les crée et ne peuvent pas être manipulés par d'autres utilisateurs.
    Par conséquent, vous êtes responsable de la gestion de vos conteneurs de données et de leur contenu au sein de votre projet d'infonuagique.

Si vous créez un nouveau conteneur **public**, n'importe qui sur Internet peut lire son contenu en naviguant simplement à l'adresse suivante

```
https://object-arbutus.alliancecan.ca/<OPENSTACK PROJECT ID>:<NOM DE VOTRE CONTENEUR>/<NOM DE VOTRE OBJET>
```

avec vos noms de conteneurs et d'objets insérés au bon endroit.

Pour rendre un conteneur de données accessible au public, nous pouvons modifier sa politique pour autoriser l'accès public. Cela peut s'avérer pratique si nous avons à partager des fichiers avec une audience élargie. Nous pouvons gérer les politiques de conteneur avec des fichiers JSON, nous permettant de spécifier divers contrôles d'accès pour nos conteneurs et objets.

### Gestion des politiques de conteneurs de données (buckets) pour l'entreposage d'objets sur Arbutus

!!! warning "Attention"
    Faites bien attention aux politiques, car une politique mal conçue peut vous empêcher d'accéder à votre conteneur de données.

Présentement, le [Stockage d'Objet](https://arbutus.cloud.computecanada.ca/project/containers) d'Arbutus implémente seulement un sous-ensemble de la spécification AWS pour les [politiques de conteneurs de données](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-iam-policies.html). L'exemple suivant montre comment créer, appliquer et visualiser une politique. La première étape consiste à créer un fichier JSON de politique.

```json
{
    "Version": "2012-10-17",
    "Id": "S3PolicyId1",
    "Statement": [
        {
            "Sid": "IPAllow",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::testbucket",
                "arn:aws:s3:::testbucket/*"
            ],
            "Condition": {
                "NotIpAddress": {
                    "aws:SourceIp": "206.12.0.0/16",
                    "aws:SourceIp": "142.104.0.0/16"
                }
            }
        }
    ]
}
```

Cet exemple refuse l'accès sauf à partir des plages d'adresses IP sources spécifiées en notation [CIDR (Classless Inter-Domain Routing)](https://fr.wikipedia.org/wiki/Adresse_IP#Agr%C3%A9gation_des_adresses). Dans cet exemple, le `s3://testbucket` est limité à la plage d'adresses IP publiques (206.12.0.0/16) utilisée par le nuage Arbutus et à la plage d'adresses IP publiques (142.104.0.0/16) utilisée par l'Université de Victoria.

Une fois que vous avez votre fichier de politique, vous pouvez l'appliquer à votre conteneur de données :

```bash
s3cmd setpolicy testbucket.policy s3://testbucket
```

Pour voir la politique, vous pouvez utiliser la commande suivante :

```bash
s3cmd info s3://testbucket
```

### Sous-ensemble

En date de septembre 2023, nous supportons les actions suivantes :

*   s3:GetObject
*   s3:GetObjectVersion
*   s3:PutObject
*   s3:GetObjectAcl
*   s3:GetObjectVersionAcl
*   s3:PutObjectAcl
*   s3:PutObjectVersionAcl
*   s3:DeleteObject
*   s3:DeleteObjectVersion
*   s3:ListMultipartUploadParts
*   s3:AbortMultipartUpload
*   s3:GetObjectTorrent
*   s3:GetObjectVersionTorrent
*   s3:RestoreObject
*   s3:CreateBucket
*   s3:DeleteBucket
*   s3:ListBucket
*   s3:ListBucketVersions
*   s3:ListAllMyBuckets
*   s3:ListBucketMultipartUploads
*   s3:GetAccelerateConfiguration
*   s3:PutAccelerateConfiguration
*   s3:GetBucketAcl
*   s3:PutBucketAcl
*   s3:GetBucketCORS
*   s3:PutBucketCORS
*   s3:GetBucketVersioning
*   s3:PutBucketVersioning
*   s3:GetBucketRequestPayment
*   s3:PutBucketRequestPayment
*   s3:GetBucketLocation
*   s3:GetBucketPolicy
*   s3:DeleteBucketPolicy
*   s3:PutBucketPolicy
*   s3:GetBucketNotification
*   s3:PutBucketNotification
*   s3:GetBucketLogging
*   s3:PutBucketLogging
*   s3:GetBucketTagging
*   s3:PutBucketTagging
*   s3:GetBucketWebsite
*   s3:PutBucketWebsite
*   s3:DeleteBucketWebsite
*   s3:GetLifecycleConfiguration
*   s3:PutLifecycleConfiguration
*   s3:PutReplicationConfiguration
*   s3:GetReplicationConfiguration
*   s3:DeleteReplicationConfiguration
*   s3:GetObjectTagging
*   s3:PutObjectTagging
*   s3:DeleteObjectTagging
*   s3:GetObjectVersionTagging
*   s3:PutObjectVersionTagging
*   s3:DeleteObjectVersionTagging
*   s3:PutBucketObjectLockConfiguration
*   s3:GetBucketObjectLockConfiguration
*   s3:PutObjectRetention
*   s3:GetObjectRetention
*   s3:PutObjectLegalHold
*   s3:GetObjectLegalHold
*   s3:BypassGovernanceRetention
*   s3:GetBucketPolicyStatus
*   s3:PutPublicAccessBlock
*   s3:GetPublicAccessBlock
*   s3:DeletePublicAccessBlock
*   s3:GetBucketPublicAccessBlock
*   s3:PutBucketPublicAccessBlock
*   s3:DeleteBucketPublicAccessBlock
*   s3:GetBucketEncryption
*   s3:PutBucketEncryption