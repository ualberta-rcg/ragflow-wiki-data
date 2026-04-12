---
title: "OpenSim"
slug: "opensim"
lang: "base"

source_wiki_title: "OpenSim"
source_hash: "fe9a0ffcb5f0fef9109d3c6135b80fd3"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:05:00.141799+00:00"

tags:
  - software

keywords:
  - "OpenSim Moco"
  - "musculoskeletal structures"
  - "OpenSim"
  - "dynamic simulations"
  - "Python and Matlab APIs"

questions:
  - "What is the primary purpose of the OpenSim software system and what key components does it include?"
  - "How do you configure and verify the setup of OpenSim for use within Matlab on a cluster?"
  - "What are the necessary prerequisites and module dependencies for using the OpenSim package in Python?"
  - "What is the primary purpose of the OpenSim software system and what key components does it include?"
  - "How do you configure and verify the setup of OpenSim for use within Matlab on a cluster?"
  - "What are the necessary prerequisites and module dependencies for using the OpenSim package in Python?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Description

"[OpenSim](https://simtk.org/projects/opensim) is a freely available, user extensible software system that lets users develop models of musculoskeletal structures and create dynamic simulations of movement." OpenSim includes Python and Matlab APIs. It is commonly used with [OpenSim Moco](https://opensim-org.github.io/opensim-moco-site/).

The OpenSim module available through our software stack includes support for OpenSim Moco, as well as bindings to enable scripting in Python or Matlab.

## Using OpenSim via Matlab

### Setup

!!! note "Matlab Setup for First Use"
    Before first use of OpenSim on a cluster, you must configure the necessary Java paths by running the following command:

    ```bash
    matlab -batch "cd ${EBROOTOPENSIM}/share/doc/OpenSim/Code/Matlab/; configureOpenSim"
    ```

    After exiting and relaunching Matlab, you can verify that OpenSim is imported by running the following in Matlab: `org.opensim.modeling.opensimCommon.GetVersion()`

## Using OpenSim via Python

In order to use the OpenSim Python package, an OpenSim module must be loaded, and a numpy package must be available through a [virtual environment](python.md#creating-and-using-a-virtual-environment) or loading a [scipy-stack](python.md#scipy-stack) module. You should subsequently be able to import the `opensim` package in Python.