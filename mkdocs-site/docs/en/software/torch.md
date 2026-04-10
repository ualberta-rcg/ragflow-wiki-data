---
title: "Torch/en"
slug: "torch"
lang: "en"

source_wiki_title: "Torch/en"
source_hash: "28dc4a4f8cc7c68d5f8cb29416bc5002"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T11:51:47.732175+00:00"

tags:
  - software
  - ai-and-machine-learning

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

[Torch](http://torch.ch/) is a scientific computing framework with wide support for machine learning algorithms that puts GPUs first. It is easy to use and efficient, thanks to an easy and fast scripting language, LuaJIT, and an underlying C/CUDA implementation.

Torch has a distant relationship to PyTorch. PyTorch provides a [Python](python.md) interface to software with similar functionality, but PyTorch is not dependent on Torch. See [PyTorch](pytorch.md) for instructions on using it.

!!! note "Torch and PyTorch Relationship"
    For more information on the relationship between Torch and PyTorch, refer to:
    *   https://stackoverflow.com/questions/44371560/what-is-the-relationship-between-pytorch-and-torch
    *   https://www.quora.com/What-are-the-differences-between-Torch-and-Pytorch
    *   https://discuss.pytorch.org/t/torch-autograd-vs-pytorch-autograd/1671/4

Torch depends on [CUDA](cuda.md). In order to use Torch, you must first load a CUDA module, like so:

```bash
module load cuda torch
```

## Installing Lua packages
Torch comes with the Lua package manager, named [luarocks](https://luarocks.org/). To see a list of installed packages, run:

```bash
luarocks list
```

If you need a package that does not appear on the list, use the following to install it in your own folder:

```bash
luarocks install --local --deps-mode=all <package name>
```

If after this installation you are having trouble finding the packages at runtime, then add the following command (referencing [this LuaRocks wiki page](https://github.com/luarocks/luarocks/wiki/Using-LuaRocks#Rocks_trees_and_the_Lua_libraries_path)) right before running "lua your_program.lua":

```bash
eval $(luarocks path --bin)
```

From our experience, we often find packages that do not install well with `luarocks`. If you have a package that is not installed in the default module and need help installing it, please contact our [Technical support](technical-support.md).