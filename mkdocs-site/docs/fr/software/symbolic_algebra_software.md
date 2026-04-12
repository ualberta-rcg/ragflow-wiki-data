---
title: "Symbolic algebra software/fr"
slug: "symbolic_algebra_software"
lang: "fr"

source_wiki_title: "Symbolic algebra software/fr"
source_hash: "eba41456320099e73ea2f528666be56b"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:43:37.801085+00:00"

tags:
  - software

keywords:
  - "expressions symboliques"
  - "calcul numérique"
  - "logiciel d'algèbre symbolique"
  - "SageMath"
  - "logiciels libres"

questions:
  - "Qu'est-ce qu'un logiciel d'algèbre symbolique et quelles sont ses principales fonctionnalités ?"
  - "Comment peut-on utiliser des logiciels commerciaux comme Mathematica ou Maple sur les grappes de calcul ?"
  - "Quelles sont les alternatives libres disponibles sur les grappes et comment démarrer une session avec SageMath ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Un logiciel d’algèbre symbolique est une application qui fonctionne souvent comme un environnement interactif pouvant travailler directement avec des expressions symboliques (dérivées, intégrales, etc.) et permettant d’employer l’arithmétique exacte (par exemple `exp(-i*pi/2) = -i`) et d'autres opérations formelles dans des domaines comme la théorie des nombres, la théorie des groupes, la géométrie différentielle, l’algèbre commutative et ainsi de suite. La plupart de ces applications permettent aussi d’utiliser le calcul numérique approximatif avec des nombres à virgule flottante pour traiter des problèmes autrement insolubles. Les applications bien connues [Mathematica](http://www.wolfram.com/mathematica/) et [Maple](http://www.maplesoft.com/Maple) ne sont pas disponibles sur nos grappes, mais peuvent être installées dans votre répertoire `/home` si votre licence le permet. Vous pouvez utiliser [SageMath](https://www.sagemath.org/) comme alternative, en chargeant le module comme suit :

```bash
module load sagemath/9.3
```

Vous pourrez exécuter l’application de façon interactive.

```bash
sage
```
```
┌────────────────────────────────────────────────────────────────────┐
│ SageMath version 9.3, Release Date: 2021-05-09                     │
│ Using Python 3.8.10. Type "help()" for help.                       │
└────────────────────────────────────────────────────────────────────┘
sage:
```

Parmi les autres logiciels libres (*open source*) qui peuvent vous intéresser et qui sont [des modules](utiliser-des-modules.md) disponibles sur nos grappes, on trouve [Number Theory Library (NTL)](https://www.shoup.net/ntl/) (`ntl`), [SINGULAR](https://www.singular.uni-kl.de/) (`singular`), [Macaulay2](https://faculty.math.illinois.edu/Macaulay2/) (`m2`) et [PARI/GP](http://pari.math.u-bordeaux.fr/) (`pari-gp`).