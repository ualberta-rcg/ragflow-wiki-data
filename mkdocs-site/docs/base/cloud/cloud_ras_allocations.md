---
title: "Cloud RAS Allocations"
slug: "cloud_ras_allocations"
lang: "base"

source_wiki_title: "Cloud RAS Allocations"
source_hash: "047c0728024a31875bdbead3754b84bd"
last_synced: "2026-08-26T10:16:11.334907+00:00"
last_processed: "2026-08-26T11:06:42.284308+00:00"

tags:
  - cloud

keywords:
  - "Rapid Access Service (RAS)"
  - "RAC project requirements"
  - "Resource Allocation Competition (RAC)"
  - "default duration"
  - "shared filesystem storage"
  - "Google Form"
  - "allocation period April-March"
  - "Persistent instances"
  - "renewable"
  - "Compute instances"
  - "Notes"
  - "vGPU (H100)"
  - "Requesting RAS"
  - "fill out this form"
  - "Cloud"

questions:
  - "What are the key differences between compute instances and persistent instances in the Cloud RAS offering?"
  - "How can users obtain larger resource allocations if the Rapid Access Service limits are insufficient for their research needs?"
  - "What are the default resource limits (e.g., vCPUs, storage, duration) and renewal schedule for Cloud RAS allocations?"
  - "How can a user request RAS using the information provided?"
  - "Where is the Google Form link located for submitting a RAS request?"
  - "Under which category is this RAS request page classified?"
  - "What is the default allocation duration and its renewal schedule?"
  - "How much shared filesystem storage (in TB) is provided under the RAC project requirements?"
  - "During which month does the allocation period align with the RAC fiscal year?"

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

*   **Compute instances**: These are instances that have a **limited life-time** (wall-time) and typically have **constant high CPU** requirements. They are sometimes referred to as *batch* instances. Users may need a large number of compute instances for production activities. Maximum wall-time for compute instances is **one month**. Upon reaching their life-time limit these instances will be scheduled for deactivation and their owners will be notified in order to ensure they clean up their instances and download any required data. Any grace period is subject to resource availability at that time.
*   **Persistent instances**: These are instances that are meant to run **indefinitely** and would include **Web servers**, **database servers**, etc. In general, these instances provide a persistent service and use **less CPU** power than compute instances.
*   **vGPU**: Arbutus currently offers H100 GPUs in a single flavour for RAS use (`g1-12gb-c3-35gb-125`). This flavour has 12GB GPU memory, 3 vCPUs, 35GB of memory, and 125GB of ephemeral storage. Alternative GPU flavours are available for RAC recipients; researcher feedback on useful resource combinations for those new flavours is welcomed. For more information on setting up your VM to use vGPUs, see [Using cloud vGPUs](using_cloud_vgpus.md).

## Cloud RAS resources limits

!!! note
    Users may request both a compute and persistent allocation to share a single project. Storage is shared between the two allocations and is limited to 10TB/PI per storage type. PIs may request a 1-year renewal of their cloud RAS allocations an unlimited number of times; however, allocations will be given based on available resources and are not guaranteed. Requests made after January 1 will expire March of the following year and therefore may be longer than 1 year. Allocation requests made between May-December will be less than 1 year. Renewals will take effect in April.

| Attributes | Compute instances | Persistent instances |
| :-------------------------------------- | :------------------------------------------- | :--------------------------- |
| May be requested by | PIs only | PIs only |
| vCPUs (see [VM flavours](virtual_machine_flavors.md)) | 80 | 25 |
| vGPU (RGU-years)[^1] | 1.8 | 1.8 |
| Instances[^2] | 20 | 10 |
| Volumes[^2] | 2 | 10 |
| Volume snapshots[^2] | 2 | 10 |
| RAM (GB) | 300 | 50 |
| Floating IP | 2 | 2 |
| Persistent storage (TB) | 10 | 10 |
| Object storage (TB)[^1] | 10 | 10 |
| Shared filesystem storage (TB)[^1] | 10 | 10 |
| Default duration | 1 year[^3], with 1 month wall-time | 1 year (renewable)[^3] |
| Default renewal | April[^3] | April[^3] |

## Requesting RAS

To request RAS, please [fill out this form](https://docs.google.com/forms/d/e/1FAIpQLSeU_BoRk5cEz3AvVLf3e9yZJq-OvcFCQ-mg7p4AWXmUkd5rTw/viewform).

## Notes

[^1]: Currently only available at Arbutus and only available subject to RAC project requirements.
[^2]: This is a metadata quota and not a hard limit, users can request an increase beyond these values without a RAC request.
[^3]: This is to align with the RAC allocation period of April-March.