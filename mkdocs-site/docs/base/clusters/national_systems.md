---
title: "National systems"
slug: "national_systems"
lang: "base"

source_wiki_title: "National systems"
source_hash: "e3eb53301a6e05de5adf4f24a9d9223c"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T09:10:29.219830+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: false
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
| :------------ | :----------- | :--------------------------------------- | :----------- |
| [Béluga](béluga.md) | General-purpose | beluga-compute, beluga-gpu, beluga-storage | End of life |
| [Cedar](cedar.md) | General-purpose | cedar-compute, cedar-gpu, cedar-storage | End of life |
| [Fir](fir.md) | General-purpose | fir-compute, fir-gpu, fir-storage | In production |
| [Graham](graham.md) | General-purpose | graham-compute, graham-gpu, graham-storage | End of life |
| [Narval](narval.md) | General-purpose | narval-compute, narval-gpu, narval-storage | In production |
| [Niagara](niagara.md) | Large parallel | niagara-compute, niagara-storage, hpss-storage | End of life |
| [Nibi](nibi.md) | General-purpose | nibi-compute, nibi-storage, nibi-storage | In production |
| [Rorqual](rorqual.md) | General-purpose | rorqual-compute, rorqual-gpu, rorqual-storage | In production |
| [Trillium](trillium.md) | Large parallel | trillium-compute, trillium-gpu, trillium-storage | In production |

## Cloud - Infrastructure as a Service
Our cloud systems are offering an Infrastructure as a Service (IaaS) based on OpenStack.

| Name and link | Sub-systems | Description | Status |
| :------------ | :--------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------- |
| [Arbutus cloud](cloud-resources.md#arbutus-cloud) | arbutus-compute-cloud, arbutus-persistent-cloud, arbutus-dcache | VCPU, VGPU, RAM, Local ephemeral disk, Volume and snapshot storage, Shared filesystem storage (backed up), Object storage, Floating IPs, dCache storage | In production |
| [Béluga cloud](cloud-resources.md#béluga-cloud) | beluga-compute-cloud, beluga-persistent-cloud | VCPU, RAM, Local ephemeral disk, Volume and snapshot storage, Floating IPs | In production |
| [Cedar cloud](cloud-resources.md#cedar-cloud) | cedar-persistent-cloud, cedar-compute-cloud | VCPU, RAM, Local ephemeral disk, Volume and snapshot storage, Floating IPs | In production |
| [Graham cloud](cloud-resources.md#graham-cloud) | graham-persistent-cloud | VCPU, RAM, Local ephemeral disk, Volume and snapshot storage, Floating IPs | In production |

## PAICE clusters

[Pan-Canadian AI Compute Environment (PAICE)](https://alliancecan.ca/en/services/advanced-research-computing/pan-canadian-ai-compute-environment-paice) clusters are systems dedicated to the current and emerging AI needs of Canada’s research community.

| Name and link | Institute | Status |
| :------------ | :---------------- | :----------- |
| [TamIA](tamia.md) | [Mila](https://mila.quebec/) | In production |
| [Killarney](killarney.md) | [Vector Institute](https://vectorinstitute.ai/) | In production |
| [Vulcan](vulcan.md) | [Amii](https://www.amii.ca/) | In production |