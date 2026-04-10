---
title: "Keras/en"
slug: "keras"
lang: "en"

source_wiki_title: "Keras/en"
source_hash: "36766f6fc55bf20bc6bbd9c981478d03"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T07:45:51.375682+00:00"

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

"Keras is a high-level neural networks API, written in Python and capable of running on top of TensorFlow, CNTK, or Theano." (Source: [Keras.io](https://keras.io/))

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

You are then good to go. Do not call `install_keras()` in R, as Keras and TensorFlow have already been installed in your virtual environment with `pip`. To use the Keras package installed in your virtual environment, enter the following commands in R after the environment has been activated.
```r
library(keras)
use_virtualenv(Sys.getenv('VIRTUAL_ENV'))
```

## References