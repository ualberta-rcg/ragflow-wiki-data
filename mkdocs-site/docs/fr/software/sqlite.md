---
title: "SQLite/fr"
slug: "sqlite"
lang: "fr"

source_wiki_title: "SQLite/fr"
source_hash: "4f291c96b3f3e539a012fbb4dc2fc1c3"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:12:22.353180+00:00"

tags:
  []

keywords:
  - "requêtes SQL"
  - "SQLite"
  - "base de données"
  - "architecture client-serveur"
  - "fichier disque"

questions:
  - "Quelles sont les caractéristiques principales de SQLite et comment se différencie-t-il des bases de données relationnelles à architecture client-serveur ?"
  - "Quelles sont les bonnes pratiques et les précautions à prendre concernant l'emplacement des fichiers SQLite et l'écriture simultanée par plusieurs processus ?"
  - "Quelles sont les limites de SQLite en termes de taille et de complexité qui justifieraient la transition vers un système de gestion de base de données plus sophistiqué ?"
  - "Quelles sont les caractéristiques principales de SQLite et comment se différencie-t-il des bases de données relationnelles à architecture client-serveur ?"
  - "Quelles sont les bonnes pratiques et les précautions à prendre concernant l'emplacement des fichiers SQLite et l'écriture simultanée par plusieurs processus ?"
  - "Quelles sont les limites de SQLite en termes de taille et de complexité qui justifieraient la transition vers un système de gestion de base de données plus sophistiqué ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[SQLite](https://www.sqlite.org) est un moteur de bases de données pour construire des BD dites *de poche*, car elles offrent toutes les fonctionnalités des BD relationnelles sans l'architecture client-serveur, avec en plus l'avantage que toutes les données résident sur un seul fichier disque qui peut être copié sur un autre ordinateur. Des applications écrites dans plusieurs langages bien connus peuvent lire et écrire dans un fichier SQLite par des requêtes [SQL](https://fr.wikipedia.org/wiki/Structured_Query_Language) standard via leur API d'interaction avec les BD.

!!! warning "Bonnes pratiques d'emplacement et d'écriture des fichiers SQLite"

    Les bases de données SQLite, comme toutes les autres, ne devraient pas être utilisées dans des systèmes de fichiers partagés comme /home, /scratch et /project. Au début d'une tâche, vous devriez en principe copier le fichier SQLite sur l'espace local `$SLURM_TMPDIR` où vous pourrez utiliser la base de données sans problème, tout en bénéficiant de la meilleure performance. Notez que SQLite ne prévoit pas l'emploi de plusieurs fils ou processus qui écrivent dans la base de données en même temps; pour ce faire, vous devriez utiliser une [solution client-serveur](database-servers.md).

## Utiliser SQLite directement

Vous pouvez aussi accéder directement à une base de données SQLite en utilisant le client natif.

```bash
sqlite3 foo.sqlite
```

Si le fichier `foo.sqlite` n'existe pas, SQLite le crée et ce client démarre dans une base de données vide. Autrement, vous êtes connecté à la base de données existante. Vous pouvez alors exécuter toutes les requêtes, par exemple lancer `SELECT * FROM tablename;` pour faire afficher à l'écran le contenu de `tablename`.

## Accéder à SQLite à partir d'une application

Le moyen habituel d'interagir avec une BD SQLite (ou toute autre) est d'utiliser des appels de fonctions pour établir la connexion; exécuter les requêtes de lecture, d'écriture ou de mise à jour des données; et fermer la connexion pour que les modifications soient enregistrées dans le fichier disque SQLite. Dans l'exemple simple montré ci-dessous, nous supposons que la BD existe déjà et qu'elle contient la table `employee` de deux colonnes : la chaîne `name` et l'entier `age`.

=== "Python"

    ```python
    # Pour Python, on peut utiliser le module sqlite3, installé dans un environnement virtuel,
    # pour accéder à une base de données SQLite
    import sqlite3

    age = 34

    # Connexion à la base de données...
    dbase = sqlite3.connect("foo.sqlite")

    dbase.execute("INSERT INTO employee(name,age) VALUES(\"John Smith\"," + str(age) + ");")

    # Fermeture de la connexion à la base de données
    dbase.close()
    ```

=== "R"

    ```r
    # Avec R, la première étape est d'installer le paquet RSQLite dans votre environnement R,
    # après quoi vous pouvez utiliser un code similaire à ce qui suit pour interagir avec la base de données SQLite
    library(DBI)

    age <- 34

    # Connexion à la base de données...
    dbase <- dbConnect(RSQLite::SQLite(),"foo.sqlite")

    # Une requête paramétrée
    query <- paste(c("INSERT INTO employee(name,age) VALUES(\"John Smith\",",toString(age),");"),collapse='')
    dbExecute(dbase,query)

    # Fermeture de la connexion à la base de données
    dbDisconnect(dbase)
    ```

=== "C++"

    ```cpp
    #include <iostream>
    #include <string>
    #include <sqlite3.h>

    int main(int argc,char** argv)
    {
      int age = 34;
      std::string query;
      sqlite3* dbase;

      sqlite3_open("foo.sqlite",&dbase);

      query = "INSERT INTO employee(name,age) VALUES(\"John Smith\"," + std::to_string(age) + ");";
      sqlite3_exec(dbase,query.c_str(),nullptr,nullptr,nullptr);

      sqlite3_close(dbase);

      return 0;
    }
    ```

## Limites

Comme son nom le suggère, SQLite est facile d'utilisation et conçu pour les bases de données relativement simples dont la taille n’excède pas quelques centaines de Go et dont le [modèle entités-associations](https://fr.wikipedia.org/wiki/Mod%C3%A8le_entit%C3%A9-association) n'est pas trop complexe. Au fur et à mesure que la taille et la complexité de votre BD augmentent, vous pourriez remarquer une baisse de performance; si c’est le cas, il serait temps de trouver un [outil plus sophistiqué sur le modèle client-serveur](database-servers.md). Vous trouverez sur le site web SQLite des [critères de sélection entre SQLite et les SGBDR client-serveur](https://www.sqlite.org/whentouse.html).