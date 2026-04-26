---
title: "Managing your cloud resources with OpenStack"
slug: "managing_your_cloud_resources_with_openstack"
lang: "base"

source_wiki_title: "Managing your cloud resources with OpenStack"
source_hash: "5a7e3be2438b23266310e4c5bcce1d4a"
last_synced: "2026-04-25T23:42:08.699101+00:00"
last_processed: "2026-04-26T00:18:49.108029+00:00"

tags:
  - cloud

keywords:
  - "SSH keys"
  - "OpenStack"
  - "Virtual machine"
  - "Virtual machines"
  - "security groups"
  - "network traffic"
  - "default security group"
  - "Projects"
  - "CIDR rules"
  - "VM creation"
  - "Manage Rules"
  - "Security groups"
  - "Dashboard"
  - "Default security group"
  - "cloudInit"
  - "virtual machines"
  - "YAML format"
  - "user configuration"
  - "add users"
  - "instance customization"

questions:
  - "What is OpenStack and what primary functions does it serve in a cloud computing environment?"
  - "How do OpenStack projects manage resource quotas, user permissions, and ownership?"
  - "What is the purpose of security groups and how can users configure them to control network traffic for their virtual machines?"
  - "What is the purpose of the default security group and what specific ingress and egress rules does it contain?"
  - "How can administrators effectively manage security groups and use CIDR rules to restrict access to their virtual machines?"
  - "What is cloudInit, and how can it be utilized to customize an instance during its initial launch?"
  - "What is the primary purpose of using security groups for your virtual machines?"
  - "Where in the interface do you navigate to view and manage your currently defined security groups?"
  - "What are the specific steps required to add or remove rules within a particular security group?"
  - "When can you customize your instance using cloudInit?"
  - "What are the two methods available for applying a cloudInit script to an OpenStack instance?"
  - "What specific administrative task can be accomplished using cloudInit during VM creation?"
  - "How can a cloudInit script be configured to add new users with specific permissions and SSH keys during the creation of a VM?"
  - "What specific configuration must be added to the YAML script to preserve the default distribution user instead of overwriting it?"
  - "How can you verify in the instance logs that the public SSH keys for the new users were successfully added after the VM has spawned?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Parent page: [Cloud](cloud.md)*

