---
title: "MuJoCo/en"
slug: "mujoco"
lang: "en"

source_wiki_title: "MuJoCo/en"
source_hash: "0d01aa9e79bae01823ce962c3d8ba2ad"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:33:35.005493+00:00"

tags:
  - software

keywords:
  - "MuJoCo"
  - "physics engine"
  - "Python bindings"
  - "reinforcement learning"
  - "robotics"

questions:
  - "What does MuJoCo stand for and what are its primary fields of application?"
  - "How is MuJoCo frequently utilized in the context of reinforcement learning research?"
  - "What are the specific command-line steps required to load the MuJoCo library and verify its Python bindings?"
  - "What does MuJoCo stand for and what are its primary fields of application?"
  - "How is MuJoCo frequently utilized in the context of reinforcement learning research?"
  - "What are the specific command-line steps required to load the MuJoCo library and verify its Python bindings?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*MuJoCo stands for **Mu**lti-**Jo**int dynamics with **Co**ntact. It is a physics engine aiming to facilitate research and development in robotics, biomechanics, graphics and animation, and other areas where fast and accurate simulation is needed.*

It is frequently used with the associated Python bindings `mujoco` as an environment for reinforcement learning (RL) research.

The module contains the MuJoCo C/C++ library and its Python bindings.

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
    If the command displays nothing, the import was successful.