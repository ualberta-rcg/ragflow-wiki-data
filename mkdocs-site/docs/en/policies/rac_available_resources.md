---
title: "RAC available resources/en"
slug: "rac_available_resources"
lang: "en"

source_wiki_title: "RAC available resources/en"
source_hash: "beaad741ea1ee1bf73731b9f8e53fead"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:55:03.996084+00:00"

tags:
  []

keywords:
  - "Cloud resources"
  - "compute and storage resources"
  - "CCDB portal"
  - "VM flavours"
  - "compute or persistent VMs"
  - "subsystem"
  - "CCDB"
  - "online application form"
  - "Resource Allocation Competition"
  - "Rorqual cluster"
  - "locations"
  - "HPC resources"
  - "separate requests"
  - "storage resources"
  - "CPU resources"

questions:
  - "What is the policy regarding discrepancies between the resource requests in the attached application document and the online form?"
  - "Which specific systems and sub-systems provide backup storage according to the available resources list?"
  - "How must an applicant submit their request in the CCDB portal if they require multiple types of resources, such as both CPU and storage, on a single cluster?"
  - "How must a user proceed when requesting cloud resources across multiple locations?"
  - "What are the differences in virtual machine availability between the Arbutus, Fir, Béluga clouds and the Nibi cloud?"
  - "Which email address should be contacted for assistance with the resource allocation process?"
  - "How are storage resources displayed and restricted within individual subsystems?"
  - "What is the required procedure for requesting both CPU and storage resources on the Rorqual cluster?"
  - "Which specific subsystems and units of measurement must be used when requesting core years versus project storage?"
  - "How must a user proceed when requesting cloud resources across multiple locations?"
  - "What are the differences in virtual machine availability between the Arbutus, Fir, Béluga clouds and the Nibi cloud?"
  - "Which email address should be contacted for assistance with the resource allocation process?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Below is the list of resources available for the **Resource Allocation Competition** **2026**.

Resources in the clusters and in the cloud are organized by subsystems. Each subsystem will only show the resources that it has available. For example, the `trillium-storage` subsystem will only show `/project` storage as `/nearline` storage is available in the `hpss-storage` subsystem; `trillium-compute` will only show CPU (and memory), etc.

!!! warning "Important"
    **There should be no discrepancies between the resources requested in the document attached to your application and the online form. In case of discrepancy, what is requested in the online form will prevail.**

