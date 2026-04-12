---
title: "MuJoCo"
slug: "mujoco"
lang: "base"

source_wiki_title: "MuJoCo"
source_hash: "e7f10866bd99dcfb099542496485f5b7"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:33:29.020817+00:00"

tags:
  - software

keywords:
  - "MuJoCo"
  - "physics engine"
  - "Python bindings"
  - "reinforcement learning"
  - "robotics"

questions:
  - "What does MuJoCo stand for and what are its primary applications?"
  - "How is MuJoCo typically utilized in the context of reinforcement learning research?"
  - "What are the command-line steps required to load the MuJoCo library and successfully import its Python bindings?"
  - "What does MuJoCo stand for and what are its primary applications?"
  - "How is MuJoCo typically utilized in the context of reinforcement learning research?"
  - "What are the command-line steps required to load the MuJoCo library and successfully import its Python bindings?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*MuJoCo stands for **Mu**lti-**Jo**int dynamics with **Co**ntact. It is a physics engine aiming to facilitate research and development in robotics, biomechanics, graphics and animation, and other areas where fast and accurate simulation is needed. [MuJoCo's official website](http://www.mujoco.org/).*

It is frequently used with the associated Python bindings `mujoco` as an environment for reinforcement learning (RL) research.

The module contains MuJoCo C/C++ library and its Python bindings.

## Library
In order to access headers and binaries, load the module:

```bash
module load mujoco
```

## Python bindings
To discover which are the compatible Python versions, run:

```bash
module spider mujoco/2.2.2
```

1.  Load the required modules.
    ```bash
    module load mujoco python
    ```

2.  Import MuJoCo.
    ```bash
    python -c "import mujoco"
    ```

!!! note
    If the command displays nothing, the import was successful.