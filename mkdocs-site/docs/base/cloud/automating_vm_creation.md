---
title: "Automating VM creation"
slug: "automating_vm_creation"
lang: "base"

source_wiki_title: "Automating VM creation"
source_hash: "254f0875a809e2f5a693a87f63d65ada"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:33:58.722554+00:00"

tags:
  - cloud

keywords:
  - "OpenStack"
  - "cloud-init"
  - "CVMFS"
  - "DataSourceOpenStack"
  - "Terraform"
  - "Cloud VMs"
  - "VM"
  - "Cloud-init"
  - "Stack creation"
  - "Instance Name"
  - "Log tab"
  - "Heat templates"
  - "HOT files"

questions:
  - "What tools are available for automating the creation and provisioning of cloud VMs?"
  - "What is CVMFS, and how does it benefit users accessing research software on cloud systems?"
  - "How can a user specify a cloud-init file and monitor its execution progress when launching a new VM instance?"
  - "What are Heat templates used for in OpenStack, and how do they interact with cloud-init files?"
  - "What are the specific steps required to launch a new stack using a HOT file in the OpenStack dashboard?"
  - "How can a user visually monitor the progress of a stack's creation and view its final output details?"
  - "How can a user access the detailed information and logs for a specific Virtual Machine?"
  - "What keyword should be searched for within the Log tab to track the various phases of initialization?"
  - "What specific log entry indicates that the Cloud-init process has successfully completed?"
  - "What are Heat templates used for in OpenStack, and how do they interact with cloud-init files?"
  - "What are the specific steps required to launch a new stack using a HOT file in the OpenStack dashboard?"
  - "How can a user visually monitor the progress of a stack's creation and view its final output details?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Parent page: [Cloud](cloud.md)*

