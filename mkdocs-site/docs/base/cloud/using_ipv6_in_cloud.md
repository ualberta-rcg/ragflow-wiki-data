---
title: "Using ipv6 in cloud"
slug: "using_ipv6_in_cloud"
lang: "base"

source_wiki_title: "Using ipv6 in cloud"
source_hash: "92235ab50e884a861394339a0dff7a06"
last_synced: "2026-10-11T01:39:35.690021+00:00"
last_processed: "2026-10-11T02:40:19.420753+00:00"

tags:
  - cloud

keywords:
  - "SLAAC address configuration"
  - "ifcfg-eth1"
  - "sysctl.conf"
  - "IPv6-GUA"
  - "Permission Denied"
  - "launch instance"
  - "initial user account"
  - "SSH key pair"
  - "OpenStack network"
  - "IPv6 enabled"
  - "IPv6‑GUA"
  - "Customization Script"
  - "IPv6 connection issues"
  - "MTU 1452"
  - "OpenStack security groups"

questions:
  - "What temporary MTU value should be set on each end’s IPv6 interface to mitigate migration‑related connection problems, and when should the default MTU be restored?"
  - "How are IPv6‑GUA network interfaces attached to a VM via the OpenStack CLI and the Horizon dashboard, and what happens to the GUA address when the interface is detached versus when the VM is rebuilt or restarted?"
  - "Why do Debian or Ubuntu 26.04 instances launched with an IPv6‑GUA network fail to install the selected SSH key pair, and what steps can be taken to create an initial user account to work around the “Permission Denied” error?"
  - "How do you add a user with sudo privileges and an SSH authorized key using the customization script in the Cloud Quick Start guide?"
  - "What are the required steps to enable, configure, and verify IPv6 on the new eth1 interface in the Linux virtual machine?"
  - "Which configuration files and kernel parameters must be modified to ensure IPv6 functionality on the system?"
  - "Why does the selected SSH key pair fail to install when the instance is launched on an IPv6‑GUA network?"
  - "What specific “Permission Denied” error message do researchers see when they try to SSH into the instance?"
  - "What are the exact steps researchers should follow to create an initial user account as a workaround when launching a new instance?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! warning "Attention"
    Some users have reported IPv6 connection issues when migrating contents between old and new Arbutus. A temporary MTU of 1452 on each end's IPv6 network interface may address the problem. Once migration has been completed, the default MTU can be restored.

## IPv6 in Arbutus Cloud
IPv6 Link-Local (LLA) and Global Unicast Addresses (GUA) are generally available within the Arbutus cloud environment.
GUA can be set up via a separate interface, which in turn also handles only the IPv6 traffic.
Addresses are being set up using *Stateless Address Auto Configuration* (SLAAC), which automatically sets up the IP on the VM interface. By default, the security group rules will allow all outbound traffic from the VM via the IPv6 GUA, but no traffic that originates from outside the VM will be allowed until specific security group rules have been defined. This is the same behaviour as IPv4.

### Example of an OpenStack CLI Configuration

Get the ID of the VM to attach the network interface.
````bash
openstack server list
+--------------------------------------+-----------------+---------+-----------------------------------------------+----------------------------------+----------+
| ID                                   | Name            | Status  | Networks                                      | Image                            | Flavor   |
+--------------------------------------+-----------------+---------+-----------------------------------------------+----------------------------------+----------+
| 74be352d-19ca-46cc-9661-7088d2652e34 | test            | ACTIVE  | def-bott-network=192.168.27.140, 206.12.93.29 | Debian-10.9.2-Buster-x64-2021-05 | p1-1.5gb |
+--------------------------------------+-----------------+---------+-----------------------------------------------+----------------------------------+----------+
````

Assign a new network interface to the VM, using IPv6 as network.

````bash
openstack server add network 74be352d-19ca-46cc-9661-7088d2652e34  IPv6-GUA
````

Check the status of the assignment.

