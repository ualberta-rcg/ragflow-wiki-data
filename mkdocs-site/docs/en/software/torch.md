---
title: "Torch/en"
slug: "torch"
lang: "en"

source_wiki_title: "Torch/en"
source_hash: "28dc4a4f8cc7c68d5f8cb29416bc5002"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:59:37.611831+00:00"

tags:
  - software
  - ai-and-machine-learning

keywords:
  - "PyTorch"
  - "luarocks"
  - "CUDA"
  - "machine learning"
  - "Torch"

questions:
  - "What is the Torch computing framework and how does it relate to PyTorch?"
  - "What are the system prerequisites for using Torch and what command is used to load it?"
  - "How do you install additional Lua packages using luarocks and resolve runtime path issues?"
  - "What is the Torch computing framework and how does it relate to PyTorch?"
  - "What are the system prerequisites for using Torch and what command is used to load it?"
  - "How do you install additional Lua packages using luarocks and resolve runtime path issues?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Torch](http://torch.ch/) is a scientific computing framework with wide support for machine learning algorithms that puts GPUs first. It is easy to use and efficient, thanks to an easy and fast scripting language, LuaJIT, and an underlying C/CUDA implementation.

Torch has a distant relationship to PyTorch.
!!! note
    For some attempts to explain the connection between PyTorch and Torch, refer to:
    *   [What is the relationship between PyTorch and Torch?](https://stackoverflow.com/questions/44371560/what-is-the-relationship-between-pytorch-and-torch)
    *   [What are the differences between Torch and Pytorch?](https://www.quora.com/What-are-the-differences-between-Torch-and-Pytorch)
    *   [Torch autograd vs PyTorch autograd](https://discuss.pytorch.org/t/torch-autograd-vs-pytorch-autograd/1671/4)

PyTorch provides a [Python](python.md) interface to software with similar functionality, but PyTorch is not dependent on Torch. See [PyTorch](pytorch.md) for instructions on using it.

Torch depends on [CUDA](cuda.md). In order to use Torch you must first load a CUDA module, like so:

```bash
module load cuda torch
```

## Installing Lua packages
Torch comes with the Lua package manager, named [luarocks](https://luarocks.org/). Run
`luarocks list`
to see a list of installed packages.

If you need some package which does not appear on the list, use the following to install it in your own folder:

```bash
luarocks install --local --deps-mode=all <package name>
```

If after this installation you are having trouble finding the packages at runtime, then add the following command right before running "lua your_program.lua":

```bash
eval $(luarocks path --bin)
```

!!! note
    This recommendation for resolving runtime path issues is based on the [LuaRocks Wiki](https://github.com/luarocks/luarocks/wiki/Using-LuaRocks#Rocks_trees_and_the_Lua_libraries_path).

By experience, we often find packages that do not install well with `luarocks`. If you have a package that is not installed in the default module and need help installing it, please contact our [Technical support](technical-support.md).