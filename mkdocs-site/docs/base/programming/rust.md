---
title: "Rust"
slug: "rust"
lang: "base"

source_wiki_title: "Rust"
source_hash: "d9b66d491cce40fff35084418791c368"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:10:15.718731+00:00"

tags:
  []

keywords:
  - "Compiler"
  - "Rust"
  - "Crate"
  - "Module"
  - "Cargo"

questions:
  - "What are the primary characteristics of the Rust programming language, particularly regarding memory safety?"
  - "What are the steps to build and install a Rust crate locally from Crates.io or a Git repository?"
  - "How can a user install the Rust nightly compiler for unstable features and clean up the Cargo cache to reclaim space?"
  - "What are the primary characteristics of the Rust programming language, particularly regarding memory safety?"
  - "What are the steps to build and install a Rust crate locally from Crates.io or a Git repository?"
  - "How can a user install the Rust nightly compiler for unstable features and clean up the Cargo cache to reclaim space?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Rust](https://www.rust-lang.org/) is a multi-paradigm, high-level, general-purpose programming language. Rust emphasizes performance, type safety, and concurrency. Rust enforces memory safety — that is, that all references point to valid memory — without requiring the use of a garbage collector or reference counting present in other memory-safe languages.

## Module
The Rust compiler is available as a [module](utiliser_des_modules.md).
```bash
module spider rust
```

## Installing a crate
A package written in Rust is called a [*crate*](https://doc.rust-lang.org/book/ch07-01-packages-and-crates.html).

### From Crates.io
1. Load the required modules.
```bash
module load rust
```
2. Build and install the crate locally. This must be done from a login node.
```bash
cargo install ungoliant
```
3. Test the binary.
```bash
$HOME/.cargo/bin/ungoliant -h
```
You can also add `.cargo/bin` to your `$PATH` with: `export PATH="$HOME/.cargo/bin:$PATH"`.

### From a Git repository
1. Load the required modules.
```bash
module load rust
```
2. Build and install the crate locally. This must be done from a login node.
```bash
cargo install --git https://github.com/username/repo-name
```
3. Test the binary.
```bash
$HOME/.cargo/bin/<binname> -h
```
You can also add `.cargo/bin` to your `$PATH` with: `export PATH="$HOME/.cargo/bin:$PATH"`.

## Using the Rust nightly compiler
Since some optimization features are not yet stable they are not part of the stable release, but nonetheless some crates make use of them.
If you require the Rust nightly compiler, you can install it locally.

1. Install the compiler as a local module.
```bash
eb Rust-1.53.0.eb --try-software-version=nightly --disable-enforce-checksums
```
2. Load the local module.
```bash
module load rust/nightly
```

## Clean up cache
Cargo cache and registry can eat up a lot of space. You can reclaim space by removing the registry:
```bash
rm -r ~/.cargo/registry