---
title: "Comet.ml"
slug: "comet_ml"
lang: "base"

source_wiki_title: "Comet.ml"
source_hash: "155799fb00963d272db49d924cc16e03"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:29:05.139640+00:00"

tags:
  - ai-and-machine-learning

keywords:
  - "logging metrics"
  - "cluster availability"
  - "hyperparameter search"
  - "machine learning platform"
  - "Comet"

questions:
  - "What is the Comet platform and what are its primary functions in the machine learning model lifecycle?"
  - "How does Comet's availability vary across different compute clusters, and when is the httpproxy module required?"
  - "Why should users avoid logging metrics at a high frequency when using Comet, and what is the recommended logging interval?"
  - "What is the Comet platform and what are its primary functions in the machine learning model lifecycle?"
  - "How does Comet's availability vary across different compute clusters, and when is the httpproxy module required?"
  - "Why should users avoid logging metrics at a high frequency when using Comet, and what is the recommended logging interval?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Comet](https://comet.ml) is a meta machine learning platform designed to help AI practitioners and teams build reliable machine learning models for real-world applications by streamlining the machine learning model lifecycle. By using Comet, users can track, compare, explain and reproduce their machine learning experiments. Comet can also greatly accelerate hyperparameter search, by providing a [module for the Bayesian exploration of hyperparameter space](https://www.comet.ml/parameter-optimization).

## Using Comet on our clusters

### Availability

Since it requires an internet connection, Comet has restricted availability on compute nodes, depending on the cluster:

| Cluster | Comet Availability | Note |
| :------ | :----------------- | :--- |
| Narval | Yes ✅ | `module load httpproxy` required |
| Rorqual | Yes ✅ | `module load httpproxy` required |
| TamIA | Yes ✅ | `module load httpproxy` required |
| Fir | Yes ✅ | `httpproxy` not required |
| Nibi | Yes ✅ | `httpproxy` not required |
| Trillium | No ❌ | internet access is disabled on compute nodes |
| Vulcan | Yes ✅ | `httpproxy` not required |
| Killarney | Yes ✅ | `httpproxy` not required |

### Best practices

!!! warning "Best practices"
    Avoid logging metrics (e.g. loss, accuracy) at a high frequency. This can cause Comet to throttle your experiment, which can make your job duration harder to predict. As a rule of thumb, please log metrics (or request new hyperparameters) at an interval >= 1 minute.