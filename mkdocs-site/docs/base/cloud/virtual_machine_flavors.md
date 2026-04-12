---
title: "Virtual machine flavors"
slug: "virtual_machine_flavors"
lang: "base"

source_wiki_title: "Virtual machine flavors"
source_hash: "4de06374afdd996b84f3b15ae2623628"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:41:49.002080+00:00"

tags:
  - cloud

keywords:
  - "virtual machine"
  - "virtual hardware templates"
  - "OpenStack flavors"
  - "compute flavor"
  - "persistent flavor"

questions:
  - "What are OpenStack \"flavors\" and how can researchers view or request them for their projects?"
  - "What do the specific prefixes and numbers in a virtual machine flavor's naming convention represent?"
  - "What are the key differences in intended use cases, storage redundancy, and CPU management between \"c\" (compute) and \"p\" (persistent) flavors?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Parent page: [Cloud](cloud.md)*

!!! note
    Virtual hardware templates are called "flavours" in OpenStack, defining sizes for RAM, disk, number of cores, and so on. ... Flavours define a number of parameters, resulting in the user having a choice of what type of virtual machine to run—just like they would have if they were purchasing a physical server. - [NetApp OpenStack Deployment and Operations Guide](http://netapp.github.io/openstack-deploy-ops-guide/icehouse/content/section_nova-key-concepts.html)

Researchers are able to view all the flavours they have been allocated for their project. These can be seen in the Horizon Dashboard and via the [OpenStack command line client](openstack_command_line_clients.md) with the following command:

```bash
openstack flavour list --sort-column RAM
```

If you have a project and need a flavour not currently allocated, please email cloud@tech.alliancecan.ca.

Virtual machine flavours have names like: `c2-7.5gb-92`, `p1-0.75gb`, `g1-8gb-c4-22gb`. By convention the prefix "c" designates "compute", "p" designates "persistent", and "g" designates "vGPU". The prefix is followed by the number of virtual vCPUs/vGPUs, then the amount of RAM after the dash. If a second dash is present it is followed by the size of secondary ephemeral disk in gigabytes. In the case of vGPUs, the compute flavour is included after the vGPU information.

A virtual machine of "c" flavour is intended for jobs of finite lifetime and for development and testing tasks. It starts from a [qcow2](https://en.wikipedia.org/wiki/Qcow)-format image. Its disks reside on the local hardware running the VM and have no redundancy ([raid0](https://en.wikipedia.org/wiki/Standard_RAID_levels#RAID_0)). The root disk is typically 20GB in size. "c" flavour VMs also have a secondary ephemeral data disk. These storage devices are created and destroyed with the instance. The Arbutus cloud treats “c” flavours differently as they have no over-commit on CPU so are targeted towards CPU intensive tasks.

A virtual machine of "p" flavour is intended to run for an indeterminate length of time. There is no predefined root disk. The intended use of "p" flavours is that they should be [booted from a volume](working_with_volumes.md#booting-from-a-volume), in which case the instance will be backed by the Ceph storage system and have greater redundancy and resistance to failure than a "c" instance. We recommend using a volume size of at least 20GB for the persistent VM root disk. The Arbutus cloud treats “p” flavours differently as they will be on compute nodes with a higher level of redundancy (disk and network) and do over-commit the CPU so are geared towards web servers, database servers and instances that have a lower CPU or bursty CPU usage profile in general.