---
title: "Tensorboard"
slug: "tensorboard"
lang: "base"

source_wiki_title: "Tensorboard"
source_hash: "4c33212e96a55cb45607ee7bac0cadc5"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T11:46:11.232880+00:00"

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

On clusters where [JupyterHub](jupyterhub.md) is available, you can launch TensorBoard by clicking on the following icon on an active launcher tab:
This will open the application on a new tab on your web browser. Switch to that tab to start using TensorBoard.

Upon launching TensorBoard on JupyterHub, a directory `$HOME/tensorboard_logs` will be created. This is the location where TensorBoard will look for data to display on your web browser.

!!! note
    You must make sure any calls to TensorBoard in your code write data to this directory. Failing to do so will result in no data being displayed on the TensorBoard tab on your browser.

You can change the location of this directory by adding `export TENSORBOARD_LOGDIR=/some/other/path` in your `.bashrc`.

For detailed examples on the many uses of TensorBoard, see the official documentation for your preferred AI framework:

*   [PyTorch](https://docs.pytorch.org/tutorials/intermediate/tensorboard_tutorial.html)
*   [TensorFlow](https://www.tensorflow.org/tensorboard/get_started)
*   [Jax](https://docs.jaxstack.ai/en/latest/JAX_visualizing_models_metrics.html)