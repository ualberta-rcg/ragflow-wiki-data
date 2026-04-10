---
title: "Accessing object storage with s3cmd/fr"
slug: "accessing_object_storage_with_s3cmd"
lang: "fr"

source_wiki_title: "Accessing object storage with s3cmd/fr"
source_hash: "9c05c25e0783fe242f8351992128df7f"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T01:50:37.038806+00:00"

tags:
  - cloud

keywords:
  - "s3cmd"
  - "BUCKET_NAME"
  - "bucket"
  - "Téléversement de fichiers"
  - "type MIME"
  - "configuration"
  - "création de buckets"
  - "stockage objet"
  - "listes de contrôle d'accès"
  - "ACL"
  - "Arbutus"

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

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: true
---

Cette page contient les renseignements sur la configuration et l'accès au [stockage objet sur Arbutus](arbutus-object-storage.md) avec s3cmd, l'un des [clients pour ce type de stockage](arbutus-object-storage-clients.md).

## Installation

Selon votre distribution Linux, l'outil `s3cmd` s'installe avec `yum` (RHEL, CentOS) ou `apt` (Debian, Ubuntu).

```bash
sudo yum install s3cmd
```

```bash
sudo apt install s3cmd
```

## Configuration

Pour configurer l'outil `s3cmd`, lancez la commande :

```bash
s3cmd --configure
```

Effectuez les configurations suivantes avec les clés qui vous ont été fournies ou qui ont été créées avec la commande `openstack ec2 credentials create` :

```console
Entrez les nouvelles valeurs ou acceptez les valeurs par défaut entre crochets en appuyant sur Entrée.
Consultez le manuel de l'utilisateur pour une description détaillée de toutes les options.

La clé d'accès et la clé secrète sont vos identifiants pour Amazon S3. Laissez-les vides pour utiliser les variables d'environnement.
Clé d'accès []: CLÉ_D'ACCÈS_À_20_CHIFFRES
Clé secrète []: CLÉ_SECRÈTE_À_40_CHIFFRES
Région par défaut [US] :

Utilisez "s3.amazonaws.com" pour le point d'accès S3 et ne le modifiez pas pour cibler Amazon S3.
Point d'accès S3 []: object-arbutus.alliancecan.ca

Utilisez "%(bucket)s.s3.amazonaws.com" pour cibler Amazon S3. Les variables "%(bucket)s" et "%(location)s" peuvent être utilisées
si le système S3 cible prend en charge les conteneurs basés sur DNS.
Modèle d'hôte : port de style DNS pour l'accès aux conteneurs []: object-arbutus.alliancecan.ca

Le mot de passe de chiffrement est utilisé pour protéger vos fichiers de la lecture
par des personnes non autorisées pendant le transfert vers S3
Mot de passe de chiffrement []:
Chemin du programme GPG [/usr/bin/gpg] :

Lorsque vous utilisez le protocole HTTPS sécurisé, toutes les communications avec les serveurs Amazon S3
sont protégées de l'écoute de tiers. Cette méthode est
plus lente que le HTTP simple, et ne peut être proxifiée qu'avec Python 2.7 ou une version plus récente
Utiliser le protocole HTTPS []: Oui

Sur certains réseaux, tout accès à Internet doit passer par un proxy HTTP.
Essayez de le configurer ici si vous ne pouvez pas vous connecter directement à S3
Nom du serveur proxy HTTP :
```

Ceci devrait produire un fichier de configuration comme celui ci-dessous, où vous spécifierez les valeurs de vos propres clés. Utilisez les autres options de configuration selon votre cas particulier.

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

## Création de buckets

Les conteneurs (buckets) contiennent des fichiers, et leur nom doit être unique dans toute la solution de stockage objet sur Arbutus. Vous devez donc créer un conteneur avec un nom unique pour éviter les conflits avec les autres utilisateurs. Par exemple, les conteneurs `s3://test/` et `s3://data/` existent probablement déjà. Utilisez plutôt des noms reliés à votre projet, par exemple `s3://def-test-bucket1` ou `s3://atlas_project_bucket`. Les caractères valides pour un nom de conteneur sont les lettres majuscules, les lettres minuscules, les chiffres, le point, le trait d'union et la barre de soulignement (A-Z, a-z, 0-9, ., -, et _ ).

Pour créer un conteneur, utilisez la commande `mb` (*make bucket*).

```bash
s3cmd mb s3://NOM_DU_CONTENEUR/
```

Pour connaître l'état d'un conteneur, lancez la commande :

```bash
s3cmd info s3://NOM_DU_CONTENEUR/
```

Le résultat sera semblable à ceci :

```console
s3://NOM_DU_CONTENEUR/ (conteneur) :
   Emplacement : par défaut
   Payeur : Propriétaire du conteneur
   Règle d'expiration : aucune
   Politique : aucune
   CORS : aucune
   ACL : *anon* : LECTURE
   ACL : UTILISATEUR : CONTRÔLE_TOTAL
   URL : http://object-arbutus.alliancecan.ca/NOM_DU_CONTENEUR/
```

## Téléversement de fichiers

Pour téléverser un fichier dans un conteneur, lancez :

```bash
s3cmd put --guess-mime-type NOM_FICHIER.dat s3://NOM_DU_CONTENEUR/NOM_FICHIER.dat
```

où le nom du conteneur et le nom du fichier sont indiqués. Le mécanisme MIME (*Multipurpose Internet Mail Extensions*) gère les fichiers selon leur type. Le paramètre `--guess-mime-type` détecte le type MIME d'après l'extension du fichier. Par défaut, le type MIME est `binary/octet-stream`.

## Supprimer un fichier

Pour supprimer un fichier dans un conteneur, lancez :

```bash
s3cmd rm s3://NOM_DU_CONTENEUR/NOM_FICHIER.dat
```

## Listes de contrôle d'accès et politiques

Il est possible d'associer des listes de contrôle d'accès (ACL) et des politiques à un conteneur pour indiquer qui peut avoir accès à une ressource particulière de l'espace de stockage objet. Ces fonctionnalités sont très avancées. Voici deux exemples simples d'utilisation des ACL avec la commande `setacl`.

```bash
s3cmd setacl --acl-public -r s3://NOM_DU_CONTENEUR/
```

Par cette commande, le public peut avoir accès au conteneur et, de manière récursive (-r), à chaque fichier qu'il contient. L'accès aux fichiers peut se faire avec des URL comme :
`https://object-arbutus.alliancecan.ca/ID_PROJET:NOM_DU_CONTENEUR/NOM_FICHIER.dat`

Avec la commande suivante, le conteneur est accessible uniquement par son propriétaire.

```bash
s3cmd setacl --acl-private s3://NOM_DU_CONTENEUR/
```

Pour voir la configuration actuelle d'un conteneur, utilisez la commande :

```bash
s3cmd info s3://conteneurtest
```

Pour d'autres exemples plus avancés, voir le [site d'aide de s3cmd](https://www.s3express.com/help/help.html) ou la page man de s3cmd(1).

Voir la page [Stockage objet sur Arbutus](arbutus-object-storage.md) pour des exemples et pour les [directives sur la gestion des politiques des conteneurs](arbutus-object-storage.md#gestion-des-politiques-de-conteneurs-pour-le-stockage-objet-arbutus).