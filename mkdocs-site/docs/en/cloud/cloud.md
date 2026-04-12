---
title: "Cloud/en"
slug: "cloud"
lang: "en"

source_wiki_title: "Cloud/en"
source_hash: "719a2aec1ec00339377b842dce7d9fd2"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:17:31.294400+00:00"

tags:
  - cloud

keywords:
  - "OpenStack"
  - "virtual machine"
  - "Cloud resources"
  - "High Performance Computing"
  - "Security"
  - "Cloud computing"
  - "Cloud project"
  - "cloud infrastructure"
  - "Cloud systems"
  - "Virtual machines"
  - "troubleshooting"
  - "user responsibilities"
  - "Infrastructure as a Service"
  - "storage options"

questions:
  - "What are the main advantages and disadvantages of using a virtual machine in the cloud compared to an HPC environment?"
  - "What steps and justifications are required to request access to a new or existing cloud project?"
  - "What are the user's responsibilities and available resources for creating, securing, and troubleshooting a virtual machine?"
  - "What are the fundamental steps and best practices for creating, securing, and backing up virtual machines?"
  - "What advanced tools and specific use cases, such as GPU allocation or automation, are available for experienced users?"
  - "Which specific cloud systems are available for hosting projects, and how can users access system status updates or technical support?"
  - "How can a user manually create their first virtual machine on the cloud infrastructure?"
  - "What resources are available for understanding cloud terminology, selecting storage options, and troubleshooting common issues?"
  - "What are the specific responsibilities a user has when managing a cloud project?"
  - "What are the fundamental steps and best practices for creating, securing, and backing up virtual machines?"
  - "What advanced tools and specific use cases, such as GPU allocation or automation, are available for experienced users?"
  - "Which specific cloud systems are available for hosting projects, and how can users access system status updates or technical support?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

