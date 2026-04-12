---
title: "Transferring files with Aspera Connect/ascp/fr"
slug: "transferring_files_with_aspera_connect_ascp"
lang: "fr"

source_wiki_title: "Transferring files with Aspera Connect/ascp/fr"
source_hash: "90f46c6d6b5970fc99e54618c5312346"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:02:44.354221+00:00"

tags:
  []

keywords:
  - "transfert de données"
  - "ascp"
  - "installation locale"
  - "serveurs de transfert"
  - "Aspera Connect"

questions:
  - "À quoi sert le logiciel ascp (ou Aspera Connect) ?"
  - "Quelle erreur peut survenir si la version d'ascp utilisée est incompatible avec le serveur de destination ?"
  - "Quelles sont les étapes à suivre pour installer localement la version la plus récente d'Aspera Connect sous Linux ?"
  - "À quoi sert le logiciel ascp (ou Aspera Connect) ?"
  - "Quelle erreur peut survenir si la version d'ascp utilisée est incompatible avec le serveur de destination ?"
  - "Quelles sont les étapes à suivre pour installer localement la version la plus récente d'Aspera Connect sous Linux ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

ascp est un logiciel utilisé pour transférer des données en provenance et à destination de serveurs de transfert Aspera sur lesquels vous détenez une licence, par exemple pour téléverser un jeu de données dans un dépôt de données.

Plusieurs serveurs de transfert exigent une version à jour du logiciel, appelé maintenant Aspera Connect. En raison de certaines modifications qui y ont été apportées, vous devrez peut-être installer localement la plus récente version.

## ascp 3.5.4

Dans les piles logicielles moins récentes, ce logiciel est disponible via un module.

!!! warning "Incompatibilité de version"
    Si le serveur de destination est incompatible avec cette version, vous pourriez obtenir une erreur similaire à celle-ci :

    ```text
    Error with Aspera:

    ascp: failed to authenticate, exiting.

    Session Stop  (Error: failed to authenticate)
    ```

## Aspera Connect/ascp 4+

Pour utiliser Aspera Connect (auparavant nommé *ascp*), vous devez [l'installer dans un de vos répertoires locaux](../getting-started/installing_software_in_your_home_directory.md).

1.  Copiez le lien de la version la plus récente pour Linux à partir du [site web d'Aspera Connect](https://www.ibm.com/aspera/connect).
2.  Rendez-vous dans le répertoire où vous souhaitez installer le logiciel, par exemple votre répertoire personnel (`/home`).
3.  Téléchargez le logiciel dans ce répertoire à l'aide de `wget`.

    ```bash
    wget link-i-copied-here
    ```

4.  Extrayez le logiciel de l'archive.

    ```bash
    tar -zxf ibm-aspera-connect_some_version_linux.tar.gz
    ```

5.  Lancez le script d'installation.

    ```bash
    bash ibm-aspera-connect_some_version_linux.sh
    ```

5a. Rendez les fichiers de la bibliothèque exécutables.

    ```bash
    chmod u+x ~/.aspera/connect/plugins/*/*.so ~/.aspera/connect/lib/*
    ```

6.  Lancez le script `setrpaths`.

    ```bash
    setrpaths.sh --path $HOME/.aspera
    ```

7.  (Optionnel) Ajoutez les exécutables d'ascp à votre chemin (`PATH`).

    ```bash
    export PATH=~/.aspera/connect/bin:$PATH