---
title: "Accessing object storage with s3cmd/fr"
tags:
  - cloud

keywords:
  - s3cmd
  - BUCKET_NAME
  - bucket
  - Téléversement de fichiers
  - type MIME
  - configuration
  - création de buckets
  - stockage objet
  - listes de contrôle d'accès
  - ACL
  - Arbutus
---

Cette page contient les renseignements sur la configuration et l'accès au [stockage objet sur Arbutus](arbutus-object-storage-fr.md) avec s3cmd, l'un des [clients pour le stockage de ce type](arbutus_object_storage_clients-fr.md).

## Installation 
Dépendant de votre distribution Linux, la commande `s3cmd` est installée avec `yum` (RHEL, CentOS) ou `apt` (Debian, Ubuntu).

`$ sudo yum install s3cmd`

`$ sudo apt install s3cmd `

<span id="Configuring_s3cmd"></span>
## Configuration  

Pour configurer l’outil `s3cmd`, lancez la commande</br>
`$ s3cmd --configure`

Effectuez les configurations suivantes avec les clés qui vous ont été fournies ou qui ont été créées avec la commande `openstack ec2 credentials create`&nbsp;:
<pre>
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
</pre>

Ceci devrait produire un fichier de configuration comme celui ci-dessous où vous spécifierez les valeurs de vos propres clés.  Utilisez les autres options de configuration selon votre cas particulier.

<pre>[default]
access_key = <redacted>
check_ssl_certificate = True
check_ssl_hostname = True
host_base = object-arbutus.alliancecan.ca
host_bucket = object-arbutus.alliancecan.ca
secret_key = <redacted>
use_https = True
</pre>

## Création de buckets 
Les buckets contiennent des fichiers et un nom de bucket doit être unique dans toute la solution de stockage objet sur Arbutus. Vous devez donc créer un bucket avec un nom unique pour éviter les conflits avec les autres utilisateurs. Par exemple, les buckets 
`s3://test/` et `s3://data/` existent probablement déjà. Utilisez plutôt des noms reliés à votre projet, par exemple `s3://def-test-bucket1` ou `s3://atlas_project_bucket`. Les caractrères valides pour un nom de bucket sont les lettres majuscules, les lettres minuscules, les chiffres, le point, le trait d'union et la barre de soulignement (A-Z, a-z, 0-9, ., -, et _ ).

Pour créer un bucket, utilisez la commande `mb` (<i>make bucket</i>).

`$ s3cmd mb s3://BUCKET_NAME/`

Pour connaître l'état d'un bucket, lancez la commande

`$ s3cmd info s3://BUCKET_NAME/`

Le résultat sera semblable à ceci :

<pre>
s3://BUCKET_NAME/ (bucket):
   Location:  default
   Payer:     BucketOwner
   Expiration Rule: none
   Policy:    none
   CORS:      none
   ACL:       *anon*: READ
   ACL:       USER: FULL_CONTROL
   URL:       http://object-arbutus.alliancecan.ca/BUCKET_NAME/
</pre>

## Téléversement de fichiers 
Pour téléverser un fichier dans un bucket, lancez

`$ s3cmd put --guess-mime-type FILE_NAME.dat s3://BUCKET_NAME/FILE_NAME.dat`

où le nom du bucket et le nom du fichier sont indiqués. Le mécanisme MIME (<i>Multipurpose Internet Mail Extensions</i>) gère les fichiers selon leur type. Le paramètre `--guess-mime-type` détecte le type MIME d'après l'extension du fichier. Par défaut, le type MIME est `binary/octet-stream`.

## Supprimer un  fichier 
Pour supprimer un fichier dans un bucket, lancez

`$ s3cmd rm s3://BUCKET_NAME/FILE_NAME.dat`

## Listes de contrôle d’accès et politiques 
Il est possible d’associer des listes de contrôle d’accès (ACL) et des politiques à un bucket pour indiquer qui peut avoir accès à une ressource particulière de l'espace de stockage objet. Ces fonctionnalités sont très avancées. Voici deux exemples simples d’utilisation de ACL avec la commande `setacl`.

`$ s3cmd setacl --acl-public -r s3://BUCKET_NAME/`

Par cette commande, le public peut avoir accès au bucket et, de manière récursive (-r), à chaque fichier dans le bucket. L’accès aux fichiers peut se faire avec des URL comme

<code><nowiki>https://object-arbutus.alliancecan.ca/PROJECT_ID:BUCKET_NAME/FILE_NAME.dat</nowiki></code>

Avec la prochaine commande, le bucket est accessible uniquement par le propriétaire.

`$ s3cmd setacl --acl-private s3://BUCKET_NAME/`

Pour voir la configuration actuelle d'un bucket, utilisez la commande 

`$ s3cmd info s3://testbucket `

Pour d’autres exemples plus avancés, voir le   [site d’aide de s3cmd](https://www.s3express.com/help/help.html) ou la page man de s3cmd(1).

Voir la page [Stockage objet sur Arbutus](arbutus_object_storage-fr.md) pour des exemples et pour les  [directives sur la gestion des politiques des conteneurs](arbutus_object_storage-fr#managing_data_container_(bucket)_policies_for_your_arbutus_object_store.md).