---
title: "MuJoCo/en"
tags:
  - software

keywords:
  []
---

*MuJoCo stands for **Mu**lti-**Jo**int dynamics with **Co**ntact. It is a physics engine aiming to facilitate research and development in robotics, biomechanics, graphics and animation, and other areas where fast and accurate simulation is needed.<ref>http://www.mujoco.org/</ref>*

It is frequently used with the associated Python bindings `mujoco` as an environment for reinforcement learning (RL) research.

The module contains MuJoCo C/C++ library and its Python bindings.

== Library == 
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

```bash
python -c "import mujoco"
```

If the command displays nothing, the import was successful.