To automate the creation of cloud VMs, volumes, etc., the [OpenStack CLI](openstack_command_line_clients.md), [Heat](#using-heat-templates), [Terraform](terraform.md), or the OpenStack Python API can be used. Both the OpenStack CLI and Terraform are command line tools. While Heat is used through the OpenStack web dashboard, Horizon. To install and configure settings and software within the VM, [cloud-init](#using-cloud-init) is used.

In addition to these tools to create and provision your VMs, you can also gain access to the Digital Research Alliance of Canada (the Alliance) software stack (CVMFS) that is available on our general purpose computing clusters, within your VM. See the [Enabling CVMFS on your VM](#enabling-cvmfs-on-your-vm) section below.

## Enabling CVMFS on your VM
CVMFS is a HTTP-based file system that provides a scalable, reliable, and low maintenance research software distribution service. At the client end, users just need to mount CVMFS and then use the software or libraries directly without worrying about compiling, building, or patching. All the software are pre-compiled for common OS flavours and even modularized so that users can simply load a software as a module.
CVMFS has already been installed on Alliance cluster systems such as Cedar, Graham, and Beluga, while on cloud systems users need to enable it by hand, following these cloud instructions: [To enable CVMFS on CC Clouds](https://github.com/ComputeCanada/CVMFS/tree/main/cvmfs-cloud-scripts).

For more information please see the [Compute Canada CVMFS documentation](../software/cvmfs/accessing_cvmfs.md) and [CERN CVMFS documentation](https://cvmfs.readthedocs.io/en/stable/).

## Using cloud-init
Cloud-init files are used to initialize a particular VM and run within that VM. They can be thought of as a way to automate tasks you would perform at the command line while logged into your VM. They can be used to perform tasks such as updating the operating system, installing and configuring applications, creating files, running commands, and creating users and groups. Cloud-init can be used to set up other provisioning tools such as [Ansible](https://docs.ansible.com/) or [Puppet](https://puppet.com/) to continue with the software and VM configuration if desired.

Cloud-init configuration is specified using plain text in the [YAML](https://en.wikipedia.org/wiki/YAML) format. To see how to create cloud-init files see the official cloud-init [documentation](https://cloudinit.readthedocs.io/en/latest/). Cloud-init files can be used with the Horizon dashboard (OpenStack's web GUI), Terraform, the CLI, or the Python API. Here we describe how to use a cloud-init file with Horizon.

### Specifying a cloud-init File
1.  Start as normal when launching an instance, by clicking under *Project*->*Compute*->*Instances* and specifying your VM's configuration as described in [Launching a VM](cloud_quick_start.md#launching-a-vm).
2.  !!! note
    **Before** clicking *Launch*, select the *Post-Creation* tab and specify your *Customization Script Source*, in this case a Cloud-init YAML file, by either copying and pasting into a text box (*Direct Input* method) or uploading from a file from your desktop computer (*File* method). Older versions of OpenStack, in particular IceHouse, only provide a text box to copy and paste your Cloud-init file into.
3.  Once the usual selections for your VM, as described in [Launching a VM](cloud_quick_start.md#launching-a-vm), have been made and the Cloud-init YAML file is included, click *Launch* to create the VM. It may take some time for Cloud-init to complete depending on what has been specified in the Cloud-init YAML file.

### Checking Cloud-init Progress
To see the progress of Cloud-init on a VM, check the console log of the VM by:

1.  Selecting *Project*->*Compute*->*Instances* in the left hand menu.
2.  Click on the *Instance Name* of the VM. This will provide more information about the particular VM.
3.  Select the *Log* tab and look for lines containing 'cloud-init' for information about the various phases of Cloud-init.
4.  When Cloud-init has finished running the following line will appear near or at the end of the log:

```text
Cloud-init v. 0.7.5 finished at Wed, 22 Jun 2016 17:52:29 +0000. Datasource DataSourceOpenStack [net,ver=2]. Up 44.33 seconds
```

5.  !!! tip
    The log must be refreshed manually by clicking the *Go* button

## Using Heat Templates
Heat templates are even more powerful; they can be used to automate tasks performed in the OpenStack dashboard such as creating multiple VMs at once, configuring security groups, creating and configuring networks, and creating and attaching volumes to VMs. Heat templates can be used in conjunction with cloud-init files; once Heat has created the VM it can pass a cloud-init file to that VM to perform setup tasks and even include information about other resources dynamically in the cloud-init files (e.g., floating IPs of other VMs).

As with cloud-init the creation of [Heat](https://wiki.openstack.org/wiki/Heat) Orchestration Template (HOT) files is not covered here; instead, see the official [documentation](http://docs.openstack.org/developer/heat/template_guide/hot_guide.html). HOT files are also written in the [YAML](https://en.wikipedia.org/wiki/YAML) format. Heat allows automation of operations performed in the OpenStack dashboard (Horizon) as well as the ability to pass information into the embedded Cloud-init files, such as an IP of another server.

!!! warning
    Before using a Heat template there is usually no need to create any resources in advance. In fact it is often good practice to remove any resources you are not currently using beforehand, as using a Heat template consumes resources towards your quota and will fail if it tries to exceed your quota.

To create a stack using a HOT file:

1.  Select *Project*->*Orchestration*->*Stacks* and click the *Launch Stack* button to start creating a new stack.
2.  Provide a HOT file by entering the URL, the File name, or by Direct Input. Here, we will use a HOT file from one of the links in section *Available Setups* below.
3.  In the *Template Source* box, select *URL* from the drop-down list.
4.  Paste the selected URL into the *Template URL* box.
5.  Click *Next* to begin setting stack parameters; these vary depending on the template, however all stacks have the following parameters by default:
    *   **Stack Name**; choose a name which is meaningful.
    *   **Creation Timeout**; indicates how long after stack creation before OpenStack will give up trying to create the stack if it hasn't finished; the default value is usually sufficient.
    *   **Password for user**; sets the password required for later stack changes. This is seldom used as many of the stacks mentioned in the next section are not designed to be updated.
6.  Click *Launch* to begin creating your stack.

To graphically see the progress of your stack creation click on the *Stack Name* and select the *Topology* tab. Grey nodes indicate that creation is in progress, green nodes have finished being created, and red nodes indicate failures. Once the stack has completed successfully click the *Overview* tab to see any information that the stack may provide (e.g., a URL to access a service or website).