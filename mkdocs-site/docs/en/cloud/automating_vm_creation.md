---
title: "Automating VM creation/en"
slug: "automating_vm_creation"
lang: "en"

source_wiki_title: "Automating VM creation/en"
source_hash: "1bb3f278d8cf5122a7f06d16a1cbc856"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T04:43:11.108394+00:00"

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

_Parent page: [Cloud](cloud.md)_

To automate the creation of cloud VMs, volumes, etc., the [OpenStack CLI](openstack-command-line-clients.md), [Heat](#using-heat-templates), [Terraform](https://www.terraform.io/), or the OpenStack python API can be used. Both the OpenStack CLI and Terraform are command-line tools. Heat is used through the OpenStack web dashboard, Horizon. To install and configure settings and software within the VM, [cloud-init](#using-cloud-init) is used.

In addition to these tools to create and provision your VMs, you can also gain access to the Digital Research Alliance of Canada (the Alliance) software stack (CVMFS) that is available on our general purpose computing clusters, within your VM. See the [Enabling CVMFS](#enabling-cvmfs-on-your-vm) section below.

## Enabling CVMFS on your VM
CVMFS is an HTTP-based file system that provides a scalable, reliable, and low-maintenance research software distribution service. At the client end, users just need to mount CVMFS and then use the software or libraries directly without worrying about compiling, building, or patching. All the software are pre-compiled for common OS flavours and even modularized so that users can simply load software as a module.

CVMFS has already been installed on Alliance cluster systems such as Cedar, Graham, and Beluga. On cloud systems, users need to enable it by hand, following these cloud instructions: [To enable CVMFS on Alliance Clouds](https://github.com/ComputeCanada/CVMFS/tree/main/cvmfs-cloud-scripts).

For more information please see the [Alliance CVMFS documentation](accessing-cvmfs.md) and [CERN CVMFS documentation](https://cvmfs.readthedocs.io/en/stable/).

## Using cloud-init
Cloud-init files are used to initialize a particular VM and run within that VM. They can be thought of as a way to automate tasks you would perform at the command line while logged into your VM. They can be used to perform tasks such as updating the operating system, installing and configuring applications, creating files, running commands, and creating users and groups. Cloud-init can be used to set up other provisioning tools such as [Ansible](https://docs.ansible.com/) or [Puppet](https://puppet.com/) to continue with the software and VM configuration if desired.

Cloud-init configuration is specified using plain text in the [YAML](https://en.wikipedia.org/wiki/YAML) format. To see how to create cloud-init files, see the official cloud-init [documentation](https://cloudinit.readthedocs.io/en/latest/). Cloud-init files can be used with the Horizon dashboard (OpenStack's web GUI), Terraform, the CLI, or the Python API. Here we describe how to use a cloud-init file with Horizon.

### Specifying a cloud-init File
1.  Start as normal when launching an instance, by clicking under _Project_ -> _Compute_ -> _Instances_ and specifying your VM's configuration as described in [Launching a VM](cloud-quick-start.md#launching-a-vm).
2.  !!! tip
    **Before** clicking _Launch_, select the _Post-Creation_ tab and specify your _Customization Script Source_, in this case a Cloud-init YAML file, by either copying and pasting into a text box (_Direct Input_ method) or uploading from a file from your desktop computer (_File_ method). Older versions of OpenStack, in particular IceHouse, only provide a text box to copy and paste your CloudInit file into.
3.  Once the usual selections for your VM, as described in [Launching a VM](cloud-quick-start.md#launching-a-vm), have been made and the Cloud-init YAML file is included, click _Launch_ to create the VM. It may take some time for Cloud-init to complete depending on what has been specified in the Cloud-init YAML file.

### Checking Cloud-init Progress
To see the progress of Cloud-init on a VM, check the console log of the VM by:

1.  Selecting _Project_ -> _Compute_ -> _Instances_ in the left-hand menu.
2.  Click on the _Instance Name_ of the VM. This will provide more information about the particular VM.
3.  Select the _Log_ tab and look for lines containing 'cloud-init' for information about the various phases of Cloud-init.
4.  When Cloud-init has finished running, the following line will appear near or at the end of the log:

    ```
    Cloud-init v. 0.7.5 finished at Wed, 22 Jun 2016 17:52:29 +0000. Datasource DataSourceOpenStack [net,ver=2]. Up 44.33 seconds
    ```

    !!! note
    The log must be refreshed manually by clicking the _Go_ button.

## Using Heat Templates
Heat templates are even more powerful; they can be used to automate tasks performed in the OpenStack dashboard such as creating multiple VMs at once, configuring security groups, creating and configuring networks, and creating and attaching volumes to VMs. Heat templates can be used in conjunction with cloud-init files. Once Heat has created the VM, it can pass a cloud-init file to that VM to perform setup tasks and even include information about other resources dynamically in the cloud-init files (e.g., floating IPs of other VMs).

As with cloud-init, the creation of [Heat](https://wiki.openstack.org/wiki/Heat) Orchestration Template (HOT) files is not covered here; instead, see the official [documentation](http://docs.openstack.org/developer/heat/template_guide/hot_guide.html). HOT files are also written in the [YAML](https://en.wikipedia.org/wiki/YAML) format. Heat allows automation of operations performed in the OpenStack dashboard (Horizon) as well as the ability to pass information into the embedded Cloud-init files, such as an IP of another server. Before using a Heat template, there is usually no need to create any resources in advance.

!!! warning
    It is often good practice to remove any resources you are not currently using beforehand, as using a Heat template consumes resources towards your quota and will fail if it tries to exceed your quota.

To create a stack using a HOT file:

1.  Select _Project_ -> _Orchestration_ -> _Stacks_ and click the _Launch Stack_ button to start creating a new stack.
2.  Provide a HOT file by entering the URL, the File name, or by Direct Input. Here, we will use a HOT file from one of the links in section _Available Setups_ below.
3.  In the _Template Source_ box, select _URL_ from the drop-down list.
4.  Paste the selected URL into the _Template URL_ box.
5.  Click _Next_ to begin setting stack parameters; these vary depending on the template. However, all stacks have the following parameters by default:
    *   _Stack Name_; choose a name which is meaningful.
    *   _Creation Timeout_; indicates how long after stack creation OpenStack will wait before giving up if it hasn't finished; the default value is usually sufficient.
    *   _Password for user_; sets the password required for later stack changes. This is seldom used as many of the stacks mentioned in the next section are not designed to be updated.
6.  Click _Launch_ to begin creating your stack.

To graphically see the progress of your stack creation, click on the _Stack Name_ and select the _Topology_ tab. Grey nodes indicate that creation is in progress, green nodes have finished being created, and red nodes indicate failures. Once the stack has completed successfully, click the _Overview_ tab to see any information that the stack may provide (e.g., a URL to access a service or website).