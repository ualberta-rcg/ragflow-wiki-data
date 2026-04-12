---
title: "Tensorboard"
slug: "tensorboard"
lang: "base"

source_wiki_title: "Tensorboard"
source_hash: "4c33212e96a55cb45607ee7bac0cadc5"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:55:25.214224+00:00"

tags:
  []

keywords:
  - "JupyterHub"
  - "tensorboard_logs"
  - "AI frameworks"
  - "Machine Learning"
  - "TensorBoard"

questions:
  - "What is TensorBoard and what are its primary functions for AI and Machine Learning runs?"
  - "How can a user launch the TensorBoard application when working on a cluster with JupyterHub?"
  - "What is the default directory for TensorBoard logs on JupyterHub, and how can this location be modified?"
  - "What is TensorBoard and what are its primary functions for AI and Machine Learning runs?"
  - "How can a user launch the TensorBoard application when working on a cluster with JupyterHub?"
  - "What is the default directory for TensorBoard logs on JupyterHub, and how can this location be modified?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

TensorBoard is a suite of web applications for inspecting and understanding your AI and Machine Learning runs. It includes visual tools to track performance and evaluation metrics, profile code, explore intermediate layers inside models, visualize embeddings and more. Originally built for [TensorFlow](https://www.tensorflow.org/tensorboard/get_started), it also supports other frameworks such as [PyTorch](https://docs.pytorch.org/tutorials/intermediate/tensorboard_tutorial.html) and [Jax](https://docs.jaxstack.ai/en/latest/JAX_visualizing_models_metrics.html).

## On JupyterHub

On clusters where [JupyterHub](../../interactive/jupyterhub.md) is available, you can launch TensorBoard by clicking on an icon on an active launcher tab. This will open the application in a new tab in your web browser. Switch to that tab to start using TensorBoard.

!!! note "TensorBoard Log Directory"
    Upon launching TensorBoard on JupyterHub, a directory `$HOME/tensorboard_logs` will be created. This is the default location where TensorBoard will look for data to display in your web browser, so you must ensure any calls to TensorBoard in your code write data to this directory. Failing to do so will result in no data being displayed in the TensorBoard tab in your browser.

    You can change the default location of this directory by adding the following to your `.bashrc` file:

    ```bash
    export TENSORBOARD_LOGDIR=/some/other/path
    ```

For detailed examples on the many uses of TensorBoard, see the official documentation for your preferred AI framework:

*   [PyTorch](https://docs.pytorch.org/tutorials/intermediate/tensorboard_tutorial.html)
*   [TensorFlow](https://www.tensorflow.org/tensorboard/get_started)
*   [Jax](https://docs.jaxstack.ai/en/latest/JAX_visualizing_models_metrics.html)