---
title: "Git/fr"
slug: "git"
lang: "fr"

source_wiki_title: "Git/fr"
source_hash: "96876d578a10475815f2b94bd1cb4090"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:42:26.477163+00:00"

tags:
  - software

keywords:
  - "décentralisé"
  - "git reset"
  - "commandes Git"
  - "dépôt"
  - "Git"
  - "validation"
  - "commandes"
  - "branche"
  - "gestion de code source"
  - "git format-patch"
  - "configuration"
  - "rustines"

questions:
  - "Qu'est-ce que Git et dans quel contexte initial a-t-il été créé par Linus Torvalds ?"
  - "Comment fonctionne le principe décentralisé de Git et son modèle de développement basé sur les branches ?"
  - "Quelles sont les étapes générales et les commandes de base utilisées par un développeur pour gérer ses modifications avec Git ?"
  - "Comment doit-on configurer son environnement Git global (nom, courriel, éditeur de texte) avant de commencer à développer ?"
  - "Quelles sont les commandes de base permettant de créer ou cloner un dépôt, puis d'y valider et pousser des modifications ?"
  - "Quelle est la solution au message d'erreur \"Unable to create thread\" lié aux limites de ressources sur les nœuds de connexion ?"
  - "À quoi sert la commande `git reset` selon le document ?"
  - "Quelles sont les commandes spécifiques permettant de créer, appliquer et envoyer des rustines ?"
  - "Quelle commande est introduite dans la section \"Autres commandes\" à la fin du texte ?"
  - "Comment doit-on configurer son environnement Git global (nom, courriel, éditeur de texte) avant de commencer à développer ?"
  - "Quelles sont les commandes de base permettant de créer ou cloner un dépôt, puis d'y valider et pousser des modifications ?"
  - "Quelle est la solution au message d'erreur \"Unable to create thread\" lié aux limites de ressources sur les nœuds de connexion ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Git](https://en.wikipedia.org/wiki/Git) est un outil distribué rapide et sécuritaire pour la gestion de code source (voir le site [gitscm.org](http://git-scm.org)). L’application a été créée pour le projet Linux par [Linus Torvalds](http://en.wikipedia.org/wiki/Linus_Torvalds) et est maintenue par Junio Hamano.

