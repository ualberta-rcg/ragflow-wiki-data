---
title: "Cloud RAS Allocations/en"
slug: "cloud_ras_allocations"
lang: "en"

source_wiki_title: "Cloud RAS Allocations/en"
source_hash: "27f8a25bfc66b84707042ca398fb2e8c"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:22:15.644714+00:00"

tags:
  - cloud

keywords:
  - "references"
  - "Cloud"
  - "RAC allocation period"
  - "Resource Allocation Competition (RAC)"
  - "Compute instances"
  - "Default duration"
  - "Cloud instances"
  - "Rapid Access Service (RAS)"
  - "Notes"
  - "Requesting RAS"
  - "1 month wall-time"
  - "Category"
  - "Default renewal"
  - "small"
  - "Persistent instances"

questions:
  - "What is the Rapid Access Service (RAS) and how does it differ from the Resource Allocation Competition (RAC)?"
  - "What are the key differences between compute instances and persistent instances in terms of lifespan and typical use cases?"
  - "What are the specific resource limits, such as vCPUs, RAM, and storage, allocated for compute and persistent instances under RAS?"
  - "What is the significance of the \"Cloud\" category assigned to this document?"
  - "How does the references tag function within the \"Notes\" section?"
  - "Why is the small HTML tag used to format this specific section of the text?"
  - "What is the default duration and wall-time for a RAS allocation?"
  - "In which month does the default renewal for RAS occur, and what allocation period does this align with?"
  - "How can a user submit a request to obtain RAS?"
  - "What is the significance of the \"Cloud\" category assigned to this document?"
  - "How does the references tag function within the \"Notes\" section?"
  - "Why is the small HTML tag used to format this specific section of the text?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Parent page: [Cloud](cloud.md)*

Any Digital Research Alliance of Canada user can access modest quantities of resources as soon as they have an Alliance account. The Rapid Access Service (**RAS**) allows users to experiment and to start working right away. Many research groups can meet their needs with the Rapid Access Service only. Users requiring larger resource quantities can apply to our annual [Resource Allocation Competition](../policies/rac_application_guide.md) (**RAC**). Primary Investigators (PIs) with a current RAC allocation are also able to request resources via RAS.

Using cloud resources, researchers can create ***cloud instances*** (also known as *virtual machines* or *VMs*). There are two options available for cloud resources:
* **Compute instances**: These are instances that have a **limited life-time** (wall-time) and typically have **constant high CPU** requirements. They are sometimes referred to as *batch* instances. Users may need a large number of compute instances for production activities. Maximum wall-time for compute instances is **one month**. Upon reaching their life-time limit these instances will be scheduled for deactivation and their owners will be notified in order to ensure they clean up their instances and download any required data. Any grace period is subject to resources availability at that time.
* **Persistent instances**: These are instances that are meant to run **indefinitely** and would include **Web servers**, **database servers**, etc. In general, these instances provide a persistent service and use **less CPU** power than compute instances.
* **vGPU**: Arbutus currently offers H100 GPUs in a single flavour for RAS use (**g1-12vgb-c3-35gb-125**). This flavour has 12GB GPU memory, 3 vCPUs, 35GB of memory, and 125GB of ephemeral storage. Alternative GPU flavours are available for RAC recipients; researcher feedback on useful resource combinations for those new flavours is welcomed. For more information on setting up your VM to use vGPUs, see [Using cloud vGPUs](using_cloud_vgpus.md).

## Cloud RAS resources limits

| Attributes | Compute instances[^both-renewal] | Persistent instances[^both-renewal] |
| :--------- | :------------------------------- | :---------------------------------- |
| May be requested by | PIs only                         | PIs only                            |
| vCPUs (see [VM flavours](virtual_machine_flavors.md)) | 80                               | 25                                  |
| vGPUs[^arbutusonly] | 1                                | 1                                   |
| Instances[^softquota] | 20                               | 10                                  |
| Volumes[^softquota] | 2                                | 10                                  |
| Volume snapshots[^softquota] | 2                                | 10                                  |
| RAM (GB) | 300                              | 50                                  |
| Floating IP | 2                                | 2                                   |
| Persistent storage (TB) | 10                               | 10                                  |
| Object storage (TB)[^arbutusonly] | 10                               | 10                                  |
| Shared filesystem storage (TB)[^arbutusonly] | 10                               | 10                                  |
| Default duration | 1 year[^renwal], with 1 month wall-time | 1 year (renewable)[^renwal]         |
| Default renewal | April[^renwal]                   | April[^renwal]                      |

## Requesting RAS
To request RAS, please [fill out this form](https://docs.google.com/forms/d/e/1FAIpQLSeU_BoRk5cEz3AvVLf3e9yZJq-OvcFCQ-mg7p4AWXmUkd5rTw/viewform).

## Notes
[^both-renewal]: Users may request both a compute and persistent allocation to share a single project. Storage is shared between the two allocations and is limited to 10TB/PI per storage type. PIs may request a 1-year renewal of their cloud RAS allocations an unlimited number of times; however, allocations will be given based on available resources and are not guaranteed. Requests made after January 1 will expire March of the following year and therefore may be longer than 1 year. Allocation requests made between May-December will be less than 1 year. Renewals will take effect in April.
[^arbutusonly]: Currently only available at Arbutus and only available subject to RAC project requirements.
[^softquota]: This is a metadata quota and not a hard limit, users can request an increase beyond these values without a RAC request.
[^renwal]: This is to align with the RAC allocation period of April-March.