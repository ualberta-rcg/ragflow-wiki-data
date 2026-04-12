---
title: "Accessing object storage with s3cmd/fr"
slug: "accessing_object_storage_with_s3cmd"
lang: "fr"

source_wiki_title: "Accessing object storage with s3cmd/fr"
source_hash: "9c05c25e0783fe242f8351992128df7f"
last_synced: "2026-04-10T14:10:18.226633+00:00"
last_processed: "2026-04-10T14:40:40.362528+00:00"

tags:
  - cloud

keywords:
  - "configuration"
  - "listes de contrôle d'accès"
  - "Téléversement de fichiers"
  - "ACL"
  - "Arbutus"
  - "type MIME"
  - "création de buckets"
  - "BUCKET_NAME"
  - "bucket"
  - "s3cmd"
  - "stockage objet"

questions:
  - "Comment installer et configurer l'outil s3cmd pour accéder au stockage objet sur Arbutus ?"
  - "Quelles sont les règles de nommage à respecter et la commande à utiliser pour créer un nouveau bucket ?"
  - "Quelle est la commande permettant de téléverser un fichier spécifique dans un bucket ?"
  - "Comment le mécanisme MIME détermine-t-il le type de fichier et quel est le type par défaut ?"
  - "Quelle commande permet de supprimer un fichier spécifique à l'intérieur d'un bucket ?"
  - "Comment configurer les listes de contrôle d'accès (ACL) pour rendre le contenu d'un bucket public ou privé ?"
  - "Quelles sont les permissions d'accès (ACL) actuellement configurées pour ce bucket ?"
  - "Quelle commande permet de téléverser un fichier dans le bucket tout en devinant son type MIME ?"
  - "Quelle est l'URL exacte permettant d'accéder aux objets stockés dans ce bucket ?"
  - "Comment le mécanisme MIME détermine-t-il le type de fichier et quel est le type par défaut ?"
  - "Quelle commande permet de supprimer un fichier spécifique à l'intérieur d'un bucket ?"
  - "Comment configurer les listes de contrôle d'accès (ACL) pour rendre le contenu d'un bucket public ou privé ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Cette page contient les renseignements sur la configuration et l'accès au [stockage objet sur Arbutus](arbutus_object_storage.md) avec s3cmd, l'un des [clients pour le stockage de ce type](arbutus_object_storage_clients.md).

## Installation
Dépendant de votre distribution Linux, la commande `s3cmd` est installée avec `yum` (RHEL, CentOS) ou `apt` (Debian, Ubuntu).

```bash
$ sudo yum install s3cmd
$ sudo apt install s3cmd
```

## Configuration

Pour configurer l’outil `s3cmd`, lancez la commande :
```bash
$ s3cmd --configure
```

Effectuez les configurations suivantes avec les clés qui vous ont été fournies ou qui ont été créées avec la commande `openstack ec2 credentials create` :

```text
Enter new values or accept defaults in brackets with Enter.
Refer to user manual for detailed description of all options.

Access key and Secret key are your identifiers for Amazon S3. Leave them empty for using the env variables.
Access Key []: 20_DIGIT_ACCESS_KEY
Secret Key []: 40_DIGIT_SECRET_KEY
Default Region [US]:

Use "s3.amazonaws.com" for S3 Endpoint and not modify it to the target Amazon S3.
S3 Endpoint []: object-arbutus.alliancecan.ca

Use "%(bucket)s.s3.amazonaws.com" to the target Amazon S3. "%(bucket)s" and "%(location)s" vars can be used
if the target S3 system supports dns based buckets.
DNS-style bucket+hostname:port template for accessing a bucket []: object-arbutus.alliancecan.ca

Encryption password is used to protect your files from reading
by unauthorized persons while in transfer to S3
Encryption password []:
Path to GPG program [/usr/bin/gpg]: 

When using secure HTTPS protocol all communication with Amazon S3
servers is protected from 3rd party eavesdropping. This method is
slower than plain HTTP, and can only be proxied with Python 2.7 or newer
Use HTTPS protocol []: Yes

On some networks all internet access must go through a HTTP proxy.
Try setting it here if you can't connect to S3 directly
HTTP Proxy server name:
```

