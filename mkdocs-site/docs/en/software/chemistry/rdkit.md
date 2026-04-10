---
title: "RDKit/en"
tags:
  []

keywords:
  []
---

[RDKit](https://www.rdkit.org/) is a collection of cheminformatics and machine-learning software written in C++ and Python.

__FORCETOC__

= Available versions =
`rdkit` C++ libraries and Python bindings are available as a module.

You can find available versions with:

```bash
module spider rdkit
```

and look for more information on a specific version with:

```bash
module spider rdkit/X.Y.Z
```

where `X.Y.Z` is the exact desired version, for instance `2024.03.5`.

= Python bindings =
The module contains bindings for multiple Python versions. To discover which are the compatible Python versions, run:

```bash
module spider rdkit/X.Y.Z
```

where <TT>X.Y.Z</TT> represents the desired version.

## rdkit as a Python package dependency 
When `rdkit` is a dependency of another package, the dependency needs to be fulfilled:

1. Deactivate any Python virtual environment.

```bash
test $VIRTUAL_ENV && deactivate
```

<b>Note:</b> If you had a virtual environment activated, it is important to deactivate it first, then load the module, before reactivating your virtual environment.

2. Load the module.

```bash
module load rdkit/2024.03.5 python/3.12
```

3. Check that it is visible by `pip`

```bash

```
 grep rdkit
|result=
rdkit            2024.3.5
}}

```bash
python -c 'import rdkit'
```

If no errors are raised, then everything is OK!

4. [Create a virtual environment and install your packages](python#creating_and_using_a_virtual_environment.md).

= Troubleshooting =

## ModuleNotFoundError: No module named 'rdkit' 
If `rdkit` is not accessible, you may get the following error when importing it:
`
ModuleNotFoundError: No module named 'rdkit'
`

Possible solutions:
* check which Python versions are compatible with your loaded RDKit module using `module spider rdkit/X.Y.Z`. Once a compatible Python module is loaded, check that `python -c 'import rdkit'` works.
* load the module before activating your virtual environment: please see the  [rdkit as a package dependency](rdkit#rdkit_as_a_python_package_dependency.md) section above.

See also [ModuleNotFoundError: No module named 'X'](python#modulenotfounderror:_no_module_named_'x'.md).