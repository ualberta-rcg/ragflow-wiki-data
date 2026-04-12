---
title: "Prolonging terminal sessions/fr"
slug: "prolonging_terminal_sessions"
lang: "fr"

source_wiki_title: "Prolonging terminal sessions/fr"
source_hash: "270d9df932588aeae43a1497d6aa2f78"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:28:51.118071+00:00"

tags:
  []

keywords:
  - "SSH"
  - "tmux imbriqué"
  - "GNU Screen"
  - "connexion active"
  - "tmux"
  - "session de terminal détachée"
  - "Ctrl+B"
  - "nœud de connexion"
  - "attacher à une session"
  - "screen"
  - "réinitialiser"
  - "screen -list"
  - "multiplexeur de terminal"

questions:
  - "Comment modifier la configuration du client SSH pour empêcher la déconnexion lors d'une longue période d'inactivité ?"
  - "Quel est l'avantage principal d'utiliser un multiplexeur de terminal comme tmux ou screen, et quel risque faut-il prendre en compte concernant les nœuds de connexion ?"
  - "Pourquoi l'erreur \"lost server\" se produit-elle lors du lancement de tmux à l'intérieur d'une tâche déjà soumise par tmux, et comment peut-on résoudre ce problème ?"
  - "Comment créer une nouvelle session de terminal détachée avec GNU Screen ?"
  - "Quelle commande permet d'afficher la liste des sessions détachées disponibles sur un nœud ?"
  - "Comment peut-on s'attacher à une session GNU Screen existante ?"
  - "Quelle commande permet de réinitialiser l'environnement tmux ?"
  - "Comment doit-on procéder pour envoyer des commandes à une session tmux imbriquée ?"
  - "Quel outil est recommandé comme alternative à l'utilisation de plusieurs niveaux de tmux ?"
  - "Comment créer une nouvelle session de terminal détachée avec GNU Screen ?"
  - "Quelle commande permet d'afficher la liste des sessions détachées disponibles sur un nœud ?"
  - "Comment peut-on s'attacher à une session GNU Screen existante ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Pour soumettre et faire le suivi des tâches, modifier des fichiers et plusieurs autres opérations, vous aurez sans doute besoin de vous connecter à une grappe via [SSH](ssh.md). Il est parfois nécessaire de garder la connexion active pendant plusieurs heures, même plusieurs jours. Nous décrivons ici certaines techniques pour ce faire.

## Configuration de SSH

Une solution simple pour prolonger une connexion est de modifier la configuration de votre client SSH. Avec macOS et Linux, cette configuration se trouve dans `` `$HOME/.ssh/config` `` alors qu'avec Windows, elle est dans `` `C:\Users\<username>\.ssh\config` ``. Si le fichier n'existe pas, vous devez le créer et ajouter les lignes suivantes :

```ini title="Configuration SSH"
Host *
    ServerAliveInterval 240
```
Ceci transmet un signe de vie au serveur distant (comme une grappe de l'Alliance) à toutes les 240 secondes (4 minutes), ce qui devrait garder la connexion vivante même si elle est inactive pendant quelques heures.

## Multiplexeur de terminal

Les programmes `tmux` et `screen` sont des exemples de multiplexeurs de terminal qui vous permettent de complètement détacher une session de terminal qui restera active jusqu'à ce que vous vous y rattachiez. Vous pouvez donc vous déconnecter de la grappe, fermer le poste de travail ou le mettre en veille, puis reprendre le travail le lendemain en vous rattachant à la même session.

!!! warning "Dépendance au nœud de connexion"
    Chacune de nos grappes comprend plusieurs nœuds de connexion et votre session `tmux` ou `screen` est lancée sur un nœud particulier. Pour vous rattacher à une session, vous devez utiliser le même nœud de connexion que celui où vous avez lancé `tmux` ou `screen`. Il arrive qu'un nœud de connexion soit redémarré, ce qui élimine les sessions qui se trouvent sur ce nœud; dans un tel cas, vos sessions et tous les processus associés seront perdus.

### tmux

Le logiciel [tmux](https://en.wikipedia.org/wiki/Tmux) est un multiplexeur de terminal qui permet plusieurs sessions virtuelles à l'intérieur d'une même session de terminal. Vous pouvez donc vous déconnecter d'une session SSH sans que les processus soient affectés.

Pour une introduction à tmux (en anglais) :
* [*The Tao of tmux*](https://leanpub.com/the-tao-of-tmux/read)
* [*Getting Started With TMUX*](https://www.youtube.com/watch?v=252K9lrRdMU), vidéo de 24 minutes
* [*Turbo boost your interactive experience on the cluster with tmux*](https://www.youtube.com/watch?v=Y1Of3S5iVog), vidéo de 58 minutes

#### Aide-mémoire

[Voyez la documentation complète (en anglais)](http://hyperpolyglot.org/multiplexers).

| Commande    | Description                                                                     |
| :---------- | :------------------------------------------------------------------------------ |
| `tmux`      | Démarrer le serveur                                                             |
| `Ctrl+B D`  | Se déconnecter du serveur                                                       |
| `tmux a`    | Se reconnecter au serveur                                                       |
| `Ctrl+B C`  | Créer une nouvelle fenêtre                                                      |
| `Ctrl+B N`  | Aller à la prochaine fenêtre                                                    |
| `Ctrl+B [`  | Activer le mode copie pour défilement avec la souris et les touches page suivante et page précédente |
| `Esc`       | Désactiver le mode copie                                                        |

#### Utiliser tmux dans une tâche soumise par tmux

Si vous utilisez tmux pour soumettre une tâche et que vous tentez de lancer tmux à l’intérieur de cette tâche, vous obtiendrez le message d'erreur `` `lost server` ``. Ceci est dû au fait que la variable d'environnement `` `$TMUX` ``, qui pointe vers le serveur tmux sur le nœud de connexion, est propagée à la tâche. La valeur de la variable n'est donc pas valide. Vous pouvez la réinitialiser avec :

```bash
unset TMUX
```

Cependant, l'usage de deux (ou plus) niveaux de tmux n'est pas recommandé. Pour envoyer des commandes à un tmux imbriqué, il faut taper deux fois les touches `` `Ctrl+B` ``; par exemple, pour créer une fenêtre, il faut taper `` `Ctrl+B Ctrl+B C` ``. Considérez plutôt d'utiliser GNU Screen (ci-dessous) à l'intérieur de vos tâches (si vous utilisez tmux sur un nœud de connexion).

### GNU Screen

Le programme [GNU Screen](https://en.wikipedia.org/wiki/GNU_Screen) est un autre multiplexeur de terminal souvent utilisé. Créez une session de terminal détachée avec :

```bash
screen -S <nom_session>
```
Donnez à vos sessions des noms faciles à retenir. Pour voir la liste des sessions détachées sur un nœud, utilisez la commande `` `screen -list` ``.

```bash title="Lister les sessions screen"
screen -list
```
```text title="Exemple de résultat"
There is a screen on:
        164133.foo      (Attached)
1 Socket in /tmp/S-stubbsda.
```
Pour vous attacher à une de vos sessions, utilisez `` `screen -d -r <nom_session>` ``.