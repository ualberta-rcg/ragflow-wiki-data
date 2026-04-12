---
title: "Symbolic algebra software"
slug: "symbolic_algebra_software"
lang: "base"

source_wiki_title: "Symbolic algebra software"
source_hash: "86b4fbdab1de59aa01c8c095261c91e1"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:43:07.460361+00:00"

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
  - "How can users access and install commercial packages like Mathematica or Maple on the clusters?"
  - "Which open-source symbolic algebra alternatives are available as modules and how can a user load them?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Symbolic algebra software is a program, often accessible as an interactive environment, that is able to work directly with symbolic expressions (derivatives, integrals and so forth) and permits exact arithmetic (e.g. `exp(-i*pi/2) = -i`) as well as other formal operations that arise in domains like number theory, group theory, differential geometry, commutative algebra and so forth. Most such programs also permit the use of approximate numerical calculations using floating point numbers for handling problems that are analytically intractable. Some well-known symbolic algebra software packages are the commercial products [Mathematica](http://www.wolfram.com/mathematica/) and [Maple](http://www.maplesoft.com/), neither of which is available on our clusters but which you can install in your home directory if your license for the software allows this. An open source alternative, [SageMath](https://www.sagemath.org/), can however be used by loading the appropriate module:

```bash
module load sagemath/9.3
```

Afterwards you can then run the software interactively, e.g.

```console
sage
┌────────────────────────────────────────────────────────────────────┐
│ SageMath version 9.3, Release Date: 2021-05-09                     │
│ Using Python 3.8.10. Type "help()" for help.                       │
└────────────────────────────────────────────────────────────────────┘
sage:
```

Additional open source software that may be of interest and which is available on the clusters as a [module](../programming/utiliser_des_modules.md) includes the [Number Theory Library (NTL)](https://www.shoup.net/ntl/) (`ntl`), [SINGULAR](https://www.singular.uni-kl.de/) (`singular`), [Macaulay2](https://faculty.math.illinois.edu/Macaulay2/) (`m2`) and [PARI/GP](http://pari.math.u-bordeaux.fr/) (`pari-gp`).