## Principe de fonctionnement
Contrairement aux outils de gestion de code source moins récents, Git fonctionne en mode décentralisé et les développeurs ne sont pas dépendants d'un dépôt central pour valider (*to commit*) des modifications. Chaque dépôt Git contient l’historique complet du projet. Chaque objet Git (*changeset*, fichier, répertoire) est une feuille d’un arbre à branches multiples. Le développement d'un projet avec Git est basé sur un modèle où une branche correspond à une fonctionnalité. Plusieurs itérations de la fonctionnalité peuvent être archivées avant que celle-ci ne soit fusionnée avec le tronc commun. Pour les détails sur le modèle de développement par branches, voyez [A successful Git branching model](http://nvie.com/posts/a-successful-git-branching-model/).

Une technique particulièrement intéressante est celle du picorage (*cherry picking*) qui consiste à prendre une partie d’une branche pour la fusionner avec une autre.

## Utilisation
Règle générale, un développeur va

1.  configurer un environnement Git global,
2.  cloner ou créer un dépôt,
3.  effectuer des modifications,
4.  valider ces modifications,
5.  propager les modifications vers un autre dépôt.

Puisque Git est décentralisé, il n'y a pas nécessairement de dépôt de référence.

### Sommaire des commandes
**Commandes de base**

| Commande | Description |
| :------- | :---------- |
| `git config` | configurer Git |
| `git init` | créer un nouveau dépôt |
| `git clone` | cloner un dépôt existant |
| `git add` | ajouter un fichier ou un répertoire au dépôt |
| `git rm` | supprimer un fichier ou un répertoire du dépôt |
| `git commit` | valider (*to commit*) les modifications dans un dépôt |
| `git push` | propager les modifications validées vers un autre dépôt |
| `git pull` | récupérer les modifications d'un autre dépôt et les appliquer (*to merge*) à votre dépôt |
| `git fetch` | récupérer les modifications d’un autre dépôt, sans les appliquer au vôtre |
| `git merge` | fusionner les modifications |

**Commandes pour voir les changements**

| Commande | Description |
| :------- | :---------- |
| `git blame` | afficher les derniers auteurs ayant modifié un fichier |
| `git log` | afficher l’historique des validations |
| `git diff` | comparer deux versions |
| `git status` | afficher l'état des fichiers |
| `git show` | afficher divers objets Git |
| `git cat-file` | afficher le contenu, le type ou la taille des objets |

**Commandes relatives aux branches, étiquettes et dépôts distants**

| Commande | Description |
| :------- | :---------- |
| `git branch` | gérer les branches de développement |
| `git tag` | gérer les étiquettes des versions |
| `git remote` | gérer les dépôts distants |
| `git checkout` | extraire une branche ou un chemin |
| `git reset` | changer la tête d'une branche |

**Commandes relatives aux rustines**

| Commande | Description |
| :------- | :---------- |
| `git format-patch` | créer une rustine |
| `git am` | appliquer une rustine |
| `git send-email` | envoyer une rustine |

**Autres commandes**

| Commande | Description |
| :------- | :---------- |
| `git bisect` | faire le diagnostic d'un problème |
| `git gc` | nettoyer le dépôt |
| `git rebase` | linéariser l’historique |
| `git grep` | chercher du contenu |

### Configuration de l'environnement Git global
Le contenu de la présente section est inspiré de [Software Carpentry - *Version Control with Git*](https://swcarpentry.github.io/git-novice/02-setup.html). Lorsque vous commencez à développer sur un nouveau système, vous devez configurer

*   votre nom et votre adresse de courriel, qui seront associés à chaque opération de validation dans un dépôt de données. Si vos révisions sont poussées dans un dépôt public, cette information sera publique.

```bash
git config --global user.name "Prénom Nom"
git config --global user.email "courriel@adresse.ca"
```

*   Limitez-vous à quatre fils, autrement vos commandes `git clone` peuvent échouer.

```bash
git config --global pack.threads 4
```

*   Si vous ne connaissez pas bien `vi`, vous pouvez utiliser un autre éditeur de texte pour rédiger vos messages de validation.

```bash
git config --global core.editor "nano -w"
```

*   Vous pouvez aussi redéfinir le nom par défaut de la branche initiale, par exemple, `main`.

```bash
git config --global init.defaultBranch main
```

Pour la liste de toutes les options configurées dans l'environnement global, utilisez la commande

```bash
git config --list --global
```

### Création ou clonage d'un dépôt
La première étape est habituellement de créer votre propre dépôt ou de cloner un dépôt existant.

Pour créer un dépôt

```bash
git init my-project
```

Pour cloner un dépôt

```bash
git clone git://github.com/git/git.git
```

### Validation et enregistrement des modifications
Quand le dépôt est prêt, changez de répertoire et éditez le fichier.

```bash
cd my-project
nano file.txt
```

Quand le travail est terminé, ajoutez le fichier

```bash
git add file.txt
```

puis validez la modification.

```bash
git commit
```

Si le dépôt a été cloné, il est maintenant possible de pousser vos modifications vers le dépôt original avec

```bash
git push origin main
```

Dans cette dernière commande, *origin* est le dépôt distant et *main* est la branche courante qui sera poussée.

Avec les dépôts Git moins récents, vous devrez peut-être utiliser `git push origin master`.

## Hébergement de dépôts Git
[GitHub](http://github.com) et [Bitbucket](http://bitbucket.org) sont deux des principaux services d’hébergement de Git. Ils sont tous les deux disponibles pour les projets commerciaux comme pour les projets libres.

## Dépannage

### Message d'erreur *Unable to create thread*
Si vous obtenez le message

```
fatal: unable to create thread: Resource temporarily unavailable
fatal: fetch-pack: invalid index-pack output
```

Cela est dû aux limites de ressources sur les nœuds de connexion des grappes. La solution est de limiter à deux le nombre de fils. Utilisez la commande suivante sur chaque grappe.

```bash
git config --global pack.threads "2"