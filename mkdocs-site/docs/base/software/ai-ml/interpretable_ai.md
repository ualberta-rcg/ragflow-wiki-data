---
title: "Interpretable AI"
slug: "interpretable_ai"
lang: "base"

source_wiki_title: "Interpretable AI"
source_hash: "9a26a05a54347c66cf72b9a1cb5116d4"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:09:14.157357+00:00"

tags:
  []

keywords:
  - "Alliance clusters"
  - "Installation"
  - "Interpretable AI"
  - "Julia"
  - "Python"

questions:
  - "What is Interpretable AI (IAI) and how can academic users access its licensing on Alliance systems?"
  - "What are the necessary steps to install and configure IAI using Python and Julia on an Alliance cluster?"
  - "What crucial initialization code must be included in a Python script before importing the IAI package?"
  - "What is Interpretable AI (IAI) and how can academic users access its licensing on Alliance systems?"
  - "What are the necessary steps to install and configure IAI using Python and Julia on an Alliance cluster?"
  - "What crucial initialization code must be included in a Python script before importing the IAI package?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Interpretable AI](http://interpretable.ai) (IAI) is a suite of machine learning tools that aim for full transparency and understandability by humans. IAI provides a Python interface for their algorithms and can only be used under license. IAI provides a free license for academic use which can be accessed on Alliance systems. For licensing issues, please contact [technical support](technical-support.md).

## Installation on Alliance clusters
1. Go to the [IAI download page](https://docs.interpretable.ai/stable/download/) and download the latest release of IAI. Be sure to select "Linux" and the correct version of Julia (1.11.3 in these instructions).

2. Upload the files from Step 1 to the cluster of your choice. Unzip the file, note the location of the files. There should be a `sys.so` and `Artifacts.toml` file in the directory. In this example, we'll say `/path/to/sysimage/`

3. Load requisite modules:
    ```bash
    module load StdEnv/2023 python/3.11.5 scipy-stack/2025a julia/1.11.3
    ```

4. Make a Python virtual environment and install IAI:
    ```bash
    virtualenv --no-download iaiENV && source iaiENV/bin/activate
    pip install --no-index --upgrade pip
    pip install interpretableai
    ```

5. Install IAI in Julia and build PyCall to work in your virtual environment. Make sure your virtual environment is active before launching Julia:
    ```bash
    (iaiENV) $ julia
    ```
    ```julia
    julia> import Pkg; Pkg.add(url="https://github.com/InterpretableAI/IAISystemImages.jl")
    julia> import IAISystemImages
    julia> IAISystemImages.install_artifacts("/path/to/sysimage/Artifacts.toml")
    julia> using Pkg, PyCall
    julia> ENV["PYTHON"] = joinpath(ENV["VIRTUAL_ENV"], "bin", "python")
    julia> Pkg.build("PyCall")
    julia> exit()
    ```

6. Finish IAI setup in Python:
    ```bash
    (iaiENV) $ python
    ```
    ```python
    from julia import Julia
    Julia(sysimage='/path/to/sysimage/sys.so')
    import interpretableai
    interpretableai.install()
    ```

7. Import IAI for use in your Python scripts
    ```python
    from interpretableai import iai
    ```

### IMPORTANT NOTE
!!! warning "Important Note"
    Any Python script using the `interpretableai` package has to include setting up Julia to run with the IAI system image. This means the following code must be included before importing IAI in your Python scripts.
    ```python
    from julia import Julia
    Julia(sysimage='/path/to/sysimage/sys.so')
    ```

It is also a good idea to disable automatic updating in your job script:
```bash
export IAI_DISABLE_UPDATE_CHECK=true