| System                             | Sub-system (as shown on CCDB)      | Available resources for each sub-system                                                                                    | Backup storage? |
| :--------------------------------- | :--------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :-------------- |
| [Arbutus](cloud.md) cloud          | `arbutus-compute-cloud`            | VCPU, VGPU, RAM, local ephemeral disk, volumes, snapshots, floating IPs, volume and snapshot storage, shared filesystem storage*, object storage | No              |
| [Arbutus](cloud.md) cloud          | `arbutus-persistent-cloud`         | VCPU, VGPU, RAM, local ephemeral disk, volumes, snapshots, floating IPs, volume and snapshot storage, shared filesystem storage*, object storage | No              |
| [Arbutus](cloud.md) cloud          | `arbutus-dcache`                   | dCache storage                                                                                                             | No              |
| [Rorqual](rorqual.md) cluster      | `rorqual-compute`                  | CPU                                                                                                                        | No              |
| [Rorqual](rorqual.md) cluster      | `rorqual-gpu`                      | GPU                                                                                                                        | No              |
| [Rorqual](rorqual.md) cluster      | `rorqual-storage`                  | Project storage, Nearline storage                                                                                          | Yes             |
| [Béluga](cloud.md) cloud           | `beluga-compute-cloud`             | VCPU, RAM, local ephemeral disk, volumes, snapshots, floating IPs, volume and snapshot storage                             | No              |
| [Béluga](cloud.md) cloud           | `beluga-persistent-cloud`          | VCPU, RAM, local ephemeral disk, volumes, snapshots, floating IPs, volume and snapshot storage                             | No              |
| [Fir](fir.md) cluster              | `fir-compute`                      | CPU                                                                                                                        | No              |
| [Fir](fir.md) cluster              | `fir-gpu`                          | GPU                                                                                                                        | No              |
| [Fir](fir.md) cluster              | `fir-storage`                      | Project storage, Nearline storage, dCache storage                                                                          | Yes             |
| Fir cloud                          | `fir-persistent-cloud`             | VCPU, RAM, local ephemeral disk, volumes, snapshots, floating IPs, volume and snapshot storage, object storage             | No              |
| Fir cloud                          | `fir-compute-cloud`                | VCPU, RAM, local ephemeral disk, volumes, snapshots, floating IPs, volume and snapshot storage, object storage             | No              |
| [Nibi](nibi.md) cluster            | `nibi-compute`                     | CPU                                                                                                                        | No              |
| [Nibi](nibi.md) cluster            | `nibi-gpu`                         | GPU                                                                                                                        | No              |
| [Nibi](nibi.md) cluster            | `nibi-storage`                     | Project storage, Nearline storage, dCache storage                                                                          | Yes             |
| [Nibi](cloud.md) cloud             | `nibi-persistent-cloud`            | VCPU, RAM, local ephemeral disk, volumes, snapshots, floating IPs, volume and snapshot storage                             | No              |
| [Narval](narval.md) cluster        | `narval-compute`                   | CPU                                                                                                                        | No              |
| [Narval](narval.md) cluster        | `narval-gpu`                       | GPU                                                                                                                        | No              |
| [Narval](narval.md) cluster        | `narval-storage`                   | Project storage                                                                                                            | Yes             |
| [Trillium](trillium.md) cluster    | `trillium-compute`                 | CPU                                                                                                                        | No              |
| [Trillium](trillium.md) cluster    | `trillium-gpu`                     | GPU                                                                                                                        | No              |
| [Trillium](trillium.md) cluster    | `trillium-storage`                 | Project storage                                                                                                            | Yes             |
| HPSS                               | `hpss-storage`                     | Nearline storage                                                                                                           | No              |

* The shared filesystem storage is backed up.

## How to request resources in the online RAC application form

On the CCDB portal, go to the *Resource Request* section of the corresponding Resources for Research Groups (RRG) or Research Platforms and Portals (RPP) online application form.

The dropdown menu under *New resource request* will show the list of all systems and subsystems with the corresponding resources available for allocation. To indicate that your request can be allocated in any resource and that you do not have a preference for a particular one, please check the option "I have to select a system but I don’t mind receiving an allocation on any other suitable one" in the *Reason for selecting system* section.

1.  **Requesting HPC resources:** compute and storage resources are shown as different subsystems on CCDB following this convention:
    *   `system-compute` (e.g. `rorqual-compute`): select these to request CPU resources. Please pay special attention to your memory requirements as this will be taken into account for final allocations.
    *   `system-gpu` (e.g. `rorqual-gpu`): select these to request GPU resources.
    *   `system-storage` (e.g. `rorqual-storage`): select these to request storage resources on a particular system. Each subsystem will only show the storage resources (`/project`, `/nearline`, etc.) available for that particular subsystem.

    For example, if you want to request both CPU resources and `/project` storage resources on the **Rorqual cluster**, you will have to fill in two separate requests: one with the `rorqual-compute` subsystem for core years and memory, and another one with the `rorqual-storage` subsystem for `/project` storage (in TB).

2.  **Requesting Cloud resources:** If you need to request cloud resources in more than one location, then you will have to make one request for each location. On CCDB, cloud resources follow this convention:
    *   `system-compute-cloud` or `system-persistent-cloud`: you can select compute or persistent VMs on the `Arbutus`, `Fir` and `Béluga` clouds, but only persistent VMs on the `NIbi` cloud. Each cloud resource will **only** show the specific "flavours" of VMs available for that particular site.

Please email allocations@tech.alliancecan.ca with any questions on how to request resources.