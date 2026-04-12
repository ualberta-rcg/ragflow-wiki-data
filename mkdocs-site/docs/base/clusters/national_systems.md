---
title: "National systems"
slug: "national_systems"
lang: "base"

source_wiki_title: "National systems"
source_hash: "e3eb53301a6e05de5adf4f24a9d9223c"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:42:10.856660+00:00"

tags:
  []

keywords:
  - "PAICE clusters"
  - "Cloud systems"
  - "Compute clusters"
  - "Infrastructure as a Service"
  - "General-purpose clusters"

questions:
  - "What are the three broad classifications of nodes found in a general-purpose compute cluster, and how do their hardware specifications differ?"
  - "What types of resources and storage options are offered through the OpenStack-based Infrastructure as a Service (IaaS) cloud systems?"
  - "What is the specific purpose of the Pan-Canadian AI Compute Environment (PAICE) clusters, and which research institutes are they associated with?"
  - "What are the three broad classifications of nodes found in a general-purpose compute cluster, and how do their hardware specifications differ?"
  - "What types of resources and storage options are offered through the OpenStack-based Infrastructure as a Service (IaaS) cloud systems?"
  - "What is the specific purpose of the Pan-Canadian AI Compute Environment (PAICE) clusters, and which research institutes are they associated with?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Compute clusters

A *general-purpose* cluster is designed to support a wide variety of types of jobs, and is composed of a mixture of different nodes. We broadly classify the nodes as:
* *base* nodes, containing typically about 4GB of memory per core;
* *large-memory* nodes, containing typically more than 8GB memory per core;
* *GPU* nodes, which contain [graphic processing units](https://en.wikipedia.org/wiki/Graphics_processing_unit).

All clusters have large, high-performance storage attached. For details about storage, memory, CPU model and count, GPU model and count, and the number of nodes at each site, please click on the cluster name in the table below.

### List of compute clusters

| Name and link | Type | Sub-systems | Status |
|---|---|---|---|
| [Béluga](béluga.md) | General-purpose | * beluga-compute<br/>* beluga-gpu<br/>* beluga-storage | End of life |
| [Cedar](cedar.md) | General-purpose | * cedar-compute<br/>* cedar-gpu<br/>* cedar-storage | End of life |
| [Fir](../software/fir.md) | General-purpose | * fir-compute<br/>* fir-gpu<br/>* fir-storage | In production |
| [Graham](graham.md) | General-purpose | * graham-compute<br/>* graham-gpu<br/>* graham-storage | End of life |
| [Narval](narval.md) | General-purpose | * narval-compute<br/>* narval-gpu<br/>* narval-storage | In production |
| [Niagara](niagara.md) | Large parallel | * niagara-compute<br/>* niagara-storage<br/>* hpss-storage | End of life |
| [Nibi](nibi.md) | General-purpose | * nibi-compute<br/>* nibi-storage<br/>* nibi-storage | In production |
| [Rorqual](rorqual.md) | General-purpose | * rorqual-compute<br/>* rorqual-gpu<br/>* rorqual-storage | In production |
| [Trillium](trillium.md) | Large parallel | * trillium-compute<br/>* trillium-gpu<br/>* trillium-storage | In production |

## Cloud - Infrastructure as a Service
Our cloud systems are offering an Infrastructure as a Service (IaaS) based on OpenStack.

| Name and link | Sub-systems | Description | Status |
|---|---|---|---|
| [Arbutus cloud](../cloud/cloud_resources.md#arbutus-cloud) | * arbutus-compute-cloud<br/>* arbutus-persistent-cloud<br/>* arbutus-dcache | * VCPU, VGPU, RAM<br/>* Local ephemeral disk<br/>* Volume and snapshot storage<br/>* Shared filesystem storage (backed up)<br/>* Object storage<br/>* Floating IPs<br/>* dCache storage | In production |
| [Béluga cloud](../cloud/cloud_resources.md#béluga-cloud) | * beluga-compute-cloud<br/>* beluga-persistent-cloud | * VCPU, RAM<br/>* Local ephemeral disk<br/>* Volume and snapshot storage<br/>* Floating IPs | In production |
| [Cedar cloud](../cloud/cloud_resources.md#cedar-cloud) | * cedar-persistent-cloud<br/>* cedar-compute-cloud | * VCPU, RAM<br/>* Local ephemeral disk<br/>* Volume and snapshot storage<br/>* Floating IPs | In production |
| [Graham cloud](../cloud/cloud_resources.md#graham-cloud) | * graham-persistent-cloud | * VCPU, RAM<br/>* Local ephemeral disk<br/>* Volume and snapshot storage<br/>* Floating IPs | In production |

## PAICE clusters

[Pan-Canadian AI Compute Environment (PAICE)](https://alliancecan.ca/en/services/advanced-research-computing/pan-canadian-ai-compute-environment-paice) clusters are systems dedicated to the current and emerging AI needs of Canada’s research community.

| Name and link | Institute | Status |
|---|---|---|
| [TamIA](tamia.md) | [Mila](https://mila.quebec/) | In production |
| [Killarney](killarney.md) | [Vector Institute](https://vectorinstitute.ai/) | In production |
| [Vulcan](vulcan.md) | [Amii](https://www.amii.ca/) | In production |