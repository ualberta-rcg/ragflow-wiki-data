---
title: "Moose"
slug: "moose"
lang: "base"

source_wiki_title: "Moose"
source_hash: "8240d0ad62ae0725753aa74ea0d348aa"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T08:58:10.012040+00:00"

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

[MOOSE (Multiphysics Object Oriented Simulation Environment)](https://mooseframework.inl.gov/) is an object-oriented C++ finite element framework for the development of tightly coupled multiphysics solvers from Idaho National Laboratory. Moose is not officially maintained on our clusters, so users need to compile the software themselves. The following compiling instructions worked for multiple users on our upgraded systems (using StdEnv/2023 environment):

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
    Let us know by writing to our [Technical support](technical-support.md) if these instructions do not work for you.