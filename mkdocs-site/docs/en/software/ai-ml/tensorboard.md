---
title: "Tensorboard/en"
slug: "tensorboard"
lang: "en"

source_wiki_title: "Tensorboard/en"
source_hash: "8a774644309968d3b6e8dfae2d825475"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T11:46:21.365181+00:00"

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

TensorBoard is a suite of web applications for inspecting and understanding your AI and Machine Learning runs. It includes visual tools to track performance and evaluation metrics, profile code, explore intermediate layers inside models, visualize embeddings and more. Originally built for [TensorFlow](https://www.tensorflow.org/tensorboard/get_started), it also supports other frameworks such as [PyTorch](https://docs.pytorch.org/tutorials/intermediate/tensorboard_tutorial.html) and [Jax](https://docs.jaxstack.ai/en/latest/JAX_visualizing_models_metrics.html).

## On JupyterHub

On clusters where [JupyterHub](jupyterhub.md) is available, you can launch Tensorboard by clicking on the relevant icon on an active launcher tab. This will open the application in a new tab in your web browser. Switch to that tab to start using Tensorboard.

!!! important "Tensorboard Log Directory"
    Upon launching Tensorboard on JupyterHub, a directory `$HOME/tensorboard_logs` will be created. This is the location where Tensorboard will look for data to display in your web browser, so you must ensure any calls to Tensorboard in your code write data to this directory. Failing to do so will result in no data being displayed on the Tensorboard tab in your browser.

    You can change the location of this directory by adding `export TENSORBOARD_LOGDIR=/some/other/path` to your `.bashrc` file.

For detailed examples on the many uses of Tensorboard, see the official documentation for your preferred AI framework:

*   [PyTorch](https://docs.pytorch.org/tutorials/intermediate/tensorboard_tutorial.html)
*   [TensorFlow](https://www.tensorflow.org/tensorboard/get_started)
*   [Jax](https://docs.jaxstack.ai/en/latest/JAX_visualizing_models_metrics.html)