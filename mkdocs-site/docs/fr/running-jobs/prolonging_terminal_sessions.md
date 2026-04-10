---
title: "Prolonging terminal sessions/fr"
slug: "prolonging_terminal_sessions"
lang: "fr"

source_wiki_title: "Prolonging terminal sessions/fr"
source_hash: "270d9df932588aeae43a1497d6aa2f78"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T10:00:44.781814+00:00"

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

Pour soumettre et faire le suivi des tâches, modifier des fichiers et plusieurs autres opérations, vous aurez sans doute besoin de vous connecter à une grappe via [SSH](ssh.md). Il est parfois nécessaire de garder la connexion active pendant plusieurs heures, même plusieurs jours. Voici quelques techniques pour y arriver.

## Configuration de SSH

Une solution simple pour prolonger une connexion est de modifier la configuration de votre client SSH. Avec macOS et Linux, cette configuration se trouve dans `$HOME/.ssh/config` alors qu'avec Windows, elle est dans `C:\Users\<username>\.ssh\config`. Si le fichier n'existe pas, vous devez le créer et ajouter les lignes suivantes :

```
Host *
    ServerAliveInterval 240
```

Ceci transmet un signe de vie au serveur distant (comme une grappe de l'Alliance) toutes les 240 secondes (4 minutes), ce qui devrait garder la connexion active même si elle est inactive pendant quelques heures.

## Multiplexeur de terminal

Les programmes `tmux` et `screen` sont des exemples de multiplexeurs de terminal qui vous permettent de complètement détacher une session de terminal, laquelle restera active jusqu'à ce que vous vous y rattachiez. Vous pouvez donc vous déconnecter de la grappe, fermer votre poste de travail ou le mettre en veille, puis reprendre le travail le lendemain en vous rattachant à la même session.

!!! attention "Dépendance au nœud de connexion"
    Chacune de nos grappes comprend plusieurs nœuds de connexion et votre session `tmux` ou `screen` est lancée sur un nœud particulier. Pour vous rattacher à une session, vous devez utiliser le même nœud de connexion que celui où vous avez lancé `tmux` ou `screen`. Il peut arriver qu'un nœud de connexion soit redémarré, ce qui élimine les sessions qui se trouvent sur ce nœud; dans un tel cas, vos sessions et tous les processus associés seront perdus.

### tmux

Le logiciel [tmux](https://en.wikipedia.org/wiki/Tmux) est un multiplexeur de terminal qui permet plusieurs sessions virtuelles à l'intérieur d'une même session de terminal. Vous pouvez donc vous déconnecter d'une session SSH sans que les processus soient affectés.

Pour une introduction à tmux (en anglais), consultez :
*   [*The Tao of tmux*](https://leanpub.com/the-tao-of-tmux/read)
*   [*Getting Started With TMUX*](https://www.youtube.com/watch?v=252K9lrRdMU), une vidéo de 24 minutes
*   [*Turbo boost your interactive experience on the cluster with tmux*](https://www.youtube.com/watch?v=Y1Of3S5iVog), une vidéo de 58 minutes

#### Aide-mémoire

[Consultez la documentation complète (en anglais)](http://hyperpolyglot.org/multiplexers).

| Commande | Description |
| :------- | :---------- |
| `tmux` | Démarrer le serveur |
| `Ctrl+B D` | Se déconnecter du serveur |
| `tmux a` | Se reconnecter au serveur |
| `Ctrl+B C` | Créer une nouvelle fenêtre |
| `Ctrl+B N` | Aller à la prochaine fenêtre |
| `Ctrl+B [` | Activer le mode copie pour le défilement avec la souris et les touches page suivante et page précédente |
| `Esc` | Désactiver le mode copie |

#### Utiliser tmux dans une tâche soumise par tmux

Si vous utilisez `tmux` pour soumettre une tâche et que vous tentez de lancer `tmux` à l’intérieur de cette tâche, vous obtiendrez le message d'erreur `lost server`. Ceci est dû au fait que la variable d'environnement `$TMUX`, qui pointe vers le serveur `tmux` sur le nœud de connexion, est propagée à la tâche. La valeur de la variable n'est donc pas valide. Vous pouvez la réinitialiser avec :

```bash
unset TMUX
```

Cependant, l'usage de deux (ou plus) niveaux de `tmux` n'est pas recommandé. Pour envoyer des commandes à un `tmux` imbriqué, il faut taper deux fois les touches `Ctrl+B`; par exemple, pour créer une fenêtre, il faut taper `Ctrl+B Ctrl+B C`. Considérez plutôt d'utiliser GNU Screen (voir ci-dessous) à l'intérieur de vos tâches (si vous utilisez `tmux` sur un nœud de connexion).

### GNU Screen

Le programme [GNU Screen](https://en.wikipedia.org/wiki/GNU_Screen) est un autre multiplexeur de terminal souvent utilisé. Créez une session de terminal détachée avec :

```bash
screen -S <nom_de_session>
```

Donnez à vos sessions des noms faciles à retenir. Pour voir la liste des sessions détachées sur un nœud, utilisez la commande `screen -list`.

```bash
screen -list
There is a screen on:
        164133.foo      (Attached)
1 Socket in /tmp/S-stubbsda.
```

Pour vous attacher à une de vos sessions, utilisez `screen -d -r <nom_de_session>`.