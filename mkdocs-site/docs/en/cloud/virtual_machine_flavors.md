---
title: "Virtual machine flavors/en"
slug: "virtual_machine_flavors"
lang: "en"

source_wiki_title: "Virtual machine flavors/en"
source_hash: "169a6f0bade3ee0eae3ea896b43ee1b5"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T12:43:42.626562+00:00"

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

!!! note
    Virtual hardware templates are called "flavors" in OpenStack, defining sizes for RAM, disk, number of cores, and so on. ... Flavors define a number of parameters, resulting in the user having a choice of what type of virtual machine to run—just like they would have if they were purchasing a physical server. - [*NetApp OpenStack Deployment and Operations Guide*](http://netapp.github.io/openstack-deploy-ops-guide/icehouse/content/section_nova-key-concepts.html)

Researchers are able to view all the flavors they have been allocated for their project. These can be seen in the Horizon Dashboard and via the [OpenStack command line client](openstack-command-line-clients.md) with the following command:

```bash
openstack flavor list --sort-column RAM
```

If you have a project and need a flavour not currently allocated, please email cloud@tech.alliancecan.ca.

Virtual machine flavors have names like:
`c2-7.5gb-92`
`p1-0.75gb`
`g1-8gb-c4-22gb`
By convention the prefix "c" designates "compute", "p" designates "persistent", and "g" designates "vGPU". The prefix is followed by the number of virtual vCPUs/vGPUs, then the amount of RAM after the dash. If a second dash is present it is followed by the size of secondary ephemeral disk in gigabytes. In the case of vGPUs, the compute flavour is included after the vGPU information.

A virtual machine of "c" flavor is intended for jobs of finite lifetime and for development and testing tasks. It starts from a [qcow2](https://en.wikipedia.org/wiki/Qcow)-format image. Its disks reside on the local hardware running the VM and have no redundancy ([raid0](https://en.wikipedia.org/wiki/Standard_RAID_levels#RAID_0)). The root disk is typically 20GB in size. "c" flavor VMs also have an secondary ephemeral data disk. These storage devices are created and destroyed with the instance. The Arbutus cloud treats “c” flavors differently as they have no over-commit on CPU so are targeted towards CPU intensive tasks.

A virtual machine of "p" flavor is intended to run for an indeterminate length of time. There is no predefined root disk. The intended use of "p" flavors is that they should be [booted from a volume](working-with-volumes.md#booting-from-a-volume), in which case the instance will be backed by the Ceph storage system and have greater redundancy and resistance to failure than a "c" instance. We recommend using a volume size of at least 20GB for the persistent VM root disk. The Arbutus cloud treats “p” flavors differently as they will be on compute nodes with a higher level of redundancy (disk and network) and do over-commit the CPU so are geared towards web servers, data base servers and instances that have a lower CPU or bursty CPU usage profile in general.