---
title: "Comet.ml"
slug: "comet_ml"
lang: "base"

source_wiki_title: "Comet.ml"
source_hash: "155799fb00963d272db49d924cc16e03"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T05:43:44.128095+00:00"

tags:
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

[Comet](https://comet.ml) is a meta machine learning platform designed to help AI practitioners and teams build reliable machine learning models for real-world applications by streamlining the machine learning model lifecycle. By using Comet, users can track, compare, explain, and reproduce their machine learning experiments. Comet can also greatly accelerate hyperparameter search, by providing a [module for the Bayesian exploration of hyperparameter space](https://www.comet.ml/parameter-optimization).

## Using Comet on our clusters

### Availability

Since it requires an internet connection, Comet has restricted availability on compute nodes, depending on the cluster:

| Cluster | Comet Availability | Note |
|---|---|---|
| Narval | Yes ✅ | `module load httpproxy` required |
| Rorqual | Yes ✅ | `module load httpproxy` required |
| TamIA | Yes ✅ | `module load httpproxy` required |
| Fir | Yes ✅ | `httpproxy` not required |
| Nibi | Yes ✅ | `httpproxy` not required |
| Trillium | No ❌ | internet access is disabled on compute nodes |
| Vulcan | Yes ✅ | `httpproxy` not required |
| Killarney | Yes ✅ | `httpproxy` not required |

### Best practices

!!! tip

    Avoid logging metrics (e.g. loss, accuracy) at a high frequency. This can cause Comet to throttle your experiment, which can make your job duration harder to predict. As a rule of thumb, please log metrics (or request new hyperparameters) at an interval >= 1 minute.