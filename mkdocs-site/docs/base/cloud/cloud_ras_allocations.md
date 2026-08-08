---
title: "Cloud RAS Allocations"
slug: "cloud_ras_allocations"
lang: "base"

source_wiki_title: "Cloud RAS Allocations"
source_hash: "7cf0c6e2cd275d2fd0b9cc0dd3435170"
last_synced: "2026-08-07T19:46:17.777436+00:00"
last_processed: "2026-08-07T22:28:37.426696+00:00"

tags:
  - cloud

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
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

| Attributes                  | Compute instances | Persistent instances |
| :-------------------------- | :---------------: | :------------------: |
| May be requested by         | PIs only          | PIs only             |
| vCPUs (see [VM flavours](virtual_machine_flavors.md)) | 80                | 25                   |
| vGPU (RGU-years)            |       1.8         |                      |
| Instances                   | 20                | 10                   |
| Volumes                     | 2                 | 10                   |
| Volume snapshots            | 2                 | 10                   |
| RAM (GB)                    | 300               | 50                   |
| Floating IP                 | 2                 | 2                    |
| Persistent storage (TB)     |       10          |                      |
| Object storage (TB)         |       10          |                      |
| Shared filesystem storage (TB) |       10          |                      |
| Default duration            | 1 year, with 1 month wall-time | 1 year (renewable) |
| Default renewal             | April             | April                |

!!! note "Shared Projects, Storage, and Renewals"
    Users may request both a compute and persistent allocation to share a single project. Storage is shared between the two allocations and is limited to 10TB/PI per storage type. PIs may request a 1-year renewal of their cloud RAS allocations an unlimited number of times; however, allocations will be given based on available resources and are not guaranteed. Requests made after January 1 will expire March of the following year and therefore may be longer than 1 year. Allocation requests made between May-December will be less than 1 year. Renewals will take effect in April.

!!! note "Arbutus-Only Resources"
    Object storage and Shared filesystem storage are currently only available at Arbutus and only available subject to RAC project requirements.

!!! note "Soft Quotas"
    The limits for Instances, Volumes, and Volume snapshots are metadata quotas and not hard limits. Users can request an increase beyond these values without a RAC request.

!!! note "Renewal Period Alignment"
    The default duration and renewal month for RAS allocations are set to align with the RAC allocation period of April-March.

## Requesting RAS
To request RAS, please [fill out this form](https://docs.google.com/forms/d/e/1FAIpQLSeU_BoRk5cEz3AvVLf3e9yZJq-OvcFCQ-mg7p4AWXmUkd5rTw/viewform).