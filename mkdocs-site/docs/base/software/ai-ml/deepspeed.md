---
title: "Deepspeed"
slug: "deepspeed"
lang: "base"

source_wiki_title: "Deepspeed"
source_hash: "bfb82f676ae903cd77b8b67d759152a6"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:53:05.207803+00:00"

tags:
  []

keywords:
  - "deepspeed_stage_3"
  - "ZeRO stage 3"
  - "PyTorch Lightning"
  - "data parallel"
  - "ds_config.json"
  - "Net"
  - "ConvPart"
  - "DeepSpeedCPUAdam"
  - "Deepspeed"
  - "progress_bar_refresh_rate"
  - "mixed-precision training"
  - "pl.Trainer"
  - "transforms"
  - "deepspeed offload"
  - "Zero Redundancy Optimizer"
  - "Data Parallelism"
  - "nn.Linear"
  - "FusedAdam"
  - "CPU offloading"
  - "MLPPart"
  - "PyTorch"
  - "nvme test"
  - "pl.LightningModule"
  - "distributed training"
  - "GPU"
  - "Neural Network"
  - "CIFAR10"
  - "NVMe offloading"
  - "Model training"
  - "argparse"
  - "half-precision (fp16)"
  - "multi-GPU and multi-node jobs"
  - "ZeRO Stage 3"
  - "DeepSpeed Stage 3"
  - "DeepSpeedStrategy"
  - "DeepSpeed"
  - "SLURM"
  - "nn.ReLU"
  - "cifar10 classification models"

questions:
  - "What is DeepSpeed and how does the Zero Redundancy Optimizer (ZeRO) enable the efficient training of massive deep learning models?"
  - "What is the recommended procedure for installing DeepSpeed and PyTorch using a Python virtual environment?"
  - "How are multi-GPU and multi-node training jobs configured and launched using DeepSpeed, Slurm scripts, and torchrun?"
  - "What specific hyperparameters and optimization settings are defined in the provided DeepSpeed JSON configuration?"
  - "How does the `pytorch-deepspeed.py` script integrate DeepSpeed with PyTorch to train a convolutional neural network on the CIFAR10 dataset?"
  - "What are the memory efficiency advantages of using ZeRO Stage 3 with PyTorch Lightning, and what are the requirements for using the `FusedAdam` optimizer?"
  - "What characterizes the job as being purely data parallel?"
  - "How does mixed-precision training utilizing half-precision (fp16) improve computational speed and memory efficiency?"
  - "What resource is recommended for finding more details on the configurable parameters used in the DeepSpeed configuration file?"
  - "Why is sharding gradients across GPUs considered more memory-efficient than pure Data Parallelism?"
  - "How does DeepSpeed's FusedAdam optimizer affect performance compared to using a native PyTorch optimizer?"
  - "What specific CUDA module version requirement must be met to successfully compile DeepSpeed's optimizers at run-time?"
  - "How does the SLURM batch script configure the environment and compute resources to ensure PyTorch Lightning executes correctly across multiple GPUs?"
  - "What specific method is implemented in the PyTorch Lightning module to shard the neural network layers for DeepSpeed Stage 3?"
  - "Which optimizer and trainer strategy are explicitly defined in the Python script to accelerate the training of the CIFAR10 model?"
  - "What are the primary benefits of enabling CPU offloading for model parameters and optimizer states in DeepSpeed ZeRO stage 3?"
  - "Why is it necessary to use the DeepSpeedCPUAdam optimizer and load a specific CUDA module version when implementing this offloading technique?"
  - "How must a SLURM batch job be configured to properly execute a PyTorch Lightning script utilizing DeepSpeed CPU offloading?"
  - "Why is the progress_bar_refresh_rate set to 0 in this configuration?"
  - "What hardware and distributed training strategy are configured for the PyTorch Lightning Trainer?"
  - "Which dataset is being loaded and what specific transformations are applied to it before training?"
  - "What are the input and output dimensions of the three linear layers defined within the MLPPart class?"
  - "How is the forward pass structured in the MLPPart module, specifically regarding the application of ReLU activation functions?"
  - "What parent class does the Net module inherit from, and what two sub-components does it initialize in its constructor?"
  - "How does ZeRO Stage 3 with NVMe offloading extend GPU memory, and what is its impact on training performance?"
  - "What specific arguments must be passed to the DeepSpeedStrategy in PyTorch Lightning to enable the offloading of model parameters and optimizer states?"
  - "What are the required SLURM configurations and environment dependencies needed to successfully execute the DeepSpeed offloading script?"
  - "What is the primary purpose of the script as indicated by the argument parser's description?"
  - "Which default hyperparameters are configured in the argument parser for training the model?"
  - "What specific neural network layer is initialized within the `ConvPart` class?"
  - "How is the neural network architecture structured and divided within the PyTorch Lightning module?"
  - "What specific DeepSpeed strategy and offloading configurations are used to optimize the training process?"
  - "Which dataset is being used for training, and how is the data preprocessed before being fed into the model?"
  - "How is the neural network architecture structured and divided within the PyTorch Lightning module?"
  - "What specific DeepSpeed strategy and offloading configurations are used to optimize the training process?"
  - "Which dataset is being used for training, and how is the data preprocessed before being fed into the model?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

