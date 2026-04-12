---
title: "Arrow"
slug: "arrow"
lang: "base"

source_wiki_title: "Arrow"
source_hash: "74cf23f2185610a29728bfa6f9f5eb1d"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:30:39.662810+00:00"

tags:
  - software

keywords:
  - "pyarrow"
  - "Apache Arrow"
  - "PyArrow"
  - "Python virtual environment"
  - "R bindings"
  - "Troubleshooting"
  - "install bindings"
  - "load modules"
  - "Parquet format"
  - "ModuleNotFoundError"
  - "arrow"
  - "Arrow module"
  - "library"
  - "in-memory data"
  - "R"

questions:
  - "What is Apache Arrow and what are its primary features for handling in-memory data?"
  - "How do you check for compatible Python versions and verify the installation of the PyArrow module?"
  - "What are the required steps and environment variables needed to install and load the Arrow bindings in R?"
  - "What are the two main reasons that cause the \"ModuleNotFoundError: No module named 'pyarrow'\" error to occur?"
  - "What steps must be taken regarding Python virtual environments to properly load the Arrow module?"
  - "How can a user verify that the pyarrow package is successfully installed and accessible after loading the necessary modules?"
  - "How are the arrow bindings installed in R according to the provided instructions?"
  - "Which specific environment modules must be loaded before using the arrow bindings?"
  - "What command is used to load the arrow library within R after the setup is complete?"
  - "What are the two main reasons that cause the \"ModuleNotFoundError: No module named 'pyarrow'\" error to occur?"
  - "What steps must be taken regarding Python virtual environments to properly load the Arrow module?"
  - "How can a user verify that the pyarrow package is successfully installed and accessible after loading the necessary modules?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Apache Arrow](https://arrow.apache.org/) is a cross-language development platform for in-memory data. It uses a standardized language-independent columnar memory format for flat and hierarchical data, organized for efficient analytic operations. It also provides computational libraries and zero-copy streaming messaging and interprocess communication. Languages currently supported include C, C++, C#, Go, Java, JavaScript, MATLAB, Python, R, Ruby, and Rust.

## CUDA
Arrow is also available with CUDA.
```bash
module load gcc arrow/X.Y.Z cuda
```
where `X.Y.Z` represent the desired version.

## Python Bindings
The module contains bindings for multiple Python versions.
To discover which are the compatible Python versions, run
```bash
module spider arrow/X.Y.Z
```
where `X.Y.Z` represent the desired version.

Or search *pyarrow* directly, by running
```bash
module spider pyarrow
```

### PyArrow
The Arrow Python bindings (also named *PyArrow*) have first-class integration with NumPy, Pandas, and built-in Python objects. They are based on the C++ implementation of Arrow.

1.  Load the required modules.
    ```bash
    module load gcc arrow/X.Y.Z python/3.11
    ```
    where `X.Y.Z` represent the desired version.

2.  Import PyArrow.
    ```bash
    python -c "import pyarrow"
    ```

If the command displays nothing, the import was successful.

For more information, see the [Arrow Python](https://arrow.apache.org/docs/python/) documentation.

#### Fulfilling other Python Package Dependency
Other Python packages depend on PyArrow in order to be installed.
With the `arrow` module loaded, your package dependency for `pyarrow` will be satisfied.
```bash
pip list | grep pyarrow
```
```text+output
pyarrow    17.0.0
```

If `pip list` shows an entry, then `pyarrow` is available and seen by `pip`. Otherwise, in case of no entry, `pyarrow` is not available.

#### Apache Parquet Format
The [Parquet](http://parquet.apache.org/) file format is available.

To import the Parquet module, execute the previous steps for `pyarrow`, then run
```bash
python -c "import pyarrow.parquet"
```

If the command displays nothing, the import was successful.

## R Bindings
The Arrow package exposes an interface to the Arrow C++ library to access many of its features in R. This includes support for analyzing large, multi-file datasets ([open_dataset()](https://arrow.apache.org/docs/r/reference/open_dataset.html)), working with individual Parquet files ([read_parquet()](https://arrow.apache.org/docs/r/reference/read_parquet.html), [write_parquet()](https://arrow.apache.org/docs/r/reference/write_parquet.html)) and Feather files ([read_feather()](https://arrow.apache.org/docs/r/reference/read_feather.html), [write_feather()](https://arrow.apache.org/docs/r/reference/write_feather.html)), as well as lower-level access to the Arrow memory and messages.

### Installation
1.  Load the required modules.
    ```bash
    module load StdEnv/2020 gcc/9.3.0 arrow/8 r/4.1 boost/1.72.0
    ```

2.  Specify the local installation directory.
    ```bash
    mkdir -p ~/.local/R/$EBVERSIONR/
    export R_LIBS=~/.local/R/$EBVERSIONR/
    ```

3.  Export the required variables to ensure you are using the system installation.
    ```bash
    export PKG_CONFIG_PATH=$EBROOTARROW/lib/pkgconfig
    export INCLUDE_DIR=$EBROOTARROW/include
    export LIB_DIR=$EBROOTARROW/lib
    ```

4.  Install the bindings.
    ```R
    R -e 'install.packages("arrow", repos="https://cloud.r-project.org/")'
    ```

### Usage
After the bindings are installed, they have to be loaded.

1.  Load the required modules.
    ```bash
    module load StdEnv/2020 gcc/9.3.0 arrow/8 r/4.1
    ```

2.  Load the library.
    ```R
    R -e "library(arrow)"
    ```
    ```text+output
    > library("arrow")
    Attaching package: ‘arrow’
    ```

For more information, see the [Arrow R documentation](https://arrow.apache.org/docs/r/index.html)

## Troubleshooting

## This is a Normal Error Generated by This Dummy Wheel
See [This is a normal error generated by this dummy wheel](dummywheel.md#this-is-a-normal-error-generated-by-this-dummy-wheel).

## ModuleNotFoundError: No Module Named 'pyarrow'
When importing the `pyarrow`, one may get the following error:
```python
python -c "import pyarrow"
```
```text+error
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'pyarrow'
```

This usually means one of the two following cases:
1.  [A module for Arrow was not loaded](#module-arrow-not-loaded)
2.  [A Python module was not loaded](#python-module-not-loaded)

### Module Arrow Not Loaded
Find a *compatible* `arrow` module and load it. See [PyArrow](#pyarrow).

### Python Module Not Loaded
When omitting to load a Python module, and activating a virtual environment, the Python bindings will not be available, hence resulting in `pyarrow` not seen.

To remedy:

1.  Deactivate any Python virtual environment.
    ```bash
    test $VIRTUAL_ENV && deactivate
    ```

!!! note
    If you had a virtual environment activated, it is important to deactivate it first, then load the module, before reactivating your virtual environment.

2.  Load the module.
    ```bash
    module load arrow/x.y.z python/x.y.z
    ```

3.  Check that it is visible by `pip`
    ```bash
    pip list | grep pyarrow
    ```
    ```text+output
    pyarrow            23.0.1
    ```
    and is accessible for your currently loaded Python module.
    ```python
    python -c 'import pyarrow'
    ```
    If no errors are raised, then everything is OK!