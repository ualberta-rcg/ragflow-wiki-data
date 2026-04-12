---
title: "Moose/fr"
slug: "moose"
lang: "fr"

source_wiki_title: "Moose/fr"
source_hash: "0966364ae4146b3c390fb69c0f561ec4"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:30:42.335627+00:00"

tags:
  []

keywords:
  - "MOOSE"
  - "environnement de développement C++"
  - "solveurs multiphysiques"
  - "simulation par éléments finis"
  - "compilation"

questions:
  - "Qu'est-ce que l'environnement MOOSE et par quelle organisation est-il développé ?"
  - "Pourquoi les utilisateurs doivent-ils compiler eux-mêmes le logiciel MOOSE sur les grappes de calcul ?"
  - "Quelles sont les étapes et les modules requis pour compiler et tester MOOSE sous l'environnement StdEnv/2023 ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[MOOSE (*Multiphysics Object Oriented Simulation Environment*)](https://mooseframework.inl.gov/) est un environnement de développement C++ orienté objet pour la simulation par éléments finis de solveurs multiphysiques étroitement couplés. Il est développé par l'Idaho National Laboratory. MOOSE n'est pas maintenu officiellement sur nos grappes; pour l'utiliser, vous devez donc compiler vous-même le logiciel. Les instructions de compilation suivantes ont fonctionné sous l'environnement StdEnv/2023 de notre nouvelle infrastructure.

```bash
module load StdEnv/2023
module load python/3.11.5 scipy-stack/2023b python-build-bundle/2025b petsc/3.23.4 eigen/3.4.0 boost/1.85.0
export MOOSE_JOBS=6 METHODS=opt
git clone --depth 1 https://github.com/idaholab/moose.git
cd moose/scripts/
./update_and_rebuild_libmesh.sh --with-xdr-include=$EBROOTGENTOO/include/tirpc --with-glpk-include=$EBROOTGENTOO/include --with-eigen-include=$EBROOTEIGEN/include
./update_and_rebuild_wasp.sh
cd ../test
make -j6
./run_tests -j6
```

Si vous éprouvez des difficultés, écrivez au [soutien technique](../support/technical_support.md).