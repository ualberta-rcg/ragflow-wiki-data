---
title: "Cloud RAS Allocations"
slug: "cloud_ras_allocations"
lang: "base"

source_wiki_title: "Cloud RAS Allocations"
source_hash: "b25366e6416faee78ec864c087053d86"
last_synced: "2026-11-08T02:07:32.985064+00:00"
last_processed: "2026-11-08T02:54:09.422009+00:00"

tags:
  - cloud

keywords:
  - "default renewal"
  - "Resource Allocation Competition (RAC)"
  - "Requesting RAS"
  - "Compute instances"
  - "Rapid Access Service (RAS)"
  - "renewable"
  - "Persistent instances"
  - "Google Forms"
  - "1 year"
  - "Notes"
  - "vGPU"
  - "shared filesystem storage"
  - "default duration"
  - "Cloud"
  - "fill out this form"

questions:
  - "What are the main differences between Compute instances and Persistent instances offered through the Cloud Rapid Access Service?"
  - "How can users obtain larger quantities of cloud resources beyond the Rapid Access Service, and what is the purpose of the Resource Allocation Competition (RAC)?"
  - "What are the current limits and renewal policies for Cloud RAS allocations, such as vCPU, RAM, storage, and allocation duration?"
  - "What is the purpose of the RAS request mentioned in the text?"
  - "How can a user submit a request for RAS according to the instructions?"
  - "Where can the Google Form for requesting RAS be accessed?"
  - "What is the default allocation period for the shared filesystem storage?"
  - "How many terabytes of shared filesystem storage are allocated?"
  - "In which month does the default renewal of the allocation occur?"

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

Using cloud resources, researchers can create *cloud instances* (also known as *virtual machines* or *VMs*). There are two options available for cloud resources:
*   **Compute instances**: These are instances that have a **limited life-time** (wall-time) and typically have **constant high CPU** requirements. They are sometimes referred to as *batch* instances. Users may need a large number of compute instances for production activities. Maximum wall-time for compute instances is **one month**. Upon reaching their life-time limit these instances will be scheduled for deactivation and their owners will be notified in order to ensure they clean up their instances and download any required data. Any grace period is subject to resources availability at that time.
*   **Persistent instances**: These are instances that are meant to run **indefinitely** and would include **Web servers**, **database servers**, etc. In general, these instances provide a persistent service and use **less CPU** power than compute instances.
*   **vGPU**: Arbutus currently offers H100 GPUs in a single flavour for RAS use (**g1-12gb-c3-35gb-125**). This flavour has 12GB GPU memory, 3 vCPUs, 35GB of memory, and 125GB of ephemeral storage. Alternative GPU flavours are available for RAC recipients; researcher feedback on useful resource combinations for those new flavours is welcomed. For more information on setting up your VM to use vGPUs, see [Using cloud vGPUs](using_cloud_vgpus.md).

## Cloud RAS resources limits

| Attributes | Compute instances[^both-renewal] | Persistent instances[^both-renewal] |
|---|---|---|
| May be requested by | PIs only | PIs only |
| vCPUs (see [VM flavours](virtual_machine_flavors.md)) | 80 | 25 |
| vGPU (RGU-years)[^arbutusonly] | 1.8 | |
| Instances[^softquota] | 20 | 10 |
| Volumes[^softquota] | 2 | 10 |
| Volume snapshots[^softquota] | 2 | 10 |
| RAM (GB) | 300 | 50 |
| Floating IP | 2 | |
| Persistent storage (TB) | 10 | |
| Object storage (TB)[^arbutusonly] | 10 | |
| Shared filesystem storage (TB)[^arbutusonly] | 10 | |
| Default duration | 1 year[^renwal], with 1 month wall-time | 1 year (renewable)[^renwal] |
| Default renewal | April[^renwal] | April[^renwal] |

## Requesting RAS
To request RAS, please [fill out this form](https://docs.google.com/forms/d/e/1FAIpQLSeU_BoRk5cEz3AvVLf3e9yZJq-OvcFCQ-mg7p4AWXmUk5rTw/viewform).

## Notes
[^both-renewal]: Users may request both a compute and persistent allocation to share a single project. Storage is shared between the two allocations and is limited to 10TB/PI per storage type. PIs may request a 1-year renewal of their cloud RAS allocations an unlimited number of times; however, allocations will be given based on available resources and are not guaranteed. Requests made after January 1 will expire March of the following year and therefore may be longer than 1 year. Allocation requests made between May-December will be less than 1 year. Renewals will take effect in April.
[^arbutusonly]: Currently only available at Arbutus however RAS access to this limited resource is subject to availability.
[^softquota]: This is a metadata quota and not a hard limit, users can request an increase beyond these values without a RAC request.
[^renwal]: This is to align with the RAC allocation period of April-March.