---
title: "Accessing the Arbutus object storage with AWS CLI/fr"
slug: "accessing_the_arbutus_object_storage_with_aws_cli"
lang: "fr"

source_wiki_title: "Accessing the Arbutus object storage with AWS CLI/fr"
source_hash: "975f8fd72303e0116c85b2f8ac32dc85"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T01:51:11.219191+00:00"

tags:
  - cloud

keywords:
  - "configuration"
  - "stockage objet"
  - "installation"
  - "AWS CLI"
  - "Arbutus"

questions:
  - "Quels sont les avantages d'utiliser AWS CLI pour le stockage objet sur Arbutus par rapport aux autres clients ?"
  - "Comment doit-on générer et configurer les clés d'accès pour lier AWS CLI au stockage Arbutus ?"
  - "Quelles sont les commandes de base présentées pour lister et synchroniser des fichiers une fois l'outil installé ?"
  - "Quels sont les avantages d'utiliser AWS CLI pour le stockage objet sur Arbutus par rapport aux autres clients ?"
  - "Comment doit-on générer et configurer les clés d'accès pour lier AWS CLI au stockage Arbutus ?"
  - "Quelles sont les commandes de base présentées pour lister et synchroniser des fichiers une fois l'outil installé ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: true
---

Cette page contient les renseignements sur la configuration et l'accès au [stockage objet sur Arbutus](arbutus-object-storage.md) avec AWS CLI, l'un des [clients pour le stockage de ce type](arbutus-object-storage-clients.md).

!!! note "Considérations sur AWS CLI"
    En comparaison des autres clients utilisés pour le stockage objet, AWS CLI offre un meilleur support pour les gros fichiers (>5Go) en plus de la commande `sync` qui est très utile. Notez cependant que nous n'avons pas testé toutes les fonctionnalités.

## Installation

```bash
pip install awscli awscli-plugin-endpoint
```

## Configuration

Générez l'ID de la clé d'accès et la clé secrète.

```bash
openstack ec2 credentials create
```

Modifiez ou créez `~/.aws/credentials` et ajoutez les renseignements qui viennent d'être générés.

```ini
[default]
aws_access_key_id = <access_key>
aws_secret_access_key = <secret_key>
```

Modifiez `~/.aws/config` et ajoutez la configuration suivante :

```ini
[plugins]
endpoint = awscli_plugin_endpoint

[profile default]
s3 =
  endpoint_url = https://object-arbutus.alliancecan.ca
  signature_version = s3v4
s3api =
  endpoint_url = https://object-arbutus.alliancecan.ca
```

## Utilisation

```bash
export AWS_PROFILE=default
aws s3 ls <nom-du-conteneur>
aws s3 sync répertoire_local s3://nom-du-conteneur/préfixe
```

Vous trouverez d'autres exemples d'utilisation de AWS CLI sur [ce site externe](https://docs.ovh.com/us/en/storage/getting_started_with_the_swift_S3_API/).