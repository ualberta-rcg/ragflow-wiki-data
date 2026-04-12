---
title: "CUDA/en"
slug: "cuda"
lang: "en"

source_wiki_title: "CUDA/en"
source_hash: "6f6299f0dbe0383608f4ed25b1ec1a79"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:05:50.456717+00:00"

tags:
  []

keywords:
  - "Slurm"
  - "Streaming Multiprocessor"
  - "CMAKE_CUDA_ARCHITECTURES"
  - "GPU"
  - "Compute Capability"
  - "nvcc fatal error"
  - "gencode"
  - "GPU architecture"
  - "kernel image"
  - "nvcc"
  - "CUDA"
  - "CUDA GPU Compute Capability"
  - "cmake"
  - "compute capability"

questions:
  - "What is CUDA and what is its primary purpose in computing?"
  - "How do you compile a CUDA C/C++ program and submit it as a job using the Slurm scheduler?"
  - "What does the term \"compute capability\" refer to in the context of NVIDIA GPUs and troubleshooting?"
  - "What is the correct flag syntax to use with the nvcc compiler to specify the GPU compute capability?"
  - "How do you configure the CUDA architecture compute capability when building a project with cmake?"
  - "How can a user determine the correct two-digit compute capability value for their specific Nvidia GPU?"
  - "Where can developers find official documentation regarding GPU Compute Capability and Streaming Multiprocessor Versions?"
  - "What specific error messages are listed as being directly connected to issues with compute capability?"
  - "What underlying hardware parameters dictate whether a kernel image is available for execution on a specific device?"
  - "What is the correct flag syntax to use with the nvcc compiler to specify the GPU compute capability?"
  - "How do you configure the CUDA architecture compute capability when building a project with cmake?"
  - "How can a user determine the correct two-digit compute capability value for their specific Nvidia GPU?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

"CUDA® is a parallel computing platform and programming model developed by NVIDIA for general computing on graphical processing units (GPUs)." [NVIDIA CUDA Home Page](https://developer.nvidia.com/cuda-toolkit). CUDA is a registered trademark of NVIDIA.

It is reasonable to think of CUDA as a set of libraries and associated C, C++, and Fortran compilers that enable you to write code for GPUs. See [OpenACC Tutorial](openacc_tutorial.md) for another set of GPU programming tools.

## Quick start guide

### Compiling
Here we show a simple example of how to use the CUDA C/C++ language compiler, `nvcc`, and run code created with it. For a longer tutorial in CUDA programming, see [CUDA tutorial](../software/cuda_tutorial.md).

First, load a CUDA [module](utiliser_des_modules.md).
```bash
$ module purge
$ module load cuda
```

The following program will add two numbers together on a GPU. Save the file as `add.cu`.

!!! tip "Important"
    The `cu` file extension is important!

```c++ title="add.cu"
#include <iostream>

__global__ void add (int *a, int *b, int *c){
  *c = *a + *b;
}

int main(void){
  int a, b, c;
  int *dev_a, *dev_b, *dev_c;
  int size = sizeof(int);

  //  allocate device copies of a,b, c
  cudaMalloc ( (void**) &dev_a, size);
  cudaMalloc ( (void**) &dev_b, size);
  cudaMalloc ( (void**) &dev_c, size);

  a=2; b=7;
  //  copy inputs to device
  cudaMemcpy (dev_a, &a, size, cudaMemcpyHostToDevice);
  cudaMemcpy (dev_b, &b, size, cudaMemcpyHostToDevice);

  // launch add() kernel on GPU, passing parameters
  add <<< 1, 1 >>> (dev_a, dev_b, dev_c);

  // copy device result back to host
  cudaMemcpy (&c, dev_c, size, cudaMemcpyDeviceToHost);
  std::cout<<a<<"+"<<b<<"="<<c<<std::endl;

  cudaFree ( dev_a ); cudaFree ( dev_b ); cudaFree ( dev_c );
}
```

Compile the program with `nvcc` to create an executable named `add`.
```bash
$ nvcc add.cu -o add
```

### Submitting jobs
To run the program, create a Slurm job script as shown below. Be sure to replace `def-someuser` with your specific account (see [Accounts and projects](../running-jobs/running_jobs.md#accounts-and-projects)). For options relating to scheduling jobs with GPUs see [Using GPUs with Slurm](../running-jobs/using_gpus_with_slurm.md).

```sh title="gpu_job.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --gres=gpu:1              # Number of GPUs (per node)
#SBATCH --mem=400M                # memory (per node)
#SBATCH --time=0-00:10            # time (DD-HH:MM)
./add #name of your program
```

Submit your GPU job to the scheduler with
```bash
$ sbatch gpu_job.sh
Submitted batch job 3127733
```
For more information about the `sbatch` command and running and monitoring jobs, see [Running jobs](../running-jobs/running_jobs.md).

Once your job has finished, you should see an output file similar to this:
```bash
$ cat slurm-3127733.out
2+7=9
```
If you run this without a GPU present, you might see output like `2+7=0`.

### Linking libraries
If you have a program that needs to link some libraries included with CUDA, for example [cuBLAS](https://developer.nvidia.com/cublas), compile with the following flags
```bash
nvcc -lcublas -Xlinker=-rpath,$CUDA_PATH/lib64
```

To learn more about how the above program works and how to make the use of GPU parallelism, see [CUDA tutorial](../software/cuda_tutorial.md).

## Troubleshooting

### Compute capability

NVidia has created this technical term, "which indicates what features are supported by that GPU and specifies some hardware parameters for that GPU."
See [Compute Capability and Streaming Multiprocessor Versions](https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/cuda-platform.html#cuda-platform-compute-capability-sm-version) for more details.

The following errors are connected with compute capability:

```text
nvcc fatal : Unsupported gpu architecture 'compute_XX'
```

```text
no kernel image is available for execution on the device (209)
```

If you encounter either of these errors, you may be able to fix it by adding the correct *flag* to the `nvcc` call:

```text
-gencode arch=compute_XX,code=[sm_XX,compute_XX]
```

If you are using `cmake`, provide the following flag:

```text
cmake .. -DCMAKE_CUDA_ARCHITECTURES=XX
```

where “XX” is the compute capability of the Nvidia GPU that you expect to run the application on.
To find the value to replace “XX“, see [CUDA GPU Compute Capability](https://developer.nvidia.com/cuda/gpus) and omit the decimal point.

**For example,** if you will run your code on a Narval A100 node, the NVidia table gives its compute capability as "8.0".
The correct flag to use when compiling with `nvcc` is then:

```text
-gencode arch=compute_80,code=[sm_80,compute_80]
```

The flag to supply to `cmake` is:

```text
cmake .. -DCMAKE_CUDA_ARCHITECTURES=80