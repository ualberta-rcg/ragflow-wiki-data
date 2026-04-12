---
title: "Keras"
slug: "keras"
lang: "base"

source_wiki_title: "Keras"
source_hash: "2940ff887d331c0968c2e5f4515e317b"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:23:13.603604+00:00"

tags:
  - software
  - ai-and-machine-learning

keywords:
  - "Keras"
  - "R package"
  - "virtual environment"
  - "Python"
  - "TensorFlow"

questions:
  - "What is Keras and which backend frameworks is it capable of running on top of?"
  - "What are the necessary steps to install Keras within a Python virtual environment?"
  - "How is the Keras package installed and configured for use within an R environment?"
  - "What is Keras and which backend frameworks is it capable of running on top of?"
  - "What are the necessary steps to install Keras within a Python virtual environment?"
  - "How is the Keras package installed and configured for use within an R environment?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Keras is a high-level neural networks API, written in Python and capable of running on top of TensorFlow, CNTK, or Theano. More information can be found on the [official Keras website](https://keras.io/).

!!! tip

    If you are porting a Keras program to one of our clusters, you should follow [our tutorial on the subject](tutoriel-apprentissage-machine.md).

## Installing

1.  Install [TensorFlow](tensorflow.md), CNTK, or Theano in a Python [virtual environment](python.md#creating-and-using-a-virtual-environment).
2.  Activate the Python virtual environment (named `$HOME/tensorflow` in our example).
    ```bash
    source $HOME/tensorflow/bin/activate
    ```
3.  Install Keras in your virtual environment.
    ```bash
    pip install keras
    ```

### R package

This section details how to install Keras for R and use TensorFlow as the backend.

1.  Install TensorFlow for R by following [these instructions](tensorflow.md#r-package).
2.  Follow the instructions from the parent section.
3.  Load the required modules.
    ```bash
    module load gcc/7.3.0 r/3.5.2
    ```
4.  Launch R.
    ```bash
    R
    ```
5.  In R, install the Keras package with `devtools`.
    ```r
    devtools::install_github('rstudio/keras')
    ```

Once these steps are completed, Keras is ready for use. To use the Keras package installed in your virtual environment, enter the following commands in R after the environment has been activated:

!!! warning

    Do not call `install_keras()` in R, as Keras and TensorFlow have already been installed in your virtual environment using `pip`.

```r
library(keras)
use_virtualenv(Sys.getenv('VIRTUAL_ENV'))