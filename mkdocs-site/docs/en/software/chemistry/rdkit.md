---
title: "RDKit/en"
slug: "rdkit"
lang: "en"

source_wiki_title: "RDKit/en"
source_hash: "c1e426b899bd2872ed5923be40162ebd"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T10:41:46.820290+00:00"

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
```bash
pip list | grep rdkit
# Expected output:
# rdkit            2024.3.5
```

```bash
python -c 'import rdkit'
```
If no errors are raised, then everything is OK!

4. [Create a virtual environment and install your packages](python.md#creating-and-using-a-virtual-environment).

## Troubleshooting

### ModuleNotFoundError: No module named 'rdkit'
If `rdkit` is not accessible, you may get the following error when importing it:
```python
ModuleNotFoundError: No module named 'rdkit'
```

Possible solutions:
* check which Python versions are compatible with your loaded RDKit module using `module spider rdkit/X.Y.Z`. Once a compatible Python module is loaded, check that `python -c 'import rdkit'` works.
* load the module before activating your virtual environment: please see the [rdkit as a Python package dependency](#rdkit-as-a-python-package-dependency) section above.

See also [ModuleNotFoundError: No module named 'X'](python.md#modulenotfounderror-no-module-named-x).