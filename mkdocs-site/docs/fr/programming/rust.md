---
title: "Rust/fr"
slug: "rust"
lang: "fr"

source_wiki_title: "Rust/fr"
source_hash: "66f284e6f9499ab4e7698dae76db7fa6"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T10:59:40.600605+00:00"

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

[Rust](https://www.rust-lang.org/fr/) est un langage de programmation multiparadigmes, de haut niveau et à usage général. Rust met l'accent sur les performances, la sécurité des types et la simultanéité. Rust applique la sécurité de la mémoire, c'est-à-dire que toutes les références pointent vers une mémoire valide sans nécessiter l'utilisation d'un ramasse-miettes (*garbage collector*) ou d'un compteur de références, lesquels sont présents dans d'autres langages sécurisés pour la mémoire.

## Module

Le compilateur Rust est disponible sous forme de [module](utiliser-des-modules.md).

```bash
module spider rust
```

## Installer un *crate*

Un paquet écrit en Rust s'appelle un [*crate*](https://doc.rust-lang.org/book/ch07-01-packages-and-crates.html).

### À partir de Crates.io

1.  Chargez les modules nécessaires.

    ```bash
    module load rust
    ```

2.  Bâtissez et installez le *crate* localement. Cette opération doit être effectuée à partir d'un nœud de connexion.

    ```bash
    cargo install ungoliant
    ```

3.  Testez le binaire.

    ```bash
    $HOME/.cargo/bin/ungoliant -h
    ```

Vous pouvez aussi ajouter `.cargo/bin` à votre variable d'environnement `$PATH` à l'aide de la commande `export PATH="$HOME/.cargo/bin:$PATH"`.

### À partir d'un dépôt Git

1.  Chargez les modules nécessaires.

    ```bash
    module load rust
    ```

2.  Bâtissez et installez le *crate* localement à partir d'un nœud de connexion.

    ```bash
    cargo install --git https://github.com/username/repo-name
    ```

3.  Testez le binaire.

    ```bash
    $HOME/.cargo/bin/<binname> -h
    ```

Vous pouvez aussi ajouter `.cargo/bin` à votre variable d'environnement `$PATH` à l'aide de la commande `export PATH="$HOME/.cargo/bin:$PATH"`.

## Utiliser le compilateur *nightly*

Puisque certaines fonctionnalités ne sont pas encore stables, elles ne sont pas incluses dans la version stable offerte, mais sont cependant utilisées par certains *crates*. Par exemple, si vous souhaitez utiliser la version *nightly* du compilateur, vous pouvez l'installer localement.

1.  Installez le compilateur en tant que module local.

    ```bash
    eb Rust-1.53.0.eb --try-software-version=nightly --disable-enforce-checksums
    ```

2.  Chargez le module local.

    ```bash
    module load rust/nightly
    ```

## Nettoyer le cache

Puisque le cache et le registre occupent souvent beaucoup d'espace, vous pouvez en récupérer en supprimant le registre à l'aide de la commande :

```bash
rm -r ~/.cargo/registry