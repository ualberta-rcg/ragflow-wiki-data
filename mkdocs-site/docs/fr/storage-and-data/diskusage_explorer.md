---
title: "Diskusage Explorer/fr"
slug: "diskusage_explorer"
lang: "fr"

source_wiki_title: "Diskusage Explorer/fr"
source_hash: "2a1f00aaf3f1c9ff844cee49e6f43887"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T06:10:12.703407+00:00"

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

## Contenu des répertoires

!!! attention
    Pour l'instant, cet outil est seulement disponible sur [Narval](narval.md).

L'outil Diskusage Explorer vous permet d'obtenir le détail de l'utilisation de l'espace dans vos répertoires `/home`, `/scratch` et `/project`. Cette information est mise à jour quotidiennement et est triée selon un format [SQLite](sqlite.md) pour un accès rapide.

Dans notre exemple, nous verrons la consommation de l'espace disque du répertoire `def-professor` dans `/project`.

### Interface ncurse

Sélectionnez un espace `/project` auquel vous avez accès et que vous voulez analyser; dans notre exemple, nous analysons `def-professor`.

```bash
diskusage_explorer /project/def-professor
```

Cette commande charge un navigateur qui montre les ressources consommées par tous les fichiers dans l'arborescence d'un répertoire.

Entrez `c` pour alterner entre l'espace disque consommé et le nombre de fichiers, `q` ou `<esc>` pour quitter et `h` pour l'aide.

Pour ne consulter qu'un sous-répertoire de cet espace `/project` sans avoir à naviguer dans toute l'arborescence, utilisez

```bash
diskusage_explorer /project/def-professor/subdirectory/
```

La commande `man duc` affiche une page du manuel.

### Interface graphique

Si le nœud de connexion est particulièrement occupé ou si vous avez un trop grand nombre de fichiers dans votre espace `/project`, l'affichage peut être lent et irrégulier. Pour de meilleurs résultats, voyez comment utiliser `diskusage_explorer` sur votre propre ordinateur.

Nous recommandons d'utiliser le mode texte ncurse standard sur nos nœuds de connexion, mais `diskusage_explorer` inclut aussi une belle interface graphique.

Assurez-vous d'abord que votre connexion [SSH](ssh.md) fait en sorte que l'affichage des applications d'interfaces se fait correctement. Vous pouvez alors utiliser une interface graphique avec la commande

```bash
duc gui -d /project/.duc_databases/def-professor.sqlite  /project/def-professor
```

Vous pouvez naviguer avec la souris et aussi utiliser `c` pour alterner entre la taille des fichiers et le nombre de fichiers.

### Naviguer plus rapidement sur votre ordinateur

[Installez d'abord le logiciel diskusage_explorer](http://duc.zevv.nl/#download) sur votre ordinateur local puis, toujours sur votre ordinateur local, téléchargez le fichier SQLite de votre grappe et lancez `duc`.

```bash
rsync -v --progress username@beluga.calculcanada.ca:/project/.duc_databases/def-professor.sqlite  .
duc gui -d ./def-professor.sqlite  /project/def-professor
```

Vous pourrez ainsi naviguer de manière plus agréable.