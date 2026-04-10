---
title: "Keras"
tags:
  - software
  - ai-and-machine-learning

keywords:
  []
---

"Keras is a high-level neural networks API, written in Python and capable of running on top of TensorFlow, CNTK, or Theano."<ref>https://keras.io/</ref>

If you are porting a Keras program to one of our clusters, you should follow [our tutorial on the subject](tutoriel-apprentissage-machine-en.md).

==Installing== 

#Install [TensorFlow](tensorflow.md), CNTK, or Theano in a Python [virtual environment](python#creating_and_using_a_virtual_environment.md).
#Activate the Python virtual environment (named <tt>$HOME/tensorflow</tt> in our example).
#:
```bash
source $HOME/tensorflow/bin/activate
```

#Install Keras in your virtual environment.
#:
```bash
pip install keras
```

=== R package === 

This section details how to install Keras for R and use TensorFlow as the backend.

#Install TensorFlow for R by following [these instructions](tensorflow#r_package.md).
#Follow the instructions from the parent section.
#Load the required modules. 
#:
```bash
module load gcc/7.3.0 r/3.5.2
```

# Launch R.
#:
```bash
R
```

#In R, install the Keras package with `devtools`. 
#:<syntaxhighlight lang='r'>
devtools::install_github('rstudio/keras')
</syntaxhighlight>

You are then good to go. Do not call `install_keras()` in R, as Keras and TensorFlow have already been installed in your virtual environment with `pip`. To use the Keras package installed in your virtual environment, enter the following commands in R after the environment has been activated.
<syntaxhighlight lang='r'>
library(keras)
use_virtualenv(Sys.getenv('VIRTUAL_ENV'))
</syntaxhighlight>

== References ==