````bash
openstack server list
+--------------------------------------+-----------------+---------+------------------------------------------------------------------------------------------------+----------------------------------+----------+
| ID                                   | Name            | Status  | Networks                                                                                       | Image                            | Flavor   |
+--------------------------------------+-----------------+---------+------------------------------------------------------------------------------------------------+----------------------------------+----------+
| 74be352d-19ca-46cc-9661-7088d2652e34 | test            | ACTIVE  | IPv6-GUA=2607:f8f0:c11:7004:f816:3eff:fef1:8cee; def-bott-network=192.168.27.140, 206.12.93.29 | Debian-10.9.2-Buster-x64-2021-05 | p1-1.5gb |
+--------------------------------------+-----------------+---------+------------------------------------------------------------------------------------------------+----------------------------------+----------+
````

### Example of a Web Interface Configuration
Log into the dashboard and go to the *Instances* menu, then click on *Attach Interface* to open a dialog.
From the network menu, select IPv6-GUA (2607:f8f0:c11:7004::/64) and click on *Attach*.

The IPv6 address is now available and can be used until the interface is detached. Every time the interface is detached,
the GUA is released and put back into the pool and thus, can be used by anyone else. Rebuilding or restarting the VM, however, will not
release the GUA.

Access from any IPv6 GUA can be granted via *Security Groups* in OpenStack; the only difference is the CIDR which automatically detects the address type.

### Example of a Debian or Ubuntu 26.04 Instance
When researchers launch an instance with the Debian or Ubuntu 26.04 operating system with the IPv6 network (i.e., IPv6-GUA), the selected SSH key pair will not install successfully. As a result, the researchers cannot SSH into the instance and will receive a *Permission Denied* error message instead. To work around this problem, when launching a new instance, researchers can create an initial user account by completing the following steps:

1. To create a virtual machine, select *Compute->Instances* on the left menu, then click on the *Launch Instance* button.
2. Follow the [Cloud Quick Start Guide](cloud_quick_start.md) to complete the displayed form where you define your virtual machine.
3. Select *Configuration* in the left menu.
4. Add the following script to the *Customization Script*. Replace `[username]` with the researcher's preferred username and `[public key]` with the user's public key.
5. Select *Configuration Drive*.

````yaml
users:
  - name: [username]
    gecos: [username]
    groups: sudo
    sudo: ALL=(ALL) NOPASSWD:ALL
    shell: /bin/bash
    lock_passwd: true
    ssh_authorized_keys:
      - [public key]

ssh_pwauth: false
````

## Example of a Linux Configuration

The OpenStack network you configured above will appear in Linux as an additional eth-type interface. In most cases, `/dev/eth0` will be your existing interface. Your new IPv6-enabled interface will typically be `/dev/eth1`. The easiest way to pick up your new device is to reboot. But first, check to confirm that IPv6 is enabled with this command:
````bash
sudo sysctl -a | grep ipv6.*disable
````
The output should all end in zeros. IPv6 enabled is the default in all recent images. Any kernel parameters that need to be changed to zero should be added to `/etc/sysctl.conf`.

Also, add the following kernel parameters in `/etc/sysctl.conf`.
````bash
net.ipv6.conf.eth1.forwarding=0
net.ipv6.conf.eth1.accept_ra=1
````

Reboot your system and confirm IPv6 is enabled and that `/dev/eth1` exists.

Next, add the following configurations to `/etc/sysconfig/network-scripts/ifcfg-eth1`.
````bash
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_FAILURE_FATAL=no
````

Reboot your system again. The `/dev/eth1` interface should be configured and ready to be used.

You may then confirm the IPv6 configuration with:
````bash
ip -6 address
````

Finally, confirm that IPv6 is working with:
````bash
ping6 -c 1 www.google.com
````

That's all. Congratulations. Your system is now configured to use IPv6.

## Further Reading
* From Red Hat, [What you need to know about IPv6](https://www.redhat.com/sysadmin/what-you-need-know-about-ipv6)
* From Red Hat, [Configuring an IPv6 address in Red Hat Enterprise Linux 7 and 8](https://www.redhat.com/sysadmin/configuring-ipv6-rhel-7-8)
* From OpenStack, [IPv6](https://docs.openstack.org/neutron/pike/admin/config-ipv6.html)