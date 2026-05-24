---
title: "RAC available resources"
slug: "rac_available_resources"
lang: "base"

source_wiki_title: "RAC available resources"
source_hash: "b69bec1d8d1afffc7c2bfe8bd1ecf31b"
last_synced: "2026-05-24T00:00:16.123503+00:00"
last_processed: "2026-05-24T00:49:31.189506+00:00"

tags:
  []

keywords:
  - "CCDB"
  - "GPU resources"
  - "Storage resources"
  - "Resource Allocation Competition"
  - "CCDB portal"
  - "Subsystems"
  - "Rorqual cluster"
  - "VMs"
  - "Cloud resources"
  - "memory requirements"
  - "CPU resources"
  - "request resources"
  - "storage resources"
  - "Compute resources"
  - "system allocations"

questions:
  - "How are the resources organized within the clusters and cloud systems for the Resource Allocation Competition 2026?"
  - "Which document prevails if there is a discrepancy between the resource requests in the attached application document and the online form?"
  - "How can applicants indicate in the CCDB portal that they are willing to accept a resource allocation on any suitable system?"
  - "How must a user format their request if they need both CPU and storage resources on the Rorqual cluster?"
  - "What are the specific rules and available virtual machine options when requesting cloud resources across different locations?"
  - "Which email address should be contacted for further assistance with resource allocation requests?"
  - "Why must users pay special attention to their memory requirements when requesting CPU resources?"
  - "Which system selection should be used to request GPU resources?"
  - "How does the system determine which storage resources are shown when a user selects a storage subsystem?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Below is the list of resources available for the **Resource Allocation Competition 2026**.

Resources in the clusters and in the cloud are organised by *subsystems*. Each subsystem will only show the resources that it has available. For example, the *trillium-storage* subsystem will only show /project storage as /nearline storage is available in the *hpss-storage* subsystem; *trillium-compute* will only show CPU (and memory), etc.

!!! important "Important"
    **There should be no discrepancies between the resources requested in the document attached to your application and the online form. In case of discrepancy, what is requested in the online form will prevail.**

| System | Sub-system (as shown on CCDB) | Available resources for each sub-system | Backup storage? |
|---|---|---|---|
| [Arbutus](../cloud/cloud.md) cloud | arbutus-compute-cloud | VCPU, VGPU, RAM, local ephemeral disk, volumes, snapshots, floating IPs, volume and snapshot storage, shared filesystem storage\*, object storage | No |
| ^ | arbutus-persistent-cloud | ^ | ^ |
| ^ | arbutus-dcache | dCache storage | No |
| [Rorqual](../clusters/rorqual.md) cluster | rorqual-compute | CPU | No |
| ^ | rorqual-gpu | GPU | No |
| ^ | rorqual-storage | Project storage, Nearline storage | Yes |
| [Béluga](../cloud/cloud.md) cloud | beluga-compute-cloud | VCPU, RAM, local ephemeral disk, volumes, snapshots, floating IPs, volume and snapshot storage | No |
| ^ | beluga-persistent-cloud | ^ | ^ |
| [Fir](../software/fir.md) cluster | fir-compute | CPU | No |
| ^ | fir-gpu | GPU | No |
| ^ | fir-storage | Project storage, Nearline storage, dCache storage | Yes |
| Fir cloud | fir-persistent-cloud | VCPU, RAM, local ephemeral disk, volumes, snapshots, floating IPs, volume and snapshot storage, object storage | No |
| ^ | fir-compute-cloud | ^ | ^ |
| [Nibi](../clusters/nibi.md) cluster | nibi-compute | CPU | No |
| ^ | nibi-gpu | GPU | No |
| ^ | nibi-storage | Project storage, Nearline storage, dCache storage | Yes |
| [Nibi](../cloud/cloud.md) cloud | nibi-persistent-cloud | VCPU, RAM, local ephemeral disk, volumes, snapshots, floating IPs, volume and snapshot storage | No |
| [Narval](../clusters/narval.md) cluster | narval-compute | CPU | No |
| ^ | narval-gpu | GPU | No |
| ^ | narval-storage | Project storage | Yes |
| [Trillium](../clusters/trillium.md) cluster | trillium-compute | CPU | No |
| ^ | trillium-gpu | GPU | No |
| ^ | trillium-storage | Project storage | Yes |
| HPSS | hpss-storage | Nearline storage | No |

\* The shared filesystem storage is backed up.

## How to request resources in the online RAC application form
On the CCDB portal, go to the *Resource Request* section of the corresponding Resources for Research Groups (RRG) or Research Platforms and Portals (RPP) online application form.

The dropdown menu under *New resource request* will show the list of all systems and subsystems with the corresponding resources available for allocation. To indicate that your request can be allocated in any resource and that you do not have a preference for a particular one, please check the option "I have to select a system but I don’t mind receiving an allocation on any other suitable one" in the *Reason for selecting system* section.

**1. Requesting HPC resources:** compute and storage resources are shown as different subsystems on CCDB following this convention:

*   system-compute (e.g., *rorqual-compute*): select these to request CPU resources. Please pay special attention to your memory requirements as this will be taken into account for final allocations.
*   system-gpu (e.g., *rorqual-gpu*): select these to request GPU resources.
*   system-storage (e.g., *rorqual-storage*): select these to request storage resources on a particular system. Each subsystem will only show the storage resources (/project, /nearline, etc.) available for that particular subsystem.

For example, if you want to request both CPU resources and /project storage resources on the Rorqual cluster, you will have to fill in two separate requests: one with the *rorqual-compute* subsystem for core years and memory, and another one with the *rorqual-storage* subsystem for /project storage (in TB).

**2. Requesting Cloud resources:** If you need to request cloud resources in more than one location, then you will have to make one request for each location. On CCDB, cloud resources follow this convention:

*   *system-compute-cloud* or *system-persistent-cloud*: you can select compute or persistent VMs on the Arbutus, Fir and Béluga clouds, but only persistent VMs on the Nibi cloud. Each cloud resource will **only** show the specific "flavours" of VMs available for that particular site.

Please email allocations@tech.alliancecan.ca with any questions on how to request resources.