---
title: "Cloud RAS Allocations/en"
slug: "cloud_ras_allocations"
lang: "en"

source_wiki_title: "Cloud RAS Allocations/en"
source_hash: "9d213571d7e223d1233c95444c996f5c"
last_synced: "2026-08-26T10:16:11.334907+00:00"
last_processed: "2026-08-26T11:07:12.059865+00:00"

tags:
  - cloud

keywords:
  - "Rapid Access Service (RAS)"
  - "RAC allocation period"
  - "Google form"
  - "Resource Allocation Competition (RAC)"
  - "Requesting RAS"
  - "Category:Cloud"
  - "Persistent instances"
  - "renewable"
  - "Default duration"
  - "Compute instances"
  - "Notes"
  - "vGPU"
  - "references"
  - "Category"
  - "Cloud"

questions:
  - "What are the key differences between compute instances and persistent instances in the Cloud RAS offering?"
  - "How can users request Rapid Access Service (RAS) resources, and what are the specific limits for compute and persistent instances?"
  - "Which vGPU options are provided for RAS users, and how do they compare to the GPU flavors available to RAC recipients?"
  - "What information is intended to be included in the \"Notes\" section?"
  - "Which sources or citations are expected to be listed within the <references/> tag?"
  - "Why is the article categorized under \"Cloud\" and what relevance does that category have?"
  - "What is the default duration and renewal period for the RAC allocation mentioned in the text?"
  - "When does the default renewal for the allocation occur each year?"
  - "How can someone request RAS according to the provided instructions?"

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

*   **Compute instances**: These are instances that have a **limited life-time** (wall-time) and typically have **constant high CPU** requirements. They are sometimes referred to as *batch* instances. Users may need a large number of compute instances for production activities. Maximum wall-time for compute instances is **one month**. Upon reaching their life-time limit these instances will be scheduled for deactivation and their owners will be notified in order to ensure they clean up their instances and download any required data. Any grace period is subject to resources availability at that time.
*   **Persistent instances**: These are instances that are meant to run **indefinitely** and would include **Web servers**, **database servers**, etc. In general, these instances provide a persistent service and use **less CPU** power than compute instances.
*   **vGPU**: Arbutus currently offers H100 GPUs in a single flavour for RAS use (**g1-12gb-c3-35gb-125**). This flavour has 12GB GPU memory, 3 vCPUs, 35GB of memory, and 125GB of ephemeral storage. Alternative GPU flavours are available for RAC recipients; researcher feedback on useful resource combinations for those new flavours is welcomed. For more information on setting up your VM to use vGPUs, see [Using cloud vGPUs](using_cloud_vgpus.md).

## Cloud RAS resources limits

!!! note "RAS Allocation Renewal and Storage"
    Users may request both a compute and persistent allocation to share a single project. Storage is shared between the two allocations and is limited to 10TB/PI per storage type. PIs may request a 1-year renewal of their cloud RAS allocations an unlimited number of times; however, allocations will be given based on available resources and are not guaranteed. Requests made after January 1 will expire March of the following year and therefore may be longer than 1 year. Allocation requests made between May-December will be less than 1 year. Renewals will take effect in April.

| Attributes                       | Compute instances              | Persistent instances       |
| :------------------------------- | :----------------------------- | :------------------------- |
| May be requested by              | PIs only                       | PIs only                   |
| vCPUs (see [VM flavours](virtual_machine_flavors.md)) | 80                             | 25                         |
| vGPU (RGU-years)[^1]             | 1.8                            |                            |
| Instances[^2]                    | 20                             | 10                         |
| Volumes[^2]                      | 2                              | 10                         |
| Volume snapshots[^2]             | 2                              | 10                         |
| RAM (GB)                         | 300                            | 50                         |
| Floating IP                      | 2                              |                            |
| Persistent storage (TB)          | 10                             |                            |
| Object storage (TB)[^1]          | 10                             |                            |
| Shared filesystem storage (TB)[^1] | 10                             |                            |
| Default duration[^3]             | 1 year, with 1 month wall-time | 1 year (renewable)         |
| Default renewal[^3]              | April                          | April                      |

## Requesting RAS
To request RAS, please [fill out this form](https://docs.google.com/forms/d/e/1FAIpQLSeU_BoRk5cEz3AvVLf3e9yZJq-OvcFCQ-mg7p4AWXmUkd5rTw/viewform).

[^1]: Currently only available at Arbutus and only available subject to RAC project requirements.
[^2]: This is a metadata quota and not a hard limit, users can request an increase beyond these values without a RAC request.
[^3]: This is to align with the RAC allocation period of April-March.