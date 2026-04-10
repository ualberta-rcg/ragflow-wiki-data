---
title: "Accessing the Arbutus object storage with AWS CLI/fr"
tags:
  - cloud

keywords:
  - configuration
  - stockage objet
  - installation
  - AWS CLI
  - Arbutus
---

Cette page contient les renseignements sur la configuration et l'accès au [stockage objet sur Arbutus](arbutus-object-storage-fr.md) avec AWS CLI, l'un des [clients pour le stockage de ce type](arbutus_object_storage_clients-fr.md).

En comparaison des autres clients utilisés pour le stockage objet, AWS CLI offre un meilleur support pour les grands fichiers (>5Go) en plus de la commande `sync` qui est très utile. Notez cependant que nous n'avons pas testé toutes les fonctionnalités.

<span id="Installing_AWS_CLI"></span>
## Installation 

<pre>
pip install awscli awscli-plugin-endpoint
</pre>

<span id="Configuring_AWS_CLI"></span>
## Configuration  

Générez l'ID de la clé d'accès et la clé secrète.

<pre>
openstack ec2 credentials create
</pre>

Modifiez ou créez `~/.aws/credentials` et ajoutez les renseignements qui viennent d'être générés.

<pre>
[default]
aws_access_key_id = <access_key>
aws_secret_access_key = <secret_key>
</pre>

Modifiez `~/.aws/config` et ajoutez la configuration suivante&nbsp;:

<pre>
[plugins]
endpoint = awscli_plugin_endpoint

[profile default]
s3 =
  endpoint_url = https://object-arbutus.alliancecan.ca
  signature_version = s3v4
s3api =
  endpoint_url = https://object-arbutus.alliancecan.ca
</pre>

<span id="Using_AWS_CLI"></span>
## Utilisation 

<pre>
export AWS_PROFILE=default
aws s3 ls <container-name>
aws s3 sync local_directory s3://container-name/prefix
</pre>

Vous trouverez d'autres exemples d'utilisation de AWS CLI sur [ce site externe. ](https://docs.ovh.com/us/en/storage/getting_started_with_the_swift_S3_API/)