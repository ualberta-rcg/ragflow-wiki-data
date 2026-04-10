---
title: "Recent changes to the software environment"
slug: "recent_changes_to_the_software_environment"
lang: "base"

source_wiki_title: "Recent changes to the software environment"
source_hash: "d0d5e93fef847aca67ee4171e921d6d9"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T10:45:49.452160+00:00"

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

Installation of software packages within the Alliance software environment is always performed using scripts. We use multiple tools, including [EasyBuild](https://easybuild.io/), [Gentoo Overlays](https://overlays.gentoo.org/) (starting in 2020), and [NixOS](https://github.com/NixOS/nixpkgs) (formerly). This software environment can be [used on any computer in the world](accessing-cvmfs.md) thanks to [CVMFS](https://cvmfs.readthedocs.io/en/stable/).

We also track all changes and new installations made to the software environment through [Git](git.md), and you can see a list of recent changes in the links below.

## Changes to software installed as modules

*   [Changes to the core modules and modules installed for the AVX2 CPU architecture](https://github.com/ComputeCanada/easybuild-easyconfigs-installed-avx2/commits/main)
*   [Changes to the modules installed for the AVX512 CPU architecture](https://github.com/ComputeCanada/easybuild-easyconfigs-installed-avx512/commits/main)
*   [Changes to the modules installed for the AVX CPU architecture](https://github.com/ComputeCanada/easybuild-easyconfigs-installed-avx/commits/main)
*   [Changes to the modules installed for the SSE3 CPU architecture](https://github.com/ComputeCanada/easybuild-easyconfigs-installed-sse3/commits/main)

## Other changes

*   [Changes to the primary configuration files](https://github.com/ComputeCanada/software-stack-config/commits/main)
*   [Changes to the EasyBuild configuration](https://github.com/ComputeCanada/easybuild-computecanada-config/commits/main)
*   [Changes to custom modules and scripts](https://github.com/ComputeCanada/software-stack-custom/commits/main)
*   [Changes to the core of the Gentoo layer, for the module `gentoo/YYYY`, used with `StdEnv/2020` and `StdEnv/2023`](https://github.com/ComputeCanada/gentoo-overlay/commits/main)
*   !!! warning "Deprecated"
    [Changes to the core of the Nix layer, for the module `nixpkgs/16.09`, used in `StdEnv/2016.4`, `StdEnv/2018.3`](https://github.com/ComputeCanada/nixpkgs/commits/computecanada-16.09)