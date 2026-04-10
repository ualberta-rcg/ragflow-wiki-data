---
title: "Autotools/fr"
slug: "autotools"
lang: "fr"

source_wiki_title: "Autotools/fr"
source_hash: "8bb97a031941c23ca39b56225dd5b8fd"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T04:46:10.336434+00:00"

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

## Description
La suite [Autotools](https://fr.wikipedia.org/wiki/Autotools) (aussi appelée *système de compilation GNU*) comprend l'outil `autoconf`. Cet outil automatise la création des fichiers `Makefile` de l'utilitaire [Make](make.md) pour différents systèmes et (peut-être) différents compilateurs.

Lorsqu'un programme est bâti à l'aide de `autoconf`, la première étape est d'appeler le script `configure` ainsi :

```bash
./configure
```

`Autoconf` vérifie que les versions des compilateurs et logiciels nécessaires sont installés sur l'ordinateur et génère le `Makefile` approprié.

On appelle ensuite `Make` de manière habituelle.
```bash
make
```

Les fichiers sont installés aux bons endroits par `make install`.
Afin de vous assurer l'accès exclusif au logiciel, vous devez normalement spécifier l'endroit où votre logiciel sera installé, ce qui se fait (habituellement) comme suit :

```bash
mkdir $HOME/LOGICIEL
make install --prefix=$HOME/LOGICIEL
```
Dans certains cas, il faut utiliser l'option `--prefix` plutôt que `make`; référez-vous à la documentation du logiciel que vous voulez installer.
Pour indiquer au système les chemins vers notre nouveau logiciel, il faut [créer un module](creer-un-module.md).

Une compilation de base d'un programme utilisant `Autoconf` peut être aussi simple que
```bash
./configure && make && make install --prefix=$HOME/LOGICIEL
```

## Options pour les scripts `configure`
Il existe de nombreuses options dont l'utilisation varie selon le projet. Pour obtenir la liste détaillée, lancez
```bash
./configure --help
```
Nous présentons ici les options les plus communes.

### Répertoire d'installation
Une option toujours disponible est `--prefix`. Celle-ci permet de définir dans quel répertoire `make install` installera l'application ou la bibliothèque. Par exemple, pour installer une application dans le sous-répertoire `programmes` de votre répertoire personnel, vous pouvez utiliser
```bash
./configure --prefix=$HOME/programmes/
```

### Options de fonctionnalités
La plupart des scripts de configuration permettent d'activer ou de désactiver certaines fonctionnalités du programme ou de la bibliothèque à compiler; elles sont généralement de type `--enable-feature` ou `--disable-feature`. En calcul informatique de pointe, il est fréquent que ces options incluent la parallélisation via fils d'exécution ou via MPI, par exemple
```bash
./configure --enable-mpi
```
ou encore
```bash
./configure --enable-threads
```

Il est aussi fréquent d'avoir des options `--with-...` pour paramétrer spécifiquement les fonctionnalités.

!!! attention
    Il est généralement recommandé de ne pas utiliser ces options et de laisser Autoconf trouver les paramètres automatiquement.

Cependant, il est parfois nécessaire de spécifier des paramètres via les options `--with-...`, par exemple
```bash
./configure --enable-mpi --with-mpi-dir=$MPIDIR
```

### Options définies par des variables
Vous pouvez généralement spécifier le compilateur à utiliser et les options qui doivent lui être passées en déclarant des variables après la commande `./configure`. Par exemple, pour définir le compilateur C et les options à lui passer, vous pourriez lancer
```bash
./configure CC=icc CFLAGS="-O3 -xHost"
```
Voici une description des options les plus communes :

| Option    | Description                                                                 |
|:----------|:----------------------------------------------------------------------------|
| `CFLAGS`  | pour le compilateur C                                                       |
| `CPPFLAGS`| pour le préprocesseur et les compilateurs C, C++, Objective C et Objective C++ |
| `CXXFLAGS`| pour le compilateur C++                                                     |
| `DEFS`    | pour définir une macro pour préprocesseur                                 |
| `FCFLAGS` | pour le compilateur Fortran                                                 |
| `FFLAGS`  | pour le compilateur Fortran 77                                              |
| `LDFLAGS` | pour l'éditeur de liens                                                     |
| `LIBS`    | pour les bibliothèques à lier                                               |

La liste exhaustive des variables et options types est disponible dans la [documentation Autoconf](http://www.gnu.org/software/autoconf/manual/autoconf.html).