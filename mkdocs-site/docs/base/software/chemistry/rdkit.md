---
title: "RDKit"
slug: "rdkit"
lang: "base"

source_wiki_title: "RDKit"
source_hash: "bfac83756f134f02a8a690c087570ca3"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:57:28.937572+00:00"

tags:
  []

keywords:
  - "cheminformatics"
  - "RDKit"
  - "virtual environment"
  - "Python bindings"
  - "module"

questions:
  - "How can a user search for and find specific available versions of the RDKit module?"
  - "What are the necessary steps to properly load RDKit as a dependency when using a Python virtual environment?"
  - "How can a user troubleshoot and resolve a \"ModuleNotFoundError\" when attempting to import RDKit?"
  - "How can a user search for and find specific available versions of the RDKit module?"
  - "What are the necessary steps to properly load RDKit as a dependency when using a Python virtual environment?"
  - "How can a user troubleshoot and resolve a \"ModuleNotFoundError\" when attempting to import RDKit?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[RDKit](https://www.rdkit.org/) is a collection of cheminformatics and machine-learning software written in C++ and Python.

## Available versions
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

## Python bindings
The module contains bindings for multiple Python versions. To discover which are the compatible Python versions, run:
```bash
module spider rdkit/X.Y.Z
```

where `X.Y.Z` represents the desired version.

### rdkit as a Python package dependency
When `rdkit` is a dependency of another package, the dependency needs to be fulfilled:

1. Deactivate any Python virtual environment.
```bash
test $VIRTUAL_ENV && deactivate
```

!!! note
    If you had a virtual environment activated, it is important to deactivate it first, then load the module, before reactivating your virtual environment.

2. Load the module.
```bash
module load rdkit/2024.03.5 python/3.12
```

3. Check that it is visible by `pip`
```console
$ pip list | grep rdkit
rdkit            2024.3.5
```

```bash
python -c 'import rdkit'
```
If no errors are raised, then everything is OK!

4. [Create a virtual environment and install your packages](../python.md#creating-and-using-a-virtual-environment).

## Troubleshooting

### ModuleNotFoundError: No module named 'rdkit'
If `rdkit` is not accessible, you may get the following error when importing it:
```
ModuleNotFoundError: No module named 'rdkit'
```

Possible solutions:
* check which Python versions are compatible with your loaded RDKit module using `module spider rdkit/X.Y.Z`. Once a compatible Python module is loaded, check that `python -c 'import rdkit'` works.
* load the module before activating your virtual environment: please see the [rdkit as a package dependency](#rdkit-as-a-python-package-dependency) section above.

See also [ModuleNotFoundError: No module named 'X'](../python.md#modulenotfounderror-no-module-named-x).