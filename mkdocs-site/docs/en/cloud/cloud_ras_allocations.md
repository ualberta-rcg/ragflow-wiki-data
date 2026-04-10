---
title: "Cloud RAS Allocations/en"
slug: "cloud_ras_allocations"
lang: "en"

source_wiki_title: "Cloud RAS Allocations/en"
source_hash: "27f8a25bfc66b84707042ca398fb2e8c"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T05:33:42.161035+00:00"

tags:
  - cloud

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

*Parent page: [Cloud](cloud.md)*

Any Digital Research Alliance of Canada user can access modest quantities of resources as soon as they have an Alliance account. The Rapid Access Service (**RAS**) allows users to experiment and to start working right away. Many research groups can meet their needs with the Rapid Access Service only. Users requiring larger resource quantities can apply to our annual [Resource Allocation Competition](rac-application-guide.md) (**RAC**). Primary Investigators (PIs) with a current RAC allocation are also able to request resources via RAS.

Using cloud resources, researchers can create ***cloud instances*** (also known as *virtual machines* or *VMs*). There are two options available for cloud resources:
*   **Compute instances**: These are instances that have a **limited life-time** (wall-time) and typically have **constant high CPU** requirements. They are sometimes referred to as *batch* instances. Users may need a large number of compute instances for production activities. Maximum wall-time for compute instances is **one month**. Upon reaching their life-time limit these instances will be scheduled for deactivation and their owners will be notified in order to ensure they clean up their instances and download any required data. Any grace period is subject to resources availability at that time.
*   **Persistent instances**: These are instances that are meant to run **indefinitely** and would include **Web servers**, **database servers**, etc. In general, these instances provide a persistent service and use **less CPU** power than compute instances.
*   **vGPU**: Arbutus currently offers H100 GPUs in a single flavour for RAS use (**g1-12vgb-c3-35gb-125**). This flavour has 12GB GPU memory, 3 vCPUs, 35GB of memory, and 125GB of ephemeral storage. Alternative GPU flavours are available for RAC recipients; researcher feedback on useful resource combinations for those new flavours is welcomed. For more information on setting up your VM to use vGPUs, see [Using cloud vGPUs](using-cloud-vgpus.md).

## Cloud RAS resources limits

| Attributes | Compute instances[^both-renewal] | Persistent instances[^both-renewal] |
| :--- | :--- | :--- |
| May be requested by | PIs only | PIs only |
| vCPUs (see [VM flavours](virtual-machine-flavors.md)) | 80 | 25 |
| vGPUs[^arbutusonly-vpgus] | 1 | 1 |
| Instances[^softquota] | 20 | 10 |
| Volumes[^softquota] | 2 | 10 |
| Volume snapshots[^softquota] | 2 | 10 |
| RAM (GB) | 300 | 50 |
| Floating IP | 2 | 2 |
| Persistent storage (TB) | 10 | 10 |
| Object storage (TB)[^arbutusonly-object] | 10 | 10 |
| Shared filesystem storage (TB)[^arbutusonly-sharedfs] | 10 | 10 |
| Default duration | 1 year[^renwal-duration], with 1 month wall-time | 1 year (renewable)[^renwal-duration] |
| Default renewal | April[^renwal-renewal] | April[^renwal-renewal] |

## Requesting RAS
To request RAS, please [fill out this form](https://docs.google.com/forms/d/e/1FAIpQLSeU_BoRk5cEz3AvVLf3e9yZJq-OvcFCQ-mg7p4AWXmUkd5rTw/viewform).

## Notes

!!! note "Note (both-renewal): Compute and Persistent Allocations"
    Users may request both a compute and persistent allocation to share a single project. Storage is shared between the two allocations and is limited to 10TB/PI per storage type. PIs may request a 1-year renewal of their cloud RAS allocations an unlimited number of times; however, allocations will be given based on available resources and are not guaranteed. Requests made after January 1 will expire March of the following year and therefore may be longer than 1 year. Allocation requests made between May-December will be less than 1 year. Renewals will take effect in April.

!!! note "Note (arbutusonly-vpgus): Arbutus Only (vGPUs)"
    Currently only available at Arbutus and only available subject to RAC project requirements.

!!! note "Note (softquota): Metadata Quota"
    This is a metadata quota and not a hard limit, users can request an increase beyond these values without a RAC request.

!!! note "Note (arbutusonly-object): Arbutus Only (Object Storage)"
    Currently only available at Arbutus and only available subject to RAC project requirements.

!!! note "Note (arbutusonly-sharedfs): Arbutus Only (Shared Filesystem Storage)"
    Currently only available at Arbutus and only available subject to RAC project requirements.

!!! note "Note (renwal-duration): Allocation Duration"
    This is to align with the RAC allocation period of April-March.

!!! note "Note (renwal-renewal): Allocation Renewal"
    This is to align with the RAC allocation period of April-March.