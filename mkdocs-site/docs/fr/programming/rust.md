---
title: "Rust/fr"
tags:
  []

keywords:
  []
---

[Rust](https://www.rust-lang.org/fr/) est un langage de programmation multiparadigmes, de haut niveau et à usage général. Rust met l'accent sur les performances, la sécurité des types et la simultanéité. Rust applique la sécurité de la mémoire, c'est-à-dire que toutes les références pointent vers une mémoire valide sans nécessiter l'utilisation d'un ramasse-miettes (<i>garbage collector</i>) ou d'un compteur de références présent dans d'autres langages sécurisés pour la mémoire.

## Module 
Le compilateur Rust est disponible sous forme de [module](utiliser_des_modules.md).

```bash
module spider rust
```

## Installer un crate 
Un paquet écrit en Rust s'appelle un [*crate*](https://doc.rust-lang.org/book/ch07-01-packages-and-crates.html).

### De Crates.io 
1. Chargez les modules requis.

```bash
module load rust
```

2. Construisez et installez le crate localement. Cela doit être fait à partir d'un nœud de connexion.

```bash
cargo install ungoliant
```

3. Testez le binaire.

```bash
$HOME/.cargo/bin/ungoliant -h
```

Vous pouvez également ajouter `.cargo/bin` à votre `$PATH` avec `export PATH="$HOME/.cargo/bin:$PATH"`.

### D'un répertoire Git 
1. Chargez les modules requis.

```bash
module load rust
```

2. Construisez et installez le crate localement à partir d'un nœud de connexion.

```bash
cargo install --git https://github.com/username/repo-name
```

3. Testez le binaire.

```bash
$HOME/.cargo/bin/<binname> -h
```

Vous pouvez aussi ajouter `.cargo/bin` à votre `$PATH` avec `export PATH="$HOME/.cargo/bin:$PATH"`.

## Utiliser le compilateur <i>nightly</i> 
Puisque certaines fonctionnalités ne sont pas encore stables, elles ne sont pas incluses dans la version stable offerte, mais sont cependant utilisées par certains crates. 
Par exemple, si vous voulez utiliser la version <I>nightly</i> du compilateur, vous pouvez l'installer localement.

1. Installez le compilateur en tant que module local.

```bash

```
nightly --disable-enforce-checksums}}

2. Chargez le module local.

```bash
module load rust/nightly
```

## Nettoyer la cache 
Comme la cache et le registre prennent souvent beaucoup de place, vous pouvez en regagner en supprimant le registre avec

```bash
rm -r ~/.cargo/registry
```