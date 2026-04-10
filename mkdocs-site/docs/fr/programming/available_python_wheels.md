---
title: "Available Python wheels/fr"
tags:
  []

keywords:
  []
---

Vous trouverez à la dernière section les [<i>wheels</i> Python](https://pythonwheels.com/) qui sont disponibles sur nos grappes nationales. Ces listes sont mises à jour quand un nouveau wheel est ajouté. Pour demander l'ajout ou la mise à jour d'un wheel, contactez le [soutien technique](technical-support-fr.md).
__TOC__

= Wheels faisant partie d'un module =
Certains wheels ne paraissent pas dans les tableaux parce qu'ils font partie de modules, par exemple :
* [pyarrow (Arrow)](arrow-fr#pyarrow.md)
* pyqt5 (QT)
* petsc4py (PETSc)
* [opencv_python (OpenCV)](opencv-fr#python_bindings.md)

Pour trouver ces extensions, lancez la commande

```bash
module spider <python package>
```

= Lister un wheel dans votre environnement logiciel actif =
1. Chargez l'environnement logiciel.

```bash
module load StdEnv/YYYY
```

où `YYYY` est `2020` ou `2023`

2. Cherchez un wheel en particulier.

```bash
avail_wheels <name>
```

où `name` est le nom du wheel que vous cherchez.

<span id="Available_wheels_across_all_software_environments"></span>
= Wheels disponibles dans tous nos environnements logiciels =

<tabs>
<tab name="Python 3.14">
 
</tab>
<tab name="Python 3.13">
 
</tab>
<tab name="Python 3.12">
 
</tab>
<tab name="Python 3.11">
 
</tab>
<tab name="Python 3.10">
 
</tab>
<tab name="Python 3.9 (no longer supported)">
 
</tab>
<tab name="Python 3.8 (no longer supported)">
 
</tab>
</tabs>