Ceci devrait produire un fichier de configuration comme celui ci-dessous où vous spécifierez les valeurs de vos propres clés. Utilisez les autres options de configuration selon votre cas particulier.

```ini
[default]
access_key = <redacted>
check_ssl_certificate = True
check_ssl_hostname = True
host_base = object-arbutus.alliancecan.ca
host_bucket = object-arbutus.alliancecan.ca
secret_key = <redacted>
use_https = True
```

## Création de compartiments
Les compartiments contiennent des fichiers et un nom de compartiment doit être unique dans toute la solution de stockage objet sur Arbutus. Vous devez donc créer un compartiment avec un nom unique pour éviter les conflits avec les autres utilisateurs. Par exemple, les compartiments `s3://test/` et `s3://data/` existent probablement déjà. Utilisez plutôt des noms reliés à votre projet, par exemple `s3://def-test-bucket1` ou `s3://atlas_project_bucket`. Les caractères valides pour un nom de compartiment sont les lettres majuscules, les lettres minuscules, les chiffres, le point, le trait d'union et la barre de soulignement (A-Z, a-z, 0-9, ., -, et _ ).

Pour créer un compartiment, utilisez la commande `mb` (*make bucket*).

```bash
$ s3cmd mb s3://NOM_DU_COMPARTIMENT/
```

Pour connaître l'état d'un compartiment, lancez la commande :

```bash
$ s3cmd info s3://NOM_DU_COMPARTIMENT/
```

Le résultat sera semblable à ceci :

```text
s3://NOM_DU_COMPARTIMENT/ (compartiment):
   Localisation:  default
   Payeur:     PropriétaireDuCompartiment
   RègleD'expiration: aucune
   Politique:    aucune
   CORS:      aucune
   ACL:       *anon*: LECTURE
   ACL:       UTILISATEUR: CONTRÔLE_COMPLET
   URL:       http://object-arbutus.alliancecan.ca/NOM_DU_COMPARTIMENT/
```

## Téléversement de fichiers
Pour téléverser un fichier dans un compartiment, lancez :

```bash
$ s3cmd put --guess-mime-type NOM_DU_FICHIER.dat s3://NOM_DU_COMPARTIMENT/NOM_DU_FICHIER.dat
```

où le nom du compartiment et le nom du fichier sont indiqués. Le mécanisme MIME (*Multipurpose Internet Mail Extensions*) gère les fichiers selon leur type. Le paramètre `--guess-mime-type` détecte le type MIME d'après l'extension du fichier. Par défaut, le type MIME est `binary/octet-stream`.

## Suppression de fichiers
Pour supprimer un fichier dans un compartiment, lancez :
```bash
$ s3cmd rm s3://NOM_DU_COMPARTIMENT/NOM_DU_FICHIER.dat
```

## Listes de contrôle d’accès (ACL) et politiques
Il est possible d’associer des listes de contrôle d’accès (ACL) et des politiques à un compartiment pour indiquer qui peut avoir accès à une ressource particulière de l'espace de stockage objet. Ces fonctionnalités sont très avancées. Voici deux exemples simples d’utilisation d'ACL avec la commande `setacl`.

```bash
$ s3cmd setacl --acl-public -r s3://NOM_DU_COMPARTIMENT/
```

Par cette commande, le public peut avoir accès au compartiment et, de manière récursive (-r), à chaque fichier dans le compartiment. L’accès aux fichiers peut se faire avec des URL comme :
```text
https://object-arbutus.alliancecan.ca/ID_PROJET:NOM_DU_COMPARTIMENT/NOM_DU_FICHIER.dat
```

Avec la prochaine commande, le compartiment est accessible uniquement par le propriétaire.

```bash
$ s3cmd setacl --acl-private s3://NOM_DU_COMPARTIMENT/
```

Pour voir la configuration actuelle d'un compartiment, utilisez la commande :

```bash
$ s3cmd info s3://compartimentdetest
```

Pour d’autres exemples plus avancés, voir le [site d’aide de s3cmd](https://www.s3express.com/help/help.html) ou la page man de s3cmd(1).

Voir la page [Stockage objet sur Arbutus](arbutus_object_storage.md) pour des exemples et pour les [directives sur la gestion des politiques de conteneurs (compartiments) pour votre stockage objet Arbutus](arbutus_object_storage.md).