---
title: "Cloud"
tags:
  - cloud

keywords:
  []
---

We offer [Infrastructure as a Service](https://en.wikipedia.org/wiki/Cloud_computing#Infrastructure_as_a_service_.28IaaS.29) that supports [virtualization](https://en.wikipedia.org/wiki/Hardware_virtualization).

A user of the cloud will typically create or <i>spin up</i> one or more virtual machines (VMs or <i>instances</i>). He or she then logs into the VM with administrative privileges, installs any desired software, and runs the software applications needed. These applications could be as diverse as a CPU-intensive analysis of particle physics data, or a web service directed towards scholars of literature and the humanities. The advantage is that the user has complete control over the collection of installed software (the <i>software stack</i>). The disadvantage is that the user must have some degree of experience in installing software and otherwise managing a computer.

Virtual machines can be easily replicated. One can take a <i>snapshot</i> of a VM which can then be started again elsewhere. This makes it easy to replicate or scale up a service, and to recover from (for example) a power interruption.

If you can fit your work easily into the [HPC](https://en.wikipedia.org/wiki/Supercomputer) [batch](https://en.wikipedia.org/wiki/Batch_processing) submission workflow and environment (see [What is a scheduler?](what-is-a-scheduler?.md)) it is preferable to work outside the cloud, as there are more [resources available](national-systems.md) for HPC and software is already configured and installed for many common needs. There are also tools like [Apptainer](apptainer.md) to run custom software stacks inside containers within our HPC clusters.
If your need isn't served by Apptainer or HPC batch, then the cloud is your solution.

## Getting a cloud project
* Review and understand the [important role](cloud-shared-security-responsibility-model.md) you are about to take on to [safeguard your research](https://science.gc.ca/site/science/en/safeguarding-your-research) and the shared cloud infrastructure.
* If you do not have an account with us, create one with [these instructions](https://docs.alliancecan.ca/wiki/Apply_for_a_CCDB_account).
* A [project](managing_your_cloud_resources_with_openstack#projects.md) is an allocation of resources for creating VMs within a cloud.
* If you are a primary investigator (PI) with an active cloud resource allocation (see [RAC](https://alliancecan.ca/en/services/advanced-research-computing/research-portal/accessing-resources/resource-allocation-competitions)) you should already have a project. See the sections below on using the cloud to get started. If not or if you are not sure please contact [technical support](technical-support.md).
* Otherwise go to the [Alliance cloud project and RAS request form](https://docs.google.com/forms/d/e/1FAIpQLSeU_BoRk5cEz3AvVLf3e9yZJq-OvcFCQ-mg7p4AWXmUkd5rTw/viewform) to
** request access to an existing project (see the section below for information you will need to supply)
** and if you are a PI you may also
*** request a new project with our Rapid Access Service ([RAS](cloud_ras_allocations.md)),
*** or request an increase in quota of an existing project.

* Requests are typically processed within two business days.

### Preparing your request
* When requesting access to an existing project, you will need to know the project name and which cloud it is on. See the section on [projects](managing_your_cloud_resources_with_openstack#projects.md) for guidance on how to find the project name and the section about [cloud systems](cloud#cloud_systems.md) for a list of our clouds. Requests for access must be confirmed by the PI owning the project.
* When requesting either a new project or an increase in quota for an existing project some justification, in the form of a few sentences, is required:
**why you need cloud resources,
**why an HPC cluster is not suitable,
**your plans for efficient usage of your resources,
**your plans for maintenance and security ([refer to this page](security_considerations_when_running_a_vm.md)).
*A PI may own up to 3 projects, but the sum of all project quotas must be within the [RAS](cloud_ras_allocations.md) allocation limits. A PI may have both compute and persistent cloud RAS allocations.

## Creating a virtual machine on the cloud infrastructure
* The [cloud quick start guide](cloud-quick-start.md) describes how to manually create your first VM.
* Review the [glossary](cloud_technical_glossary.md) to learn definitions of common topics.
* Consider [storage options](cloud_storage_options.md) best suited to your use case.
* See the [troubleshooting guide](cloud-troubleshooting-guide.md) for steps to deal with common issues in cloud computing.

## User responsibilities
For each cloud project, you are responsible for
*[Creating and managing your virtual machines](managing_your_cloud_resources_with_openstack.md)
*[Securing and patching software on your VM](cloud_shared_security_responsibility_model.md)
*[Defining security groups to allow access to your network](managing_your_cloud_resources_with_openstack#security_groups.md)
*[Creating user accounts](managing_your_linux_vm.md)
*[Following best practices](vm-best-practices.md)
*[Considering security issues](security_considerations_when_running_a_vm.md)
*[Backing up your VMs](backing_up_your_vm.md)

## Advanced topics
More experienced users can
*[Automatically create VMs](automating_vm_creation.md),
*Describe your VM infrastructure as code using [Terraform](terraform.md).
## Use cases
More detailed instructions are available for some of the common cloud use cases, including
*[Configure a data or web server](configuring-a-data-or-web-server.md)
*[Using vGPUs (standard shared GPU allocation) in the cloud](using-cloud-vgpus.md)
*[Using PCI-e passthrough GPUs in the cloud](using-cloud-gpu.md)
*[Setting up GUI Desktop on a VM](setting-up-gui-desktop-on-a-vm.md)
*[Using IPv6 in Arbutus cloud](using-ipv6-in-cloud.md)

## Cloud systems
Your project will be on one of the following clouds:
* [Béluga](https://beluga.cloud.computecanada.ca)
* [Arbutus](https://arbutus.alliancecan.ca)
* [Legacy Arbutus](https://arbutus.cloud.computecanada.ca)
* [Nibi](https://nibi.cloud.alliancecan.ca)
* [Cedar](http://cedar.cloud.computecanada.ca)
The details of the underlying hardware and OpenStack versions are described on the [cloud resources](cloud-resources.md) page. The [System status](system-status.md) wiki page contains information about the current cloud status and future planned maintenance and upgrade activities.

## Support
For questions about our cloud service, contact [technical support](technical-support.md).