---
title: "Symbolic algebra software/en"
slug: "symbolic_algebra_software"
lang: "en"

source_wiki_title: "Symbolic algebra software/en"
source_hash: "382f5e0e06a9b7c32cf25069f74106e6"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:43:22.340649+00:00"

tags:
  - software

keywords:
  - "software packages"
  - "open source software"
  - "Symbolic algebra software"
  - "SageMath"
  - "exact arithmetic"

questions:
  - "What is symbolic algebra software and what types of mathematical operations is it designed to handle?"
  - "How does the availability and installation process on the clusters differ between commercial packages like Mathematica and open-source alternatives like SageMath?"
  - "What are some of the additional open-source symbolic algebra tools available as modules on the clusters besides SageMath?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Symbolic algebra software is a program, often accessible as an interactive environment, that is able to work directly with symbolic expressions (derivatives, integrals and so forth) and permits exact arithmetic (e.g. `exp(-i*pi/2) = -i`) as well as other formal operations that arise in domains like number theory, group theory, differential geometry, commutative algebra and so forth. Most such programs also permit the use of approximate numerical calculations using floating-point numbers for handling problems that are analytically intractable.

Some well-known symbolic algebra software packages are the commercial products [Mathematica](http://www.wolfram.com/mathematica/) and [Maple](http://www.maplesoft.com/), neither of which is available on our clusters but which you can install in your home directory if your licence for the software allows this.

!!! note "Using SageMath"
    An open-source alternative, [SageMath](https://www.sagemath.org/), can be used by loading the appropriate module:

    ```bash
    module load sagemath/9.3
    ```

    Afterwards, you can run the software interactively, e.g.

    ```bash
    sage
    ```

    ```text
    ┌────────────────────────────────────────────────────────────────────┐
    │ SageMath version 9.3, Release Date: 2021-05-09                     │
    │ Using Python 3.8.10. Type "help()" for help.                       │
    └────────────────────────────────────────────────────────────────────┘
    sage:
    ```

Additional open-source software that may be of interest and which is available on the clusters as a [module](utiliser-des-modules.md) includes the [Number Theory Library (NTL)](https://www.shoup.net/ntl/) (`ntl`), [SINGULAR](https://www.singular.uni-kl.de/) (`singular`), [Macaulay2](https://faculty.math.illinois.edu/Macaulay2/) (`m2`) and [PARI/GP](http://pari.math.u-bordeaux.fr/) (`pari-gp`).