---
title: "SSH configuration file/fr"
slug: "ssh_configuration_file"
lang: "fr"

source_wiki_title: "SSH configuration file/fr"
source_hash: "c1c3f65c399d8ba9ef674b8f5d1afe16"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:16:13.579987+00:00"

tags:
  - connecting

keywords:
  - "configuration SSH"
  - "redirection X11"
  - "~/.ssh/config"
  - "redirection de l'agent"
  - "clé SSH"

questions:
  - "Comment configurer le fichier local SSH pour simplifier la connexion et le transfert de fichiers vers un serveur spécifique ?"
  - "Comment optimiser le fichier de configuration pour se connecter facilement à plusieurs grappes différentes avec un seul bloc de code ?"
  - "Quels sont les risques de sécurité associés à l'activation par défaut de la redirection X11 et de la redirection de l'agent SSH ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Page enfant de [SSH](ssh.md)*

Sous Linux et macOS, vous pouvez modifier votre fichier local de configuration SSH pour changer le comportement de `ssh` et simplifier la procédure de connexion. Par exemple, pour vous connecter à `narval.alliancecan.ca` comme `username` avec une [clé SSH](using-ssh-keys-in-linux.md), vous pourriez devoir utiliser la commande :

```bash
ssh -i ~/.ssh/your_private_key username@narval.alliancecan.ca
```

Pour ne pas avoir à entrer cette commande chaque fois que vous vous connectez à Narval, ajoutez ce bloc de configuration au fichier `~/.ssh/config` sur votre ordinateur local :

```config
Host narval
  User username
  HostName narval.alliancecan.ca
  IdentityFile ~/.ssh/your_private_key
```

Vous pouvez maintenant vous connecter à Narval en entrant :

```bash
ssh narval
```

Ceci change aussi le comportement de `sftp`, `scp` et `rsync` et vous pouvez maintenant [transférer des fichiers](transferring-data.md) en entrant, par exemple :

```bash
scp local_file narval:work/
```

Si vous vous connectez souvent à des grappes différentes, modifiez le bloc `Host` ci-dessus plutôt que d'ajouter une entrée pour chacune des grappes. Par exemple, pour Narval, Béluga, Graham et Cedar, utilisez :

```config
Host narval beluga graham cedar
  [...]
  HostName %h.alliancecan.ca
  [...]
```

Notez qu'il faut installer votre [clé SSH publique](ssh-keys.md) sur chacune des grappes, ou utiliser plutôt [la CCDB](ssh-keys.md#par-la-ccdb).

D'autres options de la commande `ssh` ont des paramètres correspondants qui peuvent être entrés dans le fichier `~/.ssh/config` de votre ordinateur. En particulier :

*   `-X` (redirection X11)
*   `-Y` (redirection X11 sans contrôles de sécurité)
*   `-A` (redirection de l'agent)

peuvent être définies dans les sections correspondantes du fichier de configuration en ajoutant les lignes :

*   `ForwardX11 yes`
*   `ForwardX11Trusted yes`
*   `ForwardAgent yes`

!!! attention "Attention"
Cependant, ceci n'est pas recommandé, car :

*   activer la redirection X11 par défaut pour toutes vos connexions peut ralentir vos sessions, particulièrement si le client X11 de votre ordinateur est mal configuré;
*   activer la redirection X11 sans les extensions de sécurité présente un risque et nous vous recommandons de l'utiliser quand vous n'avez aucune autre option; si le serveur auquel vous vous connectez est compromis, quelqu'un qui a les permissions *root* pourrait détecter l'activité du clavier de votre ordinateur;
*   malgré le fait que la redirection de l'agent est pratique et plus sécuritaire que d'entrer un mot de passe sur un ordinateur distant, elle comporte un risque. Dans le cas où le serveur auquel vous vous connectez est compromis, un utilisateur avec les privilèges `root` pourrait utiliser votre agent pour se connecter à un autre hôte à votre insu. Nous recommandons d'utiliser la redirection de l'agent *uniquement lorsque nécessaire*. De plus, si vous utilisez cette fonctionnalité, combinez-la avec `ssh-askpass` pour que chaque utilisation de votre agent déclenche une invite sur votre ordinateur pour vous avertir que votre agent est utilisé.