We offer [Infrastructure as a Service](https://en.wikipedia.org/wiki/Cloud_computing#Infrastructure_as_a_service_.28IaaS.29) that supports [virtualization](https://en.wikipedia.org/wiki/Hardware_virtualization).

A user of the cloud will typically create or *spin up* one or more virtual machines (VMs or *instances*). He or she then logs into the VM with administrative privileges, installs any desired software, and runs the software applications needed. These applications could be as diverse as a CPU-intensive analysis of particle physics data, or a web service directed towards scholars of literature and the humanities. The advantage is that the user has complete control over the collection of installed software (the *software stack*). The disadvantage is that the user must have some degree of experience in installing software and otherwise managing a computer.

Virtual machines can be easily replicated. One can take a *snapshot* of a VM which can then be started again elsewhere. This makes it easy to replicate or scale up a service, and to recover from (for example) a power interruption.

If you can fit your work easily into the [HPC](https://en.wikipedia.org/wiki/Supercomputer) [batch](https://en.wikipedia.org/wiki/Batch_processing) submission workflow and environment (see [What is a scheduler?](../running-jobs/what_is_a_scheduler.md)) it is preferable to work outside the cloud, as there are more [resources available](../clusters/national_systems.md) for HPC and software is already configured and installed for many common needs. There are also tools like [Apptainer](../software/containers/apptainer.md) to run custom software stacks inside containers within our HPC clusters.
If your need isn't served by Apptainer or HPC batch, then the cloud is your solution.

## Getting a cloud project
* Review and understand the [important role](cloud_shared_security_responsibility_model.md) you are about to take on to [safeguard your research](https://science.gc.ca/site/science/en/safeguarding-your-research) and the shared cloud infrastructure.
* If you do not have an account with us, create one with [these instructions](https://docs.alliancecan.ca/wiki/Apply_for_a_CCDB_account).
* A [project](managing_your_cloud_resources_with_openstack.md#projects) is an allocation of resources for creating VMs within a cloud.
* If you are a primary investigator (PI) with an active cloud resource allocation (see [RAC](https://alliancecan.ca/en/services/advanced-research-computing/research-portal/accessing-resources/resource-allocation-competitions)) you should already have a project. See the sections below on using the cloud to get started. If not or if you are not sure please contact [technical support](../support/technical_support.md).
* Otherwise go to the [Alliance cloud project and RAS request form](https://docs.google.com/forms/d/e/1FAIpQLSeU_BoRk5cEz3AvVLf3e9yZJq-OvcFCQ-mg7p4AWXmUkd5rTw/viewform) to
  * request access to an existing project (see the section below for information you will need to supply)
  * and if you are a PI you may also
    * request a new project with our Rapid Access Service ([RAS](cloud_ras_allocations.md)),
    * or request an increase in quota of an existing project.

* Requests are typically processed within two business days.

### Preparing your request
* When requesting access to an existing project, you will need to know the project name and which cloud it is on. See the section on [projects](managing_your_cloud_resources_with_openstack.md#projects) for guidance on how to find the project name and the section about [cloud systems](cloud.md#cloud-systems) for a list of our clouds. Requests for access must be confirmed by the PI owning the project.
* When requesting either a new project or an increase in quota for an existing project, some justification, in the form of a few sentences, is required:
  * why you need cloud resources,
  * why an HPC cluster is not suitable,
  * your plans for efficient usage of your resources,
  * your plans for maintenance and security ([refer to this page](security_considerations_when_running_a_vm.md)).
* A PI may own up to 3 projects, but the sum of all project quotas must be within the [RAS](cloud_ras_allocations.md) allocation limits. A PI may have both compute and persistent cloud RAS allocations.

## Creating a virtual machine on the cloud infrastructure
* The [cloud quick start guide](cloud_quick_start.md) describes how to manually create your first VM.
* Review the [glossary](cloud_technical_glossary.md) to learn definitions of common topics.
* Consider [storage options](cloud_storage_options.md) best suited to your use case.
* See the [troubleshooting guide](cloud_troubleshooting_guide.md) for steps to deal with common issues in cloud computing.

## User responsibilities
For each cloud project, you are responsible for
* [Creating and managing your virtual machines](managing_your_cloud_resources_with_openstack.md)
* [Securing and patching software on your VM](cloud_shared_security_responsibility_model.md)
* [Defining security groups to allow access to your network](managing_your_cloud_resources_with_openstack.md#security-groups)
* [Creating user accounts](managing_your_linux_vm.md)
* [Following best practices](vm_best_practices.md)
* [Considering security issues](security_considerations_when_running_a_vm.md)
* [Backing up your VMs](backing_up_your_vm.md)

## Advanced topics
More experienced users can
* [Automatically create VMs](automating_vm_creation.md),
* Describe your VM infrastructure as code using [Terraform](terraform.md).

## Use cases
More detailed instructions are available for some of the common cloud use cases, including
* [Configure a data or web server](configuring_a_data_or_web_server.md)
* [Using vGPUs (standard shared GPU allocation) in the cloud](using_cloud_vgpus.md)
* [Using PCI-e passthrough GPUs in the cloud](cloud.md)
* [Setting up GUI Desktop on a VM](setting_up_gui_desktop_on_a_vm.md)
* [Using IPv6 in Arbutus cloud](using_ipv6_in_cloud.md)

## Cloud systems
Your project will be on one of the following clouds:
* [Béluga](https://beluga.cloud.computecanada.ca)
* [Arbutus](https://arbutus.alliancecan.ca)
* [Legacy Arbutus](https://arbutus.cloud.computecanada.ca)
* [Nibi](https://nibi.cloud.alliancecan.ca)
* [Cedar](http://cedar.cloud.computecanada.ca)
The details of the underlying hardware and OpenStack versions are described on the [cloud resources](cloud_resources.md) page. The [System status](../support/system_status.md) wiki page contains information about the current cloud status and future planned maintenance and upgrade activities.

## Support
For questions about our cloud service, contact [technical support](../support/technical_support.md).