OpenStack is the software suite used on our clouds to control hardware resources such as computers, storage and networking. It allows the creation and management of virtual machines ("VMs" or "instances"), which act like separate individual machines, by emulation in software. This allows complete control over the computing environment, from choosing an operating system to software installation and configuration. Diverse use cases are supported, from hosting websites to creating virtual clusters. More documentation on OpenStack can be found at the [OpenStack website](http://docs.openstack.org/).

This page describes how to perform common tasks encountered while working with OpenStack. It is assumed that you have already read [Cloud Quick Start](cloud_quick_start.md) and understand the basic operations of launching and connecting to a VM. Most tasks can be performed using either the dashboard (as described below), the [OpenStack command line clients](openstack_command_line_clients.md), or a tool called [Terraform](terraform.md); however, some tasks require using command line tools, for example [sharing an image with another project](working_with_images.md#sharing-an-image-with-another-project).

# Working with the dashboard
The web browser user interface used to manage your cloud resources, as described in most of our documentation, is referred to as the "dashboard". The dashboard is developed under an OpenStack sub-project referred to as Horizon. Horizon and dashboard might be used interchangeably. The dashboard is well documented [here](https://docs.openstack.org/horizon/latest/). This documentation lists all of the options available on the dashboard, what they do, and how to navigate the system.

# Projects
OpenStack projects group VMs together and provide a quota out of which VMs and related resources can be created. A project is unique to a particular cloud. All accounts which are members of a project have the same level of permissions, meaning anyone can create or delete a VM within a project if they are a member. You can view the projects you are a member of by logging into an OpenStack dashboard for the clouds you have access to (see [Cloud systems](cloud.md#cloud-systems) for a list of cloud URLs). The active **project name** will be displayed in the top left of the dashboard, to the right of the cloud logo. If you are a member of more than one project, you can switch between active projects by clicking on the drop-down menu and selecting the project's name.

Depending on your allocation, your project may be limited to certain types of VM [flavors](virtual_machine_flavors.md). For example, compute allocations will generally only allow "c" flavours, while persistent allocations will generally only allow "p" flavours.

Projects can be thought of as owned by primary investigators (PIs) and new projects and quota adjustments can only be requested by PIs. In addition, request for access to an existing project must be confirmed by the PI owning the project.

# Working with volumes
Please see [this page](working_with_volumes.md) for more information about creating and managing storage volumes.

# Working with images
Please see [this page](working_with_images.md) for more information about creating and managing disk image files.

# Working with VMs
Please see [this page](working_with_vms.md) for more information about managing certain characteristics of your VMs in the dashboard.

# Availability zones
Availability zones allow you to indicate what group of physical hardware you would like your VM to run on. On Beluga and Graham clouds, there is only one availability zone, *nova*, so there isn't any choice in the matter. However, on Arbutus there are three availability zones: *Compute*, *Nova*, and *Persistent*. The *Compute* and *Persistent* zones only run compute or persistent flavours respectively (see [Virtual machine flavours](virtual_machine_flavors.md)). Using two persistent zones can present an advantage; for example, two instances of a website can run in two different zones to ensure its continuous availability in the case where one of the sites goes down.

# Security groups
A security group is a set of rules to control network traffic into and out of your virtual machines. To manage security groups, go to *Project->Network->Security Groups*. You will see a list of currently defined security groups. If you have not previously defined any security groups, there will be a single default security group.

To add or remove rules from a security group, click *Manage Rules* beside that group. When the group description is displayed, you can add or remove rules by clicking the *+Add Rule* and *Delete Rule* buttons.

## Default security group
The **default security group** contains rules which allow a VM access out to the internet, for example to download operating system upgrades or package installations, but does not allow another machine to access it, except for other VMs belonging to the same default security group.

!!! warning
    We recommend you do not remove rules from the default security group as this may cause problems when creating new VMs.

The default security group rules typically include:
*   2 Egress rules to allow your instance to access an outside network without any limitation; there is one rule for IPV4 and one for IPV6.
*   2 Ingress rules to allow communication for all the VMs that belong to that security group, for both IPV4 and IPV6.

It is safe to add rules to the default security group and you may recall that we did this in [Cloud Quick Start](cloud_quick_start.md) by either adding security rules for [SSH](cloud_quick_start.md#network-settings) or [RDP (see *Firewall, add rules to allow RDP* under the Windows tab)](cloud_quick_start.md) to your default security group so that you could connect to your VM.

## Managing security groups
You can define multiple security groups and a VM can belong to more than one security group. When deciding on how to manage your security groups and rules, think carefully about what needs to be accessed and who needs to access it. Strive to minimize the IP addresses and ports in your Ingress rules. For example, if you will always be connecting to your VM via SSH from the same computer with a static IP, it makes sense to allow SSH access only from that IP. To specify the allowed IP or IP range, use the CIDR box (use this web-based tool for converting [IP ranges to CIDR](http://www.ipaddressguide.com/cidr) rules). Further, if you only need to connect to one VM via SSH from the outside and then can use that as a gateway to any other cloud VMs, it makes sense to put the SSH rule in a separate security group and add that group only to the gateway VM. However, you will also need to ensure your SSH keys are configured correctly to allow you to use SSH between VMs (see [SSH Keys](../getting-started/ssh_keys.md)). In addition to CIDR, security rules can be limited within a project using security groups. For example, you can configure a security rule for a VM in your project running a MySQL Database to be accessible from other VMs in the default security group.

The security groups a VM belongs to can be chosen when it is created on the *Launch Instance* with the *Security Groups* option, or after the VM has been launched by selecting *Edit Security Groups* from the drop-down menu of actions for the VM on the *Project->Compute->Instances* page.

## Using CIDR rules
CIDR stands for Classless Inter-Domain Routing and is a standardized way of defining IP ranges (see also this Wikipedia page on [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)).

An example of a CIDR rule is `192.168.1.1/24`. This looks just like a normal IP address with a `/24` appended to it. IP addresses are made up of 4, 1-byte (8 bits) numbers ranging from 0 to 255. What this `/24` means is that this CIDR rule will match the first left most 24 bits (3 bytes) of an IP address. In this case, any IP address starting with `192.168.1` will match this CIDR rule. If `/32` is appended, the full 32 bits of the IP address must match exactly; if `/0` is appended, no bits must match and therefore any IP address will match it.

# Working with cloudInit

**The first time your instance is launched**, you can customize it using cloudInit. This can be done either
*   via the OpenStack command-line interface, or
*   by pasting your cloudInit script in the *Customization Script* field of the OpenStack dashboard (*Project-->Compute-->Instances-->Launch instance* button, *Configuration* option).

## Add users with cloudInit during VM creation
The following cloudInit script adds two users `gretzky` and `lemieux` with and without sudo permissions respectively.

```yaml
#cloud-config
users:
  - name: gretzky
    shell: /bin/bash
    sudo: ALL=(ALL) NOPASSWD:ALL
    ssh_authorized_keys:
      - <Gretzky's public key goes here>
  - name: lemieux
    shell: /bin/bash
    ssh_authorized_keys:
      - <Lemieux's public key goes here>
```

For more about the YAML format used by cloudInit, see [YAML Preview](http://www.yaml.org/spec/1.2/spec.html#Preview).

!!! tip
    YAML is very picky about white space formatting, so there must be a space after the "-" before your public key string.

Also, this configuration overwrites the default user that is added when no cloudInit script is specified, so the users listed in this configuration script will be the *only* users on the newly created VM. It is therefore vital to have at least one user with sudo permission. More users can be added by simply including more `- name: username` sections.

If you wish to preserve the default user created by the distribution (users `debian`, `centos`, `ubuntu`, *etc.*), use the following form:

```yaml
#cloud-config
users:
  - default
  - name: gretzky
    shell: /bin/bash
    sudo: ALL=(ALL) NOPASSWD:ALL
    ssh_authorized_keys:
      - <Gretzky's public key goes here>
  - name: lemieux
    shell: /bin/bash
    ssh_authorized_keys:
      - <Lemieux's public key goes here>
```

After the VM has finished spawning, look at the log to ensure that the public keys have been added correctly for those users. The log can be found by clicking on the name of the instance on the "Compute->Instances" panel and then selecting the "log" tab. The log should show something like this:

```
ci-info: ++++++++Authorized keys from /home/gretzky/.ssh/authorized_keys for user gretzky++++++++
ci-info: +---------+-------------------------------------------------+---------+------------------+
ci-info: | Keytype |                Fingerprint (md5)                | Options |     Comment      |
ci-info: +---------+-------------------------------------------------+---------+------------------+
ci-info: | ssh-rsa | ad:a6:35:fc:2a:17:c9:02:cd:59:38:c9:18:dd:15:19 |    -    | rsa-key-20160229 |
ci-info: +---------+-------------------------------------------------+---------+------------------+
ci-info: ++++++++++++Authorized keys from /home/lemieux/.ssh/authorized_keys for user lemieux++++++++++++
ci-info: +---------+-------------------------------------------------+---------+------------------+
ci-info: | Keytype |                Fingerprint (md5)                | Options |     Comment      |
ci-info: +---------+-------------------------------------------------+---------+------------------+
ci-info: | ssh-rsa | ad:a6:35:fc:2a:17:c9:02:cd:59:38:c9:18:dd:15:19 |    -    | rsa-key-20160229 |
ci-info: +---------+-------------------------------------------------+---------+------------------+
```

Once this is done, users can log into the VM with their private keys as usual (see [SSH Keys](../getting-started/ssh_keys.md)).