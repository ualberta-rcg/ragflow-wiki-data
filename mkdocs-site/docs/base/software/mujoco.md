---
title: "MuJoCo"
slug: "mujoco"
lang: "base"

source_wiki_title: "MuJoCo"
source_hash: "e7f10866bd99dcfb099542496485f5b7"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T09:01:27.037961+00:00"

tags:
  - software

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

*MuJoCo stands for **Mu**lti-**Jo**int dynamics with **Co**ntact. It is a physics engine aiming to facilitate research and development in robotics, biomechanics, graphics and animation, and other areas where fast and accurate simulation is needed.[http://www.mujoco.org/](http://www.mujoco.org/)*

It is frequently used with the associated Python bindings `mujoco` as an environment for reinforcement learning (RL) research.

The module contains MuJoCo C/C++ library and its Python bindings.

## Library
In order to access headers and binaries, load the module:
```bash
module load mujoco
```

## Python bindings
To discover which are the compatible Python versions, run
```bash
module spider mujoco/2.2.2
```

1. Load the required modules.
```bash
module load mujoco python
```

2. Import MuJoCo.
```python
python -c "import mujoco"
```

!!! success
    If the command displays nothing, the import was successful.