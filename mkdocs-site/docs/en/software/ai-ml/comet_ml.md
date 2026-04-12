---
title: "Comet.ml/en"
slug: "comet_ml"
lang: "en"

source_wiki_title: "Comet.ml/en"
source_hash: "13f3fc991ac8de24c7160af15511f031"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:29:15.936440+00:00"

tags:
  - ai-and-machine-learning

keywords:
  - "logging metrics"
  - "cluster availability"
  - "hyperparameter search"
  - "machine learning platform"
  - "Comet"

questions:
  - "What are the primary functions and benefits of using the Comet platform for machine learning practitioners?"
  - "Which compute clusters support Comet, and what specific module must be loaded on some of them to ensure internet connectivity?"
  - "Why is it recommended to avoid logging metrics at a high frequency when using Comet, and what is the suggested logging interval?"
  - "What are the primary functions and benefits of using the Comet platform for machine learning practitioners?"
  - "Which compute clusters support Comet, and what specific module must be loaded on some of them to ensure internet connectivity?"
  - "Why is it recommended to avoid logging metrics at a high frequency when using Comet, and what is the suggested logging interval?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Comet](https://comet.ml) is a meta machine learning platform designed to help AI practitioners and teams build reliable machine learning models for real-world applications by streamlining the machine learning model lifecycle. By using Comet, users can track, compare, explain, and reproduce their machine learning experiments. Comet can also greatly accelerate hyperparameter search, by providing a [module for the Bayesian exploration of hyperparameter space](https://www.comet.ml/parameter-optimization).

## Using Comet on our clusters

### Availability

Since it requires an internet connection, Comet has restricted availability on compute nodes, depending on the cluster:

| Cluster   | Wandb Availability | Note                          |
| :-------- | :----------------- | :---------------------------- |
| Narval    | Yes ✅             | `module load httpproxy` required |
| Rorqual   | Yes ✅             | `module load httpproxy` required |
| TamIA     | Yes ✅             | `module load httpproxy` required |
| Fir       | Yes ✅             | `httpproxy` not required      |
| Nibi      | Yes ✅             | `httpproxy` not required      |
| Trillium  | No ❌              | internet access is disabled on compute nodes |
| Vulcan    | Yes ✅             | `httpproxy` not required      |
| Killarney | Yes ✅             | `httpproxy` not required      |

### Best practices

!!! tip
    Avoid logging metrics (e.g., loss, accuracy) at a high frequency. This can cause Comet to throttle your experiment, which can make your job duration harder to predict. As a rule of thumb, please log metrics (or request new hyperparameters) at an interval `>= 1` minute.