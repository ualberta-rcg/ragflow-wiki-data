---
title: "Moose/en"
slug: "moose"
lang: "en"

source_wiki_title: "Moose/en"
source_hash: "2d0e16426cf2b8d0b32221025d53e68a"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:30:29.121616+00:00"

tags:
  []

keywords:
  - "multiphysics solvers"
  - "compiling instructions"
  - "Multiphysics Object Oriented Simulation Environment"
  - "MOOSE framework"
  - "finite element framework"

questions:
  - "What is the MOOSE framework and what is its primary purpose?"
  - "Why do users need to compile the MOOSE software themselves on the clusters?"
  - "What are the specific steps and commands required to successfully compile and test MOOSE using the StdEnv/2023 environment?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[MOOSE (Multiphysics Object Oriented Simulation Environment)](https://mooseframework.inl.gov/) is an object-oriented C++ finite element framework for the development of tightly coupled multiphysics solvers from Idaho National Laboratory. MOOSE is not officially maintained on our clusters, so users need to compile the software themselves. The following compiling instructions worked for multiple users on our upgraded systems (using StdEnv/2023 environment):

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

!!! note
    Please let us know by writing to our [Technical support](../support/technical_support.md) if these instructions do not work for you.