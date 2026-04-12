---
title: "Rust/fr"
slug: "rust"
lang: "fr"

source_wiki_title: "Rust/fr"
source_hash: "66f284e6f9499ab4e7698dae76db7fa6"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:10:39.416604+00:00"

tags:
  []

keywords:
  - "Rust"
  - "langage de programmation"
  - "cargo"
  - "compilateur"
  - "crate"

questions:
  - "Quelles sont les caractéristiques principales du langage Rust, notamment en matière de performances et de sécurité de la mémoire ?"
  - "Quelles sont les étapes à suivre pour installer un \"crate\" localement à partir de Crates.io ou d'un répertoire Git ?"
  - "Comment peut-on installer la version \"nightly\" du compilateur et nettoyer le cache de Rust pour libérer de l'espace ?"
  - "Quelles sont les caractéristiques principales du langage Rust, notamment en matière de performances et de sécurité de la mémoire ?"
  - "Quelles sont les étapes à suivre pour installer un \"crate\" localement à partir de Crates.io ou d'un répertoire Git ?"
  - "Comment peut-on installer la version \"nightly\" du compilateur et nettoyer le cache de Rust pour libérer de l'espace ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Rust](https://www.rust-lang.org/fr/) est un langage de programmation multiparadigme, de haut niveau et à usage général. Rust met l'accent sur les performances, la sécurité des types et la simultanéité. Rust assure la sécurité de la mémoire, ce qui signifie que toutes les références pointent vers une mémoire valide sans nécessiter l'utilisation d'un ramasse-miettes (*garbage collector*) ou d'un compteur de références présent dans d'autres langages sécurisés pour la mémoire.

## Module
Le compilateur Rust est disponible sous forme de [module](utiliser_des_modules.md).

```bash
module spider rust
```

## Installer un "crate"
Un paquet écrit en Rust s'appelle un [*crate*](https://doc.rust-lang.org/book/ch07-01-packages-and-crates.html).

### À partir de Crates.io
1. Chargez les modules requis.

```bash
module load rust
```

2. Créez et installez le "crate" localement. Cela doit être fait à partir d'un nœud de connexion.

```bash
cargo install ungoliant
```

3. Testez le binaire.

```bash
$HOME/.cargo/bin/ungoliant -h
```

Vous pouvez également ajouter `.cargo/bin` à votre `$PATH` avec `export PATH="$HOME/.cargo/bin:$PATH"`.

### À partir d'un répertoire Git
1. Chargez les modules requis.

```bash
module load rust
```

2. Créez et installez le "crate" localement à partir d'un nœud de connexion.

```bash
cargo install --git https://github.com/username/repo-name
```

3. Testez le binaire.

```bash
$HOME/.cargo/bin/<binname> -h
```

Vous pouvez aussi ajouter `.cargo/bin` à votre `$PATH` avec `export PATH="$HOME/.cargo/bin:$PATH"`.

## Utiliser le compilateur *nightly*
Puisque certaines fonctionnalités ne sont pas encore stables, elles ne sont pas incluses dans la version stable offerte, mais sont cependant utilisées par certains "crates".
Par exemple, si vous voulez utiliser la version *nightly* du compilateur, vous pouvez l'installer localement.

1. Installez le compilateur en tant que module local.

```bash
eb Rust-1.53.0.eb --try-software-version=nightly --disable-enforce-checksums
```

2. Chargez le module local.

```bash
module load rust/nightly
```

## Nettoyer le cache
Puisque le cache et le registre occupent souvent beaucoup d'espace, vous pouvez en libérer en supprimant le registre avec :

```bash
rm -r ~/.cargo/registry