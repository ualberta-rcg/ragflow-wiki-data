---
title: "RDKit/fr"
tags:
  []

keywords:
  []
---

[RDKit](https://www.rdkit.org/) est un ensemble d'applications pour la chimie computationnelle et l'apprentissage machine qui sont écrites en C++ et en Python.

__FORCETOC__

= Versions disponibles =
Les bibliothèques C++ et les interfaces Python sont disponibles via un module.

Pour connaître les versions disponibles, utilisez

```bash
module spider rdkit
```

Pour l'information sur une version particulière, utilisez

```bash
module spider rdkit/X.Y.Z
```

où `X.Y.Z` est la version recherchée, par exemple `2024.03.5`.

= Interfaces (<i>bindings</i>) Python  =
Le module contient des interfaces pour plusieurs versions de Python. Pour connaître les versions disponibles, utilisez

```bash
module spider rdkit/X.Y.Z
```

où <TT>X.Y.Z</TT> est la version que vous voulez.

## Dépendance 
Quand un autre wheel dépend de `rdkit`, la dépendance doit être satisfaite.

1. Désactivez tout environnement virtuel Python.

```bash
test $VIRTUAL_ENV && deactivate
```

<b>Remarque</b> : Si un environnement virtuel est actif, il est important de le désactiver avant de charger le module. Une fois le module chargé, activez à nouveau votre environnement virtuel.

2. Chargez le module.

```bash
module load rdkit/2024.03.5 python/3.12
```

3. Vérifiez qu'il est visible par `pip` avec

```bash

```
 grep rdkit
|result=
rdkit            2024.3.5
}}
et que le module Python que vous avez chargé lui a accès, avec

```bash
python -c 'import rdkit'
```

Si aucune erreur ne survient, le problème devrait être réglé.

```bash
python -c 'import rdkit'
```

Si aucune erreur ne survient, tout va bien.

4. [Créez un environnement virtuel](python-fr#créer_et_utiliser_un_environnement_virtuel.md) et installez les paquets.

= Dépannage =

## Message <i>ModuleNotFoundError: No module named 'rdkit'</i> 
Ce message peut survenir si `rdkit` n’est pas disponible.
`
ModuleNotFoundError: No module named 'rdkit'
`

<b>Solutions possibles</b>
* Vérifiez quelles versions de Python sont compatibles avec le module RDKit chargé avec `module spider rdkit/X.Y.Z`. Une fois qu'un module Python compatible est chargé, vérifiez que `python -c 'import rdkit'` fonctionne.
* Chargez le module avant d'activer votre environnement virtuel; voir  [Dépendance ci-dessus](rdkit-fr#dépendance.md).

Voir aussi [ModuleNotFoundError: No module named 'X'](python-fr#message_modulenotfounderror:_no_module_named_'x'.md).