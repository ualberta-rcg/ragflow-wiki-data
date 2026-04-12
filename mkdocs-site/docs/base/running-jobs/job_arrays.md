---
title: "Job arrays"
slug: "job_arrays"
lang: "base"

source_wiki_title: "Job arrays"
source_hash: "fbc8577863c297ba0fabe2b20359bc16"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:10:35.234263+00:00"

tags:
  - slurm

keywords:
  - "NumPy array"
  - "parallel"
  - "Slurm"
  - "Multiple parameters"
  - "array tasks"
  - "Python script"
  - "case_list"
  - "job array"
  - "task array"
  - "SLURM_ARRAY_TASK_ID"
  - "job submission script"
  - "sbatch"

questions:
  - "What is a SLURM job array and how is the $SLURM_ARRAY_TASK_ID environment variable used to differentiate individual tasks?"
  - "What are the advantages of using job arrays over submitting separate serial jobs, and why should they be avoided for tasks with very short run times?"
  - "How can a job array be configured to execute a script across multiple directories that have non-sequential or unsystematic names?"
  - "How does the tutorial propose parallelizing the sequential calculation of the beta parameters?"
  - "What modifications are made to the Python script to allow it to process a specific task from the job array?"
  - "How is the bash submission script configured to execute the 100 parallel tasks using Slurm?"
  - "Why must the `case_list` file remain unchanged until all tasks in the array have completed?"
  - "What type of data structures are used to define the parameters in the provided Python script example?"
  - "What is the primary function of the `my_script.py` file mentioned in the multiple parameters example?"
  - "How does the tutorial propose parallelizing the sequential calculation of the beta parameters?"
  - "What modifications are made to the Python script to allow it to process a specific task from the job array?"
  - "How is the bash submission script configured to execute the 100 parallel tasks using Slurm?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Parent page: [Running jobs](running-jobs.md)*

If your work consists of a large number of tasks which differ only in some parameter, you can conveniently submit many tasks at once using a *job array*, also known as a *task array* or an *array job*. The individual tasks in the array are distinguished by an environment variable, `$SLURM_ARRAY_TASK_ID`, which Slurm sets to a different value for each task. You set the range of values with the `--array` parameter.

See [Job Array Support](https://slurm.schedmd.com/job_array.html) for more details.

## Examples of the --array parameter

```bash
sbatch --array=0-7       # $SLURM_ARRAY_TASK_ID takes values from 0 to 7 inclusive
sbatch --array=1,3,5,7   # $SLURM_ARRAY_TASK_ID takes the listed values
sbatch --array=1-7:2     # Step size of 2, same as the previous example
sbatch --array=1-100%10  # Allows no more than 10 of the jobs to run simultaneously
```

## A simple example

```bash title="simple_array.sh"
#!/bin/bash
#SBATCH --array=1-10
#SBATCH --time=3:00:00
program_x <input.$SLURM_ARRAY_TASK_ID
program_y $SLURM_ARRAY_TASK_ID some_arg another_arg
```

This job will be scheduled as ten independent tasks. Each task has a separate time limit of 3 hours, and each may start at a different time on a different host.

The script references `$SLURM_ARRAY_TASK_ID` to select an input file (named *program_x* in our example), or to set a command-line argument for the application (as in *program_y*).

Using a job array instead of a large number of separate serial jobs has advantages for you and other users. A waiting job array only produces one line of output in squeue, making it easier for you to read its output. The scheduler does not have to analyze job requirements for each task in the array separately, so it can run more efficiently too.

!!! warning
    Note that, other than the initial job-submission step with `sbatch`, the load on the scheduler is the same for an array job as for the equivalent number of non-array jobs. The cost of dispatching each array task is the same as dispatching a non-array job. You should not use a job array to submit tasks with very short run times, e.g. much less than an hour. Tasks with run times of only a few minutes should be grouped into longer jobs using [META](meta-a-package-for-job-farming.md), [GLOST](glost.md), [GNU Parallel](gnu-parallel.md), or a shell loop inside a job.

## Example: Multiple directories

Suppose you have multiple directories, each with the same structure, and you want to run the same script in each directory. If the directories can be named with sequential numbers then the example above can be easily adapted. If the names are not so systematic, then create a file with the names of the directories, like so:

```bash
$ cat case_list
```

```text title="case_list"
pacific2016
pacific2017
atlantic2016
atlantic2017
```

There are several ways to select a given line from a file; this example uses `sed` to do so:

```bash title="directories_array.sh"
#!/bin/bash
#SBATCH --time=3:00:00
#SBATCH --array=1-4

echo "Starting task $SLURM_ARRAY_TASK_ID"
DIR=$(sed -n "${SLURM_ARRAY_TASK_ID}p" case_list)
cd $DIR

# Place the code to execute here
pwd
ls
```

!!! warning "Cautions"
    *   Take care that the number of tasks you request matches the number of entries in the file.
    *   The file `case_list` should not be changed until all the tasks in the array have run, since it will be read each time a new task starts.

## Example: Multiple parameters

Suppose you have a Python script doing certain calculations with some parameters defined in a Python list or a NumPy array such as

```python title="my_script.py"
import time
import numpy as np

def calculation(x, beta):
    time.sleep(2) #simulate a long run
    return beta * np.linalg.norm(x**2)

if __name__ == "__main__":
    x = np.random.rand(100)
    betas = np.linspace(10,36.5,100) #subdivise the interval [10,36.5] with 100 values
    for i in range(len(betas)): #iterate through the beta parameter
        res = calculation(x,betas[i])
        print(res) #show the results on screen

# Run with: python my_script.py
```

The above task can be processed in a job array so that each value of the beta parameter can be treated in parallel.
The idea is to pass the `$SLURM_ARRAY_TASK_ID` to the Python script and get the beta parameter based on its value.
The Python script becomes

```python title="my_script_parallel.py"
import time
import numpy as np
import sys

def calculation(x, beta):
    time.sleep(2) #simulate a long run
    return beta * np.linalg.norm(x**2)

if __name__ == "__main__":
    x = np.random.rand(100)
    betas = np.linspace(10,36.5,100) #subdivise the interval [10,36.5] with 100 values
    
    i = int(sys.argv[1]) #get the value of the $SLURM_ARRAY_TASK_ID
    res = calculation(x,betas[i])
    print(res) #show the results on screen

# Run with: python my_script_parallel.py $SLURM_ARRAY_TASK_ID
```

The job submission script is (note the array parameters goes from 0 to 99 like the indexes of the NumPy array)

```bash title="data_parallel_python.sh"
#!/bin/bash
#SBATCH --array=0-99
#SBATCH --time=1:00:00
module load scipy-stack
python my_script_parallel.py $SLURM_ARRAY_TASK_ID