DeepSpeed is a deep learning training optimization library, providing the means to train massive billion parameter models at scale. Fully compatible with PyTorch, DeepSpeed features implementations of novel memory-efficient distributed training methods, based on the Zero Redundancy Optimizer (ZeRO) concept. Through the use of ZeRO, DeepSpeed enables distributed storage and computing of different elements of a training task - such as optimizer states, model weights, model gradients and model activations - across multiple devices, including GPU, CPU, local hard disk, and/or combinations of these devices. This "pooling" of resources, notably for storage, allows models with massive amounts of parameters to be trained efficiently, across multiple nodes, without explicitly handling Model, Pipeline or Data Parallelism in your code.

## Installing DeepSpeed

Our recommendation is to install it using our provided Python [wheel](https://pythonwheels.com/) as follows:
1.  Load a Python [module](../../programming/utiliser_des_modules.md#sub-command-load), thus `module load python`
2.  Create and start a [virtual environment](../python.md#creating-and-using-a-virtual-environment).
3.  Install both PyTorch and DeepSpeed in the virtual environment with `pip install`.

```bash
# (venv) [name@server ~]
pip install --no-index torch deepspeed
```

## Multi-GPU and Multi-Node Jobs with DeepSpeed

In the example that follows, we use `deepspeed` to reproduce our [PyTorch tutorial](../pytorch.md#pytorch-with-multiple-gpus) on how to train a model with multiple GPUs distributed over multiple nodes. Notable differences are:

1.  Here we define and configure several common elements of the training task (such as optimizer, learning rate scheduler, batch size and more) in a config file, rather than using code in the main Python script.
2.  We also define DeepSpeed-specific configurations, such as what modality of ZeRO to utilize, in a config file.

```bash title="deepspeed-example.sh"
#!/bin/bash
#SBATCH --nodes 2
#SBATCH --ntasks-per-node=1
#SBATCH --gpus-per-task=2
#SBATCH --cpus-per-task=4
#SBATCH --mem=16000M
#SBATCH --time=0-00:10
#SBATCH --output=%N-%j.out

## Create a virtualenv and install deepspeed + its dependencies on all nodes ##
srun -N $SLURM_NNODES -n $SLURM_NNODES config_env.sh

export HEAD_NODE=$(hostname) # store head node's address

module load cuda/11.4

srun launch_training_deepspeed.sh
```

Where the script `config_env.sh` is:

```bash title="config_env.sh"
#!/bin/bash

module load python

virtualenv --no-download $SLURM_TMPDIR/ENV

source $SLURM_TMPDIR/ENV/bin/activate

pip install --upgrade pip --no-index

pip install --no-index torchvision deepspeed

echo "Done installing virtualenv!"
```

The script `launch_training_deepspeed.sh` is as shown below. Notice that we use [torchrun](https://pytorch.org/docs/stable/elastic/run.html) to launch our Python script. While DeepSpeed has [its own launcher](https://pytorch.org/docs/stable/elastic/run.html), we do not recommend using it at this time:

```bash title="launch_training_deepspeed.sh"
#!/bin/bash

source $SLURM_TMPDIR/env/bin/activate
export NCCL_ASYNC_ERROR_HANDLING=1

echo "r$SLURM_NODEID master: $HEAD_NODE"
echo "r$SLURM_NODEID Launching python script"

torchrun \
--nnodes $SLURM_NNODES \
--nproc_per_node 2 \ # This is the number of GPUs on each node!
--rdzv_backend c10d \
--rdzv_endpoint "$HEAD_NODE" \
pytorch-deepspeed.py --deepspeed_config="./ds_config.json"
```

Next we define and configure our training task in the file `ds_config.json`. Here we set up ZeRO stage 0, meaning ZeRO is disabled - no model parallelism will take place and this will be a purely data parallel job. We also enable mixed-precision training, where some tensors are computed/stored in half-precision (fp16) to accelerate computations using less memory space. See [DeepSpeed's documentation](https://deepspeed.readthedocs.io/en/latest/zero3.html#deepspeed.runtime.zero.config.DeepSpeedZeroConfig) for more details on all configurable parameters.

```json title="ds_config.json"
{
  "train_batch_size": 16,
  "steps_per_print": 2000,
  "optimizer": {
    "type": "Adam",
    "params": {
      "lr": 0.001,
      "betas": [
        0.8,
        0.999
      ],
      "eps": 1e-8,
      "weight_decay": 3e-7
    }
  },
  "scheduler": {
    "type": "WarmupLR",
    "params": {
      "warmup_min_lr": 0,
      "warmup_max_lr": 0.001,
      "warmup_num_steps": 1000
    }
  },
  "gradient_clipping": 1.0,
  "prescale_gradients": false,
  "fp16": {
      "enabled": true,
      "fp16_master_weights_and_grads": false,
      "loss_scale": 0,
      "loss_scale_window": 500,
      "hysteresis": 2,
      "min_loss_scale": 1,
      "initial_scale_power": 15
  },
  "wall_clock_breakdown": false,
  "zero_optimization": {
      "stage": 0,
      "allgather_partitions": true,
      "reduce_scatter": true,
      "allgather_bucket_size": 50000000,
      "reduce_bucket_size": 50000000,
      "overlap_comm": true,
      "contiguous_gradients": true,
      "cpu_offload": false
  }
}
```

And finally, `pytorch-deepspeed.py` is:

```python title="pytorch-deepspeed.py"
import os
import time
import datetime

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.backends.cudnn as cudnn

import torchvision
import torchvision.transforms as transforms
from torchvision.datasets import CIFAR10
from torch.utils.data import DataLoader

import deepspeed

import torch.distributed as dist
import torch.utils.data.distributed

import argparse

parser = argparse.ArgumentParser(description='cifar10 classification models, deepspeed test')
parser.add_argument('--local_rank', type=int, default=-1, help='local rank argument added automatically by the launcher')

parser = deepspeed.add_config_arguments(parser)

def main():

    args = parser.parse_args()

    deepspeed.init_distributed()

    class Net(nn.Module):

       def __init__(self):
          super(Net, self).__init__()

          self.conv1 = nn.Conv2d(3, 6, 5)
          self.pool = nn.MaxPool2d(2, 2)
          self.conv2 = nn.Conv2d(6, 16, 5)
          self.fc1 = nn.Linear(16 * 5 * 5, 120)
          self.fc2 = nn.Linear(120, 84)
          self.fc3 = nn.Linear(84, 10)

       def forward(self, x):
          x = self.pool(F.relu(self.conv1(x)))
          x = self.pool(F.relu(self.conv2(x)))
          x = x.view(-1, 16 * 5 * 5)
          x = F.relu(self.fc1(x))
          x = F.relu(self.fc2(x))
          x = F.relu(self.fc3(x))
          return x

    net = Net()

    parameters = filter(lambda p: p.requires_grad, net.parameters())

    transform_train = transforms.Compose([transforms.ToTensor(),transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    dataset_train = CIFAR10(root='./data', train=True, download=False, transform=transform_train)

    model_engine, optimizer, trainloader, __ = deepspeed.initialize(args=args, model=net, model_parameters=parameters, training_data=dataset_train)

    fp16 = model_engine.fp16_enabled()

    criterion = nn.CrossEntropyLoss().cuda()

    for batch_idx, (inputs, targets) in enumerate(trainloader):

       inputs = inputs.to(model_engine.local_rank)
       inputs = inputs.half()
       targets = targets.to(model_engine.local_rank)
       outputs = model_engine(inputs)
       loss = criterion(outputs, targets)

       model_engine.backward(loss)
       model_engine.step()

if __name__=='__main__':
   main()
```

## Using PyTorch Lightning

In the following tutorial, we use PyTorch Lightning as a wrapper around DeepSpeed and demonstrate how to use ZeRO Stage 3 with a pool of GPUs, with offloading to the CPU, and with offloading to the compute node's local storage.

### ZeRO on GPU

In the following example, we use ZeRO Stage 3 to train a model using a "pool" of 4 GPUs. Stage 3 means all three of: optimizer states; model parameters; and model gradients will be split (sharded) between all 4 GPUs. This is more memory-efficient than pure Data Parallelism, where we would have a full replica of the model loaded on each GPU. Using DeepSpeed's optimizer `FusedAdam` instead of a native PyTorch one, performance is comparable with pure Data Parallelism.

!!! note
    DeepSpeed's optimizers are JIT compiled at run-time and you must load the module `cuda/<version>` where **<version>** must match the version used to build the PyTorch install you are using.

```bash title="deepspeed-stage3.sh"
#!/bin/bash
#SBATCH --nodes 1
#SBATCH --gres=gpu:2          # Request 2 GPU "generic resources”.
#SBATCH --tasks-per-node=2    # Request 1 process per GPU. You will get 1 CPU per process by default. Request more CPUs with the "cpus-per-task" parameter to enable multiple data-loader workers to load data in parallel.
#SBATCH --mem=32G
#SBATCH --time=0-00:20
#SBATCH --output=%N-%j.out
#SBATCH --account=<your account>

module load python cuda # CUDA must be loaded if using a DeepSpeed optimizer
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate
pip install torchvision pytorch-lightning deepspeed --no-index

export TORCH_NCCL_ASYNC_HANDLING=1

# PyTorch Lightning will query the environment to figure out if it is running inside a SLURM batch job
# If it is, it expects the user to have requested one task per GPU.
# If you do not ask for 1 task per GPU, and you do not run your script with "srun", your job will fail!

srun python deepspeed-stage3.py  --batch_size 256
```

```python title="deepspeed-stage3.py"
import torch
from torch import nn
import torch.nn.functional as F

import pytorch_lightning as pl

import torchvision
import torchvision.transforms as transforms
from torchvision.datasets import CIFAR10
from torch.utils.data import DataLoader

from deepspeed.ops.adam import FusedAdam
from pytorch_lightning.strategies import DeepSpeedStrategy

import argparse

parser = argparse.ArgumentParser(description='cifar10 classification models deep seed stage 3 test')
parser.add_argument('--lr', default=0.1, help='')
parser.add_argument('--max_epochs', type=int, default=2, help='')
parser.add_argument('--batch_size', type=int, default=768, help='')
parser.add_argument('--num_workers', type=int, default=0, help='')

def main():
    print("Starting...")

    args = parser.parse_args()

    class ConvPart(nn.Module):
        def __init__(self):
            super(ConvPart, self).__init__()

            self.conv1 = nn.Conv2d(3, 6, 5)
            self.pool = nn.MaxPool2d(2, 2)
            self.conv2 = nn.Conv2d(6, 16, 5)
            self.relu = nn.ReLU()

        def forward(self, x):
            x = self.pool(self.relu(self.conv1(x)))
            x = self.pool(self.relu(self.conv2(x)))
            x = x.view(-1, 16 * 5 * 5)

            return x

    # Dense feedforward part of the model
    class MLPPart(nn.Module):
        def __init__(self):
            super(MLPPart, self).__init__()

            self.fc1 = nn.Linear(16 * 5 * 5, 120)
            self.fc2 = nn.Linear(120, 84)
            self.fc3 = nn.Linear(84, 10)
            self.relu = nn.ReLU()

        def forward(self, x):
            x = self.relu(self.fc1(x))
            x = self.relu(self.fc2(x))
            x = self.relu(self.fc3(x))

            return x

    class Net(pl.LightningModule):
        def __init__(self):
            super(Net, self).__init__()

            self.conv_part = ConvPart()
            self.mlp_part = MLPPart()

        def configure_sharded_model(self):
            self.block = nn.Sequential(self.conv_part, self.mlp_part)

        def forward(self, x):
            x = self.block(x)

            return x

        def training_step(self, batch, batch_idx):
            x, y = batch
            y_hat = self(x)
            loss = F.cross_entropy(y_hat, y)
            return loss

        def configure_optimizers(self):
            return FusedAdam(self.parameters())

    net = Net()

    """ Here we initialize a Trainer() explicitly with 1 node and 2 GPU.
            To make this script more generic, you can use torch.cuda.device_count() to set the number of GPUs
            and you can use int(os.environ.get("SLURM_JOB_NUM_NODES")) to set the number of nodes.
            We also set progress_bar_refresh_rate=0 to avoid writing a progress bar to the logs,
            which can cause issues due to updating logs too frequently."""

    trainer = pl.Trainer(accelerator="gpu", devices=2, num_nodes=1, strategy="deepspeed_stage_3", max_epochs = args.max_epochs)

    transform_train = transforms.Compose([transforms.ToTensor(),transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    dataset_train = CIFAR10(root='./data', train=True, download=False, transform=transform_train)

    train_loader = DataLoader(dataset_train, batch_size=args.batch_size, num_workers=args.num_workers)

    trainer.fit(net,train_loader)


if __name__=='__main__':
   main()
```

### ZeRO with Offload to CPU

In this example, we will again use ZeRO stage 3, but this time we enable offloading model parameters and optimizer states to the CPU. This means that the compute node's memory will be available to store these tensors while they are not required by any GPU computations, and additionally, optimizer steps will be computed on the CPU. For practical purposes, you can think of this as though your GPUs were gaining an extra 32 GB of memory. This takes even more pressure off from GPU memory and would allow you to increase your batch size, for example, or increase the size of the model. Using DeepSpeed's optimizer `DeepSpeedCPUAdam` instead of a native PyTorch one, performance remains at par with pure Data Parallelism.

!!! note
    DeepSpeed's optimizers are JIT compiled at run-time and you must load the module `cuda/<version>` where **<version>** must match the version used to build the PyTorch install you are using.

```bash title="deepspeed-stage3-offload-cpu.sh"
#!/bin/bash
#SBATCH --nodes 1
#SBATCH --gres=gpu:2          # Request 2 GPU "generic resources”.
#SBATCH --tasks-per-node=2    # Request 1 process per GPU. You will get 1 CPU per process by default. Request more CPUs with the "cpus-per-task" parameter to enable multiple data-loader workers to load data in parallel.
#SBATCH --mem=32G
#SBATCH --time=0-00:20
#SBATCH --output=%N-%j.out
#SBATCH --account=<your account>

module load python cuda # CUDA must be loaded if using ZeRO offloading to CPU or NVMe. Version must be the same used to compile PyTorch.
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate
pip install torchvision pytorch-lightning deepspeed --no-index

export TORCH_NCCL_ASYNC_HANDLING=1

# PyTorch Lightning will query the environment to figure out if it is running inside a SLURM batch job
# If it is, it expects the user to have requested one task per GPU.
# If you do not ask for 1 task per GPU, and you do not run your script with "srun", your job will fail!

srun python deepspeed-stage3-offload-cpu.py  --batch_size 256
```

```python title="deepspeed-stage3-offload-cpu.py"
import torch
from torch import nn
import torch.nn.functional as F

import pytorch_lightning as pl

import torchvision
import torchvision.transforms as transforms
from torchvision.datasets import CIFAR10
from torch.utils.data import DataLoader

from deepspeed.ops.adam import DeepSpeedCPUAdam
from pytorch_lightning.strategies import DeepSpeedStrategy

import argparse

parser = argparse.ArgumentParser(description='cifar10 classification models, deepspeed offload to cpu test')
parser.add_argument('--lr', default=0.1, help='')
parser.add_argument('--max_epochs', type=int, default=2, help='')
parser.add_argument('--batch_size', type=int, default=768, help='')
parser.add_argument('--num_workers', type=int, default=0, help='')


def main():
    print("Starting...")

    args = parser.parse_args()

    class ConvPart(nn.Module):
        def __init__(self):
            super(ConvPart, self).__init__()

            self.conv1 = nn.Conv2d(3, 6, 5)
            self.pool = nn.MaxPool2d(2, 2)
            self.conv2 = nn.Conv2d(6, 16, 5)
            self.relu = nn.ReLU()

        def forward(self, x):
            x = self.pool(self.relu(self.conv1(x)))
            x = self.pool(self.relu(self.conv2(x)))
            x = x.view(-1, 16 * 5 * 5)

            return x

    # Dense feedforward part of the model
    class MLPPart(nn.Module):
        def __init__(self):
            super(MLPPart, self).__init__()

            self.fc1 = nn.Linear(16 * 5 * 5, 120)
            self.fc2 = nn.Linear(120, 84)
            self.fc3 = nn.Linear(84, 10)
            self.relu = nn.ReLU()

        def forward(self, x):
            x = self.relu(self.fc1(x))
            x = self.relu(self.fc2(x))
            x = self.relu(self.fc3(x))

            return x

    class Net(pl.LightningModule):
        def __init__(self):
            super(Net, self).__init__()

            self.conv_part = ConvPart()
            self.mlp_part = MLPPart()

        def configure_sharded_model(self):
            self.block = nn.Sequential(self.conv_part, self.mlp_part)

        def forward(self, x):
            x = self.block(x)

            return x

        def training_step(self, batch, batch_idx):
            x, y = batch
            y_hat = self(x)
            loss = F.cross_entropy(y_hat, y)
            return loss

        def configure_optimizers(self):
            return DeepSpeedCPUAdam(self.parameters())

    net = Net()

    """ Here we initialize a Trainer() explicitly with 1 node and 2 GPU.
            To make this script more generic, you can use torch.cuda.device_count() to set the number of GPUs
            and you can use int(os.environ.get("SLURM_JOB_NUM_NODES")) to set the number of nodes.
            We also set progress_bar_refresh_rate=0 to avoid writing a progress bar to the logs,
            which can cause issues due to updating logs too frequently."""

    trainer = pl.Trainer(accelerator="gpu", devices=2, num_nodes=1, strategy=DeepSpeedStrategy(
            stage=3,
            offload_optimizer=True,
            offload_parameters=True,
            ), max_epochs = args.max_epochs)

    transform_train = transforms.Compose([transforms.ToTensor(),transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    dataset_train = CIFAR10(root='./data', train=True, download=False, transform=transform_train)

    train_loader = DataLoader(dataset_train, batch_size=args.batch_size, num_workers=args.num_workers)

    trainer.fit(net,train_loader)


if __name__=='__main__':
   main()
```

### ZeRO with Offload to NVMe

In this example, we use ZeRO stage 3 yet again, but this time we enable offloading model parameters and optimizer states to the local disk. This means that the compute node's local disk storage will be available to store these tensors while they are not required by any GPU computations. As before, optimizer steps will be computed on the CPU. Again, for practical purposes, you can think of this as extending GPU memory by however much storage is available on the local disk, though this time performance will significantly degrade. This approach works best (i.e., performance degradation is least noticeable) on NVMe-enabled drives, which have higher throughput and faster response times, but it can be used with any type of storage.

```bash title="deepspeed-stage3-offload-nvme.sh"
#!/bin/bash
#SBATCH --nodes 1
#SBATCH --gres=gpu:2          # Request 2 GPU "generic resources”.
#SBATCH --tasks-per-node=2    # Request 1 process per GPU. You will get 1 CPU per process by default. Request more CPUs with the "cpus-per-task" parameter to enable multiple data-loader workers to load data in parallel.
#SBATCH --mem=32G
#SBATCH --time=0-00:20
#SBATCH --output=%N-%j.out
#SBATCH --account=<your account>

module load python cuda # CUDA must be loaded if using ZeRO offloading to CPU or NVMe. Version must be the same used to compile PyTorch.
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate
pip install torchvision pytorch-lightning deepspeed --no-index

export TORCH_NCCL_ASYNC_HANDLING=1

# PyTorch Lightning will query the environment to figure out if it is running inside a SLURM batch job
# If it is, it expects the user to have requested one task per GPU.
# If you do not ask for 1 task per GPU, and you do not run your script with "srun", your job will fail!

srun python deepspeed-stage3-offload-nvme.py  --batch_size 256
```

```python title="deepspeed-stage3-offload-nvme.py"
import os

import torch
from torch import nn
import torch.nn.functional as F

import pytorch_lightning as pl

import torchvision
import torchvision.transforms as transforms
from torchvision.datasets import CIFAR10
from torch.utils.data import DataLoader

from deepspeed.ops.adam import DeepSpeedCPUAdam
from pytorch_lightning.strategies import DeepSpeedStrategy

import argparse

parser = argparse.ArgumentParser(description='cifar10 classification models, deepspeed offload to nvme test')
parser.add_argument('--lr', default=0.1, help='')
parser.add_argument('--max_epochs', type=int, default=2, help='')
parser.add_argument('--batch_size', type=int, default=768, help='')
parser.add_argument('--num_workers', type=int, default=0, help='')


def main():
    print("Starting...")

    args = parser.parse_args()

    class ConvPart(nn.Module):
        def __init__(self):
            super(ConvPart, self).__init__()

            self.conv1 = nn.Conv2d(3, 6, 5)
            self.pool = nn.MaxPool2d(2, 2)
            self.conv2 = nn.Conv2d(6, 16, 5)
            self.relu = nn.ReLU()

        def forward(self, x):
            x = self.pool(self.relu(self.conv1(x)))
            x = self.pool(self.relu(self.conv2(x)))
            x = x.view(-1, 16 * 5 * 5)

            return x

    # Dense feedforward part of the model
    class MLPPart(nn.Module):
        def __init__(self):
            super(MLPPart, self).__init__()

            self.fc1 = nn.Linear(16 * 5 * 5, 120)
            self.fc2 = nn.Linear(120, 84)
            self.fc3 = nn.Linear(84, 10)
            self.relu = nn.ReLU()

        def forward(self, x):
            x = self.relu(self.fc1(x))
            x = self.relu(self.fc2(x))
            x = self.relu(self.fc3(x))

            return x

    class Net(pl.LightningModule):
        def __init__(self):
            super(Net, self).__init__()

            self.conv_part = ConvPart()
            self.mlp_part = MLPPart()

        def configure_sharded_model(self):
            self.block = nn.Sequential(self.conv_part, self.mlp_part)

        def forward(self, x):
            x = self.block(x)

            return x

        def training_step(self, batch, batch_idx):
            x, y = batch
            y_hat = self(x)
            loss = F.cross_entropy(y_hat, y)
            return loss

        def configure_optimizers(self):
            return DeepSpeedCPUAdam(self.parameters())

    net = Net()

    """ Here we initialize a Trainer() explicitly with 1 node and 2 GPU.
            To make this script more generic, you can use torch.cuda.device_count() to set the number of GPUs
            and you can use int(os.environ.get("SLURM_JOB_NUM_NODES")) to set the number of nodes.
            We also set progress_bar_refresh_rate=0 to avoid writing a progress bar to the logs,
            which can cause issues due to updating logs too frequently."""

    local_scratch = os.environ['SLURM_TMPDIR'] # Get path where local storage is mounted

    print(f'Offloading to: {local_scratch}')

    trainer = pl.Trainer(accelerator="gpu", devices=2, num_nodes=1, strategy=DeepSpeedStrategy(
            stage=3,
            offload_optimizer=True,
            offload_parameters=True,
            remote_device="nvme",
            offload_params_device="nvme",
            offload_optimizer_device="nvme",
            nvme_path="local_scratch",
            ), max_epochs = args.max_epochs)

    transform_train = transforms.Compose([transforms.ToTensor(),transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    dataset_train = CIFAR10(root='./data', train=True, download=False, transform=transform_train)

    train_loader = DataLoader(dataset_train, batch_size=args.batch_size, num_workers=args.num_workers)

    trainer.fit(net,train_loader)


if __name__=='__main__':
   main()