---
title: "Weights & Biases (wandb)"
slug: "weights___biases__wandb"
lang: "base"

source_wiki_title: "Weights & Biases (wandb)"
source_hash: "90f00461281cb746e67b26aadd12466d"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:52:30.187526+00:00"

tags:
  - ai-and-machine-learning

keywords:
  - "python script"
  - "Machine learning"
  - "metric logging"
  - "Alliance clusters"
  - "Weights & Biases"
  - "wandb sync"
  - "SBATCH"
  - "SLURM"
  - "offline mode"
  - "Experiment tracking"
  - "python virtualenv"
  - "Offline mode"
  - "API key"
  - "wandb"

questions:
  - "What is the Weights & Biases (wandb) platform and what are its primary functions in the machine learning lifecycle?"
  - "How does the availability and required configuration for wandb vary across different Alliance clusters?"
  - "What is the recommended workaround for using wandb on restricted clusters like Narval, Rorqual, and TamIA to prevent job crashes?"
  - "How do you initialize a Weights & Biases project and log metrics using a Python script?"
  - "What command is used to set Weights & Biases to operate in offline mode?"
  - "How do you synchronize the locally saved offline run data to the Weights & Biases server after training?"
  - "What are the specific SLURM resource allocations and output configurations defined in the script?"
  - "How does the script set up the Python virtual environment and install the required dependencies?"
  - "What steps must a user take to configure the Weights & Biases API key for online mode execution?"
  - "How do you initialize a Weights & Biases project and log metrics using a Python script?"
  - "What command is used to set Weights & Biases to operate in offline mode?"
  - "How do you synchronize the locally saved offline run data to the Weights & Biases server after training?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Weights & Biases (wandb)](https://wandb.ai) is a *meta machine learning platform* designed to help AI practitioners and teams build reliable machine learning models for real-world applications by streamlining the machine learning model lifecycle. By using wandb, you can track, compare, explain, and reproduce machine learning experiments.

## Using wandb on Alliance clusters

### Availability on compute nodes

Full usage of `wandb` on compute nodes requires internet access as well as access to Google Cloud Storage, both of which may not be available depending on the cluster:

| Cluster | Wandb Availability | Note |
|:--------|:-------------------|:-----|
| Narval | Limited ❌ | Users from **MILA and other eligible groups only** via `httpproxy` |
| Rorqual | Limited ❌ | Users from **MILA and other eligible groups only** via `httpproxy` |
| TamIA | Limited ❌ | Users from **MILA and other eligible groups only** via `httpproxy` |
| Fir | Yes ✅ | `httpproxy` not required |
| Nibi | Yes ✅ | `httpproxy` not required |
| Trillium | No ❌ | internet access is disabled on compute nodes |
| Vulcan | Yes ✅ | `httpproxy` not required |
| Killarney | Yes ✅ | `httpproxy` not required |

## Users from MILA and other eligible groups

Members of the MILA Québec AI Institute may use `wandb` on any of our clusters with internet access, provided that they use a valid **Mila-org** Weights & Biases account to log into `wandb`. Please see the table above for more information on modules required for using `wandb` on each cluster.

Other groups are known to have made arrangements with Weights & Biases to bypass calls to the Google Cloud Storage API. Please contact your PI to find out if your group has made such arrangements.

## Narval, Rorqual and TamIA

!!! warning
    While it is possible to upload basic metrics to Weights&Biases during a job on Narval, Rorqual, and TamIA, the wandb package will automatically attempt to upload information about your environment to a Google Cloud Storage bucket, which is not allowed on the compute nodes of these clusters. This will result in a crash during or at the very end of a training run. Your job may also freeze until it reaches its wall time, thereby wasting resources. It is not currently possible to disable this behaviour. Note that uploading artifacts to W&B with `wandb.save()` also requires access to Google Cloud Storage and will cause your job to freeze or crash.

You can still use wandb by enabling the [`offline`](https://docs.wandb.ai/library/cli#wandb-offline) mode. In this mode, wandb will write all metrics, logs, and artifacts to the local disk and will not attempt to sync anything to the Weights&Biases service on the internet. After your jobs finish running, you can sync their wandb content to the online service by running the command [`wandb sync`](https://docs.wandb.ai/ref/cli#wandb-sync) on the login node.

!!! note
    `Comet.ml` is a product very similar to Weights & Biases, and works on Narval, Rorqual, and TamIA.

## Example

The following is an example of how to use wandb to track experiments in offline mode. To run in online mode, load the module `httpproxy` on applicable clusters and follow the comments on the example script below.

```bash title="wandb-test.sh"
#!/bin/bash
#SBATCH --account=YOUR_ACCOUNT
#SBATCH --cpus-per-task=2 # At least two cpus is recommended - one for the main process and one for the wandB process
#SBATCH --mem=4G       
#SBATCH --time=0-03:00
#SBATCH --output=%N-%j.out

module load python
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate
pip install --no-index wandb

### Save your wandb API key in your .bash_profile or replace $API_KEY with your actual API key. Uncomment the line below and comment out "wandb offline" if running in online mode ###

#wandb login $API_KEY 

wandb offline

python wandb-test.py
```

The script wandb-test.py is a simple example of metric logging. See [W&B's full documentation](https://docs.wandb.ai) for more options.

```python title="wandb-test.py"
import wandb

wandb.init(project="wandb-pytorch-test", settings=wandb.Settings(start_method="fork"))

for my_metric in range(10):
    wandb.log({'my_metric': my_metric})
```

After a training run in offline mode, there will be a new folder `./wandb/offline-run*`. You can send the metrics to the server using the command `wandb sync ./wandb/offline-run*`. Note that using `*` will sync all runs.